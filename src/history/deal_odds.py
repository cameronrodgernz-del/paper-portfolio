"""Sharper starting odds for live deals, from the deal database (deals/all_deals.csv).

Three changes from the plain completion rate:
1. The holder's outcome, not the bidder's. A deal superseded by a rival that completed at the same or
   a higher price paid its holders: for an arbitrage position that is a win, not a failure.
2. The stage reached. A scheme whose booklet is out, or whose holders have voted for it, completes
   far more often than one announced last week. Rates are worked out for deals that reached each
   stage, counting only failures that happened after it. Where a failed deal's booklet date isn't
   recorded, it is counted against the booklet stage if it failed later than a quarter of completed
   deals had their booklet out (or if its failure date isn't known either): a cautious reading.
   Meetings and court hearings are recorded for every failed deal that reached them (the follow-up
   pass looked for them), so those stages use dated deals only. Rates are smoothed towards a half
   (Jeffreys: paid plus a half over deals plus one), so no stage reads as certain.
3. Timing: days from each stage to payment, for completed deals, by structure and by the approvals
   needed.

A small model on deal features (bidder type, approvals, board support, lock-ups, premium, size) is
also tested, by five-fold cross-validation against the structure rate alone. It is used only if it
scores better out of sample.

Writes reports/deal_odds.json (read by the deal monitor) and reports/deal_odds.md.
Usage: python3 -I src/history/deal_odds.py <repo_root>
"""
import csv
import json
import math
import os
import statistics as stats
import sys
from collections import defaultdict
from datetime import date

RESOLVED = {"completed", "terminated", "withdrawn", "lapsed", "superseded_by_rival"}
STAGES = ["announced", "booklet_out", "vote_passed", "court_approved"]
STAGE_LABEL = {"announced": "announced", "booklet_out": "booklet or target's statement out", "vote_passed": "holders voted for it",
               "court_approved": "court approved or unconditional"}


def d(s):
    try:
        return date.fromisoformat((s or "").strip()[:10])
    except ValueError:
        return None


def num(s):
    try:
        return float(str(s).replace("%", "").replace(",", "").strip())
    except ValueError:
        return None


def holder_outcome(r: dict, by_id: dict) -> int | None:
    """1 if holders were paid at least the offer (by this bidder or a rival), 0 if not, None if unresolved."""
    o = r["outcome"]
    if o == "completed":
        return 1
    if o not in RESOLVED:
        return None
    if o == "superseded_by_rival":
        offer = num(r.get("offer_price_final")) or num(r.get("offer_price_initial"))
        best = None
        for x in (r.get("related_deal_ids") or "").split(";"):
            rv = by_id.get(x.strip())
            if rv and rv["outcome"] == "pending":
                return None   # the rival is still live: not resolved yet
            if rv and rv["outcome"] == "completed":
                p = num(rv.get("offer_price_final")) or num(rv.get("offer_price_initial"))
                best = max(best or 0, p or 0) if p else (best or -1)
        if best is None:
            return 0          # the rival didn't complete either
        if best == -1 or offer is None or best >= offer * 0.995:
            return 1          # a rival completed (at the same or a higher price, or price not recorded)
        return 0              # a rival completed, but at a lower price than this offer
    return 0


def reached(r: dict, stage: str) -> bool | None:
    """Did the deal reach this stage before its outcome? None when the dates can't say."""
    if stage == "announced":
        return True
    o, out = r["outcome"], d(r.get("outcome_date"))
    scheme = r["structure"] == "scheme"
    if o == "completed":
        if stage == "vote_passed" and not scheme:
            return None
        return True
    fr = (r.get("failure_reason") or "").lower()
    if stage == "booklet_out":
        b = d(r.get("booklet_date"))
        if b and (out is None or b <= out):
            return True
        if fr.startswith("vote"):
            return True
        if b is None and fr.startswith("regulator"):
            return False      # blocked by a regulator with no booklet recorded: it failed before the booklet
        return False if b is None and out and d(r["announce_date"]) and (out - d(r["announce_date"])).days < 30 else None
    if stage == "vote_passed":
        if not scheme:
            return None
        m = d(r.get("meeting_date"))
        if fr.startswith("vote"):
            return False
        if m and (out is None or m < out):
            return True
        return None
    if stage == "court_approved":
        c = d(r.get("court_date"))
        if c and (out is None or c <= out):
            return True
        return None
    return None


