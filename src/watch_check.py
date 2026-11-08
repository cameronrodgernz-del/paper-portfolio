"""The research watch list, checked each night (rulebook section 5a).

Deep dives and red-team reviews that end in "wait" set a price at which the case would be looked at again
(research/watch_triggers.csv), and the dated events to watch (research/watch_events.csv). This reads the
latest close for each watched share and writes reports/watch_triggers.md: every trigger with its latest price
and how far away it is, any that has been hit, and the events in the next 14 days. A hit sends the share back
to the research desk for a fresh look against the conditions in its file; it never places an order.

Prices: data/prices/<market>/<ticker>.csv (the nightly fetch), else for ASX the last trade in
data/research_data/asx_company.json (header.priceLast, as at its fetch date).
Usage: python3 -I src/watch_check.py <repo_root> [--today YYYY-MM-DD]
"""
import csv
import json
import os
import sys
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

NEAR = 0.05          # within 5% of a trigger counts as near
EVENT_DAYS = 14


def latest(root: str, market: str, ticker: str) -> tuple[float | None, str, str]:
    """(close, date, source) for the latest stored price, or (None, "", reason)."""
    path = os.path.join(root, "data", "prices", market, f"{ticker}.csv")
    if os.path.exists(path):
        rows = [r for r in csv.DictReader(open(path, encoding="utf-8")) if r.get("close")]
        if rows:
            r = rows[-1]
            return float(r["close"]), r["date"], f"data/prices/{market}"
    if market == "ASX":
        cpath = os.path.join(root, "data", "research_data", "asx_company.json")
        if os.path.exists(cpath):
            e = json.load(open(cpath, encoding="utf-8")).get(ticker) or {}
            px = (e.get("header") or {}).get("priceLast")
            if px:
                return float(px), (e.get("fetched") or "")[:10], "ASX company data (last trade at fetch)"
    return None, "", "no price stored"


def check(root: str, today: str) -> dict:
    trig = list(csv.DictReader(open(os.path.join(root, "research", "watch_triggers.csv"), encoding="utf-8")))
    rows, hits = [], []
    for t in trig:
        px, d, src = latest(root, t["market"], t["ticker"])
        level = float(t["trigger_price"])
        gap = None if px is None else px / level - 1
        state = "no price" if px is None else ("HIT" if px <= level else ("near" if gap <= NEAR else ""))
        row = dict(t, price=px, price_date=d, price_source=src, gap=gap, state=state)
        rows.append(row)
        if state == "HIT":
            hits.append(row)
    evp = os.path.join(root, "research", "watch_events.csv")
    events = []
    if os.path.exists(evp):
        end = (date.fromisoformat(today) + timedelta(days=EVENT_DAYS)).isoformat()
        events = [e for e in csv.DictReader(open(evp, encoding="utf-8")) if today <= e["date"] <= end]
    return {"today": today, "rows": rows, "hits": hits, "events": sorted(events, key=lambda e: e["date"])}


def write(root: str, res: dict) -> str:
    out = [f"# Research watch list, {res['today']}", "",
           "Prices at which a \"wait\" verdict would be looked at again (research/watch_triggers.csv), and the dated "
           "events in the next 14 days (research/watch_events.csv). A hit sends the share back to the research desk "
           "to check the other conditions in its file; nothing is bought from this list. This is a simulation and "
           "not financial advice.", ""]
    if res["hits"]:
        out += ["## Hit", ""] + [f"- {h['market']}:{h['ticker']} ({h['company']}) at {h['price']:g} on {h['price_date']}, "
                                 f"at or below {float(h['trigger_price']):g}. Also needs: {h['also_needs']}. File: {h['source']}"
                                 for h in res["hits"]] + [""]
    else:
        out += ["No trigger hit.", ""]
    out += ["## Triggers", "", "| Share | Trigger | Latest | Date | Away | State | Source of price |",
            "| --- | --- | --- | --- | --- | --- | --- |"]
    for r in sorted(res["rows"], key=lambda r: (r["gap"] is None, r["gap"] if r["gap"] is not None else 0)):
        away = "" if r["gap"] is None else f"{r['gap']:+.1%}"
        latest_px = "" if r["price"] is None else f"{r['price']:g}"
        out.append(f"| {r['market']}:{r['ticker']} | {r['currency']} {float(r['trigger_price']):g} | {latest_px} | "
                   f"{r['price_date']} | {away} | {r['state']} | {r['price_source']} |")
    out += ["", "## Events in the next 14 days", ""]
    out += [f"- {e['date']}: {e['market']}:{e['ticker']}, {e['event']} ({e['date_basis']})" for e in res["events"]] or ["None."]
    path = os.path.join(root, "reports", "watch_triggers.md")
    open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")
    return path


def main() -> int:
    root = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "."
    today = (sys.argv[sys.argv.index("--today") + 1] if "--today" in sys.argv
             else datetime.now(ZoneInfo("Pacific/Auckland")).date().isoformat())
    res = check(root, today)
    write(root, res)
    print(f"watch list: {len(res['rows'])} triggers, {len(res['hits'])} hit, {len(res['events'])} events in 14 days")
    for h in res["hits"]:
        print(f"HIT {h['market']}:{h['ticker']} {h['price']:g} <= {float(h['trigger_price']):g}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
