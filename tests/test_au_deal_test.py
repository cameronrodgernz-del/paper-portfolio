"""Checks for the ASX deal history test (rulebook 9c, src/history/au_deal_test.py) on made-up prices."""
import os
import sys
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "src"))
sys.path.insert(0, os.path.join(HERE, "..", "src", "history"))
import au_deal_test as t  # noqa: E402

fails = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail and not ok else ""))
    if not ok:
        fails.append(name)


class FlatRates:
    def three_month(self, ccy, d):
        return 0.04


def series(start: str, n: int, before: float, after: float, jump_at: int) -> list[dict]:
    out, d = [], date.fromisoformat(start)
    while len(out) < n:
        if d.weekday() < 5:
            p = before if len(out) < jump_at else after
            out.append({"date": d.isoformat(), "open": p, "high": p * 1.01, "low": p * 0.99, "close": p, "volume": 100000})
        d += timedelta(days=1)
    return out


px = series("2020-01-01", 200, 1.00, 1.45, 30)            # announced on session 30, offer A$1.50
ann = px[29]["date"]
paid = {"id": "X", "ticker": "X", "announce": ann, "offer": 1.50, "paid": 1.50, "y": 1, "pay_date": px[120]["date"], "outcome_date": px[118]["date"], "booklet": "", "structure": "scheme"}
st, r = t.result(paid, px, FlatRates(), ann)
check("a paid deal is credited at the final price on the payment date", st == "ok" and r["kind"] == "paid" and abs(r["gross"] - (1.50 / 1.45 - 1)) < 1e-9, (st, r))
check("costs include brokerage, conversion, the hedge and half the spread", r and r["costs"] > t.FEE + t.FX_ROUND_TRIP + t.HEDGE, r)
check("cash over the same days comes off the result", r and r["net"] < r["gross"] - r["costs"], r)
broke = dict(paid, y=0, outcome_date=px[100]["date"])
px2 = px[:101] + [dict(b, open=1.05, close=1.05, high=1.06, low=1.04) for b in px[101:]]
st, r = t.result(broke, px2, FlatRates(), ann)
check("a broken deal is sold at the next open after it ended, with costs", st == "ok" and r["kind"] == "broke" and abs(r["gross"] - (1.05 / 1.45 - 1)) < 1e-9, (st, r))
other = dict(paid, offer=3.00, paid=3.00)
st, r = t.result(other, px, FlatRates(), ann)
check("a price far from the offer fails the entry check (a different share on the code)", r is None and "entry price" in st, st)
early = dict(paid, pay_date=px[30]["date"])
st, r = t.result(early, px, FlatRates(), ann)
check("a payment before the entry date is left out", r is None, st)

print("\nALL PASS" if not fails else f"\n{len(fails)} FAILED: {fails}")
sys.exit(1 if fails else 0)
