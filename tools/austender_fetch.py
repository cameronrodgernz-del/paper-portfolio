"""Downloads every Australian Government contract notice (AusTender) from its two public sources and
saves each as a normalised extract for tools/austender_build.py, which merges them into
data/austender/contracts_YYYY.csv.gz.

  1. data.gov.au "Historical Australian Government Contract Notice Data": yearly files to 2019-20 and
     cumulative "CNs published up to" files (back to the first AusTender notices). One extract per file.
  2. The AusTender OCDS API (api.tenders.gov.au), paged one UTC day at a time on contract publish date,
     from 1 January 2013 (the earliest it serves) to today. One extract per year. The API returns each
     contract together with all of its amendment releases, in the window of the contract's publish date.

Extract columns: src, snap (snapshot order), cn_id, parent_cn_id, amendment (0 or n), publish_date
(the contract's, Canberra date), amend_date (the amendment's, Canberra date, files only), start_date,
end_date, value_total (contract value, or the total after an amendment), value_change (an amendment's
change, where the file gives it), agency, supplier_name, supplier_abn, description, unspsc,
procurement_method, release_date and release_id (API only, UTC) and signed_utc (API publish time).

Usage (the workflow runs these as parallel jobs):
  python3 -I tools/austender_fetch.py api YEAR OUTDIR     one year of API pages
  python3 -I tools/austender_fetch.py files OUTDIR        every data.gov.au file
"""
import csv
import gzip
import html
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
import zipfile
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

UA = "paper-portfolio research (github.com/cameronrodgernz-del/paper-portfolio)"
CKAN = "https://data.gov.au/data/api/3/action/package_show?id=5c7fa69b-b0e9-4553-b8df-2a022dd2e982"
API = "https://api.tenders.gov.au/ocds/findByDates/contractPublished/{a}/{b}"
API_START = date(2013, 1, 1)
CANBERRA = ZoneInfo("Australia/Sydney")
# internal record, shared by both sources
REC_COLS = ["src", "snap", "cn_id", "parent_cn_id", "amendment", "publish_date", "amend_date", "start_date",
            "end_date", "value_total", "value_change", "agency", "supplier_name", "supplier_abn", "description",
            "unspsc", "procurement_method", "release_date", "release_id"]

# data.gov.au resources in the order their snapshot was taken (earliest first); the build keeps the
# earliest snapshot of each notice as closest to what was published.
# (The 2014-15 xlsx repeats the 2014-15 csv and the GaPS export is the pre-AusTender system with no CN
# IDs, so both are left out.)
FILES = [
    ("2014-2015 Commonwealth Government Contract Data", "20142015fy.csv", "2015-10-25"),
    ("AusTender CNs published up to 31 December 2015", "austenderallcnsupto31dec15.zip", "2016-01-01"),
    ("2015-2016 Commonwealth Government Contract Data", "20152016-fy-austender-cns.zip", "2016-09-02"),
    ("AusTender CNs published up to 19 September 2016", "austenderallcnsupto19sep16.zip", "2016-09-20"),
    ("2016 Calendar Year Commonwealth Government Contract Data", "2016calyearbypublishdate.csv", "2017-03-03"),
    ("AusTender CNs published up to 30 June 2017", "austenderallcnsupto30jun17.zip", "2017-07-06"),
    ("2016-2017 Australian Government Contract Data", "2016-2017-australian-government-contract-data.csv", "2017-09-11"),
    ("2016-17 CNs published up to 11 September 2017", "2016-2017-austender-cns-published-to-11-sept-2017.csv", "2017-09-14"),
    ("AusTender CNs published up to 3 January 2018", "austenderallcnupto03jan18.zip", "2018-01-04"),
    ("AusTender CNs published up to 28 August 2018", "cns-parent-and-amendments-28082018.zip", "2018-08-28"),
    ("2017-18 Australian Government Contract Data", "17-18-fy-dataset.csv", "2019-01-25"),
    ("2018-19 Australian Government Contract Data", "cn-parent-and-amendments-2018-19-30082019.xlsx", "2019-08-30"),
    ("AusTender CNs published up to 30 August 2019", "cn-parent-and-amendments-30092019-ltr.xlsx", "2019-08-31"),
    ("2019-20 Australian Government Contract Data", "2019-20-australian-government-contract-data.xlsx", "2021-01-31"),
]
API_SNAP = 99


