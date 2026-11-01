"""History test 9k (rulebook): buying ASX deals after the ACCC raises concerns.

Events: the ASX cash deals of test 9c (src/history/au_deal_test.py, announced 2015 to 2025, resolved) where,
while the deal was live, the ACCC published a statement of issues or moved its provisional decision date
later or suspended it (data/regulators/accc_deals.csv: soi_dates and delay_events). A request for
information on its own doesn't count. The event date is the first such signal.
Buy at the open of the first session after the event date if the deal hasn't ended and the open is between
the undisturbed price (the close before the announcement) and 101% of the offer. Exit as in 9c. Costs as in
the shared terms for 9g to 9j at A$3,000 (no currency conversion per deal); A$10,000 is reported beside it.
Result: return after costs less the Australian three-month bank bill rate. Nothing is tuned.
Writes reports/accc_history.md and a lock. Usage: python3 -I src/history/accc_test.py <repo_root> [--force]
"""
import csv
import math
import os
import re
import statistics as stats
import sys
from collections import defaultdict
from datetime import date, datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from au_deal_test import events  # noqa: E402
from insider_test import load_prices  # noqa: E402
from norgate_link import verified as norgate_verified  # noqa: E402
from rates import Rates  # noqa: E402
from spreads import spread_estimate  # noqa: E402

HEDGE = 0.001
NZD_PER_AUD = 1.08
MIN_EVENTS = 12
DELAY_WORDS = re.compile(r"suspend|extend|moved|postpon|delay|later date|new (provisional )?date|revised|deferred|pushed back|on hold|put on hold", re.I)
ROUTINE = re.compile(r"^(the accc )?(requested|request for|received|receipt of)\b", re.I)


def fee(stake: float) -> float:
    return min(0.019 * stake, 15.0) / stake


def signals(row: dict) -> list[tuple[str, str]]:
    """(date, kind) for every statement of issues and every timeline delay in an ACCC row."""
    out = []
    for d in (row.get("soi_dates") or "").split(";"):
        d = d.strip()[:10]
        if re.fullmatch(r"\d{4}-\d\d-\d\d", d):
            out.append((d, "statement of issues"))
    for ev in (row.get("delay_events") or "").split(";"):
        ev = ev.strip()
        m = re.match(r"(\d{4}-\d\d-\d\d)\s*:?\s*(.*)", ev)
        if not m:
            continue
        text = m.group(2)
        if DELAY_WORDS.search(text) and not (ROUTINE.search(text) and not re.search(r"suspend|extend|moved|postpon|delay|on hold", text, re.I)):
            out.append((m.group(1), "delay"))
    return sorted(out)


def result(e: dict, px: list[dict], rates: Rates, entry_on: str, stake: float) -> tuple[str, dict | None]:
    dates = [b["date"] for b in px]
    i = next((k for k, d in enumerate(dates) if d > entry_on), None)
    a = next((k for k, d in enumerate(dates) if d >= e["announce"]), None)
    if i is None or a is None or a < 22:
        return "no prices around the event", None
    und = px[a - 1]["close"]
    entry = px[i]
    if e["y"] == 1 and e["pay_date"] and entry["date"] >= e["pay_date"]:
        return "deal had paid before the entry date", None
    if e["y"] == 0 and e["outcome_date"] and entry["date"] > e["outcome_date"]:
        return "deal had ended before the entry date", None
    if not (und <= entry["open"] <= 1.01 * e["offer"]):
        return "entry price outside the range from the undisturbed price to 101% of the offer", None
    window = px[max(0, i - 21): max(1, i - 1)]
    med_value = stats.median(b["close"] * b["volume"] for b in window) if window else 0.0
    half = spread_estimate([b["high"] for b in window], [b["low"] for b in window], med_value * NZD_PER_AUD) / 2 if len(window) >= 5 else 0.01
    f = fee(stake)
    if e["y"] == 1:
        exit_px, exit_date, sell_cost, kind = e["paid"], e["pay_date"], 0.0, "paid"
    else:
        j = next((k for k, d in enumerate(dates) if d > e["outcome_date"]), None) if e["outcome_date"] else None
        if j is None:
            return "no prices after the deal ended", None
        exit_px, exit_date, sell_cost, kind = px[j]["open"], px[j]["date"], f + half, "broke"
    days = (date.fromisoformat(exit_date) - date.fromisoformat(entry["date"])).days
    if days <= 0:
        return "paid before the entry date", None
    buy_cost = f + half + HEDGE
    gross = exit_px / entry["open"] - 1
    try:
        cash = rates.three_month("AUD", entry["date"]) * days / 365
    except ValueError:
        cash = 0.0
    implied = min(1.0, max(0.0, (entry["open"] - und) / (e["offer"] - und))) if e["offer"] > und else None
    return "ok", {"id": e["id"], "ticker": e["ticker"], "entry": entry["date"], "exit": exit_date, "kind": kind, "gross": gross,
                  "costs": buy_cost + sell_cost, "cash": cash, "net": gross - buy_cost - sell_cost - cash, "days": days,
                  "implied": implied, "y": e["y"], "year": entry["date"][:4]}


