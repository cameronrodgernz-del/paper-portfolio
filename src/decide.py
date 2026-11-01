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
       python3 -I src/decide.py <ledger_name> review "<what the review found>"   (after a 12% fall)
A card is placed only once tonight's nightly run is in the ledger. Deal and special situation
cards need an industry; deal cards also need a group. A special situation card states its "type"
(e.g. "insider_cluster"); only a type that has passed its history test is traded, and US deals wait
for test 9b.
"""
import csv
import json
import os
import sys
from datetime import date, datetime, timezone
from zoneinfo import ZoneInfo

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import math  # noqa: E402

from clerk import HEDGE_COST, HEDGE_SLEEVES, HEDGE_TENOR_DAYS, SLEEVES, place_order, plan_for_month, state  # noqa: E402
from costs import FX_FEE, PlanState, brokerage  # noqa: E402
from fills import size_cost  # noqa: E402
from daily import ROOT, cash_rate  # noqa: E402
from ledger import Ledger  # noqa: E402
from market_data import CURRENCY, FX, NZX_SMALL_ORDER_CAP_NZD, Prices, nzx_large  # noqa: E402
from rates import Rates  # noqa: E402
from risk import annualised, check_order, size_position  # noqa: E402


def entry_costs(L: Ledger, market: str, sleeve: str, value_nzd: float, nzd_per: float, stats: dict,
                p_sale_exit: float, today: str, days_held: int = 91) -> dict:
    """Expected costs of the round trip, as a share of the stake: buy brokerage (after the plan's
    monthly cover), half the spread and the size cost on the way in and on a sale exit, the
    brokerage on a sale exit (consideration is paid free), a currency conversion when the
    foreign cash is short, and the hedge's dealing cost."""
    if value_nzd <= 0:
        return {"total": 0.0}
    local = value_nzd / nzd_per
    plan = plan_for_month(L, today[:7])
    fee_in = brokerage(market, local, value_nzd, plan) / local
    fee_out = brokerage(market, local, value_nzd, PlanState(month="later", used_nzd=1e12)) / local   # a later sale, no cover left
    half_spread = stats["spread"] / 2
    if stats["adv_local"] is None:      # NZX: volumes unknown, order size capped instead (rulebook section 7)
        impact = 0.0
    else:
        impact = size_cost(local, stats["adv_local"], stats["daily_vol"]) if stats["adv_local"] else 0.02
    ccy = CURRENCY[market]
    fx = 0.0
    if ccy != "NZD" and state(L)["cash"].get(ccy, 0.0) < local:
        fx = FX_FEE
    # a hedge is dealt again at each three-month roll
    hedge = HEDGE_COST * max(1, math.ceil(days_held / HEDGE_TENOR_DAYS)) if sleeve in HEDGE_SLEEVES and ccy != "NZD" else 0.0
    total = fee_in + half_spread + impact + fx + hedge + p_sale_exit * (fee_out + half_spread + impact)
    return {"total": round(total, 5), "brokerage_in": round(fee_in, 5), "half_spread": round(half_spread, 5),
            "size_cost": round(impact, 5), "fx": fx, "hedge": hedge, "sale_exit_share": p_sale_exit}


def labels(L: Ledger, cfg: dict, key: str) -> dict:
    """(market, ticker) -> industry or regulator/bidder group, from the decision cards in the ledger,
    with config/run.json's lists filling any gaps."""
    field = {"industries": "industry", "groups": "group"}[key]
    out = {tuple(k.split(":", 1)): v for k, v in (cfg.get(key) or {}).items()}
    for r in L.records("decisions"):
        c = r["payload"].get("card") or {}
        if c.get(field) and c.get("market") and c.get("ticker"):
            out[(c["market"], c["ticker"])] = c[field]
    return out


def with_open_orders(L: Ledger, val: dict, fx: FX, today: str) -> dict:
    """The latest valuation as if every waiting buy had filled at its reference close, so the limits
    count orders already placed (and a sell had freed nothing yet)."""
    v = {"total_nzd": val["total_nzd"], "cash_nzd_total": val["cash_nzd_total"], "by_sleeve": dict(val["by_sleeve"]),
         "positions": [dict(x) for x in val["positions"]]}
    for o in state(L)["open_orders"]:
        if o["side"] != "buy":
            continue
        dec = next((r["payload"] for r in L.records("decisions") if r["payload"].get("order_id") == o["order_id"]), {})
        nzd = o["remaining"] * dec.get("ref_close", 0.0) * fx.nzd_per(CURRENCY[o["market"]], today)
        v["positions"].append({"sleeve": o["sleeve"], "market": o["market"], "ticker": o["ticker"], "value_nzd": nzd, "waiting": True})
        v["by_sleeve"][o["sleeve"]] = v["by_sleeve"].get(o["sleeve"], 0.0) + nzd
        v["cash_nzd_total"] -= nzd
    return v


