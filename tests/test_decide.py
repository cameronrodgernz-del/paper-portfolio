"""Decision cards end to end on October 2026 prices (a test, not the practice run).
Run: python3 -I tests/test_decide.py"""
import json
import os
import sys
import tempfile
from datetime import date, datetime, timezone

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "src"))
from clerk import run, state  # noqa: E402
from daily import weekdays  # noqa: E402
from decide import decide  # noqa: E402
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
cfg = json.load(open(os.path.join(ROOT, "config", "run.json")))
with tempfile.TemporaryDirectory() as d:
    L = Ledger(d)
    L.append("cash", {"kind": "deposit", "ccy": "NZD", "amount": 100000.0}, ts="2026-10-01T00:00:00Z")
    for day in weekdays(date(2026, 10, 1), date(2026, 10, 29)):
        run(L, prices, fx, day.isoformat(), {"cash_rate": 0.025}, rates)
    now = datetime(2026, 10, 29, 8, 30, tzinfo=timezone.utc)      # 9:30pm NZ, 29 Oct
    card = {"sleeve": "deal", "market": "ASX", "ticker": "SDF", "side": "buy", "thesis": "test card",
            "outcomes": [[0.96, 6.00], [0.04, 3.95]], "complete_price": 6.00, "break_price": 3.95,
            "resolve_by": "2026-12-22", "exit_rule": "test", "industry": "industrials", "group": "test",
            "base_rate": 0.84, "adjustments": ["test"]}
    out = decide(L, prices, fx, rates, cfg, card, now)
    check("a sound deal card is placed", out["placed"] is not None, out)
    check("costs (currency conversion, hedge, spread) come off the expected return",
          out["costs"]["fx"] == 0.005 and out["expected_net"] < out["sizing"]["expected_return"], out.get("costs"))
    thin = decide(L, prices, fx, rates, cfg, dict(card, outcomes=[[0.92, 6.00], [0.08, 3.95]]), now, dry_run=True)
    check("a thin spread that only beats cash before costs is refused",
          any("after costs" in b for b in thin["breaches"]), thin["breaches"])
    check("the stake respects the 1% loss-on-break cap",
          out["value_nzd"] * (1 - 3.95 / out["price_seen"]) <= 0.01 * 100500 + 1, (out["value_nzd"], out["price_seen"]))
    calls = [r["payload"] for r in L.records("calls")]
    check("the dated call is logged with the market-implied chance", len(calls) == 1 and calls[0]["market_implied"] is not None, calls)
    bad = dict(card, outcomes=[[0.5, 6.00], [0.5, 3.95]])
    out2 = decide(L, prices, fx, rates, cfg, bad, now)
    check("a card whose odds do not beat the price is vetoed", out2["placed"] is None and out2["breaches"], out2["breaches"])
    vetoes = [r["payload"] for r in L.records("decisions") if r["payload"].get("vetoed")]
    check("the veto is logged with its reasons", len(vetoes) == 1 and vetoes[0]["breaches"], vetoes)
    run(L, prices, fx, "2026-10-30", {"cash_rate": 0.025}, rates)
    st = state(L)
    check("the order fills at the next ASX open (30 Oct)", ("deal", "ASX", "SDF") in st["positions"], st["positions"])
    check("the new deal position is hedged", any(h["ticker"] == "SDF" for h in st["hedges"].values()), list(st["hedges"]))
    sell = {"sleeve": "deal", "market": "ASX", "ticker": "SDF", "side": "sell", "thesis": "test exit"}
    out3 = decide(L, prices, fx, rates, cfg, sell, datetime(2026, 10, 30, 8, 30, tzinfo=timezone.utc))
    check("an exit for the whole holding is placed", out3["placed"] is not None and out3["placed"]["qty"] > 0, out3)
    check("ledger chain intact", all(v == "ok" for v in L.verify().values()), L.verify())
print("\nALL PASS" if not fails else f"\n{len(fails)} FAILED: {fails}")
sys.exit(1 if fails else 0)
