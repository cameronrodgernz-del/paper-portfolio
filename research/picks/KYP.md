# Kinatico (ASX:KYP): deep dive. Not a value pick: the bad case (A$0.055) is 53% below the price and the middling case (A$0.09) is 23% below it

Status: finished. Verdict: **No case.** No card, no red team. Not a value pick (both legs fail), and as an ordinary pick resolving after the first-half FY27 result (due by 28 February 2027; resolve-by 5 March 2027) the expected gain after costs is about -29%, against a minimum of +2.3%. The first test kills the case: on cash earnings after capitalised development the market already pays Kinatico about 29 times last year's figure, more than it pays Objective, so the fact sheet's "our way" anchor gets nothing from the multiple and rests entirely on cash earnings doubling in a year in which first-quarter EBITDA grew 4%. The conditions that would reopen it are under "What would make this wrong". This is a simulation and not financial advice.

Written 2026-11-08 by the research desk. Price at writing: A$0.1175 (last trade on Friday 6 November 2026, `header.priceLast` in data/research_data/asx_company.json, fetched 7 November 2026 UTC; bid A$0.115, ask A$0.12; the A$0.12 `priceClose` is the 5 November close) [D2]. Market value: A$51.0m on 434,341,447 shares (436,629,484 quoted less 2,288,037 bought back to 5 November [K13]), including 18,037,500 loan-funded employee shares; A$48.9m on the 416,303,947 ordinary shares without them.
Fact sheet: research/facts/KYP.md (8 November 2026), grade A, "only just, and only on a growth multiple". The question it set: does the move to subscriptions turn into cash (FY26 cash earnings after capitalised development A$1.37m; September quarter EBITDA +4%, subscription revenue +18%)? Its "our way" anchor was A$0.170 (FY27 cash earnings of A$2.95m at Objective's 21.3 times); "against us" A$0.050 (A$1.37m at hipages' 7.6 times).

Order of work. The brief and the fact sheet both quote the price, so it was in view from the start. "What the filings show" and "Valuation" use Kinatico's filings, the peers' filings and the peers' prices only; Kinatico's own price enters in one reference line of the peer table, in "Why the market is wrong", "Outcomes and chances" and the checks. Arithmetic was run in `python3 -I` from scratch scripts (kyp_calc1.py, kyp_calc2.py, kyp_dcf2.py, kyp_rev.py; not committed); the key lines are shown where each figure is used.

In short:
1. Which multiple does the market pay for a company like this, on cash earnings after capitalised development? For ANZ software at the 6 November closes: hipages 7.5 times, ReadyTech 14.6 times, Objective 20.8 times (and First Advantage, the global background-screening leader, about 22 times free cash flow after interest and tax, from a secondary source). Kinatico itself trades at 29 times its FY26 figure (A$1.37m), or about 20 times before a working-capital build. It is already priced at the top of the range, while having the thinnest cash margin (3.9% against 9.5% to 19.8%), the lowest share of contracted revenue and, after the September quarter, slower growth than hipages or Objective.
2. The "move to subscriptions" is mostly a change of label. Of the A$20.5m FY26 "SaaS" revenue, only A$8.35m was recognised over time, which is how the company's policy books subscription fees; the other A$12.2m was recognised at a point in time, as checks are [K2 note 6]. Revenue recognised over time grew 5.8% in FY25 and 5.7% in FY26, and fell 1.5% in the second half of FY26 [K2, K4, K7]. My reading, which the filings don't state outright, is that most of the "SaaS" growth is check revenue bought under plans; from October 2026 the new plans charge verifications separately, "as used" [K9].
3. Cash is improving, from a low base. Cash earnings (fact sheet definition) went from A$0.29m in FY25 to A$1.37m in FY26, and the September quarter's free cash outflow was A$0.17m against A$0.66m a year earlier [K2, K9]. The fact sheet had that last comparison the wrong way round.
4. Value. About A$0.09 a share in the middle (range A$0.05 to A$0.19), from FY27 cash earnings at peer multiples and a discounted cash flow that agree within about 1c in each case. At A$0.1175 the market price implies EBITDA margins rising from 16% to about 23% by FY31 on 5% to 6% growth, or revenue growing about 14% a year from FY28.
5. The board's own one-year projection, used in the goodwill test, assumed 22% revenue growth in Australia in FY27; the first quarter delivered 3.8% for the group [K2 note 17, K9]. The year before, the same test assumed 11% and Australia delivered 7.4%.