def review_pending(L: Ledger) -> bool:
    """True after a 12% fall from the peak until a review is logged (rulebook section 3)."""
    flag = False
    for r in L.records("decisions"):
        e = r["payload"].get("event")
        if e == "review_required":
            flag = True
        elif e == "review_done":
            flag = False
    return flag


HISTORY_ROOT = ROOT   # where the history test reports are read from (the engine tests point it at an empty folder)
TESTS = {"us_deal": ("reports", "deal_us_history.md"), "insider_cluster": ("reports", "special_insider_history.md"),
         "asx_cash_deal": ("reports", "deal_au_history.md")}


def test_passed(name: str, root: str = ROOT) -> bool:
    """True once the history test's report records a pass (rulebook section 9)."""
    p = os.path.join(root, *TESTS[name])
    return os.path.exists(p) and "**Result: pass.**" in open(p).read()


def test_failed(name: str, root: str = ROOT) -> bool:
    """True once the history test's report records a fail."""
    p = os.path.join(root, *TESTS[name])
    return os.path.exists(p) and "**Result: fail.**" in open(p).read()


def cash_only(card: dict, root: str = ROOT) -> bool:
    """A deal paid wholly in cash, by the live list's terms (no scrip ratio)."""
    p = os.path.join(root, "config", "live_deals.csv")
    for r in (csv.DictReader(open(p, encoding="utf-8")) if os.path.exists(p) else []):
        if r["target_market"] == card["market"] and r["target_ticker"].upper() == card["ticker"].upper():
            try:
                return float(r.get("scrip_ratio") or 0) == 0
            except ValueError:
                return False
    return False


def untested(card: dict, root: str = ROOT) -> str | None:
    """Why a buy can't be placed because its kind of trade hasn't passed a history test, or None.
    US deals wait for 9b. A special situation card states its type, and only a type that has passed
    its test is traded (so far only "insider_cluster" has a test: 9a)."""
    if card.get("side") != "buy":
        return None
    if card["sleeve"] == "deal" and card["market"] == "US" and not test_passed("us_deal", root):
        return "US deals are not traded until the US cash deal test (9b) passes"
    if card["sleeve"] == "deal" and card["market"] == "ASX" and test_failed("asx_cash_deal", root) and cash_only(card, root):
        return "ASX cash deals are not traded: the ASX cash deal test (9c) failed (rulebook section 9c)"
    if card["sleeve"] == "special":
        kind = card.get("type")
        if kind not in TESTS or kind in ("us_deal", "asx_cash_deal"):
            return f"special situation type {kind!r} has no history test, so it is watched but not traded"
        if not test_passed(kind, root):
            return f"special situation type {kind!r} has not passed its history test"
    return None


