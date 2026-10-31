"""Place one analyst decision in a ledger, with sizing and every limit checked first.

Input is a decision card (JSON), written by the analyst before any order:
{
  "sleeve": "deal", "market": "ASX", "ticker": "SDF", "side": "buy",
  "thesis": "why the market's spread is wrong",
  "outcomes": [[0.92, 6.00], [0.08, 4.10]],      # chance and price in each outcome; chances add to 1
  "complete_price": 6.00, "break_price": 4.10,   # deals: used for the market-implied chance
  "resolve_by": "2026-12-22", "exit_rule": "exit on completion, break, or a rival bid (fresh decision)",
  "industry": "industrials", "group": "ACCC",     # for the 15% industry and 10% regulator/bidder limits
  "base_rate": 0.84, "adjustments": ["no ACCC issue raised: +4 points", "..."],
  "limit": null, "value_nzd": null               # optional: a limit price; a smaller stake than the sizing gives
}
The decision is timed when this runs (never backdated). The card, the sizing, the limit checks and
the market-implied chance are written to the ledger's decisions and calls tables. If any limit is
breached, the decision is logged as vetoed and no order is placed.
Usage: python3 -I src/decide.py <ledger_name> <card.json> [--dry-run]
"""
import json
import os
import sys
from datetime import date, datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from clerk import HEDGE_COST, HEDGE_SLEEVES, place_order, plan_for_month, state  # noqa: E402
from costs import FX_FEE, brokerage  # noqa: E402
from fills import size_cost  # noqa: E402
from daily import ROOT, cash_rate  # noqa: E402
from ledger import Ledger  # noqa: E402
from market_data import CURRENCY, FX, Prices  # noqa: E402
from rates import Rates  # noqa: E402
from risk import annualised, check_order, size_position  # noqa: E402


def entry_costs(L: Ledger, market: str, sleeve: str, value_nzd: float, nzd_per: float, stats: dict,
                p_sale_exit: float, today: str) -> dict:
    """Expected costs of the round trip, as a share of the stake: buy brokerage (after the plan's
    monthly cover), half the spread and the size cost on the way in and on a sale exit, the
    brokerage on a sale exit (consideration is paid free), a currency conversion when the
    foreign cash is short, and the hedge's dealing cost."""
    if value_nzd <= 0:
        return {"total": 0.0}
    local = value_nzd / nzd_per
    plan = plan_for_month(L, today[:7])
    fee_in = brokerage(market, local, value_nzd, plan) / local
    fee_out = brokerage(market, local, value_nzd, plan) / local       # a sale later, after this month's cover
    half_spread = stats["spread"] / 2
    impact = size_cost(local, stats["adv_local"], stats["daily_vol"]) if stats["adv_local"] else 0.02
    ccy = CURRENCY[market]
    fx = 0.0
    if ccy != "NZD" and state(L)["cash"].get(ccy, 0.0) < local:
        fx = FX_FEE
    hedge = HEDGE_COST if sleeve in HEDGE_SLEEVES and ccy != "NZD" else 0.0
    total = fee_in + half_spread + impact + fx + hedge + p_sale_exit * (fee_out + half_spread + impact)
    return {"total": round(total, 5), "brokerage_in": round(fee_in, 5), "half_spread": round(half_spread, 5),
            "size_cost": round(impact, 5), "fx": fx, "hedge": hedge, "sale_exit_share": p_sale_exit}


