"""Live deal monitor: what each pending deal's price says, against the base rates.

For each deal in config/live_deals.csv:
- offer value now = cash + scrip ratio x the acquirer's last close (in the target's currency);
- gross spread = offer value / target's last close - 1, and its yearly rate to the expected payment date;
- market-implied completion chance = (price - break price) / (offer - break price), where the break
  price is the undisturbed price moved by the market since the announcement (the target's local index
  fund, total return: VAS for ASX, ENZL in NZ dollars for NZX, VT for US), since a deal that fails falls
  back towards where the share would be without it, not where it was months ago;
- the starting chance from reports/deal_odds.json: the rate at which holders were paid in past deals
  of the same structure that reached the same stage (config/live_deals.csv `stage`), moved by the
  deal-feature model where it scored better out of sample, with less weight the further the deal is
  along (a deal past its vote is decided mostly by the stage);
- a late payment date: the latest stage reached (announced, booklet out, vote, court) plus the days
  three in four past deals of the same kind took from that stage to payment (reports/deal_odds.json,
  by approvals from announcement), when that is later than the expected date; and the yearly rate
  after costs if it pays then, so a thin spread that only works on time is plain;
- the expected return at the base rate: the value if the base rate is right (chance x offer value,
  plus the rest x the break price) against today's price, after costs, and its yearly rate, so a wide
  gap in the odds on a small upside doesn't outrank a better trade;
- the implied chance each day since the announcement (reports/deal_history.json), for the hub. Each
  night's figure is kept as it was worked out then, with the terms known then; only new days are
  added. Days before the record began ("_since") were worked out with the terms on that date, so a
  later change of terms shows from the day it was made. To rebuild a deal's record (a wrong row
  corrected), delete its entry.
A gap between the two chances is where an edge might be; it is a prompt for the analyst, not a trade.
Usage: python3 -I src/deal_monitor.py <repo_root>
"""
import bisect
import csv
import json
import math
import os
import sys
from datetime import date, datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "history"))
from market_data import FX, Prices  # noqa: E402

RESOLVED = {"completed", "terminated", "withdrawn", "lapsed", "superseded_by_rival"}
TYPICAL_STAKE_NZD = 3500      # about the size the 4% and 1%-on-break caps allow
FIXED_COSTS = {"fx": 0.005, "hedge": 0.001}   # currency conversion on entry, hedge dealing cost


STAGE_WEIGHT = {"announced": 1.0, "booklet_out": 0.75, "vote_passed": 0.25, "court_approved": 0.0, "unconditional": 0.0}
STAGE_KEY = {"unconditional": "court_approved", "implemented": "court_approved"}
STAGE_WORDS = {"announced": "announced", "booklet_out": "booklet out", "vote_passed": "past the vote", "court_approved": "court approved",
               "unconditional": "unconditional"}
INDEX = {"ASX": ("ASX", "VAS"), "NZX": ("US", "ENZL"), "US": ("US", "VT")}
MARKET_CCY = {"ASX": "AUD", "NZX": "NZD", "US": "USD"}


def acq_fx(fx: FX, live: dict, d: str) -> float:
    """Target-currency units per unit of the acquirer's currency on date d (1 when they match),
    so an acquirer listed elsewhere (OceanaGold on the NYSE for Ausgold) is valued in A$."""
    a, t = MARKET_CCY.get(live.get("acquirer_market") or "", ""), MARKET_CCY.get(live["target_market"], "")
    if not a or not t or a == t:
        return 1.0
    return fx.per_nzd(t, d) / fx.per_nzd(a, d)


def logit(p: float) -> float:
    p = min(max(p, 1e-4), 1 - 1e-4)
    return math.log(p / (1 - p))


