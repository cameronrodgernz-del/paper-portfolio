# GDI Property Group (ASX:GDI): red team review of the value pick deep dive. Don't buy at A$0.64

Written 2026-11-08 by the red team, on research/picks/GDI.md (8 November 2026): "case for review as a value pick (marginal)", A$0.64, resolve 31 August 2028. Before writing this I read only that deep dive, docs/RED_TEAM.md, RULEBOOK.md sections 3, 4 and 5a, and src/decide.py and src/risk.py for how the minimum gain and the outcomes are worked out. I read no other research file. This is a simulation and not financial advice.

Rules as they stand (section 5a, changed 8 November 2026): a value pick needs its bad case no more than 10% below the price and its middling case at least 15% above it; every research pick needs an expected gain after costs of at least the cash rate plus 5% a year over the days to its resolve date. src/decide.py works that out as (2.13% + 5%) x 661 / 365 = 12.9% for a card placed on 9 November 2026. The deep dive was written after these changes and already applies them, so I test it against them as they stand.

Verdict: don't buy. Reasons in the last section.

> In short. Most of the facts hold: I re-opened the sources for 15 of them (table below). One reading is wrong and it matters. The A$175m swap at 3.72% can be cancelled by the bank, and a bank cancels such a swap when rates are above 3.72%, not below, so GDI keeps the protection only in the world where it doesn't need it. With three-month bills at 4.80% and six-month bills at 5.17% in October 2026, the likely outcome is no hedging at all from January 2028, when the A$100m cap has also ended. On rates flat near 5%, FY28 net interest is about A$23.0m, not the deep dive's A$21.0m, and the FY29 run-rate the market will price in August 2028 is about A$24.3m: 0.4c to 0.6c off cash earnings per security. Beyond that, the case isn't "clearly cheap on its own figures", which is what a value pick needs, and the deep dive says so itself: at A$0.64 the market already pays about 6.9% on the deep dive's FY28 middling cash once the interest is corrected, which is Growthpoint's yield, for a one-city, sub-scale Perth owner. The return is the distribution, and the 5.0c isn't covered by cash: the FY26 cash flow statement covers 59% of it, with asset sales paying the rest. The bad case counts all four 2.5c payments in full, which is the best version of bad, not the floor; with a cut row the bad case is about -15%, outside the 10% limit. The price has also had a prop: the Rockefeller group bought 34.5% of all GDI volume from 13 January to 14 September 2026, and GDI returned +5% in 2026 to 30 October while listed office peers returned -15% to -28%. On my numbers the expected gain after costs is about +8.8% against the 12.9% minimum, and the expected price in August 2028 is about A$0.62, below today's.

## 1. Are the facts right?