def decide(L: Ledger, prices: Prices, fx: FX, rates: Rates, cfg: dict, card: dict, now_utc: datetime,
           dry_run: bool = False) -> dict:
    vals = L.records("valuations")
    if not vals:
        raise SystemExit("no valuation yet: run the clerk first")
    val = vals[-1]["payload"]
    m, t, sleeve, side = card["market"], card["ticker"], card["sleeve"], card["side"]
    ts = now_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    today = now_utc.date().isoformat()
    px = prices.last_close(m, t, today, now_utc)
    if not px:
        raise SystemExit(f"no price for {m}:{t}")
    nzd_per = fx.nzd_per(CURRENCY[m], today)
    st = prices.stats(m, t, today, nzd_per)
    out = {"price_seen": px}
    if side == "buy":
        outcomes = [tuple(o) for o in card["outcomes"]]
        sz = size_position(sleeve, outcomes, px, card.get("break_price"), val["total_nzd"])
        want = sz["value_nzd"] if card.get("value_nzd") is None else min(float(card["value_nzd"]), sz["value_nzd"])
        days = (date.fromisoformat(card["resolve_by"]) - date.fromisoformat(today)).days
        # deals: the first outcome is paid as consideration, the others are exits by sale
        p_sale = 1 - outcomes[0][0] if sleeve == "deal" else 1.0
        costs = entry_costs(L, m, sleeve, want, nzd_per, st, p_sale, today)
        net = sz["expected_return"] - costs["total"]
        exp_annual = annualised(net, days)
        rate, _ = cash_rate(cfg, rates, today[:7])
        breaches = check_order(val, val.get("drawdown", 0.0), sleeve, m, t, side, want, nzd_per,
                               adv_value_nzd=st.get("median_value_nzd"), industry=card.get("industry"),
                               industries=cfg.get("industries"), group=card.get("group"), groups=cfg.get("groups"),
                               expected_annual=exp_annual if sleeve == "deal" else None, cash_rate=rate)
        if sleeve == "deal":
            breaches = [b.replace("expected return", "expected return after costs") for b in breaches]
        if want <= 0:
            breaches.append("sizing gives no stake (the stated odds do not beat the price)")
        out.update(sizing=sz, value_nzd=round(want, 2), costs=costs, expected_net=round(net, 4),
                   expected_annual=round(exp_annual, 4), cash_rate=rate)
    else:
        held = state(L)["positions"].get((sleeve, m, t), 0.0)
        want = held * px * nzd_per if card.get("value_nzd") is None else float(card["value_nzd"])
        breaches = [] if held > 0 else [f"nothing held in {sleeve} {m}:{t}"]
        out.update(value_nzd=round(want, 2))
    implied = None
    if card.get("complete_price") and card.get("break_price") is not None and card["complete_price"] > card["break_price"]:
        implied = (px - card["break_price"]) / (card["complete_price"] - card["break_price"])
    out.update(breaches=breaches, market_implied=None if implied is None else round(implied, 4))
    if dry_run:
        return out
    if side == "buy" and card.get("outcomes"):
        L.append("calls", {"market": m, "ticker": t, "sleeve": sleeve, "made_utc": ts, "resolve_by": card["resolve_by"],
                           "outcomes": card["outcomes"], "p_main": card["outcomes"][0][0],
                           "market_implied": out["market_implied"], "base_rate": card.get("base_rate"),
                           "adjustments": card.get("adjustments", []), "price_seen": px}, ts=ts)
    if breaches:
        L.append("decisions", {"vetoed": True, "breaches": breaches, "card": card, **{k: v for k, v in out.items() if k != "breaches"}}, ts=ts)
        out["placed"] = None
        return out
    o = place_order(L, prices, fx, ts, sleeve, m, t, side, value_nzd=want, limit=card.get("limit"),
                    decision={"card": card, **{k: v for k, v in out.items() if k != "breaches"}})
    out["placed"] = o
    return out


def resolve_call(L: Ledger, market: str, ticker: str, made_utc: str, happened: bool, note: str, now_utc: datetime) -> dict:
    """Log how a dated call turned out (did its first, main outcome happen?), for success test 5."""
    if not any(r["payload"].get("made_utc") == made_utc and r["payload"]["ticker"] == ticker for r in L.records("calls")):
        raise SystemExit(f"no call on {market}:{ticker} made {made_utc}")
    return L.append("calls", {"event": "outcome", "market": market, "ticker": ticker, "made_utc": made_utc,
                              "main_outcome_happened": bool(happened), "note": note},
                    ts=now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"))


def main(name: str, card_path: str, dry: bool = False) -> int:
    cfg = json.load(open(os.path.join(ROOT, "config", "run.json")))
    data = os.path.join(ROOT, "data")
    L = Ledger(os.path.join(ROOT, cfg["ledgers"][name]["dir"]))
    bad = {k: v for k, v in L.verify().items() if v != "ok"}
    if bad:
        raise SystemExit(f"ledger chain broken: {bad}")
    out = decide(L, Prices(data), FX(data), Rates(data), cfg, json.load(open(card_path)), datetime.now(timezone.utc), dry)
    print(json.dumps(out, indent=1, default=str))
    return 0


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if x != "--dry-run"]
    sys.exit(main(a[0], a[1], "--dry-run" in sys.argv))
