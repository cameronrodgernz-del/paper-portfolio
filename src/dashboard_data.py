"""Export the files the build dashboard reads, from the repository as it stands.

reports/dashboard/
  deal_monitor.csv  live deals (copied from reports/deal_monitor.csv)
  base_rates.csv    deal base rates by group (from reports/deal_base_rates.csv)
  checks.csv        history tests and engine checks, with their status
  milestones.csv    the timeline (config/milestones.csv) with days to go
  database.csv      deal database rows by market and announcement year
Usage: python3 -I src/dashboard_data.py <repo_root>
"""
import csv
import glob
import os
import re
import shutil
import subprocess
import sys
from collections import Counter
from datetime import date


def first_line(path: str, pattern: str) -> str:
    if not os.path.exists(path):
        return ""
    m = re.search(pattern, open(path, encoding="utf-8").read())
    return m.group(1) if m else ""


def main(root: str) -> int:
    out = os.path.join(root, "reports", "dashboard")
    os.makedirs(out, exist_ok=True)
    today = date.today().isoformat()
    shutil.copy(os.path.join(root, "reports", "deal_monitor.csv"), os.path.join(out, "deal_monitor.csv"))
    shutil.copy(os.path.join(root, "reports", "deal_base_rates.csv"), os.path.join(out, "base_rates.csv"))

    checks = []
    for t in sorted(glob.glob(os.path.join(root, "tests", "test_*.py"))):
        r = subprocess.run([sys.executable, "-I", t], capture_output=True, text=True, cwd=root)
        n_pass = r.stdout.count("\nPASS ") + (1 if r.stdout.startswith("PASS ") else 0)
        n_fail = r.stdout.count("FAIL ")
        checks.append({"check": os.path.basename(t)[5:-3].replace("_", " "), "kind": "Engine checks",
                       "status": "pass" if r.returncode == 0 else "fail", "detail": f"{n_pass} checks pass, {n_fail} fail", "as_of": today})
    rules = os.path.join(root, "reports", "rules_only_history.md")
    checks.append({"check": "Rules-only screen (section 6)", "kind": "History tests", "status": "fail",
                   "detail": "About 1% a year ahead of the market before costs; behind after Sharesies' costs as 10 shares. Sleeve dropped, its 10% to cash",
                   "as_of": "2026-11-01" if os.path.exists(rules) else today})
    ins = os.path.join(root, "reports", "special_insider_history.md")
    waiting = first_line(ins, r"Waiting for prices: (\d+ of \d+)")
    result = first_line(ins, r"\*\*Result: (pass|fail)\.\*\*")
    checks.append({"check": "US director and officer buying clusters (9a)", "kind": "History tests",
                   "status": result or "waiting", "detail": (f"Prices fetched for {waiting} sampled tickers; runs once when all are in"
                                                             if waiting else "See reports/special_insider_history.md"), "as_of": today})
    dl = os.path.join(root, "reports", "deal_us_history.md")
    result = first_line(dl, r"\*\*Result: (pass|fail)\.\*\*")
    n_deals = sum(1 for _ in open(os.path.join(root, "config", "universe_history_deals.csv"))) - 1 \
        if os.path.exists(os.path.join(root, "config", "universe_history_deals.csv")) else 0
    checks.append({"check": "US cash deal spreads (9b)", "kind": "History tests", "status": result or "waiting",
                   "detail": f"{n_deals} tickers sampled; prices being fetched from 1 Nov within Tiingo's free limits" if not result else "See reports/deal_us_history.md",
                   "as_of": today})
    with open(os.path.join(out, "checks.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["check", "kind", "status", "detail", "as_of"])
        w.writeheader(); w.writerows(checks)

    ms = list(csv.DictReader(open(os.path.join(root, "config", "milestones.csv"), newline="")))
    for m in ms:
        m["days_to_go"] = (date.fromisoformat(m["date"]) - date.today()).days
    with open(os.path.join(out, "milestones.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["milestone", "date", "status", "days_to_go"])
        w.writeheader(); w.writerows(ms)

    rows = list(csv.DictReader(open(os.path.join(root, "deals", "all_deals.csv"), newline="")))
    c = Counter((r["market"], (r["announce_date"] or "")[:4]) for r in rows if r["announce_date"])
    with open(os.path.join(out, "database.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["year", "ASX", "NZX"])
        for y in sorted({k[1] for k in c}):
            w.writerow([y, c.get(("ASX", y), 0), c.get(("NZX", y), 0)])
    print("written:", sorted(os.listdir(out)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
