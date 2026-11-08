"""The research section of the hub snapshot: the write-up, the funnel, the watch list, the dated
events and every company the research desk has looked at, read from the files the desk keeps.

  research/summary.md          the write-up, as sections of paragraphs, lists and tables
  research/picks/INDEX.md      one row per company: date, verdict, status, next event
  research/facts, picks, red_team, cards   which stage each company reached
  research/watch_triggers.csv, watch_events.csv   the watch list (prices via src/watch_check.py)
  reports/research_rank.md     the screen's counts

Nothing here judges a company; it only arranges what the files say. Used by src/hub_export.py.
"""
import csv
import glob
import json
import os
import re
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import watch_check  # noqa: E402

REPO = "https://github.com/cameronrodgernz-del/paper-portfolio/blob/main/"
LANDED = {"trigger": "Watch list", "wait": "Waiting for an event", "todo": "Deep dive to do",
          "nocase": "No case", "dropped": "Dropped", "card": "Card written"}
FILE_RE = re.compile(r"((?:research/(?:facts|picks|red_team)|reports)/[A-Za-z0-9_\-]+\.md)")


# ---------- the write-up ----------
def inline(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def md_blocks(lines: list[str]) -> list[dict]:
    """Paragraphs, bullet lists, numbered lists and pipe tables; anything else reads as a paragraph."""
    out, i = [], 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1
            continue
        if ln.lstrip().startswith("|"):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                    rows.append([inline(c) for c in cells])
                i += 1
            if rows:
                out.append({"table": {"head": rows[0], "rows": rows[1:]}})
            continue
        m = re.match(r"\s*(?:[-*]|(\d+)\.)\s+(.*)", ln)
        if m:
            kind = "ol" if m.group(1) else "ul"
            items = []
            while i < len(lines):
                m2 = re.match(r"\s*(?:[-*]|(\d+)\.)\s+(.*)", lines[i])
                if m2 and ("ol" if m2.group(1) else "ul") == kind:
                    items.append(m2.group(2))
                elif lines[i].strip() and not lines[i].lstrip().startswith("|") and items and lines[i].startswith((" ", "\t")):
                    items[-1] += " " + lines[i].strip()            # a wrapped item
                else:
                    break
                i += 1
            out.append({kind: [inline(x) for x in items]})
            continue
        para = []
        while i < len(lines) and lines[i].strip() and not lines[i].lstrip().startswith("|") \
                and not re.match(r"\s*(?:[-*]|\d+\.)\s+", lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append({"p": inline(" ".join(para))})
    return out


def summary(root: str) -> dict:
    p = os.path.join(root, "research", "summary.md")
    if not os.path.exists(p):
        return {}
    title, intro, secs, cur = "", [], [], None
    for ln in open(p, encoding="utf-8").read().splitlines():
        if ln.startswith("# ") and not title:
            title = ln[2:].strip()
        elif ln.startswith("## "):
            cur = {"h": ln[3:].strip(), "lines": []}
            secs.append(cur)
        else:
            (cur["lines"] if cur else intro).append(ln)
    return {"title": title, "intro": md_blocks(intro),
            "sections": [{"h": s["h"], "blocks": md_blocks(s["lines"])} for s in secs], "path": REPO + "research/summary.md"}


# ---------- the companies ----------
def index_rows(root: str) -> list[dict]:
    p = os.path.join(root, "research", "picks", "INDEX.md")
    rows = []
    if not os.path.exists(p):
        return rows
    for ln in open(p, encoding="utf-8"):
        if not ln.startswith("| ") or ln.startswith("| Ticker") or ln.startswith("| ---"):
            continue
        c = [x.strip() for x in ln.strip().strip("|").split(" | ")]
        if len(c) != 6 or ":" not in c[0]:
            continue
        mkt, tk = c[0].split(":", 1)
        rows.append({"market": mkt, "ticker": tk, "name": c[1], "date": c[2], "verdict": c[3], "status": c[4], "next": c[5]})
    return rows


def stem(market: str, ticker: str) -> str:
    return ("NZ_" if market == "NZX" else "") + ticker


def grade_of(path: str) -> str | None:
    if not os.path.exists(path):
        return None
    m = re.search(r"^## 7\. Grade\s*\n+\s*\**([ABC])\b", open(path, encoding="utf-8").read(), re.M)
    return m.group(1) if m else None


SEG = re.compile(
    r"(?P<dd>(?:Earlier |Value-pick |Special situation |Special-situation )?[Dd]eep dive(?: \d{4}-\d\d-\d\d)? \(research/picks/[^)]*\)(?:, as [^:]{0,80})?:)"
    r"|(?P<rt>Red team \d{4}-\d\d-\d\d(?: \(research/red_team/[^)]*\))?(?:, [^:]{0,160})?:|^Red team:)"
    r"|(?P<tr>Special situation triage \d{4}-\d\d-\d\d \(reports/[^)]*\):)"
    r"|(?P<fs>Fact sheet \d{4}-\d\d-\d\d \(research/facts/[^)]*\):)")
LEAD = re.compile(r"^(?:Dropped at the quick look(?: \([^)]*\))?:|Dropped:)\s*")


def current(verdict: str) -> tuple[str, str]:
    """(kind, text) of the stage that decides where a company stands: the last red team, else the first deep dive
    (an 'Earlier deep dive' comes after the current one), else the last fact sheet or triage, else the whole line."""
    ms = list(SEG.finditer(verdict))
    segs = [(m.lastgroup, verdict[m.end():ms[i + 1].start() if i + 1 < len(ms) else len(verdict)].strip()) for i, m in enumerate(ms)]
    for kind in ("rt",):
        hits = [x for x in segs if x[0] == kind]
        if hits:
            return hits[-1]
    hits = [x for x in segs if x[0] == "dd"]
    if hits:
        return hits[0]
    if segs:
        return segs[-1]
    return "", LEAD.sub("", verdict).strip()


def plain_why(verdict: str) -> str:
    """The index verdict without its file references and batch notes, which the page shows as links."""
    s = re.sub(r"\s*\((?:research|reports)/[^)]*\)", "", verdict)
    return re.sub(r"\s{2,}", " ", s).strip()


def first_sentence(s: str, at_least: int = 40, at_most: int = 260) -> str:
    for m in re.finditer(r"[.;](?=\s+[A-Z(])", s):
        if m.start() >= at_least:
            return s[:m.start() + 1] if m.start() < at_most else s[:at_most].rsplit(" ", 1)[0] + "…"
    return s if len(s) <= at_most else s[:at_most].rsplit(" ", 1)[0] + "…"


def companies(root: str, triggers: dict, cards: set) -> list[dict]:
    out = []
    for r in index_rows(root):
        st = stem(r["market"], r["ticker"])
        files = {}
        for kind in ("facts", "picks", "red_team"):
            p = os.path.join("research", kind, st + ".md")
            if os.path.exists(os.path.join(root, p)):
                files[kind] = p
        for p in FILE_RE.findall(r["verdict"]):               # files named in the verdict (COF_SS.md, the triage reports)
            if os.path.exists(os.path.join(root, p)):
                kind = p.split("/")[1] if p.startswith("research/") else "report"
                files.setdefault(kind, p)
        grade = grade_of(os.path.join(root, files["facts"])) if "facts" in files else None
        if not grade:
            m = re.search(r"\bgrade ([ABC])\b", r["verdict"])
            grade = m.group(1) if m else None
        v = r["verdict"]
        kind, cur = current(v)
        if "red_team" in files:
            stage = "Red team"
        elif "picks" in files:
            stage = "Deep dive"
        elif "facts" in files:
            stage = "Fact sheet"
        elif v.lower().startswith("special situation triage") or "report" in files:
            stage = "Triage"
        else:
            stage = "Quick look"
        key = (r["market"], r["ticker"])
        if key in cards:
            landed = "card"
        elif key in triggers:
            landed = "trigger"
        elif r["status"] == "rejected":
            landed = "dropped"
        elif "picks" in files or "red_team" in files:
            landed = "wait" if re.match(r"[^.]*\bwait\b", cur.lower()) else "nocase"
        elif grade == "A" and stage == "Fact sheet":
            landed = "todo"
        else:
            landed = "wait"
        why = plain_why(v)
        head = first_sentence(plain_why(cur))
        head = head[:1].upper() + head[1:]
        out.append({"market": r["market"], "ticker": r["ticker"], "name": r["name"], "date": r["date"], "stage": stage,
                    "grade": grade, "landed": landed, "status": r["status"], "head": head, "why": why,
                    "next": r["next"], "files": {k: REPO + p for k, p in files.items()},
                    "trigger": triggers.get(key)})
    return out


# ---------- the funnel ----------
def screen_counts(root: str) -> dict:
    p = os.path.join(root, "reports", "research_rank.md")
    if not os.path.exists(p):
        return {}
    txt = open(p, encoding="utf-8").read()
    m = re.search(r"(\d+) on the screen: (\d+) dropped on rules, (\d+) sent to the special situations watch list, (\d+) ranked", txt)
    run = re.search(r"Run (\d{4}-\d\d-\d\d)", txt)
    if not m:
        return {}
    return {"screen": int(m.group(1)), "rules": int(m.group(2)), "special": int(m.group(3)), "ranked": int(m.group(4)),
            "run": run.group(1) if run else None}


def research_cards(root: str) -> list[dict]:
    out = []
    for p in sorted(glob.glob(os.path.join(root, "research", "cards", "*.json"))):
        try:
            c = json.load(open(p, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if c.get("sleeve") == "research":
            out.append({"market": c.get("market"), "ticker": c.get("ticker"), "status": c.get("status"),
                        "file": REPO + os.path.relpath(p, root)})
    return out


def funnel(root: str, rows: list[dict], cards: list[dict]) -> dict:
    facts = [p for p in glob.glob(os.path.join(root, "research", "facts", "*.md"))
             if os.path.basename(p) != "TEMPLATE.md" and re.fullmatch(r"(NZ_)?[A-Z0-9]+\.md", os.path.basename(p))]
    grades = {"A": 0, "B": 0, "C": 0}
    for p in facts:
        g = grade_of(p)
        if g:
            grades[g] += 1
    picks = [p for p in glob.glob(os.path.join(root, "research", "picks", "*.md")) if os.path.basename(p) not in ("INDEX.md", "TEMPLATE.md")]
    rts = [p for p in glob.glob(os.path.join(root, "research", "red_team", "*.md")) if re.fullmatch(r"(NZ_)?[A-Z0-9]+\.md", os.path.basename(p))]
    landed = {k: sum(1 for r in rows if r["landed"] == k) for k in LANDED}
    return {**screen_counts(root), "looked_at": len(rows), "quick_looks": sum(1 for r in rows if r["stage"] == "Quick look"),
            "triage": sum(1 for r in rows if r["stage"] == "Triage"), "fact_sheets": len(facts), "grades": grades,
            "deep_dives": len(picks), "red_teams": len(rts), "cards": len(cards), "landed": landed,
            "markets": {m: sum(1 for r in rows if r["market"] == m) for m in ("ASX", "NZX")}}


# ---------- all of it ----------
def section(root: str, today: str | None = None) -> dict:
    today = today or date.today().isoformat()
    names = {(r["market"], r["ticker"]): r["name"] for r in index_rows(root)}
    try:
        wc = watch_check.check(root, today)
    except (OSError, KeyError, ValueError):
        wc = {"rows": []}
    watch, triggers = [], {}
    for t in wc["rows"]:
        key = (t["market"], t["ticker"])
        level = float(t["trigger_price"])
        triggers[key] = level
        watch.append({"market": t["market"], "ticker": t["ticker"], "name": names.get(key) or t.get("company"), "trigger": level,
                      "ccy": t["currency"], "price": t["price"], "price_date": t["price_date"], "gap": t["gap"],
                      "state": t["state"], "needs": t["also_needs"], "source": REPO + t["source"] if t.get("source") else None})
    watch.sort(key=lambda w: (w["gap"] is None, w["gap"] if w["gap"] is not None else 0))
    events = []
    evp = os.path.join(root, "research", "watch_events.csv")
    if os.path.exists(evp):
        for e in csv.DictReader(open(evp, encoding="utf-8")):
            if e["date"] >= today:
                events.append({"date": e["date"], "market": e["market"], "ticker": e["ticker"],
                               "name": names.get((e["market"], e["ticker"]), ""), "event": e["event"], "basis": e["date_basis"]})
    events.sort(key=lambda e: e["date"])
    cards = research_cards(root)
    rows = companies(root, triggers, {(c["market"], c["ticker"]) for c in cards})
    return {"as_of": today, "summary": summary(root), "funnel": funnel(root, rows, cards), "watch": watch, "events": events,
            "companies": rows, "cards": cards, "landed_names": LANDED, "repo": REPO}


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    s = section(root)
    print(json.dumps(s["funnel"], indent=1))
    print(len(json.dumps(s)) // 1024, "KB")
