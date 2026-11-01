"""One-off: does FinancialFilings hold the substantial holder notices of our ASX deal targets?

For each ASX deal announced 2015 to 2025 in deals/all_deals.csv, one request (1 free credit): the
substantial holder notices (type MRQ) whose company name matches the target, released in the 12 months
before the announcement. A target with none is either missing from FinancialFilings or named differently.
Stops if the free credits left would not cover the run. Writes data/financialfilings/deal_coverage.csv
and data/financialfilings/deal_coverage.md. Usage: python3 -I tools/ff_deal_coverage.py <repo_root>
"""
import csv
import os
import re
import sys
from datetime import date, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ff_probe as P  # noqa: E402

P.MAX_CALLS = 300
DROP = r"\b(limited|ltd|group|holdings?|corporation|corp|trust|reit|fund|plc|inc|nl|the|australia|australian|stapled|securities|property)\b"


def core(name: str) -> str:
    n = re.sub(r"\(.*?\)", " ", name or "")
    n = re.sub(DROP, " ", n, flags=re.I)
    n = re.sub(r"[^A-Za-z0-9&' -]", " ", n)
    words = n.split()
    return " ".join(words[:3])


def main(root: str) -> int:
    out = os.path.join(root, "data", "financialfilings")
    rows = [r for r in csv.DictReader(open(os.path.join(root, "deals", "all_deals.csv"), encoding="utf-8"))
            if r["market"] == "ASX" and "2015" <= (r.get("announce_date") or "")[:4] <= "2025"]
    st, u = P.get("/usage/")
    left = (u.get("free_credits") or {}).get("remaining") if isinstance(u, dict) else None
    if left is None or left < len(rows) + 10:
        print(f"free credits left {left}, need {len(rows) + 10}; stopping"); return 1
    res = []
    for r in rows:
        ann = date.fromisoformat(r["announce_date"][:10])
        q = core(r["target_name"])
        st, b = P.get("/filings/", {"search": q, "countries": "AU", "types": "MRQ", "page_size": 5,
                                    "release_datetime_from": f"{ann - timedelta(days=365)}T00:00:00Z",
                                    "release_datetime_to": f"{ann - timedelta(days=1)}T23:59:59Z"})
        names = sorted({(x.get("company") or {}).get("name", "") for x in P.items(b) if isinstance(x, dict)})
        res.append({"deal_id": r["deal_id"], "target": r["target_name"], "ticker": r["target_ticker"], "announce": str(ann),
                    "outcome": r.get("outcome", ""), "searched": q, "status": st, "notices_12m_before": P.count_of(b),
                    "companies_matched": "; ".join(names)[:200]})
    with open(os.path.join(out, "deal_coverage.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(res[0].keys())); w.writeheader(); w.writerows(res)
    ok = [x for x in res if x["status"] == 200]
    found = [x for x in ok if (x["notices_12m_before"] or 0) > 0]
    L = ["# FinancialFilings coverage of ASX deal targets, 2015 to 2025", "",
         f"{len(found)} of {len(ok)} targets have substantial holder notices in the 12 months before their deal "
         f"({len(res) - len(ok)} requests failed).", "", "| Year announced | Deals | With notices | Median notices |", "| --- | --- | --- | --- |"]
    for y in sorted({x["announce"][:4] for x in ok}):
        ys = [x for x in ok if x["announce"][:4] == y]
        ns = sorted(x["notices_12m_before"] or 0 for x in ys)
        L.append(f"| {y} | {len(ys)} | {sum(1 for x in ys if (x['notices_12m_before'] or 0) > 0)} | {ns[len(ns) // 2]} |")
    L += ["", "Targets with none (missing, or named differently):", ""] + \
         [f"- {x['announce']} {x['ticker']} {x['target']} (searched '{x['searched']}')" for x in ok if not (x["notices_12m_before"] or 0)]
    st, u = P.get("/usage/")
    L += ["", f"Requests made: {P.calls}. Free credits left: {(u.get('free_credits') or {}).get('remaining') if isinstance(u, dict) else '?'}."]
    open(os.path.join(out, "deal_coverage.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    if not os.environ.get("FINANCIALFILINGS_API_KEY"):
        sys.exit("FINANCIALFILINGS_API_KEY is not set")
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
