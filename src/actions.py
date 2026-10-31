"""Enter corporate actions in a ledger, checked, and find ones that are missing.

  python3 -I src/actions.py <ledger> dividend <market> <ticker> <ccy> <per_share> --ex YYYY-MM-DD --pay YYYY-MM-DD [--source URL]
  python3 -I src/actions.py <ledger> consideration <market> <ticker> <ccy> <per_share> --pay YYYY-MM-DD [--record YYYY-MM-DD] [--source URL]
  python3 -I src/actions.py <ledger> split <market> <ticker> <ratio> --effective YYYY-MM-DD [--source URL]
  python3 -I src/actions.py <ledger> void <seq> "<why>"
  python3 -I src/actions.py <ledger> check

A dividend is paid on its pay date to shares held before its ex-date. Consideration is paid on
its payment date to shares held before the record date (or still held, if none is given). A
split changes holdings from the first session on its effective date (the date the price feed
shows the new share count). A void stops an action that has not been applied yet.
`check` lists what the price feeds and the holdings suggest is missing.
"""
import json
import os
import sys
from datetime import date, datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from clerk import business_days, state  # noqa: E402
from ledger import Ledger  # noqa: E402
from market_data import CURRENCY, Prices  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _date(s: str, what: str) -> str:
    try:
        return date.fromisoformat(s).isoformat()
    except (TypeError, ValueError):
        raise SystemExit(f"{what} must be a date like 2026-12-31, not {s!r}")


def enter(L: Ledger, kind: str, args: list[str], opts: dict, now_utc: datetime) -> dict:
    ts = now_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    if kind == "void":
        seq = int(args[0])
        if not any(r["seq"] == seq for r in L.records("corporate_actions")):
            raise SystemExit(f"no corporate action {seq}")
        if seq in state(L)["applied"]:
            raise SystemExit(f"action {seq} has already been applied; book a correcting action instead")
        return L.append("corporate_actions", {"type": "void", "ref": seq, "why": args[1] if len(args) > 1 else ""}, ts=ts)
    market, ticker = args[0], args[1].upper()
    if market not in CURRENCY:
        raise SystemExit(f"market must be one of {', '.join(CURRENCY)}")
    rec = {"type": kind, "market": market, "ticker": ticker, "source": opts.get("source", "")}
    if kind in ("dividend", "consideration"):
        ccy, per = args[2].upper(), float(args[3])
        if per <= 0:
            raise SystemExit("per_share must be above zero")
        rec.update(ccy=ccy, per_share=per, pay_date=_date(opts.get("pay"), "--pay"))
        if kind == "dividend":
            rec["ex_date"] = _date(opts.get("ex"), "--ex")
            if rec["ex_date"] > rec["pay_date"]:
                raise SystemExit("the ex-date must be on or before the pay date")
        elif opts.get("record"):
            rec["record_date"] = _date(opts["record"], "--record")
    elif kind == "split":
        ratio = float(args[2])
        if ratio <= 0 or ratio == 1:
            raise SystemExit("ratio is new shares per old share, e.g. 2 for 2-for-1, 0.1 for a 1-for-10 consolidation")
        rec.update(ratio=ratio, effective_date=_date(opts.get("effective"), "--effective"))
    else:
        raise SystemExit(f"unknown action {kind}")
    return L.append("corporate_actions", rec, ts=ts)


def missing(L: Ledger, prices: Prices, today: str) -> list[str]:
    """Dividends and splits the price feed shows for a held share with no action entered, and held
    shares with no new price for five business days (a scheme may have been implemented)."""
    out = []
    st = state(L)
    held = {(m, t) for (_, m, t), q in st["positions"].items() if q > 0}
    ca = [r["payload"] for r in L.records("corporate_actions")]
    first_fill = {}
    for r in L.records("fills"):
        p = r["payload"]
        first_fill.setdefault((p["market"], p["ticker"]), p["date"])
    for m, t in sorted(held):
        path = os.path.join(prices.dir, "prices", m, f"{t}.csv")
        if os.path.exists(path):
            import csv
            for r in csv.DictReader(open(path, newline="")):
                if r["date"] <= first_fill.get((m, t), "9999"):
                    continue
                try:
                    div, split = float(r.get("dividend") or 0), float(r.get("split") or 1)
                except ValueError:
                    continue
                if div > 0 and not any(a.get("type") == "dividend" and a["ticker"] == t and a.get("ex_date") == r["date"] for a in ca):
                    out.append(f"{m}:{t}: the price feed shows a dividend of {div:g} going ex on {r['date']}, and none is entered")
                if split not in (0, 1) and not any(a.get("type") == "split" and a["ticker"] == t and a.get("effective_date") == r["date"] for a in ca):
                    out.append(f"{m}:{t}: the price feed shows a split of {split:g} on {r['date']}, and none is entered")
        bars = prices.bars(m, t)
        if bars and business_days(bars[-1].date, today) >= 5:
            pending = any(a.get("type") == "consideration" and a["ticker"] == t for a in ca)
            out.append(f"{m}:{t}: no new price since {bars[-1].date}" +
                       ("" if pending else "; if a scheme or offer has been paid out, enter the consideration"))
    return out


def main(argv: list[str]) -> int:
    name, kind = argv[0], argv[1]
    cfg = json.load(open(os.path.join(ROOT, "config", "run.json")))
    L = Ledger(os.path.join(ROOT, cfg["ledgers"][name]["dir"]))
    if kind == "check":
        for line in missing(L, Prices(os.path.join(ROOT, "data")), date.today().isoformat()) or ["nothing missing"]:
            print(line)
        return 0
    args, opts, i = [], {}, 2
    while i < len(argv):
        if argv[i].startswith("--"):
            opts[argv[i][2:]] = argv[i + 1]
            i += 2
        else:
            args.append(argv[i])
            i += 1
    rec = enter(L, kind, args, opts, datetime.now(timezone.utc))
    print(json.dumps(rec["payload"]), "as record", rec["seq"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
