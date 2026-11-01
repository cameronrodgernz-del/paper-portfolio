# Deal spreads history test: US cash deals

Rulebook section 9b. Run 2026-11-01 13:06 UTC. Sample: 360 tickers (seed 20261102), 358 with prices; 240 events used.

| Measure | Value |
| --- | --- |
| Events | 240 (completed 203, broke 24, still open at 400 days 13) |
| Mean gross return | +0.93% |
| Mean costs | 1.03% |
| Mean cash over the same days | 0.60% |
| Mean result after costs, less cash | -0.70% (median -0.24%) |
| t-statistic | -1.62 |
| Median days held | 63 |
| Median yearly rate after costs (held 20 days or more) | +1.4% |
| Mean market-implied chance at entry | 91% |
| Actual completion rate (same events) | 85% |
| Brier score 2020 to 2025: market-implied / base rate from 2015 to 2019 | 0.137 / 0.145 (lower is better) |

| Year | Events | Mean result |
| --- | --- | --- |
| 2015 | 20 | -0.25% |
| 2016 | 22 | +0.55% |
| 2017 | 17 | +1.89% |
| 2018 | 15 | -1.01% |
| 2019 | 28 | -4.32% |
| 2020 | 15 | -0.96% |
| 2021 | 27 | -0.59% |
| 2022 | 21 | +0.02% |
| 2023 | 24 | -0.45% |
| 2024 | 29 | -0.28% |
| 2025 | 22 | -1.06% |

| Pass mark | Met | Value |
| --- | --- | --- |
| At least 60 events | yes | 240 |
| Mean after costs and cash above zero with t of 2 or more | no | -0.70%, t -1.62 |
| No single year more than half the total gain | no | no total gain |
| Worst year no worse than -4% per event | no | 2019: -4.32% |

**Result: fail.**

Events left out, by reason: entry price outside 85% to 101% of the cash price 69; no prices around the filing 44; no prices from Tiingo 39.

Caveats: a share that stops trading is taken as completed; a dividend paid during the hold is left out; events that overlap in time move together, so the t-statistic overstates the evidence somewhat.
