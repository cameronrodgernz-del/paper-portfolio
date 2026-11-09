"""Checks for sizing and the pre-trade limits. Run: python3 -I tests/test_risk.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from risk import annualised, check_order, kelly, size_position  # noqa: E402

fails = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (f"  [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)


# Kelly for a simple bet: win b per 1 with chance p, lose all of a per 1 otherwise: f* = p/a - q/b
p, b, a = 0.6, 1.0, 1.0
check("Kelly matches the textbook even-money answer (0.2)", abs(kelly([(p, 2.0), (1 - p, 0.0)], 1.0) - 0.2) < 0.002,
      kelly([(p, 2.0), (1 - p, 0.0)], 1.0))
check("no stake when the expected return is not positive", kelly([(0.5, 1.1), (0.5, 0.9)], 1.0) == 0.0)
try:
    kelly([(0.5, 1.1), (0.4, 0.9)], 1.0)
    check("chances that do not add to 1 are refused", False)
except ValueError:
    check("chances that do not add to 1 are refused", True)

# A typical cash scheme: 90% completes at 1.00, 10% breaks to 0.70, price 0.95
s = size_position("deal", [(0.9, 1.0), (0.1, 0.7)], 0.95, 0.70, 100000)
check("deal stake is held to a 1% loss if it breaks", abs(s["share"] - 0.01 / (1 - 0.70 / 0.95)) < 1e-4, s)
s2 = size_position("deal", [(0.97, 1.0), (0.03, 0.93)], 0.98, 0.93, 100000)
check("tight deal stops at the 4% position cap", s2["share"] == 0.04 and "4%" in s2["limited_by"], s2)
check("annualising 2% over 73 days is about 10.4%", abs(annualised(0.02, 73) - 0.1041) < 0.001, annualised(0.02, 73))

val = {"total_nzd": 100000.0, "cash_nzd_total": 30000.0, "by_sleeve": {"core": 40000.0, "deal": 20000.0},
       "positions": [{"sleeve": "core", "market": "US", "ticker": "VT", "value_nzd": 40000.0},
                     {"sleeve": "deal", "market": "ASX", "ticker": "OML", "value_nzd": 3500.0}]}
nzd_per_aud = 1 / 0.81
ok = check_order(val, 0.0, "deal", "ASX", "SDF", "buy", 3000, nzd_per_aud)
check("an ordinary deal entry passes", ok == [], ok)
r = check_order(val, 0.0, "deal", "ASX", "OML", "buy", 1000, nzd_per_aud)
check("adding to a full position breaks the 4% cap", any("cap" in x for x in r), r)
r = check_order(val, 0.0, "deal", "ASX", "SDF", "buy", 1000, nzd_per_aud)
check("an order under A$1,500 is refused", any("minimum" in x for x in r), r)
r = check_order(val, 0.0, "deal", "ASX", "SDF", "buy", 11000, nzd_per_aud)
check("the deal sleeve cannot pass 30%", any("band" in x for x in r), r)
r = check_order(dict(val, cash_nzd_total=7000.0), 0.0, "deal", "ASX", "SDF", "buy", 3000, nzd_per_aud)
check("cash cannot fall under 5%", any("floor" in x for x in r), r)
r = check_order(val, -0.13, "deal", "ASX", "SDF", "buy", 3000, nzd_per_aud, review_pending=True)
check("no new deals after a 12% fall until the review is logged", any("review" in x for x in r), r)
r = check_order(val, -0.09, "deal", "ASX", "SDF", "buy", 3000, nzd_per_aud)
check("after an 8% fall the deal sleeve is held to half weight", any("half" in x for x in r), r)
r = check_order(val, 0.0, "deal", "ASX", "SDF", "buy", 3000, nzd_per_aud, expected_annual=0.02, cash_rate=0.03)
check("a deal must beat the cash rate", any("cash rate" in x for x in r), r)
r = check_order(val, 0.0, "deal", "ASX", "SDF", "buy", 3000, nzd_per_aud, adv_value_nzd=10000)
check("liquidity limit applies (two sessions at 10% of volume)", any("median trading value" in x for x in r), r)
r = check_order(val, 0.0, "research", "ASX", "SDF", "buy", 2500, nzd_per_aud, adv_value_nzd=6000)
check("a research pick may be five sessions at 10% of volume", not any("median trading value" in x for x in r), r)
r = check_order(val, 0.0, "research", "ASX", "SDF", "buy", 2500, nzd_per_aud, adv_value_nzd=4000)
check("but not more", any("five sessions" in x for x in r), r)
r = check_order(val, 0.0, "special", "ASX", "XYZ", "buy", 3000, nzd_per_aud, industry="mining",
                industries={("ASX", "OML"): "mining"}, )
check("industry cap counts holdings outside the core", r == [], r)
r = check_order(dict(val, positions=val["positions"] + [{"sleeve": "special", "market": "ASX", "ticker": "M1", "value_nzd": 13000.0}]),
                0.0, "special", "ASX", "XYZ", "buy", 3000, nzd_per_aud, industry="mining", industries={("ASX", "M1"): "mining"})
check("a second mining name past 15% is refused", any("15%" in x for x in r), r)
import random
rng = random.Random(1)
vetoed = 0
for _ in range(2000):
    tot = rng.uniform(90000, 110000)
    v = {"total_nzd": tot, "cash_nzd_total": 0.5 * tot, "by_sleeve": {}, "positions": []}
    stake = size_position("deal", [(0.99, 1.0), (0.01, 0.99)], 0.985, 0.98, tot)["value_nzd"]
    if any("cap" in x for x in check_order(v, 0.0, "deal", "ASX", "SDF", "buy", stake, nzd_per_aud)):
        vetoed += 1
check("a stake sized at the 4% cap is never vetoed by the cap", vetoed == 0, vetoed)
r = check_order(val, 0.0, "deal", "ASX", "OML", "buy", 300, nzd_per_aud, break_loss=0.32)
check("the 1% loss-on-break counts the position already held", any("breaks" in x for x in r), r)
r = check_order(val, 0.0, "deal", "ASX", "SDF", "buy", 3000, nzd_per_aud, review_pending=True)
check("a pending 12% review blocks new deals", any("review" in x for x in r), r)
check("an unknown sleeve is refused", check_order(val, 0.0, "Deal", "ASX", "SDF", "buy", 3000, nzd_per_aud) != [])
print("\nALL PASS" if not fails else f"\n{len(fails)} FAILED: {fails}")
sys.exit(1 if fails else 0)
