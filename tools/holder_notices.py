"""Reads every substantial holder notice lodged on the ASX for the companies on the research screen, and flags
holders that aren't funds (private companies, families, trade buyers) whose stake has been rising across notices.
Added 9 Nov 2026, after Saunders: Ahrens Group had built 16.2% over 16 months in notices that are mostly scanned
images, which a search of announcement text can't see.

What it does:
  1. For each ASX company in reports/research_screen.csv, lists its announcements for each calendar year from
     --since (the ASX's announcements.do pages) and keeps the substantial holder notices (forms 603, 604, 605).
  2. Reads each notice it hasn't read before: the first three pages as text, or by OCR (pdftoppm and tesseract)
     when the PDF is a scan. Each notice is parsed for the holder's name, the date of change and the voting power
     before and after. Results are cached in data/research_data/holder_notices.csv, keyed on the ASX document id,
     so a weekly run only reads new notices.
  3. Groups notices by company and holder, classes each holder as a fund or not (a name list, below), and writes
     data/research_data/holder_builds.csv and reports/holder_builds.md: the holders that aren't funds whose
     latest stake is 7% or more, at least two points above their first notice in the window, and still held.

Parsing is approximate: OCR misreads names and numbers, so every flag is a pointer to read the notices, not a fact.
Downloads go to a scratch folder outside the repo and are only read with pdftotext and tesseract.

Usage:
  python3 -I tools/holder_notices.py ROOT [--since 2024-11-01] [--workers 4] [--scratch /tmp/holder_notices]
  python3 -I tools/holder_notices.py ROOT --report-only [--reparse]
"""
import csv
import html
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import date

UA = "paper-portfolio research"
LIST_URL = "https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode={code}&timeframe=Y&year={year}"
DOC_URL = "https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId={ids}"
HEADLINE = re.compile(r"substantial\s+hold", re.I)
CACHE_COLS = ["market", "ticker", "ids_id", "ann_date", "headline", "form", "holder", "change_date", "prev_pct", "pct",
              "text_chars", "ocr", "status"]

