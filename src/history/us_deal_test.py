"""Rulebook 9b: the history test for US cash deal spreads.

Runs once, when every sampled ticker in config/universe_history_deals.csv is fetched (as the
insider test does), and writes reports/deal_us_history.md and a lock file.
Usage: python3 -I src/history/us_deal_test.py <repo_root> [--force]
"""
import csv
import math
import os
import statistics as stats
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from insider_test import NZD_PER_USD, load_prices  # noqa: E402
from spreads import spread_estimate  # noqa: E402

STAKE_USD = 2300.0
FEE = 5.0 / STAKE_USD
FX_ROUND_TRIP = 0.005
BREAK_DROP, MAX_DAYS, BRK_LOOKBACK = 0.15, 400, 60
ENTRY_BAND = (0.85, 1.01)


def tbill(root: str) -> list[tuple[str, float]]:
    out = []
    with open(os.path.join(root, "data", "rates", "DTB3.csv"), newline="") as f:
        for r in csv.DictReader(f):
            if r["DTB3"] not in ("", "."):
                out.append((r["observation_date"], float(r["DTB3"]) / 100))
    return out


def rate_on(series, d):
    prior = [v for k, v in series if k <= d]
    return prior[-1] if prior else 0.0


def event_result(ev: dict, px: list[dict], last_data_date: str, bills) -> tuple[str, dict | None]:
    cash = float(ev["cash_price"])
    dates = [b["date"] for b in px]
    i = next((k for k, d in enumerate(dates) if d > ev["date"]), None)
    if i is None or i < BRK_LOOKBACK + 1:
        return "no prices around the filing", None
    entry = px[i]
    if not ENTRY_BAND[0] * cash <= entry["open"] <= ENTRY_BAND[1] * cash:
        return "entry price outside 85% to 101% of the cash price", None
    window = px[i - 20:i]
    med_value = stats.median(b["close"] * b["volume"] for b in window)
    half_spread = spread_estimate([b["high"] for b in window], [b["low"] for b in window], med_value * NZD_PER_USD) / 2
    end_by = (date.fromisoformat(entry["date"]) + timedelta(days=MAX_DAYS)).isoformat()
    exit_kind, exit_px, exit_date = None, None, None
    for k in range(i, len(px)):
        b = px[k]
        if b["date"] > end_by:
            exit_kind, exit_px, exit_date = "time", px[k - 1]["close"], px[k - 1]["date"]
            break
        if b["close"] < (1 - BREAK_DROP) * cash and k + 1 < len(px):
            exit_kind, exit_px, exit_date = "break", px[k + 1]["open"], px[k + 1]["date"]
            break
    if exit_kind is None:
        last = px[-1]
        stale = (date.fromisoformat(last_data_date) - date.fromisoformat(last["date"])).days > 14
        if not stale:
            return "not resolved yet", None
        exit_kind, exit_px, exit_date = "completed", max(cash, last["close"]), last["date"]
    # prices are unadjusted (deal targets rarely split); a dividend paid during the hold is left out (conservative)
    buy_cost = FEE + half_spread + FX_ROUND_TRIP
    sell_cost = 0.0 if exit_kind == "completed" else FEE + half_spread
    gross = exit_px / entry["open"] - 1
    days = (date.fromisoformat(exit_date) - date.fromisoformat(entry["date"])).days
    cash_ret = rate_on(bills, entry["date"]) * max(days, 1) / 365
    brk = px[i - BRK_LOOKBACK]["close"]
    implied = None
    if cash > brk:
        implied = min(1.0, max(0.0, (entry["open"] - brk) / (cash - brk)))
    return "ok", {"ticker": ev["ticker"], "date": ev["date"], "entry": entry["date"], "exit": exit_date, "kind": exit_kind,
                  "gross": gross, "costs": buy_cost + sell_cost, "cash": cash_ret, "net": gross - buy_cost - sell_cost - cash_ret,
                  "days": days, "implied": implied, "year": entry["date"][:4]}


