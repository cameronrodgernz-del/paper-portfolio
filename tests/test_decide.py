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
from decide import decide, resolve_call  # noqa: E402
import decide as _dm  # noqa: E402
_dm.HISTORY_ROOT = tempfile.mkdtemp()   # the engine checks below don't depend on the live history test results
from monthly import brier  # noqa: E402
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
    out2 = decide(L, prices, fx, rates, cfg, bad, now.replace(minute=45))
    check("a card whose odds do not beat the price is vetoed", out2["placed"] is None and out2["breaches"], out2["breaches"])
    vetoes = [r["payload"] for r in L.records("decisions") if r["payload"].get("vetoed")]
    check("the veto is logged with its reasons", len(vetoes) == 1 and vetoes[0]["breaches"], vetoes)
    again = decide(L, prices, fx, rates, cfg, card, now.replace(minute=50), dry_run=True)
    check("the same card twice is refused while the first order waits", any("already waiting" in b for b in again["breaches"]), again["breaches"])
    topup = decide(L, prices, fx, rates, cfg, dict(card, top_up=True), now.replace(minute=51), dry_run=True)
    check("a top-up counts the waiting order against the 4% cap and the 1% break loss",
          any("cap" in b or "breaks" in b for b in topup["breaches"]), topup["breaches"])
    nobrk = {k: v for k, v in card.items() if k not in ("break_price", "complete_price")}
    nb = decide(L, prices, fx, rates, cfg, dict(nobrk, ticker="CWY", outcomes=[[0.98, 3.095], [0.02, 2.0]], resolve_by="2027-03-31"),
                now.replace(minute=52), dry_run=True)
    check("a deal card without a break price is held to 1% using its worst outcome",
          "loss-on-break" in nb["sizing"]["limited_by"], nb["sizing"])
    try:
        decide(L, prices, fx, rates, cfg, dict(card, sleeve="Deal"), now.replace(minute=53), dry_run=True)
        check("a card with an unknown sleeve is refused", False)
    except SystemExit:
        check("a card with an unknown sleeve is refused", True)
    run(L, prices, fx, "2026-10-30", {"cash_rate": 0.025}, rates)
    st = state(L)
    check("the order fills at the next ASX open (30 Oct)", ("deal", "ASX", "SDF") in st["positions"], st["positions"])
    check("the new deal position is hedged", any(h["ticker"] == "SDF" for h in st["hedges"].values()), list(st["hedges"]))
    sell = {"sleeve": "deal", "market": "ASX", "ticker": "SDF", "side": "sell", "thesis": "test exit"}
    out3 = decide(L, prices, fx, rates, cfg, sell, datetime(2026, 10, 30, 8, 30, tzinfo=timezone.utc))
    check("an exit for the whole holding sells every share", out3["placed"] is not None
          and out3["placed"]["qty"] == st["positions"][("deal", "ASX", "SDF")], (out3.get("placed"), st["positions"]))
    c = [r["payload"] for r in L.records("calls") if r["payload"].get("event") != "outcome"][0]
    resolve_call(L, "ASX", "SDF", c["made_utc"], True, "test: scheme implemented", datetime(2026, 10, 30, 9, 0, tzinfo=timezone.utc))
    recs = [r["payload"] for r in L.records("calls")]
    outs = {(x["market"], x["ticker"], x["made_utc"]): x["main_outcome_happened"] for x in recs if x.get("event") == "outcome"}
    ours, mkt, n = brier([x for x in recs if x.get("event") != "outcome"], outs)
    check("a resolved call is scored against the market's chance", n == 1 and abs(ours - (1 - 0.96) ** 2) < 1e-9
          and abs(mkt - (1 - c["market_implied"]) ** 2) < 1e-9, (ours, mkt, n))
    check("ledger chain intact", all(v == "ok" for v in L.verify().values()), L.verify())

