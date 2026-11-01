"""Research ranking (rulebook section 5a): the second stage of the research funnel.

Stage 1, src/research_screen.py: every ASX share outside the S&P/ASX 300 and NZX share outside the NZX 20 that
we can trade at our size (prices only).
Stage 2, this script: adds each company's facts from the exchanges' own data (tools/research_company_data.py),
then
  - gates: drops a company only on a rule a deep dive can't change (a fund or trust, no business yet, Cam's
    excluded list or the gaming hold, too thin to trade, suspended or delisting);
  - routes: sends takeover, scheme, strategic review and controlling-holder cases to a special situations watch
    list instead of dropping them;
  - scores the rest on points anyone can check: value anchors (earnings, assets, net cash, dividends, steady
    profits), signs it's overlooked (an index exit, small size, a big fall, a fall worse than its industry,
    director notices, a substantial holder leaving), a dated result soon, and red flags (a recent raising, a
    loss, heavy debt, heavy shorting).
Stage 3 is a fact sheet for the top of this list (research/facts/TEMPLATE.md), then deep dives.
The score is not a buy signal and has no tested edge: it decides where the research time goes, nothing else.
Writes reports/research_rank.md and reports/research_rank.csv.
Usage: python3 -I src/research_rank.py <repo_root>
"""
import csv
import json
import os
import re
import statistics as stats
import sys
from datetime import date, datetime, timedelta, timezone

FUND = re.compile(r"INVESTMENT (COMPANY|CO\b)|INVESTMENTS LIMITED|\bFUND\b|INCOME TRUST|CREDIT INCOME|CAPITAL INCOME|LONG SHORT|"
                  r"FUTURE GENERATION|GLOBAL VALUE|EMERGING MARKETS|ABSOLUTE RETURN|OPPORTUNITIES TRUST|\bETF\b|INVESTMENT TRUST|"
                  r"FOUNDATION INVESTMENT|FAR EAST INCOME|\bPLC\b", re.I)
HOLD_WORDS = re.compile(r"gaming|lotter|wager|racing|casino|\bbet|bookmak|bloodstock", re.I)
HOLD_TICKERS = {("ASX", "JIN"), ("ASX", "SGR"), ("ASX", "SXL"), ("ASX", "RTH"), ("NZX", "SKC"), ("NZX", "SKT"),
                ("NZX", "NZM"), ("NZX", "PGW")}
BIG_NZX = {"ANZ", "WBC", "FCG", "FSF", "AIR", "VNT"}          # dual-listed or large, outside the NZX 20 by a little
NZX_FUNDS = {"AFI", "BIT", "BRM", "FCT", "HFL", "KFL", "MLN", "TEM", "PLP", "BIF", "CO2"}   # investment companies and funds
COMMODITY = re.compile(r"resources|minerals|mining|metals|gold|oil|gas|coal|platinum|lithium|uranium|iron|copper|zinc", re.I)
PROPERTY_NZX = re.compile(r"property|investore|asset plus|cdl investments|vital healthcare|land ", re.I)
MONTHS = {m: i for i, m in enumerate(("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"), 1)}
SPECIAL = re.compile(r"non-binding (indicative )?(proposal|offer)|indicative (proposal|offer)|unsolicited|"
                     r"receipt of (a )?(revised )?proposal|target'?s statement|strategic review|sale process|"
                     r"scheme booklet|scheme meeting", re.I)                 # the company looks like the target
DEAL_CHECK = re.compile(r"takeover|bidder'?s statement|scheme implementation|off-market|compulsory acquisition|"
                        r"change of control", re.I)                          # could be either side: flag, don't route
MONTHLY_NTA = re.compile(r"\bNTA\b|net tangible asset|net asset (value|backing)|\bNAV\b|investment update|"
                         r"portfolio update|investment report", re.I)     # what investment companies publish monthly
DELIST = re.compile(r"delist|removal from (the )?official list", re.I)
RAISE = re.compile(r"placement|entitlement offer|rights issue|share purchase plan|capital raising|\bSPP\b", re.I)
RESULTS = re.compile(r"appendix 4[de]|half[- ]year (results|report|financial)|full[- ]year (results|report)|"
                     r"preliminary final|annual results|interim results|results announcement|annual report", re.I)
