"""Director and officer buying clusters in US shares, from the SEC's free insider data sets.

Source: SEC Financial Statement and Notes / Insider Transactions Data Sets (Forms 3, 4 and 5),
one zip per quarter, https://www.sec.gov/files/structureddata/data/insider-transactions-data-sets/
Each zip is downloaded, the open-market purchases (Form 4, transaction code P, shares acquired)
by directors and officers are kept, and the zip is deleted.

A cluster is at least MIN_BUYERS different directors or officers buying on the market within
WINDOW_DAYS, together for at least MIN_VALUE_USD. The event date is the filing date of the
report that completes the cluster: the first moment the cluster was public. Ten-per-cent holders
who are not directors or officers are left out (they are funds, not insiders with company knowledge).

Writes data/history/insider_buys.csv (every qualifying purchase; large, kept out of git) and
data/history/insider_clusters_n{2,3,4}.csv (one row per cluster event, for 2, 3 or 4 buyers).
Usage: python3 -I src/history/insider_events.py <repo_root> [first_quarter] [last_quarter]   e.g. 2010q1 2026q3
"""
import csv
import io
import os
import sys
import time
import urllib.request
import zipfile
from collections import defaultdict
from datetime import date, datetime, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from fetch_sec import USER_AGENT  # noqa: E402

BASE = "https://www.sec.gov/files/structureddata/data/insider-transactions-data-sets/{q}_form345.zip"
MIN_BUYERS, WINDOW_DAYS, MIN_VALUE_USD = 3, 30, 100_000
BUY_FIELDS = ["filing_date", "accession", "issuer_cik", "ticker", "issuer_name", "owner_cik", "owner_name",
              "role", "trans_date", "shares", "price", "value_usd"]


def quarters(first: str, last: str):
    y, q = int(first[:4]), int(first[-1])
    while (y, q) <= (int(last[:4]), int(last[-1])):
        yield f"{y}q{q}"
        y, q = (y + 1, 1) if q == 4 else (y, q + 1)


def d(s: str) -> str:
    return datetime.strptime(s.strip(), "%d-%b-%Y").date().isoformat() if s.strip() else ""


def read_tsv(z: zipfile.ZipFile, name: str):
    with z.open(name) as f:
        yield from csv.DictReader(io.TextIOWrapper(f, encoding="latin-1", newline=""), delimiter="\t")


def purchases(q: str, tmp: str) -> list[dict]:
    path = os.path.join(tmp, f"{q}.zip")
    req = urllib.request.Request(BASE.format(q=q), headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=300) as r, open(path, "wb") as f:
        f.write(r.read())
    out = []
    try:
        with zipfile.ZipFile(path) as z:
            names = {n.split("/")[-1]: n for n in z.namelist()}
            subs = {}
            for r in read_tsv(z, names["SUBMISSION.tsv"]):
                if r["DOCUMENT_TYPE"].strip() in ("4", "4/A") and r["ISSUERTRADINGSYMBOL"].strip():
                    subs[r["ACCESSION_NUMBER"]] = r
            owners = defaultdict(list)
            for r in read_tsv(z, names["REPORTINGOWNER.tsv"]):
                if r["ACCESSION_NUMBER"] in subs:
                    owners[r["ACCESSION_NUMBER"]].append(r)
            for r in read_tsv(z, names["NONDERIV_TRANS.tsv"]):
                a = r["ACCESSION_NUMBER"]
                if a not in subs or r["TRANS_CODE"].strip() != "P" or r["TRANS_ACQUIRED_DISP_CD"].strip() != "A":
                    continue
                try:
                    sh, px = float(r["TRANS_SHARES"] or 0), float(r["TRANS_PRICEPERSHARE"] or 0)
                except ValueError:
                    continue
                if sh <= 0 or px <= 0:
                    continue
                for o in owners[a]:
                    rel = o["RPTOWNER_RELATIONSHIP"].lower()
                    role = "director" if "director" in rel else ("officer" if "officer" in rel else "")
                    if not role:
                        continue
                    s = subs[a]
                    out.append({"filing_date": d(s["FILING_DATE"]), "accession": a, "issuer_cik": s["ISSUERCIK"].lstrip("0"),
                                "ticker": s["ISSUERTRADINGSYMBOL"].strip().upper(), "issuer_name": s["ISSUERNAME"].strip(),
                                "owner_cik": o["RPTOWNERCIK"].lstrip("0"), "owner_name": o["RPTOWNERNAME"].strip(), "role": role,
                                "trans_date": d(r["TRANS_DATE"]), "shares": sh, "price": px, "value_usd": round(sh * px, 2)})
                    break     # a joint filing counts once per transaction
    finally:
        os.remove(path)
    return out


