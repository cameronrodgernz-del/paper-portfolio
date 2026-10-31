"""The monthly report for a ledger (rulebook section 8): return, the passive comparisons, the
worst fall, costs paid, trades, dated calls and their scores so far, and every limit flag.
Usage: python3 -I src/monthly.py <ledger_name> <YYYY-MM>
"""
import json
import os
import statistics as stats
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ledger import Ledger  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def brier(calls: list[dict], outcomes: dict) -> tuple[float | None, float | None, int]:
    """Our chance of the main outcome against the market-implied chance, on resolved calls."""
    ours, mkt = [], []
    for c in calls:
        key = (c["market"], c["ticker"], c["made_utc"])
        if key not in outcomes or c.get("market_implied") is None:
            continue
        o = 1.0 if outcomes[key] else 0.0
        ours.append((c["p_main"] - o) ** 2)
        mkt.append((c["market_implied"] - o) ** 2)
    return (stats.mean(ours) if ours else None, stats.mean(mkt) if mkt else None, len(ours))


def main(name: str, month: str) -> int:
    cfg = json.load(open(os.path.join(ROOT, "config", "run.json")))
    L = Ledger(os.path.join(ROOT, cfg["ledgers"][name]["dir"]))
    vals = [r["payload"] for r in L.records("valuations")]
    in_month = [v for v in vals if v["date"][:7] == month]
    if not in_month:
        print("no valuations in", month)
        return 0
    before = [v for v in vals if v["date"][:7] < month]
    start = before[-1]["total_nzd"] if before else float(cfg["bankroll_nzd"])
    end = in_month[-1]
    fills = [r["payload"] for r in L.records("fills") if r["payload"]["date"][:7] == month]
    cash = [r["payload"] for r in L.records("cash")]
    fees = defaultdict(float)
    for f in fills:
        fees["brokerage_nzd"] += f["fee_local"] * f["nzd_per_local"]
        fees["spread_nzd"] += f["gross_nzd"] * f.get("spread_used", 0) / 2
    for h in (r["payload"] for r in L.records("hedges")):
        if h.get("event") == "open" and h["trade_date"][:7] == month:
            fees["hedge_nzd"] += h["notional_foreign"] / h["forward_mid"] * (h["forward_rate"] / h["forward_mid"] - 1)
    for c in cash:
        if c["kind"] == "fx_in" and (c.get("date") or "")[:7] == month:
            fees["fx_nzd"] += c.get("fee_nzd", 0)
        if c["kind"] == "plan_fee" and c.get("month") == month:
            fees["plan_nzd"] += -c["amount"]
    flags = [(v["date"], f) for v in in_month for f in v.get("flags", [])]
    records = [r["payload"] for r in L.records("calls")]
    calls = [c for c in records if c.get("event") != "outcome"]
    month_calls = [c for c in calls if c["made_utc"][:7] == month]
    outcomes = {(c["market"], c["ticker"], c["made_utc"]): c["main_outcome_happened"]     # logged by decide.resolve_call
                for c in records if c.get("event") == "outcome"}
    b_ours, b_mkt, n_scored = brier(calls, outcomes)
    bench = {}
    bp = os.path.join(ROOT, "reports", name, "benchmarks.json")
    if os.path.exists(bp):
        bench = json.load(open(bp))
    lines = [f"# {name}: {month}", "",
             "| Measure | Value |", "| --- | --- |",
             f"| Value at month end | NZ${end['total_nzd']:,.2f} |",
             f"| Return in the month | {end['total_nzd'] / start - 1:+.2%} |",
             f"| Return since the start | {end['total_nzd'] / float(cfg['bankroll_nzd']) - 1:+.2%} |",
             f"| Unhedged value at month end | NZ${end.get('total_unhedged_nzd', end['total_nzd']):,.2f} |",
             f"| Worst fall from peak so far | {min(v['drawdown'] for v in vals[:vals.index(end) + 1]):.2%} |"]
    if bench:
        lines += [f"| Core index mix since the start (test 3) | {bench['index_mix']:+.2%} |",
                  f"| Matched index-and-cash mix since the start (test 2) | {bench['matched_mix']:+.2%} |"]
    lines += [f"| Trades filled | {len(fills)} ({', '.join(f'{k} {v}' for k, v in Counter(f['sleeve'] for f in fills).items()) or 'none'}) |",
              f"| Brokerage paid | NZ${fees['brokerage_nzd']:,.2f} |", f"| Currency conversion fees | NZ${fees['fx_nzd']:,.2f} |",
              f"| Plan fee | NZ${fees['plan_nzd']:,.2f} |", f"| Hedge dealing costs | NZ${fees['hedge_nzd']:,.2f} |",
              f"| Estimated spread paid (the size cost is also inside fill prices) | NZ${fees['spread_nzd']:,.2f} |",
              f"| Dated calls made this month | {len(month_calls)} |",
              f"| Calls scored so far | {n_scored}" + (f" (our Brier {b_ours:.3f} against the market's {b_mkt:.3f}; lower is better)" if n_scored else "") + " |",
              "", "## By sleeve at month end", "", "| Sleeve | NZ$ |", "| --- | --- |",
              *[f"| {k} | {v:,.2f} |" for k, v in sorted(end["by_sleeve"].items())],
              f"| cash | {end['cash_nzd_total']:,.2f} |", ""]
    if flags:
        lines += ["## Limit flags", ""] + [f"- {d}: {f}" for d, f in flags] + [""]
    out = os.path.join(ROOT, "reports", name, "monthly")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, f"{month}.md"), "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
