# Rulebook, version 0 (draft, 31 October 2026)

This is the working draft. It's tightened during the practice run and locked on 31 December 2026, once Cam signs it off. After that, a rule changes only to fix a defect, through a dated entry in the change log at the end, and every change is reported to Cam.

## 1. The run
- Bankroll: NZ$100,000, in NZ dollars.
- Practice run: 2 November 2026 to 31 December 2026. It runs live and nothing counts.
- Counted run: from the open on 4 January 2027 to the close on 2 July 2027. (The NZX is shut on 4 January for the New Year holiday and opens on the 5th.)
- Tax is ignored entirely, including withholding on foreign dividends.

## 2. Sleeves
| Sleeve | Target weight | Band | Holds |
|---|---|---|---|
| Market core | 40% | 35–45% | VT 20%, VAS 10%, ENZL 10% (to confirm on Sharesies before day one). ENZL, the US-listed iShares MSCI New Zealand fund, replaces FNZ because no free feed carries NZX prices |
| Deal spreads | 25% | 0–30% | Agreed schemes and takeover offers: NZX, ASX and US |
| Research picks | 10% | 0–10% | Overlooked NZX and ASX small and mid caps, each bought only after a deep dive from primary sources (section 5a). At most five companies. Added on 1 Nov 2026 |
| Special situations | 5% (was 15%) | 0–10% | Dated events: holder build-ups, strategic reviews, rejected bids, director buying clusters, index changes, offers priced at a discount. No type has passed a history test yet (9a and 9d to 9j failed on 1 Nov 2026), so this weight sits in cash until one does |
| Rules-only | 0% (was 10%) | n/a | Dropped on 1 Nov 2026: failed the history test (section 6, reports/rules_only_history.md). Its 10% goes to cash under section 9 |
| Cash | 20% (was 10%) | 5% floor | On-call cash, including the rules-only sleeve's 10% |

Only special situation types that pass a history test are traded (section 9). Four types have been tested and failed: US director and officer buying clusters (9a), shares left behind when a deal fails (9d), a model of the next takeover target (9e) and the June tax-year sell-off (9f). Holder build-ups, strategic reviews and discounted offers have no event data yet, and index changes have data but no registered test, so they are watched and written up but not traded.

Money an active sleeve can't use well stays in cash. The core and the rules-only sleeve are brought back inside their bands at the first open of each quarter.

## 3. Limits
- Per deal: 4% of the portfolio, and the loss if the deal breaks no more than 1% of the portfolio. The break price is the undisturbed price, or lower where the evidence says so.
- Deals waiting on one regulator, or from one bidder: 10% of the portfolio.
- Per special situation: 3%. Per research pick: 2.5%, and at most five companies at once (the sleeve's 10% binds first). Per rules-only share: 1%.
- One industry outside the core: 15%.
- Smallest order: NZ$2,500 on NZX, A$1,500 on ASX, US$500 in the US.
- Liquidity: no position larger than two sessions' trading at 10% of daily volume, measured on the 20-session median.
- Fall from peak: at 8% below the portfolio's peak, half of each deal and special situation holding is sold, by rule, the same evening. At 12%, the rest is sold, waiting active buys are cancelled, and no new deal or special situation is entered until a review is logged (`src/decide.py <ledger> review`). Each step happens once for each peak. While the fall is 8% or more, new entries keep each active sleeve to half its target weight. The core is never timed.
- Deal and special situation cards state an industry, and deal cards a group (the regulator the deal waits on, or the bidder), so the 15% and 10% limits can be counted. A card is placed only once that night's clerk run is in the ledger.
- A buy must be payable from NZ$ (less the next plan fee, kept back) or cash in its own currency; Australian and US dollars aren't swapped for each other.
- Every limit counts orders already placed and waiting to fill, as if they had filled. A second buy of the same share while one waits needs a card marked as a top-up. The 1% loss-on-break counts the whole position after the order; a deal card without a break price uses its worst outcome.
- No borrowing, shorting or options.
- Only shares Sharesies offers.

## 4. Sizing
Deal and special situation positions are sized at a quarter of the Kelly stake from the analyst's stated odds and payoffs, then cut to the limits in section 3. The analyst states, before entry:
- the chance of each outcome;
- the price in each outcome;
- the date by which it should resolve;
- the exit rule.

## 5. Deals
- Eligible only after a binding agreement or a formal offer. Rumours and non-binding approaches go in special situations.
- US deals are watched and written up but not traded until the US cash deal test (9b) passes. ASX and NZX deals trade on the deal database's base rates.
- Entry needs an expected return above the cash rate, after costs and annualised to the expected completion date, and a stated reason why the market's spread is wrong. The costs counted are the buy brokerage after the plan's cover, half the spread and the size cost, a currency conversion if foreign cash is short, the hedge's dealing cost, and the sale costs weighted by the chance of exiting by sale rather than by consideration.
- Odds start from the deal database (reports/deal_odds.md): how often holders were paid in past deals of the same structure that had reached the same stage (announced, booklet out, past the vote, court approved or unconditional), counting a rival bid that completed at the same or a higher price as paid. That rate is moved by a model of deal features (bidder type, approvals needed, board support, lock-ups, premium, size, market) only because it scored better than the structure rate in cross-validation, and with less weight the further along the deal is. The analyst then adjusts for evidence specific to the deal, each adjustment written down.
- The break price is the undisturbed price moved by the local market since the announcement (the index fund's total return: VAS for ASX, ENZL in NZ dollars for NZX, VT for US), unless the evidence points lower.
- Deal positions in AUD and USD are hedged back to NZ dollars in the simulation at the forward rate (the interest-rate gap, from published rates), and also reported unhedged. The hedge is a rolling three-month forward sale of the currency for the position's value at the close, opened in the run that books the fill, re-sized when it is more than 20% off the position, closed when the position goes, and charged 0.1% of its size as a dealing cost, since Sharesies offers no hedging.
- Exit when the deal completes, breaks, or a rival bid makes holding on a new decision. A rival bid is treated as a fresh entry decision.

## 5a. Research picks (added 1 Nov 2026)
- What: NZX and ASX small and mid caps that bigger investors are likely to overlook (outside the S&P/ASX 300 or the NZX 20, thinly traded, little or no analyst coverage, a concentrated or messy register, an out-of-favour sector), bought when a deep dive finds the price well below what the business is worth and a dated event should show it.
- It can't be tested on history: Claude knows how these companies' past turned out, so any back-dated deep dive would be fitted to the answer. It is judged going forward, in the practice and counted runs, like the deal sleeve's stated odds.
- Every pick needs, before any order (src/decide.py refuses a card without them):
  - a deep dive in research/picks/ in the format of research/picks/TEMPLATE.md, from primary sources only (annual and half-year reports, ASX or NZX announcements, the company and share registers, substantial holder notices, director dealings, regulator and court records), with at least two valuation methods, a plain statement of why the market is wrong, and every source linked;
  - at least three outcomes (bad, middling, good), each with a chance and a price by the resolve date, sized at a quarter of the Kelly stake from them (section 4) and capped at 2.5% of the portfolio;
  - an expected gain after costs, from those outcomes, of at least the cash rate plus 5% a year over the holding period (added 8 Nov 2026): about 3.6% for a six-month pick and about 14% for a two-year value pick at November 2026's 2.13% cash rate (section 4's NZ rate, the one src/decide.py uses);
  - at least one dated event expected to show the market is wrong, on or before the resolve date, and an exit rule;
  - a review by a separate agent that hasn't seen the analyst's reasoning, working through docs/RED_TEAM.md, saved in research/red_team/ with a verdict.
- Value picks (added 8 Nov 2026): a pick whose business is clearly cheap on its own figures may run up to 24 months to its resolve date, with its dated events being the results and meetings in that time rather than one event that forces the price. It qualifies when the deep dive's "nothing happens" or bad-case value is no more than 10% below the price and its middling value is at least 15% above it (25% until 8 Nov 2026, when the minimum expected gain was added). Everything else (the deep dive, the review, three outcomes, the 2.5% cap and the liquidity limit) is unchanged.
- Special situations (added 2 Nov 2026): a research pick may be a pre-deal or holder situation, such as an approach, a strategic review, a holder build-up or a controlling holder's moves, a failed bid, or a legal claim. It needs the same deep dive, review, outcomes, dated events and limits as any research pick, plus a section on the players and what the rules allow: who can move the price, their stakes, what they paid and can afford, what the takeover and trust rules let them do and when, and what the share is worth if nothing happens. The bad outcome's price is that "nothing happens" value. Binding deals stay in the deal sleeve under its own rules. The mechanical special situation types in section 9 stay barred because their history tests failed: only deep-dived, reviewed judgement calls are allowed, judged forward from 2 November 2026.
- Off limits: any company on Cam's excluded list (config/judgement_excluded.csv: companies Evergreen advises, has pitched or is pitching, or about which Cam holds information that isn't public). Gaming, wagering and racing picks wait until Cam has confirmed that list. No new position in the 30 sessions after a placement-pattern reopening (section 9, from test 9g).
- Cam's own calls go in this sleeve too, on the same terms, with his reason in his words on the card (the sector judgement allowance proposal in docs/JUDGEMENT_ALLOWANCE.md is folded in here).
- Rhythm: a research desk runs weekly (a scheduled task, docs/RESEARCH_TASK.md) through a five-stage funnel: the screen (src/research_screen.py); a ranking on the exchanges' own company data (tools/research_company_data.py and src/research_rank.py), which drops a company only on a rule a deep dive can't change and sends special situations to a watch list; fact sheets for the top 20 (research/facts/TEMPLATE.md), graded on the question a deep dive would settle and the gap if it goes our way, with no expected gain and no dropping on judgement; up to four deep dives a week from the A grades, each valuing the business before looking at the price; then the red team and the card. The evening desk places cards and watches the dated events.
- Judged on two things across the practice run: money made against the market (VAS for ASX picks, ENZL for NZX picks, both with dividends), and how accurate the stated chances turn out (Brier score). At the 18 December review Cam decides whether it carries into the counted run, and whether the 2.5% cap rises to 3%.
- The usual limits apply: one industry outside the core 15%, the liquidity limit, and the fall-from-peak rule (research holdings are sold with the other active sleeves at 8% and 12%).

