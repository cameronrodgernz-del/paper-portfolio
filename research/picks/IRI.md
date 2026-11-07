# Integrated Research (ASX:IRI): deep dive. Not a value pick: the bad case (A$0.21) is 21% below the price and the middling case (A$0.30, A$0.335 with dividends) is 12% above it (25% with dividends)

Written 2026-11-08 by the research desk. Price at writing: A$0.2675 (last trade on Friday 6 November 2026, bid A$0.26, ask A$0.27, ASX company data in data/research_data/asx_company.json, fetched 7 November 2026 UTC; Norgate's last close in the repo is A$0.26 on 30 October [D1, D2]). Market value: A$48.8m (182,388,666 shares on issue, Appendix 2A of 30 September 2026 [I32]).
Status: finished. This is a simulation and not financial advice.
Verdict: **Wait for a named event**: the first-half FY27 trading update (expected mid-November 2026, last year 14 November) and the AGM on 25 November 2026, then the first-half FY27 result (about 26 February 2027). Reopen conditions are under "What would make this wrong". Not a value pick, and not an ordinary research pick either, because nothing inside six months shows the answer (the FY27 renewals are weighted to the second half and land in July and August 2027).
Fact sheet: research/facts/IRI.md, grade A (a value pick, only just). The question it set: has the Prognosis contract book stopped shrinking? Its "our way" anchor was A$0.584 (pro forma revenue held at A$65.8m, earnings of A$8.0m at 8 times, plus A$42.7m of net cash); its "against us" anchor A$0.242 (two more years of 12% decline, then nothing but the cash).

Order of work. The brief and the fact sheet both quoted the price, so it was in view from the start. The filings section and the three valuation methods take no input from IRI's own share price (the peer method uses the peers' prices). IRI's price is used only in "Why the market is wrong", "Outcomes and chances" and the liquidity check. Arithmetic was run in `python3 -I`; the scripts are summarised where each figure is used.

> In one paragraph: the fact sheet's A$0.584 doesn't survive the first test. Its premise, pro forma revenue holding at A$65.8m, was already broken in the second half of FY26, which ran at A$31.4m (A$62.8m a year) with the second-half pro forma EBITDA at only A$2.5m. The decline did not slow: in constant currency pro forma revenue fell about 7% in the first half and about 11% in the second, the contracted cash book (receivables plus unbilled multi-year commitments) fell 20% in the year, and second-half new-client licence revenue was A$0.9m. The A$0.58 figure is what an owner who ran the customer book for cash would get (method 3: A$0.44 to A$0.55), which only a bid or a change of course by the board would deliver, so it is the good case. The floor isn't simply net cash either: the board's capital plan earmarks all "available capital" for product, an acquisitions reserve (20% to 35%) and a contingency reserve, and if the decline runs at 12% with costs held, the business is losing cash by FY28 and the market would price it below its cash. My bad case is A$0.21 (21% below), middling A$0.30 plus about 3.5c of dividends, good A$0.42. Expected value about A$0.31 including dividends, about 7% above today after round-trip costs of about 9%, over two years. Wait for the trading update and AGM; reopen at A$0.23 or below if the cash path holds, or on a capital return, an approach, or a first half that shows the decline slowing.

## The company in plain words
Integrated Research sells Prognosis, software that watches the health of large organisations' critical systems: card and high-value payment switches (Transact), HPE NonStop and other infrastructure (Infrastructure), and phone, video and contact-centre systems from Cisco, Avaya, Microsoft and others (Collaborate) [I1, I36]. Customers are big banks, telcos, government agencies and Fortune 500 companies; the Americas were A$41.3m of A$57.6m of FY26 revenue [I1, note 2]. It sells mostly one-to-five-year term licences: the licence fee is booked as revenue when the contract is signed, maintenance is booked over the term, and creditworthy customers may pay the licence by instalments over the term [I1, notes 1 and 11]. So statutory revenue swings with the renewal cycle, and the company publishes "pro forma" revenue that spreads licence fees over the contract [I3, slide 26]. FY26: statutory revenue A$57.6m, pro forma A$65.8m, statutory profit A$1.2m, operating cash flow A$12.6m, cash A$51.7m and no debt; 138 staff [I1, I2].

