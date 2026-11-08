# Listed fund discount screen, 8 November 2026

A first look at the listed investment companies and trusts on the research screen (ASX and NZX) that trade below the value of what they own, to see which have a dated event that could close the gap. This is for the simulated NZ$100,000 paper portfolio only. It is not financial advice. The research funnel drops funds at its first gate today (src/research_rank.py, "fund, trust or investment company"), so nothing here can be bought. No rule, template or data file was changed.

## The short answer

- **70 funds** on the screen: 57 ASX and 13 NZX, after removing 39 index ETFs and four operating companies that the gate's name test catches (Etherstack, Fineos and Structural Monitoring Systems because of "PLC", NZ King Salmon because of "Investments").
- **39 trade at a discount of 10% or more and clear the liquidity floor** (34 ASX, 5 NZX). The Bankers Investment Trust's NZX line is counted on the UK standard measure (debt at fair value, 11.4%); at par debt it is 9.1%.
- **Only one has a firm date attached to a mechanism**: Barramundi (NZX:BRM), whose board must finish a non-renewal decision on Fisher Funds' management agreement by 31 March 2027 and buys back stock whenever the discount is over 6%. Two more have a board commitment on the discount but no date: Pengana International Equities (ASX:PIA, AGM 26 November, new board reviewing discount controls) and RAM Essential Services Property Fund (ASX:REP, UBS appointed, first stage of capital management "shortly").
- **The best event of the last two years has already happened**: PIA bought back 58.6% of its shares at after-tax NTA less 0.15 cents in September 2026, eleven months after Geoff Wilson and a colleague joined its board at the October 2025 AGM and a strategic review began. WAM Strategic Value was a substantial holder throughout. The other full closing event was Diversified United's merger into AUI (proposed January 2026, done in April).
- **View**: the opportunity is real but thin and lumpy, about 1–2 tradable cases a year. I would not change the rule now. Details at the end.

## How the screen was built

