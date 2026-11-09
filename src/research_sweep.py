"""The weekly sweep for research picks (rulebook section 5a, from 9 Nov 2026).

It doesn't value anything. It tags each company on the research screen with the places a wrong price most often
comes from, using facts already gathered (the screen, the ASX's announcement headlines in
data/research_data/asx_company.json, Norgate's index changes), so the research desk can read the most promising
ones and write the candidate list (reports/research_candidates.md). The tags are pointers to read, not signals:
none of them has a tested edge on its own (the mechanical versions in rulebook section 9 failed).

Places, with the weight each carries in the order:
  forced sellers (2 each): left an S&P/ASX index in the last 12 months; a substantial holder left in the last six
    months; a spin-off or demerger in the last 18 months; shares coming out of escrow in the last six months
  back from a suspension in the last three months (3): holders who waited it out often sell on the return
  fresh (1 more): any of the forced-seller events, or the return, in the last six weeks. The edge decays fast:
    Corporate Travel rose 55% in seven weeks after its return on 3 Sep 2026, before the sweep found it
  a share raising in the last nine months (1, from 2 on 9 Nov 2026): holders who didn't want more often sell, but a
    company that has just raised is often under strain, and its bad case is another raising
  insiders (2): director interest notices in the last three months on a share at least 40% below its high
    (the notice may be a sale: the desk opens it)
  buy-back (1): a buy-back notice in the last six months
  results that may hide the earnings (1): an impairment, write-down or one-off in the last 12 months
  a reported loss after earlier profits (1): the loss may be one-offs
  neglect (1): market value under A$100m
  the balance sheet (added 9 Nov 2026, after Alliance Aviation and Bapcor both failed the value test on a bad case
    that was another raising): net cash (enterprise value below the market value) adds 1; net debt, including
    leases, of half to all of the market value takes 1 off; more than the market value takes 3 off
  less 4 for little or no revenue (under A$5m): explorers and developers raise and release escrow as routine
  a holder that isn't a fund building a stake (3, added 9 Nov 2026 after Saunders): from
    data/research_data/holder_builds.csv, written by tools/holder_notices.py, which reads every substantial holder
    notice (OCR for scanned ones); latest stake 7% or more, two points or more above the window's start, still held.
    Fresh if the latest rise was in the last six weeks. A pointer to read the notices: names and figures from OCR
    can be wrong
A company with a deep dive or fact sheet in the last three months goes to the bottom unless the evening desk has
marked it reopened. Live control proposals and strategic reviews are listed apart, as special situations.
NZX companies have no announcement headlines in the stored data, so they are listed with what the screen shows
and the desk reads their announcements itself.

Writes reports/research_sweep.md and reports/research_sweep.csv.
Usage: python3 -I src/research_sweep.py <repo_root> [YYYY-MM-DD]
"""
import csv
import json
import os
import re
import sys
from datetime import date, timedelta

PLACES = [
    # (tag, weight, months back, headline pattern)
    ("a substantial holder left", 2, 6, re.compile(r"ceasing to be (a )?substantial", re.I)),
    ("spin-off or demerger", 2, 18, re.compile(r"demerg|spin[- ]?off|in[- ]specie", re.I)),
    ("shares out of escrow", 2, 6, re.compile(r"escrow", re.I)),
    ("a share raising", 1, 9, re.compile(r"entitlement offer|placement|capital raising|share purchase plan|\bSPP\b|rights issue", re.I)),
    ("buy-back", 1, 6, re.compile(r"buy-?back|appendix 3[CEF]\b", re.I)),
    ("one-offs in the results", 1, 12, re.compile(r"impairment|write-?down|one-?off|non-?cash|restructur", re.I)),
]
DIRECTOR = re.compile(r"director'?s'? interest|appendix 3Y", re.I)
FORCED = {"a substantial holder left", "spin-off or demerger", "shares out of escrow"}
RETURN = re.compile(r"reinstatement to (official )?quotation|reinstated to (official )?quotation", re.I)
SPECIAL = re.compile(r"strategic review|non-binding|indicative proposal|takeover|scheme implementation|bidder'?s statement", re.I)


# Cam avoids software companies exposed to AI disruption (9 Nov 2026, docs/RESEARCH_PROCESS.md step 1).
# ASX: the GICS industry group in the exchange's company data; NZX has no sector field, so known names are listed.
AVOID_GROUPS = {"Software & Services"}
AVOID_NZX = {"SKO", "ERD", "VGL", "GTK", "PYS"}


