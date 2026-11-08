# G8 Education (ASX:GEM): deep dive. Wait for a named event: the CY26 result (about 23 February 2027). At A$0.105 my expected price of A$0.11 is 5% above the price before costs and 2.5% below it after them, short of the 3.4% minimum. Not a value pick

Written 2026-11-08 by the research desk. Price at writing: A$0.105 (last trade on Friday 6 November 2026, bid A$0.100, ask A$0.105, ASX company data in data/research_data/asx_company.json, fetched 7 November 2026 UTC [D1]; Norgate's last close in the repo is A$0.100 on 30 October [D2]). Market value: A$79.4m (756,618,193 shares on issue, half-year report note 11 and the Appendix 3H of 3 November 2026 [G1, G12]).
Status: finished. Verdict: wait for a named event (the CY26 result, about 23 February 2027, which reports early-2027 occupancy, the 31 December 2026 covenant and goodwill tests and the CY26 earnings); the exact conditions that reopen it, including a price trigger of a close at or below A$0.095, are under "Dated events". No card, no red team. This is a simulation and not financial advice.
Fact sheet: research/facts/GEM.md (2 November 2026, earlier template), grade A. Its question: has occupancy stopped falling at 57%, and is the equity worth anything if it settles there instead of returning to the 65.8% the goodwill test assumes by 2030? Its range: +507% (A$0.61) against -100% (A$0.00), at A$0.10.

Value pick (rulebook section 5a, from 8 November 2026): no. My bad case (A$0.04) is 62% below the price, against a limit of 10%, and my middling case (A$0.09) is 14% below it, against a need for 15% above. The equity is a thin slice on top of A$613m of leases and A$128m of bank debt, so no outcome where occupancy keeps falling can sit within 10% of the price. It could only ever be an ordinary pick with a dated event inside six months; the CY26 result is that event.

Order of work. The brief and the fact sheet both quote the price, so it was in view from the start. "What the filings show" and "Valuation" are worked from G8's filings and the listed peers' filings and prices; G8's own price enters only in "Why the market is wrong", "Outcomes and chances" and the checks. Arithmetic was run in `python3 -I` from a scratch script (gem_calc.py, not committed); the lines that matter are shown below.

> In short: the fact sheet's two anchors are both off the measure the market uses. Childcare operators are priced on earnings before interest, tax, depreciation and amortisation after paying rent (what the industry calls pre-AASB16 EBITDA; "EBITDA after rent" below), against bank debt. On that measure G8 made A$125.7m in CY25, A$100.8m in the year to June 2026 and A$30.9m in the first half of 2026. The listed peers trade at 3.4 times (Embark) and 6.6 times (Nido), and Nido bought four centres in April 2026 at 4.8 times. My CY26 estimate is A$84m to A$91m (operating EBIT A$51m to A$58m, above the fact sheet's A$41.7m because the second half of 2025 already carried the Point Cook shock, the A$10m of savings start in the second half, and the 40 suspended centres' losses and rent leave operating earnings). If occupancy holds at this year's level, CY27 EBITDA after rent is about A$94m and the equity is worth about A$0.17 to A$0.29 a share at 3.5 to 4.5 times and A$0.18 to A$0.25 on cash flow (about A$0.18 to A$0.20 in the middle); if it falls another 3 points, about A$0.06 to A$0.18 (A$0.08 to A$0.09 in the middle); another 6 points, about nil to A$0.06. Each point of occupancy is worth about A$6.5m of EBITDA after rent, about 3 to 4 cents a share. At A$0.105 the market pays about 3.0 times the flat-occupancy view, which is roughly where a further 3-point fall at a peer-like 3.5 to 4 times would put it. Whether occupancy has stopped falling is not yet shown: the year-on-year gap narrowed from 7.5 points in February to 5.1 points in August, but the August figure excludes the 40 suspended centres (which ran at about 33% occupancy), the first-half decline on the same centres was 7.7 points, and the June quarter 2026 government data still had more centres and fewer children than a year earlier. Covenant thresholds are not disclosed anywhere I could read; on the usual definitions the fixed charge cover was about 1.8 times at June and about 1.6 to 1.7 times at December 2026 on my estimate, which fits the lenders having loosened that test to December 2027. With chances of 25% bad, 45% middling and 30% good, the expected price by 30 April 2027 is A$0.11, so there is no case at A$0.105 once a one-tick spread of 4.9% is paid. Below A$0.10 the ASX tick falls to A$0.001 and costs drop to about 3.9%, so a close at or below A$0.095 would reopen it.

Corrections to the fact sheet, for the record:
1. Price and value: the latest trade is A$0.105 on 6 November 2026 (market value A$79.4m), not A$0.10 on 30 October [D1].
2. The good-case anchor (A$0.61) applies 9.09 times (the inverse of G8's 11% pre-tax discount rate) to operating EBIT, which is after rent. G8's 11% is a weighted cost of capital whose "cost of debt is based on the interest-bearing borrowings of the Group and the lease portfolio of the Group" [G4 note 17], used on cash flows before rent and compared with carrying amounts that include the right-of-use assets [G1 note 7(a)]. Using it on after-rent earnings overstates value. It also leaves out the suspended centres' leases (about A$40m, my estimate below) and assumes a return to 2025 occupancy, which the company's own test dates to 2030. On peers' multiples a full return to 2025 earnings is worth about A$0.50 to A$0.59, but that is a long-run good case, not a middling one inside 24 months.
3. The bad-case anchor (A$0.00) starts from a CY26 run rate of A$41.7m that assumes the second half falls by the same A$25.8m as the first. The second half of 2025 (A$52.8m) already included the July 2025 Point Cook shock, the savings start in the second half, and the suspended centres' trading losses and rent are now outside operating earnings. My bottom-up estimate is A$36.5m to A$43.4m for the second half (A$51m to A$58m for the year). A near-nil equity is right for a further 6-point fall, but not for "occupancy stays at 57%".
4. "Spot occupancy 61.9%, down 5.1 points" (21 August 2026) is for the 350 operating centres, excluding the 40 suspended ones; the presentation doesn't say whether the comparison year is on the same centres [G3]. The first-half decline on the same centres was 7.7 points (59.7% against 67.4%), not 7.5 [G1, directors' report]. Removing centres that ran at about 33% lifts the group figure by about 2.7 points on its own (arithmetic under "What the filings show").
5. Allan Gray's last notice (153,329,172 shares, 19.87% of 771.6m then quoted) is 20.27% of the 756,618,193 shares on issue after the 3 November 2026 cancellation of 14,940,562 bought-back shares; Soul Patts' 74,532,158 shares are 9.85% [G12, G15, G4 shareholder information]. Neither has filed since February 2026.
6. G8 left the S&P/ASX 300 and the All Ordinaries before the open on 21 September 2026 [G13]. The fact sheet doesn't mention it.
7. The Department of Education's June quarter 2026 data was already out by 23 September 2026 (centre-based day care services 9,963, up 279 or 2.9% on a year earlier, with fewer children than a year earlier, as reported by The Sector [S2]); the fact sheet lists the next release as about December 2026, which is the September quarter.
8. The Fair Work Ombudsman case is small: it alleges A$1.03m of underpayments and seeks A$1.045m of compensation (more than A$2m combined) for more than 1,400 workers from June 2020 to July 2022, plus penalties; no first court date had been listed at 8 July 2026 [S1]. G8 holds A$21.5m of regulatory, legal and other provisions [G1 note 10]. The larger unpriced legal tail is civil claims by Point Cook families, which a law firm said in July 2025 it was preparing [S4]; G8 lists the matter as a contingent liability with uncertain outcomes [G1 note 14].

## The company in plain words
G8 runs long day care centres in Australia: 350 operating centres at 30 June 2026 (NSW 128, Victoria 115, Queensland 54, WA 33, SA 20) under 21 brands, with about 6,900 centre team members and more than 29,000 children enrolled, plus 40 centres whose operations were suspended between April and June 2026; four of those had been sold or their leases ended by 30 June and two more by 1 August [G1, page 2 and notes 4 and 17]. At the end of 2025 it had 395 centres and 33,032 licensed places [G4, page 3]. It owns almost no property: the centres are leased (right-of-use assets A$435.3m, lease liabilities A$613.3m at 30 June 2026) [G1 note 6].

Where the money comes from: childcare fees, a large part paid directly by the federal Child Care Subsidy, and state funding for kindergarten programs. In the first half of 2026 revenue was A$409.0m, of which A$397.6m was centre revenue and A$11.4m program funding [G1 note 2]. The main costs are centre wages (61.2% of centre revenue in the half), rent (14.7% on G8's "rent proxy" of lease depreciation, lease interest and outgoings) and other centre costs [G3, page 20]. Since December 2024 the federal Worker Retention Payment has funded wages 15% above the award; the grant now runs to 30 June 2028 and caps fee increases for operators that take it [G1 note 7, G2]. The business is seasonal: children leave for school each February and occupancy rebuilds through the year, so the second half makes most of the profit [G1 note 2(b)].

Who runs it: Pejman Okhovat, chief executive since January 2023 (formerly managing director of BIG W and chief executive of The Warehouse) [G4]; Steven Becker, CFO since January 2025; Debra Singh, chair. A chief operating officer was appointed in June 2026, and Anne Lockwood replaced Peter Trimble as audit and risk chair from 21 October 2026 [G14].

Who owns it: 15,235 holders at 16 February 2026; the top 20 held 73.28%, almost all custodians (HSBC 18.69%, Citicorp 17.98%, JPMorgan 17.10%, WHSP Holdings 9.85%, BNP agency lending 3.45%), with chief executive Okhovat the 13th largest at 1,688,012 shares [G4, shareholder information]. Substantial holders now: Allan Gray about 20.27% of the current share count and Soul Patts 9.85% (correction 5). The other seven listed in February 2026 (Macquarie, Host-Plus, Australian Retirement Trust, Dimensional, Vanguard, Vinva, State Street) have all gone below 5% since, as has Tanarra, and Citigroup, JPMorgan and UBS moved in and out around 5% in September (fact sheet section 4, which I didn't re-open beyond Allan Gray). Directors bought on market: Julie Cogin 50,000 shares for A$8,500 on 6 May 2026 [G16] and 25,000 in February; no sales.

Five years [G4 remuneration report, G5, G1]:

| A$m | CY21 | CY22 | CY23 | CY24 | CY25 | H1 CY26 |
| --- | --- | --- | --- | --- | --- | --- |
| Revenue | 878.7 | 905.2 | 987.0 | 1,021.8 | 948.2 | 413.6 |
| Operating EBIT (after lease depreciation and lease interest) | 80.1 | 80.3 | 100.7 | 115.0 | 93.3 | 14.7 |
| Operating profit after tax | 39.5 | 45.7 | 63.4 | 72.4 | 59.0 | 6.7 |
| Statutory profit after tax | 45.7 | 36.6 | 56.1 | 67.7 | -303.3 | -38.8 |
| Group occupancy | | | | 70.7% | 65.8% | 57.0% |
| Share price at period end (A$) | 1.11 | 1.11 | 1.18 | 1.31 | 0.69 | 0.14 |

The price was A$0.685 on 2 January 2026, A$0.38 on the day of the full-year result (23 February), A$0.17 after the April trading update and A$0.095 on 18 September before the index exit; its 2026 low was A$0.088 on 20 October [D2].

## Why big investors may be overlooking it
- Index exit: G8 left the S&P/ASX 300 and the All Ordinaries on 21 September 2026 [G13], so index funds had to sell. Vanguard went below 5% on 21 July 2026, and custodian banks crossed 5% for a few days at a time in September (fact sheet section 4). Reported short positions were 6.3% of shares in mid-September and 1.4% by 26 October [D3], which looks like the index-deletion trade closing.
- Size: at A$79.4m it is below most institutions' minimum size, and a single-tick spread is 4.9% while the price is between A$0.10 and A$0.105.
- A messy year: a former employee charged in July 2025 with offences against children at the Point Cook centre, with more charges in December 2025 [G17]; a A$349.1m goodwill write-down; centre suspensions; a Fair Work Ombudsman case; the covenant amendment.
- An out-of-favour sector: Nido withdrew its 2026 target in August [P1]; Mayfield cut guidance, raised A$3m at A$0.10 in August and now trades at A$0.12, 76% below the A$0.50 Embark offered in December 2025 [P11, P13, P14].
- It is not unknown. Search results show broker coverage (Macquarie's July 2025 downgrade was reported by the Motley Fool and Capital Brief) and an aggregator page citing about a dozen analysts cutting price targets [S5]; I did not open or verify those. Two large value holders (Allan Gray, Soul Patts) bought heavily in late 2025 and early 2026 at much higher prices.

So the register and the index exit explain some selling pressure, but most of the fall is the business: occupancy down 13.7 points in two years.

## What the filings show

### Earnings after rent
G8's "operating EBIT" is after lease depreciation and lease interest [G6, page 18, footnote 2], so adding back only the depreciation of plant and software gives EBITDA after rent, the measure the peers report:

| A$m | CY24 | H1 CY25 | H2 CY25 | CY25 | H1 CY26 | Year to June 2026 |
| --- | --- | --- | --- | --- | --- | --- |
| Operating EBIT | 115.0 | 40.5 | 52.8 | 93.3 | 14.7 | 67.5 |
| Plus non-lease depreciation and amortisation | 32.4 | 15.3 | 17.1 | 32.4 | 16.2 | 33.3 |
| EBITDA after rent | 147.4 | 55.8 | 69.9 | 125.7 | 30.9 | 100.8 |
| Lease depreciation plus lease interest (accounting rent) | 116.7 | 60.5 | 55.0 | 115.5 | 52.5 | 107.5 |
| EBITDA before rent | 264.1 | 116.3 | 124.9 | 241.2 | 83.4 | 208.3 |
| Occupancy | 70.7% | 64.5% | about 67% | 65.8% | 57.0% | |

Sources: CY25 depreciation of plant A$31.7m, software A$0.7m, right-of-use A$74.1m, lease interest A$41.5m [G4 note 5, note 18]; H1 CY25 total depreciation A$53.3m of which right-of-use A$38.0m [G10 notes 5 and 6]; H1 CY26 total A$48.7m of which right-of-use A$32.5m, lease interest A$20.4m of which A$0.4m on suspended centres is outside operating earnings [G1 notes 3 and 6]; CY24 depreciation of plant A$31.1m and software A$1.3m [G4 note 5]. Half-year occupancy: CY24 68.2% and 73%, CY25 64.5% and 67% [G6, page 14; G11].

Cash rent runs slightly above accounting rent this year: lease payments were A$55.5m in the first half against A$52.9m of lease depreciation and interest [G1 note 6], partly because the 36 suspended centres' leases are still paid while their rent is now booked outside operating earnings.

### How much an occupancy point is worth
Centre revenue was A$7.16m per occupancy point per half in H1 CY25 and A$7.18m in H1 CY26 (A$462.1m at 64.5%, A$409.0m at 57.0%) [G3, page 20]. Centre EBIT fell A$26.9m on A$53.1m less revenue, 51% of each lost dollar. EBITDA after rent fell from A$55.8m to A$30.9m for 7.5 points: A$3.3m per point per half, about A$6.6m a year. From CY24 to CY25 the fall was A$4.4m a year per point, because cost savings and fee rises offset part of it. I use A$6.5m a year per point.

The seasonal step is large: operating EBIT rose from the first half to the second by A$35.3m in CY23 and A$36.2m in CY24 (when occupancy rose from 68.2% to about 73%), but only A$12.3m in CY25 (64.5% to about 67%) once the Point Cook news broke in July 2025 [G4, G6, G11].

### Occupancy, as reported

| Date | Spot | Change on a year earlier | Year to date | Change | Centres | Source |
| --- | --- | --- | --- | --- | --- | --- |
| 15 Feb 2026 | 54.4% | -7.5 | 57.2% | -7.8 | all | [G5] |
| 24 Apr 2026 | 56.4% | -7.0 | 56.1% | -7.9 | all | [G8] |
| H1 CY26 | | | 57.0% | -7.5 | all | [G1] |
| H1 CY26 | | | 59.7% | -7.7 | excluding the 40 suspended | [G1] |
| end of July 2026 | | | 58.0% | -7.0 | not stated | [G3] |
| 21 Aug 2026 | 61.9% | -5.1 | | | 350 operating | [G3] |

If the 40 suspended centres held about the same share of places as their share of the roughly 390 centres, their first-half occupancy was (57.0 - (350/390) x 59.7) / (40/390) = 33.4%, and leaving them out lifts the group figure by about 2.7 points. If the August comparison year includes those centres, the like-for-like gap in August is still about 7 to 8 points; if it is on the same 350 centres, the gap really has narrowed by about 2.6 points. The filings don't say which. Management's own words: conditions "to remain similar to the first half"; "seasonal patterns remain similar to last year, albeit at a lower level"; "small trend improvement since June YTD"; enquiries "remain lower than PCP"; conversion up 2 points to 32% [G2, G3, pages 14 and 23].

### The sector
- Demand: children in centre-based day care fell 2.8% in the year to March 2026 (Department of Education data cited by G8 and Nido) [G2, P1]. The June quarter 2026 report had 783,860 children, fewer than a year earlier, and 9,963 services, up 279 (2.9%) [S2; the Department's own page blocked automated reading, S3].
- Supply: long day care services counted by the national regulator rose 2.5% to 9,705 in the year to the June quarter 2026, the slowest growth in 10 quarters [G3, page 14; P1].
- Peers: Embark says occupancy growth since May 2026 is "materially higher than PCP", and centre EBITDA for the week ending 16 August 2026 was above the same week of 2025 [P7]. Nido's days of learning fell 4% in the first half (434,000 against 453,000), its offers of enrolment are about 17% ahead of last year, and it withdrew its 2026 target [P1]. Mayfield's spot occupancy was 56% in early October 2026, down from 59% [P14].

### Cash, debt and leases
- CY25: operating cash flow A$168.0m, lease principal A$66.3m, capital spending A$51.0m plus A$0.7m software, centre exit and surrender payments A$12.7m, dividends A$43.0m and buy-backs A$42.6m; borrowings rose A$41.0m [G4 cash flow statement].
- H1 CY26: operating cash flow A$49.5m (including a A$1.4m tax refund, against A$21.0m of tax paid a year earlier), lease principal A$35.1m, capital spending A$24.4m, exits A$0.5m: minus A$10.5m before financing; borrowings rose A$9.6m [G1 cash flow statement]. Capital spending for CY26 is guided at about A$50m [G3, page 23]. No dividend for the half and the buy-back has ended [G2].
- At 30 June 2026: cash A$36.4m; drawn A$160.0m of A$200.0m revolving facilities plus A$4.6m of insurance premium funding; net bank debt A$128.2m (A$123.6m on G8's definition, which leaves out the insurance funding) [G1 note 9, G3 page 28]. Facilities: A$100m to January 2029 (extended from December 2027 on 7 July 2026), A$100m and a A$40m guarantee line to December 2029 [G7, G1 note 9]. Contracted interest on the debt over the next 12 months is A$10.9m [G1 note 8].
- Leases: A$613.3m (A$73.0m current); A$795.3m of undiscounted payments, A$110.3m due within 12 months [G1 notes 6 and 8]. That is 5.8 times this year's accounting rent, a short average remaining term.
- Provisions: regulatory, legal and other A$21.5m (wage remediation, the Fair Work case, legal claims); onerous contracts A$11.1m for the suspended centres; make-good A$13.2m; employee benefits A$56.2m [G1 note 10]. Current liabilities exceed current assets by A$175.3m [G1 note 1(b)].
- Suspended centres' leases: interest on them was A$0.38m in the half [G1 note 3(c)]. At a lease rate of about 6.4% (A$40.8m a year on an average A$639m), that is about A$36m of lease liability if the interest covered two months; I use A$40m. Their rent is outside operating earnings, so I count these leases as debt.
- Book value: goodwill A$697.1m against equity of A$486.4m; net tangible assets minus 43 cents a share [G1].

### The goodwill test
At December 2025 the test used an 11% pre-tax discount rate, 2% terminal growth and full support-office costs [G4 note 17]. At 30 June 2026 it passed assuming occupancy returns to 2025 levels by 2030, and it would fail with a 0.7-point higher discount rate, a 0.5-point lower growth rate or 4% less EBITDA in 2030 [G1 note 7]. It assumes the Worker Retention Payment keeps funding wages 15% above the award, or that fees and wages adjust to the same net result [G1 note 7]. With a market value of A$79m against A$486m of book equity, another write-down at December 2026 looks likely; it is non-cash, but it matters for the gearing covenant (below).

### Covenants
The bank facility tests three ratios at every half-year and year end: net leverage, fixed charge cover and gearing [G1 note 9, G4 note 20]. No filing I read gives the thresholds or exact definitions (the half-year and annual reports, the July 2026 debt announcement and G8's published treasury policy [G19]). What the filings do say: G8 met all covenants at June 2026 and forecasts it will for at least 12 months from 25 August 2026, so through the December 2026 and June 2027 tests; the fixed charge cover covenant "was reduced up to and including the 31 December 2027 testing point" as part of the July 2026 extension [G1 note 9]; and the February 2026 A$350m write-down "will not impact the Company's financial covenants" [G9].

On the usual definitions (fixed charge cover = EBITDA after rent plus rent, divided by rent plus net interest; net leverage = net bank debt over EBITDA after rent):

| Test date | EBITDA after rent | Rent | Net interest | Fixed charge cover | Net leverage |
| --- | --- | --- | --- | --- | --- |
| Dec 2025 | 125.7 | 115.5 | 7.4 | 1.96x | 0.93x |
| Jun 2026 (12 months) | 100.8 | 107.5 | 8.4 | 1.80x | 1.23x |
| Dec 2026, my range | 84 to 91 | 105 | 10.5 | 1.63x to 1.69x | 1.4x to 1.5x |
| Dec 2026 if A$75m | 75 | 105 | 10.5 | 1.56x | 1.7x |
| Dec 2026 if A$60m | 60 | 105 | 10.5 | 1.43x | 2.1x |

Fixed charge cover reaches 1.75 times at EBITDA after rent of A$97m, 1.5 times at A$68m, 1.4 times at A$57m and 1.3 times at A$45m. If the original level was around 1.75 times, December 2026 would have failed it on my estimate, which fits the lenders loosening it to December 2027. A loosened level of 1.3 to 1.4 times leaves room for EBITDA after rent to fall to about A$45m to A$57m, roughly 4 to 6 occupancy points below this year. Net leverage is not close on any common limit (2.5 to 3 times). Gearing (net debt over net debt plus equity) was 20% [G3, page 28]; a further A$200m write-down takes it to 30%, A$350m to 48%, and a write-down of A$363m would take it to 50%. Whether gearing is tested on book equity after write-downs is not disclosed. These are my calculations on assumed definitions; the thresholds are the main thing I couldn't verify.

## Valuation
Two methods, both on earnings after rent and with debt-like items counted: (1) enterprise value over EBITDA after rent, the way the listed operators report and the way Nido prices its purchases; (2) free cash flow to equity after rent, capital spending, interest and tax. A lease-adjusted check follows. The value per share comes from the business and the peers' prices, not from G8's price.

### The peers on the same measure (prices 6 November 2026 [D1])

| | Market value | Net bank debt | Enterprise value | EBITDA after rent, 12 months to June 2026 | Multiple | Leases | Lease-adjusted multiple | Leases over annual rent |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nido (NDO), A$0.25 | 56.7 | 40.1 | 96.8 | 14.8 | 6.6x | 196.6 | 7.5x | 8.1x |
| Embark (EVO), A$0.39 | 83.3 | net cash 12.2, Mayfield stake 6.6 | 64.5 | 19.1 | 3.4x | 117.9 | 6.1x | 11.0x |
| Nido's purchase of 4 services, April 2026 | | | 9.1 | 1.9 (annualised) | 4.8x | | | |

Nido: 226,928,885 shares; borrowings A$46.8m and cash A$6.7m at 30 June 2026; adjusted EBITDA (before AASB16 and stamp duty) A$17.0m in 2025, A$6.6m in H1 2025 and A$4.3m in H1 2026; rent A$22.6m, A$11.2m and A$12.9m [P1, P2, P3]. A$18m of Nido's borrowing funds a loan to its incubator partner, repayable by October 2029 [P1]; counting it as an asset would lower Nido's multiple to about 5.3 times. Embark: 213,661,284 shares after its August placement at A$0.40 [P9]; net cash A$12.2m on 28 August 2026 [P7]; 55,216,247 Mayfield shares [P10] at A$0.12; underlying EBITDA after rent A$21.3m in 2025, A$9.0m in H1 2025 and A$6.75m in H1 2026, down 25% [P7, P8]. Nido's April purchase was A$9.1m for four services from its own incubator program, 348 places, A$1.9m of estimated annualised EBITDA before AASB16, about A$26,000 a place [P4]; it is a pre-agreed purchase from a partner, not a market sale. Embark's occupancy is higher than G8's (80% spot at its 30 better centres in August; nine others weaker [P7]); Nido's incubated services were at 52% spot [P1]. Both had falling earnings in the half.

G8 against the peers on the lease-adjusted check: at A$0.105, (A$79.4m + A$128.2m + A$32.6m of provisions + A$613.3m of leases) / A$208.3m = 4.1 times. That flatters G8, because its leases are only 5.8 times a year's rent against 8.1 and 11.0 times at the peers; the rent beyond the lease term is still paid if the centres stay open. Capitalising G8's rent at Nido's 8.1 times adds about A$244m and gives 5.3 times, a little below Embark's 6.1 and Nido's 7.5. So the lease-adjusted view says G8 is cheap but not wildly so, and I rely on method 1.

### Earnings to value
CY26 estimate (continuing centres). The second half is built from the first: like-for-like occupancy from 59.7% to about 62.5% (the 21 August spot was 61.9%), priced at the CY25 seasonal rate (A$12.3m per 2.5 points) or the CY23-24 rate (about A$7.4m per point per half), giving A$13.8m to A$20.7m; plus half a year of the "at least c$10m, annualised" savings [G3, page 7], A$5m; plus the suspended centres' trading losses and rent leaving operating earnings, about A$3m. H2 operating EBIT A$36.5m to A$43.4m, CY26 A$51.2m to A$58.1m, EBITDA after rent A$83.7m to A$90.6m. Cross-check from the other side: H2 CY25 A$52.8m less 6.5 like-for-like points at A$3.3m, plus A$5m of savings and A$5m for the suspended centres, gives A$41.3m.

CY27 if occupancy stays at this year's level: first half A$14.7m + A$5m savings + A$4.5m for the suspended centres = A$24.2m; second half A$39.9m (the middle of my range); less A$3m for wage and rent rises not passed on in fees (fees are near the subsidy's hourly cap: the national average was 3 cents below it in June 2026 [S2]). Operating EBIT A$61.1m, EBITDA after rent A$94.1m. Each point of occupancy is A$6.5m.

Debt and debt-like items: net bank debt A$128.2m + suspended centres' leases about A$40m + regulatory and legal provisions A$21.5m + onerous contracts A$11.1m = A$200.8m. (The second half is usually cash-positive, so December net debt may be A$5m to A$15m lower; I leave it at June's figure.)

Method 1: enterprise value at a multiple of CY27 EBITDA after rent, less A$200.8m, per share:

| CY27 occupancy against 2026 | EBITDA after rent | 3.0x | 3.5x | 4.0x | 4.5x | 5.0x |
| --- | --- | --- | --- | --- | --- | --- |
| 6 points lower | 55.1 | 0.00 | 0.00 | 0.03 | 0.06 | 0.10 |
| 3 points lower | 74.6 | 0.03 | 0.08 | 0.13 | 0.18 | 0.23 |
| the same | 94.1 | 0.11 | 0.17 | 0.23 | 0.29 | 0.36 |
| 3 points higher | 113.6 | 0.19 | 0.26 | 0.34 | 0.41 | 0.49 |

The range of multiples is the peers': Embark 3.4 times, Nido's purchase 4.8 times, Nido trading 6.6 times (5.3 times if its loan to its incubator partner is counted). I put G8 at 3.5 to 4.5 times: it has falling occupancy, heavier rent, a legal tail and covenant pressure that the peers don't, but it is far larger and has kept its quality ratings (97.4% of centres meeting or exceeding the national standard [G2]).

Method 2: free cash flow to equity, steady state. Capital spending A$33m (the level of non-lease depreciation; CY24 was A$32.5m, CY25 A$51.7m with upgrades, CY26 about A$50m with the CCTV pilot), bank interest A$10m, tax at 30% of (EBITDA after rent less A$33m depreciation less interest), software-as-a-service costs about A$4m (A$5.3m in CY25, kept out of operating EBIT by G8 [G4]). Value = cash flow divided by the return a buyer of a risky, indebted small company would want (12% or 15%), less the A$72.6m of non-bank debt-like items:

| CY27 occupancy | EBITDA after rent | Tax | Free cash flow | at 12% | at 15% |
| --- | --- | --- | --- | --- | --- |
| 6 points lower | 55.1 | 3.6 | 4.5 | 0.00 | 0.00 |
| 3 points lower | 74.6 | 9.5 | 18.2 | 0.10 | 0.06 |
| the same | 94.1 | 15.3 | 31.8 | 0.25 | 0.18 |
| 3 points higher | 113.6 | 21.2 | 45.5 | 0.40 | 0.30 |

The range, per share: occupancy holding at this year's level, A$0.17 to A$0.29 on method 1 and A$0.18 to A$0.25 on method 2, so about A$0.18 to A$0.20 in the middle; 3 points lower, A$0.06 to A$0.18 (about A$0.08 to A$0.09 in the middle); 6 points lower, nil to A$0.06; 3 points higher, A$0.26 to A$0.41. A return to 2025 earnings on the continuing centres (EBITDA after rent about A$144m) is worth A$0.50 to A$0.59 at 4 to 4.5 times, but the company's own test puts that in 2030. What it depends on: occupancy (each point about 3 to 4 cents a share) and the multiple (each half-turn about 6 cents). If the second half of 2026 comes in at the fact sheet's A$27m of operating EBIT instead of my A$40m, every value above falls by about 6 cents a share.

## Why the market is wrong
At A$0.105 the market value is A$79.4m and enterprise value with the debt-like items is A$280.2m: 2.8 times the last 12 months' EBITDA after rent, 3.2 times my CY26 estimate and 3.0 times the CY27 flat-occupancy view. That is roughly what the 3-point-lower case is worth at a peer-like 3.75 times, or the flat case at a distressed 3 times. So the market is pricing a further fall in occupancy, or covenant trouble, or both.

Reasons it may be too gloomy: the July 2025 shock is lapped from July 2026, so year-on-year comparisons should get easier; the savings and the removal of centres running at a third full help the second half; Embark's August update shows occupancy growth and centre earnings ahead of last year [P7]; and the index exit forced selling that had nothing to do with the business.

Reasons it may be right: like-for-like occupancy was still 7.7 points down at June and the August narrowing may be mostly the suspended centres; the June quarter government data still had supply up 2.9% and fewer children; Mayfield's occupancy was still falling in October [P14]; fees are at the subsidy cap, so further rises fall on families; the lenders had to loosen a covenant; and Mayfield shows how the equity of a low-occupancy operator is rescued: a rights issue at A$0.10 seven months after a A$0.50 offer [P13].

I can't say with confidence that the market is wrong today. The CY26 result will show the same-centre occupancy at the start of 2027, the December covenant tests and the earnings run rate, which is what decides it.

## Outcomes and chances

| Outcome | What happens | Chance | Price by resolve date (30 April 2027) |
| --- | --- | --- | --- |
| Bad | Same-centre occupancy keeps falling (early-2027 spot 4 or more points below a year earlier); CY26 operating EBIT under about A$45m and a CY27 outlook near A$55m to A$60m of EBITDA after rent; a covenant waiver beyond the July 2026 change, or an equity raise | 25% | A$0.04 (method 1 on A$55m at 3.5 to 4.5 times: nil to A$0.06; a rescue raise would likely be priced at a deep discount, as Mayfield's was) |
| Middling | Decline slows but doesn't stop (same-centre gap 2 to 4 points in February and April 2027); CY26 operating EBIT about A$50m; another goodwill write-down; covenants met under the loosened test; no raise | 45% | A$0.09 (3 points lower: method 1 at 3.5 to 4 times A$0.08 to A$0.13, method 2 A$0.06 to A$0.10) |
| Good | Occupancy has stopped falling: early-2027 spot and April year to date within about a point of a year earlier on the same centres; CY26 operating EBIT A$55m or more; covenants met, no raise | 30% | A$0.20 (flat case: method 1 at 3.5 to 4 times A$0.17 to A$0.23, method 2 A$0.18 to A$0.25) |

Why these chances: the good case needs the narrowing in August to be real rather than the suspended centres, and needs the sector's demand to steady while supply still grows 2.5% to 2.9% a year. Embark's update and the easier comparison after July 2025 support it; G8's own same-centre figure to June, the June quarter government data and Mayfield's October figure argue against it. I put the good case at 30%, a little below the bad case plus a margin for the legal and covenant tail. The bad case is 25% rather than higher because G8 has A$76m of cash and undrawn debt, no debt due before January 2029, and a covenant already loosened through December 2027.

Expected price: 0.25 x A$0.04 + 0.45 x A$0.09 + 0.30 x A$0.20 = A$0.1105, 5.2% above A$0.105.

Round-trip costs, assumed: at A$0.100 to A$0.105 the ASX tick is half a cent, so the spread is 4.9% of the middle price (bid A$0.100, ask A$0.105 [D1]), paid half on entry and half on exit; brokerage at the A$15 cap on a position of about A$2,000 (2.5% of NZ$100,000 at NZ$1 = A$0.806 [D4]), 0.75% each way; size cost of 4.1% daily volatility x the square root of A$2,000 / A$228,169, about 0.4% each way; and 0.5% to convert NZ dollars to Australian. Total about 7.7%.

Expected gain after costs: 5.2% - 7.7% = -2.5%. Minimum (rulebook section 5a): the 2.13% cash rate plus 5% a year over the 172 days from 9 November 2026 to 30 April 2027, 7.13% x 172/365 = 3.4%. Not a case for review.

How sensitive that is: with chances of 35/40/25 (good/middling/bad) the gain after costs is +2.8%, still short; with 25/45/30 it is -10.1%. At A$0.100 the central chances give +2.8%. Below A$0.10 the tick falls to A$0.001, so the spread drops to about 1% and costs to about 3.9%: at A$0.095 the central chances give +12.5% and the gloomier 25/45/30 give +4.1%, both above the minimum. That is the price trigger below.

## Dated events
- September quarter 2026 Child Care Subsidy data: expected about December 2026 (the June quarter report was out by 23 September [S2]). Shows sector children and services.
- 31 December 2026: covenant tests and the goodwill test, reported with the result.
- CY26 result: about 23 February 2027 (23 February 2026 last year, with the advance notice on 10 February [G20]). Shows CY26 earnings, early-2027 spot and year-to-date occupancy, covenant compliance, any write-down and the CY27 outlook. This is the named event.
- AGM and trading update: about late April 2027 (29 April 2026 last year [G8, G18]).
- H1 CY27 result: about late August 2027 (25 August 2026 last year).
- Fair Work Ombudsman case: first court date not listed at 8 July 2026 [S1].
- Debt: the loosened fixed charge cover test runs to 31 December 2027; facilities mature January 2029 and December 2029 [G1, G7].

Conditions that reopen it:
1. Before the result: a close at or below A$0.095 with no new adverse filing (no raise, no covenant news, no trading downgrade). Rerun as an ordinary research pick resolving 30 April 2027, with the CY26 result as the dated event.
2. After the result, all of: (a) G8 reports early-2027 occupancy on the same centres within 1.5 points of a year earlier, or says in words that it has stopped falling; (b) CY26 operating EBIT of at least A$50m; (c) all covenants met at 31 December 2026 with no further amendment or waiver, and no raise; (d) the price at or below A$0.14. Then rerun with the AGM update and the H1 CY27 result as the dated events.
3. It closes for good on an equity raise priced below A$0.08, a covenant waiver beyond the July 2026 change, or a same-centre fall of 5 points or more in early 2027.

## What would make this wrong
1. Occupancy has already turned. The comparison base got easier from July 2026, supply growth is the slowest in 10 quarters and Embark is already seeing it. If the February result shows the same-centre gap closed, the price could go to about A$0.20 at once, and waiting misses it (my 30%).
2. The bad case is worse or more likely than I have it. The covenant thresholds are unknown; the loosened test runs out after December 2027; a write-down could press the gearing test; the Point Cook civil claims are not provided for; and a low-occupancy operator's equity is rescued at deep discounts (Mayfield). At 35% bad, even A$0.095 would not be enough.
3. My CY26 estimate is too high. If the second half comes in near the fact sheet's A$27m of operating EBIT rather than my A$36.5m to A$43.4m, all the values above drop by about 6 cents a share and the middling case moves to about A$0.03 to A$0.05.

Exit rule (if it is reopened and bought): sell after the result if conditions 2(a) to 2(c) fail, on any raise or waiver, or at the resolve date.

## Checks
- Not on Cam's excluded list: config/judgement_excluded.csv has no entries (confirmed by Cam on 8 November 2026).
- No placement-pattern reopening in the last 30 sessions: G8 has made no placement or share issue in 2026; its 2026 ASX announcements show only buy-back cancellations [G20].
- Liquidity: median daily value traded over the 20 sessions 5 to 30 October 2026 was A$228,169 (lowest A$87,974), from Norgate volume x close [D2], above the A$10,000 floor. Section 3's cap (two sessions at 10% of the median) is A$45,634; the 2.5% research cap (about A$2,016) binds first.

## Sources
G8 Education (ASX announcements and company documents)
- [G1] CY26 Half Year Report and Accounts, 25 Aug 2026 (03129291): https://announcements.asx.com.au/asxpdf/20260825/pdf/0734zbs8v3g2s1.pdf
- [G2] CY26 Half Year ASX Announcement, 25 Aug 2026 (03129292): https://announcements.asx.com.au/asxpdf/20260825/pdf/0734zdyhgs3s30.pdf
- [G3] CY26 Half Year Investor Presentation, 25 Aug 2026 (03129293): https://announcements.asx.com.au/asxpdf/20260825/pdf/0734zh4cxwk5gj.pdf
- [G4] FY25 Financial and Statutory Report and Appendix 4E, 23 Feb 2026 (03063087): https://announcements.asx.com.au/asxpdf/20260223/pdf/06wlh9r4wl5pcn.pdf
- [G5] FY25 Full Year Results Announcement, 23 Feb 2026 (03063091): https://announcements.asx.com.au/asxpdf/20260223/pdf/06wlhl3rrb1dvq.pdf
- [G6] FY25 Investor Presentation, 23 Feb 2026 (03063089): https://announcements.asx.com.au/asxpdf/20260223/pdf/06wlhfxwgxbgtb.pdf
- [G7] Update on debt arrangements, 7 Jul 2026 (03112389): https://announcements.asx.com.au/asxpdf/20260707/pdf/071g1swhqdx1px.pdf
- [G8] Trading Update, 29 Apr 2026 (03087419): https://announcements.asx.com.au/asxpdf/20260429/pdf/06yz868x5vg35m.pdf
- [G9] Market Update, 10 Feb 2026 (03058560): https://announcements.asx.com.au/asxpdf/20260210/pdf/06w4jgy26mfhzy.pdf
- [G10] Half Yearly Report and Accounts, 26 Aug 2025 (02985180): https://announcements.asx.com.au/asxpdf/20250826/pdf/06nb476jysjdzz.pdf
- [G11] CY24 half-year results announcement, 22 Aug 2024: https://announcements.asx.com.au/asxpdf/20240822/pdf/066wr6b17ds81s.pdf
- [G12] Appendix 3H, cessation of 14,940,562 bought-back shares, 3 Nov 2026 (03161493): https://announcements.asx.com.au/asxpdf/20261103/pdf/0765kn90h6mq7y.pdf
- [G13] S&P DJI September 2026 quarterly rebalance, 4 Sep 2026 (03136141): https://announcements.asx.com.au/asxpdf/20260904/pdf/073rbz4q8nrckg.pdf
- [G14] Board Update, 25 Aug 2026 (03129421): https://announcements.asx.com.au/asxpdf/20260825/pdf/07358h30l7f5lw.pdf
- [G15] Change in substantial holding, Allan Gray, 25 Feb 2026 (03065025): https://announcements.asx.com.au/asxpdf/20260225/pdf/06wrfwq7tdf64b.pdf
- [G16] Change of Director's Interest Notice, Julie Cogin, 6 May 2026 (03091032): https://announcements.asx.com.au/asxpdf/20260506/pdf/06z9dhftf2yvfc.pdf
- [G17] Market Update, further charges against former employee, 4 Dec 2025 (03037027): https://announcements.asx.com.au/asxpdf/20251204/pdf/06sy8g8l7dwwk4.pdf
- [G18] Chair and CEO address to shareholders, 29 Apr 2026 (03087437): https://announcements.asx.com.au/asxpdf/20260429/pdf/06yz9gjpsmf3yz.pdf
- [G19] G8 Treasury Policy, November 2023 (company website; no covenant levels): https://g8education.edu.au/wp-content/uploads/2024/10/treasury-policy-final-november-2023.pdf
- [G20] ASX announcement list, GEM, 2026: https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=GEM&timeframe=Y&year=2026

Peers (ASX announcements)
- [P1] Nido, 2026 Half Year results announcement and presentation, 26 Aug 2026 (03130697): https://announcements.asx.com.au/asxpdf/20260826/pdf/0738htvr92gx59.pdf
- [P2] Nido, Appendix 4D and 2026 Half Year Financial Report (03130694): https://announcements.asx.com.au/asxpdf/20260826/pdf/0738hm83n1j25f.pdf
- [P3] Nido, FY2025 results release and presentation, 25 Feb 2026 (03065058): https://announcements.asx.com.au/asxpdf/20260225/pdf/06wrjg3mxbzqx8.pdf
- [P4] Nido, A$9.1 million acquisition of 4 child care services, 27 Apr 2026 (03086508): https://announcements.asx.com.au/asxpdf/20260427/pdf/06ywn7dlg29p5x.pdf
- [P5] Nido, acquisition of 9 early education services, 23 Oct 2026 (03156153; no price disclosed): https://announcements.asx.com.au/asxpdf/20261023/pdf/075p66y30p998g.pdf
- [P6] Embark, Half Year Accounts and Report, 28 Aug 2026 (03131932): https://announcements.asx.com.au/asxpdf/20260828/pdf/073cqypm5d9n9m.pdf
- [P7] Embark, Market Update, 28 Aug 2026 (03131940): https://announcements.asx.com.au/asxpdf/20260828/pdf/073crhxqbhr6k0.pdf
- [P8] Embark, Investor Presentation FY2025, 25 Feb 2026 (03064446): https://announcements.asx.com.au/asxpdf/20260225/pdf/06wq2c5psgm5qg.pdf
- [P9] Embark, A$4.0 million placement, 4 Aug 2026 (03121569): https://announcements.asx.com.au/asxpdf/20260804/pdf/072d78ynsc7dx1.pdf
- [P10] Embark, increase in Mayfield holding, 9 Oct 2026 (03150832): https://announcements.asx.com.au/asxpdf/20261009/pdf/07551kffrn2tl7.pdf
- [P11] Embark, Replacement Bidder's Statement for Mayfield, 5 Jan 2026 (03047034): https://announcements.asx.com.au/asxpdf/20260105/pdf/06tz3jwq35zrpy.pdf
- [P12] Mayfield, Target's Statement, 20 Jan 2026 (03051416): https://announcements.asx.com.au/asxpdf/20260120/pdf/06vfghfqp5j33y.pdf
- [P13] Mayfield, entitlement offer to raise A$3 million at A$0.10, 3 Aug 2026 (03121302): https://announcements.asx.com.au/asxpdf/20260803/pdf/072cbpq5bzyxxt.pdf
- [P14] Mayfield, FY26 guidance reinstated, 15 Oct 2026 (03152787): https://announcements.asx.com.au/asxpdf/20261015/pdf/075c5tppsxqfjz.pdf

Regulator and secondary sources
- [S1] Fair Work Ombudsman media release, 8 Jul 2026: https://www.fairwork.gov.au/newsroom/media-releases/2026-media-releases/july-2026/20260708-g8-litigation-media-release
- [S2] The Sector (secondary), June quarter 2026 Child Care Subsidy data, 23 Sep 2026: https://thesector.com.au/article/fewer-children-using-care-centres-fees-rise-june-2026-ccs-data
- [S3] Department of Education, Child Care Subsidy data report, June quarter 2026 (not readable here: the site blocks automated reading): https://www.education.gov.au/node/20627
- [S4] Arnold Thomas & Becker (secondary, law firm's own page, published July 2025): https://www.arnoldthomasbecker.com.au/media/arnold-thomas-becker-launches-legal-action-against-childcare-giant-g8-education/10414/
- [S5] Search results only, not opened: Simply Wall St analyst page (https://simplywall.st/community/narratives/au/consumer-services/asx-gem/g8-education-shares/mg8tkvux-gem-occupancy-recovery-forecast-will-drive-long-term-upside-despite-near-term-risks/updates/12-analysts-have-lowered-their-price-target-for-g8-education-fr); Motley Fool on Macquarie, 3 Jul 2025 (https://www.fool.com.au/2025/07/03/why-did-macquarie-just-re-rate-g8-education-shares/); Capital Brief (https://www.capitalbrief.com/briefing/g8-education-shares-continue-slide-after-macquarie-downgrade-1bf7a1f1-01de-465a-9f45-bf75d244fe62/)

Data in the repo
- [D1] data/research_data/asx_company.json, fetched 7 Nov 2026: GEM last trade A$0.105, bid A$0.100, ask A$0.105; NDO A$0.25; EVO A$0.39 (all 6 Nov 2026).
- [D2] data/norgate/universe/prices_2026.csv.gz, to 30 Oct 2026: GEM, EVO, NDO, MFD prices and volumes.
- [D3] data/asic/shorts_2026.csv.gz: ASIC short positions in GEM, to 26 Oct 2026.
- [D4] data/fx/fx_daily.csv: NZ$1 = A$0.806387 on 6 Nov 2026.

Not read or not verified: covenant thresholds and definitions (not in any filing read); the Department of Education's own June quarter 2026 page; the Point Cook civil claims' status; analyst coverage; the substantial holder notices other than Allan Gray's February 2026 notice (taken from the fact sheet).
