# EML Payments (ASX:EML): deep dive. Wait for the half-year result (about 25 February 2027). Not a value pick: the bad case (A$0.10 in 2028) is 64% below the price

Written 2026-11-08 by the research desk. Price at writing: A$0.28 (last trade on Friday 6 November 2026; bid A$0.28, ask A$0.29; close on 5 November A$0.265; ASX company data fetched 7 November 2026 UTC [M1]). Norgate's last close in the repo is A$0.215 on 30 October [M2]. Market value: A$109.6m (391,262,494 shares on issue at 8 October 2026 [A18][M1]). Unquoted: 63,627,800 performance rights, 2,619,304 rights and 64,358 restricted rights, 66.3m in all, which vest in full on a change of control [A18][A1 remuneration report].
Status: finished. Verdict: **wait for a named event**, the 1H FY27 result (about 25 February 2027, inferred from 25 February 2026 [A6]), with the AGM on 18 November 2026 as a first look [A19]. At A$0.28 the price is within 4% of my probability-weighted value (A$0.29). The six-month expected price is A$0.309, +10.4% before costs and +5.4% after, against a minimum of +2.4%. That clears only on my central chances and a 13% cost of equity. Move five points of chance from the good outcome to the bad one, or use 14%, and it fails. I can't say why the market is wrong at A$0.28, so no case today. Watch trigger before the result: **A$0.25 or lower**, with nothing else changed. The conditions that reopen or close it are under "Dated events". This is a simulation and not financial advice.
Fact sheet: research/facts/EML.md (8 November 2026), grade A. Its question: do the costs EML calls non-recurring (A$28.2m in FY25, A$33.9m in FY26) stop, so that A$50m to A$54m of FY27 underlying EBITDA turns into the A$30m to A$35m of "proforma" free cash flow forecast for FY28? Its anchors: A$0.40 if it goes our way (+44%), A$0.12 if it goes against us (-56%).

Value pick (rulebook section 5a): it doesn't qualify. Over 24 months (to the FY28 result, late August 2028) the bad case is worth about A$0.10, 64% below the price, against the limit of 10%. The middling case (A$0.46) clears the +15% leg easily. As an ordinary pick, the half-year result is inside six months, but the expected gain only clears the minimum on the central inputs, and the price isn't clearly below value.

Order of work: the price was in the brief and the fact sheet, so it was in view from the start. "What the filings show" and "Valuation" were worked from EML's own accounts for FY23 to FY26, its presentations, and Tyro's and Payoneer's filings. The share price enters only in "Why the market is wrong" and "Outcomes and chances", and in one line backing out what the price implies. The arithmetic was run in `python3 -I` from scratch scripts (eml_calc.py and eml_sens.py, not committed); key lines are shown.

> In short. Liquidity passes: A$123,896 a day median over the 20 sessions 5 to 30 October 2026 [M2], which caps a position at A$24,779; the 2.5% cap (about A$2,016) binds first. Tested line by line, the "non-recurring" items have recurred in every one of the last four years: A$28.1m (FY23), A$10.7m (FY24), A$28.2m (FY25) and A$33.9m (FY26), A$100.8m in all, and a new kind of item has appeared each year (fraud losses, the PCSIL exit, legacy tax, a stored value shortfall, and for FY27 the cost of an APRA-required bank guarantee) [A5][A3][A1][A10]. Over those four years EML reported A$192.6m of underlying EBITDA and about minus A$5m of free cash flow before the class action payment [A5][A3][A1]. "Proforma" free cash flow is not defined in any filing. The way EML builds its other cash measure, and its 2024 plan's "~60%" cash conversion target, point to underlying EBITDA less interest, tax, capital spending and leases, with every item EML labels non-recurring left out [A2][A8]. On that reading the A$30m to A$35m could be "met" while shareholders get A$20m or less. The FY28 target itself has been cut: in November 2024 the plan was about A$95m of FY28 underlying EBITDA with about 60% converting to free cash, and Project Arlo was to cost A$12m to A$15m; Arlo is now A$34m and runs to 2029 [A8][A1]. Of A$2.2bn of balances, none is EML's; the A$37.8m of cash is not all free either: UK and EU rules need own funds of 2% of e-money (about A$29m across EML's pound and euro float), APRA's standard for licensed payment facilities needs 4% of covered stored value (up to A$21m if it covered all the Australian float), and A$13.6m is already owed to cardholders under the shortfall provision [A1][A2][R1][R2][R3]. Bank debt is A$84m drawn; the gearing covenant (0.45) stood at 0.41 [A1]. Valued on cash flow after the costs that keep recurring, the range today is A$0.07 (bad) to A$0.68 (good), A$0.40 in the middling case, and about A$0.29 weighted by my chances (A$0.22 at a 15% cost of equity, A$0.39 at 11%). The fact sheet's A$0.40 is roughly my middling case, but it is a 2028 value, built from a peer multiple on a different basis. At the 30 October close of A$0.215 the expected gain after costs was about +38%; the 30% rise in the week to 6 November, with no announcement, took the price to about fair.

Corrections to the fact sheet, for the record:
1. Copia's April 2026 buys averaged A$0.44 (3,010,000 shares for A$1,327,267), not A$0.41; its May buys A$0.40 (4,140,000 for A$1,653,942). Most of its 48.55m shares were bought at A$0.69 to A$1.05 (August 2025 to February 2026), so "buying at about A$0.40" describes only the last 7m to 9m shares [A14].
2. Facilities: the A$125m includes a A$10m bank guarantee facility. Lending facilities are A$115m, A$84m drawn, A$31m undrawn [A1 note 19, going concern note].
3. Covenants: there is a third, gearing (debt including leases over debt plus equity) no more than 0.45. It was 0.41 at 30 June 2026: about A$17m more debt or A$21m less equity would breach it [A1 note 19].
4. Net debt of A$46.9m leaves out the A$13.6m stored value shortfall provision, which is cash owed to cardholders and expected to be paid in FY27, and A$4.7m of leases. Including the provision it is A$60.4m [A1 notes 19, 21].
5. Rate sensitivity: EML states A$16.2m a year per 1% on its floating-rate balances, about A$4.1m per 0.25%, not A$5.5m. A$0.72bn sits in bonds held to maturity at fixed yields (average 4.0%, 2.5 years) and A$0.5bn of Australian float earns EML nothing [A1 note 23][A2].
6. The Tyro anchor: Tyro's A$145.3m is "available own funds (before regulatory req's)". Tyro is a bank and must hold capital, so not all of it is surplus. Tyro's free cash flow (A$29.4m) is before tax, interest, share-based pay and one-offs [T2]. Its EV to free cash flow is 7.7 times if all the own funds are surplus and 12.6 times if none are. Applying that multiple to an EML "proforma" figure of unknown definition mixes bases.
7. The "our way" case counts all 63.6m performance rights as vested. They are tied to share price hurdles (cumulative return of 30% to 40% over three years from bases of about A$0.75 to A$1.07) and would mostly lapse without a bid; with a bid all 66.3m unquoted rights vest [A1 remuneration report][A18].
8. Tendren: the A$7.0m for 28% of Mobilata International (renamed Tendren) is an investment in a company in which the Executive Chair, Anthony Hynes, separately holds an interest; the annual report says the holding "may grow over time" [A1 note 28, release]. EML also lent A$3.8m to a client [A2].
9. EML left the All Ordinaries on 21 September 2026 and was not in the S&P/ASX 300 [A17].
10. Mr Hynes's on-market buy (6 to 12 March 2026, A$0.60 to A$0.61) came four weeks before the 13 April guidance cut [A13][A10]. It was not a signal about that half's trading.
11. Last year's AGM affirmed FY26 guidance of A$58m to A$63m although first-quarter underlying EBITDA was A$6.8m, 42% down; the year came in at A$48.3m [A9][A1]. An AGM update is a weak test.
12. The cost of the APRA-required bank guarantee will be left out of underlying EBITDA, so FY27 already has a new "non-recurring" line [A10]. "Not material" referred to the guarantee only, not to capital under an ADI licence [A12].

