# Deal size trial

Run 2026-11-16. A forward test registered on 1 Nov 2026 (rulebook section 5, "Deal size trial"): every live ASX and NZX deal that passes section 5's entry rule, applied mechanically at the base rate, held in two separate trial books at A$10,000 and A$3,000 a position with the engine's fills and costs. Outside the ledger: nothing here changes the portfolio.

| Book | Positions | Money laid out (NZ$) | Gain after costs (NZ$) | Over cash (NZ$) | Mean per position, over cash |
| --- | --- | --- | --- | --- | --- |
| large (A$10,000) | 6 | 74,455 | +390 | +266 | +0.29% |
| small (A$3,000) | 6 | 22,401 | -28 | -66 | -0.35% |

Book totals are in NZ$ at tonight's exchange rate; each position's own amounts are in its currency. Open positions are marked at tonight's close less half the spread and brokerage.

| Deal | Entered | Market's chance / base rate at entry | State | Large book | Small book |
| --- | --- | --- | --- | --- | --- |
| BET (AU-2026-16) | 2026-11-02 | 76% / 88% | held | 9,952 AUD, -5.12% (marked) | 3,005 AUD, -6.09% (marked) |
| AUC (AU-2026-18) | 2026-11-02 | 73% / 86% | held | 10,366 AUD, +9.31% (marked) | 3,118 AUD, +8.68% (marked) |
| RWC (AU-2026-21) | 2026-11-02 | 71% / 87% | held | 10,224 AUD, +1.47% (marked) | 3,074 AUD, +0.80% (marked) |
| MEI (AU-2026-22) | 2026-11-02 | 62% / 96% | held | 10,136 AUD, -0.32% (marked) | 3,049 AUD, -0.94% (marked) |
| A11 (AU-2026-25) | 2026-11-02 | 47% / 97% | held | 10,173 AUD, +0.29% (marked) | 3,053 AUD, -0.07% (marked) |
| GL1 (AU-2026-27) | 2026-11-02 | 50% / 83% | held | 9,969 AUD, -3.88% (marked) | 2,998 AUD, -4.50% (marked) |

Live deals not entered (latest reason):

- AX1 (AU-2026-13): no break price or base rate
- VAU (AU-2026-14): price outside the range from the break price to the offer
- OML (AU-2026-17): expected -0.32% after costs, cash +0.31%
- SDF (AU-2026-19): expected -1.16% after costs, cash +0.46%
- PPC (AU-2026-20): price outside the range from the break price to the offer
- CWY (AU-2026-23): expected -1.54% after costs, cash +1.75%
- FPR (AU-2026-24): expected +1.07% after costs, cash +1.75%
- RTH (AU-2026-26): expected -4.82% after costs, cash +1.11%
- BRI (AU-2026-28): expected -2.52% after costs, cash +1.32%

Scored on 2027-07-02 over every position entered by 2027-03-31: pass needs the large book's total gain after costs above cash, and its mean per position above zero. The small book is the comparison.
