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
| Market core | 40% | 35–45% | VT 20%, VAS 10%, FNZ 10% (to confirm on Sharesies before day one) |
| Deal spreads | 25% | 0–30% | Agreed schemes and takeover offers: NZX, ASX and US |
| Special situations | 15% | 0–20% | Dated events: holder build-ups, strategic reviews, rejected bids, director buying clusters, index changes, offers priced at a discount |
| Rules-only | 10% | 5–15% | 10 US shares from the quarterly screen (section 6) |
| Cash | 10% | 5% floor | On-call cash |

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

## 6. Rules-only screen (to be fixed by the history test)
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

## 8. The daily cycle (each weekday, 7:30pm NZ time)
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
