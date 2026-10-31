"""Engine dry run on October 2026 prices (a test, not the practice run).
Buys a stand-in core (VAS on ASX, VT and SPY in the US) on 1 Oct and runs the clerk each weekday.
Checks: fill timing, fees, currency conversion, the ledger chain and the valuation.
Run: python3 -I tests/test_clerk.py"""
import os
import sys
import tempfile
from datetime import date, timedelta

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "src"))
from clerk import place_order, run, state  # noqa: E402
from ledger import Ledger  # noqa: E402
from market_data import FX, Prices  # noqa: E402

fails = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (f"  [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)


prices, fx = Prices(os.path.join(ROOT, "data")), FX(os.path.join(ROOT, "data"))
with tempfile.TemporaryDirectory() as d:
    L = Ledger(d)
    L.append("cash", {"kind": "deposit", "ccy": "NZD", "amount": 100000.0}, ts="2026-10-01T00:00:00Z")
    decided = "2026-10-01T06:30:00Z"     # 7:30pm NZ, 1 Oct
    o1 = place_order(L, prices, fx, decided, "core", "ASX", "VAS", "buy", value_nzd=10000)
    o2 = place_order(L, prices, fx, decided, "core", "US", "VT", "buy", value_nzd=20000)
    o3 = place_order(L, prices, fx, decided, "core", "US", "SPY", "buy", value_nzd=10000)
    reports = []
    day = date(2026, 10, 1)
    while day <= date(2026, 10, 30):
        if day.weekday() < 5:
            reports.append(run(L, prices, fx, day.isoformat(), {"cash_rate": 0.025}))
        day += timedelta(days=1)
    fills = {r["payload"]["ticker"]: r["payload"] for r in L.records("fills")}
    check("ASX order fills the next ASX session (2 Oct)", fills["VAS"]["date"] == "2026-10-02", fills["VAS"]["date"])
    check("US order fills the US session that opens after 7:30pm NZ (1 Oct US date)", fills["VT"]["date"] == "2026-10-01", fills["VT"]["date"])
    first_run_fills = reports[0]["fills"]
    check("nothing fills on the run that placed the orders", first_run_fills == [], first_run_fills)
    vas_bar = prices.bar_on("ASX", "VAS", "2026-10-02")
    check("buy fills above the open (spread and size)", fills["VAS"]["price"] > vas_bar.open, (fills["VAS"]["price"], vas_bar.open))
    check("an order larger than the plan's NZ$5,000 cover pays the capped fee", fills["VT"]["fee_local"] == 5.0, fills["VT"]["fee_local"])
    check("later orders pay capped fees", fills["VAS"]["fee_local"] in (15.0,) and fills["SPY"]["fee_local"] == 5.0,
          (fills["VAS"]["fee_local"], fills["SPY"]["fee_local"]))
    st = state(L)
    check("no negative cash in any currency", all(v >= -0.01 for v in st["cash"].values()), st["cash"])
    fx_fees = sum(r["payload"].get("fee_nzd", 0) for r in L.records("cash") if r["payload"]["kind"] == "fx_in")
    nzd_out = -sum(r["payload"]["amount"] for r in L.records("cash") if r["payload"]["kind"] == "fx_out")
    check("currency fee is 0.5% of the NZ$ converted", abs(fx_fees - 0.005 * nzd_out) < 0.05, (round(fx_fees, 2), round(nzd_out, 2)))
    vals = [r["payload"] for r in L.records("valuations")]
    check("one valuation per run", len(vals) == len(reports), (len(vals), len(reports)))
    check("valuation within 10% of the bankroll", 90000 < vals[-1]["total_nzd"] < 110000, vals[-1]["total_nzd"])
    check("ledger chain intact", all(v == "ok" for v in L.verify().values()), L.verify())
    print(f"\nEnd value {vals[-1]['total_nzd']:,.2f} NZD; cash {vals[-1]['cash_local']}; sleeves {vals[-1]['by_sleeve']}")
    for f in fills.values():
        print(f"  {f['date']} {f['ticker']} {f['qty']:g} @ {f['price']} fee {f['fee_local']} {f['ccy']} spread used {f['spread_used']}")
print("\nALL PASS" if not fails else f"\n{len(fails)} FAILED: {fails}")
sys.exit(1 if fails else 0)
