"""Deal size trial (rulebook section 5, "Deal size trial"), a forward test registered on 1 Nov 2026.

A separate trial book, outside the ledger, so the portfolio's limits and risk don't change. It asks whether
the deal sleeve earns more than cash once positions are big enough that brokerage, capped per order, stops
eating the spread.

- Entry: each night from 2 Nov 2026 to 31 Mar 2027, every live ASX and NZX deal in config/live_deals.csv
  (cash, scrip or mixed; ASX cash deals included) not already in the trial is entered when section 5's
  entry rule holds, applied mechanically: the expected return at the base rate (reports/deal_monitor.csv:
  chance x offer value plus the rest x the break price, against tonight's close), less the costs of a
  A$10,000 position, beats the local three-month rate to the expected payment date. One entry per deal.
- Two books with the same entries and exits: "large" at A$10,000 (NZ$10,000 on NZX) and "small" at A$3,000
  (NZ$3,000), each cut to the liquidity limit of section 3 (two sessions at 10% of the 20-session median
  daily value; NZX orders outside the 20 largest companies at most NZ$2,500 a session).
- Fills as the engine's (src/fills.py): a market order at the open of a session after the decision, half
  the spread and the size cost, at most 10% of the session's volume, the rest rolling; it lapses after 5
  sessions that traded or 10 business days. NZX days with no price movement don't fill. Brokerage 1.9% of
  each order, capped at A$15 (ASX) or NZ$25 (NZX), with no monthly plan cover; the hedge's 0.1% on ASX.
- Dividends: from EODHD's dividends feed (ASX), credited to shares held before the ex-date.
- Exit: paid on the implementation date at the latest terms (cash, plus scrip at the acquirer's close
  that day less half its spread and brokerage on selling it); after a break (terminated, withdrawn,
  lapsed) sold from the first session after the outcome date; a deal superseded by a rival follows the
  rival's row. Positions still open are marked at the close less half the spread and brokerage.
- Result per position: gain after all costs less the local three-month rate on the money laid out over the
  days held. Scored on 2 July 2027 (section 5); read at the 18 December review.
State: data/trial/deal_size_trial.json. Report: reports/deal_size_trial.md.
Usage: python3 -I src/deal_trial.py <repo_root> [YYYY-MM-DD]
"""
import csv
import json
import math
import os
import sys
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deal_monitor import MARKET_CCY, acq_fx  # noqa: E402
from fills import Bar, fill_order, size_cost  # noqa: E402
from market_data import FX, NZX_SMALL_ORDER_CAP_NZD, Prices, closed_by, nzx_large, session_open_utc  # noqa: E402
from rates import Rates  # noqa: E402

BOOKS = {"large": 10000.0, "small": 3000.0}          # in the target's currency
FEE_CAP = {"ASX": 15.0, "NZX": 25.0}
MIN_ORDER = {"ASX": 1500.0, "NZX": 2500.0}      # section 3: smallest order
HEDGE = 0.001
ORDER_LIFE, ORDER_DAYS = 5, 10
START, LAST_ENTRY, SCORE_DATE = "2026-11-02", "2027-03-31", "2027-07-02"
BROKE = {"terminated", "withdrawn", "lapsed"}


def fee(market: str, value: float) -> float:
    return round(min(0.019 * value, FEE_CAP[market]), 2) if value > 0 else 0.0


def business_days(a: str, b: str) -> int:
    d, n = date.fromisoformat(a), 0
    while d < date.fromisoformat(b):
        d += timedelta(days=1)
        n += d.weekday() < 5
    return n


def read_csv(path: str) -> list[dict]:
    return list(csv.DictReader(open(path, encoding="utf-8"))) if os.path.exists(path) else []


def eodhd_dividends(ticker: str, since: str) -> list[dict] | None:
    key = os.environ.get("EODHD_API_KEY")
    if not key:
        return None
    url = f"https://eodhd.com/api/div/{urllib.parse.quote(ticker)}.AU?api_token={key}&fmt=json&from={since}"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "paper-portfolio"}), timeout=60) as r:
            rows = json.loads(r.read().decode())
    except Exception:
        return None
    return [{"ex": x.get("date"), "per_share": float(x.get("unadjustedValue") or x.get("value") or 0)} for x in rows if x.get("date")]


