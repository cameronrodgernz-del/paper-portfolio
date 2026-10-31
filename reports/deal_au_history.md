# Deal spreads history test: ASX cash deals

Rulebook section 9c. Run 2026-10-31 23:43 UTC. 133 events in the database, 117 of 121 tickers with prices, 88 events used.

Coverage: 64% of the deals that paid and 80% of the deals that broke have prices and pass the entry check (the test needs 70% of each, so that missing delisted shares can't tilt it).

Not enough coverage to run. **Result: not run.**

Events left out, by reason: entry price outside 85% to 101% of the offer (a different share on the code, or not a cash deal) 21; no payment date 6; no prices around the announcement 2; no prices from EODHD 16.

Caveats: dividends paid during the hold are left out; a deal paid is credited at the final price on the implementation date with no sale costs; overlapping events move together, so the t-statistic overstates the evidence somewhat.