Corrections to the fact sheet, for the record:
1. The price: A$0.12 is the 5 November close (`priceClose`); the last trade on 6 November was A$0.1175 [D2].
2. "Free cash flow 74% lower than a year earlier after bonus payments" is the wrong way round. The September 2026 quarter's free cash flow was an outflow of A$0.17m against an outflow of A$0.66m in the September 2025 quarter: the outflow was 74.3% smaller. Operating cash flow was A$0.57m against A$0.04m [K9, slide 4].
3. "Subscription revenue (SaaS) ... the recurring part": only A$8.35m of FY26 revenue was recognised over time; A$12.2m of the A$20.5m SaaS line was recognised at a point in time [K2 note 6]. The recurring part, on the accounts' own split, is about 24% of revenue, not 58%.
4. Missing: the board-approved FY27 projection in the impairment test (Australian revenue +22%, employee costs +16%; New Zealand revenue -2%) [K2 note 17].
5. Missing holder: Microequities Asset Management lifted its substantial holding to 31,993,030 shares (7.40%) on 27 August 2025 [K17]. No later notice was found, so on the filings it is the largest holder that has named itself; the 9.92% and 9.91% lines are custodians whose clients aren't disclosed.
6. Objective is not priced "for durable growth" in the plain sense: its ARR fell 2% in FY26 to A$117.3m (Information Intelligence -5%) while revenue grew 9% [P4]. Its multiple is paid for contracted revenue (87% recurring) and a 20% cash margin.
7. hipages' "guidance cut": at its 5 November AGM hipages said it now expects FY27 revenue, margin and cash flow at the lower end of its ranges (revenue growth 9% to 11%) [P2]. A softening, not a cut below the range. hipages also failed the desk's own liquidity check (median A$3,803 a day), so its price is thin (research/facts/HPG.md).
8. The full-year revenue note is not on the same basis as the half-year note: "other checks" were A$1.81m in the first half but "other verifications" A$0.97m for the full year, which would make the second half minus A$0.84m [K2 note 6, K4 note 4]. Something was moved between lines; the half-on-half "SaaS" comparison (49.5% then about 29%) mixes the two bases.

## The company in plain words
Kinatico (its screening brand is Kinatico CVCheck) sells workforce screening and compliance to Australian and New Zealand employers. Two kinds of revenue [K2 note 6]:
- Checks: national police checks (Kinatico is an accredited body of the National Police Checking Service) and other verifications, paid per check. FY26: criminal history A$13.66m, other A$0.97m, A$14.63m in all, down from A$17.20m.
- "SaaS": the compliance platforms (Kinatico Cited, and Kinatico Compliance, which began signing customers in August 2025) and plans under which customers buy checks. FY26 A$20.54m, up 37.5%. Of total revenue A$35.17m, A$8.35m was recognised over time and A$26.81m at a point in time.
Australia is 90% of revenue (A$31.75m), New Zealand 10% (A$3.42m). No customer is material [K2 note 5].

Who runs it: Michael Ivanchenko, chief executive (appointment announced 4 August 2021); Jason Margach, CFO; Ivan Gustavino, non-executive chair [K2]. Who owns it, at 30 July 2026 [K2, shareholder information]: 1,438 holders; the top 20 hold 53.6%. HSBC Custody Nominees 9.92% and J P Morgan Nominees 9.91% (custodians), Nicdam (Birman family, director Jon Birman) 5.23%, Charles Stewart 3.00%, then private holders and family companies; the chief executive 1.55%. Microequities held 7.40% at its last notice in August 2025 [K17]. The register is mostly private holders.

Five years [K3, slides 7 to 9]:

| Year to 30 June | FY22 | FY23 | FY24 | FY25 | FY26 |
| --- | --- | --- | --- | --- | --- |
| Revenue | A$26.4m | A$27.7m | A$28.7m | A$32.1m | A$35.2m |
| of which "SaaS" | A$2.4m | A$5.1m | A$9.7m | A$14.9m | A$20.5m |
| EBITDA | A$1.1m | A$2.6m | A$3.7m | A$4.3m | A$5.6m |
| Profit after tax | -A$1.5m | A$0.2m | A$0.8m | A$1.1m | A$2.0m |
| Operating cash flow | A$3.1m | A$3.6m | A$4.2m | A$5.3m | A$6.3m |
| Investing cash flow (mostly development) | A$3.5m | A$4.0m | A$3.2m | A$3.9m | A$3.8m |

