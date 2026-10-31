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

from costs import FEE_CAP, PLAN_MONTHLY_NZD, PlanState, brokerage, FX_FEE
from fills import Bar, fill_order
from ledger import Ledger
from market_data import CURRENCY, FX, Prices, closed_by, nz_evening_utc, session_open_utc
from rates import Rates

CAPS = {"deal": 0.04, "special": 0.03}          # share of portfolio per position
CASH_FLOOR = 0.05
DRAWDOWN_HALVE, DRAWDOWN_EXIT = 0.08, 0.12
ORDER_LIFE_SESSIONS = 5                           # an order lapses after 5 sessions that traded ...
ORDER_LIFE_DAYS = 10                              # ... or 10 business days, whichever comes first
SLEEVES = ("core", "deal", "special")
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
        if p.get("type") == "split_applied" and "qty_change" in p:     # holder records; the bare marker has no qty
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
    ca = [r["payload"] for r in L.records("corporate_actions")]
    applied = {p["ref"] for p in ca if p.get("type", "").endswith("_applied") and "qty_change" not in p}
    voided = {p["ref"] for p in ca if p.get("type") == "void"}
    hedges = {}
    for r in L.records("hedges"):
        p = r["payload"]
        if p["event"] == "open":
            hedges[p["hedge_id"]] = p
        elif p["event"] == "close":
            hedges.pop(p["hedge_id"], None)
    return {"cash": dict(cash), "positions": {k: v for k, v in pos.items() if abs(v) > 1e-9},
            "open_orders": open_orders, "applied": applied, "voided": voided, "hedges": hedges,
            "hedge_realised_nzd": hedge_realised}


def position_before(L: Ledger, key: tuple, before: str) -> float:
    """Shares held in (sleeve, market, ticker) from sessions before `before` (an ex-date or record date)."""
    q = 0.0
    for r in L.records("fills"):
        p = r["payload"]
        if (p["sleeve"], p["market"], p["ticker"]) == key and p["date"] < before:
            q += p["qty"] if p["side"] == "buy" else -p["qty"]
    for r in L.records("corporate_actions"):
        p = r["payload"]
        if p.get("type") == "split_applied" and "qty_change" in p and (p["sleeve"], p["market"], p["ticker"]) == key \
                and p.get("effective_date", "") < before:
            q += p["qty_change"]
    return q