DIRECTOR = re.compile(r"change of director'?s interest|initial director'?s interest|appendix 3y", re.I)
CEASE = re.compile(r"ceasing to be (a )?substantial holder", re.I)
NOT_INDUSTRIAL = re.compile(r"bank|financial|insurance|real estate|reit", re.I)


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def load_json(path):
    return json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}


def excluded(root):
    p = os.path.join(root, "config", "judgement_excluded.csv")
    rows, confirmed = set(), False
    for line in open(p, encoding="utf-8") if os.path.exists(p) else []:
        if line.lower().startswith("# confirmed by cam"):
            confirmed = True
        if line.startswith("#") or line.startswith("ticker,") or not line.strip():
            continue
        rows.add(line.split(",")[0].strip().upper())
    return rows, confirmed


def covered(root):
    """Ticker -> (status, kind, verdict) from research/picks/INDEX.md."""
    out = {}
    p = os.path.join(root, "research", "picks", "INDEX.md")
    for line in open(p, encoding="utf-8") if os.path.exists(p) else []:
        m = re.match(r"\| (ASX|NZX):(\w+) \|", line)
        if not m:
            continue
        cells = [c.strip() for c in line.split("|")]
        verdict, status = cells[4], cells[5]
        kind = "deep dive" if re.search(r"deep dive \(|red team:", verdict, re.I) else "quick look"
        out[(m.group(1), m.group(2))] = (status, kind, verdict)
    return out


def index_exits(root, today):
    out = {}
    p = os.path.join(root, "data", "norgate", "index_changes.csv")
    cut = (date.fromisoformat(today) - timedelta(days=270)).isoformat()
    for r in csv.DictReader(open(p, encoding="utf-8")) if os.path.exists(p) else []:
        if r["change"] == "left" and r["date"] >= cut:
            code = r["symbol"].split(".")[0].upper()
            out.setdefault(code, []).append(f"left the {r['index']} {r['date']}")
    return out


def next_result(anns, today):
    """Expected next result date: a results headline a year earlier, moved on a year, within 150 days."""
    t = date.fromisoformat(today)
    best = None
    for a in anns:
        if not RESULTS.search(a["headline"]):
            continue
        d = date.fromisoformat(a["date"])
        nxt = d.replace(year=d.year + 1) if not (d.month == 2 and d.day == 29) else d.replace(year=d.year + 1, day=28)
        if t < nxt <= t + timedelta(days=150) and (best is None or nxt < best):
            best = nxt
    return best.isoformat() if best else None