# a draft card from src/card_draft.py can't be placed until it's finished
try:
    decide(L, prices, fx, rates, cfg, dict(sell, side="buy", draft=True, outcomes=[[0.9, 6.0], [0.1, 4.0]]), datetime(2026, 10, 30, 8, 30, tzinfo=timezone.utc), dry_run=True)
    check("a draft card is refused", False)
except SystemExit as e:
    check("a draft card is refused", "draft" in str(e), str(e))

# trade types without a passed history test are refused (rulebook sections 2, 5 and 9)
import decide as _d  # noqa: E402
with tempfile.TemporaryDirectory() as root:
    os.makedirs(os.path.join(root, "reports"))
    us = {"sleeve": "deal", "market": "US", "ticker": "XYZ", "side": "buy"}
    ins = {"sleeve": "special", "market": "US", "ticker": "XYZ", "side": "buy", "type": "insider_cluster"}
    check("a US deal is refused before test 9b passes", _d.untested(us, root) is not None)
    check("an ASX deal needs no test", _d.untested(dict(us, market="ASX"), root) is None)
    check("a special situation without a type is refused", _d.untested(dict(ins, type=None), root) is not None)
    check("an untested special situation type is refused", _d.untested(dict(ins, type="strategic_review"), root) is not None)
    check("an insider cluster is refused before test 9a passes", _d.untested(ins, root) is not None)
    open(os.path.join(root, "reports", "special_insider_history.md"), "w").write("**Result: fail.**")
    check("an insider cluster is refused after test 9a fails", _d.untested(ins, root) is not None)
    open(os.path.join(root, "reports", "special_insider_history.md"), "w").write("**Result: pass.**")
    open(os.path.join(root, "reports", "deal_us_history.md"), "w").write("**Result: pass.**")
    check("an insider cluster is allowed once test 9a passes", _d.untested(ins, root) is None)
    check("a US deal is allowed once test 9b passes", _d.untested(us, root) is None)
    check("a sale never needs a test", _d.untested(dict(us, side="sell"), root) is None)
    os.makedirs(os.path.join(root, "config"))
    open(os.path.join(root, "config", "live_deals.csv"), "w").write(
        "deal_id,target_market,target_ticker,cash_per_share,scrip_ratio\nA1,ASX,CASHCO,1.00,0\nA2,ASX,MIXCO,0.50,0.2\n")
    acash, amix = dict(us, market="ASX", ticker="CASHCO"), dict(us, market="ASX", ticker="MIXCO")
    check("an ASX cash deal is allowed while 9c has no result", _d.untested(acash, root) is None)
    open(os.path.join(root, "reports", "deal_au_history.md"), "w").write("Not enough coverage to run. **Result: not run.**")
    check("an ASX cash deal is allowed when 9c could not be run", _d.untested(acash, root) is None)
    open(os.path.join(root, "reports", "deal_au_history.md"), "w").write("**Result: fail.**")
    check("an ASX cash deal is refused once 9c fails", "9c" in (_d.untested(acash, root) or ""))
    check("an ASX scrip deal is not covered by 9c", _d.untested(amix, root) is None)


