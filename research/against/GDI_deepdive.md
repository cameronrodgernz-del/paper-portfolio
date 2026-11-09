# GDI Property Group (ASX:GDI): independent deep dive by the second model

Cam ran the prompt below in a second model on 10 November 2026 (docs/RESEARCH_PROCESS.md step 4; the prompt's own notes are in research/against/GDI_deepdive_prompt.md). The answer came back as a 12-page PDF, saved as research/against/GDI_deepdive.pdf. The text under "The answer" is extracted from it with pdftotext -layout so it can be searched. Claude's view on each point is in research/debate/GDI.md.

## The prompt


I'd like a deep dive on GDI Property Group (ASX: GDI), done to the standard of a professional analyst who goes well past the news: the company's filings and the notes to its accounts, substantial holder notices, directors' interest notices, and published property market research. I want your own view, worked from the evidence. Others have looked at GDI and reached different answers. You haven't seen their work, and that's deliberate. Your answer will be checked point by point against theirs, so be specific, show your working and source every fact.

#### The setting

- Today is 10 November 2026. GDI last traded at A$0.64 (bid A$0.63, ask A$0.645). It has about 539.2 million stapled securities on issue, a market value of about A$345m, and trades a median of about A$175,000 a day.
- GDI is a stapled company and trust, managed internally. It owns Perth CBD offices (Westralia Square WS1 and WS2, 197 St Georges Terrace, 5 Mill Street, and the empty 1 Mill Street), an empty building in East Perth, two Perth CBD car parks, and a consolidated share of a Townsville office trust. It manages unlisted property trusts for wholesale investors, and owns half of a mining-town accommodation business (the Co-living JV) with Tulla Group.
- The latest reports are the FY26 results (24 August 2026), the 2026 annual report (29 September 2026) and the AGM addresses (5 November 2026). The next result, for the half to 31 December 2026, is due about mid-February 2027, with the December building valuations.
- This is for a simulated portfolio. The position would be small (about A$2,250), held for up to about three years, and judged on what it's worth on 31 August 2028, counting the distributions received by then. Allow about 2.6% for costs in total (brokerage both ways, the bid-ask spread and a currency fee).
- The portfolio only buys if all three of these hold:
  1. the bad case is no more than 30% below today's price;
  2. the middling case is above today's price by at least 1.5 times the bad case's fall, and never by less than 15%;
  3. the expected gain after costs, weighting each outcome by its chance, is at least about 12.9% over the period to 31 August 2028.

  A "special situation" (for example a holder building toward a bid, or a sale or wind-up of the assets) skips the first two rules but must still pass the third, with its bad case set at the value if nothing happens.

Please check every number above against the filings and correct any that are wrong.

#### What I need answered

##### 1. What the price assumes
From the price, net tangible assets (NTA), funds from operations (FFO), the distribution and the cash GDI actually keeps, work out what today's price implies: the yield on cash earnings, the discount to NTA, and the cap rate the market is putting on the buildings once debt and the other assets are taken out. Show the arithmetic. Compare it with the listed office peers on the same measures at current prices: at least Centuria Office REIT, Abacus Group, Growthpoint and Dexus.

##### 2. Cash earnings, not FFO
FFO counts rent at its face value through rent-free periods. I want the cash GDI keeps.
- For each half from FY24 to FY26, take FFO and subtract rent-free given, fit-outs and floor subdivisions, maintenance spending and leasing fees. Use GDI's own share: FFO counts only the distributions and fees GDI receives from its consolidated trusts, so don't deduct those trusts' own spending. Say which note or page each figure comes from.
- Check what's in FFO that won't repeat or isn't cash: one-off funds management fees (disposal and performance fees), GDI's share of the Co-living JV's income tax added back, and how much of the JV's contribution actually came back to GDI in cash.
- Then estimate cash earnings for FY27 and FY28, and the yearly rate the market will be pricing in August 2028. Explain each step: rent-free still to run off from the FY25 and FY26 leasing, the lease expiries ahead, fit-out spending, and interest.

##### 3. The distribution
- The distribution has been 5.0 cents a year since FY23. The board seeks to pay 5.0 cents in FY27, which "may be paid wholly or partly out of capital". For FY24 to FY26, how much of it was covered by operating cash flow, and what paid for the rest (asset sales, debt)?
- What's the chance it's cut before August 2028, and what would trigger a cut? What happened to the prices of Australian office REITs that cut distributions from 2023 to 2026 (Abacus's cut from 8.5 cents to 6.7 cents for FY27 is one), in the days after and six months on?

##### 4. The buildings and their values
- For each building: book value, cap rate, date of the last independent valuation, occupancy, weighted average lease expiry, main tenants and their lease end dates, and the share of income expiring in each year from FY27 to FY30. The expiry charts are in the FY26 results presentation and the property tables in the annual report.
- Test the cap rates (WS1 and WS2 are at 6.50%) against Perth CBD evidence: prime yields from Knight Frank, JLL, CBRE, Colliers or Cushman & Wakefield, and every Perth CBD office sale since 2024 with a published yield. Is there a sound reason for WS1 to be valued at the tight end of the range, for example its WA Government lease?
- Estimate NTA at 30 June 2028 under the cap rates you think plausible, and say what the 31 December 2026 valuations are likely to show.
- The Perth office market: vacancy, new supply to 2029, face rents, and incentives (prime net incentives have been reported at about 47%). Which way are incentives heading, and what does that mean for re-leasing 197 St Georges Terrace, 5 Mill Street and WS1 from FY28?

##### 5. Debt, hedging and refinancing
- Read the derivatives note in the FY26 annual report exactly. For each hedge, give the amount, the rate, the start and end dates, and any right for the bank to cancel or extend it. Then work out, in plain English, in what interest rate conditions the bank would use a cancellation right, and so how much of GDI's debt is likely to be hedged in FY28 and FY29.
- Estimate net interest for FY27, FY28 and FY29 at current market rates (use current Australian swap rates or, failing that, the RBA's bank bill and three-year bond yields), and show the effect per security.
- The facility maturities (one tranche falls due in February 2028), the covenants (loan to value and interest cover), the headroom under your cap-rate scenarios from section 4, and what refinancing in 2027 and 2028 is likely to cost.

##### 6. The Co-living JV and funds management
- The Co-living JV: its contracts and customers, the Moranbah take-or-pay arrangement ending in March 2027 and what replaces it, its debt, how much cash it has paid to GDI, and the consent needed before it can pay out profits. How exposed is it to Queensland coal and mining activity?
- Funds management: the base fees on the remaining funds against the one-off fees, and what's left after the Autoleague sales.

##### 7. Why the gap to NTA might close, or not
- GDI's price-to-NTA at each year end since 2017, and the history of its earlier buy-backs and asset sales. Did they close the gap?
- The board's stated plan:
  - the 5% buy-back: how much has been bought, at what prices, and when it last bought;
  - the A$100m of non-core sales: what's been sold, what's left, and which assets are the likely candidates;
  - joint ventures over core buildings;
  - the Mill Green redevelopment.
- Australian REITs that traded well below NTA between 2018 and 2026 and then closed the gap through sales, wind-ups, buy-backs or takeovers: what made the difference, and does GDI have those features?

##### 8. Who owns it and what they might do
- Robert Rockefeller and his entities went from about 5% to about 10.1% between April and September 2026. List every notice with its dates, prices and volumes. How much of GDI's total traded volume in 2026 was his buying? Has he said what he intends? What has he done with his other ASX holdings: board seats, meeting requisitions, bids or sales?
- The other substantial holders (Paradice, Renaissance Property Securities, Salt Funds Management and Pathfinder, and any others): their recent changes, and what they tend to do.
- The new chair, James Warburton (from 25 August 2026): his record at Seven West Media, APN Outdoor and Supercars, especially any sales, mergers or capital returns he led, and his own buying. The managing director's on-market sale in May 2026, his holding, and how his performance rights pay out.
- Could anyone bid, and at what price would a bid make sense to them? Take account of the takeover rules (the 20% threshold, and the 3% "creep" every six months allowed to holders at 19% or more).

##### 9. Anything else
Anything else in the accounts, the notes or the history that makes GDI look better or worse than it seems: related-party dealings, the valuers used, accounting choices, guarantees, commitments, or legal matters.

#### What I want back

1. One paragraph up front: buy, wait or reject at A$0.64, and the main reason.
2. The strongest case for buying and the strongest case against, each in its best honest form. For each argument on one side, say whether the other side answers it.
3. Your outcomes for 31 August 2028: the price then, plus the distributions received by then. Say which payments you count (the interim and final usually go ex in late December and late June, and are paid in late February and late August). Give a bad, a middling and a good case, plus a worse case if you think one is needed. For each, say what has to happen, the value, and its chance. The chances should add to 100%. Then show the expected gain after costs, and say plainly whether GDI passes each of the three rules at A$0.64, both as an ordinary pick and as a special situation.
4. The highest price at which you'd buy, and the events that would change your mind either way, with the dates they're due. For example: the December 2026 valuations, the February 2027 result, a distribution decision, any hedging or refinancing news, or a substantial holder notice.
5. A list of every source, with links. Use primary sources wherever you can: GDI's ASX announcements (asx.com.au and announcements.asx.com.au) and website, peers' filings, the RBA, and property agents' published research. Use broker notes and press only as pointers, and say when you have. Mark anything you couldn't verify.

Some ground rules:
- Be fair. If one side's case is thin, say so.
- Show the working for every figure you calculate.
- Write in plain English, and explain any property term the first time you use it. Use Australian dollars throughout.
- Aim for about 3,500 words, plus tables and the sources list.

## The answer

```text
 GDI Property Group (ASX: GDI): deep dive at A$0.64
 Prepared 10 November 2026 for a simulated portfolio. Judged on value at 31 August 2028 plus distributions
 received. All figures are Australian dollars. Bracketed codes such as [F1] point to the source list at the end.
 This is research, not personal financial advice.


 1. The answer: wait
 Wait at A$0.64. I would buy at A$0.615 or below. On my numbers GDI fails two of the three rules today: the
 expected gain to 31 August 2028 is about 8.8% after costs against the 12.9% needed, and the middling case
 (+17%) is less than 1.5 times the bad case's fall (-13%). The main reason is that A$0.64 is already what a 5.0 cent
 distribution supports, and that distribution is not paid for by cash the business keeps. GDI's own cash earnings were
 3.2 cents a security in FY26 against 8.24 cents of funds from operations (FFO, the property industry's profit
 measure, which counts rent at face value through rent-free periods). Since the accounts were signed the RBA cash
 rate has gone to 4.85%, GDI's main interest rate hedge can be cancelled by the bank on 1 January 2028, and the
 two Westralia Square buildings sit in the books at a 6.50% capitalisation rate (cap rate: a building's yearly income
 divided by its value) when the two Perth CBD investment sales since mid-2024 were struck at 8.2% and 8.3%.
 Against that, the price implies about 10% on the buildings, which is harsher than those sales, so there is real value
 underneath, and a single holder bought about 28% of this year's traded volume to reach 10.1%. That is enough to
 keep GDI on the list and not enough to pay today's price.

 Checking the numbers in the brief
Item                    Brief                    What the filings show
Securities on issue     About 539.2m             Correct. 539,196,501 quoted at 6 Nov 2026; a further 6,045 bought back on 14 Oct await
                                                 cancellation, leaving 539,190,456 [F9, F10]. It was 539,822,485 at 30 June [F1].
Market value            About A$345m             Correct: 539.19m x A$0.64 = A$345.1m.
Median daily turnover   About A$175,000          Could not reproduce. Yahoo Finance daily data gives a median of about A$233,000 for
                                                 2026 to date and A$272,000 over the last 60 trading days [M9]. Either figure makes a
                                                 A$2,250 position trivial.
Rockefeller             5% to 10.1%, April to    Correct (5.01% on 1 April, 10.11% on 14 September). His first notice also shows buying
                        September                from 13 January, and about 20.4m securities (3.8%) held before that [H1].
MD's sale               May 2026, on market      Correct: 500,000 sold on 29 May at an average A$0.602 (A$301,000), lodged 3 June [D1].
Debt facility           One tranche due Feb      Correct. The headline A$426.5m includes a A$5.0m bank guarantee; the usable limit is
                        2028                     A$421.5m with A$343.3m drawn [F1, F12].
Hedge rate              Not given                The results slides label the swaps "BBSY@3.43%". The audited note says 3.72%. I use the
                                                 note [F1 note 28, F2 p12].
Everything else                                  Price, assets, report dates, 5.0 cent history, 6.50% cap rates, the March 2027 Moranbah
                                                 date and the Abacus cut all check out.



 2. The case for buying and the case against
Argument for buying                                                    Does the other side answer it?
The price implies about 9.7% to 10.4% on the buildings (section 5),    Only partly. At 8.25% the lenders' loan-to-value test would read 45%
against 6.8% in the books and 8.2% to 8.3% in actual sales. Even if    to 47% against a 50% limit, so the banks would be steering, not
every building were marked to 8.25%, net tangible assets (NTA,         equity. And the discount has sat between 46% and 53% at four
assets less debts per security) would be about A$0.91.                 straight year ends.
Cash earnings are turning: -1.9 cents in FY24, 0.4 cents in FY25, 3.2 Mostly. Rent-free given is still rising (A$16.2m in FY26), interest is
cents in FY26, and 4.1 cents annualised in the June 2026 half. The    going up, the Autoleague fees end, and 27% of 197 St Georges
fit-out programme is largely done.                                    Terrace expires in FY28. I get about 3.7 cents for FY28: better, still
                                                                      under 5.0.
Perth has no new towers before 2030 or 2031, vacancy is falling and Not yet in the numbers. Incentives rose in 2025 (45% to 47%) and
face rents are rising. Knight Frank expects incentives to ease from net effective rents fell 0.4% under the same supply story [M1].
47% to about 40% by 2030.




GDI Property Group deep dive, 10 November 2026                                                                                         Page 1
Argument for buying                                                     Does the other side answer it?
A 10.1% holder kept buying up to A$0.645, the new chair says his        Thin so far. Rockefeller has stated no intention and lodged nothing
job is to close the gap, a 5% buy-back is open, A$100m of non-core      since 14 September. The buy-back has bought 0.12% in two months
assets are for sale and joint ventures over core buildings are on the   and nothing since 14 October. The chair bought A$49,623 of stock.
table.                                                                  The MD sold.
There are fees the market may not be counting: about A$6.2m from        Fair, but both are one-offs. The A$18m is an assumption inside an
the last Autoleague sales lands in FY27, and the goodwill test          impairment test, not guidance, and depends on Broadmeadow being
assumes an A$18m performance fee in FY28, worth 3.3 cents a             rezoned and sold.
security [F1 note 12, F13].

Argument against buying                                                 Does the other side answer it?
The 5.0 cent distribution is above cash earnings and has been paid      Partly. The gap is now A$8m to A$12m a year and GDI has A$78m
partly out of capital: debt funded it in FY24 and FY25, Autoleague      undrawn plus the sale programme, so it can pay through FY28 if
sale proceeds in FY26.                                                  lenders are relaxed. It is also only 61% of FFO.
Rates: the cash rate is 4.85%, the cap steps up from 3.75% to           Yes on size. I estimate net interest rises from A$20.2m to about
4.50% in January 2027 and the bank can cancel the A$175m swap           A$22.8m by FY29, which is 0.5 cents a security. Painful against 3 to
in January 2028.                                                        4 cents of cash earnings, not fatal.
Book values look full. Westralia Square at 6.50% matches Cushman        Partly. Half of WS1 is let to the WA Government to FY34. And the
& Wakefield's premium yield; A-grade is 7.85% and Knight Frank's        price already assumes worse than any agent benchmark. The risk is
prime average is 7.90% [M2, M5].                                        the path (falling NTA, rising LVR), not the end value.
Mill Green has a wall of expiries: at 197 St Georges Terrace about      Partly. These are small suites, GDI has leased well for three years
27% in FY28, 12% in FY29 and 20% in FY30; at 5 Mill Street 21%,         and tenants are asking for early extensions [F4]. But each renewal
34% and 24%.                                                            costs fresh incentives.
History: GDI paid 7.75 cents on about 5.3 cents of FFO until it cut     No good answer. The board and chair have changed since; the habit
35% in December 2022, and the last 5% buy-back, renewed three           of paying above earnings has not.
times, bought 2.4% in four years.



 3. Outcomes for 31 August 2028
 Distributions I count: the December 2026 half (ex about 30 December 2026, paid late February 2027), the June
 2027 half (paid end of August 2027), the December 2027 half (paid late February 2028) and the June 2028 half (ex
 late June 2028, paid about 31 August 2028; the last two August payments were on 29 August 2025 and 31 August
 2026). That is four payments, 10.0 cents if nothing changes. A buyer after the 30 December ex date gets three.

Case         Chanc     What has to happen                                             Price      Distributio   Total        Against A$0.64
             e                                                                                   ns
Worse        7%        Rates stay above 5%, WA slows, valuers move to 8.75% or        A$0.35     6.25c         A$0.41       -35.5%
                       more, the loan-to-value test nears 50% and GDI raises
                       equity or sells under pressure. Distribution suspended in
                       FY28.
Bad          28%       December 2026 and June 2027 valuations take NTA to            A$0.47      8.5c          A$0.555      -13.3%
                       about A$0.97, the swap is cancelled, re-leasing at Mill
                       Green is slow, and the board resets the distribution to about
                       3.5 cents with the August 2027 result. Stock trades near half
                       of NTA.
Middling     45%       The 5.0 cents is held with help from non-core sales. NTA       A$0.65     10.0c         A$0.75       +17.2%
                       drifts to about A$1.12. Cash earnings reach about 4 cents.
                       The buy-back stays small. Rockefeller sits between 10%
                       and 15%. The market still prices the distribution at 7.5% to
                       8%.
Good         20%       One or more of: A$100m of sales near book and a real          A$0.85      10.5c         A$0.955      +49.2%
                       buy-back; a joint venture over a core building near book; the
                       Broadmeadow fee; rate cuts in 2028; or a bid in the A$0.85
                       to A$0.95 range. Stock re-rates to about 0.7 times an NTA
                       of A$1.20. Distributions are 10.0 cents plus a small special.
Expected     100%      0.07 x 0.4125 + 0.28 x 0.555 + 0.45 x 0.75 + 0.20 x 0.955 =                             A$0.713      +11.4% before
                       A$0.713                                                                                              costs, +8.8%
                                                                                                                            after 2.6%




GDI Property Group deep dive, 10 November 2026                                                                                         Page 2
Rule                                      Test at A$0.64                                                                    Result
1. Bad case no more than 30% below        Bad case is -13.3%. (The worse case is -35.5% but carries a 7% chance; I          Pass
price                                     treat it as the tail, not the bad case.)
2. Middling case at least 1.5 times the   Needs 1.5 x 13.3% = 19.9%. Middling is +17.2%.                                    Fail, narrowly
bad fall, and at least 15%
3. Expected gain after costs at least     +8.8%                                                                             Fail
about 12.9%
As a special situation (rules 1 and 2     If nothing happens the value is the middling case or lower, about A$0.75. I   Fail
skipped)                                  put the chance of a bid by August 2028 at about 10% and of a material asset
                                          realisation at about 20%; both are already in the good case. Expected gain is
                                          the same +8.8%.



 4. The price I would pay, and what would change my mind
 Holding the four outcomes fixed, rule 3 is the binding one: A$0.713 / 1.155 = A$0.617. At A$0.615 the expected gain
 after costs is 13.3%, the bad case is -9.8% and the middling case +22.0%, so all three rules pass. After the
 December ex date the limit drops by the 2.5 cents no longer received, to about A$0.59. For reference, Rockefeller's
 34.2m securities this year cost an average A$0.615 and the buy-back has paid A$0.615 to A$0.635.

When                 Event                                            What I would look for
8 Dec 2026           RBA decision                                     Another rise to 5.10% pushes the bad case up; a clear pause helps
                                                                      a little.
Mid to late Dec      December-half distribution declared; ex about    Anything other than 2.5 cents is a reject signal.
2026                 30 Dec
1 Jan 2027           Cap on A$100m steps from 3.75% to 4.50%          Already in my numbers.
Mid to late Feb      Half-year result and December valuations         Buy signal: NTA A$1.18 or better with the loan-to-value test under
2027                 (WS1, WS2, car parks, Townsville)                38%. Reject signal: NTA under A$1.10, or the test above 42%. Also
                                                                      rent-free, fit-out spend, any change to hedges, news on Stanmore.
By 31 Mar 2027       Moranbah take-or-pay ends unless Stanmore        Small either way (about 0.3 cents).
                     extends
Feb to Jun 2027      Extension of the February 2028 tranche           It becomes a current liability from February 2027. A higher margin or
                                                                      tighter covenants would be a reject signal.
Late Aug 2027        FY27 result, FY28 distribution guidance, June  The likeliest date for a cut. A held 5.0 cents with cash cover above
                     valuations of Mill Green; buy-back ends 23 Aug 80% would move me to buy at market.
                     2027
31 Dec 2027 and 1 4.50% cap expires; bank's first right to cancel     New hedging at market rates would lift interest by about A$2m a
Jan 2028          the swap                                            year.
Any day              Substantial holder notice from Rockefeller (next Buy at up to A$0.64 if he states an intention, seeks a board seat or
                     due at about 11.1%); non-core or core asset      passes 15%, or if GDI sells a core interest within 10% of book. A
                     sale; sale of 256 St Georges Terrace             sale of the Fortescue building near A$200m would be the best new
                                                                      evidence on Perth yields. Reject if he sells.



 5. What the price assumes
Step                                              A$m            Working
Market value                                      345.1          539.19m x A$0.64
Add GDI's own net debt                            333.6          Syndicated facility 343.3 less cash 9.8 [F1 notes 6, 17]
Enterprise value                                  678.7
Less other assets at book                         -74.3          Co-living JV 42.1; 43.68% of Townsville trust net assets 14.0; 47.19% of
                                                                 Autoleague trust net assets 14.7 (returned as cash in August); loans to
                                                                 funds 3.5 [F1 notes 8, 14, 34]
Implied value of wholly owned buildings and car   604.3          Against A$921.3m in the books: 66 cents in the dollar
parks
Implied cap rate on face income                   9.7%           Property Division FFO 58.4 / 604.3
Implied cap rate on the valuers' basis            10.4%          Book average 6.8% / 0.656
Implied yield on cash income                      7.0%           (58.4 less rent-free 16.2) / 604.3




GDI Property Group deep dive, 10 November 2026                                                                                          Page 3
                     Price 9       NTA                 Price /         Earnings yield               Distribution yield   Book cap    Implied cap rate
                     Nov                               NTA                                                               rate        (rough)
GDI                  A$0.64        A$1.21              0.53            FFO 8.24c: 12.9%. Cash       5.0c: 7.8%           6.8%        9.7% to 10.4%
                                                                       earnings 3.18c: 5.0%
Centuria Office      A$0.895       A$1.66              0.54            FY27 FFO guide 11.3c:        9.0c (cut from       7.04%       About 9.7% if
REIT                                                                   12.6%                        10.1c): 10.1%                    gearing is 40%
                                                                                                                                     (not checked)
Abacus Group         A$0.86        A$1.52 pro          0.57            FY26 FFO 9.08c: 10.6%        6.7c (cut from       6.70%       About 9.3% at
                                   forma                                                            8.5c): 7.8%                      36% gearing
Growthpoint          A$2.05        A$3.05              0.67            FY27 FFO guide 22.6c to      18.4c: 9.0%          Not         Not calculated
                                                                       23.5c: 11.2%                                      checked
Dexus                A$5.90        A$8.92              0.66            FY27 AFFO guide 37.5c        37.0c: 6.3%          Not         Not calculated
                                                                       to 39.5c: 6.5%                                    checked

 GDI is priced like Centuria Office REIT on FFO and on discount to NTA. The difference is underneath. Dexus reports AFFO, which is
 after incentives and upkeep; on that like-for-like measure Dexus yields 6.5% and GDI 5.0%. And GDI is the only one of the five paying
 well above its cash earnings. Sources: [P1 to P5], prices from [M9].



 6. Cash earnings, not FFO
A$m, GDI share                            1H24           2H24            1H25          2H25       1H26       2H26        FY24       FY25      FY26
FFO                                       13.1           16.4            16.5          19.1       21.3       23.2        29.6       35.6      44.5
Rent-free given                           -2.3           -6.3            -6.4          -6.6       -8.3       -7.9        -8.6       -13.0     -16.2
Fit-outs and floor subdivisions           -11.0          -14.8           -10.7         -7.0       -5.9       -3.4        -25.8      -17.6     -9.4
Maintenance spending                      -0.6           -0.5            -0.4          -0.4       -0.4       -0.4        -1.1       -0.7      -0.8
Leasing fees                              -2.0           -2.1            -0.6          -1.5       -0.6       -0.3        -4.1       -2.1      -0.9
Cash earnings                             -2.7           -7.3            -1.6          3.6        6.1        11.0        -10.0      2.1       17.2
Cents per security                        -0.5           -1.4            -0.3          0.7        1.1        2.0         -1.9       0.4       3.2

 Where each line comes from: FFO from the directors' report reconciliation; rent-free is "Incentives paid (GDI Property Trust)" in the
 investment property note, which ties to "Non-cash incentives" in the cash flow reconciliation; fit-outs are "Property improvements" in the
 same note (not split between GDI and the consolidated trusts, so slightly overstated); maintenance is "Maintenance capital (GDI
 Property Trust)"; leasing fees are "Lease costs". Second halves are full year less first half [F1 notes 9 and 25, F4, F5, F6, F7, F8].


 What is in FFO that will not repeat or is not cash
Item                           FY26                      Comment
Funds management FFO           A$6.2m                    A$2.0m of outside fees (A$0.59m one-off disposal fee on Bassendean, A$1.41m ongoing)
                                                         plus A$4.2m of fees and distributions from the two consolidated trusts, mostly Autoleague,
                                                         now sold. Ongoing level is about A$2.0m to A$2.5m. FY27 gets about A$6.2m of final
                                                         Autoleague disposal and performance fees [F1 note 2 and 23, F13].
Co-living JV tax               A$1.7m                    FFO takes GDI's share of the JV's profit before tax. The JV pays the tax; FFO adds it back
                                                         (A$1.5m in FY25, A$1.2m in FY24) [F1 s7.2].
Co-living JV cash              A$5.2m of                 Only 55% of the JV's FFO contribution reached GDI as cash; the rest stayed in the JV,
                               A$9.45m                   which also borrowed to buy Moranbah. FY25: A$4.6m of A$6.5m [F1 note 14, cash flow].
Loan set-up costs              A$1.2m                    Amortised set-up fees are left out of FFO interest. Cash paid was A$0.84m in FY26 and
                                                         A$1.1m in FY24 [F1 note 23].


 My estimate for FY27 and FY28
A$m                               FY26           FY27            FY28           Reasoning
Property Division FFO             58.4           62.0            62.5           June-half run rate was A$58.8m. Add fixed rent reviews and the last WS2
                                                                                and 197 St Georges Terrace leases. FY28 gains are offset by downtime
                                                                                on the 27% of 197 that expires.
Funds management                  6.2            8.4             2.2            FY27 includes A$6.2m of final Autoleague fees. No Broadmeadow fee
                                                                                assumed.
Co-living JV                      9.5            10.5            10.5           Full year of Moranbah and the Norseman rooms, less higher JV interest.
                                                                                Moranbah contract risk from April 2027.
Net interest                      -20.2          -19.9           -21.5          Section 9.



GDI Property Group deep dive, 10 November 2026                                                                                                      Page 4
A$m                             FY26       FY27        FY28     Reasoning
Corporate costs                 -10.1      -10.4       -10.7
FFO                             44.5       50.6        43.0     9.4 cents and 8.0 cents
Rent-free given                 -16.2      -15.0       -13.5    GDI does not say how its incentives are split between up-front rent-free
                                                                and abatements spread over the lease. The steady climb from A$8.6m to
                                                                A$16.2m as buildings filled suggests much of it runs for the life of the
                                                                leases, so I let it fall slowly. New FY28 renewals add fresh incentives.
Fit-outs                        -9.4       -6.0        -7.0     Programme winding down; FY28 re-leasing at Mill Green. Excludes Mill
                                                                Green Stage 1A, whose cost GDI has not disclosed.
Maintenance and leasing         -1.7       -1.6        -2.5
fees
Cash earnings                   17.2       28.0        20.0     5.2 cents (4.0 cents without the one-off fees) and 3.7 cents

 If the JV is counted at the cash it pays out instead of its pre-tax profit, take off about A$5m a year: 4.3 cents in FY27
 and 2.8 cents in FY28. In August 2028 I expect the market to be looking at a yearly rate of about 8 cents of FFO and
 3.5 to 4.0 cents of cash.


 7. The distribution
A$m                                                FY24        FY25        FY26           Source
Distributions to GDI holders (5.0 cents)           26.6        26.9        27.0           Statement of changes in equity
GDI cash earnings (section 6)                      -10.0       2.1         17.2
Share covered by cash earnings                     None        8%          64%
Consolidated operating cash flow, before any       22.5        23.5        21.6           Cash flow statement. Includes outside investors'
building spend                                                                            share of the two consolidated trusts.
Share covered on that looser measure               85%         87%         80%
Change in syndicated debt drawn                    +42.2       +17.0       -21.0          A$305.1m (June 2023), 347.3, 364.3, 343.3
Sale proceeds, consolidated                        0           20.5        81.3           Autoleague trust sales; GDI owns 47.19%

 So debt paid the gap in FY24 and FY25, and GDI's share of the Autoleague sales paid it in FY26 while also repaying
 A$21m. The Autoleague money is now finished: the last A$12.2m of capital and A$6.2m of fees arrived in August
 2026 [F13].
 Chance of a cut before August 2028: about 30%. Almost none of that is in FY27, where 5.0 cents was restated at
 the AGM on 5 November. The risk sits with the FY28 guidance in August 2027. Triggers, in order: valuations that
 push the loan-to-value test past about 42%; no progress on the A$100m of sales; tighter terms on the February
 2028 tranche; the swap cancellation; or a board decision to put the cash into Mill Green and the buy-back. A cut to
 what cash covers would land at about 3.5 to 4.0 cents.

Cut (announced)                                        Size      Day          5 days        6 months                A-REIT index over 6
                                                                                                                    months
GDI, 7.75c to 5.0c (9 Dec 2022)                        -35%      +0.6%        -1.9%         -11.0%                  -1.6%
Centuria Office, 14.1c to 12.0c (17 Aug 2023)          -15%      -3.5%        -8.8%         -10.9%                  +17.9%
Growthpoint, 21.4c to 19.3c (17 Aug 2023)              -10%      -4.2%        -9.5%         -12.5%                  +17.9%
Dexus, 51.6c to 48.0c (16 Aug 2023)                    -7%       -3.1%        -3.9%         -2.5%                   +14.1%
Centuria Office, 12.0c to 10.1c (15 Aug 2024)          -16%      -2.4%        -4.0%         -8.4%                   +4.0%
Growthpoint, 19.3c to 18.2c (22 Aug 2024)              -6%       +6.2%        +7.9%         +4.8%                   +5.3%
Dexus, 48.0c to 37.0c (20 Aug 2024)                    -23%      -8.9%        -4.1%         +3.5%                   +6.2%
Centuria Office, 10.1c to 9.0c (4 Aug 2026)            -11%      -2.2%        -1.7%         Too soon (-2.2% at 1
                                                                                            month)
Abacus, 8.5c to 6.7c (25 Aug 2026)                     -21%      +2.3%        -1.7%         Too soon (-4.5% at 1
                                                                                            month)

 Price moves only, not adjusted for distributions going ex. The usual pattern is a few per cent on the day and roughly 10% behind the
 sector over six months, with less damage when the cut was expected. Sources: [P1 to P8], prices [M9].




GDI Property Group deep dive, 10 November 2026                                                                                        Page 5
 8. The buildings and their values
Building                Book    Cap         Last outside Occupied          WALE,     Main tenants and lease end            Expiring FY27 / 28
                        A$m     rate        valuation                      years                                           / 29 / 30
WS1, 141 St             401.0   6.50%       31 Dec 2025     100%           6.0       WA Government: 16,347 sqm to          0 / 6 / 15 / 0
Georges Tce                                                                          FY34 and 1,833 sqm to FY33
                                                                                     (printed as "MOW")
WS2, 143 St             105.4   6.50%       31 Dec 2025     100% incl. a   6.6       Arup, 2,598 sqm to FY32               0/0/9/9
Georges Tce                                                 heads of
                                                            agreement
197 St Georges Tce      234.0   7.00%       30 Jun 2026     92%            3.3       Hatch, 2,381 sqm to FY32              3 / 27 / 12 / 20
5 Mill St               54.0    7.25%       30 Jun 2026     93%            2.3       Vix Technology, 737 sqm to            13 / 21 / 34 / 24
                                                                                     FY28
1 Mill St               36.5    8.00%       30 Jun 2026     Empty                    None; held for redevelopment
180 Hay St, East        18.7    8.00%       30 Jun 2025     Empty                    None
Perth
Murray St car park      48.8    6.13%       31 Dec 2025                              Wilson, management agreement
Wellington St car       24.2    6.25%       31 Dec 2025                              Wilson, management agreement
park
235 Stanley St,         40.0    8.75%       31 Dec 2025     86%            2.6       Commonwealth agency, 4,644            20 / 39 / 0 / 0
Townsville (43.7%                                                                    sqm to FY28
owned)

 WALE is the weighted average lease expiry, the average time left on leases. Expiry shares are my reading of GDI's bar charts, good to
 within two or three points; GDI does not print the numbers [F2 pp19 to 28].


 Are the cap rates believable?
Evidence                            Yield                 Detail
GDI books                           6.50% to 7.25%        WS1 and WS2 6.50%, 197 St Georges Terrace 7.00%, 5 Mill Street 7.25%; average
                                                          6.8%
Cushman & Wakefield, Q3 2026        6.50% / 7.85%         Premium 6.50% (from 6.44%), A-grade 7.85% (from 7.69%), prime average 7.29%
                                                          [M5, press report of the firm's MarketBeat]
Knight Frank, Q2 2026               7.90%                 Prime, up 32 points after 21 flat months; secondary 8.95% [M2]
181 St Georges Tce, Apr 2024        6.1%                  A$26.5m, 3,590 sqm, WALE 2.5 years, Charter Hall to Yamamoto [M3]
66 St Georges Tce, Oct 2024         8.2%                  A$75.0m, A$6,664 per sqm, WALE 3.3 years, RF CorVal to Oceania Capital [M2]
1 Nash St, 2026                     8.3%                  A$79.4m, A$6,422 per sqm, WALE 5.5 years, CorVal to Castlerock [M2]
No yield published                                        178 St Georges Tce (A$9.5m, hotel conversion, Jan 2026); 10 Telethon Ave
                                                          (A$72.3m, bought by its occupier). Knight Frank counts no CBD investment sale at
                                                          all in 2025 [M1, M2].
Pending                                                   256 St Georges Tce: 23,050 sqm, fully let to Fortescue, offered at about A$200m
                                                          (about A$8,700 per sqm), now shown as under offer [M6, M7]

 Is there a sound reason for WS1 to sit at the tight end? Some. Half the building is let to the State to FY34, it is full,
 and the WALE is six years. But WS1 is an A-grade building carried at a premium-grade yield and at A$12,277 per
 square metre, against A$6,400 to A$6,700 in the two investment sales and about A$8,700 asked for the Fortescue
 building. I think 6.75% to 7.25% is defensible for WS1 and WS2, which is one or two valuation steps from here.

Average cap rate on wholly owned            Value A$m         Change per            NTA             Loan-to-value test at A$343m /
assets                                                        security                              A$360m of debt
6.80% (today)                               921                                     A$1.21          37% / 39%
7.05%                                       889               -6c                   A$1.15          39% / 41%
7.30%                                       858               -12c                  A$1.09          40% / 42%
7.90% (Knight Frank prime)                  793               -24c                  A$0.97          43% / 45%
8.25% (the two sales)                       759               -30c                  A$0.91          45% / 47%
8.75%                                       716               -38c                  A$0.83          48% / 50%
9.10%                                       688               -43c                  A$0.78          50% / 52%




GDI Property Group deep dive, 10 November 2026                                                                                                Page 6
 This holds income constant. GDI's own note is a little harsher (25 points costs A$37.9m, or 7.0 cents, across all
 A$963m) and shows the offset: every A$25 per square metre of market rent adds A$35.4m, or 6.6 cents [F1 note
 29]. For 30 June 2028 I use: about A$1.25 to A$1.30 if valuers hold cap rates and rents keep rising; about A$1.12
 as the central case (cap rates out 50 points, rent growth recovering a third of it); about A$0.95 to A$1.00 if valuers
 go to the sales evidence. For 31 December 2026 I expect WS1, WS2 and the car parks to move out by 12.5 to 37.5
 points with some rent offset, and NTA of A$1.15 to A$1.20. Every benchmark has softened since those assets were
 last valued, and the cash rate is 1.25 points higher.

 The Perth office market
Measure                Latest                                                                                        Source
Vacancy                15.4% all grades (July 2026): premium 10.2%, A-grade 16.3%, B-grade 19.2%. JLL: 15.4% in      [F2 p17, M4, M8]
                       Q3, down from 16.0%. Knight Frank: prime now 13.7%, total forecast to reach about 8% by
                       2030.
New supply to 2029     None. Next are 15 The Esplanade (Brookfield, about 50,000 sqm, 2031, under offer) and Lot 4 [M1, M2, F3]
                       Elizabeth Quay (60,000 sqm, planning). CBRE: 10,400 sqm a year over five years against
                       33,000 in the last five.
Face rents             Prime net A$749 per sqm, up 2.8% in a year. Knight Frank forecasts A$935 by 2030.             [M2, M8]
Incentives             Prime 47%, secondary 50%. They rose from 45% to 47% during 2025 and have been flat in         [M1, M2, M8]
                       2026. Knight Frank expects about 40% by 2030.

 An incentive is what a landlord gives to win a tenant: rent-free months, a fit-out or a lower rent for the term. At 47%,
 a A$749 face rent is A$397 in the hand. Incentives have stopped rising and should ease as vacancy falls, but slowly.
 For the FY28 expiries at 197 St Georges Terrace and 5 Mill Street I assume 40% to 45%, so each renewal still costs
 about two years of rent on a five-year lease. WS1 has little to re-let before FY29. GDI's workaround is to pay for the
 fit-out itself and give less rent-free, which moves the cost from one line of section 6 to another.


 9. Debt, hedging and refinancing
Hedge (note 28, 30 June     Amount             Rate                              Start              End              Bank's rights
2026)
Interest rate cap with a    A$100m             GDI pays the bank bill rate,      Replaced a 4.25%   December         None stated
floor                                          never more than 3.75% and         cap that ended 1   2026
                                               never less than 2.65%             July 2025
Forward-start cap           Not stated in      Never more than 4.50%             January 2027       12 months, so    None stated
                            the note; the                                                           December
                            results chart                                                           2027
                            shows A$100m
Callable swap               A$175m             3.72% fixed                       Not stated; in     January 2031     The bank may
                                                                                 place                               cancel on 1 January
                                                                                                                     2028, 2029 or 2030.
                                                                                                                     No right to extend is
                                                                                                                     stated.

 A year earlier the note showed A$100m at 3.39% and A$75m at 3.49%, ending January 2030, cancellable from 1
 January 2027 [F5]. So during FY26 GDI bought one more year of certainty and paid for it with a higher rate. In plain
 English: under the swap GDI pays 3.72% and the bank pays GDI the floating rate. The bank cancels when floating
 rates are above 3.72%, because that is when the swap is costing it money. That is also exactly when GDI needs it. If
 rates fall below 3.72% the bank keeps the swap and GDI pays above market until 2031. One-month bank bills are
 4.81% and three-year swaps about 4.75% [M10, M11], so rates would have to fall by more than a full point by
 January 2028 for the swap to survive.

                                 FY26                 FY27               FY28                             FY29
Share of A$343m debt hedged      80% at June          80%                80% to December, then none:      None (51% only if rates fall
                                                                         about 40% on average             below 3.72%)
Average base rate paid           About 3.7%           4.07%              4.54%                            4.90%
Net interest, A$m                20.2                 19.9               21.5                             22.8
Cents per security               3.75                 3.69               3.99                             4.22




GDI Property Group deep dive, 10 November 2026                                                                                       Page 7
 Assumptions: debt of A$345m, bank bills at 4.85% to 4.90%, and an all-in spread of 1.83 points that I backed out of FY26 (A$20.1m of
 interest on about A$361m at an average base rate near 3.7%). GDI does not publish its margin. Each extra point on unhedged debt is
 A$3.4m, or 0.64 cents. FY27 is flat only because debt is A$21m lower.

 Maturities. Tranche A, A$210.75m, fully drawn, February 2029. Tranche B, A$210.75m with A$132.6m drawn,
 February 2028. The Townsville trust's A$10m loan was extended to November 2026 and is secured only on that
 trust [F1 note 17, F12]. Covenants. Loan to value (LVR, debt divided by the last independent valuation of the
 secured buildings) must stay under 50% and was 37.1%. Interest cover (earnings before interest divided by interest)
 must stay above 1.5 times and was 2.4 times. The table in section 8 shows the LVR at each cap rate: comfortable to
 7.3%, uncomfortable at the sales evidence, breached near 9.1%. Interest cover would be about 2.1 times at my
 FY29 interest bill and only breaks if interest reaches about A$33m. Refinancing. GDI has extended this facility four
 times in three years, most recently in June 2026. I assume a similar margin; a quarter point either way is A$0.9m a
 year, and fees have run at A$0.8m to A$1.1m a time.


 10. The Co-living JV and funds management
Village               Rooms        Customers and contracts                                                        FY26 site earnings
                                                                                                                  (100%)
Norseman, WA          425          Pantoro Gold, take-or-pay (the customer pays whether or not rooms are          A$6.4m
                                   used). Demand exceeds capacity; 140 rooms added.
South Hedland, WA     235          Rio Tinto projects, Acciona, Ventia, Monadelphous and others; at capacity      A$10.3m
Newman, WA            88           BHP, Hancock, CPB, Ventia and others                                           A$3.2m
Moranbah, Qld         239          Stanmore Resources: take-or-pay on 144 rooms, paying for at least 75%, to      Not shown; bought for
                                   31 March 2027. Stanmore has a one-year option on six months' notice and        A$18.3m in October 2025
                                   may end or shrink the contract for compensation.

 GDI has not said what replaces the Stanmore contract or whether the option was exercised; the notice date has
 passed and the AGM address was silent [F3, F14]. If Moranbah earns the JV's 20% target on its A$18.3m cost, that
 is about A$3.7m, or roughly 15% of the JV and 0.3 cents a security to GDI. So Queensland coal matters little; WA
 gold at Norseman and Pilbara iron ore and construction matter a lot. The JV's non-current liabilities rose from
 A$33.9m to A$57.5m in FY26 and its interest bill was A$1.85m; GDI's half, up to about A$29m, is not in GDI's
 gearing. GDI put in A$33.0m in FY23 and has had A$9.8m of distributions since (A$4.6m in FY25, A$5.2m in FY26)
 against A$18.9m of booked profit. Profits cannot be paid out without both partners' consent [F1 note 14].
 Funds management. Three funds remain: 1 Adelaide Terrace Perth, the Broadmeadow site near Newcastle (GDI
 holds no units) and Townsville. Assets under management were A$260m at June including A$42m of Autoleague
 since sold. Ongoing outside fees were A$1.41m in FY26. The goodwill test for this division now rests on
 performance fees of A$6m in FY27 and A$18m in FY28 and a A$250m "Office JV Fund" paying 0.10% [F1 note 12].


 11. Why the gap to NTA might close, or not
30 June                    2017       2018       2019        2020       2021       2022        2023        2024       2025       2026
Price, A$                  1.025      1.29       1.385       1.115      1.12       0.91        0.65        0.56       0.645      0.60
NTA, A$                    1.119      1.184      1.255       1.30       1.25       1.27        1.25        1.19       1.20       1.21
Price / NTA                0.92       1.09       1.10        0.86       0.90       0.72        0.52        0.47       0.54       0.50
Bought back in year, m     1.1        1.1        0.0         1.8        1.0        7.1         3.3         0          0          0
Distribution, cents        7.75       7.75       7.75        7.75       7.75       7.75        5.0         5.0        5.0        5.0

 Earlier buy-backs and sales did not close the gap. The premium in 2018 and 2019 came from the market. The
 March 2020 buy-back was "up to 5%", was renewed three times and bought 13.2m securities (2.4%) in four years,
 most of them above A$1.00, before being cancelled in March 2024. Sales of Sydney, Parramatta, Ashfield and
 Surfers Paradise assets were sold between 2017 and 2021, years in which GDI by its own account paid more than
 its AFFO [F7, F17 to F22].

The board's plan                                   Where it stands
5% buy-back (up to 26,991,124 securities, 7        632,029 bought for A$394,708, average A$0.6245, between A$0.615 and A$0.635. Last
Sept 2026 to 23 Aug 2027)                          purchase 14 October. That is 2.3% of the programme [F9].




GDI Property Group deep dive, 10 November 2026                                                                                         Page 8
The board's plan                                     Where it stands
A$100m of non-core sales                             Nothing sold from GDI's own balance sheet yet. The AGM said A$100m "remaining"
                                                     after about A$50m already released from Autoleague. GDI has not named the assets.
                                                     The two car parks (A$73.0m), 180 Hay Street (A$18.7m) and the Townsville stake
                                                     (about A$14m) add to A$106m; that is my inference.
Joint ventures over core buildings                   "Subject to liquidity and pricing suitability". The A$250m fund in the goodwill test is the
                                                     size of 197 St Georges Terrace (A$234m).
Mill Green                                           Master plan lodged. Stage 1A is the lobby, retail and podium at 197 St Georges Terrace;
                                                     cost not disclosed. The 1 Mill Street tower needs outside funding and a partner [F3].

Precedent                            What happened                                                     What made the difference
Elanor Commercial Property           Lederer family office, already at 27.5%, bid 70 cents cash:       A holder with a blocking stake, its own
Fund, 2025                           1.4% above an NTA of A$0.69 that had already been written         money and a grievance.
                                     down. Board rejected; Lederer reached 43% [M12, M13].
Hotel Property Investments,          Charter Hall and Hostplus bought 14.8%, then bid A$3.65, a        A buyer who could get control below
2024                                 10% discount to NTA [M14].                                        NTA once on the register.
Australian Unity Office Fund,        Bids above NTA were blocked by holders in 2019. The fund          Holders forcing a wind-up; the cash
2019 to 2024                         later traded at a 44% discount and went to asset sales and        came back at sale prices, not old book
                                     wind-up after a failed merger [M15, M16].                         values.

 GDI has one of the features, a 10% holder, but with no stated aim. It lacks the others: Perth's core office market is
 too illiquid to sell at book (no CBD investment sale in 2025), and no holder has asked for a wind-up. Elanor's own
 target statement put the median premium to NTA in cash bids for listed property trusts at 18.5% [M12]; the two
 recent ones above were done at or under NTA.


 12. Who owns it and what they might do
Rockefeller           Buying dates             Securities        Cost          Average        Range                   Holding after
notice
603, 1 Apr 2026       13 Jan to 1 Apr          6,602,538         A$3.96m       A$0.600        0.585 to 0.630          27,022,538 (5.01%)
604, 13 May           2 Apr to 13 May          5,407,576         A$3.22m       A$0.596        0.595 to 0.598          32,430,114 (6.01%)
604, 17 Jun           14 May to 17 Jun         5,794,779         A$3.51m       A$0.606        0.595 to 0.628          38,224,893 (7.08%)
604, 14 Aug           29 Jun to 14 Aug         4,960,907         A$3.11m       A$0.626        0.600 to 0.645          43,185,800 (8.00%)
604, 25 Aug           18 to 24 Aug             5,927,496         A$3.75m       A$0.632        0.625 to 0.635          49,113,296 (9.10%)
604, 14 Sep           9 and 14 Sep             5,489,000         A$3.46m       A$0.630        0.630 to 0.631          54,602,296 (10.11%)
Total                 13 Jan to 14 Sep         34,182,296        A$21.0m       A$0.615

 All purchases were on market, through five family companies and trusts and family members, all with a Hobart
 address [H1 to H6]. Yahoo shows 122.4m GDI securities traded from 1 January to 9 November 2026, so his buying
 was about 28% of the year's volume and about 47% between March and mid-September. The match is rough
 because some of his parcels were crossings larger than the day's on-screen volume. The last two notices were
 single blocks: 3.0m on results day and 5.5m in September, days after Renaissance reported a lower holding. He has
 lodged nothing in the eight weeks since, so he has added less than 1%. The forms state no intention and do not
 have to. I found no record of him taking board seats, calling meetings or bidding at other ASX companies; he is
 known as a direct property owner in Tasmania who sold seven shopping centres for A$145m and the ANZ Centre in
 Hobart for A$50.3m to a Charter Hall fund [M17, M18]. That absence is not verified.

Holder                               Holding                Latest notice     Pattern
Paradice Investment                  45,415,479 (8.4%)      22 Apr 2025       Arrived at 39.7m in September 2024 as index funds were selling
Management                                                                    (Vanguard went from 10.2% to 9.2% that month); added 5.7m
                                                                              since. Long-only small-company manager, half owned by
                                                                              Charter Hall. Has not sold [H8, H9, M19].
Renaissance Property                 33,991,610 (6.30%)     2 Sep 2026        Since February 2024 bought 6.6m at A$0.593 and sold 11.9m at
Securities                                                                    A$0.616. A value-style property fund that has been trimming into
                                                                              the bid [H7].
Salt Funds Management and            32,539,417 (6.03%)     2 Mar 2026        Has crossed 5% up or down five times since mid-2023. A trader
Pathfinder (NZ)                                                               of the range [H10].




GDI Property Group deep dive, 10 November 2026                                                                                              Page 9
Holder                           Holding               Latest notice      Pattern
MA Financial                     Below 5%              30 Jan 2026        Held 27.9m (5.16%) in October 2025 and sold down within four
                                                                          months [H11].

 The chair. James Warburton ran APN Outdoor for ten months in 2018 and sold it to JCDecaux for about A$1.1bn to
 A$1.2bn. At Seven West Media (2019 to April 2024) he sold Pacific Magazines for A$40m and an Airtasker stake for
 A$45m, bought Prime for about A$132m and cut debt from A$565m to A$249m, while the share price fell to about
 25 cents. Before that he ran Supercars [M20 to M23]. His record is one clean sale and a debt clean-up, not capital
 returns. He bought 76,923 GDI securities for A$49,623 on his first day [D2].
 The MD. Stephen Burns sold 500,000 on 29 May 2026 "primarily to satisfy a personal tax obligation". He now holds
 2,938,729 securities and 4,286,086 performance rights [D1, D3, D4]. Half of each long-term grant pays on total
 return against office peers (half at the median, all at the top quarter) and half on NTA plus distributions against an
 office fund index. The FY23 grant shows how that works: the peer half vested in full on a return of 5.4% a year,
 second of eight, while the price went from A$0.645 to A$0.60. Management can be paid in full with the stock at half
 of NTA.
 Could anyone bid? Nobody may go past 20% without a bid or holder approval, except that a holder who has been
 at 19% or more for six months may add 3% every six months [M24, M25]. Rockefeller can buy another 53m
 securities, about A$34m, before that matters; at this year's pace that is a year. A full bid at A$0.85 means A$458m
 of equity and refinancing A$343m of debt, a stretch for one family. At A$0.85 the buildings would be bought on
 about 8.1% of face income and 5.9% of cash income, below the cost of debt at about 6.7%, so a bid makes more
 sense to a buyer after rates fall. A price that works for a bidder is about A$0.80 to A$0.90, which is 7.8% to 8.5% on
 the buildings; the board would argue for NTA. I put the chance of any bid by August 2028 at about 10%.


 13. Anything else in the accounts
Item                          Why it matters
Goodwill of A$18.1m           Held on the strength of assumed performance fees (A$6m, then A$18m) discounted at 17.5%. It is outside
                              NTA, so no hit to the A$1.21 if written off [F1 note 12].
Valuers                       Not named. "Rotational." WS1 and WS2 were valued in December only and carried at June on the directors'
                              own check. The empty 180 Hay Street has not had an independent valuation since June 2025 [F1 note 9].
Fees owed by GDI's own        A$2.4m of management fees unpaid by managed funds, A$1.9m of receivables more than six months old,
funds                         no provision; plus A$3.5m lent to managed funds [F1 notes 7, 8, 28].
Related parties               The trust lends A$20m to GDI's management company to hold the JV stake (internal, at A$1.8m of interest).
                              A new A$1.0m "loan to related parties" appears without explanation. No dealings with directors [F1 notes 8,
                              27].
Auditor                       Hall Chadwick, a mid-tier firm, also paid A$125,000 for tax advice against A$212,000 for audit [F1 note 32].
Guarantees and                A$5m bank guarantee for the fund manager's licence. No capital commitments, no contingent liabilities, no
commitments                   legal matters disclosed [F1 notes 24, 35].
Townsville trust              Value down to A$40.0m from a A$53.5m purchase price, 14% empty, about 39% of income expiring in
                              FY28, and a A$10m loan that fell due in August and was extended three months [F1 notes 9, 36].
Dilution                      12.5m performance rights outstanding, 2.3% of securities [F10].



 What I could not verify
 The brief's A$175,000 median turnover. Whether the swap rate is 3.72% or 3.43%, and when it changed. GDI's loan
 margin (mine is derived). The split of incentives between up-front rent-free and abatements. The cost of Mill Green
 Stage 1A. Which assets make up the A$100m. Whether Stanmore extended at Moranbah. Rockefeller's intentions
 and the absence of activity elsewhere. Cap rates and gearing for Growthpoint, Dexus and Centuria Office, so their
 implied cap rates are rough or missing. Cushman & Wakefield's yields come from a press report of its MarketBeat,
 not the report itself. Colliers and CBRE figures appear only as quoted in GDI's slides. Daily prices and volumes are
 from Yahoo Finance, a secondary source. Six-month price moves for the August 2026 cuts are not yet available.
 Probabilities and scenario prices are my judgement.




GDI Property Group deep dive, 10 November 2026                                                                                      Page 10
 Sources
 GDI filings (ASX)
 [F1] Appendix 4E and Annual Financial Report, 30 June 2026 (24 Aug 2026)
 [F2] Annual Results Presentation (24 Aug 2026)
 [F3] Chairman's and Managing Director's AGM addresses (5 Nov 2026)
 [F4] Appendix 4D and Half Yearly Financial Report, 31 Dec 2025
 [F5] Appendix 4E and Annual Financial Report, 30 June 2025
 [F6] Appendix 4D, 31 Dec 2024
 [F7] Appendix 4E and Annual Financial Report, 30 June 2024
 [F8] Half Yearly Report, 31 Dec 2023
 [F9] Buy-back daily notification (15 Oct 2026)
 [F10] Appendix 3G showing securities on issue (6 Nov 2026)
 [F11] Annual Report 2026, including holder tables (29 Sep 2026)
 [F12] Extension of Syndicated Facility (23 Jun 2026)
 [F13] Sale of final five Autoleague properties (28 May 2026)
 [F14] Co-living JV: settlement of Moranbah (9 Oct 2025)
 [F15] Annual Results Announcement (24 Aug 2026)
 [F16] Appendix 4E 2023
 [F17] Appendix 4E 2022
 [F18] Appendix 4E 2021
 [F19] Appendix 4E 2020
 [F20] Appendix 4E 2019
 [F21] Appendix 4E 2018
 [F22] Appendix 4E 2017
 [F23] On-market buyback announcement (24 Aug 2026)
 [F24] Distribution notice, 9 Dec 2022
 [F25] Annual Results Presentation 2024 (GDI's own AFFO table)
 [F26] Sale of Wood Street, Bassendean (19 Dec 2025)
 Holder and director notices (ASX)
 [H1] Rockefeller 603, 1 Apr 2026
 [H2] 604, 13 May
 [H3] 604, 17 Jun
 [H4] 604, 14 Aug
 [H5] 604, 25 Aug
 [H6] 604, 14 Sep
 [H7] Renaissance 604, 4 Sep 2026
 [H8] Paradice 604, 24 Apr 2025
 [H9] Paradice 603, 24 Sep 2024
 [H10] Salt and Pathfinder 604, 4 Mar 2026
 [H11] MA Financial 605, 3 Feb 2026
 [D1] Burns sale, 3 Jun 2026
 [D2] Warburton purchase, 26 Aug 2026
 [D3] Burns rights vesting, 8 Sep 2026
 [D4] Burns rights issue, 6 Nov 2026
 Peers (ASX releases)
 [P1] Centuria Office REIT FY26 results
 [P2] Abacus Group FY26 results
 [P6] Centuria Office FY23
 [P7] Centuria Office FY24
 [P8] Growthpoint FY23
 [P8] Growthpoint FY24
 [P8] Dexus FY23
 [P8] Dexus FY24
 [P3] Growthpoint FY26 results
 [P4] Dexus 2026 results release
 [P5] Abacus pro forma NTA after Storage King sale (press, pointer only)
 Market research, rates and other
 [M1] Knight Frank, Perth CBD Office Market, March 2026
 [M2] Knight Frank, Perth CBD Office State of the Market, Q2 2026
 [M3] Knight Frank, State of the Market, Q1 2026
 [M4] JLL, Q3 2026 office markets release
 [M5] Cushman & Wakefield Q3 2026 MarketBeat as reported (press)
 [M6] 256 St Georges Terrace sale campaign (agent release)



GDI Property Group deep dive, 10 November 2026                              Page 11
 [M7] RWC WA listings showing 256 St Georges Terrace under offer
 [M8] Knight Frank Perth forecasts, October 2026 (press)
 [M9] Yahoo Finance daily prices and volumes (GDI, peers, A-REIT index)
 [M10] RBA decision, 3 November 2026
 [M11] ASX bank bill rates and YieldReport bond and swap rates
 [M12] Elanor Commercial Property Fund target's statement presentation, Sept 2025
 [M13] Lederer bid for Elanor Commercial Property Fund (press)
 [M14] Charter Hall bid for Hotel Property Investments (press)
 [M15] Starwood bid for Australian Unity Office Fund, 2019 (press)
 [M16] Australian Unity Office Fund merger fails (press)
 [M17] Rockefeller sells ANZ Centre, Hobart (press)
 [M18] Rockefeller profile and A$145m centre sale (press)
 [M19] Charter Hall's 50% of Paradice (Wikipedia, pointer only)
 [M20] Warburton and the APN Outdoor sale (press)
 [M21] Warburton at Seven West Media (press)
 [M22] Seven West debt and Prime under Warburton (press)
 [M23] Seven West share price at his exit (press)
 [M24] Takeovers Panel summary of takeover provisions
 [M25] Corporations Act 2001, section 611
 Broker notes were not used. Press items are pointers to facts I could not get from a primary document and are marked as such.




GDI Property Group deep dive, 10 November 2026                                                                                   Page 12
```