Revenue has grown about 7.5% a year over four years. The share price went from A$0.12 in January 2024 to a close of A$0.385 on 24 October 2025 (the day of last year's AGM update), and has fallen 69% since [D1].

## Why big investors may be overlooking it
- Size and index: A$51m market value, outside the S&P/ASX 300; removed from the S&P/ASX All Technology Index on 23 March 2026 [K18].
- Liquidity: median traded value A$27,036 a day over the 20 sessions to 30 October 2026 [D1].
- Register: two custodian lines, then private holders; no institution other than Microequities has filed a substantial holding since August 2025 [K17, K19].
- Out of favour: small software sold off in 2026; management blames "a global software de-rating" [K3, slide 18].
None of this makes it cheap by itself. The price fall is better explained by the business: it was priced at about 4.7 times FY25 revenue at the October 2025 peak, when "SaaS" was growing 57%, and now at about 1.1 times, with growth down to 18% on that line and 3.8% in total (python3 -I: A$0.385 x 418.59m less A$10.22m of cash = A$150.9m, over A$32.13m).

## What the filings show

### What the "SaaS" line is made of
From the revenue notes (A$m) [K2 note 6, K7 note 6, K4 note 4, K8]:

| | FY24 | FY25 | FY26 | H1 FY26 | H2 FY26 |
| --- | --- | --- | --- | --- | --- |
| Recognised over time | 7.47 | 7.91 (+5.8%) | 8.35 (+5.7%) | 4.30 (+13.5%) | 4.05 (-1.5%) |
| Recognised at a point in time | 21.24 | 24.23 (+14.0%) | 26.81 (+10.7%) | 13.33 | 13.48 (+8.6%) |
| "SaaS" line | 9.70 | 14.94 | 20.54 | 9.73 | 10.80 |
| "SaaS" recognised at a point in time (SaaS less over time) | 2.23 | 7.03 | 12.18 | | |

The accounting policy says subscription revenue "is recognised evenly over the subscription period", and revenue from "pre-employment screening and workforce compliance monitoring is recognised at the point in time when the service is provided" [K2 note 6]. So of the A$10.8m of "SaaS" growth since FY24, about A$10.0m was revenue recognised as checks are, and A$0.9m was subscription fees. The directors' report says the fall in check revenue "reflects the migration of customers from point-in-time screening to subscription-based compliance management" [K2, page 24]. The new plans launched on 13 October and in early November 2026 charge verifications "as used on every plan", with "only monitored verifications" included in the per-worker fee (A$7 and A$12 per worker per month) [K9, slides 13 to 15]. Read together, the shift is mainly in how checks are bought and labelled. Total revenue is the honest growth figure: +13.0% in H1 FY26, +6.1% in H2 FY26, +3.8% in the September 2026 quarter (A$9.41m) [K4, K2, K9].

The September 2026 quarter [K9, slides 3 and 4, unaudited]: revenue A$9.41m (+3.8%), "SaaS" A$5.66m (+17.8%), so checks A$3.75m (-12.0%); gross profit A$6.31m (+5.8%, margin 67.1%); EBITDA A$1.51m (+4.3%); profit after tax A$0.47m (-10.5%); cash A$11.48m.

### Cash earnings
Cash earnings here are the fact sheet's: operating cash flow excluding interest and tax, less capitalised development, equipment, lease payments and the insurance premium funding repaid (A$m) [K2 cash flow statement and note 10]:

| | FY25 | FY26 | September quarter FY26 / FY27 |
| --- | --- | --- | --- |
| EBITDA (after share-based pay) | 4.35 | 5.58 | 1.44 / 1.51 |
| plus share-based pay (paid in shares) | 0.37 | 0.69 | |
| less capitalised development | 3.66 | 3.74 | investing 0.71 / 0.74 |
| less equipment | 0.06 | 0.07 | |
| less lease payments and finance costs | 0.47 | 0.43 | |
| Before working capital | 0.53 | 2.04 | |
| Working capital and insurance funding timing | -0.24 | -0.67 | |
| Cash earnings | 0.29 | 1.37 | free cash flow -0.66 / -0.17 |
| With share-based pay counted as a cost, before working capital | 0.16 | 1.34 | |

Capitalised development is 10.6% of revenue and 67% of EBITDA; it ran ahead of amortisation (A$2.35m) by A$1.39m in FY26 [K2 note 17]. The company's "free cash flow" of A$2.5m leaves out leases and insurance funding [K3]. Two things follow. Cash earnings are improving by about A$1m a year (FY25 to FY26, and the first quarter's A$0.49m year-on-year improvement), which is the real progress. But they are a thin residual: on revenue of A$35m, a one-point change in margin moves cash earnings by A$0.35m, a quarter of the FY26 figure.

