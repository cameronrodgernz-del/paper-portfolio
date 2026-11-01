"""NZX end-of-day prices from FinFeedAPI (exchange XNZE), paid by usage credits.

- Symbols are ISINs; the NZX code comes from FinFeedAPI's symbol list and is kept in
  config/nzx_isins.csv (refreshed weekly).
- Each night, one request per missing trading day returns the whole exchange (about 250 shares,
  about 3 credits); every ordinary share is appended to data/prices/NZX/<code>.csv.
- --backfill-from YYYY-MM-DD loads each share's history (one request each, the feed starts in
  July 2023), a few dozen shares a run, until all are done.
- The feed carries no trading volume (it reports zero), so the volume column is left blank. The
  fill rules treat NZX volume as unknown, not as no trading (rulebook section 7).
- FinFeedAPI's starting tier allows 10 requests a minute, so requests are spaced 7 seconds apart.
- Dates: FinFeedAPI labels each NZX session with the UTC date on which it opens, which is the evening
  before in New Zealand (10am NZ is 9pm or 10pm UTC the day before). Its bar labelled D is the NZX
  session of D + 1, so every date is moved forward a day here (checked against the same companies'
  ASX prices on 1 Nov 2026: daily moves line up on D + 1 and not on D).
Key: FINFEED_API_KEY. Usage: python3 -I src/fetch_nzx.py [data_dir] [--backfill-from DATE] [--max-requests N]
"""
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from market_data import closed_by  # noqa: E402

BASE = "https://api-historical.stock.finfeedapi.com"
PAUSE = 7.0
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP = os.path.join(ROOT, "config", "nzx_isins.csv")
FIELDS = ["date", "open", "high", "low", "close", "volume", "adj_close", "dividend", "split", "source"]
NOT_SHARES = re.compile(r"\b(futures?|calls?|puts?|options?|warrants?|rights?|notes?|bonds?|pref|preference|capital notes|perpetual)\b"
                        r"|\d+(\.\d+)?%", re.I)   # a coupon rate marks a bond even when the name doesn't say so


