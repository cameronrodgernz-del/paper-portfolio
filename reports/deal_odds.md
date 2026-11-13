# Deal odds: starting chances by stage, as a holder sees them

From 320 resolved deals in the database (majority-holder buy-outs left out). Made 2026-11-13.

- Completed with the first bidder: 81%. Holders paid at least the offer, counting rival bids that completed at the same or a higher price: 87%.
- A rival bid that wins is a win for a holder, so the second figure is the one the engine starts from.

## By stage reached

Only failures after the stage count against it. A deal with no booklet date counts at the booklet stage if it ended later than a quarter of completed deals had their booklet out, whether it failed or its holders were paid by a rival, so wins and failures are treated alike; a deal blocked by a regulator with no booklet recorded failed before it. Meetings and court hearings are recorded for every failed deal that reached them, so those stages use dated deals only. Rates are smoothed so none reads as certain (paid plus a half, over deals plus one).

| Structure | Stage reached | Deals | Paid | Rate used | Dated deals only | Undated failures | Undated rival wins |
| --- | --- | --- | --- | --- | --- | --- | --- |
| scheme | announced | 233 | 211 | 90% | 91% of 233 | 0 | 0 |
| scheme | booklet or target's statement out | 226 | 201 | 92% | 95% of 211 | 8 | 7 |
| scheme | holders voted for it | 202 | 200 | 99% | 99% of 202 | 0 | 0 |
| scheme | court approved or unconditional | 200 | 200 | 100% | 100% of 200 | 0 | 0 |
| full takeover | announced | 79 | 62 | 78% | 78% of 79 | 0 | 0 |
| full takeover | booklet or target's statement out | 77 | 56 | 79% | 85% of 66 | 6 | 5 |
| full takeover | court approved or unconditional | 55 | 55 | 99% | 100% of 55 | 0 | 0 |
| all | announced | 320 | 278 | 87% | 87% of 320 | 0 | 0 |
| all | booklet or target's statement out | 311 | 262 | 88% | 92% of 285 | 14 | 12 |
| all | holders voted for it | 202 | 200 | 99% | 99% of 202 | 0 | 0 |
| all | court approved or unconditional | 260 | 260 | 100% | 100% of 260 | 0 | 0 |

## Days to payment, completed deals

| From | Median | Middle half | Deals |
| --- | --- | --- | --- |
| scheme, announced | 125 | 107 to 154 | 185 |
| scheme, booklet or target's statement out | 59 | 53 to 69 | 140 |
| scheme, holders voted for it | 20 | 16 to 24 | 172 |
| scheme, court approved or unconditional | 14 | 11 to 16 | 169 |
| scheme, announced, needing ACCC | 155 | 126 to 178 | 34 |
| scheme, announced, needing FIRB | 125 | 106 to 155 | 74 |
| scheme, announced, needing OIO | 135 | 120 to 159 | 30 |
| scheme, announced, needing overseas | 147 | 109 to 163 | 31 |
| scheme, announced, needing no approvals | 108 | 91 to 130 | 8 |
| full takeover, announced | 85 | 60 to 133 | 46 |
| full takeover, booklet or target's statement out | 54 | 40 to 105 | 32 |
| full takeover, announced, needing FIRB | 78 | 46 to 137 | 5 |
| full takeover, announced, needing OIO | 123 | 105 to 133 | 5 |
| full takeover, announced, needing no approvals | 65 | 49 to 84 | 11 |

## Deal features

A penalised logistic model on 18 features (bidder type, approvals needed, board support, lock-ups, bidder's stake, premium, market, size), tested by five-fold cross-validation on 320 deals. Brier score (lower is better): model 0.0981, structure rate alone 0.1114. Result: scores better out of sample than the structure rate, so the engine adjusts the stage rate by it.

| Feature | Weight (log-odds) |
| --- | --- |
| board not for | -2.12 |
| nzx | -1.16 |
| lockups 15 | +0.80 |
| oio | +0.77 |
| accc | -0.73 |
| premium 40 | +0.59 |
| consortium | -0.52 |
| small | -0.44 |
| private equity | -0.36 |
| overseas | +0.30 |
| partial | -0.28 |
| takeover | -0.24 |
| infrastructure | -0.23 |
| scrip or mixed | -0.20 |
| stake 20 | +0.15 |
| board for | -0.12 |
| firb | -0.05 |
| existing holder | +0.02 |