### Deal size trial (a forward test, registered 1 Nov 2026 before its first night)
- The question: does the deal sleeve beat cash once positions are big enough that brokerage, capped per order, stops eating the spread? The history test of ASX cash deals (9c) found the market underpricing completion (74% implied, 90% paid) but the gain lost to costs at A$3,000 a deal.
- A separate trial book, outside the ledger, so the portfolio's limits and risk don't change (src/deal_trial.py, nightly after the deal monitor; reports/deal_size_trial.md).
- Entry: each night from 2 November 2026 to 31 March 2027, every live ASX and NZX deal not already in the trial, ASX cash deals included, enters when this section's entry rule holds at the base rate with no analyst adjustment: the chance times the offer value plus the rest times the break price, against the night's close, less the costs of a A$10,000 position, beats the local three-month rate to the expected payment date. One entry per deal.
- Two books with the same entries and exits: large at A$10,000 (NZ$10,000 on NZX) a position, small at A$3,000 (NZ$3,000), each cut to section 3's liquidity limit and smallest order, and the NZX order cap of section 7.
- Fills, spreads, size cost and lapses as in section 7; brokerage at 1.9% of each order capped at A$15 or NZ$25, with no monthly plan cover; the hedge's 0.1% on ASX positions. Dividends from EODHD's dividends feed are credited to shares held before the ex-date.
- Exit: paid on the implementation date at the latest terms (scrip at the acquirer's close that day, less half its spread and the brokerage to sell it); after a break, sold from the first session after the outcome date; a deal superseded by a rival follows the rival.
- Result per position: the gain after all costs less the local three-month rate on the money laid out for the days held. Open positions are marked at the close less half the spread and brokerage.
- Scored on 2 July 2027 over every position entered by 31 March 2027. Pass needs both: the large book's total gain after costs above cash, and its mean result per position above zero. The small book is reported beside it, so the effect of size alone shows.
- What a pass does and doesn't settle: it would show the deal spread pays at that size. Bigger positions also mean a bigger loss when a deal breaks (a 20% fall on A$10,000 is about 2% of the portfolio, against section 3's 1%), so changing the deal limits stays Cam's decision. The trial is read at the 18 December review, but with few deals resolved by then it can't settle anything for the counted run on its own.

## 6. Rules-only screen (failed its history test on 1 Nov 2026; kept for the record)

Result: on survivorship-free published data (Kenneth French library, to Sep 2026) a momentum-plus-profitability blend of large US shares beat the market by about 1% a year before costs. Holding it as 10 shares at Sharesies costs about 2.4% to 3.5% a year, so it falls behind the market. Holding it as two factor funds costs about 0.5% a year and stays ahead by 0.3% to 0.6%, but in the hold-out years one year (2020) supplied 75% of the gain, which fails the pass mark. Under section 9 the sleeve is dropped and its weight goes to cash.

- Universe: US shares that Sharesies offers, with a market value above US$2bn and a median daily trading value above US$20m.
- Score: rank on 12-month price return skipping the last month, and on gross profitability (gross profit over total assets). Average the two ranks.
- Hold the top 10, equal weight, rebalanced at the first open of each quarter.
- Every setting in this section is provisional until the history test (section 9) picks it.