| # | What the deep dive says | Source re-opened | Held? |
| --- | --- | --- | --- |
| 1 | Price A$0.64 on 6 Nov 2026, A$0.64 the session before, market value A$345.1m, 539,196,501 securities | data/research_data/asx_company.json: priceLast 0.64, priceClose 0.64, marketCap 345,085,761, numOfShares 539,196,501 | Held |
| 2 | FY26 FFO A$44.5m, 8.24c; distributions 5.0c (A$27.0m); NTA A$1.21; GDI's A$1.7m share of the Co-living JV's tax added back to FFO | [G1] Appendix 4E highlights, FFO reconciliation and footnote | Held |
| 3 | Rent-free given (incentives paid, GDI Property Trust) A$16.2m in FY26 and A$13.0m in FY25; property improvements A$9.4m and A$17.6m; amortisation of incentives A$17.9m; maintenance A$0.8m; lease costs A$0.9m; first half of FY26 A$8.3m rent-free and A$5.9m improvements | [G1] note 9(a); [G7] investment property note | Held |
| 4 | WS1 A$400.0m and WS2 A$105.0m at 6.50%, valued 31 Dec 2025; 197 St Georges Tce A$234.0m at 7.00% and 5 Mill St A$54.0m at 7.25%, 30 Jun 2026; 180 Hay St a June 2025 value; total A$962.6m | [G2] pages 19 to 22; [G1] note 9(e) | Held. Also there: WS1's discount rate is 6.88% and WS2's 7.00% |
| 5 | Lease expiries by income read from the bar charts | [G2] page 27, rendered and read again | Held, within a point or two |
| 6 | A$343.3m drawn of A$421.5m plus a A$5m guarantee; Tranche A to Feb 2029, Tranche B (A$210.75m) to Feb 2028; LVR 37.1% (covenant 50%), ICR 2.4x (covenant 1.5x) | [G1] directors' report and note 28; [G3]; [G18] | Held |
| 7 | A$100m cap at 3.75% (2.65% floor) to Dec 2026, then a 12-month cap at 4.50%; A$175m swap at 3.72% to Jan 2031, cancellable by the counterparty on 1 Jan 2028, 2029 and 2030 | [G1] note 28 | The facts hold; the reading of the cancellation is wrong (section 3d) |
| 8 | Distribution dates (ex 30 Dec 2025, paid 27 Feb 2026; ex 29 Jun 2026, paid 31 Aug 2026); FY27 "seeking to pay a cash distribution of 5.0 cents", "may be paid wholly or partly out of capital" | [G20]; [G3] | Held |
| 9 | AGM: "maintain our through-cycle distribution of 5.00 cents"; A$78.0m undrawn; "$100.0 million in total remaining, noting approximately $50.0 million already released" from Autoleague | [G5] | Held |
| 10 | Buy-back: 632,029 securities for A$394,708, nothing after 14 October | [G13] 15 Oct update (625,984 plus 6,045; A$390,990 plus A$3,718); ASX list to 6 Nov shows no later update | Held |
| 11 | Rockefeller group 54,602,296 securities, 10.11%; last batch 9 to 14 Sep at about A$0.63 | [G14] 14 Sep 2026 notice | Held |
| 12 | Burns sold 500,000 for A$301,000 on 29 May 2026 and holds 2,938,729 | [G17] 3 Jun notice; 8 Sep notice (1,328,906 rights vested into securities on 4 Sep, which is how he reached 2,938,729) | Held |
| 13 | Salt and Pathfinder 6.03% | 4 Mar 2026 change of substantial holding [G23] | Held |
| 14 | Knight Frank Q2 2026: Perth prime yield 7.90% (up 32 points of a percent after 21 flat months), net incentive 47.0%, net face rent A$749, prime vacancy 15.6%; 1 Nash St A$79.4m at 8.3% (WALE 5.5 years), 66 St Georges Tce A$75.0m at 8.2% | [M1] | Held. Also: Perth's 7.90% is the highest prime yield of the capital cities (Sydney 5.70%, Melbourne 7.02%, Brisbane 7.25%, Adelaide 7.43%) [M4] |
| 15 | Peer cash: Abacus A$81.2m - 12.6 - 10.3 - 18.1 = A$40.2m, 4.50c on 893.7m; Growthpoint A$177.6m - 15.2 - 19.2 - 11.3 - 30.8 = A$101.1m, 13.40c on 754.3m; Centuria Office FFO A$66.9m, maintenance A$7.1m, capex incentives A$10.5m | [P1]; [P2]; [P3] presentation | Held. COF's A$25.6m rent-free line is in its financial report, which I didn't open |

What the deep dive gets wrong or leaves out:
1. The swap. It says "the swap is below market, so the bank is unlikely to cancel it while rates stay up". It's the other way round (section 3d).
2. GDI's own capital rules. Its policy is to "target gearing of less than 40%", and the note lists "adjusting the level of distributions paid to securityholders" among the ways it manages capital [G1, note 28]. That's the board telling holders where the distribution sits when gearing rises.
3. Cash cover from the cash flow statement. Operating cash flow A$21.6m, plus A$5.2m from the JV, less A$10.0m of capital spending and A$0.9m of incentives and leasing fees, is A$15.9m (2.95c): 59% of the A$26.9m paid to GDI holders in FY26, or 50% after the A$2.4m spent on Mill Green works [G1, cash flow statement]. Debt fell in FY26 (A$37.5m repaid, A$5.0m drawn) because A$81.3m of asset sales came in. So FY26's shortfall was paid from sale money; FY27's will be paid from the Autoleague money (about A$18.4m back to GDI in August 2026) and then from the facility.
4. The JV's cash. The deep dive notes that only A$5.2m came back from the JV in FY26, but its "cash kept" still counts the JV's after-tax FFO (about A$7.75m) in full, about 0.5c a security that never reached GDI. And it's getting thinner: A$4.6m came in the first half and A$0.6m in the second [G1, G7]. The JV's borrowings rose from A$33.9m to A$57.5m (whole JV) and its profits "cannot be distributed without consent from the two joint venture partners" [G1, note 14].
5. Who held the price up. The Rockefeller group's 34,182,296 securities bought from 13 January to 14 September 2026 were 34.5% of all GDI volume in that time (99.1m, Norgate [D1]). GDI's total return in 2026 to 30 October was +5.0%; Centuria Office -17.5%, Abacus -27.6%, Growthpoint -16.1%, Dexus -14.5%, Cromwell -21.6% [D1]. The deep dive says GDI was flat while peers fell, but not why.
6. What the valuers assume: tenant retention of 50% and 12 to 24 months of downtime [G1, note 9(b)]. That matters for the FY28 expiries at 197 St Georges Tce and 5 Mill St (section 3b).
7. Costs with the plan's cover. The engine charges the sale brokerage even when the plan covers the buy (src/decide.py, entry_costs: "a later sale, no cover left"), so with cover the round trip is about 2.3%, not 1.5%. The deep dive's "+16.9% with plan cover" is +16.2% on its own outcomes.
8. A small reporting point: the first-half FY26 cash flow statement put A$9.1m of "payment of tenant incentives and leasing fees" in investing (rent-free grossed up), while the full-year statement shows A$0.9m on that line [G7, G1]. The two aren't on the same basis, so half-year cash lines can't be compared directly. Not material to the case.
9. Nothing found on capital raisings (none in two years), litigation or regulators. The audit opinion (Hall Chadwick) is unqualified, with investment property values as the key audit matter; it records a policy of valuing the portfolio "annually on a rotation basis or more frequently if market conditions are volatile" [G1, pages 80 to 81]. Giles Woodgate, chair since April 2024, left the board on 31 October 2026 holding 600,000 securities [G24].

