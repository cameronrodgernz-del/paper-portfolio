# Special situations history test: US director and officer buying clusters

Rulebook section 9a. Run 2026-10-31 21:51 UTC. Sample: 336 tickers drawn at random (seed 20261101), 329 with Tiingo prices.

Each event is bought at the open after the filing that completes the cluster and sold at the open H sessions later. Result = return less SPY over the same sessions, after US$5 brokerage each way on a US$1,700 stake, 0.5% currency conversion and the estimated spread.

## Tuning, 2010 to 2019 (all 12 versions tried)

| Buyers | Hold (sessions) | Min traded value | Events | Mean after costs | Median | t | Hit rate | Mean costs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 63 | US$1m | 364 | -0.22% | -0.74% | -0.23 | 48% | 1.94% |
| 2 | 63 | US$5m | 228 | -1.43% | -0.80% | -1.22 | 47% | 1.81% |
| 2 | 126 | US$1m | 364 | -1.51% | -1.84% | -1.12 | 47% | 1.94% |
| 2 | 126 | US$5m | 228 | -3.50% | -1.97% | -2.29 | 46% | 1.81% |
| 3 | 63 | US$1m | 191 | -0.84% | -1.32% | -0.64 | 47% | 2.03% |
| 3 | 63 | US$5m | 106 | -2.76% | -1.32% | -1.82 | 46% | 1.87% |
| 3 | 126 | US$1m | 191 | -1.35% | -0.76% | -0.69 | 48% | 2.03% |
| 3 | 126 | US$5m | 106 | -4.70% | -1.25% | -2.20 | 46% | 1.87% |
| 4 | 63 | US$1m | 118 | -0.33% | +0.00% | -0.20 | 50% | 2.07% |
| 4 | 63 | US$5m | 63 | -2.73% | -0.27% | -1.19 | 48% | 1.91% |
| 4 | 126 | US$1m | 118 | -1.98% | -1.35% | -0.87 | 47% | 2.07% |
| 4 | 126 | US$5m | 63 | -5.81% | -1.97% | -2.19 | 43% | 1.91% |

Picked: 2 or more buyers, held 63 sessions, traded value at least US$1m (tuning mean -0.22% on 364 events).

## Hold-out, 2020 onwards (run once)

| Measure | Value |
| --- | --- |
| Events | 420 |
| Mean return | +5.25% |
| Mean SPY return | +5.71% |
| Mean costs | 2.16% |
| Mean after costs, less SPY | -2.62% |
| Median | -4.68% |
| t-statistic | -2.47 |
| Hit rate | 39% |

| Year | Sum of results |
| --- | --- |
| 2020 | -367.3% |
| 2021 | -6.8% |
| 2022 | +111.7% |
| 2023 | -445.2% |
| 2024 | -177.2% |
| 2025 | -127.6% |
| 2026 | -86.2% |

| Pass mark | Met | Value |
| --- | --- | --- |
| At least 30 events | yes | 420 |
| Mean after costs above zero with t of 2 or more | no | -2.62%, t -2.47 |
| Still above zero without the best 5% of events | no | -5.63% |
| No single year more than half the total gain | no | no total gain |

**Result: fail.**

Events left out of the hold-out, by reason: exit not reached yet 2; no prices around the event 6; no prices from Tiingo 8; not NYSE or Nasdaq 87; price check failed (ticker may have been reused) 71; too little trading 120; under US$3 at entry 28.

Caveats: events that overlap in time move together, so the t-statistic overstates the evidence somewhat. Tiingo may lack some delisted shares. A pass is a screen, not proof.
