# Mayfield Group Holdings (ASX:MYG): deep dive. Not a value pick: the two-year bad case (A$0.83) is 46% below the price. Wait for the 1H FY27 result (about 27 February 2027)

Written 2026-11-08 by the research desk. Price at writing: A$1.55 (last trade on Friday 6 November 2026; the close on 5 November was A$1.535; ASX company data in data/research_data/asx_company.json, fetched 7 November, and the same figure from the ASX company header read again on 8 November [M24]; Norgate's last close in the repo is A$1.605 on 30 October [M25]). Market value: A$181.9m (117,336,443 quoted shares, Appendix 2A of 12 October 2026 [M22]; 118.91m diluted for the managing director's partly paid shares and the options in the money, worked below).
Status: finished. Verdict: **Wait for a named event**: the 1H FY27 result, due about 27 February 2027 (last year a half-year profit update came a month earlier, on 27 January [M8]). It will show work in hand at 31 December 2026, the half's operating cash flow and whether FY27 guidance holds. No card, no red team. Not a value pick at A$1.55: over two years the bad case (orders stay at the September quarter's pace) is A$0.83 with dividends, 46% below the price, against the 10% the rule allows; the middling case (A$1.88) is 21% above it. As an ordinary pick to 31 March 2027 the expected gain is +3.2% before costs and 0.0% after them, against a minimum of +2.8%. Watch triggers, nothing else changing: A$1.50 as an ordinary pick, A$0.92 as a value pick. The exact conditions that reopen or close it are under "Dated events". This is a simulation and not financial advice.
Fact sheet: research/facts/MYG.md (8 November 2026), grade B. Its question: can Mayfield refill its order book (A$151m on 6 May, A$114.7m on 30 September) and turn profit into cash (FY26 operating cash flow A$5.0m against A$18.5m of underlying EBITDA) to deliver FY27 revenue of A$226m to A$232m? Its "our way" anchor: A$2.12 (FY27 EBITDA at the guidance midpoint, A$24.0m, at IPD Group's 9.97 times, plus A$8.71m of net cash); "against us" A$1.64 (FY26's A$18.46m at the same multiple).

Value pick (rulebook section 5a): tested both ways, as the brief asked. Not a value pick: the two-year bad case is 46% below the price. It would pass every value-pick test only at A$0.92 or below with nothing else changing. As an ordinary pick it fails the minimum gain at A$1.55 and would pass at A$1.50 or below.

Order of work. The brief and the fact sheet quoted the price, so it was in view from the start. The filings, the cash analysis, the order book arithmetic and both valuation methods were worked from Mayfield's and the peers' own documents first; Mayfield's price enters only where the market's multiple is backed out, in "Why the market is wrong", in "Outcomes and chances" and in the liquidity check. Arithmetic was run in `python3 -I` from scratch scripts (not committed); the key lines are shown.

> In short. Liquidity passes (median A$488,423 traded a day over the 20 sessions to 30 October [M25]). The fact sheet's A$2.12 does not survive the first test: it puts IPD Group's trailing multiple on Mayfield's forward year, and nothing in the window would make the market pay that for a company whose order book has shrunk for five months while its peers report records. Measured the way the market prices these businesses, enterprise value over EBITDA after lease payments (Mayfield owns its Adelaide sites; its peers mostly lease), the listed peers trade at 9.0 to 10.0 times this year's guided earnings (Southern Cross Electrical Engineering, GenusPlus) and 9.6 to 11.7 times last year's (Korvest, IPD Group). Mayfield at A$1.55 is 8.2 times its FY27 guidance midpoint on the same basis and 13.5 times FY27 cash earnings of about 11.45c a share. A discount of 10% to 20% is what the order book earns: work in hand fell from A$151m (6 May) to A$114.7m (30 September), and September-quarter orders were roughly A$30m to A$37m against about A$57m of revenue a quarter at guidance, while Southern Cross's order book rose 18% to a record A$810m, Korvest reported record work on hand and Genus A$2.2bn. The cash question is mostly timing with a structural step down underneath. FY26's weak second half (operating cash flow minus A$1.4m) came from building SMEC's debtors from nothing (it was bought as an asset deal and no receivables came across), A$1.3m paid into a solicitor's trust for the inherited Nicon case, the first year of tax after the losses ran out, and June billing; receivables are 77% not overdue, last year's contract assets were all billed, and there is no sign of a loss-making project. But with tax now about A$6m a year and acquired units that carry working capital the old business never did, cash conversion won't return to FY25's 79%. The 15 September director's notice was a purchase, not a sale: its acquired row, its holdings (30,812,608 to 31,562,608) and its consideration all say so, and only the "nature of change" line, copied word for word from the May sale notice, says otherwise; but the whole market traded only 339,723 shares that day, so the 750,000 shares cannot all have been bought on market on 15 September, and I don't count it as an on-market buy. On my valuation the middle case is about A$1.65 by 31 March 2027, the bad case A$1.17 and the good case A$2.06; a discounted cash flow on the middle path gives less, A$1.20 to A$1.49. The price is about where the business is worth, with the downside larger than the upside until the order book turns.

## The company in plain words
Mayfield designs and builds the electrical equipment that takes power from the grid or a generator to the machines and servers that use it: low and medium voltage switchboards, transportable switchrooms (prefabricated buildings that house switchgear), kiosk substations, power skids and protection and control panels. It builds them in Adelaide (Edinburgh, and the Old Port Road site at Royal Park bought in January 2026), Perth (Bibra Lake, and from 1 December 2026 a leased 20,000m² site at Hope Valley) and Kalgoorlie [M2 slide 19; M4 slide 15]. Customers are data centre builders (NEXTDC's M2 in Melbourne, the Mel03 data centre), renewable energy zones (Central West Orana), miners (Rio Tinto at Cape Lambert, Roy Hill), utilities and transport (the T2D road project in Adelaide) [M2 slide 12; M4 slide 10]. 91% of FY26 revenue was project work recognised as it progresses, measured by costs incurred against expected costs, which the auditor KPMG made a key audit matter [M1, auditor's report]. The group reports one segment. Its units: Mayfield Industries (the core switchroom and switchboard maker), BE Switchcraft (commercial switchboards, bought August 2025), SMEC Power & Technology (underground mining electrical gear, bought March 2026), the N-Series switchboard range bought from Nilsen (control from 31 October 2026, final handover now 30 November), ATI (communications and control systems) and Power Parameters (UPS, batteries and test instruments) [M1 notes 36 and 39; M4 slide 14]. It employed 535 people at 30 June 2026 [M2 slide 14].

Who runs it. Andrew Rowe, Managing Director, holds 1,565,895 partly paid shares (issued at A$0.455) and 45,000 ordinary shares bought on 23 October 2026 [M19]. Simon Higgins, Chair, holds 631,907 shares, which came to him off market from Mr Rowe's partly paid shares in December 2025 [M1 note 24]. Lindsay Phillips is executive chairman of Nightingale Partners, the largest holder; Alan Steele holds 5,000,000 through Alan Steele Consulting; Rodney Henderson, appointed October 2025, holds 100,000 [M1; M19]. One related party: the Chair's daughter is employed as a market analyst (A$57,755 in FY26) [M1 note 34].

