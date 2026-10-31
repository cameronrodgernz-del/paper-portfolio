# The nightly cycle

Two parts, run one after the other each weekday, New Zealand time.

## 1. The nightly job (GitHub, 8:30pm NZ)
Runs without anyone. Defined in `.github/workflows/nightly-data.yml`.

1. Free series: RBA currencies and rates, FRED rates.
2. SEC daily filing index, and the US deal targets list built from merger filings.
3. End-of-day prices: Tiingo (US) and EODHD (ASX), stalest first within the free limits. A session is stored only once its prices are final.
4. Every test in `tests/`. A failure stops the job before anything is saved.
5. Deal monitor: `reports/deal_monitor.md`.
6. Clerk, for the ledger named active in `config/run.json`: fills, fees, interest, corporate actions, hedges, valuation, limit flags, core by rule. Writes `reports/<ledger>/daily/<date>.md` and `latest.json`.
7. Commit and push.

Two schedules (07:30 and 08:30 UTC) with a gate keep the job at 8:30pm NZ in both daylight-saving seasons. A push that changes `config/run_now.txt` starts an extra run.

## 2. The evening desk (a scheduled Claude task, 9:30pm NZ, from 7 December)
Follows rulebook section 8. Each step leaves a file, so a missed or partial night is visible.

1. **Check.** Pull the repository. Verify the ledger chain. Confirm tonight's valuation exists; if the nightly job is late, wait up to 30 minutes, then carry on with yesterday's prices and say so in the desk log.
2. **Scan.**
   - ASX: announcement lists for each holding, each live deal and the watchlist (dated titles, then the documents that matter).
   - NZX: the same for NZX names.
   - SEC: `data/sec/deal_filings.csv` for new merger proxies, tender offers and responses.
   - Flag: new deals, changed terms, meeting results, court dates, regulator news, rival bids, holder build-ups, strategic reviews.
3. **Analyse.** For each flagged event, a note in `research/events/<date>-<ticker>.md`. For each candidate entry or exit, a decision card (`research/cards/<date>-<ticker>.json`, format in `src/decide.py`):
   - the outcomes, their chances and prices;
   - the base rate it starts from and each adjustment, written down;
   - the resolve-by date and the exit rule;
   - why the market's spread is wrong.
4. **Red team.** A separate agent that has not seen the analyst's reasoning argues against each card. Its points go in the card's file. The analyst may revise the card once.
5. **Risk manager.** `python3 -I src/decide.py <ledger> <card> --dry-run` gives the stake, the costs and every limit breach. A card with a breach is not placed. A veto by judgement is logged with its reason.
6. **Place.** `python3 -I src/decide.py <ledger> <card>` logs the decision, the dated call and the order, timed when it runs. Commit and push.
7. **Tell Cam** only when a trade is placed, a holding has material news, or a limit trips.

Nothing is backdated: a decision is timed when `decide.py` runs, and the clerk fills it only in a session that opens afterwards. A missed desk means no decisions that night.

## Monthly
At the first run of each month: the report (`reports/<ledger>/monthly/<month>.md`) covering return against the passive mixes, the worst fall, costs paid, hit rate on calls, and every rule exception. Cash rate set for the month in `config/run.json` (otherwise the NZ three-month rate less one point).

## Before 7 December
- Set `"active": "practice"` in `config/run.json` (the nightly job then starts the practice ledger on 7 December).
- Create the evening desk scheduled task.
- Confirm VT, VAS and ENZL are offered on Sharesies.
