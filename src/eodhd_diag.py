"""One-off check of how EODHD names NZX shares (the first nightly run got 'not found'
for every .NZ symbol). Uses 3 of the free plan's 20 daily requests.
Writes data/diagnostics/eodhd_nz.json. Usage: python3 -I src/eodhd_diag.py [data_dir]
"""
import json
import os
import sys
import urllib.request


def get(url: str):
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        return {"error": f"{type(e).__name__}: {str(e)[:200]}"}


def main(data_dir: str = "data") -> int:
    key = os.environ.get("EODHD_API_KEY")
    if not key:
        print("no EODHD_API_KEY"); return 1
    out = {}
    ex = get(f"https://eodhd.com/api/exchanges-list/?api_token={key}&fmt=json")
    out["exchanges_matching_new_zealand_or_australia"] = (
        [e for e in ex if any(w in json.dumps(e).lower() for w in ("zealand", "australia", "nzx", "asx"))]
        if isinstance(ex, list) else ex)
    out["search_air_new_zealand"] = get(f"https://eodhd.com/api/search/Air%20New%20Zealand?api_token={key}&fmt=json&limit=10")
    out["search_fletcher_building"] = get(f"https://eodhd.com/api/search/Fletcher%20Building?api_token={key}&fmt=json&limit=10")
    os.makedirs(os.path.join(data_dir, "diagnostics"), exist_ok=True)
    with open(os.path.join(data_dir, "diagnostics", "eodhd_nz.json"), "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1)[:3000])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data"))