## The company in plain words
EML runs prepaid card programs for other businesses: gift and incentive cards for shopping centres and retailers (Europe, North America), general purpose reloadable cards for salary packaging in Australia and for government and corporate payments in the UK and Europe, and virtual card numbers for business payments in North America [A1 segments]. It earns transaction and account fees, breakage (balances never spent), establishment fees and, separately, interest on the money cardholders have loaded but not spent. In FY26 customer revenue was A$150.3m (transaction A$107.8m, breakage A$14.9m, account fees A$10.4m, establishment A$13.3m, other A$3.9m) and interest A$56.7m (on stored value A$26.6m, on bonds A$29.5m, on its own cash A$0.7m) [A1 note 3]. Segments: Europe A$111.8m revenue and A$35.7m underlying EBITDA, Asia Pacific A$56.5m and A$10.4m, North America A$39.0m and A$7.1m, corporate costs A$5.0m [A1 note 2]. The top 30 customers give about 47% of revenue excluding interest, the top 5 about 23%, the largest about 8% [A2].

Who runs it: Anthony Hynes, Executive Chair since December 2024 (founder of eNett, sold with Optal in 2020 for about A$940m, then at WEX); Adam Olding, CEO since 30 March 2026; Stuart Will, CFO since 1 December 2025. Non-executive directors: Ken Poutakidis (deputy chair), Petrina Coventry, Andre Reich [A1][A11].

Who owns it (31 July 2026 register and later notices) [A1 ASX additional information][A14][A15][A16]: Copia Investment Partners 48,550,000 (12.49% on 13 May 2026), QVG Capital 32,937,625 (8.43% on 28 September 2026), Viburnum Funds 20,385,106 (5.23%, notice of 2 September 2026), Argo Investments 14,390,447 (3.69%), Hynes 4,917,569 shares (1.26%) plus 11,111,111 performance rights. Regal Partners sold out by 2 September 2026 and Wilson Asset Management by 27 February 2026 [A16][W1]. The top 20 held 67.09%; 7,746 holders held unmarketable parcels.

Five years: year-end closes A$3.23 (2021, high A$5.89), A$0.63 (2022), A$0.79 (2023), A$0.835 (2024), A$0.925 (2025), A$0.215 on 30 October 2026 and A$0.28 on 6 November [M2][M1]. Statutory losses every year: A$284.8m (FY23), A$26.5m (FY24), A$53.4m (FY25), A$19.7m (FY26) [A5][A3][A1]. The 2026 fall (A$0.92 in January to A$0.19 in October) came through the February half-year result, the April guidance cut, index removal and holder exits [M2].

## Why big investors may be overlooking it
- Size: A$110m market value.
- Index: removed from the All Ordinaries on 21 September 2026; not in the S&P/ASX 300 [A17]. Funds tracking the All Ordinaries had to sell around that date.
- Holders leaving: Wilson Asset Management (out February 2026), Regal (out September, selling at A$0.24 to A$0.26), Viburnum (7.85% to 5.23%), QVG (sold 3.8m at an average A$0.39 between March and September) [W1][A16][W2][A15].
- A messy history: regulators in the UK and Ireland (2021 to 2023), the PCSIL liquidation, a A$37.4m class action settlement, takeover talks in 2022 that went nowhere, a strategic review in 2023, and a November 2024 plan whose FY28 targets have since been cut [A20][A21][A8][A1].
- Analyst coverage: I didn't check broker coverage. Edison Group, a paid research firm, has a page on EML [W3].
These explain why the price can sit away from value. They don't by themselves make it cheap: several are reasons for a discount.

## What the filings show

