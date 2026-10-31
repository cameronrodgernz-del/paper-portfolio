"""Checks for the nightly data checks (src/data_checks.py)."""
import csv
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
import data_checks as dc  # noqa: E402

fails = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail and not ok else ""))
    if not ok:
        fails.append(name)


def write(root, m, t, rows):
    os.makedirs(os.path.join(root, "data", "prices", m), exist_ok=True)
    with open(os.path.join(root, "data", "prices", m, f"{t}.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["date", "open", "high", "low", "close", "volume"]); w.writerows(rows)


with tempfile.TemporaryDirectory() as root:
    os.makedirs(os.path.join(root, "config"))
    open(os.path.join(root, "config", "live_deals.csv"), "w").write("deal_id,target_market,target_ticker,acquirer_market,acquirer_ticker,announce_date\nD1,ASX,DEAL,,,2026-10-21\n")
    days = ["2026-10-19", "2026-10-20", "2026-10-21", "2026-10-22", "2026-10-23", "2026-10-26"]
    write(root, "ASX", "GOOD", [[d, 1, 1.02, 0.98, 1.0, 1000] for d in days])
    write(root, "ASX", "JUMP", [[d, 1, 1.02, 0.98, 1.0 if i < 4 else 1.6, 1000] for i, d in enumerate(days)])
    write(root, "ASX", "DEAL", [[d, 1, 1.5, 0.98, 1.0 if i < 2 else 1.45, 1000] for i, d in enumerate(days)])
    write(root, "ASX", "OLD", [[d, 1, 1.02, 0.98, 1.0, 1000] for d in days[:2]])
    write(root, "ASX", "BAD", [[d, 1, 1.02, 0.98, 1.0 if i != 3 else 1.10, 1000] for i, d in enumerate(days)])
    iss = dc.check_prices(root, {("ASX", t) for t in ("GOOD", "JUMP", "DEAL", "OLD", "BAD")})
    kinds = {(i["ticker"], i["kind"]) for i in iss}
    check("a clean share raises nothing", not any(t == "GOOD" for t, _ in kinds), kinds)
    check("a 60% jump is flagged", ("JUMP", "jump") in kinds, kinds)
    check("a jump on a deal's announcement day is flagged as the deal", any(i["ticker"] == "DEAL" and "deal announced" in i["text"] for i in iss), iss)
    check("a share four days behind its market is stale", ("OLD", "stale") in kinds, kinds)
    check("a close above the day's high is a bad bar", ("BAD", "bad_bar") in kinds, kinds)
    check("a missing file is reported", any(i["kind"] == "missing" for i in dc.check_prices(root, {("ASX", "NONE")})))

print("\nALL PASS" if not fails else f"\n{len(fails)} FAILED: {fails}")
sys.exit(1 if fails else 0)
