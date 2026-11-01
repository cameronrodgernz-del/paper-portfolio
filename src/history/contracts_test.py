"""History test 9l (rulebook): government contracts and ASX small companies.

Events: AusTender contract notices (data/austender/contracts_YYYY.csv.gz), and amendments that raise a
contract's value (counted at the rise), matched to an ASX-listed company (data/austender/matched.csv: high
confidence, or medium and checked by hand), whose ordinary shares traded on the publication date, worth at
least 5% of the company's market value at the close before publication. Notices published the same day
are added together. Market value: that close times the shares on issue from ASIC's daily files (latest
within 30 days), else EODHD's reported shares outstanding (data/austender/shares_eodhd.csv, latest earlier
date); a company with neither is left out and counted. A company's notices within 20 sessions after an
event are part of that event.
Buy at the open of the first session after publication, hold H sessions, against the equal-weighted
benchmark (shared terms for 9g to 9j), after costs, the share passing the tradable test on entry.
Tuning on events published 2013 to 2018 picks H (20 or 60); the picked version runs once on events from 2019.
Writes reports/contracts_history.md and a lock. Usage: python3 -I src/history/contracts_test.py <repo_root> [--force]
"""
import bisect
import csv
import glob
import gzip
import os
import statistics as stats
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from event_tools import Bench, asic, code_of, monthly_t, top_year_share, trimmed_mean  # noqa: E402
from universe import Universe, ready  # noqa: E402

HOLDS = [20, 60]
TUNE_END, TEST_FROM = "2018-12-31", "2019-01-01"
MIN_SHARE = 0.05
MIN_EVENTS = 40
MERGE = 20


def fnum(x) -> float | None:
    try:
        v = float(str(x).replace(",", "").replace("$", "").strip())
        return v if v == v else None
    except (TypeError, ValueError):
        return None


