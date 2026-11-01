"""History test 9m (rulebook): buying predicted S&P/ASX 200 and 300 additions before S&P announces them.

At each quarterly reference date (S&P's timetable, which changed in September 2021), rank every eligible ASX
ordinary share by its average market value over the 63 sessions to the reference date (close times the latest
ASIC share count). A non-member of the ASX 200 within the cut-off is a predicted ASX 200 addition; in March
and September, a non-member of the ASX 300 within its cut-off is a predicted ASX 300 addition. Buy at the open
after the reference date; sell at the first open after the announcement, or at the open of the third Friday.
Against the equal-weighted return of the shares ranked 101st to 400th, after costs.
Tuning on 2011 to 2017 rebalances picks the cut-offs and the exit; the picked version runs once on 2018 to
September 2026. Writes reports/index_additions_history.md and a lock.
Usage: python3 -I src/history/index_test.py <repo_root> [--force]
"""
import calendar
import csv
import math
import os
import statistics as stats
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from event_tools import Bench, asic, code_of, top_year_share, trimmed_mean  # noqa: E402
from failed_deal_test import deal_symbol  # noqa: E402
from universe import Universe, ready  # noqa: E402

VERSIONS = [(r2, r3, ex) for r2 in (160, 179) for r3 in (260, 274) for ex in ("after announcement", "third Friday")]
TUNE = (2011, 2017)
TEST = (2018, 2026)
LAST_REBALANCE = "2026-09"
WINDOW, MIN_DAYS = 63, 40
MIN_TRADES = 60


def fridays(y: int, m: int) -> list[date]:
    return [date(y, m, d) for d in range(1, calendar.monthrange(y, m)[1] + 1) if date(y, m, d).weekday() == 4]


def schedule(y: int, m: int) -> dict:
    """S&P's reference date, announcement date and last session before the change takes effect."""
    py, pm = (y, m - 1) if m > 1 else (y - 1, 12)
    prev = fridays(py, pm)
    if (y, m) >= (2021, 9):
        ref, ann = prev[-2], fridays(y, m)[0]
    elif m == 9:
        ref, ann = prev[-2], fridays(y, m)[0]
    else:
        ref, ann = prev[-1], fridays(y, m)[1]
    return {"month": f"{y}-{m:02d}", "ref": ref.isoformat(), "ann": ann.isoformat(), "third": fridays(y, m)[2].isoformat()}


class Members:
    def __init__(self, root: str):
        d = os.path.join(root, "data", "norgate")
        self.start = {}
        for r in csv.DictReader(open(os.path.join(d, "index_members.csv"), encoding="utf-8")):
            self.start[(r["index"], r["symbol"])] = (r["first_date"][:10], int(r["member_at_first"]), r["last_date"][:10])
        self.ev = defaultdict(list)
        for r in csv.DictReader(open(os.path.join(d, "index_changes.csv"), encoding="utf-8")):
            self.ev[(r["index"], r["symbol"])].append((r["date"][:10], 1 if r["change"] == "joined" else 0))
        for k in self.ev:
            self.ev[k] = sorted(set(self.ev[k]))

    def member(self, idx: str, sym: str, d: str) -> int | None:
        st = self.start.get((idx, sym))
        if not st:
            return None
        first, v, last = st
        if d < first or d > last:
            return 0
        for when, val in self.ev.get((idx, sym), []):
            if when <= d:
                v = val
        return v

    def joined(self, idx: str, sym: str, lo: str, hi: str) -> bool:
        return any(v == 1 and lo <= when <= hi for when, v in self.ev.get((idx, sym), []))


def issue_matrix(u: Universe, A: dict) -> np.ndarray:
    """Shares on issue by Norgate row and column, carried forward at most 21 sessions from the latest ASIC file."""
    m = np.full(u.c.shape, np.nan, dtype="float64")
    row = {d: i for i, d in enumerate(u.datestr)}
    by_code = defaultdict(list)
    for s in u.symbols:
        by_code[code_of(s)].append(s)
    for code, (dates, _, issue) in A.items():
        spans = [(u.sec[s]["first"], u.sec[s]["last"], u.col[s]) for s in by_code.get(code, []) if s in u.sec]
        for d, iss in zip(dates, issue):
            i = row.get(d)
            if i is None or not (iss > 0):
                continue
            for a, b, j in spans:
                if a <= d <= b:
                    m[i, j] = iss
                    break
    out = m.copy()
    age = np.where(np.isnan(m), np.inf, 0.0)
    for i in range(1, m.shape[0]):
        carry = np.isnan(out[i]) & (age[i - 1] < 21)
        out[i, carry] = out[i - 1, carry]
        age[i] = np.where(np.isnan(m[i]), age[i - 1] + 1, 0.0)
    return out


