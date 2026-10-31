# Readiness review, 4 December 2026

What has to be true before the practice run starts on 7 December, and where each item stands.
Updated 1 November 2026.

| # | Item | Status | Notes |
|---|---|---|---|
| 1 | Nightly prices land for every name, five weekdays running, with no failures | To come | First scheduled run Monday 2 November, 8:30pm NZ |
| 2 | A price feed for NZX-only shares | Open | No free feed found. Options: FinFeedAPI credits, NZX's market activity report, Twelve Data's paid plan. Until then NZ exposure is ENZL and NZ companies' ASX lines |
| 3 | VT, VAS and ENZL confirmed on Sharesies | Open | A one-minute check in the Sharesies app |
| 4 | Engine checks pass | Done | 7 suites in every nightly job |
| 5 | Independent review of the engine code | In progress | A separate reviewer, not the builder |
| 6 | Deal database and base rates | Done, provisional | 314 rows before the follow-up pass; follow-up fills outcomes, prices and missing deals |
| 7 | Live deal monitor | Done | Runs nightly; terms need the evening desk to stay current |
| 8 | History test: rules-only | Done: failed | Sleeve dropped, its 10% to cash |
| 9 | History test: US director and officer buying clusters (9a) | Running | Prices fetched hourly within free limits; result once all 336 are in |
| 10 | History test: US cash deal spreads (9b) | To come | Prices 1 to 4 December on that month's free allowance |
| 11 | Hedging, passive comparisons, monthly report | Done | Tested on October prices |
| 12 | Evening desk as a scheduled task | Ready to switch on | Prompt in docs/DESK_TASK.md |
| 13 | Nightly copy to Google Drive | Needs a 5-minute setup | docs/DRIVE_BACKUP.md |
| 14 | Build dashboard | Done | claude.ai/artifact/1BxrCHRc4NQFynLysHdFvz |
| 15 | Set the practice ledger active | On 6 December | `"active": "practice"` in config/run.json |
