# Cash Converters International (ASX:CCV): deep dive. Not a value pick. Wait for the 1H27 result (about 23 February 2027)

Written 2026-11-08 by the research desk. Price at writing: A$0.265 (last trade on 6 November 2026, bid A$0.265, offer A$0.27; ASX company data fetched 7 November 2026 UTC [M1]; Norgate's last close in the repo is also A$0.265, on 30 October [M2]). Market value: A$189.9m (716,585,333 shares on issue [M1]: 711,522,934 at 12 August [C1] plus 5,062,399 issued under the dividend reinvestment plan at A$0.27 on 7 October [C11]).
Status: finished. Verdict: wait for a named event, the 1H27 result due about 23 February 2027, with the AGM on 19 November 2026 (and its likely first-quarter trading update) as the first read. The exact conditions that reopen or close it are under "Dated events". At A$0.265 there is no case: the expected price by 5 March 2027 is A$0.263, -0.9% before costs and about -3.8% to -5.2% after them, against a minimum of +2.3%. Watch trigger A$0.245 (a close at or below it with nothing else changed). No card, not sent to the red team. This is a simulation and not financial advice.
Fact sheet: research/facts/CCV.md (8 November 2026), grade B. The question it set: was 2H26's lower operating profit (A$10.0m against A$13.2m in 1H26) the up-front loss provisions on the fast-growing Cashies Loan book, which turn into profit as the loans mature, or worse loans? "Our way" A$0.346 (1H26 profit run-rate, 15% return on tangible equity, priced like Credit Corp), "against us" A$0.205.

Value pick (rulebook section 5a, from 8 Nov 2026): it doesn't qualify. Valued over 24 months (to after the FY28 result in August 2028), my bad case is A$0.194, 27% below the price, against the 10% the rule allows; the middling case is A$0.311, 17.5% above, which would pass the 15% test on its own. This is a lender growing a new unsecured book fast while the RBA raises rates, so the bad case sits a long way down. It would only qualify at A$0.215 or below. As an ordinary pick, the dated events inside six months are the AGM (19 November 2026) and the 1H27 result (about 23 February 2027).

Order of work. The fact sheet shows a price, so a price was in view before this file was started. "What the filings show" and "Valuation" were worked from the company's filings, the peers' published figures and multiples, and CCV's own past multiples at its result dates; no figure in them was set by reference to today's price. The price, "Why the market is wrong" and the outcomes were written last. Arithmetic in python3 -I (scratchpad scripts model.py, forward.py and outcomes.py), shown in the text.

> In short. Liquidity passes: A$108,903 a day (20-session median to 30 October). The answer to the fact sheet's question is "mostly neither". Of the A$3.7m fall in operating profit before tax from 1H26 to 2H26, the largest single cause was lost interest on the old loan books being run off (personal loan interest down A$3.9m and vehicle loan interest down A$1.5m half on half) [C1][C5]. Faster up-front provisioning on Cashies was about A$2.6m of it, and net write-offs rose A$1.4m, partly offset by bigger releases on the shrinking old books; the six-month net loss rate went up from 5.3% to 6.0% (my arithmetic; the company gives only the first half). And the provisions did not hold FY26 profit down at all: the loss allowance fell by A$10.1m over the year, because the old books shrank faster than Cashies grew, and that release added to profit [C1]. In FY27 the old books are small (A$72.8m at June, and the NZ personal loans were sold in July), so the release largely stops while Cashies keeps growing. My central FY27 operating profit is about A$19m (2.6c a share), below FY26's A$23.2m and below the two brokers' 3.2c and 3.8c [S1]. FY28 is the year it can recover (central 3.8c), as the old books are gone and Cashies' growth slows. The fact sheet's A$0.346 uses the 1H26 rate, which included about A$34m of half-year income from books now nearly gone and a A$5.6m provision release: it is a good case for FY28, not something the 1H27 result can show. On two methods the business is worth about A$0.17 to A$0.36 a share, central A$0.274, close to the A$0.265 price.

## The company in plain words
Cash Converters runs second-hand goods stores that also lend against goods left with them (pawnbroking), and a separate unsecured personal loan business. At June 2026 it owned 200 stores (124 in Australia, 10 in New Zealand, 66 in the UK) and collected fees from 164 franchise stores in the same three countries, plus master franchise fees from 283 stores in Europe, southern Africa and Asia [C2][C3, pp. 3 and 27].

Where the money comes from in FY26 (year to 30 June 2026), A$m [C1, note 3]:
- Retail sales 240.5 (cost of goods 135.9);
- Pawnbroking and buyback fees 78.7;
- Personal loan interest and fees 76.9, vehicle loan interest 8.7;
- Franchise fees 14.6, other 8.9.
Total revenue 429.2. The lending is now one product, the Cashies Loan: a line of credit from A$2,050 to A$10,000, repaid over up to 36 months a draw, priced from 19.95% a year, launched nationwide in October 2025 [C2][C3, p. 2][C7]. Payday loans (small amount credit contracts) stopped being written on 30 September 2025, medium amount loans are also running off, vehicle loans stopped in June 2024, and New Zealand personal lending stopped in April 2026 [C1, note 2].

Who runs it: Sam Budiselik, CEO and managing director; Timothy Jugmans chairs the board (he is EZCORP's chief financial officer); Lachlan Given, EZCORP's chief executive, is a director; Peter Cumins, with the company since 1990, is executive deputy chairman and retires on 30 June 2027 [C1][C13].

Who owns it: EZCORP Inc (a US pawn operator) holds 309,735,956 shares, 43.53%, the only substantial holder. Then Citicorp Nominees 2.99%, J P Morgan Nominees 2.99%, BNP Paribas Nominees 2.96%, FiftyFive Capital Investco 1.49% (the managing director's holding), Bond Street Custodians (Salter) 1.30%, and Peter Cumins's super fund 0.97%. The top 20 hold 64.15%; there are 3,834 holders [C1, shareholder information].

Five years [C1, remuneration report; M2]:

| Years to 30 June | FY22 | FY23 | FY24 | FY25 | FY26 |
| --- | --- | --- | --- | --- | --- |
| Revenue (A$m) | 245.9 | 302.7 | 382.6 | 385.3 | 429.2 |
| Statutory profit after tax (A$m) | 11.2 | -97.2 | 17.4 | 24.5 | 19.7 |
| Operating profit after tax (A$m) | | | 20.9 | 25.1 | 23.2 |
| Dividends (cents) | 2.0 | 2.0 | 2.0 | 2.0 | 2.0 |
| Share price at 30 June (cents) | 23.0 | 22.5 | 22.0 | 28.0 | 30.0 |

The dividend has been 1.0c a half for every half since FY22, including the FY23 year of a A$97.2m loss [C1]. Operating profit for FY24 and FY25 is from the FY25 AGM deck [C7]. The share has traded between A$0.14 and A$0.35 for seven years (Norgate month ends since 2019 [M2]).

## Why big investors may be overlooking it
- Size and float: A$190m, with EZCORP holding 43.5%, so the free float is about A$107m, and the top 20 hold 64% [C1].
- Index: not in the S&P/ASX 300 now; it was a member at the start of Norgate's 2010 history (data/norgate/index_members.csv).
- Trading: A$108,903 a day (median, 20 sessions to 30 October 2026 [M2]), too small for most funds.
- Sector: payday lending sits on many funds' exclusion lists. The payday exit (now 2.4% of the book [C2]) may change that over time.
- Coverage: thin, not none. FNArena (a secondary source) lists Bell Potter (Buy, A$0.35 target, FY27 EPS 3.8c, FY28 4.8c, 25 August 2026) and Shaw and Partners (Buy, A$0.41, FY27 3.2c, FY28 4.7c, 26 August 2026), plus a restricted Research as a Service note [S1][S2].
- History: the FY23 loss of A$97.2m [C1], past remediation programs over its lending and current requests for information from regulators (the contingent liabilities note says there were matters where it was "providing information requested by regulators" [C1, note 16]), and a controlling-sized holder with two board seats including the chair.

Size, float, index, liquidity and sector all apply. The plainer reason it is cheap is visible in the filings: profit is falling while the lending book is replaced, and the rate cycle is against it.

## What the filings show

### The halves, and where 2H26 went
Operating figures exclude A$3.5m after tax of transition and acquisition costs in FY26 [C2]. Since FY26 the company counts interest on its securitisation facility inside net financial services revenue, so "operating EBITDA" is after that interest [C2, note 5]. Second halves are the full year less the first (model.py).

| A$m | 1H26 | 2H26 | Change |
| --- | --- | --- | --- |
| Net store revenue (sales less cost of goods) | 49.5 | 55.1 | +5.6 |
| Net financial services revenue | 74.8 | 75.7 | +0.9 |
| of which personal loan interest and fees | 40.4 | 36.5 | -3.9 |
| of which vehicle loan interest | 5.1 | 3.6 | -1.5 |
| of which pawnbroking and buyback fees | 35.8 | 42.9 | +7.0 |
| of which securitisation interest (a cost) | 5.3 | 5.6 | -0.3 |
| (the rest: other financial services revenue less other financial services costs) | | | |
| Net other revenue (franchise fees, webshop, other) | 10.8 | 7.9 | -2.9 |
| Employee and other costs | 93.8 | 96.5 | -2.7 |
| Bad debts and loss allowance | 7.1 | 9.4 | -2.4 |
| Operating EBITDA | 34.2 | 32.8 | -1.4 |
| Depreciation and amortisation | 10.7 | 13.1 | -2.4 |
| Finance costs (leases, UK and term debt) | 4.7 | 4.6 | +0.1 |
| Operating profit before tax | 18.8 | 15.1 | -3.7 |
| Operating profit after tax | 13.2 | 10.0 | -3.2 |

Sources: 1H26 from the 1H26 deck [C6, p. 9] and interim report [C5, notes 3 and 4]; FY26 from the FY26 deck [C3, p. 23] and annual report [C1, notes 3 and 4]. The first half's net other revenue included about A$1.6m of "other revenue" that didn't recur (A$1.9m in 1H26 against A$0.3m in 1H25 and A$0.7m in 2H26) [C5][C1].

By segment, operating profit before tax went from 1H26 to 2H26 [C5, note 2][C1, note 2; non-operating costs added back]: Personal Finance A$8.2m to A$1.2m; Vehicle A$4.1m to A$1.7m; Australian stores A$13.1m to A$15.2m; UK A$5.0m to A$6.2m; New Zealand A$0.3m to A$1.7m; head office minus A$11.9m to minus A$11.0m.

### The answer to the fact sheet's question
Of the three parts of the fall in lending profit:
1. Lost interest on the old books, the biggest. Personal loan and vehicle interest fell A$5.4m half on half. Payday lending stopped on 30 September 2025, and the old books (payday, medium loans, vehicle, NZ) went from A$182m at June 2025 to A$72.8m at June 2026 [C3, pp. 11 and 24][C6, p. 10]. Cashies grew from A$23.1m to A$58.2m in the first half and to A$114.1m in the second [C4][C2]. Solving the two halves together, the old personal loans earned about 57% a year and Cashies about 40% a year on their average balances (model.py; a derived estimate, not a disclosed figure). So each dollar of old loan running off took more revenue with it than a dollar of Cashies added.
2. Up-front provisions, the second. In FY26, A$124.5m of new loans in Personal Finance and store lending were booked with A$15.1m of loss allowance, 12.1% [C1, note 7.c]. At that rate Cashies' growth needed about A$4.2m of new allowance in the first half and A$6.8m in the second: A$2.6m more. Bad debts rose A$2.4m in total, because larger releases on the shrinking old books offset part of it.
3. Worse loans, a little. Net write-offs (written off less recoveries) were A$12.6m in 1H26 and A$14.0m in 2H26; recoveries from debt sales fell from A$6.7m to A$5.9m [C5, note 4][C1, note 4]. On the company's own definition the six-month net loss rate was 5.3% in 1H26 [C6, p. 5] and, by the same arithmetic, 6.0% in 2H26 (A$14.0m over an average gross book of A$233.6m). The half-year rates the year before were 7.3% and 8.5% [C9, p. 10]. So losses are lower than a year ago but rose in the second half, which fits management's own warning that loss rates are "at lower range, likely to normalise as growth continues" [C6, p. 5].

Other signs on credit quality point both ways [C1, note 7.c]. In Personal Finance and store lending, loans in stage 2 (a significant rise in credit risk since they were written) rose from A$35.8m (22% of A$166.5m) to A$50.0m (27% of A$182.3m), while stage 3 (credit-impaired) fell from A$38.7m to A$28.9m and loans 31 to 90 days past due fell from A$10.3m to A$7.3m. A A$5.5m release from "changes in PDs/LGDs/EADs" (the model's default and loss assumptions) helped FY26.

So the fact sheet's premise needs turning round. Up-front provisions did not hold FY26 profit down. The total loss allowance fell from 17.1% of the gross book to 13.7%, and the year's charge included a net A$10.1m release (A$5.6m in the first half, A$4.5m in the second): the charge was A$16.5m against net write-offs of A$26.6m [C1, note 4 and OFR p. 13][C5]. That happened because the old books, carrying high allowances, shrank faster than Cashies grew. In FY27 the old books are much smaller (and the NZ book was sold in July [C1, note 18]), so the offset mostly goes while Cashies keeps growing. The provision "turning into profit as the loans mature" is real only in the sense that once growth slows, the annual charge drops back to the write-offs. That is an FY28 effect.

### Two things a reader of the segment table would miss
- Commission inside the group. Personal Finance pays the corporate stores a commission on loans they originate, shown as "transactions with other segments": A$15.8m in FY26 (A$12.1m in FY25), A$6.4m in 1H26 and A$9.4m in 2H26 [C1, note 2][C5, note 2]. The auditor's key audit matter on goodwill names "forecast loan volumes driving revenue from commissions to corporate stores" [C1, auditor's report]. So A$15.8m of the Australian stores' A$46.8m operating EBITDA is lending money moving inside the group. Counting the commission back into lending, Australian lending (Personal Finance plus Vehicle) made A$18.7m before tax in 1H26 and A$12.2m in 2H26, A$31.0m for the year; everything else (stores net of commission, UK, NZ, head office) made A$0.1m and A$2.8m. Head office (franchise fees less central costs) lost A$23.0m before tax on an operating basis [C1, note 2]. The fact sheet's "store profits now carry the group" overstates it.
- The New Zealand personal loans were sold on 20 July 2026 to Pioneer Credit Solutions, 5,370 loans with a face value of NZ$11.66m, for NZ$10.67m cash, about A$8.9m [C1, note 18; FX data/fx/fx_daily.csv]. The NZ loan book was A$9.56m gross and A$7.80m after allowance at June [C1, note 7.c]. So 1H27 probably carries a one-off gain of around A$1m, and NZ lending income ends.

### Funding, cash and what is committed
- Securitisation (Fortress): limit A$173.25m, A$114.0m drawn, A$59.25m undrawn at June; effective cost 11.3% (12.1% in FY25); drawing period ends 27 August 2027, repayable by 27 August 2028; minimum draw cut permanently to A$90m on 17 February 2026 [C1, note 7.e]. Interest on it was A$10.9m in FY26 (A$5.3m and A$5.6m by half) [C1][C5]. The facility funds about 63% of the loans pledged to it (A$114.0m drawn against A$179.8m of Personal Finance and vehicle loans). Management lists "funding cost reduction with future securitisation facility refinancing" as a priority [C2].
- UK bank debt: term loan A$11.2m and a A$7.7m revolver (A$6.5m drawn) at 7.9% [C1, note 7.e].
- Cash A$37.2m: A$3.9m restricted, A$6.0m is cash held in stores, and Fortress requires at least A$10m of unrestricted cash in the Australian companies [C1, note 7.a]. So about A$17m is free, plus the A$8.9m NZ sale in July.
- Committed or planned for FY27: 20 or more franchise store purchases (A$1.2m a store in Australia, A$0.7m in the UK, at 4 to 5 times EBITDA) and 10 new stores a year [C3, p. 18]; the equity share of Cashies' growth (about 25% of each dollar of new loans after the facility and the loss allowance); dividends of about A$14.3m a year less the reinvestment plan (about A$1.4m was reinvested in October [C11]). The old books release capital as they run off (about A$16m of equity in the Australian old books plus the A$8.9m NZ sale), which roughly pays for Cashies' equity need over two years.
- FY26 cash: operating cash flow A$33.5m after a net A$9.1m more lent; less A$13.2m of equipment and software and A$13.9m of lease payments leaves A$6.4m, against A$12.8m of dividends paid. The A$51.4m of store purchases came from the A$24.1m equity raising and cash, which fell A$36.0m [C1, cash flow]. So the FY26 dividend was not covered by cash after leases and loan growth.
- Franking credits A$78.3m [C1].

### Who owns it and who is moving
- EZCORP: 43.53%, unchanged apart from its full take-up in the November 2025 raising at A$0.305; no substantial holder notice in two years [C1][C14]. With the chair and one other director it is the natural buyer of the rest, but there is no sign of an approach.
- Directors: Peter Cumins sold 350,000 shares on market at A$0.31 to A$0.33 on 2 to 5 March 2026 (about A$110,000), keeping 3,023,468 direct and 6,937,226 in his super fund [C12]; he retires on 30 June 2027 [C13]. No director has bought on market in the last 12 months (entitlement shares and vesting rights don't count) [C14].
- Related parties: a A$6.4m four-year sponsorship of Perth Bears Limited, of which Cumins is a director (A$0.3m paid in FY26); A$120,000 a year of consulting to an entity controlled by Mr P Cohen, EZCORP's beneficial owner; the Perth City franchise store bought from a Cumins-related party for A$365,000 [C1, note 19.c].
- AGM business on 19 November 2026: re-election of Lachlan Given and Mark Ashby, the remuneration report, up to 3,572,644 performance rights for the CEO (valued at A$0.2939, the five-day average price after the FY26 result; half on an undisclosed three-year EPS target, half on relative shareholder return), and a rise in the directors' fee pool from A$1.0m to A$1.3m [C8].

### Guidance and record
No profit guidance. The FY26 deck sets FY27 as "investment and scale" and FY28 onward as "earnings growth", and says of Personal Finance: "Earnings to rebuild in FY27" [C3, pp. 6, 15 and 26]. Last year's AGM gave a first-quarter trading update (revenue by segment, the Cashies book at 31 October) and said the first-half Personal Finance result would be below the prior year [C7]; it was (A$8.2m against A$12.3m [C5]). CCIG, 29 stores bought for A$37.1m at 4.5 times FY25 EBITDA, is forecast to add to EPS in its first full year, FY27 [C10].

### What a quick reader would miss
1. FY26's bad debt charge was cut by a A$10.1m net release of loss allowance; that offset mostly ends in FY27.
2. 2H26's fall was mainly lost interest on old books, not provisions.
3. The six-month net loss rate rose from 5.3% to 6.0% in 2H26; stage 2 loans rose to 27% of the Personal Finance and store book.
4. A$15.8m of the Australian stores' EBITDA is commission from the group's own lending business.
5. The NZ personal loans were sold in July: a likely one-off gain in 1H27, and no more NZ lending income.
6. The securitisation facility's drawing period ends in August 2027, while the RBA has raised five times in 2026 to 4.85% [R1].
7. The FY26 dividend was paid from more than the cash left after leases and loan growth.
8. A A$6.4m sponsorship with a company the deputy chairman is a director of.

## Valuation
Shares: about 725m on average in FY27 and 735m in FY28 (716.6m now, plus dividend reinvestment and rights). Tax 31% (FY26 operating: A$10.7m on A$33.9m [C3]). Net tangible assets A$171.6m at June, 24.1c a share (equity A$253.8m less goodwill A$54.9m and other intangibles A$27.3m, on 711.5m shares [C1]); it includes A$26.9m of deferred tax assets, as Solvar's does. Arithmetic in forward.py.

### Earnings in three cases
The approach: start from FY26 operating profit before tax (A$33.9m) and change the lending lines and the rest of the group. Australian lending (Personal Finance plus Vehicle, with the commission to stores added back) made A$31.0m before tax in FY26 on A$79.2m of interest, an estimated A$14.7m of bad debts (group A$16.5m less about A$1.3m for NZ personal loans and A$0.5m for pawn, my estimates), A$10.9m of securitisation interest and A$2.6m of depreciation and interest; that leaves about A$20.0m of running costs.

| FY27 assumption | Bad | Middle | Good |
| --- | --- | --- | --- |
| Cashies book at June 2027 (A$114.1m at June 2026) | A$185m | A$200m | A$210m |
| Cashies yield (my estimate for FY26: about 40%) | 39% | 40% | 41.5% |
| Cashies net loss rate before debt-sale recoveries | 11% | 9.5% | 8.5% |
| Loss allowance on Cashies at June 2027 (12% assumed at June 2026) | 12.5% | 12% | 11.5% |
| Old books' interest (medium loans, payday, vehicle) | A$15.4m | A$15.4m | A$15.4m |
| Old books' losses beyond their allowance | A$3.5m | A$2.9m | A$2.0m |
| Debt-sale recoveries (FY26 A$12.6m) | A$6m | A$8m | A$9m |
| Securitisation interest (FY26 A$10.9m) | A$14.0m | A$13.6m | A$13.0m |
| Lending running cost saving | A$0.5m | A$1.0m | A$1.5m |
| NZ personal lending gone (one-off gain excluded) | -A$1.5m | -A$1.5m | -A$1.5m |
| Stores, UK, NZ stores, head office, change on FY26 | +A$2.0m | +A$3.5m | +A$5.0m |

| FY27 result, A$m | Bad | Middle | Good |
| --- | --- | --- | --- |
| Australian lending interest | 73.7 | 78.2 | 82.7 |
| Bad debts (of which allowance build on Cashies) | 23.4 (9.4) | 20.1 (10.3) | 17.2 (10.5) |
| Australian lending profit before tax | 14.2 | 22.9 | 31.3 |
| Group operating profit before tax | 17.7 | 27.8 | 37.7 |
| Operating profit after tax | 12.2 | 19.2 | 26.0 |
| EPS | 1.7c | 2.6c | 3.6c |

FY28, with the old books nearly gone (A$4m of interest left) and Cashies' growth slowing (to A$215m, A$240m, A$260m), securitisation interest A$14.5m to A$15.5m and the rest of the group up A$2.5m to A$4m: operating profit after tax A$19.0m, A$27.9m and A$37.0m; EPS 2.6c, 3.8c and 5.0c.

Where the inputs come from: the yields are solved from the two halves of FY26 (model.py); the 12% allowance is the FY26 rate on new loans [C1, note 7.c]; the old books' run-off follows their FY26 pace (Personal Finance old books halved each half; vehicle fell about A$11m a half) [C1][C5]; securitisation interest assumes 63% funding at about 10.8% (FY26's effective 10.1% on average drawings plus about 0.7 points of higher bank bill rates [R1]); store growth counts a full year of CCIG (about A$2.8m more EBITDA: five more months of the A$6.7m pro forma figure [C9, p. 19][C10]), the FY26 purchases' full year, about half a year of the 20 targeted FY27 purchases, 0% to 4% same-store growth, and the loss of franchise fees and of 1H26's one-off revenue. These are my estimates, not company figures.

In the half year, the middle case gives 1H27 operating profit after tax of about A$9.5m to A$10m (Cashies to about A$160m by December, allowance build about A$5.5m, old books' interest about A$10.6m), against A$13.2m in 1H26. The NZ sale gain would add about A$0.7m after tax if the company counts it in operating profit.

The brokers' FY27 EPS (Shaw 3.2c, Bell Potter 3.8c [S1]) sit between my middle and good cases; their FY28 (4.7c, 4.8c) sit between my middle and good. My lower FY27 comes mainly from bad debts: without the FY26 release, the charge rises from A$16.5m to about A$20m to A$23m.

### Method 1: price to earnings
Multiples: CCV itself was priced at about 6.8 times operating EPS at the end of August 2024 (A$0.225 on 3.33c), 8.5 times in August 2025 (A$0.34 on 4.0c) and 8.8 times in August 2026 (A$0.285 on 3.24c) [M2][C7][C3]. Solvar (Money3, consumer and car loans) is at 7.2 times normalised and 8.8 times statutory FY26 EPS (A$1.37 on 19.0c and 15.5c) [P1][M1]; Credit Corp 10.1 times (A$15.64 on A$1.543) [M1]; Plenti 10.6 times [M1]. I use 7 times in the bad case, 8.5 in the middle and 9.5 in the good.

By early March 2027 the market will see FY27's half and will look ahead to FY28, so I take the average of FY27 EPS at the multiple and FY28 EPS at the multiple discounted a year at 13%:
- Bad: 7 x 1.7c = 11.8c; 7 x 2.6c / 1.13 = 16.0c; average 13.9c.
- Middle: 8.5 x 2.6c = 22.5c; 8.5 x 3.8c / 1.13 = 28.5c; average 25.5c.
- Good: 9.5 x 3.6c = 34.1c; 9.5 x 5.0c / 1.13 = 42.3c; average 38.2c.

### Method 2: price to net tangible assets against the return on them
Lenders trade on price to net tangible assets in line with their return on them. Solvar earns about 11.2% on its NTA (normalised profit A$36.1m on NTA of A$1.66 to A$1.72 a share, 187m shares) and trades at about 0.87 times NTA after the 8.5c it paid in October [P1][M1], so the market asks it for about 13%. Credit Corp earns about 11.9% and trades at 1.19 times its A$13.18 [P2][M1], an ask of about 10%, but it is a larger, steadier debt buyer. I use 13% for CCV, cap the multiple at 1.35 times (CCV's highest recent level was about 1.18 times, August 2025 at A$0.34 on 28.8c [C7]), and apply it to FY28's return on NTA of about 24.3c a share (A$179m):
- Bad: 10.7% return, 0.82 times, 19.9c.
- Middle: 15.6% return, 1.20 times, 29.2c.
- Good: 20.7% return, capped at 1.35 times, 32.8c.

### Range
Midpoint of methods 1 and 2: bad A$0.169, middle A$0.274, good A$0.355.
- The low end depends on Cashies losing 11% a year in a rising-rate year with the provision build still running. A worse case (losses at 13%, growth stopped, a raising near NTA) would be about A$0.12 to A$0.14.
- The high end depends on Cashies losses staying near the FY26 group half-year rate and stores adding about A$5m.
- The input that moves the answer most is the Cashies loss rate: one point is A$1.5m before tax in FY27 and A$2.2m in FY28, about 1.6c a share in value at 8.5 times. Next is the yield (the same size per point), then the multiple.

Over 24 months (valued after the FY28 result in August 2028, FY28 EPS at the case multiple and NTA of about 25c): bad A$0.194, middle A$0.311, good A$0.406 (outcomes.py).

### The fact sheet's anchors retested
- "Our way", A$0.346: 1H26 operating profit doubled (A$26.4m) at Credit Corp's price to NTA. The 1H26 half had about A$28.6m of interest from old personal loans (average A$100m at about 57%) and A$5.1m from vehicle loans, plus a A$5.6m allowance release; in FY27 the old books earn about A$15m for the whole year. My middle FY28 (A$27.9m) does reach that level, so the anchor is a FY28 outcome, and priced at Credit Corp's 1.43 times NTA rather than CCV's own history (about 1.1 to 1.2 times). Inside six months the earnings the market can see (1H27) will in my middle case be about A$10m, down on 1H26. So A$0.346 is a good case for 2028, not a middle case for March 2027.
- "Against us", A$0.205: 2H26 profit doubled at Solvar's multiple. My middle FY27 (A$19.2m) is about the 2H26 rate, but FY28 is better, so the market should pay more than A$0.205 if the middle case holds; my bad case (FY27 A$12.2m) is lower than this anchor.

## Why the market is wrong
I can't say it is at A$0.265. The price is 1.1 times NTA, 10 times my middle FY27 EPS and 7 times my middle FY28 EPS; my middle value (A$0.274) is only 3% above it. The two brokers' targets (A$0.35 and A$0.41) rest on FY27 EPS of 3.2c and 3.8c, which need the FY26 allowance release to be replaced by Cashies profit straight away; the market's discount to them looks reasonable to me. What would make the market wrong is a 1H27 result that shows Cashies' losses holding near 5% a half while the book grows past A$160m: then FY28 at 3.8c to 5.0c comes into view and the price should move towards A$0.31 to A$0.36. That is the good case, and I give it 25%.

## Outcomes and chances
Resolve date: 5 March 2027, ten days after the 1H27 result (inferred from 23 February 2026 [C4]).

| Outcome | What happens | Chance | Price by resolve date |
| --- | --- | --- | --- |
| Bad | 1H27 operating profit after tax below A$8m (excluding the NZ sale gain), or the six-month net loss rate above 6.5%, or a raising; the market prices FY27 at about 1.7c | 30% | A$0.169 |
| Middling | 1H27 operating profit A$8m to A$12m, Cashies at A$150m to A$175m, net loss rate 5% to 6.5%; FY28 recovery still the story | 45% | A$0.274 |
| Good | 1H27 operating profit A$12m or more with the loss rate at or below 5.5% and Cashies past A$160m, or a securitisation refinancing at a lower cost | 25% | A$0.355 |

Chances add to 100%. Each price is the midpoint of methods 1 and 2 for that case: bad A$0.169, middling A$0.274, good A$0.355. No dividend falls in the window: last year's interim went ex on 23 March [C11].

- Expected price: 0.30 x 0.169 + 0.45 x 0.274 + 0.25 x 0.355 = A$0.263, 0.9% below A$0.265.
- Round-trip costs at about A$2,016 (2.5% of NZ$100,000 at 0.806 Australian dollars to the NZ dollar, data/fx/fx_daily.csv, 6 November): the spread, 1.87% (the quoted spread on 6 November, A$0.265 to A$0.27, a one-tick minimum; the Corwin and Schultz estimate is 1.5%); size cost 0.24% each way (src/fills.py: 2.1% daily volatility, A$157,258 average daily value); 0.5% to change NZ dollars; and A$15 brokerage each way (0.74%) unless the monthly plan covers it. That is 2.8% to 4.3%.
- Expected gain after costs: about -3.8% to -5.2%.
- Minimum (rulebook section 5a): (2.13% + 5%) x 117 days / 365 = 2.29%. Below it, so not a case for review.
- What it would take: at these chances, a price of A$0.245 or lower (A$0.2463 at the high cost, A$0.2498 at the low). With the chances moved to 25%, 45%, 30%, A$0.255; at 20%, 45%, 35%, A$0.26.

## Dated events
- 12 November 2026: deadline for shareholders' written questions; 17 November proxy deadline [C8].
- 19 November 2026, 9:00am AWST: virtual AGM [C8]. Last year's AGM released a first-quarter update with segment revenue and the Cashies book at 31 October, and a direction for the first-half Personal Finance result [C7]; one is likely again (inferred).
- December 2026 and February 2027: RBA meetings; the facility cost moves with bank bill rates.
- 31 December 2026: half-year end; allowance and covenant tests.
- About 23 February 2027: 1H27 result and interim dividend (inferred from 23 February 2026 [C4]).
- About 23 March 2027: interim dividend ex date (inferred from 23 March 2026 [C11]).
- Before 27 August 2027: securitisation refinancing or extension (drawing period ends) [C1].
- 30 June 2027: Peter Cumins retires [C13].
- About late August 2027 and 2028: FY27 and FY28 results.

What the AGM must show to reopen early (19 November):
- Cashies book at 31 October 2026 of A$140m or more, first-quarter Personal Finance revenue at or above Q1 FY26's A$17.7m [C7], and a statement that 1H27 group operating profit will be at or above 1H26's A$13.2m. Then the chances move to about 20%, 45%, 35% (expected A$0.281); send to the red team as an ordinary pick resolving 5 March 2027 if the price is A$0.26 or less at the next close.
- If the AGM says the first-half Personal Finance result or group profit will be below 1H26 with no number, nothing changes: wait for the result, trigger A$0.245.
- If it gives a 1H27 figure below A$8m, or Cashies below A$125m (growth stalled), the bad case is under way: chances about 50%, 40%, 10%, expected about A$0.231, no case above about A$0.215.

What the 1H27 result (about 23 February 2027) must show:
- Reopen as an ordinary pick: operating profit after tax of A$12m or more excluding the NZ sale gain; six-month net loss rate (net write-offs over the average gross book) at or below 5.5%; Cashies at A$160m or more; loss allowance on the Personal Finance book not falling below about 12% (so the profit isn't made by releasing it). Then rerun with a resolve date after the FY27 result, at prices up to about A$0.30.
- Reopen as a value pick: the same, plus a securitisation refinancing agreed or in term sheet, at a price at or below about A$0.215 (where my 24-month bad case is within 10%).
- Close: operating profit below A$8m, a six-month loss rate above 6.5%, stage 2 loans still rising as a share, a capital raising below NTA (about 24c), or a dividend cut.

Watch trigger: A$0.245 (a close at or below it, with no news), as an ordinary pick to 5 March 2027. The share's 52-week low is A$0.245 [M1].

## What would make this wrong
1. Cashies is better than I allow. If its yield is above 42% or its loss rate below 8%, FY27 lands near the brokers' 3.2c to 3.8c and the price should be A$0.33 to A$0.38 by March. The two-half solve that gives 40% uses straight-line average balances, so it could be off by a couple of points either way.
2. Credit turns. The RBA has raised five times in 2026 to 4.85% and sees inflation above 3% until late 2027 [R1]. Cashies' customers average a credit score of about 550 [C3, p. 3], and the FY26 vintages are only now reaching the age when write-offs peak. A loss rate of 13% on Cashies would put FY27 profit near A$9m, and a raising would follow if growth continued.
3. Funding. The facility must be refinanced by August 2027 for drawing; a higher margin, a lower advance rate or a tighter minimum cash covenant would cut both profit and growth. On the other side, a cheaper facility is the company's own stated aim.
4. EZCORP. With 43.5% and the chair, a bid is possible at any time. Nothing in the filings suggests one.

Exit rule, if a card is ever written: sell at the next open after a result or update showing six-month net losses above 6.5%, operating profit below A$8m for the half, a raising below NTA or a dividend cut; otherwise sell on or after the resolve date unless a fresh deep dive renews it.

## Checks
- Not on Cam's excluded list: config/judgement_excluded.csv has no entries (confirmed by Cam on 8 November 2026). Consumer lending and second-hand retail are not gaming, wagering or racing.
- No placement-pattern reopening in the last 30 sessions: CCV traded on all 31 sessions from 18 September to 30 October 2026, the worst opening gap was -2.0% on 26 October, and the last capital raising was the A$25m placement and entitlement offer at A$0.305 in October and November 2025 [M2][C9].
- Liquidity: median value traded A$108,903 a day over the 20 sessions 5 to 30 October 2026 (lowest A$12,303; no session under A$10,000; 60-session median A$141,273) [M2]. Section 3 allows two sessions at 10%, about A$21,800. The research cap of 2.5% (about A$2,016) fits inside it and is above the A$1,500 minimum order.
- The share is not in data/prices/ASX, so the nightly fetch would need a line before a card could be placed.

## Corrections to the fact sheet
- "Expected losses are provided for when loans are written, so fast growth holds profit down early": in FY26 the opposite showed in the accounts. The allowance fell, and the year's charge included a A$10.1m net release (A$5.6m and A$4.5m by half) [C1][C5].
- The 2H26 fall was mainly lost interest on the old books (A$5.4m), not provisions (about A$2.6m more than in 1H26).
- "The net loss rate fell from 16.0% to 11.1%" is right for the year, but the six-month rate rose from 5.3% in 1H26 to 6.0% in 2H26 (derived from [C1][C5]).
- "Store profits now carry the group": A$15.8m of the Australian stores' A$46.8m operating EBITDA is commission from the group's own lending [C1, note 2].
- The "our way" anchor includes about A$34m of half-year income from old books that will earn about A$15m in all of FY27, and a A$5.6m allowance release: it is a FY28 good case.
- Cash A$37.2m is not free: A$3.9m is restricted, A$6.0m is in stores and A$10m must stay unrestricted under the Fortress covenant [C1, note 7.a]. The NZ personal loans were sold for about A$8.9m in July [C1, note 18], which the fact sheet left out.
- Solvar's NTA of A$1.66 is before its 6.0c final and 2.5c special dividends paid on 7 October 2026 [P1], so its price to NTA is about 0.87 times, not 0.84; peer prices are now A$15.64 (Credit Corp) and A$1.37 (Solvar), 6 November [M1].
- The minimum unrestricted cash covenant and the commission between segments, both material, are not in the fact sheet.
- Related party: the A$6.4m Perth Bears sponsorship [C1, note 19.c].

## What I couldn't verify
- Cashies' own yield, loss rate and allowance: the company reports Personal Finance as a whole. My 40% yield and 12% allowance are derived.
- The split of FY26 bad debts between Personal Finance, vehicle, NZ and pawn.
- How much of FY26's A$12.6m of recoveries came from one-off debt sales.
- The gain on the NZ book sale and whether it will be counted in operating profit.
- The securitisation facility's margin over bank bills, its advance rate rules and covenants beyond the minimum cash.
- The CEO's EPS target for the FY27 rights (not disclosed in the notice [C8]).
- EZCORP's intentions and the value it carries its stake at (its 10-K was not read).
- Broker models beyond FNArena's and the Motley Fool's summaries [S1][S2] (secondary sources).
- Whether the AGM will give a number.

## Sources
- [C1] Appendix 4E and FY26 Annual Report, 21 August 2026 (03128502): operating and financial review, notes 1 to 19, auditor's report, shareholder information: https://announcements.asx.com.au/asxpdf/20260821/pdf/07322qqmd0jqdc.pdf
- [C2] FY26 Financial Results Announcement, 21 August 2026 (03128507): https://announcements.asx.com.au/asxpdf/20260821/pdf/07323523vh76tz.pdf
- [C3] FY26 Results Presentation, 21 August 2026 (03128508): https://announcements.asx.com.au/asxpdf/20260821/pdf/073237rvr3g0m8.pdf
- [C4] 1H FY2026 Financial Results, 23 February 2026 (03063032): https://announcements.asx.com.au/asxpdf/20260223/pdf/06wlcjxx07m36f.pdf
- [C5] H1 FY2026 Appendix 4D and Interim Financial Report, 23 February 2026 (03063030): https://announcements.asx.com.au/asxpdf/20260223/pdf/06wlcdpbcz8wkd.pdf
- [C6] 1H FY2026 Investor Presentation, 23 February 2026 (03063033): https://announcements.asx.com.au/asxpdf/20260223/pdf/06wlcm1zx32p7j.pdf
- [C7] 2025 AGM Address and Presentation, 20 November 2025 (03029416), with the Q1 FY26 trading update: https://announcements.asx.com.au/asxpdf/20251120/pdf/06s8dq9cz4lb3w.pdf
- [C8] Notice of 2026 Annual General Meeting, 19 October 2026 (03153996): https://announcements.asx.com.au/asxpdf/20261019/pdf/075h5vvbcgh8yh.pdf
- [C9] Equity Raising Investor Presentation, 27 October 2025 (03015685): https://announcements.asx.com.au/asxpdf/20251027/pdf/06r26g512jfdf7.pdf
- [C10] Cash Converters Completes Acquisition of Franchise Stores, 4 December 2025 (03036729): https://announcements.asx.com.au/asxpdf/20251204/pdf/06sxl426jts1c0.pdf
- [C11] Dividend/Distribution, 1H26 interim (ex 23 March 2026, paid 15 April 2026), 23 February 2026 (03063031): https://announcements.asx.com.au/asxpdf/20260223/pdf/06wlcgstlss7d3.pdf ; Update - Dividend/Distribution, FY26 final (ex 3 September, paid 7 October 2026, reinvestment price A$0.27), 17 September 2026 (03140684): https://announcements.asx.com.au/asxpdf/20260917/pdf/0746k6lx29cbxl.pdf ; Application for quotation, 5,062,399 reinvestment plan shares issued 7 October 2026 (03149576): https://announcements.asx.com.au/asxpdf/20261007/pdf/0751kgzpcyk6b4.pdf
- [C12] Change of Director's Interest Notice, Peter Cumins, 10 March 2026 (03070023): https://announcements.asx.com.au/asxpdf/20260310/pdf/06x7bkzrcrxkj0.pdf
- [C13] Board Change, Retirement of Director, 14 July 2026 (03114588): https://announcements.asx.com.au/asxpdf/20260714/pdf/071p41msbxy765.pdf
- [C14] ASX announcements lists for CCV, 2025 and 2026 (nothing lodged after 19 October 2026 as at 8 November): https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=CCV&timeframe=Y&year=2026 ; https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=CCV&timeframe=Y&year=2025
- [C15] Australian Microcap and Shaws Conferences presentation, 11 May 2026 (03092385), read for any update (none beyond 1H26): https://announcements.asx.com.au/asxpdf/20260511/pdf/06zfy51mqwf18p.pdf
- [P1] Solvar FY26 Investor Presentation (03126867) and results release (03126865), 19 August 2026: https://announcements.asx.com.au/asxpdf/20260819/pdf/072xqy2g8nxfgv.pdf ; https://announcements.asx.com.au/asxpdf/20260819/pdf/072xqsqzq7m52n.pdf
- [P2] Credit Corp Group FY26 Appendix 4E, 4 August 2026 (03121586), NTA per share: https://announcements.asx.com.au/asxpdf/20260804/pdf/072d8g0918x2tv.pdf
- [M1] ASX company data: data/research_data/asx_company.json (fetched 7 November 2026 UTC: CCV last A$0.265, bid A$0.265, offer A$0.27, 716,585,333 shares, 52-week range A$0.245 to A$0.35; Solvar A$1.37; Plenti A$0.79 and 10.6 times); ASX key statistics read 8 November 2026 for Credit Corp (A$15.64 last, EPS A$1.543), e.g. https://asx.api.markitdigital.com/asx-research/1.0/companies/ccp/key-statistics
- [M2] Norgate prices in this repository, data/norgate/universe/prices_2019.csv.gz to prices_2026.csv.gz (to 30 October 2026); index membership data/norgate/index_members.csv; FX data/fx/fx_daily.csv; spread and size cost src/spreads.py and src/fills.py.
- [R1] RBA raised the cash rate to 4.85% on 4 November 2026, its fifth rise of 2026, and sees inflation above 3% until late 2027 (secondary sources): https://investinglive.com/central-banks/more-rba-lifts-cash-rate-to-4-85-in-split-6-3-vote-sees-inflation-above-3-until-late-2027/ ; https://www.savings.com.au/news/rba-lifts-cash-rate-to-4-85 ; the RBA's own table is cited in research/picks/ASG.md.
- [S1] FNArena, CCV page, read 8 November 2026 (secondary source: Bell Potter and Shaw and Partners targets and forecasts): https://fnarena.com/stock-price-analysis/business-consumer-credit/CCV
- [S2] The Motley Fool Australia, 25 August 2026, on Shaw and Partners' A$0.41 target (secondary source): https://www.fool.com.au/2026/08/25/this-high-yield-asx-stock-could-deliver-40-share-price-gains-broker/
