"""History test 9i (rulebook): short sellers covering.

ASIC's daily aggregated short positions (data/asic), each day's file known only from the fifth business
day after its date. ASIC codes are matched to the Norgate share trading on that code on that day.
At each month end, among tradable ordinary shares in ASIC's files whose short position was at least a set
share of shares on issue L sessions before the latest known file: the 10 with the largest fall in that share
since then are held in equal amounts for the month, bought at the next open and sold at the open after the
next month end. Only names entering or leaving are traded (brokerage and half the spread each way, plus the
hedge's 0.1% on entry). Result each month: the picks against the equal-weighted return of every tradable
share in ASIC's files over the same days.
Tuning on 2011 to 2017 picks the threshold (2% or 5%) and L (20 or 60 sessions); the picked version runs
once on 2018 onwards. Writes reports/short_cover_history.md and a lock.
Usage: python3 -I src/history/short_cover_test.py <repo_root> [--force]
"""
import csv
import os
import statistics as stats
import sys
from collections import defaultdict
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from event_tools import Bench, asic, code_of, top_year_share  # noqa: E402
from universe import FEE, HEDGE, Universe, ready  # noqa: E402

VERSIONS = [(0.02, 20), (0.02, 60), (0.05, 20), (0.05, 60)]
PICKS = 10
LAG = 5
NZ_ASX_TO_NZX = {"AIZ": "AIR", "MEZ": "MEL", "SNZ": "SUM"}


def short_matrix(u: Universe, A: dict) -> np.ndarray:
    """Share of shares on issue reported short, by Norgate row and column (NaN where ASIC has nothing)."""
    sp = np.full(u.c.shape, np.nan, dtype="float32")
    row = {d: i for i, d in enumerate(u.datestr)}
    by_code = defaultdict(list)
    for s in u.symbols:
        if u.is_share(s):
            by_code[code_of(s)].append(s)
    for code, (dates, short, issue) in A.items():
        cands = by_code.get(code)
        if not cands:
            continue
        spans = [(u.sec[s]["first"], u.sec[s]["last"], u.col[s]) for s in cands if s in u.sec]
        for d, sh, iss in zip(dates, short, issue):
            i = row.get(d)
            if i is None or not (iss > 0) or not (sh >= 0):
                continue
            for a, b, j in spans:
                if a <= d <= b:
                    sp[i, j] = sh / iss
                    break
    return sp


def latest(sp: np.ndarray, i: int, window: int = 5) -> np.ndarray:
    """For each column, the latest value at or before row i, looking back at most `window` rows."""
    blk = sp[max(0, i - window + 1): i + 1]
    out = np.full(sp.shape[1], np.nan, dtype="float32")
    for k in range(blk.shape[0]):
        r = blk[k]
        m = ~np.isnan(r)
        out[m] = r[m]
    return out


def month_ends(u: Universe) -> list[int]:
    return [i for i in range(len(u.dates) - 1) if u.datestr[i][:7] != u.datestr[i + 1][:7]]


def run(u: Universe, bench: Bench, sp: np.ndarray, thr: float, L: int, start: str, end: str) -> list[dict]:
    mes = month_ends(u)
    held, out = set(), []
    for k in range(len(mes) - 1):
        me, me_next = mes[k], mes[k + 1]
        if not (start <= u.datestr[me] <= end):
            continue
        i_in, i_out = me + 1, me_next + 1
        if i_out >= len(u.dates):
            break
        d = me - LAG
        now, then = latest(sp, d), latest(sp, d - L)
        in_file = ~np.isnan(now)
        elig = bench.eligible(i_in) & in_file
        fall = then - now
        cand = np.where(elig & (then >= thr) & (fall > 0))[0]
        picks = [int(j) for j in cand[np.argsort(-fall[cand])][:PICKS]]
        bmk = bench.ret(i_in, i_out, elig)
        if not picks:
            # nothing to hold: positions left are sold, the month is skipped
            held = set(); continue
        gross = []
        for j in picks:
            p0 = bench.tro[i_in, j]
            p1 = bench.tro[i_out, j] if np.isfinite(bench.tro[i_out, j]) else bench.tr_ff[i_out, j]
            gross.append(float(p1 / p0 - 1))
        new, gone = set(picks) - held, held - set(picks)
        cost = sum(FEE + u.half_spread(j, i_in) + HEDGE for j in new) + sum(FEE + u.half_spread(j, i_in) for j in gone)
        r = stats.mean(gross) - cost / len(picks)
        out.append({"month": u.datestr[me][:7], "year": u.datestr[me][:4], "picks": len(picks), "gross": stats.mean(gross), "cost": cost / len(picks),
                    "bench": bmk, "result": r - bmk, "names": [u.symbols[j] for j in picks], "turnover": len(new)})
        held = set(picks)
    return out


def tstat(xs: list[float]) -> float:
    return stats.mean(xs) / (stats.stdev(xs) / len(xs) ** 0.5) if len(xs) > 2 and stats.stdev(xs) > 0 else float("nan")