def business_days(a: str, b: str) -> int:
    """Weekdays after date a up to and including date b."""
    d, n = date.fromisoformat(a), 0
    while d < date.fromisoformat(b):
        d += timedelta(days=1)
        n += d.weekday() < 5
    return n


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
    if sleeve not in SLEEVES:
        raise ValueError(f"unknown sleeve {sleeve!r}: use one of {', '.join(SLEEVES)}")
    if side not in ("buy", "sell"):
        raise ValueError(f"unknown side {side!r}")
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
    seq_next = len(L.records("decisions")) + 1
    order_id = f"{when:%Y%m%d%H%M%S}-{sleeve}-{market}-{ticker}-{side}-{seq_next}"
    if any(r["payload"].get("order_id") == order_id for r in L.records("orders")):
        raise ValueError(f"order {order_id} already exists")
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
    booked = any(r["payload"].get("kind") == "interest" and r["payload"].get("for_date") == run_date for r in L.records("cash"))
    if last and st["cash"].get("NZD", 0) > 0 and not booked:     # once per run date, even if a run is repeated after a failure
        days = (date.fromisoformat(run_date) - date.fromisoformat(last[-1])).days
        if days > 0:
            amt = round(st["cash"]["NZD"] * cfg["cash_rate"] * days / 365, 2)
            L.append("cash", {"kind": "interest", "ccy": "NZD", "amount": amt, "days": days, "rate": cfg["cash_rate"],
                              "for_date": run_date}, ts=ts)

    # 1b. splits, once the first session at the new share count is final, and before any fill from it:
    # holdings change from that session, and orders sized before it are cancelled for a fresh decision
    st = state(L)
    for r in L.records("corporate_actions"):
        p = r["payload"]
        if p.get("type") != "split" or r["seq"] in st["applied"] or r["seq"] in st["voided"]:
            continue
        eff = p.get("effective_date")
        if not eff or not p.get("ratio"):
            report["flags"].append(f"split record {r['seq']} for {p.get('market')}:{p.get('ticker')} lacks its date or ratio; not applied")
            continue
        if not closed_by(p["market"], eff, utc(ts)):
            continue
        new_bars = [b for b in prices.bars(p["market"], p["ticker"]) if b.date >= eff and closed_by(p["market"], b.date, utc(ts))]
        if not new_bars:      # the feed is a night behind: wait, so the holding and its price change together
            report["flags"].append(f"split of {p['market']}:{p['ticker']} due {eff} is waiting for that session's price")
            continue
        done = {tuple(x["payload"].get("holder") or ()) for x in L.records("corporate_actions") if x["payload"].get("ref") == r["seq"]}
        keys = {k for k in st["positions"] if k[1] == p["market"] and k[2] == p["ticker"]}
        for key in sorted(keys):
            q = position_before(L, key, eff)
            if key in done or q <= 1e-9:
                continue
            L.append("corporate_actions", {"type": "split_applied", "sleeve": key[0], "market": key[1], "ticker": key[2],
                                           "qty_change": q * (p["ratio"] - 1), "ref": r["seq"], "holder": list(key),
                                           "effective_date": eff}, ts=ts)
        ref_dates = {x["seq"]: x["payload"].get("ref_date", "") for x in L.records("decisions")}
        for o in state(L)["open_orders"]:
            if o["market"] == p["market"] and o["ticker"] == p["ticker"] and ref_dates.get(o.get("decision_seq"), "") < eff:
                L.append("orders", {"event": "cancel", "order_id": o["order_id"], "reason": "share split"}, ts=ts)
                report["cancelled"].append(o["order_id"])
        L.append("corporate_actions", {"type": "split_applied", "ref": r["seq"]}, ts=ts)
        report["actions"].append(f"split {p['market']}:{p['ticker']}")

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
            if m == "NZX" and bar.volume <= 0:
                # NZX volumes are unknown (rulebook section 7): a day with no price movement is taken as
                # no trading; otherwise the order fills with no volume cap or size cost, since NZX order
                # sizes are capped before they are placed
                if bar.open == bar.high == bar.low == bar.close:
                    L.append("orders", {"event": "no_fill", "order_id": o["order_id"], "date": bar.date,
                                        "reason": "no price movement (NZX volume unknown)"}, ts=ts)
                    continue
                bar = Bar(bar.date, bar.open, bar.high, bar.low, bar.close, 1e12)
                s = dict(s, adv_local=1e15)
            if o["side"] == "sell":
                held = state(L)["positions"].get((o["sleeve"], m, t), 0.0)
                qty = min(qty, held)
            f = fill_order(o["side"], qty, bar, s["spread"], s["adv_local"], s["daily_vol"], o.get("limit"))
            if f.qty <= 0:
                L.append("orders", {"event": "no_fill", "order_id": o["order_id"], "date": bar.date, "reason": f.reason}, ts=ts)
                continue
            if plan.month != bar.date[:7]:
                plan = plan_for_month(L, bar.date[:7])

            def fee_for(q):       # brokerage on q shares, without using up the plan's cover yet
                trial = PlanState(month=plan.month, used_nzd=plan.used_nzd)
                return brokerage(m, q * f.price, q * f.price * nzd_per_local, trial)
            if o["side"] == "buy":
                need = f.qty * f.price + fee_for(f.qty)
                cash_now = state(L)["cash"]
                have = cash_now.get(ccy, 0.0)
                if ccy != "NZD" and have < need:
                    # convert from NZ$, but never more NZ$ than there is: no borrowing
                    rate = fx.per_nzd(ccy, bar.date)
                    want_nzd = (need - have) * (1 + FX_BLOCK_BUFFER) / rate / (1 - FX_FEE)
                    nzd_in = min(want_nzd, max(0.0, cash_now.get("NZD", 0.0) - PLAN_MONTHLY_NZD))   # keep the plan fee back
                    if nzd_in >= 1.0:
                        _convert_nzd(L, fx, bar.date, ccy, nzd_in, ts)
                    have = state(L)["cash"].get(ccy, 0.0)
                if have < need:   # cut the fill to what the cash allows, fee included
                    take = math.floor(max(0.0, have - FEE_CAP[m][1]) / f.price)
                    while take > 0 and take * f.price + fee_for(take) > have:
                        take -= 1
                    if take <= 0:
                        L.append("orders", {"event": "no_fill", "order_id": o["order_id"], "date": bar.date, "reason": "no cash"}, ts=ts)
                        break
                    f.qty = take
            gross_local = f.qty * f.price
            gross_nzd = gross_local * nzd_per_local
            fee = brokerage(m, gross_local, gross_nzd, plan)
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
        # lapse after ORDER_LIFE_SESSIONS sessions that traded, or ORDER_LIFE_DAYS business days (a halted share)
        traded = [b for b in sessions if b.volume > 0 or (m == "NZX" and not (b.open == b.high == b.low == b.close))]
        age = business_days(utc(o["decided_at_utc"]).date().isoformat(), run_date)
        if remaining > 1e-9 and (len(traded) >= ORDER_LIFE_SESSIONS or age >= ORDER_LIFE_DAYS):
            why = f"unfilled after {ORDER_LIFE_SESSIONS} sessions that traded" if len(traded) >= ORDER_LIFE_SESSIONS \
                else f"unfilled after {ORDER_LIFE_DAYS} business days"
            L.append("orders", {"event": "cancel", "order_id": o["order_id"], "reason": why}, ts=ts)
            report["cancelled"].append(o["order_id"])

    # 3. dividends and consideration entered with src/actions.py that fall due.
    # Dividends go to holders before the ex-date; consideration to holders before the record date
    # (or at payment, if none is given). Each holder is booked once, even if a run is repeated.
    st = state(L)
    done_refs = defaultdict(set)       # (ref) -> holders paid in cash
    done_fills = defaultdict(set)      # (ref) -> holders whose consideration sale is booked
    for x in L.records("cash"):
        q = x["payload"]
        if q.get("ref") is not None and q.get("holder"):
            done_refs[q["ref"]].add(tuple(q["holder"]))
    for x in L.records("fills"):
        q = x["payload"]
        if q.get("ref") is not None and q.get("holder"):
            done_fills[q["ref"]].add(tuple(q["holder"]))
    for r in L.records("corporate_actions"):
        p = r["payload"]
        if p.get("type") not in ("dividend", "consideration") or r["seq"] in st["applied"] or r["seq"] in st["voided"]:
            continue
        due = p.get("pay_date")
        if not due or (p["type"] == "dividend" and not p.get("ex_date")):
            report["flags"].append(f"{p['type']} record {r['seq']} for {p.get('market')}:{p.get('ticker')} lacks its dates; not applied")
            continue
        if due > run_date:
            continue
        cut = p["ex_date"] if p["type"] == "dividend" else p.get("record_date")
        keys = {k for k in st["positions"] if k[1] == p["market"] and k[2] == p["ticker"]}
        if cut:
            keys |= {(f["sleeve"], f["market"], f["ticker"]) for f in (x["payload"] for x in L.records("fills"))
                     if f["market"] == p["market"] and f["ticker"] == p["ticker"]}
        for key in sorted(keys):
            if key in done_refs[r["seq"]]:
                continue
            sleeve, m, t = key
            if p["type"] == "consideration" and key in done_fills[r["seq"]]:
                f0 = next(x["payload"] for x in L.records("fills") if x["payload"].get("ref") == r["seq"] and tuple(x["payload"]["holder"]) == key)
                L.append("cash", {"kind": "consideration", "ccy": p["ccy"], "amount": f0["gross_local"], "ref": r["seq"], "holder": list(key)}, ts=ts)
                continue
            q = position_before(L, key, cut) if cut else st["positions"].get(key, 0.0)
            if p["type"] == "consideration":
                q = min(q, st["positions"].get(key, 0.0))     # only shares still held can be paid out
            if q <= 1e-9:
                continue
            if p["type"] == "dividend":
                L.append("cash", {"kind": "dividend", "ccy": p["ccy"], "amount": round(q * p["per_share"], 2), "ref": r["seq"],
                                  "holder": list(key), "shares": q}, ts=ts)
            elif p["type"] == "consideration":
                L.append("fills", {"order_id": f"CA{r['seq']}", "sleeve": sleeve, "market": m, "ticker": t, "side": "sell",
                                   "date": due, "qty": q, "price": p["per_share"], "gross_local": round(q * p["per_share"], 2),
                                   "gross_nzd": round(q * p["per_share"] * fx.nzd_per(p["ccy"], due), 2), "fee_local": 0.0,
                                   "ccy": p["ccy"], "nzd_per_local": fx.nzd_per(p["ccy"], due), "reason": "consideration",
                                   "ref": r["seq"], "holder": list(key)}, ts=ts)
                L.append("cash", {"kind": "consideration", "ccy": p["ccy"], "amount": round(q * p["per_share"], 2), "ref": r["seq"],
                                  "holder": list(key)}, ts=ts)
        L.append("corporate_actions", {"type": f"{p['type']}_applied", "ref": r["seq"]}, ts=ts)
        report["actions"].append(f"{p['type']} {p['market']}:{p['ticker']}")

    # 4. hedges: deal positions in AUD or USD carry a rolling forward sale of that currency for NZ$
    if rates is not None and cfg.get("hedge", True):
        report["hedges"] = manage_hedges(L, prices, fx, rates, run_date, ts)

    # 5. value the portfolio and check the limits; a dividend past its ex-date but not yet paid is owed
    st = state(L)
    owed = 0.0
    for r in L.records("corporate_actions"):
        p = r["payload"]
        if p.get("type") == "dividend" and r["seq"] not in st["applied"] and r["seq"] not in st["voided"] \
                and p.get("ex_date") and p.get("pay_date") and p["ex_date"] <= run_date < p["pay_date"]:
            seen = [b for b in prices.bars(p["market"], p["ticker"]) if closed_by(p["market"], b.date, utc(ts))]
            if not seen or seen[-1].date < p["ex_date"]:
                continue          # the close in tonight's value is still from before the ex-date: the dividend is in it
            keys = {k for k in st["positions"] if k[1] == p["market"] and k[2] == p["ticker"]}
            keys |= {(f["sleeve"], f["market"], f["ticker"]) for f in (x["payload"] for x in L.records("fills"))
                     if f["market"] == p["market"] and f["ticker"] == p["ticker"]}
            for key in keys:
                owed += position_before(L, key, p["ex_date"]) * p["per_share"] * fx.nzd_per(p["ccy"], run_date)
    val = value(st, prices, fx, run_date, utc(ts), rates, receivable_nzd=owed)
    peaks = [r["payload"]["total_nzd"] for r in L.records("valuations")]
    peak = max(peaks + [val["total_nzd"]])
    dd = val["total_nzd"] / peak - 1
    flags = list(report["flags"])
    for line in val["positions"]:
        cap = CAPS.get(line["sleeve"])
        if cap and line["value_nzd"] > cap * val["total_nzd"] * 1.10:
            flags.append(f"{line['market']}:{line['ticker']} is {line['value_nzd'] / val['total_nzd']:.1%} of the portfolio (cap {cap:.0%})")
    if st["cash"].get("NZD", 0.0) < -0.005:
        flags.append(f"NZ$ cash is {st['cash']['NZD']:,.2f}: below zero (convert foreign cash back or sell)")
    if val["cash_nzd_total"] < CASH_FLOOR * val["total_nzd"]:
        flags.append(f"cash {val['cash_nzd_total'] / val['total_nzd']:.1%} is below the 5% floor")
    if dd <= -DRAWDOWN_EXIT:
        flags.append(f"fall from peak {dd:.1%}: move active sleeves to cash and review")
    elif dd <= -DRAWDOWN_HALVE:
        flags.append(f"fall from peak {dd:.1%}: halve the active sleeves")
    L.append("valuations", dict(val, date=run_date, peak_nzd=round(peak, 2), drawdown=round(dd, 5), flags=flags), ts=ts)
    report.update(total_nzd=val["total_nzd"], drawdown=dd, flags=flags)
    return report


