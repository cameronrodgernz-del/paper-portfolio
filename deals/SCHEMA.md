# Deal database: schema and rules

One row per control transaction for an NZX- or ASX-listed target. A revised offer from the same bidder stays in the same row (initial and final prices). A rival bidder gets its own row, linked through `related_deal_ids`.

## What counts
- Schemes of arrangement and full takeover offers that would give the bidder control, plus partial offers for control (over 50%).
- Counted from the first binding announcement: a signed scheme implementation agreement or deed, a takeover notice (NZ), or a bidder's statement or announced intention to bid (AU). Non-binding indicative proposals don't count on their own. If one later becomes binding, the row starts at the binding date, and the first non-binding approach date goes in `first_approach_date`.
- NZ: every deal with target equity value at the offer price of NZ$20m or more.
- AU: every deal with target equity value at the offer price of A$100m or more.

## Columns (CSV, UTF-8, comma-separated, header exactly as below)
| Column | Meaning |
|---|---|
| deal_id | NZ-YYYY-NN or AU-YYYY-NN (year of binding announcement, two-digit sequence) |
| market | NZX or ASX |
| target_name | Listed target |
| target_ticker | Exchange code at the time |
| bidder_name | Bidder (and consortium members) |
| bidder_type | trade, private_equity, infrastructure, consortium, existing_holder, other |
| bidder_country | Country of the ultimate bidder |
| structure | scheme, full_takeover, partial_takeover |
| consideration_type | cash, scrip, mixed |
| currency | NZD, AUD, USD |
| first_approach_date | First public non-binding approach, if any (YYYY-MM-DD) |
| announce_date | Binding announcement date (YYYY-MM-DD) |
| undisturbed_price | Price the target or bidder used as undisturbed, per share |
| undisturbed_basis | e.g. "close 12 Mar 2025" or "1-month VWAP to 12 Mar 2025" |
| offer_price_initial | Offer per share at announce_date, cash-equivalent (state scrip basis in notes) |
| offer_price_final | Final offer per share paid or last offered |
| premium_pct_announced | Premium as stated in the announcement, % |
| equity_value_m | Target equity value at the initial offer, millions of `currency` |
| regulators | Semicolon list from: OIO, ComCom, FIRB, ACCC, overseas_competition, overseas_foreign_investment, gaming_or_sector_regulator, other, none |
| shareholder_vote | Y or N |
| court_approval | Y or N |
| financing_condition | Y or N |
| due_diligence_condition | Y or N |
| min_acceptance_pct | Takeovers only: minimum acceptance condition, % |
| break_fee_m | Target break fee, millions of `currency` |
| board_recommendation | unanimous_for, majority_for, against, neutral, none |
| ier_name | Independent adviser or expert |
| ier_low | IER value range, low, per share |
| ier_high | IER value range, high, per share |
| ier_verdict | e.g. "fair and reasonable", "not fair but reasonable", "within range" |
| pre_bid_stake_pct | Bidder's stake before the deal, % |
| intentions_pct | % of shares with stated voting or acceptance intentions or lock-ups in favour |
| blocking_holders | Holders big enough to block, with %, as stated in filings |
| booklet_date | Scheme booklet or target statement date |
| meeting_date | Scheme meeting date |
| court_date | Final court approval date |
| implementation_date | Implementation or final payment date |
| outcome | completed, terminated, withdrawn, lapsed, superseded_by_rival, pending |
| outcome_date | Date the outcome became final |
| failure_reason | For failed deals: vote, regulator, rival, financing, material_adverse_change, bidder_walked, other (with a short note) |
| rival_bid | Y or N |
| price_raised | Y or N |
| days_to_outcome | outcome_date minus announce_date, in days (leave blank if pending) |
| related_deal_ids | Semicolon list of linked rows (rival bids, re-bids) |
| sources | Semicolon list of URLs actually opened, primary filings first |
| notes | Anything a reader needs: scrip basis, special dividends inside the price, uncertainties |

## Rules
- Primary sources first: NZX or ASX announcements, scheme booklets, target statements, bidder's statements, Takeovers Panel records, regulator decisions. A news story is only a pointer to the filing.
- Never guess. A field you can't find stays blank, and the gap goes in `notes`.
- Prices are per share in the deal currency. A special dividend paid as part of the price is included in the offer price, with a note.
- Dates are YYYY-MM-DD.
- Every row lists the URLs it was built from.