def main(root: str, force: bool = False) -> int:
    report = os.path.join(root, "reports", "short_cover_history.md")
    lock = report + ".lock"
    title = "# History test 9i: short sellers covering\n\n"
    if os.path.exists(lock) and not force:
        print("result already written; use --force to re-run (the re-run is recorded)"); return 0
    A = asic(root)
    if not ready(root) or not A:
        open(report, "w").write(title + "Waiting for the Norgate whole-market prices and ASIC's daily files.\n")
        print("waiting for data"); return 0
    u = Universe(root)
    bench = Bench(u)
    sp = short_matrix(u, A)
    L = [title.strip(), "", f"Rulebook section 9i. Run {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC{' (forced re-run)' if force else ''}.", "",
         f"ASIC daily files: {len(A):,} codes; matched to Norgate shares on {int(np.sum(~np.isnan(sp))):,} share-days.", "",
         "## Tuning, 2011 to 2017 (all 4 versions)", "", "| Short at least | Fall over | Months | Mean monthly result after costs | t |", "| --- | --- | --- | --- | --- |"]
    tuned = []
    for thr, lb in VERSIONS:
        r = run(u, bench, sp, thr, lb, "2011-01-01", "2017-12-31")
        xs = [x["result"] for x in r]
        m = stats.mean(xs) if xs else float("nan")
        tuned.append((m, thr, lb))
        L.append(f"| {thr:.0%} | {lb} sessions | {len(xs)} | {m:+.2%} | {tstat(xs):.2f} |")
    m_best, thr, lb = max((t for t in tuned if np.isfinite(t[0])), key=lambda t: t[0])
    L += ["", f"Picked: short at least {thr:.0%} of shares on issue {lb} sessions earlier.", "", "## Run once, 2018 onwards", ""]
    res = run(u, bench, sp, thr, lb, "2018-01-01", "2099-12-31")
    xs = [x["result"] for x in res]
    passed = False
    if len(xs) < 24:
        L += [f"Only {len(xs)} months; **Result: fail.**"]
    else:
        m, t = stats.mean(xs), tstat(xs)
        ahead = sum(1 for v in xs if v > 0) / len(xs)
        ty = top_year_share(res)
        checks = [("Mean monthly result after costs above zero with t of 2 or more", m > 0 and t >= 2, f"{m:+.2%} a month, t {t:.2f}"),
                  ("Ahead in at least 55% of months", ahead >= 0.55, f"{ahead:.0%} of {len(xs)}"),
                  ("No single year more than half the total gain", ty <= 0.5, f"{ty:.0%}" if np.isfinite(ty) else "no total gain")]
        passed = all(c[1] for c in checks)
        L += ["| Measure | Value |", "| --- | --- |", f"| Months | {len(xs)} ({res[0]['month']} to {res[-1]['month']}) |",
              f"| Mean picks a month | {stats.mean(x['picks'] for x in res):.1f} |", f"| Mean new names a month | {stats.mean(x['turnover'] for x in res):.1f} |",
              f"| Mean monthly return of the picks, before costs | {stats.mean(x['gross'] for x in res):+.2%} |", f"| Mean monthly costs | {stats.mean(x['cost'] for x in res):.2%} |",
              f"| Mean monthly benchmark | {stats.mean(x['bench'] for x in res):+.2%} |", f"| Mean monthly result after costs, less the benchmark | {m:+.2%} (median {stats.median(xs):+.2%}) |",
              f"| t-statistic | {t:.2f} |", "", "| Year | Months | Sum of results |", "| --- | --- | --- |"]
        by = defaultdict(list)
        for x in res:
            by[x["year"]].append(x["result"])
        for y in sorted(by):
            L.append(f"| {y} | {len(by[y])} | {sum(by[y]):+.2%} |")
        L += ["", "| Pass mark | Met | Value |", "| --- | --- | --- |"] + [f"| {a} | {'yes' if b else 'no'} | {c} |" for a, b, c in checks]
        L += ["", f"**Result: {'pass' if passed else 'fail'}.**"]
    # reported only: the same signal on New Zealand companies listed on both exchanges, against their NZX prices
    nz = [s for s in u.symbols if "NZX" in (u.sec.get(s, {}).get("name") or "").upper()]
    rows = []
    for me in month_ends(u):
        if u.datestr[me] < "2023-07-31" or me + 25 >= len(u.dates):
            continue
        now, then = latest(sp, me - LAG), latest(sp, me - LAG - lb)
        for s in nz:
            j = u.col[s]
            if np.isnan(now[j]) or np.isnan(then[j]) or then[j] < thr:
                continue
            code = NZ_ASX_TO_NZX.get(code_of(s), code_of(s))
            p = os.path.join(root, "data", "prices", "NZX", f"{code}.csv")
            if not os.path.exists(p):
                continue
            px = {r["date"]: float(r["close"]) for r in csv.DictReader(open(p)) if r["close"]}
            ds = sorted(px)
            a = [d for d in ds if d <= u.datestr[me]]
            b = [d for d in ds if d <= u.datestr[min(me + 21, len(u.dates) - 1)]]
            if a and b and b[-1] > a[-1]:
                rows.append((float(then[j] - now[j]) > 0, px[b[-1]] / px[a[-1]] - 1))
    if rows:
        cov = [r for f, r in rows if f]
        rest = [r for f, r in rows if not f]
        L += ["", f"Reported only, New Zealand companies on both exchanges since July 2023 (NZX prices, about a month ahead): {len(rows)} company-months "
                  f"with a short position of at least {thr:.0%}; where shorts fell, mean {stats.mean(cov):+.2%} ({len(cov)}); where they didn't, "
                  f"mean {stats.mean(rest):+.2%} ({len(rest)})." if cov and rest else ""]
    L += ["", "Caveats: ASIC's files cover only shares with reported short positions; the threshold and look-back were picked on 2011 to 2017, "
          "so the 2018 onwards run is the test."]
    os.makedirs(os.path.dirname(report), exist_ok=True)
    open(report, "w").write("\n".join(L) + "\n")
    open(lock, "w").write(datetime.now(timezone.utc).isoformat())
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    sys.exit(main(a[0] if a else ".", "--force" in sys.argv))