class Feed:
    def __init__(self, key: str, max_requests: int):
        self.key, self.left, self.used = key, max_requests, 0

    def get(self, path: str):
        if self.left <= 0:
            raise RuntimeError("request budget for this run used")
        if self.used:
            time.sleep(PAUSE)
        self.left -= 1
        self.used += 1
        req = urllib.request.Request(BASE + path, headers={"Authorization": self.key, "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read().decode())


def nz_date(label: str) -> str:
    """The NZX session date of a FinFeedAPI bar: its UTC label plus one day."""
    return (date.fromisoformat(label[:10]) + timedelta(days=1)).isoformat()


def day_rows(feed: Feed, d: str) -> list[dict]:
    """Every share's bar for the NZX session on NZ date d (FinFeedAPI labels it d - 1)."""
    label = (date.fromisoformat(d) - timedelta(days=1)).isoformat()
    return feed.get(f"/v1/ohlcv/exchange/XNZE/history?period_id=1DAY&time_start={label}T00:00:00&time_end={d}T00:00:00&limit=2000")


def load_map() -> dict:
    if not os.path.exists(MAP):
        return {}
    return {r["isin"]: r for r in csv.DictReader(open(MAP, newline=""))}


def refresh_map(feed: Feed, isins: list[str]) -> dict:
    """Look up the NZX code and name of each ISIN, 40 at a time."""
    known = load_map()
    todo = [i for i in isins if i not in known]
    for k in range(0, len(todo), 40):
        batch = todo[k:k + 40]
        for r in feed.get(f"/v1/symbols/XNZE?filter_symbol_id={','.join(batch)}&limit=100") or []:
            known[r["symbol_id"]] = {"isin": r["symbol_id"], "ticker": (r.get("name_ticker") or "").strip(),
                                     "name": r.get("name", ""), "category": r.get("security_category", ""),
                                     "checked": date.today().isoformat()}
    os.makedirs(os.path.dirname(MAP), exist_ok=True)
    with open(MAP, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["isin", "ticker", "name", "category", "checked"])
        w.writeheader()
        w.writerows(sorted(known.values(), key=lambda r: r["ticker"]))
    return known


def is_share(m: dict) -> bool:
    return bool(m.get("ticker")) and re.fullmatch(r"[A-Z0-9]{2,6}", m["ticker"]) is not None and not NOT_SHARES.search(m.get("name", ""))


def last_date(path: str) -> str | None:
    if not os.path.exists(path):
        return None
    rows = list(csv.DictReader(open(path, newline="")))
    return rows[-1]["date"] if rows else None


def write_rows(path: str, rows: list[dict]) -> int:
    have = set()
    if os.path.exists(path):
        have = {r["date"] for r in csv.DictReader(open(path, newline=""))}
    new = sorted((r for r in rows if r["date"] not in have), key=lambda r: r["date"])
    if not new:
        return 0
    all_rows = (list(csv.DictReader(open(path, newline=""))) if os.path.exists(path) else []) + new
    all_rows.sort(key=lambda r: r["date"])
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(all_rows)
    return len(new)


def to_row(r: dict) -> dict:
    return {"date": nz_date(r["time_period_start"]), "open": r.get("price_open"), "high": r.get("price_high"),
            "low": r.get("price_low"), "close": r.get("price_close"), "volume": "", "adj_close": "", "dividend": "",
            "split": "", "source": "finfeed"}


def main(data_dir: str = "data", backfill_from: str | None = None, max_requests: int = 40) -> int:
    key = os.environ.get("FINFEED_API_KEY")
    if not key:
        print("no FINFEED_API_KEY"); return 0
    feed = Feed(key, max_requests)
    pdir = os.path.join(data_dir, "prices", "NZX")
    report, problems = [], []
    now = datetime.now(timezone.utc)
    try:
        # 1. the nightly days: every weekday after the last stored date whose session is final
        stored = [last_date(os.path.join(pdir, f)) for f in os.listdir(pdir) if f.endswith(".csv")] if os.path.isdir(pdir) else []
        start = max([d for d in stored if d] or ["2026-10-26"])
        d = date.fromisoformat(start) + timedelta(days=1)
        days = []
        while d <= now.date():
            if d.weekday() < 5 and closed_by("NZX", d.isoformat(), now):
                days.append(d.isoformat())
            d += timedelta(days=1)
        maps = load_map()
        for ds in days:
            rows = day_rows(feed, ds)
            if not rows:
                report.append(f"{ds}: no rows (a holiday, or not yet published)")
                continue
            isins = [r["symbol_id_exchange"] for r in rows]
            if any(i not in maps for i in isins):
                maps = refresh_map(feed, isins)
            n = 0
            for r in rows:
                m = maps.get(r["symbol_id_exchange"])
                if m and is_share(m):
                    n += write_rows(os.path.join(pdir, f"{m['ticker']}.csv"), [to_row(r)])
            report.append(f"{ds}: {n} shares")
        # 2. history, a few dozen shares a run
        if backfill_from:
            shares = sorted((m for m in load_map().values() if is_share(m)), key=lambda m: m["ticker"])
            for m in shares:
                path = os.path.join(pdir, f"{m['ticker']}.csv")
                done = os.path.exists(path + ".hist")
                if done:
                    continue
                hist = feed.get(f"/v1/ohlcv/exchange-symbol/XNZE/{m['isin']}/history?period_id=1DAY"
                                f"&time_start={backfill_from}T00:00:00&time_end={now.date().isoformat()}T00:00:00&limit=10000") or []
                rows = [to_row(r) for r in hist if closed_by("NZX", nz_date(r["time_period_start"]), now)]
                added = write_rows(path, rows)
                open(path + ".hist", "w").write(f"{backfill_from} {date.today().isoformat()} {len(rows)}")
                report.append(f"history {m['ticker']}: +{added}")
    except RuntimeError as e:
        problems.append(str(e))
    except urllib.error.HTTPError as e:
        problems.append(f"HTTP {e.code}: {e.read().decode(errors='replace')[:200]}")
    except Exception as e:
        problems.append(f"{type(e).__name__}: {str(e)[:200]}")
    os.makedirs(pdir, exist_ok=True)
    with open(os.path.join(pdir, "last_run.txt"), "w") as f:
        f.write(f"run {now:%Y-%m-%d %H:%M} UTC, {feed.used} requests\n" + "\n".join(report) +
                ("\nPROBLEMS:\n" + "\n".join(problems) if problems else "\nno problems") + "\n")
    print("\n".join(report[-20:])); print("requests", feed.used, "problems", problems or "none")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    bf = a[a.index("--backfill-from") + 1] if "--backfill-from" in a else None
    mx = int(a[a.index("--max-requests") + 1]) if "--max-requests" in a else 40
    pos = [x for i, x in enumerate(a) if not x.startswith("--") and (i == 0 or not a[i - 1].startswith("--"))]
    sys.exit(main(pos[0] if pos else "data", bf, mx))
