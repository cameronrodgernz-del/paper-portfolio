"""The snapshot Cam's Hub shows on its Portfolio tab: one JSON document with everything the page
draws, built from the repository as it stands (ledgers, prices, deal monitor, reports, checks).

  reports/hub/snapshot.json

With --post it is sent to the hub's database through the Supabase edge function
`portfolio-ingest`. The function accepts it only with a GitHub Actions identity token for this
repository's main branch, so nothing secret is stored anywhere: the token is minted for the job by
GitHub itself (the workflow needs `permissions: id-token: write`).

Usage: python3 -I src/hub_export.py [source] [--post]      (source: nightly, desk, history, manual)
The run's step results can be passed in HUB_RUN_STEPS as JSON ({"step": "success" | "failure" | ...}).
"""
import csv
import glob
import json
import os
import re
import statistics as stats
import subprocess
import sys
import urllib.request
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from benchmarks import index_mix, matched_mix  # noqa: E402
from clerk import hedge_value_nzd, state  # noqa: E402
from ledger import Ledger  # noqa: E402
from market_data import CURRENCY, FX, nzx_large  # noqa: E402
from monthly import brier  # noqa: E402
from rates import Rates  # noqa: E402
from risk import CAPS, CASH_FLOOR, DD_EXIT, DD_HALVE, GROUP_CAP, INDUSTRY_CAP, SLEEVE_MAX  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NZ = ZoneInfo("Pacific/Auckland")
SCHEMA = 1
INGEST_URL = "https://vschefjwiocnffbirjrs.supabase.co/functions/v1/portfolio-ingest"
AUDIENCE = "cam-hub-portfolio"
TARGETS = {"core": 0.40, "deal": 0.25, "special": 0.15, "cash": 0.20}
BANDS = {"core": (0.35, 0.45), "deal": (0.0, 0.30), "special": (0.0, 0.20)}


# ---------- small helpers ----------
def rd(x, n=2):
    return None if x is None else round(float(x), n)


def nz_date(ts: str) -> str:
    return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(NZ).date().isoformat()