class Trial:
    def __init__(self, root: str, today: str, now: datetime, prices: Prices | None = None, fx: FX | None = None,
                 rates: Rates | None = None, dividends=eodhd_dividends):
        self.root, self.today, self.now = root, today, now
        data = os.path.join(root, "data")
        self.prices, self.fx = prices or Prices(data), fx or FX(data)
        self.rates = rates or Rates(data)
        self.get_divs = dividends
        self.path = os.path.join(data, "trial", "deal_size_trial.json")
        self.st = json.load(open(self.path)) if os.path.exists(self.path) else {"registered": "2026-11-01", "positions": {}, "watch": {}}

    # ---- helpers ----
    def stats(self, m: str, t: str, d: str) -> dict:
        ccy = MARKET_CCY[m]
        return self.prices.stats(m, t, d, self.fx.nzd_per(ccy, d))

    def rate(self, ccy: str, d: str) -> float:
        try:
            return self.rates.three_month(ccy, d)
        except Exception:
            return 0.0

    def liquidity_cap(self, m: str, t: str, d: str) -> float:
        """Section 3: no position larger than two sessions at 10% of the 20-session median daily value."""
        s = self.stats(m, t, d)
        if s.get("median_value_nzd") is None:          # NZX: volumes unknown, the order cap stands in
            return float("inf")
        return 2 * 0.10 * s["median_value_nzd"] * self.fx.per_nzd(MARKET_CCY[m], d)

    # ---- 1. entries ----
    def decide(self, live: dict, mon: dict) -> list[str]:
        out = []
        if not (START <= self.today <= LAST_ENTRY):
            return out
        for did, d in live.items():
            m, t = d["target_market"], d["target_ticker"]
            if m not in ("ASX", "NZX") or did in self.st["positions"]:
                continue
            r = mon.get(did)
            why = None
            if not r:
                why = "not valued by the deal monitor tonight"
            else:
                try:
                    px, offer, brk, p = (float(r[k]) for k in ("price", "offer_value", "break_price", "base_rate"))
                except (TypeError, ValueError):
                    px = offer = brk = p = None
                    why = "no break price or base rate"
                if why is None:
                    days = (date.fromisoformat(d["expected_payment"]) - date.fromisoformat(self.today)).days
                    if days <= 0:
                        why = "expected payment date has passed"
                    elif not (brk <= px <= offer):
                        why = "price outside the range from the break price to the offer"
                    else:
                        s = self.stats(m, t, self.today)
                        size = min(BOOKS["large"], self.liquidity_cap(m, t, self.today))
                        cost = s["spread"] / 2 + fee(m, size) / max(size, 1) + (HEDGE if m != "NZX" else 0) + \
                            (size_cost(size, s["adv_local"], s["daily_vol"]) if s.get("adv_local") else 0)
                        ev = (p * offer + (1 - p) * brk) / px - 1 - cost
                        hurdle = (1 + self.rate(MARKET_CCY[m], self.today)) ** (days / 365) - 1
                        if ev > hurdle:
                            self.enter(did, d, px, offer, brk, p, ev, hurdle)
                            out.append(f"{t}: entered (expected {ev:+.2%} against cash {hurdle:+.2%})")
                            continue
                        why = f"expected {ev:+.2%} after costs, cash {hurdle:+.2%}"
            self.st["watch"][did] = {"ticker": t, "date": self.today, "why": why}
        return out

    def enter(self, did, d, px, offer, brk, p, ev, hurdle):
        m, t = d["target_market"], d["target_ticker"]
        cap = self.liquidity_cap(m, t, self.today)
        books = {}
        for b, size in BOOKS.items():
            value = min(size, cap)
            qty = math.floor(value / px) if value >= MIN_ORDER[m] else 0      # below the smallest order: that book stays out
            books[b] = {"order_value": round(value, 2), "qty_ordered": qty, "fills": [], "divs": [], "exit": None}
        implied = (px - brk) / (offer - brk) if offer > brk else None
        self.st["positions"][did] = {
            "deal_id": did, "track": did, "market": m, "ticker": t, "ccy": MARKET_CCY[m],
            "decided": self.today, "decided_at_utc": self.now.isoformat(), "status": "ordered",
            "at_entry": {"price": px, "offer": offer, "break": brk, "base_rate": p, "implied": implied, "expected": ev, "cash": hurdle,
                         "expected_payment": d["expected_payment"], "structure": d["structure"]},
            "terms": self.terms_of(d), "books": books, "flags": []}
        self.st["watch"].pop(did, None)

    @staticmethod
    def terms_of(d: dict) -> dict:
        return {k: d.get(k, "") for k in ("cash_per_share", "cash_ccy", "scrip_ratio", "acquirer_market", "acquirer_ticker", "target_market")}

    # ---- 2. fills (buys, and sales after a break) ----
    def work_orders(self, pos: dict, side: str) -> None:
        m, t = pos["market"], pos["ticker"]
        if side == "buy":       # sessions that open after the decision
            start_utc = datetime.fromisoformat(pos["decided_at_utc"])
            sessions = [b for b in self.prices.bars(m, t) if b.date <= self.today and session_open_utc(m, b.date) > start_utc
                        and closed_by(m, b.date, self.now)]
        else:                   # sessions after the day the deal broke
            sessions = [b for b in self.prices.bars(m, t) if pos["sell_from"] < b.date <= self.today and closed_by(m, b.date, self.now)]
        small_nzx = m == "NZX" and t.upper() not in nzx_large()
        for name, bk in pos["books"].items():
            key = "fills" if side == "buy" else "sells"
            bk.setdefault(key, [])
            held = sum(f["qty"] for f in bk["fills"])
            target = bk["qty_ordered"] if side == "buy" else held
            done = sum(f["qty"] for f in bk[key])
            seen = {f["date"] for f in bk[key]} | set(bk.get(f"tried_{side}", []))
            for bar in sessions:
                if done >= target or bk.get(f"lapsed_{side}"):
                    break
                if bar.date in seen:
                    continue
                s = self.stats(m, t, bar.date)
                qty = target - done
                use = bar
                if m == "NZX" and bar.volume <= 0:
                    if bar.open == bar.high == bar.low == bar.close:
                        bk.setdefault(f"tried_{side}", []).append(bar.date); continue
                    use = Bar(bar.date, bar.open, bar.high, bar.low, bar.close, 1e12)
                    s = dict(s, adv_local=1e15)
                if small_nzx:
                    qty = min(qty, math.floor(NZX_SMALL_ORDER_CAP_NZD * self.fx.per_nzd("NZD", bar.date) / bar.open))
                f = fill_order(side, qty, use, s["spread"], s["adv_local"] or 0.0, s["daily_vol"])
                if f.qty <= 0:
                    bk.setdefault(f"tried_{side}", []).append(bar.date); continue
                value = f.qty * f.price
                bk[key].append({"date": bar.date, "qty": f.qty, "price": round(f.price, 6), "fee": fee(m, value)})
                done += f.qty
            traded = [b for b in sessions if b.volume > 0 or (m == "NZX" and not (b.open == b.high == b.low == b.close))]
            since = pos["decided"] if side == "buy" else pos["sell_from"]
            if done < target and (len(traded) >= ORDER_LIFE or business_days(since, self.today) >= ORDER_DAYS):
                if side == "buy":
                    bk[f"lapsed_{side}"] = True
                else:
                    # a sale that can't complete keeps trying: a broken deal's shares are still held
                    bk.setdefault("tried_sell", [])
        if side == "buy":
            filled = [sum(f["qty"] for f in bk["fills"]) for bk in pos["books"].values()]
            open_orders = [bk for bk in pos["books"].values() if sum(f["qty"] for f in bk["fills"]) < bk["qty_ordered"] and not bk.get("lapsed_buy")]
            if not open_orders:
                pos["status"] = "open" if any(filled) else "lapsed"

    # ---- 3. dividends ----
    def credit_dividends(self, pos: dict) -> None:
        if pos["market"] != "ASX" or self.get_divs is None:
            return
        first = min((f["date"] for bk in pos["books"].values() for f in bk["fills"]), default=None)
        if not first:
            return
        cache = pos.setdefault("div_feed", {"checked": "", "rows": []})
        if cache["checked"] != self.today:
            rows = self.get_divs(pos["ticker"], first)
            if rows is not None:
                cache["rows"], cache["checked"] = rows, self.today
        for bk in pos["books"].values():
            got = {x["ex"] for x in bk["divs"]}
            for x in cache["rows"]:
                ex = x["ex"]
                if ex in got or ex > self.today or x["per_share"] <= 0:
                    continue
                held = sum(f["qty"] for f in bk["fills"] if f["date"] < ex) - sum(f["qty"] for f in bk.get("sells", []) if f["date"] < ex)
                if held > 0 and not bk["exit"]:
                    bk["divs"].append({"ex": ex, "per_share": x["per_share"], "amount": round(held * x["per_share"], 2)})

    # ---- 4. exits ----
    def follow(self, pos: dict, db: dict, live: dict) -> None:
        if pos["track"] in live:
            pos["terms"] = self.terms_of(live[pos["track"]])
        row = db.get(pos["track"])
        if not row:
            return
        outcome = (row.get("outcome") or "").strip()
        if outcome == "superseded_by_rival":
            rivals = [x.strip() for x in (row.get("related_deal_ids") or "").split(";") if x.strip() in db]
            live_or_paid = [x for x in rivals if (db[x].get("outcome") or "pending") not in BROKE | {"superseded_by_rival"}]
            if live_or_paid and live_or_paid[0] != pos["track"]:
                pos["flags"].append(f"{self.today}: followed rival deal {live_or_paid[0]}")
                pos["track"] = live_or_paid[0]
                if pos["track"] in live:
                    pos["terms"] = self.terms_of(live[pos["track"]])
                row = db[pos["track"]]
                outcome = (row.get("outcome") or "").strip()
        if outcome == "completed":
            pay = (row.get("implementation_date") or row.get("outcome_date") or "")[:10]
            if pay and pay <= self.today:
                self.pay(pos, row, pay)
        elif outcome in BROKE and pos["status"] == "open":
            od = (row.get("outcome_date") or self.today)[:10]
            pos["status"], pos["sell_from"] = "selling", od
            pos["flags"].append(f"{self.today}: deal {outcome} on {od}; selling")

    def pay(self, pos: dict, row: dict, pay: str) -> None:
        tm = pos["terms"]
        cash = float(tm.get("cash_per_share") or 0)
        if tm.get("cash_ccy") == "USD" and pos["ccy"] == "AUD":
            cash *= self.fx.per_nzd("AUD", pay) / self.fx.per_nzd("USD", pay)
        ratio = float(tm.get("scrip_ratio") or 0)
        if not (cash or ratio) and row.get("offer_price_final"):
            cash = float(row["offer_price_final"])        # a rival's terms not in the live list: its final cash-equivalent price
        scrip_px = 0.0
        if ratio:
            a = self.prices.last_close(tm["acquirer_market"], tm["acquirer_ticker"], pay)
            if a is None:
                pos["flags"].append(f"{self.today}: no acquirer price to value the scrip; payment waits"); return
            s = self.stats(tm["acquirer_market"], tm["acquirer_ticker"], pay)
            scrip_px = a * acq_fx(self.fx, tm, pay) * (1 - s["spread"] / 2)
        for bk in pos["books"].values():
            held = sum(f["qty"] for f in bk["fills"]) - sum(f["qty"] for f in bk.get("sells", []))
            if held <= 0 or bk["exit"]:
                continue
            scrip_value = held * ratio * scrip_px
            proceeds = held * cash + scrip_value - (fee(pos["market"], scrip_value) if scrip_value else 0.0)
            bk["exit"] = {"date": pay, "how": "paid", "proceeds": round(proceeds, 2)}
        pos["status"] = "closed"

    def settle_sales(self, pos: dict) -> None:
        for bk in pos["books"].values():
            held = sum(f["qty"] for f in bk["fills"])
            sold = sum(f["qty"] for f in bk.get("sells", []))
            if held > 0 and sold >= held and not bk["exit"]:
                bk["exit"] = {"date": bk["sells"][-1]["date"], "how": "sold after the deal broke",
                              "proceeds": round(sum(f["qty"] * f["price"] - f["fee"] for f in bk["sells"]), 2)}
        if all(bk["exit"] or not bk["fills"] for bk in pos["books"].values()):
            pos["status"] = "closed"

    # ---- 5. results ----
    def result(self, pos: dict, bk: dict) -> dict | None:
        if not bk["fills"]:
            return None
        m = pos["market"]
        basis = sum(f["qty"] * f["price"] + f["fee"] for f in bk["fills"])
        basis += HEDGE * sum(f["qty"] * f["price"] for f in bk["fills"]) if m != "NZX" else 0.0
        start = bk["fills"][0]["date"]
        divs = sum(x["amount"] for x in bk["divs"])
        if bk["exit"]:
            value, end, marked = bk["exit"]["proceeds"], bk["exit"]["date"], False
        else:
            held = sum(f["qty"] for f in bk["fills"]) - sum(f["qty"] for f in bk.get("sells", []))
            px = self.prices.last_close(m, pos["ticker"], self.today, self.now) or bk["fills"][-1]["price"]
            s = self.stats(m, pos["ticker"], self.today)
            gross = held * px * (1 - s["spread"] / 2)
            value = gross - fee(m, gross) + sum(f["qty"] * f["price"] - f["fee"] for f in bk.get("sells", []))
            end, marked = self.today, True
        days = max(0, (date.fromisoformat(end) - date.fromisoformat(start)).days)
        cash = basis * ((1 + self.rate(pos["ccy"], start)) ** (days / 365) - 1)
        gain = value + divs - basis
        return {"basis": basis, "value": value + divs, "gain": gain, "over_cash": gain - cash, "pct": (gain - cash) / basis,
                "days": days, "marked": marked}

    # ---- the nightly run ----
    def run(self) -> dict:
        root = self.root
        live = {d["deal_id"]: d for d in read_csv(os.path.join(root, "config", "live_deals.csv"))}
        mon = {r["deal_id"]: r for r in read_csv(os.path.join(root, "reports", "deal_monitor.csv")) if r.get("as_of", self.today) == self.today}
        db = {r["deal_id"]: r for r in read_csv(os.path.join(root, "deals", "all_deals.csv"))}
        # the desk records outcomes in the current deal files, which are newer than the combined database
        for part in ("au/au_deals_2025_2026.csv", "nz/nz_deals.csv"):
            for r in read_csv(os.path.join(root, "deals", part)):
                if r.get("deal_id"):
                    db[r["deal_id"]] = {**db.get(r["deal_id"], {}), **{k: v for k, v in r.items() if v}}
        log = []
        for pos in self.st["positions"].values():
            if pos["status"] == "ordered":
                self.work_orders(pos, "buy")
            if pos["status"] in ("open", "ordered"):
                self.credit_dividends(pos)
                self.follow(pos, db, live)
            if pos["status"] == "selling":
                self.work_orders(pos, "sell")
                self.settle_sales(pos)
            # a deal that has left the live list with no outcome recorded needs one
            if pos["status"] == "open" and pos["track"] not in live and (db.get(pos["track"], {}).get("outcome") or "pending") == "pending":
                note = f"{self.today}: no longer in the live deal list and no outcome recorded"
                if not pos["flags"] or not pos["flags"][-1].endswith("no outcome recorded"):
                    pos["flags"].append(note)
        log += self.decide(live, mon)
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        json.dump(self.st, open(self.path, "w"), indent=1)
        self.write_report()
        return {"log": log}

    def write_report(self) -> None:
        P = self.st["positions"]
        L = ["# Deal size trial", "", f"Run {self.today}. A forward test registered on 1 Nov 2026 (rulebook section 5, \"Deal size trial\"): every live ASX "
             "and NZX deal that passes section 5's entry rule, applied mechanically at the base rate, held in two separate trial books at "
             "A$10,000 and A$3,000 a position with the engine's fills and costs. Outside the ledger: nothing here changes the portfolio.", ""]
        tot = {b: {"basis": 0.0, "gain": 0.0, "over": 0.0, "n": 0, "pcts": []} for b in BOOKS}
        rows = []
        for did, pos in sorted(P.items(), key=lambda x: x[1]["decided"]):
            res = {b: self.result(pos, bk) for b, bk in pos["books"].items()}
            to_nzd = self.fx.nzd_per(pos["ccy"], self.today)
            for b, r in res.items():
                if r:
                    tot[b]["basis"] += r["basis"] * to_nzd; tot[b]["gain"] += r["gain"] * to_nzd; tot[b]["over"] += r["over_cash"] * to_nzd
                    tot[b]["n"] += 1; tot[b]["pcts"].append(r["pct"])
            e = pos["at_entry"]
            lg, sm = res.get("large"), res.get("small")
            state = {"ordered": "order waiting", "open": "held", "selling": "selling after a break", "closed": "closed", "lapsed": "order lapsed"}[pos["status"]]
            how = next((bk["exit"]["how"] for bk in pos["books"].values() if bk["exit"]), "")
            rows.append(f"| {pos['ticker']} ({did}) | {pos['decided']} | {e['implied']:.0%} / {e['base_rate']:.0%} | {state}{', ' + how if how else ''} | "
                        + (f"{lg['basis']:,.0f} {pos['ccy']}, {lg['pct']:+.2%}{' (marked)' if lg['marked'] else ''}" if lg else "") + " | "
                        + (f"{sm['basis']:,.0f} {pos['ccy']}, {sm['pct']:+.2%}{' (marked)' if sm['marked'] else ''}" if sm else "") + " |"
                        if e.get("implied") is not None else
                        f"| {pos['ticker']} ({did}) | {pos['decided']} | n/a | {state} | | |")
        L += ["| Book | Positions | Money laid out (NZ$) | Gain after costs (NZ$) | Over cash (NZ$) | Mean per position, over cash |", "| --- | --- | --- | --- | --- | --- |"]
        for b in BOOKS:
            T = tot[b]
            mean = sum(T["pcts"]) / len(T["pcts"]) if T["pcts"] else float("nan")
            L.append(f"| {b} ({'A$10,000' if b == 'large' else 'A$3,000'}) | {T['n']} | {T['basis']:,.0f} | {T['gain']:+,.0f} | {T['over']:+,.0f} | "
                     + (f"{mean:+.2%} |" if T["pcts"] else " |"))
        L += ["", "Book totals are in NZ$ at tonight's exchange rate; each position's own amounts are in its currency. Open positions are marked at tonight's close "
              "less half the spread and brokerage.", "", "| Deal | Entered | Market's chance / base rate at entry | State | Large book | Small book |",
              "| --- | --- | --- | --- | --- | --- |"] + rows
        closed = [p for p in P.values() if p["status"] == "closed"]
        if closed:
            paid = sum(1 for p in closed if any((bk["exit"] or {}).get("how") == "paid" for bk in p["books"].values()))
            imp = [p["at_entry"]["implied"] for p in closed if p["at_entry"].get("implied") is not None]
            L += ["", f"Closed: {len(closed)}, of which paid {paid}. Mean market-implied chance at entry for these: "
                      f"{sum(imp) / len(imp):.0%}." if imp else ""]
        W = self.st["watch"]
        if W:
            L += ["", "Live deals not entered (latest reason):", ""] + [f"- {w['ticker']} ({k}): {w['why']}" for k, w in sorted(W.items())]
        flags = [f"- {p['ticker']}: {f}" for p in P.values() for f in p["flags"][-3:]]
        if flags:
            L += ["", "Notes:", ""] + flags
        L += ["", f"Scored on {SCORE_DATE} over every position entered by {LAST_ENTRY}: pass needs the large book's total gain after costs "
              "above cash, and its mean per position above zero. The small book is the comparison."]
        os.makedirs(os.path.join(self.root, "reports"), exist_ok=True)
        open(os.path.join(self.root, "reports", "deal_size_trial.md"), "w").write("\n".join(L) + "\n")


def main(argv: list[str]) -> int:
    root = argv[0] if argv else "."
    now = datetime.now(timezone.utc)
    today = argv[1] if len(argv) > 1 else now.astimezone(ZoneInfo("Pacific/Auckland")).date().isoformat()     # the NZ date of the evening run
    out = Trial(root, today, now).run()
    print("\n".join(out["log"]) or "no new entries")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
