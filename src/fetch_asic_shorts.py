"""ASIC's daily aggregated short positions for every ASX product with reported shorts (free, from
16 June 2010), saved as data/asic/shorts_YYYY.csv.gz with columns date, code, short, issue:
  short: shares reported as short positions on that day
  issue: the total of that product on issue that day (so share counts, and capital raisings, by day)
One file a trading day at download.asic.gov.au/short-selling/RR<YYYYMMDD>-001-SSDailyAggShortPos.csv
(tab-separated). Days already saved are skipped, so it can run again to add new days. Requests are
spread over a few threads with a pause, to be polite.
Usage: python3 -I src/fetch_asic_shorts.py [data_dir] [--from YYYY-MM-DD]
"""
import csv
import gzip
import io
import os
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta

URL = "https://download.asic.gov.au/short-selling/RR{d}-001-SSDailyAggShortPos.csv"
START = date(2010, 6, 16)
UA = "paper-portfolio research (cameron.rodger.nz@gmail.com)"
lock = threading.Lock()


def decode(raw: bytes) -> str:
    if raw[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return raw.decode("utf-16")
    for enc in ("utf-8-sig", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1", errors="replace")


def num(x: str) -> str:
    x = (x or "").strip().replace(",", "")
    try:
        return str(int(float(x)))
    except ValueError:
        return ""


def fetch(d: date) -> tuple[str, list[tuple] | None, str]:
    url = URL.format(d=d.strftime("%Y%m%d"))
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                text = decode(r.read())
            break
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return d.isoformat(), None, "none"
            if attempt == 2:
                return d.isoformat(), None, f"HTTP {e.code}"
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            if attempt == 2:
                return d.isoformat(), None, type(e).__name__
        time.sleep(3 * (attempt + 1))
    rows = []
    lines = text.splitlines()
    sep = "\t" if lines and "\t" in lines[0] else ","
    for rec in csv.reader(io.StringIO("\n".join(lines[1:])), delimiter=sep):
        if len(rec) < 4 or not rec[1].strip():
            continue
        rows.append((d.isoformat(), rec[1].strip().upper(), num(rec[2]), num(rec[3])))
    return d.isoformat(), rows, "ok"


def main(data_dir: str = "data", start: date = START) -> int:
    out = os.path.join(data_dir, "asic")
    os.makedirs(out, exist_ok=True)
    have = {}
    for y in range(start.year, date.today().year + 1):
        p = os.path.join(out, f"shorts_{y}.csv.gz")
        if os.path.exists(p):
            with gzip.open(p, "rt", newline="") as f:
                have[y] = list(csv.reader(f))[1:]
    done = {r[0] for rows in have.values() for r in rows}
    missing_path = os.path.join(out, "no_file.txt")
    known_none = set(open(missing_path).read().split()) if os.path.exists(missing_path) else set()
    todo, d = [], start
    while d <= date.today() - timedelta(days=4):          # ASIC publishes about four business days late
        if d.weekday() < 5 and d.isoformat() not in done and d.isoformat() not in known_none:
            todo.append(d)
        d += timedelta(days=1)
    print(f"{len(todo)} days to fetch")
    got, none, bad = 0, [], []

    def work(dd):
        time.sleep(0.15)
        return fetch(dd)
    with ThreadPoolExecutor(4) as ex:
        for ds, rows, status in ex.map(work, todo):
            if rows:
                have.setdefault(int(ds[:4]), []).extend(rows); got += 1
            elif status == "none":
                none.append(ds)
            else:
                bad.append(f"{ds} {status}")
    for y, rows in have.items():
        rows.sort()
        with gzip.open(os.path.join(out, f"shorts_{y}.csv.gz"), "wt", newline="") as f:
            w = csv.writer(f); w.writerow(["date", "code", "short", "issue"]); w.writerows(rows)
    # weekdays with no file (holidays) are remembered so they aren't asked for again; older than 30 days only
    old = {x for x in none if x < (date.today() - timedelta(days=30)).isoformat()}
    open(missing_path, "w").write("\n".join(sorted(known_none | old)) + "\n")
    msg = f"saved {got} new days; {len(none)} weekdays had no file (holidays); {len(bad)} failed" + (": " + ", ".join(bad[:20]) if bad else "")
    open(os.path.join(out, "last_run.txt"), "w").write(msg + "\n")
    print(msg)
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    st = date.fromisoformat(a[a.index("--from") + 1]) if "--from" in a else START
    pos = [x for i, x in enumerate(a) if not x.startswith("--") and (i == 0 or not a[i - 1].startswith("--"))]
    sys.exit(main(pos[0] if pos else "data", st))