1. **Universe.** Every row of reports/research_screen.csv that the fund gate in src/research_rank.py catches: the FUND name pattern, the "Listed investment" group, NZX names with "Units", the NZX_FUNDS set, and ASX names with three or more monthly NTA headlines in six months. That gives 113 securities, the same count research_rank.md shows for the gate. ETFs and index funds were removed, and so were the four operating companies.
2. **NTA.** Read by hand from each fund's own latest NTA announcement (links at the end). Where a fund publishes both, pre-tax and post-tax are shown; the discount uses pre-tax (or the only figure published). Weekly publishers use 30 October; monthly-only publishers mostly still show 30 September because October figures land in mid-November.
3. **Price.** header.priceLast in data/research_data/asx_company.json (the 6 November last trade). Seven ASX trusts are missing from that file (KKC, LED, LRT, MRE, OPH, REP, RF1), so they use the 30 October Norgate close. NZX prices are the 6 November close in data/prices/NZX. Discount = price ÷ NTA − 1.
4. **Like-for-like check.** Because many NTAs are five weeks old, the table also shows the discount on the close of the NTA date itself. October was a heavy month for small-cap resources and technology (WAM Active's NTA fell from 102.6c to 79.9c), so for funds still on a 30 September NTA the 6 November discount overstates the gap. WAM Capital is the clearest case: 21.4% against a stale, cum-dividend NTA, but 6.6% like for like.
5. **NZX lines of foreign funds.** The UK trusts and AFI publish NAV in pence or Australian dollars. These were converted with the RBA's AUD/GBP and AUD/NZD rates for 4 and 6 November (data/fx/rba_f11_1.csv): GBP/NZD 2.406, AUD/NZD 1.2401.
6. **Liquidity.** ASX: median of volume × close over the last 20 sessions in data/norgate/universe/prices_2026.csv.gz (5 to 30 October), floor A$10,000 a day. NZX: median on-market value over the last 20 sessions from NZX's own activity data (api.nzx.com instrument activity, 9 October to 6 November), floor NZ$12,500. NZX refused the request for Booster's two funds (BIF, PLP), so their liquidity is unknown; both trade under a 10% discount anyway.
7. **Catalysts.** For every fund on the short list, all 2025 and 2026 headlines were scanned (asx_company.json for most ASX funds, the ASX announcement search for the seven missing, NZX's announcement feed for NZX), then the documents that mattered were read: strategic reviews, buyback booklets, AGM notices, management agreement notices, substantial holder notices and litigation updates. All November AGM notices for the short list were scanned for wind-up, conversion, spill, requisition and buyback resolutions.

Four NTAs are softer than the rest and are flagged in the table: Metrics' MOT and MRE (NTA cut after audit, underlying funds' valuations and redemptions suspended, a remediation review still running), Clime Capital (auditor qualified A$36.2m of unlisted trusts) and 360 Capital Mortgage REIT (largest borrower group in administration). The three property trusts (REP, LED, VHP) carry half-yearly book values, not market prices.

## Every fund

Liquidity is the median value traded a day. "On short list" means a discount of 10% or more and above the liquidity floor. Catalysts were checked in depth only for the short list and for CD2, TOP and FPC (deep discounts below the floor).

| Market | Code | Fund | Latest NTA | NTA date | Price | Discount | Discount at NTA date | Liquidity (median a day) | On short list | Catalyst |
|---|---|---|---|---|---|---|---|---|---|---|
| ASX | CD3 | CD Private Equity Fund III Units | A$1.54 pre / A$1.50 post | 30 Sep | A$0.77 (6 Nov) | -50.0% (post -48.7%) | -51.6% | A$28.8k | yes | None dated. Self-liquidating private equity fund selling assets over time; sister fund CD2 has just sold four fund interests at about 64% of their reported value |
| ASX | BHD | Benjamin Hornigold Limited | A$0.3292 | 30 Sep | A$0.165 (6 Nov) | -49.9% | -21.0% | A$23.6k | yes | Board says it will consider capital management once a A$1.8m litigation settlement is received (20 Jul 2026); no date. AGM 27 Nov. Price fell from about A$0.26 to A$0.165 after the 30 Sep NTA |
| ASX | CD2 | CD Private Equity Fund II Units | A$0.59 pre / A$0.56 post | 20 Oct | A$0.31 (6 Nov) | -47.5% (post -44.6%) | -50.8% | A$8.0k (below floor) | no | Below the liquidity floor. Partial secondary sale signed (Oct 2026): three interests due to complete about 1 Nov 2026, the fourth in early Jan 2027; Wilson Asset Management held 6.05% in March 2026 |
| ASX | BTI | Bailador Technology Investments Limited | A$1.63 pre / A$1.50 post | 30 Sep | A$0.875 (6 Nov) | -46.3% (post -41.7%) | -47.2% | A$89.4k | yes | None. Pays 4% of pre-tax NTA a year in dividends; dividend plan issues new shares at a 2.5% discount to the share price |
| ASX | TOP | Thorney Opportunities Ltd | A$0.956 pre / A$0.885 post | 30 Sep | A$0.52 (6 Nov) | -45.6% (post -41.2%) | -42.5% | A$6.1k (below floor) | no | Below the liquidity floor. On-market buyback extended to Mar 2027 |
| ASX | LED | LDR Capital Property Fund Units Stapled Securities | A$0.58 | 30 Jun | A$0.33 (30 Oct) | -43.1% | -19.8% | A$19.3k | yes | None dated. New manager LDR Capital (Feb 2026) selling about 28% of the portfolio to cut gearing from 42.6% to 29.3%; Kenxue Pty Ltd built to 9.9% (Oct 2026) |
| ASX | REP | RAM Essential Services Property Fund Units Stapled Securities | A$0.71 | 30 Jun | A$0.43 (30 Oct) | -39.4% | -43.0% | A$89.3k | yes | Board, advised by UBS, assessing capital management and other steps to cut the discount; first stage to be announced 'shortly' (22 Oct 2026). No date |
| ASX | GC1 | Glennon Small Companies Limited | A$0.6293 pre / A$0.6584 post | 5 Nov | A$0.39 (6 Nov) | -38.0% (post -40.8%) | n/a | A$11.5k | yes | None dated. Acorn Capital built to 7.5% (Sep 2026); 2025 spill vote failed; AGM 12 Nov |
| ASX | MRE | Metrics Real Estate Multi-Strategy Fund Units Stapled Securities | A$2.2953 | 30 Sep | A$1.45 (30 Oct) | -36.8% | -26.8% | A$182k | yes | None. Audit cut the NTA; underlying Metrics funds suspended valuations and redemptions (30 Sep); NTA under a remediation review. A risk, not a catalyst |
| ASX | MOT | Metrics Income Opportunities Trust Units | A$1.9324 | 30 Sep | A$1.31 (6 Nov) | -32.2% | -16.2% | A$692k | yes | None. Audit cut 30 Jun NTA by 10% to A$1.93; underlying funds' valuations and redemptions suspended; NTA under a remediation review. A risk, not a catalyst |
| ASX | CIN | Carlton Investments Limited | A$49.03 pre / A$40.30 post | 31 Oct | A$35.00 (6 Nov) | -28.6% (post -13.2%) | -28.6% | A$124k | yes | On-market buyback running. Post-tax discount 13% |
| ASX | ACQ | Acorn Capital Investment Fund Limited | A$1.1106 pre / A$1.1247 post | 30 Sep | A$0.795 (6 Nov) | -28.4% (post -29.3%) | -20.8% | A$61.6k | yes | AGM 19 Nov votes on a new five-year management agreement with Acorn; expert says advantages outweigh. Locks in the manager, not a closing event |
| NZX | VHP | Vital Healthcare Property Trust | NZ$2.41 (NZX data field, not checked against a trust release) | latest reported | NZ$1.805 (6 Nov) | -25.1% | n/a | NZ$491.9k | yes | Management internalised in late 2025 (search results only; NZX's announcement feed refused access for VHP). No new mechanism found |
| ASX | TCF | 360 Capital Mortgage Reit Units | A$5.968 | 30 Sep | A$4.52 (6 Nov) | -24.3% | -20.2% | A$24.6k | yes | Largest borrower group (Bathla) in administration, receivers selling the security; on-market buyback with 4.8% left; off-market buyback postponed (Apr 2026) |
| ASX | CAM | Clime Capital Limited | A$0.81 pre / A$0.835 post | 31 Oct | A$0.625 (6 Nov) | -22.8% (post -25.1%) | -23.5% | A$87.0k | yes | Auditor qualified the A$36.2m value of unlisted unit trusts; independent review of the private debt under way. On-market buyback. A risk, not a catalyst |
| ASX | WAM | WAM Capital Limited | A$1.2146 | 30 Sep | A$0.955 (6 Nov) | -21.4% | -6.6% | A$1,976k | yes | None. NTA is 30 Sep, before the 7.75c dividend (ex 8 Oct); at 30 Sep prices the discount was 6.6% |
| ASX | FPC | Fat Prophets Global Contrarian Fund Ltd | A$1.6524 | 31 Oct | A$1.30 (6 Nov) | -21.3% | -21.9% | A$8.5k (below floor) | no | Below the liquidity floor |
| ASX | PE1 | Pengana Private Equity Trust Units | A$1.8674 | 30 Sep | A$1.47 (6 Nov) | -21.3% | -28.0% | A$386k | yes | On-market buyback; none dated |
| ASX | WMA | WAM Alternative Assets Limited | A$1.1982 | 30 Sep | A$0.96 (6 Nov) | -19.9% | -18.6% | A$92.4k | yes | None. Management agreement extended to Oct 2030 (Oct 2025); new NAV-backed debt facility (Nov 2026) |
| ASX | AMH | Amcil Limited | A$1.06 | 30 Oct | A$0.855 (6 Nov) | -19.3% | -18.4% | A$63.5k | yes | On-market buyback; none dated |
| ASX | WHF | Whitefield Industrials Limited | A$5.98 pre / A$5.35 post | 30 Sep | A$4.86 (6 Nov) | -18.7% (post -9.2%) | -21.1% | A$356k | yes | On-market buyback of up to 10% from 19 Aug 2026 to 18 Aug 2027; management agreement extended to 2031. Post-tax discount 9% |
| ASX | HM1 | Hearts and Minds Investments Limited | A$3.34 pre / A$3.13 post | 30 Oct | A$2.74 (6 Nov) | -18.0% (post -12.5%) | -17.1% | A$414k | yes | Fee change cut the effective cost by about 0.35% a year (from 1 Jul 2026). AGM 19 Nov carries a conditional spill after a 2025 first strike |
| ASX | LRT | Lowell Resources Fund Units | A$2.0816 | 31 Oct | A$1.72 (30 Oct) | -17.4% | -17.4% | A$33.3k | yes | On-market buyback; placement and unit purchase plan Aug to Sep 2026. None dated |
| ASX | RG8 | Regal Asian Investments Limited | A$2.39 post-tax | 30 Oct | A$1.99 (6 Nov) | -16.7% | -15.1% | A$137k | yes | Daily on-market buyback; Regal's Philip King to retire by 30 Jun 2027; AGM 17 Nov. None dated |
| ASX | LSX | Lion Selection Group Limited | A$0.953 pre / A$0.923 post | 31 Oct | A$0.80 (6 Nov) | -16.1% (post -13.3%) | -11.9% | A$67.2k | yes | None |
| ASX | WAR | WAM Strategic Value Limited | A$1.2692 | 30 Sep | A$1.07 (6 Nov) | -15.7% | -10.2% | A$128k | yes | None. NTA is 30 Sep, before a 3.25c dividend; at 30 Sep prices the discount was 10.2% |
| ASX | OPH | Ophir High Conviction Fund Units | A$2.6345 | 30 Oct | A$2.23 (30 Oct) | -15.4% | -15.4% | A$414k | yes | On-market buyback authority for 10% (Jan 2026); none dated |
| ASX | KKC | KKR Credit Income Fund Units | A$2.2956 | 28 Oct | A$1.96 (30 Oct) | -14.6% | -13.3% | A$589k | yes | None |
| ASX | AUI | Australian United Investment Company Limited | A$14.20 | 30 Oct | A$12.22 (6 Nov) | -13.9% | -13.5% | A$931k | yes | Merger with DUI completed Apr 2026; on-market buyback. None now |
| ASX | TGF | Tribeca Global Natural Resources Limited | A$2.59 pre / A$2.44 post | 30 Oct | A$2.24 (6 Nov) | -13.5% (post -8.2%) | -15.8% | A$217k | yes | On-market buyback renewed Sep 2026; none dated |
| ASX | SNC | Sandon Capital Investments Limited | A$0.8112 pre / A$0.8053 post | 30 Sep | A$0.705 (6 Nov) | -13.1% (post -12.5%) | -7.5% | A$12.3k | yes | None. NTA is 30 Sep; at 30 Sep prices the discount was 7.5% |
| ASX | BKI | BKI Investment Company Limited | A$2.07 | 30 Oct | A$1.80 (6 Nov) | -13.0% | -14.0% | A$571k | yes | None |
| ASX | WGB | WAM Global Limited | A$2.1214 | 30 Sep | A$1.85 (6 Nov) | -12.8% | -4.8% | A$655k | yes | None. NTA is 30 Sep, before a 6.6c dividend; at 30 Sep prices the discount was 4.8% |
| NZX | CO2 | Carbon Fund (Salt) | NZ$1.5433 | 5 Nov | NZ$1.36 (6 Nov) | -11.9% | n/a | NZ$12.3k (below floor) | no | Fund buys back its own units most days. No date |
| NZX | KFL | Kingfish | NZ$1.2396 | 4 Nov | NZ$1.095 (6 Nov) | -11.7% | n/a | NZ$179.0k | yes | Buys back stock when the discount exceeds 6% (up to 5% a year). None dated |
| ASX | DJW | Djerriwarrh Investments Limited | A$3.35 | 30 Oct | A$2.96 (6 Nov) | -11.6% | -10.7% | A$593k | yes | On-market buyback; none dated |
| ASX | AIQ | Alternative Investment Trust Units | A$1.554 | 30 Sep | A$1.38 (6 Nov) | -11.2% | -10.6% | A$14.0k | yes | On-market buyback capped at the adjusted NTA (A$1.41); discount to adjusted NTA only 2.4% |
| NZX | BRM | Barramundi | NZ$0.5369 | 4 Nov | NZ$0.478 (6 Nov) | -11.0% | n/a | NZ$66.0k | yes | Replacement management agreement being negotiated (fees, term, performance-linked termination); the non-renewal process must finish by 31 Mar 2027. Buys back stock above a 6% discount |
| ASX | MIR | Mirrabooka Investments Limited | A$2.72 | 30 Oct | A$2.43 (6 Nov) | -10.7% | -15.1% | A$334k | yes | On-market buyback; none dated |
| ASX | PIA | Pengana International Equities Limited | A$1.1849 pre / A$1.1684 post | 31 Oct | A$1.06 (6 Nov) | -10.5% (post -9.3%) | -2.9% | A$61.9k | yes | Equal-access buyback at after-tax NTA less 0.15c completed 30 Sep 2026 (58.6% of shares). New board reviewing 'ongoing discount-management initiatives'; AGM 26 Nov with a conditional spill |
| NZX | FCT | F&C Investment Trust (NZX line) | 367.68p cum income, debt at market (= NZ$8.85) | 4 Nov | NZ$7.92 (6 Nov) | -10.5% | n/a | NZ$1.0k (below floor) | no | Below the liquidity floor; regular buybacks |
| NZX | MLN | Marlin Global | NZ$0.8184 (undiluted) | 3 Nov | NZ$0.735 (6 Nov) | -10.2% | n/a | NZ$61.6k | yes | Buys back stock above a 6% discount; management agreement expires late 2027; warrants exercisable 23 Apr 2027 at about NZ$0.85 (out of the money) |
| ASX | RF1 | Regal Investment Fund Units | A$3.34 | 30 Oct | A$3.00 (30 Oct) | -10.2% | -10.2% | A$650k | yes | On-market buyback; none dated |
| NZX | BIT | Bankers Investment Trust (NZX line) | 156.0p, or 160.0p with debt at fair value (= NZ$3.75 / NZ$3.85) | 4 Nov | NZ$3.41 (6 Nov) | -9.1% (fair-value debt -11.4%) | n/a | NZ$42.8k | yes | Regular buybacks in London; none dated |
| ASX | NAC | Naos Ex-50 Opportunities Company Limited | A$0.66 pre / A$0.73 post | 30 Sep | A$0.60 (6 Nov) | -9.1% (post -17.8%) | -7.6% | A$30.0k | no | Not checked: discount under 10% or premium |
| NZX | AFI | Australian Foundation Investment Co (NZX line) | A$7.92 pre-tax, A$6.62 post-tax, ex dividend (= NZ$9.82 / NZ$8.21) | 31 Oct | NZ$8.975 (6 Nov) | -8.6% (post 9.3%) | n/a | NZ$22.7k | no | Below 10% |
| ASX | RYD | Ryder Capital Limited | A$2.2395 pre / A$2.0175 post | 30 Sep | A$2.05 (6 Nov) | -8.5% (post 1.6%) | -4.4% | A$64.2k | no | Not checked: discount under 10% or premium |
| ASX | RG1 | Regal Partners Global Investments Limited | A$2.66 post-tax | 30 Oct | A$2.45 (6 Nov) | -7.9% | -9.4% | A$392k | no | Not checked: discount under 10% or premium |
| ASX | NCC | Naos Emerging Opportunities Company Limited | A$0.45 pre / A$0.54 post | 30 Sep | A$0.415 (6 Nov) | -7.8% (post -23.1%) | 1.1% | A$32.7k | no | Not checked: discount under 10% or premium |
| NZX | TEM | Templeton Emerging Markets IT (NZX line) | 319.22p cum income (= NZ$7.68) | 4 Nov | NZ$7.15 (6 Nov) | -6.9% | n/a | NZ$19.9k | no | Below 10% |
| ASX | ALI | Argo Global Listed Infrastructure Limited | A$2.67 | 30 Oct | A$2.51 (6 Nov) | -6.0% | -7.5% | A$139k | no | Not checked: discount under 10% or premium |
| ASX | WMI | WAM Microcap Limited | A$1.1795 | 30 Sep | A$1.11 (6 Nov) | -5.9% | 10.2% | A$358k | no | Not checked: discount under 10% or premium |
| NZX | PLP | Private Land and Property Fund (Booster) | NZ$1.2652 unit price | 2 Nov | NZ$1.191 (6 Nov) | -5.9% | n/a | not available (NZX refused) | no | Below 10%; open-ended, units redeemed at the unit price |
| NZX | BIF | Booster Innovation Fund | NZ$1.5078 unit price | 2 Nov | NZ$1.434 (6 Nov) | -4.9% | n/a | not available (NZX refused) | no | Below 10%; open-ended, units issued and redeemed at the unit price |
| ASX | FGG | Future Generation Global Limited | A$1.6055 | 30 Sep | A$1.53 (6 Nov) | -4.7% | 1.5% | A$390k | no | Not checked: discount under 10% or premium |
| ASX | CDM | Cadence Capital Limited | A$0.766 pre / A$0.976 post | 30 Sep | A$0.73 (6 Nov) | -4.7% (post -25.2%) | -0.8% | A$123k | no | Not checked: discount under 10% or premium |
| ASX | WAX | WAM Research Limited | A$0.7716 | 30 Sep | A$0.745 (6 Nov) | -3.4% | 11.5% | A$134k | no | Not checked: discount under 10% or premium |
| ASX | SEC | Spheria Emerging Companies Limited | A$2.236 | 5 Nov | A$2.17 (6 Nov) | -3.0% | n/a | A$85.9k | no | Discount trigger: a vote on converting to an unlisted fund if the average discount over Apr 2025 to Mar 2026 exceeded 5%; it averaged a 0.3% premium, so no vote (9 Apr 2026) |
| ASX | GVF | Staude Capital Global Value Fund Limited | A$1.2915 pre / A$1.2596 post | 30 Sep | A$1.255 (6 Nov) | -2.8% (post -0.4%) | 2.6% | A$119k | no | Not checked: discount under 10% or premium |
| ASX | WQG | WCM Global Growth Limited | A$1.93 pre / A$1.769 post | 30 Oct | A$1.905 (6 Nov) | -1.3% (post 7.7%) | -2.3% | A$478k | no | Not checked: discount under 10% or premium |
| ASX | PCX | Pengana Global Private Credit Trust Units | A$1.9733 | 31 Oct | A$1.955 (6 Nov) | -0.9% | -1.7% | A$235k | no | Not checked: discount under 10% or premium |
| ASX | GCI | Gryphon Capital Income Trust Units | A$2.0062 | 5 Nov | A$1.995 (6 Nov) | -0.6% | n/a | A$1,433k | no | Not checked: discount under 10% or premium |
| ASX | FGX | Future Generation Australia Limited | A$1.3352 | 30 Sep | A$1.365 (6 Nov) | 2.2% | -0.4% | A$309k | no | Not checked: discount under 10% or premium |
| ASX | CDO | Cadence Opportunities Fund Limited | A$2.035 pre / A$2.137 post | 30 Sep | A$2.11 (6 Nov) | 3.7% (post -1.3%) | 11.1% | A$19.7k | no | Not checked: discount under 10% or premium |
| ASX | GLS | L1 Global Long Short Fund Limited | A$1.7815 pre / A$1.8026 post | 30 Oct | A$1.86 (6 Nov) | 4.4% (post 3.2%) | 8.3% | A$3,630k | no | Not checked: discount under 10% or premium |
| NZX | HFL | Henderson Far East Income (NZX line) | 234.8p cum income (= NZ$5.65) | 4 Nov | NZ$5.90 (6 Nov) | 4.4% | n/a | NZ$11.8k (below floor) | no | Premium |
| ASX | WAA | WAM Active Limited | A$0.7993 | 31 Oct | A$0.895 (6 Nov) | 12.0% | 13.8% | A$279k | no | Not checked: discount under 10% or premium |
| ASX | PL8 | Plato Income Maximiser Limited | A$1.134 pre / A$1.127 post | 23 Oct | A$1.39 (6 Nov) | 22.6% (post 23.3%) | 19.9% | A$646k | no | Not checked: discount under 10% or premium |
| ASX | NSC | Naos Small Cap Opportunities Company Limited | A$0.24 pre / A$0.33 post | 30 Sep | A$0.30 (6 Nov) | 25.0% (post -9.1%) | 27.1% | A$15.9k | no | Not checked: discount under 10% or premium |
| NZX | FSF | Fonterra Shareholders' Fund | no NTA: units carry the economic rights of Fonterra shares | n/a | NZ$9.23 (6 Nov) | n/a | n/a | NZ$679.2k | no | Not a discount-to-NTA fund |

## Fees, cash and debt for the short list

Taken from the funds' own monthly reports, results and annual reports. "Not in the documents read" means the fee or balance sheet line was not in the NTA notices and monthly reports downloaded for this screen; it is not a statement that there is none.

| Code | Manager's fee | Cash and debt |
|---|---|---|
| CD3 | Not in the documents read | No borrowings mentioned |
| BHD | Not in the documents read (former manager John Bridgeman was paid a A$4.55m performance fee in advance in earlier years) | Cash A$3.78m at 30 Jun 2026 |
| BTI | Not in the documents read | Cash A$12.5m (8c a share) at 30 Sep |
| LED | LDR Capital's fees are A$1.9m a year (37%) lower than Elanor's | Gearing 42.6% at 30 Jun, 29.3% pro forma after contracted sales |
| REP | 0.65% a year of gross assets up to A$1.5b | Gearing 43.5% at 30 Jun, 16.8% pro forma after the retail sale settled 22 Oct |
| GC1 | Not in the documents read | Has a convertible loan agreement (extended Dec 2025) |
| MRE, MOT | Not in the documents read | No fund-level debt mentioned; MOT's look-through book is 66% loans |
| CIN | Running costs 0.08% of average assets | No borrowings |
| ACQ | 0.95% a year plus 20% of outperformance of the Small Ordinaries (new agreement keeps both) | No debt mentioned |
| VHP | Internalised (no external manager) | Not checked (NZX feed refused) |
| TCF | Target return is RBA cash rate plus 4% after fees | Cash A$5.9m at 29 Sep; never borrowed |
| CAM | Not in the documents read | Convertible notes (CAMG, 6.5% a year) on issue |
| WAM, WAR, WGB, WMA | Not in the documents read | WAR holds 41.5% cash; WMA is drawing A$10m on a new NAV-backed facility |
| PE1 | Not in the documents read | Cash 1% |
| AMH | Management cost 0.57% | Cash 2.8% |
| WHF | Not in the documents read | Cash 1.5% |
| HM1 | No management fee; gives 1.5% of NTA a year to medical research, which from 1 Jul 2026 also covers all other costs | Cash 8% |
| LRT | Not in the documents read | Cash 14.3% |
| RG8 | Not in the documents read | Not in the documents read |
| LSX | Not in the documents read | Cash A$28.1m of A$136.6m total assets |
| OPH | 1.20% a year plus 20% of outperformance | Not in the documents read |
| KKC | 0.88% a year of NTA (plus GST) | Not in the documents read |
| AUI | Costs 0.09% of assets | A$57m drawn of a A$225m facility; cash A$39m; portfolio A$3,078m |
| TGF | Not in the documents read | Not in the documents read |
| SNC | Not in the documents read | 8.5% notes (SNCHA) on issue, restructured Jun 2026 |
| BKI | Not in the documents read | Cash A$55m; no debt |
| KFL, BRM, MLN | 1.25% a year of gross assets, reduced if the manager underperforms, plus a performance fee (Kingfish: 10% of returns above the 90-day bank bill plus 7%, with a high-water mark) | No debt; cash NZ$7.0m (KFL), NZ$3.4m (BRM), NZ$5.3m (MLN) at the last balance date |
| DJW | Management cost 0.41% | Cash 0.4% |
| AIQ | 1.5% a year plus GST, performance fee above an 8% hurdle | Net cash A$3.8m |
| MIR | Management cost 0.52% | Cash 2.5% |
| PIA | 1.23% a year plus 15.38% performance fee (September report; may change with Antipodes) | 106.9m shares left after the buyback |
| RF1 | 1.5% a year plus 20% above the RBA cash rate | Not in the documents read |
| BIT | Not in the documents read | Has sterling and euro loan notes (NAV shown with debt at par and at fair value) |

## The strongest cases

### 1. Barramundi (NZX:BRM): a management agreement with a deadline

**Mechanism.** Barramundi's agreement with Fisher Funds dates from its 2006 listing and its five-year term came up on 25 October 2026. The board of independent directors is negotiating a replacement with independent advice on "fees, the term of any new agreement, expectations of performance and termination rights related to performance". Fisher Funds has waived its right to have the non-renewal process finished by 25 October, provided it is finished by **31 March 2027**; meanwhile the manager follows a tighter mandate the board specified (tracking error of no more than 8%). Separately, the board buys back stock whenever the discount is over 6% to its fair value adjusted NAV: 2.6 million shares in the September quarter and 1.0 million in October, with daily notices continuing into November.

**Date.** 31 March 2027 at the latest for the agreement. The buyback runs now.

**Discount at the event.** Undiluted NAV NZ$0.5369 on 4 November against a NZ$0.478 close: 11.0%. It was 17% at 30 September and has narrowed as the buyback ran. If a cheaper agreement is signed and the buyback holds the gap near its 6% line, the price would be about NZ$0.505, a gain of about 5.6% before any NAV move. If the board decides not to renew and the outcome is a change of manager or an exit near NAV, the gain would be up to 12%. Kingfish and Marlin share the board and the manager, and Marlin's agreement expires in late 2027, so the Barramundi terms are likely to become the template.

**What could go wrong.** The talks end in a roll-over with small changes and the discount drifts back toward 17% (about a 7% loss on the price). NAV moves with Australian shares (benchmark ASX 200, 70% hedged to NZ dollars), and that risk is as large as the discount gain. The buyback is capped at about 5% of shares a year, so it slows a widening, it doesn't stop one.

### 2. Pengana International Equities (ASX:PIA): after the buyback, a new board's discount policy

**Mechanism.** This is the case that already paid out. WAM Strategic Value built a substantial stake; Geoff Wilson and Jesse Hamilton joined the board at the October 2025 AGM; a strategic review began that month; in May 2026 the board proposed an equal-access buyback at after-tax NTA, a special dividend and a move to Antipodes as manager. After a Takeovers Panel application and a settlement in September, 151.1 million shares (58.6%) were bought back at A$1.2132, the 25 September after-tax NTA less 0.15 cents, and the Wilson directors left. What remains is a A$127m fund whose new board (interim chair Frank Gooch, with Brendan O'Dea from Pengana Capital Group, now a substantial holder) says it is "reviewing the Company's post-Buy-Back position, including recapitalisation alternatives and ongoing discount-management initiatives". The May proposal had said a rolling quarterly buyback at or around NTA would be considered after a stabilisation period.

**Date.** AGM on **26 November 2026**, which carries a conditional spill if 25% or more vote against the remuneration report (PIA took a first strike in 2025). No date for the board's review.

**Discount at the event.** NTA at 31 October A$1.1849 pre-tax and A$1.1684 post-tax against A$1.06: 10.5% and 9.3%. While the review ran, the post-tax discount sat at 3–7%. If the board adopts a standing buyback at or near NTA, a 3% discount means about A$1.15, a gain of about 7–8%. If it doesn't, the pre-review norm of 9–12% means a flat to slightly lower price.

**What could go wrong.** The activist has gone, so the pressure is lower and the new board may prefer a rights issue and growth. The move to the Antipodes global small and mid cap strategy can realise gains and costs. NTA fell about 4% in the second half of October. A A$127m fund carries fixed costs that weigh more than before.

### 3. RAM Essential Services Property Fund (ASX:REP): a board and UBS working on the discount, no date

**Mechanism.** REP sold five retail centres for A$218.6m (settled 22 October), cutting gearing from 43.5% to a pro forma 16.8%. The board says it "continues to assess capital management and other strategic initiatives aimed at reducing the trading discount to NTA and maximising securityholder value", has appointed UBS to advise, and will "shortly provide details on the first stage of the proposed capital management strategy". In August the manager said it was "considering all pathways".

**Date.** None given. The next fixed date is the half-year result in late February 2027 (last year's was 26 February), which brings a 31 December NTA.

**Discount at the event.** NTA A$0.71 at 30 June against A$0.43: 39%. A buyback alone is unlikely to close much of that: REP bought back stock in early 2025 and the price still fell from about A$0.58 in January 2026 to A$0.43. A sale of the portfolio or the fund at book NTA would be worth about 65% more than the price; at a 20% haircut to book, about 32%. Nothing like that has been announced.

**What could go wrong.** The NTA is a book value and fell 11% in the six months to June as draft valuations came in A$14.5m lower. Healthcare property values move with interest rates. RAM manages the fund for 0.65% of gross assets and its own funds hold units, so it gains from keeping the fund going. Sale proceeds went to debt, so a large cash return would need new borrowing. The "first stage" may be a small on-market buyback.

### Just outside the screen: CD Private Equity Fund II (ASX:CD2)

CD2 has the clearest dated cash event in the universe but trades only about A$8,000 a day, under the floor. Its underlying partnership (87.28% owned) signed a sale of four fund interests for about US$6.1m in October: three due to complete around 1 November 2026, the fourth in early January 2027. CD2's share is about A$7.6m, or roughly 14.5 cents a unit before any US tax, against a 31 cent price. Wilson Asset Management held 6.05% at its March 2026 notice. The warning sign is the price of the sale: about 64% of the underlying funds' reported value, which suggests the rest of the book (and CD3's, a 50% discount on a A$1.54 NTA) may be overstated too.

### Other dated events to watch

| Date | Fund | Event |
|---|---|---|
| 12 Nov 2026 | GC1 | AGM; Acorn Capital has built to 7.5% |
| 16 Nov 2026 | CAM | AGM, after the auditor's qualification |
| 17 Nov 2026 | RG8 | AGM; Philip King's retirement from Regal by 30 Jun 2027 raises the question of who runs RG8 |
| mid Nov 2026 | Wilson funds, NAOS, Cadence and other monthly reporters | October NTAs, which will show how much of the stale-NTA discount is real |
| 19 Nov 2026 | ACQ | Vote on a new five-year agreement with Acorn; a "no" would keep the manager on a three-month notice holdover |
| 19 Nov 2026 | HM1 | AGM with a conditional spill |
| 26 Nov 2026 | PIA | AGM with a conditional spill |
| 27 Nov 2026 | BHD | AGM; litigation proceeds and promised look at capital management |
| early Jan 2027 | CD2 | Last of the four sales completes |
| late Feb 2027 | REP | Half-year result and 31 Dec NTA |
| 31 Mar 2027 | BRM | Management agreement non-renewal process deadline |
| 23 Apr 2027 | MLN | Warrants exercisable at about NZ$0.85 (out of the money today) |
| 18 Aug 2027 | WHF | On-market buyback window closes |
| late 2027 | MLN | Management agreement expires |

## How often does a gap get closed by an event?

Inside the screen, over 2025 and 2026:

- **Closed to NTA:** PIA (buyback at NTA, September 2026); Diversified United (DUI) into AUI by scheme (proposed 30 January 2026, effective 21 April 2026).
- **Discount controls with a date:** Spheria Emerging Companies' trigger (a vote on converting to an unlisted fund if the average discount from April 2025 to March 2026 exceeded 5%; it averaged a 0.3% premium, so no vote); 360 Capital Mortgage REIT's holder-approved off-market buyback (approved December 2024, then postponed in April 2026).
- **Manager changes and contracts:** LED (Elanor to LDR Capital, February 2026), VHP (management internalised, late 2025), WMA (agreement extended to 2030), WHF (extended to 2031), ACQ (vote 19 November), BRM (deadline 31 March 2027).
- **Partial realisations:** CD1 and CD2 ran a sale process in 2025 that failed; CD2 signed a partial sale in October 2026.
- **Activist build-ups in funds:** Wilson's WAR in PIA (paid out), NSC (sold by May 2026) and CD2; Acorn Capital in GC1; Kenxue in LED.

The screen only sees survivors. Norgate's delisting dates show other fund vehicles that left the ASX in the same stretch: QV Equities and the Magellan Global Fund closed class (July 2024), Keybridge Capital (August 2024), Fat Prophets Global Property Fund (April 2025), Platinum Asia Investments (August 2025), DUI (April 2026) and Australian Unity Office Fund (June 2026). I haven't checked why each left; a fund delisting usually comes with a merger, conversion or wind-up that pays holders close to NTA, but that is not confirmed here for these seven.

Taken together, that is about 2–4 events a year across ASX and NZX small listed funds that force the price to or near NTA, and perhaps 1–2 a year that are announced with a date while a worthwhile gap is still open.

PIA also shows where the money is made. Its post-tax discount was about 12% before the board changed in October 2025, 4–7% in the months after the review started and about 3% by May 2026. Most of the gap closed on the announcement, not on the payout. Someone buying after the review was announced earned a further 3–6% from the discount, while the post-tax NTA per share moved from about A$1.39 to A$1.22 over the year, part of it paid out as dividends. The portfolio mattered as much as the discount.

## Plain view

There is a real opportunity here, but it is small and irregular, and it doesn't suit the research sleeve as it stands.

- **What works** is buying after a board has committed to a dated exit at or near NTA: an equal-access buyback or tender at NTA, a wind-up or conversion vote, a merger priced on NTA, or a discount trigger with a measurement date. That is a deal-spread trade with one difference: the payout is NTA, which moves with markets, so the position carries the portfolio's risk as well as the event's.
- **How many**: about 1–2 a year across ASX and NZX funds outside the large caps, with a remaining gap of roughly 3–8% once announced. Buying earlier, on an activist's stake or a board fight, is a judgement call with long waits (PIA took eleven months).
- **Today**: none of the 39 short-list funds meets that bar. Barramundi has a date but a small gap; PIA has a gap and a board talking about discount control but no commitment; REP has a big gap and a board working on it but no date and a softer NTA. At even odds on each outcome above, PIA works out at roughly +2–3% over six months and Barramundi at about break-even, both below the research rule's cash-plus-5% bar (about 3.6% for six months).
- **What it would add**: at 2.5% a position and 1–2 cases a year with a 3–8% gain, roughly 0.1–0.2% of the portfolio a year, before the wide spreads these funds trade on.

My recommendation is not to change the rule now. If Cam wants to catch these, the narrowest version would let a listed fund through the gate only when the board has announced a specific exit or discount control with a date, and treat it like a deal card with NTA risk; undated buybacks and activist stakes would go to the special situations watch list instead. Re-running this screen each quarter, and checking the dated events above as they pass, would show whether a qualifying case turns up.

## Sources

NTA announcements used for each fund (ASX display pages give the PDF link; NZX links give the announcement record):

- ASX: [ACQ](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03151884); [AIQ](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03152199); [ALI](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03161400); [AMH](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03161069); [AUI](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03161348); [BHD](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03151544); [BKI](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03160922); [BTI](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03151977); [CAM](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03161151); [CD2](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03155089); [CD3](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03152343); [CDM](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03152401); [CDO](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03152425); [CIN](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03161130); [DJW](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03161058); [FGG](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03152435); [FGX](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03152440); [FPC](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03163109); [GC1](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03163239); [GCI](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03163122); [GLS](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03161695); [GVF](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03152118); [HM1](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03160864); [KKC](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03160885); [LED](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03131198); [LRT](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03161350); [LSX](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03162436); [MIR](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03161061); [MOT](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03152358); [MRE](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03152366); [NAC](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03152029); [NCC](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03152028); [NSC](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03152031); [OPH](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03160970); [PCX](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03162852); [PE1](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03151604); [PIA](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03162325); [PL8](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03160735); [REP](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03130186); [RF1](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03160962); [RG1](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03160957); [RG8](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03160961); [RYD](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03150108); [SEC](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03163257); [SNC](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03149418); [TCF](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03150169); [TGF](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03161110); [TOP](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03149071); [WAA](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03162863); [WAM](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03151094); [WAR](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03150495); [WAX](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03151098); [WGB](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03151053); [WHF](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03152112); [WMA](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03152165); [WMI](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03152058); [WQG](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03161490)
- NZX: [AFI](https://api.nzx.com/public/announcement/483216/data.json); [BIF](https://api.nzx.com/public/announcement/483062/data.json); [BIT](https://api.nzx.com/public/announcement/483137/data.json); [BRM](https://api.nzx.com/public/announcement/483126/data.json); [CO2](https://api.nzx.com/public/announcement/483222/data.json); [FCT](https://api.nzx.com/public/announcement/483139/data.json); [HFL](https://api.nzx.com/public/announcement/483138/data.json); [KFL](https://api.nzx.com/public/announcement/483124/data.json); [MLN](https://api.nzx.com/public/announcement/483127/data.json); [PLP](https://api.nzx.com/public/announcement/483061/data.json); [TEM](https://api.nzx.com/public/announcement/483136/data.json)
- VHP's NTA is NZX's company data field (data/research_data/nzx_company.json). NZX's announcement feed refused access for VHP, BIF and PLP. VHP's internalisation comes from search results only: [RNZ, 10 Nov 2025](https://www.rnz.co.nz/news/top/578379/vital-healthcare-takes-management-in-house) and [Northwest REIT completion release](https://www.newsfilecorp.com/release/279150/Northwest-Healthcare-Properties-REIT-Announces-Completion-of-Vital-Management-Internalization?lang=fr).

Catalyst documents relied on most:

- BRM: [management agreement renewal date (22 Oct 2026)](https://api.nzx.com/public/announcement/482265/data.json)
- BRM: [investment mandate waiver (29 Oct 2026)](https://api.nzx.com/public/announcement/482708/data.json)
- BRM: [annual meeting presentation and chair's address (30 Oct 2026)](https://api.nzx.com/public/announcement/482761/data.json)
- BRM: [2026 annual report (fees, cash)](https://api.nzx.com/public/announcement/480630/data.json)
- MLN: [buyback continuation (22 Oct 2026)](https://api.nzx.com/public/announcement/482278/data.json)
- MLN: [warrant issue (16 Feb 2026)](https://api.nzx.com/public/announcement/467529/data.json)
- MLN: [annual meeting chair's address (6 Nov 2026)](https://api.nzx.com/public/announcement/483150/data.json)
- KFL: [2026 annual report (fees, cash)](https://api.nzx.com/public/announcement/474968/data.json)
- PIA: [buyback, special dividend and Antipodes proposal (8 May 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03091921)
- PIA: [board update (17 Sep 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03140696)
- PIA: [buyback completion and board changes (30 Sep 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03145977)
- PIA: [2026 AGM notice](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03156485)
- REP: [FY26 results (26 Aug 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03130186)
- REP: [contracts exchanged and valuations (23 Jul 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03117424)
- REP: [settlement of retail assets, UBS appointed (22 Oct 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03155811)
- CD2: [secondary sale and NTA update (21 Oct 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03155089)
- CD2: [2025 sale process update (27 Nov 2025)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03033556)
- CD2: [Wilson Asset Management substantial holding (10 Mar 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03070476)
- SEC: [outcome of the discount trigger (9 Apr 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03081136)
- AUI: [proposed merger with DUI (30 Jan 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03054509)
- AUI: [DUI scheme effective (21 Apr 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03084660)
- TCF: [buyback update (2 Apr 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03078924)
- TCF: [trust update on Bathla loans (29 Sep 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03145356)
- MOT: [circumstances affecting the 4E (28 Sep 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03144657)
- MOT: [delay and suspension of underlying NAVs (30 Sep 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03146000)
- CAM: [response to ASX on the qualified audit (16 Oct 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03153887)
- ACQ: [2026 AGM notice and expert's report](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03154740)
- HM1: [cost change (26 Aug 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03130452)
- HM1: [2026 AGM notice](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03153987)
- BHD: [litigation update (20 Jul 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03116102)
- GC1: [Acorn Capital substantial holding (16 Sep 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03140204)
- LED: [FY26 results (27 Aug 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03131198)
- LED: [Kenxue substantial holding (9 Oct 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03150672)
- WHF: [on-market buyback (4 Aug 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03121801)
- WHF: [management agreement extension (19 May 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03095194)
- WMA: [management agreement extension (24 Oct 2025)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03014884)
- WAA: [estimated October NTA (20 Oct 2026)](https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03154336)

Data in the repo: prices from data/research_data/asx_company.json and data/prices/NZX; liquidity from data/norgate/universe/prices_2026.csv.gz and NZX's instrument activity data (api.nzx.com/public/instrument/<ISIN>/metrics/activity/past/2Y.json); FX from data/fx/rba_f11_1.csv; delisting dates from data/norgate/universe/securities.csv.