def score_asx(r, e, ctx):
    pts, why, flags = 0, [], []
    h = (e or {}).get("header") or {}
    k = (e or {}).get("key-statistics") or {}
    anns = (e or {}).get("announcements") or []
    today = ctx["today"]
    six = (date.fromisoformat(today) - timedelta(days=182)).isoformat()
    nine = (date.fromisoformat(today) - timedelta(days=270)).isoformat()
    recent = [a for a in anns if a["date"] >= six]
    mcap = num(h.get("marketCap"))
    px = num(r["price"])
    eps = num(k.get("earningsPerShare"))
    pe = px / eps if px and eps and eps > 0 else None
    if pe is not None and pe <= 8:
        pts += 2; why.append(f"{pe:.1f} times earnings")
    elif pe is not None and pe <= 12:
        pts += 1; why.append(f"{pe:.1f} times earnings")
    ta, tl = num(k.get("totalAssets")), num(k.get("totalLiabilities"))
    book = (ta - tl) * 1e6 if ta is not None and tl is not None else None
    pb = mcap / book if mcap and book and book > 0 else None
    if pb is not None and pb <= 0.7:
        pts += 2; why.append(f"{pb:.2f} times book")
    elif pb is not None and pb <= 1.0:
        pts += 1; why.append(f"{pb:.2f} times book")
    ev = num(k.get("enterprisevalue"))
    nc = (mcap / 1e6 - ev) / (mcap / 1e6) if mcap and ev is not None else None
    if nc is not None and nc >= 0.30:
        pts += 2; why.append(f"net cash about {nc:.0%} of market value")
    elif nc is not None and nc >= 0.10:
        pts += 1; why.append(f"net cash about {nc:.0%} of market value")
    yld = num(k.get("yieldAnnual"))
    if yld is not None and yld >= 6:
        pts += 1; why.append(f"{yld:.1f}% yield")
    inc = [num(x.get("netIncome")) for x in (k.get("incomeStatement") or [])]
    inc = [x for x in inc if x is not None]
    if len(inc) >= 4 and all(x > 0 for x in inc[:4]):
        pts += 1; why.append("profit in each of the last four years")
    if inc and inc[0] <= 0:
        pts -= 1; flags.append("loss in the latest year")
    if len(inc) >= 2 and inc[1] > 0 and 0 < inc[0] < 0.5 * inc[1]:
        flags.append("profit more than halved last year (check why)")
    # overlooked
    ex = ctx["exits"].get(r["ticker"])
    if ex:
        pts += 2; why.append("; ".join(ex))
    if mcap and mcap < 250e6:
        pts += 1; why.append(f"small (A${mcap / 1e6:.0f}m)")
    bh = num(r["below_high"])
    if bh is not None and bh <= -0.35:
        pts += 1; why.append(f"{-bh:.0%} below its 12-month high")
    grp = h.get("industryGroup")
    r12 = num(r["return_12m"])
    med = ctx["group_median"].get(grp)
    if r12 is not None and med is not None and r12 <= med - 0.25:
        pts += 1; why.append(f"12 months {r12:+.0%} against {med:+.0%} for its industry")
    nd = sum(1 for a in recent if DIRECTOR.search(a["headline"]))
    nce = sum(1 for a in recent if CEASE.search(a["headline"]))
    if nce:
        pts += 1; why.append("a substantial holder left in the last six months")
    nr = next_result(anns, today)
    deal = [a for a in anns if a["date"] >= nine and DEAL_CHECK.search(a["headline"])]
    if deal:
        flags.append(f"deal headline to check, which side it's on ({deal[0]['date']}: {deal[0]['headline'][:80]})")
    # red flags
    if any(RAISE.search(a["headline"]) for a in recent):
        pts -= 1; flags.append("a share raising in the last six months")
    if ev is not None and mcap and ev > 2.5 * mcap / 1e6 and not NOT_INDUSTRIAL.search(grp or ""):
        pts -= 1; flags.append(f"heavy debt (enterprise value {ev / (mcap / 1e6):.1f} times market value)")
    sp = num(r["short_pct"])
    if sp is not None and sp >= 0.05:
        pts -= 1; flags.append(f"{sp:.1%} of shares sold short")
    first = re.sub(r"^(the)\s+", "", r["name"], flags=re.I).split()[0].lower() if r["name"] else ""

    def about_us(a):
        m = re.match(r"^([A-Z0-9]{3}):", a["headline"])
        return not m or m.group(1) == r["ticker"] or first in a["headline"].lower()
    special = [a for a in anns if a["date"] >= nine and SPECIAL.search(a["headline"]) and about_us(a)]
    other = [a for a in anns if a["date"] >= nine and SPECIAL.search(a["headline"]) and not about_us(a)]
    if other:
        flags.append(f"deal headline about another company ({other[0]['date']}: {other[0]['headline'][:80]})")
    delist = [a for a in recent if DELIST.search(a["headline"])]
    facts = {"industry": grp or "", "market_value_m": round(mcap / 1e6, 1) if mcap else "", "pe": round(pe, 1) if pe else "",
             "price_to_book": round(pb, 2) if pb else "", "net_cash_share": round(nc, 2) if nc is not None else "",
             "yield": round(yld, 1) if yld is not None else "", "next_result": nr or "", "director_notices": nd,
             "spread": ""}
    return pts, why, flags, special, delist, facts


