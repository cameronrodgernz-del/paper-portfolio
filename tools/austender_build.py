"""Merges the extracts written by tools/austender_fetch.py into data/austender/contracts_YYYY.csv.gz,
one file per calendar year of publish date, and writes data/austender/README.md. Columns:
  cn_id, parent_cn_id, amendment, publish_date, start_date, end_date, value_aud, agency,
  supplier_name, supplier_abn, description, unspsc, procurement_method

  cn_id         the notice's own ID: CN1234 for a contract, CN1234-A2 for its second amendment
  parent_cn_id  for an amendment, the contract it changes (blank for a contract)
  amendment     0 for a contract, n for amendment An
  publish_date  the day the notice went up on AusTender, Canberra time (for an amendment, the day the
                amendment went up)
  value_aud     for a contract, its value as published (AUD incl. GST); for an amendment, the change in
                value it made (negative for a cut)

Rules
- De-duplicated on CN ID plus amendment number. The data.gov.au snapshots are read earliest first, then
  the API; the first source holding a notice is kept and later ones only fill blank fields.
- Amendment publish dates come from the files (to June 2020). API amendment releases carry the date of
  their latest change, and the move of older amendments onto the API stamped thousands with the same
  few timestamps, so an API amendment date is used only if it is on or after 2023-04-28 and is not a
  timestamp shared by 50 or more amendments. Amendments with no usable date go to contracts_undated.
- An amendment's value change is taken from the files where given, otherwise worked out as its total
  less the total before it (the contract, or amendment n-1), only when that previous total is known.
- A contract known only through its amendments (some older snapshots list a contract only as its latest
  amendment) is written as a contract row with a blank value.
Usage: python3 -I tools/austender_build.py EXTRACTS_DIR REPO_DIR
"""
import csv
import gzip
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

CANBERRA = ZoneInfo("Australia/Sydney")
CKAN = "https://data.gov.au/data/api/3/action/package_show?id=5c7fa69b-b0e9-4553-b8df-2a022dd2e982"
LANDING = "https://data.gov.au/data/dataset/5c7fa69b-b0e9-4553-b8df-2a022dd2e982"
API_DOC = "https://github.com/austender/austender-ocds-api"
API_URL = "https://api.tenders.gov.au/ocds/findByDates/contractPublished/{start}/{end}"
OUT_COLS = ["cn_id", "parent_cn_id", "amendment", "publish_date", "start_date", "end_date", "value_aud",
            "agency", "supplier_name", "supplier_abn", "description", "unspsc", "procurement_method"]
FILL = ["publish_date", "amend_date", "start_date", "end_date", "value_total", "value_change", "agency",
        "supplier_name", "supplier_abn", "description", "unspsc", "procurement_method", "parent_cn_id"]
KEEP = FILL + ["src", "seen_api"]
BULK_N, MIGRATION_END = 50, "2023-04-28"


def read_rows(path):
    with gzip.open(path, "rt", newline="", encoding="utf-8") as f:
        yield from csv.DictReader(f)


def write_rows(path, cols, rows):
    with gzip.open(path, "wt", newline="", encoding="utf-8", compresslevel=9) as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in rows:
            w.writerow([r.get(c, "") for c in cols])


