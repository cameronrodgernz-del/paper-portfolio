# Centuria Office REIT (ASX:COF): special situation deep dive

Written 2026-11-02 by the research desk. Price at writing: A$0.875 (close on 30 October 2026, Norgate, data/norgate/universe/prices_2026.csv.gz; the ASX company data shows the same last price [S13]). Market value: A$522.7m (597,336,931 units, FY26 financial report [S1]).
Status: finished. This is a simulation and not financial advice.
Fact sheet: research/facts/COF.md, grade A. Earlier deep dive: research/picks/COF.md (no card; the business on its own is priced about right). The question here: will someone act to close the gap between the price and NTA (A$1.66) before the debt problem arrives, and what are the units worth if nobody does?

> The desk's view in one line: if nothing happens the units are worth about A$0.83 by 30 April 2027, which with the two distributions in the window (4.5c) is exactly today's price. The Lederers are the only party with a reason and a record of acting: in 2025 the same family company, LDR Assets, bid for another externally managed office REIT at a 5% premium and then replaced its manager, and the holders who stayed are down about 41%. Centuria can vote its 18.9% against any change of manager and blocks a full takeover. Weighting a 14% chance of a partial move (about A$0.92) and a 4% chance of a full proposal (about A$1.09 traded) gives an expected gain of about +0.6% to +1.1% after costs, against a 9% bar. Wait for a named event: a Lederer filing above 17.9%, a bid, or a meeting requisition.

Order of work: the price was in the brief, so it was in view from the start. The "nothing happens" value is built from COF's NTA, its cash earnings and what the market pays listed office peers for each; the prices in the partial and full outcomes come from what parties have actually paid in comparable cases. COF's own price is used only in "Why the market is wrong" and at the end of "Outcomes and chances".

Corrections to the earlier deep dive (research/picks/COF.md), for the red team:
1. Removing the responsible entity of a listed scheme needs an ordinary resolution (more than half of the votes cast), not an extraordinary one; the extraordinary resolution applies only to unlisted schemes (s601FM) [S21]. And Centuria can vote: s253E bars a responsible entity and its associates from voting where they have an interest beyond their units, but makes an exception for resolutions to remove and replace the responsible entity of a listed scheme [S22]. The Lederers' ECF meeting notice applied both rules [S33].
2. The Lederer company is LDR Assets Pty Ltd, not "LOR". The 30 June 2026 notice is a scanned page whose text layer reads "LOR" in ten places and "LDR" once; the annual report's substantial holder table says LDR Assets [S3, S6].
3. The March 2026 notice records the previous holding as 90,074,100 units; the September 2024 notice had misstated it as 88,846,543 [S8, S9].

## The company in plain words
COF owns 18 office buildings worth A$1,842.0m at 30 June 2026 (plus a A$32.3m ground lease) in Melbourne, the Sydney fringe and Wollongong, the Brisbane fringe, Perth, Canberra and Adelaide [S2]. It has no staff. Centuria Property Funds Limited (CPFL), a subsidiary of Centuria Capital Group (ASX:CNI), is the responsible entity, paid 0.55% of gross assets a year (A$10.9m in FY26); Centuria companies took A$20.2m in all from the trust in FY26 for management, property and facility management, leasing, custody, projects and administration [S1].

