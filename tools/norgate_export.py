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
With --universe it writes daily prices for every Australian security Norgate has, listed and
delisted, from --since (default 2010-01-01), for the tests that need the whole market (a takeover
target model, the June tax-year sell-off):
  <out>/universe/securities.csv          symbol, name, database, first, last, days
  <out>/universe/prices_<YYYY>.csv.gz    symbol,date,open,high,low,close,volume,tr_close
     close: as traded; tr_close: total return (dividends and capital events), for working out returns
With --universe-only it skips the deal-target export and the index changes.
Usage: python tools/norgate_export.py <repo_root> <out_dir> [--index] [--universe] [--universe-only] [--since YYYY-MM-DD]
"""
import csv
import gzip
import os
import sys
from datetime import date

import norgatedata as nd
import pandas as pd

# Norgate's own index names first, then the index symbols as a fallback.
INDEXES = {"S&P/ASX 200": ["S&P/ASX 200", "$XJO", "$XJO.au"],
           "S&P/ASX 300": ["S&P/ASX 300", "$XKO", "$XKO.au"]}
PROBES = ["BHP", "BHP.au", "CBA", "CBA.au"]


def series(sym: str, adjust, start: str):
    return nd.price_timeseries(sym, stock_price_adjustment_setting=adjust, padding_setting=nd.PaddingType.NONE,
                               start_date=pd.Timestamp(start), timeseriesformat="pandas-dataframe")


def au_databases() -> list[str]:
    """Current and delisted Australian equity databases (not options, warrants or indices)."""
    names = nd.databases()
    au = [n for n in names if "AU" in n.upper() or "ASX" in n.upper() or "AUSTRALIA" in n.upper()]
    eq = [n for n in au if "EQUIT" in n.upper() or "STOCK" in n.upper()]
    return eq or au


def candidates(dbs: list[str]) -> dict:
    """Code -> [(symbol, name)] across the current and delisted Australian databases."""
    out = {}
    for db in dbs:
        try:
            rows = nd.database(db)
        except Exception as e:
            print("could not read", db, e); continue
        print(db, len(rows), "securities")
        for r in rows:
            if isinstance(r, dict):
                sym = r.get("symbol") or r.get("Symbol")
                name = next((v for k, v in r.items() if "name" in k.lower()), "")
            else:
                sym, name = r[0], (r[2] if len(r) > 2 else "")
            if not sym:
                continue
            code = sym.split("-")[0].split(".")[0].upper()
            lst = out.setdefault(code, [])
            if all(s != sym for s, _ in lst):  # Norgate lists some symbols twice
                lst.append((sym, name))
    return out


def constituent(sym: str, idx: str, since: str):
    ts = nd.index_constituent_timeseries(sym, idx, padding_setting=nd.PaddingType.NONE,
                                         start_date=pd.Timestamp(since), timeseriesformat="pandas-dataframe")
    if ts is None or len(ts) == 0:
        return None
    col = "Index Constituent" if "Index Constituent" in ts.columns else ts.columns[-1]
    return ts[col]


def index_name(label: str, since: str):
    """The name Norgate accepts for this index, found by asking about a long-standing member."""
    for name in INDEXES[label]:
        for probe in PROBES:
            try:
                s = constituent(probe, name, since)
            except Exception:
                continue
            if s is not None and s.max() == 1:
                return name
    return None


def fmt(x) -> str:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return ""
    if v != v:
        return ""
    return f"{v:.6g}"


def universe(dbs: list[str], out: str, since: str) -> int:
    """Daily prices for every listed and delisted Australian security, one gzip file a year."""
    udir = os.path.join(out, "universe")
    os.makedirs(udir, exist_ok=True)
    files, writers = {}, {}
    def writer(year: str):
        if year not in writers:
            fh = gzip.open(os.path.join(udir, f"prices_{year}.csv.gz"), "wt", newline="", encoding="utf-8")
            w = csv.writer(fh)
            w.writerow(["symbol", "date", "open", "high", "low", "close", "volume", "tr_close"])
            files[year], writers[year] = fh, w
        return writers[year]
    secs, seen = [], set()
    for db in dbs:
        try:
            rows = nd.database(db)
        except Exception as e:
            print("could not read", db, e); continue
        for r in rows:
            if isinstance(r, dict):
                sym = r.get("symbol") or r.get("Symbol")
                name = next((v for k, v in r.items() if "name" in k.lower()), "")
            else:
                sym, name = r[0], (r[2] if len(r) > 2 else "")
            if sym and sym not in seen:  # Norgate lists some symbols twice
                seen.add(sym)
                secs.append((sym, name, db))
    print("universe:", len(secs), "securities across", dbs, flush=True)
    done = 0
    with open(os.path.join(udir, "securities.csv"), "w", newline="", encoding="utf-8") as sf:
        sw = csv.writer(sf)
        sw.writerow(["symbol", "name", "database", "first", "last", "days"])
        for i, (sym, name, db) in enumerate(secs, 1):
            if i % 250 == 0:
                print(f"  {i} of {len(secs)} securities, {done} with prices", flush=True)
            try:
                raw = series(sym, nd.StockPriceAdjustmentType.NONE, since)
            except Exception:
                continue
            if raw is None or len(raw) == 0:
                continue
            try:
                tr = series(sym, nd.StockPriceAdjustmentType.TOTALRETURN, since)
                trc = tr["Close"] if tr is not None and "Close" in tr else None
            except Exception:
                trc = None
            for d, row in raw.iterrows():
                ds = str(d)[:10]
                writer(ds[:4]).writerow([sym, ds, fmt(row["Open"]), fmt(row["High"]), fmt(row["Low"]), fmt(row["Close"]),
                                         fmt(row.get("Volume", "")), fmt(trc.get(d)) if trc is not None else ""])
            sw.writerow([sym, name, db, str(raw.index[0])[:10], str(raw.index[-1])[:10], len(raw)])
            done += 1
    for fh in files.values():
        fh.close()
    print(f"universe written: {done} securities with prices since {since}", flush=True)
    return done


def main(root: str, out: str, index: bool = False, since: str = "2010-01-01", universe_too: bool = False,
         universe_only: bool = False) -> int:
    if not nd.status():
        print("Norgate Data Updater is not running. Open it, let it finish updating, then run this again.")
        return 2
    os.makedirs(os.path.join(out, "prices"), exist_ok=True)
    dbs = au_databases()
    with open(os.path.join(out, "databases.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(nd.databases()) + "\n")
    print("Australian databases:", dbs)
    if universe_only:
        universe(dbs, out, since)
        return 0
    cand = candidates(dbs)
    if not cand:
        print("No Australian securities found: check the subscription in Norgate Data Updater.")
        return 3
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
        try:
            tr = series(sym, nd.StockPriceAdjustmentType.TOTALRETURN, "2010-01-01")
        except Exception as e:
            print(tk, "total return series failed:", e); tr = None
        path = os.path.join(out, "prices", f"{tk}__{ann}.csv")
        with open(path, "w", newline="", encoding="utf-8") as f:
            wr = csv.writer(f)
            wr.writerow(["date", "open", "high", "low", "close", "volume", "adj_close", "dividend", "split", "source"])
            for d, row in raw.iterrows():
                adj = tr["Close"].get(d) if tr is not None and "Close" in tr else ""
                div = row.get("Dividend", "") if hasattr(row, "get") else ""
                wr.writerow([str(d)[:10], row["Open"], row["High"], row["Low"], row["Close"], row.get("Volume", ""),
                             adj, div if div else "", "", "norgate"])
        matches.append([tk, ann, sym, name, first, last, "ok"])
        print(tk, ann, "->", sym, name, first, last)
    with open(os.path.join(out, "matches.csv"), "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f); wr.writerow(["ticker", "announce_date", "norgate_symbol", "norgate_name", "first", "last", "status"])
        wr.writerows(matches)
    if index:
        syms = [(sym, name) for lst in cand.values() for sym, name in lst]
        with open(os.path.join(out, "index_changes.csv"), "w", newline="", encoding="utf-8") as f:
            wr = csv.writer(f); wr.writerow(["index", "symbol", "name", "date", "change"])
            for label in INDEXES:
                idx = index_name(label, since)
                if not idx:
                    print("WARNING: Norgate did not recognise", label, "under any of", INDEXES[label]); continue
                print("index", label, "as", repr(idx), "across", len(syms), "securities")
                n = 0
                for i, (sym, name) in enumerate(syms, 1):
                    if i % 1000 == 0:
                        print(f"  {label}: {i} of {len(syms)} checked, {n} changes so far", flush=True)
                    try:
                        s = constituent(sym, idx, since)
                    except Exception:
                        continue
                    if s is None:
                        continue
                    prev = None
                    for d, v in s.items():
                        v = int(v)
                        if prev is not None and v != prev:
                            wr.writerow([label, sym, name, str(d)[:10], "joined" if v == 1 else "left"]); n += 1
                        prev = v
                print(f"  {label}: {n} changes")
        print("index changes written")
    print(f"done: {sum(1 for m in matches if m[-1] == 'ok')} of {len(matches)} found")
    if universe_too:
        universe(dbs, out, since)
    return 0


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    since = next((sys.argv[i + 1] for i, x in enumerate(sys.argv) if x == "--since"), "2010-01-01")
    sys.exit(main(a[0], a[1], "--index" in sys.argv, since, "--universe" in sys.argv, "--universe-only" in sys.argv))
