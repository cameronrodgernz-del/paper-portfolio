"""One-off look at the AusTender sources before the bulk download. Prints only; saves nothing.
Round 2: downloads each data.gov.au contract file and prints its layout (zip members, sheet names,
header and first rows), counts API pages for one day, and compares one day of the 2018-19 file
with the API (publish dates, amendment dates and values) so the merge rules rest on the real data.
Usage: python3 -I tools/austender_probe.py
"""
import csv
import io
import json
import time
import urllib.request
import zipfile

UA = "paper-portfolio research (github.com/cameronrodgernz-del/paper-portfolio)"
CKAN = "https://data.gov.au/data/api/3/action/package_show?id=5c7fa69b-b0e9-4553-b8df-2a022dd2e982"
API = "https://api.tenders.gov.au/ocds"


def get(url, quiet=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    t = time.time()
    with urllib.request.urlopen(req, timeout=600) as r:
        body = r.read()
    if not quiet:
        print(f"GET {url[:150]} -> {len(body)} bytes {time.time()-t:.1f}s")
    return body


def decode(raw):
    for enc in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            pass


def show_csv(raw, label):
    text = decode(raw)
    lines = text.splitlines()
    print(f"  [{label}] {len(lines)} lines")
    for ln in lines[:4]:
        print("   |", ln[:600])
    return text


def show_xlsx(raw, label):
    import openpyxl
    wb = openpyxl.load_workbook(io.BytesIO(raw), read_only=True)
    for ws in wb.worksheets:
        print(f"  [{label}] sheet {ws.title!r} dims={ws.dimensions}")
        for i, row in enumerate(ws.iter_rows(values_only=True)):
            print("   |", [c for c in row][:40])
            if i >= 4:
                break


def main():
    pkg = json.loads(get(CKAN))["result"]
    files = {}
    for res in pkg["resources"]:
        url = res["url"]
        if "data.gov.au" not in url or "unspsc" in url.lower() or url.endswith(".pdf"):
            continue
        print("=== resource:", res["name"])
        try:
            raw = get(url)
        except Exception as e:
            print("  download failed:", repr(e))
            continue
        files[res["name"]] = raw
        try:
            if raw[:2] == b"PK" and not url.endswith(".xlsx"):
                z = zipfile.ZipFile(io.BytesIO(raw))
                for m in z.infolist():
                    print(f"  member {m.filename} {m.file_size}")
                    data = z.read(m)
                    if m.filename.lower().endswith(".csv"):
                        show_csv(data, m.filename)
                    elif m.filename.lower().endswith(".xlsx"):
                        show_xlsx(data, m.filename)
            elif url.endswith(".xlsx"):
                show_xlsx(raw, "xlsx")
            else:
                show_csv(raw, "csv")
        except Exception as e:
            print("  read failed:", repr(e))

    print("=== API pages for 2019-03-01 (Canberra day: 2019-02-28T13:00Z to 2019-03-01T12:59:59Z)")
    url = f"{API}/findByDates/contractPublished/2019-02-28T13:00:00Z/2019-03-01T12:59:59Z"
    rels, pages = [], 0
    while url:
        d = json.loads(get(url, quiet=True))
        pages += 1
        rels += d.get("releases", [])
        url = (d.get("links") or {}).get("next")
        if not d.get("releases"):
            break
        time.sleep(0.5)
    print(f"pages={pages} releases={len(rels)}")
    api = {}
    for r in rels:
        c = r["contracts"][0]
        key = c["amendments"][0]["id"] if c.get("amendments") else c["id"]
        api[key] = (r["date"], c.get("dateSigned"), c["value"]["amount"], r["tag"][0], c.get("id"))
    print("sample api keys:", list(api.items())[:6])
    ams = [k for k in api if "-A" in k]
    print("amendment releases:", len(ams))
    for k in ams[:15]:
        parent = k.split("-A")[0]
        print("  ", k, api[k], "| parent:", api.get(parent))

    print("=== 2018-19 file rows published 2019-03-01")
    import openpyxl
    raw = files.get("2018-19 Australian Government Contract Data")
    if raw:
        wb = openpyxl.load_workbook(io.BytesIO(raw), read_only=True)
        ws = wb.worksheets[0]
        header, n, hits = None, 0, []
        for row in ws.iter_rows(values_only=True):
            if header is None:
                if row and any(isinstance(c, str) and "CN ID" in c for c in row if c):
                    header = [str(c) for c in row]
                    print("header:", header)
                continue
            n += 1
            rec = dict(zip(header, row))
            s = " ".join(str(v) for v in rec.values())
            if "2019-03-01" in s:
                hits.append(rec)
        print("rows:", n, "rows mentioning 2019-03-01:", len(hits))
        for rec in hits[:25]:
            print("  ", {k: rec[k] for k in header if k and ("ID" in k or "Date" in k or "Value" in k)})
            cid = None
            for k in header:
                if k and k.strip().upper() == "CN ID":
                    cid = rec[k]
            print("     api:", api.get(str(cid)))


if __name__ == "__main__":
    main()
