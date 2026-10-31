"""Price, currency and calendar helpers for the engine.

Prices: data/prices/<market>/<ticker>.csv (unadjusted open, high, low, close, volume).
Currency: data/fx/fx_daily.csv from the RBA (nzd_usd, nzd_aud = units of foreign per NZ$1).
A session's opening time decides which orders it can fill: an order fills only in a
session that opens after the decision was logged.
"""
import csv
import math
import os
from datetime import date, datetime, time, timezone
from functools import lru_cache
from zoneinfo import ZoneInfo

from fills import Bar
from spreads import spread_estimate

OPEN = {"NZX": ("Pacific/Auckland", time(10, 0)), "ASX": ("Australia/Sydney", time(10, 0)),
        "US": ("America/New_York", time(9, 30))}
CURRENCY = {"NZX": "NZD", "ASX": "AUD", "US": "USD"}
# A session's prices count as final from these local times: the close plus the closing auction and a margin
# (NZX closes 4:45pm, ASX's closing auction ends about 4:12pm, US markets close 4pm).
FINAL = {"NZX": time(17, 0), "ASX": time(16, 30), "US": time(16, 30)}


def session_open_utc(market: str, d: str) -> datetime:
    tz, t = OPEN[market]
    return datetime.combine(date.fromisoformat(d), t, ZoneInfo(tz)).astimezone(timezone.utc)


def session_final_utc(market: str, d: str) -> datetime:
    tz, _ = OPEN[market]
    return datetime.combine(date.fromisoformat(d), FINAL[market], ZoneInfo(tz)).astimezone(timezone.utc)


def closed_by(market: str, d: str, as_of_utc: datetime) -> bool:
    """True once that session's prices are final (see FINAL) at the given time."""
    return session_final_utc(market, d) <= as_of_utc


def nz_evening_utc(d: str, hh: int = 21, mm: int = 0) -> datetime:
    """The daily run's time: 9pm in New Zealand on that date, in UTC (moves with daylight saving)."""
    return datetime.combine(date.fromisoformat(d), time(hh, mm), ZoneInfo("Pacific/Auckland")).astimezone(timezone.utc)


class Prices:
    def __init__(self, data_dir: str):
        self.dir = data_dir

    @lru_cache(maxsize=None)
    def bars(self, market: str, ticker: str) -> tuple:
        p = os.path.join(self.dir, "prices", market, f"{ticker}.csv")
        if not os.path.exists(p):
            return tuple()
        out = []
        with open(p, newline="") as f:
            for r in csv.DictReader(f):
                try:
                    out.append(Bar(r["date"], float(r["open"] or 0), float(r["high"] or 0), float(r["low"] or 0),
                                   float(r["close"] or 0), float(r["volume"] or 0)))
                except ValueError:
                    continue
        return tuple(out)

    def bar_on(self, market: str, ticker: str, d: str) -> Bar | None:
        return next((b for b in self.bars(market, ticker) if b.date == d), None)

    def last_close(self, market: str, ticker: str, d: str, as_of_utc: datetime | None = None) -> float | None:
        """Last close on or before date d; with as_of_utc, only sessions that had closed by then."""
        prior = [b for b in self.bars(market, ticker) if b.date <= d and b.close > 0
                 and (as_of_utc is None or closed_by(market, b.date, as_of_utc))]
        return prior[-1].close if prior else None

    def history(self, market: str, ticker: str, before: str, n: int = 21) -> list[Bar]:
        return [b for b in self.bars(market, ticker) if b.date < before][-n:]

    def stats(self, market: str, ticker: str, before: str, nzd_per_local: float) -> dict:
        """20-session median traded value (NZD), average traded value (local), daily volatility, spread."""
        h = self.history(market, ticker, before, 21)
        if len(h) < 5:
            return {"adv_local": 0.0, "median_value_nzd": 0.0, "daily_vol": 0.03, "spread": 0.015}
        values = sorted(b.close * b.volume for b in h)
        rets = [math.log(b.close / a.close) for a, b in zip(h, h[1:]) if a.close > 0 and b.close > 0]
        vol = (sum(r * r for r in rets) / max(1, len(rets))) ** 0.5 if rets else 0.03
        median_nzd = values[len(values) // 2] * nzd_per_local
        spread = spread_estimate([b.high for b in h], [b.low for b in h], median_nzd)
        return {"adv_local": sum(values) / len(values), "median_value_nzd": median_nzd, "daily_vol": vol, "spread": spread}


class FX:
    """Units of foreign currency per NZ$1, latest published on or before the date."""

    def __init__(self, data_dir: str):
        self.rows = []
        p = os.path.join(data_dir, "fx", "fx_daily.csv")
        with open(p, newline="") as f:
            for r in csv.DictReader(f):
                d = datetime.strptime(r["date"], "%d-%b-%Y").date().isoformat()
                self.rows.append((d, float(r["nzd_usd"]), float(r["nzd_aud"])))
        self.rows.sort()

    def per_nzd(self, ccy: str, d: str) -> float:
        if ccy == "NZD":
            return 1.0
        prior = [r for r in self.rows if r[0] <= d]
        if not prior:
            raise ValueError(f"no FX on or before {d}")
        row = prior[-1]
        return row[1] if ccy == "USD" else row[2]

    def nzd_per(self, ccy: str, d: str) -> float:
        return 1.0 / self.per_nzd(ccy, d)
