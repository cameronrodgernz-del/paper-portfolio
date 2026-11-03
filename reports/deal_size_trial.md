# Deal size trial

Run 2026-11-03. A forward test registered on 1 Nov 2026 (rulebook section 5, "Deal size trial"): every live ASX and NZX deal that passes section 5's entry rule, applied mechanically at the base rate, held in two separate trial books at A$10,000 and A$3,000 a position with the engine's fills and costs. Outside the ledger: nothing here changes the portfolio.

| Book | Positions | Money laid out (NZ$) | Gain after costs (NZ$) | Over cash (NZ$) | Mean per position, over cash |
| --- | --- | --- | --- | --- | --- |
| large (A$10,000) | 6 | 69,091 | -861 | -861 | -1.43% |
| small (A$3,000) | 6 | 22,697 | -446 | -446 | -1.97% |

Book totals are in NZ$ at tonight's exchange rate; each position's own amounts are in its currency. Open positions are marked at tonight's close less half the spread and brokerage.

| Deal | Entered | Market's chance / base rate at entry | State | Large book | Small book |
| --- | --- | --- | --- | --- | --- |
| BET (AU-2026-16) | 2026-11-02 | 76% / 88% | order waiting | 4,833 AUD, -3.39% (marked) | 3,005 AUD, -3.72% (marked) |
| AUC (AU-2026-18) | 2026-11-02 | 73% / 86% | held | 10,366 AUD, -1.43% (marked) | 3,118 AUD, -2.03% (marked) |
| RWC (AU-2026-21) | 2026-11-02 | 71% / 87% | held | 10,224 AUD, +0.36% (marked) | 3,074 AUD, -0.31% (marked) |
| MEI (AU-2026-22) | 2026-11-02 | 62% / 96% | held | 10,136 AUD, -0.23% (marked) | 3,049 AUD, -0.85% (marked) |
| A11 (AU-2026-25) | 2026-11-02 | 47% / 97% | held | 10,173 AUD, -2.59% (marked) | 3,053 AUD, -2.95% (marked) |
| GL1 (AU-2026-27) | 2026-11-02 | 50% / 83% | held | 9,969 AUD, -1.32% (marked) | 2,998 AUD, -1.95% (marked) |

Live deals not entered (latest reason):

- AX1 (AU-2026-13): no break price or base rate
- VAU (AU-2026-14): expected -2.18% after costs, cash +0.30%
- OML (AU-2026-17): expected -0.34% after costs, cash +0.48%
- SDF (AU-2026-19): expected -1.69% after costs, cash +0.63%
- PPC (AU-2026-20): price outside the range from the break price to the offer
- CWY (AU-2026-23): expected -1.52% after costs, cash +1.92%
- FPR (AU-2026-24): expected -0.54% after costs, cash +1.92%
- RTH (AU-2026-26): expected -1.53% after costs, cash +1.28%

Scored on 2027-07-02 over every position entered by 2027-03-31: pass needs the large book's total gain after costs above cash, and its mean per position above zero. The small book is the comparison.
