# Mayne Pharma (ASX:MYX): what the business is worth on its own

Written 2026-11-02 by the research desk. Settles the gap between the fact sheet (research/facts/MYX.md, about A$2.93 a share) and the external special situations review (about A$0.60, weighted A$0.73). Both leave out any damages from the Cosette claim. Price A$2.54 (close 30 Oct 2026). Arithmetic run in `python3 -I`. This is a simulation and not financial advice.

## The answer
On the inputs the filings support, the business alone is worth about **A$0.51 a share** at the fact sheet's own 10 times multiple, and nothing at all below about 8.5 times. The review (A$0.60) was much closer. The fact sheet's A$2.93 came from the FY25 earnings figure and June cash; the same sheet's section 6 already gets A$0.52 when it uses the last twelve months, so the A$2.93 line and the "+15% on the business alone" read should not be relied on.

## Where the two differ
| Input | Fact sheet (A$2.93 line) | Review (A$0.60) | What the filings say | Used here |
| --- | --- | --- | --- | --- |
| Earnings base | FY25 underlying EBITDA A$47.0m | FY26 underlying EBITDA A$34.2m | FY26 A$34.2m [1][2]. Quarters: Q1 FY26 A$11.0m, Q3 minus A$1.4m, Q4 A$4.6m, Q1 FY27 A$5.3m [3][4][5]. Last twelve months to Sep 2026: 34.2 - 11.0 + 5.3 = A$28.5m | A$28.5m |
| Is the base cash? | EBITDA | EBITDA, plus a made-up cash forecast | Royalties are paid out of the earn-out liability, so they sit outside underlying EBITDA and the payments show as financing cash flows [2]. FY26 operating cash before Cosette costs A$25.6m, earn-out payments A$25.7m, capex A$3.3m, leases A$3.2m: minus A$6.6m after obligations [1] | EBITDA, with the full earn-out liability deducted |
| Earn-out royalties | Book A$264.8m deducted | Book A$264.83m deducted in one method; paid inside the DCF in the other | Other financial liabilities A$265.5m at 30 Jun 2026 after a A$125.6m downward reassessment, A$34.2m of discount unwind and A$25.7m paid [1]. Royalties paid were A$3.5m in the Sep 2026 quarter [5]. The TXMD licence pays 8% of the first US$80m of annual net sales and 7.5% above, for 20 years from closing, with a US$3m yearly minimum for 12 years and sales milestones of US$5m, US$10m and US$15m [6] | Book A$264.8m |
| Convertible notes | A$41.1m face | A$41.1m principal | Repayable at a fixed A$ amount; the annual report gives the amount repayable as A$41.6m [1]. Issued in Dec 2022 as US$27.95m [7]. Due 31 Dec 2026 per both pieces; the date is in the notes, which I could not open | A$41.6m |
| Cash | A$80.0m (30 Jun) | A$67.3m (30 Sep) | A$80.0m at 30 Jun, A$67.3m at 30 Sep 2026 [1][5] | A$67.3m |
| Leases | A$4.1m | Left out | A$43.1m of interest-bearing liabilities with leases, A$39.1m without [1] | A$4.1m |
| Cash reserve | None | A$25m deducted | No minimum cash figure is disclosed | None |
| Multiple or discount rate | 10 times | 6 times, or a 15% DCF on assumed flows of 5, 8, 12, 15, 18, then averaged | The filings give no multiple. The price implies 15.8 times last twelve months' EBITDA once earn-outs are counted | 10 times, with a range |
| Shares | 81.89m | 81.25m | 81,245,827 at 30 Jun 2026 [1]; 81.89m per the fact sheet | 81.89m (under 1c difference) |

## The arithmetic
Net financial liabilities at 30 Sep 2026: earn-outs 264.8 + notes 41.6 + leases 4.1 - cash 67.3 = A$243.2m.

Moving the fact sheet's A$2.93 one input at a time (10 times throughout):

| Step | Equity A$m | Per share |
| --- | --- | --- |
| Fact sheet start: FY25 EBITDA 47.0, June cash | 240.0 | A$2.93 |
| FY26 EBITDA 34.2 | 112.0 | A$1.37 |
| Last twelve months EBITDA 28.5 | 55.0 | A$0.67 |
| September cash 67.3 | 42.3 | A$0.52 |
| Notes at A$41.6m repayable | 41.8 | **A$0.51** |

