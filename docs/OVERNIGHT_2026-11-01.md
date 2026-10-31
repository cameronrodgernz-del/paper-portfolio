# Overnight build, 31 October to 1 November 2026

What was built while Cam slept, in the order it matters. Everything is in the repository, and
every check runs in the nightly job.

## Engine
- **Deal monitor** (src/deal_monitor.py, config/live_deals.csv): the 11 pending ASX deals, with the
  offer value (acquirer shares at their last close for scrip deals), gross spread, yearly rate
  before and after costs, the chance the price implies, and the base rate for the structure.
  Runs nightly. US leads from SEC merger filings are listed under it.
- **Hedging**: deal positions in AUD and USD carry rolling three-month forwards priced from
  published rates (RBA, FRED), with a 0.1% dealing cost. Values are reported hedged and unhedged.
- **Sizing and limits** (src/risk.py, src/decide.py): quarter Kelly from the card's odds, then
  every rulebook limit, counting orders already waiting. Costs come off the expected return
  before the cash-rate test. A thin spread that only beats cash before costs is refused.
- **Nightly runner** (src/daily.py): deposit, catch-up runs, the core bought by rule, the
  fall-from-peak sales by rule, the passive comparisons for success tests 2 and 3, and the
  monthly report.
- **Corporate actions** (src/actions.py): checked entry of dividends, scheme payments and splits,
  and a nightly list of ones the feeds suggest are missing.
- **Timing**: prices land at 8:30pm NZ and the run is at 9pm NZ in both daylight-saving seasons.
  Before, a fixed UTC time drifted an hour and would have missed the ASX close in winter.

## Two independent reviews of the engine
A reviewer who had not built the code found 20 problems. None was lookahead. The worst were
these:
- a split would have stopped every later run;
- dividends went to whoever held on the pay date;
- buying foreign shares could overdraw NZ$ cash for free;
- placing the same card twice doubled a position past the 4% cap.

All 20 were fixed. A second reviewer then checked the fixes and found 13 smaller problems, which
were fixed too. Both reports, with what changed, are in docs/reviews/engine_review_2026-11-01.md.

## Data
- **Deal database**: Australian 2015 to 2016 added, then a follow-up pass filled 535 fields and
  added 33 missing deals. It now holds 347 rows. Of the 320 resolved deals, 81% completed, with a
  median of 119 days. Schemes completed 85% of the time and takeover bids 70%. Open items are in
  deals/au_hist/followup/OPEN_ITEMS.md.
- **Live prices**: an extra data run fetched the pending deal targets, the acquirers, ENZL and
  40 US deal targets.
- **SEC data**: 390,049 open-market purchases by directors and officers, 2010 to 2026, and 2,002
  first merger proxies and tender responses, 2015 to 2025, with the ticker each company used at
  the time.

## History tests, registered before any result (rulebook 9a and 9b)
- **US director and officer buying clusters** (for the special situations sleeve): a sample of 336
  tickers is being priced hourly within Tiingo's free limits. The test runs once, when all are in.
- **US cash deal spreads** (for the deal sleeve): a sample of 360 tickers, priced on 1 to 4
  December on that month's free allowance.
- Only one of the six special situation types can be tested on free data. The others are watched
  but not traded. If the insider test fails, the sleeve's 15% goes to cash.

## What the deal monitor shows (a prompt for analysis, not advice)
- After costs and assuming on-time completion, BET, MEI, RWC, SDF and OML show double-digit yearly
  rates.
- For BET and MEI the price implies about 62% to 67% odds against an 85% base rate.
- Peet (PPC) trades below its pre-deal price although no termination has been announced.
- Ausgold's (AUC) offer value is mostly in TSX-listed OceanaGold shares, which the feed doesn't
  carry.
- Most of these deals will have finished before the practice run starts on 7 December.

## For Cam, when convenient (none is urgent)
1. Check VT, VAS and ENZL are offered in the Sharesies app.
2. The Google Drive copy needs a five-minute rclone setup (docs/DRIVE_BACKUP.md).
3. The evening desk is written as a scheduled task (docs/DESK_TASK.md). It can be switched on at
   any time, and must be before 7 December.

## Next
- Monday 2 November, 8:30pm NZ: the first scheduled nightly run. It is the first of the five clean
  runs the readiness review needs.
- The insider test result, once its prices are in.
- The NZX price feed choice (week 3).
- The readiness review on 4 December (docs/READINESS.md).