# Names that mark a holder as a fund, bank, custodian or other institution (upper case, matched as substrings).
FUNDS = [
    "ASSET MANAGEMENT", "INVESTMENT MANAGEMENT", "FUNDS MANAGEMENT", "FUND MANAGEMENT", "CAPITAL MANAGEMENT",
    "INVESTMENT MANAGERS", "INVESTORS MUTUAL", "WEALTH", "SUPERANNUATION", "SUPER FUND", "PENSION", "NOMINEES",
    "CUSTODIAN", "CUSTODY", "SECURITIES LENDING", "TRUSTEE SERVICES", "RESPONSIBLE ENTITY", "SUBSTANTIAL HOLDERS",
    "REGAL", "PERPETUAL", "NAOS", "MICROEQUITIES", "SPHERIA", "THORNEY", "WILSON ASSET", "WAM ", "PARADICE",
    "FIDELITY", "VANGUARD", "BLACKROCK", "STATE STREET", "DIMENSIONAL", "UBS", "MORGAN STANLEY", "CITIGROUP",
    "CITICORP", "J.P. MORGAN", "JPMORGAN", "JP MORGAN", "MACQUARIE", "GOLDMAN", "BANK OF AMERICA", "MERRILL",
    "HSBC", "MITSUBISHI UFJ", "MUFG", "MIZUHO", "NOMURA", "CREDIT SUISSE", "BARCLAYS", "BNP PARIBAS", "SOCIETE",
    "DEUTSCHE", "ALLAN GRAY", "OPHIR", "FIRETRAIL", "SANDON", "ELLERSTON", "TRIBECA", "PINNACLE", "AUSBIL",
    "CELESTE", "ACORN CAPITAL", "ELEY GRIFFITHS", "GANES", "AUSTRALIAN ETHICAL", "LAZARD", "SCHRODER", "PENDAL",
    "PERENNIAL", "SMALLCO", "RENAISSANCE", "FORAGER", "CYAN", "BENNELONG", "HYPERION", "SELECTOR", "ARGO",
    "AUSTRALIAN FOUNDATION", "MIRRABOOKA", "DJERRIWARRH", "CADENCE", "SIGNATURE", "SG HISCOCK", "QVG", "TYNDALL",
    "NIKKO", "COLONIAL FIRST STATE", "FIRST SENTIER", "AUSTRALIANSUPER", "AWARE SUPER", "HOSTPLUS", "UNISUPER",
    "CBUS", "HESTA", "REST ", "IFM ", "MLC ", "INSIGNIA", "AMP ", "NATIONAL AUSTRALIA BANK", "COMMONWEALTH BANK",
    "WESTPAC", "ANZ ", "BELL POTTER", "CANACCORD", "MORGANS", "SHAW AND PARTNERS", "EUROZ", "CLIME", "AIRLIE",
    "PLATO", "PROSPERITY", "SALTER", "LANYON", "TOPHAT", "WAVESTONE", "ALPHINITY", "SOLARIS", "MAN GROUP",
    "CITADEL", "MILLENNIUM", "SUSQUEHANNA", "JANE STREET", "INVESCO", "FRANKLIN", "T. ROWE", "T ROWE", "NORGES",
    "GOVERNMENT OF SINGAPORE", "GIC ", "TEMASEK", "CAPITAL GROUP", "NORTHERN TRUST", "ABERDEEN", "ABRDN",
    "LIONTRUST", "JUPITER", "BAILLIE GIFFORD", "WELLINGTON", "NEUBERGER", "MONDRIAN", "KAIROS", "MONASH INVESTORS",
    "DNR CAPITAL", "WATERMARK", "LHC CAPITAL", "1851", "NATIXIS", "AMUNDI", "LEGAL & GENERAL", "ROYAL LONDON",
    "MAWER", "SCHONFELD", "ACADIAN", "GEODE", "CHARLES SCHWAB", "EQUITY TRUSTEES", "ONE MANAGED", "MELBOURNE TRUST",
    "LIM ADVISORS", "SPRINGTOWN", "HAREWOOD", "ORBIS", "COOPER INVESTORS", "AUSTRALIAN UNITED", "BKI ",
    "HOST-PLUS", "HOST PLUS", "TANARRA", "VIBURNUM", " FUNDS ", "MA FINANCIAL", "COPIA", "INVESTMENT PARTNERS",
    "PILGRIM", "MUTUAL TRUST", "CAPITAL PARTNERS", "PRIVATE EQUITY", "VENTURE", "OAKTREE", "BAIN CAPITAL", "KKR",
    "TPG", "CARLYLE", "BLACKSTONE", "APOLLO", "PACIFIC EQUITY", "ADAMANTEM", "QUADRANT", "ANACACIA", "ROYAL BANK",
    "TORONTO DOMINION", "CREDIT AGRICOLE", "SAMSON ROCK", "NAVIGATOR", "BRIDGEWATER", "EMINENT", "WARAKIRRI",
    "MERCER", "NOVA SCOTIA", "L1 CAPITAL", "HUB24", "MAYBANK", "RYDER CAPITAL", "IOLITE", "BGH CAPITAL", "TIGA",
    "THORNEY", "SECURITIES PTE", "SECURITIES LIMITED", "BANK ", "BANKING", "UDN ", " FIL LIMITED", "SPROTT", "TEES RIVER",
]
NOISE = re.compile(r"^(\W|annexure|listed in|see |entity listed|nfp|nfpfrn|entities\)|group entity|fund;|ltd\.|management limited$|"
                   r"travel limited$|associates)|personal use|if applicable", re.I)  # a parse that missed the name


def run(cmd, timeout=60):
    return subprocess.run(cmd, capture_output=True, timeout=timeout)


def curl(url, out=None, timeout=60):
    cmd = ["curl", "-sSL", "--max-time", str(timeout), "-A", UA, url]
    if out:
        cmd += ["-o", out]
    r = run(cmd, timeout=timeout + 10)
    return r.stdout if not out else (r.returncode == 0)


