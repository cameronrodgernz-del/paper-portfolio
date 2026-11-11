# Deal size trial

Run 2026-11-11. A forward test registered on 1 Nov 2026 (rulebook section 5, "Deal size trial"): every live ASX and NZX deal that passes section 5's entry rule, applied mechanically at the base rate, held in two separate trial books at A$10,000 and A$3,000 a position with the engine's fills and costs. Outside the ledger: nothing here changes the portfolio.

| Book | Positions | Money laid out (NZ$) | Gain after costs (NZ$) | Over cash (NZ$) | Mean per position, over cash |
| --- | --- | --- | --- | --- | --- |
| large (A$10,000) | 6 | 74,541 | +1,899 | +1,823 | +2.38% |
| small (A$3,000) | 6 | 22,426 | +424 | +401 | +1.73% |

Book totals are in NZ$ at tonight's exchange rate; each position's own amounts are in its currency. Open positions are marked at tonight's close less half the spread and brokerage.

| Deal | Entered | Market's chance / base rate at entry | State | Large book | Small book |
| --- | --- | --- | --- | --- | --- |
| BET (AU-2026-16) | 2026-11-02 | 76% / 88% | held | 9,952 AUD, -2.78% (marked) | 3,005 AUD, -3.76% (marked) |
| AUC (AU-2026-18) | 2026-11-02 | 73% / 86% | held | 10,366 AUD, +12.70% (marked) | 3,118 AUD, +12.06% (marked) |
| RWC (AU-2026-21) | 2026-11-02 | 71% / 87% | held | 10,224 AUD, +2.41% (marked) | 3,074 AUD, +1.74% (marked) |
| MEI (AU-2026-22) | 2026-11-02 | 62% / 96% | held | 10,136 AUD, +4.18% (marked) | 3,049 AUD, +3.54% (marked) |
| A11 (AU-2026-25) | 2026-11-02 | 47% / 97% | held | 10,173 AUD, -1.17% (marked) | 3,053 AUD, -1.53% (marked) |
| GL1 (AU-2026-27) | 2026-11-02 | 50% / 83% | held | 9,969 AUD, -1.05% (marked) | 2,998 AUD, -1.68% (marked) |

Live deals not entered (latest reason):

- AX1 (AU-2026-13): no break price or base rate
- VAU (AU-2026-14): expected -3.70% after costs, cash +0.19%
- OML (AU-2026-17): expected -0.31% after costs, cash +0.37%
- SDF (AU-2026-19): expected -1.45% after costs, cash +0.53%
- PPC (AU-2026-20): price outside the range from the break price to the offer
- CWY (AU-2026-23): expected -1.44% after costs, cash +1.81%
- FPR (AU-2026-24): expected +0.12% after costs, cash +1.81%
- RTH (AU-2026-26): expected -4.80% after costs, cash +1.18%

Scored on 2027-07-02 over every position entered by 2027-03-31: pass needs the large book's total gain after costs above cash, and its mean per position above zero. The small book is the comparison.
