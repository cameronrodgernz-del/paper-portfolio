"""Checks for the substantial holder notice reader (tools/holder_notices.py) and its tag in the weekly sweep."""
import csv
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.join(ROOT, "src"))
import holder_notices as h  # noqa: E402

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail and not ok else ""))
    if not ok:
        FAILS.append(name)


# A text-layer 604 (layout as pdftotext gives it)
T604 = """Form 604
Notice of change of interests of substantial holder
To Company Name/Scheme   Saunders International Limited
ACN/ARSN 050 287 431
1. Details of substantial holder(1)
Name                                   Ahrens Group Pty Ltd
ACN/ARSN (if applicable)   114 260 230
There was a change in the interests of the
substantial holder on                          14/01/2026
2. Previous and present voting power
Class of securities (4) Previous notice Present notice
Person's votes Voting power (5) Person's votes Voting power (5)
full paid ordinary 17,272,815 12.8% 18,223,815 13.1%
3. Changes in relevant interests
"""
r = h.parse(T604, "Change in substantial holding")
check("604 holder", r["holder"] == "Ahrens Group Pty Ltd", r)
check("604 date", r["change_date"] == "2026-01-14", r)
check("604 before and after", (r["prev_pct"], r["pct"]) == ("12.80", "13.10"), r)

# An OCR'd 603: the name and the date sit on later lines
T603 = """To Company Name/Scheme

Saunders International Ltd

1, Details of substantial holder (1)

Name

Ahrens Group Pty Ltd

ACN/ARSN (if applicable)

The holder became a substantial holder on

2. Details of voting power

02/12/2024

Class of securities (4) Number of securities Person's votes (5) Voting power (6)
Ordinary 6,333,000 6,333,000 5.34%
3. Details of relevant interests
"""
r = h.parse(T603, "Becoming a substantial holder")
check("603 holder from the next line", r["holder"] == "Ahrens Group Pty Ltd", r)
check("603 date across lines", r["change_date"] == "2024-12-02", r)
check("603 stake", (r["form"], r["pct"]) == ("603", "5.34"), r)

r = h.parse(T604.replace("12.8% 18,223,815 13.1%", "5.298524% 18,223,815 6.323057%"), "Change in substantial holding")
check("long decimals aren't cut into small numbers", (r["prev_pct"], r["pct"]) == ("5.30", "6.32"), r)

r = h.parse("Form 605\nNotice of ceasing to be a substantial holder\n1. Details of substantial holder(1)\nName  NAOS Asset Management\n",
            "Ceasing to be a substantial holder")
check("605 is a nil stake", (r["form"], r["pct"]) == ("605", "0"), r)
check("a headline name is the fallback", h.parse("no form text", "Change in substantial holding - Harcourt")["holder"] == "Harcourt")
check("funds are recognised", h.is_fund("NAOS Substantial Holders referred to in Annexure A") and h.is_fund("Regal Partners Limited"))
check("a family company is not a fund", not h.is_fund("Ahrens Group Pty Ltd"))
check("another company's code is skipped", h.other_code("Ceasing to be a substantial holder for MMA", "MGX")
      and not h.other_code("Change in substantial holding", "SND"))

# builds(): a rising non-fund holder is flagged; a fund, a ceased holder and the company's own escrow are not
rows = {}


def add(i, t, holder, form, cd, prev, pct):
    rows[str(i)] = {"market": "ASX", "ticker": t, "ids_id": str(i), "ann_date": cd, "headline": "", "form": form,
                    "holder": holder, "change_date": cd, "prev_pct": prev, "pct": pct, "text_chars": "500", "ocr": "False",
                    "status": "ok"}


add(1, "SND", "Ahrens Group Pty Ltd", "603", "2024-12-02", "", "5.34")
add(2, "SND", "Ahrens Group Pty Ltd", "604", "2025-07-17", "9.90", "13.40")
add(3, "SND", "AHRENS GROUP PTY. LTD.", "604", "2026-03-30", "13.10", "16.20")
add(4, "SND", "NAOS Asset Management", "604", "2026-08-28", "9.99", "11.04")
add(5, "SND", "Saunders International Limited", "603", "2025-11-25", "", "6.75")
add(6, "XYZ", "Smith Family Pty Ltd", "604", "2025-01-01", "5.0", "9.0")
add(7, "XYZ", "Smith Family Pty Ltd", "605", "2025-06-01", "", "0")
out = h.builds(ROOT, rows, {"SND": "Saunders International Limited", "XYZ": "Xyz Limited"})
check("only the rising trade holder is flagged", [(b["ticker"], b["last_pct"]) for b in out] == [("SND", "16.20")], out)
check("the build starts at the first notice", out and out[0]["first_pct"] == "5.34", out)

