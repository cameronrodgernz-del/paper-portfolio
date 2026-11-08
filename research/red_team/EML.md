# EML Payments (ASX:EML): red team review. Wait for the 1H FY27 result (about 24 to 25 February 2027); priced on what the market has paid EML after its results, the expected gain after costs is about -9%, against a 2.4% minimum

Written 2026-11-08 by the red team, against docs/RED_TEAM.md (research pick checklist) and RULEBOOK.md sections 3, 4 and 5a as they stand today. The deep dive was written after the two 8 November rule changes and already applies them, so it is tested against them as current rules, not as changes it missed. This is a simulation and not financial advice.

What I reviewed: research/picks/EML.md (written 8 November 2026, verdict "wait for the 1H FY27 result"; sent here because its central expected gain, +5.4% after costs to 12 March 2027, clears the 2.4% minimum). No card has been drafted. Price: A$0.28 (last trade on 6 November 2026; close on 5 November A$0.265; range on 6 November A$0.255 to A$0.285 on 2.01m shares; bid A$0.28, ask A$0.29; data/research_data/asx_company.json). Norgate's last close in the repo is A$0.215 on 30 October.

Rules applied:
- Ordinary pick: expected gain after costs of at least the cash rate (2.13%) plus 5% a year over the days to the resolve date. To 12 March 2027 that is 123 days and 2.40%.
- Value pick (up to 24 months): bad case no more than 10% below the price, middling at least 15% above, and the same minimum gain (13.1% to 8 September 2028).