## 7. Orders, fills and costs
- Decisions are logged with their time before any fill. Orders fill on a session that starts after the decision.
- Market orders fill at the official open, plus half the estimated spread (minus on sells), plus a size cost: one times daily volatility times the square root of order value over the 20-session average daily value, capped at 2%.
- Limit orders fill only when the session opens better than the limit, or trades through it by at least 0.1%.
- No fill above 10% of a session's volume; the rest rolls to the next session. A session with no volume gives no fill.
- An order that hasn't filled lapses after five sessions in which the share traded, or ten business days (a halted share), whichever comes first. The analyst can place it again as a fresh decision.
- NZX prices come from FinFeedAPI, which has no trading volumes. Agreed with Cam on 1 Nov 2026:
  - an NZX day counts as traded only if the price moved (open, high, low and close not all the same); on a day with no movement nothing fills;
  - outside the 20 largest NZX companies (config/nzx_top20.csv), no order is bigger than NZ$2,500;
  - the buy-sell gap charged is at least 0.6% outside the 20 largest and 0.25% for them;
  - with volumes unknown there is no volume cap and no size cost on NZX fills: the order cap stands in for both.
  The 20 largest are taken from a published table of NZX companies by market value (interest.co.nz's NZX 50 table, as at 30 October 2026) and refreshed at the first run of each quarter.
- A buy is cut to the cash there is. Foreign currency is converted from NZ$ only up to the NZ$ held, so nothing is ever borrowed.
- Costs are Sharesies NZ's, as at 31 October 2026:
  - the $15 plan, covering fees on the first NZ$5,000 of orders each month;
  - then 1.9% per order, capped at NZ$25 (NZX), A$15 (ASX) or US$5 (US);
  - 0.5% on every currency conversion.
- AUD and USD are bought in blocks and held as foreign cash.
- Spreads are estimated each month from daily highs and lows (Corwin and Schultz), with floors by liquidity.
- Dividends are credited on the payment date to holders on the ex-date. Scheme and offer consideration is paid on the real payment date. Halts, splits, consolidations and delistings are applied as they happened.
- NZ$ cash earns an on-call rate set at the start of each month from a major NZ bank's published rate, entered in config/run.json. If none is entered for a month, the NZ three-month bank rate less one point is used, fixed at the month's first run. Australian and US dollar cash earns nothing, as in a Sharesies wallet.

## 8. The daily cycle (each weekday, 9pm NZ time, after the nightly prices land at about 8:30pm)
1. Clerk: load the new prices, fill the orders waiting from the last decision, apply corporate actions, value the portfolio, check the limits.
2. Scanners: read the day's NZX, ASX and SEC filings for holdings and the watchlist, and flag events.
3. Analysts: write up new events and re-test any holding with material news.
4. Red team: argue against each proposed entry or exit.
5. Risk manager: approve or veto. A veto is logged with its reason.
6. Clerk: queue approved orders for the next open.

A missed run is caught up on real prices, and no decision is ever backdated. Cam is told only when a trade is placed, a holding has material news, or a limit trips. A report follows each month.

## 9. Testing on history before the run
- Tune on 2010 to 2019, then test once on 2020 to 2026.
- Record every version of a rule that's tried.
- Free data leaves out delisted shares, so the pass marks are set higher to allow for it.
- Pass marks:
  - Rules-only must beat US shares after Sharesies' costs in 2020 to 2026, with no single year providing more than half the gain, and a worst fall no more than 1.5 times the market's.
  - Each special situation type needs positive returns after costs in 2020 to 2026, on at least 30 events.
  - Deals must beat cash after costs, and our odds must score better than the market's spread.
- A sleeve that fails is dropped and its weight goes to cash.
- A special situation type that has not passed its test is not traded in the counted run.
- From test 9g: no new position in an ASX share within 30 sessions after it reopened from a halt at least 5% below its last close on heavy volume (the price pattern of a placement), unless it is a deal target whose deal was announced in that halt. Shares in that position lagged other small companies over the following month, before costs as well as after.

### 9a. Test registered on 1 Nov 2026, before any result: US director and officer buying clusters
- Events: at least N different directors or officers of a company buy its shares on the market within 30 days, together for at least US$100,000 (SEC Form 4 data sets). Ten-per-cent holders who are not directors or officers don't count. The event is the filing date of the report that completes the cluster; a new cluster on the same company needs a 90-day gap.
- Universe at entry: NYSE or Nasdaq shares at US$3 or more, with a 20-session median traded value of at least L. The Form 4 purchase price must be within 25% of the share's close on the trade date (this catches tickers that were later reused).
- Entry at the open of the first session after the filing date. Exit at the open H sessions later.
- Result per event: return less the S&P 500 (SPY) over the same sessions, after costs: US$5 brokerage each way at a US$1,700 stake, 0.5% currency conversion per round trip, half the estimated spread each way (Corwin and Schultz, with the engine's floors).
- Tuning on 2010 to 2019: N of 2, 3 or 4; H of 63 or 126 sessions; L of US$1m or US$5m. All 12 versions are recorded. The version with the highest mean after costs on at least 60 events is picked.
- One run of the picked version on events from 2020 to the latest event whose exit has happened. Pass needs all of: at least 30 events; mean after costs above zero with a t-statistic of 2 or more; still above zero with the best 5% of events removed; no single year more than half the total gain.
- Prices: Tiingo, for a fixed random sample of tickers (seed 20261101) within the free plan's 500 symbols a month: 336 tickers, drawn from 2,736 with a cluster from 2020 and 3,624 with one in 2010 to 2019 (280 hold-out, 200 tuning, 144 in both). Tiingo may miss some delisted shares, so the result is a screen, not proof.
- The data: 390,049 open-market purchases by directors and officers from January 2010 to March 2026, giving 18,264 clusters of two or more buyers, 10,987 of three or more and 6,955 of four or more.

### 9b. Test registered on 1 Nov 2026, before any result: US cash deal spreads
- Events: the first preliminary merger proxy (PREM14A) or first response to a tender offer (SC 14D9) filed by each company from 2015 to 2025, from the SEC's quarterly form indexes. The company's ticker at the time comes from the SEC's Form 4 data sets, because completed targets are delisted and missing from today's ticker list.
- Terms: the cash price per share found in the filing's text. The event counts only if, at entry, the share trades between 85% and 101% of that price, which confirms the price is the deal's and the deal is cash. Events with no cash price, or failing the check, are left out and counted.
- Entry at the open of the first session after the filing date. Exit at the first of:
  - the last session the share traded (taken as completion, paid at the higher of the cash price and the last close, so a raised price counts, with no sale costs);
  - the open after the first close more than 15% below the cash price (taken as a break, sold with costs);
  - the close 400 days after entry (sold with costs).
- Result per event: return after US$5 brokerage on a US$2,300 stake (and again on a sale), 0.5% currency conversion, and half the estimated spread on each trade, less the 3-month Treasury bill rate over the same days.
- Nothing is tuned. Pass needs all of: at least 60 events; mean result above zero with a t-statistic of 2 or more; no single year more than half the total gain; worst calendar year no worse than a 4% loss per event on average (the sleeve's loss limit at 4% positions).
- Odds: the market-implied chance at entry is (entry price less the break price) over (cash price less the break price), with the break price the close 60 sessions before the filing. Reported with the actual completion rate, so the test shows whether spreads have overstated the risk of a break.
- Prices: Tiingo, for a fixed random sample (seed 20261102) fetched from 1 November 2026 within the free plan's limits (anything a month's limit holds back follows in December): 360 tickers, drawn from 1,169 with a cash price found. The events: 2,002 companies with a first PREM14A or SC 14D9 from 2015 to 2025, 1,821 matched to their ticker at the time, 1,201 with a cash price in the filing.

### 9c. Test registered on 1 Nov 2026, before any result: ASX cash deal spreads
- Events: every resolved ASX cash scheme or full takeover bid in the deal database (deals/all_deals.csv) announced from 2015 to 2025, leaving out majority-holder buy-outs: 133 events on 121 codes as at registration. The outcome is the holder's: paid if the deal completed, or a rival completed at the same or a higher price; otherwise broke.
- Entry at the open of the first session after the announcement date, only if that open is between 85% and 101% of the cash offer (which confirms the share on the code and that the deal is cash).
- Exit: a deal that paid is credited at the final price paid on the implementation date (or the outcome date if none is recorded), with no sale costs. A deal that broke is sold at the open of the first session after its outcome date, with costs.
- Result per event: return after Sharesies' ASX brokerage on a A$3,000 order (on the buy, and on a sale), 0.5% currency conversion, the hedge's 0.1% dealing cost, and half the estimated spread on each trade (from the 20 sessions before the announcement), less the Australian three-month bank bill rate over the same days.
- Nothing is tuned. Pass needs all of: at least 60 events; mean result above zero with a t-statistic of 2 or more; no single year more than half the total gain; worst calendar year no worse than a 4% loss per event on average.
- Runs only if prices are found, and the entry check passed, for at least 70% of the deals that paid and 70% of the deals that broke, so that delisted shares missing from the feed can't tilt it. Otherwise it reports "not run" and ASX deals carry on under the base-rate method.
- If it runs and fails, ASX cash deals are dropped from the deal sleeve under this section (scrip and NZX deals carry on), and the weight goes to cash.
- Reported only, not a pass mark: the same rules entering when the scheme booklet is out; the market-implied chance at entry against the actual paid rate.
- Prices: EODHD (paid plan), fetched once for the 121 codes. The test runs once when they are in, writes reports/deal_au_history.md and locks.

### Shared terms for 9d to 9f (registered 1 Nov 2026, before any result)
- Prices: Norgate Data's daily prices for every listed and delisted ASX security since 2010 (data/norgate/), as traded for entry checks and price floors, and with dividends and capital events for returns. A delisted share is sold at its last close.
- The market: the Vanguard Australian Shares ETF (VAS) with dividends, the same fund the core holds.
- Costs on every position: Sharesies' ASX brokerage on a A$3,000 order on the buy and on the sale (A$15 each), and half the estimated spread on each trade (Corwin and Schultz, from the 20 sessions before the trade, with the engine's floors). No currency conversion per trade: the sleeve holds Australian dollars and converts only when it is funded or emptied. The hedge's 0.1% dealing cost on each position.
- Tradable: at entry, a price of at least A$0.10 and a median daily traded value of at least A$50,000 over the previous 60 sessions, the liquidity limit the rulebook already uses for a A$3,000 position.
- Each test runs once when its data is in, writes its report and locks. A pass makes its type tradable in the special situations sleeve at up to 3% a position; a fail leaves it untraded.

### 9d. Test registered on 1 Nov 2026, before any result: shares left behind when a deal fails
- Events: every ASX scheme or full takeover in the deal database announced from 2015 to 2025 that ended without paying holders (the holder outcome used in section 5: terminated, withdrawn or lapsed, or topped by a rival that also failed), with an outcome date, leaving out majority-holder buy-outs.
- Entry at the open of the first session after the outcome date, when the arbitrage funds sell.
- Exit at the first of: the open after a new control deal for the company is announced (from the deal database); the open 252 sessions after entry; the last close if the share delists.
- Result per event: return after costs less the market's return over the same days.
- Nothing is tuned. Pass needs all of: at least 20 events with prices; mean result above zero with a t-statistic of 2 or more; still above zero without the best 5% of events; no single year more than half the total gain.
- Reported only: how many were bid again within the hold, and the return of those against the rest.

### 9e. Test registered on 1 Nov 2026, before any result: a model of the next takeover target
- The question: which ASX shares receive a binding control deal (a scheme or takeover bid in the deal database) within the next 12 months.
- Universe at each quarter end: ASX shares passing the tradable test, with at least 252 sessions of prices, leaving out exchange-traded funds by name.
- Features, from prices and the deal database only, known at the quarter end: median daily traded value (size); total return over 1, 3 and 12 months, and against the market over 12 months; distance below the 52-week high; 3-month volatility; volume over the last 20 sessions against the previous 120 (a surge); a failed or rejected deal for the company in the previous 2 years; the number of deals in its industry code in the previous 2 years is not available and is left out.
- Model: a penalised logistic regression fitted on quarter ends from 2011 to 2017, so that no label (a bid within 12 months) reaches into the 2019 run. The penalty is chosen by five-fold cross-validation on those years only.
- The trading rule: at each quarter end from 2019 to the latest quarter whose 3 months have passed, buy the 5 highest-scored shares in equal amounts at the next open and sell at the open 3 months later (a share bid in the meantime is held to that date, or sold at its last close if it delists).
- Run once on 2019 onwards. Pass needs all of: mean quarterly result after costs above the market with a t-statistic of 2 or more across the quarters; the shares picked received a bid within 12 months at least three times as often as the universe did; no single year more than half the total gain.
- Reported only: how often the top 20 and top 50 were bid, and a lift chart by score band.
- Its weakness, stated now: deals under about A$100m and approaches that never became binding are missing from the deal database, so some shares the model ranks highly count as misses when they were in fact approached.

### 9f. Test registered on 1 Nov 2026, before any result: the June tax-year sell-off
- Why it might work: Australian investors sell losing shares before 30 June to claim the loss; a New Zealand holder has no such reason, so can buy what they sell.
- Each year, on the ranking date: the tradable ASX shares with the lowest total return since the previous 1 July (at least 200 sessions of prices), the bottom 10% up to 20 shares.
- The benchmark: the equal-weighted return of every tradable share over the same days, so a general small-share rally in July doesn't count as the effect.
- Tuning on 2010 to 2017 (all 4 versions recorded): ranking and buying on 15 June (or the session before) or on the last session of June; selling on the last session of July or of August. The version with the highest mean yearly result after costs is picked.
- One run of the picked version on 2018 to 2026. Pass needs all of: picks beat the benchmark after costs in at least 6 of the 9 years; the 9-year mean of yearly results above 2%; no single year more than half the total gain.
- Reported only: the same with the bottom 5% and with no 20-share cap.

### Shared terms for 9g to 9j (registered 1 Nov 2026, before any result)
- The terms shared by 9d to 9f apply (Norgate prices, costs, the tradable test, run once and lock), except where a test below says otherwise.
- Equal-weighted benchmark: where a test says so, the mean return over the same sessions of every ordinary share that passes the tradable test on the entry day, rather than VAS, because these tests trade small companies and VAS is mostly large ones. The result against VAS is reported alongside.
- The t-statistic is worked out on monthly averages (events grouped by the month they start), so overlapping positions don't count as separate evidence.

### 9g. Test registered on 1 Nov 2026, before any result: placement flippers
- The question: after an ASX small company raises money by placement, do the shares recover once the people given cheap shares have sold theirs?
- An event, from Norgate prices alone: an ordinary share that traded on each of the 20 sessions before a gap of 1 to 3 sessions with no trades (a trading halt), then reopens at least 5% below its last close before the gap, on at least 3 times its median volume of the 60 sessions before the gap. Left out: a gap across which Norgate records a dividend or capital event (rights issues and consolidations show as one), and any event within 60 sessions of an earlier event for the same share.
- The trade: buy at the open a set number of sessions after the share reopens, sell at the open a set number of sessions later, against the equal-weighted benchmark, after costs. The share must pass the tradable test on the entry day.
- Tuning on events from 2010 to 2017 picks the version: entry 5 or 10 sessions after reopening; held 20 or 40 sessions. The picked version runs once on 2018 onwards, on every event whose holding period has ended.
- Pass needs all of: at least 100 events in the run; a mean result after costs above zero with a t-statistic of 2 or more; still above zero without the best 5% of events; no single year more than half the total gain.
- Reported only: results by size of the drop (5 to 15%, over 15%) and against VAS; for shares in ASIC's daily files, how often the share count rose at least 3% within 20 sessions of reopening (how often the pattern really was a raising).
- Its weakness, stated now: a halt and a drop can be bad news rather than a raising; the ASIC check measures how often.

### 9h. Test registered on 1 Nov 2026, before any result: listed options below what they're worth
- The question: do ASX-listed options trade below their value if exercised (the share price less the strike) by enough to lock in a gain after costs?
- Options: every ASX-listed option in Norgate whose name gives its strike and expiry, matched to its company's ordinary shares by code; one option is taken to convert into one share (the usual terms).
- An event: a session at least 15 sessions before expiry when the option closes at or below 95% of (the share's close less the strike), with the share above the strike. Only the first event for each option counts.
- The trade: buy the option at the next open, exercise at once (paying the strike), and sell the shares at the open 10 sessions later, the time allowed for the new shares to arrive. Return on the money laid out (option plus strike), after brokerage on both trades, half the spread on each (the option's own spread from its highs and lows, with the engine's floors) and the hedge's dealing cost. The option must have traded at least A$5,000 on the entry day, so a position of a few hundred dollars or more fits the rulebook's 10% of volume limit.
- Run once on every event to the latest whose 10 sessions have passed. Nothing is tuned.
- Pass needs all of: at least 30 events; a mean result above zero with a t-statistic of 2 or more; still above zero without the best 5% of events.
- A pass does not make it tradable until Cam chooses a broker that trades and exercises ASX-listed options and its costs go into section 7; Sharesies is not assumed to.
- Its weakness, stated now: Norgate holds options from about 2024 only; some options convert at other ratios or have conditions, which the name doesn't show.

### 9i. Test registered on 1 Nov 2026, before any result: short sellers covering
- The question: when hedge funds cut their short positions in an ASX share quickly, does the share then beat the market?
- Data: ASIC's daily aggregated short positions (data/asic), each day's file treated as known only from the fifth business day after its date, since ASIC publishes about four business days late. ASIC codes are matched to the Norgate share trading on that code on that day.
- At each month end, among tradable ordinary shares in ASIC's files whose short position was at least a set share of shares on issue a set number of sessions earlier: the 10 with the largest fall in that share since then are held in equal amounts for the month. Only names entering or leaving are traded, each at the next open, after costs.
- Tuning on 2011 to 2017 picks the version: the earlier short position at least 2% or at least 5% of shares on issue; the fall measured over 20 or 60 sessions. The picked version runs once on 2018 onwards.
- Result each month: the picks against the equal-weighted return of every tradable share in ASIC's files over the same month.
- Pass needs all of: a mean monthly result after costs above zero with a t-statistic of 2 or more; ahead in at least 55% of months; no single year more than half the total gain.
- Reported only: the same signal on the 52 New Zealand companies also listed on the ASX, against their NZX prices from July 2023 (too few for a pass mark).

### 9j. Test registered on 1 Nov 2026, before any result: franked special dividends in ASX schemes
- The question: before a target pays a special dividend as part of a scheme, does the market price the Australian tax credit into the shares, so that a New Zealand holder, who can't use the credit, does better selling before the dividend than holding to the end?
- Events: ASX schemes in the deal database announced 2015 to 2025 that paid holders, where Norgate records a dividend of at least 1% of the share price with an ex-date between the announcement and the last day of trading.
- The comparison, for each event: selling at the open on the last session before the ex-date (less half the spread and brokerage), against holding: the dividend plus the last traded price before the shares stop trading (the remaining scheme payment, which holders receive without brokerage). Result: selling divided by holding, less one.
- Run once; nothing is tuned. Pass needs all of: at least 15 events; a mean result above zero with a t-statistic of 2 or more; still above zero without the best 5% of events.
- A pass adds a rule to section 5: for an ASX scheme position, the desk sells before a special dividend's ex-date when the price is above the dividend plus the remaining payment by more than the cost of selling.
- Its weakness, stated now: Norgate doesn't say whether a dividend is franked, so unfranked specials are included and would weaken any effect.

### 9k. Test registered on 1 Nov 2026, before its data was gathered: buying ASX deals after the ACCC raises concerns
- The question: when the ACCC signals trouble with a takeover, does the market mark the deal down further than the deals' later completion justifies?
- Data: the ACCC's public merger registers (the informal review register for 2002 to 2025, and authorisations), matched to the deal database's ASX deals by target and bidder (data/regulators/accc_deals.csv); prices as in 9c (Norgate where its file is the company the database names, EODHD otherwise).
- Events: the ASX cash schemes and takeover bids of test 9c (announced 2015 to 2025, resolved), where, while the deal was live, the ACCC published a statement of issues or moved its provisional decision date later or suspended it. A request for information on its own doesn't count. The event date is the first such signal.
- The trade: buy at the open of the first session after the event date, if the deal hasn't ended by then and the open is between the undisturbed price and 101% of the offer. Exit as in 9c: a deal that paid is credited at the final price on the payment date with no sale costs; a deal that broke is sold at the first open after its outcome date, with costs. Rival bids are followed as in 9c.
- Costs as in the shared terms for 9g to 9j (a A$3,000 position, brokerage both ways where there is a sale, half the spread on each trade, the hedge's 0.1%, no currency conversion per deal). Result: return after costs less the Australian three-month bank bill rate over the same days.
- Run once; nothing is tuned. Pass needs all of: at least 12 events; a mean result above zero with a t-statistic of 2 or more; still above zero without the best 5% of events (at least one); and a lower market-implied chance at entry than the share of these deals that paid.
- Reported only: the same at A$10,000 a position (the deal size trial's size); events that were a statement of issues against those that were only a delay; and the outcomes of ACCC-reviewed deals with no signal.
- Its weakness, stated now: few deals draw a statement of issues, so the sample will be small; NZ regulators (Commerce Commission, Overseas Investment Office) are left out of the run for the same reason.

### 9l. Test registered on 1 Nov 2026, before its data was gathered: government contracts and ASX small companies
- The question: when a Commonwealth contract that is large for the company that won it is published on AusTender, does the company's share price rise afterwards?
- Data: AusTender contract notices (data/austender/), matched to ASX-listed companies by supplier name and ABN (data/austender/matched.csv, high-confidence matches and medium ones checked by hand); Norgate prices.
- Events: a published contract notice, or an amendment that raises a contract's value (counted at the rise), for a matched company whose ordinary shares traded on the publication date, worth at least 5% of the company's market value at the close before publication. Market value is that close times the shares on issue from ASIC's daily files (the latest within 30 days), or failing that from EODHD's reported shares outstanding at the latest earlier date; a company with neither is left out and counted in the report. A company's notices within 20 sessions of an event are part of that event.
- The trade: buy at the open of the first session after publication, hold a set number of sessions, against the equal-weighted benchmark of the shared terms for 9g to 9j, after costs, the share passing the tradable test on entry.
- Tuning on events published 2013 to 2018 picks the holding period: 20 or 60 sessions. The picked version runs once on events from 2019 whose holding period has ended.
- Pass needs all of: at least 40 events in the run; a mean result after costs above zero with a t-statistic of 2 or more (monthly); still above zero without the best 5% of events; no single year more than half the total gain.
- Reported only: results by contract size (5 to 20% of market value, over 20%), Defence against other agencies, and against VAS.
- Its weakness, stated now: a company must announce a material contract to the ASX, often before AusTender publishes it, so an effect can only come from contracts the company didn't announce or the market didn't price; contract value is not profit.

### 9m. Test registered on 1 Nov 2026, before the membership data arrived: buying predicted index additions before S&P announces them
- The question: can the S&P/ASX 200 and 300 additions be predicted from public data before S&P announces them, and does buying the predictions beat mid-sized shares once costs are paid?
- S&P's rules (S&P Dow Jones Indices): the ASX 200 is rebalanced each quarter and adds a non-member that ranks 179th or higher by three-month average float-adjusted market value at the reference date; the ASX 300 is rebalanced in March and September, adding at 274th or higher. Since September 2021 the reference date is the second-to-last Friday of the month before the rebalance and the changes are announced on the first Friday of the rebalance month; before that, the reference date was the last Friday of the month before (the second-to-last for September) and the announcement the second Friday (the first for September). Changes take effect after the third Friday.
- Data: Norgate's daily prices and its record of each security's membership of both indexes (data/norgate/index_changes.csv and index_members.csv); shares on issue from ASIC's daily files; the deal database.
- The prediction, at each reference date: rank every ASX ordinary share by its average market value over the 63 sessions to the reference date (each day's close times the latest ASIC share count; there is no free-float figure, so this is the full market value). Left out: shares not in ASIC's files, New Zealand and other "Foreign Exempt" listings, funds and ETFs by name, and targets of a live deal in the deal database. A non-member of the ASX 200 ranked within a set cut-off is a predicted ASX 200 addition; at the March and September rebalances, a non-member of the ASX 300 ranked within a set cut-off is a predicted ASX 300 addition (a share predicted for both counts once).
- The trade: buy each prediction at the open of the first session after the reference date, sell at a set exit, against the equal-weighted return of the shares ranked 101st to 400th at the reference date over the same sessions, after the costs of the shared terms for 9g to 9j.
- Tuning on rebalances from 2011 to 2017 picks the version: the ASX 200 cut-off at 160th or 179th; the ASX 300 cut-off at 260th or 274th; the exit at the first open after the announcement or at the open of the third Friday (the last session before the change takes effect). The picked version runs once on rebalances from 2018 to September 2026.
- Pass needs all of: at least 60 trades in the run; a mean result after costs above zero with a t-statistic of 2 or more, worked out on the average of each rebalance; still above zero without the best 5% of trades; no single year more than half the total gain.
- Reported only: how many predictions S&P did add at that rebalance; ASX 200 against ASX 300 predictions; the result against VAS.
- Its weakness, stated now: without free-float figures and S&P's liquidity screen the ranks are rougher than S&P's; index funds and others trade the same changes, and the announcement-day rise has shrunk over the years.

## 10. Success tests (scored on 2 July 2027)
1. Ahead after all costs.
2. Ahead of an index-and-cash mix with the same ups and downs.
3. Reported against the core's index mix held at 100%.
4. Worst fall never more than 10% below the peak.
5. Across at least 40 dated calls, our odds score better than the market's implied odds.

## Change log
| Date | Change | Why |
|---|---|---|
| 2026-10-31 | Version 0 drafted from the build plan | Start of build |
| 2026-11-08 | Value picks: the middling case needs to be at least 15% above the price, down from 25% (section 5a) | Cam's decision, after the minimum expected gain was added the same day. Capral was the case in view: bad case -7%, expected about +15% after costs over 22 months, middling +18.5%. Judged forward from 8 Nov 2026 |
| 2026-11-08 | Research picks need an expected gain after costs of at least the cash rate plus 5% a year over the holding period (section 5a; src/decide.py refuses a card below it) | Cam's decision, choosing this over a stricter bar with 5 more points for estimation error and over no minimum. The first case to reach the red team (AI-Media) expected about +9% in four months, so the bar needed setting before any card. Judged forward from 8 Nov 2026 |
| 2026-11-08 | Research picks: the screen's trading floor drops from A$50,000 to A$10,000 a day (the A$2,000 position stays within section 3's 10% of two days' volume), and value picks may run up to 24 months (section 5a) | Cam's decision. Eight deep dives found nothing that cleared a six-month window; the two changes aim the research at where a small portfolio has an edge, smaller companies and patience. Judged forward from 8 Nov 2026 |
| 2026-11-02 | Research picks may cover special situations (section 5a): pre-deal and holder situations and legal claims, deep-dived and reviewed, with a players-and-rules section and the bad case set at the "nothing happens" value; binding deals stay in the deal sleeve and the mechanical special situation types stay barred | Cam's decision. Seven deep dives on 1 and 2 Nov 2026 found the businesses fairly priced on their own; the remaining gaps sat in what big holders, bidders or courts might do. The judgement-based version has never been tested, so it is judged forward |
| 2026-11-02 | Research picks: the screening funnel rebuilt (section 5a, Rhythm). A ranking stage on the exchanges' own company data replaces the quick look as the first cut; quick looks are replaced by standard fact sheets that grade the question and the gap if it goes our way, with no expected gain; deep dives value the business before looking at the price, and take outcome prices from that valuation | Cam's decision. On 1 Nov 2026, 51 of 69 companies were dropped on judgement after a quick read, and every rough estimate came out between +2% and +5% with none negative: a quick read anchors on the price, so it can't find an edge. The new stages drop only on rules and spend deep-dive time where the checkable gap is largest |
| 2026-11-01 | Research picks: the cap per pick lifted from 2% to 2.5% of the portfolio; the sleeve stays at 10% and at most five companies | Cam's decision. At 2% (NZ$2,000) no NZX pick could ever be bought, since the smallest NZX order is NZ$2,500 (which keeps NZX brokerage near 1%) |
| 2026-11-01 | Research picks added (section 5a): up to 10% in at most five overlooked NZX and ASX small and mid caps, 2% each, each bought only after a deep dive from primary sources and a red-team review; special situations cut from 15% to 5% to make room (it holds cash while no type has passed a test). Cam's own calls fold into it on the same terms | Cam asked for deep dives into overlooked small and mid caps; 13 history tests of public-data patterns failed, and this is judged going forward instead, since it can't be fairly tested on the past |
| 2026-11-01 | Section 9l result: fail. Commonwealth contracts worth at least 5% of the winning company's market value, bought the session after AusTender published them and held 20 sessions (the version tuning picked; both lost in tuning), beat small shares by about 1.1% before costs but lagged them by 1.19% after costs (51 events from 2019, t of -0.41). 168 such contracts since 2013 across 469 matched listed companies; notices for companies with no share count (not in ASIC's files, and EODHD's fundamentals aren't in the plan) were left out, as registered. Not traded | Recorded as the registered test found it (reports/contracts_history.md) |
| 2026-11-01 | Section 9l: amendments left out, new contract notices only, in tuning and the run alike. Decided when the data arrived and before any result | AusTender's API dates amendments published from July 2020 with migration dates, and later ones possibly with the date of a later edit, so their dates aren't when the market could first see them (data/austender/README.md) |
| 2026-11-01 | Section 9m result: fail. Predicted index additions (ASX 200 cut-off 160th, ASX 300 cut-off 260th, sold at the open of the third Friday, the version tuning picked) lagged mid-sized shares by 0.90% a trade after costs (798 trades from 2018, t of -2.13 by rebalance). S&P added only 178 of the 798 predictions (52 of 409 for the ASX 200): without free-float figures and S&P's liquidity screen the ranks pick too many companies S&P passes over. The ones it did add made 3.1% after costs; the rest lost 2.1%. Not traded | Recorded as the registered test found it (reports/index_additions_history.md); nothing in the test was changed after the result. Norgate's membership file (data/norgate/index_members.csv) was exported for this test before it ran |
| 2026-11-01 | Section 9m registered before the index membership data arrived: buying predicted S&P/ASX 200 and 300 additions before the announcement | Cam asked for the index change angle; the timetable and buffers are S&P's published rules |
| 2026-11-01 | Section 9k result: fail. Of the ASX cash deals in 9c's set, the ACCC publicly reviewed 17, and only 4 drew a statement of issues or a delay while live (3 usable, 12 needed): Origin broke after its statement of issues (-12.6% after costs and cash); Mantra and Tox Free paid after delays, about break-even. The ACCC-reviewed deals with no concern or delay paid 12 of 13. The other ten deals with a statement of issues were paid in shares or partly in shares, outside 9c's set. 22 cash deals weren't searched on the registers (a search limit); spot checks of the likeliest found nothing to add. Not traded | Recorded as the registered test found it (reports/accc_history.md); the ACCC data is in data/regulators/ for the desk to use on live deals |
| 2026-11-01 | Sections 9k and 9l registered before their data was gathered: buying ASX deals after the ACCC raises concerns, and government contracts on AusTender against ASX small companies | Cam asked for angles that need information put together from several sources |
| 2026-11-01 | Section 9: no new position in an ASX share in the 30 sessions after a halt and a reopening at least 5% lower on heavy volume, unless it is a deal target announced in that halt | From the 9g result: those shares kept lagging small companies, before costs as well as after |
| 2026-11-01 | Section 5: deal size trial registered before its first night. A separate trial book enters every live ASX and NZX deal that passes the entry rule at the base rate, at A$10,000 and at A$3,000 a position, with the engine's fills and costs; scored on 2 July 2027 | Cam asked for it: 9c found the market underpricing completion but the gain lost to costs at A$3,000, and brokerage is capped per order, so size may change the answer. History can't test that without reusing data already seen; the run's own days are new |
| 2026-11-01 | Section 9i result: fail. The 10 shares a month where short positions fell most (from at least 5% of shares on issue, over 60 sessions, the version tuning picked) returned 0.48% a month before costs against 0.72% for all shorted shares, and 1.17% a month less after costs (104 months from 2018, t of -2.24; ahead in 41% of months). Not traded | Recorded as the registered test found it (reports/short_cover_history.md); nothing in the test was changed after the result |
| 2026-11-01 | Section 9j result: fail. Selling an ASX scheme target before a dividend's ex-date did worse than holding in 36 of 42 schemes (mean -3.31%, t of -1.82); on the ex-date prices fell by a median 0.95 times the dividend, so the market did not pay extra for franking credits in these shares | Recorded as the registered test found it (reports/scheme_special_history.md) |
| 2026-11-01 | Section 9h result: fail. Only 11 listed options in tradable shares closed below 95% of their exercise value at least 15 sessions before expiry (30 needed), and those 11 lost 5.7% on average after costs and the 10 sessions waiting for the shares | Recorded as the registered test found it (reports/listed_options_history.md) |
| 2026-11-01 | Section 9g result: fail. After a halt and a drop of 5% or more on heavy volume (70% of them confirmed as share issues by ASIC's share counts), ASX shares bought 5 sessions after reopening and held 20 sessions (the version tuning picked; all four versions lost in tuning) lagged small shares by 3.20% after costs (531 events from 2018, t of -4.89), about 0.6% of it before costs. Not traded | Recorded as the registered test found it (reports/placement_history.md) |
| 2026-11-01 | Sections 9g, 9h and 9j: details set in the code before any of their results: an order that can't fill rolls to the next session the share trades, up to 10 (9g, as in section 7); option strikes, which Norgate's names round to the cent, are taken half a cent higher, and the share must pass the tradable test (9h); a target still trading more than 120 days after its scheme's outcome is a different company on a reused code and is left out (9j) | Data handling, decided before the results |
| 2026-11-01 | Sections 9g to 9j registered, with their rules and pass marks, before any of their data was examined for results: placement flippers, listed options below their value, short sellers covering (ASIC's daily files), and franked special dividends in ASX schemes. A one-day trade between the ASX and NZX lines of New Zealand companies was considered and not registered: NZX costs on a NZ$2,500 order (about 1% each way plus a spread of at least 0.6%) are larger than any such gap is likely to be | Cam asked for angles a small New Zealand account can take that others don't, using Norgate and other data few people use |
| 2026-11-01 | NZX prices: every date moved forward one trading day, and the nightly fetch now asks for the right day. FinFeedAPI labels each NZX session with the UTC date it opens on, the evening before in New Zealand, so every NZX price had been stored a day early and the nightly job would have missed every Monday. Found by lining NZX moves up against the same companies' ASX lines (Norgate): they matched a day later, not on the day. NZ public holidays now have no prices, as they should | A data fault, fixed before the practice run's first night; nothing had been traded on NZX prices |
| 2026-11-01 | Section 9e result: fail. The 5 highest-scored ASX shares each quarter lost 3.09% a quarter against the market after costs (30 quarters from 2019, t of -2.01; ahead in 12). They were bid within 12 months 3.7 times as often as the market as a whole (14 of 135 against 2.8%), but the model's scores did not rank the rest of the market (each tenth of it was bid at about the same rate), and the shares it picked were mostly beaten-down companies whose losses outweighed the bids. Not traded | Recorded as the registered test found it (reports/target_model_history.md); nothing in the test was changed after the result |
| 2026-11-01 | Section 9e: only a share that trades at the open after the quarter end can be bought; a halted or delisting share is passed over for the next highest score, as in 9f. Made after the first run stopped on four such picks and before any 9e result was seen | The first run could not price those picks and stopped without a result; the registered rule buys at the next open, which a share with no trade that day doesn't have |
| 2026-11-01 | Section 9f result: fail. The ASX's biggest losers since 1 July, bought at the end of June (the version tuning on 2010 to 2017 picked, though all four versions lost there) and sold at the end of August, beat small shares in 4 of 9 years from 2018; the mean of +2.96% a year came from 2022 and 2025 alone. Not traded | Recorded as the registered test found it (reports/june_selloff_history.md); nothing in the test was changed after the result |
| 2026-11-01 | Section 9d result: fail. Shares left behind when an ASX deal failed beat the market by 3.07% after costs on average over the next year, but the median was -2.96% and t was 0.46 (22 events from 2016); without the best event the mean was below zero, and 2020 alone held 70% of the total gain. Not traded | Recorded as the registered test found it (reports/failed_deal_history.md); nothing in the test was changed after the result |
| 2026-11-01 | Section 9e: model fitted on quarter ends to 2017, not 2018, before any data was read | A 2018 quarter's label looks 12 months ahead into 2019, the years the model is tested on |
| 2026-11-01 | Sections 9d to 9f registered, with their rules and pass marks, before the data they need was looked at: shares left behind when a deal fails, a model of the next takeover target, and the June tax-year sell-off | The tests so far looked at strategies many investors already trade; these look for forced selling and for your knowledge of how takeovers happen |
| 2026-11-01 | Section 9c result: fail. ASX cash deals bought at the first open after the announcement returned 0.61% less than cash after costs (108 deals from 2015 to 2025, t of -0.49; 2019 averaged a 9% loss a deal). The market's prices implied a 74% chance of completion against 90% that paid, but the costs a New Zealand holder pays (about 1.7% a deal) took the spread. ASX cash deals are not traded; ASX scrip deals and NZX deals carry on, and US deals wait for 9b | Recorded as the registered test found it (reports/deal_au_history.md); nothing in the test was changed after the result |
| 2026-11-01 | Deal database: seven missing dates filled from the original announcements (payment dates for PLG, CRD, VRL, AST, IAP and ABC; the date Pioneer Credit's Carlyle scheme ended), before the 9c result | Every gap of this kind was filled, not only the ones that changed the 9c count |
| 2026-11-01 | Section 9c: prices from Norgate Data (which keeps delisted ASX shares, each under its own symbol when a code is reused) wherever its file is the company the deal database names, and EODHD otherwise; COF, FND and PRG are left out because neither source holds the old company under those codes. Set before any return was worked out | EODHD has no ASX shares delisted before about 2017, which kept coverage under the 70% the test needs |
| 2026-11-01 | Section 9c: first run stopped at the coverage check (60% of paid deals and 80% of broken deals priced and past the entry check, against 70% needed), so no returns were worked out. Seven targets whose ASX codes were later reused by other companies (CCL, CRD, MTR, PLG, SLA, SRX, VRL) are now priced from EODHD's symbols for the old company, and the test runs again when its prices are in; a pass or fail is final, a "not run" is not | The prices were for the wrong companies, which is a data fault, not a change to the test |
| 2026-11-01 | Section 9a result: fail. US director and officer buying clusters lost 2.62% a trade against the S&P 500 after costs in 2020 to 2026 (420 events, t of -2.47, 39% beat the index); they are not traded, and with no other type tested the special situations weight sits in cash | Recorded as the registered test found it (reports/special_insider_history.md); nothing in the test was changed after the result |
| 2026-11-01 | Rules-only sleeve dropped; its 10% goes to cash | Failed the history test before the rules were locked: see reports/rules_only_history.md |
| 2026-11-01 | Dates brought forward at Cam's request: practice run 2 November to 31 December 2026 (was 7 December to 29 January), counted run 4 January to 2 July 2027 (was 1 February to 30 July), rulebook locked 31 December | The build finished early; most live ASX deals end before December |
| 2026-11-01 | Section 9c: history test for ASX cash deal spreads registered, with its rules and pass marks, before any data was looked at | The deal sleeve is the core of the strategy and had no history test of its own |
| 2026-11-01 | Section 5: starting odds by stage and as a holder sees them, a tested deal-feature model, and a break price moved by the market | The plain completion rate treated every scheme alike whatever its stage, and counted a winning rival bid as a failure |
| 2026-11-01 | Section 7: list of the 20 largest NZX companies filled from interest.co.nz's NZX 50 table as at 30 October 2026 | The S&P/NZX 20 list itself isn't published in a form that can be read; the top 10 by S&P's March 2026 weights are all in it |
| 2026-11-01 | Section 9b: prices fetched from 1 November rather than December; nothing else in the test changes | So US deals can join the practice run sooner. No 9b result has been seen |
| 2026-11-01 | Section 5: US deals not traded until test 9b passes | The practice run now starts before 9b can be priced |
| 2026-11-01 | NZX rules for prices without volumes (section 7), agreed with Cam | FinFeedAPI's NZX feed has prices but no volumes |
| 2026-11-01 | After an independent review of the engine: order lapse, no borrowing, fall-from-peak sales by rule with a review lock, limits counting waiting orders, the break-loss test on the whole position, foreign cash earning nothing | Fixes for findings 3, 4, 8, 9 and 14 of the review |
| 2026-11-01 | Hedging, cash rate and deal-entry costs written out as the engine applies them; special situation types limited to those with a passed test | So the rulebook and the code say the same thing |
| 2026-11-01 | Section 9b: deal spreads history test for US cash deals registered, with its rules and pass marks, before any data was looked at | As for 9a |
| 2026-11-01 | Section 9a: special situations test for US director and officer buying clusters registered, with its settings and pass marks, before any data was looked at | So the test can't be fitted to the hold-out years |
| 2026-11-01 | Daily cycle moved from 7:30pm to 9pm NZ time; prices fetched at 8:30pm NZ time in both daylight-saving seasons | At 7:30pm NZ in winter the ASX close is barely an hour old and the free feed may not have it; a fixed UTC time drifted by an hour across seasons |
| 2026-10-31 | NZ core moved from FNZ to ENZL; NZ companies with an ASX listing are priced and traded on that line until an NZX feed is in place | EODHD does not carry NZX (its exchange list has no NZ entry), and no free feed found does |