### Earnings, and the gap between underlying and reported
| A$m | FY23 | FY24 | FY25 | FY26 | Source |
| --- | --- | --- | --- | --- | --- |
| Revenue (statutory, restated for businesses sold) | 183.9 | 202.1 | 221.8 | 207.0 | [M1][A3][A1] |
| Underlying EBITDA | 36.7 | 49.0 (51.8 restated) | 58.6 | 48.3 | [A5][A3][A1] |
| Reported EBITDA (company's "operating EBITDA") | 8.6 | 38.1 | 30.5 | 14.4 | [A5][A3][A1] |
| Items added back as "non-recurring" | 28.1 | 10.9 (10.7 restated) | 28.2 | 33.9 | [A5][A3][A1] |
| Share-based pay (below EBITDA, issued as shares) | 1.6 | 9.9 | 15.4 | 15.0 | [A5][A3][A1] |
| Statutory loss after tax | -284.8 | -26.5 | -53.4 | -19.7 | [A5][A3][A1] |

FY26 underlying EBITDA fell 18% as customer revenue fell 4% (A$10.8m of FY25 revenue from exited customers did not recur) and interest fell 11% [A1]. Net overheads were A$104.1m, and the FY27 guidance assumes they rise to "the longer-term average of ~$110m" [A2]. FY27 guidance of A$50m to A$54m therefore needs gross profit of about A$160m to A$164m, up 5% to 8% on FY26's A$152.4m, with customer revenue growth and yields "forecast to improve ~20bps" [A2].

Guidance record: FY24 guidance of A$52m to A$58m (November 2023) was met on the group basis given (A$57.1m including PCSIL) [A21][A5]; FY25's A$54m to A$60m was met (A$58.6m) [A3]; FY26's A$58m to A$63m was affirmed at the AGM despite a weak first quarter, "tightened" to A$58m to A$60m in February, cut to A$47m to A$50m on 13 April and delivered at A$48.3m [A9][A6][A10][A1].

### The "non-recurring" items, line by line
EBITDA add-backs in each year's reconciliation, A$m [A5 performance overview][A3 performance overview, note 2][A1 performance overview, note 2][A2 page 25]:

| Item | FY23 | FY24 | FY25 | FY26 | FY27 and FY28, my read |
| --- | --- | --- | --- | --- | --- |
| Restructuring and strategy establishment (termination payments, strategic work) | 7.3 | 3.0 | 6.5 | 15.3 | Every year. A$7.4m of it fell in 2H FY26, the half the company says restructuring finished [A7 page 27][A2 page 4]. The Sofia operations centre is to grow in FY27 and Arlo's migrations are meant to save at least A$12m a year, mostly roles: both mean more termination payments through FY29. Expect A$3m to A$6m a year, not nil. |
| Regulatory remediation and class action costs | 14.0 | 0.7 | 9.5 | 1.4 | Lumpy but present in all four years. The Australian ADI application and guarantee are the next round [A11][A12]. A$1m to A$4m a year. |
| Fraud losses | 6.1 | | | | Ended, but replaced by later categories. |
| PCSIL separation | | 7.1 | 1.0 | | Ended. A$0.8m still owed to the liquidator [A1 note 19]. |
| Legacy tax obligations | | | 8.4 | 1.2 | Probably ending. |
| Arlo, expensed part | | | 2.8 | 4.2 | Company plan: A$15.7m of non-recurring Arlo spending in FY27 (expensed and capitalised), A$2.4m in FY28, A$1.0m in FY29 [A1 release]. The budget was A$12m to A$15m in November 2024, A$15m for FY26 alone in August 2025, then A$20m, now A$34m, with migrations running to 2029 [A8][A4][A1]. 1H FY26 expensed A$4.5m, the full year A$4.2m, so some was moved to capitalised in the second half [A7][A1]. A further overrun is more likely than not. |
| Stored value shortfall, and a related receivable | | | | 11.7 | A$13.6m provision, cash still to be paid; the review "expect[s] to conclude by the end of 2026 calendar year", so the figure can still move [A1 notes 21, page 15]. |
| AASB 3 fair value | 0.7 | | | | Ended. |
| ADI guarantee (new) | | | | | To be left out of underlying EBITDA from FY27 [A10]. |
| **Total** | **28.1** | **10.7 to 10.9** | **28.2** | **33.9** | Four years: A$100.8m, average A$25.2m; excluding Arlo and PCSIL, A$21.5m a year. |

Below EBITDA, FY25 also carried the A$37.4m class action settlement, paid in FY26 as A$40.9m with fees [A1].

The test the brief set: does the label hold? Restructuring, regulatory remediation and some new category have each recurred. One year in four (FY24) was low, at about A$11m. On this record the right base case is that "non-recurring" costs fall from FY26's peak but keep running at A$10m or more a year, not that they fall to Arlo's A$2.4m.

### Cash: what the business has actually produced
Free cash flow as the cash flow statement shows it (operating cash flow less equipment, capitalised software and lease principal), A$m [A5][A3][A1]:

| | FY23 | FY24 | FY25 | FY26 |
| --- | --- | --- | --- | --- |
| Operating cash flow | -2.3 | 14.1 | 16.7 | -26.5 |
| Capital spending | -11.7 | -9.2 | -6.0 | -12.9 (A$8.9m Arlo) |
| Lease principal | -2.2 | -1.9 | -1.7 | -2.5 |
| Free cash flow | -16.2 | 3.0 | 9.1 | -41.9 (-0.9 before the class action) |
| Tax paid / interest paid | 0.1 / 2.0 | 12.0 / 6.1 | 8.0 / 5.4 | 0.7 / 6.1 | 

Four years: A$192.6m of underlying EBITDA, minus A$46.0m of free cash flow, about minus A$5m before the class action payment. FY23 and FY24 include PCSIL and Sentenial, which were losing money and were later liquidated or sold, so the gap is overstated for those years; FY25 and FY26 are continuing businesses only.

The company's own bridge for FY26 (page 18 of [A2]): underlying EBITDA A$48.3m, plus A$6.4m of working capital and interest received (helped by collecting interest accrued in FY25), less A$6.1m interest paid and A$0.7m tax, gave "underlying operating cash flow" of A$47.8m. Then the class action (A$40.9m), other one-offs (A$20.4m, after A$5.5m of insurance settlement received) and Project Arlo (A$13.0m) took it to minus A$26.5m. The bridge puts A$13.0m of Arlo inside operating cash flow, and the cash flow statement shows A$8.9m of Arlo capitalised under investing; the accounts show A$4.2m expensed and A$8.9m capitalised [A1][A2]. I could not reconcile these: FY26 Arlo cash was A$13m to A$22m against the A$15m guided in August 2025 [A4].

By half: 1H FY26 operating cash flow was minus A$33.2m (class action paid) and 2H plus A$6.7m. Capital spending was A$4.2m in 1H and about A$8.7m in 2H, so the second half, with no class action, was still about minus A$3m after capital spending and leases [A6][A7][A1].

### What "proforma" free cash flow includes
The phrase appears twice, with no definition: "Proforma free cash flow of $30-$35m forecast in FY28 as the bulk of Arlo, transformation and legacy remediation expenditure falls away" (results release) and "FY28 $30m-$35m proforma Free Cash Flow forecast as non-recurring cash outflows materially reduce" (presentation) [A1 release][A2 page 20]. Three clues:
1. EML's other cash measure, "underlying operating cash flow", is underlying EBITDA plus working capital, less interest and tax, with every item EML calls non-recurring added back (A$74.3m in FY26, A$25.5m in FY25) [A2 page 18][A4].
2. The November 2024 plan set FY28 targets of "~A$95m EBITDA", "~35% EBITDA margin", "~13c earnings per share" and "~60% Free Cashflow", the last read naturally as cash conversion of EBITDA [A8 page 29]. A$30m to A$35m at 60% implies FY28 underlying EBITDA of about A$50m to A$58m.
3. "As the bulk of Arlo ... falls away" says some Arlo remains (A$2.4m in FY28), and "proforma" in EML's usage, like "underlying", is a before-one-offs number.
My reading, which the company should confirm at the AGM: proforma free cash flow is underlying EBITDA less interest, tax, ordinary capital spending and leases, with the remaining Arlo and anything else labelled non-recurring left out, and with share-based pay (A$15m a year, issued as shares) ignored as non-cash. On my scenarios below, that measure comes out at A$28m (bad), A$34m (middling) and A$39m (good) in FY28, against true free cash flow of A$6m, A$21m and A$35m. The forecast can be "met" in most outcomes, so meeting it won't settle the question by itself.

### Customer funds, regulatory capital and free cash
At 30 June 2026, A$m [A1 notes 13, 19, 20, 21, 23, 27][A2 pages 17, 26, 27]:

| Layer | A$m | Free for shareholders? |
| --- | --- | --- |
| Owed to cardholders (stored value, payable on demand) | 2,205.2 | No. |
| Held against it: bank deposits 1,503.3, bonds 722.8 | 2,226.1 | No. The A$20.9m above the liability is the bonds' amortised cost over par, recovered through the yield, not cash EML can withdraw. Bonds' fair value was A$720.4m. |
| Interest earned on it in FY26 | 56.7 | Yes, as income: 27% of revenue. A$0.5bn of the Australian float earns EML nothing. About 45% of the float's yield was locked for three years in 2025 [A9]. |
| EML's own cash | 37.8 | Only partly. The UK's Electronic Money Regulations and the EU directive Ireland applies require own funds of 2% of average e-money outstanding [R1][R2]: about A$29m on the A$1,463.8m of pound and euro float, held inside the regulated subsidiaries. The filings don't say how much of the A$37.8m that ties up. The parent "has offered financial support to some of its wholly owned subsidiaries ... This may give rise to a future cash outflow which is unknown" [A1 note 27]. A$13.6m is owed under the shortfall provision. |
| Possible new requirement | up to 21.4 | If APRA licenses EML's Australian issuer, its standard for purchased payment facility providers sets a minimum of 4% of stored value liabilities in common equity [R3]. On all A$534.5m of Australian dollar float that is A$21.4m; only "certain" programs are covered, so it is an upper bound. EML hasn't said what it expects to hold. Treasury's draft reforms (March 2026) would remove the need [A11]. |
| Tangible equity | 22.4 (5.9 after the A$16.5m tax asset) | Net assets A$130.1m less A$107.7m of goodwill and software. |
| Bank debt drawn / undrawn | 84.0 / 31.0 | Gearing covenant 0.41 against 0.45. |

The plain reading: the group's regulated capital is in effect funded by the parent's bank debt, so none of the cash is spare, and the A$31m undrawn facility is what funds FY27's shortfall payment and Arlo.

### Debt and covenants
A$50m four-year term loan (to 26 September 2029, fully drawn) and a A$65m syndicated facility (to 26 September 2028, A$34m drawn), margins 3.25% to 4.5% over floating rates [A1 note 19]. Covenants tested each 31 December and 30 June: gearing no more than 0.45 (0.407 at June 2026: A$89.3m of debt including leases, against A$130.1m of equity); senior debt no more than 2.5 times EBITDA "as adjusted ... including extraordinary non-recurring gains and losses" (about 1.7 times on underlying); interest cover at least 5 times. The syndicated facility falls due inside a 24-month window, on 26 September 2028.

### Other things a quick reader would miss
- The FY28 target has already been cut. November 2024: FY28 underlying EBITDA about A$95m, margin about 35%, earnings about 13c a share, cost base flat at about A$105m, Arlo capital spending A$12m to A$15m with A$8m to A$12m of savings by FY27 [A8]. August 2026: FY27 EBITDA A$50m to A$54m, overheads about A$110m, Arlo A$34m with savings of at least A$12m "on full deployment", migrations to FY29, and a proforma free cash flow target [A1][A2].
- Goodwill (A$78.3m) is supported by forecasts of revenue growth of 7% (Europe), 11% (Asia Pacific) and 14% (North America) a year to FY31; revenue fell 6% in FY26 [A1 note 16]. Since late June 2026 the market value has mostly been below net assets (A$130.1m, about A$0.33 a share) [M2].
- FY26 operating cash flow included A$5.5m of insurance settlement and the collection of interest accrued in FY25 [A1][A2].
- EML holds Visa shares worth A$3.9m, a small surplus asset [A1 note 22].
- Takeover history: Bain Capital discussed a change of control proposal early in 2022 and two parties did so in June 2022; all discussions ceased [A20]. The 2023 strategic review sold Sentenial and exited PCSIL; the group was not sold [A21].

## Valuation
Cash earnings, not accounting profit: the measure is equity free cash flow, underlying EBITDA less interest, tax, ordinary capital spending (A$5m a year, about FY25 and FY26 levels before Arlo), lease payments (A$2.5m) and the "non-recurring" cash costs I expect to recur. Share-based pay is counted as dilution of 2% a year (EML issued 1.8% in FY25 and 1.7% in FY26 [A1 note 24]). Opening adjusted net debt is A$60.4m (bank debt, premium funding and the PCSIL loan, less cash, plus the shortfall provision) [A1].

Three paths, A$m:

| | FY27 | FY28 | FY29 | FY30 |
| --- | --- | --- | --- | --- |
| Good: guidance met then growth, Arlo on budget, one-offs fade | EBITDA 53, one-offs 19.7, FCF 16.3 | EBITDA 58, one-offs 4, FCF 35.0 | 61, 2, FCF 40.0 | 62, 1, FCF 42.0 |
| Middling: guidance low end, Arlo overruns a little, one-offs fall but recur | 50, 24, FCF 9.0 | 52, 13, FCF 21.0 | 54, 10, FCF 25.5 | 55, 8, FCF 28.5 |
| Bad: guidance missed, record continues, shortfall up A$4m | 46, 35, FCF -6.0 | 46, 22, FCF 6.0 | 47, 18, FCF 11.0 | 47, 16, FCF 13.0 |

Interest A$6.5m a year (A$7.5m in the bad case from FY28), tax paid A$3m to A$6m. Net debt in June 2028: A$9m (good), A$30m (middling), A$60m (bad). The company-style proforma figure for FY28 on these paths: A$39m, A$34m, A$28m.

Method 1, a multiple of equity free cash flow. Payments companies are priced on cash. Tyro, the nearest ASX payments name, trades at 7.7 to 12.6 times its free cash flow before tax and interest, depending on how much of its A$145.3m own funds is surplus to its bank capital needs (A$370.6m market value at A$0.695 on 30 October, 533,172,818 shares) [T2][T3][M2]. On EV to EBITDA it is 3.4 to 5.5 times. The payments companies Qatalyst used for Payoneer's sale traded at 3.8 times (WEX) to 10.7 times (Corpay) 2026 EBITDA in June 2026, with Paysafe at 5.9 times and PayPal at 5.5 times; Payoneer was sold to Nuvei at US$7.40, about 7.8 times plan EBITDA and 8.1 times next-year consensus by my interpolation of Qatalyst's ranges [P1]. EML's history (losses in each of the last four years, missed targets, regulators, heavy share-based pay at 31% of underlying EBITDA against Tyro's 7%) earns a discount to Tyro. I use 8 times FY28 equity free cash flow in the middling case, 9 times in the good, 6 times in the bad: on 405m shares in September 2028, A$0.78, A$0.42 and A$0.09.