Order of work: I read the deep dive, the checklist and the rulebook, then downloaded every filing listed under Sources myself from the ASX and read them as text (Copia's notices are images, so I read them by OCR). I did not open the fact sheet (research/facts/EML.md) or any other research file before this review was written. The deep dive's scratch scripts were not committed and I did not look for them; I rebuilt its valuation from the figures it prints.

In short:
1. The facts I re-checked held, with two corrections and two things left out. Regal Partners did not "sell out by 2 September": it ceased to be a substantial holder, meaning it fell below 5%; its last notice leaves it with about 18.4m shares (4.7%) unless it sold more since. The A$13.6m stored value shortfall provision includes A$1.8m from FY26's own activity, so the fault was still running last year. And the August annual report and presentation say nothing at all about the APRA licence application or the bank guarantee APRA and the RBA required, so the size of that capital need is undisclosed.
2. The discounted cash flow counts the bank debt twice. Its cash flows already pay A$6.5m of interest every year, including in the terminal value, and it then subtracts A$60.4m of net debt as well. I reproduced its path values exactly (A$0.68, A$0.40, A$0.07 at 13%) and, done consistently, each path is about A$0.12 a share higher: A$0.80, A$0.52, A$0.18. On the deep dive's own paths and weights the value is A$0.41 at 13% and A$0.34 at 15%, and A$0.28 implies a cost of equity of about 17.5%. The two errors offset: the deep dive's "13%" behaves like a consistent 17%, which is a defensible rate for this company, so its "about fair" conclusion survives, but for a different reason than it gives.
3. The outcome prices for March 2027 are weighted path values, not what the market pays. The market has paid EML 7.6, 5.2, 3.8 and 3.3 times guided underlying EBITDA after its last four results or updates, and 2.8 times on 30 October. The middling price (A$0.36) needs about 3.85 times after a half that is in line but still cash-negative. Since August 2025 EML's in-line results and updates have been followed by falls of 8% to 33% over the next 20 sessions, and none lifted the stock. I use A$0.31 (3.5 times).
4. The bad outcome is any one of five triggers (a guidance cut, one-offs outside Arlo above A$8m, a higher Arlo budget, the shortfall above A$13.6m, a raising or covenant waiver). At least one of these fired at each of the last three reporting dates. I put it at 45%, not 40%.
5. On my numbers (bad 45% at A$0.17, middling 40% at A$0.31, good 15% at A$0.45) the expected price is A$0.268: -4.3% before costs and about -8.8% after, against +2.4%. It fails with the deep dive's chances too (-6.3%). It clears only if the middling price is A$0.34 or more and the deep dive's bad and good prices also hold, or if the price falls to about A$0.24 with nothing else changed.
6. The 30% rise from 30 October to 6 November was specific to EML (fourth best of the 397 ASX companies in the repo's data; the median fell 1.1%), came with no announcement and no holder notice, and short covering can explain little of it. I couldn't find the cause.
7. The value pick test fails however the bad case is measured: A$0.09 to A$0.23 in 2028 depending on method (18% to 68% below the price), before any raising.

## 1. Are the facts right?

Re-checked against the primary sources (links under Sources):

| Fact in the deep dive | What the source says | Held? |
| --- | --- | --- |
| FY26 underlying EBITDA A$48.3m; reported ("operating") EBITDA A$14.4m; add-backs A$33.9m; statutory loss A$19.7m; revenue A$207.0m (customer A$150.3m, interest A$56.7m); share-based pay A$15.0m [S1 p13] | Underlying A$48,293k; operating EBITDA A$14,417k; add-backs shortfall 9,562, related receivable 2,175, remediation and class action 1,439, legacy tax 1,240, Arlo 4,151, restructuring 15,309 = A$33,876k; loss A$19,673k | Yes |
| FY25 add-backs A$28.2m [S1 p13] | 9,521 + 1,009 + 8,397 + 2,796 + 6,459 = A$28,182k | Yes |
| 1H FY26 one-offs outside Arlo A$9.3m, 2H A$20.4m [S3] | 1H restructuring A$9,235k, Arlo A$4,525k; 2H outside Arlo by difference A$20.5m | Yes. The deep dive's "A$7.4m of restructuring in 2H" is A$6.1m by my arithmetic (15,309 less 9,235); the point stands |
| Cash A$37.8m; A$125m facilities incl. a A$10m guarantee facility; A$50m term loan to 26 Sep 2029 fully drawn; A$65m syndicated to 26 Sep 2028, A$34m drawn; A$31m undrawn [S1 note 19, going concern] | As stated | Yes |
| Gearing covenant 0.45 (indebtedness incl. leases over indebtedness plus equity), tested 31 Dec and 30 Jun; 0.407 at June 2026; senior debt 2.5 times adjusted EBITDA; interest cover 5 times [S1 note 19] | As stated; borrowings A$89.34m against equity A$130.10m gives 0.407 | Yes |
| Shortfall provision A$13.58m, review to conclude by the end of calendar 2026 [S1 note 21, p15] | As stated. Also: "these items represent $11.8m of the total $13.6m ... with the remaining balance relating to current-year activity" [S1 p15]. The shortfalls arose in the North American and UK "unregulated businesses" [S1 p13 note 2] | Yes, with a detail left out (below) |
| FY27 guidance A$50m to A$54m, overheads ~A$110m, yields up ~20bps; FY28 "proforma" free cash flow A$30m to A$35m, undefined; Arlo A$34m, non-recurring spend ~A$15.7m FY27, ~A$2.4m FY28, ~A$1.0m FY29 [S1 release, S2 p9 and p20] | As stated. "Proforma" is not defined in either document | Yes |
| 391,262,494 shares; 63,627,800 performance rights, 2,619,304 rights, 64,358 restricted rights [S17] | As stated | Yes |
| Copia 48,550,000 shares, 12.49% on 13 May 2026; May buys 4,140,000 for A$1,653,942 [S10] | As stated (by OCR). The notice itself doesn't add up: 42.9m before plus 4.14m bought is 47.04m, not 48.55m | Yes |
| QVG 32,937,625, 8.43% on 28 Sep 2026 [S11] | As stated; sold 3.8m and bought 0.1m since March | Yes |
| Regal "sold out by 2 September 2026" [S12 to S15] | Regal held 37.9m (9.75%) after buying in early March, sold to 32.0m (15 June), 26.3m (17 June), 22.2m (20 August), then 3.84m more on 21 August and 2 September at A$0.24 to A$0.26 and fell below 5%. That leaves about 18.4m (4.7%) unless it sold more after 2 September | No: below 5%, not out |
| Hynes bought 1,000,000 shares for A$606,046 on 6 to 12 March 2026 [S8] | As stated; 4,917,569 shares after | Yes |
| 2025 AGM: Q1 FY26 underlying EBITDA A$6.8m, down 42%; FY26 guidance A$58m to A$63m affirmed [S4] | As stated; the update also said Q1 trading was "in line with guidance forecasts". FY26 came in at A$48.3m | Yes |
| 13 April 2026 cut to A$47m to A$50m; the ADI guarantee cost to be left out of underlying EBITDA [S5] | As stated | Yes |
| APS 610 sets a minimum of 4% of stored value liabilities in Common Equity Tier 1 [R1] | Paragraph 13: "The minimum PCR for a PPF provider is 4 per cent of total outstanding stored value liabilities", held as CET1 | Yes |
| Goodwill tested at 11.7% to 11.8% post-tax WACC, 3% terminal growth, revenue growth 7% to 14% a year [S1 note 16] | As stated | Yes |
| A$7m for 28% of Mobilata (renamed Tendren), in which the Executive Chair separately holds an interest [S1 note 28] | As stated. Mobilata had net assets of A$9.5m and profit of A$2.5m for FY26; EML's 28% of those net assets is about A$2.7m, against A$7m paid. The note then says the group "did not enter into any other related party transactions" | Yes |
| Removed from the All Ordinaries effective 21 September 2026 [S18] | As stated | Yes |
| A$16.2m a year per 1% on floating-rate balances [S1 note 23] | A$16,234k | Yes |
| Liquidity: median A$123,896 a day (5 to 30 October), lowest A$21,482; daily volatility 4.6% [Norgate] | Same figures from the repo's Norgate file | Yes |

What was left out or understated:
- The shortfall wasn't only historical. A$1.8m of the A$13.6m relates to FY26 activity and sits inside underlying EBITDA. A review that is still running, of a fault that was still occurring last year, is more likely to come in above the provision than below it.
- The APRA matter has gone quiet in the filings. On 30 March EML said APRA and the RBA required an ADI guarantee over certain stored value by 30 April; on 1 May the date was extended and EML said it would not update the market again unless something material changed [S6, S7]. The FY26 annual report and presentation don't mention the licence application, the guarantee, Treasury's reforms or the capital an ADI licence would need. The only guarantee costs in FY26 (A$230k) were already running in the first half, before the APRA notice. Treasury's reforms were still at exposure draft stage on the last status I could read, with the government aiming to introduce a bill in 2026 [R2].
- Regal's remaining stake, about 4.7% if unsold, is a possible seller into any rise.
- "Recalibration of near-term revenue flow from several key contracts", a A$3.8m loan to a key client, and "renew several key contracts" among the top 30 as an FY27 priority [S1 release, S2 p18 and p20] point to pricing pressure at renewal, which the deep dive mentions only as a loan.
- Auditor: unqualified, no emphasis of matter; key audit matters were revenue recognition and goodwill [S1]. Nothing missed there.

## 2. Is it really overlooked, or cheap for a reason?

Who has been selling: Wilson Asset Management sold 25m shares on 27 February 2026 at about A$0.60 and fell below 5% [S16]; Regal bought about 11.9m that week, then sold about 19.5m between March and early September, the last at A$0.24 [S12 to S15]; QVG sold 3.8m (9.43% to 8.43%); Viburnum went from 7.85% to 5.23%. The heaviest day in October was 13 October, 3.88m shares traded down to A$0.1925, the year's low. Copia holds 12.5% at a large loss and has said nothing. This is a register of funds leaving after being wrong, not one being built, at least until whatever happened in early November.

The sector: Tyro, the nearest ASX payments name, is also priced at 3.4 to 5.5 times EBITDA on the deep dive's own figures. EML at 3.3 times is not an outlier against that.

Debt falling due: the A$65m syndicated facility matures 26 September 2028; the covenants are tested every 31 December and 30 June, the next in seven weeks.

Management's record against its own guidance: FY24 and FY25 were met; FY26 was affirmed at the AGM on a 42% weaker first quarter, "tightened" to the bottom of the range in February, and cut 19% in April. The November 2024 plan's FY28 targets (about A$95m of EBITDA, 60% cash conversion) have become A$50m to A$54m for FY27 and an undefined A$30m to A$35m of "proforma" cash for FY28. Arlo's budget has gone from A$12m to A$15m, to A$20m, to A$34m. The answer to this heading is mainly "cheap for a reason", with the reasons already in the price at A$0.215 and arguably less so at A$0.28.

## 3. The valuation

### The discounted cash flow counts the debt twice
I rebuilt Method 2 from the paths printed in the deep dive (free cash flow FY27 to FY30, interest A$6.5m a year, 1% growth after FY30, cash flows at each 30 June, discounted from 8 November 2026, less A$60.4m of adjusted net debt, on 391.262m shares). It reproduces the deep dive to the cent: good A$0.679, middling A$0.398, bad A$0.065, weighted A$0.291 at 13%, A$0.254 at 14%, A$0.222 at 15%, A$0.388 at 11%.

The cash flows are after A$6.5m of interest in every year and in the terminal value, so the equity is already paying for the debt forever. Subtracting the net debt as well charges for it a second time. (The deep dive's Method 1, a multiple of the same after-interest cash flow, correctly subtracts nothing.) Two consistent ways to do it:
- Keep the interest, and deduct only obligations that carry no interest and aren't in the cash flows: the A$13.6m shortfall and the A$0.8m owed to PCSIL's liquidator. The A$37.8m of cash isn't credited, which matches the deep dive's own view that it is tied up as regulatory capital.
- Add the interest back and deduct the debt instead.

| Cost of equity | Deep dive's method (good / middling / bad, weighted) | Consistent (good / middling / bad, weighted) |
| --- | --- | --- |
| 13% | 0.68 / 0.40 / 0.07, **0.29** | 0.80 / 0.52 / 0.18, **0.41** |
| 14% | 0.61 / 0.35 / 0.05, 0.25 | 0.73 / 0.47 / 0.16, 0.37 |
| 15% | 0.56 / 0.31 / 0.03, 0.22 | 0.67 / 0.43 / 0.15, 0.34 |
| 16% | | 0.62 / 0.40 / 0.13, 0.31 |
| 17% | | 0.58 / 0.37 / 0.12, 0.29 |
| 18% | | 0.54 / 0.34 / 0.11, 0.27 |

Weights 13% / 44% / 43%, the deep dive's. At A$0.28 the market is discounting the deep dive's own paths at about 17.5%; at A$0.215 on 30 October it was about 21%.

### The cost of equity
13% is too low for this equity, but because of the double count it doesn't matter in the direction the deep dive feared. EML's own goodwill tests use 11.7% to 11.8% after tax for the whole company. At today's market values the equity carries a lot of debt: about A$103m of borrowings, leases and the shortfall provision against a A$110m market value (about A$65m if the cash is netted). Relevering 11.75% at those gearings with a borrowing cost of about 7.5% and no tax shield (EML carries A$18m of tax assets from losses it hasn't recognised, so interest saves little tax for now) gives 14% to 16%, before anything for size, the index exit and the record. I'd use 15% (14% to 17%). Done consistently, that gives a weighted value of about A$0.34, 20% above the price; the deep dive's A$0.29 is what a consistent 17% gives. So the business probably is somewhat below value on a long view, but within the range of reasonable discount rates, which is the same conclusion the deep dive reached: no clear mispricing today.

### Which single input moves the answer most
For the long-run value, the discount rate: A$0.27 to A$0.41 across 13% to 18%. For the four-month pick, it is the multiple the market pays after the half-year, which no discounted cash flow can give. That is section 5.

### Net assets
Tangible equity is A$22.4m, and A$5.9m after the A$16.5m tax asset. Goodwill of A$78.3m rests on 7% to 14% a year revenue growth to FY31 after a 6% fall in FY26. Book value (A$0.33 a share) is no floor: a buyer would pay for the float income and the client contracts, and nothing in the balance sheet would fetch book in a sale.

## 4. Capital, covenants and the shortfall

Regulatory capital. UK and EU rules require own funds of 2% of average e-money in the regulated issuers. The deep dive's A$29m (2% of A$1,464m of pound and euro float) is an upper bound: part of the UK float sits in "unregulated businesses" [S1 p13], and own funds are capital, not cash as such. But capital that has to be tangible can't come from goodwill, and the group's tangible equity is only A$6m to A$22m, so the deep dive's plain reading is right: the regulated subsidiaries' capital is in effect funded by the parent's bank debt. APS 610 adds up to A$21m (4% of A$534.5m of Australian float in CET1) if APRA licenses EML's Australian issuer and treats all of it as covered. EML expected the licence "within the next 12 months" of 30 March 2026, so the answer could come close to the resolve date. Treasury's reforms would remove the need if passed in their draft form.

Covenant headroom. At 0.407, about A$17m more borrowing, or A$21m less equity, breaches 0.45. Both move together in a bad half. Equity fell A$17.6m in the second half of FY26 alone (loss A$15.7m, currency translation A$5.8m, partly offset by share-based pay credited to equity), and the currency reserve has fallen A$11.9m in a year as the Australian dollar rose against the euro and pound. In the deep dive's bad path (FY27 free cash flow of minus A$6m, a statutory loss I estimate at about A$17m, A$15m of share-based pay credited back to equity), gearing at June 2027 is about 0.44 before any currency move or APRA capital. A A$15m to A$21m APRA requirement funded by debt would breach it on its own. The deep dive's statement that the A$31m undrawn facility funds FY27 is true only up to about A$17m.

The shortfall. A$13.6m, paid in cash in FY27, with a review that hasn't finished and that found A$1.8m arising in FY26 itself. I'd put the chance that the final figure is higher at about one in three.

Will the "non-recurring" costs keep running? Yes, on the record. Every year from FY23 to FY26 had A$10.7m to A$33.9m of them, a new category appeared in most years, and FY27 already has a new one (the ADI guarantee). The company's own FY27 Arlo figure is A$15.7m. The deep dive's view (falling from FY26's peak but A$10m or more a year) is reasonable, and if anything the shortfall review and the APRA licence make FY27 the riskier year.

## 5. The dated events and the exit

AGM, 18 November. A weak test, as the deep dive says: last year's Q1 was "in line with guidance forecasts" and the year was cut. Its threshold is miscalibrated, though. First quarters were A$11.6m (FY25, a A$58.6m year) and A$6.8m (FY26, a A$48.3m year); the second quarter, with Christmas gift cards, was about A$21m to A$22m in both. FY27 guidance needs a first half of about A$28m to A$31m (the first half was 57% to 58% of the year in both FY25 and FY26), so a Q1 of A$8m or more is on track. The deep dive's A$12m would read a normal quarter as a failure.

The half-year result, about 24 to 25 February 2027. This result can come and go without moving the price: 1H FY26 was in line and the stock fell 1.4% on the day and 15% over 20 sessions. The half will carry the shortfall payment and Arlo, so the cash flow will be negative even in the middling case, and the market has spent 15 months marking EML down for exactly that. The deep dive's reopening condition of A$25m of underlying EBITDA for the half is too low: on the last two years' split, A$25m points to a year of about A$43m to A$44m, below guidance. A$28m is the right bar.

Liquidity: fine. A A$2,016 position is 1.6% of a median day and 9% of the lowest day in October. Results come out before the open, so the price gaps; an exit rule can't avoid a fall like 13 April's (-36% on the day).

## 6. The stated chances and the outcome prices

### What EML's own results days have done
Close-to-close moves around each result or trading update since November 2023 (Norgate; VAS moved 1.1% or less on each of these days). The full set of 20 events from August 2021 is summarised under the table:

| Date | Event | Day | 5 sessions | 20 sessions |
| --- | --- | --- | --- | --- |
| 29 Nov 2023 | Strategic review update | -29.7% | -21.0% | -27.9% |
| 18 Jan 2024 | PCSIL exit | +22.1% | +18.8% | +30.9% |
| 28 Feb 2024 | 1H24 | +7.7% | +17.3% | +51.2% |
| 28 Aug 2024 | FY24 | -7.1% | -5.2% | -19.4% |
| 26 Nov 2024 | EML 2.0 plan, AGM | +29.2% | +43.1% | +15.3% |
| 26 Feb 2025 | 1H25 | +14.6% | +15.8% | +15.8% |
| 27 Aug 2025 | FY25 (in line) | 0.0% | -7.6% | -13.5% |
| 19 Nov 2025 | AGM update (in line, affirmed) | -0.6% | -1.7% | -8.0% |
| 25 Feb 2026 | 1H26 (tightened to the bottom) | -1.4% | -10.8% | -15.1% |
| 13 Apr 2026 | Guidance cut | -35.7% | -29.6% | -29.6% |
| 18 Aug 2026 | FY26 (in line with the cut) | -17.1% | -30.0% | -32.9% |

Across all 20 events since August 2021 the average move on the day was 15% either way and the median 20-session move was -11%; 3 of 20 were +29% or more over 20 sessions, none +79%. Over the 13 windows from early November to mid-March and early May to mid-September since 2019, each spanning a result, the median return was -18%; 3 were +29% or more (the best +66%) and 3 were -30% or worse. These carry the stock's long decline, so they aren't a forecast, but the deep dive's chances put 60% on +29% or more in four months, between two and three times what the stock has done in its own result windows, recoveries included.

### What the market pays after each kind of result
EV (market value plus adjusted net debt) over the guided underlying EBITDA for the year:

| Date | Price | EV | Guidance midpoint | Multiple |
| --- | --- | --- | --- | --- |
| 27 Aug 2025 (FY25) | A$1.115 | about A$462m | A$60.5m | 7.6 |
| 25 Feb 2026 (1H26) | A$0.685 | about A$306m | A$59.0m | 5.2 |
| 13 Apr 2026 (cut) | A$0.370 | about A$184m | A$48.5m | 3.8 |
| 18 Aug 2026 (FY26) | A$0.290 | A$173m | A$52.0m | 3.3 |
| 30 Oct 2026 | A$0.215 | A$145m | A$52.0m | 2.8 |
| 6 Nov 2026 | A$0.280 | A$170m | A$52.0m | 3.3 |

With adjusted net debt about flat at A$60m by December (the middling half, as the deep dive defines it, is cash-negative only by the shortfall and Arlo), each 0.1 of multiple on A$52m is about A$0.013 a share: 3.3 times is A$0.28, 3.5 times A$0.31, 3.85 times A$0.36, 4.5 times A$0.44.

### My outcomes
| Outcome | Chance | Price by 12 March 2027 | Why |
| --- | --- | --- | --- |
| Bad: guidance cut, one-offs outside Arlo above A$8m, Arlo budget up, the shortfall above A$13.6m, a raising or a covenant waiver | 45% (deep dive 40%) | A$0.17 (deep dive A$0.18) | The last two bad events took 30% to 36% off within five sessions: A$0.18 to A$0.20 from here. A cut to about A$45m at 2.8 to 3.0 times (the 30 October multiple) is A$0.15 to A$0.18; a raising at these prices would be heavily dilutive. Five triggers, any one sufficient; at least one fired at each of the last three reporting dates; the shortfall alone I put at one in three |
| Middling: in line with guidance, one-offs lower but present, cash negative only by the shortfall and Arlo | 40% (45%) | A$0.31 (A$0.36) | 3.5 times, a modest lift from 3.3. A$0.36 needs about 3.85 times, a lift the market hasn't given EML on an in-line result since February 2025 |
| Good: guidance held or raised, small one-offs, cash positive before the shortfall, proforma cash defined; or a bid | 15% (15%) | A$0.45 (A$0.50) | The two biggest 20-session recoveries (+51%, +54%) from A$0.28 give A$0.42 to A$0.43; 4.5 times is A$0.44; a bid at 5 to 6 times EBITDA with every right vested is A$0.43 to A$0.54 |

Expected price: 0.45 x 0.17 + 0.40 x 0.31 + 0.15 x 0.45 = **A$0.268**, -4.3% before costs.

Costs: as src/decide.py counts them on A$2,016 (half the 1.8% spread and 0.49% size cost each way, A$15 brokerage on the sale, A$15 on the buy unless the plan's monthly cover applies, 0.5% conversion once): 4.0% to 4.8%; the deep dive's 5.0% is slightly cautious. At 4.5%, **about -8.8% after costs**, against the 2.4% minimum. Quarter Kelly is zero.

How far each input would have to move:

| Chances | Bad / good prices | Middling A$0.31 | A$0.34 | A$0.36 |
| --- | --- | --- | --- | --- |
| 40 / 45 / 15 (deep dive) | A$0.17 / A$0.45 (mine) | -6.3% | -1.5% | +1.7% |
| 40 / 45 / 15 | A$0.18 / A$0.50 (deep dive) | -2.2% | +2.6% | +5.9% |
| 45 / 40 / 15 (mine) | A$0.17 / A$0.45 | -8.8% | -4.5% | -1.6% |
| 45 / 40 / 15 | A$0.18 / A$0.50 | -4.5% | -0.2% | +2.6% |

After costs at 4.5%, to 12 March 2027. The pick clears 2.4% only in the cells that keep the deep dive's bad and good prices and a middling price of A$0.34 or more. On my outcome prices the break-even entry is about A$0.25; at A$0.24 the expected gain is about +7%, and at the 30 October close of A$0.215 it would have been about +20%.

## 7. Why did the price rise 30% in the week to 6 November?

What can be checked:
- It was specific to EML. Of the 397 ASX companies with both a 30 October Norgate close and a 6 November price in the repo, EML's +30.2% was the fourth largest; the median was -1.1%.
- No ASX announcement from 19 October (the AGM notice, not price sensitive) to 6 November; the list I read on 8 November shows nothing newer.
- No substantial holder notice by 6 November, so before about 4 November no existing holder moved by 1% (Copia would have needed to reach 13.5%) and no new holder crossed 5%. A notice for a later crossing would be due by about 10 November.
- Short positions had already fallen from 16.0m (4.1%) on 1 September to 6.1m (1.6%) by 26 October, most of it around the index exit on 21 September, so covering can't explain much.
- Volume on 6 November was 2.01m shares, about A$0.55m, roughly four and a half times October's median day. Daily prices for 2 to 5 November aren't in the repo.
- The AGM notice holds only the usual business (remuneration report, one director's re-election, renewing the proportional takeover rule): no spill, no capital item.
- Web searches turned up no news of a bid, a broker note or a peer deal; the one Reuters item found was about the November 2025 AGM.

So the cause is unknown. Three readings fit: a bounce once forced selling (the index exit, Regal) had run its course, which can reverse before any event; someone building a stake, which a notice may show this week; or trading ahead of the AGM update. The first argues against buying at A$0.28; the second would lift the chance of a bid a little. Either way, a buyer today pays for part of a good outcome before seeing it.

## 8. The value pick test, as the rules stand

The deep dive's bad case for September 2028 (A$0.10, -64%) is too low because of the double count, but it still isn't close to the 10% floor. By method: 6 times FY28 free cash flow of A$6m is A$0.09; about 3 times FY28 EBITDA of A$46m less A$60m of net debt and leases is about A$0.19; the consistent discounted cash flow is A$0.23 at 15% and A$0.27 at 13%. And the bad path assumes no raising, no covenant waiver and no APRA capital call, each of which sits inside a genuinely bad two years: gearing reaches about 0.44 by June 2027 on that path before any of them. The middling case (A$0.42 to A$0.59 by method) clears +15% easily. The floor is the binding test and it fails, so it can't be held as a value pick.

## 9. Special situations

Not one. A bid is the upside tail inside the good outcome: the register is concentrated, the float earns A$57m a year, Bain and two other parties talked to EML in 2022 (per the deep dive's sources, which I didn't re-open), and every unquoted right (66.3m, 17% more shares) vests on a change of control. Nothing in the filings shows an approach now.

## The three points most likely to make this pick wrong
1. The middling price. An in-line half that still burns cash (the shortfall and Arlo both land in it) has not re-rated EML since early 2025; A$0.36 needs the multiple to rise from 3.3 to about 3.85 times. At 3.3 to 3.5 times the middling outcome is A$0.28 to A$0.31, and the case fails.
2. The bad case is more likely than 40%, and wider. It needs only one of five things to go wrong; the shortfall review is still running and found FY26 activity; APRA capital of up to A$21m is undisclosed and could land near the resolve date against about A$17m of covenant room; and the gearing ratio has to absorb losses and currency moves as well as borrowing.
3. The entry follows an unexplained 30% jump on thin trading. If it was a bounce after forced selling ended, the price can give it back before any event; Regal may still hold about 4.7%.

## Verdict
**Wait for a named event: the 1H FY27 result (about 24 to 25 February 2027).** No card now. The deep dive reached "wait" too, and its case for clearing the minimum rests on a middling price taken from a path-weighted value rather than from what the market pays; priced on EML's own history after results, the expected gain after costs is about -9% against +2.4%. Separately, its discounted cash flow counts the debt twice; corrected, the long-run value is higher than it says (about A$0.34 at a 15% cost of equity), which is a reason to keep watching, not a reason to buy for March.

Before the result:
- **AGM, 18 November.** Close the case until the result if first-quarter underlying EBITDA is below A$6.8m (last year's level), or guidance is qualified or cut. A Q1 of A$8m or more is on track; it doesn't reopen the case on its own.
- **Substantial holder notices this week.** A new holder above 5%, or Copia above 13.5%, explains the rise and lifts the bid chance; a change of control approach at any time reopens it as a special situation, as the deep dive says.
- **Shortfall review (by 31 December) and the 31 December covenant test.** A final shortfall above A$13.6m closes the case; any APRA capital figure goes into the covenant arithmetic above.
- **Watch trigger: A$0.24 or lower** with nothing else changed (my break-even for the minimum is about A$0.25; A$0.24 leaves a margin).

At the result, reopen as an ordinary pick resolving at the FY27 result (late August 2027) only if all of these hold, and price the outcomes from the multiple the market then pays, not from weighted path values:
1. Underlying EBITDA for the half of A$28m or more (not A$25m), with FY27 guidance of A$50m to A$54m held.
2. One-offs outside Arlo of A$4m or less in the half, and no new category above A$1m.
3. Arlo's non-recurring spend for the half of A$9m or less, with the A$34m budget and timetable unchanged.
4. The shortfall settled at or below A$13.6m, with no further current-period shortfall.
5. Operating cash flow before the shortfall payment positive; drawn debt A$95m or less; gearing 0.42 or less at 31 December.
6. The APRA position stated: the guarantee in place at its cost, or the licence's capital need quantified and funded within the covenant.
7. "Proforma" free cash flow defined; if it is before interest, tax or the one-offs, cut it accordingly before using it.

Close it on a guidance cut, a shortfall above the provision, a higher Arlo budget, a raising, a covenant waiver, or gearing above 0.43.

If a later card does go ahead, the exit rule I'd want on it: sell on any of the closing conditions above, on a new non-recurring line above A$3m, and at the resolve date if the reopening conditions no longer hold.

## What I couldn't verify
- The cause of the rise from A$0.215 to A$0.28, and daily prices and volumes for 2 to 5 November.
- Whether Regal sold its remaining shares (about 18.4m) after 2 September.
- How much of the A$37.8m of cash each regulated subsidiary holds, its own funds, and how much of the UK float is in regulated issuers.
- The status of the APRA guarantee and licence since 1 May 2026, and what capital EML expects to hold; the FY26 accounts are silent.
- Whether Treasury's payments bill has been introduced; the last status I could read was the exposure draft with introduction aimed for 2026.
- The definition of "proforma" free cash flow.
- FY23 and FY24 add-backs and cash flows (I didn't re-open the 2024 annual report) and Tyro's figures.
- First-quarter FY27 trading.

## Sources
- [S1] 2026 Appendix 4E and Annual Report, 18 Aug 2026 (03126182): release, performance overview pp13 to 17, notes 7, 16, 19, 20, 21, 23, 28, parent entity note, auditor's report: https://announcements.asx.com.au/asxpdf/20260818/pdf/072vww3jvymxwc.pdf
- [S2] FY26 Results Investor Presentation, 18 Aug 2026 (03126187), pp9, 18, 20: https://announcements.asx.com.au/asxpdf/20260818/pdf/072vx7c3wvy876.pdf
- [S3] EML Announces 1HFY26 results, 25 Feb 2026 (03064563): https://announcements.asx.com.au/asxpdf/20260225/pdf/06wqbfzq6cd51z.pdf
- [S4] AGM Trading Update, 19 Nov 2025 (03028371): https://announcements.asx.com.au/asxpdf/20251119/pdf/06s5t7v4cz5lny.pdf
- [S5] FY26 Underlying EBITDA Guidance Revised, 13 Apr 2026 (03081864): https://announcements.asx.com.au/asxpdf/20260413/pdf/06yf139py9nwz7.pdf
- [S6] Global CEO Appointment and Australian Regulatory Update, 30 Mar 2026 (03077129): https://announcements.asx.com.au/asxpdf/20260330/pdf/06xy6gx7ykwg97.pdf
- [S7] Australian Regulatory Update, 1 May 2026 (03089231): https://announcements.asx.com.au/asxpdf/20260501/pdf/06z3vc8cl1ln20.pdf
- [S8] Change of Director's Interest Notice (Hynes), 13 Mar 2026 (03071606): https://announcements.asx.com.au/asxpdf/20260313/pdf/06xcqx8w0yxyjg.pdf
- [S9] EML 2026 Notice of Annual General Meeting, 19 Oct 2026 (03153951): https://announcements.asx.com.au/asxpdf/20261019/pdf/075h23xm3264bb.pdf
- [S10] Change in substantial holding (Copia), 18 May 2026 (03095007), read by OCR: https://announcements.asx.com.au/asxpdf/20260518/pdf/06zq0rkh5pl7dq.pdf
- [S11] Change in substantial holding (QVG Capital), 30 Sep 2026 (03146446): https://announcements.asx.com.au/asxpdf/20260930/pdf/074rg6k0mzbmzy.pdf
- [S12] Change in substantial holding (Regal), 3 Mar 2026 (03067933): https://announcements.asx.com.au/asxpdf/20260303/pdf/06x0nz18lyyn2d.pdf
- [S13] Change in substantial holding (Regal), 15 Jun 2026 (03104267): https://announcements.asx.com.au/asxpdf/20260615/pdf/070n99jckhf121.pdf ; 19 Jun 2026 (03105984): https://announcements.asx.com.au/asxpdf/20260619/pdf/070tbd9vlm926t.pdf
- [S14] Change in substantial holding (Regal), 24 Aug 2026 (03129133): https://announcements.asx.com.au/asxpdf/20260824/pdf/0734f76hb2jkkt.pdf
- [S15] Ceasing to be a substantial holder (Regal), 4 Sep 2026 (03136169): https://announcements.asx.com.au/asxpdf/20260904/pdf/073rf3vs2d7jtr.pdf
- [S16] Ceasing to be a substantial holder (WAM/WMI), 3 Mar 2026 (03067958): https://announcements.asx.com.au/asxpdf/20260303/pdf/06x0r4vr368dxf.pdf
- [S17] Notification of cessation of securities, 8 Oct 2026 (03150095): https://announcements.asx.com.au/asxpdf/20261008/pdf/07530k0z46mzfj.pdf
- [S18] S&P DJI Announces September 2026 Quarterly Rebalance, 4 Sep 2026 (03136141): https://announcements.asx.com.au/asxpdf/20260904/pdf/073rbz4q8nrckg.pdf
- [S19] ASX announcements lists for EML, 2021 to 2026 (read 8 Nov 2026), for event dates and price-sensitive flags: https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=EML&timeframe=Y&year=2026
- [R1] APRA Prudential Standard APS 610 (June 2023), paragraphs 13 and 14: https://www.apra.gov.au/sites/default/files/2023-05/Prudential%20Standard%20APS%20610%20Prudential%20Requirements%20for%20Providers%20of%20Purchased%20Payment%20Facilities%20-%20clean_0.pdf
- [R2] Gilbert + Tobin, "Regulation of payment service providers: where things stand" (secondary; status of Treasury's reforms): https://www.gtlaw.com.au/insights/regulation-in-motion/regulation-of-payment-services-providers
- [W1] Reuters via Tiger Brokers, 19 Nov 2025, on the 2025 AGM update (secondary, for the date only): https://www-web.itiger.com/news/2584624049
- [M1] data/research_data/asx_company.json (fetched 7 Nov 2026 UTC): EML header and key statistics, and every company's 6 November price for the cross-section.
- [M2] data/norgate/universe/prices_2019.csv.gz to prices_2026.csv.gz: EML.au and VAS.au daily prices to 30 Oct 2026; 2026 file for the 30 October cross-section.
- [M3] data/asic/shorts_2025.csv.gz and shorts_2026.csv.gz: EML short positions and shares on issue.
