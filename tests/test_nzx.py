"""Checks for the NZX rules (rulebook section 7: NZX volumes unknown). Run: python3 -I tests/test_nzx.py"""
import os
import sys
import tempfile

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "src"))
from clerk import place_order, run, state  # noqa: E402
from ledger import Ledger  # noqa: E402
from market_data import FX, NZX_SMALL_FLOOR, Prices  # noqa: E402
from risk import check_order  # noqa: E402

fails = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (f"  [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)


def write(d, ticker, rows):
    os.makedirs(os.path.join(d, "prices", "NZX"), exist_ok=True)
    with open(os.path.join(d, "prices", "NZX", f"{ticker}.csv"), "w") as f:
        f.write("date,open,high,low,close,volume,adj_close,dividend,split,source\n")
        for r in rows:
            f.write(",".join(str(x) for x in r) + ",,,,,finfeed\n")


with tempfile.TemporaryDirectory() as d:
    import shutil
    shutil.copytree(os.path.join(ROOT, "data", "fx"), os.path.join(d, "fx"))
    days = ["2026-10-%02d" % x for x in (1, 2, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23)]
    rows = [(dd, 1.00, 1.02, 0.99, 1.01, "") for dd in days[:-3]]
    rows += [(days[-3], 1.0, 1.0, 1.0, 1.0, ""), (days[-2], 1.0, 1.0, 1.0, 1.0, ""), (days[-1], 1.00, 1.03, 0.99, 1.02, "")]
    write(d, "XYZ", rows)
    prices, fx = Prices(d), FX(d)
    st = prices.stats("NZX", "XYZ", "2026-10-21", 1.0)
    check("NZX stats mark traded value as unknown", st["median_value_nzd"] is None and st["adv_local"] is None, st)
    check("a smaller NZX company is charged at least the 0.6% gap", st["spread"] >= NZX_SMALL_FLOOR, st["spread"])
    L = Ledger(os.path.join(d, "ledger"))
    L.append("cash", {"kind": "deposit", "ccy": "NZD", "amount": 100000.0}, ts="2026-10-01T00:00:00Z")
    place_order(L, prices, fx, "2026-10-20T08:30:00Z", "special", "NZX", "XYZ", "buy", value_nzd=2500)
    for dd in ("2026-10-21", "2026-10-22", "2026-10-23"):
        run(L, prices, fx, dd, {"cash_rate": 0.02})
    nofill = [r["payload"]["reason"] for r in L.records("orders") if r["payload"].get("event") == "no_fill"]
    fills = [r["payload"] for r in L.records("fills")]
    check("an NZX day with no price movement is taken as no trading", any("no price movement" in x for x in nofill), nofill)
    check("an NZX order fills on a day the price moved, with no volume cap", fills and fills[0]["qty"] == 2475 and fills[0]["date"] == "2026-10-23",
          [(f["date"], f["qty"]) for f in fills])
    val = {"total_nzd": 100000.0, "cash_nzd_total": 50000.0, "by_sleeve": {}, "positions": []}
    r = check_order(val, 0.0, "special", "NZX", "XYZ", "buy", 4000, 1.0, industry="x")
    check("an order over NZ$2,500 in a smaller NZX company is refused", any("NZ$2,500" in x for x in r), r)
    r = check_order(val, 0.0, "special", "NZX", "XYZ", "buy", 2500, 1.0, industry="x")
    check("an order of NZ$2,500 passes", r == [], r)
print("\nALL PASS" if not fails else f"\n{len(fails)} FAILED: {fails}")
sys.exit(1 if fails else 0)