Who runs it. Ian Lowe has been CEO since October 2024 and holds no shares (984,621 performance rights) [I1, directors' interests]. Chair Peter Lloyd (director since 2010, 51,263 shares); Mark Brayan (a former IRI CEO, 260,000 shares); Michael Hitz (300,000 shares, all bought on market in November and December 2025), who is also a director of the Institute for Economics and Peace [I1], the think tank founded by IRI's founder Steve Killelea [S1; I1, note 27]; Kate Greenhill (audit chair, 90,000 shares), who leaves by 28 February 2027 [I6]. Outside Killelea the board owns about 0.4% of the company.

Who owns it. Killelea holds 51,880,619 shares directly (28.45%), 52,218,231 with a related entity (28.63%) [I4, p. 79]. Then Citicorp Nominees 6.56%, Santos L Helper (the van Paassen family, Brisbane) 6.21%, B & R James Investments 4.39%, BNP Paribas Nominees (Interactive Brokers retail) 3.03%, Andrew Rutherford 1.46%; the top 20 hold 58.0%; 4,075 holders; 4,983,574 performance rights on issue [I4, pp. 78 to 79]. Substantial holders: Killelea and van Paassen only [I4].

Five years (A$m) [I3, slide 27; I13, appendix; I22; I1]:

| | FY22 | FY23 | FY24 | FY25 | FY26 |
| --- | --- | --- | --- | --- | --- |
| Pro forma revenue | 79.8 | 75.6 | 74.8 | 74.3 | 65.8 |
| Statutory revenue | 62.9 | 69.8 | 83.3 | 68.3 | 57.6 |
| Statutory profit after tax | n/a | (29.2) incl. A$31.8m impairment | 27.1 | 13.4 | 1.2 |
| Cash receipts from customers | n/a | 76.3 | 72.4 | 66.7 | 64.7 |
| Total contract value signed (TCV) | ~47 ex services (chart) | 68.5 | 83.9 | 67.3 | 54.3 |

The share price follows the statutory renewal cycle: from A$0.31 in January 2024 to A$0.93 in June 2024 as the big FY24 renewal year came through, then back to A$0.26 [D1].

## Why big investors may be overlooking it
- Size and trading: A$48.8m market value. Median value traded over the 20 sessions 5 to 30 October 2026 was A$12,362 a day (lowest day A$11) [D1]. Volume has dried up: 1.16m shares traded in October 2026 against 10.3m in November 2025 [D1]. I didn't check index lists; at this size it is far below the S&P/ASX 300.
- Register: the founder holds 28.6% and the top 20 hold 58%, so the free float is small.
- Coverage: I didn't check broker databases, so "little coverage" isn't claimed.
- Mood: small enterprise software exposed to AI disruption is out of favour, and management itself says AI is making customers cautious and shortening contracts [I2].
- History: a A$31.8m impairment in FY23, a CEO change in 2024, and a statutory profit that swings from A$27.1m to A$1.2m in two years with the renewal cycle [I22, I1].

So it has the signs of an overlooked share, but the business is also shrinking, which is the more obvious reason for the price.

## What the filings show

### 1. The contract book, rebuilt
IRI stopped publishing annual recurring revenue after December 2024 (A$67.5m at June 2023, A$66.6m at June 2024, A$65.2m at December 2024) [I23, slide 27; I19, slide 25]. What it still publishes lets the book be rebuilt three ways.

**Total contract value signed (A$m)** [I3, slide 23; I10, slide 21; I16, slide 24; I19, slide 8; I23, slide 7]:

| | 1H FY24 | 2H FY24 | 1H FY25 | 2H FY25 | 1H FY26 | 2H FY26 |
| --- | --- | --- | --- | --- | --- | --- |
| Total | 41.4 | 42.5 | 26.5 | 40.8 | 26.8 | 27.5 |
| Renewals | n/a | n/a | 15.9 | 32.7 | 15.1 | 23.4 |
| New business (new clients, upsell) | n/a | n/a | 7.6 | 6.2 | 8.3 | 2.6 |
| Services | n/a | n/a | 3.0 | 1.9 | 3.4 | 1.5 |
| Full year (renewal / new / services) | | 83.9 (61.0 / 15.3 / 7.6) | | 67.3 (48.6 / 13.8 / 4.9) | | 54.3 (38.5 / 10.9 / 4.9) |

Second halves are full year less first half; 1H FY24 is backed out of the 36% fall to A$26.5m in 1H FY25 [I19, slide 8]. Average contract term: 4 years in 1H FY24, 3.1 in FY24, 3.4 in FY25, 3.0 in 1H FY26 and 3.2 in FY26 [I25; I16, slide 24; I10, slide 21; I1]. Shorter terms cut TCV even when the yearly price holds, which is why TCV overstates the fall in the business [I25].

New business collapsed in the second half of FY26: A$2.6m of TCV against A$6.2m a year earlier. New-client licence revenue was A$4.6m in the first half and A$5.5m for the year, so A$0.9m in the second; expansion licence revenue A$1.6m then A$1.3m [I9; I3, slide 17]. Management says several deals were deferred into 1H FY27 [I7].

**The contracted cash book** (A$m, 30 June): net trade receivables (licence instalments and billed fees still to collect) plus the remaining performance obligations the accounts leave off the balance sheet (multi-year non-cancellable commitments not yet billed, due in two to five years) [I1, notes 3 and 11; I15, note 3; I22, note 3]:

| 30 June | Receivables (due within a year / later) | Unbilled commitments | Contracted cash to come | Change |
| --- | --- | --- | --- | --- |
| 2023 | 63.5 (40.9 / 22.5) | 21.4 | 84.8 | |
| 2024 | 73.5 (41.6 / 31.9) | 19.1 | 92.6 | +9% |
| 2025 | 73.7 (40.8 / 33.0) | 20.5 | 94.2 | +2% |
| 2026 | 58.2 (35.9 / 22.3) | 17.0 | 75.2 | -20% |

It roughly reconciles: opening book plus TCV less cash received gives A$83.9m for FY26 against A$75.2m actual; the A$8.7m gap is the A$4.9m credit loss allowance plus currency (the Australian dollar rose from US$0.655 to US$0.687 between the two balance dates, shrinking the US-dollar receivables) [I1; D3]. The book shrank by a fifth because signings (A$54.3m) ran A$10m below cash collected (A$64.7m).

**Recurring cash, not reported revenue** (A$m) [I1, I8, I15, I18, I22, I26]:

| | FY23 | FY24 | FY25 | FY26 | 1H FY25 | 2H FY25 | 1H FY26 | 2H FY26 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cash receipts from customers | 76.3 | 72.4 | 66.7 | 64.7 | 28.3 | 38.4 | 31.3 | 33.4 |
| Cash paid to suppliers and staff | 60.7 | 58.4 | 53.6 | 52.1 | 27.0 | 26.6 | 25.6 | 26.5 |
| Difference | 15.5 | 14.0 | 13.1 | 12.6 | 1.2 | 11.9 | 5.6 | 6.9 |

Receipts have run at 92% to 101% of pro forma revenue, and nearer 100% once the financing part of the licence instalments is added back: IRI books that part as "interest received" in investing cash flows (FY26 interest received A$3.6m, of which I estimate about A$1.7m was interest on cash and about A$1.9m customer instalment interest; the split isn't disclosed) [I1, notes 1(O) and 6]. So pro forma revenue is a fair guide to cash, and cash has been held up by cost cuts (staff 175 in FY23, 142, 131, 138 now) rather than by revenue [I22, I15, I1].

**Has the decline slowed? No.** Pro forma revenue by half (A$m), and at a constant AUD/USD of 0.70, using the Americas' 68% share of FY26 pro forma revenue and half-year average rates (my estimate) [I10, slide 25; I3, slides 10 and 27; D3]:

| | 1H FY25 | 2H FY25 | 1H FY26 | 2H FY26 |
| --- | --- | --- | --- | --- |
| Pro forma revenue | 36.6 | 37.7 | 34.4 | 31.4 |
| AUD/USD average | 0.662 | 0.634 | 0.655 | 0.703 |
| At US$0.70 | 35.2 | 35.3 | 32.9 | 31.5 |
| Change on a year earlier, A$ / constant currency | | | -6.0% / -6.6% | -16.7% / -10.7% |

For FY26 as a whole the company's 12% fall is about 8.6% in constant currency; the stronger Australian dollar took the rest. The second half was the weakest half on record and fell 4.3% on the first half in constant currency (about 8.5% a year). The exit rate is A$31.4m a half, A$62.8m a year, at today's exchange rate. The 1H FY26 pro forma EBITDA was A$6.2m and the full year A$8.7m, so the second half was A$2.5m, after about A$1.5m of net currency and other losses [I10, slide 24; I3, slide 26].

**Churn by product line.** Collaborate kept 86% of its revenue from existing customers in constant currency in FY24 and 83% in FY25 and FY26 [I21; I15; I1]. In the last disclosed recurring revenue bridges, Collaborate lost 19% of opening recurring revenue to churn and down-sell in FY24 and 12.2% in the half to December 2024, while Transact and Infrastructure lost 5% and 3.2% and grew through upsell [I23, slide 27; I19, slide 25]. In FY26 the damage spread: pro forma revenue fell 11% in Collaborate ("churn and down sell"), 14% in Transact and 11% in Infrastructure ("mainly due to down sell") [I3, slide 10]. By half, pro forma subscription revenue (A$m) [I10, slide 25; I3, slide 27]:

| | 1H FY24 | 2H FY24 | 1H FY25 | 2H FY25 | 1H FY26 | 2H FY26 |
| --- | --- | --- | --- | --- | --- | --- |
| Collaborate | 17.3 | 17.6 | 15.7 | 15.6 | 14.9 | 13.6 |
| Transact | 6.2 | 6.5 | 6.8 | 9.5 | 7.3 | 6.8 |
| Infrastructure | 9.3 | 9.9 | 9.9 | 10.0 | 9.2 | 8.5 |

The chair's own account: Microsoft's bundled tools are displacing Avaya and Cisco in Collaborate, and the HPE NonStop market behind Transact and Infrastructure "is approaching saturation" [I12]. New AI products (Iris, Prognosis Elevate, the IR Labs testing product) and the high-value payments product have first clients but no material revenue; subscription fees fell 54% to A$1.8m in FY26 [I3, slides 6 and 17].

### 2. The renewal schedule
IRI doesn't publish one. What it has said: FY25's book was "softer" than FY24's and weighted to the second half; FY26's was "softer"; for FY27 it says only that the book "is weighted to the second half", without the word softer [I23, slide 24; I16; I2; I3, slide 20]. At the 2024 AGM the chair gave the size direction a year ahead ("less TCV due for renewal in FY25 versus FY24") [I21], so the 25 November AGM may do the same for FY27 and FY28.

A rough rebuild from past signings: product TCV by year (FY18 to FY22 read off the bar chart in the 23 December 2024 trading update, accurate to about A$2m; FY23 to FY26 from the results), split by contract life using the disclosed FY23 mix (30% one or two years, 28% three or four, 42% five) and FY24 mix (16%, 41%, 43%) [I20; I23, slide 7]. Original TCV falling due (A$m), and how much was renewed:

| Year | Falling due (estimate) | Renewal TCV signed | Renewed as % of due |
| --- | --- | --- | --- |
| FY24 | 68.5 | 61.0 | 89% |
| FY25 | 66.7 | 48.6 | 73% |
| FY26 | 52.4 | 38.5 | 74% |
| FY27 | 53.0 (FY22 five-year 19.7, FY23 four-year 8.6, FY24 three-year 15.6, FY25 and FY26 short deals 9.0) | | |
| FY28 | 58.3 plus any one-year FY27 deals (FY23 five-year 25.9, FY24 four-year 15.6, FY25 three-year 12.8, FY26 two-year 4.0) | | |

What it says: FY27's book is about the size of FY26's, consistent with management dropping "softer", and FY28's is bigger, driven by FY23's five-year deals and FY24's four-year deals. If FY27 renews at FY25 to FY26's 74%, renewal TCV is about A$39m, like FY26; FY28 at 74% about A$45m or more. So statutory revenue probably bottoms in FY27 and rises in FY28 (reported in August 2028). That matters for the share price, which has chased statutory results before, but not for value: pro forma revenue and cash depend on how much of each contract's yearly value is kept, and the fall from 89% to 74% says less is being kept (churn, down-sell and shorter terms together). These estimates rest on chart readings and assumed term splits; treat them as direction, not numbers.

### 3. Costs: what they could be cut to
FY26 costs before credit losses and depreciation were A$53.1m: product and technology A$17.4m (up 29%; none capitalised), sales, professional services and marketing A$30.8m, administration about A$5.6m before the A$5.0m credit loss charge; staff costs A$38.7m [I1, note 4; I3, slides 12 and 25]. In FY24 the same product line cost A$12.8m and sales A$38.7m [I22]. Management's plan is to keep spending: "Investment in product-led growth will impact profit performance over the short to medium term" [I2].

An owner running the book for cash would cut product to keeping Prognosis current (about A$9m to A$10m), sales to account management and renewals (about A$18m to A$20m), and overheads to about A$5m: a cost base of roughly A$32m to A$37m, against A$52m of cash costs now. That would cost about A$5m in redundancies (employee leave provisions are A$3.0m now) [I1, note 20], and revenue would fall faster, perhaps 15% to 20% a year, because Collaborate is in structural decline. This is the harvest case in the valuation; nothing the board has said points to it.

### 4. Cash at 30 September 2026
Not disclosed: IRI files no quarterly cash report, the annual report (14 October) and AGM notice (23 October) give no later figure, and the first-half trading update hasn't been released [I4; I5; ASX announcements list]. From the filings: A$51.7m at 30 June [I1]. First halves are seasonally weak for cash (receipts less payments A$1.2m in 1H FY25 and A$5.6m in 1H FY26), and receivables due within a year are lower than a year ago (A$35.9m against A$40.8m) [I18; I8; I1]. My estimate is A$52m to A$54m at 30 September, then A$9.03m of dividends paid on 15 October (3c ordinary and 2c special on 180.6m shares) [I1, note 22], and about A$46m (range A$44m to A$47m) at 31 December 2026, about A$0.25 a share. Lease liabilities are A$1.5m; there are no borrowings, earn-outs or restructuring provisions [I1, notes 20 and 21].

### 5. The capital plan and the acquisitions reserve
The FY27 capital allocation framework puts 30% to 35% of "available capital" into product innovation, 20% to 35% into "flexibility reserves... to fund opportunistic deals e.g. M&A if right-sized, synergistic, in growth markets and supportive of product strategy", and 30% to 35% into contingency reserves for working capital; the dividend policy is at least 25% of free cash flow, at the board's discretion [I3, slide 14; the FY26 version is the same, I13]. "Available capital" isn't defined, but read plainly the three buckets take all of it: on A$46m, A$14m to A$16m for product, A$9m to A$16m for deals, and A$14m to A$16m kept back. Nothing in the plan is set aside for holders beyond the dividend. The chair's letter does say the balance sheet gives "capacity to... return capital to shareholders", and the 2c special (A$3.6m) was the first sign of it [I4, p. 6]. There is no buy-back [I4, p. 80].

The board hasn't named any target. Its record: the only acquisition announced since 2012 is IQ Services (contact-centre testing, May 2015), for US$1.5m plus earn-outs of up to US$3.5m over three years [I34; ASX announcement lists 2012 to 2026]. Goodwill of A$3.7m was written off with A$24.9m of intangibles in the FY23 impairment [I22, note 17], and in December 2024 IRI sold its "non-core testing solution business" for A$0.76m, a A$1.2m gain because it took A$0.4m of net liabilities with it [I18, note 8; I15, note 5]. The filings don't name the testing business sold as IQ Services, but it is the business that acquisition brought in. I found no acquisitions called Inform or Ideal in IRI's announcements. The record is small, and not good.

The CEO's long-term incentive is tied to growth in underlying earnings per share (10% a year from a 3.96c base to FY29) and the FY27 grant of 1,149,601 rights is priced off a A$0.3262 average [I5]. Nothing in it rewards returning cash, though a buy-back would lift earnings per share.

### 6. Holders and dealings, last 12 months
- Killelea's 52,218,231 shares are unchanged since at least September 2025; his percentage has slipped from 29.25% to 28.92% at 30 June 2026 only through staff share issues [I17; I1, note 27].
- Building: van Paassen's Santos L Helper became substantial on 7 January 2026 at 5.04% (9,106,551), having bought about 1.0m shares on 14 to 18 November 2025 at A$0.27 to A$0.30, then bought 1,875,555 more on market to 23 June 2026 for A$572,746 (about A$0.305) to reach 6.08% [I27; I28]; 11,317,272 (6.21%) on the register at 30 September [I4]. B & R James went from 3.88% to 4.39%, Citicorp Nominees from 5.50% to 6.56%, and Interactive Brokers' retail nominee from 1.75% to 3.03% [I17; I4].
- Leaving: the Debenham family held 2.46% and 0.54% (about 5.4m shares) in September 2025 and is no longer in the top 20 (the cut-off is 0.38%), so it sold at least about 4m shares; J P Morgan Nominees fell from 1.29% to 0.38% [I17; I4].
- Directors, on market: Greenhill bought 90,000 shares on 25 to 27 November 2025 for A$28,088 (about A$0.31); Hitz bought 150,500 on 25 November to 1 December 2025 for A$47,251 (about A$0.31) and 149,500 on 5 December 2025 for A$51,949 (about A$0.35) [I29; I30; I31]. No director has bought or sold since, although the price has fallen to A$0.26. Ian Lowe's January 2026 notice was a grant of rights, not a purchase.
- No approach, review or sale process has been announced. The 2025 AGM passed everything with 97% to 99% of votes [I14]. The 2026 AGM adds a new constitution (including the usual proportional takeover approval clause) [I5]. Greenhill, the audit chair, leaves by 28 February 2027 [I6].

## Valuation
Done from the filings; the only prices used are the peers'.

**Method 1: net cash plus a peer multiple.** Small listed software companies that are shrinking or run for cash, on the measures the market uses for them (enterprise value against revenue and against cash earnings):

| Company | Business and trend | Enterprise value | Multiple |
| --- | --- | --- | --- |
| Reckon (ASX:RKN) | Accounting and legal software, revenue flat in constant currency (1H 2026 A$32m), run for cash with a dividend | About A$47m (A$45.3m market value at A$0.395 plus A$1.5m net debt) | 5.4x FY25 operating cash after development (A$8.7m); 4.2x on 1H 2026 doubled (A$11.2m) [P1, P2, D2] |
| AI-Media (ASX:AIM) | Captioning; revenue down 7% to A$60.2m as legacy services shrink, recurring software revenue growing | About A$25m (A$41.0m at A$0.195 less A$15.9m cash) | 0.42x revenue; about 10x FY26 operating cash flow (A$2.4m) [P3, D2] |
| Prophecy International (ASX:PRO) | Log and service monitoring software (Snare, eMite); revenue down 15% to A$18.4m, operating cash outflow A$3.7m, A$9.5m of cost cuts | About A$5.4m (80.55m shares at A$0.067 on 23 October, A$1.0m cash, A$1.0m debt and leases) | 0.29x revenue [P4, D1] |

Applied to IRI's FY27 on my middling path (pro forma revenue about A$59m; recurring cash earnings, meaning customer cash less cash costs, leases and capital spending, about A$4.5m): 0.29x to 0.43x revenue gives A$17m to A$25m; 4x to 5x cash earnings gives A$18m to A$23m. Add A$46m of net cash: A$63m to A$71m on about 185m shares (allowing for rights vesting), **A$0.34 to A$0.38**. It depends on IRI earning peer multiples, which is generous: Reckon isn't shrinking, Prophecy has already cut costs and AI-Media's recurring revenue is growing, while IRI's cash earnings are falling.

**Method 2: the cash the business throws off as it is run now, to June 2028.** Half-yearly from the A$31.5m second-half run rate (at US$0.70); customer cash at 98% of pro forma revenue; interest on cash at 4.0% (RBA cash rate 4.60% in October 2026 [D4]); leases and capital spending A$1.0m a year; dividends as stated; about 3m more shares from rights. In A$m:

| | Bad: 12% a year decline, costs held at A$53m | Middling: 6% to 8% decline, costs trimmed to A$51.8m by FY28 | Good: 3% decline, costs held |
| --- | --- | --- | --- |
| Pro forma revenue FY27 / FY28 | 57.3 / 50.4 | 59.2 to 59.9 / 54.5 to 55.8 | 61.6 / 59.7 |
| Free cash flow FY27 / FY28 | 4.1 / -2.8 | 5.9 to 6.6 / 2.0 to 4.0 | 7.3 / 5.6 |
| Dividends, Oct 2027 / Oct 2028 | 0.55c / nil (25% of free cash flow) | 2.0c / 1.5c | 3.0c / 3.0c |
| Net cash at 30 June 2028 | 43.0 (A$0.232 a share) | 46.9 to 49.9 (A$0.253 to A$0.269) | 50.1 (A$0.270) |
| FY28 operating cash after leases | -4.6 | 0.6 to 2.6 | 4.5 |
| What the market would pay for the business | Less than nothing: FY29 would burn A$8.8m if costs aren't cut; take half of that | About 3x a small, falling cash earning | 4x to 5x, Reckon's range |
| Price | (43.0 - 4.4) / 185.4 = **A$0.21** | 0.26 + 0.03 = **A$0.29 to A$0.31** | 0.27 + 0.10 to 0.12 = **A$0.37 to A$0.39** |

The single input that moves this most is the rate of decline: each point a year is worth about 0.5c a share by mid-2028 in cash alone, more once the market's multiple responds. The second is whether the board cuts costs when revenue falls; if it trims to A$47m by FY28 in the bad case, the bad price is about A$0.235 rather than A$0.21. The third is the acquisitions reserve: A$10m spent on a deal the market values at half is 2.7c a share.

**Method 3: the customer book run for cash by a buyer.** FY27 as a transition year (current cash earnings of about A$4m less A$5m of redundancies), then revenue falling 12% to 20% a year from A$58m, a 35% to 45% EBITDA margin (costs of about A$30m on FY28 revenue of A$49m), 25% tax, 12% discount rate, ten years. The book is worth A$34m to A$61m, central A$47.5m (15% decline, 40% margin). Add A$46m of cash: A$81m to A$101m, **A$0.44 to A$0.55** a share. Legacy software buyers pay for this kind of book, but only a bid, or a board decision to stop new-product spending and return the cash, would realise it; a bidder would also want its own margin, so a bid would more likely be A$0.40 to A$0.45.

Cross-check: net tangible assets were 54.3c at 30 June, about 48.8c after the October dividend [I1, I3]. That counts the receivables at face value and leaves out the cost of servicing them, so it sits close to method 3, not method 2.

**Range.** A$0.21 (the business run as now through a fast decline) to A$0.55 (the book harvested by a buyer). As run now, with the decline at about FY26's constant-currency rate, the business is worth about A$0.29 to A$0.31 including nothing for the dividends paid along the way, and about A$0.34 to A$0.38 if the market paid peer multiples. Each depends mainly on the rate of decline, on the board keeping the cash, and on how many of the FY27 and FY28 renewals are kept.

## Why the market is wrong
At A$0.2675 the market pays A$48.8m, about A$3m above my A$46m year-end cash estimate (A$6m above the A$42.7m June cash less the dividend). That is about 0.05x to 0.09x pro forma revenue and 0.3x to 0.5x last year's recurring cash earnings, far below the peers' 0.29x to 0.43x revenue and 4x to 5x cash earnings. On that comparison IRI is the cheapest of the group by a distance.

But I can't say why the gap should close inside two years without a bid or a change of course. The market has three good reasons for the price: the business is shrinking by about 9% to 11% a year in constant currency and the second half of FY26 was the weakest half on record; cash earnings fall from A$12.6m to roughly A$4m to A$6m in FY27 on today's costs and close to nothing by FY28 in the middling case; and the board has earmarked the cash for product, acquisitions and reserves rather than holders. The likeliest way the price rises is that the market again chases a statutory renewal year (FY28 looks bigger), or that Killelea or the board decides to realise the book's value. Neither is something I can date or put better than one in five.

## Outcomes and chances
| Outcome | What happens | Chance | Price by resolve date |
| --- | --- | --- | --- |
| Bad | The decline runs at about 12% a year in constant currency (the second half of FY26 ran at 11%); the FY27 and FY28 renewals keep 74% or less; costs stay near A$53m as product spending continues; FY28 is cash-negative; or an acquisition from the reserve or another large credit loss. Dividends about 0.5c | 40% | A$0.21 |
| Middling | The decline settles at 6% to 8%; costs trimmed slightly; cash builds to about A$48m by June 2028; dividends of about 2c (October 2027) and 1.5c (October 2028); the market pays net cash plus about 3x a small cash earning | 40% | A$0.30 |
| Good | Either the FY27 and FY28 renewal books renew well (89%, as in FY24), deferred new business closes and new products add revenue, so the decline stops and the market pays 4x to 5x cash earnings with 6c of dividends paid; or a bid or a harvest-and-return at A$0.40 to A$0.45 | 20% | A$0.42 |

Resolve-by date if this were carded: 30 September 2028, after the FY28 result. Chances add to 100%. Each price comes from the valuation: bad from method 2's bad column (A$0.208, rounded); middling from method 2's middling column (A$0.29 to A$0.31, central A$0.30), below method 1's A$0.34 because cash earnings near A$2m by FY28 won't earn peer multiples; good from method 2's good column (A$0.37 to A$0.39 plus 6c of dividends) and the bid end of method 3 (A$0.40 to A$0.45), central A$0.42.

Against A$0.2675: bad -21.5% (-19.6% with its dividends), middling +12.1% (+25.2% with its 3.5c of dividends), good +57% (+68% with dividends). The value pick rule needs the bad case within 10% of the price; it isn't, under any treatment I tried (even pricing the bad outcome at full net cash gives A$0.238, 11% below). The middling case clears 25% only with dividends counted, and only just.

Expected value, dividends included: 0.40 x 0.215 + 0.40 x 0.335 + 0.20 x 0.45 = A$0.310, 15.9% above A$0.2675 before costs.

Round-trip costs, for the most the pick could be (2.5% of NZ$100,000 is about A$2,016 at AUD/NZD 1.2401, below the A$2,472 liquidity cap) [D3]: brokerage A$15 each way (0.74%), half the one-tick spread each way (A$0.26 bid to A$0.27 ask: 1.89%), size cost each way (daily volatility of 3.2% outside the ex-dividend day, times the square root of A$2,016 over the A$12,604 average day: 1.29%), and 0.5% for each currency conversion. That is about 8.8% round trip. Expected return after costs: about 7% over 23 months, 3.6% a year, below the 4.60% cash rate. No trade.

## Dated events
- Mid-November 2026 (14 November last year; in FY25 the update came on 23 December and 16 January): first-half FY27 trading update with ranges for TCV, statutory revenue and EBITDA [I11; I20].
- 18 November 2026: last day for written questions before the AGM [I5].
- 25 November 2026: AGM, with the chair's and CEO's addresses. Last year's included the FY26 outlook; in 2024 the chair gave the next year's renewal book direction [I12; I21; I5].
- About 26 February 2027: first-half FY27 result, with pro forma revenue by product, TCV, cash at 31 December and any interim dividend.
- By 28 February 2027: Kate Greenhill leaves the board [I6].
- About July 2027: FY27 trading update, the first read on the second-half-weighted FY27 renewals; late August 2027: FY27 result; October 2027: dividend.
- November 2027 AGM; February 2028 first half; late August 2028 FY28 result (the bigger renewal year on my rebuild).

## What would make this wrong
The two things most likely to make "wait" the wrong call:
1. The renewals hold. If the FY27 book (about the size of FY26's) and the larger FY28 book renew at FY24's 89% rather than FY25 to FY26's 74%, and the new business deferred into 1H FY27 closes, the decline could stop and the cash earnings would recover towards A$10m. The market has rerated IRI fast before: A$0.31 to A$0.93 between January and June 2024 on a big statutory renewal year [D1].
2. A control move. With the business valued at almost nothing beyond its cash, a buyer of legacy software could pay A$0.40 or more and still earn a high return on the book (method 3). Killelea's 28.6% decides whether that happens; he hasn't sold a share in the last year.

Reopen conditions (any one):
- **Price.** The price is at or below A$0.23 after the trading update and AGM (the bad case's A$0.21 is then within 10% and the middling A$0.30 is 30% above), provided the update doesn't cut the cash path: first-half FY27 EBITDA no worse than a A$3m loss before currency and credit losses, and net cash of at least A$44m at 31 December 2026 when reported.
- **Capital.** A buy-back or special distribution of at least A$10m (about 5.5c a share), or a change to the capital allocation framework that returns the flexibility reserve to holders. Cash paid out can't be spent on a deal, which lifts the bad case.
- **Control.** An approach, a strategic review, or a substantial holder notice from Killelea: then a special situation deep dive under section 5a.
- **Trading.** The first-half FY27 result shows pro forma revenue of at least A$31m for the half (a constant-currency fall of about 6% or less on 1H FY26's A$32.9m at US$0.70), new business TCV of at least A$8m, and the board confirms the FY27 renewal book is at least FY26's size. Then the middling case moves to about A$0.34 and the bad case to about A$0.24.

## Corrections to the fact sheet
- "If it goes our way" assumes pro forma revenue holds at A$65.8m. The second half of FY26 already ran at A$31.4m (A$62.8m a year), and second-half pro forma EBITDA was A$2.5m, not the A$12.1m a year the fact sheet's anchor builds to [I3; I10]. The A$0.584 is method 3's harvest value, a good-case figure.
- "If it goes against us" (A$0.242) treats the cash as a floor the market will pay in full. Under the board's framework the cash is earmarked; a business that is cash-negative by FY28 would be priced below its cash; and about 3m to 6m more shares come from rights. My bad case is A$0.21, and the value pick test fails on that leg.
- Pro forma revenue fell 12% in A$ (11.4% on the rounded figures) but about 8.6% in constant currency; within the year the constant-currency fall sped up from 6.6% to 10.7% [I3; D3].
- The A$15.5m fall in receivables in FY26 was the A$4.9m allowance, about A$2m to A$3m of currency translation and the rest collected, not only collections [I1; D3].
- The A$1.0m of "other income" taken out of the fact sheet's anchor was a one-off US employee retention tax credit [I1, note 5]; right to exclude it.
- The A$3.6m of "interest received" includes the financing part of customers' licence instalments (about A$1.9m on my estimate), so interest on cash is about A$1.7m a year, not A$3.6m; at today's 4.60% cash rate it is about A$1.9m [I1, notes 1(O) and 6; D4].
- The binding size limit is the 2.5% pick cap (about A$2,016), not the A$2,470 liquidity cap.
- From my brief rather than the fact sheet: I found no acquisitions called Inform or Ideal. The only acquisition announced since 2012 is IQ Services (2015) [I34].

## What I couldn't verify
- Cash at 30 September 2026: not disclosed; estimated.
- A renewal schedule: IRI doesn't publish one; my rebuild uses chart readings for FY18 to FY22 and the disclosed FY23 and FY24 term splits.
- Annual recurring revenue since December 2024: no longer disclosed.
- The split of interest received between interest on cash and customer instalment interest: estimated.
- That the testing business sold in December 2024 was the IQ Services business: the filings don't name it.
- The first-half FY27 trading update: not yet released at 8 November 2026.
- Broker coverage and index membership: not checked.
- Prophecy's price is its last Norgate close on 23 October 2026.

## Checks
- Not on Cam's excluded list: config/judgement_excluded.csv has no entries. Not gaming, wagering or racing: Prognosis monitors payment switches, infrastructure and communications systems.
- No placement-pattern reopening (rulebook section 9): no capital raising in the last two years; new shares came only from staff rights (1,796,863 on 30 September 2026) [I32].
- Liquidity: median value traded A$12,362 a day over the 20 sessions 5 to 30 October 2026 (Norgate volume times close; lowest day A$11, three days under A$1,000); two sessions at 10% is A$2,472 [D1]. The 2.5% cap (about A$2,016) binds first. A sale in a bad week could take several sessions at this size.

## Sources
Integrated Research (ASX announcements):
- [I1] Appendix 4E and FY26 Financial Report, 27 Aug 2026 (03131270): https://announcements.asx.com.au/asxpdf/20260827/pdf/0739zgb4g775vs.pdf
- [I2] FY26 Full Year Results, 27 Aug 2026 (03131274): https://announcements.asx.com.au/asxpdf/20260827/pdf/0739zr7k7v3zx2.pdf
- [I3] FY26 Investor Presentation, 27 Aug 2026 (03131277): https://announcements.asx.com.au/asxpdf/20260827/pdf/0739zyvr34kfts.pdf
- [I4] 2026 Annual Report (shareholder information at 30 Sep 2026), 14 Oct 2026 (03152310): https://announcements.asx.com.au/asxpdf/20261014/pdf/0759w6763xrw5w.pdf
- [I5] Notice of Annual General Meeting, 23 Oct 2026 (03156265): https://announcements.asx.com.au/asxpdf/20261023/pdf/075pg6vqz796w0.pdf
- [I6] Non-executive Director Resignation, 5 Nov 2026 (03162488): https://announcements.asx.com.au/asxpdf/20261105/pdf/0768fw5l6pqz9g.pdf
- [I7] FY26 Results Trading Update, 24 Jul 2026 (03117885): https://announcements.asx.com.au/asxpdf/20260724/pdf/0720m2qbpqdpyf.pdf
- [I8] Appendix 4D and Interim Financial Report 1H FY26, 26 Feb 2026 (03065335): https://announcements.asx.com.au/asxpdf/20260226/pdf/06wsb41jqnsyml.pdf
- [I9] FY26 Interim Results, 26 Feb 2026 (03065337): https://announcements.asx.com.au/asxpdf/20260226/pdf/06wsb8bt4y2ws2.pdf
- [I10] 1H FY26 Investor Presentation, 26 Feb 2026 (03065339): https://announcements.asx.com.au/asxpdf/20260226/pdf/06wsbdmj9vm67w.pdf
- [I11] FY26 Half Year Results Trading Update, 14 Nov 2025 (03025690): https://announcements.asx.com.au/asxpdf/20251114/pdf/06ryfx9hrq5p6z.pdf
- [I12] 2025 AGM Chair's Address, 24 Nov 2025 (03030711): https://announcements.asx.com.au/asxpdf/20251124/pdf/06sdftjykj90dx.pdf
- [I13] 2025 AGM CEO's Presentation, 24 Nov 2025 (03030715): https://announcements.asx.com.au/asxpdf/20251124/pdf/06sdg34b6bs750.pdf
- [I14] 2025 AGM Results of Meeting, 24 Nov 2025 (03030918): https://announcements.asx.com.au/asxpdf/20251124/pdf/06sdy3hs4fh00y.pdf
- [I15] Appendix 4E and FY25 Financial Report, 26 Aug 2025 (02985416): https://announcements.asx.com.au/asxpdf/20250826/pdf/06nbnbj4vjq6gb.pdf
- [I16] FY25 Results Presentation, 26 Aug 2025 (02985421): https://announcements.asx.com.au/asxpdf/20250826/pdf/06nbnp3j7n5xyx.pdf
- [I17] 2025 Annual Report (shareholder information at 15 Sep 2025), 17 Oct 2025 (03011383): https://announcements.asx.com.au/asxpdf/20251017/pdf/06qnsg8vv7khz8.pdf
- [I18] Appendix 4D and Interim Financial Report 1H FY25, 20 Feb 2025 (02916517): https://announcements.asx.com.au/asxpdf/20250220/pdf/06fqj2fkfp99lf.pdf
- [I19] 1H FY25 Investor Presentation, 20 Feb 2025 (02916532): https://announcements.asx.com.au/asxpdf/20250220/pdf/06fqk2yv0w3dhq.pdf
- [I20] Trading Update, 23 Dec 2024 (02899309): https://announcements.asx.com.au/asxpdf/20241223/pdf/06cyyhqlfpyzfz.pdf
- [I21] 2024 AGM Address, 25 Nov 2024 (02886169): https://announcements.asx.com.au/asxpdf/20241125/pdf/06bsm5kyz1gpd1.pdf
- [I22] Appendix 4E and FY24 Financial Report, 20 Aug 2024 (02841170): https://announcements.asx.com.au/asxpdf/20240820/pdf/066sg83f85y3kg.pdf
- [I23] FY24 Results Presentation, 20 Aug 2024 (02841174): https://announcements.asx.com.au/asxpdf/20240820/pdf/066sgjbpt0zhhx.pdf
- [I24] FY24 Earnings Call Transcript, 23 Aug 2024 (02843518): https://announcements.asx.com.au/asxpdf/20240823/pdf/066zdkmy4jlyss.pdf
- [I25] FY24 Half Year Results Call Transcript, 28 Feb 2024 (02779250): https://announcements.asx.com.au/asxpdf/20240228/pdf/060yb6lh5jz2nr.pdf
- [I26] Appendix 4D and FY24 Half Year Financial Report, 22 Feb 2024 (02775964): https://announcements.asx.com.au/asxpdf/20240222/pdf/060nm12kxy1kdj.pdf
- [I27] Becoming a substantial holder, Santos L Helper Pty Ltd, 8 Jan 2026 (03048225; scanned, read by OCR): https://announcements.asx.com.au/asxpdf/20260108/pdf/06v2m016fx4wqc.pdf
- [I28] Change in substantial holding, Santos L Helper Pty Ltd, 24 Jun 2026 (03107083; scanned, read by OCR): https://announcements.asx.com.au/asxpdf/20260624/pdf/070y7mgylfzjr3.pdf
- [I29] Change of Director's Interest Notice, Kate Greenhill, 28 Nov 2025 (03034007): https://announcements.asx.com.au/asxpdf/20251128/pdf/06snwbfjd97pg5.pdf
- [I30] Change of Director's Interest Notice, Michael Hitz, 1 Dec 2025 (03034931): https://announcements.asx.com.au/asxpdf/20251201/pdf/06srvm6qnr3t90.pdf
- [I31] Change of Director's Interest Notice, Michael Hitz, 8 Dec 2025 (03038119): https://announcements.asx.com.au/asxpdf/20251208/pdf/06t1vyrg7br909.pdf
- [I32] Application for quotation of securities, 30 Sep 2026 (03146301): https://announcements.asx.com.au/asxpdf/20260930/pdf/074r3xl4x6341l.pdf
- [I33] Notification of cessation of securities, 13 Oct 2026 (03151829): https://announcements.asx.com.au/asxpdf/20261013/pdf/0758jh3rcrlbyw.pdf
- [I34] IR Acquires IQ Services, 4 May 2015 (01622038): https://announcements.asx.com.au/asxpdf/20150504/pdf/42ybb5qfplzkcl.pdf
- [I36] Investor Session Presentation, 24 Mar 2026 (03075342): https://announcements.asx.com.au/asxpdf/20260324/pdf/06xrgs38ph3nt8.pdf
- ASX announcement lists for IRI, 2012 to 2026 (checked for acquisitions, approaches and reviews): https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=IRI&timeframe=Y&year=2026 (and the same address for each year)

Peers (ASX announcements):
- [P1] Reckon, 2026 Half Year Results Summary, 4 Aug 2026 (03121566): https://announcements.asx.com.au/asxpdf/20260804/pdf/072d72lnwnmydy.pdf
- [P2] Reckon, FY25 Results Commentary, 10 Feb 2026 (03058470): https://announcements.asx.com.au/asxpdf/20260210/pdf/06w49z08w6b4f6.pdf
- [P3] AI-Media, FY26 Results Announcement, 27 Aug 2026 (03130792): https://announcements.asx.com.au/asxpdf/20260827/pdf/0738x6cwx2yd74.pdf
- [P4] Prophecy International, Annual Report, 1 Oct 2026 (03147151): https://announcements.asx.com.au/asxpdf/20261001/pdf/074t7cy4wlr4s0.pdf

Data:
- [D1] Norgate prices and volumes: data/norgate/universe/prices_2026.csv.gz (and 2022 to 2025 files), IRI.au and PRO.au.
- [D2] ASX company data (last price, bid, ask, market value for IRI, RKN, AIM): data/research_data/asx_company.json, fetched 7 Nov 2026 UTC.
- [D3] AUD/USD and AUD/NZD daily rates: data/fx/fx_daily.csv.
- [D4] RBA F1.1 money market rates (cash rate 4.60% and 3-month bills 4.80% in October 2026): data/rates/rba_f1_1.csv.

Secondary source:
- [S1] Carnegie Council profile of Steve Killelea (founder of the Institute for Economics and Peace): https://carnegiecouncil.org/people/steve-killelea