def _convert_nzd(L: Ledger, fx: FX, d: str, to: str, nzd_in: float, ts: str) -> None:
    """Convert `nzd_in` NZ$ into currency `to`, paying Sharesies' 0.5% on the NZ$ entered."""
    rate = fx.per_nzd(to, d)
    nzd_in = round(nzd_in, 2)
    L.append("cash", {"kind": "fx_out", "ccy": "NZD", "amount": -nzd_in, "rate": rate, "date": d}, ts=ts)
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


def value(st: dict, prices: Prices, fx: FX, d: str, as_of_utc: datetime | None = None, rates: Rates | None = None,
          receivable_nzd: float = 0.0) -> dict:
    lines, by_sleeve = [], defaultdict(float)
    for (sleeve, m, t), q in st["positions"].items():
        px = prices.last_close(m, t, d, as_of_utc) or 0.0
        v = q * px * fx.nzd_per(CURRENCY[m], d)
        lines.append({"sleeve": sleeve, "market": m, "ticker": t, "qty": q, "close": px, "value_nzd": round(v, 2)})
        by_sleeve[sleeve] += v
    cash_nzd = {c: round(a * fx.nzd_per(c, d), 2) for c, a in st["cash"].items()}
    hedge_mtm = sum(hedge_value_nzd(h, fx, rates, d) for h in st["hedges"].values())
    total = sum(by_sleeve.values()) + sum(cash_nzd.values()) + hedge_mtm + receivable_nzd
    realised = st.get("hedge_realised_nzd", 0.0)
    return {"total_nzd": round(total, 2), "total_unhedged_nzd": round(total - hedge_mtm - realised, 2),
            "positions": lines, "by_sleeve": {k: round(v, 2) for k, v in by_sleeve.items()},
            "cash_local": {c: round(a, 2) for c, a in st["cash"].items()}, "cash_nzd": cash_nzd,
            "cash_nzd_total": round(sum(cash_nzd.values()), 2), "hedge_mtm_nzd": round(hedge_mtm, 2),
            "dividends_owed_nzd": round(receivable_nzd, 2),
            "hedge_realised_nzd": round(realised, 2)}
