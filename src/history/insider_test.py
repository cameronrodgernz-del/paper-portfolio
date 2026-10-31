"""Rulebook 9a: the history test for US director and officer buying clusters.

Runs only when every sampled ticker in config/universe_history.csv has been fetched (or found to
have no data). Until then it writes a progress note and stops, so the hold-out years are run once,
on the full sample. After a full run it writes a lock file, and later runs leave the result alone
unless given --force (any re-run is recorded in the report).

Inputs: data/history/insider_clusters_n{2,3,4}.csv, data/history/prices/US/*.csv (Tiingo, with
adjusted closes), data/history/tiingo_supported.csv (exchange of each ticker).
Output: reports/special_insider_history.md
Usage: python3 -I src/history/insider_test.py <repo_root> [--force]
"""
import csv
import math
import os
import statistics as stats
import sys
from collections import defaultdict
from datetime import datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from fills import size_cost  # noqa: E402
from spreads import spread_estimate  # noqa: E402

STAKE_USD = 1700.0
BROKERAGE = 2 * 5.0 / STAKE_USD
FX_ROUND_TRIP = 0.005
NZD_PER_USD = 1.6          # only used to place a share in the engine's spread floors
EXCHANGES = {"NYSE", "NASDAQ"}
VERSIONS = [(n, h, liq) for n in (2, 3, 4) for h in (63, 126) for liq in (1e6, 5e6)]
MIN_TUNING_EVENTS = 60


def load_prices(path: str) -> list[dict]:
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            try:
                o, h, l, c, v = (float(r[k]) for k in ("open", "high", "low", "close", "volume"))
                adj = float(r["adj_close"]) if r.get("adj_close") else c
            except (TypeError, ValueError):
                continue
            if c <= 0 or o <= 0:
                continue
            k = adj / c                       # adjusted = raw x (adjusted close / raw close)
            rows.append({"date": r["date"], "open": o, "high": h, "low": l, "close": c, "volume": v,
                         "aopen": o * k, "aclose": adj})
    return rows


def event_result(ev: dict, px: list[dict], spy: dict, hold: int, min_liq: float) -> tuple[str, dict | None]:
    dates = [b["date"] for b in px]
    # sanity: the reported purchase price is within 25% of the close on (or just before) the first trade
    prior = [b for b in px if b["date"] <= ev["first_trade"]]
    if not prior or abs(prior[-1]["close"] / float(ev["avg_price"]) - 1) > 0.25:
        return "price check failed (ticker may have been reused)", None
    i = next((k for k, d in enumerate(dates) if d > ev["event_date"]), None)
    if i is None or i < 21:
        return "no prices around the event", None
    if i + hold >= len(px):
        return "exit not reached yet", None
    window = px[i - 20:i]
    med_value = stats.median(b["close"] * b["volume"] for b in window)
    if px[i]["open"] < 3:
        return "under US$3 at entry", None
    if med_value < min_liq:
        return "too little trading", None
    entry, exit_ = px[i], px[i + hold]
    if entry["date"] not in spy or exit_["date"] not in spy:
        return "benchmark missing a date", None
    raw = exit_["aopen"] / entry["aopen"] - 1
    bench = spy[exit_["date"]]["aopen"] / spy[entry["date"]]["aopen"] - 1
    spread = spread_estimate([b["high"] for b in window], [b["low"] for b in window], med_value * NZD_PER_USD)
    rets = [math.log(b["close"] / a["close"]) for a, b in zip(window, window[1:]) if a["close"] > 0 and b["close"] > 0]
    vol = (sum(r * r for r in rets) / max(1, len(rets))) ** 0.5 if rets else 0.03
    impact = size_cost(STAKE_USD, stats.mean(b["close"] * b["volume"] for b in window), vol)
    costs = BROKERAGE + FX_ROUND_TRIP + spread + 2 * impact
    return "ok", {"ticker": ev["ticker"], "event_date": ev["event_date"], "entry": entry["date"], "exit": exit_["date"],
                  "raw": raw, "bench": bench, "costs": costs, "net": raw - bench - costs, "year": ev["event_date"][:4]}


