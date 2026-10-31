# NZ deal database: verification notes

Checked 31 October 2026 against `../nz/nz_deals.csv` (46 rows), `../nz/nz_candidates.csv` and `../nz/NOTES.md`.

Files in this folder:

- `nz_deals_verified.csv`: the full database after corrections. Same header, row order and deal IDs as the original.
- `nz_deals_verification_log.csv`: one line per change or flag (133 lines: 25 corrected, 76 filled, 32 flagged). Lines for the `sources` and `notes` columns record the URLs added and the short verification sentence appended to each changed row.

## What I checked

All 46 rows were checked against at least one primary record: a Takeovers Panel register page, a target company statement, an offer document, a scheme booklet, a scheme implementation agreement, an NZX announcement, an OIO decision or a company release. How deep the check went varied:

- **Full re-read of the main document** (TCS, booklet, offer document or SIA, plus the register page): Finzsoft, Horizon, Kathmandu, Scott, Pulse, Hellaby, Abano 2016, TeamTalk, Zeta/NZOG, Opus, Fliway, Restaurant Brands 2018, Methven, Abano 2019, Manawa, NZ Windfarms, Marsden, Smartpay, Comvita, Bremworth/Floorscape, Rakon, 2 Cheap Cars, SLI, Tilt 2018.
- **Register page plus NZX or company announcements**: Diligent, Nuplex, Airwork 2016, Fairfax/Tower, Vero/Tower, OGOG/NZOG, Trilogy, Tegel, Trade Me, Augusta, Abano 2020, Z Energy, Pushpay, MHM, Millennium & Copthorne, Restaurant Brands 2025, Mangawhai/Bremworth.
- **Register page only** (dates, prices and outcome confirmed; booklet figures such as adviser ranges and conditions not re-read): Airwork 2017, Orion Health, Metlifecare, Tilt 2021, Arvida.

days_to_outcome was recomputed for every row. All 45 original values matched their dates. Two changed because dates changed (Nuplex filled, SLI corrected).

## How many rows changed

- 20 rows had at least one data field changed.
- 7 of those had a correction (a value that was wrong): Horizon, Tegel, SLI, MHM, Marsden, Bremworth/Floorscape, 2 Cheap Cars.
- 10 field corrections: intentions_pct 2, and one each of blocking_holders, outcome_date, days_to_outcome, financing_condition, premium_pct_announced, undisturbed_basis, failure_reason, pre_bid_stake_pct.
- 59 blanks filled. The largest groups: financing_condition 6, due_diligence_condition 6, equity_value_m 5, booklet_date 5, board_recommendation 4, ier_verdict 4, ier_low 3, ier_high 3, break_fee_m 3, regulators 3, undisturbed_price 3.

The corrections that matter most:

- **Tegel (NZ-2018-01)**: the locked-up 45% holder, Claris Investments, was recorded as a Bain Capital vehicle. Tegel's private equity owner was Affinity Equity Partners. This is the same kind of error as the substantial holder notice caught earlier.
- **SLI Systems (NZ-2018-03)**: outcome_date was the unconditional date (19 Dec 2018). The register shows the offer closed on 2 Jan 2019 at 95.45%, and the database convention for takeovers is the close date. days_to_outcome goes from 58 to 72.
- **Bremworth/Floorscape (NZ-2025-07)**: failure_reason was "vote", but no meeting was held. The SIA lapsed at its end date after holders of 38% said they would vote against. Now "other", with the detail.
- **Marsden (NZ-2025-03)**: intentions_pct counted only Northland Regional Council (53.61%). Port of Auckland's 19.90% had also agreed to vote in favour, so the figure is 73.51%.
- **Horizon (NZ-2015-02)**: financing_condition changed from N to Y. The offer had the same bankers-funding condition that is recorded as Y for Hellaby.

The named blanks are now filled or explained:

- Nuplex implementation date: 13 Sep 2016 ("Scheme of Arrangement Completed" on the ASX list; Dechert gives the same date). outcome_date and days (155) filled.
- Trilogy outcome date: not settled. Secondary sources put implementation at 18 Apr 2018 (OIO consent was 27 Mar 2018), but no NZX notice was found, so outcome_date stays at the scheduled court date and is flagged.
- Tickers: Finzsoft is FIN (from its own NZX announcement), Horizon is HED (from the TCS). Pulse Energy's NZAX code is still not found.

## Errors seen more than once

