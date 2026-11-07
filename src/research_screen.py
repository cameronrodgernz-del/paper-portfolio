"""Research screen (rulebook section 5a): a shortlist of overlooked NZX and ASX small and mid caps for the
research desk's deep dives. It is not a buy signal; the history tests showed screens alone don't beat the
market after costs. It narrows thousands of shares to the ones worth reading about.

ASX (Norgate's whole-market prices, ASIC's share counts and short positions, Norgate's index membership):
  ordinary shares outside the S&P/ASX 300, at least two years listed, price at least A$0.10, a median daily
  traded value over 60 sessions between A$10,000 (enough for a A$2,000 position at 10% of two days' volume) and A$2m (too small for most funds);
  market value A$40m to A$1.5bn where ASIC gives a share count; not a live deal target; no placement-pattern
  reopening in the last 30 sessions (section 9).
NZX (FinFeedAPI prices): shares outside the NZX 20 that traded on most days of the last 60 sessions.
Each share gets plain facts to help choose: 12-month return, distance below its 52-week high, dividends paid
over 12 months as a share of the price (from the total-return series, ASX only), daily volatility, short
position (ASIC), and how often it traded. Groups: steady dividend payers, fallen but still paying, others.
Writes reports/research_screen.md and reports/research_screen.csv.
Usage: python3 -I src/research_screen.py <repo_root>
"""
import csv
import math
import os
import statistics as stats
import sys
from collections import defaultdict
from datetime import date, datetime, timezone

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "history"))
from event_tools import asic, code_of  # noqa: E402
from universe import Universe, ready  # noqa: E402

MIN_VALUE, MAX_VALUE = 10_000.0, 2_000_000.0   # A$10,000 floor from 8 Nov 2026 (rulebook 5a change log)
MV_RANGE = (40e6, 1.5e9)


def asx(root: str) -> list[dict]:
    u = Universe(root)
    i = len(u.dates) - 1
    while i > 0 and np.sum(~np.isnan(u.c[i])) < 500:       # the last full session
        i -= 1
    today = u.datestr[i]
    A = asic(root)
    members = {}
    mp = os.path.join(root, "data", "norgate", "index_members.csv")
    for r in csv.DictReader(open(mp, encoding="utf-8")) if os.path.exists(mp) else []:
        if r["index"] == "S&P/ASX 300":
            members[r["symbol"]] = r["member_at_last"] == "1" and r["last_date"] >= u.datestr[i - 5]
    live = set()
    lp = os.path.join(root, "config", "live_deals.csv")
    for r in csv.DictReader(open(lp, encoding="utf-8")) if os.path.exists(lp) else []:
        if r.get("target_market") == "ASX":
            live.add(r["target_ticker"].upper())
    out = []
    with np.errstate(all="ignore"):
        for j, s in enumerate(u.symbols):
            name = (u.sec.get(s, {}).get("name") or "")
            up = name.upper()
            if not u.is_share(s) or any(w in up for w in ("FOREIGN EXEMPT", "DEFERRED", "CAP NOTE", "NOTE ", "NOTES", "HYBRID", "PREF",
                                                           "CONVERTIBLE", "BOND", "PERP")) or "-" in s.split(".")[0]:
                continue
            if np.isnan(u.c[i, j]) and np.isnan(u.c[i - 1, j]):
                continue
            if members.get(s) or code_of(s) in live:
                continue
            first = u.sec.get(s, {}).get("first", "9999")
            if first > f"{int(today[:4]) - 2}{today[4:]}":
                continue
            px = float(u.c[i, j]) if not np.isnan(u.c[i, j]) else float(u.c[i - 1, j])
            if px < 0.10:
                continue
            w = u.value[i - 59: i + 1, j]
            w = w[~np.isnan(w)]
            med = float(np.median(w)) if len(w) else 0.0
            if not (MIN_VALUE <= med <= MAX_VALUE):
                continue
            traded = int(np.sum(~np.isnan(u.c[i - 59: i + 1, j])))
            # placement pattern in the last 30 sessions (section 9)
            has = ~np.isnan(u.c[:, j])
            placement = False
            for k in range(i - 29, i + 1):
                if not has[k]:
                    continue
                g = k - 1
                while g >= 0 and not has[g]:
                    g -= 1
                gap = k - g - 1
                if 1 <= gap <= 3 and g >= 60:
                    vol_med = np.nanmedian(u.v[g - 59: g + 1, j])
                    if u.o[k, j] <= 0.95 * u.c[g, j] and vol_med > 0 and u.v[k, j] >= 3 * vol_med:
                        placement = True
            if placement:
                continue
            shares = None
            rec = A.get(code_of(s))
            short = None
            if rec:
                d, sh, iss = rec
                k = len(d) - 1
                while k >= 0 and d[k] > today:
                    k -= 1
                if k >= 0 and (date.fromisoformat(today) - date.fromisoformat(d[k])).days <= 30 and iss[k] > 0:
                    shares, short = iss[k], sh[k] / iss[k]
            mv = px * shares if shares else None
            if mv is not None and not (MV_RANGE[0] <= mv <= MV_RANGE[1]):
                continue
            a = i - 252
            r12 = float(u.tr[i, j] / u.tr[a, j] - 1) if a >= 0 and not np.isnan(u.tr[a, j]) and not np.isnan(u.tr[i, j]) else None
            p12 = float(u.c[i, j] / u.c[a, j] - 1) if a >= 0 and not np.isnan(u.c[a, j]) and not np.isnan(u.c[i, j]) else None
            div = (r12 - p12) / (1 + p12) if r12 is not None and p12 is not None and p12 > -1 else None
            high = float(np.nanmax(u.c[max(0, i - 251): i + 1, j]))
            daily = u.tr[i - 59: i + 1, j]
            daily = daily[~np.isnan(daily)]
            vol = float(np.std(np.diff(np.log(daily)))) if len(daily) > 10 else None
            out.append({"market": "ASX", "ticker": code_of(s), "name": name.replace(" Ordinary", "").strip(), "price": round(px, 4),
                        "market_value_m": round(mv / 1e6, 1) if mv else "", "median_traded_k": round(med / 1e3, 1),
                        "traded_days_of_60": traded, "return_12m": round(r12, 4) if r12 is not None else "",
                        "below_high": round(px / high - 1, 4) if high else "", "dividends_12m": round(div, 4) if div is not None else "",
                        "volatility": round(vol, 4) if vol else "", "short_pct": round(short, 4) if short is not None else "", "as_of": today})
    return out


