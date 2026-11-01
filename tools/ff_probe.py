"""One-off check of FinancialFilings' ASX coverage, using the free monthly credits (about 60 of 500).

Answers, before any money is spent: how far back Australian substantial holder notices and takeover
filings go, year by year; whether companies that delisted years ago still have their filings; and what
the filing titles look like (whether a holder's name can be read from the title alone).
Saves each raw answer to data/financialfilings/probe/ and a summary to data/financialfilings/probe/SUMMARY.md.
The key is read from FINANCIALFILINGS_API_KEY and sent only in the X-API-Key header; it is never written out.
Usage: python3 -I tools/ff_probe.py <out_dir>
"""
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://api.financialreports.eu"
MAX_CALLS = 90                     # hard stop, well inside the 500 free credits
calls = 0


def get(path: str, params: dict | None = None) -> tuple[int, object]:
    global calls
    if calls >= MAX_CALLS:
        return 0, "call budget reached"
    calls += 1
    url = BASE + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, headers={"X-API-Key": os.environ["FINANCIALFILINGS_API_KEY"],
                                               "Accept": "application/json", "User-Agent": "paper-portfolio coverage check"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read().decode("utf-8", errors="replace")
                try:
                    return r.status, json.loads(body)
                except ValueError:
                    return r.status, body[:2000]
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 2:
                time.sleep(5); continue
            return e.code, e.read().decode("utf-8", errors="replace")[:2000]
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt < 2:
                time.sleep(3); continue
            return -1, str(e)[:500]
    return -1, "failed"


def items(body) -> list:
    if isinstance(body, dict):
        return body.get("results") or body.get("data") or []
    if isinstance(body, list):
        # the docs' examples sometimes nest each result in an extra list
        return [x[0] if isinstance(x, list) and x else x for x in body]
    return []


def count_of(body):
    return body.get("count") if isinstance(body, dict) else None


def main(out: str) -> int:
    pdir = os.path.join(out, "probe")
    os.makedirs(pdir, exist_ok=True)
    L = ["# FinancialFilings coverage check", "", f"Run {time.strftime('%Y-%m-%d %H:%M', time.gmtime())} UTC.", ""]

    def save(name, status, body):
        json.dump({"status": status, "body": body}, open(os.path.join(pdir, name + ".json"), "w"), indent=1, default=str)

    # 1. filing types and categories
    st, ft = get("/filing-types/", {"page_size": 500}); save("filing_types", st, ft)
    st2, fc = get("/filing-categories/", {"page_size": 200}); save("filing_categories", st2, fc)
    types = items(ft)
    L += [f"Filing types: status {st}, {len(types)} listed.", ""]
    wanted = {}
    for t in types:
        if not isinstance(t, dict):
            continue
        nm = (t.get("name") or "") + " " + (t.get("code") or "")
        low = nm.lower()
        if any(w in low for w in ("shareholding", "substantial", "m&a", "takeover", "merger", "acquisition", "delist", "director", "trading halt", "strategic review")):
            wanted[t.get("id")] = t.get("name") or t.get("code")
    L += ["| Type id | Name |", "| --- | --- |"] + [f"| {k} | {v} |" for k, v in wanted.items()] + [""]

    # 2. for the two types the tests need, filings per year in Australia (up to 100 a year shown)
    def pick(*words):
        for k, v in wanted.items():
            if any(w in (v or "").lower() for w in words):
                return k, v
        return None, None
    targets = [x for x in (pick("shareholding", "substantial"), pick("m&a", "takeover", "merger")) if x[0] is not None]
    for tid, tname in targets:
        L += [f"## {tname} (type {tid}), Australia", "", "| Year | Status | Filings returned (100 max) | Count reported | First | Last |", "| --- | --- | --- | --- | --- | --- |"]
        for y in range(2010, 2027):
            st, b = get("/filings/", {"countries": "AU", "types": tid, "release_datetime_from": f"{y}-01-01T00:00:00Z",
                                      "release_datetime_to": f"{y}-12-31T23:59:59Z", "page_size": 100, "ordering": "release_datetime"})
            save(f"type{tid}_{y}", st, b)
            rows = items(b)
            dates = sorted((r.get("release_datetime") or "")[:10] for r in rows if isinstance(r, dict))
            L.append(f"| {y} | {st} | {len(rows)} | {count_of(b)} | {dates[0] if dates else ''} | {dates[-1] if dates else ''} |")
        st, b = get("/filings/", {"countries": "AU", "types": tid, "page_size": 10, "ordering": "release_datetime"})
        save(f"type{tid}_earliest", st, b)
        first = [(r.get("release_datetime") or "")[:10] + " " + (r.get("title") or "")[:90] for r in items(b) if isinstance(r, dict)][:3]
        L += ["", "Earliest held: " + ("; ".join(first) or f"none (status {st})"), "", "Sample titles from 2016, 2020 and 2024:", ""]
        for y in (2016, 2020, 2024):
            try:
                rows = items(json.load(open(os.path.join(pdir, f"type{tid}_{y}.json")))["body"])
            except (OSError, KeyError, ValueError):
                rows = []
            for r in rows[:8]:
                if isinstance(r, dict):
                    co = (r.get("company") or {}).get("name", "") if isinstance(r.get("company"), dict) else ""
                    L.append(f"- {(r.get('release_datetime') or '')[:10]} | {co} | {(r.get('title') or '')[:120]} | source type: {r.get('source_filing_type')}")
        L.append("")

    # 3. delisted Australian companies held, and a few deal targets that delisted in different years
    st, b = get("/companies/", {"countries": "AU", "listing_status": "DELISTED", "page_size": 5}); save("au_delisted", st, b)
    st2, b2 = get("/companies/", {"countries": "AU", "listing_status": "LISTED", "page_size": 5}); save("au_listed", st2, b2)
    L += ["## Companies", "", f"Australian companies marked delisted: {count_of(b)} (status {st}); listed: {count_of(b2)} (status {st2}).", "",
          "| Searched for (year it delisted) | Found | Filings returned (10 max) | Earliest filing |", "| --- | --- | --- | --- |"]
    for name, yr in (("Sirtex Medical", 2018), ("Greencross", 2019), ("Mantra Group", 2018), ("Ruralco", 2019), ("Japara Healthcare", 2022),
                     ("Sydney Airport", 2022), ("Crown Resorts", 2022), ("Pacific Smiles", 2025), ("Vocus Group", 2021), ("Healthscope", 2019)):
        st, b = get("/companies/", {"search": name, "countries": "AU", "page_size": 3}); save("co_" + name.replace(" ", "_"), st, b)
        cos = [c for c in items(b) if isinstance(c, dict)]
        if not cos:
            L.append(f"| {name} ({yr}) | no (status {st}) | | |"); continue
        c = cos[0]
        st2, f = get("/filings/", {"company": c.get("id"), "page_size": 10, "ordering": "release_datetime"}); save("filings_" + name.replace(" ", "_"), st2, f)
        rows = [r for r in items(f) if isinstance(r, dict)]
        L.append(f"| {name} ({yr}) | {c.get('name')} (id {c.get('id')}) | {len(rows)} | {(rows[0].get('release_datetime') or '')[:10] if rows else ''} |")

    st, b = get("/usage/"); save("usage", st, b)
    L += ["", f"Requests made: {calls}. Usage endpoint: status {st}."]
    open(os.path.join(pdir, "SUMMARY.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    if not os.environ.get("FINANCIALFILINGS_API_KEY"):
        sys.exit("FINANCIALFILINGS_API_KEY is not set")
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data/financialfilings"))