NTA was A$990.7m, A$1.659 a unit, at 30 June 2026. Debt was A$832.5m drawn on A$1,012.5m of facilities maturing from 31 March 2029 to 31 March 2031; gearing 43.7%, loan to value 44.8% against a 60% covenant, interest cover 2.0 times against 1.75 [S1, S2]. FY27 guidance, reaffirmed on 15 October 2026, is FFO of 11.3c and distributions of 9.0c [S5]. After rent-free periods, fit-out incentives and upkeep the trust keeps about 4.1c a unit a year (the earlier deep dive's cash AFFO), so most of the distribution is paid from debt and sales [S14].

Register at 24 July 2026 [S3]: Centuria Capital Group 112,721,666 units (18.9%) and LDR Assets 101,001,333 (16.9%), together 35.8%. No other holder files as substantial. The top 20 hold 61.6%; there are 8,721 holders. Year-end closes: A$2.34 (2021), A$1.53 (2022), A$1.34 (2023), A$1.10 (2024), A$1.15 (2025), A$0.875 now (Norgate).

## Why big investors may be overlooking it
- COF left the S&P/ASX 300 on 23 March 2026, and Vanguard went from 7.34% to below 5% between February and March 2026 [S14].
- A$523m market value; median traded value of A$376,558 a day over the 20 sessions to 30 October (Norgate) [S14].
- The two big holders own 35.8% and rarely trade, so the free float is about A$336m.
- Office REITs are out of favour: listed peers trade at 0.53 to 0.64 times NTA [S14].
- The control angle is easy to miss because the decisive precedent sits in a different fund: the Lederers' 2025 campaign at Elanor Commercial Property Fund (now LDR Capital Property Fund, ASX:LED), which no COF filing mentions.

## What the filings show

### The debt path that sets the clock
Worked in python3 -I (scratch script cof_ss.py), scaling the reported 2.0 times cover by the change in the all-in cost of debt (margins and fees about 1.23% after the March 2026 refinancing; hedges at about 3.7%; three-month bank bills 4.82% in FY27 and 4.92% after) [S1, S2, S14]:

| Year | Share of debt hedged | All-in cost | Cover, debt flat | Cover, debt rising A$39m a year |
| --- | --- | --- | --- | --- |
| FY26 (reported) | 79% | 5.2% | 2.0 times | |
| FY27 | 69% | 5.28% | 1.97 | |
| FY28 | 62% | 5.39% | 1.93 | |
| FY29, no new hedges | 0% | 6.15% | 1.69 | 1.51 (flat earnings) to 1.65 (earnings up 3% a year) |

The swaps (A$555m at 3.7%, average life 1.9 years at June 2026) run out around May 2028 on average; the first facility (A$310m) falls due on 31 March 2029 [S1, S2]. Distributions of 9.0c against about 4.1c of cash mean debt rises by about A$39m a year with no sales [S14]. So the covenant doesn't bind inside this note's window, but by the FY28 guidance in August 2027 the trust has to show how it gets through FY29: sell buildings, cut the distribution towards cash, or both. That is the date a would-be controller wants to beat, because the cut lowers the price and the sales shrink the asset base. Loan to value isn't the pressure: values could fall about 25% before it reached 60% [S14].

### Fees and what the manager stands to lose
Base fee A$10.9m; property management A$3.7m; facility management A$2.1m; leasing A$2.1m; custody A$1.0m; projects A$1.0m; administration A$0.55m; less A$1.3m of rent paid to the trust by Centuria-related tenants: A$20.2m net in FY26 [S1]. Centuria also receives about A$10.1m a year of distributions on its 112.7m units. The constitution allows a base fee of 0.60% [S1]. The filings don't say whether the constitution or any management agreement pays Centuria a fee if it is removed; Elanor's agreement with ECF paid two years of management fees [S31].

## The players and what the rules allow

### LDR Assets (the Lederer family): 16.9%
Who: LDR Assets Pty Ltd (ACN 689 671 396) as trustee for the LDR Assets Trust; Paul and Eva Lederer each have more than 20% of its voting power [S6]. Units are held through HSBC Custody Nominees [S6].

Stake history from the notices (the 2021 notices are scanned faxes read by OCR, so their figures are approximate) [S6, S8, S9, S10]:

| Date | Event | Units | Holding | Price |
| --- | --- | --- | --- | --- |
| by May 2021 | PEJR Investments substantial | about 36.5m | about 7.1% | not legible |
| Sep 2021 | on market and off market buying | about 63.7m | 11.25% | not legible |
| Dec 2023 | notice | 79,160,874 | 13.25% | |
| 30 Aug 2024 | one purchase | +10,913,226 | 15.08% | A$13,194,762, A$1.209 a unit |
| 13 Feb to 20 Mar 2026 | 19 on-market purchases | +8,209,587 | 16.45% | A$8,113,385, A$0.988 average |
| 21 Mar to 30 Jun 2026 | buying below the 1% notice step | +2,717,646 | 16.91% | not disclosed; COF traded A$0.875 to A$0.995 in that period |
| 30 Jun 2026 | all units moved from PEJR Investments (65,788,315) and PELSF Nominees, the family super fund (35,213,018), to LDR Assets [S6, S7] | 101,001,333 | 16.91% | A$92.42m, A$0.915 a unit; an internal transfer |
| since 30 Jun 2026 | no notice, so any change is under 1% | | | |

In the two years from November 2024 the only open-market buying is the 10.9m units in February to June 2026, at about A$0.99. The noticed purchases since August 2024 come to 19.1m units for A$21.3m, about A$1.11 a unit. Most of the stake was bought in 2020 to 2023 when COF traded between A$1.34 and A$2.34 (year-end closes), so the family is well under water on COF and has kept buying anyway.

What they did at ECF, from primary documents:
- Elanor Commercial Property Fund was an externally managed office REIT run by Elanor Investors Group. The Lederers built a 27.5% stake in September to November 2024 (law firm client note, secondary) [S36] and signed a 2024 term sheet with Elanor that restrained them from supporting a change of responsible entity until September 2026 [S33].
- 4 August 2025: LDR Assets announced an off-market bid at A$0.70 cash, a 5.3% premium to the A$0.665 close and 10.0% over the one-month average, and 1.4% above NTA of A$0.69 [S31, S35]. The bidder's statement said that with more than 50% it would replace the responsible entity and appoint LDR Capital as manager [S30]. Elanor's independent committee went to the Takeovers Panel over disclosure, and LDR Assets agreed to issue a replacement bidder's statement [S30].
- The bid opened 11 September and closed 13 October 2025 with the Lederers at 42.68%, under 15.2% of the fund bought in the bid [S33].
- 24 December 2025: Elanor agreed to hand over [S33, S37]. 30 December: LDR Assets, with 42.68%, called a meeting under s252D and s601FM(1A)(b) to remove Elanor's responsible entity and appoint Evolution Trustees, by ordinary resolution, with Elanor free to vote [S32]. Elanor's committee said it would pass; the fund paid Elanor A$8.5m of compensation, 2.1c a unit [S33]. The meeting was held on 30 January 2026 [S34]; Evolution became responsible entity and LDR Capital manager from 4 February 2026, and the fund was renamed LDR Capital Property Fund (LED) [S38].
- Since then: NTA A$0.69 to A$0.58; four buildings sold for A$105.4m to cut gearing from 42.6% to 29.3%; management fees cut by A$1.9m a year (37%) and waived for the first half of FY27; the distribution reset to cash, 1.5c for FY27 against 6.5c in FY26 [S38]. LED closed at A$0.33 on 30 October 2026 (Norgate).

So the Lederer method is: build a stake, bid at a small premium to the market (not to NTA) to get past 40%, then use an ordinary resolution to change the manager, then cut fees, sell weaker assets and pay out only cash earnings. Holders who sold into the bid got A$0.70; holders who stayed have A$0.33 plus 6.5c of distributions, about 41% below the undisturbed price.

What they can afford: LDR Capital manages about A$600m of office assets for the family and raised A$165.5m for a A$305m health fund in December 2025 [S33]; the family office was reported to hold A$1.2bn of property in August 2025 (secondary) [S35]. The ECF bid cost at most about A$43m (under 15.2% of 407m units at about A$0.69). On COF, a bid that took them from 16.9% to 40% would cost A$127m at A$0.92 and A$159m at A$1.15; buying every other unit would cost A$457m to A$571m, before refinancing A$832.5m of secured debt. The first is within what they have shown; the second isn't. Their private cash and borrowing aren't disclosed.

Realistic moves: buy up to 20% on market (18.5m units, A$16.2m at A$0.875) at any time; an ECF-style bid at a small premium; or, from 16.9%, call a meeting to replace CPFL (they need 5%) [S23]. LED's record since February 2026 makes that pitch harder to sell to other COF holders than it was a year ago, and LDR Capital is still in the middle of repositioning LED.

### Centuria Capital Group: 18.9%, the manager's parent
Holding (no change in two years; the same 112,721,666 units appear in the 2024, 2025 and 2026 annual reports) [S1, S3, S11]: Centuria Capital No. 2 Office Fund 85,433,773; Over 50s Guardian Benefit Funds Trust 14,861,980; Centuria Growth Bond Fund 5,808,906; Centuria Capital No. 2 Fund 3,396,219; CPFL itself 2,263,375; Centuria Balanced Bond Fund 957,413. Of these, CNI's own balance sheet holds 91,093,367 units (15.25%), carried at A$102.5m (A$1.125) at June 2025 and A$81.1m (A$0.89) at June 2026, a A$23.0m fair value loss in FY26; the benefit funds hold the rest for policyholders [S15]. What CNI paid isn't disclosed in the filings I read. At A$0.875 its own units are worth A$79.7m.

Its strain [S15, S16, S17, S18, S19]:
- CNI closed at A$1.155 on 30 October 2026, down 43% from A$2.02 at the end of 2025 and 42% below the A$2.00 at which it raised A$300m in June 2026 (150m new securities, about 17.6% more). NAV was A$1.76 at June 2026.
- The raising was mainly for ResetData, the AI data centre business it owns half of (A$10.9m operating loss in FY26), and the proceeds back parent guarantees for project finance. ResetData is COF's fifth-largest tenant.
- Its Centuria Bass credit funds lent to Bathla Group, which went into voluntary administration in August 2026; CNI itself has only a A$4.5m loan to a Bathla vehicle.
- Cash and undrawn debt A$445m, balance sheet gearing 5.1%, FY27 guidance of A$130m operating profit. John McBain hands over to Jason Huljich as sole chief executive at the AGM on 27 November 2026.

What it can do: it can't creep (18.87% is under the 19% it would need to have held for six months) [S26], and can buy only 6.7m units (A$5.9m) before reaching 20%. Buying out the other 81% (about A$425m at today's price) would take most of its liquidity, which is committed to ResetData. Its realistic moves are to defend (vote its 18.9% against any change of manager; refuse a bid, which on its own stops compulsory acquisition) or to sell: a sale of the management rights with an internalisation, as Abacus did at Storage King, or a sale of its units into a bid. It can't simply sell its block to the Lederers: that would take them to 35.8%, which needs a takeover bid or a vote [S26]. When Propertylink approached Centuria Industrial REIT in September 2018, Centuria requisitioned a meeting to replace Propertylink's board, and Propertylink dropped its proposal for CIP [S20]. Nothing CNI has filed in 2026 mentions COF's strategy or its COF units.