def table(res: list[dict]) -> tuple[list[str], dict]:
    nets = [r["net"] for r in res]
    n, mean = len(nets), stats.mean(nets)
    sd = stats.stdev(nets) if n > 1 else 0.0
    t = mean / (sd / math.sqrt(n)) if sd else 0.0
    k = max(1, round(0.05 * n))
    trimmed = stats.mean(sorted(nets)[:-k]) if n > k else float("nan")
    imp = [r for r in res if r["implied"] is not None]
    implied, paid = (stats.mean(r["implied"] for r in imp), stats.mean(r["y"] for r in imp)) if imp else (float("nan"), float("nan"))
    lines = ["| Measure | Value |", "| --- | --- |",
             f"| Events | {n} (paid {sum(1 for r in res if r['kind'] == 'paid')}, broke {sum(1 for r in res if r['kind'] == 'broke')}) |",
             f"| Mean gross return | {stats.mean(r['gross'] for r in res):+.2%} |", f"| Mean costs | {stats.mean(r['costs'] for r in res):.2%} |",
             f"| Mean cash over the same days | {stats.mean(r['cash'] for r in res):.2%} |",
             f"| Mean result after costs, less cash | {mean:+.2%} (median {stats.median(nets):+.2%}) |", f"| t-statistic | {t:.2f} |",
             f"| Median days held | {int(stats.median(r['days'] for r in res))} |",
             f"| Mean market-implied chance at entry / share that paid | {implied:.0%} / {paid:.0%} |" if imp else "| Market-implied chance | n/a |"]
    return lines, {"n": n, "mean": mean, "t": t, "trimmed": trimmed, "implied": implied, "paid": paid}


