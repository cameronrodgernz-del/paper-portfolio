"""Nightly end-of-day prices from providers that permit automated use.

US: Tiingo (free plan: 1,000 requests a day, 500 symbols a month, personal use). Every symbol
asked of Tiingo is recorded by month (data/tiingo_symbols_<YYYY-MM>.txt for the nightly job,
data/history/... for the history samples); --tiingo-month-cap N stops a run from taking the
month's total of different symbols past N, so the history samples never crowd out nightly prices.
ASX: EODHD. The day's allowance is read from EODHD's account endpoint, so a paid plan is used
in full without a code change; if it can't be read, the free plan's 20 a day is assumed.
Keys come from the environment (TIINGO_API_KEY, EODHD_API_KEY); in GitHub they are
repository secrets, so they never sit in the code or the chat.

Each share is kept in data/prices/<market>/<ticker>.csv with unadjusted open, high,
low, close and volume (fills use these), plus dividend and split fields where the
provider gives them. Only dates after the last stored date are requested, and a session is stored only once its
prices are final.
Usage: python3 -I src/fetch_prices.py <universe.csv> [data_dir] [--start YYYY-MM-DD] [--once]
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
EODHD_DAILY_BUDGET = 20     # the free plan; used only when the account endpoint can't be read
EODHD_RUN_MAX = 500
TIINGO_RUN_BUDGET = 45      # free plan: 50 requests an hour
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def eodhd_budget(key: str | None) -> int:
    """Requests left today on the EODHD account; 20 (the free plan) if it can't be read."""
    if not key:
        return 0
    try:
        return budget_from_user(http_json(f"https://eodhd.com/api/user?api_token={key}&fmt=json"))
    except Exception:
        return EODHD_DAILY_BUDGET


def budget_from_user(u: dict, today_utc: str | None = None) -> int:
    """Requests left today from EODHD's account record. apiRequests keeps the last active day's count
    until a request is made after midnight UTC, so a count dated before today (UTC) means none used."""
    today_utc = today_utc or datetime.now(timezone.utc).date().isoformat()
    used = int(u.get("apiRequests") or 0)
    on = str(u.get("apiRequestsDate") or "")[:10]
    if on and on != today_utc:
        used = 0
    return max(0, min(EODHD_RUN_MAX, int(u["dailyRateLimit"]) - used))


def eodhd_limit(key: str | None, cache: str | None = None) -> int:
    """The account's daily request limit (20 on the free plan), or 0 if it can't be read. With a cache
    file, the account is asked at most once a UTC day, in case asking counts against the allowance."""
    if not key:
        return 0
    today = datetime.now(timezone.utc).date().isoformat()
    if cache and os.path.exists(cache):
        parts = open(cache).read().split()
        if len(parts) == 2 and parts[0] == today and parts[1].isdigit():
            return int(parts[1])
    try:
        n = int(http_json(f"https://eodhd.com/api/user?api_token={key}&fmt=json")["dailyRateLimit"])
    except Exception:
        return 0
    if cache:
        os.makedirs(os.path.dirname(cache) or ".", exist_ok=True)
        open(cache, "w").write(f"{today} {n}\n")
    return n


def tiingo_month_files(month: str) -> list[str]:
    return [os.path.join(ROOT, "data", f"tiingo_symbols_{month}.txt"),
            os.path.join(ROOT, "data", "history", f"tiingo_symbols_{month}.txt")]


def tiingo_month_symbols(month: str) -> set[str]:
    out = set()
    for p in tiingo_month_files(month):
        if os.path.exists(p):
            out |= {x.strip() for x in open(p) if x.strip()}
    return out


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


