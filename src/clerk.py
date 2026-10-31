"""The booking clerk: no discretion. Each run, for a given date, it
  1. charges the monthly plan fee and accrues interest on cash,
  2. fills open orders in sessions that opened after the decision was logged,
  3. applies corporate actions (dividends, scheme or offer consideration, splits),
  4. keeps deal positions in AUD or USD hedged back to NZ$ with rolling forwards,
  5. values the portfolio in NZ dollars (hedged, and unhedged for comparison) and checks the limits.
Everything it does is appended to the ledger; nothing is edited.

Orders are placed with place_order(), which sizes them from the last close the
decision-maker could have seen, and stamps the decision time.
"""
import json
import math
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone

from costs import PLAN_MONTHLY_NZD, PlanState, brokerage, FX_FEE
from fills import fill_order
from ledger import Ledger
from market_data import CURRENCY, FX, Prices, closed_by, nz_evening_utc, session_open_utc
from rates import Rates

CAPS = {"deal": 0.04, "special": 0.03}          # share of portfolio per position
CASH_FLOOR = 0.05
DRAWDOWN_HALVE, DRAWDOWN_EXIT = 0.08, 0.12
ORDER_LIFE_SESSIONS = 5
FX_BLOCK_BUFFER = 0.02                            # convert 2% more than needed, then hold it
HEDGE_SLEEVES = ("deal",)                         # rulebook: deal positions in AUD and USD are hedged
HEDGE_TENOR_DAYS = 91                             # rolling three-month forwards
HEDGE_COST = 0.001                                # simulated dealing cost, 0.1% of notional (Sharesies offers no hedging)
HEDGE_REBALANCE = 0.20                            # re-size when hedge and position differ by more than 20%


