# The Colonial Motor Company (NZX:CMO): deep dive. No case: too thin to trade. NZX's own data gives a median of NZ$7,407 traded on market a day over the 20 sessions to 6 November 2026, against the NZ$12,500 the rulebook needs. Not tested as a value pick

Written 2026-11-08 by the research desk. Price at writing: NZ$6.95 (close on Friday 6 November 2026, FinFeedAPI, data/prices/NZX/CMO.csv; NZX's company data gives the same close with a bid of NZ$6.95 and an offer of NZ$7.25 [C2]; NZX's market value for that day, NZ$227,227,692.40, divided by 32,694,632 shares also gives NZ$6.95 [C1]). Market value: NZ$227.2m (32,694,632 shares on issue, NZX [C2]).
Status: finished. Verdict: no case. No card and no red team. This is a simulation and not financial advice.
Fact sheet: research/facts/NZ_CMO.md (written 2 November 2026 under the earlier template, price from 30 October), grade B, "likely C on liquidity". The question it set: is the property worth its NZ$251.4m valuation, and is a 5.9% return on equity the new normal or a low point? Cam's framing for this deep dive: is the property worth what the book says, and is it within reach of holders?

Value pick (rulebook section 5a): not tested. The brief said to measure liquidity first and stop if it fails, and it fails by a factor of about 1.7. No valuation was done, so there is no bad, middling or good case, no expected price and no expected gain. There is no watch trigger price either: the case fails on trading, and a lower price doesn't fix that.

> In short. NZX's own daily trading data for the 20 sessions from 9 October to 6 November 2026 gives a median of NZ$7,407 traded on market a day [C1]. The rulebook needs at least NZ$12,500 on NZX. The most a position could be under the section 3 limit (two sessions at 10% of the median) is NZ$1,481, below the NZ$2,500 smallest NZX order. This failure is narrow, unlike most: four of the last five sessions traded more than NZ$12,500 as the price slid from NZ$7.18 to NZ$6.95, and if the next three sessions (9 to 11 November) do the same, the median crosses the line. But the annual meeting, held on 6 November (not 5 November), has already answered half of Cam's question. The retiring chair said a shareholder had asked for the "lazy balance sheet" to pay bigger dividends and the board's answer was "a polite 'no'"; the company "favours owning strategically important property" for the long term and will recycle capital into new dealerships [C5]. The chief executive said first-quarter FY27 earnings were "significantly impacted" against the year before [C6]. So the property is not within reach of holders short of a sale of the company, and the profit the fact sheet's downside rests on is already falling. Even if trading picks up, the case starts weak.

## Liquidity, measured first
From NZX's activity file for ISIN NZCMOE0001S7 (config/nzx_isins.csv), read on 8 November 2026 [C1]. Arithmetic in python3 -I on that file, with each day's timestamp converted to NZ time:

| Window (to 6 November 2026) | Median on-market value a day | Mean on-market value a day | Sessions at or above NZ$12,500 |
| --- | --- | --- | --- |
| 20 sessions (from 9 October) | NZ$7,407 | NZ$14,043 | 8 of 20 |
| 60 sessions (from 14 August) | NZ$7,528 | NZ$18,002 | 29 of 60 |
| 120 sessions (from 20 May) | NZ$12,799 | NZ$18,875 | 60 of 120 |
| 250 sessions (from 7 November 2025) | NZ$10,263 | NZ$17,358 | 112 of 250 |

- Off-market volume on one session in the 20 (3 November, 1,304 shares, NZ$9,363); counting it, the median is still NZ$7,407 [C1].
- Every session traded, but five of the 20 (20, 22, 28, 29 and 30 October) traded under NZ$1,000, with three trades or fewer [C1].
- The last five sessions (2 to 6 November) traded NZ$167,543 on market (23,931 shares). The price fell from NZ$7.18 to NZ$6.95 on 3 November, three days before the meeting, with no announcement from the company between 21 October and the meeting papers on 6 November [C1][C3]. The 15 sessions before that had a median of NZ$5,010.
- Section 3 limit: 2 x 10% x NZ$7,407 = NZ$1,481. A position reaches the NZ$2,500 smallest NZX order only when the 20-session median is NZ$12,500, so the floor and the position limit agree.
- Over two years, the rolling 20-session median was at or above NZ$12,500 in 101 of 482 windows (21%), in short runs that mostly follow results and dividends: 13 to 27 December 2024; late June to early July 2025; 2 to 8 September 2025; mid to late December 2025; 10 April to 12 May 2026; 17 June to 29 July 2026; and 18 August to 10 September 2026, peaking at NZ$23,265 on 27 August after the 14 August result [C1]. It doesn't stay there, so a position bought in one of those runs may not be sellable at our size in a bad week, which is the red team's liquidity test.
- The spread at the 6 November close was NZ$6.95 bid, NZ$7.25 offer, 4.2% of the mid [C2], so a round trip would cost about 4% in spread alone before brokerage.