# The sweep tags a build
import research_sweep as s  # noqa: E402
with tempfile.TemporaryDirectory() as d:
    os.makedirs(os.path.join(d, "reports")); os.makedirs(os.path.join(d, "data", "research_data"))
    os.makedirs(os.path.join(d, "research", "picks"))
    open(os.path.join(d, "research", "picks", "INDEX.md"), "w").write("| Ticker | Name | Date | Verdict | Status | Next |\n")
    with open(os.path.join(d, "reports", "research_screen.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["group", "market", "ticker", "name", "price", "market_value_m", "median_traded_k", "traded_days_of_60",
                    "return_12m", "below_high", "dividends_12m", "volatility", "short_pct", "as_of"])
        w.writerow(["x", "ASX", "SND", "Saunders International Limited", "0.725", "102", "11", "60", "-0.2", "-0.35", "0", "0.03", "", "2026-11-09"])
    with open(os.path.join(d, "data", "research_data", "holder_builds.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
    s.main(d, "2026-11-09")
    rep = open(os.path.join(d, "reports", "research_sweep.md"), encoding="utf-8").read()
    check("the sweep tags the build", "building a stake (5.34% to 16.20%" in rep, rep[-600:])

# Links to the board or another holder (added 10 Nov 2026 after TOT and EGH)
D3Y = """Appendix 3Y
Change of Director's Interest Notice
Name of entity     360 Capital REIT
Name of Director                              Tony Robert Pitt
Date of last notice 23 October 2026
Nature of indirect interest   TT Investments Pty Limited as trustee for
360 Capital Equity Co-investment Trust (CECT)
"""
check("director name from a 3Y", h.director_names(D3Y) == ["Tony Robert Pitt"], h.director_names(D3Y))
TOT604 = """1. Details of substantial holder
Name TT Investments Pty Limited and Tony Robert Pitt
6. Addresses
TT Investments Pty Limited   Level 8, 56 Pitt Street, Sydney NSW 2000
"""
note = h.link_notes("TT Investments Pty Limited", TOT604, {}, [D3Y])
check("holder names a director", "names director Tony Robert Pitt" in note, note)
check("holder named in a director's notice", "named in a director's notice" in note, note)
check("a street isn't a director's name", not h.name_in("Tony Robert Pitt", "Level 8, 56 Pitt Street"), "")
FIL = """6. Addresses
Filetron and each member of the Filetron Group   22-24 Junction Street, Forest Lodge NSW 2037"""
DMC = """7. Addresses
DMC and each member of the DMC group 22-24 Junction St Forest Lodge NSW 2037"""
check("addresses normalise", h.addresses(FIL) == h.addresses(DMC) == {"22-24 junction st"}, (h.addresses(FIL), h.addresses(DMC)))
note = h.link_notes("Filetron Pty Ltd as trustee for Hunter Discretionary Trust", FIL,
                    {"Development Management & Constructions Pty Ltd": h.addresses(DMC), "Copia": {"80 collins st"}}, [D3Y])
check("same address as another holder", note.startswith("same address as Development Management"), note)
check("an outsider has no link", h.link_notes("Ahrens Group Pty Ltd", "6. Addresses\nAhrens  3 Ahrens Road, Sandy Creek SA",
                                              {"Copia": {"80 collins st"}}, [D3Y]) == "", "")
import research_sweep as rs  # noqa: E402
src = open(os.path.join(ROOT, "src", "research_sweep.py"), encoding="utf-8").read()
check("sweep scores a linked builder lower", "score += 1 if linked else 3" in src, "")

cov = h.covered(ROOT)
check("covered reads the index", cov.get("GDI") and cov.get("SND"), {k: cov.get(k) for k in ("GDI", "SND")})

print("\nALL PASS" if not FAILS else f"\n{len(FAILS)} FAILED")
sys.exit(1 if FAILS else 0)