def base_rate(root: str, structure: str, stage: str = "announced", deal: dict | None = None) -> tuple[float, int, str]:
    """The starting chance for a deal of this structure at this stage, moved by the feature model."""
    path = os.path.join(root, "reports", "deal_odds.json")
    if not os.path.exists(path):
        return float("nan"), 0, ""
    odds = json.load(open(path))
    st = STAGE_KEY.get(stage, stage)
    if structure == "full_takeover" and st == "vote_passed":
        st = "booklet_out"
    key = f"{structure}|{st}" if f"{structure}|{st}" in odds["stages"] else f"all|{st}"
    if key not in odds["stages"]:
        key = f"{structure}|announced"
    r = odds["stages"][key]
    note = f"{r['rate']:.0%} of {r['n_cautious']} {structure.replace('_', ' ')}s {STAGE_WORDS.get(stage, stage)}"
    rate = r["rate"]
    m = odds.get("model") or {}
    w = STAGE_WEIGHT.get(stage, 1.0)
    if m.get("used") and deal and w > 0:
        from deal_odds import feats
        x = feats(deal)
        z = m["intercept"] + sum(m["coef"][f] * float(v) for f, v in zip(odds["features"], x))
        a0 = odds["stages"].get(f"{structure}|announced", r)["rate"]
        adj = w * (z - logit(a0))
        new = 1 / (1 + math.exp(-(logit(rate) + adj)))
        if abs(new - rate) >= 0.005:
            pts = round(abs(new - rate) * 100)
            note += f", {'+' if new > rate else '-'}{pts} point{'' if pts == 1 else 's'} for this deal's features"
        rate = new
    return rate, r["n_cautious"], note


LATE_GROUPS = (("ACCC", lambda g: "ACCC" in g), ("FIRB", lambda g: "FIRB" in g), ("OIO", lambda g: "OIO" in g),
               ("overseas", lambda g: any(x.startswith("overseas") for x in g)))


def dated_stage(live: dict, deal: dict | None, today: str) -> str:
    """The latest stage the dates show the deal has passed, for a live row with no stage set."""
    deal = deal or {}
    for k, dt in (("court_approved", live.get("court_date") or deal.get("court_date")),
                  ("vote_passed", live.get("meeting_date") or deal.get("meeting_date")),
                  ("booklet_out", live.get("booklet_date") or deal.get("booklet_date"))):
        if dt and dt[:10] <= today:
            return "booklet_out" if (k == "vote_passed" and live["structure"] != "scheme") else k
    return "announced"


def late_payment(root: str, live: dict, deal: dict | None, today: str) -> tuple[str, str]:
    """The payment date if the deal takes as long as the slowest quarter of past deals of its kind,
    from the latest stage it has reached; and a note saying where the number comes from."""
    path = os.path.join(root, "reports", "deal_odds.json")
    if not os.path.exists(path):
        return "", ""
    tim = json.load(open(path)).get("timing") or {}
    deal = deal or {}
    st = live["structure"] if live["structure"] in ("scheme", "full_takeover") else "scheme"
    dated = [("court_approved", live.get("court_date") or deal.get("court_date")),
             ("vote_passed", live.get("meeting_date") or deal.get("meeting_date")),
             ("booklet_out", live.get("booklet_date") or deal.get("booklet_date"))]
    anchor, stage = live["announce_date"], "announced"
    for k, dt in dated:
        if dt and dt[:10] <= today and f"{st}|{k}" in tim:
            anchor, stage = dt[:10], k
            break
    words = {"announced": "announcement", "booklet_out": "the booklet", "vote_passed": "the vote", "court_approved": "court approval"}[stage]
    key, label = f"{st}|{stage}", ""
    if stage == "announced":
        g = {x.strip() for x in (deal.get("regulators") or "").split(";") if x.strip()}
        opts = [(tim[f"{st}|announced|{name}"]["q3"], name) for name, test in LATE_GROUPS if test(g) and f"{st}|announced|{name}" in tim]
        if not opts and (deal.get("regulators") or "").strip() == "none" and f"{st}|announced|no approvals" in tim:
            opts = [(tim[f"{st}|announced|no approvals"]["q3"], "no approvals")]
        if opts:
            q3, name = max(opts)
            key, label = f"{st}|announced|{name}", " needing " + {"ACCC": "ACCC clearance", "FIRB": "FIRB approval", "OIO": "OIO consent",
                                                                  "overseas": "overseas approvals", "no approvals": "no approvals"}[name]
            label = " with no approvals beyond the vote and court" if name == "no approvals" else label
    if key not in tim:
        return "", ""
    t = tim[key]
    late = (date.fromisoformat(anchor) + timedelta(days=t["q3"])).isoformat()
    note = (f"a quarter of {t['n']} past {st.replace('_', ' ')}s{label} took {t['q3']} days or more from {words} to payment "
            f"(half took {t['median']})")
    exp = live.get("expected_payment") or ""
    if late <= today:
        return "", note + "; this deal is already past that"
    return (late if late > exp else ""), note