Why it is thin, from the fact sheet's reading of the annual report (not re-checked): Gibbons family interests sit in several substantial holder groups, P L Bennett holds 7.42% and the Wilson and Majors group 5.49%. At the meeting, 18,065,764 votes were cast on the first resolution, 55% of the shares on issue [C4], which fits a long-standing register that votes and rarely sells.

## What the annual meeting said (6 November 2026)
The brief asked for this only if liquidity passed. It didn't, but the meeting bears directly on Cam's question and on what would reopen the case, so the points that matter are recorded here as facts, without a valuation.

1. Capital and the property. The chair, Ashley Waugh, said: "A Shareholder recently contacted me to question the Board's dividend policy, implying our 'lazy balance sheet' should be utilised to increase dividends ... my response to the Shareholder's question was a polite 'no'." He went on: "CMC values operating with a conservative balance sheet, favours owning strategically important property, which requires a long-term view", and "Capital re-cycling is something you will hear more about from the Company", citing the Christchurch BYD investment [C5].
2. Trading. The chief executive's outlook slide, headed "Q1 – Headwinds", says "Challenging economic and market conditions have significantly impacted Q1 earnings relative to the prior year" [C6]. No figure and no FY27 guidance was given. The chair said 2027 "may prove to be an even greater challenge" and "life going forward is expected to continue to be very tough" [C5].
3. New business. The chair mentioned "other significant projects" that he couldn't talk about [C5]; the chief executive said the company expects "to have more to share as FY 2027 unfolds" [C6]. Neither says whether these need capital or release it.
4. The board. Ashley Waugh retired at the end of the meeting and John Journee, an independent director since December 2018 who has chaired the audit committee for five years, was elected chair [C7]. G D Gibbons was re-elected with 97.7% of votes cast and S B Gibbons with 100.0% [C4].

What this does to the fact sheet's question, before any valuation: the "within reach of holders" half is answered no, for now and in the board's own words. Dividends stay at up to 70% of trading profit, and the property is kept and recycled into new sites. The NZ$9.77 net tangible assets a share would reach holders only through a sale of the company or a wind-up, and with a settled family-linked register and a board that has just said no, neither has any sign of coming. Under the brief's first test (a value that only a sale or a wind-up would realise is the good case, not the middling one), NZ$9.77 is the good case.

