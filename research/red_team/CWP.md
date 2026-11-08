# Red team: Cedar Woods Properties (ASX:CWP) as a value pick at A$6.33

Written 2026-11-08 by the red team, a separate agent that saw only the deep dive (research/picks/CWP.md), the checklist (docs/RED_TEAM.md) and the rulebook. No card was drafted. This is a simulation and not financial advice.

What was asked: the deep dive was written under the old value-pick test (middling case at least 25% above the price) and said "wait for the H1 FY27 result". Under today's rules (section 5a, 8 Nov 2026) a value pick needs its bad case no more than 10% below the price, its middling case at least 15% above it, and every research pick needs an expected gain after costs of at least the cash rate plus 5% a year to its resolve date: 2.13% plus 5% over about 730 days is 14.3% (src/decide.py counts it simply: the yearly rate times days over 365). On the deep dive's own numbers it scrapes through: bad -9.6% at 0.75 times book, middling +22.1%, expected about +17.9% before costs.

> In short: it doesn't qualify at A$6.33. The deep dive's June 2028 book (A$6.90 in the bad case) is about A$0.21 too high: it leaves in the A$21.4m FY26 final dividend paid on 30 October 2026. On a corrected book the bad case is -13% at 0.75 times and -18% at 0.70 times, so the 10% leg fails at either multiple, and 0.70 times is the better-supported one (weaker developers trade at 0.68 to 0.75 times today, Cedar Woods itself troughed at 0.67 times in June 2022, and AVJennings traded at 0.40 times before its bid). Even with the deep dive's own multiples and chances, the corrected expected gain after costs is about 11% to 13%, below the 14.3% minimum. On my chances and prices it is about 4%. The deep dive also missed that management pulled sales releases forward into FY26 "anticipating a slowdown", which makes the weak Q4 FY26 and Q1 FY27 partly payback rather than a choice that reverses. Verdict: wait for the H1 FY27 result (about 24 February 2027); before then it qualifies only at or below about A$5.75.

## 1. Are the facts right?

I re-opened twelve primary sources (listed under Sources) and checked the numbers the case rests on.

