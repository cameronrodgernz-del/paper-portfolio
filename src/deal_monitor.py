"""Live deal monitor: what each pending deal's price says, against the base rates.

For each deal in config/live_deals.csv:
- offer value now = cash + scrip ratio x the acquirer's last close (in the target's currency);
- gross spread = offer value / target's last close - 1, and its yearly rate to the expected payment date;
- market-implied completion chance = (price - break price) / (offer - break price), where the break
  price is the undisturbed price (a deal that fails tends to fall back towards it);
- base-rate completion chance from the deal database for the same structure.
A gap between the two chances is where an edge might be; it is a prompt for the analyst, not a trade.
Usage: python3 -I src/deal_monitor.py <repo_root>
"""
import csv
import os
import sys
from datetime import date, datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from market_data import FX, Prices  # noqa: E402

RESOLVED = {"completed", "terminated", "withdrawn", "lapsed", "superseded_by_rival"}


def base_rate(root: str, structure: str) -> tuple[float, int]:
    path = os.path.join(root, "deals", "all_deals.csv")
    if not os.path.exists(path):
        return float("nan"), 0
    rows = [r for r in csv.DictReader(open(path, encoding="utf-8")) if r["majority_buyout"] == "N"
            and r["outcome"] in RESOLVED and r["structure"] == structure]
    return (sum(1 for r in rows if r["outcome"] == "completed") / len(rows) if rows else float("nan")), len(rows)


def us_section(root: str, prices: Prices, today: str, now: datetime) -> list[str]:
    """US leads: companies with recent merger filings, the cash price found in the filing text, and
    the spread to the last close. The price is a lead to confirm from the filing, not a term."""
    path = os.path.join(root, "data", "sec", "us_deal_targets.csv")
    if not os.path.exists(path):
        return []
    out, rows = [], []
    for r in csv.DictReader(open(path, encoding="utf-8")):
        lead = r.get("cash_price_lead") or ""
        if not r.get("ticker") or not lead or lead.startswith("error"):
            continue
        px = prices.last_close("US", r["ticker"], today, now)
        if not px:
            continue
        rows.append((float(lead) / px - 1, r, px))
    if not rows:
        return ["", "## US leads", "", "No US deal targets with prices yet."]
    out += ["", "## US leads from SEC merger filings", "",
            "Cash price per share found in the latest filing's text, against the last close. "
            "A spread far from the usual few per cent usually means the lead is wrong (a different price in the text, "
            "a stock-and-cash deal, or a bidding contest), so confirm from the filing before any use.", "",
            "| Ticker | Company | Cash lead | Last close | Gross spread | First filing | Latest filing | Forms |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for g, r, px in sorted(rows, key=lambda x: -x[0]):
        flag = " (check)" if g < -0.02 or g > 0.25 else ""
        out.append(f"| {r['ticker']} | {r['company'][:38]} | {float(r['cash_price_lead']):.2f} | {px:.2f} | {g:+.1%}{flag} | "
                   f"{r['first_seen']} | {r['latest']} | {r['forms']} |")
    return out


def main(root: str) -> int:
    data = os.path.join(root, "data")
    prices, fx = Prices(data), FX(data)
    today = date.today().isoformat()
    now = datetime.now(timezone.utc)
    lines = ["# Live deal monitor", "", f"Run {today}. Prices are the last closes in the repository; a blank means no price yet.", "",
             "| Deal | Price | Offer value | Gross spread | Days to payment | Yearly rate | Market-implied chance | Base-rate chance | Note |",
             "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for d in csv.DictReader(open(os.path.join(root, "config", "live_deals.csv"), encoding="utf-8")):
        px = prices.last_close(d["target_market"], d["target_ticker"], today, now)
        cash = float(d["cash_per_share"] or 0)
        if d["cash_ccy"] == "USD":
            cash *= fx.per_nzd("AUD", today) / fx.per_nzd("USD", today)      # A$ per US$
        ratio = float(d["scrip_ratio"] or 0)
        acq = prices.last_close(d["acquirer_market"], d["acquirer_ticker"], today, now) if ratio else 0.0
        offer = cash + ratio * acq if (ratio == 0 or acq) else None
        brk = float(d["undisturbed"]) if d["undisturbed"] else None
        p_base, n = base_rate(root, d["structure"])
        days = (date.fromisoformat(d["expected_payment"]) - date.today()).days
        if px and offer:
            gross = offer / px - 1
            yearly = (1 + gross) ** (365 / max(days, 1)) - 1 if days > 0 else float("nan")
            implied = (px - brk) / (offer - brk) if brk and offer > brk else float("nan")
            cells = [f"{px:.3f}", f"{offer:.3f}", f"{gross:+.1%}", str(days), f"{yearly:+.1%}",
                     "" if implied != implied else f"{implied:.0%}"]
        else:
            cells = ["" if not px else f"{px:.3f}", "" if not offer else f"{offer:.3f}", "", str(days), "", ""]
        lines.append(f"| {d['target_ticker']} ({d['deal_id']}) | " + " | ".join(cells) +
                     f" | {p_base:.0%} of {n} {d['structure']}s | {d['terms_note']} |")
    lines += ["", "The base rate is for all resolved deals of the same structure in the database. "
              "The analyst adjusts it for this deal's conditions and records each adjustment before any entry."]
    lines += us_section(root, prices, today, now)
    os.makedirs(os.path.join(root, "reports"), exist_ok=True)
    open(os.path.join(root, "reports", "deal_monitor.md"), "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
