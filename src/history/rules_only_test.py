"""History test for the rules-only sleeve on published, survivorship-free data.

Source: Kenneth French data library (CRSP-based, includes delisted companies).
- 6 portfolios on size and prior 12-2 month return: BIG HiPRIOR = large US companies
  in the top 30% of momentum, value-weighted, rebalanced monthly.
- 6 portfolios on size and operating profitability: BIG HiOP = large US companies in the
  top 30% of profitability, rebalanced each June.
- Market = Mkt-RF + RF from the three-factor file.
These are wide portfolios (hundreds of shares), so they measure the premium itself.
Our sleeve would hold 10 shares or two factor funds, so costs are layered on top.

Tune period 2010-01 to 2019-12; hold-out 2020-01 to the latest month.
Usage: python3 -I src/history/rules_only_test.py <cache_dir> <report.md>
"""
import csv
import io
import math
import os
import sys
import urllib.request
import zipfile

BASE = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/"
FILES = {"mom": "6_Portfolios_ME_Prior_12_2_CSV.zip", "op": "6_Portfolios_ME_OP_2x3_CSV.zip",
         "ff": "F-F_Research_Data_Factors_CSV.zip"}


def fetch(cache: str, name: str) -> str:
    os.makedirs(cache, exist_ok=True)
    path = os.path.join(cache, name)
    if not os.path.exists(path):
        with urllib.request.urlopen(BASE + name, timeout=60) as r:
            open(path, "wb").write(r.read())
    with zipfile.ZipFile(path) as z:
        return z.read(z.namelist()[0]).decode("latin-1")


def first_monthly_block(text: str) -> tuple[list[str], dict[str, list[float]]]:
    """The first table of monthly rows (YYYYMM) after its header line."""
    rows = list(csv.reader(io.StringIO(text)))
    out, header, started = {}, None, False
    for r in rows:
        if r and r[0].strip() == "" and len(r) > 1 and not started:
            header = [c.strip() for c in r[1:]]
            continue
        if header and r and r[0].strip().isdigit() and len(r[0].strip()) == 6:
            started = True
            out[r[0].strip()] = [float(x) for x in r[1:len(header) + 1]]
        elif started:
            break
    return header, out


def series(text: str, col: str) -> dict[str, float]:
    header, data = first_monthly_block(text)
    i = header.index(col)
    return {k: v[i] / 100 for k, v in data.items() if v[i] > -99}


def stats(rets: list[float]) -> dict:
    n = len(rets)
    growth = math.prod(1 + r for r in rets)
    ann = growth ** (12 / n) - 1
    vol = (sum((r - sum(rets) / n) ** 2 for r in rets) / (n - 1)) ** 0.5 * math.sqrt(12)
    peak, level, worst = 1.0, 1.0, 0.0
    for r in rets:
        level *= 1 + r
        peak = max(peak, level)
        worst = min(worst, level / peak - 1)
    return {"ann": ann, "vol": vol, "worst_fall": worst}


def yearly(months: list[str], rets: list[float]) -> dict[str, float]:
    out = {}
    for m, r in zip(months, rets):
        out[m[:4]] = (1 + out.get(m[:4], 0.0)) * (1 + r) - 1
    return out


def main(cache: str, report: str) -> int:
    mom_t, op_t, ff_t = (fetch(cache, FILES[k]) for k in ("mom", "op", "ff"))
    mom = series(mom_t, "BIG HiPRIOR")
    op = series(op_t, "BIG HiOP")
    mkt_rf, rf = series(ff_t, "Mkt-RF"), series(ff_t, "RF")
    months = sorted(set(mom) & set(op) & set(mkt_rf))
    mkt = {m: mkt_rf[m] + rf[m] for m in months}
    blend = {m: 0.5 * mom[m] + 0.5 * op[m] for m in months}
    periods = {"Tune: Jan 2010 to Dec 2019": ("201001", "201912"),
               "Hold-out: Jan 2020 to " + months[-1][:4] + "-" + months[-1][4:]: ("202001", months[-1])}
    # Costs at Sharesies for a NZ$10,000 sleeve (about US$5,640 at 0.564).
    sleeve_usd = 5640.0
    cost_cases = {
        "10 shares, quarterly, half the names change each time (40 orders a year)": 40 * 5 / sleeve_usd,
        "10 shares, quarterly, a third change (about 27 orders a year)": 27 * 5 / sleeve_usd,
        "Two factor funds, rebalanced once a year (4 orders a year)": 4 * 5 / sleeve_usd + 0.0015,
    }
    lines = ["# Rules-only sleeve: history test on published data", "",
             f"Data: Kenneth French data library, CRSP to {months[-1][:4]}-{months[-1][4:]}, which includes delisted companies. "
             "BIG HiPRIOR is large US companies in the top 30% of 12-month momentum; BIG HiOP is large US companies in the top 30% "
             "of operating profitability; the blend is half of each. Returns are before costs.", ""]
    for label, (a, b) in periods.items():
        ms = [m for m in months if a <= m <= b]
        rows = {"US market": [mkt[m] for m in ms], "Momentum (big, top 30%)": [mom[m] for m in ms],
                "Profitability (big, top 30%)": [op[m] for m in ms], "Blend 50/50": [blend[m] for m in ms]}
        s = {k: stats(v) for k, v in rows.items()}
        lines += [f"## {label}", "", "| Portfolio | Return a year | Ahead of market a year | Volatility | Worst fall |", "| --- | --- | --- | --- | --- |"]
        for k, v in s.items():
            gap = v["ann"] - s["US market"]["ann"]
            lines.append(f"| {k} | {v['ann']:.1%} | {'' if k == 'US market' else f'{gap:+.1%}'} | {v['vol']:.1%} | {v['worst_fall']:.1%} |")
        ym, yb = yearly(ms, rows["US market"]), yearly(ms, rows["Blend 50/50"])
        gaps = {y: yb[y] - ym[y] for y in ym}
        total_gap = sum(gaps.values())
        best_year = max(gaps, key=gaps.get)
        share = gaps[best_year] / total_gap if total_gap > 0 else float("nan")
        lines += ["", f"Blend ahead of the market in {sum(1 for g in gaps.values() if g > 0)} of {len(gaps)} years. "
                  f"Best year {best_year} ({gaps[best_year]:+.1%}) is {share:.0%} of the summed yearly gaps.", ""]
        blend_gap = s["Blend 50/50"]["ann"] - s["US market"]["ann"]
        lines += ["| How the sleeve is held | Cost a year | Blend ahead of market after cost |", "| --- | --- | --- |"]
        for c, cost in cost_cases.items():
            lines.append(f"| {c} | {cost:.1%} | {blend_gap - cost:+.1%} |")
        ratio = s["Blend 50/50"]["worst_fall"] / s["US market"]["worst_fall"] if s["US market"]["worst_fall"] else float("nan")
        lines += ["", f"Worst fall of the blend is {ratio:.2f} times the market's.", ""]
    lines += ["## Reading", "",
              "The pass mark in the rulebook: ahead of US shares after Sharesies' costs in the hold-out years, no single year "
              "giving more than half the gain, and a worst fall no more than 1.5 times the market's. The ten-share version adds "
              "the noise of holding only ten names, which these wide portfolios don't show, so a thin margin after costs is a fail.", ""]
    os.makedirs(os.path.dirname(report), exist_ok=True)
    open(report, "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
