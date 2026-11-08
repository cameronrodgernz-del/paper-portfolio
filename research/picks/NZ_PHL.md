# Promisia Healthcare (NZX:PHL): deep dive. No case: too thin to trade. NZX's own data gives a median of NZ$451 traded on market a day over the last 20 sessions, against the NZ$12,500 the rulebook needs. Not tested as a value pick

Written 2026-11-08 by the research desk. Price at writing: NZ$0.645 (close on Friday 6 November 2026, FinFeedAPI, data/prices/NZX/PHL.csv; NZX's own market value for that day, NZ$34,971,029.25, divided by 54,218,650 shares gives the same price [L1][L2]). Market value: NZ$35.0m (54,218,650 shares, from the same NZX figure; the 9 October Gould notice uses 54,206,650 [L3]).
Status: finished. Verdict: no case. No card and no red team. This is a simulation and not financial advice.
Fact sheet: research/facts/NZ_PHL.md (written 2 November 2026 under the earlier template, prices from 30 October), grade B. The question it set: is Promisia worth its net tangible assets (NZ$0.885 a share once all warrants are exercised), or only what its earnings support at the roughly 10 times EBITDAF it paid for Chatswood (NZ$0.65)?

Value pick (rulebook section 5a): not tested. The brief for this deep dive said to measure liquidity first and stop if it fails, and it fails by a factor of about 28. No valuation was done, so there is no bad, middling or good case, no expected price and no expected gain.

> In short. The fact sheet could not measure liquidity and asked for it to be measured before any deep dive. NZX's own daily trading data for the 20 sessions from 9 October to 6 November 2026 gives a median of NZ$451 traded on market a day [L1]. The rulebook (section 3) needs at least NZ$12,500 on NZX. The most a position could be under the section 3 liquidity limit (two sessions at 10% of the median) is NZ$90, below the NZ$2,500 smallest NZX order. The case stops here, whatever the business is worth. The three-month average the fact sheet quoted from Investing.com (46,550 shares a day, about NZ$31,000) is lifted by one block: Gould Holdings' 2,044,205 shares for NZ$1,328,733.25 on 8 October, which NZX's data books as an off-market trade [L1][L3].

## Liquidity, measured first
From NZX's activity file for ISIN NZPRPE0001S5 (config/nzx_isins.csv), read on 8 November 2026 [L1]. Arithmetic in python3 -I on that file, with each day's timestamp converted to NZ time:

| Window (to 6 November 2026) | Median on-market value a day | Mean on-market value a day | Sessions at or above NZ$12,500 |
| --- | --- | --- | --- |
| 20 sessions (from 9 October) | NZ$451 | NZ$2,606 | 1 of 20 (20 October, NZ$15,615) |
| 60 sessions | NZ$1,266 | NZ$6,831 | 11 of 60 |
| 120 sessions | NZ$2,381 | NZ$10,582 | 30 of 120 |
| 250 sessions | NZ$1,222 | NZ$8,464 | 50 of 250 |

- There were no off-market trades in the 20 sessions; the 8 October block falls the session before the window starts. The 20 sessions to 8 October, block included, have a median of NZ$692 [L1].
- Two of the 20 sessions had no trades at all (16 and 19 October). Total on-market value over all 20 sessions was NZ$52,124 [L1].
- Median on-market volume over the 20 sessions was 683 shares a day. Since 1 August 2026 (69 sessions) the mean volume including off-market trades is 41,950 shares a day, close to the Investing.com average, but the mean on-market volume is 12,323 and the median on-market volume 2,243 [L1].
- Section 3 limit: 2 x 10% x NZ$451 = NZ$90. A position reaches the NZ$2,500 smallest NZX order only when the 20-session median is NZ$12,500 (2 x 10% x NZ$12,500 = NZ$2,500), so the floor and the position limit agree.

Why it is so thin, from the filings: the Brankin Family Interest Trust is still the registered holder of 22,535,796 shares (41.57%) until its sale of 7,000,000 to Gould settles on 1 April 2027 [L4], and Gould owns 2,044,205 more (3.77%) [L3]. Those two hold 45.3% of the shares between them, and the fact sheet records Asset Management Limited with a further 9.48% at 31 March 2026 (not re-checked).

## What would reopen it
- The half-year result (due mid-November 2026; no date announced on NZX by 8 November [L5]) can't reopen the case by itself, because the case fails on trading, not on value. News can lift trading for a day or two (the day after the selldown announcement, 7 October, traded NZ$14,384 on market), but over the last 250 sessions only one in five reached NZ$12,500, and the median needs about half of a 20-session window to.
- It reopens only when NZX's own 20-session median on-market value is at least NZ$12,500 a day. The weekly research ranking can test that on the same NZX file.
- Two things could change trading for good, both after the half-year: the warrants (27,947,900 at 50c, expiring 24 March 2027) and the Brankin to Gould settlement on 1 April 2027. Neither obviously helps: the fact sheet records most of the warrants with Gould (21.48%) and Asset Management (32.22%), so new shares from exercise would mostly go to holders who already hold blocks (not re-checked).
- Gould's build-up (16.69% of the shares counting the Brankin agreement, plus warrants [L3]) stays a lead for the special situations watch list. Any approach or bid would be assessed under the deal or special situation rules, and the same section 3 liquidity limit applies to those positions.

If it does reopen, the deep dive should start from these tests, none of which was done here:
1. The "our way" anchor is the company's own NTA, NZ$0.885 a share fully diluted, which rests on investment property revalued up NZ$11.7m in FY26 and includes a NZ$2.4m deferred tax add-back (fact sheet, not re-checked). It needs the measure the market actually uses for NZ aged care and village operators, checked against named listed peers, before it can be a middling case.
2. The "against" anchor (NZ$0.652 at 10 times run-rate EBITDAF) is now 1.1% above the NZ$0.645 price. It takes FY27 guidance plus the Chatswood midpoint as run rate and counts the warrant money as certain; the half-year result and its updated guidance are the first test of the run rate, and operating free cash flow (the new dividend base) the test of cash earnings.

## Corrections to the fact sheet
1. Liquidity: measured at NZ$451 a day (20-session median, on market, NZX's own data), not "not measured". The fact sheet's guess that the median may be below NZ$12,500 was right by a wide margin [L1].
2. Gould's 2,044,205 shares on 8 October: the Gould notice says "on-market trades" for NZ$1,328,733.25 [L3], but NZX's data records that exact number of shares and value as an off-market trade on 8 October, with only 20,556 shares traded through the market that day [L1]. It was one negotiated block, as the fact sheet suspected, and says nothing about the depth of the order book.
3. Price: NZ$0.645 on 6 November 2026, not NZ$0.67 (30 October) [L1][L2]. At NZ$0.645 the fact sheet's anchors are +37.2% (NZ$0.885) and +1.1% (NZ$0.652). Arithmetic only; neither anchor was tested.
4. Share counts: the "our way" anchor divides by 81.1m shares (the 31 March shares plus the 31 March warrants), while the "against" anchor uses 82.2m (current). On current counts (54,218,650 shares and 27,947,900 warrants, with the 1,489,100 shares issued since March at 50c), the NTA anchor is about NZ$0.880, not NZ$0.885. Arithmetic on the fact sheet's figures, which were not re-checked.
5. For later work: NZX's announcement list for Promisia is under the company code SVY (from its Savoy Equities name), at api.nzx.com/public/company/SVY000000/announcements/2026/all.json; PHL000000 returns "access denied" [L5].

## What I couldn't verify
- The business itself: no financial statements were read, because the liquidity test ended the work first. Every number above from the fact sheet is marked as not re-checked.
- The exact date of the half-year result: none had been announced on NZX by 8 November 2026 [L5].
- The current bid and offer: not read.

## Checks
- Not on Cam's excluded list: config/judgement_excluded.csv has no entry for Promisia.
- Placement-pattern reopening in the last 30 sessions (rulebook section 9): not checked, as the case stopped at liquidity. The only share issues since 1 October are the Chatswood shares at 50c and warrant exercises at 50c (fact sheet; capital change notice of 14 October [L5]).
- Liquidity: fails. Median NZ$451 a day on market over 20 sessions to 6 November 2026 against NZ$12,500; the most the position could be under section 3 is NZ$90, below the NZ$2,500 smallest order [L1].

## Sources
- [L1] NZX daily trading activity for NZPRPE0001S5 (Promisia Healthcare ordinary shares), two years to 6 November 2026, read 8 November 2026: https://api.nzx.com/public/instrument/NZPRPE0001S5/metrics/activity/past/2Y.json
- [L2] Closing prices, FinFeedAPI: data/prices/NZX/PHL.csv (close NZ$0.645 on 6 November 2026)
- [L3] Gould Holdings substantial holder notice, 9 October 2026 (event 8 October): https://www.nzx.com/announcements/481431 ; PDF https://api.nzx.com/public/announcement/481431/attachment/478852/481431-478852.pdf
- [L4] Brankin Family Interest Trust substantial holder notice, 6 October 2026 (event 5 October): https://www.nzx.com/announcements/481193 ; PDF https://api.nzx.com/public/announcement/481193/attachment/478558/481193-478558.pdf
- [L5] Promisia's 2026 NZX announcement list, read 8 November 2026 (latest item: Gould notice of 30 October 2026): https://api.nzx.com/public/company/SVY000000/announcements/2026/all.json
- Fact sheet: research/facts/NZ_PHL.md (2 November 2026), used as leads only
- config/nzx_isins.csv (ISIN), config/judgement_excluded.csv (excluded list), RULEBOOK.md sections 3 and 5a
