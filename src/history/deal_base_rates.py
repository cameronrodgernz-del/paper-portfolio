"""Merge the deal database parts and work out base rates.

Parts: deals/nz/nz_deals.csv, deals/au/au_deals_2025_2026.csv, deals/au_hist/*/au_deals_*.csv.
Writes deals/all_deals.csv (with derived columns) and reports/deal_base_rates.md.
Majority-holder buy-outs (NZ rows flagged 'scope' in the verification log) are kept in the
file but left out of the base rates, matching the Australian rule.
Usage: python3 -I src/history/deal_base_rates.py <repo_root>
"""
import csv
import glob
import os
import statistics as stats
import sys
from collections import Counter, defaultdict

KEY_FIELDS = ("undisturbed_price", "offer_price_initial", "equity_value_m", "announce_date", "outcome_date", "outcome")
RESOLVED = {"completed", "terminated", "withdrawn", "lapsed", "superseded_by_rival"}


def load(root: str) -> list[dict]:
    parts = [os.path.join(root, "deals", "nz", "nz_deals.csv"), os.path.join(root, "deals", "au", "au_deals_2025_2026.csv")]
    parts += sorted(glob.glob(os.path.join(root, "deals", "au_hist", "*", "au_deals_*.csv")))
    rows = []
    for p in parts:
        with open(p, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                r["part"] = os.path.relpath(p, root)
                rows.append(r)
    flagged = set()
    log = os.path.join(root, "deals", "nz", "nz_deals_verification_log.csv")
    if os.path.exists(log):
        with open(log, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                if r["field"] == "scope" and "already" in (r.get("note") or "").lower():
                    flagged.add(r["deal_id"])
    for r in rows:
        r["majority_buyout"] = "Y" if r["deal_id"] in flagged else "N"
        r["filled_key_fields"] = str(sum(1 for k in KEY_FIELDS if (r.get(k) or "").strip()))
        try:
            r["days_to_outcome"] = r["days_to_outcome"] or ""
            int(float(r["days_to_outcome"]))
        except ValueError:
            r["days_to_outcome"] = ""
    return rows


def pct(n, d):
    return f"{n / d:.0%}" if d else "n/a"


def main(root: str) -> int:
    rows = load(root)
    fields = list(rows[0].keys())
    for r in rows[1:]:
        for k in r:
            if k not in fields:
                fields.append(k)
    with open(os.path.join(root, "deals", "all_deals.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader(); w.writerows(sorted(rows, key=lambda r: (r["market"], r["announce_date"] or "9999")))
    base = [r for r in rows if r["majority_buyout"] == "N"]
    res = [r for r in base if r["outcome"] in RESOLVED]
    done = [r for r in res if r["outcome"] == "completed"]
    days = [int(float(r["days_to_outcome"])) for r in res if r["days_to_outcome"]]
    days_done = [int(float(r["days_to_outcome"])) for r in done if r["days_to_outcome"]]

    flat = []      # the same tables as rows, for reports/deal_base_rates.csv

    def table(key, label):
        g = defaultdict(list)
        for r in res:
            g[(r.get(key) or "unknown").strip() or "unknown"].append(r)
        out = [f"| {label} | Resolved | Completed | Completion | Median days |", "| --- | --- | --- | --- | --- |"]
        for k, v in sorted(g.items(), key=lambda kv: -len(kv[1])):
            dd = [int(float(r["days_to_outcome"])) for r in v if r["days_to_outcome"]]
            c = sum(1 for r in v if r["outcome"] == "completed")
            flat.append({"group": label, "value": k, "resolved": len(v), "completed": c, "completion": round(c / len(v), 4),
                         "median_days": int(stats.median(dd)) if dd else ""})
            out.append(f"| {k} | {len(v)} | {sum(1 for r in v if r['outcome'] == 'completed')} | "
                       f"{pct(sum(1 for r in v if r['outcome'] == 'completed'), len(v))} | {int(stats.median(dd)) if dd else ''} |")
        return out

    years = Counter(r["announce_date"][:4] for r in base if r["announce_date"])
    fails = Counter((r.get("failure_reason") or "not recorded").split(" ")[0].strip(";,") or "not recorded"
                    for r in res if r["outcome"] != "completed")
    thin = sum(1 for r in base if int(r["filled_key_fields"]) < 5)
    q = sorted(days)
    lines = [
        "# Deal database: base rates", "",
        f"{len(rows)} rows in all ({sum(1 for r in rows if r['market'] == 'NZX')} NZX, {sum(1 for r in rows if r['market'] == 'ASX')} ASX); "
        f"{len(rows) - len(base)} majority-holder buy-outs left out of the rates. "
        f"{len(res)} resolved deals and {sum(1 for r in base if r['outcome'] == 'pending')} pending.", "",
        "The Australian 2015 to 2024 rows are incomplete: the research hit shared web limits, so some deals are missing "
        f"and {thin} rows have fewer than five of the six key fields. Treat the rates as provisional until the follow-up pass.", "",
        "## Headline rates", "",
        "| Measure | Value |", "| --- | --- |",
        f"| Completed, of resolved deals | {pct(len(done), len(res))} ({len(done)} of {len(res)}) |",
        f"| Median days, announcement to outcome | {int(stats.median(days)) if days else ''} (middle half {q[len(q) // 4] if q else ''} to {q[3 * len(q) // 4] if q else ''}) |",
        f"| Median days, completed deals | {int(stats.median(days_done)) if days_done else ''} |",
        f"| Deals with a rival bid | {pct(sum(1 for r in res if r.get('rival_bid') == 'Y'), len(res))} |",
        f"| Deals where the price was raised | {pct(sum(1 for r in res if r.get('price_raised') == 'Y'), len(res))} |", "",
        "## By market", "", *table("market", "Market"), "",
        "## By structure", "", *table("structure", "Structure"), "",
        "## By bidder type", "", *table("bidder_type", "Bidder"), "",
        "## By consideration", "", *table("consideration_type", "Paid in"), "",
        "## Why deals failed", "", "| Reason | Deals |", "| --- | --- |",
        *[f"| {k} | {v} |" for k, v in fails.most_common()], "",
        "## Rows by announcement year", "", "| Year | Rows |", "| --- | --- |",
        *[f"| {y} | {n} |" for y, n in sorted(years.items())], "",
    ]
    os.makedirs(os.path.join(root, "reports"), exist_ok=True)
    open(os.path.join(root, "reports", "deal_base_rates.md"), "w").write("\n".join(lines) + "\n")
    flat.insert(0, {"group": "All", "value": "all", "resolved": len(res), "completed": len(done),
                    "completion": round(len(done) / len(res), 4) if res else "", "median_days": int(stats.median(days)) if days else ""})
    with open(os.path.join(root, "reports", "deal_base_rates.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["group", "value", "resolved", "completed", "completion", "median_days"])
        w.writeheader(); w.writerows(flat)
    print("\n".join(lines[:22]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
