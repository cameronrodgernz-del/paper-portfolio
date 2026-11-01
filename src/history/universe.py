"""Norgate's daily prices for every listed and delisted ASX security (data/norgate/universe/), loaded as
wide tables (one row a session, one column a security), and the costs and checks shared by the
history tests 9d to 9f (rulebook, "Shared terms for 9d to 9f").

  open, high, low, close, volume: as traded
  tr: the close with dividends and capital events added back, for returns
A trade at an open is valued on the total-return scale as open x (tr / close) for that session.
"""
import csv
import glob
import gzip
import os

import numpy as np
import pandas as pd

from spreads import spread_estimate

STAKE_AUD = 3000.0
FEE = min(0.019 * STAKE_AUD, 15.0) / STAKE_AUD      # Sharesies ASX brokerage on a A$3,000 order, each side
HEDGE = 0.001                                       # the hedge's dealing cost, once a position
NZD_PER_AUD = 1.08                                  # for the spread floors, which are set in NZ$
MIN_PRICE = 0.10
MIN_VALUE = 50_000.0                                # A$ median daily traded value over 60 sessions
MARKET = "VAS.au"
NOT_SHARES = ("ETF", "EXCHANGE TRADED", " ETP", "ACTIVE FUND", "MANAGED FUND", "OPTION", "WARRANT", "RIGHTS")


def ready(root: str) -> bool:
    d = os.path.join(root, "data", "norgate", "universe")
    return os.path.exists(os.path.join(d, "securities.csv")) and bool(glob.glob(os.path.join(d, "prices_*.csv.gz")))


class Universe:
    def __init__(self, root: str):
        d = os.path.join(root, "data", "norgate", "universe")
        parts = []
        for p in sorted(glob.glob(os.path.join(d, "prices_*.csv.gz"))):
            parts.append(pd.read_csv(p, dtype={"symbol": str}, parse_dates=["date"]))
        df = pd.concat(parts, ignore_index=True)
        df = df.drop_duplicates(["symbol", "date"]).sort_values(["date", "symbol"])
        wide = {}
        for col in ("open", "high", "low", "close", "volume", "tr"):
            src = "tr_close" if col == "tr" else col
            wide[col] = df.pivot(index="date", columns="symbol", values=src).astype("float32")
        self.dates = wide["close"].index
        self.symbols = list(wide["close"].columns)
        self.col = {s: i for i, s in enumerate(self.symbols)}
        self.o, self.h, self.l, self.c = (wide[k].to_numpy() for k in ("open", "high", "low", "close"))
        self.v, self.tr = wide["volume"].to_numpy(), wide["tr"].to_numpy()
        self.tr = np.where(np.isnan(self.tr), self.c, self.tr)
        self.value = self.c * self.v                  # A$ traded each session
        self.sec = {r["symbol"]: r for r in csv.DictReader(open(os.path.join(d, "securities.csv"), encoding="utf-8"))}
        self.datestr = [str(x)[:10] for x in self.dates]

    # ---- positions in the tables ----
    def row_after(self, d: str) -> int | None:
        """The first session after date d."""
        i = int(np.searchsorted(np.array(self.datestr), d, side="right"))
        return i if i < len(self.dates) else None

    def row_on_or_before(self, d: str) -> int | None:
        i = int(np.searchsorted(np.array(self.datestr), d, side="right")) - 1
        return i if i >= 0 else None

    def is_share(self, sym: str) -> bool:
        name = (self.sec.get(sym, {}).get("name") or "").upper()
        return not any(w in name for w in NOT_SHARES)

    # ---- trading checks and costs ----
    def median_value(self, j: int, i: int, n: int = 60) -> float:
        w = self.value[max(0, i - n): i, j]
        w = w[~np.isnan(w)]
        return float(np.median(w)) if len(w) else 0.0

    def tradable(self, j: int, i: int) -> bool:
        """At entry on session i: the last close at least A$0.10 and a median traded value of A$50,000."""
        if i < 1 or np.isnan(self.c[i - 1, j]) or self.c[i - 1, j] < MIN_PRICE:
            return False
        return self.median_value(j, i) >= MIN_VALUE

    def half_spread(self, j: int, i: int) -> float:
        lo, hi = max(0, i - 21), max(1, i - 1)
        hs, ls = self.h[lo:hi, j], self.l[lo:hi, j]
        ok = ~(np.isnan(hs) | np.isnan(ls))
        if ok.sum() < 5:
            return 0.01
        return spread_estimate(list(hs[ok]), list(ls[ok]), self.median_value(j, i, 20) * NZD_PER_AUD) / 2

    def round_trip_cost(self, j: int, i_in: int, i_out: int) -> float:
        """Brokerage both sides, half the spread at entry and at exit, and the hedge's dealing cost."""
        return 2 * FEE + self.half_spread(j, i_in) + self.half_spread(j, i_out) + HEDGE

    # ---- returns on the total-return scale ----
    def tr_open(self, j: int, i: int) -> float:
        c = self.c[i, j]
        return float(self.o[i, j] * (self.tr[i, j] / c)) if c and not np.isnan(c) else float("nan")

    def last_row(self, j: int, upto: int) -> int | None:
        """The last session up to row upto with a price for security j (where a delisted share stops)."""
        col = self.c[: upto + 1, j]
        idx = np.where(~np.isnan(col))[0]
        return int(idx[-1]) if len(idx) else None

    def hold(self, j: int, i_in: int, i_out: int) -> tuple[float, int, str]:
        """Buy at the open of i_in, sell at the open of i_out; a share that stops trading first is sold
        at its last close. Returns (gross return, the row sold on, how it ended)."""
        p0 = self.tr_open(j, i_in)
        i_out = min(i_out, len(self.dates) - 1)
        if not np.isnan(self.c[i_out, j]):
            return self.tr_open(j, i_out) / p0 - 1, i_out, "held"
        last = self.last_row(j, i_out)
        return float(self.tr[last, j]) / p0 - 1, last, "delisted"

    def market(self, i_in: int, i_out: int) -> float:
        """The market's return (VAS with dividends) from the close before i_in to the close before i_out."""
        m = self.col.get(MARKET)
        if m is None:
            raise SystemExit(f"{MARKET} is not in the Norgate universe")
        a, b = self.tr[i_in - 1, m], self.tr[i_out - 1, m]
        return float(b / a - 1)