# ---------------------------------------------------------------------------------------- helpers
def get(url, tries=6, timeout=180):
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json, */*"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}"
            if e.code in (400, 404):
                break
        except Exception as e:  # network trouble: wait and try again
            last = type(e).__name__
        time.sleep(min(60, 2 * 2 ** attempt))
    raise RuntimeError(f"{last} for {url}")


def decode(raw):
    if raw[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return raw.decode("utf-16")
    for enc in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue


NULLS = {"", "null", "none", "nan", "n/a", "na", "-"}


def blank(v):
    return v is None or (isinstance(v, str) and v.strip().lower() in NULLS)


def text(v):
    if blank(v):
        return ""
    s = str(v)
    s = re.sub(r"<[^>]*>", " ", s)
    s = html.unescape(s).replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip()


def num(v):
    if blank(v):
        return ""
    if isinstance(v, (int, float)):
        x = float(v)
    else:
        s = str(v).strip().replace(",", "").replace("$", "")
        try:
            x = float(s)
        except ValueError:
            return ""
    return f"{x:.2f}".rstrip("0").rstrip(".") if x != int(x) else str(int(x))


def code(v):
    """UNSPSC or similar integer code that may arrive as a float."""
    if blank(v):
        return ""
    if isinstance(v, float):
        return str(int(v))
    s = str(v).strip()
    return s[:-2] if s.endswith(".0") else s


def abn(v):
    if blank(v):
        return ""
    if isinstance(v, float):
        v = int(v)
    d = re.sub(r"\D", "", str(v).split(".")[0])
    return d if len(d) == 11 and d != "0" * 11 else ""


MONTHS = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


def day(v):
    """Local (Canberra) calendar date as YYYY-MM-DD from the many formats the files use."""
    if blank(v):
        return ""
    if isinstance(v, datetime):
        return v.date().isoformat()
    if isinstance(v, date):
        return v.isoformat()
    if isinstance(v, (int, float)):  # an Excel serial number
        try:
            return (date(1899, 12, 30) + timedelta(days=int(v))).isoformat()
        except (OverflowError, ValueError):
            return ""
    s = str(v).strip()
    m = re.match(r"^(\d{4})-(\d{1,2})-(\d{1,2})", s)
    if m:
        y, mo, d = map(int, m.groups())
    else:
        m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{2,4})", s)
        if m:
            d, mo, y = map(int, m.groups())
        else:
            m = re.match(r"^(\d{1,2})-([A-Za-z]{3})-(\d{2,4})", s)
            if not m:
                return ""
            d, mo, y = int(m.group(1)), MONTHS.get(m.group(2).lower(), 0), int(m.group(3))
        if y < 100:
            y += 2000 if y < 50 else 1900
    try:
        return date(y, mo, d).isoformat()
    except ValueError:
        return ""


def utc_to_local_day(s):
    if blank(s):
        return ""
    try:
        t = datetime.strptime(s[:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
    except ValueError:
        return ""
    return t.astimezone(CANBERRA).date().isoformat()


def split_id(raw_id, parent_hint=""):
    cid = str(raw_id or "").strip().upper().replace(" ", "")
    m = re.match(r"^(CN\d+)-A(\d+)$", cid)
    if m:
        return cid, m.group(1), int(m.group(2))
    if re.match(r"^CN\d+$", cid):
        return cid, "", 0
    p = str(parent_hint or "").strip().upper()
    return cid, ("" if blank(p) else p), (-1 if "-" in cid else 0)


def write_rows(path, cols, rows):
    with gzip.open(path, "wt", newline="", encoding="utf-8", compresslevel=9) as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in rows:
            w.writerow([r.get(c, "") for c in cols] if isinstance(r, dict) else r)


def read_rows(path):
    with gzip.open(path, "rt", newline="", encoding="utf-8") as f:
        yield from csv.DictReader(f)


# --------------------------------------------------------------------------------------------- API
def api_record(rel):
    c = (rel.get("contracts") or [{}])[0]
    tag = (rel.get("tag") or [""])[0]
    am = [a for a in (c.get("amendments") or []) if a.get("id")]
    mine = [a for a in am if a.get("releaseID") == rel.get("id")] or am[-1:]
    if tag == "contractAmendment" and mine:
        cid, parent, n = split_id(mine[0]["id"])
    else:
        cid, parent, n = split_id(c.get("id"))
    supplier, agency = {}, {}
    for p in rel.get("parties") or []:
        roles = p.get("roles") or []
        if "supplier" in roles and not supplier:
            supplier = p
        if "procuringEntity" in roles and not agency:
            agency = p
    sabn = ""
    for ident in supplier.get("additionalIdentifiers") or []:
        if ident.get("scheme") == "AU-ABN":
            sabn = abn(ident.get("id"))
    items = c.get("items") or [{}]
    unspsc = ((items[0] or {}).get("classification") or {}).get("id", "")
    period = c.get("period") or {}
    tender = rel.get("tender") or {}
    return {
        "src": "api", "snap": API_SNAP, "cn_id": cid, "parent_cn_id": parent, "amendment": n,
        "publish_date": utc_to_local_day(c.get("dateSigned", "")),
        "amend_date": "",  # decided in build, once bulk-stamped release dates are known
        "start_date": utc_to_local_day(period.get("startDate", "")),
        "end_date": utc_to_local_day(period.get("endDate", "")),
        "value_total": num((c.get("value") or {}).get("amount")), "value_change": "",
        "agency": text(agency.get("name")), "supplier_name": text(supplier.get("name")),
        "supplier_abn": sabn, "description": text(c.get("description")), "unspsc": code(unspsc),
        "procurement_method": text(tender.get("procurementMethodDetails") or tender.get("procurementMethod")),
        "release_date": rel.get("date", ""), "release_id": rel.get("id", ""),
        "signed_utc": c.get("dateSigned", ""),
    }


def fetch_day(d):
    a = f"{d.isoformat()}T00:00:00Z"
    b = f"{(d + timedelta(days=1)).isoformat()}T00:00:00Z"
    url = API.format(a=a, b=b)
    out, pages, seen = [], 0, set()
    while url:
        body = json.loads(get(url))
        pages += 1
        rels = body.get("releases") or []
        for r in rels:
            if r.get("id") in seen:
                continue
            seen.add(r.get("id"))
            out.append(api_record(r))
        nxt = (body.get("links") or {}).get("next")
        if not rels or not nxt or nxt == url:
            break
        url = nxt
        time.sleep(0.25)
    return out, pages


def cmd_api(year, outdir):
    os.makedirs(outdir, exist_ok=True)
    first = max(date(year, 1, 1), API_START)
    last = min(date(year, 12, 31), datetime.now(timezone.utc).date())
    days = [first + timedelta(days=i) for i in range((last - first).days + 1)]
    rows, log, failed = [], {}, []
    t0 = time.time()
    for rnd in range(3):  # first pass, then two passes over any day that failed
        todo = days if rnd == 0 else failed
        failed = []
        for d in todo:
            try:
                recs, pages = fetch_day(d)
            except Exception as e:
                failed.append(d)
                log[d.isoformat()] = {"error": str(e)[:200]}
                continue
            rows += recs
            log[d.isoformat()] = {"pages": pages, "releases": len(recs)}
            if d.day == 1 and rnd == 0:
                print(f"{d} done, {len(rows)} releases so far, {time.time() - t0:.0f}s", flush=True)
        if not failed:
            break
        time.sleep(60)
    cols = REC_COLS + ["signed_utc"]
    write_rows(os.path.join(outdir, f"api_{year}.csv.gz"), cols, rows)
    with open(os.path.join(outdir, f"api_{year}_log.json"), "w") as f:
        json.dump({"year": year, "days": log, "failed": [d.isoformat() for d in failed],
                   "releases": len(rows), "seconds": round(time.time() - t0)}, f)
    print(f"{year}: {len(rows)} releases, {len(failed)} failed days, {time.time() - t0:.0f}s")


# ------------------------------------------------------------------------------------------ files
def table_rows(name, raw):
    """Yield (part name, list of rows) for a csv, a zip of csvs, or an xlsx."""
    if name.endswith(".xlsx"):
        from python_calamine import CalamineWorkbook
        wb = CalamineWorkbook.from_filelike(io.BytesIO(raw))
        for sheet in wb.sheet_names:
            yield sheet, wb.get_sheet_by_name(sheet).to_python(skip_empty_area=False)
    elif raw[:2] == b"PK":
        z = zipfile.ZipFile(io.BytesIO(raw))
        for m in z.infolist():
            if m.filename.lower().endswith(".csv"):
                yield m.filename, list(csv.reader(io.StringIO(decode(z.read(m)))))
            elif m.filename.lower().endswith(".xlsx"):
                yield from table_rows(m.filename, z.read(m))
    else:
        yield name, list(csv.reader(io.StringIO(decode(raw))))


def pick(idx, *names):
    for n in names:
        if n in idx:
            return idx[n]
    return None


def file_records(data, src, snap):
    hi = None
    for i, r in enumerate(data[:10]):
        if any(str(c).strip() in ("Contract ID", "CN ID") for c in r):
            hi = i
            break
    if hi is None:
        return [], "no header"
    hdr = [str(c).strip() for c in data[hi]]
    idx = {}
    for j, h in enumerate(hdr):
        idx.setdefault(h, j)
    col = {
        "id": pick(idx, "Contract ID", "CN ID"), "parent": pick(idx, "Parent Contract ID"),
        "agency": pick(idx, "Agency Name", "Agency"), "pub": pick(idx, "Publish Date"),
        "amd": pick(idx, "Amendment Date", "AmendmentDate"), "start": pick(idx, "Start Date"),
        "end": pick(idx, "End Date"), "value": pick(idx, "Value", "Contract Value"),
        "change": pick(idx, "Amendments Value"), "desc": pick(idx, "Description"),
        "unspsc": pick(idx, "UNSPSC Code", "UNSPSC"), "method": pick(idx, "Procurement Method"),
        "supplier": pick(idx, "Supplier Name"), "abn": pick(idx, "Supplier ABN", "ABN"),
    }
    out = []
    for r in data[hi + 1:]:
        def g(k):
            j = col[k]
            return r[j] if j is not None and j < len(r) else None
        if blank(g("id")):
            continue
        cid, parent, n = split_id(g("id"), g("parent"))
        rec = {
            "src": src, "snap": snap, "cn_id": cid, "parent_cn_id": parent, "amendment": n,
            "publish_date": day(g("pub")), "amend_date": day(g("amd")) if n else "",
            "start_date": day(g("start")), "end_date": day(g("end")),
            "value_total": num(g("value")), "value_change": num(g("change")) if n else "",
            "agency": text(g("agency")), "supplier_name": text(g("supplier")), "supplier_abn": abn(g("abn")),
            "description": text(g("desc")), "unspsc": code(g("unspsc")),
            "procurement_method": text(g("method")), "release_date": "", "release_id": "",
        }
        out.append(rec)
    return out, hdr


def cmd_files(outdir):
    os.makedirs(outdir, exist_ok=True)
    pkg = json.loads(get(CKAN))["result"]
    by_file = {res["url"].rsplit("/", 1)[-1]: res for res in pkg["resources"]}
    log = []
    for snap, (title, fname, snapdate) in enumerate(FILES):
        res = by_file.get(fname)
        if not res:
            log.append({"file": fname, "title": title, "error": "not listed in CKAN"})
            print("missing from CKAN:", fname)
            continue
        t0 = time.time()
        try:
            raw = get(res["url"], timeout=900)
        except Exception as e:
            log.append({"file": fname, "title": title, "error": str(e)[:200]})
            print("download failed:", fname, e)
            continue
        recs = []
        for part, data in table_rows(fname, raw):
            got, hdr = file_records(data, fname, snap)
            print(f"  {fname} / {part}: {len(data)} rows -> {len(got)} notices")
            recs += got
            del data
        write_rows(os.path.join(outdir, f"file_{snap:02d}.csv.gz"), REC_COLS, recs)
        log.append({"file": fname, "title": title, "url": res["url"], "snapshot": snapdate, "bytes": len(raw),
                    "notices": len(recs), "seconds": round(time.time() - t0)})
        print(f"{fname}: {len(recs)} notices, {time.time() - t0:.0f}s", flush=True)
        del raw, recs
    with open(os.path.join(outdir, "files_log.json"), "w") as f:
        json.dump(log, f, indent=1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    if sys.argv[1] == "api":
        cmd_api(int(sys.argv[2]), sys.argv[3])
    elif sys.argv[1] == "files":
        cmd_files(sys.argv[2])
    else:
        print(__doc__)
        sys.exit(1)
