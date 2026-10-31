"""Pick the fixed random sample of tickers the insider-cluster test will be priced on (rulebook 9a).

Tiingo's free plan allows 500 different symbols a month, so the test runs on a sample. The draw
is made once, with a fixed seed, before any prices are fetched, and written to
config/universe_history.csv for the history price job. SPY is always included.

Pool: every ticker with a 2-buyer cluster (the widest setting), a plain 1-to-5-letter ticker and a
cluster purchase price of at least US$3. Hold-out tickers (an event from 2020) are drawn first,
then tuning tickers (an event in 2010 to 2019) until the tuning years are covered or the budget runs out.
Usage: python3 -I src/history/insider_sample.py <repo_root> [hold_out_n] [tuning_n]
"""
import csv
import os
import random
import re
import sys

SEED = 20261101
TICKER = re.compile(r"^[A-Z]{1,5}$")


def main(root: str, hold_n: int = 250, tune_n: int = 200) -> int:
    path = os.path.join(root, "data", "history", "insider_clusters_n2.csv")
    hold, tune = set(), set()
    for r in csv.DictReader(open(path, newline="")):
        t = r["ticker"].strip().upper()
        if not TICKER.match(t) or float(r["avg_price"]) < 3:
            continue
        (tune if r["event_date"] < "2020-01-01" else hold).add(t)
    rng = random.Random(SEED)
    hold_pick = rng.sample(sorted(hold), min(hold_n, len(hold)))
    covered = set(hold_pick) & tune
    rest = sorted(tune - set(hold_pick))
    rng.shuffle(rest)
    tune_pick = rest[: max(0, tune_n - len(covered))]
    picks = sorted(set(hold_pick) | set(tune_pick))
    out = os.path.join(root, "config", "universe_history.csv")
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ticker", "market", "provider", "provider_symbol", "why"])
        w.writerow(["SPY", "US", "tiingo", "SPY", "benchmark for the history tests"])
        for t in picks:
            why = ("hold-out" if t in hold_pick else "") + ("+" if t in hold_pick and t in tune else "") + ("tuning" if t in tune else "")
            w.writerow([t, "US", "tiingo", t, f"insider clusters sample ({why})"])
    print(f"pool: {len(hold)} hold-out tickers, {len(tune)} tuning tickers; picked {len(picks)} "
          f"({len(hold_pick)} hold-out, {len(covered) + len(tune_pick)} tuning, {len(covered)} in both)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else ".", *(int(x) for x in sys.argv[2:4])))
