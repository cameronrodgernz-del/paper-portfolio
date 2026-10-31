"""The nightly mechanical run, for one ledger (practice, counted or a dry run).

1. On the start date, deposit the bankroll.
2. Run the clerk for every weekday not yet run, up to the given date (a missed run is caught up
   on real prices; nothing is backdated, because each run only fills sessions after each decision).
3. Core by rule: on the first run, buy the core at its target weights; at the first run of each
   quarter, if the core is outside its band, bring each line back to target.
4. Write reports/<ledger>/latest.json and reports/<ledger>/daily/<date>.md.

The analysts' decisions are not made here; they are placed in the ledger with place_order()
by the evening analyst session, after this run.
Usage: python3 -I src/daily.py [ledger_name] [up_to_date]   (defaults: config active ledger, today NZ)
"""
import json
import math
import os
import sys
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from clerk import place_order, run, state  # noqa: E402
from ledger import Ledger  # noqa: E402
from market_data import CURRENCY, FX, Prices, nz_evening_utc  # noqa: E402
from rates import Rates  # noqa: E402
from risk import MIN_ORDER  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def cash_rate(cfg: dict, rates: Rates, month: str, L: Ledger | None = None) -> tuple[float, str]:
    """The month's cash rate: as set in config/run.json, else the rate the first run of the month
    used (so it stays fixed for the month), else the NZ 3-month bank rate less one point."""
    if month in cfg.get("cash_rate_by_month", {}):
        return float(cfg["cash_rate_by_month"][month]), "set for the month"
    if L is not None:
        used = [r["payload"]["rate"] for r in L.records("cash")
                if r["payload"]["kind"] == "interest" and (r["payload"].get("for_date") or "")[:7] == month]
        if used:
            return used[0], "fixed at the month's first run"
    r = max(rates.three_month("NZD", f"{month}-01") - 0.01, 0.0)
    return round(r, 4), "NZ 3-month bank rate less 1 point"


