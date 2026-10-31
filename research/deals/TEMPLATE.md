---
ticker: XXX
market: ASX            # or NZX
deal_id: AU-2026-NN    # from the brief if known, else blank
target: Full listed name
bidder: Bidder and who is behind it
structure: scheme      # scheme, full_takeover, partial_takeover
consideration: Exact terms per share, including any permitted or special dividends inside the price, scrip ratios, elections, caps and scale-back
cash_per_share:        # number, cash leg only, in currency below
scrip_ratio:           # number of acquirer shares per target share, 0 if none
acquirer_ticker:       # exchange code of the scrip, if any
currency: AUD
announce_date: YYYY-MM-DD
booklet_date: YYYY-MM-DD        # scheme booklet / target's statement registered or despatched; blank if not yet
first_court_date: YYYY-MM-DD
meeting_date: YYYY-MM-DD        # scheme meeting; for a takeover, blank
offer_close_date: YYYY-MM-DD    # takeovers only
second_court_date: YYYY-MM-DD
effective_date: YYYY-MM-DD
record_date: YYYY-MM-DD
implementation_date: YYYY-MM-DD # the date holders are paid, as currently scheduled
end_date: YYYY-MM-DD             # sunset / end date in the implementation deed
dates_basis: Which of the dates above are confirmed and which are indicative
stage: announced               # one of: announced, booklet_out, vote_passed, court_approved, unconditional, implemented, terminated
vote_threshold: e.g. 75% of votes cast and a majority by number of holders voting
bidder_stake_pct:
intentions_pct:                # % of shares with stated intentions or lock-ups in favour
blocking_holders: holders big enough to matter, with %
board: e.g. unanimous, in the absence of a superior proposal and subject to the expert
ier: Expert name, value range per share, verdict (or "not yet released")
break_fee: target pays; amount
reverse_break_fee: bidder pays; amount
regulators: list each approval needed and its current status
conditions_open: semicolon list of conditions still outstanding
conditions_met: semicolon list of conditions already satisfied or waived
ticking_fee: if any
last_checked: YYYY-MM-DD
---
## In short
Three to five plain-English sentences: what the deal is, where it's up to, and the one or two things that decide whether holders get paid and when.

## Conditions
One line per condition precedent: what it is, its status, the evidence and the date.

## Key dates
Each date with whether it's confirmed or indicative, and the source.

## Risks to completion
Each specific risk with a rough chance it stops or delays the deal, and what would move that chance. Include competing-bid prospects (which help a holder) separately from break risks.

## Recent announcements
The last few relevant announcements, dated, one line each.

## Sources
Every URL actually opened, primary sources first (ASX or NZX announcements, the scheme booklet, the independent expert's report, the implementation deed, regulator registers such as ACCC mergers register, FIRB, NZ OIO decisions, NZ Takeovers Panel), then any secondary sources clearly marked as secondary.