### Balance sheet, shares and buy-back
- Cash A$11.83m at 30 June 2026, A$11.48m at 30 September, no borrowings; lease liability A$0.32m, all current (the office lease ends in FY27) [K2, K9]. Net of the A$0.32m of buy-backs since: about A$11.16m.
- Unbooked tax losses: a potential tax asset of A$4.06m at 25% (about A$16.2m of losses), not on the balance sheet [K2 note 8]. Tax paid in FY26: A$0.01m.
- Net tangible assets A$10.26m (2.5c a share); intangibles A$19.5m including goodwill A$4.7m [K1, K2].
- Shares: 18,037,500 escrowed loan-funded shares (13.5m at 12c, 4,537,500 at 29c needing a 41.47c share price to vest), 4,000,000 zero-priced performance shares for the chief executive that vest on employment to 24 January 2027, and 5,000,000 director options at 49.6c [K2 notes 19 and 21, remuneration report].
- Buy-back: up to A$5m or 43.2m shares from 5 October 2026 to 4 October 2027, because the board considers the price "does not accurately reflect the underlying value" [K12]. 2,288,037 bought for A$318,262 to 5 November (average 13.9c; 120,000 on 5 November at 12c to 12.5c) [K13]. About A$4.68m remains, roughly 9% of the market value.
- No dividends. No capital raised for cash in two years.

### What management has said, and the record
No numerical guidance ("We do not provide formal guidance") [K2, CEO report]. The FY26 annual report: "As the pipeline we have built converts, we expect SaaS growth to re-accelerate" [K2]. The chair at the 23 October 2026 AGM: results through the first quarter "continue its proven growth trajectory" [K10]. The goodwill test used a board-approved one-year projection of 22% revenue growth for Australia in FY27 (and 11% for FY26, against 7.4% delivered), with employee costs up 16% [K2 note 17]. For the group that projection is about A$42.1m of FY27 revenue (+19.7%); the first quarter grew 3.8%. Management pointed to a qualified enterprise pipeline of "A$12m+", Civeo (signed), HanRoy and Sunwater (signed after June), about 100 digital sign-ups, and a heads of agreement with OWNA for a white-label product across its 8,000-plus childcare centres [K3, slide 16; K9, slides 19 and 20]. None has a disclosed contract value.

### Who is buying and selling
Directors bought on market in 2026: Georg Chmiel 100,000 at 13.5c (20 March), Jon Birman 250,000 at 13c (4 June), Ivan Gustavino 77,607 at 13c (12 June), about A$56,000 in all [K14, K15, K16]. Australian Ethical ceased to be a substantial holder on 11 August 2025 [K19]. No substantial holder notice since 29 August 2025. AGM resolutions passed with 99.9% [K11].

## Valuation
Done from the filings and the peers' prices, without Kinatico's price. Equity value = enterprise value plus A$11.16m of cash. Shares: 416.30m ordinary plus the 4.0m performance shares (420.30m); above 12c a share the 13.5m loan-funded shares are added with their A$1.62m loan repayment.

### The first test: what the market pays for software like this, on cash earnings after capitalised development
Peers at the last trade on 6 November 2026 [D2], figures from each FY26 filing (python3 -I, kyp_calc2.py):

| Company | FY26 revenue and growth | Contracted or recurring | Cash margin | EV | EV / cash earnings | EV / (EBITDA less development) | EV / EBITDA | EV / revenue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hipages (HPG) [P1, P2] | A$90.6m, +9%; FY27 at the low end of 9% to 11% | 98% | 9.5% | A$64.6m | 7.5x | 7.9x | 2.8x | 0.71x |
| ReadyTech (RDY) [P5] | A$125.0m, +2.6%; adjusted EBITDA -12% | 83% subscription | 10.2% | A$185.8m | 14.6x | 11.4x | 5.3x | 1.49x |
| Objective (OCL) [P4] | A$134.7m, +9%; ARR -2% | 87% | 19.8% | A$553.6m | 20.8x | 16.2x | 10.7x | 4.11x |
| First Advantage (NASDAQ:FA), 25 Oct 2026, secondary [P7] | US$1.66bn | | | US$5.45bn | 21.9x free cash flow after interest and tax | | 12.9x | 3.28x |
| Reckon (RKN), desk's earlier work [R1] | flat | | | about A$47m | about 4x to 5.5x | | | |
| Kinatico at A$0.1175, for reference only | A$35.2m, +9.4%; Q1 FY27 +3.8% | 24% recognised over time | 3.9% | A$39.9m | 29.2x (19.6x before working capital) | 21.7x | 7.2x | 1.13x |

