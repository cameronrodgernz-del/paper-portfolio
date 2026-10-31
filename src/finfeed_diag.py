"""Check FinFeedAPI's NZX coverage (exchange XNZE) with the free key.
Endpoints are from its published OpenAPI file:
https://api-historical.stock.finfeedapi.com/swagger/v1/swagger.json
Four requests: exchanges, NZX symbols, one share's daily history, and one whole-exchange day.
Writes data/diagnostics/finfeed_nz.json. Usage: python3 -I src/finfeed_diag.py [data_dir]
"""
import json
import os
import sys
import urllib.error
import urllib.request

BASE = "https://api-historical.stock.finfeedapi.com"


def get(path: str, key: str):
    req = urllib.request.Request(BASE + path, headers={"Authorization": key, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            headers = {k: v for k, v in r.headers.items() if any(w in k.lower() for w in ("limit", "credit", "quota", "cost"))}
            return {"status": r.status, "headers": headers, "body": json.loads(r.read().decode())}
    except urllib.error.HTTPError as e:
        return {"status": e.code, "error": e.read().decode(errors="replace")[:500]}
    except Exception as e:
        return {"error": f"{type(e).__name__}: {str(e)[:300]}"}


def main(data_dir: str = "data") -> int:
    key = os.environ.get("FINFEED_API_KEY")
    if not key:
        print("no FINFEED_API_KEY"); return 1
    out = {}
    ex = get("/v1/exchanges", key)
    if isinstance(ex.get("body"), list):
        ex["body"] = [e for e in ex["body"] if "NZ" in json.dumps(e).upper() or "ZEALAND" in json.dumps(e).upper()]
    out["exchanges_nz"] = ex
    sy = get("/v1/symbols/XNZE?limit=400", key)
    if isinstance(sy.get("body"), list):
        sy["count"] = len(sy["body"])
        wanted = ("AIR", "FBU", "FNZ", "SKC", "OCA", "KMD", "HGH", "FPH")
        sy["sample"] = [s for s in sy["body"] if any(str(s.get("symbol_id", "")).upper().startswith(w) for w in wanted)][:30]
        del sy["body"]
    out["symbols_xnze"] = sy
    out["air_daily_october"] = get("/v1/ohlcv/exchange-symbol/XNZE/AIR/history?period_id=1DAY"
                                   "&time_start=2026-10-01T00:00:00&time_end=2026-10-31T00:00:00&limit=40", key)
    day = get("/v1/ohlcv/exchange/XNZE/history?period_id=1DAY&time_start=2026-10-30T00:00:00"
              "&time_end=2026-10-31T00:00:00&limit=1000", key)
    if isinstance(day.get("body"), list):
        day["rows"] = len(day["body"])
        day["sample"] = day["body"][:5]
        del day["body"]
    out["whole_exchange_30_oct"] = day
    os.makedirs(os.path.join(data_dir, "diagnostics"), exist_ok=True)
    with open(os.path.join(data_dir, "diagnostics", "finfeed_nz.json"), "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1)[:4000])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data"))
