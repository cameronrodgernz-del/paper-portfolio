"""Matches AusTender contract notices (data/austender/contracts_YYYY.csv.gz) to ASX-listed companies
in Norgate's list of every ASX security since 2010 (data/norgate/universe/securities.csv), and writes
data/austender/matched.csv and data/austender/MATCHING.md. Data collection only: no share prices are read.

How a supplier is matched
1. Names are normalised: lower case, accents and punctuation removed, and the words Pty, Ltd, Limited,
   Holdings, Group, Australia, Services, The, Inc, Corporation, Co, Plc, NL, Of and And dropped. A
   "trading as" or "as trustee for" tail is split off and tried as well. Norgate names lose their
   share class ("Ordinary", "CDI 1:1", "Stapled Securities" and so on).
2. A supplier matches a listed company when the supplier's name starts with the company's whole
   normalised name, word for word (also tried with the spaces taken out, so "Lend Lease Building" meets
   "Lendlease" and "Data 3" meets "Data#3"), or, for a company whose name has several words, starts with
   its first words when those are distinctive.
3. Distinctiveness comes from how common each word is in general English (the wordfreq package): brand
   words such as Codan or DroneShield score high, everyday words such as National or Seek score near
   nothing. Confidence: high for a distinctive whole-name match, medium for a plausible one that needs
   checking, low for one resting on common words. Weaker matches are dropped.
4. Notices are grouped by supplier ABN, so names entered differently for one ABN stay together; a name
   that does not match on its own takes the ABN's match when the matching names hold most of that
   ABN's notices (noted as "matched through ABN").
5. A notice is matched only if its publish date falls between the listed security's first and last
   trading dates in Norgate.
6. Hand checks recorded in data/austender/match_checks.csv (one row per supplier and company) confirm
   or reject matches, or limit them to dates when the supplier belonged to the company.
Undated amendments (contracts_undated.csv.gz) are not matched: they have no date to test on.
Usage: python3 -I tools/austender_match.py [REPO_DIR] [--worklist PATH]   (needs: pip install wordfreq)
"""
import csv
import gzip
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

from wordfreq import zipf_frequency

DROP = {"pty", "ltd", "limited", "holdings", "holding", "group", "australia", "services", "the", "inc",
        "incorporated", "corporation", "corp", "co", "company", "plc", "nl", "of", "and", "proprietary",
        "aust", "pl", "llc", "lp", "sa", "ag", "nv", "bv", "gmbh", "se", "acn", "abn"}
# Norgate equity lines only: leave out options, notes, bonds, funds and the like
NOT_EQUITY = re.compile(r"\b(Option|Options|Right|Rights|Note|Notes|Bond|Bonds|ETF|ETFs|Fund|Warrant|Warrants|"
                        r"Preference|Pref|Hybrid|Convertible|Unpaid|Deferred Settlement|Treas|Subordinated|"
                        r"Instalment|Contingent|Redeemable|Exchangeable|Perp|Capital Notes?|ETP|Mini|"
                        r"Contribution|Partly Paid)\b", re.I)
CLASS_TAIL = re.compile(r"\s+(Ordinary|CDI\b|Stapled|Units?\b|Fully Paid|Foreign Exempt|Deferred|\d+c Ordinary|"
                        r"Ordinary/Units).*$", re.I)
