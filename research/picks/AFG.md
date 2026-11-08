# Australian Finance Group (ASX:AFG): deep dive. Not a value pick at A$1.565; wait for the HY27 result (about 18 February 2027)

Written 2026-11-08 by the research desk. Price at writing: A$1.565 (last trade on 6 November 2026; the close on 5 November was A$1.57; ASX company data fetched 7 November 2026 UTC [M1]; Norgate's last close in the repo is A$1.49 on 30 October [M2]). Market value: A$412.7m (263,733,615 shares on issue after the 28 September 2026 buy-back cancellation [A23]; about 5.5m performance rights also on issue [A23][A24]).
Status: finished. Verdict: wait for a named event, the HY27 result due about 18 February 2027 (exact reopen conditions under "Dated events"). Not a value pick at A$1.565: to 31 August 2028, with dividends counted, the bad case (A$1.27) is 19% below the price, against the 10% the rule allows; the middling case (A$1.90) is 21% above it. As an ordinary pick to 31 March 2027 the expected gain is about +4.8% before costs and +2.5% after them, against a minimum of 2.8%, and most of it is the interim dividend. No card. Not sent to the red team. This is a simulation and not financial advice.
Fact sheet: research/facts/AFG.md (written 2 November 2026 under the earlier template, prices from 30 October), grade A. The question it set: can AFG hold FY26's A$48.5m profit with its lending margin above its own long-run aim, two warehouse lines expiring on 12 November and 10 December 2026, its own lending volumes down 18% in Q1 and rates rising? If it goes our way A$2.31 (FY26 profit at its five-year average 12.5 times); if not A$1.00 (five-year average profit at the non-bank lenders' 7 times).

> In short: AFG can most likely hold FY26's profit, but the price has already moved to say so. Its second half earned A$26.1m (19.2c a share annualised), the lender's book is 28% bigger than a year ago, and the lending margin held at 126bps through three rate rises in that half. My central FY27 profit is about A$49m (18.7c a share), inside a range of A$39m to A$56m. The thing that can break it is the margin, not housing volumes: in the last rate-rise cycle the margin fell from 163bps (FY22) to 113bps (FY24) and profit from A$51.3m (FY21) to A$29.0m (FY24). This time more than half of the lender's funding is term RMBS with its cost fixed over bank bills, one of the year's warehouse renewals has come in cheaper and the September RMBS priced inside warehouse costs; against that, the September RMBS cost about 7bps more than February's, bank bills no longer sit below the cash rate, the RBA raised to 4.85% at its November meeting with markets pricing more, and AFG itself reports more competition for its loans. On three methods the business is worth about A$1.50 to A$2.00 a share (central about A$1.70). The fact sheet's A$2.31 needs the market to pay AFG's own long-run multiple while rates stay high: that is the good case, not the middling one. The price has risen 25% since 13 October (A$1.25) on the AGM update, so the gap is now about 10%, not 55%. Wait for the HY27 result, which shows the margin after the 12 November and 10 December warehouse renewals and the September and November rate rises, or for a price of A$1.41 or less before it.

Order of work. The fact sheet shows a price, so a price was in view before this file was started. The filings, the margin history, the FY27 and FY28 profit model and the three valuation methods were done first from the company's own figures and the peers' multiples; AFG's price enters only in its own price history used as a multiple check, in "Why the market is wrong" and in "Outcomes and chances". Arithmetic in python3 -I (scratchpad script afg_model.py), shown in the text.

