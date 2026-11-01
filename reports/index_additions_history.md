# History test 9m: buying predicted index additions before S&P announces them

Rulebook section 9m. Run 2026-11-01 05:22 UTC.

Rebalances ranked: 63 (2011-03 to 2026-09).

## Tuning, 2011 to 2017 (all 8 versions)

| ASX 200 cut-off | ASX 300 cut-off | Exit | Trades | Mean result after costs | t (by rebalance) | Added by S&P |
| --- | --- | --- | --- | --- | --- | --- |
| 160 | 260 | after announcement | 922 | -0.57% | -2.08 | 20% |
| 160 | 260 | third Friday | 922 | +0.12% | -0.59 | 20% |
| 160 | 274 | after announcement | 1008 | -0.67% | -2.28 | 19% |
| 160 | 274 | third Friday | 1008 | -0.02% | -0.81 | 19% |
| 179 | 260 | after announcement | 1132 | -0.68% | -2.31 | 17% |
| 179 | 260 | third Friday | 1132 | -0.10% | -0.84 | 17% |
| 179 | 274 | after announcement | 1218 | -0.76% | -2.50 | 16% |
| 179 | 274 | third Friday | 1218 | -0.21% | -1.03 | 16% |

Picked: ASX 200 cut-off 160, ASX 300 cut-off 260, exit third Friday.

## Run once, 2018 to September 2026

| Measure | Value |
| --- | --- |
| Trades | 798 |
| Mean gross return | -0.15% |
| Mean costs | 2.08% |
| Mean benchmark (shares ranked 101 to 400) | -1.33% |
| Mean result after costs, less the benchmark | -0.90% (median -1.49%) |
| t-statistic (by rebalance) | -2.13 |
| Predictions S&P added at that rebalance (reported only) | 178 of 798 |
| Against VAS instead (reported only) | -1.13% |

| Year | Trades | Mean result |
| --- | --- | --- |
| 2018 | 95 | +0.14% |
| 2019 | 78 | +1.30% |
| 2020 | 81 | -1.60% |
| 2021 | 99 | -0.73% |
| 2022 | 107 | +0.61% |
| 2023 | 76 | -0.47% |
| 2024 | 89 | -0.95% |
| 2025 | 91 | -6.20% |
| 2026 | 82 | -0.09% |

| Pass mark | Met | Value |
| --- | --- | --- |
| At least 60 trades | yes | 798 |
| Mean after costs, against mid-sized shares, above zero with t of 2 or more (by rebalance) | no | -0.90%, t -2.13 over 35 rebalances |
| Still above zero without the best 5% of trades | no | -2.69% |
| No single year more than half the total gain | no | no total gain |

**Result: fail.**

- Reported only, predicted ASX 200 additions: 409 trades, mean -1.41%, added by S&P 52
- Reported only, predicted ASX 300 additions: 389 trades, mean -0.36%, added by S&P 126
- Reported only, predictions S&P added: mean +3.14%; predictions it didn't: mean -2.05%

Left out, by reason: no trade on the entry day 23; not tradable at entry 86.

Caveats: ranks use full market value from ASIC's share counts, not S&P's free-float figures, and no liquidity screen; shares not in ASIC's files can't be ranked; trades in the same rebalance move together, so the t-statistic is worked out by rebalance.