Method 2, a discounted cash flow of equity free cash flow. Cost of equity 13% (EML's goodwill tests use 11.7% to 11.8% after tax, a whole-company rate that includes cheaper debt [A1 note 16]; equity in a levered small company with this record costs more), growth after FY30 of 1% (float interest and gift card volumes have not been growing). That is 8.3 times next year's cash flow at the end, in line with Method 1. Values per share:

| Path | Today (8 Nov 2026) | Mid-March 2027 | September 2028 (DCF / multiple) |
| --- | --- | --- | --- |
| Good | A$0.68 | A$0.71 | A$0.83 / A$0.78 |
| Middling | A$0.40 | A$0.42 | A$0.50 / A$0.42 |
| Bad | A$0.07 | A$0.07 | A$0.11 / A$0.09 |

```
mid: FCF FY27-30 [9.0, 21.0, 25.5, 28.5]; company-style 'proforma' FY28 34.0; net debt Jun27 51.4 Jun28 30.4
     value Sep 2028: DCF A$0.499, 8x FY28 FCF A$0.415; Mar 2027 A$0.418; today A$0.398
```

Cross-check, what a buyer could pay: at 5 to 6 times FY27 guidance midpoint (A$52m), less adjusted net debt and leases, on 457.6m shares with every right vested, A$0.43 to A$0.54 a share; at Payoneer's 8 times, A$0.77. A buyer would also cut overheads, which the listed company can't count on.

The range, weighted by my chances (bad 43%, middling 44%, good 13%, from the signal weights below): about **A$0.29 today**. It depends most on the cost of equity, because the debt is fixed and the value sits in later years: A$0.39 at 11%, A$0.25 at 14%, A$0.22 at 15%. The next biggest input is whether FY28 one-offs are A$4m, A$13m or A$22m.

The fact sheet's anchors re-tested. "Our way", A$0.40: 7.66 times A$30m less A$46.9m, on 454.89m shares. Its pieces are off (the multiple deducts all of Tyro's regulated capital and is on a pre-tax, pre-interest basis; A$30m of "proforma" cash is probably before the one-offs; net debt leaves out the shortfall provision; rights only vest in a bid), but it lands near my middling value, which is reached in 2028, not in six months. "Against us", A$0.12: close to my bad path.

