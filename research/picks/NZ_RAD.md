# Radius Residential Care (NZX:RAD): deep dive. Wait for the H1 FY27 result on 11 November 2026. Not a value pick: the bad case (NZ$0.315) is 24% below the price

Written 2026-11-08 by the research desk. Price at writing: NZ$0.415 (close on 6 November 2026, FinFeedAPI, data/prices/NZX/RAD.csv; the NZX instrument data shows the same close, bid NZ$0.400 and offer NZ$0.415 [S13]). Market value: NZ$117.6m (283,467,009 shares on issue, NZX [S13]).
Status: finished. Verdict: wait for a named event, the H1 FY27 result on 11 November 2026 [S11]. The conditions that reopen or close the case are under "Dated events". This is a simulation and not financial advice.
Fact sheet: research/facts/NZ_RAD.md, grade A ("only just"). The question it set: is FY26's NZ$27.4m of underlying EBITDA after rent, plus Karori, the real base, or was the first half flattered by resale gains, so that the real rate is nearer the second half's NZ$12.5m a half?

Value pick (rulebook section 5a, from 8 Nov 2026): it doesn't qualify. The bad case (NZ$0.315) is 24% below the price (15% counting the 3.75c of dividends expected by May 2028); the limit is 10%. The middling case at the FY28 result is 8% above the price (17% with dividends); it needs 15%. The bad leg fails either way, because the shares carry NZ$86m of bank debt and NZ$141.5m of lease liabilities ahead of them: at 7 times after rent, a 10% fall in earnings takes about 17% off the equity, and half a turn off the multiple another 12%.

Order of work. The brief and the fact sheet both quote the price, so it was in view before I began. The filings section and the valuation take no input from Radius's own share price: they use the filings, peers' filings and prices, and transaction evidence. Radius's price is used only in "Why the market is wrong", "Outcomes and chances" and the checks. Arithmetic was done in python3 -I; the scripts are in the scratchpad, and every figure below is reproduced in the text.

Liquidity, measured first as the brief asked, from NZX's own activity data [S13]: the median value traded over the 20 sessions from 9 October to 6 November 2026 was NZ$32,278 a day, with 5 of the 20 sessions below NZ$12,500. Over 60, 120 and 250 sessions the median is NZ$30,797, NZ$28,874 and NZ$28,690. It passes the NZ$12,500 test clearly. (On NZX's data the fact sheet's window, 21 September to 16 October, gives NZ$14,080, close to the NZ$13,926 it took from Yahoo.)