## 2. Is it really overlooked, or cheap for a reason?

It isn't cheap against its peers on anything but NTA, and the NTA is the soft number:

| At 30 Oct 2026 (6 Nov for GDI) | GDI | Centuria Office | Abacus | Growthpoint |
| --- | --- | --- | --- | --- |
| FFO yield | 12.9% (8.24c at A$0.64) | 12.8% (11.2c at A$0.875) | 10.8% (9.08c at A$0.84) | 12.0% (23.5c at A$1.965) |
| Trailing cash yield | 5.0% | 4.5% | 5.4% | 6.8% |
| Distribution yield | 7.8% | 10.3% | 8.0% | 9.4% |
| Price to NTA (deep dive's figures) | 0.53 | 0.53 | 0.53 | 0.64 |

FFO and distributions from [G1], [P1], [P2], [P3]; prices from [D1], [D2].

- The NTA rests on WS1 and WS2 at 6.50% in the city with the widest prime yields in the country (section 3c).
- The price has been held up by one buyer in a falling sector. That is the mirror of "a falling price with heavy volume": a flat price held by heavy buying from one holder. There has been no Rockefeller notice since 14 September (they can add about 1% before the next one) and no buy-back since 14 October. The price went from A$0.66 on 1 September to A$0.615 on 6 October and back to A$0.64 at the AGM [D1]. How GDI trades without that support hasn't been tested.
- Industry trouble the peers already show: office REITs fell 15% to 28% in 2026; Abacus cut its distribution from 8.5c to 6.7c and now targets 80% to 90% of FFO [P1]; Centuria Office from 10.1c to 9.0c [P3]; Growthpoint held 18.4c but is reviewing its payout ratio and considering a reinvestment plan [P2].
- Debt that falls due before the resolve date: Tranche B (A$210.75m) in February 2028, refinanced by a sub-scale Perth office borrower in a market where rates are still rising and its hedges have ended.
- Management's record: fit-out spending did fall as promised, and the 5.0c has been held. But the A$100m non-core sale target has been on the slides since August 2025 with nothing on the balance sheet sold against it beyond the Autoleague fund's buildings; the managing director sold 500,000 securities at A$0.602 in May 2026; and the chair who ran the board through 2024 to 2026 has left.

## 3. The valuation

### 3a. Is the 5.0c safe, and is it paid from debt?
- It has never been covered by cash in the deep dive's window of history: cash kept was -1.86c (FY24), 0.39c (FY25) and 3.18c (FY26) on the deep dive's measure, and 2.95c in FY26 on the cash flow statement. The gap was paid from asset sales and, in FY24 and FY25, from debt.
- FY27 will be paid: the Autoleague money (A$12.2m of capital and A$6.2m of fees) plus the second-half run-rate covers it, and the board has said so twice since August.
- FY28 is the question, decided at the FY27 result around 24 August 2027. In the deep dive's middling case, FY28 cash is 4.8c; with my interest correction 4.4c, and about 3.9c after the JV's retained cash. So even in the middle, 10% to 20% of FY28's payment comes from debt. In the bad case (2.4c with the interest correction) about half of each payment is borrowed: about A$14m a year, which takes gearing up and NTA down about 2.5c a year.
- For the board holding it: three AGMs of firm language, "distributions remain a priority" [G5], and 5.0c is only 61% of FFO, so a board that sets its payout against FFO (as Abacus and Growthpoint now do) doesn't see a problem. Against: a new chair whose stated aim is the NTA gap, a buy-back competing for the same cash, peers cutting, hedges ending, a refinancing in February 2028, and the board's own note naming distributions as a lever.
- My chance of a cut that reduces the February or August 2028 payments: about 15% overall, and about 45% if the bad case happens (cash near 2.5c to 3c, values falling, bank LVR in the low-to-mid 40s going into the refinancing).

### 3b. Rent-free and leasing costs as the buildings re-lease
- Expiries by income [G2, page 27]: WS1 about 6% in FY28 and 14% in FY29; WS2 nothing until FY29, then about 9% a year; 197 St Georges Tce 3% in FY27, 27% in FY28, 12% in FY29, 20% in FY30, 18% in FY31; 5 Mill St 13% in FY27, 21% in FY28, 34% in FY29, 24% in FY30. So WS1 and WS2 re-lease mostly from FY29: outside the window's cash, but inside what the market prices in August 2028. 197 and 5 Mill re-lease inside it.
- Rough size of FY28: about A$7m of income expires (197 about A$4m to A$5m, WS1 about A$1.8m, 5 Mill about A$0.7m; my estimate from the FFO and the charts). At the valuers' 50% retention, with new leases at Knight Frank's 47% prime and 50% secondary incentives and renewals cheaper, that is roughly A$10m to A$13m of incentives committed on five-year terms in FY28, plus months without rent on the half that leaves. The deep dive's FY28 middling holds rent-free at A$10m and fit-outs at A$4m, and has property FFO a little higher than FY27. That is consistent only if most tenants renew; with the valuers' own retention and downtime, I'd expect A$0.5m to A$1.5m less property FFO in FY28 and more in FY29. I haven't put this in my numbers below; it's a further risk.
- The accounting charge for incentives already in the leases has been climbing: amortisation A$10.8m (FY24), A$13.8m (FY25), A$17.9m (FY26) [G1, G9]. That's the right base for a buyer looking past the lull in FY27 to FY28, and it's what the deep dive's through-cycle 3.69c uses.
- The first half of FY27 includes rent-free for the leases that took WS1 and WS2 to 100% after balance date and for the 197 office lease-up. I'd expect that half to show rent-free nearer A$7m than the A$6m the deep dive wants to see, which puts its exit rule (b) in play at the first test.

### 3c. The December 2026 valuations, Perth evidence and covenant headroom
- WS1 and WS2 are at 6.50% (discount rates 6.88% and 7.00%) [G2]. Knight Frank's Perth prime average is 7.90% after rising 32 points of a percent in Q2 2026, the highest of the capital cities; the two Perth investment sales with yields were 8.2% and 8.3%, and 1 Nash Street's 5.5-year WALE is close to WS1's 6.0 [M1, M4]. The RBA's cash rate has gone from 4.35% (June) to 4.60% (October) since [M3]; Knight Frank's own table had the ten-year bond at about 5.0% for 2026, so WS1's 6.88% discount rate is less than two points over the bond. WS1's State Government lease to FY34 earns it a tighter yield than the average, but not 140 points tighter than Melbourne's and Brisbane's averages.
- WS1, WS2, the car parks and Townsville are due for their annual valuations at 31 December 2026 (audit report policy above). I put the chance of a write-down on WS1 and WS2 by June 2027 at about 60%. A 0.25-point move is about -A$19m and a 0.5-point move about -A$36m, before rent growth (Perth prime face rents +2.8% in the year to Q2 2026 is worth about A$14m on the two): NTA -1c to -4c from the December round, more if 197 and 5 Mill follow at June 2027.
- Covenant headroom (bank LVR is debt on the facility, net of derivatives, over the last independent values of the secured buildings, A$921.3m) [G1, note 28]:

| Case | Secured values | Drawn debt | LVR |
| --- | --- | --- | --- |
| 30 June 2026 | A$921m | A$343m | 37.1% |
| WS1 and WS2 out 0.5 points, no rent growth, debt +A$10m by June 2027 | A$885m | A$353m | 39.9% |
| The four towers at Knight Frank's 7.9% (the deep dive's own mark), debt +A$25m by June 2028 | A$822m | A$368m | 44.8% |
| Breach at 50% with A$368m drawn | A$737m | A$368m | values 20% below book |

