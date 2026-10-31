# Deal odds: starting chances by stage, as a holder sees them

From 319 resolved deals in the database (majority-holder buy-outs left out). Made 2026-11-01.

- Completed with the first bidder: 81%. Holders paid at least the offer, counting rival bids that completed at the same or a higher price: 87%.
- A rival bid that wins is a win for a holder, so the second figure is the one the engine starts from.

## By stage reached

Only failures after the stage count against it. A failed deal with no booklet date is counted against the booklet stage if it failed later than a quarter of completed deals had their booklet out, which keeps that rate cautious. Meetings and court hearings are recorded for every failed deal that reached them, so those stages use dated deals only. Rates are smoothed so none reads as certain (paid plus a half, over deals plus one).

| Structure | Stage reached | Deals | Paid | Rate used | Dated deals only | Undated failures |
| --- | --- | --- | --- | --- | --- | --- |
| scheme | announced | 232 | 210 | 90% | 91% of 232 | 0 |
| scheme | booklet or target's statement out | 222 | 200 | 90% | 95% of 210 | 12 |
| scheme | holders voted for it | 201 | 199 | 99% | 99% of 201 | 0 |
| scheme | court approved or unconditional | 199 | 199 | 100% | 100% of 199 | 0 |
| full takeover | announced | 79 | 62 | 78% | 78% of 79 | 0 |
| full takeover | booklet or target's statement out | 72 | 56 | 77% | 85% of 66 | 6 |
| full takeover | court approved or unconditional | 55 | 55 | 99% | 100% of 55 | 0 |
| all | announced | 319 | 277 | 87% | 87% of 319 | 0 |
| all | booklet or target's statement out | 302 | 261 | 86% | 92% of 284 | 18 |
| all | holders voted for it | 201 | 199 | 99% | 99% of 201 | 0 |
| all | court approved or unconditional | 259 | 259 | 100% | 100% of 259 | 0 |

## Days to payment, completed deals

| From | Median | Middle half | Deals |
| --- | --- | --- | --- |
| scheme, announced | 125 | 107 to 155 | 179 |
| scheme, booklet or target's statement out | 59 | 53 to 69 | 139 |
| scheme, holders voted for it | 20 | 16 to 24 | 170 |
| scheme, court approved or unconditional | 14 | 11 to 16 | 168 |
| scheme, announced, needing ACCC | 156 | 128 to 179 | 32 |
| scheme, announced, needing FIRB | 126 | 105 to 157 | 71 |
| scheme, announced, needing OIO | 135 | 121 to 159 | 29 |
| scheme, announced, needing overseas | 147 | 109 to 163 | 31 |
| scheme, announced, needing no approvals | 108 | 91 to 130 | 8 |
| full takeover, announced | 84 | 60 to 123 | 45 |
| full takeover, booklet or target's statement out | 53 | 39 to 94 | 31 |
| full takeover, announced, needing OIO | 123 | 105 to 133 | 5 |
| full takeover, announced, needing no approvals | 65 | 49 to 84 | 11 |

## Deal features

A penalised logistic model on 18 features (bidder type, approvals needed, board support, lock-ups, bidder's stake, premium, market, size), tested by five-fold cross-validation on 319 deals. Brier score (lower is better): model 0.0998, structure rate alone 0.1117. Result: scores better out of sample than the structure rate, so the engine adjusts the stage rate by it.

| Feature | Weight (log-odds) |
| --- | --- |
| board not for | -2.12 |
| nzx | -1.15 |
| lockups 15 | +0.81 |
| oio | +0.77 |
| accc | -0.75 |
| premium 40 | +0.56 |
| consortium | -0.52 |
| small | -0.45 |
| private equity | -0.35 |
| overseas | +0.30 |
| partial | -0.28 |
| takeover | -0.24 |
| infrastructure | -0.23 |
| scrip or mixed | -0.21 |
| stake 20 | +0.15 |
| board for | -0.12 |
| firb | -0.04 |
| existing holder | +0.03 |
