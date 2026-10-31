"""Save EODHD's lists of Australian symbols, current and delisted, so a deal target whose ASX code
was later reused by another company can be matched to its own price history (rulebook 9c).
Two list requests, and a search for each deal target still without prices. Writes data/history/eodhd_au_symbols.json and eodhd_au_delisted.json.
Usage: python3 -I src/eodhd_symbols.py [data_dir]
"""
import json
import os
import sys
import urllib.parse
import urllib.request


def get(url: str):
    with urllib.request.urlopen(url, timeout=120) as r:
        return json.loads(r.read().decode())


def main(data_dir: str = "data/history") -> int:
    key = os.environ.get("EODHD_API_KEY")
    if not key:
        print("no EODHD_API_KEY"); return 1
    os.makedirs(data_dir, exist_ok=True)
    for name, extra in (("eodhd_au_symbols.json", ""), ("eodhd_au_delisted.json", "&delisted=1")):
        try:
            rows = get(f"https://eodhd.com/api/exchange-symbol-list/AU?api_token={key}&fmt=json{extra}")
        except Exception as e:
            print(name, "failed:", type(e).__name__, str(e)[:200]); continue
        json.dump(rows, open(os.path.join(data_dir, name), "w"), separators=(",", ":"))
        print(name, len(rows) if isinstance(rows, list) else rows)
    # names of deal targets with no price history found yet: EODHD's search may hold them under another code
    names = ["Toll Holdings", "Vision Eye Institute", "Affinity Education", "iProperty", "Veda Group", "UXC", "Sedgman",
             "Ethane Pipeline", "Asciano", "Pacific Brands", "Patties Foods", "Intecq", "Vitaco", "SAI Global", "ASG Group",
             "UGL", "Cover-More", "Generation Healthcare", "Finders Resources"]
    found = {}
    for n in names:
        try:
            found[n] = get(f"https://eodhd.com/api/search/{urllib.parse.quote(n)}?api_token={key}&fmt=json&exchange=AU&limit=10")
        except Exception as e:
            found[n] = {"error": f"{type(e).__name__}: {str(e)[:120]}"}
    json.dump(found, open(os.path.join(data_dir, "eodhd_au_search.json"), "w"), indent=1)
    print("searched", len(found))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data/history"))