Corrections to the fact sheet, for the red team:
1. Liquidity is not "close to the line": NZ$32,278 a day on the latest 20 sessions of NZX data (above).
2. The price is NZ$0.415 (6 November), not NZ$0.39 (30 October). Its "gap if it goes our way" at today's price is 32%, not 40.5%.
3. The second half of FY26 was weaker for two reasons, not one. Lower resale gains explain NZ$1.44m of the NZ$2.46m fall from the first half to the second. The other NZ$1.0m is costs: wages rose 7.7% half on half against revenue up 1.8%, and aged care EBITDAR fell from NZ$27.0m to NZ$26.6m even though St Allisa was in for six months instead of four [S1][S2][S4].
4. The good case gives Karori Radius's mature average of NZ$31.1k of EBITDAR per occupied bed from day one (NZ$2.66m). The last acquisition shows year one is much lower: St Allisa made a loss before tax of NZ$0.2m in its first ten months (NZ$0.3m on a full year pro forma) [S6, note 5.6]. Forsyth Barr, whose research Radius pays for, puts Karori's potential at NZ$2.6m "or higher within a few years", with early earnings below the group average [X3]. I use NZ$1.0m to NZ$2.6m for Karori's first full year, centre NZ$1.8m.
5. The 8 times multiple of the good case is above anything the market has paid for RAD in the last 17 months (about 6.3 times after rent in June 2025 to about 7.5 times at the August 2026 high) and is the same as an owner-operator multiple of about 9.35 times, above Regis Healthcare's 9.2 times (Valuation). It belongs to the good case only.
6. The underlying EBITDA reconciliation removes NZ$1.824m labelled as the investment property revaluation (the income statement shows NZ$1.680m) and adds back NZ$1.824m of realised resale gains; an "other adjustments" line of minus NZ$1.389m then removes the NZ$1.495m reversal of past revaluation losses, net of the NZ$0.144m difference (my reading; the line isn't itemised) [S2, appendix 6]. The net effect matches the fact sheet's description.
7. The NZ$108.6m of revalued land and buildings includes the Belfast land (NZ$5.5m added in FY26), so the twelve owned care homes at 31 March 2026 were valued at about NZ$103.0m [S1, note 3.2].
8. Radius is covered: Forsyth Barr publishes research on RAD that the company commissions and pays for (spot valuation NZ$0.54 on 2 April 2026) [X3].
9. The guidance record has a miss the fact sheet didn't list. At the 1H26 result the company said it "expects 2H26 trading to be broadly consistent with the first half" [S4, page 21]. Second-half underlying EBITDA was NZ$12.46m against NZ$14.92m, 16% lower (8% lower without resale gains).
10. Windhaven Care Holdings kept selling after it fell below 5% on 3 March 2026 (14,119,320 shares then [S20]): the register at 31 May 2026 shows 8,436,999 registered shares, 2.98% [S6]. Registered and beneficial holdings can differ, but it points to about 5.7m more shares sold in March to May.
11. Smaller points. The company now counts five retirement villages: four with residents, and Karori's 14 units, being renovated [S7]. Hokitika's construction is expected to start in early 2027, so only Belfast is under way [S7].

> In short: the first half of FY26 was flattered by resale gains (NZ$1.63m of the year's NZ$1.82m fell in it), but the full year wasn't. NZ$1.8m is a normal year for Radius's 148 village units (NZ$1.8m in FY24, NZ$1.5m in FY25), so doubling the second half understates the base. The real weakness in the second half was costs, and that is what the 1H27 result has to answer. My run-rate for the business with Karori is NZ$29.3m of underlying EBITDA after rent (range NZ$27m to NZ$31m in any plausible case). At NZ$0.415 the market pays 7.0 times that, the middle of the 6.3 to 7.5 times it has paid for 17 months, and my earnings-based value is about NZ$0.42 (NZ$0.33 to NZ$0.52). The owned property (independent values of NZ$151m against NZ$86m of bank debt and the put option) would support about NZ$0.49 if it were turned into cash by sale-and-leasebacks or a bid, but nothing in the next six months does that. Bought today and held to the FY27 result (about 14 May 2027), the expected gain is about +2% before costs and about 0% to -1% after them, against a minimum of 3.65%. The 1H27 result is three days away and answers the question directly, so the case waits for it. It reopens if the first half's underlying EBITDA excluding resale gains is NZ$14.7m or more (NZ$13.3m a year earlier) and the price is NZ$0.44 or less; or, on an in-line result, at NZ$0.39 or less as an ordinary pick and NZ$0.35 or less as a value pick. It closes if that figure is below NZ$13.3m.

## The company in plain words
Radius runs aged care homes. At 12 August 2026 it had 25 care homes with 1,989 care beds (13 homes and 959 beds owned, 12 homes and 1,030 beds leased) and 148 retirement village units at four of its owned homes, with 14 more at Karori being renovated [S7]. Most residents need hospital or dementia level care. Revenue was NZ$202.3m in FY26 (year to 31 March): rest home, hospital and dementia fees NZ$175.8m, accommodation supplements (premium room charges) NZ$12.2m, catering NZ$5.8m (it owns 51% of Cibus Catering), other services NZ$4.4m, village fees and deferred management fees NZ$3.5m [S1, note 2.1]. Health New Zealand's subsidies were NZ$118.1m of it [S1]. The money comes from daily care fees, mostly set by the Government's aged residential care contract, and the margin depends on occupancy, the mix of hospital and dementia residents, premium room charges and wage costs. Wages were NZ$123.0m, 61% of revenue [S1].

Who runs it. Brien Cree founded Radius in 2003 and is executive chair; Andrew Peskett is chief executive and Jeremy Edmonds chief financial officer [S2][S7]. The group now trades as Radius Health; the listed company is still Radius Residential Care Limited.

Who owns it, at 31 May 2026 [S6]: Kade Kings Limited (Brien Cree) 94,821,579 shares, 33.45%; Neil John Foster 5.50%; Jamie Marion Main 4.42%; ACC 4.36%; NZ Depository Nominee 3.27%; Windhaven Care Holdings 2.98%; Citibank Nominees 2.66%; Leveraged Equities Finance 2.48%; Forsyth Barr Custodians 2.40%; then eleven more between 0.65% and 1.81%, including Central Lakes Trust (1.53%) and the independent director Bret Jackson's Takatimu Investments (1.49%). The top 20 hold 76.74%. Neil Foster's company Warehouse Storage Limited is Radius's landlord at St Allisa and other homes [S6, note 5.5].

Five years [S2, pages 5, 12 and 25]:

| Year to 31 March | FY22 | FY23 | FY24 | FY25 | FY26 |
| --- | --- | --- | --- | --- | --- |
| Underlying EBITDA (after rent) | NZ$10.7m | NZ$14.2m | NZ$20.9m | NZ$23.5m | NZ$27.4m |
| Reported profit before tax | NZ$3.1m | -NZ$3.0m | NZ$3.6m | NZ$10.5m | NZ$14.3m |
| EBITDAR per occupied care bed (like for like) | NZ$20.5k | NZ$20.4k | NZ$25.3k | NZ$27.9k | NZ$31.1k |
| Care beds at year end | 1,784 | 1,889 | 1,789 | 1,789 | 1,898 |
| Average occupancy | not read | not read | 91.8% | 92.8% | 94.9% |
| Cash dividend a share | not read | not read | 0.7c | 1.45c | 2.2c |

Underlying EBITDA has grown every year since listing (profit before tax dipped in FY23), in the last three years mostly from higher occupancy, more premium rooms and better margins per bed rather than from more beds. A home was sold in FY24, St Allisa (109 beds) was bought in May 2025 and Karori (90 beds) in May 2026.

## Why big investors may be overlooking it
- Size: a market value of NZ$117.6m. It isn't one of the 20 largest NZX companies (config/nzx_top20.csv); I didn't check NZX 50 membership.
- Trading: a median of about NZ$32,000 a day; many days have fewer than 20 trades [S13].
- Register: the founder holds a third and the top 20 hold 77% [S6].
- Coverage: the only research I found is Forsyth Barr's, which Radius commissions and pays for [X3]. I ran one search for other coverage.
- Sector: New Zealand aged care and retirement companies are out of favour. Oceania Healthcare trades at 0.41 times its net tangible assets [S19]. The Government's funding model is under review after the Ministerial Advisory Group's report of 17 August 2026 [X2].
- A messy history: losses before tax in FY20 and FY23, a home sold in FY24, and NZ$7.2m of imputation credits lost in May 2025 when Cree moved his shares between his own companies [S1, note on imputation credits].

So it is small and closely held, but it isn't unknown: the price has moved with each result.

## What the filings show

### The question: the two halves of FY26
From the half-year and full-year presentations and accounts [S1][S2][S4][S5]; the second half is the full year less the first:

| NZ$m | 1H26 (Apr to Sep 2025) | 2H26 (Oct 2025 to Mar 2026) | FY26 |
| --- | --- | --- | --- |
| Underlying EBITDA (after rent) | 14.92 | 12.46 | 27.38 |
| of which realised resale gains | 1.63 (11 resales) | 0.19 (7 resales) | 1.82 (18 resales) |
| Underlying EBITDA without resale gains | 13.28 | 12.27 | 25.56 |
| Aged care EBITDAR | 27.0 | 26.6 | 53.6 |
| Retirement village EBITDAR | 2.4 | 0.8 | 3.2 |
| Group support and other | -9.8 | -9.9 | -19.7 |
| Rent (before the lease standard) | 4.69 | 5.05 | 9.73 |
| Revenue | 100.2 | 102.1 | 202.3 |
| Employee costs | 59.3 | 63.8 | 123.0 |
| Average occupancy | 95.0% | about 94.8% | 94.9% |

What it shows:
- Resale gains are lumpy by half and steady by year. Realised gains were NZ$1.8m in FY24 (28 resales), NZ$1.5m in FY25 (18) and NZ$1.8m in FY26 (18); by first half NZ$1.4m, NZ$0.6m and NZ$1.6m [S2][S4]. The company said second-half gains were lower because little vacant stock was left at 30 September 2025 [S3]. With 148 units and residents staying about five years on average [S2], 15 to 20 resales a year is normal. So FY26 as a whole wasn't flattered; only its first half was. A normal year is about NZ$1.6m, NZ$0.2m below FY26.
- The second half had a cost problem as well. Employee costs rose 7.7% from the first half to the second while revenue rose 1.8%; employee and other costs together rose 3.5% [S1][S5]. Part of this is seasonal (most public holidays and summer leave fall in October to March, and FY25's second-half wage bill also rose 7.5%), but in FY25 revenue rose 7.8% in the second half and covered it; in FY26 it didn't. Aged care EBITDAR fell NZ$0.4m half on half even with two more months of St Allisa.
- Management didn't see the second half coming: in November 2025 it said 2H26 trading would be "broadly consistent with the first half" [S4]. It was 16% lower, 8% lower without resale gains. The only dollar guidance in two years (for 1H26: NZ$12m to NZ$15m in June 2025, raised to NZ$14m to NZ$16m in August) was met at NZ$14.9m [S15][S4].
- The second half's underlying adjustments were clean: minus NZ$1.0m, mostly removing the NZ$1.5m reversal of past revaluation losses, plus NZ$0.35m of non-cash incentive cost added back [S2, appendix 6]. Nothing in them flatters or depresses the half.

So the answer to the fact sheet's question: the base is neither "FY26 plus Karori at Radius's best rate" (NZ$30.0m) nor "the second half doubled plus Karori" (NZ$27.6m). It is FY26 with normal resale gains, the second half's cost level, the occupancy gains since (96.7% at 12 August 2026 against 94.9% for FY26 [S7]) and Karori at a first-year rate: about NZ$29.3m (Valuation). The 1H27 result settles the cost question.

### Cash earnings and what they are committed to
- FY26 operating cash flow NZ$25.1m, after NZ$4.6m of bank interest, NZ$6.9m of lease interest and NZ$3.5m of tax; lease principal NZ$2.8m; so NZ$22.3m after all rent [S1][S2, appendix 5]. It includes NZ$2.8m of net village receipts (NZ$7.6m from new residents less NZ$4.8m repaid to outgoing ones).
- AFFO (the company's cash earnings: underlying EBITDA less bank interest, tax and depreciation on physical assets as a stand-in for maintenance spending) was NZ$12.7m, 4.5c a share; FY26 dividends of 2.2c a share are 49% of it [S2]. Spending on property and equipment was NZ$14.4m, of which NZ$5.5m was the Belfast land; the other NZ$8.9m included growth such as St Allisa's NZ$0.7m upgrade, so depreciation on physical assets of NZ$6.0m is a fair stand-in for maintenance [S1][S2].
- The cash is largely spoken for. The dividend policy aims at double-digit growth in dividends a share; "fixed asset investment associated with new builds will increase growth capex and will be funded from operating cashflow" [S7]. A NZ$15m development facility was added on 25 May 2026 for Belfast [S9]; construction of the 100-bed Belfast care home has begun and Hokitika's 80-bed home is to start in early 2027 [S7]. From August 2026 every new occupation right agreement carries a nine-month buyback clause, so Radius refunds outgoing residents within nine months even if the unit hasn't resold [S7]. Capital commitments were NZ$2.7m at 31 March 2026 [S1].

### Debt and leases
- Net bank debt NZ$68.7m at 31 March 2026 (NZ$71.6m drawn less NZ$2.8m cash), 2.5 times underlying EBITDA; ASB facilities of NZ$88m at effective rates of 4.63% to 5.58%, expiring 15 June 2027 and 15 June 2028; covenants (fixed charge cover, leverage and equity ratios, measured before the lease standard) all met [S1, note 4].
- On 25 May 2026 the facilities became an ASB and Bank of China syndicate, NZ$30m larger (NZ$15m core, NZ$15m development), all expiring 30 June 2029, with margins and line fees about 0.65 points lower [S9].
- Karori (NZ$13.6m) settled on 26 May 2026, funded by core debt [S8]. The company expects core debt to "remain c$85m following Karori" [S7]. My roll-forward agrees: NZ$68.7m plus NZ$13.6m plus the NZ$3.4m final dividend paid on 11 June is NZ$85.7m before the first half's cash flow. I use NZ$85.0m of net bank debt plus the NZ$1.1m put option over Cibus's other 49% (NZ$86.1m in all) as the claims ahead of shareholders. On my run-rate that is 2.9 times, above the target of below 2.5 times.
- Lease liabilities of NZ$141.5m on the 12 leased homes, with an average current term of 18.8 years and 25.2 years to final expiry [S1][S2, appendix 7]. Rent before the lease standard was NZ$9.7m in FY26 [S2].

### The property and what it is worth
- The twelve owned care homes and the Belfast land were revalued by Long Valuation and Consultancy (LVC) at NZ$108.6m at 31 March 2026, by capitalising notional rents; the sensitivities (half a point on the capitalisation rate moves the value 6.4% to 7.4%) imply rates of about 6.3% to 8.3% [S1, note 3.2]. Belfast land was bought for NZ$5.5m, so the homes are about NZ$103.0m.
- The villages' operator's interest (the value of future fees and resale gains, after residents' refundable deposits of NZ$38.9m) was NZ$30.8m, by LVC, at discount rates of 15.5% to 19.0% [S1, note 3.1].
- Karori: the business and assets, 90 beds and 14 units, for NZ$13.6m, about NZ$151,000 a bed [S8].
- St Allisa: bought on 30 May 2025 for NZ$14.6m; its land and buildings were sold the same day for NZ$13.6m to Warehouse Storage (Neil Foster) and leased back for 30 years with two 10-year renewals [S6, note 5.6]. Rent paid to Warehouse Storage rose from NZ$1.12m in FY25 to NZ$1.98m in FY26 [S6, note 5.5]: about NZ$1.03m a year for St Allisa, an initial yield of about 7.5% (my estimate, assuming the other rent was unchanged).
- Oceania Healthcare sold six care-led villages (299 care beds, 46 independent units, 14 care suites) for about NZ$50m in March 2026, "at or around carrying value", which together "contributed less than $5 million of underlying earnings in FY26" [S17]: at least 10 times their earnings before group costs, for owned homes.

### What has changed since 31 March 2026
- Karori settled; the bank syndicate formed [S8][S9].
- Occupancy was 96.7% on 12 August 2026 (1,923 occupied beds) against 95.6% a year earlier; the company "reiterates that it expects continued underlying growth in key financial metrics in FY27" [S7].
- Funding: the Government committed a 4% increase for aged care providers for the 2026/27 year, about NZ$79m, made up of a 2.66% base increase and targeted spending tied to weekend admissions from hospitals (RNZ via the ODT, 16 June 2026, a secondary source [X1]). Radius's own long-term revenue chart is "based on 1 July 2026 rates" [S7].
- The Ministerial Advisory Group's report (17 August 2026) recommended near-term funding increases, Government funding of clinical care with more means testing of living and accommodation costs, an independent pricing authority and extra funding for new beds; the Government hasn't responded (Ryman's NZX release [X2]).
- No announcement since 28 October 2026 (the 1H27 result date) [S14].

### Holders and dealings
- Directors and senior managers in the last 12 months [S12]: Bret Jackson (independent director) sold 400,000 shares on 18 May 2026 for NZ$163,592 (40.9c); Tom Wilson (independent director) sold 50,600 shares, the second trade on 20 August 2026, for NZ$23,976 (47.4c); Jeremy Edmonds (CFO) bought 50,000 on market on 27 August 2026 for NZ$23,488 (47.0c). Cree sold 490,921 shares into the company's buyback in December 2025 to stay within the Takeovers Code class exemption [S6].
- Windhaven Care Holdings fell from 5.47% to 4.98% (14,119,320 shares) on 3 March 2026 [S20], and the register at 31 May 2026 shows 8,436,999 registered shares (2.98%) [S6], so it appears to have kept selling.
- 5 November 2026 was the busiest session in the last 20: 423,691 shares, NZ$165,240, in 44 trades (about 39.0c) [S13]. No holder notice has followed.
- Capital raisings in two years: none. The buyback that ended 12 December 2025 bought 1,551,429 shares at an average of 33.06c [S6].

## Valuation
Done from the filings, peers and transactions, before using Radius's price.

### The earnings base: run-rate underlying EBITDA after rent, with Karori
From FY26's NZ$27.38m, each step with my low, central and high (NZ$m):

| Step | Low | Central | High | Basis |
| --- | --- | --- | --- | --- |
| Resale gains back to a normal year (NZ$1.0m, NZ$1.6m, NZ$1.8m) | -0.82 | -0.22 | -0.02 | FY24 to FY26 average NZ$1.70m [S2] |
| Occupancy on the 1,899 existing beds (95.0%, 96.0%, 96.7% against 94.9%), at NZ$50k for each extra occupied bed | +0.09 | +1.04 | +1.71 | 96.7% on 12 Aug 2026 [S7]; revenue is about NZ$107k per occupied bed, and about half of it is extra cost |
| St Allisa: a full year, now full and "profitable" | +0.10 | +0.50 | +1.00 | [S3]; a NZ$0.3m pro forma loss before tax in FY26 [S6] |
| Funding (+4% for 2026/27) against wages and other costs | -1.50 | -0.30 | +1.00 | [X1]; the second half's cost creep [S1][S4] |
| Rent: St Allisa's full year and rent reviews | -0.50 | -0.42 | -0.35 | [S2][S6] |
| Group support and new services (home support, Luma, the Radius Health brand) | -1.20 | -0.60 | -0.20 | group costs NZ$19.7m in FY26 [S2] |
| Karori, owned, first full year | +1.00 | +1.80 | +2.60 | [S8]; St Allisa's first year [S6]; Forsyth Barr's NZ$2.6m "within a few years" [X3] |
| Village fees on Karori's and the new villas' first residents | 0.00 | +0.10 | +0.20 | [S7] |
| Run-rate | 24.55 | 29.28 | 33.31 | |

The low column has everything going wrong at once; a plausible bad case is about NZ$27m, a plausible good one about NZ$31m. FY27 itself will be a little below the run-rate (Karori from 27 May, occupancy building through the year).

### Method 1: an earnings multiple, adjusted for the leases
There is no listed New Zealand company that only runs care homes. The usable evidence is for owners of care homes, whose earnings are before rent:
- Regis Healthcare (ASX:REG), an Australian care home owner-operator: underlying EBITDA A$138.0m in FY26 (which includes only A$1.8m of rent), net cash A$173.8m; at A$4.80 (30 October 2026, data/norgate) and about 301.8m shares (underlying NPAT A$55.6m divided by underlying EPS 18.42c) its market value is about A$1,449m and its value as a business A$1,275m: 9.2 times EBITDA [S18]. Australia's funding is different (residents' refundable deposits of A$2.3bn fund the homes interest-free and are left out of that figure), and its sector has had a reform-driven lift.
- Oceania Healthcare (NZX:OCA): at NZ$0.66, 724.2m shares and net debt of NZ$506.7m it is 10.1 times its proforma underlying EBITDA of NZ$97.7m [S16][S19]. That figure isn't comparable: NZ$85.9m of Oceania's underlying EBITDA is realised resale gains (NZ$36.9m) and development margin (NZ$49.0m) [S16], and the market prices Oceania on its assets (0.41 times NTA).
- Oceania's March 2026 sales of six care-led villages at or near book: at least 10 times their earnings before group costs [S17].
- What landlords pay for care home property: about 7.5% initial yield (St Allisa, a related-party sale [S6]); LVC's capitalisation rates of about 6.3% to 8.3% [S1].

Radius pays rent on half its homes, so its after-rent earnings carry fixed claims that an owner's don't. To compare like with like, value Radius as if it owned every home (an owner's multiple M on earnings before rent) and take off the landlords' interest (the rent of NZ$10.15m a year capitalised at 7.5%, NZ$135.3m):

```
Earnings before rent (run-rate)   29.28 + 10.15 = 39.43
M = 8:  8 x 39.43 - 135.3 = 180.1   = 6.15 x after-rent EBITDA   (180.1 - 86.1) / 283.47 = 33.2c
M = 9:  9 x 39.43 - 135.3 = 219.5   = 7.50 x                      (219.5 - 86.1) / 283.47 = 47.1c
M = 10: 10 x 39.43 - 135.3 = 259.0  = 8.84 x                      (259.0 - 86.1) / 283.47 = 61.0c
```

Regis at 9.2 times is the only clean comparator, and Radius is a fraction of its size, far less traded and exposed to New Zealand's funding, so I take M of 8 to 9: 33c to 47c, centre (M of 8.5, 6.8 times after rent) about 40c. Each half turn of after-rent multiple is worth 5.2c a share; each NZ$1m of run-rate is worth about 2.5c at 7 times.

### Method 2: the sum of the parts
Property at the independent and transaction values, plus the operating business on a full market rent:

```
Owned care homes and Belfast land (LVC)      108.6
Karori land and buildings (of the 13.6 paid)  12.0   (my split)
Villages, operator's interest (LVC)           30.8
Property                                     151.4
Notional rent on the owned homes at 7%: (103.0 + 12.0) x 7% = 8.05
Operating business after all rent: 29.28 - 3.0 (villages) - 8.05 = 18.23
At 3x: 151.4 + 54.7 = 206.1   (206.1 - 86.1) / 283.47 = 42.3c
At 4x: 151.4 + 72.9 = 224.3                            48.8c
At 5x: 151.4 + 91.1 = 242.6                            55.2c
```

An operator paying rent of about NZ$18m a year against earnings of NZ$36m before rent is heavily geared, so 3 to 5 times is the range I'd expect a buyer to pay; I found no published sale of a leasehold care business to test it. The property alone, less the claims, is 23.0c a share. This value is only reached if the property is turned into cash: sale-and-leasebacks of owned homes (Radius's framework allows owned homes to be 25% to 50% of the portfolio; they are 48% of beds now [S2][S7]) or a bid. Neither is announced.

### Method 3: a discounted cash flow
Cash flow after rent, tax and maintenance spending (set equal to depreciation on physical assets, NZ$6.4m), growing 2% a year with funding and wages:

```
(29.28 - 6.4) x (1 - 25% tax) = 17.16 a year
WACC 9.5%:  17.16 x 1.02 / 0.075 = 233.4   (233.4 - 86.1) / 283.47 = 51.9c
WACC 10.5%: 17.16 x 1.02 / 0.085 = 205.9                            42.3c
WACC 11.5%: 17.16 x 1.02 / 0.095 = 184.2                            34.6c
```

The discount rate is the input that matters most (each point is about 8c). It should be higher than for an owner because the after-rent cash flow sits behind NZ$141.5m of leases as well as the bank debt; 10.5% is my central case.

Cross-check on cash earnings: run-rate AFFO is 29.28 less interest of NZ$4.4m (NZ$86m at about 5.1%), tax of NZ$4.6m and depreciation of NZ$6.4m, about NZ$13.9m or 4.9c a share. At cash earnings yields of 9% to 12% that is 54c to 41c.

### The range
- As a listed company valued on its earnings: 33c to 52c a share, centre about 42c (Methods 1 and 3). It depends most on the multiple and the run-rate.
- With the property turned into cash: 42c to 55c, centre about 49c (Method 2). It depends on a sale-and-leaseback programme or a bid, so it is a good-case value.
- Net debt: each NZ$3m is 1.1c a share; the 1H27 balance sheet will update it.

## Why the market is wrong
At NZ$0.415, I can't say that it is. The market value plus the claims ahead of shareholders is NZ$203.8m: 7.0 times my run-rate of NZ$29.3m (7.4 times FY26's NZ$27.4m). That is within a cent of my earnings-based centre and in the middle of what the market has paid for 17 months: about 6.3 times after rent in June 2025 (28c, FY25 EBITDA of NZ$23.5m, net debt NZ$67.7m) and about 7.3 to 7.5 times at the August 2026 high of 46.5c on FY26 plus Karori.

Two things the market may be getting wrong. The 1H27 result tests the first; the second has no date:
1. It may be reading the second half's NZ$12.5m as the run-rate. The 1H27 result will show whether that is wrong, but it will probably also show low resale gains (little vacant stock, the new buyback clause), no revaluation gain and more depreciation and interest from Karori, so headline profit may be flat or lower even if care earnings grow. The test is in the appendix figures, not the headline.
2. It values the owned property at about half its independent value: take the NZ$151.4m of property out of NZ$203.8m and the operating business is left at 2.9 times its earnings after a full rent. Only sale-and-leasebacks or a bid would close that. Radius has no sale programme announced, the founder's 33.45% makes a bid without his support unlikely to succeed (he can block a scheme on his own), and he has given no sign of wanting to sell.

So there is no trade at NZ$0.415 before the result.

## Outcomes and chances
If bought at NZ$0.415 now and held to the FY27 result (about 14 May 2027; inferred from 13 May 2026 and 21 May 2025):

| Outcome | What happens | Chance | Price by resolve date |
| --- | --- | --- | --- |
| Bad | 1H27 and FY27 show the second half's costs persisting: run-rate about NZ$27.0m, Karori slow, resale gains low; the market pays 6.5 times after rent, the bottom of its 17-month range (Method 3 at an 11% discount rate on these earnings gives 31.4c; Method 1's owner multiple is then about 8.4) | 30% | NZ$0.315 ((6.5 x 27.0 - 86.1) / 283.47) |
| Middling | Care earnings grow as expected: run-rate about NZ$29.3m, FY27 underlying EBITDA about NZ$28.5m to NZ$29m with "continued growth"; the market keeps paying 7.0 times (Method 3 central, 42.3c; Method 1 at an owner's multiple of about 8.6) | 50% | NZ$0.42 ((7.0 x 29.28 - 86.1) / 283.47 = 41.9c) |
| Good | Care earnings beat: run-rate NZ$31m or more, an upgraded FY27 outlook or a Government funding reset after the advisory group's report, or a first sale-and-leaseback; the market pays 7.75 times (an owner's multiple of about 9.1; Method 2's range) | 20% | NZ$0.545 ((7.75 x 31.0 - 86.1) / 283.47 = 54.4c) |

All three would also receive the interim dividend in December, which I put at 1.1c (1.0c last year, plus the policy's double-digit growth).

```
Expected price: 0.30 x 0.315 + 0.50 x 0.419 + 0.20 x 0.544 = NZ$0.413
With the 1.1c interim dividend: NZ$0.424
Gain before costs: 0.424 / 0.415 - 1 = +2.1% (price only -0.5%)
Round-trip costs on a NZ$2,500 order (the research cap and the NZX order cap):
    brokerage 1.9% capped at NZ$25: 0% to 1.0% in (the month's plan cover), 1.0% out
    spread as src/decide.py estimates it (Corwin and Schultz, last 21 FinFeed sessions): 1.09%, above the 0.6% floor
    = 2.1% to 3.1%; at the 6 November quoted spread of 3.7% (bid 0.400, offer 0.415), 4.7% to 5.7%
Gain after costs: +0.0% to -1.0% (-2.6% to -3.6% at the quoted spread)
Minimum (rulebook 5a): (2.13% cash rate + 5%) x 187 / 365 = +3.65%
```

By outcome (price only): bad -24.0%, middling +1.0%, good +31.0%. Not a case at NZ$0.415. With these outcomes the price that clears the minimum is NZ$0.397 at 3.1% costs and NZ$0.388 at the quoted spread.

As a value pick held to the FY28 result (about 12 May 2028): bad NZ$0.315 (-24.0%, or -15.0% with 3.75c of dividends), middling NZ$0.449 (7.0 times a FY28 run-rate of NZ$30.5m with debt about flat: +8.3%, or +17.3% with dividends). It fails the bad-case leg. On share prices alone both legs pass at NZ$0.35 or less.

## Dated events
- 11 November 2026: H1 FY27 result (announced) [S11]. It covers April to September 2026, with Karori from 27 May, occupancy near 96% to 97%, the 1 July funding increase and the new buyback clause.
- About 3 December 2026: interim dividend ex-date, paid about 18 December (inferred from 2025 [S13]).
- No date: the Government's response to the Ministerial Advisory Group's report [X2]; any sale-and-leaseback or sale of Karori's 14 units (up to about NZ$7m over several years, Forsyth Barr's estimate [X3]).
- Early 2027: Hokitika construction to start [S7].
- About 14 May 2027: FY27 result and the FY28 outlook (inferred). This is the resolve date for an ordinary pick. If the date is set later than six months after entry, only a value pick can hold to it.
- About mid-November 2027 and mid-May 2028: 1H28 and FY28 results (a value pick's resolve date).
- 30 June 2029: bank facilities expire [S9].

What in the 1H27 result reopens or closes the case. The figures come from the result presentation's appendices (the underlying EBITDA reconciliation, its "realised gains on resales" line, the segment EBITDAR table and the operating metrics):

| Measure (six months to 30 Sep 2026) | 1H26 | Strong | In line | Closes the case |
| --- | --- | --- | --- | --- |
| Underlying EBITDA less realised resale gains | NZ$13.28m | NZ$14.7m or more (run-rate NZ$31m) | NZ$13.8m to NZ$14.7m | below NZ$13.3m |
| Aged care underlying EBITDAR | NZ$27.0m | NZ$29.5m or more | NZ$28.0m to NZ$29.5m | below NZ$28.0m |
| Average care bed occupancy | 95.0% | 96.5% or more | 95.5% to 96.5% | below 95.5% |
| Net bank debt at 30 September 2026 | NZ$63.7m | NZ$88m or less | NZ$88m or less | above NZ$92m |
| FY27 outlook | 1H26 said 2H26 would be "broadly consistent" with 1H26 (it was 16% lower) | raised, or underlying EBITDA of NZ$30m or more | "continued growth" kept | growth wording dropped, or below NZ$28.5m |

The run-rate is read from the first line: add the 1.9 months of Karori not yet in the half (about NZ$0.3m), double it, add normal resale gains of NZ$1.6m and take off a second-half cost gap of NZ$0 to NZ$1.0m (FY26's was NZ$1.0m; I use NZ$0.5m). So NZ$14.7m points to about NZ$31m ((14.7 + 0.3) x 2 + 1.6 - 0.5) and NZ$13.8m to about NZ$29.3m.

Reopen if any one of these holds:
1. Strong on the first two lines, net bank debt NZ$88m or less, and the outlook kept or raised, with the price NZ$0.44 or less after the result: re-test as an ordinary pick to the FY27 result. With outcomes of NZ$0.354, NZ$0.462 and NZ$0.585 at 25%, 55% and 20%, the expected gain at NZ$0.415 is about +10% after costs, against 3.6%.
2. In line, and the price is NZ$0.39 or less: re-test as an ordinary pick (outcomes as in the table above). At NZ$0.35 or less: re-test as a value pick to the FY28 result (bad 10% below, middling 28% above on share prices alone).
3. At any time, a sale-and-leaseback of owned homes at yields near 7% to 7.5%, a sale of the Karori units, or an approach for the company: re-test with the good case at the sum-of-the-parts value (49c to 55c).

Close (no case) if any line of the last column holds. Then the bad case (run-rate about NZ$27m or less) becomes the middle, and a value pick would need a price of about NZ$0.30 or less (bad case 6.5 times NZ$25.0m, 26.9c; middling 7 times NZ$27.5m, 37.5c).

Watch trigger: NZ$0.39 after an in-line result (NZ$0.44 after a strong one; NZ$0.35 for a value pick).

## What would make this wrong
1. The market pays more than 7 times once growth without resale gains shows. The shares reached 46.5c in August on less information, Forsyth Barr's sponsored valuation is 54c, and the property alone covers 23c a share after debt. If 1H27 is strong, the price may pass NZ$0.44 on the day and waiting will have cost 10% or more. No position could have been in place before 11 November in any case.
2. The run-rate is lower than NZ$29.3m. The second half's wage creep continues, Karori takes years to reach Radius's margins (as St Allisa did), resale gains stay low under the nine-month buyback clause, and building Belfast and Hokitika lifts debt. Then even NZ$0.39 isn't cheap and the bad case becomes the middle.
3. Funding policy. A Government response to the advisory group's report could add to margins (more for clinical care, an independent pricing authority) or take from them (if premium room charges or means testing change against operators). It has no date.

Exit rule, if a position is ever taken: sell at the first half-year or full-year result whose underlying EBITDA less resale gains is below the same period a year earlier, if net bank debt passes 3.25 times underlying EBITDA, or when the price reaches the good-case value; otherwise at the resolve date.

## Checks
- Not on Cam's excluded list (config/judgement_excluded.csv has no entries; confirmed by Cam on 8 November 2026).
- No placement-pattern reopening (rulebook section 9): Radius hasn't been halted and has raised no capital in two years (a buyback, employee share rights and an employee share scheme only) [S14]; the worst opening gap in the 30 FinFeed sessions from 22 September to 6 November 2026 was -1.3% (30 October). The section 9 rule applies to ASX shares in any case.
- Liquidity (section 3): median NZ$32,278 a day over 9 October to 6 November 2026 from NZX's data [S13]. Two sessions at 10% of that is NZ$6,456; the 2.5% research cap and the NZX order cap (NZ$2,500) bind first.

## What I couldn't verify
- Any 1H27 figure (due 11 November); Karori's earnings and occupancy since settlement.
- How earnings split between owned and leased homes; LVC's actual capitalisation rates (only sensitivities are published); my NZ$12.0m split of Karori's price into land and buildings.
- St Allisa's rent (estimated from the change in rent paid to Warehouse Storage, assuming the other leases were unchanged).
- Whether first sales of new villas and Karori's units will count in underlying EBITDA (the reconciliation shows only resale gains).
- The start date and split of the 4% funding increase from a primary source (I used RNZ via the ODT).
- The FY27 result date; Regis's share count (derived from its underlying NPAT and EPS); Oceania's net debt after 31 March 2026; NZX 50 membership; any broker coverage beyond Forsyth Barr's sponsored notes.
- Who bought the 423,691 shares on 5 November 2026.

## Sources
Radius (NZX:RAD), primary:
- [S1] FY26 audited financial statements (13 May 2026): https://api.nzx.com/public/announcement/472508/attachment/468249/472508-468249.pdf (announcement https://www.nzx.com/announcements/472508)
- [S2] FY26 investor presentation (13 May 2026): https://api.nzx.com/public/announcement/472508/attachment/468248/472508-468248.pdf
- [S3] FY26 media release (13 May 2026): https://api.nzx.com/public/announcement/472508/attachment/468247/472508-468247.pdf
- [S4] 1H26 investor presentation (19 November 2025): https://api.nzx.com/public/announcement/462893/attachment/457017/462893-457017.pdf
- [S5] 1H26 interim report (19 November 2025): https://api.nzx.com/public/announcement/462893/attachment/457018/462893-457018.pdf
- [S6] Annual Report 2026 (29 June 2026; holders, related parties, St Allisa business combination, buyback): https://api.nzx.com/public/announcement/475175/attachment/471511/475175-471511.pdf
- [S7] Investor day presentation (12 August 2026): https://api.nzx.com/public/announcement/477696/attachment/474321/477696-474321.pdf (announcement https://www.nzx.com/announcements/477696)
- [S8] Karori agreement (1 April 2026): https://api.nzx.com/public/announcement/470273/attachment/465774/470273-465774.pdf ; Karori completion (26 May 2026): https://api.nzx.com/public/announcement/473345/attachment/469383/473345-469383.pdf
- [S9] Loan syndication (25 May 2026): https://api.nzx.com/public/announcement/473220/attachment/469221/473220-469221.pdf
- [S10] Belfast land acquired (3 March 2026): https://api.nzx.com/public/announcement/468582/attachment/463790/468582-463790.pdf
- [S11] 1H27 result date (28 October 2026): https://www.nzx.com/announcements/482538
- [S12] Director and senior manager notices: Bret Jackson https://api.nzx.com/public/announcement/473202/attachment/469185/473202-469185.pdf ; Tom Wilson https://api.nzx.com/public/announcement/478619/attachment/475505/478619-475505.pdf ; Jeremy Edmonds https://api.nzx.com/public/announcement/478706/attachment/475647/478706-475647.pdf
- [S13] NZX activity data, read 8 November 2026: https://api.nzx.com/public/instrument/NZRADE0005S4/metrics/activity/past/2Y.json ; NZX company data (close, bid, offer, shares, dividends), fetched 7 November 2026: data/research_data/nzx_company.json ; FinFeed prices: data/prices/NZX/RAD.csv
- [S14] NZX announcement lists, 2025 and 2026: https://api.nzx.com/public/company/RAD000000/announcements/2026/all.json and https://api.nzx.com/public/company/RAD000000/announcements/2025/all.json
- [S15] FY26 outlook upgrades: 13 June 2025 https://api.nzx.com/public/announcement/453290/attachment/445557/453290-445557.pdf (announcement https://www.nzx.com/announcements/453290) ; 7 August 2025 https://www.nzx.com/announcements/456350
- [S20] Windhaven Care Holdings substantial holder notice (4 March 2026): https://api.nzx.com/public/announcement/468656/attachment/463870/468656-463870.pdf

Peers, primary:
- [S16] Oceania Healthcare FY26 result (22 May 2026): release https://www.nzx.com/announcements/473127 ; investor presentation https://api.nzx.com/public/announcement/473127/attachment/469120/473127-469120.pdf
- [S17] Oceania Healthcare, update on divestments (2 March 2026): https://www.nzx.com/announcements/468413
- [S18] Regis Healthcare FY26 results announcement (24 August 2026): https://announcements.asx.com.au/asxpdf/20260824/pdf/0733gqs8trn36c.pdf ; price A$4.80 on 30 October 2026 from data/norgate/universe/prices_2026.csv.gz
- [S19] Oceania price, shares and NTA: data/research_data/nzx_company.json (close NZ$0.66 on 6 November 2026; 724,231,030 shares; NTA NZ$1.62)

Secondary, named:
- [X1] RNZ via the Otago Daily Times, "$79m boost for aged residential care services" (16 June 2026): https://www.odt.co.nz/news/national/79m-boost-aged-residential-care-services-rnz
- [X2] Ryman Healthcare's NZX release on the Ministerial Advisory Group report (18 August 2026): https://www.nzx.com/announcements/478010 ; MinterEllison summary (18 August 2026): https://minterellison.co.nz/insights/aged-care-reform-ministerial-advisory-group-releases-recommendations
- [X3] Forsyth Barr, "Care Arrives in the Capital" (2 April 2026; research commissioned and paid for by Radius): https://www.forsythbarr.co.nz/assets/publications/RAD-2026-04-02-Care-Arrives-in-the-Capital.pdf