STAGE_FIELD = {"booklet_out": "booklet_date", "vote_passed": "meeting_date", "court_approved": "court_date"}


def stage_days(rows: list[dict]) -> dict:
    """For completed deals, the first quartile of days from announcement to each stage, by structure."""
    out = {}
    for struct in ("scheme", "full_takeover", "partial_takeover"):
        for st, f in STAGE_FIELD.items():
            xs = sorted((d(r[f]) - d(r["announce_date"])).days for r in rows
                        if r["structure"] == struct and r["outcome"] == "completed" and d(r.get(f)) and d(r["announce_date"]))
            if len(xs) >= 5:
                out[(struct, st)] = xs[len(xs) // 4]
    return out


def imputed(r: dict, st: str, q1: dict) -> bool:
    """Count an undated failure against stage st if it failed after a quarter of completed deals had got there."""
    a, o = d(r["announce_date"]), d(r.get("outcome_date"))
    days = (o - a).days if a and o else None
    if days is None:
        return True
    lim = q1.get((r["structure"], st)) or q1.get(("scheme", st))
    return lim is None or days >= lim


def stage_rates(rows: list[dict]) -> dict:
    out = {}
    q1 = stage_days(rows)
    for struct in ("scheme", "full_takeover", "all"):
        grp = [r for r in rows if struct == "all" or r["structure"] == struct]
        for st in STAGES:
            if st == "vote_passed" and struct == "full_takeover":
                continue
            known = [r for r in grp if reached(r, st) is True]
            unknown_fail = [r for r in grp if reached(r, st) is None and r["y"] == 0 and st == "booklet_out" and imputed(r, st, q1)]
            # holders paid by a rival with no booklet date: the same days rule, so wins and failures are treated alike
            unknown_win = [r for r in grp if reached(r, st) is None and r["y"] == 1 and st == "booklet_out" and imputed(r, st, q1)]
            win = sum(r["y"] for r in known)
            n_known = len(known)
            n_cautious = n_known + len(unknown_fail) + len(unknown_win)
            if not n_known:
                continue
            out[f"{struct}|{st}"] = {"structure": struct, "stage": st, "n": n_known, "paid": win,
                                     "rate_known": round(win / n_known, 4),
                                     "rate": round((win + len(unknown_win) + 0.5) / (n_cautious + 1), 4), "n_cautious": n_cautious,
                                     "undated_failures": len(unknown_fail), "undated_wins": len(unknown_win)}
    return out


def regs(r: dict) -> set:
    return {x.strip() for x in (r.get("regulators") or "").split(";") if x.strip() and x.strip() != "none"}


def timing(rows: list[dict]) -> dict:
    """Median days to payment for completed deals: from announcement, by structure and by approvals;
    and from each later stage."""
    out = {}
    done = [r for r in rows if r["outcome"] == "completed"]
    pay = lambda r: d(r.get("implementation_date")) or d(r.get("outcome_date"))
    def med(xs):
        xs = [x for x in xs if x is not None and x >= 0]
        return {"median": int(stats.median(xs)), "q1": int(sorted(xs)[len(xs) // 4]), "q3": int(sorted(xs)[3 * len(xs) // 4]), "n": len(xs)} if len(xs) >= 5 else None
    for struct in ("scheme", "full_takeover"):
        g = [r for r in done if r["structure"] == struct]
        out[f"{struct}|announced"] = med([(pay(r) - d(r["announce_date"])).days for r in g if pay(r) and d(r["announce_date"])])
        out[f"{struct}|booklet_out"] = med([(pay(r) - d(r["booklet_date"])).days for r in g if pay(r) and d(r.get("booklet_date"))])
        out[f"{struct}|vote_passed"] = med([(pay(r) - d(r["meeting_date"])).days for r in g if pay(r) and d(r.get("meeting_date"))])
        out[f"{struct}|court_approved"] = med([(pay(r) - d(r["court_date"])).days for r in g if pay(r) and d(r.get("court_date"))])
        for key, test in (("ACCC", lambda r: "ACCC" in regs(r)), ("FIRB", lambda r: "FIRB" in regs(r)),
                          ("OIO", lambda r: "OIO" in regs(r)), ("overseas", lambda r: any(x.startswith("overseas") for x in regs(r))),
                          ("no approvals", lambda r: r.get("regulators", "").strip() in ("none",))):
            out[f"{struct}|announced|{key}"] = med([(pay(r) - d(r["announce_date"])).days for r in g if test(r) and pay(r) and d(r["announce_date"])])
    return {k: v for k, v in out.items() if v}


# ---------- the feature model, tested out of sample ----------
FEATURES = ["takeover", "partial", "private_equity", "infrastructure", "existing_holder", "consortium", "scrip_or_mixed",
            "board_for", "board_not_for", "firb", "accc", "oio", "overseas", "lockups_15", "stake_20", "premium_40", "nzx", "small"]


def feats(r: dict) -> list[float]:
    bt, rg = r["bidder_type"], regs(r)
    board = (r.get("board_recommendation") or "").strip()
    prem = num(r.get("premium_pct_announced"))
    val = num(r.get("equity_value_m"))
    return [r["structure"] == "full_takeover", r["structure"] == "partial_takeover", bt == "private_equity", bt == "infrastructure",
            bt == "existing_holder", bt == "consortium", r.get("consideration_type") in ("scrip", "mixed"),
            board in ("unanimous_for", "majority_for"), board in ("against", "neutral", "none"),
            "FIRB" in rg, "ACCC" in rg, "OIO" in rg, any(x.startswith("overseas") for x in rg),
            (num(r.get("intentions_pct")) or 0) >= 15, (num(r.get("pre_bid_stake_pct")) or 0) >= 20,
            prem is not None and prem >= 40, r["market"] == "NZX", val is not None and val < 250]


def brier(p, y):
    return sum((a - b) ** 2 for a, b in zip(p, y)) / len(y)


def model_test(rows: list[dict]) -> dict:
    try:
        import numpy as np
        from sklearn.linear_model import LogisticRegression
    except ImportError:
        return {"used": False, "why": "numpy or scikit-learn not available"}
    X = np.array([[float(v) for v in feats(r)] for r in rows]); y = np.array([r["y"] for r in rows])
    rng = np.random.default_rng(20261101)
    idx = rng.permutation(len(rows)); folds = np.array_split(idx, 5)
    out = {}
    for C in (0.05, 0.1, 0.3, 1.0):
        pm, pb, ys = [], [], []
        for k in range(5):
            te = folds[k]; tr = np.concatenate([folds[j] for j in range(5) if j != k])
            m = LogisticRegression(C=C, max_iter=2000).fit(X[tr], y[tr])
            pm += list(m.predict_proba(X[te])[:, 1])
            # the plain structure rate, from the training folds
            for i in te:
                s = rows[i]["structure"]; g = [y[j] for j in tr if rows[j]["structure"] == s]
                pb.append(sum(g) / len(g) if g else y[tr].mean())
            ys += list(y[te])
        out[C] = (brier(pm, ys), brier(pb, ys))
    bestC = min(out, key=lambda c: out[c][0])
    bm, bb = out[bestC]
    m = LogisticRegression(C=bestC, max_iter=2000).fit(X, y)
    coefs = {f: round(float(c), 3) for f, c in zip(FEATURES, m.coef_[0])}
    return {"used": bool(bm < bb - 0.002), "C": float(bestC), "brier_model": round(bm, 4), "brier_structure": round(bb, 4),
            "intercept": round(float(m.intercept_[0]), 4), "coef": coefs, "n": int(len(y)),
            "why": "scores better out of sample than the structure rate" if bm < bb - 0.002 else "doesn't beat the structure rate out of sample"}


def main(root: str) -> int:
    rows = list(csv.DictReader(open(os.path.join(root, "deals", "all_deals.csv"), encoding="utf-8", newline="")))
    by_id = {r["deal_id"]: r for r in rows}
    base = [r for r in rows if r.get("majority_buyout") != "Y"]
    res = []
    for r in base:
        y = holder_outcome(r, by_id)
        if y is not None:
            r["y"] = y; res.append(r)
    plain = sum(1 for r in res if r["outcome"] == "completed") / len(res)
    paid = sum(r["y"] for r in res) / len(res)
    rates = stage_rates(res)
    tim = timing(res)
    model = model_test([r for r in res if r["structure"] in ("scheme", "full_takeover", "partial_takeover")])
    prev_path = os.path.join(root, "reports", "deal_odds.json")
    if not model.get("coef") and os.path.exists(prev_path):
        # scikit-learn missing here: keep the last tested model rather than switch it off without a word
        prev = json.load(open(prev_path)).get("model") or {}
        if prev.get("coef"):
            model = dict(prev, why=(prev.get("why") or "") + f" (kept from the last run with scikit-learn; not retested on {date.today().isoformat()})")
            print("scikit-learn not installed: the deal-feature model is kept from the last run, not retested", file=sys.stderr)
    out = {"made": date.today().isoformat(), "resolved": len(res), "completed_rate": round(plain, 4), "paid_rate": round(paid, 4),
           "stages": rates, "timing": tim, "model": model, "features": FEATURES}
    json.dump(out, open(os.path.join(root, "reports", "deal_odds.json"), "w"), indent=1)

    L = ["# Deal odds: starting chances by stage, as a holder sees them", "",
         f"From {len(res)} resolved deals in the database (majority-holder buy-outs left out). Made {out['made']}.", "",
         f"- Completed with the first bidder: {plain:.0%}. Holders paid at least the offer, counting rival bids that completed at the same or a higher price: {paid:.0%}.",
         "- A rival bid that wins is a win for a holder, so the second figure is the one the engine starts from.", "",
         "## By stage reached", "",
         "Only failures after the stage count against it. A deal with no booklet date counts at the booklet stage if it ended later than a quarter of completed deals had their booklet out, whether it failed or its holders were paid by a rival, so wins and failures are treated alike; a deal blocked by a regulator with no booklet recorded failed before it. Meetings and court hearings are recorded for every failed deal that reached them, so those stages use dated deals only. Rates are smoothed so none reads as certain (paid plus a half, over deals plus one).", "",
         "| Structure | Stage reached | Deals | Paid | Rate used | Dated deals only | Undated failures | Undated rival wins |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for k, v in rates.items():
        L.append(f"| {v['structure'].replace('_', ' ')} | {STAGE_LABEL[v['stage']]} | {v['n_cautious']} | {v['paid']} | {v['rate']:.0%} | {v['rate_known']:.0%} of {v['n']} | {v['undated_failures']} | {v.get('undated_wins', 0)} |")
    L += ["", "## Days to payment, completed deals", "", "| From | Median | Middle half | Deals |", "| --- | --- | --- | --- |"]
    for k, v in tim.items():
        parts = k.split("|")
        lab = f"{parts[0].replace('_', ' ')}, {STAGE_LABEL[parts[1]]}" + (f", needing {parts[2]}" if len(parts) > 2 else "")
        L.append(f"| {lab} | {v['median']} | {v['q1']} to {v['q3']} | {v['n']} |")
    L += ["", "## Deal features", "",
          f"A penalised logistic model on {len(FEATURES)} features (bidder type, approvals needed, board support, lock-ups, bidder's stake, premium, market, size), "
          f"tested by five-fold cross-validation on {model.get('n', '')} deals. Brier score (lower is better): model {model.get('brier_model')}, structure rate alone {model.get('brier_structure')}. "
          f"Result: {model.get('why')}" + (", so the engine adjusts the stage rate by it." if model.get("used") else ", so the engine uses the stage rate and the analyst adjusts for features by hand, writing each adjustment down."), ""]
    if model.get("coef"):
        L += ["| Feature | Weight (log-odds) |", "| --- | --- |"] + [f"| {k.replace('_', ' ')} | {v:+.2f} |" for k, v in sorted(model["coef"].items(), key=lambda kv: -abs(kv[1]))]
    open(os.path.join(root, "reports", "deal_odds.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