def nzx(root: str) -> list[dict]:
    d = os.path.join(root, "data", "prices", "NZX")
    big = set()
    tp = os.path.join(root, "config", "nzx_top20.csv")
    for r in csv.DictReader(open(tp, encoding="utf-8")) if os.path.exists(tp) else []:
        big.add((r.get("ticker") or "").upper())
    names = {}
    mp = os.path.join(root, "config", "nzx_isins.csv")
    for r in csv.DictReader(open(mp, encoding="utf-8")) if os.path.exists(mp) else []:
        names[r["ticker"]] = r.get("name", "")
    live = set()
    lp = os.path.join(root, "config", "live_deals.csv")
    for r in csv.DictReader(open(lp, encoding="utf-8")) if os.path.exists(lp) else []:
        if r.get("target_market") == "NZX":
            live.add(r["target_ticker"].upper())
    out = []
    for f in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        if not f.endswith(".csv"):
            continue
        t = f[:-4]
        if t.upper() in big or t.upper() in live:
            continue
        rows = [r for r in csv.DictReader(open(os.path.join(d, f), encoding="utf-8")) if r.get("close")]
        if len(rows) < 260:
            continue
        last60 = rows[-60:]
        moved = sum(1 for r in last60 if not (r["open"] == r["high"] == r["low"] == r["close"]))
        if moved < 30:
            continue
        px = float(rows[-1]["close"])
        if px < 0.10:
            continue
        p12 = px / float(rows[-253]["close"]) - 1 if len(rows) > 253 and float(rows[-253]["close"]) > 0 else None
        high = max(float(r["close"]) for r in rows[-252:])
        closes = [float(r["close"]) for r in last60 if float(r["close"]) > 0]
        vol = stats.pstdev([math.log(b / a) for a, b in zip(closes, closes[1:])]) if len(closes) > 10 else None
        out.append({"market": "NZX", "ticker": t, "name": names.get(t, ""), "price": px, "market_value_m": "", "median_traded_k": "",
                    "traded_days_of_60": moved, "return_12m": round(p12, 4) if p12 is not None else "", "below_high": round(px / high - 1, 4),
                    "dividends_12m": "", "volatility": round(vol, 4) if vol else "", "short_pct": "", "as_of": rows[-1]["date"]})
    return out


