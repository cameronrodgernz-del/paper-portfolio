# Independent review of the deal, data and hub changes, 1 November 2026

A separate agent, which had not seen the work being written, reviewed the day's changes at commit
453c589: the deal odds, the deal monitor, data checks, the price fetch, the ASX deal test (9c), the
hub export, the ingest function and the Portfolio page. Its findings and what was done about each:

| # | Finding | Done |
| --- | --- | --- |
| 1 | EODHD's account record keeps the last active day's request count until a request is made after midnight UTC, so a night that used all 20 free requests could leave every later night thinking none were left | The count is treated as nothing used when it is dated before today (UTC). The history job asks for the plan's limit at most once a UTC day (data/history/eodhd_plan.txt). The core fund and the live deals' shares are fetched first |
| 2 | Booklet-stage odds came out below announcement odds: undated failures were counted at the booklet stage but undated rival wins were dropped, and regulator blocks that came before any booklet were counted against it | Undated rival wins follow the same days rule as undated failures; a regulator block with no booklet recorded counts as failing before it. Schemes: 91.8% at the booklet against 90.3% at announcement (was 89.9%) |
| 3 | The implied-chance chart recomputed past days with today's terms (lookahead in the chart only; decisions use the figure recorded at the time) | reports/deal_history.json now keeps each night's figure as worked out then and only adds new days; the record starts 1 Nov 2026 |
| 4 | The break price was moved with the market from the announcement where the undisturbed price is older, and used the index's total return against a share's raw price | Every live deal has its undisturbed date (desk log); the data checks flag a missing one; the index's price level is used, read for every day rather than every fifth |
| 5 | A 9c fail wasn't enforced | decide.py refuses an ASX cash-only deal buy once reports/deal_au_history.md records a fail |
| 6 | One bad row (a blank payment date, a word in a number) stopped the whole deal monitor | Each deal is valued on its own; a bad row is reported and the rest carry on |
| 7 | A badly written date in a deal file could blank the hub's Deals view | The export drops date fields that aren't dates; the page's date helpers return blank on bad input; a view that fails to draw shows a message instead of an empty tab |
| 8 | The all-deals-break line left out a deal with no break price; dividends owed or on shares since sold sat in the "other" line | The stress line falls back to the card's worst outcome, as decide.py does; dividends have their own line |
| 9 | Some failed tests wrote "Result: fail." without the bold the hub reads, so they would show as waiting | All result lines are written the same way |
| 10 | The ingest function trusted the repository's name and any workflow on main | Pinned to the repository and owner ids, the three workflows that post, schedule, push or manual runs, RS256, and a token at most 15 minutes old (deployed as version 2). Chart ids are escaped on the page |
| 11 | Checked and fine: cross-validation (a slight flattering from choosing the penalty on the same folds), the monitor's use of the model, 9c's costs and coverage, Tiingo's November count, the nightly job's step isolation | Rebuilding the odds without scikit-learn now keeps the last tested model and says so, instead of switching it off. The weights at later stages (0.75 and 0.25) are untested and stay as written. If the EODHD paid plan starts after 4 Dec, 9c's prices need a manual run of History prices |
