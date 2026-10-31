"""Draft a deal decision card from the live list, the deal monitor and the deal file, so every card
starts from the same numbers and only the judgement is the analyst's.

Fills in: market, ticker, sleeve, side; the offer as the completion price (cash plus scrip at the
acquirer's last close, as the monitor values it); the monitor's break price (the undisturbed price
moved by the market); the base rate for the deal's stage, and the same number as the starting chance
of completion; the expected payment date as resolve_by; the standard exit rule; the group (the
regulator the deal waits on, else the bidder) from the deal file; and the deal file's open
conditions as prompts in "adjustments".

Leaves for the analyst: the thesis, the industry, every adjustment to the chance (each one written
down with its reason), and any change to the outcomes. The draft is marked "draft": true, which
decide.py doesn't read, and it is written to research/cards/draft-<date>-<TICKER>.json; the analyst
saves the finished card as research/cards/<date>-<TICKER>.json.
Usage: python3 -I src/card_draft.py <repo_root> <TICKER>
"""
import csv
import json
import os
import re
import sys
from datetime import date

GROUPS = ("ACCC", "FIRB", "OIO", "ComCom", "HSR", "SAMR", "CFIUS")


def read(path: str) -> list[dict]:
    return list(csv.DictReader(open(path, encoding="utf-8", newline=""))) if os.path.exists(path) else []


def header(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    m = re.match(r"^---\n(.*?)\n---\n", open(path, encoding="utf-8").read(), re.S)
    out = {}
    for line in (m.group(1).splitlines() if m else []):
        if ":" in line and not line.startswith((" ", "#")):
            k, v = line.split(":", 1)
            v = re.sub(r"\s+#.*$", "", v).strip()
            if v:
                out[k.strip()] = v
    return out


def draft(root: str, ticker: str) -> dict:
    ticker = ticker.upper()
    live = next((r for r in read(os.path.join(root, "config", "live_deals.csv")) if r["target_ticker"].upper() == ticker), None)
    if not live:
        raise SystemExit(f"{ticker} isn't on the live list (config/live_deals.csv)")
    mon = next((r for r in read(os.path.join(root, "reports", "deal_monitor.csv")) if r["ticker"].upper() == ticker), None)
    if not mon:
        raise SystemExit(f"{ticker} has no row in reports/deal_monitor.csv: run python3 -I src/deal_monitor.py . first")
    mk = live["target_market"]
    f = header(os.path.join(root, "research", "deals", (f"NZ_{ticker}" if mk == "NZX" else ticker) + ".md"))
    offer = float(mon["offer_value"])
    brk = float(mon["break_price"]) if mon.get("break_price") else None
    p = round(float(mon["base_rate"]), 2)
    regs = f.get("regulators", "") + " " + live.get("terms_note", "")
    group = next((g for g in GROUPS if g.lower() in regs.lower()), None) or (f.get("bidder") or "").split("(")[0].strip()[:40]
    prompts = [f"open condition: {c.strip()}" for c in (f.get("conditions_open") or live.get("conditions_open") or "").split(";") if c.strip()]
    card = {
        "draft": True,
        "sleeve": "deal", "market": mk, "ticker": ticker, "side": "buy",
        "thesis": "TO WRITE: why the market's price is wrong, in two or three sentences, with the evidence",
        "outcomes": [[p, round(offer, 4)], [round(1 - p, 2), round(brk, 4) if brk else None]],
        "complete_price": round(offer, 4), "break_price": round(brk, 4) if brk else None,
        "resolve_by": live.get("expected_payment"),
        "exit_rule": "exit on completion, break, or a rival bid (fresh decision)",
        "industry": "TO SET",
        "group": group,
        "base_rate": float(mon["base_rate"]),
        "base_note": mon.get("base_note", ""),
        "adjustments": prompts + ["TO WRITE: each adjustment to the chance, with its reason and size in points (or none)"],
        "market_implied_now": float(mon["market_implied"]) if mon.get("market_implied") else None,
        "limit": None, "value_nzd": None,
    }
    if brk is None:
        card["outcomes"][1][1] = None
        card["adjustments"].insert(0, "TO SET: no break price in the monitor (no undisturbed price on the live list): set one from the evidence")
    return card


def main(root: str, ticker: str) -> int:
    card = draft(root, ticker)
    out = os.path.join(root, "research", "cards", f"draft-{date.today().isoformat()}-{ticker.upper()}.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(card, open(out, "w"), indent=1)
    print(json.dumps(card, indent=1))
    print("written:", os.path.relpath(out, root))
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit("usage: python3 -I src/card_draft.py <repo_root> <TICKER>")
    sys.exit(main(sys.argv[1], sys.argv[2]))
