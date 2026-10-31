"""Checks for folding deal files into the live list (src/deal_files.py) and the card drafter
(src/card_draft.py)."""
import contextlib
import csv
import io
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
import deal_files as df  # noqa: E402
import card_draft as cd  # noqa: E402

fails = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail and not ok else ""))
    if not ok:
        fails.append(name)


LIVE = ("deal_id,target_market,target_ticker,structure,cash_per_share,cash_ccy,scrip_ratio,acquirer_market,"
        "acquirer_ticker,undisturbed,announce_date,expected_payment,terms_note\n"
        "AU-2026-01,ASX,OLDD,scheme,2.00,AUD,0,,,1.50,2026-09-01,2026-12-15,A$2.00 cash\n")
DB_HEAD = ("deal_id,market,target_name,target_ticker,bidder_name,structure,consideration_type,currency,announce_date,"
           "undisturbed_price,undisturbed_basis,offer_price_initial,board_recommendation,intentions_pct,meeting_date,"
           "end_date,outcome,notes\n")


def deal_file(tk, extra=""):
    return ("---\n"
            f"ticker: {tk}\nmarket: ASX\ndeal_id:\ntarget: {tk} Limited\nbidder: Big Co\nstructure: scheme\n"
            "consideration: A$1.04 cash per share, less any permitted dividend. No scrip.\n"
            "cash_per_share: 1.04\nscrip_ratio: 0\nacquirer_ticker:\ncurrency: AUD\nannounce_date: 2026-10-19\n"
            "meeting_date: 2027-01-22\nsecond_court_date: 2027-01-29   # indicative\nimplementation_date: 2027-02-10\n"
            "end_date: 2027-04-18\nstage: announced\nboard: Unanimous recommendation\nintentions_pct: 34.0\n"
            "conditions_open: Independent expert, shareholder approval, court approval\nlast_checked: 2026-11-01\n"
            + extra + "---\n## In short\nText.\n")


def run(root, **kw):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        df.main(root, **kw)
    return out.getvalue()


with tempfile.TemporaryDirectory() as root:
    for d in ("config", "deals/au", "research/deals", "data/prices/ASX", "reports"):
        os.makedirs(os.path.join(root, d))
    open(os.path.join(root, "config", "live_deals.csv"), "w").write(LIVE)
    open(os.path.join(root, "deals", "au", "au_deals_2025_2026.csv"), "w").write(DB_HEAD + "AU-2026-24,ASX,Other,OTH,X,scheme,cash,AUD,2026-10-01,1,,1.2,,,,,completed,\n")
    open(os.path.join(root, "deals", "all_deals.csv"), "w").write(DB_HEAD + "AU-2026-24,ASX,Other,OTH,X,scheme,cash,AUD,2026-10-01,1,,1.2,,,,,completed,\n")
    with open(os.path.join(root, "data", "prices", "ASX", "NEWD.csv"), "w") as f:
        f.write("date,open,high,low,close,volume\n2026-10-15,0.57,0.57,0.57,0.575,100\n2026-10-16,0.57,0.57,0.54,0.54,100\n2026-10-19,1,1.01,0.98,1.0,100\n")
    open(os.path.join(root, "research", "deals", "OLDD.md"), "w").write(deal_file("OLDD").replace("stage: announced", "stage: booklet_out"))
    open(os.path.join(root, "research", "deals", "NEWD.md"), "w").write(deal_file("NEWD"))
    open(os.path.join(root, "research", "deals", "GONE.md"), "w").write(deal_file("GONE").replace("stage: announced", "stage: terminated"))

    out = run(root)
    check("without --add a new deal file is reported, not added", "NEWD" in out and "--add" in out, out)
    rows = list(csv.DictReader(open(os.path.join(root, "config", "live_deals.csv"))))
    check("without --add the live list keeps one row", len(rows) == 1, len(rows))
    old = rows[0]
    check("the stage comes from the file", old["stage"] == "booklet_out", old.get("stage"))
    check("the second court date comes from the file, with the comment stripped", old["court_date"] == "2027-01-29", old.get("court_date"))
    check("the payment date comes from the implementation date", old["expected_payment"] == "2027-02-10", old.get("expected_payment"))
    check("the terms already on the row are kept", old["cash_per_share"] == "2.00" and old["undisturbed"] == "1.50", old)
    check("commas in the open conditions don't break the CSV", ";" in old["conditions_open"] and "," not in old["conditions_open"], old["conditions_open"])

    out = run(root, add=True)
    rows = list(csv.DictReader(open(os.path.join(root, "config", "live_deals.csv"))))
    new = next((r for r in rows if r["target_ticker"] == "NEWD"), None)
    check("--add puts the new deal on the live list", new is not None, out)
    check("a terminated deal file is never added", not any(r["target_ticker"] == "GONE" for r in rows), [r["target_ticker"] for r in rows])
    if new:
        check("the new deal gets the next id for its year", new["deal_id"] == "AU-2026-25", new["deal_id"])
        check("the undisturbed price is the last close before the announcement", new["undisturbed"] == "0.54", new["undisturbed"])
        check("the new row gets the file's dates on the same run", new["meeting_date"] == "2027-01-22" and new["court_date"] == "2027-01-29", new)
        check("the terms note is short", new["terms_note"] == "A$1.04 cash per share; less dividends", new["terms_note"])
    db = list(csv.DictReader(open(os.path.join(root, "deals", "au", "au_deals_2025_2026.csv"))))
    pend = [r for r in db if r["target_ticker"] == "NEWD"]
    check("a pending row is added to the database part", len(pend) == 1 and pend[0]["outcome"] == "pending", pend)
    if pend:
        check("the database row carries the board and intentions", pend[0]["board_recommendation"] == "unanimous_for" and pend[0]["intentions_pct"] == "34.0", pend[0])
    out = run(root, add=True)
    check("a second run changes nothing", out.strip() == "no changes", out)
    check("a second run adds no database row", sum(r["target_ticker"] == "NEWD" for r in csv.DictReader(open(os.path.join(root, "deals", "au", "au_deals_2025_2026.csv")))) == 1)

    with open(os.path.join(root, "reports", "deal_monitor.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ticker", "offer_value", "break_price", "base_rate", "base_note", "market_implied"])
        w.writerow(["NEWD", "1.04", "0.55", "0.9", "schemes at announcement", "0.93"])
    card = cd.draft(root, "NEWD")
    check("the draft card is marked as a draft", card.get("draft") is True)
    check("the draft card's chances add to 1", abs(card["outcomes"][0][0] + card["outcomes"][1][0] - 1) < 1e-9, card["outcomes"])
    check("the draft card uses the monitor's break price", card["break_price"] == 0.55, card["break_price"])
    check("the draft card resolves on the payment date", card["resolve_by"] == "2027-02-10", card["resolve_by"])
    check("the draft card lists the open conditions as prompts", any("court approval" in a for a in card["adjustments"]), card["adjustments"])
    check("the draft card leaves the thesis to write", "TO WRITE" in card["thesis"])

print(f"\n{'all passed' if not fails else str(len(fails)) + ' failed'}")
sys.exit(1 if fails else 0)