def list_notices(code, years, pattern=None):
    """The announcements whose headline matches pattern (default: substantial holder notices) on the ASX's yearly
    announcement pages for one code."""
    pattern = pattern or HEADLINE
    found = []
    for y in years:
        try:
            page = curl(LIST_URL.format(code=code, year=y)).decode("utf-8", "ignore")
        except Exception:
            continue
        for m in re.finditer(r"<tr>(.*?)</tr>", page, re.S):
            row = m.group(1)
            ids = re.search(r"idsId=(\d+)", row)
            if not ids:
                continue
            text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", row))).strip()
            d = re.match(r"(\d{2})/(\d{2})/(\d{4})", text)
            if not d or not pattern.search(text):
                continue
            ann = f"{d.group(3)}-{d.group(2)}-{d.group(1)}"
            head = re.sub(r"^\d{2}/\d{2}/\d{4}\s+\d{1,2}:\d{2}\s*[ap]m\s+", "", text)
            head = re.sub(r"\s+\d+\s+pages?\s+[\d.]+\s*[KM]B\s*$", "", head)
            found.append({"ids_id": ids.group(1), "ann_date": ann, "headline": head})
        time.sleep(0.2)
    return found


def other_code(headline, ticker):
    m = re.search(r"\b(?:for|in)\s+([A-Z0-9]{3})\b", headline)
    return bool(m) and m.group(1) != ticker


def read_pdf(ids, scratch):
    """Text of the notice's first three pages, by OCR if the PDF is a scan. Returns (text, chars, ocr)."""
    page = os.path.join(scratch, f"a_{ids}.html")
    pdf = os.path.join(scratch, f"n_{ids}.pdf")
    if not os.path.exists(pdf):
        if not curl(DOC_URL.format(ids=ids), out=page):
            return "", 0, False
        h = open(page, encoding="utf-8", errors="ignore").read()
        m = re.search(r'name="pdfURL" value="([^"]+)"', h)
        if not m or not curl(m.group(1), out=pdf):
            return "", 0, False
    r = run(["pdftotext", "-layout", "-l", "3", pdf, "-"])
    text = r.stdout.decode("utf-8", "ignore")
    body = re.sub(r"For personal use only|\s", "", text)
    if len(body) >= 300:
        return text, len(body), False
    base = os.path.join(scratch, f"o_{ids}")
    run(["pdftoppm", "-r", "150", "-png", "-l", "2", pdf, base], timeout=120)
    parts = []
    for f in sorted(x for x in os.listdir(scratch) if x.startswith(f"o_{ids}") and x.endswith(".png")):
        o = run(["tesseract", os.path.join(scratch, f), "-"], timeout=120)
        parts.append(o.stdout.decode("utf-8", "ignore"))
    text = "\n".join(parts)
    return text, len(re.sub(r"\s", "", text)), True


