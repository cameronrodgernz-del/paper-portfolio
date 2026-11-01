"""History test 9d (rulebook): shares left behind when a deal fails.

Events: ASX schemes and full takeovers in the deal database announced 2015 to 2025 that ended without
paying holders (the holder outcome of section 5), with an outcome date, leaving out majority-holder
buy-outs. Buy at the open after the outcome date; sell at the first of the open after a new control
deal for the company is announced, the open 252 sessions later, or the last close if it delists.
Result: return after costs less the market (VAS with dividends) over the same days. Nothing is tuned.
Runs once, when the Norgate universe is in; writes reports/failed_deal_history.md and a lock.
Usage: python3 -I src/history/failed_deal_test.py <repo_root> [--force]
"""
import csv
import math
import os
import statistics as stats
import sys
from collections import defaultdict
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from deal_odds import holder_outcome  # noqa: E402
from universe import Universe, ready  # noqa: E402

HOLD = 252
MIN_EVENTS = 20


def deal_symbol(root: str, u: Universe) -> callable:
    """(ticker, announce date) -> the Norgate symbol of that company, from the name-checked matches,
    else the security on that code trading on the announcement date."""
    from norgate_link import verified
    ver = verified(root)
    sym_of = {}
    mp = os.path.join(root, "data", "norgate", "matches.csv")
    for m in csv.DictReader(open(mp, encoding="utf-8")) if os.path.exists(mp) else []:
        if (m["ticker"], m["announce_date"]) in ver:
            sym_of[(m["ticker"], m["announce_date"])] = m["norgate_symbol"]
    by_code = defaultdict(list)
    for s in u.symbols:
        by_code[s.split("-")[0].split(".")[0].upper()].append(s)

    def find(ticker: str, ann: str) -> str | None:
        if (ticker, ann) in sym_of:
            return sym_of[(ticker, ann)]
        i = u.row_on_or_before(ann)
        for s in by_code.get(ticker.upper(), []):
            j = u.col[s]
            if i is not None and not math.isnan(u.c[i, j]):
                return s
        return None
    return find


def tstat(xs: list[float]) -> float:
    return stats.mean(xs) / (stats.stdev(xs) / math.sqrt(len(xs))) if len(xs) > 2 and stats.stdev(xs) > 0 else float("nan")