The multiple decides the rest. Equity is nil at 6 or 8 times, A$0.51 at 10, A$1.21 at 12, and the A$2.54 price needs 15.8 times. Each turn of the multiple is worth about 35c a share; equity reaches zero at 8.5 times.

Two checks point the same way. After royalties, capex and leases the business used A$6.6m of cash in FY26, and in the Sep 2026 quarter adjusted operating cash was minus A$2.1m before A$3.5m of royalties [1][5]. Cash left after repaying the notes and leases is about 26c a share. A generic RHOFADE launched in the US in July 2026 and the company expects lost share [4], so the last twelve months (which hold the strong Dec 2025 quarter, A$17.6m) may flatter the year ahead.

## Which was closer, and why
The review, by a long way. The fact sheet's A$2.93 rests on FY25 earnings, which were A$12.8m higher than FY26 and A$18.5m higher than the latest twelve months, and on June cash that had fallen A$12.7m by September. Those two inputs explain A$2.41 of the A$2.42 gap to A$0.51. The review got the base nearly right (FY26, September cash) but reached A$0.60 by averaging a zero with a DCF built on cash flows the filings don't show, and it added a A$25m reserve the company doesn't state. On the filed inputs its zero-to-A$1.19 spread and our A$0.51 say the same thing: the business alone is worth well under the A$2.54 price.

Open points. The annual report notes (earn-out maturity table, the A$13.2m current portion, the 31 Dec 2026 note date and A$5.356 conversion price) could not be read; the text available stopped before the financial statements. The A$41.1m against A$41.6m note figure is worth checking in the annual report notes, but it moves the value by under 1c.

## The claim against Cosette
Cosette has until 11 November 2026 to seek special leave from the High Court after the 14 October 2026 Court of Appeal decision, which dismissed its appeal on all grounds and gave Mayne its costs [8]. The damages claim filed on 18 February 2026 against Cosette, its parent, Avista and David Burgstahler has no hearing date [9]. The most it could add is the lost premium: A$7.40 less A$0.51, about A$6.89 a share or A$564m, before legal costs, the effect of the Treasurer's objection on what the deal was worth, and collection; a judgment or settlement inside six months is unlikely, and 2027 to 2028 is more realistic.

## Sources
1. Mayne Pharma, 2026 Appendix 4E and Annual Report, 27 Aug 2026: https://announcements.asx.com.au/asxpdf/20260827/pdf/0739clm7672t5m.pdf
2. Mayne Pharma, 2026 Full Year Results Media Release, 27 Aug 2026: https://announcements.asx.com.au/asxpdf/20260827/pdf/0739cyd4kqt28m.pdf
3. Mayne Pharma, unaudited 3Q FY26 results, 29 Apr 2026: https://announcements.asx.com.au/asxpdf/20260429/pdf/06yzl19ttybj11.pdf
4. Mayne Pharma, unaudited Q4 and FY26 results, 31 Jul 2026: https://announcements.asx.com.au/asxpdf/20260731/pdf/0728fx3t3rq6xg.pdf
5. Mayne Pharma, unaudited Q1 FY27 results, 26 Oct 2026: https://announcements.asx.com.au/asxpdf/20261026/pdf/075rnwfkwnmchj.pdf
6. TherapeuticsMD, Form 10-Q for the quarter to 30 Jun 2026 (Mayne licence terms): https://www.sec.gov/Archives/edgar/data/0000025743/000121390026087768/ea0297949-10q_therapeutics.htm
7. Mayne Pharma, FY24 Appendix 4E and Annual Report, 23 Aug 2024: https://announcements.asx.com.au/asxpdf/20240823/pdf/066yhqdjyzd76b.pdf
8. Mayne Pharma, Supreme Court Decision in Cosette Proceedings, 14 Oct 2026: https://announcements.asx.com.au/asxpdf/20261014/pdf/0759tbjwhnljq5.pdf
9. Mayne Pharma, MYX to claim against Cosette, Avista and Mr David Burgstahler, 18 Feb 2026: https://announcements.asx.com.au/asxpdf/20260218/pdf/06wfm3q5b2qss3.pdf