## The players and what the rules allow
Included because the brief frames this as a holder build-up to watch; it is an ordinary research pick, not a special situation.
- Copia Investment Partners, 12.49% (48.55m shares), a Melbourne fund manager. Became substantial on 28 November 2025 at 22.54m (5.81%), with buys at A$0.84 to A$1.05 in the second half of 2025 by its notice's trade table; added 4.15m at A$0.69 (February 2026), 3.01m at A$0.44 (April) and 4.14m at A$0.40 (May) [A14]. No notice since 13 May, so it still holds between 11.5% and 13.5%. It carries a large loss and has not said anything about intentions.
- QVG Capital 8.43%, Viburnum 5.23%: both selling this year [A15][W2].
- The board: the Executive Chair holds 1.26% and 11.1m performance rights; he bought A$606,046 of shares in March [A13][A1].
- What the rules allow: a holder below 20% can buy on market; above 20% only through a bid or 3% every six months. The AGM is asked to renew the proportional takeover approval rule for three years [A19]. A change of control vests all 66.3m unquoted rights, 17% more shares [A1 remuneration report].
- Comparable cases: the 2022 approaches (Bain Capital, then two parties) ceased without an offer, at prices far above today's [A20]. Nothing in the filings shows an approach now.
- If nothing happens, the value is the probability-weighted A$0.29, with the bad path at A$0.07 to A$0.11.

