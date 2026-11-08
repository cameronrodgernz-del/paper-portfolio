# Fenix Resources (ASX:FEX): deep dive. Not a value pick: the bad case (A$0.10) is 49% below the price, and the middling case (A$0.19) is 3% below it

Written 2026-11-08 by the research desk. Price at writing: A$0.195 (last trade on Friday 6 November 2026, bid A$0.19, ask A$0.20, day's low A$0.185, a new 52-week low; the session before also closed at A$0.195; ASX company data in data/research_data/asx_company.json, fetched 7 November 2026 [D1]). Market value: A$150.3m (770,684,831 shares on issue, annual report register at 20 August 2026 [F1]; no shares issued since, 2026 announcement list [F26]).
Status: finished. This is a simulation and not financial advice.
Verdict: **No case.** Not a card, as a value pick or as an ordinary pick. On the outcomes below the expected price by 30 April 2027 is A$0.181, about 7% below the price before costs and about 12% below after them, against a minimum of +3.4%. It is brought forward from grade B (deep dive when its event is close) on Cam's 8 November request; the deciding events are still ahead, so "What would make this wrong" sets out exactly what the December quarter and the feasibility study would have to show, and the prices at which this should be looked at again (a mechanical watch price of A$0.165, and no realistic value-pick price).
Fact sheet: research/facts/FEX.md, grade B. The question it set: is Fenix a road-haul miner with about five years of ore that earns about nil at today's price, or the owner of a larger project and logistics chain worth more? Its anchors: A$0.74 if it goes our way (the scoping study's value), A$0.00 against us.

Order of work. The brief and the fact sheet both quote the A$0.195 price, so it was in view from the start. The valuation was built from the filings: Fenix's own share price enters only in the market multiple check in method 2 (Fenix's own past EV to EBITDA, the measure the market uses for a small producer) and in "Why the market is wrong" and "Outcomes and chances". Arithmetic was run in `python3 -I` from scratch scripts (ops.py, value.py, value2.py, outcomes.py, runway.py, not committed); the key lines are shown.