def main(root: str, force: bool = False) -> int:
    report = os.path.join(root, "reports", "index_additions_history.md")
    lock = report + ".lock"
    title = "# History test 9m: buying predicted index additions before S&P announces them\n\n"
    if os.path.exists(lock) and not force:
        print("result already written; use --force to re-run (the re-run is recorded)"); return 0
    if not ready(root) or not os.path.exists(os.path.join(root, "data", "norgate", "index_members.csv")):
        open(report, "w").write(title + "Waiting for Norgate's index membership file (data/norgate/index_members.csv).\n")
        print("waiting for the membership file"); return 0
    u = Universe(root)
    bench = Bench(u)
    M = Members(root)
    A = asic(root)
    shares = issue_matrix(u, A)
    with np.errstate(all="ignore"):
        mv = u.c * shares
    names = {s: (u.sec.get(s, {}).get("name") or "").upper() for s in u.symbols}
    elig = np.array([bench.share[j] and "FOREIGN EXEMPT" not in names[s] for j, s in enumerate(u.symbols)])
    # live deal targets at a date (S&P leaves out companies in an acquisition)
    find = deal_symbol(root, u)
    live = defaultdict(list)
    for r in csv.DictReader(open(os.path.join(root, "deals", "all_deals.csv"), encoding="utf-8")):
        if r["market"] == "ASX" and r.get("target_ticker") and r.get("announce_date"):
            s = find(r["target_ticker"].upper(), r["announce_date"][:10])
            if s:
                live[s].append((r["announce_date"][:10], (r.get("outcome_date") or "9999")[:10]))
    rebs = []
    for y in range(TUNE[0], TEST[1] + 1):
        for m in (3, 6, 9, 12):
            sc = schedule(y, m)
            if sc["month"] > LAST_REBALANCE:
                continue
            i_ref = u.row_on_or_before(sc["ref"])
            if i_ref is None or i_ref < WINDOW:
                continue
            win = mv[i_ref - WINDOW + 1: i_ref + 1]
            cnt = np.sum(~np.isnan(win), axis=0)
            with np.errstate(all="ignore"):
                avg = np.where(cnt >= MIN_DAYS, np.nanmean(win, axis=0), np.nan)
            ok = elig & np.isfinite(avg) & ~np.isnan(u.c[i_ref])
            for s, spans in live.items():
                j = u.col.get(s)
                if j is not None and any(a <= sc["ref"] < b for a, b in spans):
                    ok[j] = False
            cols = np.where(ok)[0]
            order = cols[np.argsort(-avg[cols])]
            rank = {int(j): k + 1 for k, j in enumerate(order)}
            mid = np.zeros(len(u.symbols), dtype=bool)
            mid[order[100:400]] = True
            rebs.append({**sc, "i_ref": i_ref, "rank": rank, "mid": mid, "year": y, "m": m})


    def run(r2: int, r3: int, ex: str, lo: int, hi: int) -> tuple[list[dict], dict]:
        out, why = [], defaultdict(int)
        for rb in rebs:
            if not (lo <= rb["year"] <= hi):
                continue
            i_in = rb["i_ref"] + 1
            i_out = u.row_after(rb["ann"]) if ex == "after announcement" else u.row_on_or_before(rb["third"])
            if i_out is None or i_out <= i_in:
                why["exit not after entry"] += 1; continue
            picks = {}
            for j, k in rb["rank"].items():
                s = u.symbols[j]
                if k <= r2 and M.member("S&P/ASX 200", s, rb["ref"]) == 0:
                    picks[j] = "ASX 200"
                elif rb["m"] in (3, 9) and k <= r3 and M.member("S&P/ASX 300", s, rb["ref"]) == 0:
                    picks[j] = "ASX 300"
            b = bench.ret(i_in, i_out, rb["mid"])
            for j, idx in picks.items():
                s = u.symbols[j]
                if not np.isfinite(bench.tro[i_in, j]):
                    why["no trade on the entry day"] += 1; continue
                if not u.tradable(j, i_in):
                    why["not tradable at entry"] += 1; continue
                gross, i_sold, how = u.hold(j, i_in, i_out)
                if not np.isfinite(gross):
                    why["no price to value"] += 1; continue
                cost = u.round_trip_cost(j, i_in, i_sold)
                hit = M.joined(f"S&P/{idx}" if not idx.startswith("S&P") else idx, s, rb["ann"], (date.fromisoformat(rb["third"]) + timedelta(days=10)).isoformat())
                out.append({"sym": s, "reb": rb["month"], "year": str(rb["year"]), "index": idx, "rank": rb["rank"][j], "gross": gross, "cost": cost,
                            "bench": b, "vas": u.market(i_in, i_out), "result": gross - cost - b, "hit": hit})
        return out, why

    def per_reb_t(res: list[dict]) -> tuple[float, int]:
        by = defaultdict(list)
        for x in res:
            by[x["reb"]].append(x["result"])
        ms = [stats.mean(v) for v in by.values()]
        if len(ms) < 3 or stats.stdev(ms) == 0:
            return float("nan"), len(ms)
        return stats.mean(ms) / (stats.stdev(ms) / math.sqrt(len(ms))), len(ms)
    L = [title.strip(), "", f"Rulebook section 9m. Run {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC{' (forced re-run)' if force else ''}.", "",
         f"Rebalances ranked: {len(rebs)} ({rebs[0]['month']} to {rebs[-1]['month']}).", "",
         "## Tuning, 2011 to 2017 (all 8 versions)", "",
         "| ASX 200 cut-off | ASX 300 cut-off | Exit | Trades | Mean result after costs | t (by rebalance) | Added by S&P |", "| --- | --- | --- | --- | --- | --- | --- |"]
    tuned = []
    for r2, r3, ex in VERSIONS:
        r, _ = run(r2, r3, ex, *TUNE)
        m = stats.mean(x["result"] for x in r) if r else float("nan")
        t, _ = per_reb_t(r) if r else (float("nan"), 0)
        hit = sum(x["hit"] for x in r) / len(r) if r else float("nan")
        tuned.append((m, r2, r3, ex))
        L.append(f"| {r2} | {r3} | {ex} | {len(r)} | {m:+.2%} | {t:.2f} | {hit:.0%} |")
    m_best, r2, r3, ex = max((x for x in tuned if np.isfinite(x[0])), key=lambda x: x[0])
    L += ["", f"Picked: ASX 200 cut-off {r2}, ASX 300 cut-off {r3}, exit {ex}.", "", "## Run once, 2018 to September 2026", ""]
    res, why = run(r2, r3, ex, *TEST)
    passed = False
    if len(res) < MIN_TRADES:
        L += [f"Only {len(res)} trades; the test needs {MIN_TRADES}. **Result: fail.**"]
        if res:
            L += ["", f"Reported only: mean result {stats.mean(x['result'] for x in res):+.2%} across those {len(res)}."]
    else:
        xs = [x["result"] for x in res]
        m = stats.mean(xs)
        t, n_reb = per_reb_t(res)
        tm = trimmed_mean(xs)
        ty = top_year_share(res)
        checks = [(f"At least {MIN_TRADES} trades", True, str(len(xs))),
                  ("Mean after costs, against mid-sized shares, above zero with t of 2 or more (by rebalance)", m > 0 and t >= 2, f"{m:+.2%}, t {t:.2f} over {n_reb} rebalances"),
                  ("Still above zero without the best 5% of trades", tm > 0, f"{tm:+.2%}"),
                  ("No single year more than half the total gain", ty <= 0.5, f"{ty:.0%}" if np.isfinite(ty) else "no total gain")]
        passed = all(c[1] for c in checks)
        L += ["| Measure | Value |", "| --- | --- |", f"| Trades | {len(xs)} |", f"| Mean gross return | {stats.mean(x['gross'] for x in res):+.2%} |",
              f"| Mean costs | {stats.mean(x['cost'] for x in res):.2%} |", f"| Mean benchmark (shares ranked 101 to 400) | {stats.mean(x['bench'] for x in res):+.2%} |",
              f"| Mean result after costs, less the benchmark | {m:+.2%} (median {stats.median(xs):+.2%}) |", f"| t-statistic (by rebalance) | {t:.2f} |",
              f"| Predictions S&P added at that rebalance (reported only) | {sum(x['hit'] for x in res)} of {len(res)} |",
              f"| Against VAS instead (reported only) | {stats.mean(x['gross'] - x['cost'] - x['vas'] for x in res):+.2%} |", ""]
        by = defaultdict(list)
        for x in res:
            by[x["year"]].append(x["result"])
        L += ["| Year | Trades | Mean result |", "| --- | --- | --- |"] + [f"| {y} | {len(v)} | {stats.mean(v):+.2%} |" for y, v in sorted(by.items())]
        L += ["", "| Pass mark | Met | Value |", "| --- | --- | --- |"] + [f"| {a} | {'yes' if b else 'no'} | {c} |" for a, b, c in checks]
        L += ["", f"**Result: {'pass' if passed else 'fail'}.**", ""]
        for idx in ("ASX 200", "ASX 300"):
            g = [x for x in res if x["index"] == idx]
            if g:
                L.append(f"- Reported only, predicted {idx} additions: {len(g)} trades, mean {stats.mean(x['result'] for x in g):+.2%}, added by S&P {sum(x['hit'] for x in g)}")
        hits = [x["result"] for x in res if x["hit"]]
        miss = [x["result"] for x in res if not x["hit"]]
        if hits and miss:
            L.append(f"- Reported only, predictions S&P added: mean {stats.mean(hits):+.2%}; predictions it didn't: mean {stats.mean(miss):+.2%}")
    L += ["", "Left out, by reason: " + ("; ".join(f"{k} {v}" for k, v in sorted(why.items())) or "none") + ".",
          "", "Caveats: ranks use full market value from ASIC's share counts, not S&P's free-float figures, and no liquidity screen; shares not in "
          "ASIC's files can't be ranked; trades in the same rebalance move together, so the t-statistic is worked out by rebalance."]
    os.makedirs(os.path.dirname(report), exist_ok=True)
    open(report, "w").write("\n".join(L) + "\n")
    open(lock, "w").write(datetime.now(timezone.utc).isoformat())
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    sys.exit(main(a[0] if a else ".", "--force" in sys.argv))