def score_nzx(r, e, ctx):
    pts, why, flags = 0, [], []
    i = (e or {}).get("info") or {}
    px = num(i.get("closePrice")) or num(r["price"])
    eps, nta = num(i.get("earningsPerShare")), num(i.get("ntaPerShare"))
    cap = num(i.get("capitalisation"))
    pe = px / eps if px and eps and eps > 0 else None
    if pe is not None and pe <= 8:
        pts += 2; why.append(f"{pe:.1f} times earnings")
    elif pe is not None and pe <= 12:
        pts += 1; why.append(f"{pe:.1f} times earnings")
    if eps is not None and eps <= 0:
        pts -= 1; flags.append("no earnings in the latest year")
    pn = px / nta if px and nta and nta > 0 else None
    if pn is not None and pn <= 0.7:
        pts += 2; why.append(f"{pn:.2f} times net tangible assets")
    elif pn is not None and pn <= 1.0:
        pts += 1; why.append(f"{pn:.2f} times net tangible assets")
    gdy = num(i.get("gdyPerShare"))
    if gdy is not None and gdy >= 7:
        pts += 1; why.append(f"{gdy:.1f}% gross yield")
    if cap and cap < 250e6:
        pts += 1; why.append(f"small (NZ${cap / 1e6:.0f}m)")
    bh = num(r["below_high"])
    if bh is not None and bh <= -0.35:
        pts += 1; why.append(f"{-bh:.0%} below its 12-month high")
    facts = {"industry": "", "market_value_m": round(cap / 1e6, 1) if cap else "", "pe": round(pe, 1) if pe else "",
             "price_to_book": round(pn, 2) if pn else "", "net_cash_share": "", "yield": round(gdy, 1) if gdy is not None else "",
             "next_result": "", "director_notices": "", "spread": ""}
    bid, off = num(i.get("bestBid")), num(i.get("bestOffer"))
    if bid and off and off >= bid:
        facts["spread"] = round(off / bid - 1, 3)
    return pts, why, flags, [], [], facts


def nzx_gate(i):
    bid, off = num(i.get("bestBid")), num(i.get("bestOffer"))
    cap = num(i.get("capitalisation"))
    if (i.get("suspensionStatus") or "N") != "N":
        return "suspended"
    if (i.get("category") or "SHRS") != "SHRS":
        return "not an ordinary share"
    if cap is not None and cap < 30e6:
        return f"too small to trade at our size (NZ${cap / 1e6:.0f}m)"
    return None             # the spread isn't a gate: read outside trading hours it can be wide for no reason


def watch_events(root, today):
    """Watched companies (status watching, from a quick look) with a dated event in the next 30 days."""
    out = []
    t = date.fromisoformat(today)
    for (mkt, tick), (status, kind, verdict) in covered(root).items():
        if status != "watching" or kind != "quick look":
            continue
        line = next((l for l in open(os.path.join(root, "research", "picks", "INDEX.md"), encoding="utf-8")
                     if l.startswith(f"| {mkt}:{tick} |")), "")
        nxt = line.rstrip().rstrip("|").split("|")[-1]
        dates = []
        for d, mo, y in re.findall(r"(\d{1,2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* (20\d\d)", nxt):
            dd = date(int(y), MONTHS[mo.lower()], int(d))
            if t <= dd <= t + timedelta(days=30):
                dates.append(dd)
        if dates:
            out.append((min(dates).isoformat(), mkt, tick, nxt.strip()))
    return sorted(out)


def queue(root, ranked, today, n_asx=15, n_nzx=5, max_commodity=3, max_property=2, max_watch=5):
    """The next batch of fact sheets: watched names with an event in 30 days, then the top of each market's
    ranking, skipping anything with a fact sheet or a deep dive in the last three months, and varying sectors."""
    facts_dir = os.path.join(root, "research", "facts")
    have = set(os.listdir(facts_dir)) if os.path.isdir(facts_dir) else set()
    cov = covered(root)

    def done(mkt, tick):
        if f"{tick}.md" in have or f"NZ_{tick}.md" in have:
            return True
        c = cov.get((mkt, tick))
        return bool(c and c[1] == "deep dive")
    out = []
    for d, mkt, tick, nxt in watch_events(root, today)[:max_watch]:
        if not done(mkt, tick):
            out.append({"market": mkt, "ticker": tick, "why": f"watched, event {d}: {nxt[:90]}", "points": ""})
    picked = {(x["market"], x["ticker"]) for x in out}
    commodity = prop = 0
    for mkt, n in (("ASX", n_asx), ("NZX", n_nzx)):
        k = 0
        for x in ranked:
            if x["market"] != mkt or (mkt, x["ticker"]) in picked or done(mkt, x["ticker"]):
                continue
            is_c = (mkt == "ASX" and re.search(r"materials|energy", x["industry"], re.I)) or COMMODITY.search(x["name"])
            is_p = re.search(r"real estate", x["industry"], re.I) or (mkt == "NZX" and PROPERTY_NZX.search(x["name"]))
            if (is_c and commodity >= max_commodity) or (is_p and prop >= max_property):
                continue
            commodity += 1 if is_c else 0
            prop += 1 if is_p else 0
            out.append({"market": mkt, "ticker": x["ticker"], "why": f"ranked, {x['points']} points", "points": x["points"]})
            picked.add((mkt, x["ticker"]))
            k += 1
            if k >= n:
                break
    return out


