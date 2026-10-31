"""Success tests 2 and 3 (rulebook section 10): the passive comparisons.

Test 3, the core's index mix held at 100%: the core's lines at their weights scaled to 100%
(VT 50%, VAS 25%, ENZL 25%), bought at the start and held, valued in NZ$ with dividends
reinvested, no trading costs. Each date uses the closes the portfolio could see at its 9pm NZ
valuation (so a US session is counted the night after it closes, as in the portfolio). Dividends
are the ones entered in the ledger (not voided), the same payments the portfolio is paid, so the
two sides count the same dividends.

Test 2, an index-and-cash mix with the same ups and downs: a share b of that index mix and 1 - b
in cash at the run's cash rate, with b set so the mix's daily swings (standard deviation of daily
returns) match the portfolio's over the same days. Rebalanced daily, no costs.

The portfolio passes test 2 if it ends ahead of the matched mix.
Usage: python3 -I src/benchmarks.py <ledger_name>
"""
import csv
import json
import math
import os
import statistics as stats
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ledger import Ledger  # noqa: E402
from market_data import CURRENCY, FX, closed_by, nz_evening_utc  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def total_return(data_dir: str, market: str, ticker: str, ledger_divs: dict) -> list[tuple[str, float]]:
    """(session date, total-return index) from unadjusted closes plus dividends on their ex-dates."""
    rows = []
    with open(os.path.join(data_dir, "prices", market, f"{ticker}.csv"), newline="") as f:
        for r in csv.DictReader(f):
            try:
                c = float(r["close"])
            except (TypeError, ValueError):
                continue
            rows.append((r["date"], c, ledger_divs.get(r["date"], 0.0)))
    out, idx, prev = [], 1.0, None
    for d, c, div in sorted(rows):
        if prev:
            idx *= (c + div) / prev
        out.append((d, idx))
        prev = c
    return out


def seen_at(series: list, market: str, d: str) -> float | None:
    """The index at the last session final by the 9pm NZ valuation on date d."""
    as_of = nz_evening_utc(d)
    vals = [v for k, v in series if closed_by(market, k, as_of)]
    return vals[-1] if vals else None


def index_mix(cfg: dict, data_dir: str, fx: FX, dates: list[str], L: Ledger | None = None) -> list[float]:
    """Value of NZ$1 put into the core's index mix on dates[0]."""
    lines = cfg["core"]["lines"]
    total_w = sum(x["weight"] for x in lines)
    divs = {}
    recs = L.records("corporate_actions") if L is not None else []
    voided = {r["payload"]["ref"] for r in recs if r["payload"].get("type") == "void"}
    for r in recs:
        p = r["payload"]
        if p.get("type") == "dividend" and p.get("ex_date") and r["seq"] not in voided:
            divs.setdefault((p["market"], p["ticker"]), {})[p["ex_date"]] = float(p["per_share"])
    series = {}
    for x in lines:
        key = (x["market"], x["ticker"])
        series[key] = total_return(data_dir, x["market"], x["ticker"], divs.get(key, {}))
    out = []
    for d in dates:
        v = 0.0
        for x in lines:
            s = series[(x["market"], x["ticker"])]
            p0, p = seen_at(s, x["market"], dates[0]), seen_at(s, x["market"], d)
            if p0 is None or p is None:
                return []
            ccy = CURRENCY[x["market"]]
            v += x["weight"] / total_w * (p * fx.nzd_per(ccy, d)) / (p0 * fx.nzd_per(ccy, dates[0]))
        out.append(v)
    return out


def matched_mix(port: list[float], idx: list[float], dates: list[str], cash_rate: float) -> tuple[float, list[float]]:
    pr = [b / a - 1 for a, b in zip(port, port[1:])]
    ir = [b / a - 1 for a, b in zip(idx, idx[1:])]
    if len(pr) < 2 or stats.pstdev(ir) == 0:
        return 1.0, idx
    b = min(1.0, stats.pstdev(pr) / stats.pstdev(ir))
    out = [1.0]
    from datetime import date
    for k, r in enumerate(ir):
        days = (date.fromisoformat(dates[k + 1]) - date.fromisoformat(dates[k])).days
        out.append(out[-1] * (1 + b * r + (1 - b) * cash_rate * days / 365))
    return b, out


def main(name: str) -> int:
    cfg = json.load(open(os.path.join(ROOT, "config", "run.json")))
    data_dir = os.path.join(ROOT, "data")
    L = Ledger(os.path.join(ROOT, cfg["ledgers"][name]["dir"]))
    vals = [r["payload"] for r in L.records("valuations")]
    if len(vals) < 2:
        print("not enough valuations yet")
        return 0
    dates = [v["date"] for v in vals]
    port = [v["total_nzd"] / vals[0]["total_nzd"] for v in vals]
    fx = FX(data_dir)
    idx = index_mix(cfg, data_dir, fx, dates, L)
    if not idx:
        print("index prices missing")
        return 0
    rates = [r["payload"]["rate"] for r in L.records("cash") if r["payload"]["kind"] == "interest"]
    cash_rate = stats.mean(rates) if rates else 0.0
    b, mix = matched_mix(port, idx, dates, cash_rate)

    def dd(xs):
        peak, worst = xs[0], 0.0
        for x in xs:
            peak = max(peak, x); worst = min(worst, x / peak - 1)
        return worst
    pr = [b2 / a - 1 for a, b2 in zip(port, port[1:])]
    out = {"ledger": name, "from": dates[0], "to": dates[-1], "portfolio": port[-1] - 1, "index_mix": idx[-1] - 1,
           "matched_share_in_index": b, "matched_mix": mix[-1] - 1, "cash_rate": cash_rate,
           "portfolio_daily_sd": stats.pstdev(pr) if len(pr) > 1 else 0.0, "portfolio_worst_fall": dd(port),
           "index_worst_fall": dd(idx), "test2_ahead_of_matched_mix": port[-1] > mix[-1],
           "test3_vs_index_mix": port[-1] - idx[-1]}
    os.makedirs(os.path.join(ROOT, "reports", name), exist_ok=True)
    json.dump(out, open(os.path.join(ROOT, "reports", name, "benchmarks.json"), "w"), indent=1)
    lines = [f"# {name}: passive comparisons, {dates[0]} to {dates[-1]}", "",
             "| Measure | Value |", "| --- | --- |",
             f"| Portfolio | {out['portfolio']:+.2%} |",
             f"| Core index mix held at 100% (test 3) | {out['index_mix']:+.2%} |",
             f"| Index-and-cash mix with the same daily swings (test 2): {b:.0%} index, {1 - b:.0%} cash | {out['matched_mix']:+.2%} |",
             f"| Portfolio worst fall from peak | {out['portfolio_worst_fall']:.2%} |",
             f"| Index mix worst fall from peak | {out['index_worst_fall']:.2%} |",
             f"| Test 2 met so far | {'yes' if out['test2_ahead_of_matched_mix'] else 'no'} |"]
    open(os.path.join(ROOT, "reports", name, "benchmarks.md"), "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "dryrun"))