> In one paragraph: the fact sheet's first test fails. The A$0.74 "our way" figure gives existing holders the whole of the December 2025 scoping study's value for a project that has no feasibility study (slipped twice, now "first half of 2027"), no funding (A$521m of capital against a A$150m company), no allowance for Sinosteel's 10% to 15% share of the project's after-tax profit, and a freight cost of US$11.3/wmt when Fenix has paid US$16.0 to US$22.9/dmt in each of the last five quarters. Re-run with those three things and the discount the market applies to an unfunded development, the study is worth A$0.03 to A$0.15 a share at the company's own price deck; the whole right to that 290Mt resource changed hands in August 2025 for A$60m plus royalties. The existing business is the other half, and at today's iron ore price (about US$90/dmt at A$1 = US$0.70, which in Australian dollars is almost exactly the study's own deck) it loses money: realised A$118/dmt, freight A$29/dmt, C1 cash cost A$75/wmt (the September quarter was A$81.8) and royalties leave EBITDA of about minus A$12m a year, and about minus A$57m a year after sustaining capital, fleet and capitalised waste. With A$135m of borrowings, A$20m still owed to Sinosteel in August 2027 and about A$63m of liquidity at 1 October, the cash runs short around mid-2027 unless iron ore recovers, costs fall to about A$70/wmt or new money comes in. The market is not ignoring this: the enterprise value (A$240m) is about what it was at June 2025 (A$225m) and June 2026 (A$231m); the share price fell because debt rose. A$0.195 is what the business is worth at about US$97 to US$100 iron ore with costs back in guidance, or about 3.5 times its FY24 to FY26 average EBITDA. That is a bet on iron ore, not a mispricing.

Corrections to the fact sheet, for the red team:
1. The A$0.74 anchor (A$1,184m x 0.70 / 1.10 squared, less net debt) leaves out four things a buyer would not: (a) Sinosteel's profit share of 10% of the project's NPAT (15% above US$100), which the study's "before taxes" NPV does not appear to deduct (its A$11.10/wmt royalty line covers the fixed royalties) [F10 p.14, F11 p.7]; (b) freight at US$11.3/wmt (A$17/wmt), which needs trans-shipping to larger ships at scale, against US$16.0 to US$22.9/dmt actually paid from the September 2025 to the September 2026 quarter [F10 Table 2; F9; F8; F7; F5]; (c) the discount the market applies to an unfunded project before a feasibility study (0.3 to 0.5 of its value is used below); (d) the study's A$230m external funding figure assumed FY26 to FY28 operating cash at US$85 and 0.65 that at today's price is not arriving [F10 p.19]. On the study's own sensitivities, these take the anchor to A$0.45 a share at full value and A$0.03 to A$0.15 at a 0.3 to 0.5 development discount (Valuation, method 3).
2. "The existing operation earns roughly nil to A$20m of EBITDA a year once C1 returns to guidance": at US$90 and 0.70 it is about minus A$12m a year at a C1 of A$75 and freight of US$20/dmt; it reaches plus A$32m only with C1 at A$70 and freight at US$17 (Valuation, method 1).
3. September 2026 quarter operating cash flow: the reported A$3.9m included A$8.8m of June-quarter receipts collected in July and left out A$17.0m of September-quarter receipts collected in October [F5 p.8; F7 p.8]. The underlying figure is about A$12.1m (3.9 - 8.8 + 17.0), including A$3.9m of hedge receipts and A$1.4m of tax paid. The fact sheet added the A$17.0m but did not take off the A$8.8m.
4. Craig Mitchell's 2026 sales: the notice of 24 August 2026 shows 2,170,000 shares sold on market between 5 June and 28 July 2026 at an average of 26.7c, and 8,000,000 sold off market at 29.0c on 29 July 2026 [F14 annexure]. The fact sheet's "on-market sales of 10,170,000 at an average of about 28.5c" blends the two; 28.5c is the combined average.
5. The AGM on 27 November 2026 is not a deciding event. Its seven resolutions are the remuneration report, the election of Jenn Morris and Michael Gollschewski, the re-election of Garry Plowright, a higher fee pool for non-executive directors, a sustainability auditor and the renewal of proportional takeover provisions [F13]. Nothing on capital or the project.
6. "No holder is above 10%": APAC Resources' last notice (August 2024) was for 77.5m shares, which is 10.06% of today's 770.7m [F1 p.101]. It is not named in the top 20, so it holds through a nominee and its present holding can't be confirmed; it has lodged no notice of a 1% change since.
7. The study's valuation date is 1 July 2028 [F10 Table 1 notes], 1.65 years from now; the fact sheet discounted two years. Minor, and in the fact sheet's favour.
8. A caution rather than an error: the company's full-year FY26 C1 (A$73.7/wmt) and realised price (A$146.8/dmt) [F2] do not match its own quarterly figures weighted by tonnes shipped (A$75.5/wmt and A$144.5/dmt) [F9; F8; F7]. The quarterly figures are used here.

## The company in plain words
Fenix mines hematite iron ore in the Weld Range in Western Australia's Mid-West, crushes and screens it on site, hauls it about 500km to Geraldton in its own road trains (Fenix Road Logistics, formerly Newhaul, 93 trucks at 30 September 2026), stores it in its own three sheds on the wharf and sells lump and fines to steelmakers in Asia, priced off the Platts 61% Fe index less a discount for grade [F5; F1 note 2]. It shipped 4.4Mt in FY26 from three mines: Iron Ridge (finishing), Shine (finishing) and Beebyn-W11; from the September 2026 quarter it has moved to the "Beebyn Hub" (W11 and the new W10 mine, with a new 5Mtpa crushing plant commissioned after the quarter) [F2; F5]. The Hub's ore reserve is 26.9Mt at 60.0% Fe, "more than five years of mine life at current production rates" [F12].

The rights: Fenix doesn't own the Weld Range deposits; it has rights to mine them from Sinosteel Midwest Corporation, part of China Baowu. A 10Mt right over Beebyn-W11 (October 2023: A$10m, then A$2/t plus 12.5% of notional profit until Fenix recovers its investment and 50% after that) [F20; F10 p.14], and since August 2025 a 30-year right over the whole 290Mt Weld Range resource: A$60m in three instalments (the last A$20m due in August 2027), A$4.00 to A$5.00/dmt royalty, 10% of the project's NPAT (15% when iron ore is above US$100), Sinosteel's right to match any buyer's price for up to all of the ore, and a best-endeavours obligation to produce more than 6Mtpa after ramp-up [F11 p.6 to 8; F1 note 12]. The December 2025 scoping study proposes a 244km private haul road, a rail siding and a second port unloader to reach 10Mtpa by 2031 for A$521m, with a decision in 2028 [F10].

Who runs it: John Welborn, executive chairman (since 2020), with Garry Plowright and two independents appointed on 23 June 2026, Jenn Morris (formerly Fortescue) and Michael Gollschewski (NRW, formerly Rio Tinto) [F23; F13]. Craig Mitchell, who founded Newhaul and sold it to Fenix, left the board on 16 March 2026 once the last 20m milestone shares were issued [F22].

Who owns it, at 20 August 2026 [F1 p.101 to 102]: Mount Gibson Mining 72,500,000 (9.41%, and holder of 12.5m options at 30c expiring July 2028); Citicorp Nominees 8.57%; Resource Invest II AG 44,378,994 (5.76%), which is also Fenix's lender and its partner in the marketing company Fenix Commodities; Exxten (Mitchell) 41,890,000 (5.44%; Mitchell's total by notice 74,490,000, 9.67% [F14]); the Plowright family 2.83%; Welborn 27,300,000 then (28,000,000 after 23 October 2026 [F15]) plus 35,000,000 performance rights. Top 20 hold 50.54%; 7,662 holders. APAC Resources' last notice: 77,500,000 (correction 6).

Five years [F18; F17; F2; D1 income statement; D2]:

| Year to 30 June | 2022 | 2023 | 2024 | 2025 | 2026 |
| --- | --- | --- | --- | --- | --- |
| Revenue (A$m) | 249.2 | 196.8 | 259.2 | 316.1 | 589.7 |
| Profit after tax (A$m) | 50.7 | 29.3 | 33.6 | 5.4 | 12.3 |
| EBITDA (A$m) | not checked | not checked | 73.2 | 54.3 | 80.7 |
| Final dividend (c) | 5.25 | not checked | not checked | 1.0 | 1.0 |
| Share price at 30 June (A$) | 0.315 | 0.285 | 0.315 | 0.28 | 0.255 |

