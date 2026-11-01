# <Company> (<EXCHANGE>:<TICKER>): deep dive

Written <YYYY-MM-DD> by the research desk. Price at writing: <price> (<date of close>). Market value: <value> (shares on issue <n>, source).
Status: TO WRITE (remove this word once the file is finished; decide.py refuses a draft)

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

## Why the market is wrong
One or two plain reasons the price is below the value, and why that should change. If you can't say why
the market is wrong, there is no trade.

## Outcomes and chances
| Outcome | What happens | Chance | Price by resolve date |
| --- | --- | --- | --- |
| Bad | ... | ..% | ... |
| Middling | ... | ..% | ... |
| Good | ... | ..% | ... |
Chances add to 100%. These go on the card exactly as written here.

## Dated events
The events expected to show the market is wrong (results, a contract, a regulator decision, a sale
process, a debt refinancing), each with its date or expected date. The card's resolve_by date is the last of them.

## What would make this wrong
The two or three things that would break the case, and the exit rule.

## Checks
- Not on Cam's excluded list (config/judgement_excluded.csv).
- No placement-pattern reopening in the last 30 sessions (rulebook section 9).
- Liquidity: median daily traded value, and the most the position can be under section 3.

## Sources
Every document used, with its link: annual reports, announcements, registers, regulator pages.
