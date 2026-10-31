# Engine review: paper-portfolio

Reviewed 1 November 2026 against RULEBOOK.md sections 3, 5 and 7. Code as on disk at /home/claude/paper-portfolio (HEAD fd7d215; the src files were last changed at 01:07 NZDT on 1 November). Nothing in the repository was edited.

## How this was checked

- All seven test scripts pass (`for t in tests/test_*.py; do python3 -I $t; done`).
- Each finding below was read against the code. Most were reproduced with small scripts on the real October 2026 data, using temporary ledgers. The scripts are in `review/probes/` next to this file and take the repository path as their only argument, for example `python3 -I -B review/probes/probe1.py /home/claude/paper-portfolio`.

## Summary

| # | Severity | Area | Finding |
|---|---|---|---|
| 1 | High | State | A split entry makes every later run fail, permanently |
| 2 | High | Money | Dividends go to whoever holds on the pay date, not the ex-date |
| 3 | High | Money | NZ$ cash can go negative on foreign buys, with no interest charged |
| 4 | High | Limits, state | Pre-trade checks ignore orders already queued; placing a card twice doubles the position |
| 5 | High | Limits | Any sleeve name other than exactly "deal" or "special" skips almost every limit |
| 6 | Medium-high | Lookahead (benchmark) | The benchmark uses a US close the portfolio can't see yet, and drops dividends paid during the run |
| 7 | Medium-high | Limits | The industry 15% and regulator/bidder 10% limits never count existing holdings |
| 8 | Medium | Limits | The 1% loss-on-break is skipped without a break price and is applied per order, not per position |
| 9 | Medium | Limits | The fall-from-peak rule is only a flag: no halving, no exit, no hold until a review |
| 10 | Medium | Limits | About half of deal cards sized at the 4% cap are vetoed by the 4% cap check (rounding) |
| 11 | Medium | State, money | A run that fails part-way books interest again when it is re-run |
| 12 | Medium | Process, money | Nothing enters dividends, consideration or splits, and the desk has no step for it |
| 13 | Medium-low | State | Full exits leave a one-share stub about 15% of the time |
| 14 | Medium-low | State | Orders expire after 5 sessions, counting zero-volume sessions; the rulebook says the rest rolls |
| 15 | Low-medium | Timing | A daytime run books the evening early and the real run then skips it; the ledger can't show when a record was written |
| 16 | Low | Money | The cash-short fill path charges the fee on the uncut order (NZX only, not reachable today) |
| 17 | Low | Lookahead | Rate series are used before publication in catch-up runs |
| 18 | Low | Fills | A blank low in a price file lets a buy limit fill as "traded through" |
| 19 | Low | Costs | Entry-cost test: the sale fee can fall inside this month's cover; hedge rolls are counted once |
| 20 | Low | Reporting | The monthly report leaves hedge dealing costs and the size cost out of costs paid |

## What holds up

- Fill timing. An order only fills in a session whose open is after the decision time, and only once that session is final at the run time (clerk.py:131-132). Sizing and the prices decide.py sees use only sessions final at the decision time (clerk.py:91, decide.py:68, market_data.py:68-72), and the spread, volatility and volume figures use bars before the date. Checked for US and ASX sessions in both daylight-saving seasons. No lookahead was found in decisions, sizes or fills.
- Brokerage, the plan cover (with its stated assumption for an order that straddles the cover), the 0.5% conversion (taken once, on the NZ$ entered, clerk.py:236-242), market fill prices with half the spread and the size cost, the 10% volume cap and the Corwin and Schultz formula all match the rulebook.
- Hedges. The forward rate moves the right way with the interest gap, the mark-to-market gains when the foreign currency falls, the 0.1% cost is built into the dealt rate, re-sizing happens at 20%, the hedge closes when the position goes, and hedged less unhedged equals the hedge result.
- Consideration is booked as a fee-free sale on the payment date and kept out of the plan cover.
- Running daily.py again on a date already run does nothing (daily.py:131-136), and fills, the plan fee and corporate actions are each guarded against a second booking (but see finding 11).

## Findings

### 1. A split entry makes every later run fail (High)

Where: clerk.py:51-54 (state) with clerk.py:204-207 (split booking).

