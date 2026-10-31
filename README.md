# Paper portfolio

A simulated NZ$100,000 portfolio traded at real prices with Sharesies NZ costs. The counted run is 1 February to 30 July 2027. The build plan is the "Building the simulated trading portfolio" doc; the rules are in RULEBOOK.md.

## Layout
- `RULEBOOK.md`: the rules. Draft until 29 January 2027.
- `deals/`: the deal database (SCHEMA.md, NZ and Australian files).
- `src/costs.py`: Sharesies fees, the $15 plan and currency conversion.
- `src/fills.py`: fill rules (next open, spread, size cost, volume cap, limit orders).
- `src/spreads.py`: spread estimates from daily highs and lows.
- `src/ledger.py`: append-only, hash-chained ledger.
- `src/fetch_public.py`: free currency and interest rate series (RBA, FRED).
- `tests/test_engine.py`: checks for all of the above.
- `data/`: downloaded series.

## Running the checks
`python3 -I tests/test_engine.py`
