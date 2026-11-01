"""History test 9g (rulebook): placement flippers.

Events from Norgate prices alone: an ordinary share that traded on each of the 20 sessions before a gap
of 1 to 3 sessions with no trades (a trading halt), then reopens at least 5% below its last close before
the gap on at least 3 times its median volume of the 60 sessions before the gap; no dividend or capital
event across the gap; at most one event per share in 60 sessions. Buy at the open E sessions after
reopening (an order rolls to the next session the share trades, up to 10 sessions, as in section 7),
sell at the open H sessions later; against the equal-weighted benchmark, after costs.
Tuning on 2010 to 2017 picks E (5 or 10) and H (20 or 40); the picked version runs once on 2018 onwards.
Writes reports/placement_history.md and a lock. Usage: python3 -I src/history/placement_test.py <repo_root> [--force]
"""
import bisect
import os
import statistics as stats
import sys
from collections import defaultdict
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from event_tools import Bench, asic, code_of, monthly_t, top_year_share, trimmed_mean  # noqa: E402
from universe import Universe, ready  # noqa: E402

VERSIONS = [(5, 20), (5, 40), (10, 20), (10, 40)]
TUNE_END = "2017-12-31"
TEST_FROM = "2018-01-01"
MIN_EVENTS = 100


def find_events(u: Universe, bench: Bench) -> list[dict]:
    ev = []
    n = len(u.dates)
    with np.errstate(all="ignore"):
        factor = u.tr / u.c
    for j, s in enumerate(u.symbols):
        if not bench.share[j]:
            continue
        has = ~np.isnan(u.c[:, j])
        idx = np.where(has)[0]
        if len(idx) < 81:
            continue
        last_event = -10_000
        # gaps between consecutive trading rows of this share
        for a, b in zip(idx[:-1], idx[1:]):
            gap = b - a - 1
            if not (1 <= gap <= 3) or a < 60:
                continue
            g = a + 1                                     # first session with no trade
            if not has[g - 20: g].all():
                continue
            R = b
            if R - last_event < 60:
                continue
            last = u.c[a, j]
            if not (u.o[R, j] <= 0.95 * last):
                continue
            med_v = np.nanmedian(u.v[g - 60: g, j])
            if not (med_v > 0 and u.v[R, j] >= 3 * med_v):
                continue
            if not (abs(factor[R, j] / factor[a, j] - 1) <= 0.01):
                continue
            last_event = R
            ev.append({"j": j, "sym": s, "gap_start": g, "R": R, "drop": float(1 - u.o[R, j] / last), "date": u.datestr[R]})
    return ev


def run(u: Universe, bench: Bench, events: list[dict], E: int, H: int, period: tuple[str, str]) -> tuple[list[dict], dict]:
    res, why = [], defaultdict(int)
    n = len(u.dates)
    for e in events:
        if not (period[0] <= e["date"] <= period[1]):
            continue
        j = e["j"]
        i_in = None
        for k in range(e["R"] + E, min(e["R"] + E + 10, n)):
            if np.isfinite(bench.tro[k, j]):
                i_in = k; break
        if i_in is None:
            why["no trade within 10 sessions of the entry day"] += 1; continue
        i_out = i_in + H
        if i_out >= n:
            why["holding period not over yet"] += 1; continue
        if not u.tradable(j, i_in):
            why["not tradable at entry (price or traded value)"] += 1; continue
        gross, i_sold, how = u.hold(j, i_in, i_out)
        if not np.isfinite(gross):
            why["no price to value the holding"] += 1; continue
        cost = u.round_trip_cost(j, i_in, i_sold)
        b = bench.ret(i_in, max(i_sold, i_in + 1))
        res.append({**e, "i_in": i_in, "i_out": i_sold, "gross": gross, "cost": cost, "bench": b, "vas": u.market(i_in, max(i_sold, i_in + 1)),
                    "result": gross - cost - b, "month": u.datestr[i_in][:7], "year": e["date"][:4], "how": how})
    return res, why