## Why the market is wrong
At A$0.28 I can't say it is. The price implies, on my cost of equity, steady equity free cash flow of about A$21m a year from FY28, which is my middling path with a little more caution. The market has taken in the one-off record, the debt and the record of targets. At A$0.215 on 30 October it was pricing something closer to my bad path, and the 30% rise in the week to 6 November, with no announcement, closed most of that gap. ASIC data show short interest fell from 16.0m shares (4.1%) on 1 September to 6.1m (1.6%) on 26 October, the latest in the repo, so covering can't explain much of the rise [M3]. I found no explanation.

What would make the market wrong, in either direction, is the half-year result: it will show one-off costs line by line, Arlo's spend against its budget, the shortfall's final figure and the cash flow before the shortfall payment.

## Outcomes and chances
For an ordinary pick, resolving by 12 March 2027, two weeks after the expected half-year result. The half-year result moves the market's weights across the three paths above; each price is the weighted path value in mid-March 2027 (valuation table above).

| Outcome | What happens | Chance | Price by resolve date |
| --- | --- | --- | --- |
| Bad | The half shows the record continuing: FY27 guidance cut, or one-offs outside Arlo above A$8m in the half, or Arlo's budget raised again, or the shortfall above A$13.6m, or a capital raising or covenant waiver. Market weights paths 0% good, 30% middling, 70% bad | 40% | A$0.18 |
| Middling | Underlying EBITDA in line with A$50m to A$54m, one-offs falling but still present, operating cash flow negative only because of the shortfall payment and Arlo. Weights 15%, 55%, 30% | 45% | A$0.36 |
| Good | Guidance held or raised, one-offs outside Arlo under A$4m in the half, Arlo on budget, cash flow positive before the shortfall payment, proforma free cash flow defined and reaffirmed; or a bid at 5 to 6 times EBITDA (A$0.43 to A$0.54). Weights 40%, 50%, 10% | 15% | A$0.50 |

Each price comes from the discounted cash flow values in mid-March 2027 (good path A$0.71, middling A$0.42, bad A$0.07), weighted as stated. The chances imply 13% / 44% / 43% across the three paths, which is what my probability-weighted A$0.29 uses.

Expected price: 0.40 x 0.18 + 0.45 x 0.36 + 0.15 x 0.50 = **A$0.309**, +10.4% before costs.

Round-trip costs on the largest position (A$2,016, NZ$2,500 at NZ$1 = A$0.806387 on 6 November [M4]): spread 1.8% (Corwin and Schultz over 60 sessions; one price step is 1.75% and the 6 November quote was two steps wide, 3.5%); size cost 0.49% each way (daily volatility 4.6% over 20 sessions, times the square root of A$2,016 over the A$177,554 average day); brokerage A$15 each way (0.74%) unless the plan's monthly cover applies; 0.5% each way to convert if Australian dollars aren't held. That is 2.8% to 7.0%; I use **5.0%**.

**Expected return after costs: about +5.4%**, against the minimum of +2.4% (2.13% cash rate plus 5%, over the 123 days to 12 March 2027). It clears on these inputs, but only just: with bad 45%, middling 45%, good 10% it is about 0%, and at a 14% cost of equity the expected price is A$0.27 (-8.6% after costs). Since the price is within 4% of my probability-weighted value, I can't name a mispricing, so this goes to "wait", not to the red team. A quarter-Kelly stake on the central inputs would be 6.8% of the portfolio, cut to the 2.5% cap.

Value pick test (24 months, FY28 result, resolve by 8 September 2028): bad A$0.10 (-64%), middling A$0.46 (+63%), good A$0.80; expected A$0.366, +30.8% before costs and +25.8% after against a minimum of +13.1%. It fails the bad-case limit of -10% by a wide margin, so it can't be held as a value pick.

