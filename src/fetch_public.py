"""Free, official public series that answer a plain request (checked 31 Oct 2026).

RBA F11.1: daily AUD exchange rates, including A$1 = USD and A$1 = NZD.
RBA F1.1: Australian money market rates.
FRED: DEXUSNZ and DEXUSAL (USD per NZD and per AUD, a second check on currency),
      DTB3 (US 3-month Treasury bill), IR3TIB01NZM156N (NZ 3-month interbank, monthly).
The RBNZ site refused automated requests (HTTP 403), so NZ rates come from FRED.
Usage: python3 -I src/fetch_public.py <data_dir>
"""
import csv
import io
import os
import sys
import urllib.request

FRED = ["DEXUSNZ", "DEXUSAL", "DTB3", "IR3TIB01NZM156N"]
RBA = {"rba_f11_1": "https://www.rba.gov.au/statistics/tables/csv/f11.1-data.csv",
       "rba_f1_1": "https://www.rba.gov.au/statistics/tables/csv/f1.1-data.csv"}


def get(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=30) as r:
        return r.read()


def rba_series(raw: bytes, wanted: dict[str, str]) -> list[dict]:
    """Pull named columns (by 'Title' row) from an RBA statistical table CSV."""
    rows = list(csv.reader(io.StringIO(raw.decode("latin-1"))))
    title = next(r for r in rows if r and r[0] == "Title")
    idx = {name: title.index(col) for name, col in wanted.items()}
    out = []
    for r in rows:
        if not r or len(r) < len(title) or not r[0][:2].isdigit():
            continue
        rec = {"date": r[0]}
        for name, i in idx.items():
            rec[name] = float(r[i]) if r[i].strip() else None
        out.append(rec)
    return out


def main(data_dir: str) -> None:
    os.makedirs(os.path.join(data_dir, "fx"), exist_ok=True)
    os.makedirs(os.path.join(data_dir, "rates"), exist_ok=True)
    for s in FRED:
        open(os.path.join(data_dir, "rates", f"{s}.csv"), "wb").write(
            get(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={s}"))
    raw = get(RBA["rba_f11_1"])
    open(os.path.join(data_dir, "fx", "rba_f11_1.csv"), "wb").write(raw)
    fx = rba_series(raw, {"aud_usd": "A$1=USD", "aud_nzd": "A$1=NZD"})
    with open(os.path.join(data_dir, "fx", "fx_daily.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "aud_usd", "aud_nzd", "nzd_usd", "nzd_aud"])
        for r in fx:
            if r["aud_usd"] and r["aud_nzd"]:
                w.writerow([r["date"], r["aud_usd"], r["aud_nzd"],
                            round(r["aud_usd"] / r["aud_nzd"], 6), round(1 / r["aud_nzd"], 6)])
    open(os.path.join(data_dir, "rates", "rba_f1_1.csv"), "wb").write(get(RBA["rba_f1_1"]))
    print("fetched", len(fx), "RBA fx rows and", len(FRED), "FRED series")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data")
