"""History test 9h (rulebook): listed options below what they're worth.

Options: every ASX-listed option in Norgate whose name gives its strike and expiry ("$0.18 Option Expiring
09-Jul-2030"), matched to the ordinary share on the same code (the option code less its trailing O, OA, OB
and so on), one option to one share. An event: a session at least 15 sessions before expiry when the option
closes at or below 95% of (the share's close less the strike), the share above the strike; first event per
option only. Buy the option at the next open (it must trade at least A$5,000 that day; the order is 10% of
that day's traded value, at most A$3,000), exercise at once, sell the shares at the open 10 sessions later.
Return on the money laid out (option plus strike) after Sharesies' brokerage on both orders (1.9% capped at
A$15), half the spread on each and the hedge's 0.1%. Nothing is tuned. The share must pass the shared tradable
test on the entry day, and strikes are taken as half a cent above the rounded strike in the name.
Writes reports/listed_options_history.md and a lock. Usage: python3 -I src/history/options_test.py <repo_root> [--force]
"""
import math
import os
import re
import statistics as stats
import sys
from collections import defaultdict
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from event_tools import code_of, monthly_t, trimmed_mean  # noqa: E402
from universe import HEDGE, Universe, ready  # noqa: E402

OPT = re.compile(r"\$([\d.]+) Option Expiring (\d\d-[A-Za-z]{3}-\d{4})", re.I)
MIN_EVENTS = 30
WAIT = 10
BEFORE_EXPIRY = 15


def brokerage(v: float) -> float:
    return min(0.019 * v, 15.0)


def options(u: Universe) -> list[dict]:
    by_code = defaultdict(list)
    for s in u.symbols:
        if u.is_share(s):
            by_code[code_of(s)].append(s)
    out = []
    for s in u.symbols:
        m = OPT.search(u.sec.get(s, {}).get("name") or "")
        if not m:
            continue
        code = code_of(s)
        under = re.match(r"^(.+?)O[A-Z]?$", code)
        if not under:
            continue
        exp = datetime.strptime(m.group(2).title(), "%d-%b-%Y").date().isoformat()
        out.append({"sym": s, "strike": float(m.group(1)), "expiry": exp, "under_code": under.group(1), "shares": by_code.get(under.group(1), [])})
    return out