What's wrong: when a split falls due, the clerk writes one record per holder (`{"type": "split_applied", "sleeve", "market", "ticker", "qty_change", "ref"}`) and then a general marker `{"type": "split_applied", "ref"}` with no sleeve. state() treats every `split_applied` record as a holder record and reads `p["sleeve"]`, so the marker raises KeyError. state() is called at the start of every run, so from then on the engine can't run at all. The ledger is append-only and nothing reads a reversal record, so the marker can't be undone without breaking the chain. Each failed retry also books interest again (finding 11).

Scenario: hold 75 VAS (core) from 2 October and enter a 2-for-1 split effective 8 October. The runs for 1 to 7 October are fine; 8, 9 and 12 October all fail with `KeyError: 'sleeve'` (probe1.py, part A).

The other way round is also wrong: prices are unadjusted, so if a split is not entered the price halves while the share count doesn't. That is a phantom 50% loss on the line, enough to trip the fall-from-peak flags.

How sure: certain (reproduced).

Fix: in state(), apply only `split_applied` records that carry `qty_change` (or give the marker its own type that still ends in `_applied`). Adjust the quantity and limit of open orders on the ticker at the split. Add a reversal record type that the clerk honours.

### 2. Dividends go to pay-date holders, not ex-date holders (High)

Where: clerk.py:186-197.

What's wrong: section 7 says dividends are credited on the payment date to holders on the ex-date. The clerk pays whatever is held when the payment date arrives (`st["positions"]`); `ex_date` is never read. Buy after the ex-date and you collect a dividend the price has already given up, which is double counting with unadjusted prices. Sell between the ex-date and the payment date and you lose a dividend you were owed. ASX schemes often pay a special dividend just before implementation, so this will come up in the deal sleeve.

Scenario: dividend of A$1.00, ex-date 2 October, paid 20 October. A buy decided on 6 October fills 74 VAS on 7 October. The 20 October run credits A$74.00 (probe1.py, part B). It should credit nothing.

Also, between the ex-date and the payment date the value drops by the dividend with nothing booked in its place, which understates value and the fall from peak over that window.

How sure: certain (reproduced).

Fix: make `ex_date` required on dividend records. Work out holders from fills with a session date before the ex-date, plus splits before it. Optionally book a receivable on the ex-date and settle it on the payment date. Use the record date the same way for consideration.

### 3. NZ$ cash can go negative (High)

Where: clerk.py:155-167 and 236-242; interest at clerk.py:121.

What's wrong: for an AUD or USD buy that is short of foreign cash, the clerk converts the shortfall from NZ$ without checking the NZ$ balance. The cash cut at lines 161-167 only compares foreign cash, which the conversion has just topped up, so the fill always goes through in full. Interest is only accrued on a positive NZ$ balance, so the overdraft is free. That is borrowing, which section 3 bans. Core rebalances (daily.py:45-78) don't pass through any cash check either.

Scenario: NZ$10,000 deposited, then two US orders on the same evening for NZ$8,000 each (VT and SPY). After the next run NZ$ cash is -4,920.81 and no interest is charged; the clerk only flags "cash -48.4% is below the 5% floor" (probe2.py).

How sure: certain (reproduced).

Fix: before converting, cap the conversion at the NZ$ available and cut the quantity to what the converted amount buys; log "no cash" if nothing is affordable. Fixing finding 4 matters too, since queued orders are how this happens in practice.

### 4. Pre-trade checks ignore queued orders (High)

Where: decide.py:61-64 and 85-88; risk.py:70-95.

What's wrong: check_order works from the latest valuation, which only holds filled positions. Orders placed earlier the same evening, or not yet filled, don't count towards the position cap, the sleeve band, the cash floor, or the industry and group limits. decide.py has nothing to stop the same card being placed twice.

Scenario: run the October dry run to 29 October, then place the same SDF deal card (stake NZ$3,900) at 9:30pm and again at 9:40pm. Both pass, both fill on 30 October, and SDF ends at 7.7% of the portfolio against the 4% cap (probe3.py). A desk task that is retried after a failed push would do exactly this. Likewise, eight 4% deal cards on one night would each pass the 30% sleeve band and, with cash at 30%, take NZ$ cash negative (finding 3).

