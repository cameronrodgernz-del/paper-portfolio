"""US pending-deal candidates from the SEC's merger filings (free, official).

Targets are companies that filed a merger proxy (PREM14A or DEFM14A) or a response to a
tender offer (SC 14D9) in the last `days` days. Each is matched to its ticker with the
SEC's company_tickers.json, and the filing text is searched for a cash price per share.
The price found is a lead for the analyst to confirm from the filing, never a fact.
Usage: python3 -I src/us_deals.py [data_dir] [days]
"""
import csv
import json
import os
import re
import sys
import time
import urllib.request
from collections import Counter
from datetime import date, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_sec import USER_AGENT  # noqa: E402

TARGET_FORMS = ("PREM14A", "DEFM14A", "SC 14D9", "SC 14D9/A", "DEFM14A/A", "PREM14A/A")
CASH = re.compile(r"\$\s?(\d{1,4}\.\d{2})\s*(?:per share\s*)?in cash|\$\s?(\d{1,4}\.\d{2})\s+per share,?\s+in cash|"
                  r"receive\s+\$\s?(\d{1,4}\.\d{2})\s+(?:per share\s+)?in cash", re.I)


def sec_get(url: str, limit: int | None = None) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read(limit) if limit else r.read()


def main(data_dir: str = "data", days: int = 120) -> int:
    since = (date.today() - timedelta(days=days)).isoformat()
    with open(os.path.join(data_dir, "sec", "deal_filings.csv"), newline="") as f:
        rows = [r for r in csv.DictReader(f) if r["date"] >= since and r["form"] in TARGET_FORMS]
    tickers = {str(v["cik_str"]): v["ticker"] for v in json.loads(sec_get("https://www.sec.gov/files/company_tickers.json")).values()}
    by_cik = {}
    for r in sorted(rows, key=lambda x: x["date"]):
        e = by_cik.setdefault(r["cik"], {"cik": r["cik"], "company": r["company"], "first_seen": r["date"], "forms": [], "urls": []})
        e["forms"].append(r["form"]); e["urls"].append(r["url"]); e["latest"] = r["date"]
    out = []
    for e in by_cik.values():
        price, n = "", 0
        try:
            text = sec_get(e["urls"][-1], limit=1_500_000).decode("latin-1")
            found = Counter(next(g for g in m.groups() if g) for m in CASH.finditer(text))
            if found:
                price, n = found.most_common(1)[0]
        except Exception as ex:  # keep going; the analyst sees the gap
            price = f"error: {type(ex).__name__}"
        time.sleep(0.2)
        out.append({"cik": e["cik"], "company": e["company"], "ticker": tickers.get(e["cik"], ""),
                    "first_seen": e["first_seen"], "latest": e["latest"], "forms": ";".join(sorted(set(e["forms"]))),
                    "cash_price_lead": price, "mentions": n, "url": e["urls"][-1]})
    path = os.path.join(data_dir, "sec", "us_deal_targets.csv")
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()) if out else ["cik"])
        w.writeheader(); w.writerows(sorted(out, key=lambda x: x["latest"], reverse=True))
    # Price universe for the deal sleeve: common shares with a cash price lead, newest 40.
    common = re.compile(r"^[A-Z]{1,4}$|^[A-Z]{5}$")
    picks = [o for o in sorted(out, key=lambda x: x["latest"], reverse=True)
             if o["ticker"] and common.match(o["ticker"]) and not re.search(r"(U|W|R|WS)$", o["ticker"][4:] if len(o["ticker"]) == 5 else "")
             and o["cash_price_lead"] and not o["cash_price_lead"].startswith("error")
             and not re.search(r"acquisition corp|capital trust|property trust|fund\b", o["company"], re.I)][:40]
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "universe_us_deals.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ticker", "market", "provider", "provider_symbol", "why"])
        for o in picks:
            w.writerow([o["ticker"], "US", "tiingo", o["ticker"], f"US deal lead: {o['company'][:40]} cash {o['cash_price_lead']} ({o['latest']})"])
    print(f"{len(out)} US targets; {sum(1 for o in out if o['ticker'])} with tickers; "
          f"{sum(1 for o in out if o['cash_price_lead'] and not o['cash_price_lead'].startswith('error'))} with a cash price lead")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data", int(sys.argv[2]) if len(sys.argv) > 2 else 120))