| Fact in the deep dive | Source re-opened | Held? |
| --- | --- | --- |
| FY26 revenue A$502.4m, NPAT A$65.6m, EPS 77.9c, dividends 39c, gross margin about 30% | FY26 results announcement and annual report five-year table | Yes |
| Equity A$544.5m, NTA A$6.35, net bank debt A$157.7m, 29.0% of equity, 18.1% of tangible assets less cash | Annual report, KPIs and five-year table | Yes |
| Year-end price to book FY22 to FY26: 0.72, 0.97, 0.85, 1.20, 1.09 (average 0.97) | Annual report five-year table (year-end prices A$3.68, 5.03, 4.73, 7.09, 6.94 over NTA A$5.11, 5.21, 5.55, 5.90, 6.35) | Yes |
| Bank loans A$166.5m drawn, facilities A$330m (A$264m to Jan 2029, A$66m to Jan 2031), guarantees A$50.9m, undrawn A$112.6m, average rate 5.85%, 51% hedged | Annual report note 12 and capital management section | Yes |
| Covenants are interest cover, loan to valuation and net debt to EBITDA; only the 2 times interest cover level is published | Annual report note 12 and note 23 | Yes. The report gives interest cover as 8.1 times in the text and 8.9 times in the five-year table; either way far above 2 times |
| Inventory A$842.4m: land at cost A$460.8m, development costs A$380.4m, A$1.2m at net realisable value; key audit matter is inventory carrying value | Annual report note 7 and auditor's report | Yes |
| Directors' relevant interests: Hames 11,260,552, Brown 7,618,633 | Annual report directors' report | Yes |
| H1 FY26 NPAT A$39.6m (60% of the year), net bank debt A$85.1m at 31 Dec 2025, facility extended Feb 2026 | H1 FY26 announcement | Yes |
| Q1 FY27: presales A$763m (A$380m FY27, A$316m FY28, A$67m FY29), 311 settlements, 167 gross sales, down 24% on Q4 and 57% on the prior year, Elegan and Incontro to settle in Q1 FY28, "signs of improvement in Q2 to date" | Q1 FY27 update | Yes. The 167 is a count of lots, homes and offices, not dollars; the deep dive's table doesn't label its units |
| Q1 FY27 settled revenue about A$120m | Q1 update chart (rendered and measured) | Yes, about A$120m to A$125m; the chart puts FY27 settled plus presold at about A$503m |
| FY27 guidance about A$75m reaffirmed; Eglinton EBIT above A$20m from 162 lots at about 40% margin; distressed sites coming to market | AGM addresses and presentation | Yes |
| Shares on issue 85,480,583 | Appendix 2A, 31 Aug 2026 | Yes |
| WAM 6,617,816 shares, 7.78%, change on 5 Aug 2026 | Form 604, 7 Aug 2026 | Yes |
| Blackburne bought 14,532 on market on 2 Sep 2026, price not stated | Appendix 3Y, 2 Sep 2026 | Yes |
| Kroll: Cedar Woods 0.95 times book (4.6% below NTA), Winton 0.68 (30.5% below), Finbar 0.75 (24.5% below); Cedar Woods "the closest listed company to Peet"; four-year return on equity 9.8% | Peet scheme booklet, Kroll report section 11 and Appendix 7 | Yes |
| AVJennings: A$0.655 cash; Kroll valued it at A$0.54 to A$0.61 | AVJennings scheme booklet | Yes. Kroll's Peet report adds that the deal was 20.1% below NTA and that AVJennings traded 59.5% below NTA (0.40 times) just before it was announced, which the deep dive leaves out |
| Gross sales FY26 1,521, net 1,326 (195 cancelled, 13%); Q1 FY26 389; Q3 FY26 442 | FY26 results, Q1 FY26 and Q3 FY26 updates | Yes. Q4 FY26 was therefore 220, half of Q3 |

One arithmetic error matters (section 3): the June 2028 book in the 24-month test.

Left out of the deep dive:
- Management pulled sales forward. The FY26 results presentation (slide 13) says: "Anticipating a slowdown, CWP brought forward sales releases to increase presales", and cites "lower stock levels" for the weak Q4. So part of FY26's record sales and the A$830m presales were brought forward from FY27, and the "fewer stages being released" in Q1 FY27 is partly the stock already sold, not only a marketing choice that will reverse in Q2. Lower marketing spend has been cited three periods running (H1 FY26 upgrade, Q4 FY26, Q1 FY27); it lifted FY26 profit and may be protecting FY27 profit at the cost of FY28 presales.
- Tax changes for property investors announced in the May 2026 Federal budget, which the annual report and both the Q1 update and AGM name as a cause of weaker buying. Investors were 30% of presales at June 2026 and apartments are about 30% of the pipeline, including the 2025 and 2026 apartment sites (Fairfield VIC and QLD).
- National unemployment up to 4.7% at September 2026 and industry sales volumes about 18% below their five-year average (AGM presentation, citing Cotality).
- The annual report notes that "apartment delivery costs" continue to affect "project feasibility and delivery timeframes", which bears on the write-down risk for recent apartment and townhouse sites.
- Management's own outlook is that weak conditions "persist throughout FY27" (AGM), which is the year that has to build FY28's presales.

Nothing else turned up: no raising since the October 2025 underwritten dividend plan, no director departures (all six directors and the CFO and company secretary attended the AGM), no lawsuits (contingent liabilities are bank guarantees only), no auditor qualification, the remuneration report passed with 98% and no strike, and the Hames Sharley related-party engagement is disclosed. The 2026 ASX list has no substantial holder notice after WAM's on 7 August.

## 2. Is it really overlooked, or cheap for a reason?

