# Capral (ASX:CAA): red team review. Wait for the FY26 result on 26 February 2027; not a value pick at A$13.16 on honest bad-case numbers

Written 2026-11-08 by the red team, a separate agent that saw only the deep dive (research/picks/CAA.md), the checklist (docs/RED_TEAM.md, research pick section) and RULEBOOK.md sections 3, 4 and 5a as they stand today. Price: A$13.16 (last trade 6 November 2026, bid A$13.08, ask A$13.20, data/research_data/asx_company.json). This is a simulation and not financial advice.

Verdict: wait for a named event, the FY26 result on 26 February 2027, which comes after the company's buy-back ends (18 December 2026) and after the Minister's windows and doors decision (due about mid-January 2027). Details at the end.

> In short: the deep dive's facts hold up. Every number I re-opened matched its source, and its corrections to the fact sheet (NTA already leaves out the deferred tax asset, the payout cut, the buy-back pace, Perpetual's selling) are right. Where I part company is the bad case. It prices the business at 0.75 times NTA on pre-tax profit of about A$20m a year, which is about 8.3 times pre-tax profit, more than the market has paid for Capral at any year-end since at least 2021 and far more than it paid when returns on NTA were last that low (0.45 to 0.64 times NTA in 2016 to 2018). Priced the way the market has actually priced this business at those returns, the bad case is about 14% to 17% below today's price, outside the 10% limit. The middling case is about right but leans on the market paying more per dollar of profit as cash and stock build up inside the company; halfway between the two ways the market has priced it, it is about +15.5%, a narrow pass. On my numbers the expected gain after costs is about +9% over 662 days, against a minimum of 12.9%. On top of that the company has been the main buyer of its own shares since September, and in each of the last three years the price drifted down 3.6% to 4.6% between the end of the buy-back and the February result.

## The two rules as they stand today

| Test (rulebook section 5a, from 8 Nov 2026) | Deep dive | Red team |
| --- | --- | --- |
| Bad case no more than 10% below the price | A$12.20, -7.3%: passes | A$10.90, -17.2% (-14% without the worse tail): fails |
| Middling case at least 15% above the price | A$15.60, +18.5%: passes | A$15.20, +15.5%: passes narrowly (+13% to +18% depending on how the market prices it) |
| Expected gain after costs at least the cash rate plus 5% a year to the resolve date | +15.1% against 12.9%: passes | +9.1% against 12.9%: fails |

Days to 31 August 2028: 662 from today (the deep dive used 661). Minimum: (2.13% + 5%) x 662 / 365 = 12.93%, the arithmetic src/decide.py uses. Costs: I accept the deep dive's 2.5% round trip (half the A$0.12 spread each way, A$15 brokerage on the sale, 0.5% to convert, a small size cost); if the buy is not covered by the plan's monthly allowance, add about 0.75%.

## 1. Are the facts right?

I re-opened thirteen primary sources (links at the end) and the Norgate prices. Everything checked held.

