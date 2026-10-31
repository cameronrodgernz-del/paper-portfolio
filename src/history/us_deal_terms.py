"""Terms and tickers for the US deal history events (rulebook 9b), then the fixed price sample.

For each first PREM14A or SC 14D9 in data/history/us_deal_filings.csv:
- the ticker the company used at the time (data/history/cik_tickers.csv, from Form 4 filings);
- the cash price per share most often stated in the filing's text (same pattern as the live
  US monitor). Confirmed later against the share price at entry.
Writes data/history/us_deal_events.csv, then draws the price sample (seed 20261102) into
config/universe_history_deals.csv.
Usage: python3 -I src/history/us_deal_terms.py <repo_root> [sample_size]
"""
import csv
import os
import random
import re
import sys
import time
from collections import Counter, defaultdict
from datetime import date, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from us_deals import CASH, sec_get  # noqa: E402

SEED = 20261102


def ticker_at(rows: list[dict], d: str) -> str:
    lo = (date.fromisoformat(d) - timedelta(days=400)).isoformat()
    hi = (date.fromisoformat(d) + timedelta(days=30)).isoformat()
    live = [r for r in rows if r["first"] <= hi and r["last"] >= lo]
    if not live:
        return ""
    return max(live, key=lambda r: (int(r["filings"]), r["last"]))["ticker"]


def main(root: str, sample_n: int = 360) -> int:
    hist = os.path.join(root, "data", "history")
    by_cik = defaultdict(list)
    for r in csv.DictReader(open(os.path.join(hist, "cik_tickers.csv"), newline="")):
        by_cik[r["cik"]].append(r)
    filings = list(csv.DictReader(open(os.path.join(hist, "us_deal_filings.csv"), newline="")))
    # one event per company: its first deal filing of either kind (a later one is usually the same deal)
    first = {}
    for f in sorted(filings, key=lambda r: r["date"]):
        if f["cik"] not in first:
            first[f["cik"]] = f
    out_path = os.path.join(hist, "us_deal_events.csv")
    done = {}
    if os.path.exists(out_path):
        done = {r["cik"]: r for r in csv.DictReader(open(out_path, newline=""))}
    fields = ["cik", "company", "form", "date", "ticker", "cash_price", "mentions", "url"]
    rows = []
    for k, f in enumerate(first.values()):
        if f["cik"] in done:
            rows.append(done[f["cik"]]); continue
        t = ticker_at(by_cik.get(f["cik"], []), f["date"])
        price, n = "", 0
        if t:
            try:
                text = sec_get(f["url"], limit=1_500_000).decode("latin-1")
                found = Counter(next(g for g in m.groups() if g) for m in CASH.finditer(text))
                if found:
                    price, n = found.most_common(1)[0]
            except Exception as e:
                price = f"error: {type(e).__name__}"
            time.sleep(0.15)
        rows.append({"cik": f["cik"], "company": f["company"], "form": f["form"], "date": f["date"], "ticker": t,
                     "cash_price": price, "mentions": n, "url": f["url"]})
        if k % 100 == 0:
            print(k, "of", len(first), flush=True)
            with open(out_path, "w", newline="") as g:
                w = csv.DictWriter(g, fieldnames=fields); w.writeheader(); w.writerows(rows)
    with open(out_path, "w", newline="") as g:
        w = csv.DictWriter(g, fieldnames=fields); w.writeheader(); w.writerows(rows)
    usable = [r for r in rows if r["ticker"] and r["cash_price"] and not r["cash_price"].startswith("error")
              and float(r["cash_price"]) >= 1]
    tickers = sorted({r["ticker"] for r in usable})
    rng = random.Random(SEED)
    pick = sorted(rng.sample(tickers, min(sample_n, len(tickers))))
    with open(os.path.join(root, "config", "universe_history_deals.csv"), "w", newline="") as g:
        w = csv.writer(g)
        w.writerow(["ticker", "market", "provider", "provider_symbol", "why"])
        for t in pick:
            w.writerow([t, "US", "tiingo", t, "US deal history sample"])
    print(f"{len(first)} companies; {sum(1 for r in rows if r['ticker'])} with a ticker at the time; "
          f"{len(usable)} with a cash price; {len(tickers)} tickers; sampled {len(pick)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else ".", *(int(x) for x in sys.argv[2:3])))
