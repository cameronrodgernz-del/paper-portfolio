# Red team: Garda Property Group (ASX:GDF), special situation deep dive of 8 November 2026

Written 2026-11-08 by the red team, working only from research/picks/GDF.md, docs/RED_TEAM.md, RULEBOOK.md sections 3, 4 and 5a, and the primary sources listed at the end. This is a simulation, not financial advice.

Price: A$1.12 (last trade 6 November 2026, bid A$1.11, ask A$1.12, data/research_data/asx_company.json). The deep dive was written after the 8 November rule changes and applies them, so it is tested against the rules as they stand: the minimum expected gain after costs is the 2.13% cash rate plus 5% a year, 3.38% over the 173 days to 30 April 2027 (src/decide.py works it as (rate + 0.05) x days / 365); a value pick needs its bad case no more than 10% below the price and its middling case at least 15% above it.

In short: the facts the case rests on mostly hold, and the analyst's "wait" is right, but the case is weaker than the deep dive says. On my chances the expected gain after costs is about +1.4% against the 3.38% minimum. Four things the deep dive missed push that way: the loan book's LVRs rose between July and October; the company's own repayment schedule puts 78% of the next 12 months' repayments in January to June 2027, so the 1H27 result can't show the cash test the case turns on; the last time Garda had sale cash and a big discount (late 2025) it lent the money and the discount widened from 29% to 38%; and the special distribution release splits the capital gains between quarters in a way its own property table contradicts, which leaves more of the March special resting on Morningside than the deep dive assumes.

## 1. Are the facts right?

Fifteen facts re-checked against the filings. Eleven held as written, one held and turned out stronger than stated, one (the quarterly split of the specials) needs a correction, one was wrong (no on-market sells by directors), and one item the deep dive couldn't verify is now resolved.