Mostly cheap for a reason the market can already see.
- The fall: A$9.10 in early March 2026 to A$5.85 on 14 October (52-week low A$5.74 intraday). From the FY26 result on 25 August to 14 October it fell 24% on median daily volume of about 162,000 shares against about 94,000 in July and August, with 8.4% of the shares trading in seven weeks (Norgate). That was selling into a record result with a soft outlook. No holder crossed a 1% step (no notices), so the selling looks broad rather than one informed seller.
- Overhang: WAM (7.78%) bought at about A$6.90 to A$7.18 and is under water. Its stake is about 40 days of normal volume. If it sells, the price has to absorb it.
- Industry trouble that peers already show: on 29 October Winton traded at 0.68 times book, Finbar 0.75, Mirvac 0.77 and Lifestyle Communities 0.76 (Kroll, Appendix 7). Finbar was A$0.725 on 6 November, near its 52-week low of A$0.66. Cedar Woods at 0.95 to 0.99 times book is priced above every listed residential developer except Aspen.
- Debt doesn't fall due before January 2029 and the facility is extended each year (next review about January to February 2027).
- Management's record against its own guidance is good, which is the strongest point for the case: FY26 guidance started at 10% growth (August 2025), went to 15% (October 2025) and 30% to 35% (February 2026), and 36% was delivered. FY27's A$75m is very likely. But guidance only covers FY27; the question is FY28.

## 3. The valuation

### The bad case is not the floor

The deep dive's 24-month bad case is FY28 profit of about A$21m, write-downs avoided, the share at 0.75 times June 2028 book of A$6.90, plus 55c of dividends: A$5.72, 9.6% below A$6.33.

First, the book is overstated. The deep dive's June 2028 figures (A$6.90 bad, A$7.04 middling, A$7.17 good) are June 2026 equity of A$544.5m plus half of FY27 and FY28 profit, over about 85.9m shares; my rebuild of that method gives A$6.90, A$7.03 and A$7.14. That leaves in the A$21.4m FY26 final dividend (25c, paid 30 October 2026), which was declared after year end and is not a liability at 30 June 2026 (annual report note 30), and takes out the FY28 final, which isn't paid until about October 2028. The deep dive's own December 2026 book (A$6.65) does deduct the FY26 final, so the two are inconsistent. Rolling forward from the June 2026 accounts with dividends when paid (FY27 A$75m, interim 16c, 50% payout; FY28 H1-weighted because Elegan and Incontro settle in Q1; about 0.4m new shares a year from vesting rights):

| FY28 profit | June 2028 book, deep dive | June 2028 book, corrected | After the FY28 final goes ex (late Sep 2028) | Dividends in the window |
| --- | --- | --- | --- | --- |
| A$21m (bad) | A$6.90 | A$6.69 | A$6.62 | 56c |
| A$43m (middling) | A$7.04 | A$6.90 | A$6.75 | 69c |
| A$63m (good) | A$7.17 | A$7.08 | A$6.86 | 80c |

A November 2028 price sits on the book after the FY28 final has gone ex, since that dividend is counted separately; using June 2028 book instead adds 5c to 26c a share. I use the ex-dividend book below and show the other where it matters.

Second, 0.75 times is not where a bad FY28 would leave the shares. The evidence for the multiple:
- Weaker listed developers already trade at 0.68 (Winton, four-year return on equity 5.6%) and 0.75 times (Finbar, 5.4%) in today's market, before any FY28 drop (Kroll, 29 October).
- In the bad case Cedar Woods' FY28 return on equity is about 3.6% (A$21m on about A$575m), AVJennings territory (3.5% four-year average). AVJennings traded at 0.40 times NTA before AVID's approach; a control buyer then paid 0.80 times, and Kroll valued it at 0.67 to 0.75 times with its projects worth about book. That deal is a control price for a weak developer, not a floor for a minority holder, and the 22% Hames and Brown block makes a rescue bid for Cedar Woods unlikely without their support.
- Cedar Woods' own last downturn: 0.67 times on 17 June 2022 (A$3.42 against NTA of A$5.11), 0.72 times at June 2022 year end, and lows of about 0.79 to 0.82 times in 2023 and 2024 (Norgate closes over reported NTA). Return on equity was 7.3% to 9.1% then, higher than the bad case.