# Companies treated as S&P/ASX 100 by name (clear large caps across 2013 to 2026). Borderline mid caps
# are left out on purpose, so their matches get checked by hand.
ASX100 = set("""
AGL ALL ALQ ALX AMC AMP ANN ANZ APA APT ASX AWC AZJ BHP BLD BOQ BEN BSL BXB CAR CBA CCL CGF CHC CIM COH
COL CPU CSL CSR CTX ALD CWN CWY DMP DXS EVN FMG FPH GMG GPT IAG IGO ILU IPL JBH JHX LLC LYC MGR MIN MPL
MQG NAB NCM NST NWS ORA ORG ORI OSH OZL PLS QAN QBE QUB REA REH RHC RIO RMD S32 SCG SEK SGP SGR SHL SOL
STO SUN SVW SYD TAH TCL TLC TLS TPG TPM TWE VCX WBC WDS WPL WES WFD WOR WOW WTC XRO AIO AST DUE SKI HSO
HVN TOL SPK FBU
""".split())
TIERS = {"high": 3, "medium": 2, "low": 1}
# Names Norgate cannot know: it holds each security under its latest name, so a company that renamed
# (or a subsidiary that kept an old name after a takeover) needs pointing at the right code. Each entry:
# supplier name start (normalised), Norgate symbol, first and last publish date it holds for, and why.
ALIASES = [
    ("transfield services", "BRS-201605.au", "", "2016-05-30", "Transfield Services, renamed Broadspectrum in Nov 2015"),
    ("macquarie telecom", "MAQ.au", "", "", "Macquarie Telecom Group, renamed Macquarie Technology Group in 2023"),
    ("eclipx", "FPR.au", "", "", "Eclipx Group, renamed FleetPartners Group in 2023"),
    ("sms consulting", "SMX-201709.au", "", "2017-09-07", "subsidiary of SMS Management & Technology"),
    ("leighton contractors", "CIM-202205.au", "", "", "subsidiary of Leighton Holdings, renamed CIMIC Group in 2015"),
    ("leighton", "CIM-202205.au", "", "", "Leighton Holdings, renamed CIMIC Group in 2015"),
    ("cpb contractors", "CIM-202205.au", "", "", "CIMIC subsidiary (Leighton Contractors renamed CPB in 2016)"),
    ("primary health care", "HLS.au", "", "", "Primary Health Care, renamed Healius in 2018"),
    ("transpacific", "CWY.au", "", "", "Transpacific Industries, renamed Cleanaway in 2016"),
    ("caltex", "ALD.au", "", "", "Caltex Australia, renamed Ampol in 2020"),
    ("adelaide brighton", "ABC-202406.au", "", "", "Adelaide Brighton, renamed Adbri in 2020"),
    ("ausdrill", "PRN.au", "", "", "Ausdrill, renamed Perenti in 2019"),
    ("emerchants", "EML.au", "", "", "Emerchants, renamed EML Payments in 2017"),
    ("sigma pharmaceuticals", "SIG.au", "", "", "Sigma Pharmaceuticals, renamed Sigma Healthcare in 2016"),
    ("spotless", "DOW.au", "2019-08-28", "", "Spotless, majority owned by Downer from 2017; after it left the ASX in Aug 2019"),
    ("pacific brands workwear", "WES.au", "2014-12-01", "", "Workwear Group, bought from Pacific Brands by Wesfarmers on 1 Dec 2014"),
    ("workwear group", "WES.au", "2014-12-01", "", "Workwear Group, bought from Pacific Brands by Wesfarmers on 1 Dec 2014"),
]


