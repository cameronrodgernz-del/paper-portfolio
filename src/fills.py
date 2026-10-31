"""Fill rules. An order only ever fills on a session that starts after the decision time.

Market order: the session's official open, plus half the spread (buy) or less half the
spread (sell), plus a size cost. Limit order: only on a session that trades THROUGH the
limit by at least 0.1%, at the limit (or the open if the open is already better).
No fill above 10% of the session's volume; the rest rolls to the next session.
A session with zero volume or a missing open gives no fill.
"""
import math
from dataclasses import dataclass

PARTICIPATION = 0.10       # max share of a session's volume
THROUGH = 0.001            # a limit must be traded through by 0.1%
IMPACT_K = 1.0             # square-root size cost multiplier
IMPACT_CAP = 0.02          # size cost never above 2% of price


@dataclass
class Bar:
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: float


@dataclass
class Fill:
    date: str
    qty: float
    price: float
    remaining: float
    reason: str


def size_cost(order_value: float, adv_value: float, daily_vol: float) -> float:
    """Square-root rule: cost = k * daily volatility * sqrt(order value / average daily value)."""
    if adv_value <= 0:
        return IMPACT_CAP
    return min(IMPACT_CAP, IMPACT_K * daily_vol * math.sqrt(order_value / adv_value))


def fill_order(side: str, qty: float, bar: Bar, spread: float, adv_value: float,
               daily_vol: float, limit: float | None = None) -> Fill:
    """side is 'buy' or 'sell'; qty in shares; spread is the full spread as a fraction."""
    sgn = 1 if side == "buy" else -1
    if bar.volume <= 0 or not bar.open or bar.open <= 0:
        return Fill(bar.date, 0.0, 0.0, qty, "no trading")
    cap = math.floor(PARTICIPATION * bar.volume)
    take = min(qty, cap)
    if take <= 0:
        return Fill(bar.date, 0.0, 0.0, qty, "volume cap")
    if limit is None:
        cost = spread / 2 + size_cost(take * bar.open, adv_value, daily_vol)
        price = bar.open * (1 + sgn * cost)
        reason = "market at open"
    else:
        open_better = bar.open <= limit if side == "buy" else bar.open >= limit
        traded_through = bar.low <= limit * (1 - THROUGH) if side == "buy" else bar.high >= limit * (1 + THROUGH)
        if open_better:
            # Opens at or better than the limit: fills at the open plus half the spread, never worse than the limit.
            raw = bar.open * (1 + sgn * spread / 2)
            price = min(raw, limit) if side == "buy" else max(raw, limit)
            reason = "limit, opened better"
        elif traded_through:
            price = limit
            reason = "limit traded through"
        else:
            return Fill(bar.date, 0.0, 0.0, qty, "limit not traded through")
    return Fill(bar.date, take, round(price, 6), qty - take, reason)