Revenue grew with tonnes; profit fell as the iron ore price came off its 2021 to 2022 highs and the business took on haulage, port and new mines. Fenix has paid A$82.0m of franked dividends since 2021 and has not raised equity for cash since A$15m in August 2020 [F2 p.6].

## Why big investors may be overlooking it
- Size and index: A$150m. Not in the S&P/ASX 200 or 300 at any point in Norgate's records to 30 October 2026 [D3].
- Trading: median value traded A$187,905 a day over the 20 sessions 5 to 30 October 2026 (lowest A$41,146) [D2]; the quoted spread on 6 November was one 0.5c tick, 0.19 to 0.20 [D1].
- Register: the top 20 hold half; four holders near or above 5% each have another relationship with the company (Mount Gibson sold it its port and Shine assets, ResInvest lends to it and markets its ore, Mitchell sold it the haulage business, APAC).
- Sector: iron ore is out of favour. The two other small listed Australian iron ore producers in the exchange data both trade below their cash: Mount Gibson (MGX) at an enterprise value of minus A$50m, Grange (GRR) at minus A$143m [D1]. 
- Coverage: I didn't check broker databases, so "little coverage" isn't claimed.

Is it overlooked or cheap for a reason? Mostly the second. The share is down 63% from its 52-week high of A$0.53 [D1], but the enterprise value (market value plus borrowings less cash, before leases) is about where it was: A$224.5m at 30 June 2025 (0.28 x 741.1m shares + A$17.0m net debt), A$230.7m at 30 June 2026 (0.255 x 765.0m + A$35.7m), and A$239.8m now (0.195 x 770.7m + A$89.5m) [F1; F17; D2]. The fall in the share price is debt taken on to build the Beebyn Hub and pay Sinosteel, while the iron ore price in Australian dollars fell (realised A$147.6/dmt in the September 2025 quarter, A$126.6 in the September 2026 quarter) [F9; F5]. The heaviest trading month since January was June (47.4m shares, A$12.6m) as the price went from 30.5c to 25.5c [D2], which overlaps Mitchell's sales (correction 4). The executive chairman has bought on each fall (47.9c, 33.8c, 32.0c, and 19.9c on 23 October 2026, the last described as "on and off-market" with no split [F15]), and Jenn Morris bought at 25.25c; those buys show conviction but have not marked a bottom.

## What the filings show

### Trading by quarter
| Quarter | Shipped (k wmt) | Platts index (US$/dmt) | Realised CFR (A$/dmt) | Freight (US$/dmt, A$/dmt) | C1 (A$/wmt FOB) | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Sep 2025 | 885.4 | 102.0 (62%) | 147.6 | 16.7, 25.5 | 75.7 | [F9] |
| Dec 2025 | 1,241.5 | 106.0 (62%) | 147.4 | 18.1, 27.6 | 75.0 | [F9] |
| Mar 2026 | 973.6 | 103.7 (61%) | 145.5 | 16.0, 23.1 | 70.0 | [F8] |
| Jun 2026 | 1,298.7 | 105.3 | 138.7 | 22.5, 31.7 | 79.9 | [F7] |
| Sep 2026 | 1,097.2 | 96.9 | 126.6 | 22.9, 32.6 | 81.8 | [F5] |