def main(universe: str, data_dir: str = "data", start_default: str | None = None, once: bool = False,
         tiingo_month_cap: int | None = None, eodhd_min_limit: int | None = None) -> int:
    """`start_default`: first date for a share with no file yet (default: a year ago).
    `once`: fetch each share a single time and never top it up (for the history tests).
    `tiingo_month_cap`: the most different symbols Tiingo may have been asked for this month."""
    tiingo, eodhd = os.environ.get("TIINGO_API_KEY"), os.environ.get("EODHD_API_KEY")
    month = datetime.now(timezone.utc).strftime("%Y-%m")
    used = tiingo_month_symbols(month)
    track = os.path.join(data_dir, f"tiingo_symbols_{month}.txt")
    eodhd_left = None
    start_default = start_default or (date.today() - timedelta(days=365)).isoformat()
    eodhd_calls, tiingo_calls, problems, report = 0, 0, [], []
    if eodhd_min_limit and eodhd and eodhd_limit(eodhd, os.path.join(data_dir, "eodhd_plan.txt")) < eodhd_min_limit:
        eodhd_left = 0          # a history fetch never spends the free plan's 20 a day, which the nightly prices need
        problems.append(f"EODHD plan allows fewer than {eodhd_min_limit} requests a day: history prices wait for the paid plan")
    names, seen = [], set()
    for u in universe.split(","):
        with open(u, newline="") as f:
            for n in csv.DictReader(f):
                if (n["market"], n["ticker"]) not in seen:
                    seen.add((n["market"], n["ticker"])); names.append(n)
    # On EODHD's free plan (20 requests a day) the core fund and the live deals' shares go first, then
    # the stalest; the rest wait for tomorrow, and each request returns every missing day, so nothing
    # is lost.
    first = {("ASX", "VAS")}
    for r in (csv.DictReader(open(os.path.join(ROOT, "config", "live_deals.csv"), newline="")) if os.path.exists(os.path.join(ROOT, "config", "live_deals.csv")) else []):
        first.add((r["target_market"], r["target_ticker"]))
        if r.get("acquirer_ticker"):
            first.add((r.get("acquirer_market") or "", r["acquirer_ticker"]))
    def staleness(n):
        last = last_date(os.path.join(data_dir, "prices", n["market"], f"{n['ticker']}.csv"))
        return (n["provider"] != "eodhd", (n["market"], n["ticker"]) not in first, last or "")
    names.sort(key=staleness)
    for n in names:
        path = os.path.join(data_dir, "prices", n["market"], f"{n['ticker']}.csv")
        after = last_date(path)
        if once and (after or os.path.exists(path + ".none")):
            continue
        start = (date.fromisoformat(after) + timedelta(days=1)).isoformat() if after else start_default
        try:
            if n["provider"] == "tiingo":
                if not tiingo:
                    problems.append(f"{n['ticker']}: no TIINGO_API_KEY"); continue
                if tiingo_calls >= TIINGO_RUN_BUDGET:
                    problems.append(f"{n['ticker']}: Tiingo hourly budget used"); continue
                sym = n["provider_symbol"].upper()
                if tiingo_month_cap is not None and sym not in used and len(used) >= tiingo_month_cap:
                    problems.append(f"{n['ticker']}: Tiingo monthly symbol cap ({tiingo_month_cap}) reached"); continue
                if sym not in used:
                    used.add(sym)
                    os.makedirs(os.path.dirname(track) or ".", exist_ok=True)
                    with open(track, "a") as tf:
                        tf.write(sym + "\n")
                tiingo_calls += 1
                url = (f"https://api.tiingo.com/tiingo/daily/{urllib.parse.quote(n['provider_symbol'])}/prices"
                       f"?startDate={start}")
                rows = parse_tiingo(http_json(url, {"Content-Type": "application/json",
                                                    "Authorization": f"Token {tiingo}"}))
            elif n["provider"] == "eodhd":
                if not eodhd:
                    problems.append(f"{n['ticker']}: no EODHD_API_KEY"); continue
                if eodhd_left is None:
                    eodhd_left = eodhd_budget(eodhd)
                if eodhd_calls >= eodhd_left:
                    problems.append(f"{n['ticker']}: EODHD daily budget used"); continue
                url = (f"https://eodhd.com/api/eod/{urllib.parse.quote(n['provider_symbol'])}"
                       f"?api_token={eodhd}&fmt=json&from={start}")
                eodhd_calls += 1
                rows = parse_eodhd(http_json(url))
            else:
                problems.append(f"{n['ticker']}: unknown provider {n['provider']}"); continue
            added = append(path, rows, after, n["market"])
            if once and not added:     # remember a share with no data, so it isn't asked for again
                os.makedirs(os.path.dirname(path), exist_ok=True)
                open(path + ".none", "w").write(date.today().isoformat())
            report.append(f"{n['market']}:{n['ticker']} +{added}")
        except Exception as e:  # keep going; the clerk sees the problem list
            problems.append(f"{n['ticker']}: {type(e).__name__}: {str(e)[:120]}")
            if once and "404" in str(e):
                os.makedirs(os.path.dirname(path), exist_ok=True)
                open(path + ".none", "w").write(date.today().isoformat())
    os.makedirs(os.path.join(data_dir, "prices"), exist_ok=True)
    with open(os.path.join(data_dir, "prices", "last_run.txt"), "w") as f:
        f.write(f"run {date.today().isoformat()}\n" + "\n".join(report) +
                ("\nPROBLEMS:\n" + "\n".join(problems) if problems else "\nno problems") + "\n")
    print("\n".join(report)); print("problems:", problems or "none")
    return 0


if __name__ == "__main__":
    # python3 -I src/fetch_prices.py <universe> [data_dir] [--start YYYY-MM-DD] [--once]
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    start = next((sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == "--start"), None)
    cap = next((sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == "--tiingo-month-cap"), None)
    emin = next((sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == "--eodhd-min-limit"), None)
    args = [a for a in args if a not in (start, cap, emin)]
    sys.exit(main(args[0], args[1] if len(args) > 1 else "data", start, "--once" in sys.argv,
                  int(cap) if cap else None, int(emin) if emin else None))
