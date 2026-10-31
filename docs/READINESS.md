# Readiness review, 18 December 2026

What has to be true before the counted run starts on 4 January 2027, and where each item stands.
The practice run was brought forward to start on 2 November 2026, at Cam's request. Updated 1 November 2026.

| # | Item | Status | Notes |
|---|---|---|---|
| 1 | Nightly prices land for every name, five weekdays running, with no failures | To come | Run by hand on 1 November; first scheduled run Monday 2 November, 8:30pm NZ |
| 2 | A price feed for NZX-only shares | Done | FinFeedAPI (usage credits): 162 NZX shares nightly, history from July 2023; no volumes, so NZX has its own rules (rulebook section 7). To do: fill config/nzx_top20.csv from a published list |
| 3 | VT, VAS and ENZL confirmed on Sharesies | Done | Confirmed by Cam on 1 Nov against our closes for 30 Oct: VT (NYSE) US$155.24 against US$155.33; VAS (ASX) A$110.03, the same; ENZL (Nasdaq) US$44.81, the same |
| 4 | Engine checks pass | Done | 9 suites in every nightly job |
| 5 | Independent review of the engine code | Done | Two reviews: 20 findings, then 13 in the fixes; all fixed (docs/reviews/engine_review_2026-11-01.md) |
| 6 | Deal database and base rates | Done, provisional | 347 rows after one follow-up pass; 81% of 320 resolved deals completed, median 119 days; open items in deals/au_hist/followup/OPEN_ITEMS.md |
| 7 | Live deal monitor | Done | Runs nightly; the evening desk keeps the terms current |
| 8 | History test: rules-only | Done: failed | Sleeve dropped, its 10% to cash |
| 9 | History test: US director and officer buying clusters (9a) | Running | Prices fetched hourly within free limits; result once all 336 are in |
| 10 | History test: US cash deal spreads (9b) | To come | US deals are watched but not traded until it passes (rulebook section 5) |
| 11 | Hedging, passive comparisons, monthly report | Done | Tested on October prices |
| 12 | Evening desk as a scheduled task | Switching on 1 November | Prompt in docs/DESK_TASK.md |
| 13 | Nightly copy to Google Drive | Needs a 5-minute setup | docs/DRIVE_BACKUP.md |
| 14 | Build dashboard | Done | claude.ai/artifact/1BxrCHRc4NQFynLysHdFvz |
| 15 | Practice ledger active | Done | `"active": "practice"` in config/run.json from 1 November; the ledger starts 2 November |
| 16 | Practice run: six weeks live with every problem found fixed | Running | 2 November to 18 December |
| 17 | Rulebook signed off by Cam and the counted ledger set active | On 31 December | `"active": "counted"` in config/run.json |
