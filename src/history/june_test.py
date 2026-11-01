"""History test 9f (rulebook): the June tax-year sell-off.

Each year, on the ranking date, the tradable ASX shares (Norgate universe, ETFs left out by name) with
the lowest total return since the previous 1 July (at least 200 sessions of prices in that span): the
bottom 10%, up to 20 shares. Bought at the next open, sold at the close on the exit date, after costs.
The benchmark is the equal-weighted return of every tradable share over the same days.
Tuning on 2010 to 2017 picks the ranking date (15 June or the last session of June) and the exit (the
last session of July or of August); the picked version runs once on 2018 to 2026.
Writes reports/june_selloff_history.md and a lock. Usage: python3 -I src/history/june_test.py <repo_root> [--force]
"""
import os
import statistics as stats
import sys
from collections import defaultdict
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from universe import FEE, HEDGE, MIN_PRICE, MIN_VALUE, Universe, ready  # noqa: E402

VERSIONS = [("15 June", "end of July"), ("15 June", "end of August"), ("end of June", "end of July"), ("end of June", "end of August")]
TUNE = range(2010, 2018)
TEST = range(2018, 2027)
MAX_PICKS = 20


def last_session_of_month(u: Universe, y: int, m: int) -> int | None:
    pre = f"{y}-{m:02d}"
    rows = [i for i, d in enumerate(u.datestr) if d.startswith(pre)]
    return rows[-1] if rows else None


def ranking_row(u: Universe, y: int, when: str) -> int | None:
    return u.row_on_or_before(f"{y}-06-15") if when == "15 June" else last_session_of_month(u, y, 6)


def one_year(u: Universe, y: int, when: str, exit_: str, frac: float = 0.10, cap: int | None = MAX_PICKS) -> dict | None:
    r = ranking_row(u, y, when)
    start = u.row_on_or_before(f"{y - 1}-06-30")
    out = last_session_of_month(u, y, 7 if exit_ == "end of July" else 8)
    if r is None or start is None or out is None or r + 1 >= len(u.dates) or out <= r + 1:
        return None
    i_in = r + 1
    tr, c = u.tr, u.c
    with np.errstate(all="ignore"):
        n = np.sum(~np.isnan(c[start: r + 1]), axis=0)
        medv = np.nanmedian(u.value[max(0, i_in - 60): i_in], axis=0)
        ok = (n >= 200) & (c[r] >= MIN_PRICE) & (medv >= MIN_VALUE) & ~np.isnan(tr[start]) & ~np.isnan(u.o[i_in])
    ok &= np.array([u.is_share(s) for s in u.symbols])
    cols = np.where(ok)[0]
    if len(cols) < 50:
        return None
    fy = tr[r, cols] / tr[start, cols] - 1
    order = np.argsort(fy)
    k = max(1, int(round(frac * len(cols))))
    if cap:
        k = min(k, cap)
    picks = [int(cols[o]) for o in order[:k]]

    def ret(j: int) -> float:
        p0 = u.tr_open(j, i_in)
        if not np.isnan(c[out, j]):
            return float(tr[out, j] / p0 - 1)
        last = u.last_row(j, out)
        return float(tr[last, j] / p0 - 1)
    bench = stats.mean(ret(int(j)) for j in cols)
    after = [ret(j) - (2 * FEE + u.half_spread(j, i_in) + u.half_spread(j, out) + HEDGE) for j in picks]
    return {"year": y, "picks": len(picks), "universe": len(cols), "mean_after_costs": stats.mean(after), "bench": bench,
            "result": stats.mean(after) - bench, "names": [u.symbols[j] for j in picks]}


def main(root: str, force: bool = False) -> int:
    report = os.path.join(root, "reports", "june_selloff_history.md")
    lock = report + ".lock"
    title = "# History test 9f: the June tax-year sell-off\n\n"
    if os.path.exists(lock) and not force:
        print("result already written; use --force to re-run (the re-run is recorded)"); return 0
    if not ready(root):
        open(report, "w").write(title + "Waiting for the Norgate whole-market prices (data/norgate/universe/).\n")
        print("waiting for the universe"); return 0
    u = Universe(root)
    L = [title.strip(), "", f"Rulebook section 9f. Run {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC{' (forced re-run)' if force else ''}.", "",
         "## Tuning, 2010 to 2017 (all 4 versions)", "", "| Rank and buy | Sell | Years | Mean yearly result after costs | Years ahead |", "| --- | --- | --- | --- | --- |"]
    tuned = []
    for when, exit_ in VERSIONS:
        ys = [one_year(u, y, when, exit_) for y in TUNE]
        ys = [x for x in ys if x]
        m = stats.mean(x["result"] for x in ys) if ys else float("nan")
        tuned.append((m, when, exit_, ys))
        L.append(f"| {when} | {exit_} | {len(ys)} | {m:+.2%} | {sum(1 for x in ys if x['result'] > 0)} of {len(ys)} |")
    tuned = [t for t in tuned if t[3]]
    m_best, when, exit_, _ = max(tuned, key=lambda t: t[0])
    L += ["", f"Picked: rank and buy on {when}, sell at the {exit_}.", "", "## Run once, 2018 to 2026", "",
          "| Year | Shares picked | Universe | Picks after costs | Benchmark | Result |", "| --- | --- | --- | --- | --- | --- |"]
    res = [x for x in (one_year(u, y, when, exit_) for y in TEST) if x]
    for x in res:
        L.append(f"| {x['year']} | {x['picks']} | {x['universe']} | {x['mean_after_costs']:+.2%} | {x['bench']:+.2%} | {x['result']:+.2%} |")
    passed = False
    if len(res) < 6:
        L += ["", f"Only {len(res)} years to test. **Result: not run.**"]
    else:
        xs = [x["result"] for x in res]
        m = stats.mean(xs)
        total = sum(xs)
        top = max(xs) / total if total > 0 else float("inf")
        checks = [(f"Picks beat the benchmark after costs in at least 6 of the {len(xs)} years", sum(1 for v in xs if v > 0) >= 6, f"{sum(1 for v in xs if v > 0)} of {len(xs)}"),
                  ("Mean yearly result above 2%", m > 0.02, f"{m:+.2%}"),
                  ("No single year more than half the total gain", total > 0 and top <= 0.5, f"{top:.0%}" if total > 0 else "no total gain")]
        passed = all(c[1] for c in checks)
        L += ["", "| Pass mark | Met | Value |", "| --- | --- | --- |"] + [f"| {a} | {'yes' if b else 'no'} | {c} |" for a, b, c in checks]
        L += ["", f"**Result: {'pass' if passed else 'fail'}.**"]
        for label, frac, cap in (("bottom 5%, up to 20", 0.05, MAX_PICKS), ("bottom 10%, no cap", 0.10, None)):
            alt = [x for x in (one_year(u, y, when, exit_, frac, cap) for y in TEST) if x]
            if alt:
                L += ["", f"Reported only, {label}: mean yearly result {stats.mean(x['result'] for x in alt):+.2%}, "
                          f"ahead in {sum(1 for x in alt if x['result'] > 0)} of {len(alt)} years."]
    L += ["", "Caveats: the benchmark is every tradable share equally weighted, so the result is the losers against small "
          "shares generally; years with few tradable losers weigh as much as years with many."]
    os.makedirs(os.path.dirname(report), exist_ok=True)
    open(report, "w").write("\n".join(L) + "\n")
    if not any("Result: not run" in x for x in L):
        open(lock, "w").write(datetime.now(timezone.utc).isoformat())
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    sys.exit(main(a[0] if a else ".", "--force" in sys.argv))
