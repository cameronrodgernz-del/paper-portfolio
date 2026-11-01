"""History test 9e (rulebook): a model of the next takeover target.

At each quarter end, every tradable ASX share (Norgate universe, ETFs left out by name, at least 252
sessions of prices) gets features from its prices and the deal database, and a label: a binding control
deal announced for it within the next 12 months. A penalised logistic regression is fitted on quarter
ends 2011 to 2017 (penalty by five-fold cross-validation on those years). From 2019, at each quarter end
the 5 highest-scored shares are bought at the next open and sold at the open after the next quarter
end (a share that delists is sold at its last close). Result per quarter: the picks' mean return after
costs less the market (VAS with dividends). Runs once; writes reports/target_model_history.md and a lock.
Usage: python3 -I src/history/target_model_test.py <repo_root> [--force]
"""
import csv
import math
import os
import statistics as stats
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from deal_odds import holder_outcome  # noqa: E402
from failed_deal_test import deal_symbol, tstat  # noqa: E402
from universe import MARKET, MIN_PRICE, MIN_VALUE, Universe, ready  # noqa: E402

PICKS = 5
FEATURES = ["log_value", "ret_1m", "ret_3m", "ret_12m", "rel_12m", "below_high", "vol_3m", "volume_surge", "failed_2y"]
TRAIN = ("2011-01-01", "2017-12-31")
TEST_FROM = "2019-01-01"


def quarter_ends(u: Universe) -> list[int]:
    out = []
    for i in range(len(u.dates) - 1):
        a, b = u.datestr[i], u.datestr[i + 1]
        if a[5:7] in ("03", "06", "09", "12") and b[5:7] != a[5:7]:
            out.append(i)
    return out


def features(u: Universe, q: int, failed: dict) -> tuple[np.ndarray, np.ndarray]:
    """Rows of features for the shares eligible at quarter end q, and their column numbers."""
    if q < 260:
        return np.empty((0, len(FEATURES))), np.empty(0, dtype=int)
    tr, c = u.tr, u.c
    with np.errstate(all="ignore"):
        hist = np.sum(~np.isnan(c[: q + 1]), axis=0)
        medv = np.nanmedian(u.value[q - 59: q + 1], axis=0)
        ok = (hist >= 252) & (c[q] >= MIN_PRICE) & (medv >= MIN_VALUE) & ~np.isnan(tr[q - 252])
        ok &= np.array([u.is_share(s) for s in u.symbols])
        cols = np.where(ok)[0]
        m = u.col[MARKET]
        mret12 = tr[q, m] / tr[q - 252, m] - 1
        r1 = tr[q, cols] / tr[q - 21, cols] - 1
        r3 = tr[q, cols] / tr[q - 63, cols] - 1
        r12 = tr[q, cols] / tr[q - 252, cols] - 1
        high = np.nanmax(tr[q - 251: q + 1, cols], axis=0)
        below = tr[q, cols] / high - 1
        daily = tr[q - 62: q + 1, cols][1:] / tr[q - 62: q + 1, cols][:-1] - 1
        vol = np.nanstd(daily, axis=0)
        recent = np.nanmean(u.v[q - 19: q + 1, cols], axis=0)
        before = np.nanmedian(u.v[q - 139: q - 19, cols], axis=0)
        surge = np.log((recent + 1) / (before + 1))
    qd = date.fromisoformat(u.datestr[q])
    fl = np.array([1.0 if any(qd - timedelta(days=730) <= d <= qd for d in failed.get(u.symbols[j], [])) else 0.0 for j in cols])
    X = np.column_stack([np.log(medv[cols]), r1, r3, r12, r12 - mret12, below, vol, surge, fl])
    good = np.all(np.isfinite(X), axis=1)
    return X[good], cols[good]


def labels(u: Universe, q: int, cols: np.ndarray, deals: dict) -> np.ndarray:
    qd = date.fromisoformat(u.datestr[q])
    end = qd + timedelta(days=365)
    return np.array([1 if any(qd < d <= end for d in deals.get(u.symbols[j], [])) else 0 for j in cols])