How sure: certain (reproduced).

Fix: in decide.py, add every open order from `state(L)["open_orders"]` (quantity times `ref_close`, in NZ$) to the held value, the sleeve value, the cash used and the industry and group sums before calling check_order. Refuse a buy when the same sleeve and ticker already has an open buy, unless the card says it's a top-up.

### 5. Unknown sleeve names skip nearly every limit (High)

Where: risk.py:47-48, 78-82 and 101-107; clerk.py:28 (hedging).

What's wrong: the caps, the bands, the drawdown block and the cash-rate test are looked up by sleeve name with `.get()` or an `in` test, so a name other than exactly "deal" or "special" gets none of them. "rules" (the dropped sleeve), "Deal" or "deals" are all accepted, and such a position isn't hedged either. Decision cards are written by hand.

Scenario: a card with sleeve "Deal", outcomes 95% at 1.00 and 5% at 0.50, price 0.90, break price 0.50, the portfolio 15% below its peak, and an expected return of 0% against a 3% cash rate. It is sized at NZ$25,000 (quarter Kelly, a quarter of the portfolio) with no breaches. The same card with sleeve "deal" is sized at NZ$2,250 and gets two breaches (probe8.py).

How sure: certain (reproduced).

Fix: reject any card or order whose sleeve isn't core, deal or special, in decide.py and in place_order.

### 6. The benchmark is a US session ahead and drops dividends (Medium-high)

Where: benchmarks.py:39-58; fetch_prices.py:57-81 with benchmarks.py:28-36.

What's wrong, part (a): the index mix for valuation date d uses the last close dated on or before d. For VT and ENZL (75% of the mix) that is the US session dated d, which closes about 11 hours after the 9pm NZ valuation. At that valuation the portfolio can only see the session before. So success tests 2 and 3 compare the portfolio with a benchmark that is one session later at both ends.

Scenario (a): for the valuation on 30 October 2026 (08:00 UTC), the benchmark uses VT's 30 October close (final at 20:30 UTC), while the portfolio uses 29 October. VT fell 1.67% on 30 October, so that one day moves the comparison by about 1.2 points (probe6.py).

What's wrong, part (b): the docstring says adjusted closes make dividends count, but the nightly fetch only appends new dates, so a stored `adj_close` is never re-adjusted when a later dividend goes ex. Across an ex-date the ratio is then the price return only.

Scenario (b): store 18 March at a close of 140.00 (adjusted 140.00), then the 19 March ex-date at 139.30 after a US$0.70 dividend. The benchmark shows -0.5% for a day whose total return is nil (probe7.py). On the past year's payments, VT, VAS and ENZL going ex between February and July would leave out roughly 0.8 points over the counted run, in the portfolio's favour.

How sure: (a) certain; (b) certain on the code path, size estimated from last year's dividends.