# ---- research picks (rulebook section 5a) ----
import risk as _risk  # noqa: E402
with tempfile.TemporaryDirectory() as d, tempfile.TemporaryDirectory() as rr:
    L = Ledger(d)
    L.append("cash", {"kind": "deposit", "ccy": "NZD", "amount": 100000.0}, ts="2026-10-01T00:00:00Z")
    for day in weekdays(date(2026, 10, 1), date(2026, 10, 29)):
        run(L, prices, fx, day.isoformat(), {"cash_rate": 0.025}, rates)
    now = datetime(2026, 10, 29, 8, 30, tzinfo=timezone.utc)
    _dm.RESEARCH_ROOT = rr
    os.makedirs(os.path.join(rr, "research", "picks")); os.makedirs(os.path.join(rr, "research", "red_team")); os.makedirs(os.path.join(rr, "config"))
    open(os.path.join(rr, "research", "picks", "CWY.md"), "w").write(
        "# Cleanaway\n## Why the market is wrong\nx\n## Valuation\nx\n## Sources\n" + "\n".join(f"- http://example.com/{i}" for i in range(6)))
    open(os.path.join(rr, "research", "red_team", "CWY.md"), "w").write("# Review\n## Verdict\nproceed")
    open(os.path.join(rr, "config", "judgement_excluded.csv"), "w").write("# not yet confirmed\nticker,name,reason\nXYZ,Example Ltd,test\n")
    rc = {"sleeve": "research", "market": "ASX", "ticker": "CWY", "side": "buy", "company": "Cleanaway Waste Management",
          "thesis": "test", "outcomes": [[0.2, 2.4], [0.5, 3.2], [0.3, 4.2]], "resolve_by": "2027-06-30", "exit_rule": "test",
          "industry": "industrials", "deep_dive": "research/picks/CWY.md", "red_team": "research/red_team/CWY.md",
          "catalysts": [{"date": "2027-02-20", "event": "half-year result"}]}
    good = decide(L, prices, fx, rates, cfg, rc, now, dry_run=True)
    research_words = ("deep dive", "red team", "outcomes", "dated event", "excluded", "wait until Cam", "reopened")
    check("a complete research card has no research refusals", not any(any(w in b for w in research_words) for b in good["breaches"]), good["breaches"])
    check("a research pick is capped at 2.5% of the portfolio", good["value_nzd"] <= 0.025 * 100500 + 1, good["value_nzd"])
    nodd = decide(L, prices, fx, rates, cfg, dict(rc, deep_dive=""), now, dry_run=True)
    check("a research card with no deep dive is refused", any("deep dive" in b for b in nodd["breaches"]), nodd["breaches"])
    two = decide(L, prices, fx, rates, cfg, dict(rc, outcomes=[[0.6, 3.5], [0.4, 2.5]]), now, dry_run=True)
    check("a research card needs three outcomes", any("three outcomes" in b for b in two["breaches"]), two["breaches"])
    nocat = decide(L, prices, fx, rates, cfg, dict(rc, catalysts=[]), now, dry_run=True)
    check("a research card needs a dated event", any("dated event" in b for b in nocat["breaches"]), nocat["breaches"])
    ex = decide(L, prices, fx, rates, cfg, dict(rc, ticker="XYZ"), now, dry_run=True) if prices.last_close("ASX", "XYZ", "2026-10-29") else None
    rows, conf = _dm.excluded_list(rr)
    check("the excluded list is read, and isn't confirmed until Cam says so", rows and rows[0]["ticker"] == "XYZ" and not conf, (rows, conf))
    chk = _dm.research_checks(dict(rc, ticker="XYZ", company="Example Ltd"), prices, "2026-10-29", rr)
    check("a company on Cam's excluded list is refused", any("excluded list" in b for b in chk), chk)
    gm = _dm.research_checks(dict(rc, industry="gaming and wagering"), prices, "2026-10-29", rr)
    check("gaming picks wait until the excluded list is confirmed", any("wait until Cam" in b for b in gm), gm)
    open(os.path.join(rr, "config", "judgement_excluded.csv"), "a").write("# confirmed by Cam on 2026-11-02\n")
    gm2 = _dm.research_checks(dict(rc, industry="gaming and wagering"), prices, "2026-10-29", rr)
    check("once confirmed, a gaming pick is no longer held back", not any("wait until Cam" in b for b in gm2), gm2)
    val = {"total_nzd": 100000.0, "by_sleeve": {"research": 10000.0}, "cash_nzd_total": 50000.0,
           "positions": [{"sleeve": "research", "market": "ASX", "ticker": f"T{i}", "value_nzd": 1500.0} for i in range(5)]}
    six = _risk.check_order(val, 0.0, "research", "ASX", "NEW", "buy", 1500.0, 1.1)
    check("a sixth research company is refused", any("five" in b or "most allowed" in b for b in six), six)
    _dm.RESEARCH_ROOT = _dm.ROOT

print("\nALL PASS" if not fails else f"\n{len(fails)} FAILED: {fails}")
sys.exit(1 if fails else 0)
