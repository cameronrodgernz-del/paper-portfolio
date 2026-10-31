"""Rulebook 9c: the history test for ASX cash deal spreads, from the deal database.

The events and their outcomes come from deals/all_deals.csv (resolved ASX cash schemes and takeover
bids announced 2015 to 2025); prices come from EODHD (data/history/prices/ASX, fetched for
config/universe_history_au_deals.csv). Runs once, when every ticker in that list has been fetched
(or found missing), and writes reports/deal_au_history.md and a lock file.

The rules are in RULEBOOK.md section 9c and were registered before any result.
Usage: python3 -I src/history/au_deal_test.py <repo_root> [--force]
       python3 -I src/history/au_deal_test.py <repo_root> --sample     (writes the ticker list)
"""
import csv
import math
import os
import statistics as stats
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from deal_odds import holder_outcome, num  # noqa: E402
from insider_test import load_prices  # noqa: E402
from norgate_link import verified as norgate_verified  # noqa: E402
from rates import Rates  # noqa: E402
from spreads import spread_estimate  # noqa: E402

STAKE_AUD = 3000.0
FEE = min(0.019 * STAKE_AUD, 15.0) / STAKE_AUD        # Sharesies ASX brokerage on a A$3,000 order
FX_ROUND_TRIP = 0.005
HEDGE = 0.001
ENTRY_BAND = (0.85, 1.01)
NZD_PER_AUD = 1.08
COVERAGE = 0.70


def events(root: str) -> list[dict]:
    rows = list(csv.DictReader(open(os.path.join(root, "deals", "all_deals.csv"), encoding="utf-8", newline="")))
    by_id = {r["deal_id"]: r for r in rows}
    out = []
    for r in rows:
        if r["market"] != "ASX" or r.get("majority_buyout") == "Y" or r["structure"] not in ("scheme", "full_takeover"):
            continue
        if r.get("consideration_type") != "cash" or not ("2015" <= (r["announce_date"] or "")[:4] <= "2025"):
            continue
        offer = num(r.get("offer_price_initial"))
        y = holder_outcome(r, by_id)
        if not r.get("target_ticker") or offer is None or y is None:
            continue
        paid = num(r.get("offer_price_final")) or offer
        if r["outcome"] == "superseded_by_rival" and y == 1:
            best = [num(by_id[x.strip()].get("offer_price_final")) for x in (r.get("related_deal_ids") or "").split(";")
                    if x.strip() in by_id and by_id[x.strip()]["outcome"] == "completed"]
            best = [b for b in best if b]
            paid = max([paid] + best)
        pay_date = r.get("implementation_date") or r.get("outcome_date")
        if r["outcome"] == "superseded_by_rival" and y == 1:
            rd = [by_id[x.strip()].get("implementation_date") or by_id[x.strip()].get("outcome_date") for x in (r.get("related_deal_ids") or "").split(";")
                  if x.strip() in by_id and by_id[x.strip()]["outcome"] == "completed"]
            rd = [d for d in rd if d]
            pay_date = max(rd) if rd else pay_date
        out.append({"id": r["deal_id"], "ticker": r["target_ticker"].upper(), "announce": r["announce_date"], "offer": offer,
                    "paid": paid, "y": y, "pay_date": (pay_date or "")[:10], "outcome_date": (r.get("outcome_date") or "")[:10],
                    "booklet": (r.get("booklet_date") or "")[:10], "structure": r["structure"]})
    return out


def write_sample(root: str) -> int:
    ev = events(root)
    tickers = sorted({e["ticker"] for e in ev})
    with open(os.path.join(root, "config", "universe_history_au_deals.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ticker", "market", "provider", "provider_symbol", "why"])
        for t in tickers:
            w.writerow([t, "ASX", "eodhd", f"{t}.AU", "rulebook 9c: ASX cash deal target 2015 to 2025"])
    print(f"{len(ev)} events, {len(tickers)} tickers")
    return 0