def summarise(rs: list[dict]) -> dict:
    nets = [r["net"] for r in rs]
    n = len(nets)
    if n < 2:
        return {"n": n}
    mean, sd = stats.mean(nets), stats.stdev(nets)
    keep = sorted(nets)[: n - max(1, round(0.05 * n))]
    by_year = defaultdict(float)
    for r in rs:
        by_year[r["year"]] += r["net"]
    total = sum(nets)
    top_year = max(by_year.items(), key=lambda kv: kv[1])
    return {"n": n, "mean": mean, "median": stats.median(nets), "t": mean / (sd / math.sqrt(n)) if sd > 0 else 0.0,
            "trimmed_mean": stats.mean(keep) if keep else float("nan"), "hit": sum(1 for x in nets if x > 0) / n,
            "mean_costs": stats.mean(r["costs"] for r in rs), "mean_raw": stats.mean(r["raw"] for r in rs),
            "mean_bench": stats.mean(r["bench"] for r in rs), "by_year": dict(sorted(by_year.items())),
            "total": total, "top_year": top_year, "top_year_share": top_year[1] / total if total > 0 else float("nan")}


def main(root: str, force: bool = False) -> int:
    hist = os.path.join(root, "data", "history")
    report = os.path.join(root, "reports", "special_insider_history.md")
    lock = report + ".lock"
    if os.path.exists(lock) and not force:
        print("result already written; use --force to re-run (the re-run is recorded)")
        return 0
    sample = [r["ticker"] for r in csv.DictReader(open(os.path.join(root, "config", "universe_history.csv"))) if r["ticker"] != "SPY"]
    pdir = os.path.join(hist, "prices", "US")
    fetched = [t for t in sample if os.path.exists(os.path.join(pdir, f"{t}.csv")) or os.path.exists(os.path.join(pdir, f"{t}.csv.none"))]
    os.makedirs(os.path.dirname(report), exist_ok=True)
    if len(fetched) < len(sample) or not os.path.exists(os.path.join(pdir, "SPY.csv")):
        open(report, "w").write("# Special situations history test: US director and officer buying clusters\n\n"
                                f"Waiting for prices: {len(fetched)} of {len(sample)} sampled tickers fetched "
                                f"({datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC). The test runs once, when all are in.\n")
        print(f"waiting: {len(fetched)} of {len(sample)}")
        return 0
    exch = {}
    sup = os.path.join(hist, "tiingo_supported.csv")
    if os.path.exists(sup):
        for r in csv.DictReader(open(sup, newline="")):
            exch.setdefault(r["ticker"].upper(), set()).add(r.get("exchange", ""))
    spy = {b["date"]: b for b in load_prices(os.path.join(pdir, "SPY.csv"))}
    prices = {t: load_prices(os.path.join(pdir, f"{t}.csv")) for t in sample if os.path.exists(os.path.join(pdir, f"{t}.csv"))}
    sample_set = set(sample)
    events = {n: [e for e in csv.DictReader(open(os.path.join(hist, f"insider_clusters_n{n}.csv"), newline=""))
                  if e["ticker"].upper() in sample_set] for n in (2, 3, 4)}

    def run(n, h, liq, years):
        out, why = [], defaultdict(int)
        for e in events[n]:
            if not (years[0] <= e["event_date"][:4] <= years[1]):
                continue
            t = e["ticker"].upper()
            if t not in prices:
                why["no prices from Tiingo"] += 1; continue
            if exch and not (exch.get(t, set()) & EXCHANGES):
                why["not NYSE or Nasdaq"] += 1; continue
            status, res = event_result(e, prices[t], spy, h, liq)
            if res is None:
                why[status] += 1
            else:
                out.append(res)
        return out, why

    tuning = []
    for v in VERSIONS:
        rs, why = run(*v, ("2010", "2019"))
        tuning.append((v, summarise(rs), why))
    eligible = [x for x in tuning if x[1]["n"] >= MIN_TUNING_EVENTS]
    pick = max(eligible, key=lambda x: x[1]["mean"]) if eligible else None
    lines = ["# Special situations history test: US director and officer buying clusters", "",
             f"Rulebook section 9a. Run {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC{' (forced re-run)' if force else ''}. "
             f"Sample: {len(sample)} tickers drawn at random (seed 20261101), {len(prices)} with Tiingo prices.", "",
             f"Each event is bought at the open after the filing that completes the cluster and sold at the open H sessions later. "
             f"Result = return less SPY over the same sessions, after US$5 brokerage each way on a US${STAKE_USD:,.0f} stake, "
             f"0.5% currency conversion and the estimated spread.", "",
             "## Tuning, 2010 to 2019 (all 12 versions tried)", "",
             "| Buyers | Hold (sessions) | Min traded value | Events | Mean after costs | Median | t | Hit rate | Mean costs |",
             "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for (n, h, liq), s, _ in tuning:
        if s["n"] < 2:
            lines.append(f"| {n} | {h} | US${liq / 1e6:.0f}m | {s['n']} | | | | | |")
        else:
            lines.append(f"| {n} | {h} | US${liq / 1e6:.0f}m | {s['n']} | {s['mean']:+.2%} | {s['median']:+.2%} | {s['t']:.2f} | {s['hit']:.0%} | {s['mean_costs']:.2%} |")
    if not pick:
        lines += ["", f"No version had {MIN_TUNING_EVENTS} tuning events, so nothing is picked and the hold-out is not run. **Result: fail.**"]
    else:
        (n, h, liq), ts, _ = pick
        rs, why = run(n, h, liq, ("2020", "2026"))
        s = summarise(rs)
        checks = []
        if s["n"] >= 2:
            checks = [("At least 30 events", s["n"] >= 30, f"{s['n']}"),
                      ("Mean after costs above zero with t of 2 or more", s["mean"] > 0 and s["t"] >= 2, f"{s['mean']:+.2%}, t {s['t']:.2f}"),
                      ("Still above zero without the best 5% of events", s["trimmed_mean"] > 0, f"{s['trimmed_mean']:+.2%}"),
                      ("No single year more than half the total gain", s["total"] > 0 and s["top_year_share"] <= 0.5,
                       f"{s['top_year'][0]}: {s['top_year_share']:.0%} of the total" if s["total"] > 0 else "no total gain")]
        passed = bool(checks) and all(c[1] for c in checks)
        lines += ["", f"Picked: {n} or more buyers, held {h} sessions, traded value at least US${liq / 1e6:.0f}m "
                      f"(tuning mean {ts['mean']:+.2%} on {ts['n']} events).", "",
                  "## Hold-out, 2020 onwards (run once)", ""]
        if s["n"] < 2:
            lines += [f"Only {s['n']} events. **Result: fail.**"]
        else:
            lines += ["| Measure | Value |", "| --- | --- |",
                      f"| Events | {s['n']} |", f"| Mean return | {s['mean_raw']:+.2%} |", f"| Mean SPY return | {s['mean_bench']:+.2%} |",
                      f"| Mean costs | {s['mean_costs']:.2%} |", f"| Mean after costs, less SPY | {s['mean']:+.2%} |",
                      f"| Median | {s['median']:+.2%} |", f"| t-statistic | {s['t']:.2f} |", f"| Hit rate | {s['hit']:.0%} |", "",
                      "| Year | Sum of results |", "| --- | --- |", *[f"| {y} | {v:+.1%} |" for y, v in s["by_year"].items()], "",
                      "| Pass mark | Met | Value |", "| --- | --- | --- |", *[f"| {c[0]} | {'yes' if c[1] else 'no'} | {c[2]} |" for c in checks], "",
                      f"**Result: {'pass' if passed else 'fail'}.**"]
        lines += ["", "Events left out of the hold-out, by reason: " + "; ".join(f"{k} {v}" for k, v in sorted(why.items())) + "."]
    lines += ["", "Caveats: events that overlap in time move together, so the t-statistic overstates the evidence somewhat. "
              "Tiingo may lack some delisted shares. A pass is a screen, not proof."]
    open(report, "w").write("\n".join(lines) + "\n")
    open(lock, "w").write(datetime.now(timezone.utc).isoformat())
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else ".", "--force" in sys.argv))