def decide(L: Ledger, prices: Prices, fx: FX, rates: Rates, cfg: dict, card: dict, now_utc: datetime,
           dry_run: bool = False) -> dict:
    if card.get("draft") or "TO WRITE" in json.dumps(card) or "TO SET" in json.dumps(card):
        raise SystemExit("this is still a draft card (src/card_draft.py): write the thesis, industry and adjustments, and remove \"draft\"")
    vals = L.records("valuations")
    if not vals:
        raise SystemExit("no valuation yet: run the clerk first")
    m, t, sleeve, side = card["market"], card["ticker"], card["sleeve"], card["side"]
    if sleeve not in SLEEVES:
        raise SystemExit(f"unknown sleeve {sleeve!r}: use one of {', '.join(SLEEVES)}")
    if side not in ("buy", "sell"):
        raise SystemExit(f"unknown side {side!r}")
    today_ = now_utc.date().isoformat()
    nz_today = now_utc.astimezone(ZoneInfo("Pacific/Auckland")).date().isoformat()
    if not dry_run and vals[-1]["payload"]["date"] != nz_today:
        raise SystemExit(f"tonight's run ({nz_today}) is not in the ledger yet (latest {vals[-1]['payload']['date']}): "
                         "place nothing until the nightly job has landed")
    if side == "buy" and sleeve in ("deal", "special") and not card.get("industry"):
        raise SystemExit("a deal or special situation card needs an industry, for the 15% limit")
    if side == "buy" and sleeve == "deal" and not card.get("group"):
        raise SystemExit("a deal card needs a group (the regulator it waits on, or the bidder), for the 10% limit")
    val = with_open_orders(L, vals[-1]["payload"], fx, today_)
    drawdown = vals[-1]["payload"].get("drawdown", 0.0)
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
        # deals: the break price is the card's, or failing that its worst outcome
        brk = card.get("break_price")
        if sleeve == "deal" and brk is None:
            brk = min(v for _, v in outcomes)
        sz = size_position(sleeve, outcomes, px, brk, val["total_nzd"])
        want = sz["value_nzd"] if card.get("value_nzd") is None else min(float(card["value_nzd"]), sz["value_nzd"])
        if m == "NZX" and t.upper() not in nzx_large():
            want = min(want, NZX_SMALL_ORDER_CAP_NZD)      # NZX volumes unknown: smaller companies, smaller orders
        days = (date.fromisoformat(card["resolve_by"]) - date.fromisoformat(today)).days
        # deals: the first outcome is paid as consideration, the others are exits by sale
        p_sale = 1 - outcomes[0][0] if sleeve == "deal" else 1.0
        costs = entry_costs(L, m, sleeve, want, nzd_per, st, p_sale, today, days)
        net = sz["expected_return"] - costs["total"]
        exp_annual = annualised(net, days)
        rate, _ = cash_rate(cfg, rates, today[:7], L)
        breaches = check_order(val, drawdown, sleeve, m, t, side, want, nzd_per,
                               adv_value_nzd=st.get("median_value_nzd"), industry=card.get("industry"),
                               industries=labels(L, cfg, "industries"), group=card.get("group"), groups=labels(L, cfg, "groups"),
                               expected_annual=exp_annual if sleeve == "deal" else None, cash_rate=rate,
                               break_loss=(1 - brk / px) if sleeve == "deal" and brk is not None and px > brk else None,
                               review_pending=review_pending(L))
        # the clerk can pay for a buy only from NZ$ (less the plan fee kept back) or cash in the order's own currency
        ccy = CURRENCY[m]
        cash = state(L)["cash"]
        usable = max(0.0, cash.get("NZD", 0.0) - 15.0) + (cash.get(ccy, 0.0) * fx.nzd_per(ccy, today) if ccy != "NZD" else 0.0)
        for o in state(L)["open_orders"]:
            if o["side"] == "buy" and (CURRENCY[o["market"]] in (ccy, "NZD")):
                dec = next((r["payload"] for r in L.records("decisions") if r["payload"].get("order_id") == o["order_id"]), {})
                usable -= o["remaining"] * dec.get("ref_close", 0.0) * fx.nzd_per(CURRENCY[o["market"]], today)
        if want > usable + 0.01:
            breaches.append(f"only NZ${max(usable, 0):,.0f} of cash can pay for a {ccy} buy (other currencies can't be used)")
        waiting = [o for o in state(L)["open_orders"] if o["side"] == "buy" and (o["sleeve"], o["market"], o["ticker"]) == (sleeve, m, t)]
        if waiting and not card.get("top_up"):
            breaches.append(f"a buy of {m}:{t} is already waiting to fill ({waiting[0]['order_id']}); mark the card top_up to add")
        if sleeve == "deal":
            breaches = [b.replace("expected return", "expected return after costs") for b in breaches]
        if want <= 0:
            breaches.append("sizing gives no stake (the stated odds do not beat the price)")
        why = untested(card, HISTORY_ROOT)
        if why:
            breaches.append(why)
        out.update(sizing=sz, value_nzd=round(want, 2), costs=costs, expected_net=round(net, 4),
                   expected_annual=round(exp_annual, 4), cash_rate=rate)
    else:
        held = state(L)["positions"].get((sleeve, m, t), 0.0)
        full = card.get("value_nzd") is None
        want = held * px * nzd_per if full else float(card["value_nzd"])
        breaches = [] if held > 0 else [f"nothing held in {sleeve} {m}:{t}"]
        out.update(value_nzd=round(want, 2), sell_qty=held if full else None)
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
    if side == "sell" and out.get("sell_qty"):     # a full exit sells every share, with no rounding stub
        o = place_order(L, prices, fx, ts, sleeve, m, t, side, qty=out["sell_qty"], limit=card.get("limit"),
                        decision={"card": card, **{k: v for k, v in out.items() if k != "breaches"}})
    else:
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


def log_review(L: Ledger, note: str, now_utc: datetime) -> dict:
    """Log the review a 12% fall from the peak requires (rulebook section 3); new active positions are allowed again."""
    if not review_pending(L):
        raise SystemExit("no review is pending")
    if not note.strip():
        raise SystemExit("say what the review found")
    return L.append("decisions", {"event": "review_done", "note": note}, ts=now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"))


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
    if len(a) >= 2 and a[1] == "review":      # python3 -I src/decide.py <ledger> review "<what the review found>"
        cfg_ = json.load(open(os.path.join(ROOT, "config", "run.json")))
        L_ = Ledger(os.path.join(ROOT, cfg_["ledgers"][a[0]]["dir"]))
        print(log_review(L_, " ".join(a[2:]), datetime.now(timezone.utc))["payload"])
        sys.exit(0)
    sys.exit(main(a[0], a[1], "--dry-run" in sys.argv))