_INDEX_CACHE: dict = {}


def index_level(root: str, fx: FX, market: str, d: str) -> float | None:
    """The price level (not total return: a target's own price falls by its dividends too) of the
    market's index fund at the last close on or before d, in the target's currency."""
    m, t = INDEX[market]
    key = (root, m, t)
    if key not in _INDEX_CACHE:
        path = os.path.join(root, "data", "prices", m, f"{t}.csv")
        ser = []
        for r in (csv.DictReader(open(path, newline="")) if os.path.exists(path) else []):
            try:
                ser.append((r["date"], float(r["close"])))
            except (TypeError, ValueError, KeyError):
                continue
        _INDEX_CACHE[key] = ser
    ser = _INDEX_CACHE[key]
    i = bisect.bisect_right(ser, (d, float("inf"))) - 1
    if i < 0:
        return None
    return ser[i][1] * (fx.nzd_per("USD", d) if market == "NZX" else 1.0)


def deal_rows(root: str) -> dict:
    path = os.path.join(root, "deals", "all_deals.csv")
    return {r["deal_id"]: r for r in csv.DictReader(open(path, encoding="utf-8"))} if os.path.exists(path) else {}


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
            "| Ticker | Company | Cash lead | Last close | Gross spread | First filing | Latest filing | Forms | Terms |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for g, r, px in sorted(rows, key=lambda x: -x[0]):
        flag = " (check)" if g < -0.02 or g > 0.25 else ""
        extra = "; ".join(x for x in ("stock as well as cash" if r.get("has_stock") else "", "with a CVR" if r.get("cvr") else "",
                                       f"meeting {r['meeting']}" if r.get("meeting") else "", f"tender expires {r['tender_expires']}" if r.get("tender_expires") else "",
                                       f"close expected {r['expected_close']}" if r.get("expected_close") else "", "weak match" if r.get("strength") == "weak" else "") if x)
        out.append(f"| {r['ticker']} | {r['company'][:38]} | {float(r['cash_price_lead']):.2f} | {px:.2f} | {g:+.1%}{flag} | "
                   f"{r['first_seen']} | {r['latest']} | {r['forms']} | {extra} |")
    return out