Fix: (a) value the benchmark with the same as-of rule as the portfolio (`Prices.last_close` with `nz_evening_utc(d)`). (b) build the total return from unadjusted closes plus the stored dividend field (Tiingo's divCash; the EODHD rows for VAS have no dividend field, so VAS needs another dividend source), or re-fetch the full adjusted history for the three benchmark lines each night.

### 7. The industry and regulator/bidder limits never bite (Medium-high)

Where: decide.py:86-87; risk.py:86-95; config/run.json.

What's wrong: check_order counts existing holdings in an industry or group through maps passed in from `cfg["industries"]` and `cfg["groups"]`. run.json has neither key and nothing writes them, so only the new order is counted, and a single 3% or 4% order can never reach 15% or 10%.

Scenario: with SDF at 7.7% from finding 4 (industrials, ACCC), four more industrials/ACCC deal cards at NZ$3,900 each pass with no breach (probe3.py). Placed, they would put about 23% of the portfolio in one industry waiting on one regulator.

How sure: certain (reproduced).

Fix: store industry and group on the decision and order (they are already on the card) and build the maps from the ledger for current holdings and open orders.

### 8. The 1% loss-on-break can be bypassed (Medium)

Where: risk.py:50-53; check_order has no break-loss test.

What's wrong: the limit is applied only when the card has a `break_price`, so a deal card without one is sized with no break limit at all. It is also applied to each order's own stake rather than to the position after the order, so a top-up (or the duplicate in finding 4) can take the loss on a break above 1%.

Scenario: an OML card with outcomes 90% at +6% and 10% at -30% and no break price is sized at NZ$4,004 (the 4% cap). If it breaks, the loss is NZ$1,201, 1.2% of the portfolio. With the break price set it is sized at NZ$3,337 (probe3.py). Top-up case, from the code: hold 3.1% with a 32% break loss, then add 0.9% through a smaller card stake. The position is 4.0%, which passes the cap, and the loss on a break is 1.28%.

How sure: certain (first case reproduced; top-up traced through the code).

Fix: require `break_price` on deal cards (or use the lowest outcome price), and in check_order test (held plus order) times the break loss against 1% of the portfolio.

### 9. The fall-from-peak rule isn't carried out (Medium)

Where: clerk.py:227-230; risk.py:101-105.

What's wrong: section 3 says that at 8% below the peak the deal and special sleeves are halved, and at 12% they move to cash until a review. The clerk only adds a flag; no orders are queued. check_order blocks new deal and special buys only while the current fall is 12% or more, so a recovery to 11.9% opens new entries again (at half the sleeve's target weight) with no review on record. "Halve" is also read as half the target weight, not half of what is held.

Scenario: peak NZ$100,000; a fall to NZ$87,900 (-12.1%) is flagged; the next day at NZ$88,200 (-11.8%) a new deal that keeps the sleeve under 12.5% passes.

How sure: certain (read; the behaviour follows directly from the code).

Fix: when -12% is first reached, write a "review required" record and have check_order block deal and special buys until a review record follows. Have the clerk queue the halving and exit sales, or at least flag every day they are missing.

### 10. Deal cards sized at the cap are vetoed about half the time (Medium)

Where: risk.py:55 and 79.

What's wrong: size_position rounds the stake to cents (`round(0.04 * total, 2)`), and check_order vetoes anything more than 0.000001 over 4% of the total. When the rounding goes up, a stake sized exactly at the cap is logged as a cap breach and not placed.

Scenario: total NZ$100,176.93 gives a stake of NZ$4,007.08 against a cap of NZ$4,007.0772, so the card is vetoed with "position would be 4.0%, over the 4% cap" (probe3.py). Over 10,000 random totals, 4,854 cap-sized cards were vetoed (probe10.py). The 3% special cap behaves the same. Tight deals, where the 4% cap is the binding limit, are the common case.

How sure: certain (reproduced).

Fix: round stakes down (`math.floor(x * 100) / 100`) or give check_order a one-cent tolerance.

### 11. Interest is booked twice after a failed run (Medium)

Where: clerk.py:117-125 with daily.py:131-138.

What's wrong: interest is accrued from the last valuation date and booked at the start of the run, and the valuation is written at the end. If anything fails in between, daily.py re-runs that date next time (there is no valuation for it) and books interest for the same days again. Real triggers exist: finding 1 (every run after a split), and a dividend record with neither `pay_date` nor `effective_date`, which raises TypeError at clerk.py:191-192 (probe9.py). A consideration that fails part-way through its holder loop would also be partly booked twice.

Scenario: NZ$100,000 at 3%; the 5 October run fails after step 1 and then succeeds. There are two interest records, NZ$32.87 and NZ$32.88, for the same four days (probe5.py, with the failure simulated).

How sure: certain on the mechanism (reproduced).

Fix: tag interest with the run date and skip it if a record exists for that date (or accrue from the last interest record), and check corporate action records when they are entered.

### 12. Nothing enters dividends, consideration or splits (Medium)

Where: clerk.py:185-208 reads only `corporate_actions` records that someone has written; docs/DAILY_RUN.md and docs/DESK_TASK.md have no step that writes them, and no script does.

What's wrong: without manual entries, the core funds' dividends (about 2% a year on 40% of the portfolio) are never credited; a completed scheme leaves the position valued at its last close, with its hedge open and no cash paid; and a split shows as a loss. The price files already carry Tiingo's dividend and split fields, and nothing reads them.