def avoided(asx: dict, market: str, ticker: str) -> bool:
    if market == "NZX":
        return ticker in AVOID_NZX
    group = ((asx.get(ticker) or {}).get("header") or {}).get("industryGroup") or ""
    return group in AVOID_GROUPS


def other_code(headline: str, ticker: str) -> bool:
    """True when a holder notice is the company's own, about a stake it holds in
    another listed company ("Ceasing to be a substantial holder for MMA" lodged
    by MGX). Those say nothing about who is selling the company itself."""
    m = re.search(r"\bfor ([A-Z0-9]{3})\b", headline)
    return bool(m) and m.group(1) != ticker


def months_ago(today: date, m: int) -> str:
    return (today - timedelta(days=int(m * 30.44))).isoformat()


def coverage(root: str) -> dict:
    """Ticker -> (latest date covered, row text) from research/picks/INDEX.md."""
    out = {}
    p = os.path.join(root, "research", "picks", "INDEX.md")
    if not os.path.exists(p):
        return out
    for line in open(p, encoding="utf-8"):
        m = re.match(r"\| (ASX|NZX):([A-Z0-9]+) \| [^|]* \| (\d{4}-\d\d-\d\d) \| (.*)", line)
        if m:
            out[(m.group(1), m.group(2))] = (m.group(3), line)
    return out