def read_csv(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


SYM = {"NZD": "NZ$", "AUD": "A$", "USD": "US$"}


def cash_txt(ccy: str, x: float, d: int = 2) -> str:
    return f"{'-' if x < 0 else ''}{SYM.get(ccy, ccy + ' ')}{abs(x):,.{d}f}"


def fnum(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def names_map() -> dict:
    """(market, ticker) -> a plain company or fund name, from every list the repository keeps."""
    out = {}
    for r in read_csv(os.path.join(ROOT, "deals", "all_deals.csv")):
        if r.get("target_ticker") and r.get("target_name"):
            out[(r["market"], r["target_ticker"].upper())] = r["target_name"]
    for r in read_csv(os.path.join(ROOT, "data", "sec", "us_deal_targets.csv")):
        if r.get("ticker"):
            out[("US", r["ticker"].upper())] = r["company"].title().replace(" Inc.", " Inc").replace(", Inc", " Inc")
    for r in read_csv(os.path.join(ROOT, "config", "nzx_isins.csv")):
        nm = re.sub(r"\s*\((NS)\)|\s+(Ordinary Shares|Ord Shares|Ordinary Units|Shares)$", "", r.get("name", "")).strip()
        if r.get("ticker"):
            out[("NZX", r["ticker"].upper())] = nm
    for f in ("universe_trial.csv",):
        for r in read_csv(os.path.join(ROOT, "config", f)):
            why = r.get("why", "")
            if ":" in why and r.get("ticker"):
                nm = why.split(":", 1)[1].strip().split(" (")[0].split(";")[0]
                out.setdefault((r["market"], r["ticker"].upper()), nm)
    out.update({("US", "VT"): "Vanguard Total World Stock ETF", ("ASX", "VAS"): "Vanguard Australian Shares Index ETF",
                ("US", "ENZL"): "iShares MSCI New Zealand ETF"})
    return out


def closes(market: str, ticker: str, since: str | None = None, limit: int = 160) -> list[list]:
    rows = read_csv(os.path.join(ROOT, "data", "prices", market, f"{ticker}.csv"))
    out = [[r["date"], fnum(r["close"])] for r in rows if fnum(r.get("close")) is not None and (since is None or r["date"] >= since)]
    return out[-limit:]


# ---------- one ledger ----------
def ledger_section(cfg: dict, name: str, names: dict, fx: FX, rates: Rates | None) -> dict:
    led = cfg["ledgers"][name]
    base = {"name": name, "start": led["start"], "end": led["end"], "bankroll": float(cfg["bankroll_nzd"]), "started": False}
    path = os.path.join(ROOT, led["dir"])
    if not os.path.isdir(path):
        return base
    L = Ledger(path)
    vals = [r["payload"] for r in L.records("valuations")]
    if not vals:
        return base
    st = state(L)
    latest, prev = vals[-1], (vals[-2] if len(vals) > 1 else None)
    total = latest["total_nzd"]
    bank = base["bankroll"]

    # series, with the two passive comparisons (success tests 2 and 3)
    dates = [v["date"] for v in vals]
    port = [v["total_nzd"] / vals[0]["total_nzd"] for v in vals]
    idx = index_mix(cfg, os.path.join(ROOT, "data"), fx, dates, L) if len(dates) > 0 else []
    ints = [r["payload"]["rate"] for r in L.records("cash") if r["payload"]["kind"] == "interest"]
    cash_rate = stats.mean(ints) if ints else 0.0
    share, mix = matched_mix(port, idx, dates, cash_rate) if idx and len(idx) == len(port) else (None, [])
    v0 = vals[0]["total_nzd"]
    series = []
    for k, v in enumerate(vals):
        series.append({"d": v["date"], "v": rd(v["total_nzd"]), "vu": rd(v.get("total_unhedged_nzd", v["total_nzd"])),
                       "dd": rd(v.get("drawdown", 0.0), 5), "peak": rd(v.get("peak_nzd")), "cash": rd(v.get("cash_nzd_total")),
                       "sl": {s: rd(x) for s, x in v.get("by_sleeve", {}).items()},
                       "idx": rd(idx[k] * v0) if idx and k < len(idx) else None,
                       "mix": rd(mix[k] * v0) if mix and k < len(mix) else None})

    # cost basis and realised result per holding, from the fills
    fills = [r for r in L.records("fills")]
    basis = defaultdict(lambda: {"qty": 0.0, "cost_local": 0.0, "cost_nzd": 0.0, "realised_nzd": 0.0, "first": None, "fees_nzd": 0.0})
    for r in fills:
        p = r["payload"]
        key = (p["sleeve"], p["market"], p["ticker"])
        b = basis[key]
        fee_nzd = p.get("fee_local", 0.0) * p.get("nzd_per_local", 1.0)
        b["fees_nzd"] += fee_nzd
        if p["side"] == "buy":
            if b["qty"] <= 1e-9:
                b["first"] = p["date"]
            b["qty"] += p["qty"]; b["cost_local"] += p["gross_local"] + p.get("fee_local", 0.0); b["cost_nzd"] += p["gross_nzd"] + fee_nzd
        else:
            if b["qty"] > 1e-9:
                frac = min(1.0, p["qty"] / b["qty"])
                c_nzd, c_loc = b["cost_nzd"] * frac, b["cost_local"] * frac
                b["realised_nzd"] += p["gross_nzd"] - fee_nzd - c_nzd
                b["cost_nzd"] -= c_nzd; b["cost_local"] -= c_loc; b["qty"] -= p["qty"]
    divs = defaultdict(float)
    for r in L.records("cash"):
        p = r["payload"]
        if p["kind"] == "dividend" and p.get("holder"):
            divs[tuple(p["holder"])] += p["amount"] * fx.nzd_per(p["ccy"], latest["date"])

    # the decision behind each holding (the latest placed buy card)
    decisions = [r for r in L.records("decisions")]
    cards = {}
    for r in decisions:
        p = r["payload"]
        c = p.get("card")
        if c and not p.get("vetoed") and c.get("side") == "buy":
            cards[(c["sleeve"], c["market"], c["ticker"])] = {
                "thesis": c.get("thesis"), "outcomes": c.get("outcomes"), "resolve_by": c.get("resolve_by"),
                "exit_rule": c.get("exit_rule"), "industry": c.get("industry"), "group": c.get("group"),
                "base_rate": c.get("base_rate"), "adjustments": c.get("adjustments"), "type": c.get("type"),
                "market_implied": p.get("market_implied"), "expected_annual": p.get("expected_annual"),
                "decided": nz_date(r["ts_utc"]), "price_seen": p.get("price_seen"), "break_price": c.get("break_price")}
        elif p.get("rule") and p.get("sleeve") == "core":
            cards.setdefault(("core", p["market"], p["ticker"]), {"rule": p["rule"], "target_weight": p.get("target_weight"),
                                                                    "decided": nz_date(r["ts_utc"])})
    hedges = defaultdict(list)
    for h in st["hedges"].values():
        mtm = hedge_value_nzd(h, fx, rates, latest["date"]) if rates is not None else None
        hedges[(h["sleeve"], h["market"], h["ticker"])].append({"ccy": h["ccy"], "notional": h["notional_foreign"], "rate": h["forward_rate"],
                                                               "opened": h["trade_date"], "matures": h["maturity"], "mtm_nzd": rd(mtm)})
    prev_val = {(p["sleeve"], p["market"], p["ticker"]): p["value_nzd"] for p in (prev or {}).get("positions", [])}
    positions = []
    for p in latest.get("positions", []):
        key = (p["sleeve"], p["market"], p["ticker"])
        b = basis[key]
        ccy = CURRENCY[p["market"]]
        cost = b["cost_nzd"]
        pnl = p["value_nzd"] - cost + divs.get(key, 0.0)
        positions.append({
            "sleeve": p["sleeve"], "market": p["market"], "ticker": p["ticker"], "name": names.get((p["market"], p["ticker"].upper()), ""),
            "ccy": ccy, "qty": p["qty"], "close": p["close"], "value": rd(p["value_nzd"]), "weight": rd(p["value_nzd"] / total, 5),
            "cap": CAPS.get(p["sleeve"]), "avg_cost": rd(b["cost_local"] / b["qty"], 4) if b["qty"] > 1e-9 else None,
            "cost": rd(cost), "pnl": rd(pnl), "pnl_pct": rd(pnl / cost, 5) if cost else None, "dividends": rd(divs.get(key, 0.0)),
            "day": rd(p["value_nzd"] - prev_val[key]) if key in prev_val else None, "since": b["first"],
            "fees": rd(b["fees_nzd"]), "card": cards.get(key), "hedges": hedges.get(key, []),
            "large": p["ticker"].upper() in nzx_large() if p["market"] == "NZX" else None,
            "px": closes(p["market"], p["ticker"], (date.fromisoformat(b["first"]) - timedelta(days=45)).isoformat() if b["first"] else None)})
    positions.sort(key=lambda x: -x["value"])

    # orders waiting to fill
    dec_by_seq = {r["seq"]: r["payload"] for r in decisions}
    orders = []
    for o in st["open_orders"]:
        d = dec_by_seq.get(o.get("decision_seq"), {})
        tries = [r["payload"] for r in L.records("orders") if r["payload"].get("event") == "no_fill" and r["payload"]["order_id"] == o["order_id"]]
        orders.append({"id": o["order_id"], "sleeve": o["sleeve"], "market": o["market"], "ticker": o["ticker"],
                       "name": names.get((o["market"], o["ticker"].upper()), ""), "side": o["side"], "qty": o["qty"], "left": o["remaining"],
                       "limit": o.get("limit"), "placed": nz_date(o["decided_at_utc"]), "ref_close": d.get("ref_close"),
                       "why": (d.get("card") or {}).get("thesis") or d.get("rule"), "misses": [t.get("reason") for t in tries][-3:]})

    # the record, newest first
    acts = []
    order_meta = {r["payload"]["order_id"]: r["payload"] for r in L.records("orders") if r["payload"].get("event") == "new"}
    for r in L.records("orders"):
        p = r["payload"]
        if p.get("event") == "new":
            acts.append({"t": r["ts_utc"], "k": "order", "s": p["sleeve"], "m": p["market"], "tk": p["ticker"],
                         "txt": f"Order to {p['side']} {p['qty']:g} {p['ticker']}" + (f" at a limit of {p['limit']}" if p.get("limit") else "")})
        elif p.get("event") == "cancel":
            o = order_meta.get(p["order_id"], {})
            acts.append({"t": r["ts_utc"], "k": "cancel", "s": o.get("sleeve"), "m": o.get("market"), "tk": o.get("ticker"),
                         "txt": f"Order for {o.get('ticker', '')} cancelled: {p.get('reason', '')}"})
    for r in fills:
        p = r["payload"]
        verb = "Bought" if p["side"] == "buy" else "Sold"
        how = " (paid out by the deal)" if str(p["order_id"]).startswith("CA") else ""
        acts.append({"t": r["ts_utc"], "k": "fill", "s": p["sleeve"], "m": p["market"], "tk": p["ticker"], "d": p["date"],
                     "txt": f"{verb} {p['qty']:g} {p['ticker']} at {cash_txt(p['ccy'], p['price'], 3)}{how}", "nzd": rd(p["gross_nzd"])})
    for r in decisions:
        p = r["payload"]
        c = p.get("card") or {}
        if p.get("vetoed"):
            acts.append({"t": r["ts_utc"], "k": "refused", "s": c.get("sleeve"), "m": c.get("market"), "tk": c.get("ticker"),
                         "txt": f"Refused: {c.get('side', 'buy')} {c.get('ticker', '')}", "why": p.get("breaches", [])})
        elif p.get("event") == "drawdown_rule":
            acts.append({"t": r["ts_utc"], "k": "rule", "txt": f"Fall from peak of {abs(p['drawdown']):.1%}: the {p['level']} rule ran"})
        elif p.get("event") in ("review_required", "review_done"):
            acts.append({"t": r["ts_utc"], "k": "rule", "txt": "Review required before new positions" if p["event"] == "review_required" else "Review logged"})
        elif c and c.get("thesis"):
            acts.append({"t": r["ts_utc"], "k": "decision", "s": c.get("sleeve"), "m": c.get("market"), "tk": c.get("ticker"),
                         "txt": f"Decision to {c.get('side', 'buy')} {c.get('ticker', '')}", "why": [c["thesis"]]})
    interest = defaultdict(float)
    for r in L.records("cash"):
        p = r["payload"]
        k = p["kind"]
        if k == "interest":
            interest[nz_date(r["ts_utc"])[:7]] += p["amount"]
        elif k == "deposit":
            acts.append({"t": r["ts_utc"], "k": "cash", "txt": f"Deposit of {cash_txt(p['ccy'], p['amount'], 0)}"})
        elif k == "plan_fee":
            acts.append({"t": r["ts_utc"], "k": "cash", "txt": f"Sharesies plan fee of {cash_txt(p['ccy'], abs(p['amount']))}"})
        elif k == "dividend":
            h = p.get("holder") or ["", "", ""]
            acts.append({"t": r["ts_utc"], "k": "income", "s": h[0], "m": h[1], "tk": h[2], "txt": f"Dividend from {h[2]}: {cash_txt(p['ccy'], p['amount'])}"})
        elif k == "fx_in":
            acts.append({"t": r["ts_utc"], "k": "cash", "txt": f"Converted NZ dollars to {cash_txt(p['ccy'], p['amount'])} (fee {cash_txt('NZD', p.get('fee_nzd', 0))})"})
        elif k == "hedge_settle":
            acts.append({"t": r["ts_utc"], "k": "hedge", "txt": f"Currency hedge settled: {'+' if p['amount'] >= 0 else ''}{cash_txt('NZD', p['amount'])}"})
    for r in L.records("calls"):
        p = r["payload"]
        if p.get("event") == "outcome":
            acts.append({"t": r["ts_utc"], "k": "call", "m": p["market"], "tk": p["ticker"],
                         "txt": f"Call on {p['ticker']} resolved: the main outcome {'happened' if p['main_outcome_happened'] else 'did not happen'}"})
    for r in L.records("corporate_actions"):
        p = r["payload"]
        if p.get("type") in ("dividend", "consideration", "split"):
            acts.append({"t": r["ts_utc"], "k": "action", "m": p.get("market"), "tk": p.get("ticker"),
                         "txt": f"{p['type'].capitalize()} entered for {p.get('ticker', '')}" + (f", paid {p['pay_date']}" if p.get("pay_date") else "")})
    for a in acts:
        a["day"] = nz_date(a["t"])
        a["name"] = names.get((a.get("m"), (a.get("tk") or "").upper()), "") if a.get("tk") else ""
    acts.sort(key=lambda a: a["t"], reverse=True)

    # dated calls and their scores (success test 5)
    calls_raw = [r["payload"] for r in L.records("calls")]
    made = [c for c in calls_raw if c.get("event") != "outcome"]
    outs = {(c["market"], c["ticker"], c["made_utc"]): c["main_outcome_happened"] for c in calls_raw if c.get("event") == "outcome"}
    ours, mkt, n_res = brier(made, outs)
    calls = [{"m": c["market"], "tk": c["ticker"], "name": names.get((c["market"], c["ticker"].upper()), ""), "made": nz_date(c["made_utc"]),
              "by": c.get("resolve_by"), "p": c.get("p_main"), "mkt": c.get("market_implied"), "base": c.get("base_rate"),
              "out": outs.get((c["market"], c["ticker"], c["made_utc"]))} for c in made]

    # costs paid so far
    costs = defaultdict(float)
    for r in fills:
        p = r["payload"]
        costs["brokerage"] += p.get("fee_local", 0.0) * p.get("nzd_per_local", 1.0)
        costs["spread"] += p["gross_nzd"] * p.get("spread_used", 0.0) / 2
    for r in L.records("cash"):
        p = r["payload"]
        if p["kind"] == "plan_fee":
            costs["plan"] += -p["amount"]
        elif p["kind"] == "fx_in":
            costs["fx"] += p.get("fee_nzd", 0.0)
    for r in L.records("hedges"):
        p = r["payload"]
        if p.get("event") == "open":
            costs["hedging"] += abs(p["notional_foreign"]) * fx.nzd_per(p["ccy"], p["trade_date"]) * 0.001

    # monthly returns
    months, last_by_month = [], {}
    for v in vals:
        last_by_month[v["date"][:7]] = v["total_nzd"]
    prior = bank
    for m in sorted(last_by_month):
        months.append({"m": m, "end": rd(last_by_month[m]), "ret": rd(last_by_month[m] / prior - 1, 5), "interest": rd(interest.get(m, 0.0))})
        prior = last_by_month[m]

    # limits as they stand
    ind = {}
    grp = {}
    for r in decisions:
        c = (r["payload"].get("card") or {})
        if c.get("market") and c.get("ticker"):
            if c.get("industry"):
                ind[(c["market"], c["ticker"])] = c["industry"]
            if c.get("group"):
                grp[(c["market"], c["ticker"])] = c["group"]
    by_ind, by_grp = defaultdict(float), defaultdict(float)
    for p in latest.get("positions", []):
        if p["sleeve"] != "core" and (p["market"], p["ticker"]) in ind:
            by_ind[ind[(p["market"], p["ticker"])]] += p["value_nzd"]
        if p["sleeve"] == "deal" and (p["market"], p["ticker"]) in grp:
            by_grp[grp[(p["market"], p["ticker"])]] += p["value_nzd"]
    sleeves = {s: rd(latest.get("by_sleeve", {}).get(s, 0.0) / total, 5) for s in ("core", "deal", "special")}
    sleeves["cash"] = rd(latest["cash_nzd_total"] / total, 5)
    review = False
    for r in decisions:
        e = r["payload"].get("event")
        review = True if e == "review_required" else (False if e == "review_done" else review)
    limits = {
        "sleeves": [{"k": s, "now": sleeves.get(s, 0.0), "target": TARGETS[s], "band": BANDS.get(s), "max": SLEEVE_MAX.get(s)} for s in ("core", "deal", "special", "cash")],
        "cash_floor": CASH_FLOOR, "dd_halve": DD_HALVE, "dd_exit": DD_EXIT,
        "industry": {"cap": INDUSTRY_CAP, "top": sorted(([k, rd(v / total, 5)] for k, v in by_ind.items()), key=lambda x: -x[1])[:5]},
        "group": {"cap": GROUP_CAP, "top": sorted(([k, rd(v / total, 5)] for k, v in by_grp.items()), key=lambda x: -x[1])[:5]},
        "review_pending": review}

    # success tests (rulebook section 10), as they stand
    worst = min((v.get("drawdown", 0.0) for v in vals), default=0.0)
    tests = [
        {"n": 1, "name": "Ahead after all costs", "value": rd(total / bank - 1, 5), "met": total > bank},
        {"n": 2, "name": "Ahead of an index-and-cash mix with the same ups and downs", "value": rd((port[-1] - mix[-1]) if mix else None, 5),
         "met": (port[-1] > mix[-1]) if mix else None, "detail": f"{share:.0%} index, {1 - share:.0%} cash" if share is not None else None},
        {"n": 3, "name": "Against the core's index mix held at 100%", "value": rd((port[-1] - idx[-1]) if idx else None, 5),
         "met": (port[-1] > idx[-1]) if idx else None, "detail": "reported, not a pass mark"},
        {"n": 4, "name": "Worst fall never more than 10% below the peak", "value": rd(worst, 5), "met": worst > -0.10},
        {"n": 5, "name": "Our odds beat the market's across at least 40 dated calls", "value": n_res,
         "met": (ours < mkt) if (ours is not None and n_res >= 40) else None, "ours": rd(ours, 4), "market": rd(mkt, 4)}]

    # if every deal broke tonight: each deal holding falls to its break price (the monitor's,
    # moved by the market, or failing that the card's), in NZ$ at tonight's rate
    mon = {r["ticker"]: fnum(r.get("break_price")) for r in read_csv(os.path.join(ROOT, "reports", "deal_monitor.csv"))}
    stress = []
    for p in positions:
        if p["sleeve"] != "deal":
            continue
        bp = mon.get(p["ticker"]) or (p["card"] or {}).get("break_price")
        if bp and p["close"]:
            loss = p["qty"] * (bp - p["close"]) * (p["value"] / (p["qty"] * p["close"]))
            stress.append({"tk": p["ticker"], "break": rd(bp, 4), "loss": rd(min(0.0, loss))})
    stress_total = sum(x["loss"] for x in stress)

    # where the money came from, since the start
    hedge_mtm = latest.get("hedge_mtm_nzd", 0.0) or 0.0
    attr = {"positions": [{"tk": p["ticker"], "s": p["sleeve"], "nzd": p["pnl"]} for p in positions],
            "closed": [{"tk": k[2], "s": k[0], "nzd": rd(b["realised_nzd"])} for k, b in basis.items() if b["qty"] <= 1e-9 and abs(b["realised_nzd"]) > 0.005],
            "interest": rd(sum(interest.values())), "hedges": rd(st["hedge_realised_nzd"] + hedge_mtm),
            "plan_fees": rd(-costs.get("plan", 0.0)), "conversion_fees": rd(-costs.get("fx", 0.0))}
    explained = sum(x["nzd"] or 0 for x in attr["positions"]) + sum(x["nzd"] or 0 for x in attr["closed"]) + attr["interest"] + attr["hedges"] + attr["plan_fees"] + attr["conversion_fees"]
    attr["other"] = rd((total - bank) - explained)
    attr["total"] = rd(total - bank)

    day_change = total - prev["total_nzd"] if prev else total - bank
    return dict(base, started=True, as_of=latest["date"], days=len(vals), chain=L.verify(),
                summary={"total": rd(total), "unhedged": rd(latest.get("total_unhedged_nzd", total)), "day": rd(day_change),
                         "day_pct": rd(day_change / (prev["total_nzd"] if prev else bank), 5), "since": rd(total - bank),
                         "since_pct": rd(total / bank - 1, 5), "peak": rd(latest.get("peak_nzd")), "dd": rd(latest.get("drawdown", 0.0), 5),
                         "cash": rd(latest["cash_nzd_total"]), "cash_by_ccy": {k: rd(v) for k, v in latest.get("cash_nzd", {}).items()},
                         "hedge_mtm": rd(latest.get("hedge_mtm_nzd", 0.0)), "dividends_owed": rd(latest.get("dividends_owed_nzd", 0.0)),
                         "flags": latest.get("flags", []), "cash_rate": rd(cash_rate, 5),
                         "realised": rd(sum(b["realised_nzd"] for b in basis.values()))},
                series=series, positions=positions, orders=orders, activity=acts[:400],
                calls={"list": calls, "ours": rd(ours, 4), "market": rd(mkt, 4), "resolved": n_res, "made": len(made)},
                costs={k: rd(v) for k, v in costs.items()}, months=months, limits=limits, tests=tests,
                stress={"deals": stress, "total": rd(stress_total), "pct": rd(stress_total / total, 5)}, attribution=attr)


# ---------- deals, system and the timeline ----------
def deal_file(ticker: str, market: str = "ASX") -> dict | None:
    """research/deals/<TICKER>.md (NZX: NZ_<TICKER>.md): the header fields and the main sections."""
    p = os.path.join(ROOT, "research", "deals", (f"NZ_{ticker}" if market == "NZX" else ticker) + ".md")
    if not os.path.exists(p):
        return None
    txt = open(p, encoding="utf-8").read()
    head, body = {}, txt
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line and not line.startswith(" "):
                k, v = line.split(":", 1)
                v = re.sub(r"\s+#.*$", "", v).strip()
                head[k.strip()] = v
        body = m.group(2)
    secs = {}
    for part in re.split(r"^## ", body, flags=re.M)[1:]:
        title, _, rest = part.partition("\n")
        secs[title.strip().lower()] = rest.strip()[:3000]
    split = lambda v: [x.strip() for x in (v or "").split(";") if x.strip()]
    return {"head": {k: v for k, v in head.items() if v}, "summary": secs.get("in short", ""),
            "conditions_open": split(head.get("conditions_open")), "conditions_met": split(head.get("conditions_met")),
            "conditions": secs.get("conditions", ""), "dates": secs.get("key dates", ""), "risks": secs.get("risks to completion", ""),
            "recent": secs.get("recent announcements", ""), "checked": head.get("last_checked")}


def deal_events(rows: list[dict], today: str, days: int = 21) -> list[dict]:
    """Dated events for live deals in the next few weeks, from the deal files and the live list."""
    out = []
    end = (date.fromisoformat(today) + timedelta(days=days)).isoformat()
    names = {"booklet_date": "Scheme booklet", "first_court_date": "First court hearing", "meeting_date": "Scheme meeting",
             "offer_close_date": "Offer closes", "second_court_date": "Second court hearing", "effective_date": "Scheme effective",
             "record_date": "Record date", "implementation_date": "Payment", "end_date": "End date in the deed"}
    for r in rows:
        f = (r.get("file") or {}).get("head", {})
        seen = set()
        for k, label in names.items():
            v = (f.get(k) or r.get(k) or "")[:10]
            if re.match(r"\d{4}-\d\d-\d\d$", v) and today <= v <= end and (k, v) not in seen:
                seen.add((k, v))
                out.append({"date": v, "tk": r["tk"], "m": r["m"], "what": label, "held": r["held"],
                            "firm": "indicative" not in (f.get("dates_basis") or "").lower() or k in (f.get("dates_basis") or "")})
    return sorted(out, key=lambda e: (e["date"], e["tk"]))


def deals_section(names: dict, held: set) -> dict:
    live = {r["deal_id"]: r for r in read_csv(os.path.join(ROOT, "config", "live_deals.csv"))}
    hp = os.path.join(ROOT, "reports", "deal_history.json")
    hist = json.load(open(hp)) if os.path.exists(hp) else {}
    rows = []
    for r in read_csv(os.path.join(ROOT, "reports", "deal_monitor.csv")):
        lv = live.get(r["deal_id"], {})
        mkt = lv.get("target_market", "ASX")
        tk = r["ticker"]
        rows.append({"id": r["deal_id"], "m": mkt, "tk": tk, "name": names.get((mkt, tk.upper()), ""), "structure": r["structure"],
                     "price": fnum(r["price"]), "offer": fnum(r["offer_value"]), "spread": fnum(r["gross_spread"]),
                     "days": fnum(r["days_to_payment"]), "yearly": fnum(r["yearly"]), "yearly_net": fnum(r["yearly_after_costs"]),
                     "implied": fnum(r["market_implied"]), "implied_note": r.get("implied_note") or None, "base": fnum(r["base_rate"]),
                     "base_n": fnum(r["base_rate_n"]), "pay": r["expected_payment"], "note": r["note"], "as_of": r["as_of"],
                     "announced": lv.get("announce_date") or None, "acquirer": lv.get("acquirer_ticker") or None,
                     "cash": fnum(lv.get("cash_per_share")), "ratio": fnum(lv.get("scrip_ratio")), "held": (mkt, tk) in held,
                     "stage": r.get("stage") or lv.get("stage") or "announced", "base_note": r.get("base_note") or "",
                     "break": fnum(r.get("break_price")), "undisturbed": fnum(r.get("undisturbed")), "market_move": fnum(r.get("market_move")),
                     "meeting_date": r.get("meeting_date") or lv.get("meeting_date") or None, "end_date": r.get("end_date") or lv.get("end_date") or None,
                     "hist": hist.get(r["deal_id"], []), "file": deal_file(tk, mkt),
                     "px": closes(mkt, tk, (date.today() - timedelta(days=150)).isoformat(), 110)})
    leads = []
    md = os.path.join(ROOT, "reports", "deal_monitor.md")
    if os.path.exists(md):
        txt = open(md, encoding="utf-8").read()
        sect = txt.split("## US leads from SEC merger filings", 1)[-1] if "## US leads" in txt else ""
        for line in sect.splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 8 and cells[0] not in ("Ticker", "---"):
                m = re.match(r"([+-]?[\d.]+)%", cells[4])
                leads.append({"tk": cells[0], "name": cells[1].title(), "cash": fnum(cells[2]), "last": fnum(cells[3]),
                              "spread": fnum(m.group(1)) / 100 if m else None, "check": "check" in cells[4],
                              "first": cells[5], "latest": cells[6], "forms": cells[7]})
    return {"rows": rows, "us_leads": leads, "events": deal_events(rows, date.today().isoformat()),
            "odds_note": first_match(os.path.join(ROOT, "reports", "deal_odds.md"), r"(- Completed with the first bidder:[^\n]*)") or ""}


def checks_section() -> list[dict]:
    """Engine check suites: results from tonight's run if the workflow ran them, otherwise run them."""
    out = []
    for t in sorted(glob.glob(os.path.join(ROOT, "tests", "test_*.py"))):
        r = subprocess.run([sys.executable, "-I", t], capture_output=True, text=True, cwd=ROOT, timeout=600)
        n_pass = len(re.findall(r"^PASS ", r.stdout, re.M))
        n_fail = len(re.findall(r"^FAIL ", r.stdout, re.M))
        out.append({"name": os.path.basename(t)[5:-3].replace("_", " "), "ok": r.returncode == 0, "pass": n_pass, "fail": n_fail})
    return out


def first_match(path: str, pattern: str) -> str | None:
    if not os.path.exists(path):
        return None
    m = re.search(pattern, open(path, encoding="utf-8").read())
    return m.group(1) if m else None


def history_tests() -> list[dict]:
    ins = os.path.join(ROOT, "reports", "special_insider_history.md")
    dl = os.path.join(ROOT, "reports", "deal_us_history.md")
    def count(sample):
        rows = [r for r in read_csv(os.path.join(ROOT, "config", sample)) if r.get("ticker") != "SPY"]   # SPY is the yardstick, not a sampled company
        d = os.path.join(ROOT, "data", "history", "prices", "US")
        done = sum(1 for r in rows if os.path.exists(os.path.join(d, f"{r['ticker']}.csv")) or os.path.exists(os.path.join(d, f"{r['ticker']}.csv.none")))
        return done, len(rows)
    a, b = count("universe_history.csv")
    c, d = count("universe_history_deals.csv")
    return [
        {"name": "Rules-only screen", "ref": "6", "status": "fail", "detail": "Ahead of the market before costs, behind after them. Sleeve dropped; its 10% went to cash."},
        {"name": "US director and officer buying clusters", "ref": "9a", "status": first_match(ins, r"\*\*Result: (pass|fail)\.\*\*") or "waiting",
         "detail": f"{a} of {b} sampled companies priced", "done": a, "of": b},
        {"name": "US cash deal spreads", "ref": "9b", "status": first_match(dl, r"\*\*Result: (pass|fail)\.\*\*") or "waiting",
         "detail": f"{c} of {d} sampled companies priced", "done": c, "of": d}]


def feeds_section() -> dict:
    out = {}
    for m in ("US", "ASX", "NZX"):
        d = os.path.join(ROOT, "data", "prices", m)
        lasts = []
        for f in glob.glob(os.path.join(d, "*.csv")):
            try:
                with open(f, "rb") as fh:
                    fh.seek(0, 2); size = fh.tell(); fh.seek(max(0, size - 400))
                    tail = fh.read().decode(errors="ignore").strip().splitlines()
                lasts.append(tail[-1].split(",")[0])
            except OSError:
                continue
        lasts = [x for x in lasts if re.match(r"\d{4}-\d\d-\d\d$", x)]
        latest = max(lasts) if lasts else None
        out[m] = {"latest": latest, "names": len(lasts), "behind": sum(1 for x in lasts if latest and x < latest)}
    def problems(path):
        if not os.path.exists(path):
            return {"ran": None, "problems": []}
        txt = open(path, encoding="utf-8").read()
        ran = txt.splitlines()[0] if txt else None
        probs = txt.split("PROBLEMS:", 1)[1].strip().splitlines() if "PROBLEMS:" in txt else []
        return {"ran": ran, "problems": probs[:12]}
    out["runs"] = {"prices": problems(os.path.join(ROOT, "data", "prices", "last_run.txt")),
                   "nzx": problems(os.path.join(ROOT, "data", "prices", "NZX", "last_run.txt"))}
    return out


def readiness() -> list[dict]:
    rows = []
    p = os.path.join(ROOT, "docs", "READINESS.md")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 4 and cells[0].isdigit():
                rows.append({"n": int(cells[0]), "item": cells[1], "status": cells[2], "note": cells[3]})
    return rows


def desk_log(n: int = 8) -> list[dict]:
    p = os.path.join(ROOT, "research", "desk_log.md")
    if not os.path.exists(p):
        return []
    parts = re.split(r"^## ", open(p, encoding="utf-8").read(), flags=re.M)[1:]
    out = [{"head": x.splitlines()[0].strip(), "body": "\n".join(x.splitlines()[1:]).strip()[:2400]} for x in parts]
    return out[-n:][::-1]


def data_checks() -> dict:
    p = os.path.join(ROOT, "reports", "data_checks.json")
    return json.load(open(p)) if os.path.exists(p) else {}


def build(source: str = "manual") -> dict:
    cfg = json.load(open(os.path.join(ROOT, "config", "run.json")))
    names = names_map()
    fx = FX(os.path.join(ROOT, "data"))
    try:
        rates = Rates(os.path.join(ROOT, "data"))
    except Exception:
        rates = None
    ledgers = {}
    for name in ("practice", "counted"):
        if name in cfg["ledgers"]:
            ledgers[name] = ledger_section(cfg, name, names, fx, rates)
    act = cfg.get("active")
    held = {(p["market"], p["ticker"]) for p in (ledgers.get(act) or {}).get("positions", [])}
    ms = [{"name": r["milestone"], "date": r["date"], "status": r["status"]} for r in read_csv(os.path.join(ROOT, "config", "milestones.csv"))]
    steps = {}
    try:
        raw = json.loads(os.environ.get("HUB_RUN_STEPS") or "{}")      # the workflow's toJSON(steps)
        steps = {k: (v.get("outcome") if isinstance(v, dict) else v) for k, v in raw.items()}
    except (ValueError, AttributeError):
        pass
    commit = os.environ.get("GITHUB_SHA") or subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=ROOT).stdout.strip()
    return {
        "schema": SCHEMA, "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "source": source,
        "commit": commit[:12], "active": act, "ledgers": ledgers,
        "rules": {"targets": TARGETS, "bands": {k: list(v) for k, v in BANDS.items()}, "caps": CAPS, "cash_floor": CASH_FLOOR,
                  "dd_halve": DD_HALVE, "dd_exit": DD_EXIT, "industry_cap": INDUSTRY_CAP, "group_cap": GROUP_CAP,
                  "core": cfg["core"]["lines"]},
        "deals": deals_section(names, held),
        "system": {"run": {"source": source, "steps": steps, "run_id": os.environ.get("GITHUB_RUN_ID"),
                           "workflow": os.environ.get("GITHUB_WORKFLOW")},
                   "feeds": feeds_section(), "checks": checks_section(), "history_tests": history_tests(),
                   "readiness": readiness(), "milestones": ms, "desk_log": desk_log(), "data_checks": data_checks()},
    }


def oidc_token() -> str:
    url, tok = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL"), os.environ.get("ACTIONS_ID_TOKEN_REQUEST_TOKEN")
    if not url or not tok:
        raise SystemExit("no GitHub identity token here: posting only works inside a GitHub Actions job with id-token: write")
    req = urllib.request.Request(f"{url}&audience={AUDIENCE}", headers={"Authorization": f"bearer {tok}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())["value"]


def post(snap: dict) -> str:
    body = json.dumps(snap, separators=(",", ":")).encode()
    req = urllib.request.Request(INGEST_URL, data=body, method="POST",
                                 headers={"Authorization": f"Bearer {oidc_token()}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode()[:300]


def main(argv: list[str]) -> int:
    source = next((a for a in argv if not a.startswith("--")), "manual")
    snap = build(source)
    out = os.path.join(ROOT, "reports", "hub")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "snapshot.json"), "w") as f:
        json.dump(snap, f, separators=(",", ":"))
    size = os.path.getsize(os.path.join(out, "snapshot.json"))
    print(f"snapshot: {size / 1024:.0f} KB, active {snap['active']}, "
          + ", ".join(f"{k} {'from ' + v['as_of'] if v.get('started') else 'not started'}" for k, v in snap["ledgers"].items()))
    if "--post" in argv:
        print("posted:", post(snap))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