def main(root: str) -> int:
    screen = list(csv.DictReader(open(os.path.join(root, "reports", "research_screen.csv"), encoding="utf-8")))
    A = load_json(os.path.join(root, "data", "research_data", "asx_company.json"))
    N = load_json(os.path.join(root, "data", "research_data", "nzx_company.json"))
    excl, confirmed = excluded(root)
    cov = covered(root)
    today = max(r["as_of"] for r in screen)
    groups = {}
    for r in screen:
        if r["market"] == "ASX":
            g = ((A.get(r["ticker"]) or {}).get("header") or {}).get("industryGroup")
            if g and num(r["return_12m"]) is not None:
                groups.setdefault(g, []).append(num(r["return_12m"]))
    ctx = {"today": today, "exits": index_exits(root, today),
           "group_median": {g: stats.median(v) for g, v in groups.items() if len(v) >= 4}}
    gated, routed, ranked = [], [], []
    for r in screen:
        key = (r["market"], r["ticker"])
        name = r["name"]
        e = (A if r["market"] == "ASX" else N).get(r["ticker"])
        status = cov.get(key)
        reason = None
        if FUND.search(name) or r["group"].startswith("Listed investment") or (r["market"] == "NZX" and re.search(r"Units", name)) \
                or (r["market"] == "NZX" and r["ticker"] in NZX_FUNDS):
            reason = "fund, trust or investment company"
        elif r["market"] == "NZX" and r["ticker"] in BIG_NZX:
            reason = "large or dual-listed, only just outside the NZX 20"
        elif r["ticker"].upper() in excl:
            reason = "on Cam's excluded list"
        elif (key in HOLD_TICKERS or HOLD_WORDS.search(name)) and not confirmed:
            reason = "gaming, wagering and racing hold until Cam confirms his list"
        elif status and "liquidity" in status[2].lower() and status[1] == "quick look":
            reason = "failed the liquidity check at its quick look"
        elif e is None:
            reason = "no company data fetched yet"
        elif r["market"] == "ASX" and sum(1 for a in e.get("announcements") or []
                                          if a["date"] >= (date.fromisoformat(today) - timedelta(days=182)).isoformat()
                                          and MONTHLY_NTA.search(a["headline"])) >= 3:
            reason = "fund, trust or investment company"
        if reason is None and r["market"] == "ASX":
            k = (e.get("key-statistics") or {})
            rev = [num(x.get("revenue")) for x in (k.get("incomeStatement") or [])]
            inc = [num(x.get("netIncome")) for x in (k.get("incomeStatement") or [])]
            rev = [x for x in rev if x is not None]
            inc = [x for x in inc if x is not None]
            if rev and max(rev[:2]) < 10e6 and not any(x > 0 for x in inc):
                reason = "no business to value yet (revenue under A$10m and no profit in four years)"
        if reason is None and r["market"] == "NZX":
            reason = nzx_gate(e.get("info") or {})
        if reason:
            gated.append((r, reason))
            continue
        pts, why, flags, special, delist, facts = (score_asx if r["market"] == "ASX" else score_nzx)(r, e, ctx)
        if delist:
            gated.append((r, f"delisting ({delist[0]['date']}: {delist[0]['headline']})"))
            continue
        sp_index = status and re.search(r"special situation|indicative approach|partial takeover|control angle", status[2], re.I)
        if special or sp_index:
            routed.append((r, special[0] if special else None, status))
            continue
        row = {"market": r["market"], "ticker": r["ticker"], "name": name, "price": r["price"], "points": pts,
               "why": "; ".join(why), "flags": "; ".join(flags),
               "covered": f"{status[1]}, {status[0]}" if status else "", **facts}
        ranked.append(row)
    ranked.sort(key=lambda x: (-x["points"], x["market"], x["ticker"]))
    fields = ["market", "ticker", "name", "price", "points", "industry", "market_value_m", "pe", "price_to_book", "net_cash_share",
              "yield", "next_result", "director_notices", "spread", "why", "flags", "covered"]
    with open(os.path.join(root, "reports", "research_rank.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(ranked)
    L = ["# Research ranking", "",
         f"Run {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC on prices to {today}. Stage 2 of the research funnel (rulebook section 5a): "
         "it decides where research time goes, not what to buy. The points have no tested edge.", "",
         f"{len(screen)} on the screen: {len(gated)} dropped on rules, {len(routed)} sent to the special situations watch list, "
         f"{len(ranked)} ranked.", "",
         "Points: earnings (2 at 8 times or less, 1 at 12 or less), assets (2 at 0.7 times book or net tangible assets or less, 1 at 1.0), "
         "net cash (2 at 30% of market value, 1 at 10%), yield (1 at 6%, or 7% gross on the NZX), profit in each of four years (1), "
         "an index exit in nine months (2), small (1, under 250m), 35% or more below its high (1), 25 points worse than its industry "
         "over 12 months (1), a substantial holder leaving in six months (1); less 1 each for a recent raising, a loss, heavy debt, "
         "or 5% or more sold short. Director notices and the next result date are shown but don't score: nearly every company has "
         "both. ASX facts are the ASX's own company data (book is total assets less total liabilities, so it includes goodwill); "
         "NZX facts are the NZX instrument pages, which carry no announcements, industry or net cash, so NZX scores run lower and "
         "NZX names are ranked in their own table. Fact sheets go to the top 15 ASX and top 5 NZX names not yet covered.", ""]
    for mkt, top in (("ASX", 40), ("NZX", 25)):
        rows = [x for x in ranked if x["market"] == mkt]
        L += [f"## {mkt} ranked (top {min(top, len(rows))} of {len(rows)})", "",
              "| # | Share | Name | Points | Why it ranks | Red flags | Covered |", "| --- | --- | --- | --- | --- | --- | --- |"]
        for n, x in enumerate(rows[:top], 1):
            L.append(f"| {n} | {x['market']}:{x['ticker']} | {x['name'][:34]} | {x['points']} | {x['why']} | {x['flags']} | {x['covered']} |")
        L.append("")
    L += ["The full ranking is in reports/research_rank.csv.", "",
          "## Special situations watch list", "", "Not research picks under the current rules (a special situation type can be placed only once its "
          "history test passes); kept here for the 18 December review.", "", "| Share | Name | Why | Covered |", "| --- | --- | --- | --- |"]
    for r, a, status in sorted(routed, key=lambda z: (z[0]["market"], z[0]["ticker"])):
        why = f"{a['date']}: {a['headline']}" if a else (status[2][:140] if status else "")
        L.append(f"| {r['market']}:{r['ticker']} | {r['name'][:34]} | {why} | {status[1] + ', ' + status[0] if status else ''} |")
    L += ["", "## Dropped on rules", "", "| Reason | Count | Shares |", "| --- | --- | --- |"]
    by = {}
    for r, reason in gated:
        by.setdefault(re.sub(r" \(.*", "", reason), []).append(f"{r['market']}:{r['ticker']}")
    for reason, ts in sorted(by.items(), key=lambda z: -len(z[1])):
        L.append(f"| {reason} | {len(ts)} | {', '.join(ts[:40])}{' ...' if len(ts) > 40 else ''} |")
    q = queue(root, ranked, today)
    with open(os.path.join(root, "reports", "research_factsheet_queue.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["market", "ticker", "why", "points"])
        w.writeheader()
        w.writerows(q)
    names = {(r["market"], r["ticker"]): r["name"] for r in screen}
    L += ["", "## Next fact sheets (reports/research_factsheet_queue.csv)", "",
          "Watched companies with an event in the next 30 days first, then the top 15 ASX and top 5 NZX not yet covered, with at "
          "most three materials or energy companies and two property companies in a batch.", "", "| Share | Name | Why |", "| --- | --- | --- |"]
    for x in q:
        L.append(f"| {x['market']}:{x['ticker']} | {names.get((x['market'], x['ticker']), '')[:34]} | {x['why']} |")
    open(os.path.join(root, "reports", "research_rank.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"{len(screen)} on the screen: {len(gated)} dropped on rules, {len(routed)} special situations, {len(ranked)} ranked")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