Cash earnings for each peer: operating cash flow excluding interest and tax, less capitalised development, equipment and leases. hipages A$25.78m less A$14.68m, A$0.40m and A$2.14m = A$8.56m; ReadyTech A$33.20m less A$0.16m of contract costs, A$0.20m, A$18.57m and A$1.57m = A$12.70m (EV includes A$32.5m of net debt); Objective A$49.33m less A$3.59m interest, plus A$1.89m tax, less A$17.43m, A$0.57m and A$2.97m = A$26.66m. hipages' EV uses the desk's A$31.3m of net cash and its A$7.72m net tax asset (7.3 times if all A$34.2m of cash and deposits at 30 June counts); Objective's uses the fact sheet's A$73.7m of net cash after the 13c final dividend and later buy-backs, plus A$7.46m of deferred tax owed. Damstra, an ANZ workforce compliance software business, was bought by Ideagen in 2024 for 24c a share, 2.8 times FY23 revenue of A$29.5m (A$12.1m of net debt) [P6]: that is what a trade buyer paid, a bid, not a market multiple.

What it says: on the measure the brief asks for, the market pays 7.5 times (hipages: growing 9%, all recurring, but thinly traded) to about 21 times (Objective and First Advantage: contracted revenue and 20% to 25% margins), with ReadyTech's 14.6 times between them. Kinatico's growth is now below hipages' and Objective's, its contracted share and margin are the lowest, and it is the smallest. A company like this belongs in the lower half of that range, about 7.5 to 14.6 times, and 11 times in the middle. Objective's 21 times is a quality multiple, not one Kinatico has earned.

