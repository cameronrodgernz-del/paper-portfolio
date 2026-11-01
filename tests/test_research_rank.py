"""Checks for src/research_rank.py: gates drop only on rules, special situations are routed, points add up."""
import csv
import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
import research_rank as rr  # noqa: E402

fails = 0


def check(label, ok, got=None):
    global fails
    print(("PASS " if ok else "FAIL ") + label + ("" if ok else f"  (got {got})"))
    fails += 0 if ok else 1


root = tempfile.mkdtemp()
for d in ("reports", "data/research_data", "data/norgate", "config", "research/picks"):
    os.makedirs(os.path.join(root, d), exist_ok=True)
fields = ["group", "market", "ticker", "name", "price", "market_value_m", "median_traded_k", "traded_days_of_60", "return_12m",
          "below_high", "dividends_12m", "volatility", "short_pct", "as_of"]
screen = [
    ("Others", "ASX", "AAA", "Cheap Steady Limited", 1.00, -0.10, -0.40, 0.002),
    ("Others", "ASX", "BBB", "Bid Target Limited", 2.00, 0.10, -0.05, 0.0),
    ("Others", "ASX", "CCC", "Explorer Minerals Limited", 0.20, -0.50, -0.60, 0.0),
    ("Others", "ASX", "DDD", "Lucky Gaming Limited", 1.00, 0.0, -0.10, 0.0),
    ("Listed investment companies and trusts (check the discount to net assets)", "ASX", "EEE", "Value Investment Company", 1.0, 0, 0, 0),
    ("Others", "ASX", "FFF", "Shorted Limited", 1.00, -0.60, -0.70, 0.08),
    ("Others", "ASX", "III", "Plain Name Limited", 1.00, 0.0, -0.10, 0.0),
    ("NZX outside the NZX 20", "NZX", "GGG", "Kiwi Assets Limited Ordinary Shares", 1.00, -0.20, -0.36, ""),
    ("NZX outside the NZX 20", "NZX", "HHH", "Thin Limited Ordinary Shares", 1.00, 0.0, 0.0, ""),
]
with open(os.path.join(root, "reports", "research_screen.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for g, m, t, n, px, r12, bh, sp in screen:
        w.writerow({"group": g, "market": m, "ticker": t, "name": n, "price": px, "return_12m": r12, "below_high": bh,
                    "short_pct": sp, "as_of": "2026-10-30"})


def asx_entry(mcap, eps, ta, tl, ev, yld, incomes, revs, group, anns):
    return {"fetched": "2026-11-01T00:00:00+00:00", "errors": [],
            "header": {"marketCap": mcap, "industryGroup": group},
            "key-statistics": {"earningsPerShare": eps, "totalAssets": ta, "totalLiabilities": tl, "enterprisevalue": ev,
                               "yieldAnnual": yld,
                               "incomeStatement": [{"netIncome": i, "revenue": r} for i, r in zip(incomes, revs)]},
            "announcements": anns}


A = {
    # 7 times earnings (2), 0.67 times book (2), net cash 40% (2), 7% yield (1), four profitable years (1), small (1),
    # 40% below high (1) = 10; the result a year ago and two director notices are shown but don't score
    "AAA": asx_entry(100e6, 0.143, 250, 100, 60, 7.0, [14e6, 13e6, 12e6, 11e6], [200e6] * 4, "Capital Goods",
                     [{"date": "2026-02-20", "headline": "Appendix 4D and Half Year Report", "sensitive": True, "id": "1", "time": ""},
                      {"date": "2026-09-01", "headline": "Change of Director's Interest Notice", "sensitive": False, "id": "4", "time": ""},
                      {"date": "2026-09-02", "headline": "Change of Director's Interest Notice", "sensitive": False, "id": "5", "time": ""},
                      {"date": "2026-07-03", "headline": "Completion of Off-Market Takeover of Small Co", "sensitive": True, "id": "6", "time": ""}]),
    "BBB": asx_entry(300e6, 0.1, 400, 200, 280, 2.0, [30e6] * 4, [300e6] * 4, "Capital Goods",
                     [{"date": "2026-09-01", "headline": "Receipt of non-binding indicative proposal", "sensitive": True, "id": "2", "time": ""}]),
    "CCC": asx_entry(50e6, -0.01, 20, 2, 30, 0, [-2e6, -3e6, -1e6, -1e6], [0.1e6, 0, 0, 0], "Materials", []),
    "DDD": asx_entry(100e6, 0.1, 100, 50, 100, 0, [10e6] * 4, [100e6] * 4, "Consumer Services", []),
    "EEE": asx_entry(100e6, 0.1, 100, 0, 100, 5, [10e6] * 4, [10e6] * 4, "Financial Services", []),
    # loss (-1), heavy debt (-1), shorted (-1), small (1), 70% below high (1), raising (-1)
    "FFF": asx_entry(100e6, -0.05, 900, 850, 400, 0, [-5e6, 2e6, 3e6, 4e6], [500e6] * 4, "Retailing",
                     [{"date": "2026-08-01", "headline": "Placement and Share Purchase Plan", "sensitive": True, "id": "3", "time": ""}]),
}
N = {
    # 6.7 times earnings (2), 0.62 times NTA (2), 8% gross yield (1), small (1), 36% below high (1) = 7
    "GGG": {"fetched": "2026-11-01T00:00:00+00:00", "errors": [],
            "info": {"closePrice": "1.00", "earningsPerShare": "0.15", "ntaPerShare": "1.60", "capitalisation": 80e6,
                     "gdyPerShare": "8.0", "bestBid": "0.99", "bestOffer": "1.00", "suspensionStatus": "N", "category": "SHRS"}},
    "HHH": {"fetched": "2026-11-01T00:00:00+00:00", "errors": [],
            "info": {"closePrice": "1.00", "earningsPerShare": "0.10", "ntaPerShare": "1.0", "capitalisation": 60e6,
                     "gdyPerShare": "0", "bestBid": "0.90", "bestOffer": "1.00", "suspensionStatus": "N", "category": "SHRS"}},
}
A["III"] = asx_entry(100e6, 0.1, 100, 0, 0, 5, [10e6] * 4, [10e6] * 4, "Financial Services",
                     [{"date": f"2026-{m:02d}-10", "headline": "Net Tangible Asset Backing", "sensitive": False, "id": str(m), "time": ""}
                      for m in (6, 7, 8, 9, 10)])
json.dump(A, open(os.path.join(root, "data", "research_data", "asx_company.json"), "w"))
json.dump(N, open(os.path.join(root, "data", "research_data", "nzx_company.json"), "w"))
open(os.path.join(root, "data", "norgate", "index_changes.csv"), "w").write("index,symbol,name,date,change\n")
open(os.path.join(root, "config", "judgement_excluded.csv"), "w").write("# header\nticker,name,reason\n")
open(os.path.join(root, "research", "picks", "INDEX.md"), "w").write("| Ticker | Name | Date | Verdict | Status | Next |\n")

rr.main(root)
rank = {r["ticker"]: r for r in csv.DictReader(open(os.path.join(root, "reports", "research_rank.csv"), encoding="utf-8"))}
md = open(os.path.join(root, "reports", "research_rank.md"), encoding="utf-8").read()

check("a steady cheap company scores 10 points (director notices and the result date don't score)",
      rank.get("AAA", {}).get("points") == "10" and rank["AAA"]["director_notices"] == "2" and rank["AAA"]["next_result"] == "2027-02-20",
      rank.get("AAA"))
check("a completed takeover by the company is flagged, not routed", "deal headline to check" in rank.get("AAA", {}).get("flags", ""))
check("a company publishing monthly NTA is dropped as an investment company", "III" not in rank)
check("a company with a non-binding proposal is routed, not ranked", "BBB" not in rank and "ASX:BBB" in md.split("## Special situations")[1])
check("an explorer with no revenue is dropped on the rule", "CCC" not in rank and "no business to value yet" in md)
check("a gaming company waits for Cam's list", "DDD" not in rank and "gaming, wagering and racing hold" in md)
check("an investment company is dropped", "EEE" not in rank and "fund, trust or investment company" in md)
check("red flags take points off (loss, debt, shorting, raising)", rank.get("FFF", {}).get("points") == "-2", rank.get("FFF"))
check("an NZX company scores on earnings, net tangible assets, yield, size and fall", rank.get("GGG", {}).get("points") == "7", rank.get("GGG"))
check("an NZX spread read outside trading hours is shown, not used to drop", rank.get("HHH", {}).get("spread") == "0.111", rank.get("HHH"))
print("ALL PASS" if fails == 0 else f"{fails} FAILED")
sys.exit(1 if fails else 0)