def main(root: str, today_s: str | None = None):
    rows = list(csv.DictReader(open(os.path.join(root, "reports", "research_screen.csv"), encoding="utf-8")))
    today = date.fromisoformat(today_s or max(r["as_of"] for r in rows))
    asx = {}
    p = os.path.join(root, "data", "research_data", "asx_company.json")
    if os.path.exists(p):
        asx = json.load(open(p, encoding="utf-8"))
    left = {}
    p = os.path.join(root, "data", "norgate", "index_changes.csv")
    if os.path.exists(p):
        for r in csv.DictReader(open(p, encoding="utf-8")):
            if r["change"] == "left" and r["date"] >= months_ago(today, 12) and r["date"] <= today.isoformat():
                left.setdefault(r["symbol"].split(".")[0], []).append((r["date"], f"{r['index']} {r['date']}"))
    cov = coverage(root)
    builds = {}
    p = os.path.join(root, "data", "research_data", "holder_builds.csv")
    if os.path.exists(p):
        for b in csv.DictReader(open(p, encoding="utf-8")):
            builds.setdefault(b["ticker"], []).append(b)
    recent = months_ago(today, 3)
    fresh_since = (today - timedelta(weeks=6)).isoformat()
    out, special = [], []
    skipped = 0
    for r in rows:
        mk, t = r["market"], r["ticker"]
        if avoided(asx, mk, t):
            skipped += 1
            continue
        tags, score, fresh = [], 0, False
        if t in left and mk == "ASX":
            tags.append("left " + "; ".join(x[1] for x in left[t])); score += 2
            fresh = fresh or any(x[0] >= fresh_since for x in left[t])
        anns = (asx.get(t) or {}).get("announcements") or [] if mk == "ASX" else []
        for tag, w, back, pat in PLACES:
            since = months_ago(today, back)
            hits = [a for a in anns if since <= a.get("date", "") <= today.isoformat() and pat.search(a.get("headline", ""))
                    and not (tag == "a substantial holder left" and other_code(a.get("headline", ""), t))]
            if hits:
                tags.append(f"{tag} ({hits[0]['date']})"); score += w
                fresh = fresh or (tag in FORCED and hits[0]["date"] >= fresh_since)
        back_on = [a for a in anns if recent <= a.get("date", "") <= today.isoformat() and RETURN.search(a.get("headline", ""))]
        if back_on:
            tags.append(f"back from a suspension ({back_on[0]['date']})"); score += 3
            fresh = fresh or back_on[0]["date"] >= fresh_since
        b = builds.get(t, [None])[0] if mk == "ASX" else None  # the largest build (the file is sorted by stake)
        if b:
            tags.append(f"{b['holder'][:40]} building a stake ({b['first_pct']}% to {b['last_pct']}%, latest {b['last_date']})")
            score += 3
            fresh = fresh or b["last_date"] >= fresh_since
        if fresh:
            tags.append("fresh: within six weeks"); score += 1
        bh = float(r["below_high"]) if r.get("below_high") not in ("", None) else 0.0
        dn = [a for a in anns if recent <= a.get("date", "") <= today.isoformat() and DIRECTOR.search(a.get("headline", ""))]
        if dn and bh <= -0.40:
            tags.append(f"director notices after a {bh:.0%} fall ({len(dn)}, latest {dn[0]['date']}: open to see buy or sell)"); score += 2
        inc = ((asx.get(t) or {}).get("key-statistics") or {}).get("incomeStatement") or [] if mk == "ASX" else []
        rev = inc[0].get("revenue") if inc else None
        if rev is not None and rev < 5e6:
            # explorers and developers raise money and release escrow as a matter of course, so those tags mean little
            tags.append("little or no revenue (an explorer or developer?)"); score -= 4
        elif inc and (inc[0].get("netIncome") or 0) < 0 and any((x.get("netIncome") or 0) > 0 for x in inc[1:]):
            tags.append("a loss last year after profits before (check what the loss was)"); score += 1
        mv = float(r["market_value_m"]) if r.get("market_value_m") not in ("", None) else None
        if mv is not None and mv < 100:
            tags.append(f"small (A${mv:.0f}m)" if mk == "ASX" else f"small (NZ${mv:.0f}m)"); score += 1
        ks = (asx.get(t) or {}).get("key-statistics") or {} if mk == "ASX" else {}
        ev, sh, px = ks.get("enterprisevalue"), ks.get("numOfShares"), ks.get("priceClose")
        if isinstance(ev, (int, float)) and isinstance(sh, (int, float)) and isinstance(px, (int, float)) and sh > 0 and px > 0:
            cap = sh * px / 1e6
            nd = ev - cap
            if nd < 0:
                tags.append(f"net cash (about A${-nd:.0f}m)"); score += 1
            elif nd > cap:
                tags.append(f"net debt incl. leases about A${nd:.0f}m, more than the shares (the bad case may be a raising)"); score -= 3
            elif nd > 0.5 * cap:
                tags.append(f"net debt incl. leases about A${nd:.0f}m"); score -= 1
        sp = [a for a in anns if months_ago(today, 6) <= a.get("date", "") and SPECIAL.search(a.get("headline", ""))]
        c = cov.get((mk, t))
        covered = c[0] if c else ""
        reopened = bool(c and "reopened" in c[1].lower())
        stale = bool(c and c[0] >= recent and not reopened)
        rec = {"market": mk, "ticker": t, "name": r["name"], "price": r["price"], "market_value_m": r.get("market_value_m", ""),
               "median_traded_k": r.get("median_traded_k", ""), "below_high": r.get("below_high", ""), "score": score,
               "places": "; ".join(tags), "covered": covered + (" (reopened)" if reopened else ""), "recently_covered": stale}
        if sp:
            special.append(dict(rec, places=f"{sp[0]['headline']} ({sp[0]['date']})"))
        if score > 0:
            out.append(rec)
    out = [x for x in out if x["score"] > 0]
    out.sort(key=lambda x: (x["recently_covered"], -x["score"], float(x["below_high"] or 0)))
    fields = list(out[0].keys()) if out else ["market", "ticker"]
    with open(os.path.join(root, "reports", "research_sweep.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(out)
    L = [f"# Research sweep, {today.isoformat()}", "",
         "Pointers for the research desk (rulebook section 5a), not buy signals. Each company on the screen is tagged with the "
         "places a wrong price most often comes from; the desk reads the top of this list and writes reports/research_candidates.md. "
         "Companies covered in the last three months sit at the bottom unless reopened.", "",
         f"{len(rows)} on the screen, {skipped} software companies left out (Cam avoids software exposed to AI disruption, "
         f"9 Nov 2026), {len(out)} with at least one tag.", "",
         "| # | Share | Name | Score | Places | Price | Value (m) | Below high | Covered |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for i, x in enumerate(out[:60], 1):
        bh = f"{float(x['below_high']):.0%}" if x["below_high"] not in ("", None) else ""
        L.append(f"| {i} | {x['market']}:{x['ticker']} | {x['name'][:38]} | {x['score']} | {x['places']} | {x['price']} | "
                 f"{x['market_value_m']} | {bh} | {x['covered']} |")
    if special:
        L += ["", "## Possible special situations (last six months)", "",
              "| Share | Name | Headline |", "| --- | --- | --- |"]
        L += [f"| {x['market']}:{x['ticker']} | {x['name'][:38]} | {x['places']} |" for x in special[:30]]
    open(os.path.join(root, "reports", "research_sweep.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"sweep: {len(out)} tagged of {len(rows)}; top: " + ", ".join(f"{x['market']}:{x['ticker']}" for x in out[:10]))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".", sys.argv[2] if len(sys.argv) > 2 else None)