### Method 1: FY27 cash earnings at peer multiples
FY27 cash earnings before working capital (share-based pay added back, the peers' basis), from the September quarter and the cost base:
- Bad: revenue +2%, EBITDA margin 15% (costs grow as budgeted while revenue doesn't): EBITDA A$5.38m, cash earnings A$1.79m. At hipages' 7.5 times: A$13.4m, A$0.058 a share.
- Middling: revenue +5%, margin 16% (the September quarter's 16.0%): EBITDA A$5.91m, cash earnings A$2.23m. At 11 times: A$24.5m, A$0.085; at ReadyTech's 14.6 times, A$0.104.
- Good: revenue +10%, margin 18% (the pipeline converts): EBITDA A$6.96m, cash earnings A$3.33m. At Objective's 20.8 times: A$69.3m, A$0.189.
Cross-check on EV / (EBITDA less development) at hipages' 7.9 times, ReadyTech's 11.4 times and Objective's 16.2 times: A$0.057, A$0.082, A$0.145. The unbooked tax losses would add about 0.7c to each.

### Method 2: discounted cash flow
Inputs (kyp_dcf2.py): valuation at 1 January 2027; 12% discount rate (the company's own pre-tax rate is 13.5%); share-based pay kept as a cost; capitalised development as a share of revenue; equipment A$0.1m and leases A$0.43m a year; working capital 10% of each year's revenue increase; tax at 25% after the A$16.2m of losses are used, full tax in the terminal year.

| | Revenue growth FY27, then to FY31 | EBITDA margin FY27 to FY31 | Development, share of revenue | Terminal growth | Value a share |
| --- | --- | --- | --- | --- | --- |
| Bad | 2%, then 3% | 15% flat | 10.5% | 2% | A$0.048 |
| Middling | 5%, then 6% | 16% rising to 20% | 10.5% falling to 9% | 2.5% | A$0.098 |
| Good | 10%, then 12% and 10% | 18% rising to 25% | 10% falling to 8% | 3% | A$0.174 |

In the middling case pre-tax cash earnings rise from A$2.2m in FY27 to A$5.5m in FY31. Sensitivities on the middling case: 11% discount A$0.106, 13% A$0.091; FY31 margin of 17% A$0.077, 23% A$0.119. The input that moves it most is the margin the business reaches: each three points of FY31 EBITDA margin is worth about 2c a share.

### Range
| | Method 1 | Method 2 | Cross-check | Used |
| --- | --- | --- | --- | --- |
| Bad | A$0.058 | A$0.048 | A$0.057 | A$0.055 |
| Middling | A$0.085 to A$0.104 | A$0.098 | A$0.082 | A$0.09 |
| Good | A$0.189 | A$0.174 | A$0.145; a bid at 1.5 to 2 times revenue A$0.151 to A$0.192 | A$0.175 |

The middle depends on margins rising about a point a year while revenue grows 5% to 6%; the bad case on the cost growth the board budgeted arriving without the revenue; the good case on the pipeline converting into 10%-plus growth, or a bid. A buyer who cut development to the level of amortisation (A$2.35m) would have cash earnings of about A$3.4m on today's figures, which is how a trade buyer's price reaches the good case.

## Why the market is wrong
I can't say it is, in our favour. At A$0.1175 the enterprise value is A$39.9m: 29 times FY26 cash earnings, about 18 times my middling FY27 figure, above every peer on the cash measure. Run backwards through Method 2, the price assumes EBITDA margins reach about 23% by FY31 on 5% to 6% growth, or, with margins reaching 20%, revenue growing about 14% a year from FY28 (kyp_rev.py). That is close to management's hope, and above the September quarter's 3.8% revenue growth and 16% margin. The fact sheet's 42% gap came from putting Objective's multiple on a doubled FY27 cash figure; the market already gives Kinatico more than Objective's multiple on today's cash, so the gap is all in the doubling, and the only event inside six months that could show it (the first-half result) starts from a first quarter that points the other way. With no reason to think the price is too low, there is no trade.

## Outcomes and chances
Resolve-by 5 March 2027, after the first-half FY27 result (ASX deadline 28 February; last year 17 February).

| Outcome | What happens | Chance | Price by resolve date |
| --- | --- | --- | --- |
| Bad | The December quarter flash and the half show revenue up 3% or less, checks still falling, EBITDA flat or down as costs rise; the market prices it like hipages | 30% | A$0.055 (the bad row of the range: Method 1 A$0.058, Method 2 A$0.048) |
| Middling | Revenue up 4% to 8%, EBITDA up 5% to 15%, cash earnings for the half better than last year's; the first quarter repeated | 55% | A$0.09 (the middling row: Method 1 A$0.085 to A$0.104, Method 2 A$0.098) |
| Good | The pipeline converts: revenue up 10% or more for the half, EBITDA up 20% or more, re-acceleration on the over-time revenue line; or a bid | 15% | A$0.175 (the good row: Method 2 A$0.174, Method 1 A$0.189, a bid A$0.15 to A$0.19) |

Expected price: 0.30 x 0.055 + 0.55 x 0.09 + 0.15 x 0.175 = A$0.092, 21.5% below the price before costs. If instead the market kept paying its current multiple in the middling case (about A$0.12), the expected price would be A$0.109, still 7.4% below.

Round-trip costs, for the 2.5% cap of NZ$2,500 (A$2,016 at NZ$1 = A$0.8064 on 6 November 2026 [D3]), below the liquidity limit: brokerage A$15 each way (0.74% each way); spread one tick, A$0.005, 4.3% (the 6 November quote; the Corwin and Schultz estimate from 60 sessions is 1.8%), half each way; size cost each way of daily volatility (2.9% over 20 sessions) times the square root of A$2,016 over the 20-session average of A$49,373, 0.59%; and 0.5% to convert NZ$ to A$. About 7.4% in all. Expected gain after costs about -29% (about -15% with the middling case at today's multiple), against a minimum of +2.3% (the 2.13% cash rate plus 5% a year over the 116 days from 9 November 2026 to 5 March 2027; rulebook section 5a). Not a case for review.

As a value pick it fails both legs: the bad case is 53% below the price (the rule allows 10%) and the middling case 23% below (it needs 15% above). It would qualify only at A$0.061 or less; on today's chances the expected gain after costs clears the minimum only at about A$0.084 or less.

## Dated events
- December 2026 quarter flash: about mid-January 2027 (last year 14 January) [K6]. Revenue and "SaaS" for the quarter.
- Chief executive's 4,000,000 performance shares vest on 24 January 2027 if he is still employed [K2].
- First-half FY27 result: by 28 February 2027 (last year 17 February) [K4]. Shows EBITDA, cash flow and the revenue-timing note (over time against point in time), the best test of whether subscriptions are growing.
- Buy-back open to 4 October 2027 [K12].
- New plans (Verified from 13 October; Continuous and Complete from early November 2026) change how verifications are charged [K9]. Expect the "SaaS" and transactional lines to move for reasons of labelling; read total revenue and the over-time line.

## What would make this wrong
The two things most likely to make the no-case call wrong:
1. The pipeline converts fast. Civeo, HanRoy and Sunwater are signed, OWNA could put the product in front of 8,000-plus childcare centres, and the second tranche of the anti-money-laundering rules brings an estimated 80,000 organisations into scope from 1 July 2026 [K2, K9]. If the first half shows 10%-plus revenue growth and 20%-plus EBITDA growth, cash earnings would be heading for A$3m-plus and the good case (A$0.175) becomes the middle. The market paid 4.7 times revenue for 57% growth a year ago.
2. A bid. Net cash of A$11m, no debt, a register where the top 20 hold 54%, a board saying the price is too low, and a precedent (Damstra at 2.8 times revenue in 2024). A trade buyer at 1.5 to 2 times revenue would pay A$0.15 to A$0.19. Nothing suggests an approach. The buy-back also makes the bad-case price less likely to print while it runs.

What would reopen it (any one, checked against fresh filings):
- The first-half FY27 result shows revenue up 10% or more for the half, revenue recognised over time up 10% or more (on H1 FY26's A$4.30m), EBITDA of A$3.2m or more (H1 FY26 A$2.7m) and cash earnings for the half of A$1.0m or more (fact sheet definition), and the price is then below about A$0.14.
- The price falls to A$0.084 or less while the December quarter flash shows revenue growth of at least 4%: re-run as an ordinary pick resolving at the first-half result.
- A takeover approach, a strategic review or a holder building a stake: re-run as a special situation, with the bid precedent as the good case.

## Checks
- Not on Cam's excluded list: config/judgement_excluded.csv has no entries (Cam confirmed the list on 8 November 2026).
- No placement-pattern reopening in the last 30 sessions (21 September to 30 October 2026): no trading halt or placement in 2026 [K19]; the one opening gap of 5% or more (30 October, A$0.12 to A$0.13) was two price steps on normal volume [D1].
- Liquidity: median traded value A$27,036 a day over the 20 sessions 5 to 30 October 2026 (lowest A$10,933; all above A$10,000), 60-session median A$35,740 [D1]. Two sessions at 10% is A$5,407, so the 2.5% cap (about A$2,016) binds first.

## What I couldn't verify
- The make-up of the "SaaS" line: the filings don't split it into plan fees and checks bought under plans. The 24% figure rests on the revenue-timing note and the accounting policy; the company may define the lines differently.
- Why the half-year "other checks" (A$1.81m) exceed the full-year "other verifications" (A$0.97m); no reclassification note was found.
- Microequities' current holding (last notice 7.40%, August 2025).
- hipages' net cash (A$31.3m, the desk's figure; the filing shows A$34.2m of cash and deposits and A$0.2m of borrowings at 30 June) and Objective's buy-backs since June (A$6.55m), both from the fact sheet and only partly re-checked.
- First Advantage's multiples come from a secondary source (stockanalysis.com); I didn't read its filings.
- September quarter FY26 cash flow figures are the comparatives in the FY27 quarter deck.
- Broker coverage: not checked.

## Sources
Kinatico, ASX announcements:
- K1. Appendix 4E, 6 Aug 2026 (03122373): https://announcements.asx.com.au/asxpdf/20260806/pdf/072gmxskvppk2d.pdf
- K2. Annual Report 2026, 6 Aug 2026 (03122374): CEO report, directors' report, statements, notes 5, 6, 8, 10, 17, 18, 19, 21, remuneration report, shareholder information: https://announcements.asx.com.au/asxpdf/20260806/pdf/072gmzy64y636t.pdf
- K3. FY26 results webinar presentation, 6 Aug 2026 (03122549): https://announcements.asx.com.au/asxpdf/20260806/pdf/072h1gwrq20ptr.pdf
- K4. Half Yearly Report and Accounts, 17 Feb 2026 (03060869), note 4 and cash flow: https://announcements.asx.com.au/asxpdf/20260217/pdf/06wcrhbcpdl23t.pdf
- K5. H1 FY26 investor webinar presentation, 17 Feb 2026 (03061092): https://announcements.asx.com.au/asxpdf/20260217/pdf/06wd85lwv0kcqt.pdf
- K6. Q2 FY26 flash, 14 Jan 2026 (03049632): https://announcements.asx.com.au/asxpdf/20260114/pdf/06v7k6tcn0y3h3.pdf
- K7. Annual Report 2025, 26 Aug 2025 (02985793), note 6: https://announcements.asx.com.au/asxpdf/20250826/pdf/06nckfrp1yby1l.pdf
- K8. Half Yearly Report FY25, 25 Feb 2025 (02918699), revenue note: https://announcements.asx.com.au/asxpdf/20250225/pdf/06fxsk8kndl5w0.pdf
- K9. CEO presentation post-AGM, Q1 FY27 update, 23 Oct 2026 (03156302): https://announcements.asx.com.au/asxpdf/20261023/pdf/075pk1zwh9trlv.pdf
- K10. Chairman's address to the 2026 AGM, 23 Oct 2026 (03156299): https://announcements.asx.com.au/asxpdf/20261023/pdf/075pjtdt50s1lx.pdf
- K11. Results of the 2026 AGM, 23 Oct 2026 (03156570): https://announcements.asx.com.au/asxpdf/20261023/pdf/075q6t8ltdttmf.pdf
- K12. On-market buy-back, 21 Sep 2026 (03141594): https://announcements.asx.com.au/asxpdf/20260921/pdf/0749s3mmfqdfj1.pdf
- K13. Update, notification of buy-back, 6 Nov 2026 (03162721): https://announcements.asx.com.au/asxpdf/20261106/pdf/07696v8sk3znb3.pdf
- K14. Appendix 3Y, G Chmiel, 20 Mar 2026 (03074574): https://announcements.asx.com.au/asxpdf/20260320/pdf/06xnlb63l8s79r.pdf
- K15. Appendix 3Y, J Birman, 5 Jun 2026 (03101716): https://announcements.asx.com.au/asxpdf/20260605/pdf/070cgq0p50qtrv.pdf
- K16. Change of Director's Interest Notice, I Gustavino, 15 Jun 2026 (03104153): https://announcements.asx.com.au/asxpdf/20260615/pdf/070mznjwny3wp4.pdf
- K17. Microequities Asset Management, Form 604, 29 Aug 2025 (02988747): https://announcements.asx.com.au/asxpdf/20250829/pdf/06nltqscchr68w.pdf
- K18. S&P DJI March 2026 quarterly rebalance, 6 Mar 2026 (03069416), S&P/ASX All Technology Index removals: https://announcements.asx.com.au/asxpdf/20260306/pdf/06x4vd88v6bpg7.pdf
- K19. ASX announcements list for KYP, 2025 and 2026: https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=KYP&timeframe=Y&year=2026 (and the list in data/research_data/asx_company.json)

Peers:
- P1. hipages FY26 Appendix 4E and statutory accounts, 24 Aug 2026 (03128727): https://announcements.asx.com.au/asxpdf/20260824/pdf/0733fbkjpyy3y6.pdf
- P2. hipages Chair and CEO AGM addresses and presentation, 5 Nov 2026 (03162237): https://announcements.asx.com.au/asxpdf/20261105/pdf/0767tr5c4rk3st.pdf
- P4. Objective Corporation Preliminary Final Report FY2026, 27 Aug 2026 (03131200): https://announcements.asx.com.au/asxpdf/20260827/pdf/0739tldtq9275v.pdf
- P5. ReadyTech Appendix 4E and 2026 Annual Report, 27 Aug 2026 (03130885): https://announcements.asx.com.au/asxpdf/20260827/pdf/07393psz7byj92.pdf
- P6. Damstra Technology, scheme implementation deed with Ideagen, 25 Jan 2024 (02765837): https://cdn-api.markitdigital.com/apiman-gateway/ASX/asx-research/1.0/file/2924-02765837-3A635248
- P7. First Advantage statistics, stockanalysis.com (secondary source), data to 25 Oct 2026: https://stockanalysis.com/stocks/fa/statistics
- R1. Reckon multiples: the desk's deep dives research/picks/RKN.md and research/picks/IRI.md (Method 1 table), from Reckon's filings.

Data:
- D1. Norgate prices and volumes, data/norgate/universe/prices_2025.csv.gz and prices_2026.csv.gz (to 30 Oct 2026).
- D2. data/research_data/asx_company.json, fetched 7 Nov 2026 UTC: last trades, bids, asks and share counts for KYP, HPG, RDY and OCL.
- D3. data/fx/fx_daily.csv, 6 Nov 2026 (A$1 = NZ$1.2401, NZ$1 = A$0.8064).
