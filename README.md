# Paper portfolio

A simulated NZ$100,000 portfolio traded at real prices with Sharesies NZ costs. The practice run is 2 November to 31 December 2026; the counted run is 4 January to 2 July 2027. The build plan is the "Building the simulated trading portfolio" doc; the rules are in RULEBOOK.md; the nightly cycle is in docs/DAILY_RUN.md.

## Layout
- `RULEBOOK.md`: the rules. Draft until 31 December 2026.
- `config/`: the price universes, the live deal terms (`live_deals.csv`), and the run settings (`run.json`: which ledger is active, the bankroll, the core's lines and band).
- `deals/`: the deal database (SCHEMA.md; NZ and Australian files; `all_deals.csv` is the merged copy).
- `data/`: downloaded series (prices, currencies, interest rates, SEC filings). Written by the nightly job.
- `ledger/`: the practice and counted ledgers (append-only, hash-chained). Written by the nightly job and the evening desk.
- `reports/`: deal base rates, the live deal monitor, the rules-only history test, and each ledger's daily reports and `latest.json`.
- `src/`
  - `costs.py`: Sharesies fees, the $15 plan and currency conversion.
  - `fills.py`: fill rules (next open, spread, size cost, volume cap, limit orders).
  - `spreads.py`: spread estimates from daily highs and lows.
  - `ledger.py`: append-only, hash-chained ledger.
  - `market_data.py`: prices, currencies, session times (an order fills only in a session that opens after it).
  - `rates.py`: three-month rates for NZD, AUD and USD, and forward rates from them.
  - `clerk.py`: the booking clerk (fills, fees, interest, corporate actions, hedges, valuation, limit flags).
  - `risk.py`: quarter-Kelly sizing and every pre-trade limit.
  - `decide.py`: places an analyst's decision card, after sizing, costs and limits; logs the dated call.
  - `daily.py`: the nightly mechanical run (deposit, catch-up, core by rule, reports).
  - `deal_monitor.py`: spreads, yearly rates after costs, and market-implied against base-rate odds for live deals.
  - `fetch_public.py`, `fetch_prices.py`, `fetch_sec.py`, `us_deals.py`: the free data feeds.
  - `history/`: the rules-only history test and the deal base rates.
- `tests/`: engine, clerk, hedging, risk and decision checks. All run in the nightly job.

## Running the checks
`for t in tests/test_*.py; do python3 -I $t; done`

## Starting a run
Set `"active"` in `config/run.json` to `"practice"` (or `"counted"`). The nightly job then deposits the bankroll on the start date, runs the clerk each weekday and buys the core by rule.
