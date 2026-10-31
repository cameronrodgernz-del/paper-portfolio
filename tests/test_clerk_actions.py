"""Corporate actions, cash and repeat-run checks for the clerk, on October 2026 prices.
These cover the findings of the engine review of 1 Nov 2026. Run: python3 -I tests/test_clerk_actions.py"""
import os
import sys
import tempfile
from datetime import date

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "src"))
from clerk import business_days, place_order, run, state  # noqa: E402
from daily import drawdown_rules, weekdays  # noqa: E402
from decide import review_pending  # noqa: E402
from ledger import Ledger  # noqa: E402
from market_data import FX, Prices  # noqa: E402

fails = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (f"  [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)


prices, fx = Prices(os.path.join(ROOT, "data")), FX(os.path.join(ROOT, "data"))
CFG = {"cash_rate": 0.03}


def days(L, a, b):
    out = []
    for d in weekdays(date.fromisoformat(a), date.fromisoformat(b)):
        out.append(run(L, prices, fx, d.isoformat(), CFG))
    return out


# 1. A split: runs carry on, the holding doubles, orders on the share are cancelled
with tempfile.TemporaryDirectory() as d:
    L = Ledger(d)
    L.append("cash", {"kind": "deposit", "ccy": "NZD", "amount": 100000.0}, ts="2026-10-01T00:00:00Z")
    place_order(L, prices, fx, "2026-10-01T08:30:00Z", "core", "ASX", "VAS", "buy", value_nzd=10000)
    L.append("corporate_actions", {"type": "split", "market": "ASX", "ticker": "VAS", "ratio": 2, "effective_date": "2026-10-08"},
             ts="2026-10-02T09:00:00Z")
    days(L, "2026-10-01", "2026-10-06")
    held = state(L)["positions"][("core", "ASX", "VAS")]
    place_order(L, prices, fx, "2026-10-07T08:30:00Z", "core", "ASX", "VAS", "sell", qty=10)
    try:
        days(L, "2026-10-07", "2026-10-12")
        ok = True
    except Exception as e:
        ok = False
        held = repr(e)
    check("runs carry on after a split", ok, held)
    check("a 2-for-1 split doubles the holding", state(L)["positions"].get(("core", "ASX", "VAS")) == 2 * held, (held, state(L)["positions"]))
    cancels = [r["payload"] for r in L.records("orders") if r["payload"].get("event") == "cancel"]
    check("an order placed before the split is cancelled for a fresh decision", any(c["reason"] == "share split" for c in cancels), cancels)

# 2. Dividends: holders before the ex-date are paid on the pay date; a later buyer is not
with tempfile.TemporaryDirectory() as d:
    L = Ledger(d)
    L.append("cash", {"kind": "deposit", "ccy": "NZD", "amount": 100000.0}, ts="2026-10-01T00:00:00Z")
    L.append("cash", {"kind": "deposit", "ccy": "AUD", "amount": 20000.0}, ts="2026-10-01T00:00:00Z")
    place_order(L, prices, fx, "2026-10-01T08:30:00Z", "core", "ASX", "VAS", "buy", value_nzd=10000)     # fills 2 Oct
    L.append("corporate_actions", {"type": "dividend", "market": "ASX", "ticker": "VAS", "ccy": "AUD", "per_share": 1.0,
                                   "ex_date": "2026-10-06", "pay_date": "2026-10-20"}, ts="2026-10-02T09:00:00Z")
    days(L, "2026-10-01", "2026-10-06")
    first = state(L)["positions"][("core", "ASX", "VAS")]
    place_order(L, prices, fx, "2026-10-06T08:30:00Z", "deal", "ASX", "VAS", "buy", value_nzd=5000)      # fills 7 Oct, after the ex-date
    reps = days(L, "2026-10-07", "2026-10-21")
    divs = [r["payload"] for r in L.records("cash") if r["payload"]["kind"] == "dividend"]
    check("only the holding from before the ex-date is paid", len(divs) == 1 and abs(divs[0]["amount"] - first) < 0.01,
          (divs, first))
    vals = {r["payload"]["date"]: r["payload"] for r in L.records("valuations")}
    check("the dividend shows as owed between the ex-date and the pay date",
          abs(vals["2026-10-12"]["dividends_owed_nzd"] - first * fx.nzd_per("AUD", "2026-10-12")) < 0.5, vals["2026-10-12"]["dividends_owed_nzd"])
    check("nothing is owed once it is paid", vals["2026-10-21"]["dividends_owed_nzd"] == 0, vals["2026-10-21"]["dividends_owed_nzd"])
    days(L, "2026-10-22", "2026-10-23")
    check("a dividend is paid once", sum(1 for r in L.records("cash") if r["payload"]["kind"] == "dividend") == 1)

# 3. No borrowing: two US buys larger than the NZ$ cash stop at the cash there is
with tempfile.TemporaryDirectory() as d:
    L = Ledger(d)
    L.append("cash", {"kind": "deposit", "ccy": "NZD", "amount": 10000.0}, ts="2026-10-01T00:00:00Z")
    place_order(L, prices, fx, "2026-10-01T08:30:00Z", "core", "US", "VT", "buy", value_nzd=8000)
    place_order(L, prices, fx, "2026-10-01T08:31:00Z", "core", "US", "SPY", "buy", value_nzd=8000)
    days(L, "2026-10-01", "2026-10-05")
    c = state(L)["cash"]
    check("NZ$ cash never goes below zero", c.get("NZD", 0) >= -0.01, c)
    check("foreign cash never goes below zero", all(v >= -0.01 for v in c.values()), c)
    fills = [r["payload"] for r in L.records("fills")]
    check("the second buy is cut to what the cash allows", len(fills) == 2 and fills[1]["qty"] < 8000 * fx.per_nzd("USD", "2026-10-01") / fills[1]["price"],
          [(f["ticker"], f["qty"]) for f in fills])

# 4. A repeated run books interest once; a voided action is never applied
with tempfile.TemporaryDirectory() as d:
    L = Ledger(d)
    L.append("cash", {"kind": "deposit", "ccy": "NZD", "amount": 100000.0}, ts="2026-10-01T00:00:00Z")
    rec = L.append("corporate_actions", {"type": "dividend", "market": "ASX", "ticker": "VAS", "ccy": "AUD", "per_share": 9.0,
                                         "ex_date": "2026-10-01", "pay_date": "2026-10-05"}, ts="2026-10-01T01:00:00Z")
    L.append("corporate_actions", {"type": "void", "ref": rec["seq"], "why": "entered in error"}, ts="2026-10-01T02:00:00Z")
    run(L, prices, fx, "2026-10-01", CFG)
    run(L, prices, fx, "2026-10-05", CFG)
    run(L, prices, fx, "2026-10-05", CFG)      # as if the first attempt had failed after booking interest
    ints = [r["payload"] for r in L.records("cash") if r["payload"]["kind"] == "interest" and r["payload"].get("for_date") == "2026-10-05"]
    check("interest for a run date is booked once", len(ints) == 1, ints)
    check("a voided action is not applied", not any(r["payload"]["kind"] == "dividend" for r in L.records("cash")))
    bad = L.append("corporate_actions", {"type": "dividend", "market": "ASX", "ticker": "VAS", "ccy": "AUD", "per_share": 1.0},
                   ts="2026-10-06T01:00:00Z")
    rep = run(L, prices, fx, "2026-10-06", CFG)
    check("an action missing its dates is flagged, not a crash", any(str(bad["seq"]) in f for f in rep["flags"]), rep["flags"])

# 5. Fall from peak: half the active sleeves at 8%, the rest and a review at 12%, once per peak
with tempfile.TemporaryDirectory() as d:
    L = Ledger(d)
    L.append("cash", {"kind": "deposit", "ccy": "NZD", "amount": 100000.0}, ts="2026-10-01T00:00:00Z")
    place_order(L, prices, fx, "2026-10-01T08:30:00Z", "deal", "ASX", "SDF", "buy", value_nzd=4000)
    place_order(L, prices, fx, "2026-10-01T08:31:00Z", "core", "ASX", "VAS", "buy", value_nzd=10000)
    days(L, "2026-10-01", "2026-10-05")
    held = state(L)["positions"][("deal", "ASX", "SDF")]
    a = drawdown_rules(L, prices, fx, "2026-10-05", {"peak_nzd": 100000.0, "drawdown": -0.085})
    sells = [r["payload"] for r in L.records("orders") if r["payload"].get("side") == "sell"]
    check("at 8% below the peak, half of each deal holding is sold, and the core is not touched",
          len(sells) == 1 and sells[0]["ticker"] == "SDF" and sells[0]["qty"] == held // 2, (a, sells))
    b = drawdown_rules(L, prices, fx, "2026-10-05", {"peak_nzd": 100000.0, "drawdown": -0.09})
    check("the 8% step happens once per peak", b == [], b)
    c = drawdown_rules(L, prices, fx, "2026-10-06", {"peak_nzd": 100000.0, "drawdown": -0.125})
    check("at 12% below the peak, the rest is sold and a review is required", review_pending(L) and any("review" in x for x in c), c)
    L.append("decisions", {"event": "review_done", "note": "test"}, ts="2026-10-07T09:00:00Z")
    check("a logged review lifts the block", not review_pending(L))

# 6. Order lapse counts business days for a share that stops trading
check("business days skip weekends", business_days("2026-10-02", "2026-10-09") == 5, business_days("2026-10-02", "2026-10-09"))
try:
    place_order(Ledger(tempfile.mkdtemp()), prices, fx, "2026-10-01T08:30:00Z", "Deal", "ASX", "VAS", "buy", value_nzd=1000)
    check("an unknown sleeve name is refused", False)
except ValueError:
    check("an unknown sleeve name is refused", True)
print("\nALL PASS" if not fails else f"\n{len(fails)} FAILED: {fails}")
sys.exit(1 if fails else 0)
