"""Nightly end-of-day prices from providers that permit automated use.

US: Tiingo (free plan: 1,000 requests a day, 500 symbols a month, personal use).
NZX and ASX: EODHD (free plan: 20 requests a day, one year of history).
Keys come from the environment (TIINGO_API_KEY, EODHD_API_KEY); in GitHub they are
repository secrets, so they never sit in the code or the chat.

Each share is kept in data/prices/<market>/<ticker>.csv with unadjusted open, high,
low, close and volume (fills use these), plus dividend and split fields where the
provider gives them. Only dates after the last stored date are requested, and a session is stored only once its
prices are final.
Usage: python3 -I src/fetch_prices.py <universe.csv> [data_dir]
"""
import csv
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from market_data import closed_by  # noqa: E402

FIELDS = ["date", "open", "high", "low", "close", "volume", "adj_close", "dividend", "split", "source"]
EODHD_DAILY_BUDGET = 20
TIINGO_RUN_BUDGET = 45      # free plan: 50 requests an hour


def http_json(url: str, headers: dict | None = None):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def parse_tiingo(rows: list[dict]) -> list[dict]:
    return [{"date": r["date"][:10], "open": r.get("open"), "high": r.get("high"), "low": r.get("low"),
             "close": r.get("close"), "volume": r.get("volume"), "adj_close": r.get("adjClose"),
             "dividend": r.get("divCash", 0) or 0, "split": r.get("splitFactor", 1) or 1, "source": "tiingo"}
            for r in rows]


def parse_eodhd(rows: list[dict]) -> list[dict]:
    return [{"date": r["date"][:10], "open": r.get("open"), "high": r.get("high"), "low": r.get("low"),
             "close": r.get("close"), "volume": r.get("volume"), "adj_close": r.get("adjusted_close"),
             "dividend": "", "split": "", "source": "eodhd"} for r in rows]


def last_date(path: str) -> str | None:
    if not os.path.exists(path):
        return None
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    return rows[-1]["date"] if rows else None


def append(path: str, rows: list[dict], after: str | None, market: str | None = None,
           now_utc: datetime | None = None) -> int:
    """Add rows dated after `after`. A session whose prices are not yet final (a run during
    trading hours) is held back, so a part-day bar is never stored as the day's close."""
    new = [r for r in rows if (after is None or r["date"] > after)
           and (market is None or closed_by(market, r["date"], now_utc or datetime.now(timezone.utc)))]
    seen, clean = set(), []
    for r in sorted(new, key=lambda x: x["date"]):
        if r["date"] in seen:          # providers sometimes repeat the latest bar
            continue
        seen.add(r["date"])
        clean.append(r)
    exists = os.path.exists(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if not exists:
            w.writeheader()
        w.writerows(clean)
    return len(clean)


def main(universe: str, data_dir: str = "data") -> int:
    tiingo, eodhd = os.environ.get("TIINGO_API_KEY"), os.environ.get("EODHD_API_KEY")
    start_default = (date.today() - timedelta(days=365)).isoformat()
    eodhd_calls, tiingo_calls, problems, report = 0, 0, [], []
    names, seen = [], set()
    for u in universe.split(","):
        with open(u, newline="") as f:
            for n in csv.DictReader(f):
                if (n["market"], n["ticker"]) not in seen:
                    seen.add((n["market"], n["ticker"])); names.append(n)
    # EODHD's free plan allows 20 requests a day, so the stalest shares go first and the
    # rest wait for tomorrow; each request returns every missing day, so nothing is lost.
    def staleness(n):
        last = last_date(os.path.join(data_dir, "prices", n["market"], f"{n['ticker']}.csv"))
        return (n["provider"] != "eodhd", last or "")
    names.sort(key=staleness)
    for n in names:
        path = os.path.join(data_dir, "prices", n["market"], f"{n['ticker']}.csv")
        after = last_date(path)
        start = (date.fromisoformat(after) + timedelta(days=1)).isoformat() if after else start_default
        try:
            if n["provider"] == "tiingo":
                if not tiingo:
                    problems.append(f"{n['ticker']}: no TIINGO_API_KEY"); continue
                if tiingo_calls >= TIINGO_RUN_BUDGET:
                    problems.append(f"{n['ticker']}: Tiingo hourly budget used"); continue
                tiingo_calls += 1
                url = (f"https://api.tiingo.com/tiingo/daily/{urllib.parse.quote(n['provider_symbol'])}/prices"
                       f"?startDate={start}")
                rows = parse_tiingo(http_json(url, {"Content-Type": "application/json",
                                                    "Authorization": f"Token {tiingo}"}))
            elif n["provider"] == "eodhd":
                if not eodhd:
                    problems.append(f"{n['ticker']}: no EODHD_API_KEY"); continue
                if eodhd_calls >= EODHD_DAILY_BUDGET:
                    problems.append(f"{n['ticker']}: EODHD daily budget used"); continue
                url = (f"https://eodhd.com/api/eod/{urllib.parse.quote(n['provider_symbol'])}"
                       f"?api_token={eodhd}&fmt=json&from={start}")
                eodhd_calls += 1
                rows = parse_eodhd(http_json(url))
            else:
                problems.append(f"{n['ticker']}: unknown provider {n['provider']}"); continue
            added = append(path, rows, after, n["market"])
            report.append(f"{n['market']}:{n['ticker']} +{added}")
        except Exception as e:  # keep going; the clerk sees the problem list
            problems.append(f"{n['ticker']}: {type(e).__name__}: {str(e)[:120]}")
    os.makedirs(os.path.join(data_dir, "prices"), exist_ok=True)
    with open(os.path.join(data_dir, "prices", "last_run.txt"), "w") as f:
        f.write(f"run {date.today().isoformat()}\n" + "\n".join(report) +
                ("\nPROBLEMS:\n" + "\n".join(problems) if problems else "\nno problems") + "\n")
    print("\n".join(report)); print("problems:", problems or "none")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "data"))