| # | Fact in the deep dive | Source re-opened | Result |
| --- | --- | --- | --- |
| 1 | 218,070,098 quoted securities | Appendix 2A, 29 Oct 2026 (497,076 issued 22 Oct) and the listing rule 11 table in the sale release (217,573,022 before it) | Held |
| 2 | Pro forma: cash A$176.6m, loans A$140.1m, liabilities A$10.5m, net assets A$313.8m, NTA A$1.56, gearing 0% | Divestment presentation p7 | Held (cash 176,583; loans 121,544 + 18,521; net assets 313,829) |
| 3 | Loan limits A$194.1m excluding the A$60m Burleigh construction facility; group 8 A$95.9m (49%); 71% of limits at 80% LVR or more; limit-weighted LVR about 87%, 78% after presales | Divestment presentation p15, recomputed loan by loan | Held (87.0%, 78.1%, 71.2%, 49.4%). The group 8 subtotal of A$155.9m and the Burleigh line of A$76.9m both include the A$60m |
| 4 | FY26 lending income almost all added to loan balances, not paid in cash | Annual report: cash flow reconciliation, notes 3e, 3f and 11 | Held, and stronger: interest on amortised cost loans was A$11,577k and the cash flow reconciliation backs out A$11,572k of capitalised interest; the other A$7,586k of lending revenue is a non-cash fair value gain. Only A$160k of fees could have been cash |
| 5 | Specials of 7.3c (December quarter) and 2.7c (March quarter), against net capital gains of 15.3c and 5.5c | Special distribution release; divestment presentation p8 | The release says this, but its own property table contradicts the quarterly split (see below). The deep dive caught the 9.8c/10.0c and 1 Dec/20 Nov mismatches but not this one |
| 6 | Quarterly ex-dates and payment dates follow last year's pattern | Appendix 3A notices of 17 Dec 2025, 19 Mar 2026, 23 Jun 2026, 23 Sep 2026 | Held. Ex 29 Dec 2025, record 30 Dec, paid 16 Jan; ex 30 Mar 2026, record 31 Mar, paid 16 Apr; ex 29 Jun, paid 15 Jul; ex 29 Sep, paid 15 Oct. So the December quarter goes ex about 29 or 30 December 2026 and the March quarter about 30 March 2027, paid about 15 April, inside the 30 April resolve date |
| 7 | Buyback authority up to 21m securities from 22 Apr 2026 to 21 Apr 2027, through Morgans; none bought in FY26 | Appendix 3C and extension notice, 2 Apr 2026; annual report p18 ("preferring to invest in more accretive opportunities") | Held |
| 8 | 14.68m ESP securities carrying A$15.01m of limited recourse loans | Annual report note 17b and the ESP table in note 18 | Held |
| 9 | HGT 37,340,745 securities, 17.22% of 216,801,897 at 11 Dec 2024; last on-market buying Feb to Mar 2023 | HGT Form 604, 11 Dec 2024 | Held |
| 10 | Directors' dealings in two years: buys by Thornton and Leitch, Madsen's off-market transfers; "No on-market sells" | Appendix 3Y notices | Wrong. Mark Hallett, then an executive director, sold 480,000 securities on market on 11 to 14 August 2025 for A$600,360 (about A$1.25) through TSpan Pty Ltd. He retired from the board at the 27 November 2025 AGM and stays on as an executive, so any later dealings by him are not notified. Small, but the claim is wrong |
| 11 | Morningside "remains subject to due diligence, which Garda expects to continue throughout October 2026" | Sale release p1, footnote 3 | Held. Footnote 4 adds that Morningside was independently valued at A$66.3m at 30 June 2026, with A$14.8m of cost to complete added to reach the A$81.1m carrying value. Nothing on the due diligence by 7 November, although Garda announced the Pinkenba and Heathwood conditions separately |
| 12 | Auditor change: Pitcher Partners out after a tender, "no reportable matters", PwC in for the fund from 4 November and the company from the AGM | Change of auditor, 5 Nov 2026 | Held. The 1H27 accounts will get a PwC review, which is limited assurance, not an audit |
| 13 | Peer NTAs: TCF A$5.968, MRE A$2.2953, MXT A$1.9613, QRI A$1.6000 | NTA notices of 8 Oct, 14 Oct (two) and 4 Nov 2026 | Held. Prices on 30 Oct from Norgate match |
| 14 | Running costs after the sale A$7.3m a year | Sale release, listing rule 11 table (A$7,268k) | Held |
| 15 | The "Loan receivables 90 days 15.4" line, left unresolved by the deep dive | Annual report note 11e | Resolved: A$15,365k is the repayments expected in the first three months after 30 June, so it means loans due within 90 days, not loans 90 days past due |

### The special distributions don't add up by quarter
The presentation's table (p8) gives each property's gross capital gain. Sorted by when each property settles:
- Settling in the December quarter (the six Charter Hall properties on 20 November or 1 December, and Heathwood): A$54.2m, 24.9c gross, about 12.5c net.
- Settling in the March quarter (Pinkenba on 22 January, Morningside about March): A$36.5m, 16.8c gross, about 8.4c net. Morningside alone is A$21.4m, 9.8c gross, 4.9c net.

The release's split (30.6c gross in December, 11.1c in March) matches the table's subtotals by buyer instead: the Charter Hall assets including Morningside, and Heathwood plus Pinkenba. The release's own text says Morningside settles in the March quarter and that gains are attributed in the period the property settles. So either the release mislabelled the quarters, or the board will key the specials to something other than the settlement quarter. If the specials follow each quarter's net gain at the release's ratio (about 48%), the December special is about 6.0c and the March special about 4.0c, still about 10c in all. Either way the March special rests mostly on Morningside: if Morningside's due diligence fails, or its construction slips settlement past 31 March, the March quarter's gain falls to Pinkenba's 3.5c net and the special at the same ratio to about 1.7c, with the rest later or never.

Answer to the question the brief asked: yes, the March special depends on the Morningside settlement, more heavily than the deep dive assumed (it put the loss from a failed Morningside at the 2.7c; on the property table it is about 2.3c to 2.4c of a March special that could be 4c). The value effect is small, since a special pushed past 30 April stays in the book at the multiple (about 0.8c lost per security on my outcomes), but it changes the deep dive's price watch triggers, which assume 10.7c goes ex in December. If the split follows settlement, about 9.4c goes ex in December and the post ex-date trigger rises by about 1.3c.