## What would reopen it
- Liquidity first, and nothing else reopens it: NZX's own 20-session median on-market value must be at least NZ$12,500 a day. It is close. The three oldest sessions in the window (9, 12 and 13 October) traded NZ$3,008, NZ$5,506 and NZ$5,010; if the next three sessions (9, 10 and 11 November) each trade NZ$12,500 or more on market, the median crosses [C1]. The weekly research ranking, or the next desk run, can re-test it on the same NZX file. If it crosses, a deep dive needs to show it holds, since past runs above the line lasted from a single day to about six weeks.
- If it does reopen, the value case has to clear the 6 November evidence. Starting points, none of which was tested here:
  1. The middling case can't be the NZ$9.77 net tangible assets, because the board has ruled out returning the property's value. It has to come from earnings the market can see. The fact sheet compared nothing with peers; dealership groups are priced on earnings after rent (the PWR and ASG deep dives valued Peter Warren and Autosports that way), so CMO needs comparing with named listed dealer groups on that measure.
  2. Test the property on the rent the dealerships actually pay, not only on the Quotable Value valuation. The PWR deep dive found Peter Warren's owned property earned 3.85% on book at the rent its own dealerships paid, well below the valuer's yield (research/picks/PWR.md, a desk file; Peter Warren's figures were not re-checked here, and CMO's annual report was not read for the equivalent).
  3. The first-quarter fall. At NZ$6.95, a value pick needs a bad case no lower than NZ$6.26 and a middling case of at least NZ$7.99. The fact sheet's "against" figure, NZ$6.43, is 7.5% below the price, but it rests on FY26 trading profit after tax of NZ$18.7m. On the fact sheet's own method (6 times profit after a notional rent of 6.5% of NZ$251.4m, taxed at 28%), each NZ$1m fall in that profit takes about 18c a share off it, and it reaches the 10% limit at about NZ$17.7m, 5% below FY26 (arithmetic on the fact sheet's figures, not re-checked). So the half-year result, due about late February 2027 (inferred from 26 February 2026), must show trading profit holding near FY26's pace for the bad case to stay inside the value pick limit, and the middling case still needs a mechanism, which with no capital return can only be earnings recovering or a bid.
- So, even if liquidity passes this week, the likely result of a full deep dive on today's evidence is no case or a wait for the 1H27 result. The case would be worth a fresh look if both liquidity passes and the 1H27 result shows trading profit after tax for the half at or above 1H26's NZ$10.4m [fact sheet, from C8], or the company announces a capital return, a property sale with the cash going to holders, or receives an approach.

## Corrections to the fact sheet
1. Liquidity: measured at NZ$7,407 a day (20-session median, on market, NZX's own data), not "not measured". The fact sheet's guess that the median was below NZ$12,500 was right [C1]. Its Investing.com figure of 2,640 shares a day over three months matches NZX's own mean (2,641 shares a day over the 63 sessions from 4 August to 30 October), but the median on-market value over those sessions was NZ$7,396, and over the 20 sessions to 30 October NZ$6,451 [C1].
2. The annual meeting was held on Friday 6 November 2026, not 5 November [C4][C5][C7]. research/picks/INDEX.md also says 5 November; I haven't edited it.
3. Price: NZ$6.95 on 6 November 2026, not NZ$7.18 (30 October), with a bid of NZ$6.95 and an offer of NZ$7.25 [C1][C2]. At NZ$6.95 the fact sheet's anchors are +40.6% (NZ$9.77) and -7.5% (NZ$6.43). Arithmetic only; neither anchor was tested, and the meeting evidence above weakens both.
4. FY26 trading profit after tax was up 5.1% on FY25 (NZ$18.7m against NZ$17.8m, the fact sheet's own table), which the chair calls "up nearly 5%" [C5]. The fact sheet's guidance section calls it "about level".
5. Dividend policy: the chair describes it as "distributing up to 70% of the post-tax trading profit" [C5]; the fact sheet says 60% to 70%. The annual report wasn't re-read, so which wording is the formal policy isn't settled here.
6. John Journee has been chair since 6 November 2026 [C7].

## What I couldn't verify
- The business itself: no financial statements were read, because the liquidity test ended the work first. Every number above taken from the fact sheet is marked as not re-checked.
- The size of the first-quarter fall: the meeting gave no figure [C6].
- The substantial holder notice of 6 March 2026, which the fact sheet couldn't read: not tried.
- What the unnamed "other significant projects" are [C5].

## Checks
- Not on Cam's excluded list: config/judgement_excluded.csv has no entries (confirmed by Cam on 8 November 2026).
- Placement-pattern reopening in the last 30 sessions (rulebook section 9): not checked, as the case stopped at liquidity. NZX's 2026 announcement list shows no share issue [C3], and the fact sheet records no capital raising in two years.
- Liquidity: fails. Median NZ$7,407 a day on market over the 20 sessions to 6 November 2026 against NZ$12,500; the most the position could be under section 3 is NZ$1,481, below the NZ$2,500 smallest order [C1].

## Sources
- [C1] NZX daily trading activity for NZCMOE0001S7 (The Colonial Motor Company ordinary shares), two years to 6 November 2026, read 8 November 2026: https://api.nzx.com/public/instrument/NZCMOE0001S7/metrics/activity/past/2Y.json
- [C2] Closing prices, FinFeedAPI: data/prices/NZX/CMO.csv (close NZ$6.95 on 6 November 2026); NZX company data in data/research_data/nzx_company.json, fetched 7 November 2026 UTC (close NZ$6.95 on 6 November, bid NZ$6.95, offer NZ$7.25, 32,694,632 shares)
- [C3] Colonial Motor's 2026 NZX announcement list, read 8 November 2026 (latest items: the three meeting announcements of 6 November): https://api.nzx.com/public/company/CMO000000/announcements/2026/all.json
- [C4] 2026 Annual Meeting results, 6 November 2026: https://www.nzx.com/announcements/483210 ; PDF https://api.nzx.com/public/announcement/483210/attachment/480881/483210-480881.pdf
- [C5] Chair's address to the 108th Annual Meeting, 6 November 2026: https://www.nzx.com/announcements/483208 ; PDF https://api.nzx.com/public/announcement/483208/attachment/480878/483208-480878.pdf
- [C6] Chief Executive's presentation to the 2026 Annual Meeting, 6 November 2026 (same announcement): https://api.nzx.com/public/announcement/483208/attachment/480880/483208-480880.pdf
- [C7] Election of Chair, 6 November 2026: https://www.nzx.com/announcements/483211
- [C8] Half-year result and dividend, 26 February 2026 (1H26 trading profit after tax NZ$10.4m, as recorded in the fact sheet; not re-read): https://www.nzx.com/announcements/468286
- Desk files used for lessons only: research/picks/PWR.md (Peter Warren), research/picks/ASG.md (Autosports)
- Fact sheet: research/facts/NZ_CMO.md (2 November 2026), used as leads only
- config/nzx_isins.csv (ISIN), config/judgement_excluded.csv (excluded list), RULEBOOK.md sections 3, 5a and 7
