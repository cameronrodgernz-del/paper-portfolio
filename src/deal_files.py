"""Fold the deal files (research/deals/<TICKER>.md, NZ_<TICKER>.md for NZX) into the live list.

Each deal file starts with a header of fields between --- lines (the format is in
research/deals/TEMPLATE.md). This copies the fields the engine uses into config/live_deals.csv:
- stage, meeting_date, court_date (the second court hearing), end_date and conditions_open;
- expected_payment, from the file's implementation_date when it has one;
- cash_per_share, scrip_ratio and acquirer_ticker when the file states them and the row has none.
It never removes a deal or changes the terms already on the row (a change of terms is a decision
for the desk, logged in research/desk_log.md). It reports what it changed and any file whose
ticker isn't on the live list, so the desk can add it.
Usage: python3 -I src/deal_files.py <repo_root> [--dry-run]
"""
import csv
import os
import re
import sys

FIELDS_ADDED = ["stage", "meeting_date", "court_date", "end_date", "conditions_open", "deal_file", "file_checked"]
STAGES = {"announced", "booklet_out", "vote_passed", "court_approved", "unconditional", "implemented", "terminated"}


def header(path: str) -> dict:
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    out = {}
    if not m:
        return out
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "#")):
            k, v = line.split(":", 1)
            v = re.sub(r"\s+#.*$", "", v).strip()
            if v:
                out[k.strip()] = v
    return out


def iso(v: str) -> str:
    v = (v or "").strip()[:10]
    return v if re.match(r"\d{4}-\d\d-\d\d$", v) else ""


def main(root: str, dry: bool = False) -> int:
    path = os.path.join(root, "config", "live_deals.csv")
    with open(path, encoding="utf-8", newline="") as f:
        rd = csv.DictReader(f)
        fields = list(rd.fieldnames)
        rows = list(rd)
    for k in FIELDS_ADDED:
        if k not in fields:
            fields.append(k)
    files = {}
    ddir = os.path.join(root, "research", "deals")
    for name in sorted(os.listdir(ddir)) if os.path.isdir(ddir) else []:
        if name.endswith(".md") and name != "TEMPLATE.md":
            h = header(os.path.join(ddir, name))
            tk = (h.get("ticker") or name[:-3].replace("NZ_", "")).upper()
            mk = h.get("market") or ("NZX" if name.startswith("NZ_") else "ASX")
            files[(mk, tk)] = (name, h)
    changes, unmatched = [], []
    seen = set()
    for r in rows:
        key = (r["target_market"], r["target_ticker"].upper())
        if key not in files:
            continue
        seen.add(key)
        name, h = files[key]
        new = {"deal_file": f"research/deals/{name}", "file_checked": iso(h.get("last_checked", ""))}
        st = (h.get("stage") or "").strip()
        if st in STAGES:
            new["stage"] = st
        new["meeting_date"] = iso(h.get("meeting_date", ""))
        new["court_date"] = iso(h.get("second_court_date", ""))
        new["end_date"] = iso(h.get("end_date", ""))
        new["conditions_open"] = (h.get("conditions_open") or "").replace(",", ";")[:400]
        if iso(h.get("implementation_date", "")):
            new["expected_payment"] = iso(h["implementation_date"])
        if not r.get("acquirer_ticker") and h.get("acquirer_ticker"):
            new["acquirer_ticker"] = h["acquirer_ticker"].upper()
        for k, v in new.items():
            if v and (r.get(k) or "") != v:
                changes.append(f"{r['target_ticker']}: {k} {r.get(k) or '(blank)'} -> {v}")
                r[k] = v
    for key, (name, h) in files.items():
        if key not in seen and (h.get("stage") or "") not in ("implemented", "terminated"):
            unmatched.append(f"{key[0]}:{key[1]} ({name}) has a deal file but isn't on the live list")
    if not dry:
        with open(path, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader(); w.writerows(rows)
    print("\n".join(changes) or "no changes")
    if unmatched:
        print("\n".join(unmatched))
    return 0


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    sys.exit(main(a[0] if a else ".", "--dry-run" in sys.argv))