def drawdown_rules(L: Ledger, prices: Prices, fx: FX, run_date: str, val: dict) -> list[str]:
    """Rulebook section 3, by rule: at 8% below the peak, sell half of each deal and special
    situation holding; at 12%, sell the rest and require a review before any new active position.
    Each step happens once per peak; a new peak starts again."""
    out = []
    peak, dd = val["peak_nzd"], val["drawdown"]
    done = {(r["payload"].get("level"), r["payload"].get("peak")) for r in L.records("decisions")
            if r["payload"].get("event") == "drawdown_rule"}
    decided = (nz_evening_utc(run_date) + timedelta(minutes=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    for level, share in ((0.12, 1.0), (0.08, 0.5)):
        if dd > -level or (level, peak) in done:
            continue
        if level == 0.08 and (0.12, peak) in done:
            continue
        L.append("decisions", {"event": "drawdown_rule", "level": level, "peak": peak, "drawdown": dd, "date": run_date}, ts=decided)
        for o in state(L)["open_orders"]:       # waiting active buys would undo the rule: cancel them
            if o["sleeve"] in ("deal", "special") and o["side"] == "buy":
                L.append("orders", {"event": "cancel", "order_id": o["order_id"], "reason": f"fall of {dd:.1%} from the peak"}, ts=decided)
                out.append(f"cancelled waiting buy {o['order_id']}")
        held = {k: q for k, q in state(L)["positions"].items() if k[0] in ("deal", "special") and q > 0}
        for (sleeve, m, t), q in sorted(held.items()):
            qty = q if share == 1.0 else math.floor(q * share)
            if qty <= 0:
                continue
            try:
                o = place_order(L, prices, fx, decided, sleeve, m, t, "sell", qty=qty,
                                decision={"rule": f"fall of {dd:.1%} from the peak: sell {'all' if share == 1.0 else 'half'}"})
                out.append(f"sell {qty:g} {m}:{t} ({'all' if share == 1.0 else 'half'}, fall {dd:.1%})")
            except ValueError as e:
                out.append(f"could not place the sale of {m}:{t}: {e}")
        if level == 0.12:
            L.append("decisions", {"event": "review_required", "date": run_date, "drawdown": dd}, ts=decided)
            out.append("review required before any new deal or special situation")
        break
    # while a 12% review is pending, anything still held in the active sleeves (a sale cut by the
    # volume cap that lapsed, say) is offered for sale again each night
    from decide import review_pending
    if review_pending(L):
        st = state(L)
        selling = {(o["sleeve"], o["market"], o["ticker"]) for o in st["open_orders"] if o["side"] == "sell"}
        for (sleeve, m, t), q in sorted(st["positions"].items()):
            if sleeve in ("deal", "special") and q > 0 and (sleeve, m, t) not in selling:
                try:
                    place_order(L, prices, fx, decided, sleeve, m, t, "sell", qty=q, decision={"rule": "12% review pending: sell what is left"})
                    out.append(f"sell {q:g} {m}:{t} (left after the 12% rule)")
                except ValueError as e:
                    out.append(f"could not place the sale of {m}:{t}: {e}")
    return out


def weekdays(a: date, b: date):
    d = a
    while d <= b:
        if d.weekday() < 5:
            yield d
        d += timedelta(days=1)


def core_orders(L: Ledger, prices: Prices, fx: FX, cfg: dict, run_date: str, first: bool, val: dict) -> list[str]:
    total = val["total_nzd"]
    core_now = val["by_sleeve"].get("core", 0.0)
    lo, hi = cfg["core"]["band"]
    quarter_start = run_date[5:7] in ("01", "04", "07", "10") and not any(
        r["payload"]["date"][:7] == run_date[:7] for r in L.records("valuations")[:-1])
    held = {(p["market"], p["ticker"]): p["value_nzd"] for p in val["positions"] if p["sleeve"] == "core"}
    pending = {(o["market"], o["ticker"]) for o in state(L)["open_orders"] if o["sleeve"] == "core"}
    # a line never bought (say its price feed was late on day one) is bought at the next run
    missing = [(x["market"], x["ticker"]) for x in cfg["core"]["lines"]
               if (x["market"], x["ticker"]) not in held and (x["market"], x["ticker"]) not in pending]
    rebalance = first or (quarter_start and not lo <= core_now / total <= hi)
    if not rebalance and not missing:
        return []
    decided = (nz_evening_utc(run_date) + timedelta(minutes=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    out = []
    for line in cfg["core"]["lines"]:
        m, t = line["market"], line["ticker"]
        if (m, t) in pending or (not rebalance and (m, t) not in missing):
            continue
        gap = line["weight"] * total - held.get((m, t), 0.0)
        ccy, smallest = MIN_ORDER[m]
        if abs(gap) * fx.per_nzd(ccy, run_date) < smallest:
            continue
        side = "buy" if gap > 0 else "sell"
        try:
            o = place_order(L, prices, fx, decided, "core", m, t, side, value_nzd=abs(gap),
                            decision={"rule": "core at target" if first else ("core back inside its band at the quarter" if rebalance
                                                                  else "core line not yet bought"),
                                      "target_weight": line["weight"]})
            out.append(f"{side} {o['qty']} {m}:{t} (about NZ${abs(gap):,.0f})")
        except ValueError as e:
            out.append(f"could not place {m}:{t}: {e}")
    return out


def write_reports(name: str, L: Ledger, reports: list[dict], placed: list[str], rate_note: str) -> None:
    out_dir = os.path.join(ROOT, "reports", name)
    os.makedirs(os.path.join(out_dir, "daily"), exist_ok=True)
    vals = [r["payload"] for r in L.records("valuations")]
    if not vals:
        return
    v = vals[-1]
    latest = {"ledger": name, "date": v["date"], "total_nzd": v["total_nzd"], "total_unhedged_nzd": v.get("total_unhedged_nzd"),
              "peak_nzd": v["peak_nzd"], "drawdown": v["drawdown"], "by_sleeve": v["by_sleeve"], "cash_nzd": v["cash_nzd"],
              "positions": v["positions"], "flags": v["flags"], "hedge_mtm_nzd": v.get("hedge_mtm_nzd"),
              "history": [{"date": x["date"], "total_nzd": x["total_nzd"], "total_unhedged_nzd": x.get("total_unhedged_nzd")} for x in vals],
              "chain": L.verify(), "cash_rate_basis": rate_note,
              "written_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    with open(os.path.join(out_dir, "latest.json"), "w") as f:
        json.dump(latest, f, indent=1)
    for r in reports:
        lines = [f"# {name}: {r['date']}", "", f"Value NZ${r['total_nzd']:,.2f} (from peak {r['drawdown']:+.2%}).", ""]
        for k, title in (("fills", "Fills"), ("cancelled", "Orders expired"), ("actions", "Corporate actions"),
                         ("hedges", "Hedges"), ("flags", "Limits")):
            if r.get(k):
                lines += [f"## {title}", ""] + [f"- {x}" for x in r[k]] + [""]
        if r is reports[-1] and placed:
            lines += ["## Orders placed by rule", ""] + [f"- {x}" for x in placed] + [""]
        with open(os.path.join(out_dir, "daily", f"{r['date']}.md"), "w") as f:
            f.write("\n".join(lines))


def main(name: str | None = None, upto: str | None = None) -> int:
    cfg = json.load(open(os.path.join(ROOT, "config", "run.json")))
    name = name or cfg.get("active")
    if not name:
        print("no active ledger; nothing to run")
        return 0
    led = cfg["ledgers"][name]
    now_nz = datetime.now(ZoneInfo("Pacific/Auckland"))
    if upto is None:
        # tonight's run only once tonight's prices are in (from 8pm NZ); a daytime run stops at yesterday
        upto = now_nz.date().isoformat() if now_nz.hour >= 20 else (now_nz.date() - timedelta(days=1)).isoformat()
    upto = min(upto, led["end"])
    if upto < led["start"]:
        print(f"{name} starts {led['start']}; nothing to run")
        return 0
    data = os.path.join(ROOT, "data")
    prices, fx, rates = Prices(data), FX(data), Rates(data)
    L = Ledger(os.path.join(ROOT, led["dir"]))
    bad = {t: s for t, s in L.verify().items() if s != "ok"}
    if bad:
        raise SystemExit(f"ledger chain broken: {bad}")
    first = not L.records("cash")
    if first:
        L.append("cash", {"kind": "deposit", "ccy": "NZD", "amount": float(cfg["bankroll_nzd"])},
                 ts=datetime.combine(date.fromisoformat(led["start"]), datetime.min.time(), ZoneInfo("Pacific/Auckland"))
                 .astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    done = {r["payload"]["date"] for r in L.records("valuations")}
    reports, placed, note = [], [], ""
    for d in weekdays(date.fromisoformat(led["start"]), date.fromisoformat(upto)):
        ds = d.isoformat()
        if ds in done:
            continue
        rate, note = cash_rate(cfg, rates, ds[:7], L)
        reports.append(run(L, prices, fx, ds, {"cash_rate": rate}, rates))
        val = L.records("valuations")[-1]["payload"]
        placed += drawdown_rules(L, prices, fx, ds, val)
        placed += core_orders(L, prices, fx, cfg, ds, first and len(reports) == 1, val)
    try:
        import actions
        for line in actions.missing(L, prices, upto):
            if reports:
                reports[-1]["flags"].append(line)
    except Exception as e:
        print("actions check failed:", type(e).__name__, e)
    # an analyst's decision must be written when it is timed: flag any written more than 10 minutes later
    for r in L.records("decisions"):
        if r["payload"].get("card") and r.get("written_utc"):
            lag = (datetime.fromisoformat(r["written_utc"].replace("Z", "+00:00")) -
                   datetime.fromisoformat(r["ts_utc"].replace("Z", "+00:00"))).total_seconds()
            if lag > 600 and reports:
                reports[-1]["flags"].append(f"decision {r['seq']} was written {lag / 60:.0f} minutes after its time")
    write_reports(name, L, reports, placed, note)
    if reports:
        try:
            import benchmarks
            benchmarks.main(name)
        except Exception as e:      # the comparison is a report, never a reason to stop the run
            print("benchmarks failed:", type(e).__name__, e)
        # the monthly report, for each month that ended during these runs
        months = sorted({r["date"][:7] for r in reports})
        prior = sorted({v["payload"]["date"][:7] for v in L.records("valuations")})
        for m in prior:
            if m < months[-1] and not os.path.exists(os.path.join(ROOT, "reports", name, "monthly", f"{m}.md")):
                try:
                    import monthly
                    monthly.main(name, m)
                except Exception as e:
                    print("monthly report failed:", type(e).__name__, e)
    for r in reports:
        print(r["date"], f"{r['total_nzd']:,.2f}", r["fills"], r.get("hedges", []), r["flags"])
    print("placed by rule:", placed or "none")
    return 0


if __name__ == "__main__":
    sys.exit(main(*(sys.argv[1:3])))