def main(root: str, force: bool = False) -> int:
    report = os.path.join(root, "reports", "accc_history.md")
    lock = report + ".lock"
    title = "# History test 9k: buying ASX deals after the ACCC raises concerns\n\n"
    if os.path.exists(lock) and not force:
        print("result already written; use --force to re-run (the re-run is recorded)"); return 0
    ap = os.path.join(root, "data", "regulators", "accc_deals.csv")
    if not os.path.exists(ap):
        open(report, "w").write(title + "Waiting for the ACCC data (data/regulators/accc_deals.csv).\n")
        print("waiting for the ACCC data"); return 0
    accc = {r["deal_id"]: r for r in csv.DictReader(open(ap, encoding="utf-8"))}
    rates = Rates(os.path.join(root, "data"))
    ev = events(root)
    nv = {tk: p for (tk, _), p in norgate_verified(root).items()}
    pdir = os.path.join(root, "data", "history", "prices", "ASX")
    exp = os.path.join(root, "config", "history_price_exclusions.csv")
    excluded = {r["ticker"] for r in csv.DictReader(open(exp))} if os.path.exists(exp) else set()

    def prices(t):
        if t in nv:
            return load_prices(nv[t])
        if t not in excluded and os.path.exists(os.path.join(pdir, f"{t}.csv")):
            return load_prices(os.path.join(pdir, f"{t}.csv"))
        return None
    reviewed = [e for e in ev if (accc.get(e["id"], {}).get("accc_reviewed") or "").upper() == "Y"]
    chosen, why = [], defaultdict(int)
    for e in reviewed:
        end = e["pay_date"] if e["y"] == 1 else e["outcome_date"]
        sig = [(d, k) for d, k in signals(accc[e["id"]]) if d >= e["announce"][:10] and (not end or d < end)]
        if not sig:
            why["reviewed with no signal while the deal was live"] += 1; continue
        chosen.append((e, sig[0][0], sig[0][1], any(k == "statement of issues" for _, k in sig)))
    res, res10, kinds = [], [], {}
    for e, d, kind, had_soi in chosen:
        p = prices(e["ticker"])
        if not p:
            why["no prices"] += 1; continue
        st, r = result(e, p, rates, d, 3000.0)
        if r is None:
            why[st] += 1; continue
        r["signal"], r["signal_date"], r["had_soi"] = kind, d, had_soi
        res.append(r)
        _, r10 = result(e, p, rates, d, 10000.0)
        if r10:
            res10.append(r10)
    L = [title.strip(), "", f"Rulebook section 9k. Run {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC{' (forced re-run)' if force else ''}.", "",
         f"ASX cash deals in test 9c's set: {len(ev)}. Reviewed by the ACCC: {len(reviewed)}. With a statement of issues or a delay while live: {len(chosen)}. "
         f"Not searched on the ACCC's registers (search limit): {sum(1 for e in ev if (accc.get(e['id'], {}).get('accc_reviewed') or '').lower() == 'unknown')}; "
         "spot checks of the likeliest (Adbri, National Storage, Domain) found no ACCC concerns or delays.", ""]
    passed = False
    if len(res) < MIN_EVENTS:
        L += [f"Only {len(res)} events with prices; the test needs {MIN_EVENTS}. **Result: fail.**"]
        if res:
            body, m = table(res)
            L += ["", "Reported only, the events there were:", ""] + body
    else:
        body, m = table(res)
        checks = [(f"At least {MIN_EVENTS} events", True, str(m["n"])),
                  ("Mean after costs and cash above zero with t of 2 or more", m["mean"] > 0 and m["t"] >= 2, f"{m['mean']:+.2%}, t {m['t']:.2f}"),
                  ("Still above zero without the best 5% of events", m["trimmed"] > 0, f"{m['trimmed']:+.2%}"),
                  ("Market-implied chance at entry below the share that paid", m["implied"] < m["paid"], f"{m['implied']:.0%} against {m['paid']:.0%}")]
        passed = all(c[1] for c in checks)
        L += body + ["", "| Pass mark | Met | Value |", "| --- | --- | --- |"] + [f"| {a} | {'yes' if b else 'no'} | {c} |" for a, b, c in checks]
        L += ["", f"**Result: {'pass' if passed else 'fail'}.**"]
    if res:
        L += ["", "| Deal | Signal | Signal date | Entry | Outcome | Result |", "| --- | --- | --- | --- | --- | --- |"]
        L += [f"| {r['ticker']} ({r['id']}) | {r['signal']} | {r['signal_date']} | {r['entry']} | {r['kind']} | {r['net']:+.2%} |" for r in sorted(res, key=lambda x: x["entry"])]
        if res10:
            b10, m10 = table(res10)
            L += ["", "Reported only, at A$10,000 a position:", ""] + b10
        soi = [r["net"] for r in res if r["had_soi"]]
        dl = [r["net"] for r in res if not r["had_soi"]]
        L += ["", f"Reported only: deals with a statement of issues {len(soi)}, mean {stats.mean(soi):+.2%}; with only a delay {len(dl)}, "
                  f"mean {stats.mean(dl):+.2%}." if soi and dl else ""]
    quiet = [e for e in reviewed if e["id"] not in {c[0]["id"] for c in chosen}]
    if quiet:
        L += ["", f"Reported only: ACCC-reviewed deals with no signal while live: {len(quiet)}, of which {sum(e['y'] for e in quiet)} paid."]
    L += ["", "Events left out, by reason: " + ("; ".join(f"{k} {v}" for k, v in sorted(why.items())) or "none") + ".",
          "", "Caveats: a small sample; dividends during the hold are left out; a deal paid is credited at the final price with no sale costs."]
    os.makedirs(os.path.dirname(report), exist_ok=True)
    open(report, "w").write("\n".join(L) + "\n")
    open(lock, "w").write(datetime.now(timezone.utc).isoformat())
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    sys.exit(main(a[0] if a else ".", "--force" in sys.argv))
