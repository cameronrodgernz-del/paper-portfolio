# The nightly cycle

Two parts, run one after the other each weekday, New Zealand time.

## 1. The nightly job (GitHub, 8:17pm NZ)
Runs without anyone. Defined in `.github/workflows/nightly-data.yml`.

1. Free series: RBA currencies and rates, FRED rates.
2. SEC daily filing index, and the US deal targets list built from merger filings.
3. End-of-day prices: Tiingo (US) and EODHD (ASX), stalest first within the free limits. A session is stored only once its prices are final.
4. Every test in `tests/`. A failure stops the job before anything is saved.
5. Deal monitor: `reports/deal_monitor.md`.
6. Clerk, for the ledger named active in `config/run.json`: splits, fills, fees, interest, dividends and consideration, hedges, valuation, limit flags; then the rules that need no judgement (the fall-from-peak sales and the core). Flags any corporate action the price feed shows that has not been entered, and any analyst decision written more than 10 minutes after its time. Writes `reports/<ledger>/daily/<date>.md`, `latest.json`, the passive comparisons and, when a month ends, the monthly report.
7. Commit and push.

Two schedules (07:17 and 08:17 UTC) with a gate keep the job at 8:17pm NZ in both daylight-saving seasons (moved off the half hour on 8 Nov 2026, after GitHub started the 5 and 6 Nov runs about eight hours late). A push that changes `config/run_now.txt` starts an extra run.

## 2. The evening desk (a scheduled Claude task, weekdays 9:45pm NZ)
Follows rulebook section 8. Each step leaves a file, so a missed or partial night is visible.

1. **Check.** Pull the repository. Verify the ledger chain. Confirm tonight's valuation exists. If the nightly job is late, wait up to 30 minutes. If it is still missing, place no orders tonight (the job and the desk both write to the ledger, so they must not overlap), do the scan and write-ups only, and say so in the desk log.
2. **Corporate actions.** Run `python3 -I src/actions.py <ledger> check`. Enter each dividend, scheme or offer payment and split it lists (and any announced for a holding) with `src/actions.py`, from the company's announcement, with its source.
3. **Scan.**
   - ASX: announcement lists for each holding, each live deal and the watchlist (dated titles, then the documents that matter).
   - NZX: the same for NZX names.
   - SEC: `data/sec/deal_filings.csv` for new merger proxies, tender offers and responses.
   - Flag: new deals, changed terms, meeting results, court dates, regulator news, rival bids, holder build-ups, strategic reviews.
4. **Analyse.** Take the deals in the order of the monitor's return at the base rate (`expected_yearly` in `reports/deal_monitor.csv`: the value if the base rate is right, against the price, after costs, a year), and read the late case beside it. Keep a deal file for every live deal (`research/deals/<TICKER>.md`, `NZ_<TICKER>.md` for NZX, format in `research/deals/TEMPLATE.md`) from primary sources: the announcements, the scheme booklet or target's statement, the independent expert's report, the implementation deed and the regulators' registers. Update its header (stage, dates, conditions) whenever something changes, then run `python3 -I src/deal_files.py . --add` to carry it into `config/live_deals.csv`. For each flagged event, a note in `research/events/<date>-<ticker>.md`. For each candidate entry or exit, a decision card (`research/cards/<date>-<ticker>.json`, format in `src/decide.py`). Start a deal card with `python3 -I src/card_draft.py . <TICKER>`, which fills in the offer, the market-adjusted break price, the stage base rate, the payment date and the group, and lists the open conditions; the analyst writes the rest:
   - the outcomes, their chances and prices;
   - the base rate it starts from and each adjustment, written down;
   - the resolve-by date and the exit rule;
   - why the market's spread is wrong.
5. **Red team.** A separate agent that has not seen the analyst's reasoning argues against each card, working through docs/RED_TEAM.md with the card, the deal file and the monitor's row. Its points go in the card's file. The analyst may revise the card once.
6. **Risk manager.** `python3 -I src/decide.py <ledger> <card> --dry-run` gives the stake, the costs and every limit breach. A card with a breach is not placed. A veto by judgement is logged with its reason.
7. **Place.** `python3 -I src/decide.py <ledger> <card>` logs the decision, the dated call and the order, timed when it runs. Commit and push.
8. **Cam's Hub** updates itself: the Hub sync workflow sends a new snapshot to the Portfolio tab after each push. (The older build dashboard artifact is no longer refreshed.)
9. **Tell Cam** only when a trade is placed, a holding has material news, or a limit trips.

Nothing is backdated: a decision is timed when `decide.py` runs, and the clerk fills it only in a session that opens afterwards. A missed desk means no decisions that night.

## Quarterly
At the first desk run of each quarter: refresh config/nzx_top20.csv from interest.co.nz's NZX 50 table (the 20 largest NZX-listed companies by market value, leaving out ASX-listed lines such as ANZ and WBC), with the date.

## Monthly
At the first run of each month: the report (`reports/<ledger>/monthly/<month>.md`) covering return against the passive mixes, the worst fall, costs paid, hit rate on calls, and every rule exception. Cash rate set for the month in `config/run.json` (otherwise the NZ three-month rate less one point).

## Switching ledgers
- Practice: `"active": "practice"` in `config/run.json` from 1 November 2026; the nightly job deposits the bankroll and starts the practice ledger on 2 November.
- Counted: on 31 December 2026, once Cam has signed off the rulebook, set `"active": "counted"`; the counted ledger starts on 4 January 2027.