def utc(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(timezone.utc)


# ---------------------------------------------------------------- state
def state(L: Ledger) -> dict:
    cash = defaultdict(float)
    hedge_realised = 0.0
    for r in L.records("cash"):
        cash[r["payload"]["ccy"]] += r["payload"]["amount"]
        if r["payload"]["kind"] == "hedge_settle":
            hedge_realised += r["payload"]["amount"]
    pos = defaultdict(float)
    for r in L.records("fills"):
        p = r["payload"]
        key = (p["sleeve"], p["market"], p["ticker"])
        pos[key] += p["qty"] if p["side"] == "buy" else -p["qty"]
    for r in L.records("corporate_actions"):
        p = r["payload"]
        if p.get("type") == "split_applied":
            pos[(p["sleeve"], p["market"], p["ticker"])] += p["qty_change"]
    filled = defaultdict(float)
    for r in L.records("fills"):
        filled[r["payload"]["order_id"]] += r["payload"]["qty"]
    cancelled = {r["payload"]["order_id"] for r in L.records("orders") if r["payload"].get("event") == "cancel"}
    open_orders = []
    for r in L.records("orders"):
        p = r["payload"]
        if p.get("event") == "new" and p["order_id"] not in cancelled:
            left = p["qty"] - filled[p["order_id"]]
            if left > 1e-9:
                open_orders.append(dict(p, remaining=left))
    applied = {r["payload"]["ref"] for r in L.records("corporate_actions") if r["payload"].get("type", "").endswith("_applied")}
    hedges = {}
    for r in L.records("hedges"):
        p = r["payload"]
        if p["event"] == "open":
            hedges[p["hedge_id"]] = p
        elif p["event"] == "close":
            hedges.pop(p["hedge_id"], None)
    return {"cash": dict(cash), "positions": {k: v for k, v in pos.items() if abs(v) > 1e-9},
            "open_orders": open_orders, "applied": applied, "hedges": hedges, "hedge_realised_nzd": hedge_realised}


def plan_for_month(L: Ledger, month: str) -> PlanState:
    p = PlanState(month=month)
    p.used_nzd = sum(r["payload"]["gross_nzd"] for r in L.records("fills")
                     if r["payload"]["date"][:7] == month and r["payload"].get("reason") != "consideration")
    return p


# ---------------------------------------------------------------- decisions
def place_order(L: Ledger, prices: Prices, fx: FX, decided_at_utc: str, sleeve: str, market: str, ticker: str,
                side: str, value_nzd: float | None = None, qty: float | None = None, limit: float | None = None,
                decision: dict | None = None) -> dict:
    """Log the decision and the order. Size comes from the last close before the decision."""
    when = utc(decided_at_utc)
    seen = [b for b in prices.bars(market, ticker) if closed_by(market, b.date, when)]
    if not seen:
        raise ValueError(f"no price for {market}:{ticker} before {decided_at_utc}")
    ref_price = seen[-1].close
    ccy = CURRENCY[market]
    if qty is None:
        if value_nzd is None:
            raise ValueError("give value_nzd or qty")
        local = value_nzd * fx.per_nzd(ccy, when.date().isoformat())
        qty = math.floor(local / (limit or ref_price))
    order_id = f"{when:%Y%m%d%H%M%S}-{market}-{ticker}-{side}"
    d = L.append("decisions", dict(decision or {}, order_id=order_id, sleeve=sleeve, market=market, ticker=ticker,
                                   side=side, ref_close=ref_price, ref_date=seen[-1].date), ts=decided_at_utc)
    L.append("orders", {"event": "new", "order_id": order_id, "decision_seq": d["seq"], "sleeve": sleeve,
                        "market": market, "ticker": ticker, "side": side, "qty": qty, "limit": limit,
                        "decided_at_utc": decided_at_utc}, ts=decided_at_utc)
    return {"order_id": order_id, "qty": qty, "ref_close": ref_price}


# ---------------------------------------------------------------- the daily run
def run(L: Ledger, prices: Prices, fx: FX, run_date: str, cfg: dict, rates: Rates | None = None) -> dict:
    ts = nz_evening_utc(run_date).strftime("%Y-%m-%dT%H:%M:%SZ")   # 9pm NZ time, daylight saving or not
    st = state(L)
    report = {"date": run_date, "fills": [], "cancelled": [], "actions": [], "flags": []}

    # 1. plan fee on the first run of a month; interest on NZ$ cash since the last run
    month = run_date[:7]
    if not any(r["payload"].get("kind") == "plan_fee" and r["payload"].get("month") == month for r in L.records("cash")):
        L.append("cash", {"kind": "plan_fee", "month": month, "ccy": "NZD", "amount": -PLAN_MONTHLY_NZD}, ts=ts)
    last = [r["payload"]["date"] for r in L.records("valuations")]
    if last and st["cash"].get("NZD", 0) > 0:
        days = (date.fromisoformat(run_date) - date.fromisoformat(last[-1])).days
        if days > 0:
            amt = round(st["cash"]["NZD"] * cfg["cash_rate"] * days / 365, 2)
            L.append("cash", {"kind": "interest", "ccy": "NZD", "amount": amt, "days": days, "rate": cfg["cash_rate"]}, ts=ts)

    # 2. fills: each open order, in decision order, in the first eligible session up to run_date
    plan = plan_for_month(L, month)
    for o in sorted(state(L)["open_orders"], key=lambda x: x["decided_at_utc"]):
        m, t = o["market"], o["ticker"]
        sessions = [b for b in prices.bars(m, t) if b.date <= run_date and session_open_utc(m, b.date) > utc(o["decided_at_utc"])
                    and closed_by(m, b.date, utc(ts))]
        already = {r["payload"]["date"] for r in L.records("fills") if r["payload"]["order_id"] == o["order_id"]}
        tried = {r["payload"]["date"] for r in L.records("orders") if r["payload"].get("event") == "no_fill" and r["payload"]["order_id"] == o["order_id"]}
        remaining = o["remaining"]
        for bar in sessions:
            if bar.date in already or bar.date in tried:
                continue
            ccy = CURRENCY[m]
            nzd_per_local = fx.nzd_per(ccy, bar.date)
            s = prices.stats(m, t, bar.date, nzd_per_local)
            qty = remaining
            if o["side"] == "sell":
                held = state(L)["positions"].get((o["sleeve"], m, t), 0.0)
                qty = min(qty, held)
            f = fill_order(o["side"], qty, bar, s["spread"], s["adv_local"], s["daily_vol"], o.get("limit"))
            if f.qty <= 0:
                L.append("orders", {"event": "no_fill", "order_id": o["order_id"], "date": bar.date, "reason": f.reason}, ts=ts)
                continue
            gross_local = f.qty * f.price
            gross_nzd = gross_local * nzd_per_local
            if plan.month != bar.date[:7]:
                plan = plan_for_month(L, bar.date[:7])
            fee = brokerage(m, gross_local, gross_nzd, plan)
            if o["side"] == "buy":
                need = gross_local + fee
                have = state(L)["cash"].get(ccy, 0.0)
                if ccy != "NZD" and have < need:
                    _convert(L, fx, bar.date, "NZD", ccy, (need - have) * (1 + FX_BLOCK_BUFFER), ts)
                    have = state(L)["cash"].get(ccy, 0.0)
                if have < need:   # cut the fill to what the cash allows
                    take = math.floor((have - fee) / f.price)
                    if take <= 0:
                        L.append("orders", {"event": "no_fill", "order_id": o["order_id"], "date": bar.date, "reason": "no cash"}, ts=ts)
                        break
                    f.qty, gross_local = take, take * f.price
                    gross_nzd = gross_local * nzd_per_local
            sign = -1 if o["side"] == "buy" else 1
            L.append("fills", {"order_id": o["order_id"], "sleeve": o["sleeve"], "market": m, "ticker": t,
                               "side": o["side"], "date": bar.date, "qty": f.qty, "price": round(f.price, 6),
                               "gross_local": round(gross_local, 2), "gross_nzd": round(gross_nzd, 2), "fee_local": fee,
                               "ccy": ccy, "nzd_per_local": nzd_per_local, "reason": f.reason,
                               "spread_used": round(s["spread"], 5)}, ts=ts)
            L.append("cash", {"kind": "trade", "order_id": o["order_id"], "ccy": ccy, "amount": round(sign * gross_local, 2)}, ts=ts)
            L.append("cash", {"kind": "brokerage", "order_id": o["order_id"], "ccy": ccy, "amount": -fee}, ts=ts)
            report["fills"].append(f"{bar.date} {o['side']} {f.qty:g} {m}:{t} @ {f.price:.4f} fee {fee} {ccy}")
            remaining -= f.qty
            if remaining <= 1e-9:
                break
        # expire after ORDER_LIFE_SESSIONS eligible sessions
        if remaining > 1e-9 and len(sessions) >= ORDER_LIFE_SESSIONS:
            L.append("orders", {"event": "cancel", "order_id": o["order_id"], "reason": f"unfilled after {ORDER_LIFE_SESSIONS} sessions"}, ts=ts)
            report["cancelled"].append(o["order_id"])

    # 3. corporate actions entered by the analyst (dividends, consideration, splits) that fall due
    st = state(L)
    for r in L.records("corporate_actions"):
        p = r["payload"]
        if p.get("type") not in ("dividend", "consideration", "split") or r["seq"] in st["applied"]:
            continue
        due = p.get("pay_date") or p.get("effective_date")
        if due > run_date:
            continue
        holders = [(k, q) for k, q in st["positions"].items() if k[1] == p["market"] and k[2] == p["ticker"]]
        for (sleeve, m, t), q in holders:
            if p["type"] == "dividend":
                L.append("cash", {"kind": "dividend", "ccy": p["ccy"], "amount": round(q * p["per_share"], 2), "ref": r["seq"]}, ts=ts)
            elif p["type"] == "consideration":
                L.append("fills", {"order_id": f"CA{r['seq']}", "sleeve": sleeve, "market": m, "ticker": t, "side": "sell",
                                   "date": due, "qty": q, "price": p["per_share"], "gross_local": round(q * p["per_share"], 2),
                                   "gross_nzd": round(q * p["per_share"] * fx.nzd_per(p["ccy"], due), 2), "fee_local": 0.0,
                                   "ccy": p["ccy"], "nzd_per_local": fx.nzd_per(p["ccy"], due), "reason": "consideration"}, ts=ts)
                L.append("cash", {"kind": "consideration", "ccy": p["ccy"], "amount": round(q * p["per_share"], 2), "ref": r["seq"]}, ts=ts)
            elif p["type"] == "split":
                L.append("corporate_actions", {"type": "split_applied", "sleeve": sleeve, "market": m, "ticker": t,
                                               "qty_change": q * (p["ratio"] - 1), "ref": r["seq"]}, ts=ts)
        L.append("corporate_actions", {"type": f"{p['type']}_applied", "ref": r["seq"]}, ts=ts)
        report["actions"].append(f"{p['type']} {p['market']}:{p['ticker']}")

    # 4. hedges: deal positions in AUD or USD carry a rolling forward sale of that currency for NZ$
    if rates is not None and cfg.get("hedge", True):
        report["hedges"] = manage_hedges(L, prices, fx, rates, run_date, ts)

    # 5. value the portfolio and check the limits
    st = state(L)
    val = value(st, prices, fx, run_date, utc(ts), rates)
    peaks = [r["payload"]["total_nzd"] for r in L.records("valuations")]
    peak = max(peaks + [val["total_nzd"]])
    dd = val["total_nzd"] / peak - 1
    flags = []
    for line in val["positions"]:
        cap = CAPS.get(line["sleeve"])
        if cap and line["value_nzd"] > cap * val["total_nzd"] * 1.10:
            flags.append(f"{line['market']}:{line['ticker']} is {line['value_nzd'] / val['total_nzd']:.1%} of the portfolio (cap {cap:.0%})")
    if val["cash_nzd_total"] < CASH_FLOOR * val["total_nzd"]:
        flags.append(f"cash {val['cash_nzd_total'] / val['total_nzd']:.1%} is below the 5% floor")
    if dd <= -DRAWDOWN_EXIT:
        flags.append(f"fall from peak {dd:.1%}: move active sleeves to cash and review")
    elif dd <= -DRAWDOWN_HALVE:
        flags.append(f"fall from peak {dd:.1%}: halve the active sleeves")
    L.append("valuations", dict(val, date=run_date, peak_nzd=round(peak, 2), drawdown=round(dd, 5), flags=flags), ts=ts)
    report.update(total_nzd=val["total_nzd"], drawdown=dd, flags=flags)
    return report


def _convert(L: Ledger, fx: FX, d: str, frm: str, to: str, amount_to: float, ts: str) -> None:
    """Buy `amount_to` of currency `to` with NZ$, paying Sharesies' 0.5% on the NZ$ entered."""
    rate = fx.per_nzd(to, d)
    nzd_in = round(amount_to / rate / (1 - FX_FEE), 2)
    L.append("cash", {"kind": "fx_out", "ccy": frm, "amount": -nzd_in, "rate": rate, "date": d}, ts=ts)
    L.append("cash", {"kind": "fx_in", "ccy": to, "amount": round(nzd_in * (1 - FX_FEE) * rate, 2), "rate": rate,
                      "fee_nzd": round(nzd_in * FX_FEE, 2), "date": d}, ts=ts)


# ---------------------------------------------------------------- hedges
def hedge_value_nzd(h: dict, fx: FX, rates: Rates | None, d: str) -> float:
    """What closing the forward would pay in NZ$ today: sold foreign at the dealt rate, bought back at today's forward."""
    spot = fx.per_nzd(h["ccy"], d)
    left = (date.fromisoformat(h["maturity"]) - date.fromisoformat(d)).days
    now = rates.forward_per_nzd(h["ccy"], spot, d, left) if rates is not None else spot
    return h["notional_foreign"] / h["forward_rate"] - h["notional_foreign"] / now


def open_hedge(L: Ledger, fx: FX, rates: Rates, d: str, ts: str, sleeve: str, market: str, ticker: str,
               notional_foreign: float) -> dict:
    ccy = CURRENCY[market]
    spot = fx.per_nzd(ccy, d)
    mid = rates.forward_per_nzd(ccy, spot, d, HEDGE_TENOR_DAYS)
    p = {"event": "open", "hedge_id": f"H{d}-{market}-{ticker}-{len(L.records('hedges'))}", "sleeve": sleeve,
         "market": market, "ticker": ticker, "ccy": ccy, "notional_foreign": round(notional_foreign, 2),
         "trade_date": d, "maturity": (date.fromisoformat(d) + timedelta(days=HEDGE_TENOR_DAYS)).isoformat(),
         "spot": spot, "forward_mid": round(mid, 6), "forward_rate": round(mid * (1 + HEDGE_COST), 6),
         "rate_foreign": rates.three_month(ccy, d), "rate_nzd": rates.three_month("NZD", d)}
    L.append("hedges", p, ts=ts)
    return p


def close_hedge(L: Ledger, fx: FX, rates: Rates | None, h: dict, d: str, ts: str, reason: str) -> float:
    pnl = round(hedge_value_nzd(h, fx, rates, d), 2)
    L.append("hedges", {"event": "close", "hedge_id": h["hedge_id"], "date": d, "pnl_nzd": pnl, "reason": reason}, ts=ts)
    L.append("cash", {"kind": "hedge_settle", "ccy": "NZD", "amount": pnl, "hedge_id": h["hedge_id"]}, ts=ts)
    return pnl


def manage_hedges(L: Ledger, prices: Prices, fx: FX, rates: Rates, d: str, ts: str) -> list[str]:
    """No discretion: close hedges whose position is gone or whose forward has matured; then make sure
    each foreign-currency deal position is hedged to within 20% of its value at the last close."""
    out = []
    st = state(L)
    for h in list(st["hedges"].values()):
        held = st["positions"].get((h["sleeve"], h["market"], h["ticker"]), 0.0)
        if held <= 1e-9 or h["maturity"] <= d:
            pnl = close_hedge(L, fx, rates, h, d, ts, "position closed" if held <= 1e-9 else "matured")
            out.append(f"closed {h['hedge_id']} ({pnl:+.2f} NZD)")
    st = state(L)
    for (sleeve, m, t), q in st["positions"].items():
        if sleeve not in HEDGE_SLEEVES or CURRENCY[m] == "NZD" or q <= 0:
            continue
        px = prices.last_close(m, t, d, utc(ts))
        if not px:
            continue
        want = q * px
        cur = [h for h in st["hedges"].values() if (h["sleeve"], h["market"], h["ticker"]) == (sleeve, m, t)]
        have = sum(h["notional_foreign"] for h in cur)
        if have and abs(want / have - 1) <= HEDGE_REBALANCE:
            continue
        for h in cur:
            pnl = close_hedge(L, fx, rates, h, d, ts, "re-size")
            out.append(f"closed {h['hedge_id']} ({pnl:+.2f} NZD)")
        h = open_hedge(L, fx, rates, d, ts, sleeve, m, t, want)
        out.append(f"opened {h['hedge_id']}: sell {want:,.2f} {h['ccy']} at {h['forward_rate']} per NZD to {h['maturity']}")
    return out


def value(st: dict, prices: Prices, fx: FX, d: str, as_of_utc: datetime | None = None, rates: Rates | None = None) -> dict:
    lines, by_sleeve = [], defaultdict(float)
    for (sleeve, m, t), q in st["positions"].items():
        px = prices.last_close(m, t, d, as_of_utc) or 0.0
        v = q * px * fx.nzd_per(CURRENCY[m], d)
        lines.append({"sleeve": sleeve, "market": m, "ticker": t, "qty": q, "close": px, "value_nzd": round(v, 2)})
        by_sleeve[sleeve] += v
    cash_nzd = {c: round(a * fx.nzd_per(c, d), 2) for c, a in st["cash"].items()}
    hedge_mtm = sum(hedge_value_nzd(h, fx, rates, d) for h in st["hedges"].values())
    total = sum(by_sleeve.values()) + sum(cash_nzd.values()) + hedge_mtm
    realised = st.get("hedge_realised_nzd", 0.0)
    return {"total_nzd": round(total, 2), "total_unhedged_nzd": round(total - hedge_mtm - realised, 2),
            "positions": lines, "by_sleeve": {k: round(v, 2) for k, v in by_sleeve.items()},
            "cash_local": {c: round(a, 2) for c, a in st["cash"].items()}, "cash_nzd": cash_nzd,
            "cash_nzd_total": round(sum(cash_nzd.values()), 2), "hedge_mtm_nzd": round(hedge_mtm, 2),
            "hedge_realised_nzd": round(realised, 2)}
