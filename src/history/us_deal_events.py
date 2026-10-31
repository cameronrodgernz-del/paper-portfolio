"""US deal events for the deal-sleeve history test, from free SEC sources.

1. Every quarterly EDGAR form index (full-index/<year>/QTR<n>/form.idx), 2015 to 2025: keep the
   first PREM14A (preliminary merger proxy, filed by the target) and the first SC 14D9 (the target's
   response to a tender offer) for each company. These dates are when a deal's terms were public in
   an SEC filing, so a rule can enter on them without hindsight.
2. CIK to ticker as at the time, from the Form 4 insider data sets (each Form 4 carries the issuer's
   trading symbol). Completed targets are delisted, so today's ticker list would miss them.

Writes data/history/us_deal_filings.csv and data/history/cik_tickers.csv.
Usage: python3 -I src/history/us_deal_events.py <repo_root>
"""
import csv
import io
import os
import re
import sys
import time
import urllib.request
import zipfile
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from fetch_sec import USER_AGENT  # noqa: E402

FORMS = ("PREM14A", "SC 14D9")
IDX = "https://www.sec.gov/Archives/edgar/full-index/{y}/QTR{q}/form.idx"
F345 = "https://www.sec.gov/files/structureddata/data/insider-transactions-data-sets/{y}q{q}_form345.zip"
LINE = re.compile(r"^(?P<form>PREM14A|SC 14D9)\s{2,}(?P<company>.+?)\s{2,}(?P<cik>\d+)\s+(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<file>\S+)")


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=300) as r:
        return r.read()


def main(root: str) -> int:
    out = os.path.join(root, "data", "history")
    os.makedirs(out, exist_ok=True)
    first = {}
    for y in range(2015, 2026):
        for q in range(1, 5):
            try:
                text = get(IDX.format(y=y, q=q)).decode("latin-1")
            except Exception as e:
                print(y, q, "index failed:", e); continue
            n = 0
            for line in text.splitlines():
                m = LINE.match(line)
                if not m:
                    continue
                key = (m["cik"], m["form"])
                if key not in first or m["date"] < first[key]["date"]:
                    first[key] = {"cik": m["cik"], "company": m["company"].strip(), "form": m["form"], "date": m["date"],
                                  "url": "https://www.sec.gov/Archives/" + m["file"]}
                    n += 1
            print(y, q, n, "new first filings", flush=True)
            time.sleep(0.5)
    with open(os.path.join(out, "us_deal_filings.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["cik", "company", "form", "date", "url"])
        w.writeheader(); w.writerows(sorted(first.values(), key=lambda r: r["date"]))
    tick = {}
    for y in range(2014, 2027):
        for q in range(1, 5):
            if (y, q) > (2026, 1):
                break
            try:
                raw = get(F345.format(y=y, q=q))
            except Exception as e:
                print(y, q, "insider set failed:", e); continue
            with zipfile.ZipFile(io.BytesIO(raw)) as z:
                name = next(n for n in z.namelist() if n.endswith("SUBMISSION.tsv"))
                with z.open(name) as fh:
                    for r in csv.DictReader(io.TextIOWrapper(fh, encoding="latin-1", newline=""), delimiter="\t"):
                        cik, sym = r["ISSUERCIK"].lstrip("0"), r["ISSUERTRADINGSYMBOL"].strip().upper()
                        if not cik or not re.match(r"^[A-Z]{1,5}$", sym):
                            continue
                        try:
                            d = datetime.strptime(r["FILING_DATE"].strip(), "%d-%b-%Y").date().isoformat()
                        except ValueError:
                            continue
                        e = tick.setdefault((cik, sym), {"cik": cik, "ticker": sym, "first": d, "last": d, "filings": 0})
                        e["first"], e["last"], e["filings"] = min(e["first"], d), max(e["last"], d), e["filings"] + 1
            print(y, q, "tickers so far", len(tick), flush=True)
            time.sleep(0.5)
    with open(os.path.join(out, "cik_tickers.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["cik", "ticker", "first", "last", "filings"])
        w.writeheader(); w.writerows(sorted(tick.values(), key=lambda r: (int(r["cik"]), r["first"])))
    print(len(first), "first filings;", len(tick), "cik-ticker pairs")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
