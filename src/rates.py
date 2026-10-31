"""Three-month interest rates by currency, from free official series already in data/rates.

NZD: FRED IR3TIB01NZM156N (NZ 3-month interbank, monthly, from the OECD).
AUD: RBA F1.1, 3-month bank bills (monthly average).
USD: FRED DTB3 (3-month Treasury bills, daily).
Each lookup returns the latest value published on or before the date, as a decimal.
The forward rate follows from the gap between two of them (covered interest parity).
"""
import csv
import os
from datetime import datetime
from functools import lru_cache


class Rates:
    def __init__(self, data_dir: str):
        self.dir = os.path.join(data_dir, "rates")

    @lru_cache(maxsize=None)
    def series(self, ccy: str) -> tuple:
        out = []
        if ccy in ("NZD", "USD"):
            name = "IR3TIB01NZM156N" if ccy == "NZD" else "DTB3"
            with open(os.path.join(self.dir, f"{name}.csv"), newline="") as f:
                for r in csv.DictReader(f):
                    v = r.get(name, "")
                    if v and v != ".":
                        k = r["observation_date"]
                        if ccy == "NZD":   # a monthly average dated the 1st is only known once the month ends
                            y, m = int(k[:4]), int(k[5:7])
                            k = f"{y + m // 12}-{m % 12 + 1:02d}-01"
                        out.append((k, float(v) / 100))
        elif ccy == "AUD":
            with open(os.path.join(self.dir, "rba_f1_1.csv"), encoding="utf-8-sig", newline="") as f:
                rows = list(csv.reader(f))
            col = next(i for i, h in enumerate(rows[1]) if h.strip() == "3-month BABs/NCDs")
            for r in rows:
                if r and "/" in r[0] and len(r) > col and r[col].strip():
                    # monthly averages are dated at month end; treat them as known from that date
                    out.append((datetime.strptime(r[0], "%d/%m/%Y").date().isoformat(), float(r[col]) / 100))
        else:
            raise ValueError(ccy)
        return tuple(sorted(out))

    def three_month(self, ccy: str, d: str) -> float:
        prior = [v for k, v in self.series(ccy) if k <= d]
        if not prior:
            raise ValueError(f"no {ccy} rate on or before {d}")
        return prior[-1]

    def forward_per_nzd(self, ccy: str, spot_per_nzd: float, d: str, days: int) -> float:
        """Forward units of foreign currency per NZ$1 for `days` ahead (simple interest)."""
        t = max(days, 0) / 365
        return spot_per_nzd * (1 + self.three_month(ccy, d) * t) / (1 + self.three_month("NZD", d) * t)
