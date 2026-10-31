"""Fold the deal files (research/deals/<TICKER>.md, NZ_<TICKER>.md for NZX) into the live list.

Each deal file starts with a header of fields between --- lines (the format is in
research/deals/TEMPLATE.md). This copies the fields the engine uses into config/live_deals.csv:
- stage, meeting_date, court_date (the second court hearing), end_date and conditions_open;
- expected_payment, from the file's implementation_date when it has one;
- cash_per_share, scrip_ratio and acquirer_ticker when the file states them and the row has none.
It never removes a deal or changes the terms already on the row (a change of terms is a decision
for the desk, logged in research/desk_log.md). It reports what it changed and any file whose
ticker isn't on the live list, so the desk can add it.

With --add, a live deal file whose ticker isn't on the list is added: a new row on the live list
(the undisturbed price is the last close before the announcement, from data/prices) and a pending
row in the deal database part for its market, with the fields the file states.
Usage: python3 -I src/deal_files.py <repo_root> [--dry-run] [--add]
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


def last_close_before(root: str, market: str, ticker: str, d: str) -> str:
    p = os.path.join(root, "data", "prices", market, f"{ticker}.csv")
    if not os.path.exists(p) or not d:
        return ""
    last = ""
    for r in csv.DictReader(open(p, newline="")):
        if r["date"] >= d:
            break
        last = r.get("close") or last
    return last


def next_id(root: str, market: str, year: str, taken: set) -> str:
    pre = ("NZ" if market == "NZX" else "AU") + f"-{year}-"
    nums = [int(x[len(pre):]) for x in taken if x.startswith(pre) and x[len(pre):].isdigit()]
    return f"{pre}{(max(nums) + 1) if nums else 1:02d}"


def add_deal(root: str, rows: list[dict], fields: list[str], name: str, h: dict, dry: bool) -> str:
    mk = h.get("market") or ("NZX" if name.startswith("NZ_") else "ASX")
    tk = (h.get("ticker") or name[:-3].replace("NZ_", "")).upper()
    ann = iso(h.get("announce_date", ""))
    db_part = os.path.join(root, "deals", "nz" if mk == "NZX" else "au", "nz_deals.csv" if mk == "NZX" else "au_deals_2025_2026.csv")
    all_ids = {r["deal_id"] for r in csv.DictReader(open(os.path.join(root, "deals", "all_deals.csv"), encoding="utf-8"))} | {r["deal_id"] for r in rows}
    did = (h.get("deal_id") or "").strip()
    if not did or did in all_ids:
        did = next_id(root, mk, (ann or "2026")[:4], all_ids)
    cash, ratio = h.get("cash_per_share", ""), h.get("scrip_ratio", "") or "0"
    row = {k: "" for k in fields}
    row.update({"deal_id": did, "target_market": mk, "target_ticker": tk, "structure": h.get("structure", "scheme"),
                "cash_per_share": cash, "cash_ccy": h.get("currency", "NZD" if mk == "NZX" else "AUD"), "scrip_ratio": ratio,
                "acquirer_market": mk if h.get("acquirer_ticker") else "", "acquirer_ticker": (h.get("acquirer_ticker") or "").upper(),
                "undisturbed": last_close_before(root, mk, tk, ann), "announce_date": ann,
                "expected_payment": iso(h.get("implementation_date", "")) or iso(h.get("end_date", "")),
                "terms_note": terms_note(h.get("consideration") or ""), "stage": h.get("stage", "announced"),
                "deal_file": f"research/deals/{name}"})
    rows.append(row)
    if not dry:
        with open(db_part, encoding="utf-8", newline="") as f:
            rd = csv.DictReader(f); dbf = rd.fieldnames; db = list(rd)
        if not any(r["deal_id"] == did for r in db):
            new = {k: "" for k in dbf}
            new.update({"deal_id": did, "market": mk, "target_name": h.get("target", ""), "target_ticker": tk, "bidder_name": h.get("bidder", ""),
                        "structure": h.get("structure", "scheme"), "consideration_type": "cash" if (cash and ratio in ("", "0", "0.0")) else ("scrip" if not cash else "mixed"),
                        "currency": h.get("currency", ""), "announce_date": ann, "undisturbed_price": row["undisturbed"],
                        "undisturbed_basis": f"close before {ann} (data/prices)" if row["undisturbed"] else "",
                        "offer_price_initial": cash if ratio in ("", "0", "0.0") else "", "board_recommendation": "unanimous_for" if "unanimous" in (h.get("board") or "").lower() else "",
                        "intentions_pct": re.sub(r"[^\d.]", "", h.get("intentions_pct", "")) if h.get("intentions_pct") else "",
                        "meeting_date": iso(h.get("meeting_date", "")), "end_date": "", "outcome": "pending",
                        "notes": "added from the deal file " + name})
            new = {k: v for k, v in new.items() if k in dbf}
            db.append(new)
            with open(db_part, "w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=dbf); w.writeheader(); w.writerows(db)
    return f"added {mk}:{tk} as {did} (undisturbed {row['undisturbed'] or 'unknown'}); rerun src/history/deal_base_rates.py to rebuild deals/all_deals.csv"


def terms_note(c: str) -> str:
    first = re.split(r",|;|\.\s", c)[0].strip()
    extra = "; less dividends" if re.search(r"\bless\b.*dividend", c, re.I) else ""
    return (first + extra)[:160]


def iso(v: str) -> str:
    v = (v or "").strip()[:10]
    return v if re.match(r"\d{4}-\d\d-\d\d$", v) else ""


def main(root: str, dry: bool = False, add: bool = False) -> int:
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
    listed = {(r["target_market"], r["target_ticker"].upper()) for r in rows}
    for key, (name, h) in files.items():
        if key not in listed and (h.get("stage") or "") not in ("implemented", "terminated"):
            if add:
                changes.append(add_deal(root, rows, fields, name, h, dry))
            else:
                unmatched.append(f"{key[0]}:{key[1]} ({name}) has a deal file but isn't on the live list (run with --add to add it)")
    for r in rows:
        key = (r["target_market"], r["target_ticker"].upper())
        if key not in files:
            continue
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
    sys.exit(main(a[0] if a else ".", "--dry-run" in sys.argv, "--add" in sys.argv))