def main(root: str) -> int:
    data = os.path.join(root, "data")
    prices, fx = Prices(data), FX(data)
    today = date.today().isoformat()
    now = datetime.now(timezone.utc)
    lines = ["# Live deal monitor", "", f"Run {today}. Prices are the last closes in the repository; a blank means no price yet.", "",
             "| Deal | Price | Offer value | Gross spread | Days to payment | Yearly rate | Yearly after costs | If it runs late | Market-implied chance | Base-rate chance | Note |",
             "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    rows = []      # the same numbers as a table, for reports/deal_monitor.csv
    hp = os.path.join(root, "reports", "deal_history.json")
    try:
        kept = json.load(open(hp)) if os.path.exists(hp) else {}
    except ValueError:
        kept = {}
    hist = {"_since": kept.get("_since") or today}      # the implied chance each day, for the hub
    db = deal_rows(root)
    bad = []       # rows that couldn't be valued
    for d in csv.DictReader(open(os.path.join(root, "config", "live_deals.csv"), encoding="utf-8")):
        try:
            px = prices.last_close(d["target_market"], d["target_ticker"], today, now)
            cash = float(d["cash_per_share"] or 0)
            if d["cash_ccy"] == "USD":
                cash *= fx.per_nzd("AUD", today) / fx.per_nzd("USD", today)      # A$ per US$
            ratio = float(d["scrip_ratio"] or 0)
            acq = prices.last_close(d["acquirer_market"], d["acquirer_ticker"], today, now) if ratio else 0.0
            acq = acq * acq_fx(fx, d, today) if acq else acq
            offer = cash + ratio * acq if (ratio == 0 or acq) else None
            stage = (d.get("stage") or "").strip() or dated_stage(d, db.get(d["deal_id"]), today)
            undist = float(d["undisturbed"]) if d["undisturbed"] else None
            # the market's move since the undisturbed price (its own date when the desk set one: an earlier
            # approach or a rival bid can put it well before this deal's announcement)
            i0 = index_level(root, fx, d["target_market"], (d.get("undisturbed_date") or "").strip() or d["announce_date"])
            i1 = index_level(root, fx, d["target_market"], today)
            move = i1 / i0 if (i0 and i1) else 1.0
            brk = undist * move if undist else None
            p_base, n, bnote = base_rate(root, d["structure"], stage, db.get(d["deal_id"]))
            days = (date.fromisoformat(d["expected_payment"]) - date.today()).days
            # the implied chance each session since the announcement
            h = []
            if undist:
                acq_px = {b.date: b.close for b in prices.bars(d["acquirer_market"], d["acquirer_ticker"])} if ratio else {}
                last_acq = None
                usd = d["cash_ccy"] == "USD"
                for b in prices.bars(d["target_market"], d["target_ticker"]):
                    if b.date < d["announce_date"] or b.close <= 0:
                        continue
                    last_acq = acq_px[b.date] * acq_fx(fx, d, b.date) if b.date in acq_px else last_acq
                    c = float(d["cash_per_share"] or 0) * (fx.per_nzd("AUD", b.date) / fx.per_nzd("USD", b.date) if usd else 1.0)
                    off = (c + (ratio * last_acq if ratio else 0.0)) if (ratio == 0 or last_acq) else None
                    lv = index_level(root, fx, d["target_market"], b.date)
                    bk = undist * (lv / i0) if (lv and i0) else undist
                    imp = (b.close - bk) / (off - bk) if off and off > bk else None
                    h.append([b.date, round(b.close, 4), round(off, 4) if off else None, round(bk, 4),
                              round(min(1.0, max(0.0, imp)), 4) if imp is not None else None])
            old = kept.get(d["deal_id"]) or []
            last = old[-1][0] if old else ""
            hist[d["deal_id"]] = (old + [x for x in h if x[0] > last])[-160:]
            if px and offer:
                gross = offer / px - 1
                yearly = (1 + gross) ** (365 / max(days, 1)) - 1 if days > 0 else float("nan")
                implied = (px - brk) / (offer - brk) if brk and offer > brk else float("nan")
                if implied != implied:
                    imp = ""
                elif implied < 0:
                    imp = "The price is below the break price: the market expects less than a plain break would leave"
                elif implied > 1:
                    imp = "The price is above the offer, so the market expects a better bid"
                else:
                    imp = f"{implied:.0%}"
                ccy = "USD" if d["target_market"] == "US" else ("AUD" if d["target_market"] == "ASX" else "NZD")
                st = prices.stats(d["target_market"], d["target_ticker"], today, fx.nzd_per(ccy, today))
                local = TYPICAL_STAKE_NZD * fx.per_nzd(ccy, today)
                fee = min(0.019 * local, {"ASX": 15, "US": 5, "NZX": 25}[d["target_market"]]) / local
                cost = st["spread"] / 2 + fee + (sum(FIXED_COSTS.values()) if ccy != "NZD" else 0)
                net_y = (1 + gross - cost) ** (365 / max(days, 1)) - 1 if days > 0 else float("nan")
                ev_ret = ev_y = float("nan")
                if brk and p_base == p_base and brk <= px <= offer:
                    ev_ret = (p_base * offer + (1 - p_base) * brk) / px - 1 - cost
                    ev_y = (1 + ev_ret) ** (365 / days) - 1 if days > 0 and ev_ret > -1 else float("nan")
                late, late_note = late_payment(root, d, db.get(d["deal_id"]), today)
                ldays = (date.fromisoformat(late) - date.today()).days if late else 0
                late_y = (1 + gross - cost) ** (365 / ldays) - 1 if (ldays > 0 and abs(net_y) < 5) else float("nan")
                cells = [f"{px:.3f}", f"{offer:.3f}", f"{gross:+.1%}", str(days), f"{yearly:+.1%}" if abs(yearly) < 5 else "n/m",
                         f"{net_y:+.1%}" if abs(net_y) < 5 else "n/m",
                         (f"{late_y:+.1%} if paid {late}" if late_y == late_y and abs(late_y) < 5 else f"paid {late}") if late else "", imp]
                rows.append({"ticker": d["target_ticker"], "deal_id": d["deal_id"], "structure": d["structure"], "price": round(px, 4),
                             "offer_value": round(offer, 4), "gross_spread": round(gross, 5), "days_to_payment": days,
                             "yearly": round(yearly, 4) if abs(yearly) < 5 else "", "yearly_after_costs": round(net_y, 4) if abs(net_y) < 5 else "",
                             "market_implied": round(implied, 4) if implied == implied and 0 <= implied <= 1 else "",
                             "implied_note": imp if imp and not imp.endswith("%") else "", "base_rate": round(p_base, 4),
                             "base_rate_n": n, "expected_payment": d["expected_payment"], "note": d["terms_note"], "as_of": today,
                             "stage": stage, "base_note": bnote, "break_price": round(brk, 4) if brk else "",
                             "undisturbed": undist or "", "market_move": round(move - 1, 4),
                             "meeting_date": d.get("meeting_date", ""), "court_date": d.get("court_date", ""),
                             "end_date": d.get("end_date", ""), "conditions_open": d.get("conditions_open", ""),
                             "late_payment": late, "yearly_if_late": round(late_y, 4) if late_y == late_y and abs(late_y) < 5 else "",
                             "late_note": late_note,
                             "expected_return": round(ev_ret, 5) if ev_ret == ev_ret else "",
                             "expected_yearly": round(ev_y, 4) if ev_y == ev_y and abs(ev_y) < 5 else ""})
            else:
                cells = ["" if not px else f"{px:.3f}", "" if not offer else f"{offer:.3f}", "", str(days), "", "", "", ""]
            lines.append(f"| {d['target_ticker']} ({d['deal_id']}) | " + " | ".join(cells) +
                         f" | {p_base:.0%} ({bnote}) | {d['terms_note']} |")
        except Exception as e:   # one bad row must not stop the others: report it and carry on
            if d.get("deal_id") in kept and d["deal_id"] not in hist:
                hist[d["deal_id"]] = kept[d["deal_id"]]
            bad.append(f"{d.get('target_ticker', '?')} ({d.get('deal_id', '?')}): {type(e).__name__}: {str(e)[:120]}")
            lines.append(f"| {d.get('target_ticker', '?')} ({d.get('deal_id', '?')}) | could not be valued: {type(e).__name__} |" + " |" * 9)

    lines += ["", f"After costs assumes a NZ${TYPICAL_STAKE_NZD:,} stake: half the estimated spread, brokerage beyond the plan's "
              "monthly cover, a currency conversion and the hedge's dealing cost; consideration is paid free of brokerage. "
              "The break price is the undisturbed price moved by the local market since the announcement. "
              "If it runs late: paid when the slowest quarter of past deals of the same kind would have paid, counted from the latest "
              "stage this deal has reached (blank when the expected date is already later). "
              "The base rate is how often holders were paid in past deals of the same structure at the same stage "
              "(reports/deal_odds.md), moved by the deal-feature model where it applies. "
              "The analyst adjusts it for this deal's conditions and records each adjustment before any entry."]
    if bad:
        lines += ["", "Rows that could not be valued (fix them in config/live_deals.csv):"] + [f"- {b}" for b in bad]
        print("could not value: " + "; ".join(bad), file=sys.stderr)
    lines += us_section(root, prices, today, now)
    os.makedirs(os.path.join(root, "reports"), exist_ok=True)
    if rows:
        with open(os.path.join(root, "reports", "deal_monitor.csv"), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader(); w.writerows(rows)
    open(os.path.join(root, "reports", "deal_monitor.md"), "w").write("\n".join(lines) + "\n")
    json.dump(hist, open(hp, "w"), separators=(",", ":"))
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
