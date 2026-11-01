"""History test 9j (rulebook): franked special dividends in ASX schemes.

Events: ASX schemes in the deal database announced 2015 to 2025 that paid holders, where Norgate records a
dividend of at least 1% of the share price with an ex-date between the announcement and the last day of
trading (the largest such dividend if there are several). A target that kept trading more than 120 days
after the scheme's outcome is a different company on a reused code and is left out.
Selling: at the open on the last session before the ex-date, less half the spread and Sharesies' brokerage
(on a A$3,000 order). Holding: the dividend plus the last traded price before the shares stop trading.
Result: selling / holding - 1. Nothing is tuned. Writes reports/scheme_special_history.md and a lock.
Usage: python3 -I src/history/scheme_special_test.py <repo_root> [--force]
"""
import csv
import os
import statistics as stats
import sys
from collections import defaultdict
from datetime import date, datetime, timezone

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from deal_odds import holder_outcome  # noqa: E402
from event_tools import monthly_t, trimmed_mean  # noqa: E402
from failed_deal_test import deal_symbol  # noqa: E402
from universe import FEE, Universe, ready  # noqa: E402

MIN_EVENTS = 15


def main(root: str, force: bool = False) -> int:
    report = os.path.join(root, "reports", "scheme_special_history.md")
    lock = report + ".lock"
    title = "# History test 9j: franked special dividends in ASX schemes\n\n"
    if os.path.exists(lock) and not force:
        print("result already written; use --force to re-run (the re-run is recorded)"); return 0
    if not ready(root):
        open(report, "w").write(title + "Waiting for the Norgate whole-market prices (data/norgate/universe/).\n")
        print("waiting for the universe"); return 0
    u = Universe(root)
    find = deal_symbol(root, u)
    rows = list(csv.DictReader(open(os.path.join(root, "deals", "all_deals.csv"), encoding="utf-8")))
    by_id = {r["deal_id"]: r for r in rows}
    with np.errstate(all="ignore"):
        f = u.tr / u.c
    res, why, schemes = [], defaultdict(int), 0
    for r in rows:
        if r["market"] != "ASX" or r["structure"] != "scheme" or not ("2015" <= (r["announce_date"] or "")[:4] <= "2025"):
            continue
        if holder_outcome(r, by_id) != 1:
            continue
        schemes += 1
        s = find(r["target_ticker"].upper(), r["announce_date"][:10])
        if not s or s not in u.col:
            why["no Norgate prices"] += 1; continue
        j = u.col[s]
        idx = np.where(~np.isnan(u.c[:, j]))[0]
        last = int(idx[-1])
        end = (r.get("implementation_date") or r.get("outcome_date") or "")[:10]
        if end and (date.fromisoformat(u.datestr[last]) - date.fromisoformat(end)).days > 120:
            why["kept trading long after the scheme (a reused code)"] += 1; continue
        a = u.row_after(r["announce_date"][:10])
        best = None
        for p, i in zip(idx[:-1], idx[1:]):
            if a is None or i < a or i > last:
                continue
            D = float(u.c[i, j] * (f[i, j] / f[p, j] - 1))
            if D >= 0.01 * u.c[p, j] and (best is None or D > best[2]):
                best = (int(p), int(i), D)
        if not best:
            why["no dividend of 1% or more while trading"] += 1; continue
        p, i, D = best
        if np.isnan(u.o[p, j]):
            why["no open price on the last session before the ex-date"] += 1; continue
        sell = float(u.o[p, j]) * (1 - u.half_spread(j, p) - FEE)
        hold = D + float(u.c[last, j])
        res.append({"ticker": r["target_ticker"], "ex": u.datestr[i], "div_pct": D / float(u.c[p, j]), "result": sell / hold - 1,
                    "sessions_to_end": int(np.sum((idx > i) & (idx <= last))), "drop_ratio": (float(u.c[p, j]) - float(u.o[i, j])) / D if not np.isnan(u.o[i, j]) else float("nan"),
                    "month": u.datestr[p][:7], "year": u.datestr[p][:4]})
    L = [title.strip(), "", f"Rulebook section 9j. Run {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC{' (forced re-run)' if force else ''}.", "",
         f"ASX schemes from 2015 to 2025 that paid holders: {schemes}.", ""]
    xs = [x["result"] for x in res]
    passed = False
    if len(xs) < MIN_EVENTS:
        L += [f"Only {len(xs)} events; the test needs {MIN_EVENTS}. **Result: fail.**"]
    else:
        m = stats.mean(xs)
        t, months = monthly_t(res)
        tm = trimmed_mean(xs)
        checks = [(f"At least {MIN_EVENTS} events", True, str(len(xs))),
                  ("Selling before the ex-date beats holding, mean above zero with t of 2 or more (monthly)", m > 0 and t >= 2, f"{m:+.2%}, t {t:.2f} over {months} months"),
                  ("Still above zero without the best 5% of events", tm > 0, f"{tm:+.2%}")]
        passed = all(c[1] for c in checks)
        L += ["| Measure | Value |", "| --- | --- |", f"| Events | {len(xs)} |", f"| Mean result, selling against holding | {m:+.2%} (median {stats.median(xs):+.2%}) |",
              f"| t-statistic (monthly) | {t:.2f} |", f"| Selling did better | {sum(1 for v in xs if v > 0)} of {len(xs)} |",
              f"| Mean dividend, as a share of the price | {stats.mean(x['div_pct'] for x in res):.1%} |", "",
              "| Pass mark | Met | Value |", "| --- | --- | --- |"] + [f"| {a} | {'yes' if b else 'no'} | {c} |" for a, b, c in checks]
        L += ["", f"**Result: {'pass' if passed else 'fail'}.**", ""]
        near = [x["result"] for x in res if x["sessions_to_end"] <= 10]
        dr = [x["drop_ratio"] for x in res if np.isfinite(x["drop_ratio"])]
        big = [x["result"] for x in res if x["div_pct"] >= 0.03]
        L += ["Reported only:",
              f"- ex-date within 10 sessions of the last day of trading: {len(near)} events, mean {stats.mean(near):+.2%}" if near else "- no ex-dates within 10 sessions of the end",
              f"- dividends of 3% of the price or more: {len(big)} events, mean {stats.mean(big):+.2%}" if big else "- no dividends of 3% or more",
              f"- the price fell on the ex-date by a median {stats.median(dr):.2f} times the dividend (above 1 means the market paid for more than the cash)" if dr else "",
              "", "| Target | Ex-date | Dividend | Sessions left after | Result |", "| --- | --- | --- | --- | --- |"]
        L += [f"| {x['ticker']} | {x['ex']} | {x['div_pct']:.1%} | {x['sessions_to_end']} | {x['result']:+.2%} |" for x in sorted(res, key=lambda x: x["ex"])]
    L += ["", "Events left out, by reason: " + ("; ".join(f"{k} {v}" for k, v in sorted(why.items())) or "none") + ".",
          "", "Caveats: Norgate doesn't say whether a dividend is franked, so ordinary and unfranked dividends are included; holding is valued at the "
          "last traded price, and the time until the money arrives is ignored; a scheme that paid with hindsight makes holding look safer than it was."]
    os.makedirs(os.path.dirname(report), exist_ok=True)
    open(report, "w").write("\n".join(L) + "\n")
    open(lock, "w").write(datetime.now(timezone.utc).isoformat())
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    sys.exit(main(a[0] if a else ".", "--force" in sys.argv))