So 0.70 times is the better central bad multiple, with 0.65 possible. At A$6.33:

| Bad-case multiple | Price with 56c dividends | Change |
| --- | --- | --- |
| 0.80 | A$5.85 | -7.5% |
| 0.75 | A$5.52 (A$5.58 on June 2028 book) | -12.8% (-11.9%) |
| 0.70 | A$5.19 (A$5.24) | -18.0% (-17.2%) |
| 0.65 | A$4.86 | -23.2% |

The 10% leg needs 0.78 times of the corrected book, above every weaker developer today and above the 2022 trough. It fails.

Third, the bad case itself leaves out the tail the deep dive describes under "What would make this wrong": write-downs on the 2025 and 2026 Melbourne built-form sites (Fairfield VIC at A$132,000 to A$167,000 a dwelling, Kealba A$143,000, Springvale A$262,000, about A$105m) and a raise. Net debt rising to A$201m to A$251m by June 2028 against about A$279m that can be drawn (A$330m less A$50.9m of guarantees) leaves A$30m to A$80m of headroom, and the deep dive's low case puts net debt at about 5.5 times FY28 EBITDA against a covenant whose level isn't published. The board has shown it will issue shares (the underwritten October 2025 dividend plan at A$7.42). I give this tail about 10% at roughly 0.65 times a book cut by about A$0.46 of after-tax write-downs, plus reduced dividends: about A$4.45.

### The middling case is at the top of what the market pays

Middling is FY28 about A$43m and FY29 recovering. At 1.00 times the ex-dividend book of A$6.75 the shares would be about 11.7 times the deep dive's FY29 estimate of A$50m and about 13 times FY28, against the deep dive's own measure of the company's mid-cycle multiple, about 9.7 times. It isn't impossible (June 2023, also a trough year with a 7.3% return on equity, was 0.97 times book and 13 times trailing profit), but it is the upper end, and Kroll's 0.95 times today is in a market still paying for a record FY27. I use 0.95 times as central:

| Middling multiple | Price with 69c dividends | Change |
| --- | --- | --- |
| 1.00 | A$7.43 (A$7.58 on June 2028 book) | +17.4% (+19.8%) |
| 0.95 | A$7.10 (A$7.24) | +12.1% (+14.4%) |
| 0.90 | A$6.76 | +6.8% |

At 0.95 times the 15% leg fails too, narrowly. At 1.00 times it passes.

