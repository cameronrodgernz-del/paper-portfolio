# <Company> (<EXCHANGE>:<TICKER>): deep dive

Written <YYYY-MM-DD> by the research desk. Price at writing: <price> (<date of close>). Market value: <value> (shares on issue <n>, source).
Status: TO WRITE (remove this word once the file is finished; decide.py refuses a draft)
Fact sheet: research/facts/<TICKER>.md (NZ_<TICKER>.md for NZX), grade <A or B>, and the question it set.

Written for the one-company-at-a-time process (rulebook section 5a, from 9 Nov 2026). This is the case for buying.
A second model writes the case against without seeing this file (research/against/), then the two are argued out in
research/debate/, which ends with Cam's decision. The resolve date may be up to 36 months out; dated events are optional.
The value test: the bad case no more than 30% below the price, and the middling case above it by at least 1.5 times the
bad case's fall, never less than 15%. Special situations skip the value test.

Order of work (added 2 Nov 2026): write "What the filings show" and "Valuation" before looking at the share
price or the market value, so the value comes from the business and not from the price. Fill in the price,
"Why the market is wrong" and "Outcomes and chances" last.

## What the price assumes
Written first, from today's price: what profit, growth, margin or asset value the market is paying for,
worked backwards with the arithmetic shown, and how that compares with the company's own history and plans.

## The one thing the market is missing
One sentence, then the evidence for it. For example: "underlying profit is $X once last year's one-off is taken
out", or "the land is carried at $Y but similar land has sold for $Z". If after the full deep dive this sentence can't
be written, the company is a reject: say so here and stop.

## The test outside the filings
The evidence from outside the company's own filings that tests the one thing the market is missing: what was
collected (competitor or supplier filings, industry data, tracked prices, stock or job ads, conversations), when, and what it
showed. If the case rests only on what everyone covering the company reads, say so plainly.

## The company in plain words
What it does, where the money comes from, who runs it, who owns it (the top 20 holders and any substantial
holders, from the annual report and the register), and how it has done over five years. Short, plain, factual.

## Why big investors may be overlooking it
Size, liquidity, index membership (not in the S&P/ASX 300, or outside the NZX 20), analyst coverage you can
find, register concentration, a recent listing or demerger, a messy history, a sector out of favour. Say
which of these apply and how you know.

## What the filings show
From the primary sources only: the last two annual reports and the latest half-year, the ASX or NZX
announcements of the last two years, the company register (Companies Office or ASIC), substantial holder
notices, director dealings, regulator records, court records where relevant. Revenue, profit, cash flow,
balance sheet (net cash or debt, assets at book and any evidence of their market value), capital
raisings and their prices, dividends, and anything a quick reader would miss. Cite each fact.

## Valuation
At least two methods that suit the business (for example: earnings or cash flow multiple against named
listed peers; net assets or sum of the parts; a simple discounted cash flow with every input stated).
Show the arithmetic. End with a range of values per share and the main thing each depends on.
Done without the share price in view: the range is what the business is worth, worked from the filings.

## The players and what the rules allow (special situations only)
For a special situation pick (rulebook section 5a): every party that could move the price (bidders past and present,
holders over 5%, the board or responsible entity, a parent, a court or regulator), each with its stake, the date and
price of every change in two years, what it paid and carries the stake at, and what it can afford; what the rules let
each do and when (3% creep every six months, the 20% threshold, 90% compulsory acquisition, removing a responsible
entity, schemes, approvals); and comparable cases with what holders received. The bad outcome's price is the value if
nothing happens. Leave this section out for an ordinary research pick.

## Why the market is wrong
One or two plain reasons the price is below the value, and why that should change. If you can't say why
the market is wrong, there is no trade.

## Outcomes and chances
| Outcome | What happens | Chance | Price by resolve date |
| --- | --- | --- | --- |
| Bad | ... | ..% | ... |
| Middling | ... | ..% | ... |
| Good | ... | ..% | ... |
Chances add to 100%. These go on the card exactly as written here. Each outcome's price comes from the
valuation range above (what the market would pay for the business in that outcome by the resolve date), not
from today's price plus or minus a step. Say which valuation figure each one uses.
Dividends (rulebook section 5a, from 8 Nov 2026): add to each outcome's price the dividends and distributions that go
ex before the resolve date, at what that outcome's own earnings and cash would pay (cut or stopped in the bad case where
its earnings, borrowing or payout policy would; a payment funded by borrowing or asset sales only if the price carries
the extra debt). Show the price and the dividends separately, e.g. "A$2.12 (A$1.87 price plus 25c)". The value pick
legs and the expected gain use the total.
Then the expected price, the round-trip costs, and the expected gain after costs against the minimum (rulebook section
5a, from 8 Nov 2026): the cash rate plus 5% a year over the days to the resolve date. A case below the minimum is not
a case for review, whatever the gap.

## Dated events
Optional from 9 Nov 2026. The results, meetings and other events in the holding period that should show whether the
case is right, each with its date or expected date. The resolve date is at most 36 months out.

## What would make this wrong
The two or three things that would break the case, and the exit rule: the specific fact that would show the reason for
buying is wrong, which is when the pick is sold (rulebook section 5a). A 25% fall from the buy price means a review, not a sale.

## Checks
- Not on Cam's excluded list (config/judgement_excluded.csv).
- No placement-pattern reopening in the last 30 sessions (rulebook section 9).
- Liquidity: median daily traded value, and the most the position can be under section 3 (five sessions at 10% for research picks).

## Sources
Every document used, with its link: annual reports, announcements, registers, regulator pages.