How sure: certain (read).

Fix: add a checked entry script (dividend: ex-date, pay date, currency, amount per share; consideration: record and payment dates; split: ratio and an ex-date that matches the price feed), a desk step that uses it, and a nightly check that flags any held ticker whose price file shows a dividend or split with no record booked.

### 13. Full exits leave a one-share stub (Medium-low)

Where: decide.py:97 and clerk.py:99-100.

What's wrong: a full sale is converted to NZ$ (held times price times 1/rate) and back again (times the rate), then rounded down. Floating-point error makes it one share short about 15% of the time. The stub stays in the book, keeps a hedge re-sized to one share (with another 0.1% charge), and the sale order shows as complete.

Scenario: holding 3,869 shares at 195.55 with a rate of 0.853461 gives a sale order for 3,868. In 20,000 random cases using real FX rows, 3,057 came out one share short (probe4.py).

How sure: certain on the formula (simulated with the same arithmetic, not run end to end).

Fix: for a full exit, pass `qty=held` to place_order.

### 14. Order expiry doesn't match the rulebook (Medium-low)

Where: clerk.py:26 and 180-183.

What's wrong: section 7 says the unfilled rest rolls to the next session, with no expiry. The clerk cancels after 5 sessions since the decision, and zero-volume sessions count. In the other direction, an order on a ticker whose file gets no new rows (a halt, or the EODHD daily limit) never expires, and fills whenever rows arrive, however stale the decision has become.

Scenario: an OCA buy decided on 20 October; 21 to 27 October are zero-volume rows, and the order is cancelled on the 27 October run without ever meeting a session that could fill it (probe9.py).

How sure: certain (reproduced).

Fix: settle the rule and write it into section 7. Count only sessions with volume, and add a calendar limit (say 10 business days) so orders on halted shares lapse.

### 15. Run timing and the record of when things were written (Low-medium)

Where: daily.py:115-138; clerk.py:112; ledger.py:40-47; .github/workflows/nightly-data.yml.

What's wrong: daily.py runs the current NZ date whenever it is started and stamps it 9pm. A push to config/run_now.txt during the day books that evening early on stale ASX prices (the fetcher holds back an unfinished session), and the scheduled run that night then skips the date as done. The scheduled job itself runs at about 8:30pm but stamps 9pm. Ledger.append stores only the timestamp the caller gives, so catch-up core orders carry past times and there is no record of when anything was actually written, which is what "no decision is ever backdated" needs in order to be checked.

How sure: certain on the code. As written, no lookahead follows from it.

Fix: refuse to run today's date before `nz_evening_utc(today)`, and add a `written_utc` field set from the clock in Ledger.append.

### 16. Cash-short fill path (Low, not reachable today)

Where: clerk.py:154-167.

What's wrong: the fee and the plan cover are worked out on the uncut order before the cash check. If the fill is cut, the fee stays at the full order's fee. If nothing fills ("no cash"), the in-memory plan cover has still been used up, so later fills in the same run pay fees they shouldn't. Only NZ$ (NZX) buys reach this branch, and there is no NZX feed yet.

Fix: work out the fee after the final quantity is known, on a copy of the plan state.

### 17. Rate series used before publication in catch-up runs (Low)

Where: rates.py:22-40; daily.py:30-34.