def main(root: str, force: bool = False) -> int:
    report = os.path.join(root, "reports", "failed_deal_history.md")
    lock = report + ".lock"
    title = "# History test 9d: shares left behind when a deal fails\n\n"
    if os.path.exists(lock) and not force:
        print("result already written; use --force to re-run (the re-run is recorded)"); return 0
    if not ready(root):
        open(report, "w").write(title + "Waiting for the Norgate whole-market prices (data/norgate/universe/).\n")
        print("waiting for the universe"); return 0
    u = Universe(root)
    rows = list(csv.DictReader(open(os.path.join(root, "deals", "all_deals.csv"), encoding="utf-8")))
    by_id = {r["deal_id"]: r for r in rows}
    find = deal_symbol(root, u)
    deals_by_sym = defaultdict(list)          # every deal's announcement, by company, for the re-bid exit
    for r in rows:
        if r["market"] == "ASX" and r.get("target_ticker") and r.get("announce_date"):
            s = find(r["target_ticker"].upper(), r["announce_date"][:10])
            if s:
                deals_by_sym[s].append(r["announce_date"][:10])
    res, why = [], defaultdict(int)
    for r in rows:
        if r["market"] != "ASX" or r.get("majority_buyout") == "Y" or r["structure"] not in ("scheme", "full_takeover"):
            continue
        if not ("2015" <= (r["announce_date"] or "")[:4] <= "2025"):
            continue
        if holder_outcome(r, by_id) != 0:
            continue
        out = (r.get("outcome_date") or "")[:10]
        if not out:
            why["no outcome date"] += 1; continue
        s = find(r["target_ticker"].upper(), r["announce_date"][:10])
        if not s or s not in u.col:
            why["no Norgate prices for the company"] += 1; continue
        j = u.col[s]
        i_in = u.row_after(out)
        if i_in is None or math.isnan(u.o[i_in, j]):
            why["no price after the deal ended"] += 1; continue
        if not u.tradable(j, i_in):
            why["not tradable at entry (price or traded value)"] += 1; continue
        later = sorted(d for d in deals_by_sym[s] if d > u.datestr[i_in])
        i_out, rebid = i_in + HOLD, False
        if later:
            k = u.row_after(later[0])
            if k is not None and k < i_out:
                i_out, rebid = k, True
        if i_out >= len(u.dates):
            why["holding period not over yet"] += 1; continue
        gross, i_sold, how = u.hold(j, i_in, i_out)
        cost = u.round_trip_cost(j, i_in, i_sold)
        mkt = u.market(i_in, max(i_sold, i_in + 1))
        res.append({"id": r["deal_id"], "ticker": r["target_ticker"], "entry": u.datestr[i_in], "exit": u.datestr[i_sold],
                    "year": u.datestr[i_in][:4], "gross": gross, "cost": cost, "mkt": mkt, "result": gross - cost - mkt,
                    "rebid": rebid, "how": how})
    L = [title.strip(), "", f"Rulebook section 9d. Run {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC{' (forced re-run)' if force else ''}.", ""]
    xs = [e["result"] for e in res]
    passed = False
    if len(xs) < MIN_EVENTS:
        L += [f"Only {len(xs)} events with prices; the test needs {MIN_EVENTS}. **Result: fail.**"]
    else:
        m, t = stats.mean(xs), tstat(xs)
        k = max(1, round(0.05 * len(xs)))
        trimmed = sorted(xs)[:-k]
        by_year = defaultdict(float)
        for e in res:
            by_year[e["year"]] += e["result"]
        total = sum(xs)
        top_year = max(by_year.values()) / total if total > 0 else float("inf")
        checks = [("At least 20 events", len(xs) >= MIN_EVENTS, str(len(xs))),
                  ("Mean after costs, less the market, above zero with t of 2 or more", m > 0 and t >= 2, f"{m:+.2%}, t {t:.2f}"),
                  ("Still above zero without the best 5% of events", stats.mean(trimmed) > 0, f"{stats.mean(trimmed):+.2%}"),
                  ("No single year more than half the total gain", total > 0 and top_year <= 0.5, f"{top_year:.0%}" if total > 0 else "no total gain")]
        passed = all(c[1] for c in checks)
        rb = [e for e in res if e["rebid"]]
        L += ["| Measure | Value |", "| --- | --- |",
              f"| Events | {len(xs)} |", f"| Mean gross return | {stats.mean(e['gross'] for e in res):+.2%} |",
              f"| Mean costs | {stats.mean(e['cost'] for e in res):.2%} |", f"| Mean market return, same days | {stats.mean(e['mkt'] for e in res):+.2%} |",
              f"| Mean result after costs, less the market | {m:+.2%} (median {stats.median(xs):+.2%}) |", f"| t-statistic | {t:.2f} |",
              f"| Hit rate | {sum(1 for x in xs if x > 0) / len(xs):.0%} |",
              f"| Bid again within the hold (reported only) | {len(rb)} of {len(xs)}, mean result {stats.mean(e['result'] for e in rb):+.2%} |" if rb else "| Bid again within the hold | none |",
              "", "| Year | Events | Mean result |", "| --- | --- | --- |"]
        for y in sorted(by_year):
            ys = [e["result"] for e in res if e["year"] == y]
            L.append(f"| {y} | {len(ys)} | {stats.mean(ys):+.2%} |")
        L += ["", "| Pass mark | Met | Value |", "| --- | --- | --- |"] + [f"| {a} | {'yes' if b else 'no'} | {c} |" for a, b, c in checks]
        L += ["", f"**Result: {'pass' if passed else 'fail'}.**"]
    L += ["", "Events left out, by reason: " + ("; ".join(f"{k} {v}" for k, v in sorted(why.items())) or "none") + ".",
          "", "Caveats: the deal database holds binding deals of about A$100m or more, so a later approach that never "
          "became binding doesn't end the hold early; overlapping holds move together, so the t-statistic overstates the evidence somewhat."]
    os.makedirs(os.path.dirname(report), exist_ok=True)
    open(report, "w").write("\n".join(L) + "\n")
    open(lock, "w").write(datetime.now(timezone.utc).isoformat())
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    sys.exit(main(a[0] if a else ".", "--force" in sys.argv))
