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
| Special situations | 15% | 0–20% | Dated events: holder build-ups, strategic reviews, rejected bids, director buying clusters, index changes, offers priced at a discount |
| Rules-only | 0% (was 10%) | n/a | Dropped on 1 Nov 2026: failed the history test (section 6, reports/rules_only_history.md). Its 10% goes to cash under section 9 |
| Cash | 20% (was 10%) | 5% floor | On-call cash, including the rules-only sleeve's 10% |

Only special situation types that pass a history test are traded (section 9). So far one type can be tested on free data: US director and officer buying clusters (9a). Holder build-ups, strategic reviews, rejected bids, index changes and discounted offers have no free event data yet, so until one is found they are watched and written up but not traded.

Money an active sleeve can't use well stays in cash. The core and the rules-only sleeve are brought back inside their bands at the first open of each quarter.

## 3. Limits
- Per deal: 4% of the portfolio, and the loss if the deal breaks no more than 1% of the portfolio. The break price is the undisturbed price, or lower where the evidence says so.
- Deals waiting on one regulator, or from one bidder: 10% of the portfolio.
- Per special situation: 3%. Per rules-only share: 1%.
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
