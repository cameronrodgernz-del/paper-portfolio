"""Shares outstanding from EODHD's fundamentals, for the companies test 9l needs that ASIC's daily short
files don't cover (only shares with reported short positions are in those).
Reads data/austender/need_shares.csv (symbol = the Norgate symbol, eodhd = the EODHD code to ask for, such
as XYZ.AU, or an _old code for a delisted company whose code was reused). Writes
data/austender/shares_eodhd.csv (symbol, date, shares) from the quarterly and yearly figures.
Each request costs EODHD's fundamentals weight; the run stops at --max requests.
Usage: python3 -I tools/eodhd_shares.py [repo_root] [--max N]
"""
import csv
import json
import os
import sys
import time
import urllib.parse
import urllib.request


def main(root: str = ".", cap: int = 400) -> int:
    key = os.environ.get("EODHD_API_KEY")
    if not key:
        print("no EODHD_API_KEY"); return 1
    need = list(csv.DictReader(open(os.path.join(root, "data", "austender", "need_shares.csv"), encoding="utf-8")))
    outp = os.path.join(root, "data", "austender", "shares_eodhd.csv")
    have = {r["symbol"] for r in csv.DictReader(open(outp, encoding="utf-8"))} if os.path.exists(outp) else set()
    rows = list(csv.DictReader(open(outp, encoding="utf-8"))) if os.path.exists(outp) else []
    done, missing = 0, []
    for n in need:
        if n["symbol"] in have or done >= cap:
            continue
        url = f"https://eodhd.com/api/fundamentals/{urllib.parse.quote(n['eodhd'])}?api_token={key}&fmt=json&filter=outstandingShares"
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                data = json.loads(r.read().decode())
        except Exception as e:
            missing.append(f"{n['symbol']} ({type(e).__name__})"); done += 1; continue
        done += 1
        got = 0
        for part in ("quarterly", "annual"):
            block = (data or {}).get(part) if isinstance(data, dict) else None
            for v in (block.values() if isinstance(block, dict) else block or []):
                d, s = v.get("dateFormatted") or v.get("date"), v.get("shares")
                if d and s:
                    rows.append({"symbol": n["symbol"], "date": d[:10], "shares": s, "source": f"eodhd {part}"}); got += 1
        if not got:
            missing.append(f"{n['symbol']} (none returned)")
        time.sleep(0.2)
    rows = sorted({(r["symbol"], r["date"]): r for r in rows}.values(), key=lambda r: (r["symbol"], r["date"]))
    with open(outp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["symbol", "date", "shares", "source"]); w.writeheader(); w.writerows(rows)
    open(os.path.join(root, "data", "austender", "shares_eodhd_missing.txt"), "w").write("\n".join(missing) + "\n")
    print(f"requests {done}; rows {len(rows)}; missing {len(missing)}")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    cap = int(a[a.index("--max") + 1]) if "--max" in a else 400
    pos = [x for i, x in enumerate(a) if not x.startswith("--") and (i == 0 or not a[i - 1].startswith("--"))]
    sys.exit(main(pos[0] if pos else ".", cap))
