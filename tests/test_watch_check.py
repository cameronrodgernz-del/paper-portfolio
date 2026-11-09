"""Checks for the research watch list (src/watch_check.py)."""
import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))
import watch_check as w  # noqa: E402

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail and not ok else ""))
    if not ok:
        FAILS.append(name)


with tempfile.TemporaryDirectory() as d:
    for sub in ("research", "reports", "data/prices/NZX", "data/prices/ASX", "data/research_data"):
        os.makedirs(os.path.join(d, sub))
    open(os.path.join(d, "research", "watch_triggers.csv"), "w").write(
        "market,ticker,company,trigger_price,currency,also_needs,source\n"
        "NZX,AAA,Alpha,1.00,NZD,x,f\nNZX,BBB,Beta,1.00,NZD,x,f\nASX,CCC,Gamma,2.00,AUD,x,f\nASX,DDD,Delta,1.00,AUD,x,f\n")
    open(os.path.join(d, "research", "watch_events.csv"), "w").write(
        "date,market,ticker,event,date_basis\n2026-11-10,NZX,AAA,result,announced\n2026-12-31,NZX,BBB,meeting,inferred\n")
    open(os.path.join(d, "data/prices/NZX/AAA.csv"), "w").write("date,close\n2026-11-05,1.10\n2026-11-06,0.99\n")
    open(os.path.join(d, "data/prices/NZX/BBB.csv"), "w").write("date,close\n2026-11-06,1.04\n")
    json.dump({"CCC": {"fetched": "2026-11-07T21:00:00+00:00", "header": {"priceLast": 2.5}}},
              open(os.path.join(d, "data/research_data/asx_company.json"), "w"))
    res = w.check(d, "2026-11-08")
    st = {r["ticker"]: r["state"] for r in res["rows"]}
    check("a close at or below the trigger is a hit", st["AAA"] == "HIT", st)
    check("within 5% of the trigger is near", st["BBB"] == "near", st)
    check("ASX falls back to the company data's last trade", st["CCC"] == "" and
          next(r for r in res["rows"] if r["ticker"] == "CCC")["price"] == 2.5, res["rows"])
    check("a share with no price says so", st["DDD"] == "no price", st)
    check("only events in the next 14 days are listed", [e["ticker"] for e in res["events"]] == ["AAA"], res["events"])
    text = open(w.write(d, res), encoding="utf-8").read()
    check("the report names the hit", "## Hit" in text and "NZX:AAA" in text.split("## Triggers")[0], text[:300])
    check("no close calls without an index", "## Close calls" not in text, text[:300])

    # close calls: deep dives under the one-at-a-time process, with their stage
    for sub in ("research/picks", "research/debate", "research/against"):
        os.makedirs(os.path.join(d, sub), exist_ok=True)
    open(os.path.join(d, "research/picks/INDEX.md"), "w").write(
        "| Ticker | Name | Date | Verdict | Status | Next |\n| --- | --- | --- | --- | --- | --- |\n"
        "| ASX:CCC | Gamma | 2026-11-09 | Deep dive 2026-11-09, wait | watching | x |\n"
        "| NZX:BBB | Beta | 2026-11-02 | Fact sheet | watching | x |\n"
        "| ASX:DDD | Delta | 2026-11-09 | Deep dive 2026-11-09, on the line | watching | x |\n")
    open(os.path.join(d, "research/debate/CCC.md"), "w").write("# x\n\n## Cam's decision\nNot yet made.\n")
    open(os.path.join(d, "research/against/DDD_prompt.md"), "w").write("prompt\n")
    res = w.check(d, "2026-11-08")
    cc = {r["ticker"]: r for r in res["close"]}
    check("only one-at-a-time deep dives are close calls", sorted(cc) == ["CCC", "DDD"], sorted(cc))
    check("an open debate waits on Cam", cc["CCC"]["stage"] == "debate open, waiting on Cam", cc["CCC"]["stage"])
    check("a filed prompt is not run", cc["DDD"]["stage"] == "case against filed, not run", cc["DDD"]["stage"])
    open(os.path.join(d, "research/debate/CCC.md"), "w").write("# x\n\n## Cam's decision\nWait for A$1.90\n")
    check("a decision shows", w.stage(d, "CCC") == "decided: Wait for A$1.90", w.stage(d, "CCC"))
    text = open(w.write(d, res), encoding="utf-8").read()
    check("the report shows close calls before the triggers",
          "## Close calls" in text and text.index("## Close calls") < text.index("## Triggers"), text[:400])

print("\nALL PASS" if not FAILS else f"\n{len(FAILS)} FAILED")
sys.exit(1 if FAILS else 0)
