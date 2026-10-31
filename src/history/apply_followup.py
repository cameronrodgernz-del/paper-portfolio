"""Apply a follow-up research pass to the Australian deal files.

patches.csv (deal_id, field, old_value, new_value, source, note): a patch is applied only when
the field still holds old_value (or is blank), so nothing written since is overwritten. The
source is added to the row's sources.
new_rows.csv (the deal schema): each row goes into the file for its announcement year, unless
the same target already has a row announced within 60 days.
Every patch and row, applied or not, is logged in deals/au_hist/followup_log.csv.
Usage: python3 -I src/history/apply_followup.py <repo_root> <followup_dir> [<followup_dir> ...]
"""
import csv
import glob
import os
import sys
from datetime import date

PERIODS = {"2015": "2015_2016", "2016": "2015_2016", "2017": "2017_2018", "2018": "2017_2018", "2019": "2019_2020",
           "2020": "2019_2020", "2021": "2021_2022", "2022": "2021_2022", "2023": "2023_2024", "2024": "2023_2024"}


def load(path):
    with open(path, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def save(path, fields, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)


def main(root: str, *dirs: str) -> int:
    files = {p: load(p) for p in sorted(glob.glob(os.path.join(root, "deals", "au_hist", "*", "au_deals_*.csv")))}
    where = {r["deal_id"]: p for p, (_, rows) in files.items() for r in rows}
    log = []
    for d in dirs:
        pp = os.path.join(d, "patches.csv")
        if os.path.exists(pp):
            for p in load(pp)[1]:
                path = where.get(p["deal_id"])
                if not path:
                    log.append(dict(p, result="no such deal")); continue
                row = next(r for r in files[path][1] if r["deal_id"] == p["deal_id"])
                if p["field"] not in row:
                    log.append(dict(p, result="no such field")); continue
                cur = (row[p["field"]] or "").strip()
                if cur and cur != (p["old_value"] or "").strip():
                    log.append(dict(p, result=f"skipped: field now holds {cur!r}")); continue
                row[p["field"]] = p["new_value"]
                if p.get("source") and p["source"] not in (row.get("sources") or ""):
                    row["sources"] = ";".join(x for x in ((row.get("sources") or "").strip(";"), p["source"]) if x)
                log.append(dict(p, result="applied"))
        nr = os.path.join(d, "new_rows.csv")
        if os.path.exists(nr):
            for r in load(nr)[1]:
                y = (r.get("announce_date") or "")[:4] or (r.get("deal_id") or "")[3:7]   # undated rows go by their id's year
                folder = PERIODS.get(y)
                if not folder:
                    log.append({"deal_id": r.get("deal_id"), "field": "(new row)", "new_value": r.get("target_name"), "result": "year outside 2015-2024"}); continue
                path = os.path.join(root, "deals", "au_hist", folder, f"au_deals_{folder}.csv")
                fields, rows = files[path]
                dup = any(x["deal_id"] == r["deal_id"] for x in rows) or any(x["target_ticker"] == r["target_ticker"] and x["announce_date"] and r["announce_date"]
                          and abs((date.fromisoformat(x["announce_date"]) - date.fromisoformat(r["announce_date"])).days) <= 60
                          for x in rows)
                if dup:
                    log.append({"deal_id": r.get("deal_id"), "field": "(new row)", "new_value": r.get("target_name"), "result": "duplicate of an existing row"}); continue
                rows.append({k: r.get(k, "") for k in fields})
                log.append({"deal_id": r.get("deal_id"), "field": "(new row)", "new_value": r.get("target_name"), "result": f"added to {folder}"})
    for p, (fields, rows) in files.items():
        save(p, fields, sorted(rows, key=lambda r: (r["announce_date"] or "9999", r["deal_id"])))
    lp = os.path.join(root, "deals", "au_hist", "followup_log.csv")
    new = not os.path.exists(lp)
    with open(lp, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["deal_id", "field", "old_value", "new_value", "source", "note", "result"], extrasaction="ignore")
        if new:
            w.writeheader()
        w.writerows(log)
    from collections import Counter
    print(Counter(x["result"].split(":")[0] for x in log))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], *sys.argv[2:]))