- Interest cover: 2.4 times on FY26's A$20.2m of interest; the same earnings over a A$24.3m run-rate is about 2.0 times, against 1.5. GDI's own gearing measure (target under 40%) goes from 33% to about 37% in the tough case.
- So a covenant breach inside the window is unlikely (under 3% on my estimate). The pressure arrives as a board choice instead: an LVR in the low-to-mid 40s going into the February 2028 refinancing is when boards trim distributions or sell buildings at the market's price.

### 3d. The hedges and interest
- How the swap works: GDI pays 3.72% fixed and receives the floating rate; the bank receives 3.72%. On each call date, if market rates for the swap's remaining term are above 3.72%, the swap costs the bank money and it cancels; if they're below, it keeps the swap. So GDI keeps the protection only when it doesn't need it. The small fair value of all GDI's derivatives at 30 June 2026 (A$1.38m, with three-month bills at 4.46%) fits a bank option worth a good deal [G1, note 13].
- So from January 2028 GDI is likely to have no cover at all: the A$100m 3.75% cap ends in December 2026, the 4.50% cap runs only through calendar 2027, and the swap goes on 1 January 2028 unless rates have fallen below about 3.7% by then.
- My model of net interest for FFO (python3 -I, in the scratchpad, not committed): margin and fees about 2.0% over the base rate, calibrated to FY26's A$20.2m on about A$361m of average drawn debt and the RBA's monthly three-month bill rates [M3]; middle-case debt A$345m (FY27) and A$355m (FY28):

