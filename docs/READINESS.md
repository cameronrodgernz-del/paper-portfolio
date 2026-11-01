# Readiness review, 18 December 2026

What has to be true before the counted run starts on 4 January 2027, and where each item stands.
The practice run was brought forward to start on 2 November 2026, at Cam's request. Updated 1 November 2026.

| # | Item | Status | Notes |
|---|---|---|---|
| 1 | Nightly prices land for every name, five weekdays running, with no failures | To come | Run by hand on 1 November; first scheduled run Monday 2 November, 8:30pm NZ |
| 2 | A price feed for NZX-only shares | Done | FinFeedAPI (usage credits): 162 NZX shares nightly, history from July 2023; dates corrected on 1 Nov (the feed labels each session a day early); no volumes, so NZX has its own rules (rulebook section 7). The 20 largest (config/nzx_top20.csv) are from interest.co.nz's NZX 50 table, as at 30 October 2026 |
| 3 | VT, VAS and ENZL confirmed on Sharesies | Done | Confirmed by Cam on 1 Nov against our closes for 30 Oct: VT (NYSE) US$155.24 against US$155.33; VAS (ASX) A$110.03, the same; ENZL (Nasdaq) US$44.81, the same |
| 4 | Engine checks pass | Done | 10 suites in every nightly job |
| 5 | Independent review of the engine code | Done | Two reviews: 20 findings, then 13 in the fixes; all fixed (docs/reviews/engine_review_2026-11-01.md) |
| 6 | Deal database and base rates | Done, provisional | 347 rows after one follow-up pass; 81% of 320 resolved deals completed, median 119 days; open items in deals/au_hist/followup/OPEN_ITEMS.md |
| 7 | Live deal monitor | Done | Runs nightly; the evening desk keeps the terms current |
| 8 | History test: rules-only | Done: failed | Sleeve dropped, its 10% to cash |
| 9 | History test: US director and officer buying clusters (9a) | Done: failed | -2.62% a trade against the S&P 500 after costs, 420 events from 2020, t -2.47. Not traded; the special situations weight sits in cash until a type passes |
| 10 | History test: US cash deal spreads (9b) | To come | Prices fetched hourly from 1 November; US deals are watched but not traded until it passes (rulebook section 5) |
| 10a | History test: ASX cash deal spreads (9c) | Done: failed | -0.61% a deal against cash after costs, 108 deals from 2015, t -0.49. ASX cash deals are not traded; ASX scrip and NZX deals carry on |
| 10b | History test: shares left behind when a deal fails (9d) | Done: failed | +3.07% a deal against the market after costs but median -2.96%, 22 events from 2016, t 0.46. Not traded |
| 10c | History test: a model of the next takeover target (9e) | Done: failed | -3.09% a quarter against the market after costs, 30 quarters from 2019, t -2.01. Its picks were bid 3.7 times as often as the market but lost more than the bids made. Not traded |
| 10d | History test: the June tax-year sell-off (9f) | Done: failed | Ahead of small shares in 4 of 9 years from 2018; the +2.96% yearly mean came from two years. Not traded |
| 10e | History test: placement flippers (9g) | Done: failed | -3.20% a trade against small shares after costs, 531 events from 2018, t -4.89. Shares keep lagging after a raising |
| 10f | History test: listed options below their value (9h) | Done: failed | Only 11 events in tradable shares, and they lost money |
| 10g | History test: short sellers covering (9i) | Done: failed | -1.17% a month against shorted shares after costs, 104 months from 2018, t -2.24 |
| 10h | History test: franked special dividends in schemes (9j) | Done: failed | Selling before the ex-date did worse in 36 of 42 schemes; prices fell by about the cash dividend |
| 11 | Hedging, passive comparisons, monthly report | Done | Tested on October prices |
| 12 | Evening desk as a scheduled task | Done | Switched on 1 November: weekdays 9:45pm NZ, first run Monday 2 November (docs/DESK_TASK.md) |
| 13 | Nightly copy to Google Drive | Needs a 5-minute setup | docs/DRIVE_BACKUP.md |
| 14 | Build dashboard | Done | claude.ai/artifact/1BxrCHRc4NQFynLysHdFvz |
| 15 | Practice ledger active | Done | `"active": "practice"` in config/run.json from 1 November; the ledger starts 2 November |
| 16 | Practice run: six weeks live with every problem found fixed | Running | 2 November to 18 December |
| 17 | Rulebook signed off by Cam and the counted ledger set active | On 31 December | `"active": "counted"` in config/run.json |
