"""Check FinFeedAPI's NZX coverage (exchange XNZE).
Endpoints are from its published OpenAPI file:
https://api-historical.stock.finfeedapi.com/swagger/v1/swagger.json
NZX symbol ids are ISINs; the NZX code is in name_ticker.
Writes data/diagnostics/finfeed_nz.json. Usage: python3 -I src/finfeed_diag.py [data_dir]
"""
import json
import os
import sys
import urllib.error
import urllib.request

BASE = "https://api-historical.stock.finfeedapi.com"
WANTED = ("AIR", "FPH", "SKC", "OCA", "KMD", "HGH", "FBU", "SPK", "IFT", "MEL", "CEN", "AIA", "FNZ", "TPW", "RYM")


def get(path: str, key: str):
    req = urllib.request.Request(BASE + path, headers={"Authorization": key, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            headers = {k: v for k, v in r.headers.items() if any(w in k.lower() for w in ("limit", "credit", "quota", "cost"))}
            return {"status": r.status, "headers": headers, "body": json.loads(r.read().decode())}
    except urllib.error.HTTPError as e:
        return {"status": e.code, "error": e.read().decode(errors="replace")[:500]}
    except Exception as e:
        return {"error": f"{type(e).__name__}: {str(e)[:300]}"}


def summary(res: dict) -> dict:
    rows = res.pop("body", None)
    if isinstance(rows, list):
        res["rows"] = len(rows)
        res["first"] = rows[0] if rows else None
        res["last"] = rows[-1] if rows else None
    return res


def main(data_dir: str = "data") -> int:
    key = os.environ.get("FINFEED_API_KEY")
    if not key:
        print("no FINFEED_API_KEY"); return 1
    out = {}
    rows, sy = [], {}
    for page in range(1, 11):       # the full list in one request times out; page through it
        res = get(f"/v1/symbols/XNZE?limit=1000&page={page}", key)
        sy = {k: v for k, v in res.items() if k != "body"}
        chunk = res.get("body") or []
        rows += chunk
        if len(chunk) < 1000:
            break
    sy["count"] = len(rows)
    sy["active_dated"] = sum(1 for r in rows if r.get("date") == max((x.get("date", "") for x in rows), default=""))
    tick = {}
    for w in WANTED:
        hits = [r for r in rows if (r.get("name_ticker") or "").strip().upper() == w]
        tick[w] = hits[:3]
    sy["matches"] = tick
    out["symbols_xnze"] = sy
    os.makedirs(os.path.join(data_dir, "diagnostics"), exist_ok=True)
    with open(os.path.join(data_dir, "diagnostics", "finfeed_nz_symbols.json"), "w") as f:
        json.dump(rows, f)
    air = (tick.get("AIR") or [None])[0]
    if air:
        sid = air["symbol_id"]
        out["air_symbol"] = air
        out["air_october"] = get(f"/v1/ohlcv/exchange-symbol/XNZE/{sid}/history?period_id=1DAY"
                                 "&time_start=2026-10-01T00:00:00&time_end=2026-10-31T00:00:00&limit=40", key)
        out["air_since_2009"] = summary(get(f"/v1/ohlcv/exchange-symbol/XNZE/{sid}/history?period_id=1DAY"
                                            "&time_start=2009-01-01T00:00:00&time_end=2026-10-31T00:00:00&limit=10000", key))
    day = get("/v1/ohlcv/exchange/XNZE/history?period_id=1DAY"
              "&time_start=2026-10-29T00:00:00&time_end=2026-10-30T00:00:00&limit=1000", key)
    known = {"NZAIRE0001S2": "AIR", "NZFAPE0001S2": "FPH", "NZSKCE0001S2": "SKC", "NZOCAE0002S0": "OCA", "NZSPKE0001S8": "SPK"}
    if isinstance(day.get("body"), list):
        day["known_rows"] = {known[r["symbol_id_exchange"]]: r for r in day["body"] if r.get("symbol_id_exchange") in known}
        day["with_volume"] = sum(1 for r in day["body"] if (r.get("volume_traded") or 0) > 0)
        day["nz_isins"] = sum(1 for r in day["body"] if str(r.get("symbol_id_exchange", "")).startswith("NZ"))
    out["whole_exchange_29_oct"] = summary(day)
    out["air_by_isin_since_2009"] = summary(get("/v1/ohlcv/exchange-symbol/XNZE/NZAIRE0001S2/history?period_id=1DAY"
                                                "&time_start=2009-01-01T00:00:00&time_end=2026-10-31T00:00:00&limit=10000", key))
    with open(os.path.join(data_dir, "diagnostics", "finfeed_nz.json"), "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1)[:5000])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data"))