FUND_WORDS = ("INVESTMENT COMPANY", "INVESTMENT CO", "INVESTMENTS LIMITED", "FUND", "INCOME TRUST", "CREDIT INCOME", "CAPITAL INCOME",
              "LONG SHORT", "FUTURE GENERATION", "GLOBAL VALUE", "EMERGING MARKETS", "ABSOLUTE RETURN", "OPPORTUNITIES TRUST")


def group(r: dict) -> str:
    if any(w in (r["name"] or "").upper() for w in FUND_WORDS):
        return "Listed investment companies and trusts (check the discount to net assets)"
    div = r["dividends_12m"] if r["dividends_12m"] != "" else None
    r12 = r["return_12m"] if r["return_12m"] != "" else None
    if div is not None and div >= 0.04 and (r["volatility"] or 1) <= 0.025:
        return "Steady dividend payers"
    if div is not None and div >= 0.03 and r12 is not None and r12 <= -0.25:
        return "Fallen but still paying"
    if r12 is not None and r12 <= -0.40:
        return "Big fallers"
    return "Others"


def main(root: str) -> int:
    rows = (asx(root) if ready(root) else []) + nzx(root)
    for r in rows:
        r["group"] = group(r) if r["market"] == "ASX" else "NZX outside the NZX 20"
    fields = ["group", "market", "ticker", "name", "price", "market_value_m", "median_traded_k", "traded_days_of_60", "return_12m",
              "below_high", "dividends_12m", "volatility", "short_pct", "as_of"]
    os.makedirs(os.path.join(root, "reports"), exist_ok=True)
    with open(os.path.join(root, "reports", "research_screen.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(sorted(rows, key=lambda r: (r["group"], r["market"], r["ticker"])))
    pct = lambda x: f"{x:+.0%}" if isinstance(x, (int, float)) else ""
    L = ["# Research screen", "", f"Run {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC. A shortlist for deep dives (rulebook section 5a), "
         "not a buy list: the history tests showed screens alone don't beat the market after costs.", "",
         f"{sum(1 for r in rows if r['market'] == 'ASX')} ASX shares outside the S&P/ASX 300, tradable at our size and below most funds' "
         f"radar; {sum(1 for r in rows if r['market'] == 'NZX')} NZX shares outside the NZX 20 that trade on most days.", ""]
    for g in ("Steady dividend payers", "Fallen but still paying", "Big fallers", "Others",
              "Listed investment companies and trusts (check the discount to net assets)", "NZX outside the NZX 20"):
        gr = [r for r in rows if r["group"] == g]
        if not gr:
            continue
        gr.sort(key=lambda r: -(r["market_value_m"] or 0) if g != "NZX outside the NZX 20" else r["ticker"])
        L += [f"## {g} ({len(gr)})", "", "| Share | Name | Price | Value (A$m) | Traded a day (A$k) | 12 months | Below high | Dividends, 12 months | Short |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
        for r in gr[:60]:
            L.append(f"| {r['market']}:{r['ticker']} | {r['name'][:40]} | {r['price']} | {r['market_value_m']} | {r['median_traded_k']} | {pct(r['return_12m'])} | "
                     f"{pct(r['below_high'])} | {pct(r['dividends_12m'])} | {pct(r['short_pct']) if r['short_pct'] != '' else ''} |")
        if len(gr) > 60:
            L.append(f"| ... | {len(gr) - 60} more in reports/research_screen.csv | | | | | | | |")
        L.append("")
    L += ["Notes: market value only where ASIC's daily files give a share count; dividends from Norgate's total-return series; "
          "NZX shows price facts only (the feed has no volumes or dividends). Gaming, wagering and racing names wait for Cam's excluded list."]
    open(os.path.join(root, "reports", "research_screen.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"{len(rows)} shares: " + ", ".join(f"{g} {sum(1 for r in rows if r['group'] == g)}" for g in
                                               ("Steady dividend payers", "Fallen but still paying", "Big fallers", "Others", "NZX outside the NZX 20")))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
