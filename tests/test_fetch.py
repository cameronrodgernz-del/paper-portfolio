"""Checks for the price fetcher's allowances: EODHD's daily allowance read from the account, and
Tiingo's monthly symbol cap shared between the nightly job and the history samples. No network:
the provider calls are replaced with stubs."""
import csv
import os
import sys
import tempfile
from datetime import datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
import fetch_prices as fp  # noqa: E402

fails = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail and not ok else ""))
    if not ok:
        fails.append(name)


bar = [{"date": "2026-10-28", "open": 1, "high": 1, "low": 1, "close": 1, "volume": 100}]
asked = []


def stub(url, headers=None):
    if "api/user" in url:
        if "BROKEN" in url:
            raise OSError("no account endpoint")
        return {"dailyRateLimit": 100000, "apiRequests": 12}
    asked.append(url)
    return bar


fp.http_json = stub
check("EODHD allowance read from the account (capped per run)", fp.eodhd_budget("KEY") == fp.EODHD_RUN_MAX)
check("EODHD allowance falls back to the free plan's 20", fp.eodhd_budget("BROKEN") == 20)
check("no EODHD key, no requests", fp.eodhd_budget(None) == 0)
check("a used count from an earlier UTC day counts as none used", fp.budget_from_user({"dailyRateLimit": 20, "apiRequests": 20, "apiRequestsDate": "2026-11-01"}, "2026-11-02") == 20)
check("today's used count is taken off", fp.budget_from_user({"dailyRateLimit": 20, "apiRequests": 15, "apiRequestsDate": "2026-11-02"}, "2026-11-02") == 5)
check("an undated count is taken off", fp.budget_from_user({"dailyRateLimit": 20, "apiRequests": 15}, "2026-11-02") == 5)
with tempfile.TemporaryDirectory() as d:
    c = os.path.join(d, "eodhd_plan.txt")
    n1 = fp.eodhd_limit("KEY", c)
    fp.http_json = lambda url, headers=None: (_ for _ in ()).throw(OSError("asked again"))
    check("the plan limit is asked for once a day and then read from the cache", n1 == 100000 and fp.eodhd_limit("KEY", c) == 100000)
    fp.http_json = stub

with tempfile.TemporaryDirectory() as root:
    fp.ROOT = root
    month = datetime.now(timezone.utc).strftime("%Y-%m")
    os.makedirs(os.path.join(root, "data", "history"))
    # the nightly job has already asked for two symbols this month
    open(os.path.join(root, "data", f"tiingo_symbols_{month}.txt"), "w").write("VT\nENZL\n")
    uni = os.path.join(root, "u.csv")
    with open(uni, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ticker", "market", "provider", "provider_symbol", "why"])
        w.writeheader()
        for t in ("AAA", "BBB", "CCC", "VT"):
            w.writerow({"ticker": t, "market": "US", "provider": "tiingo", "provider_symbol": t, "why": "test"})
    os.environ["TIINGO_API_KEY"] = "x"
    hist = os.path.join(root, "data", "history")
    fp.main(uni, hist, "2010-01-01", once=True, tiingo_month_cap=4)
    got = sorted(os.path.basename(u.split("/prices")[0]) for u in asked)
    check("the cap stops new symbols once the month's total reaches it", got == ["AAA", "BBB", "VT"], got)
    rec = open(os.path.join(hist, f"tiingo_symbols_{month}.txt")).read().split()
    check("symbols asked by the history run are recorded in its own file", rec == ["AAA", "BBB"], rec)
    check("the month's total counts both files", fp.tiingo_month_symbols(month) == {"VT", "ENZL", "AAA", "BBB"})

print("\nALL PASS" if not fails else f"\n{len(fails)} FAILED: {fails}")
sys.exit(1 if fails else 0)