| Base rate path | FY27 | FY28 | FY29 run-rate |
| --- | --- | --- | --- |
| Flat near 5.0% (six-month bills were 5.17% in October) | A$20.4m | A$23.0m | A$24.3m |
| Easing to 4.25% during 2028 | A$20.4m | A$21.5m | A$21.7m |
| Up to 5.5% | A$20.5m | A$24.0m | A$26.1m |
| Deep dive | A$20.4m | A$21.0m | (not stated) |

- FY27 agrees with the deep dive. FY28 is A$0.5m to A$3m higher, and the run-rate the market prices in August 2028 A$0.7m to A$5m higher. On flat rates that's -0.37c on FY28 cash and -0.61c on through-cycle cash. Corrected: FY28 middling 4.80c becomes 4.43c, bad 3.00c becomes 2.44c (bad-case debt A$370m), good 6.10c becomes 5.73c, through-cycle 3.69c becomes 3.08c.

### 3e. The peer cash yields
- The Abacus and Growthpoint arithmetic holds [P1, P2]. Centuria Office's FFO, maintenance and capex incentives hold [P3]; its rent-free line and Dexus's 7.2% to 7.8% weren't re-opened (Dexus comes from another research file I'm not reading before writing this).
- They aren't clean comparisons. Abacus is office plus retail (18%), self storage (10%) and funds management (13%) [P1]; Growthpoint is roughly 70% office and 30% industrial [P2]; none is a Perth landlord. Perth has the widest prime yield of the capital cities and incentives about as high as Melbourne's (47% against 48.1%) [M4]. A sub-scale, ex-index, one-city stapled group with a mining-camp JV should sit at or above the top of this range, not in the middle.
- The yields are trailing (FY26 cash) and GDI is valued on a forecast (FY28 cash). At A$0.64 GDI already trades at 6.6% on the deep dive's FY27 middling cash (4.25c) and 6.9% on FY28 middling corrected for interest (4.43c): Growthpoint's yield. The price already pays for the recovery the case is waiting for.
- Method 1 corrected, at the deep dive's 6.1% middle yield: FY28 middling A$0.73, through-cycle A$0.50, midpoint A$0.62 (the deep dive's A$0.70). At Growthpoint's 6.82%: A$0.65 and A$0.45.

### 3f. Is the bad case the floor, and is the middling case what the market would pay?
- Middling: the deep dive's A$0.68 needs GDI to move from 0.53 to 0.585 times NTA, the peer middle. With NTA about A$1.13 by mid-2028 (WS1 and WS2 out 0.25 to 0.5 points, about 2c of debt-funded payout), 0.585 times gives A$0.66 and GDI's own 0.53 times A$0.60; corrected Method 1 gives A$0.62 to A$0.73. I use A$0.65, which is generous to the case: with 10c of distributions, A$0.75 (+17.2%), which passes the 15% bar.
- Bad: the deep dive's A$0.60 is A$0.50 plus all four distributions. The A$0.50 itself is fair (0.45 times an NTA of A$1.08 is A$0.49; the lowest close since 2023 is A$0.515). The issue is the 10c. I split it into two rows: distributions held from debt (A$0.49 plus 10c, A$0.59, -7.8%), and a cut to 3.5c a year from the February 2028 payment (A$0.46, about 7.5% on the new 3.5c, plus 8.5c, A$0.545, -14.8%).
- Good: the deep dive's A$0.84 holds after the interest correction (FY28 good cash of 5.73c at 6.82% is A$0.84), plus 10c, A$0.94.