def result(e: dict, px: list[dict], rates: Rates, entry_on: str) -> tuple[str, dict | None]:
    dates = [b["date"] for b in px]
    i = next((k for k, d in enumerate(dates) if d > entry_on), None)
    if i is None or i < 21:
        return "no prices around the announcement", None
    entry = px[i]
    if not ENTRY_BAND[0] * e["offer"] <= entry["open"] <= ENTRY_BAND[1] * e["offer"]:
        return "entry price outside 85% to 101% of the offer (a different share on the code, or not a cash deal)", None
    a = next((k for k, d in enumerate(dates) if d >= e["announce"]), i)
    window = px[max(0, a - 21): max(1, a - 1)]
    med_value = stats.median(b["close"] * b["volume"] for b in window) if window else 0.0
    half_spread = spread_estimate([b["high"] for b in window], [b["low"] for b in window], med_value * NZD_PER_AUD) / 2 if len(window) >= 5 else 0.01
    if e["y"] == 1:
        if not e["pay_date"]:
            return "no payment date", None
        exit_px, exit_date, sell_cost, kind = e["paid"], e["pay_date"], 0.0, "paid"
    else:
        j = next((k for k, d in enumerate(dates) if d > e["outcome_date"]), None) if e["outcome_date"] else None
        if j is None:
            return "no prices after the deal ended", None
        exit_px, exit_date, sell_cost, kind = px[j]["open"], px[j]["date"], FEE + half_spread, "broke"
    days = (date.fromisoformat(exit_date) - date.fromisoformat(entry["date"])).days
    if days <= 0:
        return "paid before the entry date", None
    buy_cost = FEE + half_spread + FX_ROUND_TRIP + HEDGE
    gross = exit_px / entry["open"] - 1
    try:
        cash = rates.three_month("AUD", entry["date"]) * days / 365
    except ValueError:
        cash = 0.0
    und = px[max(0, a - 1)]["close"] if a >= 1 else None
    implied = min(1.0, max(0.0, (entry["open"] - und) / (e["offer"] - und))) if und and e["offer"] > und else None
    return "ok", {"id": e["id"], "ticker": e["ticker"], "entry": entry["date"], "exit": exit_date, "kind": kind, "gross": gross,
                  "costs": buy_cost + sell_cost, "cash": cash, "net": gross - buy_cost - sell_cost - cash, "days": days,
                  "implied": implied, "y": e["y"], "year": entry["date"][:4]}


def summary(res: list[dict]) -> tuple[list[str], bool]:
    nets = [r["net"] for r in res]
    n, mean, sd = len(nets), stats.mean(nets), stats.stdev(nets)
    t = mean / (sd / math.sqrt(n)) if sd else 0.0
    by_year = defaultdict(list)
    for r in res:
        by_year[r["year"]].append(r["net"])
    total = sum(nets)
    top = max(((y, sum(v)) for y, v in by_year.items()), key=lambda x: x[1])
    worst = min(((y, stats.mean(v)) for y, v in by_year.items()), key=lambda x: x[1])
    checks = [("At least 60 events", n >= 60, str(n)),
              ("Mean after costs and cash above zero with t of 2 or more", mean > 0 and t >= 2, f"{mean:+.2%}, t {t:.2f}"),
              ("No single year more than half the total gain", total > 0 and top[1] / total <= 0.5, f"{top[0]}: {top[1] / total:.0%}" if total > 0 else "no total gain"),
              ("Worst year no worse than -4% per event", worst[1] >= -0.04, f"{worst[0]}: {worst[1]:+.2%}")]
    imp = [r for r in res if r["implied"] is not None]
    lines = ["| Measure | Value |", "| --- | --- |",
             f"| Events | {n} (paid {sum(1 for r in res if r['kind'] == 'paid')}, broke {sum(1 for r in res if r['kind'] == 'broke')}) |",
             f"| Mean gross return | {stats.mean(r['gross'] for r in res):+.2%} |",
             f"| Mean costs | {stats.mean(r['costs'] for r in res):.2%} |",
             f"| Mean cash over the same days | {stats.mean(r['cash'] for r in res):.2%} |",
             f"| Mean result after costs, less cash | {mean:+.2%} (median {stats.median(nets):+.2%}) |",
             f"| t-statistic | {t:.2f} |",
             f"| Median days held | {int(stats.median(r['days'] for r in res))} |",
             f"| Mean market-implied chance at entry / actual paid rate | {stats.mean(r['implied'] for r in imp):.0%} / {stats.mean(r['y'] for r in imp):.0%} |" if imp else "| Market-implied chance | n/a |",
             "", "| Year | Events | Mean result |", "| --- | --- | --- |",
             *[f"| {y} | {len(v)} | {stats.mean(v):+.2%} |" for y, v in sorted(by_year.items())], "",
             "| Pass mark | Met | Value |", "| --- | --- | --- |", *[f"| {c[0]} | {'yes' if c[1] else 'no'} | {c[2]} |" for c in checks]]
    return lines, all(c[1] for c in checks)