def clusters(buys: list[dict], min_buyers: int = MIN_BUYERS) -> list[dict]:
    by_issuer = defaultdict(list)
    for b in buys:
        if b["trans_date"]:
            by_issuer[b["issuer_cik"]].append(b)
    events = []
    for cik, rows in by_issuer.items():
        rows.sort(key=lambda r: (r["filing_date"], r["trans_date"]))
        last_event = None
        for i, r in enumerate(rows):
            start = (date.fromisoformat(r["trans_date"]) - timedelta(days=WINDOW_DAYS)).isoformat()
            window = [x for x in rows[: i + 1] if x["trans_date"] >= start and x["filing_date"] <= r["filing_date"]]
            buyers = {x["owner_cik"] for x in window}
            value = sum(x["value_usd"] for x in window)
            if len(buyers) >= min_buyers and value >= MIN_VALUE_USD:
                # one event per cluster: a new one needs a quiet gap of a full window after the last
                if last_event and date.fromisoformat(r["filing_date"]) - date.fromisoformat(last_event) <= timedelta(days=WINDOW_DAYS * 3):
                    continue
                last_event = r["filing_date"]
                events.append({"event_date": r["filing_date"], "ticker": r["ticker"], "issuer_cik": cik, "issuer_name": r["issuer_name"],
                               "buyers": len(buyers), "directors": len({x["owner_cik"] for x in window if x["role"] == "director"}),
                               "value_usd": round(value, 2), "first_trade": min(x["trans_date"] for x in window),
                               "avg_price": round(sum(x["value_usd"] for x in window) / sum(x["shares"] for x in window), 4)})
    return sorted(events, key=lambda e: e["event_date"])


def main(root: str, first: str = "2010q1", last: str = "2026q3") -> int:
    out_dir = os.path.join(root, "data", "history")
    os.makedirs(out_dir, exist_ok=True)
    buys_path = os.path.join(out_dir, "insider_buys.csv")
    done = set()
    if os.path.exists(buys_path):
        with open(buys_path, newline="") as f:
            done = {r["filing_date"][:4] + "q" + str((int(r["filing_date"][5:7]) - 1) // 3 + 1) for r in csv.DictReader(f)}
    tmp = os.path.join(out_dir, "_tmp")
    os.makedirs(tmp, exist_ok=True)
    for q in quarters(first, last):
        if q in done:
            continue
        try:
            rows = purchases(q, tmp)
        except Exception as e:
            print(q, "failed:", type(e).__name__, e)
            continue
        new = not os.path.exists(buys_path)
        with open(buys_path, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=BUY_FIELDS)
            if new:
                w.writeheader()
            w.writerows(rows)
        print(q, len(rows), "purchases", flush=True)
        time.sleep(1)
    os.rmdir(tmp)
    with open(buys_path, newline="") as f:
        buys = list(csv.DictReader(f))
    for b in buys:
        b["value_usd"], b["shares"] = float(b["value_usd"]), float(b["shares"])
    for n in (2, 3, 4):      # the test tunes the number of buyers over these
        ev = clusters(buys, n)
        with open(os.path.join(out_dir, f"insider_clusters_n{n}.csv"), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(ev[0].keys()))
            w.writeheader(); w.writerows(ev)
        print(len(buys), "purchases;", len(ev), f"cluster events with {n} or more buyers")
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:4]))
