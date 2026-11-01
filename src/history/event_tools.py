"""Shared pieces for history tests 9g to 9j (rulebook, "Shared terms for 9g to 9j"): the equal-weighted
benchmark of tradable ordinary shares, the t-statistic on monthly averages, and ASIC's daily files.
Kept apart from universe.py so the code behind the locked tests 9d to 9f doesn't change.
"""
import csv
import glob
import gzip
import math
import os
import statistics as stats
from collections import defaultdict

import numpy as np

from universe import MIN_PRICE, MIN_VALUE, Universe


class Bench:
    """Equal-weighted return of every tradable ordinary share, bought at the open of i_in and sold at the
    open of i_out (a share that stops trading is sold at its last close)."""

    def __init__(self, u: Universe):
        self.u = u
        self.share = np.array([u.is_share(s) and "DEFERRED" not in (u.sec.get(s, {}).get("name") or "").upper() for s in u.symbols])
        with np.errstate(all="ignore"):
            self.tro = u.o * (u.tr / u.c)                     # the open on the total-return scale
        tr = u.tr.copy()
        for i in range(1, tr.shape[0]):                       # last known total-return value, for delisted shares
            m = np.isnan(tr[i])
            tr[i, m] = tr[i - 1, m]
        self.tr_ff = tr
        self._elig = {}

    def eligible(self, i_in: int) -> np.ndarray:
        if i_in not in self._elig:
            u = self.u
            with np.errstate(all="ignore"):
                medv = np.nanmedian(u.value[max(0, i_in - 60): i_in], axis=0)
                ok = self.share & (u.c[i_in - 1] >= MIN_PRICE) & (medv >= MIN_VALUE) & np.isfinite(self.tro[i_in])
            self._elig[i_in] = ok
        return self._elig[i_in]

    def ret(self, i_in: int, i_out: int, cols: np.ndarray | None = None) -> float:
        ok = self.eligible(i_in) if cols is None else cols
        i_out = min(i_out, len(self.u.dates) - 1)
        p0 = self.tro[i_in, ok]
        p1 = np.where(np.isfinite(self.tro[i_out, ok]), self.tro[i_out, ok], self.tr_ff[i_out, ok])
        r = p1 / p0 - 1
        r = r[np.isfinite(r)]
        return float(np.mean(r)) if len(r) else float("nan")


def monthly_t(events: list[dict], key: str = "result", month_of: str = "month") -> tuple[float, int]:
    """t-statistic of the mean across months, each month the average of its events."""
    by = defaultdict(list)
    for e in events:
        by[e[month_of]].append(e[key])
    ms = [stats.mean(v) for v in by.values()]
    if len(ms) < 3 or stats.stdev(ms) == 0:
        return float("nan"), len(ms)
    return stats.mean(ms) / (stats.stdev(ms) / math.sqrt(len(ms))), len(ms)


def top_year_share(events: list[dict], key: str = "result", year_of: str = "year") -> float:
    by = defaultdict(float)
    for e in events:
        by[e[year_of]] += e[key]
    total = sum(by.values())
    return max(by.values()) / total if total > 0 else float("inf")


def trimmed_mean(xs: list[float], frac: float = 0.05) -> float:
    k = max(1, round(frac * len(xs)))
    return stats.mean(sorted(xs)[:-k]) if len(xs) > k else float("nan")


def asic(root: str) -> dict:
    """ASIC daily short files: {code: (dates[], short[], issue[])}, dates as YYYY-MM-DD strings."""
    out = defaultdict(lambda: ([], [], []))
    for p in sorted(glob.glob(os.path.join(root, "data", "asic", "shorts_*.csv.gz"))):
        with gzip.open(p, "rt", newline="") as f:
            for r in csv.DictReader(f):
                d, s, n = out[r["code"]]
                d.append(r["date"]); s.append(float(r["short"] or "nan")); n.append(float(r["issue"] or "nan"))
    return dict(out)


def code_of(sym: str) -> str:
    return sym.split("-")[0].split(".")[0].upper()
