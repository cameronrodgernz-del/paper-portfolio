"""One-off look at the AusTender sources before the bulk download. Prints only; saves nothing.
Round 3: xlsx layouts, publish-year spread of the cumulative files, how amendment values and dates
are carried in the files compared with the API, and how amendment release dates look across years.
Usage: python3 -I tools/austender_probe.py
"""
import csv
import io
import json
import time
import urllib.request
import zipfile
from collections import Counter

UA = "paper-portfolio research (github.com/cameronrodgernz-del/paper-portfolio)"
CKAN = "https://data.gov.au/data/api/3/action/package_show?id=5c7fa69b-b0e9-4553-b8df-2a022dd2e982"
API = "https://api.tenders.gov.au/ocds"
WATCH = {"CN3574707", "CN3574774", "CN3350299", "CN3242742", "CN1059961", "CN3479056"}


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=600) as r:
        return r.read()


def decode(raw):
    for enc in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            pass


def rows_of(name, url, raw):
    if url.endswith(".xlsx"):
        from python_calamine import CalamineWorkbook
        wb = CalamineWorkbook.from_filelike(io.BytesIO(raw))
        for sheet in wb.sheet_names:
            data = wb.get_sheet_by_name(sheet).to_python()
            print(f"  sheet {sheet!r} rows={len(data)}")
            for r in data[:5]:
                print("   |", r[:45])
            yield sheet, data
    elif raw[:2] == b"PK":
        z = zipfile.ZipFile(io.BytesIO(raw))
        for m in z.infolist():
            if m.filename.lower().endswith(".csv"):
                yield m.filename, list(csv.reader(io.StringIO(decode(z.read(m)))))
    else:
        yield "csv", list(csv.reader(io.StringIO(decode(raw))))


def year_of(s):
    s = str(s or "")
    if len(s) >= 10 and s[4] == "-":
        return s[:4]
    if "/" in s:
        p = s.split("/")
        if len(p) == 3:
            return p[2][:4]
    if "-" in s:
        return s.split("-")[-1][:4]
    return "?"


def main():
    pkg = json.loads(get(CKAN))["result"]
    for res in pkg["resources"]:
        url = res["url"]
        if "data.gov.au" not in url or "unspsc" in url.lower() or url.endswith(".pdf") or "gaps" in url.lower():
            continue
        print("=== resource:", res["name"])
        try:
            raw = get(url)
            for part, data in rows_of(res["name"], url, raw):
                hi = None
                for i, r in enumerate(data[:10]):
                    if any(str(c).strip() in ("Contract ID", "CN ID") for c in r):
                        hi = i
                        break
                if hi is None:
                    print("  no header found in", part)
                    continue
                hdr = [str(c).strip() for c in data[hi]]
                print("  header row", hi, hdr)
                idx = {h: j for j, h in enumerate(hdr)}
                cid = idx.get("Contract ID", idx.get("CN ID"))
                pub = idx.get("Publish Date")
                amd = idx.get("Amendment Date", idx.get("AmendmentDate"))
                yrs = Counter()
                ams = Counter()
                for r in data[hi + 1:]:
                    if len(r) <= max(cid, pub):
                        continue
                    yrs[year_of(r[pub])] += 1
                    if "-A" in str(r[cid]):
                        ams[year_of(r[amd]) if amd is not None else "?"] += 1
                    if str(r[cid]).split("-A")[0] in WATCH:
                        print("   watch:", [r[j] for j in range(min(len(r), 35))])
                print("  publish years:", sorted(yrs.items()))
                print("  amendment-date years:", sorted(ams.items()))
                del data
        except Exception as e:
            print("  failed:", repr(e))

    print("=== findById")
    for cn in ("CN3574707", "CN3574774"):
        try:
            d = json.loads(get(f"{API}/findById/{cn}"))
            for r in d.get("releases", []):
                c = r["contracts"][0]
                print(cn, r["tag"], r["date"], c.get("dateSigned"), c["value"], c.get("amendments"))
            print(json.dumps(d["releases"][-1], indent=1)[:2500])
        except Exception as e:
            print(cn, "failed", repr(e))

    print("=== API sample days")
    for day in ("2014-06-30", "2016-03-01", "2018-03-01", "2020-09-01", "2021-09-01", "2022-09-01",
                "2023-03-01", "2023-09-01", "2024-09-02", "2025-09-01", "2026-06-30"):
        url = f"{API}/findByDates/contractPublished/{day}T00:00:00Z/{day}T23:59:59Z"
        rels, pages, t0 = [], 0, time.time()
        while url:
            d = json.loads(get(url))
            pages += 1
            rels += d.get("releases", [])
            url = (d.get("links") or {}).get("next")
            if not d.get("releases"):
                break
            time.sleep(0.3)
        tags = Counter(r["tag"][0] for r in rels)
        am_dates = Counter(r["date"] for r in rels if r["tag"][0] == "contractAmendment")
        lag = Counter()
        for r in rels:
            if r["tag"][0] == "contractAmendment":
                lag[r["date"][:4]] += 1
        same = sum(1 for r in rels if r["tag"][0] == "contract" and r["date"] != r["contracts"][0].get("dateSigned"))
        print(f"{day}: pages={pages} releases={len(rels)} {dict(tags)} {time.time()-t0:.1f}s; "
              f"contract releases whose date differs from dateSigned={same}")
        print("   amendment release years:", sorted(lag.items()), "| top shared timestamps:", am_dates.most_common(3))
        keys = set()
        for r in rels:
            c = r["contracts"][0]
            k = c["amendments"][0]["id"] if c.get("amendments") else c["id"]
            if k in keys:
                print("   duplicate key", k)
            keys.add(k)
        ex = [r for r in rels if r["tag"][0] == "contract"][:1]
        if ex:
            p = ex[0]["parties"]
            print("   parties roles:", [(x.get("roles"), x.get("name")[:40]) for x in p])


if __name__ == "__main__":
    main()