def ascii_fold(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()


def tokens(name):
    s = ascii_fold(name or "").lower()
    s = s.replace("&", " and ").replace("'", "").replace("#", "").replace("+", " plus ")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    toks = s.split()
    # join runs of single letters (U X C -> uxc)
    out, run = [], []
    for t in toks:
        if len(t) == 1 and t.isalpha():
            run.append(t)
            continue
        if run:
            out.append("".join(run))
            run = []
        out.append(t)
    if run:
        out.append("".join(run))
    return [t for t in out if t not in DROP]


LIGHT_DROP = {"pty", "ltd", "limited", "the", "inc", "plc", "nl", "proprietary", "pl", "co"}


def light_tokens(name):
    """Tokens with only the legal-form words dropped, so "Objective Corporation Limited" keeps its second word."""
    s = ascii_fold(name or "").lower().replace("&", " and ").replace("'", "").replace("#", "")
    return [t for t in re.sub(r"[^a-z0-9]+", " ", s).split() if t not in LIGHT_DROP]


SPLITS = re.compile(r"\b(?:t/as?|t/a|trading as|as trustee for|atf|as the trustee for|trustee for|"
                    r"the trustee for|formerly|known as|aka)\b", re.I)


def name_variants(name):
    """The main name and, if present, a trading-as or trust tail, each as a token list."""
    raw = name or ""
    raw = re.sub(r"^\s*the\s+trustee\s+for\s+(the\s+)?", "", raw, flags=re.I)
    parts = [p for p in SPLITS.split(raw) if p and p.strip()]
    seen, out = set(), []
    for p in parts[:3]:
        t = tuple(tokens(p))
        if t and t not in seen:
            seen.add(t)
            out.append(list(t))
    return out


ZIPF = {}


def rarity(tok):
    if tok not in ZIPF:
        ZIPF[tok] = zipf_frequency(tok, "en")
    return ZIPF[tok]


# Words that mark a public body or a charity rather than a business: a supplier carrying one only
# matches a listed company whose name it repeats in full.
INSTITUTION = {"university", "uni", "college", "school", "council", "shire", "authority", "department",
               "hospital", "institute", "tafe", "government", "commission", "foundation", "association",
               "society", "club", "church", "catchment", "agency", "ministry", "embassy", "consulate",
               "parish", "diocese", "aboriginal", "corporation", "museum", "library", "board", "network"}
# The listed company's line of business. A partial match (first words only) is dropped when the rest of
# the listed name names a business the supplier's name does not: "Nagambie Resources" is not
# "Nagambie Developments".
SECTOR = {"resources", "resource", "minerals", "mineral", "mining", "gold", "metals", "metal", "lithium",
          "exploration", "energy", "oil", "gas", "petroleum", "uranium", "copper", "nickel", "iron", "coal",
          "graphite", "silver", "zinc", "diamonds", "potash", "phosphate", "vanadium", "cobalt", "magnesium",
          "rare", "earths", "investments", "investment", "capital", "fund", "funds", "reit", "property",
          "properties", "bridgeway", "sports", "pharmaceuticals", "biotech", "therapeutics", "medical",
          "health", "healthcare", "media", "entertainment", "agriculture", "pastoral", "wine", "wines",
          "foods", "brewing", "financial", "finance", "bank", "insurance", "mines", "industrial",
          "technologies", "technology", "telecom", "communications"}


def score(matched, exact):
    d = sum(max(0.0, 4.5 - rarity(t)) for t in matched) + 0.5 * (len(matched) - 1) + (0.75 if exact else 0.0)
    brand = any(rarity(t) < 3.5 for t in matched)
    return d, brand


def grade(kind, d, brand, matched, listed, stoks):
    """high, medium, low or None for one supplier and one listed company."""
    if any(t in INSTITUTION for t in stoks[len(matched):]) and kind != "exact":
        return None
    if kind == "partial":
        rest = set(listed[len(matched):])
        if rest & SECTOR and not (rest & SECTOR & set(stoks)):
            return None
        z = min(rarity(t) for t in matched)
        if z < 2.0 and d >= 2.0:
            return "medium"
        if z < 2.5 and d >= 1.4:
            return "low"
        return None
    if len(matched) == 1:
        # a one-word company name carries all the evidence on its own
        z = rarity(matched[0])
        if kind == "exact":
            return "high" if z < 3.2 else "medium" if z < 4.2 else "low" if z < 5.0 else None
        return "high" if z < 2.0 else "medium" if z < 3.2 else "low" if z < 3.8 else None
    if d >= 1.5 and brand:
        return "high"
    if d >= 0.75:
        return "medium"
    if d >= 0.25:
        return "low"
    return None


def load_listed(repo):
    rows = []
    with open(os.path.join(repo, "data", "norgate", "universe", "securities.csv"), newline="") as f:
        for r in csv.DictReader(f):
            if NOT_EQUITY.search(r["name"]):
                continue
            base = CLASS_TAIL.sub("", r["name"]).strip()
            toks = tokens(base)
            if not toks:
                continue
            code = r["symbol"].split(".")[0].split("-")[0]
            rows.append({"symbol": r["symbol"], "code": code, "name": r["name"], "company": base,
                         "light": " ".join(light_tokens(base)),
                         "toks": toks, "squash": "".join(toks), "first": r["first"], "last": r["last"],
                         "cid": " ".join(toks)})
    by_first, by_sq, by_code = defaultdict(list), defaultdict(list), defaultdict(list)
    for e in rows:
        by_first[e["toks"][0]].append(e)
        by_sq[e["squash"][:3]].append(e)
        by_code[e["symbol"]].append(e)
    return rows, by_first, by_sq, by_code


def candidates(stoks, by_first, by_sq):
    """Possible listed companies for one supplier token list: {cid: (grade, d, kind, entries)}."""
    found = {}

    def add(e, kind, matched):
        d, brand = score(matched, kind == "exact")
        g = grade(kind, d, brand, matched, e["toks"], stoks)
        if not g:
            return
        cur = found.get(e["cid"])
        if cur is None or (TIERS[g], d) > (TIERS[cur[0]], cur[1]):
            found[e["cid"]] = (g, d, kind, [x for x in ([] if cur is None else cur[3]) if x is not e] + [e],
                               ("0000", "9999"), "")
        elif e not in cur[3]:
            cur[3].append(e)

    for e in by_first.get(stoks[0], []):
        L = e["toks"]
        if stoks[:len(L)] == L:
            add(e, "exact" if len(stoks) == len(L) else "full", L)
        elif len(L) > 1:
            k = 0
            while k < min(len(L), len(stoks)) and L[k] == stoks[k]:
                k += 1
            if 1 <= k < len(L):
                add(e, "partial", L[:k])
    sq = "".join(stoks)
    bounds = set()
    acc = 0
    for t in stoks:
        acc += len(t)
        bounds.add(acc)
    for e in by_sq.get(sq[:3], []):
        if e["cid"] in found and found[e["cid"]][2] != "partial":
            continue
        s = e["squash"]
        if sq.startswith(s) and len(s) in bounds and len(s) >= 4:
            add(e, "exact" if len(s) == len(sq) else "full", e["toks"])
    return found


def alias_cands(stoks, by_code):
    """Curated renames: {cid: (grade, d, kind, entries, window, note)}."""
    out = {}
    for start, sym, lo, hi, note in ALIASES:
        at = tokens(start)
        if stoks[:len(at)] == at and by_code.get(sym):
            ents = by_code[sym]
            out[ents[0]["cid"]] = ("high", 9.0, "alias", ents, (lo or "0000", hi or "9999"), note)
            break
    return out


def load_notices(repo):
    d = os.path.join(repo, "data", "austender")
    out = []
    for f in sorted(os.listdir(d)):
        if not re.match(r"contracts_\d{4}\.csv\.gz$", f):
            continue
        with gzip.open(os.path.join(d, f), "rt", newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                out.append(r)
    return out


def load_checks(repo):
    p = os.path.join(repo, "data", "austender", "match_checks.csv")
    checks = {}
    if os.path.exists(p):
        with open(p, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                checks[(r["supplier_key"], r["symbol_code"])] = r
    return checks


def fval(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return 0.0


def main(repo, worklist=None):
    listed, by_first, by_sq, by_code = load_listed(repo)
    notices = load_notices(repo)
    checks = load_checks(repo)
    print(f"{len(listed)} listed equity lines, {len(notices)} dated notices", flush=True)

    # supplier groups: ABN where there is one, else the normalised name
    def skey(r):
        return r["supplier_abn"] or "name:" + " ".join(tokens(r["supplier_name"]))
    groups = defaultdict(list)
    for i, r in enumerate(notices):
        groups[skey(r)].append(i)

    name_cache = {}

    def name_cands(name):
        if name not in name_cache:
            best = {}
            for v in name_variants(name):
                found = candidates(v, by_first, by_sq)
                found.update(alias_cands(v, by_code))
                lt = " ".join(light_tokens(name))
                for cid, c in list(found.items()):
                    if c[2] != "alias" and len(lt.split()) >= 2 and any(e["light"] == lt for e in c[3]):
                        found[cid] = ("high", max(c[1], 3.0), "exact", c[3], c[4], c[5])
                for cid, c in found.items():
                    if cid not in best or (TIERS[c[0]], c[1]) > (TIERS[best[cid][0]], best[cid][1]):
                        best[cid] = c
            name_cache[name] = best
        return name_cache[name]

    matched_rows = []
    pair_info = {}
    outside = Counter()
    for key, idxs in groups.items():
        names = Counter(notices[i]["supplier_name"] for i in idxs)
        per_name = {n: name_cands(n) for n in names}
        tally = defaultdict(lambda: [0, None])  # cid -> [notices, best candidate]
        for n, cands in per_name.items():
            for cid, c in cands.items():
                t = tally[cid]
                t[0] += names[n]
                if t[1] is None or (TIERS[c[0]], c[1]) > (TIERS[t[1][0]], t[1][1]):
                    t[1] = c
        if not tally:
            continue
        # one company per supplier group: the best grade, then the most notices. A curated rename comes
        # first, with the best plain name match as the fallback for dates outside its window.
        direct = {c: t for c, t in tally.items() if t[1][2] != "alias"}
        alias = {c: t for c, t in tally.items() if t[1][2] == "alias"}
        order = []
        for pool in (alias, direct):
            if pool:
                order.append(max(pool.items(), key=lambda kv: (TIERS[kv[1][1][0]], kv[1][0], kv[1][1][1])))
        rivals = sorted({c for c in direct if c not in [o[0] for o in order]})
        for i in idxs:
            r = notices[i]
            own = per_name[r["supplier_name"]]
            pd = r["publish_date"]
            pick = None
            dated_out = False
            for cid, (cnt, best) in order:
                g, d, kind, entries, window, anote = best
                via_abn = cid not in own
                if via_abn and not (key[:5] != "name:" and cnt / len(idxs) >= 0.5 and g == "high"):
                    continue
                dated_out = True
                if not (window[0] <= pd <= window[1]):
                    continue
                live = [e for e in entries if e["first"] <= pd <= e["last"]]
                if live:
                    pick = (cid, g, kind, anote, via_abn, max(live, key=lambda x: (x["last"], x["first"])))
                    break
            if pick is None:
                if dated_out:
                    outside["before 2010" if pd < "2010-01-04" else order[0][0]] += 1
                continue
            cid, g, kind, anote, via_abn, e = pick
            conf = g
            notes = []
            if via_abn:
                conf = "medium" if conf == "high" else conf
                notes.append("matched through ABN")
            if kind == "alias":
                notes.append("name list: " + anote)
            if kind == "partial":
                notes.append("first words of the listed name only")
            if rivals:
                notes.append("other names under this ABN suggest: " + "; ".join(rivals[:3]))
            matched_rows.append({"i": i, "key": key, "cid": cid, "entry": e, "conf": conf, "notes": notes})
            pi = pair_info.setdefault((key, e["code"]), {"names": Counter(), "years": Counter(), "n": 0,
                                                          "entry": e, "conf": conf, "agencies": Counter(),
                                                          "desc": Counter()})
            pi["names"][r["supplier_name"]] += 1
            pi["years"][pd[:4]] += fval(r["value_aud"])
            pi["n"] += 1
            pi["agencies"][r["agency"]] += 1
            pi["desc"][r["description"][:80]] += 1

    # hand-check list: supplier and company pairs with A$5m or more in a year, outside the ASX 100
    need = {p for p, v in pair_info.items() if max(v["years"].values()) >= 5e6 and v["entry"]["code"] not in ASX100}
    if worklist:
        with open(worklist, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["supplier_key", "symbol_code", "symbol", "listed_name", "first", "last", "confidence",
                        "notices", "max_year_value", "years", "names", "agencies", "descriptions", "checked"])
            for p in sorted(need, key=lambda p: -max(pair_info[p]["years"].values())):
                v = pair_info[p]
                e = v["entry"]
                w.writerow([p[0], p[1], e["symbol"], e["company"], e["first"], e["last"], v["conf"], v["n"],
                            round(max(v["years"].values())),
                            "; ".join(f"{y}:{v['years'][y] / 1e6:.1f}m" for y in sorted(v["years"])),
                            " | ".join(n for n, _ in v["names"].most_common(4)),
                            " | ".join(a for a, _ in v["agencies"].most_common(3)),
                            " | ".join(dd for dd, _ in v["desc"].most_common(3)),
                            "yes" if p in checks else ""])
        print(f"worklist: {len(need)} pairs, {sum(1 for p in need if p in checks)} already checked")

    # apply hand checks and write matched.csv
    out, rejected = [], []
    for m in matched_rows:
        r = notices[m["i"]]
        e = m["entry"]
        ck = checks.get((m["key"], e["code"]))
        checked = "no"
        conf = m["conf"]
        notes = list(m["notes"])
        if ck:
            v = ck["verdict"]
            lo, hi = ck.get("valid_from") or "0000", ck.get("valid_to") or "9999"
            if v == "reject" or not (lo <= r["publish_date"] <= hi):
                rejected.append((m, ck))
                continue
            checked = "yes"
            conf = ck.get("confidence") or conf
            notes = [ck["notes"]] + [n for n in notes if n.startswith("matched through")]
        elif (m["key"], e["code"]) in need:
            checked = "pending"
        out.append({"cn_id": r["cn_id"], "publish_date": r["publish_date"], "value_aud": r["value_aud"],
                    "supplier_name": r["supplier_name"], "supplier_abn": r["supplier_abn"], "symbol": e["symbol"],
                    "listed_name": e["company"], "confidence": conf, "checked": checked,
                    "notes": "; ".join(n for n in notes if n)})
    out.sort(key=lambda x: (x["publish_date"], x["cn_id"]))
    cols = ["cn_id", "publish_date", "value_aud", "supplier_name", "supplier_abn", "symbol", "listed_name",
            "confidence", "checked", "notes"]
    with open(os.path.join(repo, "data", "austender", "matched.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(out)
    write_summary(repo, notices, out, rejected, checks, need, pair_info, outside)
    print(f"matched notices: {len(out)}; rejected by hand checks: {len(rejected)}")


def write_summary(repo, notices, out, rejected, checks, need, pair_info, outside):
    yr_all = Counter(r["publish_date"][:4] for r in notices)
    yr_con = Counter(r["publish_date"][:4] for r in notices if r["amendment"] == "0")
    yr_m = Counter(r["publish_date"][:4] for r in out)
    yr_mc = Counter(r["publish_date"][:4] for r in out if "-A" not in r["cn_id"])
    yr_hi = Counter(r["publish_date"][:4] for r in out if r["confidence"] == "high")
    conf = Counter(r["confidence"] for r in out)
    syms = {r["symbol"] for r in out}
    syms_hi = {r["symbol"] for r in out if r["confidence"] == "high"}
    cos = {r["listed_name"].lower() for r in out}
    L = []
    w = L.append
    w("# AusTender matches to ASX-listed companies\n")
    w("Written by `tools/austender_match.py` from `contracts_YYYY.csv.gz` and Norgate's list of every ASX "
      "security since 2010 (`data/norgate/universe/securities.csv`). Hand checks are in `match_checks.csv`. "
      "No share prices were read for this work.\n")
    w("## Counts by year\n")
    w("| year | notices | of which contracts | matched notices | of which contracts | high confidence |")
    w("|---|---|---|---|---|---|")
    for y in sorted(yr_all):
        w(f"| {y} | {yr_all[y]:,} | {yr_con[y]:,} | {yr_m[y]:,} | {yr_mc[y]:,} | {yr_hi[y]:,} |")
    w(f"| total | {sum(yr_all.values()):,} | {sum(yr_con.values()):,} | {len(out):,} | {sum(yr_mc.values()):,} | "
      f"{sum(yr_hi.values()):,} |\n")
    w(f"Matched notices by confidence: high {conf['high']:,}, medium {conf['medium']:,}, low {conf['low']:,}. "
      f"Distinct listed securities matched: {len(syms):,}, under {len(cos):,} company names ({len(syms_hi):,} "
      f"securities with at least one high-confidence match). Hand-checked notices: {sum(1 for r in out if r['checked'] == 'yes'):,}, covering "
      f"{len({(r['supplier_abn'] or r['supplier_name'], r['symbol']) for r in out if r['checked'] == 'yes'}):,} "
      f"supplier and company pairs. Notices before 2010 cannot match: Norgate's list starts in 2010.\n")
    w("## The 40 largest matched contracts\n")
    w("Contracts only (amendments left out), by value.\n")
    w("| symbol | listed name | supplier | value (A$) | publish date | confidence | checked |")
    w("|---|---|---|---|---|---|---|")
    top = sorted((r for r in out if "-A" not in r["cn_id"]), key=lambda r: -fval(r["value_aud"]))[:40]
    for r in top:
        w(f"| {r['symbol']} | {r['listed_name']} | {r['supplier_name']} | {fval(r['value_aud']):,.0f} | "
          f"{r['publish_date']} | {r['confidence']} | {r['checked']} |")
    w("")
    w("## Matches rejected\n")
    rej = defaultdict(lambda: [0, 0.0, None, None, Counter()])
    for m, ck in rejected:
        k = (m["key"], m["entry"]["code"])
        rej[k][0] += 1
        rej[k][1] += fval(notices[m["i"]]["value_aud"])
        rej[k][2] = ck
        rej[k][3] = m
        rej[k][4][notices[m["i"]]["supplier_name"]] += 1
    if rej:
        w("Rejected or cut back by hand checks (the notices are left out of matched.csv):\n")
        w("| supplier | proposed match | notices | value (A$) | why |\n|---|---|---|---|---|")
        for k, (n, val, ck, m, nm) in sorted(rej.items(), key=lambda kv: -kv[1][1]):
            sup = nm.most_common(1)[0][0]
            why = ck["notes"]
            if ck["verdict"] != "reject":
                why = f"kept only {ck.get('valid_from') or 'start'} to {ck.get('valid_to') or 'now'}: " + why
            w(f"| {sup} | {m['entry']['symbol']} {m['entry']['company']} | {n:,} | {val:,.0f} | {why} |")
        w("")
    if outside:
        early = outside.get("before 2010", 0)
        w(f"Also left out: {sum(outside.values()) - early:,} notices from 2010 on whose supplier matched a listed "
          "company but whose publish date falls outside that security's trading window in Norgate (before listing or "
          f"after delisting) or outside the dates a hand check allows, and {early:,} notices from before 2010, which "
          "Norgate's list does not cover.\n")
    pend = [p for p in need if p not in checks]
    if pend:
        w(f"Pairs that meet the hand-check rule but are not yet checked: {len(pend)} (marked `pending`).\n")
    weaknesses(w, repo, notices, out, need, checks)
    with open(os.path.join(repo, "data", "austender", "MATCHING.md"), "w") as f:
        f.write("\n".join(L) + "\n")


def weaknesses(w, repo, notices, out, need, checks):
    from datetime import date
    by_id = {r["cn_id"]: r for r in notices}
    years = Counter(r["publish_date"][:4] for r in notices)
    und = os.path.join(repo, "data", "austender", "contracts_undated.csv.gz")
    n_und = 0
    if os.path.exists(und):
        with gzip.open(und, "rt", newline="", encoding="utf-8") as fh:
            n_und = sum(1 for _ in csv.DictReader(fh))
    con = [r for r in out if "-A" not in r["cn_id"]]
    lag_42 = lag_365 = ahead = weekend = blank = n = 0
    for r in con:
        nr = by_id.get(r["cn_id"])
        if not nr:
            continue
        try:
            pd = date.fromisoformat(nr["publish_date"])
        except ValueError:
            continue
        n += 1
        if pd.weekday() >= 5:
            weekend += 1
        if not nr["value_aud"]:
            blank += 1
        try:
            sd = date.fromisoformat(nr["start_date"])
        except ValueError:
            continue
        lag = (pd - sd).days
        if lag > 42:
            lag_42 += 1
        if lag > 365:
            lag_365 += 1
        if lag < 0:
            ahead += 1
    big = [r for r in con if fval(r["value_aud"]) >= 1e9 and r["symbol"].split(".")[0].split("-")[0] not in ASX100]
    via_abn = sum(1 for r in out if "matched through ABN" in r["notes"])
    partial = sum(1 for r in out if "first words" in r["notes"])
    fund = sum(1 for r in out if "goes to the" in r["notes"])
    per_day = Counter((r["symbol"], r["publish_date"]) for r in con)
    crowded = sum(1 for v in per_day.values() if v >= 5)
    pct = lambda a: f"{100 * a / n:.0f}%" if n else "n/a"
    w("## What could weaken a test\n")
    w(f"- Coverage. Notices run from {min(years)} to {max(years)}, but years before 2007 are thin (only notices "
      "carried over from the old Gazette system) and Norgate's list starts in 2010, so matches start in 2010. "
      f"The last year runs only to the day of the download. {n_und:,} amendments have no usable publish date "
      "(see README.md) and are not matched; amendments made after June 2020 to contracts published before 2013 "
      "are missing altogether.")
    w(f"- Late publication. Agencies must report within 42 days of the contract starting, and many report late. "
      f"Of {n:,} matched contracts, {pct(lag_42)} were published more than 42 days after their start date and "
      f"{pct(lag_365)} more than a year after; {pct(ahead)} were published before their start date. Where a "
      "company announced the contract itself, the market heard first and the AusTender date is a second, later "
      "event.")
    wk = "none of the matched contracts carries" if not weekend else f"{pct(weekend)} of matched contracts carry"
    w(f"- Dates only. The contract files give publish dates without times, and {wk} a Saturday or Sunday date. "
      "The API time-of-day split is in README.md: most notices go up during ASX trading hours, so the publish day "
      "is partly after the event.")
    w(f"- Many notices are not news. Panel and standing-offer arrangements produce thousands of small orders "
      f"(Data#3 alone has over 5,000 notices), and {crowded:,} company-days carry five or more matched contracts. "
      "Ceiling values on panels and standing offers overstate likely spend.")
    w(f"- Values that look wrong. {blank:,} matched contracts have no value (contracts known only through a later "
      f"amendment). {len(big)} matched contracts of A$1 billion or more go to companies outside the ASX 100; each "
      "should be read before it is used, as keying errors and multi-year ceilings both occur.")
    w(f"- Weaker matches. {via_abn:,} matched notices rest on a shared ABN rather than the name, {partial:,} on the "
      "first words of the listed name only, and medium and low matches below the hand-check line have not been "
      f"read by a person. {fund:,} matched notices are leases where a listed fund manager or trustee holds the "
      "building for a fund, so the rent goes to the fund rather than the listed company (marked low).")
    w("- Names. Norgate holds each security under its latest name, so companies that renamed are only matched "
      "through the short rename list in tools/austender_match.py. Subsidiaries trading under a different name from "
      "the parent (for example Thiess under CIMIC) are mostly not matched, and a subsidiary sold to "
      "another owner keeps matching its old parent unless a hand check limits its dates.")
    w("- Gaps in Norgate's list. A few ASX companies are missing from it (for example XTEK and Duxton Water), so "
      "their contracts cannot be matched, and a company that renamed after a merger can carry a name that did not "
      "exist when the contract was let (Norgate's BJY, Barrenjoey Group, is Magellan Financial Group under a later "
      "name).")
    w("- ASX 100. The repository has no S&P/ASX 100 membership history, so the hand-check rule used a fixed list of "
      "clear large caps (ASX100 in tools/austender_match.py). Borderline mid caps such as Downer and Viva Energy were "
      "left off the list and checked by hand anyway.")
    w("- How the hand checks were done. Each check read the supplier names under the ABN, the agencies and the "
      "contract descriptions, and the company's history from Wikipedia where a page existed. The shared web search "
      "allowance ran out early in this work, so some checks rest on the notice data and the company name alone; "
      "their notes say so (for example Service Stream's 2025 Defence base services contract and the 2015 Mission "
      "Providence jobactive contracts).")
    w("- Joint ventures. Some suppliers are joint ventures (for example Downer EDI Works with F.K. Gardner & Sons); "
      "the listed company's share of the contract is not known.")
    w("")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:]]
    wl = None
    if "--worklist" in args:
        j = args.index("--worklist")
        wl = args[j + 1]
        del args[j:j + 2]
    main(args[0] if args else ".", wl)
