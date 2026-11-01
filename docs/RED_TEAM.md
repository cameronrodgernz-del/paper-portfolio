# Red team checklist for a deal card

The red team is a separate agent that has not seen the analyst's reasoning. It gets the card, the
deal file (research/deals/<TICKER>.md) and the deal monitor's row, and argues against the entry. It
works through every heading below, says which apply, and for each one that does, gives its own
chance of the deal failing or slipping on that ground, with the evidence. It ends with the three
points most likely to make the card wrong, and a plain verdict: agree, enter smaller, wait for a
named event, or don't enter.

## 1. Is the price really mispriced?
- The break price: is the undisturbed price, moved by the market, a fair floor? Sector moves since
  the announcement (gold, lithium, rates for property, credit for financials) can put it well above
  or below. Peers' moves are evidence; say which.
- For scrip deals: the offer moves with the acquirer. Is the spread a spread, or the acquirer's
  share price falling? Could the acquirer be the one in trouble?
- Is there a reason the market knows something the card doesn't: a large holder selling, short
  interest, an options market, a recent announcement read the wrong way?

## 2. Approvals
- ACCC: informal review or the mandatory regime (from 1 Jan 2026)? Phase, statutory timeline,
  market overlap, past ACCC views on this industry.
- FIRB: foreign government investors, national security land or sectors, tax conditions, extensions.
- NZ: OIO (sensitive land, significant business assets, timeframes) and Commerce Commission
  clearance or authorisation.
- Overseas: US HSR, CFIUS, EU, China SAMR, Brazil or other national approvals; sector regulators
  (APRA, ASIC, gaming regulators, the RBNZ).
- What happens at the end date if an approval is late: can either side walk?

## 3. The vote (schemes)
- 75% of votes cast and a majority by number of holders voting (the headcount test can be split or
  manipulated). Who can block: holders at or near 25% of likely turnout?
- Stated intentions and lock-ups, and whether they fall away for a superior proposal.
- Retail-heavy registers with low turnout; a register that turned over to arbitrage funds.
- Independent expert: fair and reasonable, or only reasonable? Is the price inside their range?

## 4. The bidder
- Financing: committed debt, equity commitment letters, conditions in them.
- The bidder's own position: its share price, its holders' vote if needed, a takeover of the bidder
  (as with Ingenia while bidding for Peet), management change, strategy reversal.
- Private equity: fund life, a reverse break fee as the only remedy (an option to walk).

## 5. The target
- Material adverse change and prescribed occurrence clauses: what counts, recent trading updates,
  earnings downgrades, litigation, key contracts with change-of-control clauses.
- Permitted dividends and franking: is the dividend part of the price, and is it paid before
  the record date?

## 6. Timing
- Days to payment drive the yearly return. Are the dates in the deal file confirmed or indicative?
  What do past deals with the same approvals take (reports/deal_odds.md)? Is there a ticking fee?
- A slip of three months on a thin spread can turn the trade below the cash rate.

## 7. A better bid
- Is there a rival, a blocking stake, or a strategic holder who might bid? A rival helps a holder,
  but a bidding contest can also lengthen the timetable or break the original deal.

## 8. The card itself
- Are the outcomes and chances consistent (chances add to 1; the break price matches the deal file)?
- Does the card's chance differ from the base rate by more than the written adjustments justify?
- Does the stake keep the loss on a break within 1% of the portfolio at the deal file's break price?
- Industry and group labels: right, and within the 15% and 10% limits with orders already waiting?

# Red team checklist for a research pick (rulebook section 5a)

The red team is a separate agent that has not seen the analyst's reasoning beyond the deep dive itself. It
gets the deep dive (research/picks/<TICKER>.md) and the draft card, checks the facts against the primary
sources it cites, and argues against buying. It writes research/red_team/<TICKER>.md, working through the
headings below, and ends with the three points most likely to make the pick wrong and a section
"## Verdict": proceed, proceed smaller, wait for a named event, or don't buy.

## 1. Are the facts right?
- Re-open at least five of the cited sources and check the numbers the case rests on: revenue, profit,
  cash, debt, shares on issue, assets and what they're worth, the dividend.
- Anything left out: a capital raising, a large holder selling, a director leaving, a lawsuit, a
  regulator, a customer or contract loss, related-party dealings, auditor qualifications.

## 2. Is it really overlooked, or is it cheap for a reason?
- Who owns it and who is selling. A falling price with heavy volume is someone who knows the company.
- Industry trouble that peers' prices already show. Debt that falls due before the dated events.
- Management's record against its own past guidance.

## 3. The valuation
- Are the peers really comparable? Are the multiples applied to normal or peak earnings?
- Net assets: book values against evidence of what they would fetch; who would buy them.
- The discounted cash flow: which single input moves the answer most, and is it reasonable?

## 4. The dated events and the exit
- Will the event actually show the market is wrong, or could it come and go without the price moving?
- Liquidity: can the position be sold in a bad week at our size?

## 5. The stated chances
- Are the bad, middling and good chances honest? Give your own, and say where you differ and why.