def contracts(root: str) -> dict:
    """cn_id -> (parent, amendment, value, publish_date) for every notice, to work out amendment rises."""
    out = {}
    for p in sorted(glob.glob(os.path.join(root, "data", "austender", "contracts_*.csv.gz"))):
        with gzip.open(p, "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                key = (r.get("cn_id") or "").strip()
                if key:
                    out.setdefault(key, []).append(((r.get("parent_cn_id") or "").strip(), (r.get("amendment") or "").strip(),
                                                    fnum(r.get("value_aud")), (r.get("publish_date") or "")[:10]))
    return out


def notice_value(row: dict, C: dict) -> float | None:
    """A new notice counts at its value; an amendment at the rise over the latest earlier value of its contract."""
    v = fnum(row.get("value_aud"))
    if v is None:
        return None
    cid = (row.get("cn_id") or "").strip()
    recs = C.get(cid, [])
    rec = next((x for x in recs if x[3] == row["publish_date"][:10] and x[2] == v), recs[0] if recs else None)
    amend = rec and (rec[1] not in ("", "0", "N", "n", "False", "false") or (rec[0] and rec[0] != cid))
    if not amend:
        return v
    parent = rec[0] or cid.split("-A")[0]
    earlier = [x for x in C.get(parent, []) + [y for y in recs if y is not rec] if x[3] and x[3] < row["publish_date"][:10] and x[2] is not None]
    if not earlier:
        return None
    prev = sorted(earlier, key=lambda x: x[3])[-1][2]
    return v - prev if v > prev else None


def shares_eodhd(root: str) -> dict:
    p = os.path.join(root, "data", "austender", "shares_eodhd.csv")
    out = defaultdict(list)
    if os.path.exists(p):
        for r in csv.DictReader(open(p, encoding="utf-8")):
            v = fnum(r.get("shares"))
            if v and r.get("date"):
                out[r["symbol"]].append((r["date"][:10], v))
    return {k: sorted(v) for k, v in out.items()}


def main(root: str, force: bool = False) -> int:
    report = os.path.join(root, "reports", "contracts_history.md")
    lock = report + ".lock"
    title = "# History test 9l: government contracts and ASX small companies\n\n"
    if os.path.exists(lock) and not force:
        print("result already written; use --force to re-run (the re-run is recorded)"); return 0
    mp = os.path.join(root, "data", "austender", "matched.csv")
    if not ready(root) or not os.path.exists(mp):
        open(report, "w").write(title + "Waiting for the AusTender matches (data/austender/matched.csv).\n")
        print("waiting for data"); return 0
    u = Universe(root)
    bench = Bench(u)
    A = asic(root)
    E = shares_eodhd(root)
    C = contracts(root)
    why = defaultdict(int)
    cands = defaultdict(float)                 # (symbol, publish_date) -> value
    for r in csv.DictReader(open(mp, encoding="utf-8")):
        conf, checked = (r.get("confidence") or "").lower(), (r.get("checked") or "").strip().lower()
        if not (conf == "high" or (conf == "medium" and checked in ("y", "yes", "true", "1"))):
            why["match not high confidence or not checked"] += 1; continue
        if r.get("symbol") not in u.col:
            why["matched symbol not in Norgate"] += 1; continue
        v = notice_value(r, C)
        if v is None or v <= 0:
            why["amendment with no rise, or no value"] += 1; continue
        cands[(r["symbol"], r["publish_date"][:10])] += v
    events, last_event = [], {}
    for (sym, pd), v in sorted(cands.items(), key=lambda x: (x[0][1], x[0][0])):
        j = u.col[sym]
        if not bench.share[j]:
            why["not an ordinary share"] += 1; continue
        i_in = u.row_after(pd)
        prev = u.row_on_or_before((date.fromisoformat(pd) - timedelta(days=1)).isoformat())
        if i_in is None or prev is None or np.isnan(u.c[prev, j]):
            why["no trading around publication"] += 1; continue
        if sym in last_event and i_in - last_event[sym] <= MERGE:
            continue                                   # part of the earlier event
        close = float(u.c[prev, j])
        shares = None
        rec = A.get(code_of(sym))
        if rec:
            d, _, issue = rec
            k = bisect.bisect_right(d, u.datestr[prev]) - 1
            if k >= 0 and (date.fromisoformat(u.datestr[prev]) - date.fromisoformat(d[k])).days <= 30 and issue[k] > 0:
                shares = issue[k]
        if shares is None and sym in E:
            ds = [x for x in E[sym] if x[0] <= u.datestr[prev]]
            shares = ds[-1][1] if ds else None
        if not shares:
            why["no share count (not in ASIC's files or EODHD)"] += 1; continue
        mv = close * shares
        if v < MIN_SHARE * mv:
            continue
        last_event[sym] = i_in
        events.append({"sym": sym, "j": j, "date": pd, "i_in": i_in, "value": v, "mv": mv, "share": v / mv})

    def run(H: int, lo: str, hi: str) -> tuple[list[dict], dict]:
        out, w = [], defaultdict(int)
        for e in events:
            if not (lo <= e["date"] <= hi):
                continue
            j, i_in = e["j"], e["i_in"]
            i_out = i_in + H
            if i_out >= len(u.dates):
                w["holding period not over yet"] += 1; continue
            if not np.isfinite(bench.tro[i_in, j]):
                w["no trade on the entry day"] += 1; continue
            if not u.tradable(j, i_in):
                w["not tradable at entry (price or traded value)"] += 1; continue
            gross, i_sold, how = u.hold(j, i_in, i_out)
            if not np.isfinite(gross):
                w["no price to value the holding"] += 1; continue
            cost = u.round_trip_cost(j, i_in, i_sold)
            b = bench.ret(i_in, max(i_sold, i_in + 1))
            out.append({**e, "gross": gross, "cost": cost, "bench": b, "vas": u.market(i_in, max(i_sold, i_in + 1)), "result": gross - cost - b,
                        "month": u.datestr[i_in][:7], "year": e["date"][:4]})
        return out, w
    L = [title.strip(), "", f"Rulebook section 9l. Run {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC{' (forced re-run)' if force else ''}.", "",
         f"Contract events worth at least 5% of the company's market value: {len(events)}.", "",
         "## Tuning, 2013 to 2018", "", "| Held | Events | Mean result after costs | Monthly t |", "| --- | --- | --- | --- |"]
    tuned = []
    for H in HOLDS:
        r, _ = run(H, "2000-01-01", TUNE_END)
        m = stats.mean(x["result"] for x in r) if r else float("nan")
        t, _ = monthly_t(r) if len(r) > 2 else (float("nan"), 0)
        tuned.append((m, H))
        L.append(f"| {H} sessions | {len(r)} | {m:+.2%} | {t:.2f} |")
    finite = [x for x in tuned if np.isfinite(x[0])]
    H = max(finite, key=lambda x: x[0])[1] if finite else HOLDS[0]
    L += ["", f"Picked: hold {H} sessions." + ("" if finite else " (No tuning events, so the first version is used.)"), "", "## Run once, 2019 onwards", ""]
    res, w = run(H, TEST_FROM, "2099-12-31")
    for k, v in w.items():
        why[k] += v
    passed = False
    if len(res) < MIN_EVENTS:
        L += [f"Only {len(res)} events; the test needs {MIN_EVENTS}. **Result: fail.**"]
        if res:
            L += ["", f"Reported only: mean result {stats.mean(x['result'] for x in res):+.2%} across those {len(res)}."]
    else:
        xs = [x["result"] for x in res]
        m = stats.mean(xs)
        t, months = monthly_t(res)
        tm = trimmed_mean(xs)
        ty = top_year_share(res)
        checks = [(f"At least {MIN_EVENTS} events", True, str(len(xs))),
                  ("Mean after costs, against the equal-weighted benchmark, above zero with t of 2 or more (monthly)", m > 0 and t >= 2, f"{m:+.2%}, t {t:.2f} over {months} months"),
                  ("Still above zero without the best 5% of events", tm > 0, f"{tm:+.2%}"),
                  ("No single year more than half the total gain", ty <= 0.5, f"{ty:.0%}" if np.isfinite(ty) else "no total gain")]
        passed = all(c[1] for c in checks)
        L += ["| Measure | Value |", "| --- | --- |", f"| Events | {len(xs)} |", f"| Mean gross return | {stats.mean(x['gross'] for x in res):+.2%} |",
              f"| Mean costs | {stats.mean(x['cost'] for x in res):.2%} |", f"| Mean equal-weighted benchmark | {stats.mean(x['bench'] for x in res):+.2%} |",
              f"| Mean result after costs, less the benchmark | {m:+.2%} (median {stats.median(xs):+.2%}) |", f"| t-statistic (monthly) | {t:.2f} |",
              f"| Hit rate | {sum(1 for v in xs if v > 0) / len(xs):.0%} |", f"| Against VAS instead (reported only) | {stats.mean(x['gross'] - x['cost'] - x['vas'] for x in res):+.2%} |",
              "", "| Pass mark | Met | Value |", "| --- | --- | --- |"] + [f"| {a} | {'yes' if b else 'no'} | {c} |" for a, b, c in checks]
        L += ["", f"**Result: {'pass' if passed else 'fail'}.**", ""]
        for lab, lo, hi in (("5 to 20% of market value", 0.05, 0.20), ("over 20%", 0.20, 1e9)):
            g = [x["result"] for x in res if lo <= x["share"] < hi]
            L.append(f"- Reported only, contracts {lab}: {len(g)} events, mean {stats.mean(g):+.2%}" if g else f"- Reported only, contracts {lab}: none")
    L += ["", "Events left out, by reason: " + ("; ".join(f"{k} {v}" for k, v in sorted(why.items())) or "none") + ".",
          "", "Caveats: companies must announce material contracts to the ASX, often before AusTender publishes them; contract value is not profit; "
          "matching suppliers to listed companies by name can miss subsidiaries trading under other names."]
    os.makedirs(os.path.dirname(report), exist_ok=True)
    open(report, "w").write("\n".join(L) + "\n")
    open(lock, "w").write(datetime.now(timezone.utc).isoformat())
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    sys.exit(main(a[0] if a else ".", "--force" in sys.argv))
