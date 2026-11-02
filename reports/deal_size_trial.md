# Deal size trial

Run 2026-11-02. A forward test registered on 1 Nov 2026 (rulebook section 5, "Deal size trial"): every live ASX and NZX deal that passes section 5's entry rule, applied mechanically at the base rate, held in two separate trial books at A$10,000 and A$3,000 a position with the engine's fills and costs. Outside the ledger: nothing here changes the portfolio.

| Book | Positions | Money laid out (NZ$) | Gain after costs (NZ$) | Over cash (NZ$) | Mean per position, over cash |
| --- | --- | --- | --- | --- | --- |
| large (A$10,000) | 0 | 0 | +0 | +0 |  |
| small (A$3,000) | 0 | 0 | +0 | +0 |  |

Book totals are in NZ$ at tonight's exchange rate; each position's own amounts are in its currency. Open positions are marked at tonight's close less half the spread and brokerage.

| Deal | Entered | Market's chance / base rate at entry | State | Large book | Small book |
| --- | --- | --- | --- | --- | --- |
| BET (AU-2026-16) | 2026-11-02 | 76% / 88% | order waiting |  |  |
| AUC (AU-2026-18) | 2026-11-02 | 73% / 86% | order waiting |  |  |
| RWC (AU-2026-21) | 2026-11-02 | 71% / 87% | order waiting |  |  |
| MEI (AU-2026-22) | 2026-11-02 | 62% / 96% | order waiting |  |  |
| A11 (AU-2026-25) | 2026-11-02 | 47% / 97% | order waiting |  |  |
| GL1 (AU-2026-27) | 2026-11-02 | 50% / 83% | order waiting |  |  |

Live deals not entered (latest reason):

- AX1 (AU-2026-13): no break price or base rate
- VAU (AU-2026-14): expected -1.55% after costs, cash +0.30%
- OML (AU-2026-17): expected -2.67% after costs, cash +0.48%
- SDF (AU-2026-19): expected -1.53% after costs, cash +0.63%
- PPC (AU-2026-20): price outside the range from the break price to the offer
- CWY (AU-2026-23): expected -1.54% after costs, cash +1.88%
- FPR (AU-2026-24): expected -1.33% after costs, cash +1.88%
- RTH (AU-2026-26): expected -2.04% after costs, cash +1.26%

Scored on 2027-07-02 over every position entered by 2027-03-31: pass needs the large book's total gain after costs above cash, and its mean per position above zero. The small book is the comparison.