def main(root: str, force: bool = False) -> int:
    report = os.path.join(root, "reports", "placement_history.md")
    lock = report + ".lock"
    title = "# History test 9g: placement flippers\n\n"
    if os.path.exists(lock) and not force:
        print("result already written; use --force to re-run (the re-run is recorded)"); return 0
    if not ready(root):
        open(report, "w").write(title + "Waiting for the Norgate whole-market prices (data/norgate/universe/).\n")
        print("waiting for the universe"); return 0
    u = Universe(root)
    bench = Bench(u)
    events = find_events(u, bench)
    L = [title.strip(), "", f"Rulebook section 9g. Run {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC{' (forced re-run)' if force else ''}.", "",
         f"Events found from the price pattern, 2010 to now: {len(events):,}.", "",
         "## Tuning, 2010 to 2017 (all 4 versions)", "", "| Entry after reopening | Held | Events | Mean result after costs | Monthly t |", "| --- | --- | --- | --- | --- |"]
    tuned = []
    for E, H in VERSIONS:
        r, _ = run(u, bench, events, E, H, ("2010-01-01", TUNE_END))
        m = stats.mean(x["result"] for x in r) if r else float("nan")
        t, _ = monthly_t(r) if r else (float("nan"), 0)
        tuned.append((m, E, H))
        L.append(f"| {E} sessions | {H} sessions | {len(r)} | {m:+.2%} | {t:.2f} |")
    m_best, E, H = max((t for t in tuned if np.isfinite(t[0])), key=lambda t: t[0])
    L += ["", f"Picked: buy {E} sessions after reopening, hold {H} sessions.", "", "## Run once, 2018 onwards", ""]
    res, why = run(u, bench, events, E, H, (TEST_FROM, "2099-12-31"))
    passed = False
    if len(res) < MIN_EVENTS:
        L += [f"Only {len(res)} events; the test needs {MIN_EVENTS}. **Result: fail.**"]
    else:
        xs = [x["result"] for x in res]
        m = stats.mean(xs)
        t, months = monthly_t(res)
        tm = trimmed_mean(xs)
        ty = top_year_share(res)
        checks = [(f"At least {MIN_EVENTS} events", len(xs) >= MIN_EVENTS, f"{len(xs):,}"),
                  ("Mean after costs, against the equal-weighted benchmark, above zero with t of 2 or more (monthly)", m > 0 and t >= 2, f"{m:+.2%}, t {t:.2f} over {months} months"),
                  ("Still above zero without the best 5% of events", tm > 0, f"{tm:+.2%}"),
                  ("No single year more than half the total gain", ty <= 0.5, f"{ty:.0%}" if np.isfinite(ty) else "no total gain")]
        passed = all(c[1] for c in checks)
        L += ["| Measure | Value |", "| --- | --- |", f"| Events | {len(xs):,} |", f"| Mean gross return | {stats.mean(x['gross'] for x in res):+.2%} |",
              f"| Mean costs | {stats.mean(x['cost'] for x in res):.2%} |", f"| Mean equal-weighted benchmark, same days | {stats.mean(x['bench'] for x in res):+.2%} |",
              f"| Mean result after costs, less the benchmark | {m:+.2%} (median {stats.median(xs):+.2%}) |", f"| t-statistic (monthly) | {t:.2f} |",
              f"| Hit rate | {sum(1 for v in xs if v > 0) / len(xs):.0%} |",
              f"| Mean result against VAS instead (reported only) | {stats.mean(x['gross'] - x['cost'] - x['vas'] for x in res):+.2%} |", "",
              "| Year | Events | Mean result |", "| --- | --- | --- |"]
        by = defaultdict(list)
        for x in res:
            by[x["year"]].append(x["result"])
        for y in sorted(by):
            L.append(f"| {y} | {len(by[y])} | {stats.mean(by[y]):+.2%} |")
        L += ["", "| Drop on reopening (reported only) | Events | Mean result |", "| --- | --- | --- |"]
        for lab, lo, hi in (("5 to 15%", 0.05, 0.15), ("over 15%", 0.15, 9)):
            g = [x["result"] for x in res if lo <= x["drop"] < hi]
            L.append(f"| {lab} | {len(g)} | {stats.mean(g):+.2%} |" if g else f"| {lab} | 0 | |")
        L += ["", "| Pass mark | Met | Value |", "| --- | --- | --- |"] + [f"| {a} | {'yes' if b else 'no'} | {c} |" for a, b, c in checks]
        L += ["", f"**Result: {'pass' if passed else 'fail'}.**"]
        # reported only: how often ASIC's share count confirms a raising
        A = asic(root)
        if A:
            seen = conf = 0
            for x in res:
                rec = A.get(code_of(x["sym"]))
                if not rec:
                    continue
                d, _, issue = rec
                before = bisect.bisect_left(d, u.datestr[x["gap_start"]]) - 1
                after = bisect.bisect_right(d, u.datestr[min(x["R"] + 20, len(u.dates) - 1)]) - 1
                if before < 0 or after <= before or not (issue[before] > 0):
                    continue
                seen += 1
                conf += issue[after] >= 1.03 * issue[before]
            L += ["", f"Reported only: of {seen} events in shares that appear in ASIC's daily files, {conf} ({conf / seen:.0%}) had a share count at least 3% higher "
                      f"20 sessions after reopening, so most of those were raisings." if seen else "", ""]
        else:
            L += ["", "Reported only: ASIC's daily files were not in yet, so the raising check was not made."]
    L += ["", "Events left out of the run, by reason: " + ("; ".join(f"{k} {v}" for k, v in sorted(why.items())) or "none") + ".",
          "", "Caveats: events come from the price pattern, not the announcements, so some are bad news rather than a raising; the "
          "equal-weighted benchmark is every tradable share, so the result is these shares against small companies generally."]
    os.makedirs(os.path.dirname(report), exist_ok=True)
    open(report, "w").write("\n".join(L) + "\n")
    open(lock, "w").write(datetime.now(timezone.utc).isoformat())
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    sys.exit(main(a[0] if a else ".", "--force" in sys.argv))
