"""Checks for the US deal history test on made-up prices. Run: python3 -I tests/test_deal_history.py"""
import os
import sys
from datetime import date, timedelta

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "src"))
sys.path.insert(0, os.path.join(ROOT, "src", "history"))
from us_deal_test import event_result  # noqa: E402

fails = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (f"  [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)


def path(start, closes):
    out, d = [], date.fromisoformat(start)
    for c in closes:
        while d.weekday() >= 5:
            d += timedelta(days=1)
        out.append({"date": d.isoformat(), "open": c, "high": c * 1.002, "low": c * 0.998, "close": c, "volume": 1e6,
                    "aopen": c, "aclose": c})
        d += timedelta(days=1)
    return out


bills = [("2015-01-01", 0.02)]
pre = [7.0] * 70                                   # undisturbed, then the deal at 10.00 cash
px = path("2016-01-04", pre + [9.70] * 60 + [9.90] * 20 + [9.98] * 5)
ev = {"ticker": "TGT", "date": px[70]["date"], "cash_price": "10.00"}
st, r = event_result(ev, px, "2026-10-30", bills)
check("a deal that converges and stops trading counts as completed", st == "ok" and r["kind"] == "completed", (st, r and r["kind"]))
if r:
    check("completion is paid at the cash price (above the last close)", abs(r["gross"] - (10.0 / 9.70 - 1)) < 1e-9, r["gross"])
    check("no sale costs on completion", abs(r["costs"] - (5 / 2300 + r["costs"] - 5 / 2300)) < 1e-12 and r["costs"] < 0.01, r["costs"])
    check("cash over the holding days is deducted", r["cash"] > 0 and abs(r["net"] - (r["gross"] - r["costs"] - r["cash"])) < 1e-12)
    check("market-implied chance uses the price 60 sessions before", abs(r["implied"] - (9.70 - 7.0) / (10.0 - 7.0)) < 1e-9, r["implied"])
brk = path("2016-01-04", pre + [9.70] * 30 + [8.00] * 2 + [7.50] * 200)
st, r = event_result(ev, brk, "2026-10-30", bills)
check("a fall more than 15% below the cash price is a break, sold at the next open", st == "ok" and r["kind"] == "break" and r["gross"] < -0.15, (st, r))
far = path("2016-01-04", pre + [8.0] * 50)
check("an entry far below the cash price is left out (not a confirmed cash deal)",
      event_result(ev, far, "2026-10-30", bills)[0].startswith("entry price outside"))
live = path("2026-03-02", pre + [9.70] * 100)
ev2 = {"ticker": "TGT", "date": live[70]["date"], "cash_price": "10.00"}
check("a deal still trading and under 400 days is not resolved yet", event_result(ev2, live, live[-1]["date"], bills)[0] == "not resolved yet")
print("\nALL PASS" if not fails else f"\n{len(fails)} FAILED: {fails}")
sys.exit(1 if fails else 0)
