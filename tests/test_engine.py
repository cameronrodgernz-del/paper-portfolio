"""Checks for the cost, spread, fill and ledger rules. Run: python3 -I tests/test_engine.py"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from costs import PlanState, brokerage, fx_convert  # noqa: E402
from fills import Bar, fill_order  # noqa: E402
from ledger import Ledger  # noqa: E402
from spreads import cs_two_day, spread_estimate  # noqa: E402

failures = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (f"  [{detail}]" if detail else ""))
    if not cond:
        failures.append(name)


# Brokerage: plan covers the first NZ$5,000 a month, then 1.9% capped.
p = PlanState(); p.roll("2027-02")
check("plan covers first order", brokerage("NZX", 2500, 2500, p) == 0.0)
check("plan covers to NZ$5,000", brokerage("NZX", 2500, 2500, p) == 0.0)
check("NZX cap after plan", brokerage("NZX", 4000, 4000, p) == 25.0)
check("NZX 1.9% below cap", brokerage("NZX", 1000, 1000, p) == 19.0)
check("ASX cap A$15", brokerage("ASX", 3000, 3300, p) == 15.0)
check("US cap US$5", brokerage("US", 2000, 3400, p) == 5.0)
p2 = PlanState(); p2.roll("2027-03"); p2.used_nzd = 4000
fee = brokerage("NZX", 2000, 2000, p2)
check("straddling order pays on uncovered half only", fee == 19.0, fee)
check("new month resets plan", p2.roll("2027-04") and p2.used_nzd == 0)

# Currency: 0.5% off the amount entered.
got, fee = fx_convert(10000, 0.57)
check("fx fee 0.5%", fee == 50.0 and abs(got - 9950 * 0.57) < 1e-9, (got, fee))

# Spreads: flat ranges give zero before the floor; floors by liquidity.
check("cs zero on identical days", cs_two_day(10, 10, 10, 10) == 0.0)
s = spread_estimate([10.1] * 22, [9.9] * 22, 10_000_000)
check("spread floor liquid", s >= 0.001, s)
check("spread floor thin", spread_estimate([1.0] * 22, [1.0] * 22, 50_000) == 0.015)

# Fills.
bar = Bar("2027-02-02", 2.00, 2.10, 1.95, 2.05, 1_000_000)
f = fill_order("buy", 10_000, bar, spread=0.004, adv_value=2_000_000, daily_vol=0.02)
check("market buy above open", f.price > 2.00 and f.qty == 10_000, f)
f = fill_order("sell", 10_000, bar, spread=0.004, adv_value=2_000_000, daily_vol=0.02)
check("market sell below open", f.price < 2.00, f)
f = fill_order("buy", 200_000, bar, spread=0.004, adv_value=2_000_000, daily_vol=0.02)
check("volume cap 10%", f.qty == 100_000 and f.remaining == 100_000, f)
f = fill_order("buy", 1000, bar, 0.004, 2_000_000, 0.02, limit=1.96)
check("limit buy traded through", f.qty == 1000 and f.price == 1.96, f)
f = fill_order("buy", 1000, bar, 0.004, 2_000_000, 0.02, limit=1.951)
check("limit buy only touched: no fill", f.qty == 0, f)
f = fill_order("buy", 1000, bar, 0.004, 2_000_000, 0.02, limit=2.05)
check("limit buy opened better", f.qty == 1000 and 2.00 < f.price <= 2.05, f)
f = fill_order("buy", 1000, Bar("2027-02-03", 0, 0, 0, 0, 0), 0.004, 1, 0.02)
check("no trading no fill", f.qty == 0 and f.reason == "no trading")

# Ledger: tamper shows up.
with tempfile.TemporaryDirectory() as d:
    L = Ledger(d)
    L.append("decisions", {"id": 1, "thesis": "test"})
    L.append("decisions", {"id": 2, "thesis": "test 2"})
    check("ledger verifies", L.verify()["decisions"] == "ok")
    path = os.path.join(d, "decisions.jsonl")
    txt = open(path).read().replace("test 2", "edited")
    open(path, "w").write(txt)
    check("ledger catches an edit", L.verify()["decisions"].startswith("broken"))

print("\n", "ALL PASS" if not failures else f"{len(failures)} FAILED: {failures}")
sys.exit(1 if failures else 0)