## 4. The dated events and the exit
- The 31 December 2026 valuations and the 1H FY27 result (about 16 February 2027) are real tests. But GDI's results have moved the price only 4% to 6%, and the move faded each time: FY25 result A$0.685 to A$0.715, back to A$0.635 by December 2025; 1H FY26 A$0.595 to A$0.625; FY26 result A$0.625 to A$0.665, back to A$0.615 by early October [D1]. The market has not re-rated GDI on FFO growth, which is a sign it is pricing cash and the distribution, not FFO.
- Two dated events against the case should be on any card: 1 January 2028 (the bank's first chance to cancel the swap, with the cap already gone) and February 2028 (Tranche B refinancing).
- The exit rule: (b) is likely to be tested hard at the first half (above). (c), NTA below A$1.10, needs about A$59m of write-downs and won't trigger on a normal round; "WS1 and WS2 written down by more than 5% at December 2026" is the useful test.
- Timing: the fourth distribution (ex about 29 June 2028) is paid about 31 August 2028, the resolve date itself (31 August in 2026, 29 August in 2025 [G20]). The ledger credits holders on the ex-date when it's paid, so a card would be better resolved a few days after the payment.
- Liquidity: fine at our size. A$2,016 is about 8% of the thinnest session in the deep dive's 20 and about 1% of the median; a bad week can be sold.

## 5. The stated chances

The deep dive: bad 30%, middling 50%, good 20%. Mine: bad 35% (split 15% with a cut and 20% with the 5.0c paid from debt), middling 50%, good 15%.

Why more bad: the first half of FY27 likely shows rent-free not yet falling much (new WS1 and WS2 leases commencing); WS1 and WS2 are likely written down at December 2026; interest steps up in January 2027 and probably again in January 2028; rates are still rising (cash rate 3.60% in January to 4.60% in October, six-month bills 5.17%); 197 and 5 Mill re-lease in FY28 at 47% to 50% incentives. Why not more: fit-out spending has already fallen by two-thirds, the core towers are full, Perth's economy is the strongest of the states, no new CBD office supply is due until 2030 and vacancy is forecast to fall [M1, G5].

Why less good: it needs cash above 5c and either a re-rating to the top of the peer range in a rising-rate market that has just marked the sector down 15% to 28%, or a capital event. The Rockefeller notices state no intention and the buying stopped in September; the buy-back is idle. I'd put a bid at 5% to 8% within the window rather than 8% to 10%.

| Outcome | What happens | Chance | Price incl. distributions | Against A$0.64 |
| --- | --- | --- | --- | --- |
| Bad | Cash near 2.5c to 3c, WS1 and WS2 written down, swap cancelled, LVR into the 40s; the board cuts to 3.5c a year from the February 2028 payment | 15% | A$0.545 (A$0.46 plus 8.5c) | -14.8% |
| Poor | As above, but the board pays 5.0c, about half from debt | 20% | A$0.59 (A$0.49 plus 10c) | -7.8% |
| Middling | Rent-free about A$10m and fit-outs about A$4m by FY28; cash about 4.4c after the interest step-up; 5.0c held, mostly covered; no re-rating | 50% | A$0.75 (A$0.65 plus 10c) | +17.2% |
| Good | Cash above 5c and a re-rating, or a capital event | 15% | A$0.94 (A$0.84 plus 10c) | +46.9% |

- Expected value A$0.716: +11.8% before costs, +8.8% after the 3.0% round trip (+9.6% with the plan's cover), against the 12.9% minimum. It fails by about 4 points.
- Expected price before distributions: about A$0.62, 3% below today. All of the expected return is about 9.8c of distributions.
- Value pick test: middling +17.2% passes; the cut row (-14.8%) fails the 10% limit, and so do the two bad rows merged (A$0.571, -10.8%).
- Sensitivities (python3 -I): my prices on the deep dive's chances (bad split 15/15): +11.6% after costs, fails. The deep dive's prices on my chances: +12.8%, fails by 0.1. My numbers with no cut row at all (35% at A$0.59): +9.9%, fails. Each of the two corrections, prices or chances, is enough on its own to take it below the bar.
- Prices at which it would clear on my numbers: the minimum gain at A$0.617 or less; the cut row inside 10% at A$0.606 or less; the middling 15% at A$0.652 or less. So about A$0.605, before the 30 December ex-date. After it, with three payments left, about A$0.58.

Is counting distributions in the bad case right under the value pick test? In principle yes, as done no:
- Yes in principle: the card's outcome prices are the only input to the expected gain (src/risk.py: the sum of chance times price, over the price, less one), and the ledger credits distributions in cash to holders on the ex-date (rulebook section 7). An outcome price that left out four distributions would understate every outcome on a 24-month card, so the bad case should be measured the same way.
- No as done: the bad case pays all four 2.5c payments in full, which is the payout least likely in the bad state, the state in which the board's own note says distributions are a lever. And section 5a's value pick is "a pick whose business is clearly cheap on its own figures". Before distributions, the deep dive's bad case is A$0.50, -21.9%; two-thirds of the 10c it adds back is borrowed. Counting only the part of each payment that the bad case's own cash covers (about 4.3c in FY27 with the one-off Autoleague fees, 2.4c to 3.0c in FY28), the deep dive's bad case is about A$0.57, -11%: outside the limit. Counting borrowed payouts as value lets a high-payout, under-covered stock pass a downside test its business wouldn't.

## 6. Special situations (the deep dive's players section)
The good case leans partly on a capital event. The Rockefeller group (10.11%, average about A$0.615) could go to just under 20% on market (about A$34m) or requisition a meeting, but its notices state no intention and it voted for the new chair (12,500 votes against Warburton in all) [G6, G14]. A whole-of-group bid is simpler at GDI than at an externally managed REIT, as the deep dive says, but I'd put it at 5% to 8% within the window. I didn't re-open the comparable cases, which sit in another research file. This is a value pick, not a special situation, so the "nothing happens" test of heading 6 doesn't apply, except that "nothing happens" here is the middling case, and in it the price doesn't move.

## The three points most likely to make the pick wrong
1. The hedges run out. The A$100m cap steps from 3.75% to 4.50% in January 2027 and ends in December 2027; the bank is likely to cancel the A$175m swap on 1 January 2028 if rates stay up. On flat rates FY28 interest is about A$23.0m and the run-rate about A$24.3m, against the deep dive's A$21.0m: cash 0.4c to 0.6c a security lower in exactly the years the case needs it higher.
2. The 5.0c is cut for FY28. It has been paid from asset sales and debt for three years; in the bad case half of each payment is borrowed while values fall and the refinancing approaches, and a new chair has a buy-back competing for the same money. With a cut, the bad case is about -15%, outside the value pick limit.
3. The price was held up and the re-rating doesn't come. One holder took 34.5% of the volume while peers fell 15% to 28%; at A$0.64 the market already pays Growthpoint's yield on GDI's recovered FY28 cash. If the WS1 and WS2 values give way at December 2026, the middling case is a flat price plus distributions, not a re-rating.

## What I couldn't verify
- Three-year swap rates (the market rate that decides the 1 January 2028 call): no data in the repo, so I used the RBA's three- and six-month bills as the guide.
- Rent-free by building or a schedule of rent-free still to run: GDI doesn't publish one, so the FY27 to FY28 rent-free path is judgement on both sides.
- The size of the FY28 expiries in dollars (read from percentage bar charts and FFO, not from a rent roll).
- Centuria Office's A$25.6m rent-free line (in its financial report, not opened), Dexus's cash yield and the peers' NTAs (from another research file, not opened).
- Whether the Rockefeller group has bought below the 1% notice threshold since 14 September.
- Mill Green Stage 1A's cost (not disclosed; no capital commitments at 30 June 2026).
- Knight Frank's Q1 2026 report wasn't re-opened; the Q2 report says yields held flat for 21 months before Q2, consistent with the deep dive's 7.58%.
- Broker coverage and the Corporations Act thresholds (not checked).

## Sources
GDI (ASX announcements; ids in brackets):
- [G1] Appendix 4E and Annual Financial Report FY26, 24 Aug 2026 (03128815): highlights, FFO reconciliation, directors' report, cash flow statement, notes 9, 13, 14, 24, 28 and 36, audit report: https://announcements.asx.com.au/asxpdf/20260824/pdf/0733mjp739pqjf.pdf
- [G2] FY26 Annual Results Presentation, 24 Aug 2026 (03128823): pages 4, 5, 19 to 22 and 27: https://announcements.asx.com.au/asxpdf/20260824/pdf/0733n32xfklc6x.pdf
- [G3] FY26 Annual Results Announcement, 24 Aug 2026 (03128841): https://announcements.asx.com.au/asxpdf/20260824/pdf/0733pbwbnzst2q.pdf
- [G5] Chairman's and Managing Director & CEO's AGM addresses, 5 Nov 2026 (03162306): https://announcements.asx.com.au/asxpdf/20261105/pdf/0767zs9k748gsk.pdf
- [G6] Results of Meeting, 5 Nov 2026 (03162483): Warburton elected with 12,500 votes against; remuneration report 93.77% for: https://announcements.asx.com.au/asxpdf/20261105/pdf/0768fg5kgxkzrj.pdf
- [G7] Appendix 4D and Half Yearly Financial Report, 23 Feb 2026 (03063185): cash flow statement and investment property note: https://announcements.asx.com.au/asxpdf/20260223/pdf/06wlq3gnfftg4p.pdf
- [G9] Appendix 4E and Annual Financial Report FY25 (02984594), as cited in the deep dive for FY24 amortisation (not re-opened): https://announcements.asx.com.au/asxpdf/20250825/pdf/06n8ky446wnxzf.pdf
- [G13] On-market buyback, 24 Aug 2026 (03128846): https://announcements.asx.com.au/asxpdf/20260824/pdf/0733pphryhhs80.pdf ; Update, 15 Oct 2026 (03152683): https://announcements.asx.com.au/asxpdf/20261015/pdf/075byb07l89q4f.pdf
- [G14] Rockefeller change in substantial holding, 14 Sep 2026 (03138906): https://announcements.asx.com.au/asxpdf/20260914/pdf/0741kt1lyf1k7b.pdf
- [G17] Change of Director's Interest Notices, S Burns: 3 Jun 2026 (03100771) https://announcements.asx.com.au/asxpdf/20260603/pdf/0708rxd4vt1jf5.pdf ; 8 Sep 2026 (03136970) https://announcements.asx.com.au/asxpdf/20260908/pdf/073vcgqcvxdjp3.pdf ; 6 Nov 2026 (03163117) https://announcements.asx.com.au/asxpdf/20261106/pdf/076b65lfh599x9.pdf
- [G18] Extension of Syndicated Facility, 23 Jun 2026 (03106925): https://announcements.asx.com.au/asxpdf/20260623/pdf/070xp9y38zpl83.pdf
- [G20] Dividend/Distribution, 11 Dec 2025 (03039938): https://announcements.asx.com.au/asxpdf/20251211/pdf/06t6rhbr7jty43.pdf ; Update, 24 Aug 2026 (03128792): https://announcements.asx.com.au/asxpdf/20260824/pdf/0733kxxjjcw1t2.pdf
- [G22] GDI announcement list, 2026: https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=GDI&timeframe=Y&year=2026
- [G23] Salt Funds Management and Pathfinder, change in substantial holding, 4 Mar 2026 (03068297): https://announcements.asx.com.au/asxpdf/20260304/pdf/06x1r3k5mpfgmf.pdf
- [G24] Final Director's Interest Notice, G Woodgate, 2 Nov 2026 (03161070): https://announcements.asx.com.au/asxpdf/20261102/pdf/07649g641yszj0.pdf

Peers:
- [P1] Abacus Group, FY26 Results Presentation, 25 Aug 2026 (03129655): https://announcements.asx.com.au/asxpdf/20260825/pdf/0735swcx925d02.pdf
- [P2] Growthpoint Properties Australia, FY26 Results Presentation, 17 Aug 2026 (03125641): https://announcements.asx.com.au/asxpdf/20260817/pdf/072td79bz2dp6g.pdf
- [P3] Centuria Office REIT, FY26 Results Presentation (03121615): https://announcements.asx.com.au/asxpdf/20260804/pdf/072dbl6y6dsrkm.pdf

Market (secondary, named):
- [M1] Knight Frank, Perth CBD Office State of the Market, Q2 2026: https://content.knightfrank.com/research/2984/documents/en/perth-office-state-of-the-market-report-q2-2026-12929.pdf
- [M3] RBA statistical table F1.1, monthly cash rate and bank bill rates to October 2026: data/rates/rba_f1_1.csv
- [M4] Knight Frank, Australian Office Indicators, Q2 2026: https://content.knightfrank.com/research/2910/documents/en/australian-office-indicators-q2-2026-12987.pdf

Data and code:
- [D1] Norgate prices and total-return closes, data/norgate/universe/prices_2025.csv.gz and prices_2026.csv.gz (GDI, COF, ABG, GOZ, DXS, CMW), to 30 Oct 2026
- [D2] ASX company data, data/research_data/asx_company.json (fetched 7 Nov 2026 UTC)
- src/decide.py (research minimum gain, entry costs) and src/risk.py (expected return, Kelly sizing)

All arithmetic was run in python3 -I from scratch scripts (not committed).

## Verdict

Don't buy at A$0.64.

1. It doesn't meet the first condition of a value pick: the business isn't "clearly cheap on its own figures". On FFO, cash, distribution yield and price to NTA it is priced like its peers, the deep dive's own expected price before distributions is only +2.8% (mine is -3%), and the NTA that makes it look cheap rests on the tightest cap rates in the weakest-yielding capital city.
2. On honest outcomes it fails both tests that changed today. With a distribution-cut row the bad case is about -15% (limit -10%), and the expected gain after costs is about +8.8% against the 12.9% minimum. It clears on the deep dive's numbers only because the bad case pays every distribution in full and the FY28 interest bill assumes a swap the bank will probably cancel.
3. The return is a distribution that cash hasn't covered in any of the last three years, at a time when the hedges are ending, Perth yields are rising, and the one large buyer who held the price up has gone quiet.

What would change this: either (a) the price at or below about A$0.605 before the 30 December 2026 ex-date (about A$0.58 after it), with the card's bad case written with a cut row; or (b) the 1H FY27 result (about 16 February 2027) showing rent-free given (GDI Property Trust) of A$6.0m or less for the half, WS1 and WS2 written down by no more than 3% at 31 December 2026, 5.0c reaffirmed, and a stated plan for interest rate cover from January 2028. Either would justify a fresh deep dive and review at the price then; neither is a reason to place a card now.
