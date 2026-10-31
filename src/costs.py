"""Trading costs as Sharesies NZ charges them (pricing page checked 31 Oct 2026).

Fees: 1.9% of the order, capped per order at NZ$25 (NZX), A$15 (ASX), US$5 (US).
Plan: $15 a month covers fees on the first NZ$5,000 of buy and sell orders each month.
Assumption (not stated by Sharesies): an order that straddles the end of the plan's
coverage pays the capped fee only on the uncovered part.
Currency: 0.5% of the amount exchanged.
"""
from dataclasses import dataclass, field

FEE_RATE = 0.019
FEE_CAP = {"NZX": ("NZD", 25.0), "ASX": ("AUD", 15.0), "US": ("USD", 5.0)}
FX_FEE = 0.005
PLAN_MONTHLY_NZD = 15.0
PLAN_COVER_NZD = 5000.0


@dataclass
class PlanState:
    """Tracks how much of this month's plan coverage is left."""
    month: str = ""          # 'YYYY-MM'
    used_nzd: float = 0.0
    fees_waived_nzd: float = field(default=0.0)

    def roll(self, month: str) -> bool:
        """Start a new month; returns True when the monthly plan fee falls due."""
        if month != self.month:
            self.month, self.used_nzd = month, 0.0
            return True
        return False


def brokerage(market: str, amount_local: float, amount_nzd: float, plan: PlanState) -> float:
    """Brokerage in the order's local currency for one order (buy or sell)."""
    if market not in FEE_CAP:
        raise ValueError(f"unknown market {market}")
    if amount_local <= 0:
        return 0.0
    _, cap = FEE_CAP[market]
    covered_nzd = max(0.0, min(PLAN_COVER_NZD - plan.used_nzd, amount_nzd))
    plan.used_nzd += amount_nzd
    uncovered_share = 1.0 - covered_nzd / amount_nzd
    if uncovered_share <= 0:
        return 0.0
    uncovered_local = amount_local * uncovered_share
    return round(min(FEE_RATE * uncovered_local, cap), 2)


def fx_convert(amount_from: float, rate_to_per_from: float) -> tuple[float, float]:
    """Convert currency the Sharesies way: the 0.5% fee comes off the amount entered.
    Returns (amount received in the target currency, fee in the source currency)."""
    fee = round(amount_from * FX_FEE, 2)
    return (amount_from - fee) * rate_to_per_from, fee