FY28 margin is the input that moves the middle most: each point of gross margin on about A$450m of revenue is about A$3.2m after tax, about 4c a share. FY28 opens with Elegan and Incontro, two apartment projects, which usually carry lower margins than land (Eglinton's 40% is land). The deep dive's 28% middle may be generous for that mix; I couldn't check project margins.

### The FY28 range (A$21m to A$63m)

The method (FY28 revenue as presales at June 2027 over 0.9, FY26's cost base) is reasonable and the range is wide enough. Two points on where in it to sit:
- The comparison with a year ago cuts both ways. Presales beyond the current year are A$383m now (FY28 and FY29) against A$353m a year ago (FY27 and FY28), so the forward book is not thinner. What has changed is the rate of new sales: about A$55m net in Q1 FY27 against about A$168m a quarter in FY26.
- The "about A$40m of FY27 contracts slipping or cancelled" is a derived figure. June's split is given only as "approximately 65%" in FY27 (A$519m to A$560m depending on rounding) and Q1 revenue is read from a chart (about A$120m to A$125m), so the slippage is somewhere between about A$15m and A$60m. The direction is clear from the guidance wording: in June presales covered "more than 90%" of FY27 revenue on presales alone (implying revenue up to about A$600m); in September settled plus presold covered "over 90%" (up to about A$556m). Cancellations are not disclosed for Q1; in FY26 they were 13% of gross sales in a strong market.

Management's own view (weak through FY27, rates falling in 2027) and the pulled-forward releases point to FY28 between the low and middle cases more often than above the middle.

## 4. The dated events and the exit

- H1 FY27 result (about 24 February 2027): will show a record half of about A$45m, which the market expects. The useful numbers are FY28 presales at 31 December, Q2 gross sales after the new releases, cancellations if given, and net debt. It can come and go without moving the price if FY28 presales land near A$350m.
- Facility review (about January to February 2027): an extension on the usual terms says the banks are comfortable; a smaller or shorter facility would matter more than the result.
- Q3 update (about 30 April 2027) and the FY27 result with FY28 guidance (late August 2027): the August 2027 guidance is the event that shows whether FY28 is A$25m or A$45m. On a value pick it falls inside the window; on an ordinary six-month pick it doesn't.
- Liquidity is not a problem: the 20-session median is about A$925,000 a day (NZ$1.18m) against a position of about A$2,016.

## 5. The stated chances and the expected gain

Costs. The deep dive says "about 2% round trip", but its own items add to more: half the quoted A$0.08 spread each way (1.3% in all), A$15 brokerage each way (0.74% each on A$2,016) and 0.5% to convert, 3.3% in all, or 2.5% if the plan's monthly cover pays for the buy. src/decide.py's model, using the Corwin and Schultz spread from the 21 sessions to 30 October (0.56%, below the quoted 1.26% on 6 November), gives 1.95% with the buy covered and 2.70% without. I use 2.35%.

Chances. The deep dive has 30/50/20 (bad, middling, good). I'd use 35/45/20, with 10 of the 35 points as the worse tail:
- More weight on bad: management expects weak conditions all through FY27, which is when FY28 gets sold; two quarters running at about half the earlier rate (442, 220, 167 gross sales); releases were pulled forward, so Q2's new releases test real demand; rising unemployment and investor tax changes; five rate rises in 2026, with cuts only forecast.
- Against that, and why not more: FY27 is near-certain; management has beaten guidance two years running; FY28 is about 70% presold already; the board and WAM bought near A$7; and by November 2028 the market will be pricing FY29 and FY30, so a rate-cutting 2027 lifts the price even if FY28 is weak.

| Outcome by about 8 Nov 2028, with dividends | Deep dive | Red team |
| --- | --- | --- |
| Worse: write-downs or a raise, about 0.65 times a cut book | (not shown) | 10% at A$4.45 (-29.7%) |
| Bad: FY28 about A$21m to A$30m | 30% at A$5.72 (0.75 times A$6.90) | 25% at A$5.19 (0.70 times A$6.62) |
| Middling: FY28 about A$43m, recovery under way | 50% at A$7.73 (1.00 times A$7.04) | 45% at A$7.10 (0.95 times A$6.75) |
| Good: FY28 about A$63m, full recovery or a bid | 20% at A$9.42 (1.20 times A$7.17) | 20% at A$9.04 (1.20 times A$6.86) |

Expected gain at A$6.33 against the 14.3% minimum (730 days at 2.13% plus 5%):

| Version | Before costs | After about 2.35% |
| --- | --- | --- |
| Deep dive as written | +17.9% | +15.6% (passes by about 1.3 points) |
| Deep dive's multiples and chances, corrected book (June 2028 book) | +15.7% | +13.4% (fails) |
| Same, on the ex-dividend book | +13.4% | +11.1% (fails) |
| Deep dive's chances, 0.70 / 0.95 / 1.20 times | +9.2% | +6.9% (fails) |
| Red team, four outcomes above | +6.5% (expected A$6.74) | +4.2% (fails by about 10 points) |

The book correction alone is enough to fail the minimum, before any argument about multiples or chances.

Prices at which it would qualify on my numbers: the bad leg at 0.70 times needs A$5.77 or lower; the expected gain needs A$5.78 or lower; the middling leg at 0.95 times needs A$6.17 or lower. So about A$5.75, 9% below today and near the October lows. The deep dive's reopen trigger of A$5.95 is too high: at A$5.95 the bad case at 0.70 times is -12.8% and my expected gain after costs is about 11%.

## 6. Special situations

Not a special situation. For the record, I agree with the deep dive that a bid is unlikely: the Chair and Deputy Chair hold 22.1% (about 39% of a typical vote), enough to block a scheme, and the AVJennings evidence shows bidders for listed developers in a soft market pay about 0.8 times book, which at A$6.65 is A$5.30, below today's price. A bid is a reason to own the good case, not a floor.

## Three points most likely to make the pick wrong

1. The bad case is set too high. After correcting the book, 0.75 times gives -13% and the better-supported 0.70 times gives -18%; the shares troughed at 0.67 times in 2022 and weaker developers are at 0.68 to 0.75 times now, before FY28's drop shows up in earnings.
2. FY28 sales and margins. Management expects weak conditions all through FY27, sales were pulled forward into FY26, Q4 FY26 and Q1 FY27 ran at about half the earlier pace, investor demand has a new tax headwind, and FY28 opens with apartment settlements at lower margins. The A$43m middle case needs a recovery that management itself doesn't expect before mid-2027.
3. The middling price assumes the market pays full book for a business earning about 7% on equity. At 0.95 times, still above every listed peer bar Aspen, the middling case is +12% and the expected gain is well short of the minimum. Behind both sits the balance sheet tail: thin headroom by FY28, an unpublished net debt to EBITDA covenant the low case would test, and write-down risk on the 2025 and 2026 Melbourne sites.

## What I couldn't verify

- The loan-to-valuation and net debt to EBITDA covenant levels (not published).
- Q1 FY27 net sales and cancellations (not disclosed); the FY27 share of June presales beyond "approximately 65%".
- Per-project margins beyond Eglinton, and so the margin mix of FY28.
- Short interest: a web search found nothing usable and I didn't open third-party data sites.
- Broker forecasts for FY28.
- I didn't re-open the AustralianSuper, Dimensional or Hames notices, the 2011 approach, or the desk's Peet deal file (the brief kept me from other research files until this review was written).
- Cedar Woods' price to book before 2022 (I didn't have NTA figures for those years).

## Sources

Cedar Woods (ASX announcements):
- FY26 Annual Report, 25 Aug 2026 (03129275): https://announcements.asx.com.au/asxpdf/20260825/pdf/0734y7jjy5d8b9.pdf
- FY26 Full Year Results Announcement, 25 Aug 2026 (03129277): https://announcements.asx.com.au/asxpdf/20260825/pdf/0734ycspqxpxtn.pdf
- FY26 Full Year Results Presentation, 25 Aug 2026 (03129278), slide 13 on releases brought forward: https://announcements.asx.com.au/asxpdf/20260825/pdf/0734yfygp813dv.pdf
- H1 FY26 Results Announcement and Guidance Upgrade, 24 Feb 2026 (03063701): https://announcements.asx.com.au/asxpdf/20260224/pdf/06wn4ckb3h1sk7.pdf
- FY26 First Quarter Update, 29 Oct 2025 (03017104): https://announcements.asx.com.au/asxpdf/20251029/pdf/06r5w7nmr838bp.pdf
- FY26 Third Quarter Update, 30 Apr 2026 (03087988): https://announcements.asx.com.au/asxpdf/20260430/pdf/06z0t8m6ykgtl1.pdf
- FY27 First Quarter Operational Update, 27 Oct 2026 (03157382): https://announcements.asx.com.au/asxpdf/20261027/pdf/075t6dhx63b09l.pdf
- 2026 AGM Chairman and Managing Director Addresses, 5 Nov 2026 (03162172): https://announcements.asx.com.au/asxpdf/20261105/pdf/0767p8114k1rzs.pdf
- 2026 AGM Presentation, 5 Nov 2026 (03162174): https://announcements.asx.com.au/asxpdf/20261105/pdf/0767pd8p0hn5mh.pdf
- 2026 AGM Results, 5 Nov 2026 (03162693): https://announcements.asx.com.au/asxpdf/20261105/pdf/0768z8d28nbpsw.pdf
- Application for quotation of securities, 31 Aug 2026 (03133739): https://announcements.asx.com.au/asxpdf/20260831/pdf/073jt36p0g1sz9.pdf
- Change in substantial holding, WAM, 7 Aug 2026 (03123205): https://announcements.asx.com.au/asxpdf/20260807/pdf/072jxbwls9tlr3.pdf
- Change of Director's Interest Notice, Blackburne, 2 Sep 2026 (03134788): https://announcements.asx.com.au/asxpdf/20260902/pdf/073mnwf1b5d4cv.pdf
- ASX announcement list for CWP, 2026: https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=CWP&timeframe=Y&year=2026

Peers and bids:
- Peet Limited Scheme Booklet with Kroll's Independent Expert's Report, 3 Nov 2026 (03161651), section 11 and Appendix 7: https://announcements.asx.com.au/asxpdf/20261103/pdf/07660scpcjc7r6.pdf
- AVJennings Scheme Booklet with Kroll's Independent Expert's Report, 9 May 2025: https://announcements.asx.com.au/asxpdf/20250509/pdf/06jl49d4m36m43.pdf

Data in this repository: Norgate prices and volumes 2018 to 30 Oct 2026 (data/norgate/universe/); ASX company data fetched 7 Nov 2026 UTC (data/research_data/asx_company.json: CWP last A$6.33, close A$6.36, 52-week A$5.74 to A$9.20; FRI A$0.725); FX (data/fx/fx_daily.csv, NZ$1 = A$0.8064 on 6 Nov); cost and minimum-gain logic in src/decide.py, src/risk.py and src/spreads.py. Arithmetic in python3 -I (scratchpad rt_cwp/book.py and costs.py).

## Verdict

Wait for a named event: the H1 FY27 result, about 24 February 2027. Don't buy at A$6.33 as a value pick.

Reasons: on a corrected book the bad case is 13% below the price at the deep dive's 0.75 times and 18% below at 0.70 times, which the evidence supports better, so the 10% leg fails; the middling case passes the 15% leg only at a full 1.00 times book; and the expected gain after costs is about 11% to 13% on the deep dive's own multiples and chances and about 4% on mine, against a minimum of 14.3%.

Reopen as a value pick:
- before the result, if the price closes at or below A$5.75 with FY27 guidance intact and nothing worse in Q2 (no write-down, raise or facility change);
- at the H1 FY27 result, if FY28 presales at 31 December are A$420m or more and Q2 gross sales 250 or more with guidance held: chances could then move to about 25/50/25 with the bad case at 0.75 times, and the pick qualifies at or below about A$6.10;
- on an approach, a substantial holder notice from a developer or financial buyer, or a change in the Hames or Brown holdings: write it up as a special situation.

If it reopens at A$5.75 or below, the card I would accept: resolve by 8 November 2028 (after the FY28 final dividend is paid); outcomes with dividends counted, A$4.45 (10%), A$5.19 (25%), A$7.10 (45%), A$9.04 (20%), re-priced on the book at the time of entry; dated events: H1 FY27 (Feb 2027), FY27 result and FY28 guidance (Aug 2027), H1 FY28 (Feb 2028), FY28 result (Aug 2028); exit rule: sell at the resolve date, sooner if the price reaches 1.10 times the latest book, or at once on any of FY28 guidance below A$30m, an inventory write-down above A$20m, an equity raising below book, or a covenant waiver or a facility cut at the annual review.