def main(root: str, force: bool = False) -> int:
    report = os.path.join(root, "reports", "deal_au_history.md")
    lock = report + ".lock"
    if os.path.exists(lock) and not force:
        print("result already written; use --force to re-run (the re-run is recorded)")
        return 0
    uni = os.path.join(root, "config", "universe_history_au_deals.csv")
    sample = [r["ticker"] for r in csv.DictReader(open(uni))]
    pdir = os.path.join(root, "data", "history", "prices", "ASX")
    fetched = [t for t in sample if os.path.exists(os.path.join(pdir, f"{t}.csv")) or os.path.exists(os.path.join(pdir, f"{t}.csv.none"))]
    title = "# Deal spreads history test: ASX cash deals\n\n"
    if len(fetched) < len(sample):
        open(report, "w").write(title + f"Waiting for prices: {len(fetched)} of {len(sample)} tickers fetched "
                                f"({datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC). The prices need EODHD's paid plan; "
                                "the test runs once, when all are in.\n")
        print(f"waiting: {len(fetched)} of {len(sample)}")
        return 0
    rates = Rates(os.path.join(root, "data"))
    ev = events(root)
    # Prices: Norgate (delisted shares included) where its file is the named company, else EODHD, except
    # codes where neither source has the old company (config/history_price_exclusions.csv)
    nv = {tk: p for (tk, _), p in norgate_verified(root).items()}
    exp = os.path.join(root, "config", "history_price_exclusions.csv")
    excluded = {r["ticker"] for r in csv.DictReader(open(exp))} if os.path.exists(exp) else set()
    prices, source = {}, defaultdict(int)
    for t in sample:
        if t in nv:
            prices[t] = load_prices(nv[t]); source["Norgate"] += 1
        elif t not in excluded and os.path.exists(os.path.join(pdir, f"{t}.csv")):
            prices[t] = load_prices(os.path.join(pdir, f"{t}.csv")); source["EODHD"] += 1
    res, why = [], defaultdict(int)
    alt = []
    for e in ev:
        p = prices.get(e["ticker"])
        if not p:
            why["no prices from EODHD"] += 1
            continue
        st, r = result(e, p, rates, e["announce"])
        if r is None:
            why[st] += 1
        else:
            res.append(r)
        if e["booklet"] and e["structure"] == "scheme":
            st2, r2 = result(e, p, rates, e["booklet"])
            if r2:
                alt.append(r2)
    paid_all = sum(1 for e in ev if e["y"] == 1); broke_all = len(ev) - paid_all
    paid_used = sum(1 for r in res if r["y"] == 1); broke_used = len(res) - paid_used
    cover = (paid_used / paid_all if paid_all else 0, broke_used / broke_all if broke_all else 0)
    lines = [title.strip(), "", f"Rulebook section 9c. Run {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC{' (forced re-run)' if force else ''}. "
             f"{len(ev)} events in the database, {len(prices)} of {len(sample)} tickers with prices "
             f"({', '.join(f'{v} from {k}' for k, v in sorted(source.items()))}), {len(res)} events used.", "",
             f"Coverage: {cover[0]:.0%} of the deals that paid and {cover[1]:.0%} of the deals that broke have prices and pass the entry check "
             f"(the test needs {COVERAGE:.0%} of each, so that missing delisted shares can't tilt it).", ""]
    passed = False
    if cover[0] < COVERAGE or cover[1] < COVERAGE or len(res) < 2:
        lines += ["Not enough coverage to run. **Result: not run.**"]
    else:
        body, passed = summary(res)
        lines += body + ["", f"**Result: {'pass' if passed else 'fail'}.**"]
        if len(alt) >= 10:
            b2, _ = summary(alt)
            lines += ["", "## Reported only: entering when the scheme booklet is out", "", "Not a pass mark. The same rules, entering at the first open after the booklet date.", ""] + b2
    lines += ["", "Events left out, by reason: " + ("; ".join(f"{k} {v}" for k, v in sorted(why.items())) or "none") + ".",
              "", "Caveats: dividends paid during the hold are left out; a deal paid is credited at the final price on the implementation date "
              "with no sale costs; overlapping events move together, so the t-statistic overstates the evidence somewhat."]
    os.makedirs(os.path.dirname(report), exist_ok=True)
    open(report, "w").write("\n".join(lines) + "\n")
    if not any("Result: not run" in x for x in lines):
        open(lock, "w").write(datetime.now(timezone.utc).isoformat())   # a pass or fail is final; "not run" waits for better prices
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    root = a[0] if a else "."
    if "--sample" in sys.argv:
        sys.exit(write_sample(root))
    sys.exit(main(root, "--force" in sys.argv))