EBITDA was A$48.6m in the December 2025 half (A$22.9/wmt) and A$32.1m in the June 2026 half (A$14.1/wmt, by difference from the full year's A$80.7m) [F4; F2]. In the September 2026 quarter the discount to the index widened to 7.7% (two low-grade cargoes), freight was the highest in the table, and C1 was above the A$70 to A$80 guidance, which the company kept for FY27 on the expectation that costs fall in the second half as the new plant runs at full rate [F5 p.3 to 4].

### Cash and capital
- FY26: operating cash flow A$95.9m; payments for mine property and plant A$75.8m including A$25.1m to Sinosteel with stamp duty; asset finance repaid A$32.1m and drawn A$14.2m; A$35.0m drawn from ResInvest; dividends A$7.4m; cash up A$24.2m to A$81.0m [F1 cash flow statement].
- September 2026 quarter: underlying operating cash about A$12.1m (correction 3); capital spending A$23.6m (A$19.0m Weld Range and the crushing plant, A$3.5m sustaining, A$1.1m Geraldton housing) plus A$14.3m of capitalised waste at W11; the second A$20m to Sinosteel; A$28.7m drawn "on finance facilities" and A$10.1m of fleet debt repaid; cash A$43.2m [F5 p.7 to 8]. No Appendix 5B was lodged, so the quarter can't be rebuilt line by line [F26].
- After the quarter: A$17.0m of September shipment receipts in early October; the iron ore swaps closed out on 23 October for about A$10.2m (A$8.5m in October, A$1.7m in November), so iron ore sales are now unhedged; diesel swaps (about 30% of FY27 fuel) and US$99m of currency options at an average 0.7532 remain [F6]; the 1c dividend (A$7.7m) paid on 5 October [F2].
- Capital still guided for FY27 and FY28: sustaining about A$20m, trucks and trailers A$40m to A$50m, growth about A$30m in mining (including the crusher, now largely spent) and about A$20m in logistics and port [F7 p.9].

### What is owed (A$m)
| Item | Amount | When | Source |
| --- | --- | --- | --- |
| Equipment and property loans (85 chattel mortgages, 2.42% to 7.70%) | 81.6 at 30 Jun 2026 | monthly; 25.7 within a year | [F1 note 17] |
| ResInvest facilities: US$9.28m interest-free prepayment and US$35m at SOFR + 4.5%, secured on stockpiles, receivables and Fenix's 50% of Fenix Commodities; covenants on net financial debt to EBITDA and debt service cover | 35.0 at 30 Jun 2026 (US$24.3m) | repayments from month 21, all due two years after drawdown | [F1 note 17] |
| Drawn in the September quarter, net of repayments | +18.6 | | [F5] |
| Borrowings at 30 Sep 2026 (my sum) | about 135.2 | | |
| Sinosteel instalment | 20.0 | August 2027 | [F1 note 12, 18] |
| Leases | 12.1 | | [F1 note 17] |
| Trade payables and accruals | 94.8 at 30 Jun 2026 | normally 30 days | [F1 note 15] |

Net debt at 30 September 2026, after the hedge cash and the October dividend: 135.2 - 43.2 - 10.2 + 7.7 = A$89.5m; A$109.5m with the Sinosteel instalment; A$121.6m with leases. The A$28.7m drawn in the quarter matches the undrawn US$20m of the ResInvest facility (A$28.6m at 0.70), but the report doesn't say which facility it was; at 30 June about A$38m of the A$120m asset finance limit was undrawn, tied to equipment and property [F2 p.6].

Things a quick reader would miss:
- Working capital is borrowed from suppliers: at 30 June payables of A$105.8m against receivables of A$18.8m and inventory of A$45.1m [F1 balance sheet]. If the business shrinks or suppliers shorten terms, that reverses as a cash outflow.
- Covenants: the ResInvest facilities test net financial debt to EBITDA and debt service cover; "a future breach ... may require the Group to repay these amounts earlier" [F1 note 17, 24(c)]. The levels aren't disclosed. With EBITDA near nil at today's price, this matters by mid-2027.
- The goodwill test (A$11.5m, Weld Range unit) used US$85/dmt and 0.65 for the life of mine with "significant headroom" [F1 note 13]. That test covers the whole 290Mt Weld Range plan, not just the reserve, so it says little about the reserve on its own.
- The RTMA asked Fenix to use reasonable endeavours to finish feasibility studies within 12 months of signing (by August 2026) [F11 p.8]; the study has moved from "June 2026 quarter" (December 2025) to "second half of 2026" (by the March quarterly, April 2026) to "first half of 2027" (October 2026), the last time to wait for the WA Government's plans for the state's rail freight network, and it is now to be released "alongside a project financing solution" [F10 p.2; F8; F5 p.5, p.10].
- The parent company recorded a loss of A$40.1m in FY26 and its retained earnings fell from A$55.5m to A$8.1m [F1 note 33], which leaves little room for dividends at the parent level without the subsidiaries paying up.

## Valuation
Shares 770.7m. Claims ahead of the shares: A$121.6m (net debt A$89.5m, Sinosteel A$20.0m, leases A$12.1m). Other assets: Athena stake at book A$3.0m and the Twin Peaks loan A$4.45m [F1 note 14]. Price decks are the Platts 61% index at A$1 = US$0.70 (the RBA rate was 0.69 to 0.70 in the week to 6 November [D4]); for reference, on 23 October Fenix closed out its swaps at about A$130/t, so the forward price to June 2027 was about US$91 (480kt x (151.31 - F) = A$10.2m gives F = A$130.1, at 0.7006) [F6], and Kallanish put 62% fines at US$90.3/t on 27 October [M1, secondary].

### Method 1: the existing Beebyn Hub reserve, cash flow by price deck
Per tonne at US$90 and 0.70 (spot): index A$128.6/dmt; realised A$118.3 (8% discount, the September quarter's 7.7%); freight A$28.6 (US$20, between FY26's US$18.8 and the September quarter's US$22.9); FOB A$85.7/wmt after 4.5% moisture; royalties A$10.1/wmt (state 7.5% and native title 0.5% of FOB, plus about A$3.2 for Sinosteel's fixed royalties on W11 and W10); C1 A$75 (the middle of guidance); overheads A$15m a year (A$3/wmt). EBITDA = 85.7 - 10.1 - 75.0 - 3.0 = minus A$2.4/wmt, minus A$11.9m a year at 5Mt.

Check against the record: on the same arithmetic the model gives A$49.4m for the December 2025 half (actual A$48.6m) and A$40.2m for the June 2026 half (actual A$32.1m), so if anything it flatters the business.

Cash flow adds capital of about A$45m a year (A$20m sustaining and fleet replacement, and capitalised waste of A$5/wmt; the September quarter's was A$13/wmt), Sinosteel's profit shares and tax where there is profit. Reserve 27.2Mt wet from 1 October (26.9Mt dry at 1 July less the quarter's mining, at 4.5% moisture), 5Mt a year, so 5.4 years; 10% real discount rate; at the end, the working capital unwinds (minus A$42m), closure A$15m, port and land worth A$25m. Management can stop the reserve if it loses money, so after June 2028 the value is floored at the cost of closing it.

| Deck (Platts 61%, at 0.70) | EBITDA A$m/yr: C1 80, freight US$23 / C1 75, US$20 / C1 70, US$17 | Free cash A$m/yr, middle case |
| --- | --- | --- |
| US$80 | -113 / -70 / -26 | -115 |
| US$85 | -85 / -41 / +3 | -86 |
| US$90 (spot) | -56 / -12 / +32 | -57 |
| US$95 | -27 / +17 / +61 | -28 |
| US$100 | +2 / +46 / +90 | 0 |
| US$110 | +60 / +104 / +147 | +39 |

The reserve alone pays its way after capital only at about US$100 with costs in guidance. Its value to the shares (cash flow PV less the A$121.6m of claims) is nil at every deck to US$100 in the middle case; a full-life DCF of the reserve breaks even at about US$101 and covers net debt and the Sinosteel instalment (A$109.5m) at about US$108 (ops.py).

Cash runway at spot (runway.py): liquidity at 1 October about A$62.7m (43.2 + 17.0 receipts + 10.2 hedges - 7.7 dividend). Spending a quarter: about A$3m of EBITDA loss, A$2.75m interest, A$5m sustaining and fleet, A$4m to A$6m waste, A$0 to A$5m growth, A$10m of fleet debt repayments, so A$24.5m to A$32m. Cash goes below nil between the March and June 2027 quarters, before the A$20m to Sinosteel in August 2027 and the ResInvest repayments from about March 2028, unless new asset finance, a recovery or new money fills it. With C1 at A$70 and freight at US$17 it lasts to about the September 2027 quarter.

### Method 2: what the market pays for a small producer, EV to EBITDA
Fenix's own EV to trailing EBITDA was 4.1 times at 30 June 2025 and 2.9 times at 30 June 2026 (above). At 3.0 to 4.0 times (claims A$121.6m, other assets A$7.45m), with costs in guidance:

| EBITDA basis | EBITDA A$m | Value a share at 3.0x / 3.5x / 4.0x |
| --- | --- | --- |
| US$95 | 17 | 0 / 0 / 0 |
| US$100 | 46 | 0.03 / 0.06 / 0.09 |
| US$105 | 75 | 0.14 / 0.19 / 0.24 |
| US$110 | 104 | 0.26 / 0.32 / 0.39 |
| FY24 to FY26 average (realised A$144 to A$148/dmt) | 69.4 | 0.12 / 0.17 / 0.21 |

This values the operation only, with nothing for the Weld Range expansion.

### Method 3: the Weld Range expansion, from the scoping study
The study: pre-tax NPV at 10% real of A$1,184m at 1 July 2028, at US$85 and 0.65 (A$130.8/dmt), C1 A$55.4/wmt from a haul road and larger trucks, freight US$11.3/wmt, A$521m of capital including 16% contingency, "before taxes and financing"; a 10% lower price gives A$427m and 10% higher A$1,932m; operating costs plus or minus 10% give A$617m and A$1,751m [F10 Tables 1 to 3, p.17 to 18]. It is a scoping study, accuracy -10% / +25%, with 11% of the tonnes from inferred resources [F10 p.2].

Adjustments (value.py): price change at the study's own sensitivity (about A$75m per 1% of the Australian dollar price); freight A$5/wmt above the study (A$22/wmt, at or below every quarter of the last five) costs A$330m on the study's operating cost sensitivity; tax at 30% (x 0.70); Sinosteel's 10% of NPAT (x 0.90); 1.65 years to the study date at 10%; then a development discount of 0.3 (before the feasibility study, unfunded) or 0.5 (after a feasibility study with funding).

| Deck | Pre-tax NPV after freight (A$m) | Risked value at 0.3 / 0.5 (A$m) |
| --- | --- | --- |
| US$85, 0.65 (study deck) | 854 | 138 / 230 |
| US$85, 0.70 | 313 | 51 / 84 |
| US$90, 0.70 (spot) | 726 | 117 / 196 |
| US$100, 0.70 | 1,545 | 250 / 416 |
| US$110, 0.70 | 2,362 | 381 / 636 |

At the study deck, after the claims: A$0.45 a share at full value (x 1.0), A$0.15 at 0.5, A$0.03 at 0.3. A marker for what a buyer pays for this right: Sinosteel, a steelmaker that wants the ore mined, granted the 30-year right to the whole resource in August 2025 for A$60m plus royalties and profit share, when the index was about US$100 [F11].

### Putting them together
Value of the shares = the reserve's cash flow to June 2028, plus the expansion (risked as above, replacing the reserve after June 2028), plus the reserve after June 2028 for the rest, less the claims (value2.py). In A$ a share, at a development discount of 0.3 / 0.5:

| Deck | C1 80, freight US$23 | C1 75, freight US$20 | C1 70, freight US$17 |
| --- | --- | --- | --- |
| US$85 | 0 / 0 | 0 / 0 | 0 / 0 |
| US$90 (spot) | 0 / 0 | 0 / 0 | 0 / 0.06 |
| US$95 | 0 / 0.08 | 0.01 / 0.17 | 0.13 / 0.28 |
| US$100 | 0.06 / 0.28 | 0.16 / 0.38 | 0.29 / 0.49 |
| US$105 | 0.21 / 0.49 | 0.34 / 0.60 | 0.46 / 0.71 |
| US$110 | 0.38 / 0.71 | 0.51 / 0.81 | 0.63 / 0.92 |

Range: nil at today's price and costs; A$0.13 to A$0.38 if iron ore averages US$95 to US$100 with costs back in guidance; A$0.34 to A$0.81 at US$105 to US$110. The main thing each depends on is the Australian dollar iron ore price: each US$5 moves the middle case by about 15c to 20c a share. Second is C1 and freight together (about 11c to 13c a share between the middle and better columns). Third is how much of the expansion the market will credit before it is funded.

## Why the market is wrong
I can't say it is. At A$0.195 the market prices Fenix at about the value it would have at US$97 to US$100 iron ore with costs back in guidance (middle column, between the two discounts), or about 3.5 times its FY24 to FY26 average EBITDA. The forward price in Fenix's own hedge close-out was about US$91 to June 2027, and spot was about US$90 at the end of October. If anything the price leans to the hopeful side: it assumes either a recovery in iron ore, the costs falling, or the expansion being credited at a funded-project discount before there is a feasibility study. None of these is something the market is missing; they are the open questions. With no reason the market is wrong, there is no trade.

## Outcomes and chances
Resolve date: 30 April 2027 (173 days), after the March 2027 quarterly (about 23 April), the last results before the feasibility study.

| Outcome | What happens | Chance | Price by resolve date |
| --- | --- | --- | --- |
| Bad | The index averages US$90 or less (A$129/dmt or less) into 2027 and C1 stays at A$75 or more. The December and March quarters show losses and cash sliding toward nil; growth and fleet spending are cut; a placement, an asset-level funding deal or a waiver is in view, at or before the feasibility study | 45% | A$0.10 |
| Middling | The index averages US$90 to US$100; the new plant brings C1 back inside guidance and freight eases; the quarters about break even; cash holds up with new asset finance; the feasibility study is still pending and no shares are issued | 40% | A$0.19 |
| Good | The index is above US$100 (above A$143/dmt) with costs in guidance, or the feasibility study arrives early with funding that needs few new shares, or a holder bids (Mount Gibson, APAC, ResInvest or Baowu) | 15% | A$0.40 |

Chances add to 100%. Which valuation figure each price uses:
- Bad: the combined value is nil at US$85 to US$90 in every cost case at a 0.3 discount and at most A$0.06 at 0.5. A$0.10 is a generous figure for what the market still pays for the expansion and a recovery, and about where a placement would be priced after two loss-making quarters. I use the generous end so that "no case" doesn't rest on a harsh bad case.
- Middling: the average of the US$95 deck (middle and better costs, both discounts: 0.01, 0.17, 0.13, 0.28) and the US$100 deck (middle costs, both discounts: 0.16, 0.38), A$0.187; I use A$0.19. Method 2 at the FY24 to FY26 average gives A$0.12 to A$0.21.
- Good: the low end of the US$105 deck (A$0.34 to A$0.71) and US$110 at middle costs and 0.3 (A$0.51); I use A$0.40, held down because five months is short for the market to credit it in full. Fenix traded at A$0.48 on 2 January 2026 [D2] with the index at about US$106 and lower debt.

Expected price: 0.45 x 0.10 + 0.40 x 0.19 + 0.15 x 0.40 = A$0.181, 7.2% below A$0.195 before costs.

Round-trip costs at our size (2.5% of NZ$100,000 is about A$2,016): brokerage capped at A$15 each way, 1.49% for the round trip (nil on the buy if the monthly plan covers it); currency conversion 0.5%; half of the one-tick (0.5c) spread each way, 2.56%; size cost 0.28% each way at 2.9% daily volatility and A$220,429 average daily value (0.55%). About 5.1% in all. Expected gain after costs: about minus 12.3%, against the minimum of the cash rate plus 5% a year, (2.13% + 5%) x 173 / 365 = +3.38%. Not a case for review.

Value pick test: the bad case (A$0.10) is 49% below the price, against a limit of 10%; the middling case (A$0.19) is 3% below the price, against the 15% above that it needs. Over 24 months the bad case is worse, not better: with A$20m to Sinosteel in August 2027 and ResInvest's US$44m from 2028, a long stretch at today's price ends in a recapitalisation whose price isn't bounded by the business's value. So it can't be a value pick.

## Dated events
- November 2026: the October iron ore swaps settle, about A$1.7m (announced) [F6].
- 27 November 2026: AGM, routine resolutions (correction 5); the chair's address may update guidance [F13].
- December 2026 quarter: full ramp-up of the 5Mtpa Beebyn Hub crushing plant; first W10 shipments (announced) [F5 p.4; F12 p.1].
- About 5 January 2027: December quarter production update (inferred from 5 January 2026).
- About 22 January 2027: December quarterly, the first quarter fully unhedged on iron ore. The first real read on costs at today's price.
- About 25 February 2027: half-year accounts: EBITDA, cash, any covenant or going-concern wording, the interim dividend decision.
- About 23 April 2027: March quarterly.
- First half of 2027: Weld Range feasibility study, "alongside a project financing solution" (company target, slipped twice) [F5 p.10].
- August 2027: last A$20m to Sinosteel [F1 note 12]. From about March 2028: ResInvest repayments; 2028: final investment decision [F1 note 17; F5].

## What would make this wrong
What would make "no case" wrong:
1. Iron ore. The shares are geared about three to one to the Australian dollar index: from the September quarter average (A$137) to today (about A$129), 6% lower, they fell from A$0.25 to A$0.195, 22% [F5; D2]. A move above US$100 at 0.70 sustained into 2027 puts the value at A$0.16 to A$0.38 and above, and the bad case falls away.
2. Funding from Baowu or another partner that pays for the haul road or a share of the project at a price well above the 0.3 to 0.5 discount used here, or a bid. Mount Gibson (9.4%, with an enterprise value of minus A$50m, so cash above its market value [D1]), APAC, ResInvest and Sinosteel all have reasons and, in some cases, the money.
3. Costs. If the new plant, the BP diesel contract and larger ships bring C1 to A$70 and freight to US$17, the business makes about A$32m of EBITDA a year at today's price and the runway reaches late 2027.

Reopen (a fresh deep dive, not an automatic card) if any of these happens:
- The December 2026 quarter (about 22 January 2027) shows all of: C1 at A$75/wmt or below with the new plant at full rate, freight at US$18/dmt or below, quarter-end cash of A$40m or more after the capital program and with no equity issued, and the Platts 61% index at US$100 or more in that quarter. Then the middle-to-better columns at US$100 apply (A$0.16 to A$0.49) and the case should be re-run against the price then.
- The feasibility study is released with a post-tax NPV of A$600m or more at US$85 and 0.70 or lower, freight assumed at US$15/wmt or below with a contract or trial to back it, and funding that is mostly debt or partner money with any new shares issued at or above the then share price. Then re-run with the expansion at a 0.5 discount; at today's iron ore price, with middle to better costs, a study that good is worth about A$0.05 to A$0.14 a share (value2.py), so the study alone is unlikely to be enough without a better iron ore price.
- A holder moves: a substantial holder change from Mount Gibson, APAC, ResInvest or a Baowu entity, or a proposal. That makes it a special situation deep dive.

Watch price: on the outcomes above, with nothing else changing, the expected gain clears the minimum at A$0.165 or below (0.181 / (1 + 0.0338 + 0.051)). It is mechanical: a fall to 16.5c would most likely come with a lower iron ore price, which lowers the outcome prices too, and at that price there would still be no reason the market is wrong. There is no realistic value-pick price: the arithmetic limit on these outcomes is A$0.11, but the shares would be there only after the bad outcome had happened, which resets the bad case lower.

Close the file for good (no further work until a new fact sheet) on any of: a placement or rights issue below A$0.15; a covenant waiver or breach; C1 above A$80/wmt in the December quarter; the feasibility study moved into the second half of 2027; cash below A$25m at a quarter end.

## Checks
- Not on Cam's excluded list: config/judgement_excluded.csv has no entries (confirmed by Cam 2026-11-08).
- No placement-pattern reopening in the last 30 sessions: no trading halt in the 2026 announcement list (the last was 28 August 2025) [F26]; no share issue for cash.
- Liquidity: median daily value A$187,905 over 5 to 30 October 2026 [D2], above the A$10,000 minimum. Section 3 cap: two sessions at 10% of the median, about A$37,600 (NZ$46,600), far above a 2.5% position of about NZ$2,500, which is about 1.1% of one median day.

## Sources
Filings (ASX announcements; links as resolved from displayAnnouncement.do):
- F1. FY26 Annual Report, 26 Aug 2026 (03130153): https://announcements.asx.com.au/asxpdf/20260826/pdf/073767rmnksqp6.pdf
- F2. FY26 Full Year Results, 26 Aug 2026 (03130367): https://announcements.asx.com.au/asxpdf/20260826/pdf/0737p5k5wvxlvz.pdf
- F3. Half Year Financial Report, 25 Feb 2026 (03064503): https://announcements.asx.com.au/asxpdf/20260225/pdf/06wq68z012ztdn.pdf
- F4. Half Year Results - Record Production and Earnings, 25 Feb 2026 (03064525): https://announcements.asx.com.au/asxpdf/20260225/pdf/06wq7t7c6ylctc.pdf
- F5. Quarterly Activities Report, September 2026, 22 Oct 2026 (03155535): https://announcements.asx.com.au/asxpdf/20261022/pdf/075mhszz97zm4v.pdf
- F6. Hedge Book Update, 23 Oct 2026 (03156052): https://announcements.asx.com.au/asxpdf/20261023/pdf/075nz1r39cy5q7.pdf
- F7. Quarterly Activities Report, June 2026, 21 Jul 2026 (03116547): https://announcements.asx.com.au/asxpdf/20260721/pdf/071wpkhmh4y7d6.pdf
- F8. Quarterly Activities Report, March 2026, 23 Apr 2026 (03085436): https://announcements.asx.com.au/asxpdf/20260423/pdf/06ys096mtp8fbb.pdf
- F9. Quarterly Activities Report, December 2025, 22 Jan 2026 (03051856): https://announcements.asx.com.au/asxpdf/20260122/pdf/06vgxl704mw2fz.pdf
- F10. Weld Range Scoping Study, 23 Dec 2025 (03044595): https://announcements.asx.com.au/asxpdf/20251223/pdf/06tnmfnfh4bbtz.pdf
- F11. Fenix Secures 290Mt Weld Range Iron Ore Project, 1 Sep 2025 (02989146): https://announcements.asx.com.au/asxpdf/20250901/pdf/06nnjc4rpb12p7.pdf
- F12. Maiden Beebyn Hub Ore Reserve, 3 Sep 2026 (03135107): https://announcements.asx.com.au/asxpdf/20260903/pdf/073nn057y91m66.pdf
- F13. Notice of Annual General Meeting/Proxy Form, 26 Oct 2026 (03157260): https://announcements.asx.com.au/asxpdf/20261026/pdf/075sqlv54nczkp.pdf
- F14. Change in substantial holding (C Mitchell), 24 Aug 2026 (03129190): https://announcements.asx.com.au/asxpdf/20260824/pdf/0734kpk3hym0bt.pdf
- F15. Change of Director's Interest Notice - John Welborn, 26 Oct 2026 (03156795): https://announcements.asx.com.au/asxpdf/20261026/pdf/075rlcvtf2ml3t.pdf
- F16. FY26 Production Update and FY27 Guidance, 7 Jul 2026 (03112326): https://announcements.asx.com.au/asxpdf/20260707/pdf/071fx77p7wqghy.pdf
- F17. FY25 Full Year Results, 27 Aug 2025 (02986230): https://announcements.asx.com.au/asxpdf/20250827/pdf/06ndq3xkkdr6g0.pdf
- F18. FY22 Full Year Results, 29 Aug 2022 (02559740): https://announcements.asx.com.au/asxpdf/20220829/pdf/45ddndpf29gx8g.pdf
- F19. Acquisition of Mid-West Iron Ore and Port Assets, 29 Jun 2023 (02680752): https://announcements.asx.com.au/asxpdf/20230629/pdf/05r2wxvygfkffz.pdf (A$10m cash, 60m shares and 25m options for Shine, Geraldton sheds 4 and 5 and the rail sidings: about A$27m at A$0.275)
- F20. Fenix Acquires 10M Tonne Right to Mine over Weld Range, 3 Oct 2023 (02720483): https://announcements.asx.com.au/asxpdf/20231003/pdf/05vm851qsk35zb.pdf
- F21. Fenix acquires Mid-West haulage business, 21 Jun 2022 (02533446): https://announcements.asx.com.au/asxpdf/20220621/pdf/45b2xf4w3j4b9m.pdf (A$16.5m upfront and up to 60m milestone shares for the other 50% of Newhaul)
- F22. Haulage Milestone Achievement and Leadership Update, 17 Mar 2026 (03072873): https://announcements.asx.com.au/asxpdf/20260317/pdf/06xhs1vp15hrr7.pdf
- F23. Board Update, 23 Jun 2026 (03106651): https://announcements.asx.com.au/asxpdf/20260623/pdf/070wz9fkrhqmgm.pdf
- F24. Fenix 3-Year Production Plan, 11 Dec 2025 (03039809): https://announcements.asx.com.au/asxpdf/20251211/pdf/06t6gb5pd1thhh.pdf
- F25. Operational Update (Cyclone Narelle, diesel supply), 26 Mar 2026 (03076064): https://announcements.asx.com.au/asxpdf/20260326/pdf/06xtlk5fdltf95.pdf
- F26. ASX announcement lists for FEX, 2025 and 2026: https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=FEX&timeframe=Y&year=2026 (nothing after 26 Oct 2026; no trading halt in 2026; no Appendix 5B with the September 2026 quarterly)

Data:
- D1. ASX company data, data/research_data/asx_company.json (fetched 7 Nov 2026): FEX last trade, bid, ask, 52-week range, shares, income statements; MGX and GRR enterprise values.
- D2. Norgate prices and volumes, data/norgate/universe/prices_2021.csv.gz to prices_2026.csv.gz (to 30 Oct 2026).
- D3. Norgate index membership, data/norgate/index_members.csv.
- D4. RBA AUD/USD, data/fx/fx_daily.csv (to 6 Nov 2026).

Secondary (named because no primary index price is available here):
- M1. GMK Center, "Iron ore prices remained under pressure in the second half of October", 29 Oct 2026, citing Kallanish (62% Fe KORE Qingdao US$90.3/t CFR on 27 Oct; SGX futures US$89.25/t intraday): https://gmk.center/en/news/iron-ore-prices-remained-under-pressure-in-the-second-half-of-october/

Not verified: whether the scoping study's NPV deducts Sinosteel's profit share (it says "before taxes"; the royalty line appears to hold only the fixed royalties); why the September quarter's operating cash (about A$12m underlying) runs ahead of the margin arithmetic (about minus A$6m), most likely working capital and a 250kt draw on ore stockpiles (processed 1,157kt against 907kt mined) [F5]; which facility the A$28.7m came from, and the covenant levels; iron ore prices after 27 October 2026; APAC's present holding; how much of Welborn's 23 October purchase was on market.