def main(root: str, force: bool = False) -> int:
    report = os.path.join(root, "reports", "listed_options_history.md")
    lock = report + ".lock"
    title = "# History test 9h: listed options below what they're worth\n\n"
    if os.path.exists(lock) and not force:
        print("result already written; use --force to re-run (the re-run is recorded)"); return 0
    if not ready(root):
        open(report, "w").write(title + "Waiting for the Norgate whole-market prices (data/norgate/universe/).\n")
        print("waiting for the universe"); return 0
    u = Universe(root)
    n = len(u.dates)
    opts = options(u)
    res, why = [], defaultdict(int)
    for op in opts:
        jo = u.col[op["sym"]]
        if op["strike"] <= 0:
            why["strike shown as zero"] += 1; continue
        exp_row = u.row_on_or_before(op["expiry"])
        rows = np.where(~np.isnan(u.c[:, jo]))[0]
        found = False
        for t in rows:
            if exp_row is None or t > exp_row - BEFORE_EXPIRY:
                break
            js = next((u.col[s] for s in op["shares"] if not math.isnan(u.c[t, u.col[s]])), None)
            if js is None:
                continue
            # names show strikes to the cent, so the strike is taken as half a cent higher than shown (the safe side)
            S, P, K = float(u.c[t, js]), float(u.c[t, jo]), op["strike"] + 0.005
            if not (S > K and P <= 0.95 * (S - K)):
                continue
            found = True
            i = t + 1
            if i >= n or math.isnan(u.o[i, jo]):
                why["option didn't trade the next session"] += 1; break
            if not u.tradable(js, i):
                why["share not tradable at entry (price or traded value)"] += 1; break
            traded = float(u.c[i, jo] * u.v[i, jo]) if not math.isnan(u.v[i, jo]) else 0.0
            if traded < 5000:
                why["option traded under A$5,000 on the entry day"] += 1; break
            k_out = i + WAIT
            sell = next((k for k in range(k_out, min(k_out + 5, n)) if not math.isnan(u.o[k, js])), None)
            if sell is None:
                why["holding period not over yet, or no share trade to sell into" if k_out >= n else "no share trade to sell into"] += 1; break
            Po, Ss = float(u.o[i, jo]), float(u.o[sell, js])
            v_o = min(3000.0, 0.10 * traded)
            n_opt = v_o / Po
            outlay = v_o * (1 + u.half_spread(jo, i)) + brokerage(v_o) + n_opt * K
            gross_sale = n_opt * Ss
            proceeds = gross_sale * (1 - u.half_spread(js, sell)) - brokerage(gross_sale)
            r = proceeds / outlay - 1 - HEDGE
            res.append({"sym": op["sym"], "date": u.datestr[t], "entry": u.datestr[i], "month": u.datestr[i][:7], "year": u.datestr[i][:4],
                        "gap": 1 - P / (S - K), "result": r, "order": v_o, "days_to_expiry": int(exp_row - t)})
            break
        if not found:
            why["never below 95% of its exercise value"] += 1
    L = [title.strip(), "", f"Rulebook section 9h. Run {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC{' (forced re-run)' if force else ''}.", "",
         f"Listed options in Norgate with a strike and expiry in the name: {len(opts)}.", ""]
    passed = False
    xs = [x["result"] for x in res]
    if len(xs) < MIN_EVENTS:
        L += [f"Only {len(xs)} events; the test needs {MIN_EVENTS}. **Result: fail.**"]
        if xs:
            L += ["", f"Reported only: mean result {stats.mean(xs):+.2%} across those {len(xs)}."]
    else:
        m = stats.mean(xs)
        t, months = monthly_t(res)
        tm = trimmed_mean(xs)
        checks = [(f"At least {MIN_EVENTS} events", True, str(len(xs))),
                  ("Mean result after costs above zero with t of 2 or more (monthly)", m > 0 and t >= 2, f"{m:+.2%}, t {t:.2f} over {months} months"),
                  ("Still above zero without the best 5% of events", tm > 0, f"{tm:+.2%}")]
        passed = all(c[1] for c in checks)
        L += ["| Measure | Value |", "| --- | --- |", f"| Events | {len(xs)} |", f"| Mean result on money laid out, after costs | {m:+.2%} (median {stats.median(xs):+.2%}) |",
              f"| t-statistic (monthly) | {t:.2f} |", f"| Hit rate | {sum(1 for v in xs if v > 0) / len(xs):.0%} |",
              f"| Median order size | A${stats.median(x['order'] for x in res):,.0f} |", f"| Mean gap below exercise value at the signal | {stats.mean(x['gap'] for x in res):.1%} |",
              "", "| Pass mark | Met | Value |", "| --- | --- | --- |"] + [f"| {a} | {'yes' if b else 'no'} | {c} |" for a, b, c in checks]
        L += ["", f"**Result: {'pass' if passed else 'fail'}.**"]
        near = [x["result"] for x in res if x["days_to_expiry"] <= 40]
        if near:
            L += ["", f"Reported only: events within 40 sessions of expiry: {len(near)}, mean {stats.mean(near):+.2%}."]
    L += ["", "Events left out, by reason: " + ("; ".join(f"{k} {v}" for k, v in sorted(why.items())) or "none") + ".",
          "", "Caveats: Norgate holds these options from about 2024; an option on other terms than one-for-one would be valued wrongly; "
          "a pass doesn't make it tradable until a broker that trades and exercises ASX options is chosen."]
    os.makedirs(os.path.dirname(report), exist_ok=True)
    open(report, "w").write("\n".join(L) + "\n")
    open(lock, "w").write(datetime.now(timezone.utc).isoformat())
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    sys.exit(main(a[0] if a else ".", "--force" in sys.argv))
