"""Checks for the insider-cluster history test on made-up prices. Run: python3 -I tests/test_insider_history.py"""
import os
import sys
from datetime import date, timedelta

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "src"))
sys.path.insert(0, os.path.join(ROOT, "src", "history"))
from insider_events import clusters  # noqa: E402
from insider_test import event_result, summarise  # noqa: E402

fails = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (f"  [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)


def series(start, n, p0, step, split_at=None, vol=2e6):
    out, d, p = [], date.fromisoformat(start), p0
    k = 1.0
    while len(out) < n:
        if d.weekday() < 5:
            raw = p / (2.0 if split_at is not None and len(out) >= split_at else 1.0)
            out.append({"date": d.isoformat(), "open": raw, "high": raw * 1.01, "low": raw * 0.99, "close": raw,
                        "volume": vol / raw, "aopen": p * k / 2.0 if split_at is not None else p, "aclose": p})
            p *= 1 + step
        d += timedelta(days=1)
    if split_at is not None:     # adjusted series is in post-split terms throughout
        for b in out:
            b["aopen"] = b["aclose"] = b["aclose"] / 2.0
    return out


px = series("2015-01-01", 200, 10.0, 0.001)
spy = {b["date"]: b for b in series("2015-01-01", 200, 100.0, 0.0)}
ev = {"ticker": "XYZ", "event_date": px[30]["date"], "first_trade": px[25]["date"], "avg_price": f"{px[25]['close']:.4f}"}
status, r = event_result(ev, px, spy, 63, 1e6)
check("a clean event gives a result", status == "ok", status)
if r:
    check("entry is the open after the filing date", r["entry"] == px[31]["date"], (r["entry"], px[31]["date"]))
    check("exit is the open 63 sessions after entry", r["exit"] == px[31 + 63]["date"], r["exit"])
    check("return is about 0.1% a session over 63 sessions", abs(r["raw"] - (1.001 ** 63 - 1)) < 1e-6, r["raw"])
    check("costs include brokerage, currency and spread", 0.011 < r["costs"] < 0.03, r["costs"])
    check("net is return less benchmark less costs", abs(r["net"] - (r["raw"] - r["bench"] - r["costs"])) < 1e-12)
bad = dict(ev, avg_price="20.0")
check("a purchase price far from the close fails the reused-ticker check", event_result(bad, px, spy, 63, 1e6)[0].startswith("price check"))
check("an event too recent to exit is skipped", event_result(dict(ev, event_date=px[150]["date"], first_trade=px[149]["date"],
                                                              avg_price=f"{px[149]['close']:.4f}"), px, spy, 63, 1e6)[0] == "exit not reached yet")
thin = series("2015-01-01", 200, 10.0, 0.001, vol=2e5)
check("thinly traded shares are left out", event_result(ev | {"avg_price": f"{thin[25]['close']:.4f}"}, thin, spy, 63, 1e6)[0] == "too little trading")
sp = series("2015-01-01", 200, 10.0, 0.0, split_at=60)
st, rr = event_result(ev | {"avg_price": f"{sp[25]['close']:.4f}"}, sp, spy, 63, 1e6)
check("a 2-for-1 split inside the hold does not show as a loss", st == "ok" and abs(rr["raw"]) < 1e-9, (st, rr and rr["raw"]))
s = summarise([{"net": x, "costs": 0.01, "raw": x, "bench": 0.0, "year": y} for x, y in
               [(0.05, "2020"), (0.04, "2021"), (-0.01, "2021"), (0.03, "2022"), (0.5, "2023")]])
check("one big year is caught by the half-the-gain test", s["top_year"][0] == "2023" and s["top_year_share"] > 0.5, s["top_year_share"])
check("trimming drops the best 5% (at least one event)", abs(s["trimmed_mean"] - (0.05 + 0.04 - 0.01 + 0.03) / 4) < 1e-12, s["trimmed_mean"])

buys = [{"issuer_cik": "1", "ticker": "AAA", "issuer_name": "A", "owner_cik": o, "role": "director", "filing_date": f, "trans_date": t,
         "value_usd": 60000.0, "shares": 6000.0}
        for o, f, t in [("a", "2015-03-02", "2015-02-27"), ("b", "2015-03-10", "2015-03-06"), ("c", "2015-03-20", "2015-03-18"),
                        ("d", "2015-04-01", "2015-03-30"), ("a", "2015-09-01", "2015-08-28"), ("b", "2015-09-03", "2015-09-01")]]
ev2 = clusters(buys, 2)
check("two buyers within 30 days make a cluster, dated at the second filing", ev2 and ev2[0]["event_date"] == "2015-03-10", ev2[:1])
check("later buying inside 90 days is the same cluster", len([e for e in ev2 if e["event_date"] < "2015-06-01"]) == 1, ev2)
check("buying after a 90-day gap is a new cluster", any(e["event_date"] == "2015-09-03" for e in ev2), [e["event_date"] for e in ev2])
ev3 = clusters(buys, 3)
check("three buyers: dated at the third filing", ev3 and ev3[0]["event_date"] == "2015-03-20", ev3[:1])
check("a cluster needs US$100,000 in all", not clusters([dict(b, value_usd=10000.0) for b in buys], 2))
print("\nALL PASS" if not fails else f"\n{len(fails)} FAILED: {fails}")
sys.exit(1 if fails else 0)
