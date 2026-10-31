"""Sizing and pre-trade checks from rulebook sections 3 and 4. No discretion: the analyst states the
odds and prices; this module turns them into a stake and says which limits an order would break.

size_position(): a quarter of the Kelly stake from the stated outcomes, cut to the limits.
check_order(): every limit an order would breach, given the portfolio as it stands. An order with
any breach is not placed; the breach list is logged with the decision.
"""
import math

KELLY_FRACTION = 0.25
CAPS = {"deal": 0.04, "special": 0.03}
BREAK_LOSS_CAP = 0.01                     # loss if a deal breaks: at most 1% of the portfolio
SLEEVE_MAX = {"core": 0.45, "deal": 0.30, "special": 0.20}
INDUSTRY_CAP = 0.15                       # one industry outside the core
GROUP_CAP = 0.10                          # deals waiting on one regulator, or from one bidder
MIN_ORDER = {"NZX": ("NZD", 2500), "ASX": ("AUD", 1500), "US": ("USD", 500)}
CASH_FLOOR = 0.05
LIQ_SESSIONS, LIQ_SHARE = 2, 0.10         # no position over two sessions at 10% of daily volume
DD_HALVE, DD_EXIT = 0.08, 0.12


def kelly(outcomes: list[tuple[float, float]], price: float, steps: int = 2000) -> float:
    """Growth-optimal share of capital for buying at `price` when the outcome prices and chances
    are as stated (chances must add to 1). Long only, so the answer is between 0 and 1."""
    total = sum(p for p, _ in outcomes)
    if abs(total - 1) > 1e-6:
        raise ValueError(f"chances add to {total:.3f}, not 1")
    rets = [(p, v / price - 1) for p, v in outcomes]
    if sum(p * r for p, r in rets) <= 0:
        return 0.0
    worst = min(r for _, r in rets)
    hi = 1.0 if worst >= 0 else min(1.0, 0.999 / -worst)
    best_f, best_g = 0.0, 0.0
    for i in range(1, steps + 1):
        f = hi * i / steps
        g = sum(p * math.log(1 + f * r) for p, r in rets)
        if g > best_g:
            best_f, best_g = f, g
    return best_f


def size_position(sleeve: str, outcomes: list[tuple[float, float]], price: float, break_price: float | None,
                  portfolio_nzd: float) -> dict:
    """Stake in NZ$ and the reason it stopped where it did."""
    full = kelly(outcomes, price)
    share, why = full * KELLY_FRACTION, "quarter Kelly"
    cap = CAPS.get(sleeve)
    if cap is not None and share > cap:
        share, why = cap, f"{cap:.0%} position cap"
    if sleeve == "deal" and break_price is not None and price > break_price:
        loss = 1 - break_price / price
        if share * loss > BREAK_LOSS_CAP:
            share, why = BREAK_LOSS_CAP / loss, f"1% loss-on-break cap (break loss {loss:.1%})"
    ev = sum(p * v for p, v in outcomes) / price - 1
    return {"kelly_full": round(full, 4), "share": round(share, 4), "value_nzd": round(share * portfolio_nzd, 2),
            "limited_by": why, "expected_return": round(ev, 4)}


def annualised(expected_return: float, days: int) -> float:
    return (1 + expected_return) ** (365 / max(days, 1)) - 1


def check_order(val: dict, drawdown: float, sleeve: str, market: str, ticker: str, side: str, value_nzd: float,
                nzd_per_local: float, adv_value_nzd: float | None = None, industry: str | None = None,
                industries: dict | None = None, group: str | None = None, groups: dict | None = None,
                expected_annual: float | None = None, cash_rate: float | None = None) -> list[str]:
    """All the limits this order would breach. `val` is the clerk's latest valuation; `industries`
    and `groups` map (market, ticker) of current holdings to their industry and regulator/bidder group."""
    out = []
    total = val["total_nzd"]
    held = {(p["market"], p["ticker"]): p["value_nzd"] for p in val["positions"] if p["sleeve"] == sleeve}
    after_pos = held.get((market, ticker), 0.0) + (value_nzd if side == "buy" else -value_nzd)
    ccy, smallest = MIN_ORDER[market]
    if value_nzd / nzd_per_local < smallest - 1e-6:
        out.append(f"order of {value_nzd / nzd_per_local:,.0f} {ccy} is below the {smallest:,} {ccy} minimum")
    if side == "sell":
        return out
    cap = CAPS.get(sleeve)
    if cap is not None and after_pos > cap * total + 1e-6:
        out.append(f"position would be {after_pos / total:.1%}, over the {cap:.0%} cap")
    sleeve_now = val["by_sleeve"].get(sleeve, 0.0)
    if sleeve in SLEEVE_MAX and sleeve_now + value_nzd > SLEEVE_MAX[sleeve] * total + 1e-6:
        out.append(f"{sleeve} sleeve would be {(sleeve_now + value_nzd) / total:.1%}, over its {SLEEVE_MAX[sleeve]:.0%} band")
    if val["cash_nzd_total"] - value_nzd < CASH_FLOOR * total:
        out.append(f"cash would fall to {(val['cash_nzd_total'] - value_nzd) / total:.1%}, under the 5% floor")
    if sleeve != "core" and industry:
        ind_now = sum(p["value_nzd"] for p in val["positions"] if p["sleeve"] != "core"
                      and (industries or {}).get((p["market"], p["ticker"])) == industry)
        if ind_now + value_nzd > INDUSTRY_CAP * total + 1e-6:
            out.append(f"{industry} would be {(ind_now + value_nzd) / total:.1%} outside the core, over 15%")
    if sleeve == "deal" and group:
        g_now = sum(p["value_nzd"] for p in val["positions"] if p["sleeve"] == "deal"
                    and (groups or {}).get((p["market"], p["ticker"])) == group)
        if g_now + value_nzd > GROUP_CAP * total + 1e-6:
            out.append(f"deals in group '{group}' would be {(g_now + value_nzd) / total:.1%}, over 10%")
    if adv_value_nzd is not None and after_pos > LIQ_SESSIONS * LIQ_SHARE * adv_value_nzd + 1e-6:
        out.append(f"position would be {after_pos / adv_value_nzd:.0%} of a day's median trading value; "
                   f"the limit is {LIQ_SESSIONS * LIQ_SHARE:.0%} (two sessions at 10%)")
    if sleeve in ("deal", "special"):
        if drawdown <= -DD_EXIT:
            out.append(f"portfolio is {drawdown:.1%} from its peak: no new active positions until the review")
        elif drawdown <= -DD_HALVE and sleeve_now + value_nzd > 0.5 * {"deal": 0.25, "special": 0.15}[sleeve] * total:
            out.append(f"portfolio is {drawdown:.1%} from its peak: the {sleeve} sleeve is held to half its weight")
    if sleeve == "deal" and expected_annual is not None and cash_rate is not None and expected_annual <= cash_rate:
        out.append(f"expected return {expected_annual:.1%} a year is not above the cash rate {cash_rate:.1%}")
    return out
