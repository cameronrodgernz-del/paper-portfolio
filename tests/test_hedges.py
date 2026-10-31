"""Hedging dry run on October 2026 prices (a test, not the practice run).
Buys BetMakers (ASX, a pending cash scheme) in the deal sleeve on 1 Oct, books a made-up cash
consideration on 23 Oct so the position closes, and checks the clerk's hedging along the way.
Run: python3 -I tests/test_hedges.py"""
import os
import sys
import tempfile
from datetime import date, timedelta

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "src"))
from clerk import HEDGE_COST, place_order, run, state  # noqa: E402
from ledger import Ledger  # noqa: E402
from market_data import FX, Prices  # noqa: E402
from rates import Rates  # noqa: E402

fails = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (f"  [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)


data = os.path.join(ROOT, "data")
prices, fx, rates = Prices(data), FX(data), Rates(data)
check("rates load for all three currencies", all(0 < rates.three_month(c, "2026-10-01") < 0.2 for c in ("NZD", "AUD", "USD")),
      {c: rates.three_month(c, "2026-10-01") for c in ("NZD", "AUD", "USD")})
check("NZ monthly average is not used before its month ends", rates.three_month("NZD", "2026-09-30") == rates.series("NZD")[-2][1],
      (rates.three_month("NZD", "2026-09-30"), rates.series("NZD")[-2:]))
with tempfile.TemporaryDirectory() as d:
    L = Ledger(d)
    L.append("cash", {"kind": "deposit", "ccy": "NZD", "amount": 100000.0}, ts="2026-10-01T00:00:00Z")
    place_order(L, prices, fx, "2026-10-01T06:30:00Z", "deal", "ASX", "BET", "buy", value_nzd=4000)
    place_order(L, prices, fx, "2026-10-01T06:30:00Z", "core", "ASX", "VAS", "buy", value_nzd=10000)
    L.append("corporate_actions", {"type": "consideration", "market": "ASX", "ticker": "BET", "ccy": "AUD",
                                   "per_share": 0.24, "pay_date": "2026-10-23"}, ts="2026-10-01T07:00:00Z")
    reports, day = [], date(2026, 10, 1)
    while day <= date(2026, 10, 30):
        if day.weekday() < 5:
            reports.append(run(L, prices, fx, day.isoformat(), {"cash_rate": 0.025}, rates))
        day += timedelta(days=1)
    hedges = [r["payload"] for r in L.records("hedges")]
    opens = [h for h in hedges if h["event"] == "open"]
    closes = [h for h in hedges if h["event"] == "close"]
    rec = next(r for r in L.records("fills") if r["payload"]["ticker"] == "BET" and r["payload"]["side"] == "buy")
    fill, booked = rec["payload"], rec["ts_utc"][:10]
    check("the deal position is hedged in the run that books its fill", bool(opens) and opens[0]["trade_date"] == booked,
          (opens[0]["trade_date"] if opens else None, booked, "session " + fill["date"]))
    check("only the deal sleeve is hedged (core VAS is not)", all(h["ticker"] == "BET" for h in opens), [h["ticker"] for h in opens])
    if opens:
        h = opens[0]
        close = prices.last_close("ASX", "BET", h["trade_date"])
        check("hedge notional is the position's value at the close", abs(h["notional_foreign"] - fill["qty"] * close) < 1, (h["notional_foreign"], fill["qty"] * close))
        gap = h["rate_foreign"] - h["rate_nzd"]
        check("forward reflects the interest gap (higher AUD rate means more AUD per NZ$ forward)",
              (h["forward_mid"] > h["spot"]) == (gap > 0), (h["spot"], h["forward_mid"], round(gap, 4)))
        check("dealing cost of 0.1% is in the forward", abs(h["forward_rate"] / h["forward_mid"] - 1 - HEDGE_COST) < 1e-5)
    check("hedge closes when the consideration is paid", closes and closes[-1]["reason"] == "position closed", closes[-1:] if closes else None)
    st = state(L)
    check("no hedges left open", not st["hedges"], st["hedges"])
    check("no BET left after the consideration", ("deal", "ASX", "BET") not in st["positions"], st["positions"])
    v = [r["payload"] for r in L.records("valuations")][-1]
    check("hedged less unhedged equals the hedge result", abs(v["total_nzd"] - v["total_unhedged_nzd"] - v["hedge_mtm_nzd"] - v["hedge_realised_nzd"]) < 0.02,
          (v["total_nzd"], v["total_unhedged_nzd"], v["hedge_mtm_nzd"], v["hedge_realised_nzd"]))
    if opens and closes:
        aud_move = fx.per_nzd("AUD", closes[-1]["date"]) / opens[0]["spot"] - 1
        check("hedge gains when the AUD falls against the NZ$ (and loses when it rises), net of cost",
              (sum(c["pnl_nzd"] for c in closes) > 0) == (aud_move > HEDGE_COST + 0.001) or abs(aud_move) < 0.003, (round(aud_move, 4), [c["pnl_nzd"] for c in closes]))
    check("ledger chain intact", all(x == "ok" for x in L.verify().values()), L.verify())
    print(f"\nEnd value hedged {v['total_nzd']:,.2f}, unhedged {v['total_unhedged_nzd']:,.2f} NZD; hedge realised {v['hedge_realised_nzd']}")
    for h in hedges:
        print("  ", {k: h[k] for k in h if k in ("event", "hedge_id", "notional_foreign", "spot", "forward_rate", "maturity", "pnl_nzd", "reason", "date")})
print("\nALL PASS" if not fails else f"\n{len(fails)} FAILED: {fails}")
sys.exit(1 if fails else 0)
