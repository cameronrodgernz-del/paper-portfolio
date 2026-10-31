"""US deal signals from the SEC's official daily form index (EDGAR), free.

The SEC asks every automated request to name the requester and give a contact email;
Cam agreed (31 Oct 2026) to his address being used. Its limit is 10 requests a second;
this script makes one request per business day, with a pause between them.

Forms kept: merger proxies (PREM14A, DEFM14A, PREM14C, DEFM14C), tender offers and the
target's response (SC TO-T, SC 14D9), and going-private filings (SC 13E3).
Rows go to data/sec/deal_filings.csv; only days after the last stored day are fetched.
Usage: python3 -I src/fetch_sec.py [data_dir] [first_date YYYY-MM-DD]
"""
import csv
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date, timedelta

USER_AGENT = "Cameron Rodger paper-portfolio cameron.rodger.nz@gmail.com"
FORMS = ("PREM14A", "DEFM14A", "PREM14C", "DEFM14C", "SC TO-T", "SC 14D9", "SC 13E3")
FIELDS = ["date", "form", "company", "cik", "url"]


def day_index(d: date) -> str | None:
    q = (d.month - 1) // 3 + 1
    url = f"https://www.sec.gov/Archives/edgar/daily-index/{d.year}/QTR{q}/form.{d:%Y%m%d}.idx"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read().decode("latin-1")
    except urllib.error.HTTPError as e:
        if e.code in (403, 404):     # weekends, holidays, not yet published
            return None
        raise


ROW = re.compile(r"^(?P<form>\S+(?: \S+)*?)\s{2,}(?P<company>.+?)\s{2,}(?P<cik>\d+)\s+(?P<filed>\d{8})\s+(?P<path>edgar/\S+)\s*$")


def parse(idx: str, d: date) -> list[dict]:
    out, started = [], False
    for line in idx.splitlines():
        if line.startswith("-----"):
            started = True
            continue
        m = ROW.match(line) if started else None
        if not m:
            continue
        form = m["form"]
        if form.removesuffix("/A") not in FORMS:
            continue
        out.append({"date": d.isoformat(), "form": form, "company": m["company"].strip(), "cik": m["cik"],
                    "url": "https://www.sec.gov/Archives/" + m["path"]})
    return out


def main(data_dir: str = "data", first: str | None = None) -> int:
    path = os.path.join(data_dir, "sec", "deal_filings.csv")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    last = None
    if os.path.exists(path):
        with open(path, newline="") as f:
            rows = list(csv.DictReader(f))
        last = max((r["date"] for r in rows), default=None)
    start = date.fromisoformat(last) + timedelta(days=1) if last else date.fromisoformat(first or (date.today() - timedelta(days=30)).isoformat())
    new = []
    d = start
    while d < date.today():
        if d.weekday() < 5:
            idx = day_index(d)
            if idx:
                new += parse(idx, d)
            time.sleep(0.3)
        d += timedelta(days=1)
    exists = os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if not exists:
            w.writeheader()
        w.writerows(new)
    print(f"SEC deal filings added: {len(new)} ({start} to {date.today() - timedelta(days=1)})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data", sys.argv[2] if len(sys.argv) > 2 else None))