| Fact the case rests on | Source re-opened | Result |
| --- | --- | --- |
| 749,169 shares bought back for A$8,949,228 to 5 November, 867,831 still allowed, prices A$10.66 to A$13.27 | Daily notice of 6 Nov 2026 (745,624 + 3,545 shares; A$8,903,517.63 + A$45,710.29) | Held |
| Buy-back of up to 1,617,000 shares (10% of 16,174,045), 2 March to 18 December 2026, through Taylor Collison | Appendix 3C, 26 Feb 2026 | Held. The 28 September update speaks of "the remainder of the period to 17 December 2026", so the last buying day is probably the 17th |
| From 28 September the company buys 40% to 50% of the last 20 days' volume, up to 60% | Update on on-market share buy-back, 28 Sep 2026 | Held, with two qualifiers in the notice: "other than in respect of a single large parcel", and the rate stays "at the discretion of the Board" |
| The company bought 38.5% of the shares traded from 28 September to 30 October | 132 of the 133 daily notices (the first day's 4,003 shares are carried in the second) against Norgate volume, re-computed | Held: 292,318 of 759,295 shares (38.5%). From March to October, 27% |
| NTA of A$13.43 at June 2026 already leaves out the A$29.0m deferred tax asset | Half-year report, balance sheet and Appendix 4D | Held: A$251.544m less goodwill A$6.536m, other intangibles A$2.528m and the A$29.032m asset is A$213.448m, over 15,892,408 shares is A$13.43. The deep dive's correction of the fact sheet is right |
| Net cash A$62.1m at 30 June; payables up A$25.6m | Half-year report and presentation | Held. Receivables also rose A$27.9m; the company says working capital "will lift in 2H26 as payments for higher cost inventory fall due" |
| Tax losses: A$63.9m booked (A$19.2m of tax), A$69.2m not booked (A$20.8m), A$21.5m of unbooked timing differences (A$6.5m); A$5.3m of tax value used in 1H26 | FY25 report note 9 (19,165; 69,198 and 20,759; 21,502 and 6,451); half-year note 2 (5,311) | Held |
| Payout range cut from 40-80% to 40-60% of profit | FY25 report and AGM address, 6 May 2026 | Held. The FY25 report adds "adjusted to exclude deferred tax asset benefits"; the August presentation calls it "40–60% of underlying EPS". See section 3 for why this matters after about 2028 |
| Bank covenant caps distributions below the prior year's profit (FY25 distributions A$17.84m); fixed charge cover 2.48 times; A$75m syndicated facility | FY25 report note 23 and capital risk note | Held |
| Guidance cut from "slightly above prior year" (February) to "broadly in line" | FY25 results presentation; AGM address | Held. August added "depending on some recovery of the residential housing market" |
| Allan Gray 25.05% (3,968,483), having bought 251,968 for A$2,730,501 and sold 36,693 | Allan Gray notice, 16 Jul 2026 | Held |
| Perpetual 8.03% (1,262,267), selling 42,329 at about A$11.67 on 18 September and about 100,000 at A$12.05 to A$12.20 on 13 to 15 October | Perpetual notice, 19 Oct 2026 | Held: 7,136, 42,289 and 51,062 shares on 13, 14 and 15 October; also 38,879 at about A$10.65 on 15 July |
| Register: Prudential Nominees 1,550,000 (9.60%), National Exchange 700,000 (4.33%), top 20 70.01%, 2,162 holders | 2025 Annual Report | Held; the company's own substantial holder list shows National Exchange at 2,100,000 (11.86%) |
| FY25 lease principal paid A$18.0m | FY25 cash flow statement (18,038) | Held |
| P/NTA of 0.64 (2016), 0.55 (2017) and 0.45 (2018) | FY16 and FY18 Appendix 4E NTA per share (25.8c, 27.2c, 26.7c on 474.7m to 480.3m shares) against Norgate year-end prices | Held |

Anything left out:
- Metal supply. The half-year report says "Billet supply from Middle East smelters was interrupted during the period and has been replaced with supply from alternative producers at higher base premiums", and the AGM address ties the high metal price to the closure of the Strait of Hormuz. The deep dive covers metal and freight costs but not the supply interruption.
- First-half trading detail that cuts against a steady middling case: higher metal costs "began to impact margins through the second quarter", an "unplanned under-recovery" of A$1.0m on freight, "mill operating shifts reduced late in the half in response to softer demand", window fabricators "continue to report share lost to imported windows" and "volume to resellers is lower". The company expects "the full impact of materially higher metal costs" in the second half.
- Management's own view of the cycle. The CFO called FY25 "bottom of cycle earnings" (FY25 presentation); the deep dive calls the latest twelve months mid-cycle. Both can't be right, and the deep dive's reading is the more cautious one, which I prefer.
- The board's own floor. The FY25 remuneration report set minimum incentive targets of A$29.5m of underlying EBIT and A$25.4m of profit, close to my bad case, not to the deep dive's middling.
- Cash returned against cash made. The remuneration report's free cash flow (after leases and all investing) was A$17.2m, -A$16.4m, A$52.4m, A$28.6m and A$20.2m for 2021 to 2025, A$102m in all; holders got about A$64m of it (A$45.8m of dividends, A$18.5m of buy-backs). FY22, the metal price spike year, absorbed A$16.4m.
- No capital raising, no auditor qualification, no lawsuit and no director departure in 2026 that I found.

## 2. Is it really overlooked, or is it cheap for a reason?

### Who is buying and selling
- The company is a growing share of all trading: buy-backs were about 10% of 2023's value traded (buying only from September), 17% in 2024, 21% in 2025, 27% from March to October 2026 and 38.5% since 28 September (buy-back amounts from the reports and daily notices, against Norgate value traded).
- Perpetual is a steady seller: 10.36% in February, 9.10% in July, 8.03% in October, 178,779 shares sold since July. On 13 to 15 October it sold 100,487 of the 241,172 shares traded and the company bought 60,373 of them. Its remaining 1,262,267 shares are about 65 sessions of the trading the company didn't do in October.
- Allan Gray bought in the first half at about A$10.84 and holds 25.05%. A bid needs it. There has been no notice since July, so it has not moved by 1% or more since.

### The buy-back and the price
- The rise wasn't all the company. From 25 September (A$11.31) to 27 October (A$11.88), with the company at about 41% of volume, the price rose 5%. Then in three sessions, 28 to 30 October, it rose 9.6% to A$13.02 on 181,341 shares, of which the company bought 44%, 15% and 21%. I found no ASX announcement on those days. Other buyers did most of the lifting; I don't know who or why, and a move like that can fade.
- When the buyer stops, the price has drifted. From the last buy-back day to the eve of the February result the price fell 3.8% (29 Dec 2023 to 22 Feb 2024), 3.6% (20 Dec 2024 to 25 Feb 2025) and 4.6% (5 Dec 2025 to 25 Feb 2026), with lows in those gaps up to 10% below. In the July 2026 results pause it fell from A$11.15 to A$10.33 in 12 sessions (-7.4%) while Perpetual sold, then recovered to A$11.86 by 30 July with no news. The stock's daily moves over the past year had a standard deviation of 1.9% (about 30% a year).
- So the bad case can come early. A price of about A$12.00 to A$12.60 in late February would be in line with the last three years. That doesn't break a 22-month hold, but it means buying today pays for the company's own support, and the deep dive's "wait" instinct was sound.

### Will the market ever pay more than about 0.9 times NTA?
Not on the evidence, unless returns rise or someone bids. Over ten year-ends it paid above 1.0 times once (1.18 times in 2021, a peak-profit year). Today it pays 0.97 times reported NTA, or about 0.93 times once four months of second-half profit are added. The multiple of NTA follows the pre-tax return the business earns on it:

| Year-end | Underlying pre-tax profit | Pre-tax return on NTA (about) | Price / NTA | Price / pre-tax profit |
| --- | --- | --- | --- | --- |
| 2016 | A$13.6m | 11% | 0.64 | 5.8 |
| 2017 | A$11.7m | 9% | 0.55 | 6.1 |
| 2018 | A$7.6m | 6% | 0.45 | 7.6 |
| 2022 | A$34.6m | 21% | 0.81 | 3.8 |
| 2023 | A$32.9m | 19% | 0.95 | 5.2 |
| 2024 | A$28.8m | 15% | 0.88 | 6.0 |
| 2025 | A$30.9m | 15% | 0.94 | 6.3 |
| Now (latest twelve months) | A$31.8m | 15% | 0.97 | 6.4 |

(NTA and shares for 2016 to 2018 from the Appendix 4E reports; 2022 to 2025 shares from the remuneration report's earnings per share; profit from the deep dive's rebuild; prices from Norgate.)

Reasons it is unlikely to break above 1.0 times by August 2028: dividends stay unfranked until about 2030; four holders own about half the register; it left the All Ordinaries in March; the board keeps the surplus cash; and the company is the marginal buyer. What could change it: a bid, or windows duties plus a housing recovery lifting returns towards 18% to 20%. My chance of the price being above 1.0 times NTA on 31 August 2028: about 15%.

### Management's record against its own guidance
Good until this year: upgrades in November 2022 and December 2024, FY25 delivered in line. In 2026 the outlook has softened twice ("slightly above" in February, "broadly in line" in May, a housing condition added in August). First-half underlying EBIT was A$16.7m; to be broadly in line with FY25's A$35.8m the second half needs about A$19m against A$19.7m a year earlier, with the full metal cost still to come.

## 3. The valuation
- Peers. The deep dive applies peer multiples to mid-cycle cash earnings, not peak, and picks the two low-return distributors as the closest comparisons. That is fair. But the market has never paid Capral the 7.5 times pre-tax cash earnings of Method 1, and the deep dive rightly uses Methods 1 and 2 only for its good case. Their weakness touches only the good case.
- Net assets. The A$13.43 NTA is mostly receivables and stock (A$290m) carried at a high metal price, plus presses and plant with little use to anyone but an extruder. It is a fair floor for book value, not a price anyone would pay in cash for the plant. Part of its growth (about A$4m a year) is the lease accounting catching up, since cash rent runs above the profit and loss charge.
- The discounted cash flow. The discount rate moves it most (A$15.76 to A$18.89 between 12% and 10%), and A$25m of pre-tax cash earnings is the second input: at A$20m and 11% it gives about A$14.30. Neither feeds the middling case.
- The margin step-up, four to five years old. For it: margins after rent held at A$519 to A$548 a tonne through the 2024-25 housing low on 15% less volume than FY21; the Bremer Park closure, the Smithfield purchase and five bolt-on distributors; industrial work is now 50% of volume against 41% in 2017. Against it: the step-up began in the 2021-22 freight and renovation boom; the extrusion duties on the main Chinese exporters are small (0.8% to 5.6%); fabricated window imports keep growing; and the second half of 2026 carries the full metal and freight cost. I put about 30% on margins falling back to FY24 levels or below within the window, about 8% on a slide toward the pre-2021 levels.
- Will the cash reach holders? Some of it, at about today's rate. Over 2021 to 2025 holders got about 63% of free cash flow, and cash at balance dates has stayed between A$53m and A$69m. The policy now caps distributions at 40% to 60% of profit, about A$13m to A$18m a year, mostly as buy-backs "subject to share trading liquidity". The surplus of about A$45m is kept "for growth and through-cycle volatility". And once the unbooked tax losses are used up (on my reading of the half-year tax note, around late 2028), reported profit carries a deferred tax charge, and a payout set on statutory profit falls by about 30% unless the board changes the policy. So the pile doesn't come out, and the middling case's NTA growth of about A$1.60 a share a year mostly stays inside the company.

## 4. The dated events and the exit
- Windows and doors (case 691): the Commission's preliminary findings found dumping and injury, and securities of 5.3% to 73.3% have applied since 15 October (The Good Builder, secondary). A final duty looks likely and is partly expected. The final report is due by 16 December 2026, the Minister's decision about 30 days later.
- Buy-back ends 18 December 2026 (last buying day probably 17 December); blackout to the FY26 result on 26 February 2027.
- Then the AGM (about May 2027), 1H27 (about late August 2027), FY27 (about late February 2028) and 1H28. Half-year results have come on 21 to 28 August, so a 31 August 2028 resolve date leaves only a few days.
- Could the events come and go without the price moving? Yes. A value pick relies on NTA building up and the market keeping its habit; results days in the last three Februaries moved the price +9%, +4% and +1% within a week.
- Liquidity: our A$2,016 is about 2% of a median day's trading without the company (about A$107,000). It can be sold in a bad week.
- Exit rule: the deep dive's is sound (a guidance cut taking FY27 underlying EBIT below A$30m, an acquisition above A$30m at more than book value, a close below 0.75 times the latest reported NTA). I'd add two: no new buy-back by the FY26 result, or a further cut to the payout range.

## 5. The stated chances and prices
The chances (30%, 50%, 20%) are reasonable. The prices are where I differ.

### Is the bad case the floor?
No. The deep dive's bad case has pre-tax profit of about A$20m a year and the market paying 0.75 times June 2028 NTA of A$15.44 (A$11.58, plus A$0.60 of dividends). With buy-backs that NTA sits on about 14.6m shares, so pre-tax profit is about A$1.37 a share, and A$11.58 is about 8.3 to 8.5 times that. The market's year-end multiple of Capral's pre-tax profit has run 3.8 to 6.4 times since 2022. At a 9% pre-tax return on NTA, which is what A$20m a year gives, the market paid 0.55 times NTA in 2017; that would make the deep dive's own bad case about A$9.00 to A$9.10 with dividends, about -31%.

A milder bad case is fairer: profit at about A$24m to A$25m a year (FY24-type margins on slightly lower volume, a metal price fall from today's high level, windows imports still growing). NTA would reach about A$15.80, the return on it about 10.5%, and history says the market would pay about 0.65 to 0.70 times NTA, or 6.3 times pre-tax profit: about A$10.30 to A$11.10, plus A$0.60, about A$11.30 (-14%). For the bad case to sit within 10% (A$11.84) the market would have to pay 0.71 times NTA, or 6.8 times pre-tax profit, at a 10.5% return, more than it paid at similar or higher returns in 2016 and 2017. Inside the bad case I keep the deep dive's own worse tail (a slide toward pre-2021 margins) at about a quarter of its weight and 0.6 times NTA (about A$9.40). Weighted: A$10.90, -17%.

A 30% bad case only 7% below the price is also narrow for a cyclical metals business whose share price has moved about 30% a year.

### Is the middling case what the market would pay by 31 August 2028?
Close, but it takes the more generous of the two ways the market has priced Capral. On the deep dive's own path (pre-tax profit about A$31m a year, buy-backs about A$12m a year), June 2028 NTA is A$16.65 on about 13.9m shares and pre-tax profit about A$2.23 a share.
- At 0.90 times NTA: A$14.98, which is 6.7 times pre-tax profit.
- At today's 6.4 times pre-tax profit: A$14.25, which is 0.86 times NTA.

The market has kept 0.81 to 0.97 times NTA for four years while its multiple of profit rose from 3.8 to 6.4 times, so the NTA habit has real support. But the 6.4 times is the highest year-end level in that run, set while the company's share of trading doubled, and the NTA route needs a further rise to 6.7 times. I take the halfway point: A$14.60 plus A$0.60, A$15.20 (+15.5%).

### The good case
1.15 times NTA on A$36m of pre-tax profit is 7.6 times pre-tax profit; the market hasn't paid above 6.4 times in this run. A bid needs Allan Gray. I'd use A$19.10: a bit over half the weight on profit up at about 6.6 times (A$17.60 with dividends), the rest on a re-rating or a bid at about 1.2 times NTA (A$21.00).

### My outcomes

| Outcome | What happens | Chance | Price by 31 Aug 2028, dividends counted |
| --- | --- | --- | --- |
| Bad | Pre-tax profit falls to A$24m to A$25m a year on FY24-type margins, a metal price fall and windows imports; the market prices it as it did at similar returns, 0.65 to 0.70 times NTA (A$11.30). Within it, about a quarter chance of a slide toward pre-2021 margins at about 0.6 times NTA (A$9.40) | 30% | A$10.90 (-17.2%) |
| Middling | Pre-tax profit about A$31m a year, buy-backs continue, NTA A$16.65; priced halfway between 0.90 times NTA and 6.4 times pre-tax profit | 50% | A$15.20 (+15.5%) |
| Good | Housing recovery and windows duties lift pre-tax profit to about A$36m; priced at about 6.6 times profit, or re-rated or bid at about 1.2 times NTA | 20% | A$19.10 (+45.1%) |

Expected price A$14.69, +11.6% before costs, about +9.1% after 2.5% of costs, against the 12.9% minimum over 662 days.

Which outcome decides it:

| Version | Expected gain after costs | Bad case | Passes both rules? |
| --- | --- | --- | --- |
| Deep dive as written | +15.1% | -7.3% | Yes |
| Deep dive with my bad case only | +12.2% | -17.2% | No (both) |
| Deep dive with the milder bad case only (A$11.30, no tail) | +13.1% | -14.1% | No (bad case) |
| Deep dive with my middling only | +13.6% | -7.3% | Yes, narrowly |
| Deep dive with my good case only | +13.6% | -7.3% | Yes, narrowly |
| Red team | +9.1% | -17.2% | No (both) |

The result turns on the bad case. Sizing doesn't: full Kelly is above 1 on every version, so the 2.5% cap binds (NZ$2,500, about A$2,016, 153 shares).

## 6. Special situations only
Not a special situation. One point from that list still applies: anyone wanting control needs Allan Gray's 25.05%, and Allan Gray plus the Tweed group hold about 40%.

## The three points most likely to make the pick wrong
1. The bad case isn't the floor. At the returns the deep dive's bad case implies, the market has paid 0.45 to 0.64 times NTA, not 0.75 times; priced that way the bad case is 14% to 17% down, not 7%.
2. The company has been holding the price. It bought 38.5% of all shares traded since 28 September and stops on 18 December; Perpetual still has 1.26m shares to sell; and the price has drifted 3.6% to 4.6% lower between the end of the buy-back and the February result in each of the last three years.
3. Second-half earnings and the young margin step-up. The company has already softened its outlook twice in 2026, flagged the full metal cost, freight and softer demand for the second half, and the higher margins date only from 2021.

## What I couldn't verify
- The Commission's record for case 691, including the statement of essential facts published in October 2026: industry.gov.au's public record is barred to my fetch tool by the site's robots rules, so I did not open it, and the windows facts rest on The Good Builder (secondary).
- Why the price jumped 9.6% on 28 to 30 October. No ASX announcement; Norgate's prices in the repo end on 30 October, so for November I have only the daily buy-back notices and the 6 November snapshot.
- Not re-checked: the peer figures, the ten-year margin rebuild (beyond FY25's lease payments), the director dealing notices, the 2023 Tweed group notices (scanned), and the facility's maturity date.
- The 2022 to 2025 multiples use weighted share counts implied by the remuneration report, not year-end counts, so they may differ from the deep dive's by a few tenths.

## Sources
Capral announcements on the ASX (each link is the PDF the ASX serves for that id):
1. Half Yearly Report and Accounts 1H26, 24 Aug 2026 (03128568): https://announcements.asx.com.au/asxpdf/20260824/pdf/073327tvd6dc4g.pdf
2. HY26 Half Year Results Presentation, 24 Aug 2026 (03128569): https://announcements.asx.com.au/asxpdf/20260824/pdf/07332b0prcx5ry.pdf
3. Preliminary Final Report FY25, 26 Feb 2026 (03065256): https://announcements.asx.com.au/asxpdf/20260226/pdf/06ws4pbrr48wkj.pdf
4. Full Year 2025 Results Presentation, 26 Feb 2026 (03065261): https://announcements.asx.com.au/asxpdf/20260226/pdf/06ws50vs0n32mc.pdf
5. Addresses to Shareholders and Proxy results (AGM), 6 May 2026 (03090910): https://announcements.asx.com.au/asxpdf/20260506/pdf/06z93qzl00t4l5.pdf
6. Notification of buy-back (Appendix 3C), 26 Feb 2026 (03065358): https://announcements.asx.com.au/asxpdf/20260226/pdf/06wscq5qc0f5ht.pdf
7. Update on on-market share buy-back, 28 Sep 2026 (03144412): https://announcements.asx.com.au/asxpdf/20260928/pdf/074l79rw6vn162.pdf
8. Daily buy-back notice, 6 Nov 2026 (03162742): https://announcements.asx.com.au/asxpdf/20261106/pdf/0769898bmwgxwj.pdf ; and the other 132 daily notices from 3 Mar 2026, each listed at https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=CAA&timeframe=Y&year=2026
9. Allan Gray, change in substantial holding, 16 Jul 2026 (03115653): https://announcements.asx.com.au/asxpdf/20260716/pdf/071s6qpyl19q14.pdf
10. Perpetual, change in substantial holding, 19 Oct 2026 (03154129): https://announcements.asx.com.au/asxpdf/20261019/pdf/075hjxgf0b4t9g.pdf
11. 2025 Annual Report to shareholders, 2 Apr 2026 (03078822): https://announcements.asx.com.au/asxpdf/20260402/pdf/06y2v1j2cbck4w.pdf
12. Preliminary Final Report FY16, 23 Feb 2017 (01831791): https://announcements.asx.com.au/asxpdf/20170223/pdf/43g84p1w8pc3y9.pdf ; Preliminary Final Report FY18, 22 Feb 2019 (02078492): https://announcements.asx.com.au/asxpdf/20190222/pdf/442vmlmxn2nf52.pdf
13. ASX announcement lists for CAA, 2023 to 2026 (buy-back start, pause and end dates): https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=CAA&timeframe=Y&year=2025 (and the same address for 2023, 2024 and 2026)
14. Prices and volumes: data/norgate/universe/prices_2015.csv.gz to prices_2026.csv.gz; last trade, bid and ask: data/research_data/asx_company.json (fetched 7 Nov 2026 UTC).

Secondary:
- The Good Builder, "Imported aluminium windows now carry securities: the cost starts before the duty decision" (preliminary findings in October 2026, securities from 15 October at 5.3% to 73.3%, final report due 16 December, timetable extended from 25 November): https://thegoodbuilder.com.au/imported-aluminium-windows-now-carry-securities-the-cost-starts-before-the-duty-decision/
- Not opened (robots exclusion): the statement of essential facts for case 691, https://www.industry.gov.au/sites/default/files/atrc/public-record/2026-10/691-501-report-statement-of-essential-facts-sef-691.pdf

## Verdict
Wait for a named event: the FY26 result on 26 February 2027.

Why not now:
- On honest bad-case pricing the pick fails both of today's rules: the bad case is about 17% below the price (14% without the worse tail), outside the 10% limit, and the expected gain after costs is about +9% against a 12.9% minimum. The deep dive passes only because its bad case has the market paying more for weaker profit than it has paid in a decade.
- The price is held up until 18 December by the company's own buying, and the last three years say the price tends to give back about 4% before the February result.
- The FY26 result will show the second half with the full metal cost, the working capital lift, December NTA, FY27 guidance and whether a new buy-back starts; the windows decision lands before it.

Why not "don't buy": the business is sound, the facts are right, NTA has grown about A$0.90 to A$1.50 a share a year since 2021 and should keep doing so while no tax is paid, and at a lower price or on stronger evidence it can qualify.

Reopen as a value pick, re-running the outcomes on the reported NTA, if either:
1. After the result, the price is at or below about A$11.75, with FY26 underlying EBIT of at least A$34m, December 2026 NTA of at least A$14.20, net cash of at least A$40m after the working capital lift and a new buy-back announced. (Once the March 2027 dividend has gone, my outcomes become A$10.60, A$14.90 and A$18.80; the 10% bad-case limit binds at about A$11.78, the middling test at about A$12.96, and the minimum gain over about 548 days at about A$12.71.)
2. Or, at any price, the result lifts the earnings floor: second-half margin per tonne held at A$540 or more after the full metal cost, FY27 guidance above FY26 and windows duties imposed. Then re-run with FY25-type profit (about A$29m to A$31m) as the bad case.

If it reopens, the card I'd write (resolve 31 August 2028, after the 1H28 result): bad 30% at A$10.90, middling 50% at A$15.20, good 20% at A$19.10, each less A$0.30 for every dividend already paid by the purchase date, and re-based on the latest reported NTA; size at the 2.5% cap; exit on FY27 guidance taking underlying EBIT below A$30m, an acquisition above A$30m at more than book value, a close below 0.75 times the latest reported NTA, no new buy-back by the FY26 result, or a further cut to the payout range; otherwise hold to the resolve date.
