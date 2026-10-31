# Rulebook, version 0 (draft, 31 October 2026)

This is the working draft. It's tightened during the practice run and locked on 29 January 2027, once Cam signs it off. After that, a rule changes only to fix a defect, through a dated entry in the change log at the end, and every change is reported to Cam.

## 1. The run
- Bankroll: NZ$100,000, in NZ dollars.
- Practice run: 7 December 2026 to 29 January 2027. It runs live and nothing counts.
- Counted run: from the open on 1 February 2027 to the close on 30 July 2027.
- Tax is ignored entirely, including withholding on foreign dividends.

## 2. Sleeves
| Sleeve | Target weight | Band | Holds |
|---|---|---|---|
| Market core | 40% | 35–45% | VT 20%, VAS 10%, ENZL 10% (to confirm on Sharesies before day one). ENZL, the US-listed iShares MSCI New Zealand fund, replaces FNZ because no free feed carries NZX prices |
| Deal spreads | 25% | 0–30% | Agreed schemes and takeover offers: NZX, ASX and US |
| Special situations | 15% | 0–20% | Dated events: holder build-ups, strategic reviews, rejected bids, director buying clusters, index changes, offers priced at a discount |
| Rules-only | 0% (was 10%) | n/a | Dropped on 1 Nov 2026: failed the history test (section 6, reports/rules_only_history.md). Its 10% goes to cash under section 9 |
| Cash | 20% (was 10%) | 5% floor | On-call cash, including the rules-only sleeve's 10% |

Money an active sleeve can't use well stays in cash. The core and the rules-only sleeve are brought back inside their bands at the first open of each quarter.

## 3. Limits
- Per deal: 4% of the portfolio, and the loss if the deal breaks no more than 1% of the portfolio. The break price is the undisturbed price, or lower where the evidence says so.
- Deals waiting on one regulator, or from one bidder: 10% of the portfolio.
- Per special situation: 3%. Per rules-only share: 1%.
- One industry outside the core: 15%.
- Smallest order: NZ$2,500 on NZX, A$1,500 on ASX, US$500 in the US.
- Liquidity: no position larger than two sessions' trading at 10% of daily volume, measured on the 20-session median.
- Fall from peak: at 8% below the portfolio's peak, halve the deal, special situation and rules-only sleeves. At 12%, move them to cash until a review. The core is never timed.
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
- Entry needs an expected return above the cash rate, after costs and annualised to the expected completion date, and a stated reason why the market's spread is wrong.
- Odds start from the deal database's base rates for that structure, bidder type and regulator, then adjust for evidence, each adjustment written down.
- Deal positions in AUD and USD are hedged back to NZ dollars in the simulation at the forward rate (the interest-rate gap, from published rates), and also reported unhedged.
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
- Costs are Sharesies NZ's, as at 31 October 2026:
  - the $15 plan, covering fees on the first NZ$5,000 of orders each month;
  - then 1.9% per order, capped at NZ$25 (NZX), A$15 (ASX) or US$5 (US);
  - 0.5% on every currency conversion.
- AUD and USD are bought in blocks and held as foreign cash.
- Spreads are estimated each month from daily highs and lows (Corwin and Schultz), with floors by liquidity.
- Dividends are credited on the payment date to holders on the ex-date. Scheme and offer consideration is paid on the real payment date. Halts, splits, consolidations and delistings are applied as they happened.
- Cash earns an on-call rate set at the start of each month from a major NZ bank's published rate.

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

## 10. Success tests (scored on 30 July 2027)
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
| 2026-11-01 | Section 9a: special situations test for US director and officer buying clusters registered, with its settings and pass marks, before any data was looked at | So the test can't be fitted to the hold-out years |
| 2026-11-01 | Daily cycle moved from 7:30pm to 9pm NZ time; prices fetched at 8:30pm NZ time in both daylight-saving seasons | At 7:30pm NZ in winter the ASX close is barely an hour old and the free feed may not have it; a fixed UTC time drifted by an hour across seasons |
| 2026-10-31 | NZ core moved from FNZ to ENZL; NZ companies with an ASX listing are priced and traded on that line until an NZX feed is in place | EODHD does not carry NZX (its exchange list has no NZ entry), and no free feed found does |