What's wrong: DTB3 is keyed by its observation date, so a run at 9pm NZ on date d uses the T-bill rate for US date d, which hasn't happened yet (a live run won't have it in the file; a catch-up run will). The NZ monthly average is treated as known on the 1st of the next month, but the file fetched on 31 October ends at September, so it is published later than that; the month's fallback cash rate then changes part-way through the month when the file updates. The effects are a few dollars.

Fix: key DTB3 at the next day and the NZ series at its real release date, and fix the month's cash rate once, at the first run of the month, and reuse it.

### 18. A blank low is read as zero (Low, latent)

Where: market_data.py:59-60; fills.py:60.

What's wrong: a blank low becomes 0, and a buy limit then counts as traded through and fills at the limit. No current file has a blank or zero low, but Tiingo can return nulls.

Fix: don't use a bar with any missing open, high, low or close for a limit test.

### 19. Entry-cost test details (Low)

Where: decide.py:44-46 and 53.

What's wrong: the sale brokerage is priced against what is left of this month's cover, so for small stakes it comes out nil, though the sale will usually happen in a later month. The hedge cost is counted once, though a position held past 91 days rolls its forward and pays the cost again each quarter.

Fix: price the sale fee with no cover left, and count one hedge cost for each 91 days to the resolve-by date.

### 20. Monthly costs (Low)

Where: monthly.py:43-51.

What's wrong: "costs paid" leaves out hedge dealing costs and the size cost inside fill prices.

Fix: add both (the hedge cost from each open record, notional over the mid forward times 0.001; the size cost from a figure stored with each fill).

## Other notes (checked against the code, not reproduced)

- The nightly job (daily.py) and the evening desk (decide.py) both append to `ledger/<name>/orders.jsonl` and `decisions.jsonl`, and both push after `git pull --rebase`. If the nightly job is late and the desk goes ahead, which DAILY_RUN.md allows after 30 minutes, the two appends will conflict. A hand-merged file would break the hash chain, and daily.py and decide.py both stop on a broken chain.
- Foreign cash (sale proceeds and the 2% conversion buffer) earns no interest while NZ$ cash does. The rulebook doesn't say which applies.

## Fixes (1 November 2026, the same night)

Every finding was fixed and the reviewer's probe scripts re-run against the fixed code. New checks for each fix are in tests/test_clerk_actions.py, tests/test_risk.py and tests/test_decide.py, and run in every nightly job.

| # | Status | What changed |
|---|---|---|
| 1 | Fixed | Splits are applied before fills, at the first run where the effective session is final; only holder records change holdings; open orders on the share are cancelled; a `void` record stops an action not yet applied |
| 2 | Fixed | Dividends need an ex-date and go to shares held before it; owed dividends count in the valuation until paid; consideration can take a record date |
| 3 | Fixed | Conversion is capped at the NZ$ held and the fill cut to the cash there is, fee included |
| 4 | Fixed | Limits count waiting buys as if filled; a second buy of the same share while one waits needs `top_up` |
| 5 | Fixed | Unknown sleeve names are refused in decide.py, risk.py and place_order |
| 6 | Fixed | The benchmark uses the portfolio's as-of rule and a total return from closes plus dividends (feed or ledger) |
| 7 | Fixed | Industry and regulator/bidder labels come from the cards in the ledger, with config/run.json filling gaps |
| 8 | Fixed | The 1% loss-on-break is tested on the whole position; a deal card without a break price uses its worst outcome |
| 9 | Fixed | At 8% the nightly run sells half of each deal and special holding, at 12% the rest, once per peak; a review must be logged before new active positions |
| 10 | Fixed | Stakes are rounded down to the cent and the cap check has a one-cent tolerance (0 of 10,000 vetoed in probe10) |
| 11 | Fixed | Interest is booked once per run date; each corporate action is booked once per holder |
| 12 | Fixed | src/actions.py enters and checks actions; the nightly run flags dividends and splits the feed shows with none entered, and held shares with no new price for five business days; the desk has a step for it |
| 13 | Fixed | A full exit sells the held quantity |
| 14 | Fixed | An order lapses after five sessions that traded or ten business days; written into rulebook section 7 |
| 15 | Fixed | A daytime run stops at yesterday; every record carries `written_utc`; the nightly run flags any analyst decision written more than 10 minutes after its time |
| 16 | Fixed | The fee is worked out on the final quantity, on a copy of the plan state |
| 17 | Fixed | T-bill rates count from the next day, the NZ monthly rate from the 15th of the next month, RBA rates three days after month end; the month's cash rate is fixed at its first run |
| 18 | Fixed | A bar with any price missing or zero is not used |
| 19 | Fixed | The sale fee is priced with no plan cover left; the hedge cost is counted for each three-month roll |
| 20 | Fixed | The monthly report shows hedge dealing costs; it notes the size cost is inside fill prices |
| Note: concurrent writes | Fixed | The desk places nothing if the nightly job hasn't landed |
| Note: foreign cash | Settled | Rulebook: AUD and USD cash earns nothing, as in a Sharesies wallet |
