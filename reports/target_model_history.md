# History test 9e: a model of the next takeover target

Rulebook section 9e. Run 2026-11-01 01:47 UTC.

Fitted on 13,060 share-quarters from 2011 to 2017 (196 with a bid within 12 months); penalty C = 0.01 by cross-validation (Brier 0.0148).

| Feature | Weight (standardised) |
| --- | --- |
| ret 12m | -0.08 |
| rel 12m | -0.08 |
| ret 1m | +0.08 |
| below high | +0.08 |
| vol 3m | -0.06 |
| failed 2y | +0.04 |
| volume surge | +0.04 |
| ret 3m | -0.02 |
| log value | +0.01 |

| Measure | Value |
| --- | --- |
| Quarters | 30 (2019-03-29 to 2026-06-30) |
| Mean result a quarter, after costs, less the market | -3.09% (median -1.08%) |
| t-statistic | -2.01 |
| Quarters ahead of the market | 12 of 30 |
| Picks bid within 12 months | 14 of 135 (10.4%) |
| Universe bid within 12 months | 2.8% |
| Top 20 bid within 12 months (reported only) | 25 of 540 |
| Top 50 bid within 12 months (reported only) | 38 of 1350 |

| Score band (1 = highest) | Share-quarters | Bid within 12 months |
| --- | --- | --- |
| 1 | 1,723 | 3.1% |
| 2 | 1,708 | 2.3% |
| 3 | 1,715 | 3.0% |
| 4 | 1,711 | 2.8% |
| 5 | 1,710 | 2.7% |
| 6 | 1,711 | 3.0% |
| 7 | 1,717 | 3.0% |
| 8 | 1,709 | 3.5% |
| 9 | 1,714 | 2.6% |
| 10 | 1,699 | 1.6% |

| Year | Quarters | Sum of results |
| --- | --- | --- |
| 2019 | 4 | +7.56% |
| 2020 | 4 | -0.83% |
| 2021 | 4 | +2.41% |
| 2022 | 4 | -11.80% |
| 2023 | 4 | -21.38% |
| 2024 | 4 | +16.62% |
| 2025 | 4 | -61.33% |
| 2026 | 2 | -23.94% |

| Pass mark | Met | Value |
| --- | --- | --- |
| Mean quarterly result after costs above the market, t of 2 or more | no | -3.09% a quarter, t -2.01 |
| Picks bid within 12 months at least 3 times as often as the universe | yes | 10.4% against 2.8% |
| No single year more than half the total gain | no | no total gain |

**Result: fail.**

Caveats: the deal database holds binding deals of about A$100m or more, so smaller deals and approaches that never became binding count as misses; the 5 picks a quarter make a concentrated portfolio, so one bid moves a quarter a lot.
