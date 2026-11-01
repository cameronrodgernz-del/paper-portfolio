"""One-off look at the AusTender sources before the bulk download: lists the data.gov.au resources
for the "Historical Australian Government Contract Data" dataset and prints the shape of a few
AusTender OCDS API answers (field names, paging links, amendment releases). Prints only; saves nothing.
Usage: python3 -I tools/austender_probe.py
"""
import json
import time
import urllib.request

UA = "paper-portfolio research (github.com/cameronrodgernz-del/paper-portfolio)"
CKAN = "https://data.gov.au/data/api/3/action/package_show?id=5c7fa69b-b0e9-4553-b8df-2a022dd2e982"
API = "https://api.tenders.gov.au/ocds"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    t = time.time()
    with urllib.request.urlopen(req, timeout=120) as r:
        body = r.read()
        print(f"GET {url} -> {r.status} {len(body)} bytes {time.time()-t:.1f}s")
        for k in ("Content-Type", "Content-Length", "Last-Modified"):
            if r.headers.get(k):
                print(f"  {k}: {r.headers.get(k)}")
    return body


def main():
    print("=== CKAN resources")
    try:
        pkg = json.loads(get(CKAN))["result"]
        print("title:", pkg.get("title"), "| modified:", pkg.get("metadata_modified"))
        for res in pkg["resources"]:
            print(json.dumps({k: res.get(k) for k in ("name", "format", "url", "size", "created", "last_modified")}))
    except Exception as e:
        print("CKAN failed:", repr(e))

    for window in ("2013-01-02T00:00:00Z/2013-01-02T23:59:59Z", "2024-03-01T00:00:00Z/2024-03-01T23:59:59Z",
                   "2026-10-20T00:00:00Z/2026-10-20T23:59:59Z"):
        print("=== API window", window)
        try:
            d = json.loads(get(f"{API}/findByDates/contractPublished/{window}"))
        except Exception as e:
            print("API failed:", repr(e))
            continue
        print("top keys:", list(d.keys()))
        rel = d.get("releases", [])
        print("releases:", len(rel), "| links:", d.get("links"))
        tags = {}
        for r in rel:
            t = ",".join(r.get("tag", []))
            tags[t] = tags.get(t, 0) + 1
        print("tags:", tags)
        shown = set()
        for r in rel:
            t = ",".join(r.get("tag", []))
            if t in shown:
                continue
            shown.add(t)
            print(f"--- sample release tag={t}")
            print(json.dumps(r, indent=1)[:5000])
        time.sleep(2)

    print("=== findById with amendments")
    try:
        d = json.loads(get(f"{API}/findById/CN2990589"))
        print(json.dumps(d, indent=1)[:6000])
    except Exception as e:
        print("findById failed:", repr(e))


if __name__ == "__main__":
    main()