1. **Date conventions applied unevenly.** SLI used the unconditional date instead of the close date. Tegel used the lock-up date instead of the takeover notice date. Abano 2016 used a takeover notice that was later withdrawn. Each one moves days_to_outcome.
2. **Condition fields classed inconsistently.** A condition that the bidder's bankers not withdraw funding was recorded Y for Hellaby and N for Horizon. Kathmandu and 2 Cheap Cars had the same condition and were blank. All four are now Y.
3. **Support counts that miss holders.** Marsden left out Port of Auckland. SLI used the rounded 51% from the chairman's letter instead of the 51.27% in the sale-agreement table.
4. **Secondary or rounded figures where a filing exists.** MHM's price, premium and support came from a broker note (the NZX release gives 86.8%, not 87%). 2 Cheap Cars' stake was the rounded "approximately 76%" (the offer document gives 75.924%). The Vero price came from a news report (Suncorp's own release now confirms NZ$1.40).
5. **Documents not opened.** Most of the blanks filled came from documents the builder listed or could reach but did not read through, especially the later parts of long booklets (Methven share count and fee, Abano reimbursement sums) and offer documents (Kathmandu, SLI, Tilt 2018 conditions).

## Rows I couldn't fully verify

These are flagged in the log and left as they were:

- **Tegel**: announce date (probably 25 Apr 2018, the takeover notice, not the 24 Apr lock-up), undisturbed price ($0.82 per press), premium (50% per press) and minimum acceptance (50% per press). The Panel did not publish the TCS or offer document.
- **Scott Technology**: date the binding subscription agreement was signed, implementation date, and JBS's pre-deal stake.
- **Trilogy**: implementation date (see above).
- **Vero/Tower**: board recommendation, premium, and whether termination was 6 or 7 Nov 2017.
- **Airwork 2016**: adviser range, board view and premium (press gives $4.79 to $5.56, accept, 22%; TCS not published).
- **Z Energy**: equity value and adviser range. Also, the announcement values the offer at NZ$3.83 including the first 5c of the interim dividend; under the database's own convention for permitted dividends, offer_price_initial would be 3.83, not 3.78.
- **Bremworth (both rows)**: equity value, because the share count wasn't found.
- **Pulse Energy**: ticker, and intentions_pct of 0 understates the holders who said they would accept.
- **Zeta/NZOG**: intentions_pct (lock-ups exist but no total is stated).
- **MHM**: bidder_type. Bettcher is majority owned by KKR. Kept as trade.
- **Airwork 2017, Orion Health, Metlifecare, Tilt 2021, Arvida**: register only, so adviser ranges, conditions and break fees in these rows were not re-read.

## Scope

No row fails the size threshold, and every row has a takeover notice or signed agreement. Two kinds of row are flagged for a decision, not removed:

- **Buy-outs by a holder that already had control** (nine rows: Horizon, Pulse, Airwork 2017, Tilt 2018, Orion Health, Millennium & Copthorne, Restaurant Brands 2025, 2 Cheap Cars, and Marsden, where a consortium member held 53.61%). SCHEMA counts offers "that would give the bidder control". On a strict reading these didn't, because the bidder already had it. They are the main reason the completion rate is high.
- **Scott Technology**: in scope (JBS went to at least 50.1%) but an unusual structure, priced below the market, with the binding date unconfirmed.

Missing deals: I checked the candidates file and found no deal that obviously should have been included. A fresh search for missing deals was not finished, because the shared web search limit ran out partway through. Worth a follow-up: whether any binding Tourism Holdings deal followed the non-binding offers noted at 25 Aug 2026, any NZX takeover notice or SIA after the builder's run, and the roughly 40 register entries marked "excluded without full check".

## Base rates

| | Before | After | After, excluding the nine buy-outs |
|---|---|---|---|
| Rows | 46 | 46 | 37 |
| Completed | 37 of 46 (80.4%) | 37 of 46 (80.4%) | 28 of 37 (75.7%) |
| Median days to outcome, all rows with a date | 117 (45 rows) | 119 (46 rows) | 123 |
| Median days, completed deals | 116 | 117 | 123.5 |
| Rival bid | 7 | 7 | 7 |
| Price raised | 10 | 10 | 8 |

The corrections barely move the base rates. Median days rise by one to two days, because Nuplex now has a date and SLI's is later. Completion, rival bid and price-raise counts don't change. The scope decision has more effect than any correction: dropping the controlling-holder buy-outs takes the completion rate from 80% to 76% and the median from 119 to 123 days.

## A note on NZX dates

NZX announcement pages show UTC times. A release at 8:30am New Zealand time appears on the page as the evening before. I saw this on the Tower termination (shown as 6 Nov, released 7 Nov New Zealand time), Abano 2020, Z Energy and MHM. Where a row's date came from an NZX page, it is worth checking against the register.