### Other holders over 5%
None. Vanguard ceased on 26 March 2026 [S14]; Mondrian ceased in October 2023 [S13]. Citicorp Nominees (7.0%) and JP Morgan Nominees (2.6%) are custodians, not owners [S3]. The rest of the register is spread: the 21st to the 8,721st holder own 38.4%.

### The board of the responsible entity
Matthew Hardy (chair, director since July 2013), Darren Collins (March 2015), Elizabeth McDonald (March 2022) and Peter Done (December 2007), all described as independent non-executive directors of CPFL [S1, S3, S4]. They hold 328,614 (Done), 75,000 (Collins) and 52,336 (Hardy) units; McDonald isn't listed as holding any [S1]. None bought or sold COF units in 2025 or 2026 [S14]. The board can sell buildings, run a buy-back, change the payout, recommend or oppose a bid, and is the only body that can put a trust scheme to holders. Its directors are appointed by Centuria, and nothing in its filings suggests a review of strategy or structure.

### What the rules allow
| Route | What it takes | What it means for COF |
| --- | --- | --- |
| Replace the responsible entity | Holders with 5% (or 100 holders) can make CPFL call a meeting, or holders with 5% can call it themselves [S23]; ECF's took 31 days from notice to meeting [S32]; an ordinary resolution of votes cast to remove and replace [S21]; CPFL and Centuria may vote [S22] | The Lederers can call it today. With Centuria's 18.9% against and their 16.9% for, they need about 52% to 55% of the other votes cast, depending on turnout (python). Without a bid first, that is an uphill vote. If holders remove CPFL and choose no replacement, the trust must be wound up [S21] |
| Internalise the manager | The board agrees to buy the responsible entity, or a new responsible entity takes over and pays out the old manager | Storage King paid Abacus A$19m for about A$7m of yearly savings (2.7 times), with no holder vote as it was on arm's length terms [S27]. At that multiple, COF's saving (about A$6.4m, the base fee less an assumed A$4.5m of own costs) is worth A$17.4m, 2.9c a unit; two years of Centuria's fees, the ECF formula, would be 3.6c (base fee) to 6.8c (all fees) |
| Trust scheme | The board proposes it; a special resolution under s601GC (75% of votes cast) and, for a transfer scheme, approval under item 7 of s611; votes in favour by the bidder, the responsible entity and their associates are disregarded [S25] | Needs Centuria's board to agree. Whether Centuria could vote against is a s253E question (its fees give it an interest beyond its units) and untested for COF |
| Takeover bid | Off-market or market bid for all or a proportion; compulsory acquisition needs 90% and 75% of the units bid for [S26] | Centuria's 18.9% alone blocks compulsory acquisition. A bidder can still reach control and then replace the manager by ordinary resolution, the ECF route |
| 20% rule and creep | No one may go from 20% or below to above 20% except by an exception; creep allows 3 points every six months only for a holder at 19% or more throughout the previous six months [S26] | Neither party qualifies today. If the Lederers bought to 19% this week (12.5m units, about A$10.9m), their first creep would be in May 2027, after this window. So the only ways past 20% before 30 April 2027 are a bid or a holder vote |
| Sell buildings or wind up | The board can sell buildings; selling the main undertaking needs a holder vote under ASX Listing Rule 11.2 (AOF held one; ASX told Garda it needn't) [S28, S39]; holders can direct a wind-up by extraordinary resolution (half of all units that can vote, s601NB) | Half of all the votes eligible holders could cast: about 242m units if Centuria is excluded as having an interest beyond its units (s253E), 299m if not. Either way the Lederers would need more than a third of every other unit on the register to vote yes, not just of those voting |
| Buy-back | Up to 10% in 12 months on market without a vote if the constitution allows [S24] | A 5% buy-back at A$0.875 (A$26.1m) adds 2.5% to NTA but adds debt and A$1.6m a year of interest when cover is the constraint, and lifts Centuria to 19.86% and the Lederers to 17.80% (python). DXC and DXI did exactly this in 2026 with no lasting effect on price (below) |

## Valuation
Worked in python3 -I. Units 597.337m; June 2026 NTA A$1.659.

### Worth if nothing happens
Two inputs from the earlier deep dive [S14]: (1) NTA at 31 December 2026, which the February result will report: A$1.49 if values fall 4.5%, A$1.60 if they fall 1%, A$1.66 if they rise 1%; at chances of 30%, 50% and 20% that is A$1.579. A further 1.2c comes off by 30 April as the March-quarter distribution (2.25c) is paid from about 1.0c of cash, so A$1.567. (2) What the market pays listed office peers for a dollar of NTA: 0.53 times (Abacus, GDI), 0.59 (Cromwell), 0.64 (Growthpoint, Dexus).

COF's cash cover is worse than any of those peers', so the bottom of the range applies: 0.53 times A$1.567 is A$0.830. Cross-checks: COF's FY27 cash AFFO of 4.07c at the most generous cash yield any peer gets (Abacus, 5.4%) is A$0.75; at Growthpoint's 6.8% it is A$0.60. The distribution yield at A$0.83 would be 10.8%. Nothing-happens value: A$0.83, about 0.50 times June NTA. With the two distributions in the window (Dec and Mar quarters, 4.5c), a holder in the nothing-happens case ends at exactly today's A$0.875.

The covenant path makes this a ceiling for the no-event case beyond April rather than a floor: once FY28 guidance shows the trust reducing its payout towards cash (likely August 2027, outside the window), the yield support goes. The stress case (December values down 4.5%, cover reported at 1.9 times or less) is A$0.76 [S14].

### Reconciling with the external review's A$1.03
The review averaged two numbers: income of A$0.874 (FFO of 11.3c less a 3.0c reserve for building and leasing costs, at a 9.5% yield) and stressed assets of A$1.196 (NTA after taking 15% off the buildings) [S29]. The gap to A$0.83 comes from three inputs:

| Input | Review | This note | Effect |
| --- | --- | --- | --- |
| Building and leasing cost reserve | 3.0c, "an analyst allowance" | 7.23c, FY26 actual (maintenance A$7.1m, fit-out incentives A$10.5m, rent-free A$25.6m) | At the review's own 9.5%, the income leg falls from A$0.874 to A$0.428 and the midpoint from A$1.035 to A$0.812 |
| What the asset leg is | 85% of book, as if it could be realised | What the market pays listed office peers for NTA, 0.53 times | Asset leg A$0.837 instead of A$1.196; midpoint with the review's income leg A$0.855 |
| Yield on income | 9.5% on FFO less reserve | Peers' cash yields, 5.4% to 7.8%, on cash AFFO | Cash AFFO at 5.4% is A$0.753; the review's 9.5% applied to cash would give A$0.43 |

With both of my inputs, the midpoint of the two legs is A$0.795; the NTA multiple alone gives A$0.83. Which I believe: the cost figure is the FY26 actual, and rent-free has risen three years running (A$17.8m, A$20.1m, A$25.6m), so 3c is too low even if incentives ease (a 5.5c reserve, about two-thirds of FY26, still gives only A$0.61 at 9.5%). And in a case defined as no corporate event, asset backing reaches holders only through the price the market puts on it, which for every listed office peer is 0.53 to 0.64 times NTA. The review itself noted that cash after all building spending was only 2.45c a unit and called its cash cross-check "materially weaker than FFO" [S29]. I use A$0.83.

### What a party could realistically pay
- Partial move, A$0.92. A move that puts control in play without a firm offer for every unit: a Lederer bid on the ECF template, a requisitioned meeting, a stake above 19% with stated intentions, or Centuria announcing a review or sale of its stake or the management rights. On the floor of A$0.83, the ECF bid premiums give A$0.874 (5.3% over the last close) to A$0.913 (10% over the one-month average); Garda's price rose 11.7% when it sold every building near book and kept the cash, which would be A$0.927; the Lederers' own open-market buying in 2026 averaged A$0.988. I use A$0.92.
- Full proposal, A$1.15 offered, A$1.09 traded. A priced proposal for every unit, or a whole-portfolio sale with the money returned. Marking every building to the agents' yields gives NTA of A$1.38 [S14]; less about 6c of selling, debt and wind-up costs that is A$1.32, and a buyer needs a margin and must also pay Centuria for the management rights (3c to 7c, above). A$1.15 is 0.69 times June NTA and 31% over today's price, inside the 27% to 42% that Storage King was offered over its undisturbed price. While conditional, Storage King traded 1% to 6% below the proposal, so I take 95% of the offer: A$1.09. I don't use NTA (A$1.66), the review's full-offer price: no listed office REIT trading near half of NTA has been taken out at NTA in this cycle, and ECF's bid was at NTA only because ECF already traded at 96% of it.

### Comparable cases
Prices are Norgate closes; NTA and terms from the filings.

| Case | Who acted | What happened | Time taken | Holders got, against NTA | Against the price before |
| --- | --- | --- | --- | --- | --- |
| Australian Unity Office Fund, 2019 | Charter Hall and Abacus bought 19.9% at A$2.95, then proposed a trust scheme at A$3.04 [S40] | ASIC took the consortium's sale of its 19.9% to the Panel; the scheme got over 60% of votes but failed on 18 November 2019 [S40, S41] | 5.5 months to failure | Offer 1.09 times NTA of A$2.78; nothing received | +9.4% offered (A$2.78 on 3 June 2019); A$2.84 after the vote |
| Australian Unity Office Fund, 2022 to 2026 | The manager, after holders blocked a merger with its unlisted fund in January 2022 (secondary) [S42] | Sold every building; one buyer defaulted on A$61.5m and the last building went for A$40.0m against a A$45.0m valuation; delisted June 2026 [S43, S44, S45] | About 4.5 years from the merger vote; 2.5 years from December 2023 | From December 2023 (NTA A$1.72): 116.5c of capital returned, 68% of NTA | +12% on the A$1.04 close of 29 December 2023, plus income, over 2.5 years |
| Elanor Commercial Property Fund (now LED), 2024 to 2026 | The Lederers: 27.5% stake, bid, manager replaced [S30 to S38] | Above | 9 to 11 months from stake to bid; 6 months from bid to new manager | Bid at 1.01 times NTA of A$0.69 | +5.3% to those who sold; holders who stayed are about 41% down (A$0.33 plus 6.5c of distributions) |
| Abacus Storage King (now Storage King, SKG), 2025 to 2026 | Ki Corporation (39.6% directly) and Public Storage proposed A$1.47, then A$1.65; Abacus, the manager, held 19.77% [S27] | Withdrawn on 26 August 2025 after due diligence; then Storage King internalised its manager for A$19m (May to June 2026); Abacus sold its 19.6% in September 2026 at an average A$1.11, Ki paying A$1.20 and a block trade A$1.00 [S27] | 4.5 months to withdrawal; 5 months to internalise | Offers 0.84 and 0.95 times NTA of about A$1.74; now 0.62 times NTA of A$1.77 | +27% and +42% offered over A$1.16 (4 April 2025); A$1.105 now, 5% below |
| Garda Property Group, 2019 and 2026 | The internally managed board (2019: merged with its listed manager for A$61.6m of scrip, 21% of the group [S46]) | 21 October 2026: sold all nine buildings for A$350.8m, 1.4% below book, repaid all debt and kept A$176.6m to lend [S39] | One announcement; settlements November 2026 to March 2027 | Price now 0.73 times NTA of A$1.56 | +11.7% (A$1.025 to A$1.145) |
| Dexus Convenience Retail (DXC) and Dexus Industria (DXI), 2026 | The manager, Dexus: on-market buy-backs from March 2026, doubled from 2.5% to 5% in June; DXI also sold its business parks at 4.1% below valuation in 2025 [S47] | Buying continues | Ongoing | 0.71 and 0.70 times NTA | -1% and -4% since the buy-backs began (A$2.76 to A$2.73, A$2.51 to A$2.40) |
| Cromwell Property Group, 2020 | ARA Asset Management, a 24% holder: proportional bid at A$0.90, 1.3% over the market and 15.3% below NTA; won two board seats in September and a board spill in November 2020 (secondary) [S48] | ARA reached about 29.8% | About 5 months | Bid about 0.85 times NTA | +3.4% offered over A$0.87 (22 June 2020) |
| Propertylink, 2018 | Centuria held a stake and requisitioned a board spill; ESR, a 19.89% holder, then bid A$1.201 [S20] | ESR's agreed bid; Propertylink dropped its approach for Centuria Industrial REIT | About 2 months to an agreed bid | 1.15 times NTA of A$1.04 | +14.4% over A$1.05 |

What they show:
1. Holder campaigns in externally managed REITs win control at small premiums to the market, not at NTA (ECF +5%, Cromwell +3%). Full NTA has been offered only where the target already traded near NTA (AOF 2019, Propertylink 2018).
2. The manager's own stake decides most outcomes. Abacus (19.8%) sold out at 0.63 times NTA once it was paid for the management rights; Australian Unity's manager-backed deals failed twice, and the eventual sell-down returned 68% of NTA; Centuria defended CIP in 2018.
3. Moves that keep the money inside the trust (Garda's sale to lend, Dexus's buy-backs, Storage King's internalisation) leave the discount at 0.6 to 0.7 times NTA.
4. Getting from a stake to a change of manager took six months at ECF; a failed proposal takes four to six months. So a move started before February 2027 could resolve inside this window; a move started after it couldn't.

### Range
A$0.76 (stress) to A$0.83 (nothing happens) without a corporate event; A$0.92 for a partial move; A$1.09 to A$1.15 for a full proposal. Each depends on: December valuations and the market's NTA multiple; the premium a Lederer-style bidder offers; Centuria's willingness to sell.

## Why the market is wrong
For the most part it isn't. The nothing-happens value plus the two distributions equals today's price, so the market gives the control option almost no value; on the chances below it is worth about 2.3c a unit, 2.6% of the price. That is smaller than the round-trip cost and far below the bar.

The case for a gap is that the Lederers have the motive (a stake bought mostly at A$1.34 to A$2.34, now worth A$0.875), the vehicle (the COF units sit in LDR Assets since 30 June 2026, the company of the same name and trust that bid for ECF and called its meeting) and the method (ECF), and the deadline (hedges ending in 2028) favours acting in 2027. Against that: they can't win a manager vote without a bid first; a bid that gets them to 40% pays existing holders only a small premium; Centuria can vote and has defended before; and LED's results since February 2026 make the Lederers' pitch harder. A partial move by itself would likely add 5% to 12%, as at ECF and Garda, not close the gap to NTA.

## Outcomes and chances
| Outcome | What happens by 30 April 2027 | Chance | Price by resolve date |
| --- | --- | --- | --- |
| Bad: nothing happens | No bid, requisition, review or stake above 19%; December values and FY27 guidance as the earlier deep dive expects | 82% | A$0.83 |
| Middling: a partial move | A Lederer bid on the ECF template, a requisitioned meeting to replace CPFL, a Lederer stake above 19% with intentions stated, or Centuria announcing a review or sale of its stake or the management rights | 14% | A$0.92 |
| Good: a full proposal | A priced proposal for every unit that Centuria supports, or a whole-portfolio sale with the money returned | 4% | A$1.09 (A$1.15 offered, trading at 95% while conditional) |

Chances add to 100%. Bad is the nothing-happens value (0.53 times expected NTA of A$1.567). Middling is a price a party has actually paid in comparable moves (ECF premiums and Garda's reaction on the floor, below the Lederers' own A$0.988). Good is the agents'-yield NTA less costs and a buyer's margin. Why these chances: the Lederers have taken nine to eleven months from stake to bid before and now hold their COF units in their bid vehicle, but have filed nothing since 30 June and are busy at LED, and a partial move inside six months is roughly one chance in seven. A full proposal needs Centuria to agree to give up A$20m a year of fees and a bidder able to fund about A$500m of equity plus the debt; no approach is on record, and the one office deal of this kind in the cycle (ECF) was a partial bid, so I give it one in 25.

Expected price: 0.82 x 0.83 + 0.14 x 0.92 + 0.04 x 1.0925 = A$0.853; plus 4.5c of distributions (December quarter, ex about 30 December; March quarter, ex about 30 March), A$0.898. Against A$0.875 that is +2.6% before costs and +0.6% to +1.1% after round-trip costs of 1.5% to 2%, against a guide bar of about 9% for six months.

What it would take: clearing the bar after 2% costs needs an expected price of A$0.926 before distributions, which is a 75% chance of a move at this mix of partial and full, or a 37% chance of a full proposal on its own. Sensitivities: chances of 70%, 22% and 8% give +4.7% before costs; a full proposal at June NTA (the review's price, traded at 95%) gives +4.9%; the bad case at the A$0.76 stress gives -3.9%. The external review's weighted value of A$1.087 rests on A$1.03 for nothing happening, A$1.20 for a partial move (its own words: "not a cash entitlement") and A$1.66 for a full offer; none of those is a price anyone has paid in the cases above.

Verdict: wait for a named event. No card now.

## Dated events
- 3 November 2026: RBA decision (meeting 2 to 3 November); then 7 to 8 December 2026, 8 to 9 February 2027, 22 to 23 March 2027 [S49].
- 27 November 2026: Centuria Capital AGM; McBain hands over to Huljich as sole chief executive [S19].
- About 4 December 2026: COF December quarter distribution, 2.25c expected; ex about 30 December, paid about 29 January 2027 (last year: declared 5 December, ex 30 December 2025, paid 30 January 2026) [S12].
- About 4 February 2027: COF half-year result with 31 December valuations, NTA, interest cover and hedging (4 February 2026 last year) [S14]. A Lederer move after this date has little time to resolve inside the window.
- About 25 February 2027: Centuria Capital half-year result (25 February 2026 last year) [S13]; LED's half-year result about the same time (27 February 2026 last year) [S38].
- About 5 March 2027: COF March quarter distribution, 2.25c; ex about 30 March 2027, inside the window.
- Not dated: any LDR Assets notice (one is due within two business days of any 1% move, so the next would show 17.9% or more), bidder's statement or meeting requisition; any Centuria statement on its COF units or the management rights; the sale of 154 Melbourne Street (held for sale at A$88.25m) [S14].
- Creep windows: none in the window. Neither party is at 19%; a holder reaching 19% in November 2026 could first creep in May 2027.
- Outside the window but setting the clock: FY27 result and FY28 guidance about August 2027; swaps running out around May 2028; first facility maturity 31 March 2029 [S1].
- Resolve by: 30 April 2027.

## What would make this wrong
1. The Lederers bid soon and higher than at ECF. At 0.53 times NTA, a bidder can pay 30% over the market and still buy at 0.69 times NTA, which is better value than ECF was at 1.01 times. If an LDR Assets bid or requisition appears, the partial outcome has happened and the full outcome's chance rises; re-run the note at once. A binding bid would go to the deal sleeve.
2. Centuria sells. Under strain (units down 43%, A$445m of liquidity committed to ResetData), it could sell the management rights or its units, as Abacus did at Storage King. A Centuria statement on COF would change both chances.
3. The floor is too high. December values down more than 4.5%, ResetData (a Centuria-owned tenant with a third of 818 Bourke Street) failing to pay, or an early signal of a distribution cut would put the no-event value at A$0.76 or below.

Exit rule: no position is taken. Reopen with a fresh note on any of: an LDR Assets notice at 17.9% or more or stating an intention; a bid, proposal or meeting requisition from anyone; a Centuria announcement about its COF units, CPFL or the management agreements; the board announcing a portfolio sale, wind-up or buy-back; a new substantial holder.

## Checks
- Not on Cam's excluded list (config/judgement_excluded.csv has no entries yet). Not a gaming, wagering, racing, lottery or casino company.
- No placement-pattern reopening in the last 30 sessions: COF traded on all 30 sessions from 21 September to 30 October 2026, no halt, no raising in 2025 or 2026 [S13, S14].
- Liquidity: median traded value A$376,558 a day over the 20 sessions to 30 October 2026 (close times volume, Norgate) [S14]; section 3 allows two sessions at 10%, about A$75,300, far above the research cap of 2.5% that section 5a applies to special situations (NZ$2,500, about A$2,003 at NZ$1 = A$0.8013 on 30 October 2026, data/fx/fx_daily.csv) and above the A$1,500 minimum ASX order.
- COF isn't in data/prices/ASX or config/universe_trial.csv, so the nightly price fetch would need a line before any card.

What I couldn't verify:
- What Centuria paid for its COF units, and whether the COF constitution, the property management agreements or the debt facilities give Centuria a payment or the banks a review right if CPFL is removed.
- The Lederers' cash and borrowing; the A$1.2bn property figure is from a news report. The prices of their 2020 to 2023 purchases (the scanned notices are mostly illegible) and of the 2.7m units bought between April and June 2026.
- How the ECF stake was first built in 2024 (a law firm's client note, not a filing), and the vote counts at ECF's 30 January 2026 meeting (the results page was not in the file I could read).
- The 2022 AOF merger failure and the Cromwell 2020 timeline are from press reports; I couldn't open AOF's ASX list (delisted codes are not served) or find primary copies in the time.
- The text of s606, s611 and s601NB: AustLII refused the pages, so the creep and 20% rules are from the external review's rules page and my reading of the Act, and the wind-up threshold from the Act as I know it.
- ECF's and ASK's ASX announcement lists were refused by the ASX site ("Request Rejected"); I used direct PDF links and the Abacus Group list instead.

## Sources
COF announcements (ASX; list at https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=COF&timeframe=Y&year=2026):
- [S1] FY26 Financial Report, 4 Aug 2026 (03121611): https://announcements.asx.com.au/asxpdf/20260804/pdf/072db9l8jfs50k.pdf (notes C (debt, hedges), D2 related parties and fees, units)
- [S2] FY26 Results Presentation, 4 Aug 2026 (03121615): https://announcements.asx.com.au/asxpdf/20260804/pdf/072dbl6y6dsrkm.pdf
- [S3] 2026 Annual Report, 23 Sep 2026 (03142772): https://announcements.asx.com.au/asxpdf/20260923/pdf/074f1hvfwv2k4k.pdf (top 20 and substantial holders at 24 Jul 2026; directors)
- [S4] Appendix 4G and Corporate Governance Statement, 23 Sep 2026 (03142771): https://announcements.asx.com.au/asxpdf/20260923/pdf/074f1fq68fmx4c.pdf
- [S5] Q1 FY27 Operating Update, 15 Oct 2026 (03152660): https://announcements.asx.com.au/asxpdf/20261015/pdf/075bwpdp95v5kh.pdf
- [S6] Becoming a substantial holder, LDR Assets (Form 603), 30 Jun 2026 (03109533): https://announcements.asx.com.au/asxpdf/20260630/pdf/0715m30dx2hl6f.pdf
- [S7] Ceasing to be a substantial holder, PEJR and PELSF, 30 Jun 2026 (03109531): https://announcements.asx.com.au/asxpdf/20260630/pdf/0715lxrg5lqx95.pdf
- [S8] Change in substantial holding, PEJR and PELSF, 1 Apr 2026 (03078448): https://announcements.asx.com.au/asxpdf/20260401/pdf/06y1qkkcj16853.pdf
- [S9] Change in substantial holding, PEJR, 2 Sep 2024 (02848431): https://announcements.asx.com.au/asxpdf/20240902/pdf/067dp20w6x6zxm.pdf ; corrected 3 Sep 2024 (02849080): https://announcements.asx.com.au/asxpdf/20240903/pdf/067gclb9f5t6xx.pdf
- [S10] Change in substantial holding, PEJR, 6 May 2021 (02372213): https://announcements.asx.com.au/asxpdf/20210506/pdf/44w8hjn71w9nc0.pdf ; 1 Oct 2021 (02429688): https://announcements.asx.com.au/asxpdf/20211001/pdf/4514ygnjmsscq9.pdf (scanned faxes, read by OCR)
- [S11] 2025 Annual Report (03001931): https://announcements.asx.com.au/asxpdf/20250929/pdf/06ptwfj3c6w3lm.pdf ; 2024 Annual Report (02858994): https://announcements.asx.com.au/asxpdf/20240926/pdf/068c6kgxbst9ky.pdf
- [S12] June 2026 Distribution Declaration (03101513): https://announcements.asx.com.au/asxpdf/20260605/pdf/070by1rrvfbf6c.pdf ; December 2025 Distribution Declaration (03037476): https://announcements.asx.com.au/asxpdf/20251205/pdf/06szjbylnrvvvj.pdf
- [S13] ASX announcement lists for COF (2020 to 2026) and CNI (2024 to 2026), and data/research_data/asx_company.json (fetched 1 Nov 2026); Mondrian ceasing notice, 31 Oct 2023 (02733359): https://announcements.asx.com.au/asxpdf/20231031/pdf/05wqylg3rn8p0c.pdf
- [S14] The earlier deep dive, research/picks/COF.md, and its sources (NTA cases for December 2026, cash AFFO, peer NTA multiples and cash yields, agents' yields, debt and hedge detail, Vanguard notices, liquidity)

Centuria Capital Group (ASX:CNI):
- [S15] FY26 Financial Report, 27 Aug 2026 (03131130): https://announcements.asx.com.au/asxpdf/20260827/pdf/0739nrpxm14lxy.pdf (note B3, note C3(a) related party unit trusts)
- [S16] FY26 Results Announcement, 27 Aug 2026 (03131131): https://announcements.asx.com.au/asxpdf/20260827/pdf/0739ntxvmd04zy.pdf
- [S17] CNI launches $300M fully underwritten equity raising, 22 Jun 2026 (03106313): https://announcements.asx.com.au/asxpdf/20260622/pdf/070vxvn1q6ygtr.pdf
- [S18] Response to media commentary on Centuria Bass Credit Fund, 23 Jul 2026 (03117601): https://announcements.asx.com.au/asxpdf/20260723/pdf/071zq6kdsy51y3.pdf ; Response to Bathla Group Voluntary Administration, 25 Aug 2026 (03129933): https://announcements.asx.com.au/asxpdf/20260825/pdf/0736jd3fq3rbns.pdf ; Update regarding Centuria Bass credit funds and Bathla, 22 Sep 2026 (03142124): https://announcements.asx.com.au/asxpdf/20260922/pdf/074c8p43t19ks2.pdf
- [S19] 2026 Notice of Annual General Meeting, 27 Oct 2026 (03157548): https://announcements.asx.com.au/asxpdf/20261027/pdf/075tl15ldxcqbs.pdf ; CEO appointment and transition, 27 Aug 2026 (03131214): https://announcements.asx.com.au/asxpdf/20260827/pdf/0739vkc7lkbf84.pdf
- [S20] Propertylink Group, ESR bid implementation agreement, 12 Nov 2018 (records Centuria's 20 Sep 2018 requisition and the dropped CIP proposal): https://announcements.asx.com.au/asxpdf/20181112/pdf/440640dcy70mf1.pdf

Law and regulators:
- [S21] Corporations Act 2001 s601FM: http://classic.austlii.edu.au/au/legis/cth/consol_act/ca2001172/s601fm.html
- [S22] Corporations Act 2001 s253E: https://www5.austlii.edu.au/au/legis/cth/consol_act/ca2001172/s253e.html
- [S23] ASIC Corporations (Changing the Responsible Entity) Instrument 2023/681 (inserts s601FM(1A); repealed 1 Oct 2028): https://legislation.gov.au/F2023L01307/asmade/2023-09-27/text/original/epub/OEBPS/document_1/document_1.html
- [S24] ASIC Corporations (ASX-listed Schemes On-market Buy-backs) Instrument 2016/1159, explanatory statement: https://legislation.gov.au/F2016L01946/asmade/2016-12-14/es/original/pdf
- [S25] Takeovers Panel Guidance Note 15, Trust scheme mergers: https://takeovers.gov.au/node/3606
- [S26] The external review's rules page (Takeovers Panel summary of takeover provisions; ASIC RG 6, July 2026), scratchpad/ssr/review.txt near line 3222; ASIC, Close a registered scheme: https://www.asic.gov.au/for-finance-professionals/fund-operators/close-a-registered-scheme
- [S29] The external review, scratchpad/ssr/review.txt, lines 2843 to 2963 (sources C1 to C4) and its final comparison page

Comparable cases (primary unless marked):
- [S27] Abacus Group: ASK receives non-binding proposal, 7 Apr 2025 (02934907): https://announcements.asx.com.au/asxpdf/20250407/pdf/06hfsvx65s02k4.pdf ; withdrawal, 26 Aug 2025 (02985426): https://announcements.asx.com.au/asxpdf/20250826/pdf/06nbp0l40v9z06.pdf ; ABG to internalise management of ASK, 18 May 2026 (03094776): https://announcements.asx.com.au/asxpdf/20260518/pdf/06zpf74q4sflvj.pdf ; sale of interest in SKG, 18 Sep 2026 (03140940): https://announcements.asx.com.au/asxpdf/20260918/pdf/0747c0j5zf7fcv.pdf ; Storage King FY26 results, 14 Aug 2026 (03125137): https://announcements.asx.com.au/asxpdf/20260814/pdf/072r9rsttjgy5v.pdf ; Public Storage Form 8-K exhibit, Jul 2025 (revised A$1.65): https://www.sec.gov/Archives/edgar/data/1393311/000139331125000119/psa-073025xex99_1.htm
- [S28] Australian Unity Office Fund, EGM proposal to refresh approvals, 13 Apr 2026: https://www.australianunityofficefund.com.au/-/media/opf/documents/asx-announcements/egm-proposal-to-refresh-aof-unitholder-approvals.pdf
- [S30] Takeovers Panel, Elanor Commercial Property Fund, application received, 3 Sep 2025 (TP25/080): https://takeovers.gov.au/sites/takeovers.gov.au/files/2025-09/MR25-080.pdf
- [S31] ECF independent board committee presentation, 8 Sep 2025: https://announcements.asx.com.au/asxpdf/20250908/pdf/06nysk2v5g8p26.pdf
- [S32] LDR Assets, Notice of Meeting and Explanatory Memorandum for ECF, 30 Dec 2025: https://announcements.asx.com.au/asxpdf/20251230/pdf/06tv8ys20dpcb8.pdf
- [S33] ECF independent board committee explanatory statement, 16 Jan 2026: https://announcements.asx.com.au/asxpdf/20260116/pdf/06vb7yf4wx499k.pdf
- [S34] ECF results of meeting cover letter, 30 Jan 2026: https://announcements.asx.com.au/asxpdf/20260130/pdf/06vs8dkxnnnljb.pdf
- [S35] Investor Daily, Lederer Group launches takeover bid, 4 Aug 2025 (secondary): https://www.investordaily.com.au/lederer-group-launches-takeover-bid-for-commercial-property-fund ; FilingReader summary of LDR Assets' second supplementary bidder's statement, 9 Oct 2025 (secondary): https://filingreader.com/news-wire/sydney/2025-10-09/ldr-assets-clarifies-elanor-commercial-property-fund-takeover-bid-price
- [S36] McCullough Robertson client result, The Lederer Group, Feb 2026 (secondary): https://mccullough.com.au/client_results/the-lederer-group/
- [S37] Capital Brief, Elanor Investors eyes reset after Lederer Group disruption (secondary): https://www.capitalbrief.com/article/elanor-investors-eyes-reset-after-lederer-group-disruption-32994878-25a7-4a93-9d3d-7468de14706c/
- [S38] LDR Capital Property Fund (ASX:LED): announcement list 2026 (change of name and ticker 9 Feb 2026, 03057983): https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=LED&timeframe=Y&year=2026 ; FY26 Results Announcement, 27 Aug 2026 (03131198): https://announcements.asx.com.au/asxpdf/20260827/pdf/0739tg4hgz5ksw.pdf ; FY26 Appendix 4E (copy): https://bulletin.webull.com/qbd/announcement/20260827/499502685/51f5734d2a0f853a95877db19032ebec.pdf
- [S39] Garda Property Group, Sale of property portfolio, 21 Oct 2026 (03155569): https://announcements.asx.com.au/asxpdf/20261022/pdf/075ml7ngrvt7nw.pdf
- [S40] Takeovers Panel, Australian Unity Office Fund, application received, 14 Nov 2019 (MR19-065): https://takeovers.gov.au/sites/takeovers.gov.au/files/migrate/2019/MR19-065.pdf
- [S41] Charter Hall, CHAB acquisition of AOF not proceeding, 18 Nov 2019: https://www.charterhall.com.au/News/news-article/2019/11/18/chab-acquisition-of-aof-not-proceeding ; Property Markets, AOF NTA of A$2.78 at 30 Jun 2019 (secondary): https://propertymarkets.news/?p=1162
- [S42] Commercial Real Estate, Aust Unity office fund merger torpedoed by its investors, 18 Jan 2022 (secondary): https://www.commercialrealestate.com.au/news/aust-unity-office-fund-merger-torpedoed-by-its-investors-1113480/
- [S43] AOF HY24 results, 23 Feb 2024 (NTA A$1.72): https://announcements.asx.com.au/asxpdf/20240223/pdf/060qlmtykvd8f5.pdf
- [S44] AOF Chairman's address, unitholder meeting 17 Dec 2024 (copy): https://quoteapi.com/resources/4ec85c869fdae450/announcements/aof.asx/3A658342/AOF_Chairman_Address_Unitholder_Meeting.pdf?embed=1
- [S45] AOF results of unitholder meeting, 8 May 2026: https://www.australianunityofficefund.com.au/-/media/opf/documents/asx-announcements/results-of-unitholder-meeting.pdf
- [S46] Property Markets, Garda Diversified capital raising and internalisation, Sep 2019 (secondary): https://propertymarkets.news/?p=1524
- [S47] Dexus Convenience Retail REIT: buy-back update 9 Mar 2026 (03069683) https://announcements.asx.com.au/asxpdf/20260309/pdf/06x6966m966x5n.pdf ; valuation and buy-back update 19 Jun 2026 (03105693) https://announcements.asx.com.au/asxpdf/20260619/pdf/070sl97zqnrwm1.pdf ; FY26 results 10 Aug 2026 (03123376, NTA A$3.86) https://announcements.asx.com.au/asxpdf/20260810/pdf/072l4qwd8m4wx0.pdf . Dexus Industria REIT: buy-back 9 Mar 2026 (03069663) https://announcements.asx.com.au/asxpdf/20260309/pdf/06x67r154p347r.pdf ; valuation and buy-back update 19 Jun 2026 (03105685) https://announcements.asx.com.au/asxpdf/20260619/pdf/070skppwt1xmy1.pdf ; BTP divestment 6 Aug 2025 (02977538) https://announcements.asx.com.au/asxpdf/20250806/pdf/06mljv04rr3szg.pdf ; FY26 results 12 Aug 2026 (03124198, NTA A$3.425) https://announcements.asx.com.au/asxpdf/20260812/pdf/072nlhs7490gh5.pdf
- [S48] InDaily, Cromwell board rejects ARA takeover bid, 25 Jun 2020 (secondary): https://www.indailyqld.com.au/news/archive/2020/06/25/cromwell-board-rejects-ara-takeover-bid ; Commercial Real Estate, Cromwell board torpedoed in AGM, 19 Nov 2020 (secondary): https://www.commercialrealestate.com.au/news/cromwell-board-torpedoed-in-agm-bloodbath-1007198

Rates:
- [S49] Reserve Bank of Australia, board meeting schedules: https://www.rba.gov.au/schedules-events/board-meeting-schedules.html

Prices, volumes and fair-value arithmetic: Norgate Data in this repository (data/norgate/universe/prices_2019.csv.gz to prices_2026.csv.gz; COF.au, CNI.au, LED.au, SKG.au, GDF.au, DXC.au, DXI.au, CMW.au, AOF-202606.au) as of 30 October 2026. All arithmetic was run in python3 -I from a scratch script (cof_ss.py), not committed.