## The company in plain words
AFG has two businesses, both in Australia only.
- Distribution: Australia's largest mortgage broker group (aggregator). More than 4,300 brokers write about 1 in 9 Australian home loans through more than 80 lenders; AFG keeps a slice of the upfront and trail commissions the lenders pay, and sells brokers software (BrokerEngine), compliance and marketing services by subscription. FY26 Distribution EBITDA A$70.7m, 68% of segment EBITDA, underlying return on equity 40% [A2 p9, p28].
- Manufacturing: AFG Securities, its own lender, which writes prime home loans through the network and funds them in separate trusts with bank warehouse lines and RMBS (bonds). Loan book A$7.1bn at 30 June 2026 and A$7.3bn at 30 September; net interest margin 125bps in FY26. Also a 31.88% stake in Thinktank, a commercial and residential non-bank lender (AFG's share of its profit A$6.2m). FY26 Manufacturing EBITDA A$33.1m [A1 note 12][A2 p29][A4].

Who runs it: David Bailey, CEO; Greg Medcraft, chair; Luca Pietropiccolo, CFO [A2 p24][A4]. The co-founders have all left the board: Malcolm Watkins in February 2026 and Brett McKeon at the AGM on 16 October 2026 [A4][A25][A26].

Who owns it. Substantial holders at 31 July 2026: First Sentier (Mitsubishi UFJ) 7.37%, Australian Ethical 7.36%, McKeon's MBM Investments 5.56% (15,000,000 shares), the McGougan family's Banyard Holdings 5.48%, Pendal 5.43%, Watkins' MSW Investments 5.36%. The three largest registered holders are custodians (HSBC 21.49%, Citicorp 17.38%, J P Morgan 10.29%); 5,767 holders [A1 shareholder information]. Since then Australian Ethical rose to 7.56% (notice 31 August) and First Sentier fell from 7.46% to 6.09% (notice 24 September, around the index exit) [A29][A28]. The founding families (McKeon 15.0m, McGougan 16.9m across two accounts, Watkins 14.4m, Matthews 2.8m) hold about 49m shares, 18.6%, none of them now on the board [A1][A26].

Six years (statutory profit; underlying EPS is the company's NPATA measure):

| | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
| --- | --- | --- | --- | --- | --- | --- |
| Statutory profit (A$m) | 51.3 | 38.8 | 37.3 | 29.0 | 35.0 | 48.5 |
| Statutory EPS (c) | 19.1 | 14.2 | about 13.8 | about 10.7 | 12.9 | 17.9 |
| Underlying EPS (c) | | 20.7 | 17.9 | 13.4 | 15.1 | 20.0 |
| AFG Securities margin (bps) | 178 | 163 | 136 | 113 | 116 | 125 |
| AFG Securities book at 30 June (A$bn) | 3.4 | 4.8 | 4.5 | 4.4 | 5.5 | 7.1 |
| Dividends (c) | | 14.4 | 16.2 | 8.0 | 9.1 | 9.5 |
| Share price at 30 June (A$) | 2.85 | 1.48 | 1.79 | 1.38 | 2.29 | 1.59 |

Sources: [A19] (FY21 profit and EPS), [A18] (FY22 EPS, FY21 and FY22 margin), [A16] (FY23 margin, underlying EPS), [A14] (FY24), [A13] (FY25), [A1 remuneration report five-year table] and [A2] (FY22 to FY26 profit, book, dividends, prices), [M2] (FY21 price). FY23 and FY24 statutory EPS are profit over about 270m shares.

## Why big investors may be overlooking it
- Index: removed from the S&P/ASX 300 effective 21 September 2026 [A27]. 13.85m shares (5.3% of the company) traded on 18 September, the last day before [M2].
- Size: A$413m market value; median session A$831,489 over the 20 sessions to 30 October [M2].
- How the data services show it: the consolidated balance sheet carries the lender's A$7.2bn of trust funding, so the ASX company data shows total liabilities of A$8,557.5m against equity of A$242.3m and an enterprise value of A$7,602m [M1]. On a quick screen AFG looks like a heavily indebted company; at group level it is not (see "What the filings show").
- Sector out of favour: housing finance in a rate-rise cycle. The RBA raised five times in 2026 to 4.85%; it reports housing prices in September almost 5% below their March peak, which it puts down to higher rates and the May 2026 Budget's tax changes, and new housing lending down sharply [R1]. AFG's price fell from A$2.25 on 18 February to A$1.25 on 13 October while its profit rose [M2].
- Register: concentrated in custodians and founding families; two founders are now free of board trading windows.
- Analyst coverage: I didn't find a primary source for it and did not search further.

## What the filings show

### 1. Where the profit comes from
FY26 statutory profit A$48.5m, up 39%; underlying NPATA A$54.4m (adds back trail book revaluation A$2.0m, acquired-intangible amortisation A$2.4m and "one-off" costs A$1.5m, all of which also appeared in FY25, so statutory profit is the fairer base) [A1 p58][A2 p30]. Group EBITDA A$74.4m: Distribution 70.7, Manufacturing 33.1, central costs -29.4 [A2 p7, p28, p29].

Splitting profit after tax by segment (segment profit before tax 58.5 and 38.4, central -30.3; tax at 30.6% on profit before tax excluding associates, which are booked after tax; central costs shared 72/28 by EBITDA excluding associates): Distribution about A$25.8m after its share of central costs, AFG Securities about A$16.5m, Thinktank A$6.2m. The halves: H1 A$22.4m (8.26c), H2 A$26.1m (9.60c), so the second-half run rate is 19.2c a share a year [A9][A1].

How much depends on new home loans. The company's "about 10% of earnings" is residential upfront commissions: A$16.4m of A$159.4m gross profit (10.3%) [A2 p8, p28]. Its own sensitivity is that a 10% change in residential settlements moves profit by about 3% [A4]. But more than that depends on new lending: AFG Securities' book growth (its own lodgements were down 17.7% on a year earlier in Q1 [A6]), the diversified products line (A$38.0m: white label, commercial, asset finance) and the broker investments. The bigger lever is the lender's margin: each 5bps on a A$7.4bn book is A$3.7m before tax, about A$2.6m after, about 1c a share.

### 2. The lending margin: its history and what moves it
AFG Securities lends at variable rates and funds itself at a margin over one-month bank bills (BBSW), first in warehouse lines from banks, then by selling RMBS. A level shift in rates passes through: the company's own test shows 100bps on the static book moves profit by only A$1.0m [A1 note 23]. What moves the margin is the gap between what it charges new and existing borrowers and the spread its funders charge.

Margin history: FY21 178bps, FY22 163, FY23 136 (H1 145, H2 127, and 116 in June 2023 after warehouse renewals), FY24 113 (exit 109, "affected by competition and multi-year high price warehouse"), FY25 116, FY26 125 (H1 124, H2 126, exit 128) [A18][A16][A15][A14][A13][A2 p10, p27]. In the last cycle the book also shrank, from A$4.8bn (FY22) to A$4.4bn (FY24), as AFG put returns ahead of volume [A1 five-year table].

Management's record on its own margin: in August 2023 it said "beyond FY24, NIM is expected to return to longer term average of 130-140bps" [A16]; it got 113 and 116. The FY29 aim set in February 2025 is about 120bps [A2 p5]. FY26 beat that aim.

What is different now, for the margin:
- Term funding: more than half of the lender's outstanding funding is now RMBS, whose margins over bank bills are fixed for the life of the notes [A7][A4]; 71% of the book is "funded on improved terms" at September, up from 67% at June [A4][A2 p10].
- Funding costs are edging up again. The September 2026 RMBS (A$1.2bn) paid BBSW + 103bps on the main A1-L notes against + 95bps in February 2026; across the rated notes the weighted margin rose from about 90.5bps to 97.3bps [A7][A8]. The AGM slide's "+95bps" is the February deal [A4].
- Bank bills: the FY26 margin was helped by one-month BBSW averaging about 5bps below the cash rate [A2 p10]. In the RBA's figures the gap was -3 to -5bps from June to August 2026 and +5bps and +1bp in September and October [R3]. That help has gone.
- The H2 FY26 margin (126bps) held through three rate rises (February, March and May 2026, from the RBA's monthly averages) [A2 p27][R2][R3]. In the HY26 presentation the company warned that "a cash rate increase cycle may impact BBSW spreads" [A10].
- Competition: the Q1 index reports "signs of increased competition" for AFG Securities [A6].

### 3. The warehouse facilities: what was announced
- At 30 June 2026 AFG Securities had six warehouse facilities, expiring 12 October 2026, 12 November 2026, 10 December 2026, 12 April 2027, 10 June 2027 and 13 June 2028, with A$4,087.9m drawn at an effective 5.00% and A$676.0m unused [A1 note 19]. The liquidity table puts A$1,319.0m of warehouse funding due within six months of 30 June, A$1,319.1m in six to twelve months and A$1,462.7m in one to two years [A1 note 23]: about a third of warehouse funding (18% of all the lender's funding) in the October to December 2026 window, two-thirds within a year.
- If a warehouse isn't renewed, the funder has no recourse to the rest of the group; the group loses that slice of margin income and can't fund new loans from it [A1 note 19, note 23]. The facilities are "generally renewable bi-annually or annually".
- At the AGM on 16 October the CEO said "one has already been renewed below existing pricing, and our recent $1.2 billion term transaction was priced inside existing warehouse costs" [A4]. He didn't say which facility. The A$1.2bn RMBS settled on 29 September [A7], so it took warehouse-funded loans out before the November and December expiries, shrinking what has to be renewed.
- Nothing has been announced about the 12 November or 10 December facilities; the ASX list has no AFG announcement after 23 October 2026 [A37]. AFG doesn't announce renewals one by one; the HY27 result will report the margin after them.

### 4. Q1 FY27 trading and the AGM
- AFG brokers lodged A$26.8bn of home loans in Q1 FY27, down 12.4% on a year earlier and 4.5% on the prior quarter; investors 32% of lodgements (34%), refinancing 15%, upgraders a record 46%; WA had its first year-on-year fall after 11 quarters of growth [A6].
- AFG Securities: lodgements about A$1.1bn, down 17.7% on a year earlier and 24.5% on the prior quarter, "a particularly soft July", August and September better; book A$7.3bn at September, 28% up on a year; run-off steady; loans 90+ days in arrears 0.58% (56 loans) against 0.74% a year earlier [A6][A4].
- FY27: about A$13m of extra EBITDA "expected" from FY26 investments, assuming a A$7.1bn book and a 120bps margin; the company calls these assumptions conservative [A4][A2 p12]. The footnote says the AFG Securities part (+A$10m) compares a A$7.1bn closing book at 120bps with the FY26 average. On my arithmetic that is the extra margin income (A$85.2m against FY26's A$78.0m, or A$10.8m on the book growth alone at 120bps) before the extra commissions AFG Securities pays brokers on a larger book (about A$4.3m a year on A$0.9bn at FY26's 0.48% of book). I couldn't reconcile the A$10m exactly; my FY27 model has a smaller uplift.
- Votes: remuneration report 97.02% for and David Flynn's election 97.75% for, on a poll [A5]. No strike.
- The chair: "AFG's share price has not kept pace with the evolution and performance of the business" [A4].

### 5. Cash earnings against accounting profit
- Operating cash flow A$51.1m (FY25 A$35.9m) [A1 p61]. It includes the trusts' interest and the profit share of associates is not cash: AFG booked A$7.4m from associates and received A$1.1m in dividends [A1 note 12].
- A cash bridge for the shareholders' side of the group in FY26: AFG paid A$27.1m of dividends, A$3.4m of buy-backs, A$2.4m for employee shares, A$6.6m into broker businesses, A$6.5m of capex, A$2.0m of lease principal and put about A$8.3m more into subordinated notes in its own trusts (A$34.9m to A$43.2m), A$56.3m in all, and its net corporate position moved from A$11.8m net cash to A$3.5m net debt (A$15.3m) [A1][A2 p31]. So the business generated about A$41m of cash for shareholders, against statutory profit of A$48.5m; statutory profit less associates plus their dividends is A$42.2m. Cash earnings are about 85% of reported profit, the gap being mostly Thinktank's retained earnings, which are real value but not cash.
- Dividend policy: 50% to 70% of "adjusted NPAT" (underlying, with associates' profit replaced by their cash dividends); FY26 9.5c fully franked, 60% [A2 p26][A13]. Interim dividends go ex in late February and are paid in late March (HY26: ex 25 February, paid 27 March 2026) [A11].

### 6. Balance sheet
- Corporate: unrestricted cash A$62.6m, A$66.1m drawn (A$67m face) on a A$100m ANZ/NAB facility signed 19 February 2026 for four years at BBSY + 2.00%: net debt A$3.5m at 30 June [A1 note 8, note 19]. Since then: about A$10.2m more of buy-backs (A$13.61m in all to 24 September less A$3.4m in FY26) and the 4.8c final dividend (about A$12.7m, paid 1 October) [A22][A3]. With a quarter of a year's cash earnings, net debt was probably about A$16m in October (estimate).
- The lender's funding: warehouse A$4,087.9m and "securitised funding facilities" A$3,099.1m (RMBS plus risk retention facilities) [A1 note 19]. Warehouse and RMBS funders have no recourse beyond the trusts. The risk retention facilities, which fund the 5% of each RMBS that AFG must keep for its European, UK and Japanese investors, are "supported by a guarantee provided by AFG Securities Pty Ltd" [A1 note 19]. AFG's own exposure is its subordinated notes (A$43.2m) [A2 p31].
- Trail book: future commissions on loans already written, A$1,225.4m asset against about A$1,141m owed to brokers, net A$83.9m (A$96.2m FY23, 90.6, 86.8, 83.9) [A2 p32][A1 note 23]. A 10% faster run-off would cut profit after tax by A$5.8m [A1 note 23]. This cuts both ways now: the CEO expects refinancing to lift as rates rise [A4], which helps upfront commissions but speeds run-off.
- Associates: Thinktank carried at A$44.9m, broker investments at A$16.6m [A1 note 12]. Thinktank earned A$18.8m after tax in FY26 on net assets of A$108.6m, up from A$8.2m [A1 note 12].

### 7. Capital management and director dealings
- Buy-back of up to A$15m and 9,740,260 shares from 16 June to 15 December 2026 [A21]. To 24 September it had bought 8,958,600 shares for A$13.61m (highest A$1.80, lowest about A$1.28) [A22]. No buy-back notice since 25 September [A37], so none since 24 September, through three weeks of closes between A$1.25 and A$1.34 (25 September to 16 October) [M2]. Left: 781,660 shares or A$1.39m.
- Performance rights: 1,956,378 issued on 22 October (CEO 663,050), vesting on EPS growth of 7.5% to 17.5% a year and TSR, valued off a A$1.659 base [A24].
- Directors bought on market after the FY26 result: Flynn 100,000 (21 and 24 August, A$158,912), Muirsmith 50,000 (31 August, A$76,995), King 50,000 (2 September, A$73,000), Carter 150,000 (7 September, A$227,443), Flynn 50,000 (8 September, A$74,432), Carter 50,000 (9 September, A$70,689), Flynn 42,900 (21 and 22 October, A$59,454): about A$741,000 in all at A$1.39 to A$1.59 [A30 to A36]. No on-market sales.

## Valuation
Done on the business's own figures. AFG's own past prices are used only to show what multiple the market has paid for this business.

### What the business earns, normally
A segment model for FY27 and FY28 (python, afg_model.py), from FY26's segment results:
- Distribution: residential upfront gross profit (A$16.4m) moves with settlements; diversified products (A$38.0m) slip; broker services (A$23.8m) grow by the exit run rate; trail grows a little; opex rises A$1.5m.
- AFG Securities: margin income = average book x margin; commissions paid to brokers at 0.48% of the average book (FY25 0.50%, FY26 0.479%; this rebuilds FY26's A$44.9m gross profit as A$44.4m); other costs A$3.6m; opex up about A$1.5m; Thinktank as stated.
- Central costs -A$30.5m, depreciation A$11.8m, net finance income A$3.0m, tax 30.6% on profit excluding associates.

| | FY27 bad | FY27 central | FY27 good | FY28 bad | FY28 central | FY28 good |
| --- | --- | --- | --- | --- | --- | --- |
| Residential settlements against FY26 | -15% | -10% | -3% | -15% | -5.5% | +2% |
| AFG Securities average book (A$bn) | 7.30 | 7.45 | 7.60 | 7.30 | 7.90 | 8.40 |
| Margin (bps) | 110 | 121 | 126 | 110 | 120 | 125 |
| Thinktank (A$m) | 4.5 | 6.2 | 7.0 | 4.5 | 6.5 | 7.5 |
| Group EBITDA (A$m) | 63.1 | 76.3 | 85.5 | 61.6 | 79.5 | 92.8 |
| Statutory profit (A$m) | 39.1 | 49.3 | 56.3 | 37.8 | 51.4 | 61.5 |
| EPS on 263.7m shares (c) | 14.8 | 18.7 | 21.4 | 14.3 | 19.5 | 23.3 |

The central case has the margin falling from the 128bps exit to about 121bps (the BBSW help gone, the September RMBS dearer, competition), settlements down 10% after Q1's -12.4%, and the book growing slowly after Q1's +A$0.2bn. The bad case is FY24 again: margin back to 110bps and held there for two years, the book flat, settlements down 15%, Thinktank's profit cut. It gives EPS of about 14.3c to 14.8c, close to FY24's underlying 13.4c on a book now about 65% larger. A worse tail (margin 100bps) takes profit to about A$33m. The fact sheet's "five-year average profit" of A$37.7m is close to my bad case in money but leaves out FY21 (A$51.3m) and a book now about 65% larger than in FY24.

Cash earnings are lower than profit by the associates' retained earnings: about A$41m to A$42m in FY26 (section 5) and about A$42m to A$44m in the central FY27.

### Method 1: price to earnings, against listed peers and AFG's own record
The market prices both mortgage lenders and AFG on profit: price to earnings and the dividend.
- Listed non-bank lenders (ASX company data, 6 November 2026) [M1]: Resimac 6.7 times, Pepper Money 7.6 times, Liberty 7.1 times; average 7.1. They are pure lenders, with more leverage and, for Pepper and Liberty, non-prime loans. Two-thirds of AFG's EBITDA is the capital-light broker business, which should earn a higher multiple. There is no listed pure broker aggregator in Australia since REA bought Mortgage Choice in 2021 (A$1.95 a share, about A$244m, a 65% premium to the A$1.18 close before the offer; the independent expert valued it at A$1.66 to A$1.97 on a control basis; secondary source, The Adviser [S1]; I couldn't find the earnings multiple).
- AFG's own record: from late August 2018 to October 2026, on daily closes and the last reported statutory EPS, AFG traded at a median 12.3 times (middle half 10.5 to 15.3 times) [M2][A19][A20][A18][A1]. By year: 2018 9.3, 2019 10.9, 2020 11.5, 2021 15.4, 2022 10.9, 2023 11.1, 2024 11.7, 2025 18.3, 2026 12.7 (low 7.0 in October 2026). In the high-rate years 2023 and 2024 the median was 11.1 and 11.7 times, but on falling or trough earnings; the lowest closes were A$1.28 (30 October 2023, 9.3 times) and A$1.32 (3 July 2024) [M2].
- Values: FY27 central EPS 18.7c at 7.1 times = A$1.33; at 8.8 times (between the peers and AFG's record) = A$1.65; at 10.5 times (the low quartile of its record) = A$1.96. On FY26 EPS (17.86c): A$1.27, A$1.57, A$1.88.

### Method 2: sum of the parts
- Distribution, about A$25m after tax and its share of central costs in FY27 (A$25.8m in FY26 less volume), at 9 to 12 times: A$225m to A$300m. It earns 40% on equity, a third of its gross profit is recurring trail and subscriptions, but its volumes are cyclical.
- AFG Securities, about A$19m after tax and central costs in FY27, at the lender peers' 6.5 to 7.5 times: A$124m to A$143m.
- Associates at book (Thinktank A$44.9m, about 7 times its share of FY26 profit; broker investments A$16.6m): A$61.5m.
- Net corporate debt, about A$16m (October estimate).
- Total A$394m to A$488m, A$1.49 to A$1.85 a share; middle (10.5 and 7 times) A$441m, A$1.67.

### Method 3: cash earnings capitalised
Cash earnings for shareholders of A$40m to A$44m a year, growing 2% to 3%, at a required return of 11% to 12.5% (a small, cyclical financial), plus associates at book less net debt: A$434m to A$612m, A$1.65 to A$2.32 a share; middle (A$42m, 11.5%, 2.5%) A$524m, A$1.99. The answer is most sensitive to the required return: each point moves it by about A$0.20.

### Testing the fact sheet's A$2.31
FY26 profit at 12.5 times is A$609m. AFG's median 12.3 times since 2018 says the market has paid that, but mostly in falling-rate years (2019 to 2021, 2025) or on trough earnings it expected to recover (2023 to 2024). The RBA's November forecasts assume the cash rate averages 4.7% to 4.9% through 2028, after markets priced about one and a half more rises by mid-2027 [R1]: no cuts in the window. No buyer of control is in view (no holder over 7.6%, no approach), and the buy-back has A$1.39m left. The mechanism that would get there is earnings the market can see plus a turn in the rate cycle. A$2.31 belongs in the good case.

### The range
About A$1.50 to A$2.00 a share, central about A$1.70: Method 1 A$1.33 to A$1.96 (central A$1.65), Method 2 A$1.49 to A$1.85 (A$1.67), Method 3 A$1.65 to A$2.32 (A$1.99). The main thing each depends on: the lending margin (each 5bps is about 1c of EPS, about 9c a share at 9 times), and whether the market treats AFG as a lender (7 times) or as the broker business most of it is (10 times or more).

## Why the market is wrong
Partly wrong, and less than it was.
1. It priced AFG as a bet on housing volumes. From 18 February to 13 October 2026 the price fell 44% (A$2.25 to A$1.25) while FY26 profit rose 39% and the second half ran at 19.2c a share; at A$1.25 the market paid 6.5 times that run rate, below the pure lenders [M2][A9][A1]. Only about 10% of gross profit is residential upfront commissions, the lender's book is still growing, the margin held through three rises, arrears fell, and index selling (the S&P/ASX 300 exit on 21 September) had a known end. Directors bought A$741,000 of shares on market at A$1.39 to A$1.59.
2. But the market's worry has a basis: the last rate-rise cycle cut the margin by 50bps (FY22 to FY24) and profit by 43% (FY21 to FY24), and the early signs this time (dearer RMBS, no BBSW help, more competition, more rises priced) point the same way, if more mildly. And the AGM update has already moved the price 25%, to 8.8 times FY26 EPS and 8.2 times the second-half run rate: a premium to the lenders and a discount to AFG's own record. What is left is a gap of about 10% to my central value, which a margin slip of 10bps would close.

What should change it: the HY27 result (about 18 February 2027) is the first report that includes the October to December warehouse renewals, the September RMBS and the September and November rate rises. A margin at or above 120bps and half-year profit above A$24m would show the profit base holds through the cycle; a margin near 110bps would show the market was right.

## Outcomes and chances
Value pick test, resolve by 31 August 2028 (after the FY28 result, due about late August 2028): 662 days. Prices are the FY28 EPS of each case (valuation table) at the multiple of that case, plus the dividends I expect in the window (interim FY27, final FY27, interim FY28, at 60% of adjusted profit).

| Outcome | What happens | Chance | Price by 31 Aug 2028 |
| --- | --- | --- | --- |
| Bad | Margin back to about 110bps and held there (dearer warehouse renewals, wider RMBS spreads, competition), book flat at about A$7.3bn, settlements down 15%, Thinktank's profit cut: FY28 profit about A$38m (14.3c). The market pays 8.0 times, between the lender peers (7.1) and AFG's last-cycle floor (9.3); dividends 12.3c. Inside this case: 7.0 times (October 2026's multiple) gives A$1.12, 9.3 times A$1.45 | 25% | A$1.27 (-19%) |
| Middling | Margin near the company's 120bps, book growing to about A$7.9bn, settlements recovering slowly: FY28 profit about A$51m (19.5c); the market pays 9.0 times (just above today's 8.8 times on FY26); dividends 14.8c. At 8.5 times A$1.81 | 50% | A$1.90 (+21%) |
| Good | Margin about 125bps, book A$8.4bn toward the FY29 aim, settlements growing: FY28 profit about A$61m (23.3c); with rates past their peak the market pays 11.0 times (below its 12.3 times median); dividends 15.8c | 25% | A$2.72 (+74%) |

Expected price: 0.25 x 1.27 + 0.50 x 1.90 + 0.25 x 2.72 = A$1.95, 24.4% above A$1.565.

Round-trip costs at our size (2.5% of NZ$100,000 is NZ$2,500, about A$2,016 at NZ$1 = A$0.8064 on 6 November [M3]): the spread estimated from October's daily highs and lows (Corwin and Schultz) at 0.79%, half on each side; A$15 brokerage on the sale (0.74%; the buy within the plan's monthly cover); 0.5% to convert; a size cost of about 0.09% each way (daily volatility 2.01% times the square root of A$2,016 over the A$942,509 average day). About 2.2% in all.

**Expected gain after costs: about +22% over 662 days (about 12% a year).** The minimum (rulebook section 5a) is 7.13% a year (2.13% cash rate plus 5%) over 662 days: 12.9%. It clears the minimum, but a 22-month horizon is allowed only for a value pick, and this isn't one: the bad case is 19% below the price, against the 10% allowed. Both legs pass at a price of A$1.41 or less (bad case A$1.27 = 10% below; middling then +35%). The bad case is the weak point: at 9.3 times (the 2023 floor) it would be A$1.45 (-7%) and pass; at October 2026's 7.0 times it would be A$1.12 (-28%). I use 8.0 times because the market paid 7.0 times for record earnings only a month ago.

As an ordinary pick with an event inside six months, resolve by 31 March 2027 (the HY27 result about 18 February and the interim dividend, ex about late February): 143 days. Prices on trailing twelve-month EPS to December 2026 (H2 FY26's 9.60c plus HY27) plus the interim dividend:

| Outcome | What happens | Chance | Price by 31 Mar 2027 |
| --- | --- | --- | --- |
| Bad | HY27 margin 114bps or less, profit about A$20m (7.6c); 7.5 times 17.2c plus 4.3c | 25% | A$1.33 (-15%) |
| Middling | Margin 119 to 123bps, profit about A$24.5m (9.3c, up about 13%); 8.5 times 18.9c plus 4.8c | 50% | A$1.65 (+5%) |
| Good | Margin 124bps or more, profit about A$27m (10.2c); 9.5 times 19.8c plus 5.0c | 25% | A$1.93 (+23%) |

Expected price A$1.64: +4.8% before costs, **+2.5% after them**, against a minimum of 2.79% (7.13% a year over 143 days). No case. The break-even price is A$1.56, so this is at the line and inside my estimation error; about 3 points of the expected 4.8% is the interim dividend. That isn't an edge worth a card.

## Dated events
- 12 November 2026 and 10 December 2026: AFG Securities warehouse facilities expire [A1 note 19]. Renewal terms are not usually announced on their own; they show in the HY27 margin.
- By 15 December 2026: the buy-back ends; 781,660 shares or A$1.39m left, nothing bought since 24 September [A21][A22].
- RBA decisions in December 2026 and February 2027 (dates not checked); markets priced about one and a half more rises by mid-2027 before the November rise [R1].
- About mid to late January 2027: AFG Mortgage Index for the December quarter (22 January 2026 last year [A37]): AFG Securities lodgements and book.
- About 18 February 2027: HY27 result and interim dividend (inferred from 18 February 2026 [A9]; ex-date about 25 February, paid about late March, as in 2026 [A11]). This is the event: the margin after the renewals and two more rate rises, the book, Distribution's volumes, and any word on the 12 April and 10 June 2027 renewals.
- 12 April and 10 June 2027: the next two warehouse expiries [A1 note 19]. About late August 2027: FY27 result. 13 June 2028: the last listed facility expires. About late August 2028: FY28 result.

Reopen conditions:
- As a value pick before the result: the price at or below A$1.41 with no change to the FY27 outlook and no word of margin pressure from the warehouse renewals. Then the bad case (A$1.27) is within 10% and the middling case (A$1.90) is 35% above; the expected gain after costs would be about +36% over the window. Every close from 18 September to 16 October 2026 was between A$1.25 and A$1.35 [M2].
- As a value pick after the result: HY27 AFG Securities margin of 120bps or more for the half, statutory profit of A$24m or more, and the book at A$7.4bn or more. Then the bad case moves up to a margin of about 114bps (FY28 EPS about 16.0c at 8 times plus dividends, A$1.41), and both legs pass at a price of about A$1.57 or less (bad leg A$1.57, middling leg A$1.65). Re-run the outcomes on the reported figures.
- No case: HY27 margin below 115bps, a warning on funding costs, the book shrinking, or a founder selling more than 2% of the company.

## What would make this wrong
1. The lending margin. If funders reprice the remaining warehouses as they did in 2023 and competition for prime borrowers sharpens while the RBA keeps raising, the margin could fall below 110bps, as it did to a 109bps exit in FY24, and take profit back toward A$33m to A$38m. Each 5bps is about A$2.6m after tax. The September RMBS was already 7bps dearer than February's, and the BBSW help has gone.
2. The multiple. Even if profit holds, the market can keep pricing AFG like a lender (7 times) while rates stay high and house prices fall: it paid 7.0 times record earnings in October. The 25% rise since the AGM came on little new information beyond the Q1 update and could reverse just as easily.
3. For this "wait" call the risk runs the other way: a clean HY27 could re-rate the shares above the reopen prices before the desk can act. That is an accepted cost; at A$1.565 the case doesn't clear the bars without it.
Also: about 18.6% of the shares sit with founding families now off the board; selling by them would weigh on a A$0.8m-a-day share. No such notice so far.

Exit rule (if it is ever bought): sell on a reported half-year margin below 112bps, on a warehouse not renewed, or on a guidance or outlook cut; otherwise hold to the resolve date.

## Corrections to the fact sheet
1. Price: A$1.565 on 6 November 2026, not A$1.49 (30 October). The fact sheet's "our way" gap falls from +55% to +48% and its "against us" gap from -33% to -36%.
2. The rate backdrop has moved since it was written: the RBA raised to 4.85% at its November 2026 meeting (it was 4.60% at the AGM, "highest in 15 years"), five rises in 2026 [R1][R3].
3. "Only about 10% of profit depends on new home-loan volumes": the 10% is residential upfront commissions as a share of gross profit (A$16.4m of A$159.4m) [A2]. The lender's book growth, diversified products and broker investments also depend on new lending; the company's own sensitivity (10% of settlements is about 3% of profit) covers residential settlements only [A4].
4. "Half its warehouse funding renews within eight months": by the liquidity table, A$1,319.0m (32% of warehouse funding, 18% of all the lender's funding) fell due in the October to December 2026 window and 65% of warehouse funding within twelve months of June [A1 note 23]. One facility has since been renewed below existing pricing and the A$1.2bn RMBS settled 29 September refinanced warehouse-funded loans [A4][A7].
5. "The 7,187m of warehouse and RMBS funding ... no recourse": the A$3,099.1m of "securitised funding facilities" includes the risk retention funding facilities, which carry a guarantee from AFG Securities Pty Ltd [A1 note 19]. The group's direct exposure is otherwise its A$43.2m of subordinated notes and the loss of margin income.
6. The RMBS pricing: the AGM slide's "+95bps" is the February 2026 deal; the September deal's A1-L notes priced at BBSW + 103bps and the weighted margin across rated notes rose from about 90.5bps to 97.3bps [A4][A7][A8]. "Priced inside existing warehouse costs" is right, but term funding got dearer.
7. The FY27 "+A$13m EBITDA" from investments: the A$10m AFG Securities part appears to be margin income before the extra broker commissions on a bigger book (about A$4.3m a year); I couldn't reconcile it to A$10m [A2 p12][A4].
8. Cash earnings: about A$41m to A$42m in FY26, not A$48.5m: A$7.4m of the profit is associates' share of profit, of which A$1.1m came in as cash [A1 note 12].
9. The bad case: five-year average profit (A$37.7m) leaves out FY21's A$51.3m; it is close to a "margin back to 110bps" year on today's book (my A$38m to A$39m), so it works as a bad case in money, but at 7.0 times with no dividends (A$1.00) it is a tail, not the central bad case. My bad case is A$1.27 with dividends, inside a range of A$1.12 to A$1.45.
10. The good case: the 12.5 times average at 30 June leans on FY25's 17.7 times, set in a rate-cutting year; on daily prices since 2018 the median is 12.3 times. Either way it needs the rate cycle to turn, which the RBA's forecasts don't assume before 2028 [R1].
11. The buy-back: it bought 8,958,600 shares for A$13.61m to 24 September and nothing since (no notice after 25 September), with 781,660 shares and A$1.39m left [A22][A37].
12. "The ASX company data also shows 18 February 2027" for the HY27 result: I found no such date in the data file [M1]; the date is inferred from last year.
13. Margin history to add: FY21 178bps, FY22 163, FY23 136, FY24 113, FY25 116, FY26 125, and the 2023 forecast of a return to 130 to 140bps that didn't happen [A18][A16][A14][A13][A2].
14. Holders to add: First Sentier fell from 7.46% to 6.09% (24 September notice) [A28]; McKeon kept his 15,000,000 shares on leaving the board on 16 October [A26].

## What I couldn't verify
- Which warehouse facility was renewed by 16 October, at what price, and whether the 12 November facility has been renewed. Nothing has been announced.
- The Q1 FY27 margin (not disclosed) and how much of the September RMBS replaced the expiring warehouses.
- The exact HY27 result date and interim dividend dates (inferred from 2026).
- The basis of the company's A$10m AFG Securities uplift.
- The earnings multiple REA paid for Mortgage Choice; analyst coverage of AFG.
- The fact sheet's NTA figures and its earlier substantial holder history were not re-checked; this file doesn't rely on them.

## Checks
- Not on Cam's excluded list: config/judgement_excluded.csv lists no companies (confirmed by Cam on 8 November 2026).
- No placement-pattern reopening in the last 30 sessions (rulebook section 9): AFG has had no trading halt or share issue in 2026 [A37]; the only big-volume day (18 September, 13.85m shares) was the index exit, with no halt.
- Liquidity: median value traded over the 20 sessions 5 to 30 October 2026 was A$831,489 (volume times close, lowest session A$457,716) [M2]. Two sessions at 10% of that is A$166,298; the largest position the sleeve allows (2.5%, about A$2,016) is about 1.2% of that limit.

## Sources
ASX announcements (AFG), read from the ASX announcement list on 8 November 2026:
- [A1] 2026-08-20, AFG Announces FY26 Results and AGM Date: Appendix 4E and Annual Report 2026 (document 03127201): https://announcements.asx.com.au/asxpdf/20260820/pdf/072ys01p4c9r18.pdf
- [A2] 2026-08-20, AFG FY26 Results Investor Presentation (03127203): https://announcements.asx.com.au/asxpdf/20260820/pdf/072ys497qf1h68.pdf
- [A3] 2026-08-20, AFG FY26 Results Market Release (03127204): https://announcements.asx.com.au/asxpdf/20260820/pdf/072ys6drfyv0qy.pdf
- [A4] 2026-10-16, AFG 2026 AGM Address to Shareholders, with presentation (03153061): https://announcements.asx.com.au/asxpdf/20261016/pdf/075d30txwr97cp.pdf
- [A5] 2026-10-16, AFG 2026 AGM Results (03153415): https://announcements.asx.com.au/asxpdf/20261016/pdf/075dyhpq552tgf.pdf
- [A6] 2026-10-13, AFG Mortgage Index Q1 FY2027 (03151656): https://announcements.asx.com.au/asxpdf/20261013/pdf/07581xlgl6tgnb.pdf
- [A7] 2026-09-17, AFG prices new Prime RMBS transaction (03140769): https://announcements.asx.com.au/asxpdf/20260917/pdf/0746rsssnk5695.pdf
- [A8] 2026-02-13, AFG RMBS Issue (03059814): https://announcements.asx.com.au/asxpdf/20260213/pdf/06w85y3wj50ctz.pdf
- [A9] 2026-02-18, AFG Appendix 4D and FY26 Half Year Financial Report (03061409): https://announcements.asx.com.au/asxpdf/20260218/pdf/06wf7ryr1fdvrb.pdf
- [A10] 2026-02-18, AFG FY26 Half Year Results Investor Presentation (03061412): https://announcements.asx.com.au/asxpdf/20260218/pdf/06wf7z8pjhw54h.pdf
- [A11] 2026-02-18, Dividend/Distribution - AFG (03061410): https://announcements.asx.com.au/asxpdf/20260218/pdf/06wf7v272g0cy6.pdf
- [A12] 2025-08-27, AFG Announces FY25 Results and AGM Date: Appendix 4E and Annual Report 2025 (02985960): https://announcements.asx.com.au/asxpdf/20250827/pdf/06nd3rl7yc7y5b.pdf
- [A13] 2025-08-27, AFG FY25 Results Investor Presentation (02986052): https://announcements.asx.com.au/asxpdf/20250827/pdf/06nd9zsnc27sx1.pdf
- [A14] 2024-08-30, AFG FY24 Results Investor Presentation (02846942): https://announcements.asx.com.au/asxpdf/20240830/pdf/0678lphc24qphq.pdf
- [A15] 2024-02-29, AFG 1H FY24 Investor Presentation (02779508): https://announcements.asx.com.au/asxpdf/20240229/pdf/060z1n49bvnchs.pdf
- [A16] 2023-08-25, AFG FY23 Results Investor Presentation (02702388): https://announcements.asx.com.au/asxpdf/20230825/pdf/05t1phf3r207x1.pdf
- [A17] 2023-02-24, AFG 1H FY23 Investor Presentation (02635667): https://announcements.asx.com.au/asxpdf/20230224/pdf/45lz9jjblykn20.pdf
- [A18] 2022-08-26, AFG FY22 Investor Presentation (02558752): https://announcements.asx.com.au/asxpdf/20220826/pdf/45d9txnndxh6bz.pdf
- [A19] 2021-08-27, AFG Announces FY21 Results and AGM Date: Annual Report 2021 (02413199): https://announcements.asx.com.au/asxpdf/20210827/pdf/44zt5yw7kvq6lb.pdf
- [A20] 2019-08-23, Appendix 4E and 2019 Annual Report (02137281): https://announcements.asx.com.au/asxpdf/20190823/pdf/447rw2hqv2k3gs.pdf
- [A21] 2026-06-02, On-Market Share Buyback (03100119): https://announcements.asx.com.au/asxpdf/20260602/pdf/0706ydm75y4m0f.pdf
- [A22] 2026-09-25, Update - Notification of buy-back - AFG (03143674): https://announcements.asx.com.au/asxpdf/20260925/pdf/074hmfbrj8zt7f.pdf
- [A23] 2026-10-02, Notification of cessation of securities - AFG (03148082): https://announcements.asx.com.au/asxpdf/20261002/pdf/074wpt8yt99ww0.pdf
- [A24] 2026-10-22, Notification regarding unquoted securities - AFG (03155676): https://announcements.asx.com.au/asxpdf/20261022/pdf/075mtwrqzgr2f0.pdf
- [A25] 2026-09-10, Director Appointment/Resignation (McKeon to retire) (03137894): https://announcements.asx.com.au/asxpdf/20260910/pdf/073y1b2yj27fpn.pdf
- [A26] 2026-10-19, Final Director's Interest Notice (McKeon) (03154073): https://announcements.asx.com.au/asxpdf/20261019/pdf/075hd6h2hftv5k.pdf
- [A27] 2026-09-04, S&P DJI Announces September 2026 Quarterly Rebalance (03136141): https://announcements.asx.com.au/asxpdf/20260904/pdf/073rbz4q8nrckg.pdf
- [A28] 2026-09-24, Change in substantial holding (First Sentier) (03143573): https://announcements.asx.com.au/asxpdf/20260924/pdf/074h6gqdc160pn.pdf
- [A29] 2026-08-31, Change in substantial shareholding from AEF (03133062): https://announcements.asx.com.au/asxpdf/20260831/pdf/073h6bt27s6x1q.pdf
- [A30] 2026-08-25, Change of Director's Interest Notice (Flynn) (03129717): https://announcements.asx.com.au/asxpdf/20260825/pdf/0735yx9q51yqfb.pdf
- [A31] 2026-09-02, Change of Director's Interest Notice (Muirsmith) (03134418): https://announcements.asx.com.au/asxpdf/20260902/pdf/073lt2x6zf9l4r.pdf
- [A32] 2026-09-07, Change of Director's Interest Notice (King) (03136589): https://announcements.asx.com.au/asxpdf/20260907/pdf/073t89nhwmv7b6.pdf
- [A33] 2026-09-08, Change of Director's Interest Notice (Carter) (03137105): https://announcements.asx.com.au/asxpdf/20260908/pdf/073vppw0k8ynbv.pdf
- [A34] 2026-09-09, Change of Director's Interest Notice (Flynn) (03137375): https://announcements.asx.com.au/asxpdf/20260909/pdf/073wkxt54rqk1c.pdf
- [A35] 2026-09-10, Change of Director's Interest Notice (Carter) (03137903): https://announcements.asx.com.au/asxpdf/20260910/pdf/073y1y897cvxvh.pdf
- [A36] 2026-10-23, Change of Director's Interest Notice (Flynn) (03155975): https://announcements.asx.com.au/asxpdf/20261023/pdf/075nsqgqlf7h4g.pdf
- [A37] ASX announcement list for AFG, 2026 (latest item 23 October 2026 when read on 8 November): https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=AFG&timeframe=Y&year=2026

Reserve Bank of Australia:
- [R1] Statement on Monetary Policy, November 2026, Overview (cash rate raised 25bps to 4.85%; housing prices in September almost 5% below the March peak; forecast cash rate path): https://www.rba.gov.au/publications/smp/2026/nov/overview.html
- [R2] Media release 26-12, 5 May 2026 (cash rate raised to 4.35%): https://rba.gov.au/media-releases/2026/mr-26-12.html
- [R3] RBA statistical table F1.1, interest rates and yields, money market, monthly (repo copy data/rates/rba_f1_1.csv): cash rate target and one-month bank bill averages, 2022 to October 2026.

Secondary source:
- [S1] The Adviser, "Mortgage Choice acquisition fair and reasonable: report" (independent expert range A$1.66 to A$1.97, REA's A$1.95 offer, about A$244m): https://www.theadviser.com.au/breaking-news/41547-mortgage-choice-acquisition-fair-reasonable-report

Data in the repo:
- [M1] data/research_data/asx_company.json (ASX company data, fetched 7 November 2026 21:46 UTC): AFG last trade A$1.565 (6 November), close A$1.57 (5 November), 263,733,615 shares; Resimac, Pepper Money and Liberty price to earnings.
- [M2] data/norgate/universe/prices_2018.csv.gz to prices_2026.csv.gz (Norgate daily prices to 30 October 2026).
- [M3] data/fx/fx_daily.csv (NZ$1 = A$0.806387 on 6 November 2026).
