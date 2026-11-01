# Deal spreads history test: ASX cash deals

Rulebook section 9c. Run 2026-11-01 00:04 UTC. 133 events in the database, 118 of 121 tickers with prices (3 from EODHD, 115 from Norgate), 108 events used.

Coverage: 82% of the deals that paid and 73% of the deals that broke have prices and pass the entry check (the test needs 70% of each, so that missing delisted shares can't tilt it).

| Measure | Value |
| --- | --- |
| Events | 108 (paid 97, broke 11) |
| Mean gross return | +1.89% |
| Mean costs | 1.72% |
| Mean cash over the same days | 0.79% |
| Mean result after costs, less cash | -0.61% (median +0.01%) |
| t-statistic | -0.49 |
| Median days held | 118 |
| Mean market-implied chance at entry / actual paid rate | 74% / 90% |

| Year | Events | Mean result |
| --- | --- | --- |
| 2015 | 7 | -0.17% |
| 2016 | 9 | +0.32% |
| 2017 | 7 | +1.20% |
| 2018 | 10 | +1.46% |
| 2019 | 10 | -8.96% |
| 2020 | 7 | -4.58% |
| 2021 | 15 | +3.43% |
| 2022 | 5 | +0.96% |
| 2023 | 11 | -1.12% |
| 2024 | 10 | +0.93% |
| 2025 | 17 | -1.31% |

| Pass mark | Met | Value |
| --- | --- | --- |
| At least 60 events | yes | 108 |
| Mean after costs and cash above zero with t of 2 or more | no | -0.61%, t -0.49 |
| No single year more than half the total gain | no | no total gain |
| Worst year no worse than -4% per event | no | 2019: -8.96% |

**Result: fail.**

## Reported only: entering when the scheme booklet is out

Not a pass mark. The same rules, entering at the first open after the booklet date.

| Measure | Value |
| --- | --- |
| Events | 53 (paid 51, broke 2) |
| Mean gross return | +2.12% |
| Mean costs | 1.64% |
| Mean cash over the same days | 0.43% |
| Mean result after costs, less cash | +0.05% (median -0.53%) |
| t-statistic | 0.14 |
| Median days held | 57 |
| Mean market-implied chance at entry / actual paid rate | 78% / 96% |

| Year | Events | Mean result |
| --- | --- | --- |
| 2015 | 6 | -0.28% |
| 2016 | 5 | +0.16% |
| 2017 | 3 | +3.19% |
| 2018 | 1 | -1.03% |
| 2019 | 7 | -1.80% |
| 2020 | 2 | +8.02% |
| 2021 | 3 | -0.17% |
| 2022 | 4 | -0.58% |
| 2023 | 5 | -0.84% |
| 2024 | 4 | -0.43% |
| 2025 | 11 | -0.11% |
| 2026 | 2 | +0.72% |

| Pass mark | Met | Value |
| --- | --- | --- |
| At least 60 events | no | 53 |
| Mean after costs and cash above zero with t of 2 or more | no | +0.05%, t 0.14 |
| No single year more than half the total gain | no | 2020: 620% |
| Worst year no worse than -4% per event | yes | 2019: -1.80% |

Events left out, by reason: entry price outside 85% to 101% of the offer (a different share on the code, or not a cash deal) 22; no prices from EODHD 3.

Caveats: dividends paid during the hold are left out; a deal paid is credited at the final price on the implementation date with no sale costs; overlapping events move together, so the t-statistic overstates the evidence somewhat.