def main(root: str, force: bool = False) -> int:
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    from sklearn.preprocessing import StandardScaler
    report = os.path.join(root, "reports", "target_model_history.md")
    lock = report + ".lock"
    title = "# History test 9e: a model of the next takeover target\n\n"
    if os.path.exists(lock) and not force:
        print("result already written; use --force to re-run (the re-run is recorded)"); return 0
    if not ready(root):
        open(report, "w").write(title + "Waiting for the Norgate whole-market prices (data/norgate/universe/).\n")
        print("waiting for the universe"); return 0
    u = Universe(root)
    rows = list(csv.DictReader(open(os.path.join(root, "deals", "all_deals.csv"), encoding="utf-8")))
    by_id = {r["deal_id"]: r for r in rows}
    find = deal_symbol(root, u)
    deals, failed = defaultdict(list), defaultdict(list)
    for r in rows:
        if r["market"] != "ASX" or not r.get("target_ticker") or not r.get("announce_date"):
            continue
        if r["structure"] not in ("scheme", "full_takeover") or r.get("majority_buyout") == "Y":
            continue
        s = find(r["target_ticker"].upper(), r["announce_date"][:10])
        if not s:
            continue
        deals[s].append(date.fromisoformat(r["announce_date"][:10]))
        if holder_outcome(r, by_id) == 0 and r.get("outcome_date"):
            failed[s].append(date.fromisoformat(r["outcome_date"][:10]))
    qs = quarter_ends(u)
    last_full = date.fromisoformat(u.datestr[-1]) - timedelta(days=365)
    # ---- fit on 2011 to 2017 ----
    Xs, ys = [], []
    for q in qs:
        if TRAIN[0] <= u.datestr[q] <= TRAIN[1]:
            X, cols = features(u, q, failed)
            if len(cols):
                Xs.append(X); ys.append(labels(u, q, cols, deals))
    X, y = np.vstack(Xs), np.concatenate(ys)
    sc = StandardScaler().fit(X)
    Z = sc.transform(X)
    best = None
    for C in (0.01, 0.03, 0.1, 0.3, 1.0):
        losses = []
        for tr_i, te_i in StratifiedKFold(5, shuffle=True, random_state=20261101).split(Z, y):
            mdl = LogisticRegression(C=C, max_iter=2000).fit(Z[tr_i], y[tr_i])
            p = mdl.predict_proba(Z[te_i])[:, 1]
            losses.append(float(np.mean((p - y[te_i]) ** 2)))
        if best is None or np.mean(losses) < best[1]:
            best = (C, float(np.mean(losses)))
    model = LogisticRegression(C=best[0], max_iter=2000).fit(Z, y)
    # ---- run once from 2019 ----
    res, hits, base, lift = [], [], [], defaultdict(lambda: [0, 0])
    top20, top50 = [0, 0], [0, 0]
    for k, q in enumerate(qs):
        if u.datestr[q] < TEST_FROM or k + 1 >= len(qs):
            continue
        q_next = qs[k + 1]
        i_in, i_out = q + 1, q_next + 1
        if i_out >= len(u.dates):
            continue
        X, cols = features(u, q, failed)
        if len(cols) < 50:
            continue
        p = model.predict_proba(sc.transform(X))[:, 1]
        order = np.argsort(-p)
        lab_known = date.fromisoformat(u.datestr[q]) <= last_full
        if lab_known:
            lab = labels(u, q, cols, deals)
            base.append((int(lab.sum()), len(lab)))
            for n, acc in ((20, top20), (50, top50)):
                acc[0] += int(lab[order[:n]].sum()); acc[1] += n
            dec = np.zeros(len(p), dtype=int)
            dec[order] = (np.arange(len(p)) * 10) // len(p)
            for d_, l_ in zip(dec, lab):
                lift[int(d_)][0] += int(l_); lift[int(d_)][1] += 1
        picks = [int(cols[o]) for o in order[:PICKS]]
        rets = []
        for j in picks:
            gross, i_sold, how = u.hold(j, i_in, i_out)
            rets.append(gross - u.round_trip_cost(j, i_in, i_sold))
        mkt = u.market(i_in, i_out)
        res.append({"quarter": u.datestr[q], "year": u.datestr[q][:4], "result": stats.mean(rets) - mkt,
                    "picks": [u.symbols[j] for j in picks]})
        if lab_known:
            lab_map = dict(zip((int(c) for c in cols), labels(u, q, cols, deals)))
            hits += [lab_map[j] for j in picks]
    L = [title.strip(), "", f"Rulebook section 9e. Run {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC{' (forced re-run)' if force else ''}.", "",
         f"Fitted on {len(y):,} share-quarters from 2011 to 2017 ({int(y.sum())} with a bid within 12 months); "
         f"penalty C = {best[0]} by cross-validation (Brier {best[1]:.4f}).", "",
         "| Feature | Weight (standardised) |", "| --- | --- |"] + \
        [f"| {f.replace('_', ' ')} | {w:+.2f} |" for f, w in sorted(zip(FEATURES, model.coef_[0]), key=lambda x: -abs(x[1]))] + [""]
    passed = False
    xs = [r["result"] for r in res]
    if len(xs) < 8:
        L += [f"Only {len(xs)} quarters to test. **Result: not run.**"]
    else:
        m, t = stats.mean(xs), tstat(xs)
        hit_rate = sum(hits) / len(hits) if hits else 0.0
        base_rate = sum(a for a, _ in base) / sum(b for _, b in base) if base else 0.0
        by_year = defaultdict(float)
        for r in res:
            by_year[r["year"]] += r["result"]
        total = sum(xs)
        top_year = max(by_year.values()) / total if total > 0 else float("inf")
        checks = [("Mean quarterly result after costs above the market, t of 2 or more", m > 0 and t >= 2, f"{m:+.2%} a quarter, t {t:.2f}"),
                  ("Picks bid within 12 months at least 3 times as often as the universe", base_rate > 0 and hit_rate >= 3 * base_rate,
                   f"{hit_rate:.1%} against {base_rate:.1%}"),
                  ("No single year more than half the total gain", total > 0 and top_year <= 0.5, f"{top_year:.0%}" if total > 0 else "no total gain")]
        passed = all(c[1] for c in checks)
        L += ["| Measure | Value |", "| --- | --- |", f"| Quarters | {len(xs)} ({res[0]['quarter']} to {res[-1]['quarter']}) |",
              f"| Mean result a quarter, after costs, less the market | {m:+.2%} (median {stats.median(xs):+.2%}) |", f"| t-statistic | {t:.2f} |",
              f"| Quarters ahead of the market | {sum(1 for x in xs if x > 0)} of {len(xs)} |",
              f"| Picks bid within 12 months | {sum(hits)} of {len(hits)} ({hit_rate:.1%}) |", f"| Universe bid within 12 months | {base_rate:.1%} |",
              f"| Top 20 bid within 12 months (reported only) | {top20[0]} of {top20[1]} |", f"| Top 50 bid within 12 months (reported only) | {top50[0]} of {top50[1]} |",
              "", "| Score band (1 = highest) | Share-quarters | Bid within 12 months |", "| --- | --- | --- |"]
        for d_ in sorted(lift):
            a, b = lift[d_]
            L.append(f"| {d_ + 1} | {b:,} | {a / b:.1%} |" if b else f"| {d_ + 1} | 0 | |")
        L += ["", "| Year | Quarters | Sum of results |", "| --- | --- | --- |"]
        for yr in sorted(by_year):
            L.append(f"| {yr} | {sum(1 for r in res if r['year'] == yr)} | {by_year[yr]:+.2%} |")
        L += ["", "| Pass mark | Met | Value |", "| --- | --- | --- |"] + [f"| {a} | {'yes' if b else 'no'} | {c} |" for a, b, c in checks]
        L += ["", f"**Result: {'pass' if passed else 'fail'}.**"]
    L += ["", "Caveats: the deal database holds binding deals of about A$100m or more, so smaller deals and approaches that never "
          "became binding count as misses; the 5 picks a quarter make a concentrated portfolio, so one bid moves a quarter a lot."]
    os.makedirs(os.path.dirname(report), exist_ok=True)
    open(report, "w").write("\n".join(L) + "\n")
    if not any("Result: not run" in x for x in L):
        open(lock, "w").write(datetime.now(timezone.utc).isoformat())
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    sys.exit(main(a[0] if a else ".", "--force" in sys.argv))