def main(root: str, force: bool = False) -> int:
    report = os.path.join(root, "reports", "deal_us_history.md")
    lock = report + ".lock"
    if os.path.exists(lock) and not force:
        print("result already written; use --force to re-run (the re-run is recorded)")
        return 0
    uni = os.path.join(root, "config", "universe_history_deals.csv")
    sample = [r["ticker"] for r in csv.DictReader(open(uni))]
    pdir = os.path.join(root, "data", "history", "prices", "US")
    fetched = [t for t in sample if os.path.exists(os.path.join(pdir, f"{t}.csv")) or os.path.exists(os.path.join(pdir, f"{t}.csv.none"))]
    os.makedirs(os.path.dirname(report), exist_ok=True)
    if len(fetched) < len(sample):
        open(report, "w").write("# Deal spreads history test: US cash deals\n\n"
                                f"Waiting for prices: {len(fetched)} of {len(sample)} sampled tickers fetched "
                                f"({datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC). The test runs once, when all are in.\n")
        print(f"waiting: {len(fetched)} of {len(sample)}")
        return 0
    bills = tbill(root)
    events = [e for e in csv.DictReader(open(os.path.join(root, "data", "history", "us_deal_events.csv"), newline=""))
              if e["ticker"] in set(sample) and e["cash_price"] and not e["cash_price"].startswith("error")]
    prices = {t: load_prices(os.path.join(pdir, f"{t}.csv")) for t in sample if os.path.exists(os.path.join(pdir, f"{t}.csv"))}
    last_data = max((p[-1]["date"] for p in prices.values() if p), default=date.today().isoformat())
    res, why = [], defaultdict(int)
    for e in events:
        if not ("2015" <= e["date"][:4] <= "2025"):
            continue
        p = prices.get(e["ticker"])
        if not p:
            why["no prices from Tiingo"] += 1; continue
        st, r = event_result(e, p, last_data, bills)
        if r is None:
            why[st] += 1
        else:
            res.append(r)
    lines = ["# Deal spreads history test: US cash deals", "",
             f"Rulebook section 9b. Run {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC{' (forced re-run)' if force else ''}. "
             f"Sample: {len(sample)} tickers (seed 20261102), {len(prices)} with prices; {len(res)} events used.", ""]
    if len(res) < 2:
        lines += ["Too few events. Result: fail."]
    else:
        nets = [r["net"] for r in res]
        n, mean, sd = len(nets), stats.mean(nets), stats.stdev(nets)
        t = mean / (sd / math.sqrt(n)) if sd else 0.0
        by_year = defaultdict(list)
        for r in res:
            by_year[r["year"]].append(r["net"])
        total = sum(nets)
        top = max(((y, sum(v)) for y, v in by_year.items()), key=lambda x: x[1])
        worst = min(((y, stats.mean(v)) for y, v in by_year.items()), key=lambda x: x[1])
        kinds = defaultdict(int)
        for r in res:
            kinds[r["kind"]] += 1
        days = [r["days"] for r in res]
        yearly = [((1 + r["gross"] - r["costs"]) ** (365 / max(r["days"], 1)) - 1) for r in res if r["days"] >= 20]
        checks = [("At least 60 events", n >= 60, str(n)),
                  ("Mean after costs and cash above zero with t of 2 or more", mean > 0 and t >= 2, f"{mean:+.2%}, t {t:.2f}"),
                  ("No single year more than half the total gain", total > 0 and top[1] / total <= 0.5,
                   f"{top[0]}: {top[1] / total:.0%}" if total > 0 else "no total gain"),
                  ("Worst year no worse than -4% per event", worst[1] >= -0.04, f"{worst[0]}: {worst[1]:+.2%}")]
        passed = all(c[1] for c in checks)
        imp = [r for r in res if r["implied"] is not None]
        comp = [1.0 if r["kind"] == "completed" else 0.0 for r in imp]
        early = [r for r in imp if r["year"] < "2020"]
        base = stats.mean(1.0 if r["kind"] == "completed" else 0.0 for r in early) if early else float("nan")
        late = [r for r in imp if r["year"] >= "2020"]
        brier_mkt = stats.mean(((1.0 if r["kind"] == "completed" else 0.0) - r["implied"]) ** 2 for r in late) if late else float("nan")
        brier_base = stats.mean(((1.0 if r["kind"] == "completed" else 0.0) - base) ** 2 for r in late) if late else float("nan")
        lines += ["| Measure | Value |", "| --- | --- |",
                  f"| Events | {n} (completed {kinds['completed']}, broke {kinds['break']}, still open at 400 days {kinds['time']}) |",
                  f"| Mean gross return | {stats.mean(r['gross'] for r in res):+.2%} |",
                  f"| Mean costs | {stats.mean(r['costs'] for r in res):.2%} |",
                  f"| Mean cash over the same days | {stats.mean(r['cash'] for r in res):.2%} |",
                  f"| Mean result after costs, less cash | {mean:+.2%} (median {stats.median(nets):+.2%}) |",
                  f"| t-statistic | {t:.2f} |",
                  f"| Median days held | {int(stats.median(days))} |",
                  f"| Median yearly rate after costs (held 20 days or more) | {stats.median(yearly):+.1%} |" if yearly else "| Median yearly rate | n/a |",
                  f"| Mean market-implied chance at entry | {stats.mean(r['implied'] for r in imp):.0%} |" if imp else "| Mean market-implied chance | n/a |",
                  f"| Actual completion rate (same events) | {stats.mean(comp):.0%} |" if comp else "| Actual completion rate | n/a |",
                  f"| Brier score 2020 to 2025: market-implied / base rate from 2015 to 2019 | {brier_mkt:.3f} / {brier_base:.3f} (lower is better) |", "",
                  "| Year | Events | Mean result |", "| --- | --- | --- |",
                  *[f"| {y} | {len(v)} | {stats.mean(v):+.2%} |" for y, v in sorted(by_year.items())], "",
                  "| Pass mark | Met | Value |", "| --- | --- | --- |", *[f"| {c[0]} | {'yes' if c[1] else 'no'} | {c[2]} |" for c in checks], "",
                  f"**Result: {'pass' if passed else 'fail'}.**"]
    lines += ["", "Events left out, by reason: " + "; ".join(f"{k} {v}" for k, v in sorted(why.items())) + ".",
              "", "Caveats: a share that stops trading is taken as completed; a dividend paid during the hold is left out; "
              "events that overlap in time move together, so the t-statistic overstates the evidence somewhat."]
    open(report, "w").write("\n".join(lines) + "\n")
    open(lock, "w").write(datetime.now(timezone.utc).isoformat())
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else ".", "--force" in sys.argv))