### Left out of the deep dive
- Mark Hallett's on-market sale in August 2025 and his retirement from the board (above).
- The loan book moved the wrong way between the FY26 results deck (30 July) and the divestment deck (21 October), on the same facilities:
  - group 2 (Brisbane apartments, not started): LVR 94% to 96%, after presales 73% to 82%;
  - group 3, Mackay townhouses: limit A$12.86m to A$16.81m (+31%), LVR 75% to 87%;
  - group 4, second-ranking junior loan: limit A$8.45m to A$9.46m, LVR 91% to 96%; the Gold Coast corporate facility on the settling project rose from A$7.64m to A$8.36m while settlements went from 78 of 103 to 84 of 104;
  - group 8, Eagle Farm: LVR after presales 61% to 73%, with 62% of units sold. The FY26 deck's case study 3 (a repeat borrower's 16-unit strata project in the Trade Coast precinct, which by its description appears to be this loan) showed 63% presold and effective leverage of about 53% at origination in October 2025, on an A$18.9m facility that is now A$21.07m.
  - Book-wide, the share of limits at 80% LVR or more rose from 65.6% to 71.2% and the weighted LVR after presales from 64.6% to 78.1% (partly because a Sunshine Coast loan at 0% after presales was repaid).
  With interest capitalised at about 19% to 22% a year, balances grow 1.5% or more a month unless sales keep pace. Rising LVRs are what that looks like.
- A further A$36.0m of limits (18.5%) are corporate facilities with no LVR at all (group 4's two Gold Coast facilities, one "repayable after project financier", and group 8's A$6.8m). Only about A$20m of the A$194m (10%) sits on loans below 80% LVR.
- The repayment schedule (note 11e): of A$148.6m expected back in the 12 months from 30 June 2026, A$15.4m falls in July to September, A$17.4m in October to December, A$51.9m in January to March and A$63.9m in April to June. Only A$32.8m (22%) falls in the half the 1H27 result covers.
- The macro backdrop, from a peer's filing: TCF's September quarter update (22 Oct 2026) reports the RBA raised the cash rate 25 basis points in September 2026 to 4.60%, noting rising unemployment and house prices falling faster than expected, and says many credit funds are facing redemptions and developers greater stress. Garda's own divestment deck cites persistent inflation and weakening growth. Groups 2, 3 and 4, all residential, hold 44% of Garda's limits.
- TCF's chief executive resigned on 5 November 2026, more stress at the peer the deep dive leans on.
- Governance: one independent director (Leitch) on a board of four, with an Executive Chairman who holds 10.96m ESP securities on A$11.05m of loans, overseeing the marks on a concentrated book.
- Related parties: note 19 and remuneration report section 11 disclose no transactions with directors, executives or their related parties, so neither HGT nor Thornton's Great Western Corporation is a disclosed borrower. Nothing left out here, but the "seven borrower groups" overstate the spread: every facility within groups 3, 4 and 8 is cross-collateralised, group 4's junior loan is to be repaid from its Gold Coast project, and the three largest groups hold A$168.8m, 87% of limits.

No capital raising (employee issues only), no substantial holder selling notice since 2024, no lawsuit or regulator action, and an unmodified FY26 audit opinion: the deep dive has these right.

## 2. Is it really overlooked, or is it cheap for a reason?

