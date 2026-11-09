"""Checks for the hub's research section (src/research_hub.py)."""
import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))
import research_hub as r  # noqa: E402

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail and not ok else ""))
    if not ok:
        FAILS.append(name)


# the write-up's blocks
b = r.md_blocks(["A first line", "wrapped on.", "", "- one", "- two", "  more", "", "1. first", "2. second", "",
                 "| A | B |", "| --- | --- |", "| x | **y** |", "", "Last."])
check("a wrapped paragraph joins", b[0] == {"p": "A first line wrapped on."}, b[0])
check("a bullet list, with a wrapped item", b[1] == {"ul": ["one", "two more"]}, b[1])
check("a numbered list", b[2] == {"ol": ["first", "second"]}, b[2])
check("a table drops its rule row", b[3] == {"table": {"head": ["A", "B"], "rows": [["x", "**y**"]]}}, b[3])
check("a paragraph after a table", b[4] == {"p": "Last."}, b[4])

# which stage decides where a company stands
v1 = ("Deep dive 2026-11-08 (research/picks/AIM.md): case for review as an ordinary pick. "
      "Red team 2026-11-08 (research/red_team/AIM.md): don't buy. All figures held")
check("a red team outranks the deep dive", r.current(v1) == ("rt", "don't buy. All figures held"), r.current(v1))
v2 = ("Special situation deep dive 2026-11-02 (research/picks/COF_SS.md): wait for a named event, no card. "
      "Earlier deep dive (research/picks/COF.md): don't buy on the business alone")
check("the current deep dive, not the earlier one", r.current(v2)[1].startswith("wait for a named event"), r.current(v2))
v3 = ("Red team 2026-11-08 (research/red_team/HLO.md), checked against the minimum (the deep dive had used a 9% bar): "
      "wait for the H1 result. Red team: bad 30% A$1.05")
check("a red team qualifier with brackets, and a later 'Red team:' is not a new stage",
      r.current(v3) == ("rt", "wait for the H1 result. Red team: bad 30% A$1.05"), r.current(v3))
v4 = ("Special situation deep dive 2026-11-08 (research/picks/NZ_SKC.md): wait for the sale process. "
      "Model review 2026-11-10 (research/positions/NZ_SKC.md): hold, don't add at NZ$0.70. Value NZ$0.76")
check("a model review outranks the deep dive", r.current(v4) == ("rv", "hold, don't add at NZ$0.70. Value NZ$0.76"), r.current(v4))
check("a model review gets its own label", r.why_parts(v4)[-1]["label"] == "Model review 10 Nov 2026", r.why_parts(v4))
check("a leading 'Red team:' counts", r.current("Red team: don't buy (research/red_team/SRV.md). A loss")[0] == "rt")
wp = r.why_parts("Fact sheet 2026-11-08 (research/facts/X.md): grade C. Special situation deep dive 2026-11-08 (research/picks/X.md): wait, no card")
check("the reasons split by stage, labelled, dates readable",
      wp == [{"label": "Fact sheet 8 Nov 2026", "text": "grade C."}, {"label": "Special situation deep dive 8 Nov 2026", "text": "wait, no card"}], wp)
check("a quick look is one unlabelled part", r.why_parts("Dropped at the quick look: dear") == [{"label": "", "text": "dear"}])
check("a quick look drops its lead", r.current("Dropped at the quick look: 31 times profit") == ("", "31 times profit"))
check("file references come out of the reasons", r.plain_why("Fact sheet (research/facts/X.md, note 9): grade C") == "Fact sheet: grade C")
check("the first sentence is at least 40 characters",
      r.first_sentence("Grade C. The gap if it goes our way is 13%. Next thing") == "Grade C. The gap if it goes our way is 13%.")

