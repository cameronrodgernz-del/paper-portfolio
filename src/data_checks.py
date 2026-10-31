"""Nightly checks on the data before the clerk uses it: prices that look wrong or stale, and
exchange rates that have stopped updating. Nothing is changed; the findings go in
reports/data_checks.json and .md, the clerk's flags, and the hub's Needs a look.

Price checks, for every share the portfolio holds, has an order for, or watches as a live deal (and
the core funds):
- a bar that can't be right: a close at or below zero, a high below the low, or a close outside the
  day's range;
- the same date twice;
- a move of more than 25% in a session (or 40% for NZX and shares under A$/NZ$0.50), unless the share
  is a live deal target near an announcement, which is checked by eye;
- stale: the last close is more than 2 business days older than the newest close in that market.
Currency checks: the NZ$ rates are no more than 4 days old, and each day's change is under 5%.
Usage: python3 -I src/data_checks.py <repo_root>
"""
import csv
import json
import os
import sys
from datetime import date, datetime, timedelta

ROOT_DEFAULT = "."


def bdays(a: str, b: str) -> int:
    x, y = date.fromisoformat(a), date.fromisoformat(b)
    n = 0
    while x < y:
        x += timedelta(days=1)
        if x.weekday() < 5:
            n += 1
    return n


def read(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def fnum(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def watched(root: str) -> set:
    out = set()
    for r in read(os.path.join(root, "config", "live_deals.csv")):
        out.add((r["target_market"], r["target_ticker"]))
        if r.get("acquirer_ticker"):
            out.add((r["acquirer_market"], r["acquirer_ticker"]))
    for r in read(os.path.join(root, "config", "universe_trial.csv")):
        out.add((r["market"], r["ticker"]))
    cfg = json.load(open(os.path.join(root, "config", "run.json")))
    act = cfg.get("active")
    if act:
        d = os.path.join(root, cfg["ledgers"][act]["dir"])
        for t in ("fills.jsonl", "orders.jsonl"):
            p = os.path.join(d, t)
            if os.path.exists(p):
                for line in open(p):
                    try:
                        q = json.loads(line)["payload"]
                    except (ValueError, KeyError):
                        continue
                    if q.get("market") and q.get("ticker"):
                        out.add((q["market"], q["ticker"]))
    return out


def check_prices(root: str, names: set, recent_days: int = 10) -> list[dict]:
    issues, latest = [], {}
    deal_targets = {(r["target_market"], r["target_ticker"]): r.get("announce_date", "") for r in read(os.path.join(root, "config", "live_deals.csv"))}
    bars = {}
    for m, t in sorted(names):
        rows = read(os.path.join(root, "data", "prices", m, f"{t}.csv"))
        if not rows:
            issues.append({"kind": "missing", "market": m, "ticker": t, "text": f"{m}:{t} has no price file"})
            continue
        bars[(m, t)] = rows
        latest[m] = max(latest.get(m, ""), rows[-1]["date"])
    for (m, t), rows in bars.items():
        seen = set()
        recent = rows[-(recent_days + 1):]
        for k, r in enumerate(recent):
            if r["date"] in seen:
                issues.append({"kind": "duplicate", "market": m, "ticker": t, "date": r["date"], "text": f"{m}:{t} has {r['date']} twice"})
            seen.add(r["date"])
            o, h, lo, c = (fnum(r.get(x)) for x in ("open", "high", "low", "close"))
            if c is None or c <= 0:
                issues.append({"kind": "bad_bar", "market": m, "ticker": t, "date": r["date"], "text": f"{m}:{t} close on {r['date']} is missing or not above zero"})
                continue
            if h is not None and lo is not None and (h < lo - 1e-9 or c > h * 1.0001 or c < lo * 0.9999):
                issues.append({"kind": "bad_bar", "market": m, "ticker": t, "date": r["date"], "text": f"{m}:{t} on {r['date']}: the close sits outside the day's range"})
            if k > 0:
                p = fnum(recent[k - 1].get("close"))
                if p and p > 0:
                    mv = c / p - 1
                    lim = 0.40 if (m == "NZX" or p < 0.5) else 0.25
                    if abs(mv) > lim:
                        ann = deal_targets.get((m, t), "")
                        near = ann and abs((date.fromisoformat(r["date"]) - date.fromisoformat(ann)).days) <= 3
                        issues.append({"kind": "jump", "market": m, "ticker": t, "date": r["date"], "move": round(mv, 4),
                                       "text": f"{m}:{t} moved {mv:+.0%} on {r['date']}" + (" (deal announced then)" if near else ": check against the company's announcements")})
        if latest.get(m) and bdays(rows[-1]["date"], latest[m]) > 2:
            issues.append({"kind": "stale", "market": m, "ticker": t, "date": rows[-1]["date"],
                           "text": f"{m}:{t} last close {rows[-1]['date']}, {bdays(rows[-1]['date'], latest[m])} business days behind the market"})
    return issues


def check_fx(root: str, today: str) -> list[dict]:
    issues = []
    rows = read(os.path.join(root, "data", "fx", "fx_daily.csv"))
    if not rows:
        return [{"kind": "fx", "text": "No exchange rates file"}]
    parsed = []
    for r in rows:
        try:
            parsed.append((datetime.strptime(r["date"], "%d-%b-%Y").date().isoformat(), float(r["nzd_usd"]), float(r["nzd_aud"])))
        except (ValueError, KeyError):
            continue
    parsed.sort()
    last = parsed[-1][0]
    age = (date.fromisoformat(today) - date.fromisoformat(last)).days
    if age > 4:
        issues.append({"kind": "fx", "date": last, "text": f"NZ$ exchange rates last published {last}, {age} days ago"})
    for a, b in zip(parsed[-10:], parsed[-9:]):
        for i, ccy in ((1, "USD"), (2, "AUD")):
            if a[i] > 0 and abs(b[i] / a[i] - 1) > 0.05:
                issues.append({"kind": "fx", "date": b[0], "text": f"NZ$/{ccy} moved {b[i] / a[i] - 1:+.1%} on {b[0]}: check the source"})
    return issues


def main(root: str) -> int:
    today = date.today().isoformat()
    names = watched(root)
    issues = check_prices(root, names) + check_fx(root, today)
    out = {"run": today, "checked": len(names), "issues": issues}
    os.makedirs(os.path.join(root, "reports"), exist_ok=True)
    json.dump(out, open(os.path.join(root, "reports", "data_checks.json"), "w"), indent=1)
    lines = [f"# Data checks, {today}", "", f"{len(names)} shares checked, plus the NZ$ exchange rates.", ""]
    lines += [f"- {i['text']}" for i in issues] or ["Nothing found."]
    open(os.path.join(root, "reports", "data_checks.md"), "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else ROOT_DEFAULT))