def parse(text, headline):
    t = text.replace("\r", "")
    h = headline.lower()
    form = "605" if "ceas" in h else ("603" if "becom" in h else "604")
    if re.search(r"Form\s*605|ceased to be a substantial holder", t, re.I):
        form = "605"
    elif re.search(r"Form\s*603|became a substantial holder", t, re.I) and form != "605":
        form = "603"
    holder = ""
    start = re.search(r"Details of substantial holder", t, re.I)
    lines = [x.strip(" |\t") for x in t[start.end() if start else 0:].split("\n")]
    for i, s in enumerate(lines[:40]):
        if re.search(r"Company Name|Name/Scheme|Name and ACN|Name\s+Address|Name\s+Nature|scheme name|fund name", s, re.I):
            continue
        m = re.match(r"^Name\b\s*[:\-]?\s*(.*)$", s)
        if not m:
            continue
        cand = m.group(1).strip()
        if len(cand) < 3:  # the name is on the next line with text
            cand = next((x for x in lines[i + 1:i + 6] if x and not re.match(
                r"ACN|ARSN|ABN|\(if applicable\)|There was|The holder|The previous|To Company|\d", x, re.I)), "")
        holder = re.split(r"\s{3,}|ACN|ABN|ARSN", cand)[0].strip(" .,:;|")
        if len(holder) >= 3:
            break
        holder = ""
    if not holder:
        m = re.search(r"substantial hold\w*\s*[-:]\s*(.+)$", headline, re.I)
        holder = m.group(1).strip() if m else ""
    cd = ""
    m = re.search(r"(?:substantial holder on|became a substantial holder on|ceased to be a substantial holder on)"
                  r".{0,200}?([0-9]{1,2})\s*[/.\-]\s*([0-9]{1,2})\s*[/.\-]\s*([0-9]{4}|[0-9]{2}\b)", t, re.I | re.S)
    if m:
        dd, mm, yy = m.groups()
        yy = ("20" + yy) if len(yy) == 2 else yy
        try:
            cd = date(int(yy), int(mm), int(dd)).isoformat()
        except ValueError:
            cd = ""
    sec = t
    a = re.search(r"2\.\s*(?:Previous and present voting power|Details of voting power)", t, re.I)
    b = re.search(r"\n\s*3\.\s*(?:Changes in relevant|Details of relevant|Changes)", t, re.I)
    if a:
        sec = t[a.end(): b.start() if b and b.start() > a.end() else a.end() + 2500]
    pcts = [float(x) for x in re.findall(r"(?<![\d.,])(\d{1,3}(?:\.\d{1,8})?)\s?%", sec) if 0 < float(x) <= 100]
    prev = pct = ""
    if form == "605":
        pct = "0"
    elif pcts:
        pct = f"{pcts[-1]:.2f}"
        if form == "604" and len(pcts) >= 2:
            prev = f"{pcts[0]:.2f}"
    return {"form": form, "holder": holder, "change_date": cd, "prev_pct": prev, "pct": pct}


def is_fund(name):
    n = " " + re.sub(r"[^A-Z0-9&. ]", " ", name.upper()) + " "
    return any(f in n for f in FUNDS)


def key(name):
    n = re.sub(r"[^A-Z0-9 ]", " ", name.upper())
    n = re.sub(r"\b(PTY|PROPRIETARY|LTD|LIMITED|LIMTED|THE|AS|TRUSTEE|ATF|FOR|AND|ITS|ASSOCIATES|ASSOCIATED|ENTITIES|ACN|INC|LLC|LP)\b", " ", n)
    w = n.split()
    return " ".join(w[:2]) if w else ""


def load_cache(p):
    if not os.path.exists(p):
        return {}
    return {r["ids_id"]: r for r in csv.DictReader(open(p, encoding="utf-8"))}