Who owns it [M1, shareholder information; M17; M20; M21]. Nightingale Partners 30,812,608 at 31 July 2026 (26.27%), 31,562,608 after the 15 September 2026 purchase (26.90%); Citicorp Nominees 14.89%; HSBC Custody Nominees 12.48%; Alan Steele Consulting 4.26%; Warbont Nominees 3.91%; J P Morgan Nominees 3.75%; Marlougia 2.68%; UBS Nominees 2.42%. The top 20 hold 85.89%; 1,202 holders. Substantial holders from their own notices: Nightingale 26.90%, Ellerston Capital 7.12% (23 October 2026), UBS Group 5.09% (2 November 2026). (The annual report also lists Citicorp and HSBC as "substantial holders"; they are custodians holding for others.)

Five years. Revenue A$77.8m (FY23), A$85.7m (FY24), A$118.1m (FY25), A$169.0m (FY26) [M4 slide 3]; statutory profit after tax A$5.80m, A$5.10m, A$6.76m, A$8.04m [M24, the ASX's company data; M1]. Shares on issue rose from 91.5m (1 July 2024) to 117.3m, through the November 2025 placement at A$1.90 and acquisition scrip [M1 note 24]. The price went from about A$0.45 in November 2023 to a high of A$3.525 in January 2026, and is now A$1.55 [M25; M24].

## Why big investors may be overlooking it
It is not really overlooked; it is out of favour.
- Size and index: A$182m market value. It joined the All Ordinaries at the March 2026 rebalance [M23]; at this size it is outside the S&P/ASX 300 (I did not check the index list itself).
- Coverage: three brokers. FNArena (a secondary source) lists Bell Potter (Buy, target cut from A$3.20 to A$3.10 on 21 October 2026, FY27 EPS 11.4c, FY28 13.2c) and Canaccord Genuity (Buy, target A$3.70, 30 August 2026), and Moelis without detail [S1]. The November 2025 placement was run by Unified Capital Partners [M15].
- Register: concentrated (Nightingale 26.9%, top 20 86%), but with institutions on it (Ellerston, UBS Asset Management) [M1; M20; M21].
- Liquidity: enough for this book (A$488,423 a day median) [M25].
- Messy history: a 2020 reverse takeover of Stream Group, which left the Nicon litigation [M1 note 15].
- Out of favour: the price fell 47% from A$2.91 on 30 June 2026 to A$1.55, against falls of 9% for IPD Group, 18% for Korvest, 24% for GenusPlus and 27% for Southern Cross over the same weeks [M25; M24]. The whole group has lost a fifth of its value since June; Mayfield has lost twice that.

## What the filings show
### Earnings
| A$m | FY25 | 1H FY26 | 2H FY26 | FY26 | Source |
| --- | --- | --- | --- | --- | --- |
| Revenue | 118.1 | 79.5 | 89.4 | 169.0 | [M1][M6] |
| Underlying EBITDA (margin) | 12.0 (10.1%) | 8.0 (10.0%) | about 10.5 (11.7%) | 18.5 (10.9%) | [M1 note 8][M7] |
| Statutory profit after tax | 6.76 | 4.51 | 3.52 | 8.04 | [M1][M6] |
| Underlying profit after tax | 7.29 | not given | not given | 10.94 | [M1 note 8] |
| Operating cash flow | 9.51 | 6.44 | -1.42 | 5.03 | [M1][M6] |
| Income tax paid | nil | 0.23 | 2.06 | 2.29 | [M1][M6] |

The FY26 items left out of underlying profit (A$2.91m before tax): deal costs for SMEC and BE Switchcraft A$1.21m, a A$0.92m rise in the SMEC earn-out (share based) and A$0.79m on the Nicon case [M1 note 8]. Nicon costs also appeared in FY25 (A$0.53m). The company puts organic revenue growth at 17% (A$20m) and organic underlying profit growth at 22% [M2 slides 6 and 7]. BE Switchcraft added A$18.6m of revenue and A$1.39m of profit in 10 months (A$21.3m and A$1.67m for a full year); SMEC added A$11.9m and A$0.55m in three months (A$44.6m and A$2.11m for a full year) [M1 note 36]. SMEC was bought for an enterprise value of up to A$30m, "approximately 5x EBITDA" on a forecast of A$6.0m [M13]; its earn-out was settled for A$8.6m (A$6.3m cash and 1,066,561 shares at A$2.16) [M2 slide 8]. FY26 interest income was A$1.06m, earned on the placement cash, most of which has since been spent [M1].

FY27 guidance: revenue A$226m to A$232m (raised on 20 October from A$224m to A$229m), EBITDA margin 10% to 11%, so EBITDA of A$22.6m to A$25.5m [M4 slide 11; M3]. It includes full years of SMEC and BE Switchcraft and about eight months of N-Series (A$10m to A$15m) [M4 slide 14]. On the company's own FY26 pro forma of A$204m (BE Switchcraft and SMEC for a full year) [M2 slide 6], the midpoint leaves about A$12.5m, or 6%, of organic growth after N-Series: 229 - 204 - 12.5 = 12.5. The September quarter was "ahead of expectations" on revenue and gross margin, compared with the internal budget [M4 slide 11]. Record against its own numbers: the one numeric half-year guidance in two years, "approximately $4.9 million" of 1H FY26 profit (27 January 2026), came in at A$4.51m, 8% short [M8][M6].

### Cash: timing or structural?
Working capital at three dates (A$m) [M1][M6]:
| | 30 Jun 2025 | 31 Dec 2025 | 30 Jun 2026 |
| --- | --- | --- | --- |
| Trade receivables | 12.6 | 14.6 | 31.5 |
| Contract assets (work done, not yet billable) | 8.6 | 7.9 | 13.7 |
| Inventories | 4.4 | 4.4 | 8.5 |
| Trade payables | (13.4) | (9.2) | (19.9) |
| Contract liabilities (customer money received ahead of the work) | (12.2) | (12.7) | (15.5) |
| Net | 0.1 | 4.9 | 18.3 |

Part of the rise came with the acquisitions and never passed through operating cash flow: BE Switchcraft brought A$3.06m of net working capital (receivables A$4.31m, contract assets A$2.36m, inventory A$0.36m, less payables A$2.44m and contract liabilities A$1.53m), and SMEC A$5.27m, almost all inventory [M1 note 36]. SMEC was an asset purchase "on a cash-free, debt-free basis with normal working capital" [M13], but the purchase accounting shows no trade receivables came across, only A$0.21m of other receivables [M1 note 36]. So Mayfield had to build SMEC's debtors from nothing after 1 April: on A$11.9m of June-quarter revenue and one to two months' terms, that is roughly A$4m to A$8m of the second half's outflow, less whatever SMEC's own suppliers had not yet been paid. The cash flow reconciliation puts FY26's organic working capital build at A$9.8m: receivables up A$14.4m, contract assets up A$2.7m, inventories down A$1.3m, payables up A$4.1m, contract liabilities up A$1.8m [M1 note 40]. The company's own bridge names the same causes: A$2.3m of tax (FY25: nil), "a working capital injection into newly acquired SMEC", "project timing across a 43% larger revenue base", and A$1.3m paid into trust for Nicon, which settles a provision built up over earlier years [M2 slide 9].

The evidence for timing:
- Receivables are fresh: A$24.4m not overdue, A$6.2m one month overdue, A$0.8m two months, A$80,223 over six months; the credit loss allowance is A$97,572 [M1 note 10].
- All A$8.64m of contract assets at 30 June 2025 were billed during FY26 [M1 note 11].
- Warranty provision A$135,610; no onerous contract provision; A$15.7m of performance and defect bank guarantees with "no claims ... as of the signing date" [M1 notes 22 and 32].
- Second-half margins rose (about 11.7% against 10.0% in the first half), which is not what a project gone wrong looks like.
- At the AGM: "Working capital improving, with cash position strengthening into Q2" [M4 slide 11]. Unaudited and unquantified.

The evidence for something structural:
- Tax. FY25's 79% conversion was before any tax because past losses were being used up [M2 slide 9]. At the FY27 guidance midpoint, tax is about A$6m a year.
- The acquired units carry working capital. BE Switchcraft's net working capital at purchase was about 14% of its yearly revenue (3.06 / 21.3); SMEC's will be about a quarter of its revenue once its debtors are built (about A$5m of stock and A$6m of debtors on A$44.6m). Mayfield Industries ran on customer prepayments: the group's net working capital was nil at June 2025.
- Debtor days roughly doubled: receivables over second-half revenue with GST were about 32 days at June 2025 (12.6 / (66.1 x 1.1 / 182)) and about 58 days at June 2026 (31.5 / (89.4 x 1.1 / 181)).
- One customer has written that equipment it received "may not meet certain technical specifications" and reserved its right to seek remediation; Mayfield denies it, no proceedings have started and nothing is provided [M1 note 32]. The contract and the amount are not named.

My reading: FY26's 27% conversion was mostly timing and one-off items, and there is no sign of a project that went wrong. But the normal level after tax is now perhaps 55% to 65% of EBITDA before growth, not 79%, and growth costs working capital. At the guidance midpoint I estimate FY27 free cash flow of about A$9.4m (8c a share), against cash earnings of about A$13.6m before working capital (worked under "Valuation"). The 1H FY27 operating cash flow settles it: with SMEC's debtors now built and the company saying working capital is coming back, I want at least 70% of the half's underlying EBITDA.

### The order book
Work in hand, as announced (A$m) [M11][M12][M2 slide 11][M4 slide 9]:
| 1 Jul 2025 | Aug 2025 | Oct 2025 | 31 Dec 2025 | Mar 2026 | 6 May 2026 | 30 Jun 2026 | 30 Sep 2026 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 104 | 105 | 112 | 114 | 135 | 151 | 135 | 114.7 |

BE Switchcraft is included from August 2025 and SMEC from March 2026 [M12]. Orders in a period are revenue plus the change in work in hand, less any work in hand that came with an acquisition (not disclosed). So: July to December 2025, at most A$89.5m (79.5 + 10); January to June 2026, at most A$110m (89.4 + 21). Then it turned. From 6 May to 30 September work in hand fell A$36m while revenue was roughly A$80m to A$85m (about eight weeks of the June quarter plus the September quarter, which isn't disclosed), so orders were about A$45m to A$50m in almost five months, under 0.6 of revenue. In the September quarter alone, at A$52m to A$57m of revenue, orders were roughly A$30m to A$37m (less the A$3.9m of N-Series work in hand if it was counted). Mayfield announced four order or work-in-hand updates between January and May 2026 and none since 7 May [M24 announcement list].

The peers' order books went the other way: Southern Cross a record A$810m at 30 June, up 18% [P3]; Korvest "record levels of work on hand" [P2]; GenusPlus A$2.2bn [P4]. So this is Mayfield's own problem or its own timing, not the market's.

What supports a recovery: a tender pipeline of A$1.4bn for Mayfield Industries alone, of which A$244m is on projects already awarded to Mayfield's clients; 14 live data centre tenders worth A$239m, A$189m of them past the design stage; and "when client projects proceed, Mayfield wins around two in three decided bids" [M4 slide 9]. The pipeline is unweighted and "not a forecast of revenue" [M4].

FY27 itself is not the main risk. Work in hand at 30 September (A$114.7m) plus a September quarter of about A$57m covers about A$172m of the A$229m midpoint; the rest has to be booked and delivered within the year, and the short-cycle units (BE Switchcraft, SMEC and N-Series, about A$78m a year between them) do most of that. FY28 is the risk: if orders stay at the September quarter's pace, work in hand runs down to about A$55m by June 2027 (114.7 + 3 x 37 - 170) and FY28 revenue falls.

### Balance sheet and commitments
- Cash A$21.83m at 30 June 2026 and no borrowings (A$8.4m drawn in January for Old Port Road and repaid) [M1 notes 9 and 20]. Since then: SMEC earn-out cash A$6.3m (29 July), Nilsen A$4.0m (subject to adjustments) and the final dividend of 2.4c, about A$2.82m (paid 17 September) [M1 note 39; M10]. That leaves about A$8.7m before the September quarter's own cash flow: 21.83 - 6.3 - 4.0 - 0.024 x 117.32 = 8.72.
- Facilities: an A$8.4m bank loan facility (undrawn), A$23m of bank guarantees (A$15.7m used), A$3m equipment finance; secured over the group's property [M1 note 20].
- Leases A$6.87m at 30 June, plus Hope Valley from about 1 December 2026: A$1,055,000 a year for 10 years with a 5-year option, rising 3.5% a year [M1 note 33]; at a 6.5% discount rate that adds about A$9.0m of lease liability.
- Owned land and buildings A$25.6m at independent valuation (land A$15.19m, buildings A$10.41m) [M1 note 16]; Old Port Road cost A$8.4m in January 2026 [M2].
- Intangibles A$28.3m, 35% of equity of A$80.0m. Net tangible assets 48.84c a share on the company's basis [M1].
- Contract liabilities of A$15.5m are customers' money held for work not yet done. If orders shrink, that cash goes out with the work.
- Holders refreshed the extra 10% placement capacity at the AGM (95.45% for) [M5; fact sheet]. The AGM presentation says acquisitions are "to be funded by existing balance sheet" [M4 slide 16]; with about A$9m of cash and an A$8.4m facility, that is limited.

### Who is buying and selling
Director trades over two years (on-market unless stated) [M16][M17][M18][M19]:
| Date | Director | Trade | Shares | Price |
| --- | --- | --- | --- | --- |
| 24 Oct 2025 | Phillips (Nightingale associate) | Sale | 735,883 | A$1.76 |
| 27 Oct 2025 | Steele | Sale | 487,275 | A$1.76 |
| 27 Nov 2025 | Steele | Sale | 5,000,000 | A$2.32 |
| 17 Mar to 27 Oct 2026 | Henderson | Four buys | 4 x 25,000 | A$1.73 to A$2.69 |
| 27 May 2026 | Phillips (Nightingale) | Sale | 10,000,000 | A$2.84 |
| 15 Sep 2026 | Phillips (Nightingale) | Purchase, venue unclear (below) | 750,000 | A$1.907 |
| 23 Oct 2026 | Rowe | Buy | 45,000 | A$1.56 |

The 15 September notice, settled. The Appendix 3Y gives: holding before 30,812,608; "Number acquired 750,000"; "Number disposed" blank; consideration A$1,430,100; holding after 31,562,608; "Nature of change: On market sale" [M17]. Four of its five figures describe a purchase. The 30,812,608 matches the register at 31 July and the May notice [M1; M16]. The words "On market sale" are word for word the May notice's, where they were right [M16]. So it was a purchase of 750,000 shares at A$1.907. Whether it was on market is another matter: Norgate, which includes block trades (it shows the 10.08m traded on 27 May, the day of Nightingale's crossing), records only 339,723 shares traded on 15 September, and 1,114,560 across 10 to 15 September; the A$1.907 average sits below the 14 September low (A$1.92) and near the lows of 11 and 15 September (A$1.8825 and A$1.88) [M25]. Buying 750,000 on market at that average would have meant taking two thirds of everything traded over four days at close to the day's lows. It is more likely an off-market transfer or a crossing arranged over several days. The brief counts only on-market trades, so I record it as a purchase by the largest holder that I can't confirm was on market. It is consistent with Nightingale's May statement that it would not sell more for 12 months [M16], and it means the largest holder added about A$1.4m at A$1.91 after selling A$28.4m at A$2.84.

The institutions. Ellerston bought 1,574,226 shares between 21 and 26 October at A$1.44 to A$1.62 and is now at 7.12% [M20]. UBS's trading and asset management arms bought 1.27m shares on 21 October and became substantial again on 2 November at 5.09% [M21]. On 21 October, the day after the AGM (held at 1pm on 20 October [M5]) and with no announcement but the meeting results, 5.79m shares (A$9.1m, about 5% of the company) traded, with a low of A$1.345 and a close of A$1.575 [M25]. No holder has filed a notice of ceasing or falling that matches it, so the seller was someone below 5%, or several. That is a large, motivated seller the day after the September work in hand was published.

### Things a quick reader would miss
- The N-Series handover slipped from 31 October to 30 November 2026, and "significant excluded projects" stayed with Nilsen [M4 slide 14; M14].
- Hope Valley's rent (A$1.055m a year) and the staff to run it start from about 1 December, whether or not the orders arrive to fill it [M1 note 33; M4 slide 13].
- FY25's operating cash flow was before any tax; the company itself points this out [M2 slide 9].
- Four small disclosure slips in a year: the 15 September Appendix 3Y; the final dividend release putting a 2.4c dividend at "$2.314 million" (the interim's figure; the Appendix 4E says A$2,855,029) [M10; M1]; the January 2026 release calling FY25's total comprehensive income of A$7.47m "audited NPAT" (it was A$6.76m) [M8]; and custodians listed as substantial holders [M1]. None matters alone.

## Valuation
### Method 1: what listed peers trade on
The measure. These businesses are priced on enterprise value over EBITDA, but two things distort the plain ratio here. Under the lease accounting standard (AASB 16), rent is left out of EBITDA; and Mayfield owns its Adelaide sites while its peers mostly lease. So I compare enterprise value (excluding lease liabilities) with EBITDA after lease payments (principal and interest), "EBITDAaL", and separately test whether Mayfield's owned property deserves credit. As a second angle, the price over cash earnings against the peers' price-earnings ratios.

The peers (last trades on 6 November 2026 [M24]; balance sheets at 30 June 2026):
| | Business | Market value | Enterprise value | EBITDAaL basis | EV / EBITDAaL | P/E (underlying) | Operating cash flow / EBITDA, FY26 | Order book |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IPD Group (IPG) | Electrical equipment distributor and engineering, data centres | A$536.2m (104.11m at A$5.15) | A$552.6m (net debt A$16.4m) | FY26: 55.4 - 8.1 lease payments = 47.3 | 11.7 | 17.4 | 59% (84% before tax and interest) | not reported |
| Korvest (KOV) | Cable and pipe supports, galvanising, Adelaide | A$190.8m (11.93m at A$16.00) | A$192.4m (overdraft A$1.5m) | FY26: 22.0 - 1.9 = 20.1 | 9.6 | 15.4 | 27% | record |
| Southern Cross (SXE) | Electrical contractor with a switchboard factory, data centres | A$1,089.7m (308.70m at A$3.53) | A$836.4m trailing; A$932.2m after the Entire purchase | FY26: 77.0 - 5.3 = 71.7; FY27 guidance at least A$110m, about 103 after leases | 11.7 trailing; 9.0 on FY27 | 27.7 trailing | 87% | A$810m, record |
| GenusPlus (GNP) | Power line and substation contractor | A$1,696.1m (204.10m at A$8.31) | A$1,679m after the MPK purchase | FY27 guidance A$200m to A$205m, about 167 after leases | 10.0 on FY27 | not used | not used | A$2.2bn |

Sources and adjustments: IPD Group, underlying EBITDA A$55.4m, lease payments A$7.01m plus A$1.08m interest, underlying profit A$30.9m, net debt A$16.4m, operating cash flow A$32.95m [P1]; the Platinum Cables earn-out (up to A$7.5m) is left out. Korvest, operating profit A$18.29m plus depreciation A$2.44m and A$1.31m, lease payments A$1.14m plus A$0.77m interest, profit A$12.41m, operating cash flow A$5.99m [P2]. Southern Cross, underlying EBITDA A$77.0m, underlying profit A$39.4m, lease payments A$4.43m plus A$0.91m, cash A$261.5m plus the A$15m share purchase plan less the 7.5c final dividend, and for FY27 the A$70m Entire payment and A$25.8m of base earn-outs, FY27 EBITDA guidance raised to at least A$110m with Entire [P3]. GenusPlus, net cash A$399.3m less MPK's A$325m upfront and A$25m deferred and the 3.6c final dividend, half the A$50m earn-out added, lease payments A$24.3m plus A$2.7m in FY26 grossed up 30% for MPK [P4]. Contractors' cash includes customers' advance payments, which flatters their net cash; the same is true, less so, of Mayfield.

Mayfield on the same basis. FY27 EBITDA at the guidance midpoint, A$229m at 10.5%, is A$24.0m. Lease payments in FY27: about A$2.0m on existing leases plus seven months of Hope Valley, A$0.62m, so A$2.62m. EBITDAaL A$21.43m. Diluted shares 118.91m: 117.34m quoted, plus the 1,631,106 partly paid shares and 395,000 options in the money, less what their A$0.81m of payments would buy back at A$1.80. Net cash A$8.72m. Cash earnings before working capital: 21.43 - maintenance capital spending 2.0 (FY26 spending excluding Old Port Road was A$2.16m [M1 note 16]) - tax 0.30 x (21.43 - 1.6 tax depreciation + 0.2 interest) = 6.01, + 0.2 interest = A$13.62m, or 11.45c a diluted share. (Bell Potter's FY27 EPS forecast, 11.4c [S1], is the same number by another route.) SMEC's acquired customer relationships carry a deferred tax liability [M1 note 36], so their amortisation is not deductible and is ignored.

```
equity = (multiple x 21.43 + 8.72) / 118.91
 8.0x  A$1.52     9.0x  A$1.70     10.0x  A$1.88     11.7x  A$2.18
property credited at its valuation (notional rent 6.5% x 25.59 = 1.66 taken off EBITDAaL, property added back):
equity = (multiple x (21.43 - 1.66) + 25.59 + 8.72) / 118.91
 8.0x  A$1.62     9.0x  A$1.78     10.0x  A$1.95
P/E on cash earnings of 11.45c:
 13x  A$1.49     14x  A$1.60     15.4x (Korvest)  A$1.76     17.4x (IPD)  A$1.99
```

Which multiple? The two peers with forward guidance trade at 9.0 and 10.0 times FY27 EBITDAaL. Mayfield deserves less while its order book shrinks and theirs grow, while it is a fifth to a tenth of their size, and while its cash conversion is unproven after the acquisitions: about 10% less, or 8.1 to 9.0 times, which I round to 8.5 times for the middle. The full peer multiple, 10 times, belongs to the good case: an order book back above A$135m and cash conversion shown. IPD's trailing 11.7 times is for a distributor with 84% pre-tax cash conversion and recurring trade sales; it is not a fair forward multiple for a project manufacturer. Korvest is the useful check on cash: it converted only 27% of FY26 EBITDA to operating cash after tax (a working capital build and a new factory) and still trades at 15.4 times earnings, so a weak cash year alone does not wreck a multiple when the order book is at a record.

### Method 2: a discounted cash flow
From 1 October 2026, FY27 counted as three quarters of a year, mid-year discounting. Lease payments A$2.62m, A$3.10m, then rising A$0.1m a year; capital spending A$2.5m (Hope Valley fit-out), then A$2.2m rising A$0.1m a year; tax 30% of EBITDAaL less tax depreciation of A$1.6m to A$2.0m; working capital 8% of each year's revenue growth (A$3.6m in FY27 for N-Series stock and debtors and organic growth); terminal growth 2.5%; net cash A$8.72m; 118.91m shares.

| Path | Revenue FY27 to FY31 (A$m) | EBITDA margin | Free cash flow FY27 to FY31 (A$m) | 10.5% | 11.5% | 12.5% |
| --- | --- | --- | --- | --- | --- | --- |
| Middle: orders recover to about revenue | 229, 240, 252, 262, 270 | 10.5% | 9.4, 12.9, 13.6, 14.3, 14.9 | A$1.49 | A$1.33 | A$1.20 |
| Bad: orders stay near the September quarter's pace | 212, 175, 180, 186, 192 | 9.2%, then 8.0% to 9.0% | 6.2, 8.9, 6.3, 7.1, 7.3 | A$0.79 | A$0.72 | A$0.65 |
| Good: data centre awards land, growth continues | 232, 265, 290, 310, 325 | 11.0% | 10.4, 13.9, 16.3, 18.1, 19.5 | A$1.87 | A$1.67 | A$1.51 |

The input that moves the answer most is the discount rate, then the margin: on the middle path each point of margin is worth about A$0.16 a share at 11.5% (A$1.33 at 10.5%, A$1.49 at 11.5%). The discounted cash flow values the middle path below the price; the market is paying for something between the middle and good paths, which is what peer multiples built on a data centre boom imply.

### Check: what trade buyers pay
Mayfield paid about 5 times EBITDA for SMEC [M13]; Southern Cross is paying 5.5 times EBIT for Entire, a fire and air-conditioning contractor [P3]. At 6 to 7 times FY27 EBITDAaL, Mayfield is worth A$1.15 to A$1.33. Private businesses of this kind change hands for less than the listed market pays, so a takeover is no floor under the price. Any bid would need Nightingale, at 26.9%, and there is no sign of one.

### Range
- Bad: A$1.15 to A$1.20 by March 2027 (7 times a trimmed FY27), and A$0.65 to A$0.80 on the bad path over the longer run (discounted cash flow).
- Middle: A$1.60 to A$1.70 on peer multiples less a discount (A$1.65), A$1.49 to A$1.60 on cash earnings at 13 to 14 times; the discounted cash flow gives less, A$1.20 to A$1.49.
- Good: A$1.95 to A$2.07 (10 times FY27 EBITDAaL at the top of guidance).
The main thing each depends on: whether orders return to about A$55m to A$60m a quarter, which is what keeps work in hand flat at the guided revenue.

## Why the market is wrong
I can't say it is. At A$1.55 the market prices Mayfield at 8.2 times FY27 EBITDAaL at the guidance midpoint and 13.5 times FY27 cash earnings: a 10% to 20% discount to peers whose order books are growing. That is roughly my middle case, less something for a downside that is bigger than the upside. The fact sheet's +37% came from putting IPD Group's trailing multiple on Mayfield's forward year, and from an "against" case (FY26 earnings at the same 10 times) that is really a middling case: if orders don't recover, the multiple falls too. There are reasons to think the market may be too gloomy (guidance was raised on 20 October with the September quarter in hand; the managing director, a director and the largest holder all bought after the price fell; the tender pipeline is large), but none is a mechanism that shows the answer before the 1H result, and that result could as easily confirm the slide.

## Outcomes and chances
Each price is the valuation above applied to that outcome's earnings, plus the dividends in the window. Multiples: 7 times (bad, the private-market and lower listed range), 8.5 times (middle, the forward peers less 10%), 10 times (good, the forward peers in full). The middle and good cases average the plain and property-credited versions; the bad case gives the property no credit.

### As an ordinary pick, resolve by 31 March 2027 (142 days from 9 November; after the 1H FY27 result, about 27 February, and the interim dividend, ex about early March as last year's was on 4 March [M9])
| Outcome | What happens | Chance | Price by resolve date |
| --- | --- | --- | --- |
| Bad | Work in hand at 31 December below A$100m (December-quarter orders under about A$45m), 1H operating cash flow under half of EBITDA, FY27 guidance trimmed to about A$220m at a 9.5% margin. EBITDAaL A$18.28m at 7 times, no property credit | 30% | A$1.15, plus a 2.0c interim: A$1.17 (-24.6%) |
| Middling | In line: 1H revenue about A$110m to A$115m at a 10% to 11% margin, work in hand A$105m to A$125m, operating cash flow at least 60% of EBITDA, guidance held. EBITDAaL A$21.43m at 8.5 times (plain A$1.605, property credited A$1.701) | 50% | A$1.65, plus 2.2c: A$1.67 (+8.1%) |
| Good | Data centre awards land: work in hand of A$135m or more, cash conversion of 80% or more, guidance at the top (A$232m at 11%). EBITDAaL A$22.90m at 10 times (A$1.999 and A$2.074) | 20% | A$2.04, plus 2.2c: A$2.06 (+32.8%) |

Expected value A$1.600: **+3.2% before costs, 0.0% after**. Minimum (rulebook section 5a): (2.13% + 5%) x 142 / 365 = 2.77%. Fails. It would pass at **A$1.50 or below** (1.600 / (1 + 0.0277 + 0.0325) = 1.509).

Why 30/50/20 and not even odds: work in hand has fallen for five months, September-quarter orders were about 0.6 of revenue while every peer's order book grew, a holder sold about 5% of the company in a day after the AGM, and cash conversion has not yet been shown to recover. Against that: guidance was raised on 20 October, the directors who bought did so after the September figure was known, and the pipeline is large. With even 25/50/25 chances the expected value is A$1.645, +6.1% before costs and +2.85% after, which only just clears the 2.77% minimum, with a one-in-four chance of losing a quarter. That is not a case worth sending to review now.

### As a value pick, resolve by 30 September 2028 (691 days; FY27 and FY28 results, two AGMs, four dividends)
| Outcome | What happens | Chance | Price by resolve date |
| --- | --- | --- | --- |
| Bad | Orders stay near A$150m to A$170m a year; FY28 revenue about A$175m at an 8% margin (EBITDA A$14.0m, EBITDAaL A$10.9m) at 7 times; net cash about A$12.9m after dividends | 30% | A$0.75, plus about 8c of dividends: A$0.83 (-46.5%) |
| Middling | Orders recover to about revenue; FY28 revenue A$240m at 10.5% (EBITDAaL A$22.1m) at 8.5 times; net cash about A$17.7m | 50% | A$1.78, plus about 10c: A$1.88 (+21.1%) |
| Good | Data centre and mining awards keep coming; FY28 revenue A$265m at 11% (EBITDAaL A$26.05m) at 10 times; net cash about A$18.4m | 20% | A$2.38, plus about 11c: A$2.49 (+60.9%) |

Expected value A$1.686: **+8.8% before costs, +5.5% after**, against a minimum of (2.13% + 5%) x 691 / 365 = 13.5%. The middling leg passes (+21.1% against +15%); the bad leg fails by a long way (-46.5% against -10%). All three legs pass only at **A$0.92 or below** (bad leg 0.83 / 0.9 = 0.92; middling leg 1.88 / 1.15 = 1.63; minimum leg 1.686 / 1.1675 = 1.44). With 25/50/25 chances the expected gain after costs is +10.9%, still under the minimum. A project manufacturer whose orders have fallen by a third cannot have a two-year bad case within 10% of today's price.

Round-trip costs: a 2.5% position is about A$2,016 (NZ$2,500 at 0.806 Australian dollars to the NZ dollar, 6 November [M26]). The spread is about 1.4% to 1.5% (Corwin and Schultz, src/spreads.py: 1.39% over 21 sessions and 1.55% over 60 to 30 October; the bid and ask in the 6 November data, A$1.45 and A$1.655, are after-close quotes and not used); the size cost is 0.18% each way (src/fills.py: daily volatility 4.1%, average day A$1.04m); brokerage is A$15 each way (0.74%) unless the monthly plan covers it; and 0.5% to change NZ dollars, each way. That is 2.4% to 4.4%; I use 3.25%.

## Dated events
What each must show, and what it does to the case.
- **About 1 December 2026: Hope Valley opens** and its rent starts [M1 note 33; M4 slide 15]. This shows cost, not demand. It matters only if Mayfield pairs it with new Western Australian orders.
- **Any time: order or work-in-hand announcements.** There were four from January to May 2026 and none since 7 May [M24]. One that takes work in hand back above A$130m, or a single data centre award of A$20m or more, would move the odds toward the good case before February.
- **About 24 November 2026: IPD Group's AGM update** [P1]. Not Mayfield, but it moves the peer multiple.
- **Late January 2027 (likely, not announced): a half-year profit update and the interim dividend**, as on 27 and 29 January 2026 [M8][M9].
- **About 27 February 2027: the 1H FY27 result.** The deciding event. It shows work in hand at 31 December, the half's operating cash flow, the margin and the guidance.
- **About 29 May 2027:** Nightingale's 12-month no-sale statement ends [M16].
- **Late August 2027:** the FY27 result.

Reopen or close, on the 1H result:
- **Reopen as an ordinary pick, resolving on the FY27 result (31 August 2027)**, if all of: work in hand at 31 December 2026 is A$125m or more (December-quarter orders of about A$65m or more); 1H operating cash flow is at least 70% of 1H underlying EBITDA; FY27 guidance is held or raised with a 1H margin of at least 10%. Then, on FY28 earnings, I would put the outcomes at about A$1.54 (bad, 20%), A$1.89 (middling, 55%, 9.5 times FY28 EBITDAaL of A$22.1m plus A$15m of cash) and A$2.54 (good, 25%), an expected A$1.98, and the case clears the minimum (3.6% over 183 days, plus 3.25% costs) at **A$1.86 or below**. The price may run past that on the day.
- **Close (no case)** if work in hand at 31 December is below A$100m, or 1H operating cash flow is below 40% of EBITDA, or guidance is cut. Then the bad path becomes the middle one, worth about A$1.15 to A$1.20 by mid-2027, and only a price near A$0.92 would bring it back as a value pick.
- **In between:** re-run the outcomes with the new figures; the ordinary-pick watch trigger moves with them.
- **Watch triggers now, nothing else changing:** A$1.50 as an ordinary pick resolving 31 March 2027 (the stock traded at A$1.52 on 23 October and as low as A$1.345 on 21 October [M25]); A$0.92 as a value pick.

## What would make this wrong
For any later buy, and for the verdict itself:
1. **Orders.** If December-quarter orders look like September's (about A$30m to A$37m), work in hand falls below A$100m, FY28 earnings fall, the multiple falls with them, and the stock heads for A$1.15 or lower. The price already touched A$1.345 on heavy selling on 21 October.
2. **Cash.** If 1H operating cash flow is again a small fraction of EBITDA with SMEC's debtors already built, the "timing" reading is wrong. With about A$9m of cash, an A$8.4m facility, a dividend to pay, Hope Valley to fit out and a fresh 10% placement capacity, weak cash leads to borrowing or a raise.
3. **The sector's multiple.** The peers have lost 9% to 27% since June, and Southern Cross 11% in the week to 6 November. If the data centre trade keeps unwinding, 8.5 times is too high for the middle case.
On the other side, what would make waiting wrong: a large data centre award before February, which would lift the price before the reopen test can be run.

Exit rule, if it is bought later: sell if reported work in hand falls below A$100m, if FY27 guidance is cut, or if a half's operating cash flow is below 40% of its EBITDA; otherwise hold to the resolve date.

## Checks
- Not on Cam's excluded list: config/judgement_excluded.csv has no entries (confirmed by Cam on 8 November 2026).
- No placement-pattern reopening in the last 30 sessions (rulebook section 9): the last trading halt was on 7 November 2025, before the placement; the only share issues since 12 October 2026 are 20,000 shares from options (Appendix 2A, 12 October 2026) [M22][M24]; Norgate shows a trade every session from September to 30 October [M25].
- Liquidity (rulebook section 3): median value traded A$488,423 a day over the 20 sessions 5 to 30 October 2026 (close times volume, lowest day A$102,214) [M25], above the A$10,000 floor. The most the position can be: 2 sessions x 10% x A$488,423 = A$97,685, far above a 2.5% position of about A$2,016.

## Corrections to the fact sheet
1. The 15 September 2026 notice: a purchase of 750,000 shares at A$1.907 (the acquired row, both holdings and the consideration agree), not a sale; but it can't have been bought on market on 15 September (only 339,723 shares traded that day, and the average is below the 14 September low), so it doesn't count as an on-market buy. The "on market sale" words are copied from the 29 May notice [M16][M17][M25].
2. The "our way" anchor, A$2.12, is the good case, not the middle. It applies IPD Group's trailing multiple to Mayfield's forward year. On a lease-consistent basis the forward peers trade at 9.0 to 10.0 times FY27 EBITDAaL, and a business with a shrinking order book earns a discount to them.
3. The "against us" anchor, A$1.64, is not an against case: it keeps the full peer multiple on earnings that have stopped growing. With orders at the September quarter's pace the value is about A$1.15 to A$1.20 by March 2027 and A$0.83 over two years.
4. Organic growth in the FY27 guidance is about 6% on the company's own FY26 pro forma revenue of A$204m (after A$10m to A$15m of N-Series), not about 9% [M2 slide 6].
5. The N-Series handover now finishes by 30 November 2026, not 31 October [M4 slide 14]; the acquisition date for the accounts is 31 October [M1 note 39].
6. The AGM was held on 20 October 2026 at 1pm Adelaide time; its results were released on 21 October [M5].
7. The receivables rise was not "partly from the acquisitions" in the way the sheet implies: BE Switchcraft brought A$4.31m of receivables, but SMEC brought none (an asset purchase), so Mayfield funded SMEC's debtors out of operating cash [M1 note 36].
8. Missing from the sheet: 5.79m shares traded on 21 October 2026 with a low of A$1.345, a seller below 5% who has not been identified; Ellerston and UBS were the buyers that filed [M20][M21][M25].
9. Missing from the sheet: the peers' order books rose to records while Mayfield's fell, so the fall is specific to Mayfield [P2][P3][P4].

## What I couldn't verify
- September-quarter revenue (not disclosed), so the order intake estimates are ranges; whether the A$114.7m of work in hand at 30 September includes N-Series' A$3.9m.
- Who sold on 21 October 2026, and whether anything said at the AGM on 20 October prompted it. No ASX announcement explains it.
- The venue and dates of Nightingale's 750,000-share purchase.
- The September-quarter cash flow and the cash balance today ("cash position strengthening into Q2" is the company's unaudited claim).
- Which contract the customer's specification letter concerns and how much is at stake.
- Broker coverage comes from FNArena, a secondary source [S1]; I did not see the broker notes.
- Whether Mayfield is outside the S&P/ASX 300 (inferred from its size, not checked against the list); the 1H FY27 result date (about 27 February, from last year's date and the fact sheet's reading of ASX company data).

## Sources
Mayfield Group Holdings (ASX:MYG):
- [M1] App 4E and 2026 Annual Report, 27 Aug 2026 (03131149): statements, notes 8, 9, 10, 11, 16, 20, 22, 23, 24, 32, 33, 34, 36, 39, 40, auditor's report, shareholder information: https://announcements.asx.com.au/asxpdf/20260827/pdf/0739q2gn0tfn51.pdf
- [M2] FY2026 Results Investor Presentation, 27 Aug 2026 (03131168): https://announcements.asx.com.au/asxpdf/20260827/pdf/0739rd63gyjlr7.pdf
- [M3] FY2026 Results Commentary, 27 Aug 2026 (03131166): https://announcements.asx.com.au/asxpdf/20260827/pdf/0739r7x0pmp309.pdf
- [M4] AGM Presentation, 20 Oct 2026 (03154321): https://announcements.asx.com.au/asxpdf/20261020/pdf/075j5pcq94htdf.pdf
- [M5] Notice of 2026 AGM, 18 Sep 2026 (03140931): https://announcements.asx.com.au/asxpdf/20260918/pdf/0747bbvcnxtcxg.pdf
- [M6] Half Yearly Report and Accounts, 27 Feb 2026 (03066419): https://announcements.asx.com.au/asxpdf/20260227/pdf/06ww0dfxkh1vlk.pdf
- [M7] Investor presentation, half year results, 27 Feb 2026 (03066421): https://announcements.asx.com.au/asxpdf/20260227/pdf/06ww0jsvtkvny6.pdf
- [M8] Earnings guidance, December 2025, 27 Jan 2026 (03053002): https://announcements.asx.com.au/asxpdf/20260127/pdf/06vm2g6cm9s0py.pdf
- [M9] Interim dividend declared, 29 Jan 2026 (03054211): https://announcements.asx.com.au/asxpdf/20260129/pdf/06vqc8x4typcxc.pdf
- [M10] Board declares FY2026 final dividend, 26 Aug 2026 (03130691): https://announcements.asx.com.au/asxpdf/20260826/pdf/0738hdg7hgbnbl.pdf
- [M11] Work-in-Hand Update, 14 Apr 2026 (03082361): https://announcements.asx.com.au/asxpdf/20260414/pdf/06yggk2gwyxhg0.pdf
- [M12] Contracts Update, 7 May 2026 (03091638): https://announcements.asx.com.au/asxpdf/20260507/pdf/06zc2g6bqj3hjk.pdf
- [M13] Acquisition of SMEC Power & Technology, 25 Feb 2026 (03065066): https://announcements.asx.com.au/asxpdf/20260225/pdf/06wrk214ps84c8.pdf ; Completion, 1 Apr 2026 (03078289): https://announcements.asx.com.au/asxpdf/20260401/pdf/06y1c802cwxcts.pdf
- [M14] Acquisition of Nilsen Switchboards Division, 13 Jul 2026 (03114391): https://announcements.asx.com.au/asxpdf/20260713/pdf/071nfq6q8wvlnt.pdf ; Completion, 3 Aug 2026 (03121209): https://announcements.asx.com.au/asxpdf/20260803/pdf/072c40qx000g5z.pdf
- [M15] Placement and Share Purchase Plan, 11 Nov 2025 (03023647): https://announcements.asx.com.au/asxpdf/20251111/pdf/06rs3239s4s1z0.pdf
- [M16] Sale of Mayfield Shares, 29 May 2026 (03098845): https://announcements.asx.com.au/asxpdf/20260529/pdf/0702v06j7kscsn.pdf ; Appendix 3Y, L Phillips, 29 May 2026 (03098851): https://announcements.asx.com.au/asxpdf/20260529/pdf/0702vfl5lm6znk.pdf
- [M17] Appendix 3Y, L Phillips, 15 Sep 2026 (03139807): https://announcements.asx.com.au/asxpdf/20260915/pdf/074400s4p5903m.pdf
- [M18] Appendix 3Y, L Phillips, 29 Oct 2025 (03017456): https://announcements.asx.com.au/asxpdf/20251029/pdf/06r6ntwm70f1yz.pdf ; A Steele, 29 Oct 2025 (03017455): https://announcements.asx.com.au/asxpdf/20251029/pdf/06r6nrrdbldqgp.pdf ; A Steele, 19 Nov 2025 (03028982): https://announcements.asx.com.au/asxpdf/20251119/pdf/06s77pn4gv2ps2.pdf ; A Steele, 1 Dec 2025 (03034672): https://announcements.asx.com.au/asxpdf/20251201/pdf/06sr67dhfkgzyj.pdf
- [M19] Appendix 3Y, A Rowe, 27 Oct 2026 (03157769): https://announcements.asx.com.au/asxpdf/20261027/pdf/075v3sbwbbk5yf.pdf ; R Henderson, 10 Sep 2026 (03138280): https://announcements.asx.com.au/asxpdf/20260910/pdf/073z095mc7n6dp.pdf ; R Henderson, 3 Nov 2026 (03161367): https://announcements.asx.com.au/asxpdf/20261103/pdf/076580w15y4hvv.pdf ; earlier Henderson buys per the fact sheet's sources (20 Mar and 14 May 2026)
- [M20] Ellerston Capital, change in substantial holding (amended), 27 Oct 2026 (03157965): https://announcements.asx.com.au/asxpdf/20261027/pdf/075vmcj6l0xcxn.pdf
- [M21] UBS Group: ceasing, 15 Oct 2026 (03152898): https://announcements.asx.com.au/asxpdf/20261015/pdf/075chgcprx7gbn.pdf ; becoming, 23 Oct 2026 (03156656): https://announcements.asx.com.au/asxpdf/20261023/pdf/075qfgrvq3b57m.pdf ; ceasing, 27 Oct 2026 (03157791): https://announcements.asx.com.au/asxpdf/20261027/pdf/075v5l1yh99bts.pdf ; becoming, 4 Nov 2026 (03162000): https://announcements.asx.com.au/asxpdf/20261104/pdf/07671z4d4pg770.pdf
- [M22] Application for quotation of securities: 12 Oct 2026 (03151308), 117,336,443 quoted: https://announcements.asx.com.au/asxpdf/20261012/pdf/07571s736fhdz2.pdf ; 29 Jul 2026 (03119439), unquoted securities list: https://announcements.asx.com.au/asxpdf/20260729/pdf/0725pqx24rh1jx.pdf
- [M23] S&P DJI March 2026 quarterly rebalance, All Ordinaries addition, 6 and 10 Mar 2026 (03069416, 03070446): https://announcements.asx.com.au/asxpdf/20260306/pdf/06x4vd88v6bpg7.pdf ; https://announcements.asx.com.au/asxpdf/20260310/pdf/06x8crc81mtrkl.pdf
- [M24] ASX company data: data/research_data/asx_company.json (fetched 7 Nov 2026 UTC: last trade A$1.55, previous close A$1.535, income statement history, announcement list), and the ASX company header and key statistics at https://asx.api.markitdigital.com/asx-research/1.0/companies/<code>/header read on 8 Nov 2026 for MYG, IPG, KOV, SXE and GNP; announcement list https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=MYG&timeframe=Y&year=2026
- [M25] Norgate prices and volumes, data/norgate/universe/prices_2026.csv.gz (to 30 Oct 2026)
- [M26] data/fx/fx_daily.csv (6 Nov 2026: 0.806387 Australian dollars to the NZ dollar)

Peers:
- [P1] IPD Group, FY26 Results Announcement, 14 Aug 2026 (03125098): https://announcements.asx.com.au/asxpdf/20260814/pdf/072r6vnbwfr1fr.pdf ; Appendix 4E and Financial Report (03125087): https://announcements.asx.com.au/asxpdf/20260814/pdf/072r618b2n2h9s.pdf
- [P2] Korvest, FY26 press release, 28 Jul 2026 (03118830): https://announcements.asx.com.au/asxpdf/20260728/pdf/0723zj379wfrlq.pdf ; Correction June 2026 Annual Report, 3 Aug 2026 (03121305): https://announcements.asx.com.au/asxpdf/20260803/pdf/072cbxct1nj97l.pdf
- [P3] Southern Cross Electrical Engineering, Full Year Results Announcement, 19 Aug 2026 (03126581): https://announcements.asx.com.au/asxpdf/20260819/pdf/072x2sz6hd52w7.pdf ; Annual Report (03126579): https://announcements.asx.com.au/asxpdf/20260819/pdf/072x2nq3vqkfzh.pdf ; Acquisition of Entire, 12 Oct 2026 (03150893): https://announcements.asx.com.au/asxpdf/20261012/pdf/07560x96j7htcl.pdf ; AGM Presentation, 27 Oct 2026 (03157360): https://announcements.asx.com.au/asxpdf/20261027/pdf/075t4wdt2gsxfg.pdf
- [P4] GenusPlus Group, FY2026 Results Announcement, 25 Aug 2026 (03129283): https://announcements.asx.com.au/asxpdf/20260825/pdf/0734yskstb96yn.pdf ; Appendix 4E and Annual Financial Report (03129282): https://announcements.asx.com.au/asxpdf/20260825/pdf/0734yqfrylvqhy.pdf ; Results Presentation (03129284): https://announcements.asx.com.au/asxpdf/20260825/pdf/0734yvqj839vp2.pdf

Secondary:
- [S1] FNArena consensus page for MYG (broker ratings, targets and FY27 to FY28 EPS forecasts), read 8 Nov 2026: https://www.fnarena.com/index.php/analysis-data/consensus-forecasts/stock-analysis/?code=MYG
