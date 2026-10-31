"""Bid-ask spread estimates from daily highs and lows (Corwin and Schultz, 2012).

Free data has no quotes, so the spread is estimated from consecutive daily ranges.
Each two-day estimate below zero is set to zero; the monthly figure is the mean.
A floor by liquidity band stops thin-data months understating the cost.
"""
import math

# Floors on the full (round-trip) spread by median daily traded value in NZD.
FLOORS = [(5_000_000, 0.0010), (1_000_000, 0.0025), (200_000, 0.0060), (0, 0.0150)]


def cs_two_day(h1: float, l1: float, h2: float, l2: float) -> float:
    if min(h1, l1, h2, l2) <= 0:
        return float("nan")
    beta = math.log(h1 / l1) ** 2 + math.log(h2 / l2) ** 2
    gamma = math.log(max(h1, h2) / min(l1, l2)) ** 2
    k = 3 - 2 * math.sqrt(2)
    alpha = (math.sqrt(2 * beta) - math.sqrt(beta)) / k - math.sqrt(gamma / k)
    s = 2 * (math.exp(alpha) - 1) / (1 + math.exp(alpha))
    return max(0.0, s)


def spread_estimate(highs: list[float], lows: list[float], median_value_nzd: float) -> float:
    """Full spread as a fraction of price, over the window given (use about 21 sessions)."""
    vals = [cs_two_day(highs[i], lows[i], highs[i + 1], lows[i + 1]) for i in range(len(highs) - 1)]
    vals = [v for v in vals if not math.isnan(v)]
    est = sum(vals) / len(vals) if vals else 0.0
    floor = next(f for threshold, f in FLOORS if median_value_nzd >= threshold)
    return max(est, floor)