## Dated events
- **18 November 2026: AGM** (10am Sydney) [A19]. Last year's AGM carried a first-quarter trading update [A9]. Look for: first-quarter FY27 underlying EBITDA (A$12m or more fits the guidance; last year's A$6.8m preceded a miss), FY27 guidance affirmed, a definition of proforma free cash flow, the stored value shortfall's progress. A good AGM alone doesn't reopen the case, since last year's affirmation was followed by a cut.
- **31 December 2026**: covenant test date; the shortfall review is due to conclude by the end of the calendar year [A1].
- **January 2027**: advance notice of the half-year result (inferred from 19 January 2026).
- **About 25 February 2027: 1H FY27 result** (inferred from 25 February 2026 [A6]). The deciding event. Reopen as an ordinary pick, resolving at the FY27 result in late August 2027, if all of these hold and the price is at or below about A$0.45 (that outcome's A$0.50 value, less costs, the minimum gain and a margin):
  1. Underlying EBITDA for the half of A$25m or more and FY27 guidance of A$50m to A$54m held.
  2. One-off add-backs outside Arlo of A$4m or less for the half (1H FY26 had A$9.3m, 2H FY26 A$20.4m including A$11.7m for the shortfall), with no new category above A$1m.
  3. Arlo's non-recurring spend for the half of A$9m or less, the A$34m budget and the timetable unchanged.
  4. The shortfall settled at or below the A$13.6m provision.
  5. Operating cash flow before the shortfall payment positive, drawn debt A$95m or less, gearing 0.43 or less.
  6. Proforma free cash flow defined; if it is before interest and tax, cut the A$30m to A$35m by about A$10m before using it.
  If the half is in line but these don't all hold (the middling outcome, worth about A$0.36), reopen only at A$0.32 or lower.
  Close it (no case) on a guidance cut, one-offs outside Arlo above A$8m in the half, a higher Arlo budget, the shortfall above the provision, a covenant waiver or an equity raising.
- **Watch trigger before then: A$0.25 or lower**, with nothing else changed. At A$0.25 the expected gain after costs is about +18.6% on the central inputs and still clears the minimum with bad at 45% or at a 14% cost of equity, so the price would be clearly below value.
- **A change of control approach** at any time: reopen as a special situation (all rights vest; 5 to 6 times FY27 EBITDA is A$0.43 to A$0.54 a share).
- Later: ADI licence decision expected by about May 2027 (company expectation [A12]); mobility product launch mid 2027 [A1]; FY27 result late August 2027; FY28 result, which answers the free cash flow question, late August 2028; the A$65m syndicated facility falls due on 26 September 2028 [A1].

## What would make this wrong
1. The "non-recurring" costs keep coming at A$20m or more a year (their four-year average is A$25m, or A$21.5m outside Arlo and PCSIL). Then FY28 free cash flow is near A$6m, not A$30m; FY27's shortfall payment and Arlo push net debt towards A$65m, and the gearing covenant (0.41 against 0.45) or APRA capital forces a waiver or an equity raising at a low price.
2. The FY27 revenue step doesn't arrive. Guidance needs gross profit up 5% to 8% with overheads up to about A$110m, after FY26 missed by about A$10m. A 0.25% cut in rates costs about A$4.1m a year, and northern hemisphere gift card trading has been weak.
3. The other way, for "wait": a bid. The register is concentrated, the business generates A$57m of float interest, and 5 to 6 times EBITDA would be A$0.43 to A$0.54 a share. Nothing in the filings shows one.
Exit rule if it is ever bought: sell on a guidance cut, a new non-recurring line above A$3m, an equity raising, a covenant waiver or gearing above 0.43, and at the resolve date if the half's conditions above aren't met.

## Checks
- Not on Cam's excluded list: config/judgement_excluded.csv has no entries (confirmed by Cam on 8 November 2026).
- No placement-pattern reopening in the last 30 sessions (21 September to 30 October 2026): no trading halt in 2026 [A22], and no opening 5% or more below the previous close in that window [M2].
- Liquidity (re-checked first): median daily traded value A$123,896 over 5 to 30 October 2026, lowest day A$21,482 [M2]. Section 3's limit (two sessions at 10% of the median day) is A$24,779; the research pick cap of 2.5% (about A$2,016) binds first.

## What I couldn't verify
- How much of the A$37.8m of cash sits in regulated subsidiaries, and what own funds each holds; the accounts give no split.
- Which Australian programs APRA treats as purchased payment facilities, and what capital EML expects to hold under an ADI licence.
- The definition of proforma free cash flow.
- FY26 Arlo cash (A$13.0m in the operating bridge and A$8.9m capitalised, against A$13.1m in the accounts).
- The cause of the rise from A$0.215 to A$0.28; daily prices for 2 to 5 November are not in the repo.
- Copia's holding since 13 May 2026, and the full trade table in its first notice (read by OCR; the tables are images).
- How much of Tyro's A$145.3m is surplus to its bank capital needs, and Tyro's price after 30 October.
- First-quarter FY27 trading, which isn't out yet.

## Sources
- [A1] 2026 Appendix 4E and Annual Report, 18 Aug 2026 (03126182): release, performance overview (reconciliation, pages 13 to 17), notes 2(f), 2, 3, 13, 16, 17, 19, 20, 21, 22, 23, 24, 26, 27, 28, remuneration report, ASX additional information: https://announcements.asx.com.au/asxpdf/20260818/pdf/072vww3jvymxwc.pdf
- [A2] FY26 Results Investor Presentation, 18 Aug 2026 (03126187): https://announcements.asx.com.au/asxpdf/20260818/pdf/072vx7c3wvy876.pdf
- [A3] 2025 Appendix 4E and Annual Report, 27 Aug 2025 (02986090): https://announcements.asx.com.au/asxpdf/20250827/pdf/06nddl8xk0c0k1.pdf
- [A4] FY25 Results Investor Presentation, 27 Aug 2025 (02986170): https://announcements.asx.com.au/asxpdf/20250827/pdf/06ndl12j6r01jy.pdf
- [A5] 2024 Appendix 4E and Annual Report, 28 Aug 2024 (02845354): https://announcements.asx.com.au/asxpdf/20240828/pdf/0674nxmmx1wdkz.pdf
- [A6] EML Announces 1HFY26 results, 25 Feb 2026 (03064563): https://announcements.asx.com.au/asxpdf/20260225/pdf/06wqbfzq6cd51z.pdf
- [A7] 1HFY26 Investor Presentation, 25 Feb 2026 (03064565): https://announcements.asx.com.au/asxpdf/20260225/pdf/06wqbl8dmqc5k8.pdf
- [A8] EML 2.0 Strategy Plan Investor Presentation & Trading Update, 26 Nov 2024 (02886807): https://announcements.asx.com.au/asxpdf/20241126/pdf/06bv8k7xcckcbz.pdf
- [A9] AGM Trading Update, 19 Nov 2025 (03028371): https://announcements.asx.com.au/asxpdf/20251119/pdf/06s5t7v4cz5lny.pdf
- [A10] FY26 Underlying EBITDA Guidance Revised, 13 Apr 2026 (03081864): https://announcements.asx.com.au/asxpdf/20260413/pdf/06yf139py9nwz7.pdf
- [A11] Global CEO Appointment and Australian Regulatory Update, 30 Mar 2026 (03077129): https://announcements.asx.com.au/asxpdf/20260330/pdf/06xy6gx7ykwg97.pdf
- [A12] Australian Regulatory Update, 1 May 2026 (03089231): https://announcements.asx.com.au/asxpdf/20260501/pdf/06z3vc8cl1ln20.pdf
- [A13] Change of Director's Interest Notice (Hynes), 13 Mar 2026 (03071606): https://announcements.asx.com.au/asxpdf/20260313/pdf/06xcqx8w0yxyjg.pdf
- [A14] Copia notices (trade tables read by OCR): becoming substantial, 3 Dec 2025 (03036602) https://announcements.asx.com.au/asxpdf/20251203/pdf/06sx3kpz13jbnr.pdf ; 2 Mar 2026 (03067401) https://announcements.asx.com.au/asxpdf/20260302/pdf/06wz644lr39nbr.pdf ; 17 Apr 2026 (03083922) https://announcements.asx.com.au/asxpdf/20260417/pdf/06ylwsgb094srq.pdf ; 18 May 2026 (03095007) https://announcements.asx.com.au/asxpdf/20260518/pdf/06zq0rkh5pl7dq.pdf
- [A15] Change in substantial holding (QVG Capital), 30 Sep 2026 (03146446): https://announcements.asx.com.au/asxpdf/20260930/pdf/074rg6k0mzbmzy.pdf
- [A16] Ceasing to be a substantial holder (Regal Partners), 4 Sep 2026 (03136169): https://announcements.asx.com.au/asxpdf/20260904/pdf/073rf3vs2d7jtr.pdf
- [A17] S&P DJI Announces September 2026 Quarterly Rebalance, 4 Sep 2026 (03136141): https://announcements.asx.com.au/asxpdf/20260904/pdf/073rbz4q8nrckg.pdf
- [A18] Notification of cessation of securities, 8 Oct 2026 (03150095): https://announcements.asx.com.au/asxpdf/20261008/pdf/07530k0z46mzfj.pdf
- [A19] EML 2026 Notice of Annual General Meeting, 19 Oct 2026 (03153951): https://announcements.asx.com.au/asxpdf/20261019/pdf/075h23xm3264bb.pdf
- [A20] Response to Media Speculation, 13 Apr 2022 (02510091): https://announcements.asx.com.au/asxpdf/20220413/pdf/457zh2d0bzxcgb.pdf ; 18 Jul 2022 (02542779): https://announcements.asx.com.au/asxpdf/20220718/pdf/45by0f5b586r4g.pdf
- [A21] Trading and Strategic Review Update, 29 Nov 2023 (02747369): https://announcements.asx.com.au/asxpdf/20231129/pdf/05xydmh4jqgqqw.pdf
- [A22] ASX announcements list for EML, 2022 to 2026: https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=EML&timeframe=Y&year=2026
- [W1] Ceasing to be a substantial holder from WAM/WMI, 3 Mar 2026 (03067958): https://announcements.asx.com.au/asxpdf/20260303/pdf/06x0r4vr368dxf.pdf
- [W2] Change in substantial holding (Viburnum Funds), 2 Sep 2026 (03134907): https://announcements.asx.com.au/asxpdf/20260902/pdf/073mzlrqcrrrly.pdf
- [W3] Edison Group, EML Payments page (secondary, used only for the coverage point): https://www.edisongroup.com/equity/eml-payments/
- [T2] Tyro FY26 Results Investor Presentation, 25 Aug 2026 (03129472), free cash flow and own funds pages: https://announcements.asx.com.au/asxpdf/20260825/pdf/0735d1dhxm52dr.pdf ; Tyro FY26 Results ASX Release (03129465): https://announcements.asx.com.au/asxpdf/20260825/pdf/0735ckg507b2bg.pdf
- [T3] Tyro Application for quotation of securities, 5 Nov 2026 (03162638), 533,172,818 shares: https://announcements.asx.com.au/asxpdf/20261105/pdf/0768tn485v74fw.pdf
- [P1] Payoneer Global Inc. definitive merger proxy (DEFM14A), 11 Aug 2026, Qatalyst Partners' analyses: https://www.sec.gov/Archives/edgar/data/1845815/0001104659-26-094105.txt (deal terms also in data/sec/us_deal_targets.csv)
- [R1] UK Electronic Money Regulations 2011, Schedule 2 paragraph 23 (own funds 2% of average outstanding e-money): https://legislation.gov.uk/uksi/2011/99/schedule/2/paragraph/23/2011-02-09?view=plain
- [R2] Directive 2009/110/EC, Article 5(3) (at least 2% of average outstanding e-money): https://www.legislation.gov.uk/eudr/2009/110/article/5/data.htm
- [R3] APRA Prudential Standard APS 610, Prudential Requirements for Providers of Purchased Payment Facilities (June 2023), paragraph 13 (4% of stored value liabilities): https://www.apra.gov.au/sites/default/files/2023-05/Prudential%20Standard%20APS%20610%20Prudential%20Requirements%20for%20Providers%20of%20Purchased%20Payment%20Facilities%20-%20clean_0.pdf
- [M1] data/research_data/asx_company.json, EML, fetched 7 Nov 2026 UTC: last trade A$0.28 (6 Nov), close A$0.265 (5 Nov), bid A$0.28, ask A$0.29, 391,262,494 shares.
- [M2] data/norgate/universe/prices_2021.csv.gz to prices_2026.csv.gz (Norgate), EML.au and TYR.au, to 30 Oct 2026.
- [M3] data/asic/shorts_2026.csv.gz (ASIC daily short positions), EML, 1 Sep to 26 Oct 2026.
- [M4] data/fx/fx_daily.csv, 6 Nov 2026 (NZ$1 = A$0.806387).