Cheap for a reason, mostly. The deep dive says the same.
- The most relevant comparable is Garda itself, a year ago. On 19 November 2025, with the North Lakes and Cairns sales done and A$71m of debt capacity freed, the price was A$1.13 against NTA of A$1.60 (a 29% discount, per Garda's own update). The board put the cash into loans (the book grew from A$44m to A$134m) and bought nothing back. By 20 October 2026 the price was A$1.025 against NTA of A$1.65, a 38% discount. Holders made about -1.5% over those eleven months including 8.75c of distributions. The deep dive cites the 2023 to 2024 buyback as the precedent for its middling case; the 2025 precedent is more recent, closer to today's position, and went the other way.
- Who is selling: post-announcement volume was about nine times normal (A$0.7m to A$0.9m a day for two days), and no substantial holder has filed. The buyers were likely yield and special-distribution buyers, who may leave once the specials go ex.
- Peers show the sector's trouble: TCF, MRE, MXT and the omitted MOT fell 16% to 28% between 2 January and 30 October 2026 (Norgate).
- Management's record against its own guidance is fair: FY26 distributions of 8.5c beat the 8.0c guided in November 2025. But FY27's 12.5c FFO can be met on accrued, capitalised interest even if no borrower pays cash, so meeting it says little about the loans.
- No debt falls due: all A$185.3m is repaid on 20 November.

## 3. The valuation

- Peers: the deep dive's range of 0.63 to 0.96 times NTA stands, but it left out Metrics Income Opportunities Trust (MOT), the Metrics vehicle that takes higher-yield credit and equity-like positions, the closest in risk to Garda's mezzanine and early-stage book. MOT closed at A$1.36 on 30 October against NTA of A$1.9324 at 30 September: 0.70 times, yielding about 10.0% (1.13c a month). With MOT in, the higher-risk lenders sit at 0.63 (MRE) and 0.70 (MOT), the senior-heavy TCF at 0.81, and Garda at 0.715. Garda is priced with its closest peers, not below them.
- The middling multiple of 0.80 is TCF's and MXT's level, for books that are more senior (TCF: 81.8% senior first mortgages at a 67.5% LVR) than Garda's 87% weighted LVR. It also sits above the top of Garda's own range: the company's chart shows year-end discounts of 22% to 36% (0.64 to 0.78 times). I keep the analyst's 0.80 times for the middling value but test 0.78.
- The book of A$1.408 a security after the specials is right on the deep dive's method. The question is what it would fetch. About half of it is cash, worth face. Counting the cash at face, today's price values the loans and the platform well under their book, and the A$7.3m a year of running costs (about 28c a security capitalised at 12%) explains much of that gap. That isn't a mistake by the market; it's the cost of an internally managed lender.
- Method B (yield) is the input that moves the answer most: 12.5c at TCF's 12.6% gives A$0.99, at MXT's 10.8% A$1.16. Garda's yield on the ex-special price (12.4% to 13.5% on the 3.4c run rate) already matches TCF's, so the market is paying Garda as a riskier TCF, which is what it is.

## 4. The dated events and the exit

- The 1H27 result (about 4 February 2027; 4 Feb 2026 and 6 Feb 2025 before it) is weaker evidence than the deep dive says. It will show NTA after a PwC review, the credit loss allowance and where the cash went. It can't show the thing the deep dive rightly calls the true test, loans repaid in cash with their accrued interest, because the company's own schedule puts A$115.8m of the A$148.6m in January to June 2027. That half is reported at the FY27 result in about August 2027, after the 30 April resolve date and after the counted run ends on 2 July. Some January repayments (Richlands completes in December, group 3's Sunshine Coast loan in December to January) may be mentioned at the result, but only in part.
- The deep dive's reopen condition (c), at least A$40m repaid in the half, is above the company's own schedule of A$32.8m (including interest and fees) for July to December. A clean half would likely fail it. Better: repayments at or above that schedule, and Richlands (A$44.7m) repaid or at least 60% sold by the result.
- The AGM on 26 November is the only near event that could supply a reason the market is wrong (a buyback commitment). On the 2025 precedent and the board's words ("the primary destination" for the cash is lending; buybacks are "subject to market conditions"), I put a commitment of 5% or more at about 15%.
- 20 November settlement: confirms what the price assumes. Morningside's due diligence result is the useful news there.
- Distribution dates: verified above. Both quarters' payments should land inside the window if the board keeps its pattern; the size of the March special depends on Morningside settling by 31 March.
- Liquidity: the 20-session median of A$46,184 a day (verified from Norgate) includes the post-announcement surge; before it the median was about A$38,000. A A$2,016 position is about 5% of a normal day. It can be sold in a bad week. Thin trading after the specials could widen the spread.

## 5. The stated chances

The deep dive's outcome values check out arithmetically (0.70, 0.80 and 0.92 times A$1.408, plus 1.1c of accrued June quarter distribution, plus 16.8c received). Its expected value of A$1.194 (+6.6% before costs) is right on its own chances. I differ on the chances and on the worst value.

| Outcome | Deep dive | Red team | Why I differ |
| --- | --- | --- | --- |
| Worst: a credit problem shows at the 1H27 result | 15%, A$0.95 | 17%, A$0.93 | LVRs rising on five facilities in four of the five largest groups since July; 100% of FY26 interest capitalised; an RBA rate rise with house prices falling and credit funds facing redemptions, which hurts refinancing; Richlands completes in December 58% unsold; FY26 already carried A$2.4m of loan charges (A$1.1m allowance, A$1.3m fair value loss, both added back in FFO); a new auditor. The value: the deep dive's A$0.95 is a moderate problem. A group 8 default with a 25% loss on A$95.9m at 0.55 times is about A$0.88, so I blend 13% at A$0.95 with 4% at A$0.88 |
| Bad: nothing happens | 50%, A$1.165 | 58%, A$1.165 | The more likely result when the board lends rather than buys back and the result can't show repayments. The value could be lower: if the special-distribution buyers leave, the multiple could go back toward the pre-sale 0.64 times (A$1.075); MOT is at 0.70. I keep 0.70 times and test 0.68 |
| Middling: re-rates to 0.80 times | 28%, A$1.305 | 20%, A$1.305 | The 2025 precedent (sale cash went to loans, the discount widened); the 1H27 result can't show the repayment wave; 0.80 times is at or above the top of Garda's own recent range and above its closest peer |
| Good: capital return, large buyback, wind-down or bid | 7%, A$1.474 | 5%, A$1.474 | Board, HGT and the Executive Chairman all back lending; no sign of a bid; HGT hasn't bought on market since March 2023 |

Expected value on my chances: A$1.169, +4.4% before costs. Costs: I agree with the deep dive's 2.6% to 3.3% (spread about 0.8% paid half each way, size cost about 0.27% each way, A$15 brokerage each way unless the plan covers the buy, 0.5% currency conversion); central 3.0%.

| Chances and values | After costs (3.0%) | Against the 3.38% minimum |
| --- | --- | --- |
| Red team central, 17/58/20/5 | +1.4% (+1.1% to +1.8% across costs) | Fails by about 2 points |
| Red team, bad case at 0.68 times | -0.1% | Fails |
| Red team, middling at 0.78 times | +0.9% | Fails |
| Red team, if the AGM commits to a buyback of 5% or more (16/46/32/6) | +3.4% | On the line |
| Deep dive's chances, my worst value | +3.4% | On the line |
| Deep dive's chances and values, bad case at 0.68 times | +2.3% | Fails |
| Deep dive as written | +3.6% (+3.3% at 3.3% costs) | Clears by 0.2 points, fails at the top of its own cost range |

So the case clears only on the analyst's own chances with costs at or below 3.0%, and the analyst's write-up concedes it can't state why the market is wrong, which section 5a requires of every pick whatever its expected gain. On my chances it clears at A$1.10 or below before the December ex-date (A$1.08 if the bad case is 0.68 times), and about A$1.00 after it (A$0.99). The deep dive's watch trigger of A$1.10 is close to mine; I'd watch A$1.08. A price trigger should reopen the case for review, not place a card: a fall with no news in a stock like this may be someone who knows the book selling.

Sizing: on any of these chance sets a quarter of the Kelly stake is far above the 2.5% cap, so the cap binds at about A$2,016. The worst value would lose about 17% of that, about NZ$425, 0.4% of the portfolio.

## 6. Special situations only

- The "nothing happens" value: about right at 0.70 times while the specials are pending, but not a floor. Once the March record date passes the situation is over, and the register that bought for the specials may unwind toward the pre-sale 0.64 times (about A$1.075 at 30 April, -4%). The worst outcome, not the "nothing happens" value, is the real floor, and a full group 8 default would go below the deep dive's A$0.95.
- Can the named parties do what the case needs? The case needs the board to buy back or return capital, or the market to re-rate a lender. The board can (A$176.6m of cash, an authority for 21m securities to 21 April 2027), but its record and words say it will lend. HGT can block, requisition and creep only through a buyback; it shows no sign of wanting cash back, and its director sits on the board that chose lending. Madsen's ESP securities struck at A$1.20 and A$0.96 give him a reason to want a higher price, but through a bigger lending business, which is what he says.
- Comparable cases: Garda in 2025 to 2026 (sale cash lent out, discount widened from 29% to 38%, about -1.5% for holders over eleven months); TCF (income paid, discount stayed, now a CEO departure); Australian Unity Office Fund (holders got NTA in cash only through a vote to wind up, which Garda's board and largest holders aren't proposing).
- Deal sleeve: no. The property sales are binding, but they pay Garda, not its holders; the specials are intentions subject to the board.

## The rule tests as they stand
- Minimum expected gain (cash rate plus 5% a year, 3.38% over 173 days): the deep dive's +3.6% clears by 0.2 points and fails at 3.3% costs; my +1.4% fails.
- Value pick (24 months, bad case no more than 10% below, middling at least 15% above): read literally, a special situation's bad outcome is its "nothing happens" value, and the deep dive's two-year "nothing happens" of +21% would pass. I agree with the deep dive that this would be the wrong reading here. The honest two-year floor is a credit loss (the deep dive's -15%, and a group 8 default with the A$60m Burleigh construction facility drawn would be worse), which fails the 10% test. The two-year "nothing happens" also assumes eight quarters of 3.4c funded from a book that pays little cash interest until loans repay, and the business isn't "clearly cheap on its own figures" at 0.715 times when its closest peer is at 0.70. The middling of +38% passes the new 15% bar, but the bad case decides it. Not a value pick.

## The three points most likely to make the pick wrong
1. Credit. Three borrower groups hold 87% of limits, group 8 alone 49% (51% of post-special equity with the A$60m Burleigh construction facility), 90% of limits are at 80% LVR or more or have no LVR at all, all FY26 interest was capitalised, and LVRs rose between July and October, going into an RBA hiking cycle with falling house prices and credit funds facing redemptions. Richlands (A$44.7m) completes in December 58% unsold.
2. No re-rating within the window. The last time Garda had sale cash and a deep discount it lent the money and the discount widened. The repayment wave that would prove the book (78% of the 12-month schedule) falls in January to June 2027 and is reported in about August 2027, after the resolve date, so the 1H27 result is unlikely to carry the stock to 0.80 times.
3. The specials and the register. The release's quarterly split contradicts its own property table; the March special rests mostly on Morningside, still under due diligence and tied to construction finishing; and once the specials go ex, the buyers who came for them may leave, taking the multiple back toward the pre-sale 0.64 times.

## What I couldn't verify
- Whether Morningside's due diligence is complete: nothing has been announced.
- How the board will split the specials between the December and March quarters, given the release and the property table disagree.
- Who the borrowers are, whether group 7 (a "repeat borrower" in industrial strata) is linked to group 8, and whether Eagle Farm is the FY26 deck's case study 3 (likely from its description, not stated).
- Loan repayments since 30 June: only the pro forma movement in the loan balance (A$134.1m to A$140.1m by 30 September) is public.
- Whether the LVR basis ("as is" or "as if complete") changed for any loan between the July and October tables.
- Who owns HGT Investments (ASIC extracts are paid).
- Prices after 6 November, and any broker research.

## Sources
GDF (ASX announcement IDs, all opened as PDFs through the ASX announcement pages): sale of property portfolio 21 Oct 2026 (03155569), footnotes 3 and 4 read from the rendered page; capital gains and special distribution 21 Oct 2026 (03155570); divestment presentation 21 Oct 2026 (03155572), pp 3 to 8 and 13 to 15; Annual Financial Report FY26 (03120048): FFO and payout tables pp 15 to 16, buyback p18, cash flow reconciliation, notes 3e, 3f, 11, 17b, 18, 19, remuneration report section 11, chairman's text p5; Annual Results Presentation FY26 (03120056), loan book p15 and case studies pp 16 to 18; Appendix 2A 29 Oct 2026 (03159355); change of auditor 5 Nov 2026 (03162376); buyback extension and Appendix 3C 2 Apr 2026 (03078964, 03078943); Pinkenba and Heathwood updates (03144524, 03152147, 03154116); distribution notices (03042290, 03073796, 03106877, 03142919); notice of AGM 27 Oct 2026 (03157893); 1H26 operational update 19 Nov 2025 (03028731); 2025 AGM chairman's address and results (03033055, 03033135); director notices: M Hallett 18 Aug 2025 (02981551) and final notice 28 Nov 2025 (03033773), M Madsen 2 Sep 2025 (02989891) and 3 Dec 2025 (03036404), P Leitch 5 Dec 2025 (03037667), A Thornton 6 Feb 2026 (03057720); HGT Investments Form 604 11 Dec 2024 (02894587). GDF announcement lists for 2025 and 2026: https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=GDF&timeframe=Y&year=2026

Peers: TCF NAV 30 Sep 2026 (03150169), September quarter update 22 Oct 2026 (03155899), CEO resignation 5 Nov 2026 (03162443); MRE NTA 30 Sep 2026 (03152366) and distribution 26 Oct 2026 (03157269); MOT NTA 30 Sep 2026 (03152358), NTA reporting notice 5 Oct 2026 (03148241) and distribution 26 Oct 2026 (03157268); MXT NTA 30 Sep 2026 (03152356); QRI NTA 31 Oct 2026 (03162089).

Repo data: data/research_data/asx_company.json (GDF header and key statistics, fetched 7 Nov 2026 UTC); data/norgate/universe/prices_2026.csv.gz (GDF and peer prices to 30 Oct 2026); src/decide.py (the minimum gain); src/risk.py (sizing).

## Verdict
Wait for a named event. Don't place a card at A$1.12.

Reasons: on my chances the expected gain after costs is about +1.4% against the 3.38% minimum (-1.0% to +2.4% across the sets I tried); even on the analyst's chances it clears only at the low end of the cost range; and neither of us can state why the market is wrong, which section 5a requires. The book is concentrated, highly leveraged and getting more so, and the evidence that would prove it (cash repayments) arrives after the resolve date.

The events that would reopen it for review:
1. The AGM on 26 November 2026: a commitment to buy back at least 5% of the securities (about 11m) or to return more than the 10c of specials. On my chances that brings the expected gain to about +3.4% at A$1.12, on the line, so it reopens only at A$1.11 or below. It closes if the board signals using the 10% placement capacity or funding the A$60m Burleigh construction facility without a co-lender.
2. The 1H27 result (about 4 February 2027), with the deep dive's conditions kept except (c), which should read: repayments in the half at or above the June schedule (about A$33m including interest and fees), and Richlands repaid or at least 60% sold by the result; and add to (b) no term extensions with capitalised interest at groups 8, 4 or 3. Recompute the chances then.
3. A price at or below A$1.08 before the December quarter goes ex (about 29 or 30 December 2026), or about A$0.99 after it, as a prompt to review, not a card, and only if nothing in the meantime explains the fall. Adjust the post ex-date figure if the December special is about 6.0c rather than 7.3c.

If it reopens and passes, the card I would put up: outcomes by 30 April 2027 of A$0.93 (17%), A$1.165 (58%), A$1.305 (20%) and A$1.474 (5%), adjusted for whatever the reopening event changes; resolve date 30 April 2027; exit rule: sell on a receivership, default or term extension with capitalised interest at any of groups 8, 4 or 3; reported NTA below A$1.40 on the company's count; a cut to the 3.4c quarterly distribution; the board committing to the A$60m Burleigh construction facility without a co-lender; or at the resolve date.