def utc(s):
    try:
        return datetime.strptime(s[:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc).astimezone(CANBERRA)
    except (ValueError, TypeError):
        return None


def num(x):
    return f"{x:.2f}".rstrip("0").rstrip(".") if x != int(x) else str(int(x))


def fval(s):
    try:
        return float(s) if s not in ("", None) else None
    except ValueError:
        return None


def main(indir, repo):
    outdir = os.path.join(repo, "data", "austender")
    os.makedirs(outdir, exist_ok=True)
    merged = {}
    stats = Counter()
    examples = defaultdict(list)
    src_counts = Counter()

    def absorb(rec):
        key = (rec["cn_id"], rec["amendment"])
        old = merged.get(key)
        rec_api = rec["src"] == "api"
        if old is None:
            merged[key] = {k: rec.get(k, "") for k in KEEP}
            merged[key]["seen_api"] = rec_api
            return
        kind = "files vs API" if (rec_api or old["src"] == "api") else "file vs file"
        if key[1] == 0:
            a, b = old["publish_date"], rec["publish_date"]
            if a and b and a != b:
                stats[f"contract publish date differs, {kind} (earliest kept)"] += 1
                if len(examples[kind + " date"]) < 6:
                    examples[kind + " date"].append(f"{key[0]} {old['src']} {a} vs {rec['src']} {b}")
            va, vb = fval(old["value_total"]), fval(rec["value_total"])
            if va is not None and vb is not None and abs(va - vb) > max(1.0, 0.01 * abs(va)):
                stats[f"contract value differs by more than 1%, {kind} (earliest kept)"] += 1
                if len(examples[kind + " value"]) < 6:
                    examples[kind + " value"].append(f"{key[0]} {old['src']} {va:,.0f} vs {rec['src']} {vb:,.0f}")
        else:
            a, b = old["amend_date"], rec["amend_date"]
            if a and b and a != b:
                stats[f"amendment publish date differs, {kind} (earliest kept)"] += 1
        for k in FILL:
            if not old.get(k) and rec.get(k):
                old[k] = rec[k]
        old["seen_api"] = old["seen_api"] or rec_api

    # 1. data.gov.au files, earliest snapshot first
    flog = json.load(open(os.path.join(indir, "files_log.json"))) if os.path.exists(os.path.join(indir, "files_log.json")) else []
    for p in sorted(f for f in os.listdir(indir) if re.match(r"file_\d\d\.csv\.gz$", f)):
        n0 = len(merged)
        for rec in read_rows(os.path.join(indir, p)):
            rec["amendment"] = int(rec["amendment"])
            src_counts["data.gov.au files"] += 1
            absorb(rec)
        print(f"{p}: {len(merged) - n0} new notices, {len(merged)} in all", flush=True)
    in_files = set(merged)

    # 2. API
    api_paths = sorted(f for f in os.listdir(indir) if re.match(r"api_\d{4}\.csv\.gz$", f))
    stamp = Counter()
    for f in api_paths:
        for rec in read_rows(os.path.join(indir, f)):
            if rec["amendment"] != "0":
                stamp[rec["release_date"]] += 1
    bulk = {s for s, n in stamp.items() if n >= BULK_N}
    hours = Counter()
    api_years, api_failed, api_empty = {}, {}, {}
    for f in api_paths:
        y = int(f[4:8])
        lg = os.path.join(indir, f"api_{y}_log.json")
        if os.path.exists(lg):
            L = json.load(open(lg))
            api_years[y] = L["releases"]
            # the API answers HTTP 400 for a window with no notices (weekends, public holidays)
            api_failed[y] = [d for d in L["failed"] if not L["days"].get(d, {}).get("error", "").startswith("HTTP 400")]
            api_empty[y] = [d for d in L["failed"] if d not in api_failed[y]]
        seen_rel = set()
        n0 = len(merged)
        for rec in read_rows(os.path.join(indir, f)):
            if rec["release_id"] in seen_rel:
                stats["API release read twice (dropped)"] += 1
                continue
            seen_rel.add(rec["release_id"])
            rec["amendment"] = int(rec["amendment"])
            src_counts["API"] += 1
            if rec["amendment"]:
                rd = rec["release_date"]
                t = utc(rd)
                if t and rd not in bulk and rd[:10] >= MIGRATION_END:
                    rec["amend_date"] = t.date().isoformat()
                else:
                    rec["amend_date"] = ""
                    stats["API amendment releases whose date is a bulk or pre-migration stamp (date not used)"] += 1
            else:
                t = utc(rec["signed_utc"])
                if t:
                    b = "weekend" if t.weekday() >= 5 else ("before 10:00" if t.hour < 10 else
                                                            ("10:00 to 15:59" if t.hour < 16 else "16:00 or later"))
                    hours[b] += 1
            absorb(rec)
        print(f"{f}: {len(merged) - n0} new notices, {len(merged)} in all", flush=True)

    # 3. contracts known only through amendments
    parents_seen = {k[0] for k in merged if k[1] == 0}
    for key in list(merged):
        if key[1] > 0:
            rec = merged[key]
            pid = rec["parent_cn_id"] or key[0].split("-A")[0]
            if pid not in parents_seen:
                parents_seen.add(pid)
                merged[(pid, 0)] = {k: rec.get(k, "") for k in KEEP}
                merged[(pid, 0)].update(amend_date="", value_total="", value_change="", parent_cn_id="",
                                        start_date="", end_date="")
                stats["contract known only through an amendment (written with blank value)"] += 1

    # 4. value change of each amendment
    chains = defaultdict(list)
    for key, rec in merged.items():
        if key[1] > 0:
            chains[rec["parent_cn_id"] or key[0].split("-A")[0]].append(key)
    for parent, keys in chains.items():
        prev_n, prev = 0, fval(merged.get((parent, 0), {}).get("value_total"))
        for key in sorted(keys, key=lambda k: k[1]):
            rec = merged[key]
            n = key[1]
            tot, chg = fval(rec["value_total"]), fval(rec["value_change"])
            if chg is None:
                if tot is not None and prev is not None and n == prev_n + 1:
                    rec["value_change"] = num(tot - prev)
                    stats["amendment value change worked out from totals"] += 1
                else:
                    stats["amendment value change unknown (blank)"] += 1
            if tot is not None:
                prev_n, prev = n, tot
            elif prev is not None and chg is not None and n == prev_n + 1:
                prev_n, prev = n, prev + chg
            else:
                prev = None

    # 5. write
    by_year, undated = defaultdict(list), []
    for key, rec in merged.items():
        cid, n = key
        out = {c: rec.get(c, "") for c in OUT_COLS}
        out["cn_id"], out["amendment"] = cid, n
        if n:
            out["parent_cn_id"] = rec["parent_cn_id"] or cid.split("-A")[0]
            out["publish_date"] = rec["amend_date"]
            out["value_aud"] = rec["value_change"]
        else:
            out["parent_cn_id"] = ""
            out["value_aud"] = rec["value_total"]
        if out["publish_date"]:
            by_year[int(out["publish_date"][:4])].append(out)
        else:
            undated.append(out)
    for f in os.listdir(outdir):
        if re.match(r"contracts_(\d{4}|undated)\.csv\.gz$", f):
            os.remove(os.path.join(outdir, f))
    counts = {}
    for y, rows in sorted(by_year.items()):
        rows.sort(key=lambda r: (r["publish_date"], r["parent_cn_id"] or r["cn_id"], r["amendment"]))
        path = os.path.join(outdir, f"contracts_{y}.csv.gz")
        write_rows(path, OUT_COLS, rows)
        counts[y] = (sum(1 for r in rows if not r["amendment"]), sum(1 for r in rows if r["amendment"]),
                     os.path.getsize(path))
    undated.sort(key=lambda r: (r["parent_cn_id"] or r["cn_id"], r["amendment"]))
    write_rows(os.path.join(outdir, "contracts_undated.csv.gz"), OUT_COLS, undated)
    und_by = Counter()
    for r in undated:
        if r["amendment"]:
            pd = merged.get((r["parent_cn_id"], 0), {}).get("publish_date", "")
            und_by[pd[:4] or "unknown"] += 1
    und_contracts = sum(1 for r in undated if not r["amendment"])
    api_only = sum(1 for k in merged if k not in in_files and merged[k]["seen_api"])
    files_only = sum(1 for k, r in merged.items() if k in in_files and not r["seen_api"]
                     and r.get("publish_date", "") >= "2013-01-01")
    print(json.dumps({str(k): v for k, v in counts.items()}))
    print(json.dumps(dict(stats), indent=1))
    print("top amendment release stamps:", stamp.most_common(30))

    # README
    L = []
    w = L.append
    w("# AusTender contract notices\n")
    w("Every Australian Government contract notice that the two public AusTender sources hold, contracts and "
      "their amendments, one file per calendar year of publish date (`contracts_YYYY.csv.gz`). Downloaded by "
      "`tools/austender_fetch.py` and merged by `tools/austender_build.py`, both run by "
      "`.github/workflows/austender.yml`.\n")
    w("Matches of these notices to ASX-listed companies are in `matched.csv`, described in `MATCHING.md` and made by "
      "`tools/austender_match.py`, with the hand checks in `match_checks.csv`.\n")
    w("## Columns\n")
    w("| column | meaning |\n|---|---|")
    for c, m in [
        ("cn_id", "the notice's own ID: CN1234 for a contract, CN1234-A2 for its second amendment"),
        ("parent_cn_id", "for an amendment, the contract it changes; blank for a contract"),
        ("amendment", "0 for a contract, n for amendment An"),
        ("publish_date", "the day the notice went up on AusTender, Canberra time. For an amendment, the day the amendment went up"),
        ("start_date, end_date", "contract period as reported, Canberra dates"),
        ("value_aud", "contract: value as published, AUD including GST, for the life of the contract. Amendment: the change in value it made (negative for a cut, 0 for a change of dates or wording only, blank if unknown)"),
        ("agency", "the buying agency"),
        ("supplier_name, supplier_abn", "as entered by the agency; the ABN is kept only when it has 11 digits"),
        ("description", "the agency's short description, HTML removed"),
        ("unspsc", "the product or service code the agency chose"),
        ("procurement_method", "Open tender, Limited tender or Prequalified tender"),
    ]:
        w(f"| {c} | {m} |")
    w("\nDe-duplicated on CN ID plus amendment number. Where a notice is in several sources, the earliest "
      "snapshot is kept (closest to what was published) and later sources only fill blank fields.\n")
    w("## Sources\n")
    w(f"1. data.gov.au, Historical Australian Government Contract Notice Data: {LANDING} (file list from the "
      f"CKAN API: {CKAN}). Files read, earliest snapshot first:\n")
    w("| file | snapshot | notices read |\n|---|---|---|")
    for e in flog:
        if "error" in e:
            w(f"| {e['title']} ({e['file']}) | | not read: {e['error']} |")
        else:
            w(f"| [{e['title']}]({e['url']}) | {e['snapshot']} | {e['notices']:,} |")
    w("\n   Left out: the 2014-15 xlsx (the same rows as the 2014-15 csv), the GaPS contracts export (the system "
      "before AusTender, 1997 to 2007, which has no CN IDs) and the UNSPSC code list.\n")
    w(f"2. AusTender OCDS API, `{API_URL}`, paged one UTC day at a time from 1 January 2013 (the earliest it "
      f"serves) to the day of the run. Documentation: {API_DOC}. The API returns each contract with all of its "
      "amendments, in the window of the contract's publish date.\n")
    w("| API year (contract publish date) | releases read | UTC days with no notices | days that failed after three tries |\n|---|---|---|---|")
    for y in sorted(api_years):
        fl = api_failed.get(y, [])
        em = api_empty.get(y, [])
        wk = Counter(datetime.strptime(d, "%Y-%m-%d").strftime("%a") for d in em)
        w(f"| {y} | {api_years[y]:,} | {len(em)} ({', '.join(f'{k} {v}' for k, v in wk.most_common(3))}) | "
          f"{len(fl) if fl else 'none'}{(' (' + ', '.join(fl[:8]) + ')') if fl else ''} |")
    empty_days = {d for v in api_empty.values() for d in v}
    on_empty = sum(1 for k, r in merged.items() if k[1] == 0 and r["src"] != "api" and r["publish_date"] in empty_days)
    w("\nThe API answers HTTP 400 for a window with no notices. Those days are almost all UTC Saturdays (Saturday "
      "morning to Sunday morning in Canberra) and public holidays, so they are counted as empty rather than failed. "
      f"As a check, the data.gov.au files hold {on_empty:,} contracts with a Canberra publish date on any of those "
      f"{len(empty_days):,} dates.")
    w("\nRows read: " + ", ".join(f"{k} {v:,}" for k, v in sorted(src_counts.items())) + ".\n")
    w("## Row counts by year of publish date\n")
    w("| year | contracts | amendments | file size |\n|---|---|---|---|")
    for y, (p, a, size) in sorted(counts.items()):
        w(f"| {y} | {p:,} | {a:,} | {size / 1e6:.1f} MB |")
    w(f"| total | {sum(v[0] for v in counts.values()):,} | {sum(v[1] for v in counts.values()):,} | |")
    w(f"| undated (`contracts_undated.csv.gz`) | {und_contracts:,} | {len(undated) - und_contracts:,} | |\n")
    if counts:
        w(f"Range: {min(counts)} to {max(counts)}. Years before 2007 hold only the notices carried over from the "
          "old Gazette system when AusTender began, so they are thin. The current year runs to the day of the run.\n")
    w("## Gaps and weaknesses\n")
    top = sorted(bulk, key=lambda s: -stamp[s])[:4]
    w("- Amendment dates after June 2020. The data.gov.au files give each amendment's publish date up to 30 June "
      "2020; the API does not. Each API amendment release carries the date of its latest change, and the move of "
      "older amendments onto the API stamped thousands with the same timestamp ("
      + "; ".join(f"{s} on {stamp[s]:,}" for s in top) + "). API amendment dates are used only when on or after "
      f"{MIGRATION_END} and not a timestamp shared by {BULK_N} or more amendments. Amendments with no usable date "
      "are kept in `contracts_undated.csv.gz`; by year of their contract's publish date: "
      + ", ".join(f"{k} {v:,}" for k, v in sorted(und_by.items())) + ". Most will have been published between "
      "July 2020 and April 2023. After April 2023 an API amendment date can still be the date of a later "
      "correction rather than first publication.")
    am_files = [counts[y][1] for y in range(2010, 2020) if y in counts]
    am_api = {y: counts[y][1] for y in range(2023, 2100) if y in counts}
    if am_files and am_api:
        w(f"- Amendment counts. The files give about {sum(am_files) // len(am_files):,} dated amendments a year for "
          "2010 to 2019. The API-dated years carry " + ", ".join(f"{y}: {n:,}" for y, n in am_api.items()) +
          ". The API also lists amendments that change only dates or wording, and some API dates will be the date "
          "of a later edit, so amendment dates from 2023 on are less reliable than contract dates.")
    w("- Amendments made after June 2020 to contracts published before 2013 are missing: the API only serves "
      "contracts published from 2013 and returns amendments with their contract.")
    w(f"- Notices only in the API: {api_only:,} (mostly those published after the files end). Notices from 2013 on "
      f"that are in the files but not returned by the API: {files_only:,}. They are kept.")
    for k, v in sorted(stats.items()):
        w(f"- {k}: {v:,}")
    for k, ex in sorted(examples.items()):
        w(f"  - examples ({k}): " + "; ".join(ex))
    if hours:
        tot = sum(hours.values())
        w("- Time of day. The files give dates only; the API gives a publish time. For contracts read from the "
          "API (2013 on), Canberra publish time was: "
          + ", ".join(f"{k} {100 * v / tot:.0f}%" for k, v in sorted(hours.items()))
          + ". A notice put up during the day is public while the ASX is open, so the publish day itself is "
          "partly after the event.")
    w("- Agency names. The files carry the agency's name at the time of the notice; notices found only in the API "
      "carry the agency's current name after later machinery-of-government changes (for example Department of Home "
      "Affairs on a 2014 notice).")
    w("- Values are as agencies reported them. Panel and standing-offer notices can carry a ceiling rather than "
      "expected spend, and a few notices carry keying errors (for example values in the billions for small "
      "purchases).")
    w("")
    with open(os.path.join(outdir, "README.md"), "w") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
