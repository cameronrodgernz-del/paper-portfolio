# Betr Entertainment (ASX:BBT): special situation deep dive. Not a value pick: the "nothing happens" value (A$0.104) is 17% below the price, and even a sale of the PointsBet stake to MIXI at its 2025 price (A$0.151) is only 21% above it

Written 2026-11-08 by the research desk. Price at writing: A$0.125 (last trade on Friday 6 November 2026, bid A$0.115, ask A$0.125, ASX company data in data/research_data/asx_company.json, fetched 7 November 2026 UTC [M1]; Norgate's last close in the repo is A$0.13 on 30 October [M3]). Market value: A$131.2m (1,049,587,762 shares on issue, ASX company data [M1]).
Status: finished. This is a simulation and not financial advice.
Verdict: **No case.** No card, no red team. It was treated as a special situation under rulebook section 5a (the value rests on a blocking stake in PointsBet that MIXI, the controlling holder, may want), not as a value pick. On the chances below the expected price to the 7 May 2027 resolve date is about A$0.099, about 21% below the price before costs and about 27% below after them, against a minimum gain of +3.5%. There is no dated forcing event inside six months; the one real deadline, Betr's NAB loan on 30 September 2027, presses Betr to sell, not MIXI to pay. The conditions that would reopen it are under "What would make this wrong".
Fact sheet: research/facts/BBT.md, grade C on its own. Its question: what will Betr's 27.72% PointsBet stake realise for Betr holders, and can the wagering business deliver FY27 guidance after a first quarter below its own margin assumption? Its special-situation anchor: A$0.166 a share if MIXI bought the stake at A$1.25.

Order of work. The brief quoted the price, so it was in view from the start. The PointsBet stake is valued from PointsBet's and MIXI's own filings (what MIXI paid, what the 2025 independent expert said PointsBet was worth, and PointsBet's results since); the wagering business from Betr's guidance, its cash spending and Tabcorp's market multiples, which is how the market prices a listed bookmaker. Betr's own share price enters only in "Why the market is wrong" and "Outcomes and chances", and in one line that backs out what the market is paying for each part. Arithmetic was run in `python3 -I` from a scratch script (bbt_calc.py, not committed); the key lines are shown below.

> In one paragraph: the first test kills the case. The fact sheet's good-case anchor, MIXI buying Betr's 96.35m PointsBet shares at A$1.25, is MIXI's price from a bidding contest in August 2025, when PointsBet was guiding to A$11m to A$14m of EBITDA. Since then PointsBet has gone backwards: first-half FY27 revenue fell 16% and normalised EBITDA was a loss of A$6.9m; it has net liabilities of A$34.8m and A$5.3m of its own cash, and lives on MIXI loans [P1, P2]. MIXI has said nothing about the minority in 14 months, has not crept, has funded PointsBet with debt rather than equity, and has no deadline. Betr does have one, the NAB loan of A$34.1m secured on the stake and due on 30 September 2027 [A1, A4]. On today's revenue, MIXI's own 2025 multiple puts PointsBet at about A$1.03 a share and the 2025 independent expert's midpoint at about A$0.83; PointsBet last traded at A$0.745. The bigger problem is that Betr's price already pays for a deal: with the wagering business at Tabcorp's 6.1 times EBITDA on the middle of Betr's guidance, the market is valuing the PointsBet stake at about A$0.97 a PointsBet share, 30% above where PointsBet trades. Even a sale at A$1.25 lifts Betr only to about A$0.151 on the middle of guidance (A$0.168 at the top); if nothing happens Betr is worth about A$0.104 on Tabcorp's multiple and about A$0.089 on a cash-flow count, because the business spends about A$8.5m a year on its platform against A$13m to A$19m of guided EBITDA before A$4.7m of pay settled in shares. The blocking stake is real (MIXI can't reach 90% or carry a delisting vote without Betr), but it blocks without forcing, and a PointsBet rights issue that Betr can't afford could erode the delisting veto.

Corrections to the fact sheet, for the record:
1. Matthew Tripp is Betr's Executive Chairman, not deputy chair; Michael Sullivan, the founding chairman, is a non-executive director [A1 directors' report].
2. PointsBet's last trade is A$0.745 (6 November 2026, after PointsBet's 13 October trading update and 30 October half-year result), not A$0.81 [M2, P1, P3]. The stake is worth A$71.8m at that price, not A$78.0m. PointsBet's median traded value over the 20 sessions to 30 October was A$3,329 a day, so the stake's "market value" is notional [M3].
3. The 14 January 2026 "active discussions" are about Betr's own M&A ("pursuing scale in the Australian market, both organically and via disciplined, value-accretive M&A"), not about the PointsBet stake or MIXI. No later Betr filing names a counterparty, and by October 2026 the wording had become "deploy capital selectively across organic growth, strategic investments and M&A where returns are strongest" [A7, A4].
4. Betr's cost of the stake is about A$1.19 a PointsBet share, not A$1.07 to A$1.10: A$72.5m for the first 66.0m shares (A$1.098) and, for the 30.3m from its offer, A$40.65m paid in the selective buy-back plus 5.71m Betr shares kept by accepting holders, about A$42.1m (A$1.39) [A21, A19, A20].
5. The holder list misses Tanarra Capital (103,853,879 shares, 9.98% on 22 October 2025) and Ellerston Capital (5.04%, 30 September 2025) [A26].
6. The Appendix 4C's "2.9 quarters of funding" counts A$11.1m of client money. On Betr's own cash (A$7.4m) and the A$1.3m undrawn it is about 1.3 quarters at the first-quarter burn [A4].
7. The NAB loan was extended twice: from 31 July 2026 to 31 July 2027 (25 February 2026), then to 30 September 2027 (after 30 June 2026). The rate is 6.46% plus a 2.25% facility fee [A12, A1, A4].
8. Betr left the All Ordinaries index on 21 September 2026 [A13].
9. Tabcorp now trades at A$0.915 (6 November), EV/EBITDA 6.1 times on ASX's market value; the 5.96 times used A$0.89 [M2, T1].

## The company in plain words
Betr runs one online bookmaker, betr, in Australia only, licensed in Tasmania since 7 July 2026 [A1]. It makes money from net win (what customers lose, less bonus bets and other generosity), and pays a large share of it away as point of consumption tax, GST and racing and sports product fees: cost of wagering services was A$86.6m on A$143.8m of revenue in FY26 [A1]. Its other big asset is 96,354,403 PointsBet shares (27.72%), bought in 2025 with a NAB loan, an A$130m equity raise and scrip [P4, A21].

Who runs it: Matthew Tripp (Executive Chairman; founder of the original betr), Andrew Menz (CEO since 1 July 2024, a director since 7 October 2025), Michael Sullivan (founding chairman, non-executive), with Blake Matthews CFO from 1 July 2026 [A1, A27].

Who owns it, from the register at 24 August 2026 and substantial holder notices [A1, A26]: Tripp 110.8m (10.6%, through YAST Investments), Majestic Equity (Catherine Tripp) 90.2m (8.6%; the two say they are not associates), Sullivan 93.4m (8.9%), Wilson Asset Management 10.02% (April 2026), Tanarra Capital 9.98% (October 2025), Bondi B Limited 6.74%, Host-Plus 5.30% (October 2025), Regal Partners 5.22% (May 2026), Ellerston 5.04% (September 2025). The top 20 hold 89.87%; there are 4,239 holders.

Bondi B Limited: a British Virgin Islands company (c/o OMG Chambers, Wickhams Cay 1, Road Town, Tortola; notice signed by Vivian Tang as authorised signatory) that was one of the three named investors in NTD Pty Ltd, the original betr, alongside Tripp's YAST and Catherine Tripp's Majestic Equity [A23, A24]. It received 69,840,064 shares on 1 July 2024 as its share of the merger consideration (deemed price A$0.19), escrowed for 12 months, and has held exactly that number ever since; it did not take up shares in the 2025 raise [A24, A22, A1]. Its notice lists no associates. No Betr or BlueBet filing names who owns it, and I could not find out (searches turned up nothing; an AFR article on betr's earlier News Corp backing could not be fetched) [W4]. It is a passive holder on the filings.

Five years: listed as BlueBet on 2 July 2021 (first close A$1.775); year-end closes A$1.47 (2021), A$0.365 (2022), A$0.195 (2023), A$0.30 (2024), A$0.20 (2025), A$0.125 now [M3]. Since the A$0.32 raise of May 2025 the price is down 61%.

## Why big investors may be overlooking it
- Size and trading: A$131m market value; median traded value A$10,009 a day over the 20 sessions 5 to 30 October 2026, with two days under A$1,500 [M3].
- Removed from the All Ordinaries from 21 September 2026 [A13]; not in the S&P/ASX 300.
- Concentrated register: insiders hold about 28% and the top 20 hold 89.9% [A1].
- A messy recent history: three deals in two years, a lost contest for PointsBet, a selective buy-back, an on-market buy-back, a CFO change, and an asset (the PointsBet stake) that can't be valued off a liquid price.
- An out-of-favour sector: federal advertising and inducement limits start on 1 January 2027 [A4].
None of these makes it cheap. They explain why the price can sit away from the parts, in either direction.

## What the filings show

### How Betr came to hold 27.72% of PointsBet
| Date | Event | Price |
| --- | --- | --- |
| 26 Feb 2025 | PointsBet agrees a scheme with MIXI [P7] | A$1.06 cash |
| 28 Apr 2025 | Betr buys 66,013,329 PointsBet shares (19.9%) from two of PointsBet's largest holders, funded by a A$35m NAB loan and cash [A14, A15, A21] | A$72.5m, A$1.098 a share |
| 29 Apr 2025 | Betr proposes a A$360m scheme (A$260m cash, A$100m scrip) and launches a A$130m raise at A$0.32 [A15] | Betr said "A$1.33" including synergies |
| 3 Jun 2025 | MIXI raises its scheme price [P7] | A$1.20 cash; independent expert's range A$0.96 to A$1.11 |
| 25 Jun 2025 | Scheme fails: Betr votes its 19.9% against; over 95% of other votes cast were in favour [P8] | |
| 26 Jun 2025 | MIXI announces a takeover bid [P8] | A$1.20 cash |
| 16 to 30 Jul 2025 | Betr bids all-scrip: 3.81, then 4.219 Betr shares a PointsBet share [A28, P18] | |
| 8 Aug 2025 | MIXI lifts to A$1.25, declares its bid unconditional, "best and final" unless it passes 50% [P10] | A$1.25 cash |
| 21 Aug 2025 | MIXI: A$1.30 only if it reaches 90%, "Last and Final"; acceptances 37.12% [P11] | |
| 26 Aug 2025 | Betr lifts to 4.375 Betr shares and promises a selective buy-back at A$0.32 [A16] | |
| 29 Aug 2025 | MIXI passes 50% [P12] | |
| 12 Sep 2025 | MIXI's bid closes at 66.43% (230,893,535 shares); MIXI says it paid A$289m [P13, P19] | A$1.25 |
| 25 Sep 2025 | Betr's bid closes with acceptances for 30,341,074 shares, taking it to 27.72% [A18] | 132,741,833 Betr shares issued |
| 20 Oct 2025 | Selective buy-back: 127,029,704 of those Betr shares bought back at A$0.32 [A20] | A$40.65m cash |

Betr said at the close that the stake "will be large enough to block actions that run against shareholder interests and drive constructive engagement with MIXI and the PointsBet board on value creation" [A18]. Betr's 2025 Takeovers Panel application against MIXI failed: the Panel declined to conduct proceedings and accepted that MIXI's confidentiality deed with PointsBet had no standstill [P18]. I found no standstill, voting agreement or any other agreement between Betr and MIXI in either company's filings.

### What MIXI and PointsBet have done since
- 6 October 2025: three MIXI executives join PointsBet's board; five independents leave. Chair Brett Paton and Sam Swanell stay [P14].
- December 2025: PointsBet moves its year-end to 31 March to match MIXI; Andrew Catterall replaces Swanell as CEO from 1 February 2026 [P15].
- 2 March 2026: MIXI starts lending to PointsBet. The facility is now A$23m, A$21m drawn at 30 September 2026 at 7.19%, each drawing due within 12 months; MIXI has also given a letter of financial support, and PointsBet says it is seeking a bigger MIXI facility and other working capital funding [P1].
- No creep: MIXI's holding is unchanged at 230,893,535 shares (66.43%) at 19 June and 30 September 2026, and PointsBet has published no MIXI holding notice since September 2025 [P4, P1]. MIXI's own release on the close said nothing about the remaining shares [P19].
- PointsBet's trading has worsened. H1 FY27 (April to September 2026): revenue A$112.7m, down 16%; net win A$122.1m, down 17%; normalised EBITDA a loss of A$6.9m against a A$2.9m profit a year earlier; Australian turnover down 14%, blamed on "proactive compliance actions" with its highest-value customers and on bad AFL results; operating cash outflow A$8.1m and A$7.1m of capitalised software; corporate cash A$5.3m; net liabilities A$34.8m [P1, P2, P3]. The nine months to March 2026 made a A$0.8m normalised EBITDA loss [P5]. Ontario's regulator proposed a five-day suspension of PointsBet Canada's iGaming registration in February 2026 over a 2024 reporting failure [P16].
- Betr is using its votes. At PointsBet's 28 November 2025 AGM 66m to 67m shares voted against every item, including the three MIXI directors; at the 25 August 2026 AGM 96,386,142 shares (Betr's stake, near enough) voted against the remuneration report, a first strike (28.94% against) [P6, P5].
- PointsBet's price: about A$1.00 in May and June 2026, A$0.935 at 30 June (Betr's carrying value), A$0.81 on 28 October, A$0.745 on 6 November; 52-week range A$0.715 to A$1.12 [P4, A1, M2, M3].

