"""Company facts for the research screen (rulebook section 5a), pulled from the exchanges' own public pages.

ASX: for each ASX company on the screen, the ASX company header (sector, industry group, market value), the
key statistics (EPS, P/E, total assets and liabilities, enterprise value, revenue and profit for four years,
dividend, yield) and the yearly announcements lists for this year and last (date, time, price sensitive,
headline, document id).
NZX: for each NZX share on the screen, the instrument page's data (market value, shares, P/E, EPS, net tangible
assets per share, dividends over 12 months, gross yield, best bid and offer, value traded) and its dividends.

Light and polite: one request at a time with a pause, an identifying user agent, and a full stop after two
refusals in a row (HTTP 403 or 429). Nothing is retried around a block. Results are cached for six days.
Writes data/research_data/asx_company.json and nzx_company.json.
Usage: python3 -I tools/research_company_data.py <repo_root> [asx|nzx|both] [--limit N]
"""
import csv
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

UA = "paper-portfolio research screen (cameron.rodger.nz@gmail.com)"
PAUSE = 0.8
CACHE_DAYS = 6
FUND_WORDS = re.compile(r"ETF Units|Fund Units|\bETF\b", re.I)


class Refused(Exception):
    pass


def get(url: str, refusals: list) -> str | None:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    time.sleep(PAUSE)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            refusals.clear()
            return r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        if e.code in (403, 429):
            refusals.append(e.code)
            if len(refusals) >= 2:
                raise Refused(f"refused twice in a row (HTTP {e.code}) at {url}")
        return None
    except (urllib.error.URLError, TimeoutError):
        return None


def parse_announcements(page: str) -> list[dict]:
    out = []
    for row in re.findall(r"<tr>(.*?)</tr>", page, re.S):
        m = re.search(r"(\d{2})/(\d{2})/(\d{4})<br>\s*<span class=\"dates-time\">([^<]+)</span>", row)
        a = re.search(r"idsId=(\d+)\">\s*(.*?)<br>", row, re.S)
        if not m or not a:
            continue
        sens = re.search(r'class="pricesens"[^>]*>(.*?)</td>', row, re.S)
        out.append({"date": f"{m.group(3)}-{m.group(2)}-{m.group(1)}", "time": m.group(4).strip(),
                    "sensitive": bool(sens and "<img" in sens.group(1)),
                    "headline": html.unescape(re.sub(r"\s+", " ", a.group(2)).strip()), "id": a.group(1)})
    return out


def fresh(entry: dict | None) -> bool:
    if not entry or "fetched" not in entry:
        return False
    age = datetime.now(timezone.utc) - datetime.fromisoformat(entry["fetched"])
    return age.days < CACHE_DAYS and not entry.get("errors")


def load(path: str) -> dict:
    return json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}


def save(path: str, data: dict) -> None:
    tmp = path + ".tmp"
    json.dump(data, open(tmp, "w", encoding="utf-8"), indent=0, sort_keys=True)
    os.replace(tmp, path)


def screen_tickers(root: str, market: str) -> list[tuple[str, str]]:
    rows = csv.DictReader(open(os.path.join(root, "reports", "research_screen.csv"), encoding="utf-8"))
    return [(r["ticker"], r["name"]) for r in rows if r["market"] == market and not FUND_WORDS.search(r["name"])]


def asx(root: str, out: str, limit: int | None) -> None:
    data = load(out)
    year = datetime.now(timezone.utc).year
    refusals: list = []
    todo = [t for t, _ in screen_tickers(root, "ASX") if not fresh(data.get(t))][:limit]
    print(f"ASX: {len(todo)} companies to fetch")
    for k, t in enumerate(todo, 1):
        e = {"fetched": datetime.now(timezone.utc).isoformat(timespec="seconds"), "errors": []}
        base = f"https://asx.api.markitdigital.com/asx-research/1.0/companies/{t.lower()}"
        for part in ("header", "key-statistics"):
            txt = get(f"{base}/{part}", refusals)
            try:
                e[part] = json.loads(txt)["data"] if txt else None
            except (ValueError, KeyError):
                e[part] = None
            if e[part] is None:
                e["errors"].append(part)
        e["announcements"] = []
        for y in (year, year - 1):
            page = get(f"https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode={t}"
                       f"&timeframe=Y&year={y}", refusals)
            if page is None:
                e["errors"].append(f"announcements {y}")
            else:
                e["announcements"] += parse_announcements(page)
        data[t] = e
        if k % 10 == 0 or k == len(todo):
            save(out, data)
            print(f"  {k}/{len(todo)} ({t})", flush=True)
    save(out, data)


def nzx(root: str, out: str, limit: int | None) -> None:
    data = load(out)
    refusals: list = []
    todo = [t for t, _ in screen_tickers(root, "NZX") if not fresh(data.get(t))][:limit]
    print(f"NZX: {len(todo)} instruments to fetch")
    keep = ("capitalisation", "totalIssue", "peRatio", "earningsPerShare", "ntaPerShare", "gdyPerShare",
            "dividendPerShare12mo", "bestBid", "bestOffer", "closePrice", "closePriceDate", "totalValue",
            "cumulativeValue", "marketValue", "issuerName", "description", "type", "suspensionStatus", "currency")
    for k, t in enumerate(todo, 1):
        e = {"fetched": datetime.now(timezone.utc).isoformat(timespec="seconds"), "errors": []}
        page = get(f"https://www.nzx.com/instruments/{t}", refusals)
        m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', page or "", re.S)
        try:
            pp = json.loads(m.group(1))["props"]["pageProps"] if m else None
        except (ValueError, KeyError):
            pp = None
        if pp is None:
            e["errors"].append("instrument page")
        else:
            ti = (pp.get("instrument") or {}).get("tickerInstrumentInfo") or {}
            ii = (pp.get("instrument") or {}).get("instrumentInfo") or {}
            e["info"] = {key: ti.get(key) for key in keep}
            e["info"]["category"] = ii.get("category")
            e["info"]["firstListedDate"] = ii.get("firstListedDate")
            e["dividends"] = (pp.get("dividends") or {}).get("past", [])
        data[t] = e
        if k % 10 == 0 or k == len(todo):
            save(out, data)
            print(f"  {k}/{len(todo)} ({t})", flush=True)
    save(out, data)


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = args[0]
    which = args[1] if len(args) > 1 else "both"
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None
    d = os.path.join(root, "data", "research_data")
    os.makedirs(d, exist_ok=True)
    try:
        if which in ("asx", "both"):
            asx(root, os.path.join(d, "asx_company.json"), limit)
        if which in ("nzx", "both"):
            nzx(root, os.path.join(d, "nzx_company.json"), limit)
    except Refused as e:
        print(f"Stopped: {e}. Not retrying; the data fetched so far is saved.")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