def save_cache(p, cache):
    rows = sorted(cache.values(), key=lambda r: (r["ticker"], r["ann_date"], r["ids_id"]))
    with open(p, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CACHE_COLS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def builds(root, cache, names):
    """Holders that aren't funds, with a rising stake, still held. Returns rows sorted by latest stake."""
    groups = {}
    for r in cache.values():
        if r["status"] != "ok" or not r["holder"]:
            continue
        comp = names.get(r["ticker"], "").upper()
        k = key(r["holder"])
        if not k or (comp and k.split()[0] in comp.split()[:1]):
            continue  # the company's own escrow or buy-back notices
        groups.setdefault((r["ticker"], k), []).append(r)
    out = []
    for (t, k), rs in groups.items():
        rs.sort(key=lambda r: (r["change_date"] or r["ann_date"], r["ann_date"]))
        holder = max((r["holder"] for r in rs), key=len)
        if is_fund(holder) or NOISE.search(holder):
            continue
        held = [r for r in rs if r["form"] != "605" and r["pct"]]
        if not held or rs[-1]["form"] == "605":
            continue
        first = next((float(r["prev_pct"]) for r in held if r["prev_pct"]), float(held[0]["pct"]))
        if held[0]["form"] == "603":
            first = min(first, float(held[0]["pct"]))
        last = float(held[-1]["pct"])
        rises = sum(1 for a, b in zip(held, held[1:]) if float(b["pct"]) > float(a["pct"]))
        if last >= 7 and last - first >= 2 and len(held) >= 2:
            out.append({"ticker": t, "company": names.get(t, ""), "holder": holder, "first_pct": f"{first:.2f}",
                        "last_pct": f"{last:.2f}", "notices": len(rs), "rises": rises,
                        "first_date": held[0]["change_date"] or held[0]["ann_date"],
                        "last_date": held[-1]["change_date"] or held[-1]["ann_date"],
                        "ocr": "yes" if any(str(r["ocr"]) == "True" for r in rs) else "no",
                        "ids": " ".join(r["ids_id"] for r in rs)})
    out.sort(key=lambda r: (-float(r["last_pct"]), r["ticker"]))
    return out


DIRECTOR = re.compile(r"director'?s?'?\s+interest|appendix\s+3[xyz]\b", re.I)
STREET = re.compile(r"\b(\d{1,5}(?:\s*[-–]\s*\d{1,5})?)\s+((?:[A-Z][A-Za-z']+\s+){1,3}?)"
                    r"(Street|St|Road|Rd|Avenue|Ave|Parade|Pde|Place|Pl|Lane|Drive|Dr|Terrace|Tce|Highway|Hwy|"
                    r"Boulevard|Blvd|Way|Square|Sq|Circuit|Cct|Crescent|Cres|Court|Ct|Quay|Esplanade)\b")
ABBR = {"street": "st", "road": "rd", "avenue": "ave", "parade": "pde", "place": "pl", "drive": "dr", "terrace": "tce",
        "highway": "hwy", "boulevard": "blvd", "square": "sq", "circuit": "cct", "crescent": "cres", "court": "ct"}


def director_names(text):
    """Directors named in an Appendix 3X, 3Y or 3Z ("Name of Director  Tony Robert Pitt")."""
    out = []
    for m in re.finditer(r"[Nn]ame of [Dd]irector\s*[:\-]?\s*([A-Z][A-Za-z.'\- ]{3,60})", text):
        n = re.split(r"\s{3,}|\bABN\b|\bACN\b", m.group(1).strip())[0].strip(" .")
        w = n.split()
        if 2 <= len(w) <= 6 and not re.search(r"Limited|Ltd|Group|Holdings|Trust|Pty", n, re.I):
            out.append(n)
    return out


def addresses(text):
    """Street addresses in a notice, normalised ("22-24 junction st"), from section 6 on if there is one."""
    m = re.search(r"\n\s*(?:6|7)\.?\s*Addresses", text, re.I)
    part = text[m.end():] if m else text
    out = set()
    for a in STREET.finditer(part):
        num = re.sub(r"\s", "", a.group(1)).replace("–", "-")
        kind = ABBR.get(a.group(3).lower(), a.group(3).lower())
        out.add(f"{num} {' '.join(a.group(2).split()).lower()} {kind}")
    return out


def name_in(full, text):
    """A director's name in a notice: the first and last names within 40 characters, in that order."""
    w = [x for x in re.split(r"[\s.]+", full) if x]
    if len(w) < 2 or len(w[-1]) < 3:
        return False
    return bool(re.search(re.escape(w[0]) + r"\b.{0,40}?\b" + re.escape(w[-1]) + r"\b", text, re.I | re.S))


def link_notes(holder, holder_text, others, director_texts):
    """Why a holder looks linked to the board or to another holder, or "" if nothing found.
    holder_text: the text of its notices; others: {other holder: set of addresses}; director_texts: 3X/3Y/3Z texts."""
    notes = []
    names = sorted({n for t in director_texts for n in director_names(t)})
    hit = [n for n in names if name_in(n, holder_text)]
    if hit:
        notes.append("names director " + ", ".join(hit[:2]))
    k = key(holder)
    if len(k) >= 5 and any(k in re.sub(r"[^A-Z0-9 ]", " ", t.upper()) for t in director_texts):
        notes.append("named in a director's notice")
    mine = addresses(holder_text)
    shared = sorted(o for o, a in others.items() if mine & a)
    if shared:
        notes.append("same address as " + "; ".join(x[:40] for x in shared[:2]))
    return "; ".join(notes)


def add_links(rows, cache, scratch, years, workers):
    """Adds a "linked" note to each build: whether the holder names a director, is named in a director's interest
    notice, or shares an address with another holder that isn't a fund. Reads the director notices for those
    companies only (up to 15 a company, text layer only) and the holder notices already in the scratch folder."""
    def text_of(ids):  # text layer only, first eight pages (annexures included); scans give ""
        pdf = os.path.join(scratch, f"n_{ids}.pdf")
        if not os.path.exists(pdf):
            return ""
        return run(["pdftotext", "-layout", "-l", "8", pdf, "-"]).stdout.decode("utf-8", "ignore")

    def dir_texts(t):
        found = list_notices(t, years, DIRECTOR)[-15:]
        out = []
        for a in found:
            pdf = os.path.join(scratch, f"n_{a['ids_id']}.pdf")
            if not os.path.exists(pdf):
                page = os.path.join(scratch, f"a_{a['ids_id']}.html")
                if not curl(DOC_URL.format(ids=a["ids_id"]), out=page):
                    continue
                m = re.search(r'name="pdfURL" value="([^"]+)"', open(page, encoding="utf-8", errors="ignore").read())
                if not m or not curl(m.group(1), out=pdf):
                    continue
            r = run(["pdftotext", "-layout", "-l", "2", pdf, "-"])
            out.append(r.stdout.decode("utf-8", "ignore"))
        return t, out
    tickers = sorted({r["ticker"] for r in rows})
    with ThreadPoolExecutor(workers) as ex:
        dirs = dict(ex.map(dir_texts, tickers))
    for r in rows:
        t = r["ticker"]
        mine = set(r["ids"].split())
        htext = "\n".join(text_of(i) for i in mine)
        others = {}
        for c in cache.values():
            if c["ticker"] != t or c["ids_id"] in mine or not c["holder"] or is_fund(c["holder"]) or str(c["ocr"]) == "True":
                continue
            if key(c["holder"]) == key(r["holder"]) or NOISE.search(c["holder"]) or len(key(c["holder"])) < 4:
                continue
            ot = text_of(c["ids_id"])
            k1 = key(r["holder"]).split()
            probe = k1[0] if k1 and len(k1[0]) >= 6 else " ".join(k1)
            if probe and probe in re.sub(r"[^A-Z0-9 ]", " ", ot.upper()):
                continue  # the other notice names this holder (a seller naming its buyer), so its address isn't shared
            a = addresses(ot)
            if a:
                others.setdefault(c["holder"], set()).update(a)
        r["linked"] = link_notes(r["holder"], htext, others, dirs.get(t, []))
    return rows


def write_report(root, rows, n_notices, n_companies, since, today):
    p = os.path.join(root, "data", "research_data", "holder_builds.csv")
    cols = ["ticker", "company", "holder", "first_pct", "last_pct", "notices", "rises", "first_date", "last_date", "ocr",
            "linked", "ids"]
    with open(p, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows({c: r.get(c, "") for c in cols} for r in rows)
    head = "| Share | Holder | From | To | Notices | Rises | First | Latest | OCR |"
    rule = "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"
    lines = [f"# Holders building stakes, {today}", "",
             f"From {n_notices} substantial holder notices lodged since {since} for {n_companies} ASX companies on the research "
             "screen (tools/holder_notices.py). Listed: holders that aren't funds (by a name list), whose latest stake is 7% or "
             "more and at least two points above where the window starts, and who haven't ceased. Notices that are scanned "
             "images were read by OCR, so names and figures can be misread: each line is a pointer to read the notices, not "
             "a fact. This is a simulation and not financial advice.", "",
             "Each build is checked for links to the board or to another holder: a director's name in the holder's notices, "
             "the holder named in a director's interest notice, or the same street address as another holder that isn't a "
             "fund. A linked holder can usually take control without paying other holders a premium (TOT and EGH, Nov "
             "2026), so outside buyers come first. Scanned notices can't be checked this way, so no link found isn't proof "
             "of none.", ""]
    sections = [("Outside buyers below 50% (building toward control, or a blocking stake):",
                 [r for r in rows if float(r["last_pct"]) < 50 and not r.get("linked")]),
                ("Linked to the board or another holder, below 50%:",
                 [r for r in rows if float(r["last_pct"]) < 50 and r.get("linked")]),
                ("50% or more (a controller still buying):", [r for r in rows if float(r["last_pct"]) >= 50])]
    for title, rs in sections:
        if not rs:
            continue
        lines += [title, "", head, rule]
        for r in rs:
            who = r["holder"][:45] + (f" ({r['linked']})" if r.get("linked") else "")
            lines.append(f"| ASX:{r['ticker']} ({r['company'][:30]}) | {who} | {r['first_pct']}% | {r['last_pct']}% | "
                         f"{r['notices']} | {r['rises']} | {r['first_date']} | {r['last_date']} | {r['ocr']} |")
        lines.append("")
    open(os.path.join(root, "reports", "holder_builds.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")


def main(argv):
    root = argv[1]
    since = argv[argv.index("--since") + 1] if "--since" in argv else "2024-11-01"
    workers = int(argv[argv.index("--workers") + 1]) if "--workers" in argv else 4
    scratch = argv[argv.index("--scratch") + 1] if "--scratch" in argv else "/tmp/holder_notices"
    os.makedirs(scratch, exist_ok=True)
    screen = [r for r in csv.DictReader(open(os.path.join(root, "reports", "research_screen.csv"), encoding="utf-8"))
              if r["market"] == "ASX"]
    names = {r["ticker"]: r["name"] for r in screen}
    if "--only" in argv:  # for testing on a few codes
        keep = set(argv[argv.index("--only") + 1].split(","))
        names = {t: n for t, n in names.items() if t in keep}
    cpath = os.path.join(root, "data", "research_data", "holder_notices.csv")
    cache = load_cache(cpath)
    today = date.today().isoformat()
    if "--report-only" not in argv:
        years = list(range(int(since[:4]), date.today().year + 1))
        todo = {}

        def lst(t):
            return t, list_notices(t, years)
        with ThreadPoolExecutor(workers) as ex:
            for t, found in ex.map(lst, sorted(names)):
                for a in found:
                    if a["ann_date"] >= since and not other_code(a["headline"], t) and a["ids_id"] not in cache:
                        todo[a["ids_id"]] = dict(a, market="ASX", ticker=t)
        print(f"listed: {len(todo)} new notices to read", flush=True)

        def rd(item):
            ids, a = item
            try:
                text, chars, ocr = read_pdf(ids, scratch)
                res = parse(text, a["headline"]) if chars else {"form": "", "holder": "", "change_date": "", "prev_pct": "", "pct": ""}
                status = "ok" if chars else "no text"
            except Exception as e:  # keep going; the notice is retried next run
                return ids, None
            return ids, dict(a, **res, text_chars=chars, ocr=ocr, status=status)
        done = 0
        with ThreadPoolExecutor(workers) as ex:
            for ids, row in ex.map(rd, list(todo.items())):
                if row:
                    cache[ids] = {c: row.get(c, "") for c in CACHE_COLS}
                done += 1
                if done % 100 == 0:
                    save_cache(cpath, cache)
                    print(f"read {done} of {len(todo)}", flush=True)
        save_cache(cpath, cache)
    if "--reparse" in argv:  # re-read text-layer notices already in the scratch folder (OCR results are kept)
        n = 0
        for ids, r in cache.items():
            pdf = os.path.join(scratch, f"n_{ids}.pdf")
            if str(r.get("ocr")) == "True" or not os.path.exists(pdf):
                continue
            text, chars, ocr = read_pdf(ids, scratch)
            if chars and not ocr:
                r.update(parse(text, r["headline"])); n += 1
        save_cache(cpath, cache)
        print(f"re-parsed {n} notices", flush=True)
    rows = builds(root, cache, names)
    if "--no-links" not in argv:
        rows = add_links(rows, cache, scratch, list(range(int(since[:4]), date.today().year + 1)), workers)
        print(f"linked: {sum(1 for r in rows if r.get('linked'))} of {len(rows)} builds", flush=True)
    write_report(root, rows, len(cache), len(names), since, today)
    print(f"holder builds: {len(rows)} from {len(cache)} notices", flush=True)


if __name__ == "__main__":
    main(sys.argv)