# a small repository
with tempfile.TemporaryDirectory() as d:
    for sub in ("research/picks", "research/facts", "research/red_team", "research/cards", "reports", "data/prices/NZX"):
        os.makedirs(os.path.join(d, sub))
    rows = [
        ("ASX:AAA", "Alpha", "2026-11-08", "Deep dive 2026-11-08 (research/picks/AAA.md): wait for the result, no card", "watching"),
        ("ASX:BBB", "Beta", "2026-11-08", "Deep dive 2026-11-08 (research/picks/BBB.md): no case. Priced like peers", "watching"),
        ("NZX:CCC", "Gamma", "2026-11-08", "Fact sheet 2026-11-08 (research/facts/NZ_CCC.md): grade A. A question?", "watching"),
        ("ASX:DDD", "Delta", "2026-11-01", "Dropped at the quick look: 31 times profit", "rejected"),
        ("NZX:EEE", "Epsilon", "2026-11-08", "Deep dive 2026-11-08 (research/picks/NZ_EEE.md): no case", "watching"),
        ("ASX:FFF", "Phi", "2026-11-08", "Fact sheet 2026-11-08 (research/facts/FFF.md): grade B. Waits", "fact sheet"),
    ]
    with open(os.path.join(d, "research/picks/INDEX.md"), "w") as f:
        f.write("# Index\n\n| Ticker | Name | Date | Verdict | Status | Next dated event |\n| --- | --- | --- | --- | --- | --- |\n")
        for t in rows:
            f.write("| " + " | ".join(t) + " | next |\n")
        f.write("\n## Notes\n1. A note | with a pipe.\n")
    for p in ("research/picks/AAA.md", "research/picks/BBB.md", "research/picks/NZ_EEE.md", "research/picks/TEMPLATE.md"):
        open(os.path.join(d, p), "w").write("# x\n")
    open(os.path.join(d, "research/facts/NZ_CCC.md"), "w").write("# x\n\n## 7. Grade\nA, deep dive now.\n")
    open(os.path.join(d, "research/facts/FFF.md"), "w").write("# x\n\n## 7. Grade\n**B**, later.\n")
    open(os.path.join(d, "research/facts/TEMPLATE.md"), "w").write("# x\n\n## 7. Grade\n- A, deep dive now\n")
    open(os.path.join(d, "research/red_team/BBB.md"), "w").write("# x\n")
    open(os.path.join(d, "research/red_team/MEI-2026-11-02.md"), "w").write("# a deal review\n")
    json.dump({"sleeve": "deal", "market": "ASX", "ticker": "MEI"}, open(os.path.join(d, "research/cards/a.json"), "w"))
    open(os.path.join(d, "research/watch_triggers.csv"), "w").write(
        "market,ticker,company,trigger_price,currency,also_needs,source\nNZX,EEE,Epsilon,1.00,NZD,guidance held,research/picks/NZ_EEE.md\n")
    open(os.path.join(d, "research/watch_events.csv"), "w").write(
        "date,market,ticker,event,date_basis\n2026-11-01,ASX,AAA,old,announced\n2027-02-01,ASX,AAA,result,inferred\n")
    open(os.path.join(d, "data/prices/NZX/EEE.csv"), "w").write("date,close\n2026-11-06,1.04\n")
    open(os.path.join(d, "reports/research_rank.md"), "w").write(
        "# Research ranking\n\nRun 2026-11-08 02:42 UTC.\n\n534 on the screen: 272 dropped on rules, 27 sent to the special situations watch list, 235 ranked.\n")
    open(os.path.join(d, "research/summary.md"), "w").write("# The write-up\n\nIntro.\n\n## Where it stands\n\n- Nothing bought.\n")
    s = r.section(d, "2026-11-08")
    by = {c["ticker"]: c for c in s["companies"]}
    check("index rows read, notes ignored", len(s["companies"]) == 6, [c["ticker"] for c in s["companies"]])
    check("a deep dive that waits", by["AAA"]["landed"] == "wait" and by["AAA"]["stage"] == "Deep dive", by["AAA"])
    check("a red team file sets the stage", by["BBB"]["stage"] == "Red team" and by["BBB"]["landed"] == "nocase", by["BBB"])
    check("an A grade with no deep dive is to do", by["CCC"]["landed"] == "todo" and by["CCC"]["grade"] == "A", by["CCC"])
    check("a rejected row is dropped", by["DDD"]["landed"] == "dropped" and by["DDD"]["stage"] == "Quick look", by["DDD"])
    check("a share on the watch list lands there", by["EEE"]["landed"] == "trigger" and by["EEE"]["trigger"] == 1.0, by["EEE"])
    check("a B grade in bold is read", by["FFF"]["grade"] == "B" and by["FFF"]["landed"] == "wait", by["FFF"])
    check("files link to the repository", by["CCC"]["files"].get("facts", "").endswith("research/facts/NZ_CCC.md"), by["CCC"]["files"])
    f = s["funnel"]
    check("the screen's counts", (f["screen"], f["rules"], f["special"], f["ranked"]) == (534, 272, 27, 235), f)
    check("fact sheets and grades leave out the template", f["fact_sheets"] == 2 and f["grades"] == {"A": 1, "B": 1, "C": 0}, f)
    check("deep dives leave out the index and template", f["deep_dives"] == 3, f)
    check("red teams leave out deal reviews", f["red_teams"] == 1, f)
    check("only research cards count", f["cards"] == 0 and s["cards"] == [], s["cards"])
    w = s["watch"][0]
    check("the watch list carries the gap and name", w["name"] == "Epsilon" and abs(w["gap"] - 0.04) < 1e-9 and w["state"] == "near", w)
    check("past events are left out", [e["event"] for e in s["events"]] == ["result"], s["events"])
    check("the write-up's sections", s["summary"]["sections"][0]["h"] == "Where it stands" and
          s["summary"]["sections"][0]["blocks"] == [{"ul": ["Nothing bought."]}], s["summary"])
    check("the section is JSON", len(json.dumps(s)) > 0)

print(f"\n{len(FAILS)} failed" if FAILS else "\nall passed")
sys.exit(1 if FAILS else 0)
