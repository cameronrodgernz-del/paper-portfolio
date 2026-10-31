"""Export ASX prices from Norgate Data on Cam's Windows PC, for the deal tests and the deal database.

Runs where Norgate Data Updater (NDU) is installed and running (Windows), with the norgatedata
package (pip install norgatedata pandas). Not run in GitHub Actions.

For each row of config/norgate_wanted.csv (an ASX deal target, its name and announcement date) it
finds the Norgate security that was trading under that code at the announcement: a current listing,
or a delisted one (Norgate keeps a reused code's old company under its own symbol). It writes:
  <out>/prices/<TICKER>__<YYYY-MM-DD>.csv  date,open,high,low,close,volume,adj_close,dividend,split,source
     close: no adjustment; adj_close: total return (dividends and capital events)
  <out>/matches.csv   ticker, announce_date, norgate_symbol, norgate_name, first, last, status
  <out>/databases.txt the database names this subscription has
With --index it also writes <out>/index_changes.csv: every date a security joined or left the
S&P/ASX 200 and 300 since --since (default 2010-01-01), for the index change test.
Usage: python tools/norgate_export.py <repo_root> <out_dir> [--index] [--since YYYY-MM-DD]
"""
import csv
import os
import sys
from datetime import date

import norgatedata as nd


def series(sym: str, adjust, start: str):
    return nd.price_timeseries(sym, stock_price_adjustment_setting=adjust, padding_setting=nd.PaddingType.NONE,
                               start_date=start, timeseriesformat="pandas-dataframe")


def au_databases() -> list[str]:
    names = nd.databases()
    return [n for n in names if "AU" in n.upper() or "ASX" in n.upper() or "AUSTRALIA" in n.upper()]


def candidates(dbs: list[str]) -> dict:
    """Code -> [(symbol, name)] across the current and delisted Australian databases."""
    out = {}
    for db in dbs:
        try:
            rows = nd.database(db)
        except Exception as e:
            print("could not read", db, e); continue
        for r in rows:
            sym = r["symbol"] if isinstance(r, dict) else r[0]
            name = r.get("securityname", "") if isinstance(r, dict) else (r[2] if len(r) > 2 else "")
            code = sym.split("-")[0].split(".")[0].upper()
            out.setdefault(code, []).append((sym, name))
    return out


def main(root: str, out: str, index: bool = False, since: str = "2010-01-01") -> int:
    os.makedirs(os.path.join(out, "prices"), exist_ok=True)
    dbs = au_databases()
    open(os.path.join(out, "databases.txt"), "w").write("\n".join(nd.databases()) + "\n")
    print("Australian databases:", dbs)
    cand = candidates(dbs)
    wanted = list(csv.DictReader(open(os.path.join(root, "config", "norgate_wanted.csv"), encoding="utf-8")))
    matches = []
    for w in wanted:
        tk, ann = w["ticker"].upper(), w["announce_date"][:10]
        best = None
        for sym, name in cand.get(tk, []):
            try:
                df = series(sym, nd.StockPriceAdjustmentType.NONE, "2010-01-01")
            except Exception:
                continue
            if df is None or len(df) == 0:
                continue
            first, last = str(df.index[0])[:10], str(df.index[-1])[:10]
            if first < ann <= last or (first < ann and last >= ann[:7]):
                best = (sym, name, df, first, last)
                break
        if not best:
            matches.append([tk, ann, "", "", "", "", "not found"]); continue
        sym, name, raw, first, last = best
        tr = series(sym, nd.StockPriceAdjustmentType.TOTALRETURN, "2010-01-01")
        path = os.path.join(out, "prices", f"{tk}__{ann}.csv")
        with open(path, "w", newline="") as f:
            wr = csv.writer(f)
            wr.writerow(["date", "open", "high", "low", "close", "volume", "adj_close", "dividend", "split", "source"])
            for d, row in raw.iterrows():
                adj = tr["Close"].get(d) if tr is not None and "Close" in tr else ""
                div = row.get("Dividend", "") if hasattr(row, "get") else ""
                wr.writerow([str(d)[:10], row["Open"], row["High"], row["Low"], row["Close"], row.get("Volume", ""),
                             adj, div if div else "", "", "norgate"])
        matches.append([tk, ann, sym, name, first, last, "ok"])
        print(tk, ann, "->", sym, name, first, last)
    with open(os.path.join(out, "matches.csv"), "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["ticker", "announce_date", "norgate_symbol", "norgate_name", "first", "last", "status"])
        wr.writerows(matches)
    if index:
        with open(os.path.join(out, "index_changes.csv"), "w", newline="") as f:
            wr = csv.writer(f); wr.writerow(["index", "symbol", "name", "date", "change"])
            for idx in ("S&P/ASX 200", "S&P/ASX 300"):
                for code, lst in cand.items():
                    for sym, name in lst:
                        try:
                            ts = nd.index_constituent_timeseries(sym, idx, padding_setting=nd.PaddingType.NONE,
                                                                 start_date=since, timeseriesformat="pandas-dataframe")
                        except Exception:
                            continue
                        if ts is None or len(ts) == 0:
                            continue
                        col = ts.columns[0]
                        prev = None
                        for d, v in ts[col].items():
                            v = int(v)
                            if prev is not None and v != prev:
                                wr.writerow([idx, sym, name, str(d)[:10], "joined" if v == 1 else "left"])
                            prev = v
        print("index changes written")
    print(f"done: {sum(1 for m in matches if m[-1] == 'ok')} of {len(matches)} found")
    return 0


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    since = next((sys.argv[i + 1] for i, x in enumerate(sys.argv) if x == "--since"), "2010-01-01")
    sys.exit(main(a[0], a[1], "--index" in sys.argv, since))