### Everything Betr has said about "consolidation" since 14 January 2026
- 14 January 2026: "We remain in active discussions with a number of existing and new industry participants regarding consolidation and partnership opportunities and will ensure appropriate disclosure should these discussions progress" [A7].
- 29 January and 26 February 2026: "well positioned to capitalise on market consolidation through actionable M&A opportunities with new and existing industry players"; "pursue transformative M&A" [A8, A9].
- 26 February 2026 (half-year directors' report): the PointsBet stake's carrying value "does not represent the Directors' assessment of the long-term value of the investment"; the directors believe "its underlying value may not be fully reflected in the share price" [A9].
- 30 April 2026: "Advancing discussions with existing participants, and potential new entrants; actively assessing consolidation opportunities arising from current market conditions" [A10].
- 30 July 2026: "Strategic investment in PointsBet creates additional optionality"; "multiple pathways to meaningful shareholder value" [A11].
- 27 August 2026 (annual report): "the value realised from the investment may differ from the carrying value"; Betr "intends to continue to hold the investment and assess its value over the longer term" [A1].
- 28 October 2026: "Deploy capital selectively across organic growth, strategic investments and M&A where returns are strongest"; transaction costs on "strategic initiatives" of A$0.3m in the quarter and A$0.8m the quarter before [A4].
Nothing has been filed by MIXI, PointsBet or anyone else that refers to a deal with Betr. So: deal work is going on and costing money, but 10 months after "active discussions" nothing has been disclosed, and the language has cooled.

### The wagering business on its own
| | FY25 | FY26 | Q1 FY27 | Source |
| --- | --- | --- | --- | --- |
| Turnover | A$1,420.4m | A$1,594.7m | A$432.3m (+19.1%) | [A1, A4] |
| Net win (margin) | A$145.2m (10.4%) | A$158.1m (9.9%) | A$38.4m (8.9%, 10.5% a year earlier) | [A1, A4] |
| Revenue | A$132.0m | A$143.8m | | [A1] |
| Cost of wagering services (taxes, product fees) | A$73.6m | A$86.6m (60% of revenue) | A$23.0m paid | [A1, A4] |
| Advertising and marketing | A$19.5m | A$32.8m | A$5.3m paid | [A1, A4] |
| Normalised EBITDA (before one-offs and share-settled pay) | A$7.2m | loss A$7.1m (H1 loss A$13.2m, H2 A$6.1m) | not given | [A1] |
| Statutory loss after tax | A$6.8m | A$40.2m | | [A1] |
| Operating cash flow | outflow A$19.3m | outflow A$25.7m (Q4 inflow A$2.6m) | outflow A$6.8m | [A1, A3, A4] |
| Capitalised platform development | about A$6m | A$8.7m | A$2.1m | [A1, A4] |
| Expenses settled in equity | A$2.8m | A$4.7m | | [A1] |

Guidance and record. FY27 normalised EBITDA of A$13m to A$19m, excluding one-offs and share-based payments, with positive operating cash flow weighted to the second half; it assumes "historical Net Win margins (above 10%) and no material regulatory, taxation or cost of sales changes". First set on 29 January 2026, affirmed 27 August, reaffirmed 28 October [A8, A2, A5]. The only dated target so far was met in its lower half (H2 FY26: A$6.1m against A$5m to A$8m) [A2]. FY26's first half, a A$13.2m loss, had no target in front of it [A8]. The first quarter of FY27 ran below the guidance assumption (8.9% net win margin; Betr puts the cash cost of customer-friendly results at A$4.2m), and October to 26 October ran at 11.5% (A$15.7m of net win, up 73%), which Betr says has recovered more than half of it [A4].

Cash earnings. Take the middle of guidance, A$16m, less A$4.7m of pay settled in shares (a real cost; Betr's guidance leaves it out, Tabcorp's EBITDA does not), less about A$8.5m a year of capitalised development (A$8.7m in FY26, A$2.1m in the first quarter) and about A$1.2m of lease payments: about A$1.6m a year before interest. At the top of guidance about A$4.6m; at the bottom, minus A$1.4m. The NAB loan costs about A$3.0m a year (8.71% on A$34.1m), so at the middle of guidance the company is not yet covering its interest from cash earnings [A1, A4].

Point of consumption tax and product fees. Betr pays each state's point of consumption tax and racing and sports bodies' product (race fields) fees, both set as a share of revenue or turnover; it lists increases in either as a key risk [A1]. Cost of wagering services was 60% of revenue in FY26 [A1]; PointsBet reports GST, point of consumption tax and product fees together at 47.4% of net win in its latest half [P2]. Rates are 15% in NSW, Victoria, SA, WA and Tasmania, 20% in Queensland and 25% in the ACT, per an industry news site (June 2026), which reported no scheduled change [W3]. I found no dated rate or fee change inside the window in primary sources. The federal reforms starting 1 January 2027 limit advertising and inducements and add cost-recovery levies whose size isn't set; Betr says they are "not expected to materially impact betr's trading" [A4].

### Cash and debt
- NAB: A$35m facility, A$34.1m drawn at 30 September 2026; 6.46% plus a 2.25% facility fee; secured on the PointsBet shares; loan to value below 60% "at all times" and interest cover of 1.5 times tested quarterly from 31 December 2026; due 30 September 2027 [A1, A4]. The loan-to-value line breaks if PointsBet trades below A$0.590 (A$34.1m / 0.6 / 96.35m shares); at A$0.745 it is 47.5% [calc].
- Cash A$18.5m at 30 September 2026, of which A$11.1m is client money: own cash A$7.4m [A4]. Leases A$4.9m at 30 June [A1]. Net current liabilities A$10.2m at 30 June; the auditor's report has no going-concern paragraph, and the directors' going-concern note relies on forecast cash flow and the NAB extension [A1].
- Betr says FY27 needs no new equity [A4], but the AGM on 26 November asks for the extra 10% placement capacity [A6].

### Share count, raisings, buy-backs and director dealing
- Share count: 296.3m before the betr merger; 265.4m issued to the betr vendors on 1 July 2024 at A$0.19; 44.1m at A$0.34 (February 2025, A$15m); 8.8m at A$0.34 for TopSport (April 2025); 406.3m at A$0.32 in May 2025 (A$130m); 1,025.5m at 30 June 2025; plus 132.7m for PointsBet shares (26 September 2025), less 127.0m in the selective buy-back at A$0.32 (20 October 2025), less 3.38m bought on market for A$0.68m at A$0.17 to A$0.25 (March to June 2026), plus 6.94m at A$0.18 to a contractor in lieu of fees (19 June 2026) and plan issues: 1,046.3m at 30 June 2026 and 1,049.6m now. A further 27.6m performance rights and 9.6m options are on issue [A1, M1].
- Director dealing: Tripp bought 1,842,628 shares on market at A$0.23 to A$0.2399 on 6, 7 and 14 November 2025 [A25]. No director has bought or sold on market since, through a fall from A$0.23 to A$0.125. In the May 2025 raise Tripp, Sullivan and Tim Hughes put in A$3.96m at A$0.32 [A1].
- Substantial holder moves in the last year: WAM up to 10.02% (8 April 2026), Regal in at 5.22% (4 May 2026), Australian Retirement Trust out (1 May 2026); Harvest Lane out and Host-Plus back in during October 2025 [A26].

## Valuation

### The PointsBet stake (96,354,403 shares)
| Basis | A$ a PointsBet share | Stake, A$m |
| --- | --- | --- |
| Last trade, 6 Nov 2026 [M2] | 0.745 | 71.8 |
| The 2025 independent expert's midpoint (A$1.035), as a revenue multiple (1.32 times FY25 revenue of A$261.4m) applied to today's revenue (about A$235m, desk estimate) less today's net debt (A$19.9m) [P7, P1] | 0.83 | 80.3 |
| MIXI's 2025 price (A$1.25, about 1.60 times FY25 revenue) on the same basis | 1.03 | 98.9 |
| MIXI's 2025 price itself [P10] | 1.25 | 120.4 |
| MIXI's "Last and Final" price if it reaches 90% [P11] | 1.30 | 125.3 |

```
PBH mcap 259.0, net debt incl leases 19.9, EV 278.8, LTM rev ~234.7, EV/rev 1.19
  MIXI 2025 price: EV/rev 1.60 -> PBH today A$1.026/sh
  expert 2025 midpoint: EV/rev 1.32 -> PBH today A$0.833/sh
```
The revenue estimate is H1 FY27 (A$112.7m) plus January to March 2026 (A$186.6m less A$129.3m) plus half of the July to December 2025 half (A$64.7m); PointsBet no longer reports quarters [P1, P5]. Both deal bases flatter PointsBet, because in 2025 it was guiding to positive EBITDA and now it loses money. A buyer of the stake is, in practice, only MIXI. So the stake is worth A$72m on the screen and perhaps A$80m to A$120m in a negotiated sale, with A$1.25 to A$1.30 as the ceiling that MIXI's own 2025 statements set (see the rules below).

### The wagering business
Peers. Tabcorp (ASX:TAH) is the only listed Australian bookmaker of size: A$2,110.9m market value at A$0.915 (6 November) plus A$533m of net debt including leases = A$2,643.9m; FY26 EBITDA before significant items A$431.7m; FY27 capital spending "up to $160m" [M2, T1]. PointsBet makes losses, so it has no EBITDA multiple; at A$0.745 it trades at about 1.2 times revenue, a price held up by a 5.85% free float and hopes of a MIXI buy-out, so I don't use it. Flutter (Sportsbet) and Entain (Ladbrokes, Neds) are listed abroad and much bigger; I didn't use them.

```
TAH EV 2643.9; EV/EBITDA 6.12; EV/(EBITDA-capex) 9.73
guidance 13: EBITDA after equity pay 8.3; M1 equity-ready 46.1; M2 -6.6; DCF 8.3
guidance 16: EBITDA after equity pay 11.3; M1 equity-ready 64.4; M2 22.5; DCF 48.1
guidance 19: EBITDA after equity pay 14.3; M1 equity-ready 82.8; M2 51.7; DCF 87.9
```
- Method 1, EV/EBITDA at Tabcorp's 6.12 times on guidance less A$4.68m of equity-settled pay, less A$4.9m of leases: A$46m, A$64m and A$83m at the bottom, middle and top of guidance. Tabcorp's EBITDA is flattered against Betr's because its Victorian licence payments sit below EBITDA [T1], so this method is generous to Betr.
- Method 2, value on cash earnings: Tabcorp's 9.73 times (EBITDA less capital spending) applied to Betr's EBITDA less equity pay less A$8.5m of development, less leases: minus A$7m, A$23m and A$52m. Betr spends a larger share of its EBITDA on its platform (about 75% at the middle of guidance after equity pay) than Tabcorp does (37%).
- Method 3, a simple discounted cash flow: FY27 cash earnings as above (guidance less equity pay, development and lease payments), EBITDA growing 10% a year for five years, development and leases growing 2.5%, no tax (Betr has losses), 2.5% growth after year five, discounted at 12%: A$8m, A$48m and A$88m. The input that moves it most is EBITDA growth: at the middle of guidance, 5% gives A$27m and 15% gives A$72m; a 10% discount rate instead of 12% adds about A$15m.

Range for the wagering business: about A$0m to A$88m, central A$48m (method 3) to A$64m (method 1). It depends mostly on whether the FY27 guidance is met and on whether development spending stays near A$8.5m a year as EBITDA grows.

### Betr, sum of the parts
Own cash A$7.4m, NAB loan A$34.1m, on 1,049.59m shares (the 27.6m performance rights would cut each figure by about 2.5%).
```
Nothing happens, PBH 0.745:
  g13 M1: 91.1 -> A$0.0868
  g16 M1: 109.5 -> A$0.1043
  g16 DCF: 93.2 -> A$0.0888
  g19 M1: 127.9 -> A$0.1218
  g19 DCF: 133.0 -> A$0.1267
bad 0.0781; middling 0.1043; good at 1.02 0.1296; at 1.25 0.1507; at 1.25 & top 0.1682
```
| Case | PointsBet price | Wagering | Betr a share |
| --- | --- | --- | --- |
| Nothing happens, bottom of guidance | A$0.745 | method 1 at A$13m | A$0.087 |
| Nothing happens, middle (central) | A$0.745 | method 1 at A$16m (method 3: A$0.089) | A$0.104 |
| Nothing happens, top | A$0.745 | method 1 at A$19m | A$0.122 |
| Stake sold at A$1.03 | A$1.03 | middle | A$0.130 |
| Stake sold at A$1.25 | A$1.25 | middle | A$0.151 |
| Stake sold at A$1.25 and top of guidance | A$1.25 | top | A$0.168 |

Range of value: A$0.087 to A$0.122 if nothing happens; A$0.130 to A$0.168 with a sale of the stake to MIXI. The fact sheet's A$0.166 is the very top of this table: MIXI's 2025 price and the top of guidance together.

## The players and what the rules allow
**MIXI Australia (MIXI, Inc., Tokyo, 2121).** 230,893,535 PointsBet shares (66.43%) since 12 September 2025, bought at A$1.25 for A$289m [P13, P19]; MIXI had about A$942m of cash at 30 June 2025 [P11]. Three of PointsBet's five directors are MIXI executives (the other two are the chair, Brett Paton, and the former CEO, Sam Swanell), and MIXI funds PointsBet through a A$23m loan facility [P14, P1]. Its stated intentions for the 50% to 90% case: board seats in proportion; a push to delist only if it held 75% to 90%; further purchases under the 3% creep; general compulsory acquisition if it ever reaches 90% [P9 s6.3]. It has done nothing about the minority since. What it can do:
- Creep 3% every six months (Corporations Act s611 item 9). Without Betr's shares the most it can ever reach is 72.28% (66.43% plus the 5.85% float) [calc].
- Delist: ASX normally needs a special resolution (75% of votes cast) outside the post-bid exception, and the bidder may vote only from 12 months after its bid closed, that is from 12 September 2026 [W1; P9 s6.3]. If Betr votes against, MIXI has 70.6% of the votes cast, or 72.3% if every float holder votes with it [calc]. Blocked.
- Compulsory acquisition (Part 6A.2) needs 90%: blocked while Betr holds.
- A scheme, or any share issue or asset deal with MIXI that needs the votes of non-MIXI holders (ASX Listing Rules 10.1 and 10.11, Corporations Act Chapter 2E): Betr holds about 83% of the shares MIXI doesn't. Blocked.
- A takeover bid for the rest at any price: always open. Its 2025 statements limit the price. MIXI called A$1.30 "Last and Final" and "will not be increased" [P11]; ASIC's policy is that such statements bind "as with a promise", and the Takeovers Panel treats a later increase as likely unacceptable [W2]. How long that binds a fresh bid after the first one closed I could not verify, but it makes A$1.25 to A$1.30 a practical ceiling.
- A pro-rata rights issue in PointsBet that MIXI underwrites, which needs no vote under s611 items 10 and 13 (the Takeovers Panel looks at the control effect). PointsBet needs money. If neither Betr nor the float took up their rights, about 119m new shares (34% of the register: A$89m at A$0.745, about A$48m at A$0.40) would lift MIXI to 75%, enough to carry a delisting vote; reaching 90% that way would need about 819m new shares, which is not realistic [calc]. Betr, with A$7.4m of its own cash, could not pay for its 27.72% of a raise of that size. Whether ASX Listing Rule 10.11 would also need a non-MIXI vote for MIXI's shortfall shares I have not settled.

**Betr.** 96,354,403 shares (27.72%) at an average cost of about A$1.19, carried at market (A$90.1m at 30 June 2026), and pledged to NAB [P4, A1, calc]. It can block compulsory acquisition, a scheme, delisting and related-party deals, and it is using its votes (the first strike in August 2026) [P5]. It can't appoint a director, can't force a sale, gets no dividend from a loss-making PointsBet, can't afford a rights issue, and must repay or refinance A$34.1m by 30 September 2027. If PointsBet falls below about A$0.59 the loan-to-value covenant breaks.

**PointsBet's board and NAB.** The board is MIXI's (P14). PointsBet is funded month to month by MIXI loans due within 12 months of each drawing, plus a support letter [P1]. NAB has extended Betr's loan twice and holds the PointsBet shares as security [A12, A1].

**Betr's own holders.** Tripp, Catherine Tripp and Sullivan hold about 28%, so nobody can buy Betr without them. A MIXI bid for Betr itself would take MIXI to 94.15% of PointsBet and let it compulsorily acquire the rest; Betr's own 2025 bidder's statement put the cost savings of combining betr and PointsBet at about A$44.9m a year [P11]. Nothing on file suggests MIXI wants betr's business: it called Betr's 2025 offer "materially inferior" [P11].

**Comparable case.** Seven Group in Boral (2024): a controller holding about 70% bid for the rest, called its offer "Best and Final" with stepped cash, then lifted the cash to the top step once the board agreed, crossed 90% and compulsorily acquired [W2]. Holders got the bid, but there was no single blocking holder, and the controller chose its moment. I found no cited Australian case of a single 25% to 30% blocker against a two-thirds controller to compare what the blocker received.

**Is there a forcing event, and when?** Not one that forces MIXI. PointsBet's funding gap is real, but MIXI can keep lending or underwrite a rights issue, both of which work against Betr. The only hard date is Betr's NAB maturity on 30 September 2027, and it works against Betr too: the closer it gets, the stronger MIXI's hand. PointsBet's 2027 AGM (about August 2027) could bring a second strike and a board spill vote, which MIXI would win.

## Why the market is wrong
It isn't, as far as I can tell. At A$0.125 the market is already paying for most of a good outcome. Taking the PointsBet stake at its last trade, the market values Betr's wagering business at about A$91m, 8.0 times the middle of guidance after equity pay and 6.4 times the top, against Tabcorp's 6.1 times; or, taking the wagering business at Tabcorp's multiple, it values the stake at about A$0.97 a PointsBet share, 30% above the screen price and close to what MIXI's own 2025 multiple gives on today's revenue [calc]:
```
mcap 131.2; implied wagering EV (pre-lease) 91.0 = 8.0x mid, 6.4x top
implied stake value if wagering at TAH multiple mid: 93.5 = A$0.970/PBH sh
```
For the price to be too low, MIXI would need to pay A$1.25 or more soon and the wagering business would need to reach the top of guidance. Neither has any date attached.

## Outcomes and chances
Resolve date 7 May 2027 (after the half-year result in late February and the March-quarter report in late April). This would be a special situation, not a value pick: the bad case is 38% below the price and the middling case 17% below it.

| Outcome | What happens | Chance | Price by resolve date |
| --- | --- | --- | --- |
| Bad | The half-year shows FY27 heading to the bottom of guidance or below (another weak racing or sport result, or the 1 January 2027 rules biting), PointsBet keeps falling (A$0.65) or raises equity at a discount, no deal | 35% | A$0.078 |
| Middling | Nothing happens with the stake; FY27 tracks the middle of guidance; PointsBet stays about A$0.745 | 55% | A$0.104 |
| Good | MIXI agrees to buy the stake or bids for the rest of PointsBet (or for Betr) at A$1.03 to A$1.25 a PointsBet share; wagering at the middle of guidance | 10% | A$0.140 |

Valuation figures used: bad, PointsBet at A$0.65 and method 1 at the bottom of guidance (A$0.078); middling, the central "nothing happens" value (method 1 at the middle, A$0.104; method 3 gives A$0.089); good, the stake at about A$1.14 (between A$1.03 and A$1.25) with the middle of guidance (A$0.140).

Why 10% for a deal: 14 months with no public move by MIXI; MIXI funds PointsBet with loans that avoid needing Betr; PointsBet is weaker than when MIXI paid A$1.25; and MIXI gains from waiting as Betr's loan maturity nears. Against that, Betr is spending on "strategic initiatives" and the stake does block MIXI's tidy-up.

Expected price: 0.35 x 0.078 + 0.55 x 0.104 + 0.10 x 0.140 = A$0.0985, 21% below A$0.125 before costs.

Round-trip costs on the largest position allowed (A$2,002, liquidity-capped, about NZ$2,483 at NZ$1 = A$0.8064 on 6 November [M4]): half the spread each way, 1.8% in all on the Corwin and Schultz estimate over 60 sessions, though one price step is 4.0% of the price and the quote on 6 November was two steps wide; size cost 0.83% each way (daily volatility 2.7% over 20 sessions, times the square root of A$2,002 over the A$21,428 average day), 1.7% in all; brokerage A$15 each way (0.75%) unless the plan's monthly cover applies, 0% to 1.5%; 0.5% each way to convert, 0% to 1.0%. That is 3.5% to 8.2%; I use 5.5%. **Expected return after costs: about -27%.**

Minimum gain (rulebook section 5a): the cash rate (2.13%) plus 5% a year over the 179 days from 9 November 2026 to 7 May 2027 is +3.5% (+6.4% to the NAB maturity on 30 September 2027). The case misses it by about 30 points.

How generous the chances would need to be: with a 25% chance of a sale at A$1.25 (A$0.151), 60% of nothing happening at the top of guidance (A$0.122) and only 15% of the bad case at the bottom of guidance with PointsBet unchanged (A$0.087), the expected price is A$0.124, still below the price before costs. With my chances, the price at which the expected gain after costs reaches the minimum is about A$0.090.

## Dated events
- 26 November 2026: Betr AGM (CEO equity, 10% placement capacity) [A6].
- 31 December 2026: first quarterly interest cover test on the NAB loan [A1].
- 1 January 2027: federal advertising and inducement limits start [A4].
- About 29 January 2027: Q2 FY27 quarterly report, covering the Spring Carnival (29 January 2026 last year) [A8].
- About 26 February 2027: Betr half-year result (26 February 2026 last year) [A9].
- From about March 2027: the first MIXI loan drawings to PointsBet fall due (each within 12 months of drawing; the first A$3m was drawn by 31 March 2026 under the 2 March 2026 agreement) [P1].
- About 30 April 2027: Q3 FY27 quarterly (30 April 2026 last year) [A10].
- After the window: PointsBet's full-year result (about mid-May 2027; 15 May 2026 last year) [P5]; PointsBet's 2027 AGM (about August 2027); NAB maturity 30 September 2027 [A1].

## What would make this wrong
The two things most likely to make "no case" the wrong call:
1. MIXI moves soon and pays the 2025 price, or bids for Betr itself. A sale at A$1.25 with guidance met at the top is worth A$0.168, 34% above the price; a bid for Betr at a premium could be worth more. PointsBet's funding need could push MIXI to clean up its register before putting in equity.
2. The wagering business is worth more than Tabcorp's multiple says. Betr's turnover is growing 15% to 19% a year against Tabcorp's 1%; if the October margin holds through Spring and the half-year shows FY27 at or above the top of guidance, 8 times EBITDA could be fair, and the market's price would then be about right with an option on the stake for free.

What would reopen it (any one of these, checked against a fresh look at the filings):
- A proposal, agreement or bid involving Betr's PointsBet stake, PointsBet as a whole, or Betr itself, from MIXI or anyone else. Then value it at the announced terms; a binding deal belongs in the deal sleeve.
- Betr's price at or below A$0.090 while PointsBet trades at or above A$0.745, with the half-year result (about 26 February 2027) showing H1 normalised EBITDA that keeps the A$13m to A$19m FY27 range intact and own cash not below A$7m at 31 December 2026.
- A PointsBet equity raising: read the terms and Betr's response, because it decides whether the blocking stake survives.
- An NAB refinancing or a sale of the stake before 30 September 2027.

For any future pick, the stake thesis itself breaks if PointsBet raises equity that Betr can't follow (the delisting veto goes once MIXI reaches 75%), or if PointsBet falls below about A$0.59, which breaks the loan-to-value covenant.

## Checks
- Excluded list: config/judgement_excluded.csv has no entries and records Cam's 8 November 2026 confirmation that Betr is not a conflict. Betr is a wagering company; it was opened on that confirmation, as the brief directs.
- No placement-pattern reopening in the last 30 sessions (21 September to 30 October 2026): Betr has had no trading halt since June 2025; the five opening gaps of 5% or more in that period were one or two price steps on normal volume, not reopenings after a halt [M3].
- Liquidity: median value traded A$10,009 a day over the 20 sessions 5 to 30 October 2026 (lowest A$95 on 9 October) [M3]. Two sessions at 10% is A$2,002, which binds below the 2.5% cap (A$2,016) and is barely above the A$1,500 smallest order.

## Sources
Betr Entertainment (ASX:BBT) announcements
- [A1] Appendix 4E and FY26 Annual Report, 27 Aug 2026 (03131301): review of operations, normalised EBITDA reconciliation, PointsBet investment note, NAB loan (note 17), issued capital (note 21), related parties, KMP shareholdings, shareholder information at 24 Aug 2026: https://announcements.asx.com.au/asxpdf/20260827/pdf/073b1mw9nffmzl.pdf
- [A2] betr FY26 Results, 27 Aug 2026 (03131305): https://announcements.asx.com.au/asxpdf/20260827/pdf/073b1xdcs5vqpb.pdf
- [A3] FY26 Results Investor Presentation, 27 Aug 2026 (03131313): https://announcements.asx.com.au/asxpdf/20260827/pdf/073b2gqllydf3c.pdf
- [A4] Q1 FY27 Quarterly Activities Report and Appendix 4C, 28 Oct 2026 (03158242): https://announcements.asx.com.au/asxpdf/20261028/pdf/075wfgq9zhm3n4.pdf
- [A5] betr Q1 FY27 Results and Trading Update, 28 Oct 2026 (03158255): https://announcements.asx.com.au/asxpdf/20261028/pdf/075wgct3k276y7.pdf
- [A6] Notice of Annual General Meeting, 26 Oct 2026 (03156876): https://announcements.asx.com.au/asxpdf/20261026/pdf/075rs48w2jhd01.pdf
- [A7] Trading Update and Share Buy-Back, 14 Jan 2026 (03049715): https://announcements.asx.com.au/asxpdf/20260114/pdf/06v7r7yt9nmzkd.pdf
- [A8] betr Q2 FY26 Results, 29 Jan 2026 (03053915): https://announcements.asx.com.au/asxpdf/20260129/pdf/06vpmp7db24zw5.pdf ; Q2 FY26 Quarterly Report and 4C (03053917): https://announcements.asx.com.au/asxpdf/20260129/pdf/06vpmtf521flvh.pdf
- [A9] Appendix 4D and Half Year Report, 26 Feb 2026 (03065567): https://announcements.asx.com.au/asxpdf/20260226/pdf/06wsv2hfcbj8ql.pdf ; 1H26 Investor Presentation (03065570): https://announcements.asx.com.au/asxpdf/20260226/pdf/06wsv8vk4fvww9.pdf
- [A10] Q3 FY26 Quarterly Report and 4C, 30 Apr 2026 (03088443): https://announcements.asx.com.au/asxpdf/20260430/pdf/06z1tl5vnjwrv8.pdf
- [A11] Q4 FY26 Quarterly Report and 4C, 30 Jul 2026 (03119872): https://announcements.asx.com.au/asxpdf/20260730/pdf/0726xc8qv29m39.pdf
- [A12] Extension of NAB Facility Agreement, 25 Feb 2026 (03065034): https://announcements.asx.com.au/asxpdf/20260225/pdf/06wrglsmr62273.pdf
- [A13] S&P DJI September 2026 Quarterly Rebalance, 4 Sep 2026 (03136141), All Ordinaries removals: https://announcements.asx.com.au/asxpdf/20260904/pdf/073rbz4q8nrckg.pdf
- [A14] Acquisition of Relevant Interest in PointsBet, 28 Apr 2025 (02941646): https://announcements.asx.com.au/asxpdf/20250428/pdf/06j3rv1lzwmjgr.pdf
- [A15] Proposal to acquire PointsBet; launch of A$130m equity raise, 29 Apr 2025 (02942142): https://announcements.asx.com.au/asxpdf/20250429/pdf/06j521lnxvr7kk.pdf
- [A16] Update on Offer Consideration and Selective Buy-Back, 26 Aug 2025 (02985891): https://announcements.asx.com.au/asxpdf/20250826/pdf/06ncszmvmzvysw.pdf
- [A17] Withdrawal of Resolution 3 (MIXI buy-back participation), 8 Sep 2025 (02992598): https://announcements.asx.com.au/asxpdf/20250908/pdf/06nz7m8cs4ts46.pdf
- [A18] Close of the Offer, 26 Sep 2025 (03000774): https://announcements.asx.com.au/asxpdf/20250926/pdf/06pqcwfk7rj65d.pdf
- [A19] Selective Buy-Back Booklet, 2 Oct 2025 (03004205): https://announcements.asx.com.au/asxpdf/20251002/pdf/06q0m6pq43vmkb.pdf
- [A20] Results of Selective Buy-Back, 20 Oct 2025 (03012096): https://announcements.asx.com.au/asxpdf/20251020/pdf/06qr864fsxrtw7.pdf
- [A21] Appendix 4E and FY25 Annual Report, 28 Aug 2025 (02987264), payments for investments A$72.5m and NAB loan: https://announcements.asx.com.au/asxpdf/20250828/pdf/06nh7qzr7gqksf.pdf
- [A22] Notice of EGM (Takeover Offer and Selective Buy-Back), 22 Aug 2025 (02983998), substantial holders table: https://announcements.asx.com.au/asxpdf/20250822/pdf/06n6d37gy63sg0.pdf
- [A23] BlueBet Notice of EGM, 30 Apr 2024 (02801659), consideration shares to the betr vendors including Bondi B Limited: https://announcements.asx.com.au/asxpdf/20240430/pdf/063193s832q331.pdf
- [A24] Becoming a substantial holder, Bondi B Limited, 2 Jul 2024 (02824529): https://announcements.asx.com.au/asxpdf/20240702/pdf/0655z7nq4zk1ym.pdf
- [A25] Change of Director's Interest Notices, M Tripp, 7, 12 and 20 Nov 2025 (03022318, 03024369, 03029348): https://announcements.asx.com.au/asxpdf/20251107/pdf/06rmzjdxgjfd25.pdf , https://announcements.asx.com.au/asxpdf/20251112/pdf/06rtzpvf3v6829.pdf , https://announcements.asx.com.au/asxpdf/20251120/pdf/06s87kwyqc42wz.pdf
- [A26] Substantial holder notices: Tanarra 1 Oct 2025 (03003786) https://announcements.asx.com.au/asxpdf/20251001/pdf/06pzfw2d6krcgq.pdf and 23 Oct 2025 (03014453) https://announcements.asx.com.au/asxpdf/20251023/pdf/06qyccfwcdqrvk.pdf ; Ellerston 30 Sep 2025 (03002912) https://announcements.asx.com.au/asxpdf/20250930/pdf/06px9tdg92vz8d.pdf ; Harvest Lane 23 Oct 2025 (03014484) https://announcements.asx.com.au/asxpdf/20251023/pdf/06qyfwd21s0p1j.pdf ; Host-Plus 24 Oct 2025 (03015337) https://announcements.asx.com.au/asxpdf/20251024/pdf/06r0m3tjhf32p2.pdf ; WAM 10 Apr 2026 (03081591) https://announcements.asx.com.au/asxpdf/20260410/pdf/06yckx7kslp734.pdf ; Australian Retirement Trust 5 May 2026 (03090537) https://announcements.asx.com.au/asxpdf/20260505/pdf/06z80vpyjn39br.pdf ; Regal 6 May 2026 (03091235) https://announcements.asx.com.au/asxpdf/20260506/pdf/06z9y4y7fb6nzk.pdf
- [A27] betr Board Update, 8 Oct 2025 (03006806): https://announcements.asx.com.au/asxpdf/20251008/pdf/06q82zmh8zdr58.pdf ; Appointment of CFO, 27 May 2026 (03097889): https://announcements.asx.com.au/asxpdf/20260527/pdf/07003gf45kdb8s.pdf
- [A28] Increased Takeover Offer for PointsBet, 30 Jul 2025 (02974536): https://announcements.asx.com.au/asxpdf/20250730/pdf/06m9y0ccx78xq8.pdf

PointsBet (ASX:PBH), MIXI and the Takeovers Panel
- [P1] PointsBet Appendix 4D and Half Year Interim Report to 30 Sep 2026, 30 Oct 2026 (03160412): review of operations, balance sheet, going concern, related parties and MIXI loan (note 17): https://announcements.asx.com.au/asxpdf/20261030/pdf/0761yb7x2sgxk9.pdf
- [P2] PointsBet H1 FY27 Results Presentation, 30 Oct 2026 (03160418): https://announcements.asx.com.au/asxpdf/20261030/pdf/0761yr6xgf5qhp.pdf
- [P3] PointsBet Trading Update H1 FY27, 13 Oct 2026 (03151638): https://announcements.asx.com.au/asxpdf/20261013/pdf/07580f2y4yf01h.pdf
- [P4] PointsBet 2026 Annual Report, 23 Jun 2026 (03106978), shareholder information at 19 Jun 2026: https://announcements.asx.com.au/asxpdf/20260623/pdf/070xtqqtc4k2b5.pdf
- [P5] PointsBet 2026 AGM Chairman and CEO Addresses (03129575): https://announcements.asx.com.au/asxpdf/20260825/pdf/0735m5z548j0br.pdf ; Results of 2026 AGM (03129780): https://announcements.asx.com.au/asxpdf/20260825/pdf/07364k2xd5w009.pdf ; FY26 Appendix 4E, 15 May 2026 (03094477): https://announcements.asx.com.au/asxpdf/20260515/pdf/06zmwsd2kpnfqc.pdf
- [P6] PointsBet Results of 2025 AGM, 28 Nov 2025 (03033814): https://announcements.asx.com.au/asxpdf/20251128/pdf/06snf1t5g6ydh4.pdf
- [P7] PointsBet enters Scheme Implementation Deed with MIXI, 26 Feb 2025 (02918856): https://announcements.asx.com.au/asxpdf/20250226/pdf/06fy9ywcpqjq29.pdf ; Improved MIXI Proposal, 3 Jun 2025 (02954953), including the independent expert's A$0.96 to A$1.11 range: https://announcements.asx.com.au/asxpdf/20250603/pdf/06kdb2v8cyqswh.pdf
- [P8] Updated Scheme Meeting Results, 26 Jun 2025 (02962231): https://announcements.asx.com.au/asxpdf/20250626/pdf/06l3xqxylts0nc.pdf ; MIXI Announces Recommended Takeover Offer, 26 Jun 2025 (02962286): https://announcements.asx.com.au/asxpdf/20250626/pdf/06l41ll0vxvqtb.pdf
- [P9] MIXI Australia Bidder's Statement, 17 Jul 2025 (02970242), section 6 intentions: https://announcements.asx.com.au/asxpdf/20250717/pdf/06lwp8yc4ryvs6.pdf
- [P10] PointsBet Recommends Increased MIXI Offer, 8 Aug 2025 (02978390): https://announcements.asx.com.au/asxpdf/20250808/pdf/06mnyp5d56ktt0.pdf
- [P11] MIXI Australia, Last and Final Offer, 21 Aug 2025 (02983394), including MIXI's A$942m cash and its quote of Betr's A$44.9m synergy estimate: https://announcements.asx.com.au/asxpdf/20250821/pdf/06n4rtg94kl1vw.pdf
- [P12] MIXI Australia Exceeds 50%, 29 Aug 2025 (02988577): https://announcements.asx.com.au/asxpdf/20250829/pdf/06nlfp5wk5zvlb.pdf
- [P13] PointsBet distribution schedule and top 20 after both offers closed, 30 Sep 2025 (03002522): https://announcements.asx.com.au/asxpdf/20250930/pdf/06pwdxnynyz453.pdf
- [P14] Reconstitution of PointsBet Board, 6 Oct 2025 (03005733): https://announcements.asx.com.au/asxpdf/20251006/pdf/06q5592xjg0xfr.pdf
- [P15] Change to Financial Year End, 12 Dec 2025 (03040283): https://announcements.asx.com.au/asxpdf/20251212/pdf/06t7svrqllwtmg.pdf ; Transition of Group CEO, 17 Dec 2025 (03042024): https://announcements.asx.com.au/asxpdf/20251217/pdf/06tf4v9b81s7zy.pdf
- [P16] AGCO Notice, PointsBet Canada, 13 Feb 2026 (03060061): https://announcements.asx.com.au/asxpdf/20260213/pdf/06w8sf2d1d71gq.pdf
- [P17] Takeovers Panel media release TP25/081, Variation to Undertaking, 8 Sep 2025 (02992289): https://announcements.asx.com.au/asxpdf/20250908/pdf/06nyh1pyjq0scy.pdf
- [P18] Takeovers Panel, PointsBet Holdings Limited 02 [2025] ATP 26, reasons: https://takeovers.gov.au/sites/takeovers.gov.au/files/2025-11/2025-ATP-26.pdf
- [P19] MIXI news release on the close of the PointsBet offer period, 16 Sep 2025: https://mixi.co.jp/en/news/2025/0916/53061/

Tabcorp
- [T1] Tabcorp Holdings FY26 Results ASX Release, 26 Aug 2026 (03130173): EBITDA before significant items, net debt including leases, FY27 capex: https://announcements.asx.com.au/asxpdf/20260826/pdf/07377mkd9gr34q.pdf

Market data
- [M1] data/research_data/asx_company.json, BBT header and key statistics (fetched 7 Nov 2026 UTC): last A$0.125, bid A$0.115, ask A$0.125, 1,049,587,762 shares.
- [M2] ASX company data (asx.api.markitdigital.com/asx-research/1.0/companies/pbh and /tah, header and key statistics), read 8 Nov 2026 NZ time: PBH last A$0.745, 52-week A$0.715 to A$1.12, 347,586,582 shares; TAH last A$0.915, market value A$2,110.9m.
- [M3] data/norgate/universe/prices_2021.csv.gz to prices_2026.csv.gz (Norgate), BBT and PBH daily prices and volumes to 30 Oct 2026.
- [M4] data/fx/fx_daily.csv, NZ$1 = A$0.806387 on 6 Nov 2026.

Secondary sources (named because no primary source was reachable)
- [W1] Herbert Smith Freehills Kramer, "Delisting following a takeover bid", April 2024 (summary of ASX Guidance Note 33): https://www.hsfkramer.com/insights/2024-04/delisting-following-a-takeover-bid
- [W2] Clayton Utz, "Market dynamics prevail over blackletter principles in SGH / Boral 'Best and Final' takeover offer", June 2024 (quoting ASIC RG 25 and Takeovers Panel GN 1): https://www.claytonutz.com/insights/2024/june/market-dynamics-prevail-over-blackletter-principles-in-sgh-boral-best-and-final-takeover-offer
- [W3] The Straight, "POCT powered: state governments bank over $10 billion in gambling taxes in 2025/26", 25 Jun 2026: https://thestraight.com.au/poct-powered-state-governments-bank-over-10-billion-in-gambling-taxes-in-2025-26/
- [W4] Not read: AFR, "Betr shakes off News Corp past and joins ASX in merger with BlueBet" (fetch failed); Ashurst on truth in takeovers (access not granted); the full text of ASIC RG 25 and ASX Guidance Note 33; MIXI's own quarterly results documents (the summaries found, on quartr.com and webull.com, don't mention the PointsBet minority).
