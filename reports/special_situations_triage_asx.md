# Special situations triage: ASX watch list

Written 8 Nov 2026 by the research desk, for the ten ASX names on the special situations watch list in [research_rank.md](research_rank.md) that the desk hasn't deep-dived. A simulation for the paper portfolio, not financial advice.

Rulebook section 5a allows pre-deal and holder situations, failed bids and strategic reviews as research picks once deep-dived and reviewed; binding deals belong to the deal sleeve. This triage picks which of the ten deserve that deep dive first. It doesn't size or approve anything.

How the numbers are worked:

- Price is `header.priceLast` in [asx_company.json](../data/research_data/asx_company.json), the last trade to 6 Nov 2026.
- Undisturbed price is the last close before the first public word of the proposal, from [prices_2026.csv.gz](../data/norgate/universe/prices_2026.csv.gz) (and the 2025 file).
- Market moves use STW (the S&P/ASX 200 fund) closes in the same file, to 30 Oct 2026.
- Nothing happens is the undisturbed price moved by the market since, less dividends paid since, and adjusted for any change in the business. Where the shares have traded for weeks after a bid died, that level is used as a check.
- Deal is the most recent price a bidder actually put on the table, adjusted for dividends since, unless a better marker is stated.
- Liquidity is the median of close times volume over the 20 sessions to 30 Oct 2026 (the latest in the price file). All ten clear A$10,000 a day.

## The table

| Company | Status today | Offer or proposal, and date | Price (6 Nov) | Nothing happens (gap) | Deal (gap) | Next dated event | 20-day median traded | Grade |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ASX:PAC Pacific Current | Strategic review, live | Review from 27 Aug 2026; River Capital proposal for PAC to buy River with shares at A$13.00 (27 Aug); Roc Partners proposal (May 2026) declined | A$11.02 | A$10.86 (-1.5%) | A$13.00 (+18%) | AGM 12 Nov 2026, review update at or before it | A$14,745 | A |
| ASX:CZR CZR Resources | Its own takeover bid (for Zuleika) voted down and withdrawn; cash shell 51% held by Mark Creasy's Yandal | Scrip bid for Zuleika announced 26 Jun 2026; voted down 23 Oct; withdrawn 30 Oct; the 27c buy-back tied to it lapsed | A$0.19 | A$0.19 (0%) | A$0.25 cash backing (+32%) | AGM 26 Nov 2026 (dissident director nominee) | A$33,375 | B |
| ASX:HUM Humm Group | Two failed approaches; holder situation | TAG (Abercrombie) A$0.58, 23 Jun 2025, withdrawn 6 Nov 2025; Credit Corp A$0.77 scheme or A$0.72 bid, 19 Nov 2025, cut 19 Jun 2026 and ended 22 Jun 2026 | A$0.48 | A$0.45 (-6%) | A$0.58 (+21%) | AGM 20 Nov 2026 (second strike vote, possible spill) | A$160,228 | B |
| ASX:MVF Monash IVF | Proposal rejected and lapsed; bidders hold 19.6% | Genesis Capital and Soul Patts A$0.80, 24 Nov 2025 (withdrawn 24 Dec 2025); A$0.90 "highest", 13 Apr 2026, rejected 20 Apr 2026 | A$0.74 | A$0.66 (-11%) | A$0.90 (+22%) | AGM 26 Nov 2026 | A$146,800 | B |
| ASX:EOL Energy One | Proposal rejected; bidder stood down | Volue A$16.50, 6 Jul 2026; A$17.00, 22 Jul 2026; rejected 30 Jul; Volue stood down 3 Sep 2026 | A$14.09 | A$14.40 (+2%) | A$16.47 (+17%) | H1 FY27 result, about late Feb 2027 | A$321,772 | C |
| ASX:MXI MaxiPARTS | Proposal withdrawn in due diligence | Ares A$2.50, 3 Sep 2026; withdrawn 22 Sep 2026 | A$2.00 | A$1.95 (-2.5%) | A$2.50 (+25%) | AGM 26 Nov 2026 | A$59,623 | C |
| ASX:PPM Pepper Money | Proposal cut, then ended | Challenger with Pepper Group A$2.60, confirmed 9 Feb 2026; cut to A$2.25 best and final, 17 Mar; ended 25 Mar 2026 | A$1.775 | A$1.70 (-4%) | A$2.10 (+18%) | CY2026 result, about Feb 2027 | A$238,517 | C |
| ASX:NVA Nova Minerals | No bid: the scheme moved Nova under a US parent | Redomicile schemes effective 3 Jun 2026 | A$0.51 | A$0.51 (0%) | none | none | A$300,427 | C |
| ASX:PLA Pacific Lime and Cement | Review of one asset only; halted for a capital raising | Strategic review of the Star Mountains project, 25 Mar 2026 (amended 28 Apr); trading halt 5 Nov 2026 | A$0.38 (last trade before the halt) | not knowable until the raising is priced | none | Halt ends by 9 Nov 2026 | A$56,923 | C |
| ASX:KME Kip McGrath | Binding: takeover closed, compulsory acquisition under way | Crimson Australia A$0.73 cash, 30 Jul 2026; raised to A$0.75, 12 Oct; closed 4 Nov at 93.88% | A$0.69 | not used (deal sleeve) | A$0.69 net of the 6c dividends (0%), or A$0.75 if no deduction applies (+8.7%) | Payment about six weeks after 4 Nov 2026 | A$70,009 | deal sleeve |

## Which to deep-dive first

1. **Pacific Current (PAC)**, now: the only live situation with the floor close to the price and a dated event that could bring a deal. The review update is due at or before the AGM on Thursday 12 Nov, so the deep dive has to start immediately.
2. **CZR Resources (CZR)** and **Humm (HUM)**, next, as watch cases with AGMs on 26 Nov and 20 Nov. CZR trades at about three quarters of its cash with a 51% holder and a board that tried a 27c buy-back. Humm's 31.8% holder bought on market at about A$0.46 to A$0.48 within days of Credit Corp walking, an activist has just crossed 5%, and a second strike vote is due.
3. **Monash IVF (MVF)**, watch only. Its bidders still hold 19.6% and named A$0.90 as their highest price, but nothing dated could bring them back and the floor is about 11% below.

Two triggers on the watch list were misread by the screen. The CZR headline "ZAG: CZR Takeover - Target's Statement" is Zuleika's statement as the target, and CZR was the bidder. The NVA "Scheme Booklet" moved Nova under a US parent company and wasn't a takeover. KME's bid has closed and belongs to the deal sleeve; it isn't in the [deal monitor](deal_monitor.md).

## Company notes

### ASX:PAC Pacific Current Group: grade A

**Where it stands.** On 27 Aug 2026 PAC started a strategic review ([27 Aug][pac-review]). It followed a non-binding proposal from River Capital, its largest holder, for PAC to buy River Capital for about A$80m, paid in about 6.3 million new PAC shares at A$13.00. River's funds would first sell their roughly 10 million PAC shares through a bookbuild at no less than A$13.00. The review also covers a sale of PAC, or delisting and an orderly sale of its holdings, and the on-market buy-back was suspended. On 7 Sep PAC disclosed that in May 2026 it had declined a proposal from Roc Partners ([7 Sep][pac-update]). The cash in that proposal came mostly from PAC's own assets, and it would have paid holders differently. PAC told Roc it would look at an all-cash offer at fair value, and Roc hadn't come back. PAC expects to update the review "at or before" its AGM on 12 Nov 2026 ([7 Sep][pac-update], [AGM notice][pac-agm]).

**The business.** Fair value NAV was A$16.18 a share and statutory NAV A$13.96 at 30 Jun 2026, with no debt after the facility was repaid in October 2025 ([FY26 result][pac-fy26]). A 28c final dividend has been paid since (ex 3 Sep 2026, [company data][data]). Boutique funds under management were steady at A$26.4b at 30 Sep 2026 ([30 Oct][pac-fum]).

**The players.** The substantial holders are River Capital (12,207,237 shares, 43.69%), Perpetual (10.17%), Michael Fitzpatrick (8.60%) and DS Capital (5.56%) ([2026 annual report][pac-ar]). River's share count hasn't changed in its 2026 notices; its percentage rose only because PAC bought back shares ([11 Jun notice][pac-river-jun], [14 Apr notice][pac-river-apr]). The top 20 holders own 83.8% of the register ([2026 annual report][pac-ar]).

**The rules.** River can creep up by 3 percentage points every six months. Any deal with River needs approval from holders other than River and an independent expert's report ([27 Aug][pac-review]). A scheme to sell PAC needs 75% of votes cast, so River decides it. A delisting normally needs holder approval under ASX's delisting guidance.

**Price and values.** A$11.02, against an undisturbed A$11.45 on 26 Aug 2026 ([prices][px]).

- Nothing happens: A$10.86 (-1.5%). That is A$11.45, less the 28c dividend, moved by the market's 2.8% fall since 26 Aug.
- Deal: A$13.00 (+18%). That is River's own bookbuild floor and share issue price. A full realisation near fair value NAV after the dividend (about A$15.90, +44%) is the upside, but it would take time and costs.

**Next event and liquidity.** The AGM on 12 Nov 2026. Liquidity is A$14,745 a day: thin, with several near-empty sessions, but above the floor.

**For the deep dive.** Check whether PAC falls under the ranking's "fund, trust or investment company" drop rule; the ranking sent it to this watch list instead of dropping it.

### ASX:CZR CZR Resources: grade B

**Where it stands.** CZR was the bidder here, not the target. On 26 Jun 2026 it agreed an all-scrip takeover of Zuleika Gold at 0.1742 CZR shares per Zuleika share ([26 Jun][czr-merge]). The bid needed CZR holders to approve buying the Zuleika shares held by Yandal (Mark Creasy's company) and director Annie Guo. On 23 Oct the non-associated holders voted it down: 79.75% and 81.99% against ([23 Oct][czr-rom]). CZR said the condition couldn't be met ([26 Oct][czr-cond]) and withdrew the bid with ASIC's consent on 30 Oct 2026 ([30 Oct][czr-wd]).

The independent board had proposed a buy-back of up to A$15m: first an equal-access offer to buy 10% of every holding at 27c, then on-market buying ([7 Oct notice][czr-supp]). Holders approved it with 74.03% in favour ([23 Oct][czr-rom]), but it was conditional on the Zuleika deal, so it won't proceed ([quarterly][czr-q]).

**The business.** CZR held A$61.4m of cash and term deposits at 30 Sep 2026, against A$65.1m at 30 Jun ([quarterly][czr-q], [annual report][czr-ar]). That is A$0.253 a share on 242.4m shares ([company data][data]). It spent A$3.7m on operations in the September quarter ([quarterly][czr-q]).

**The players and rules.** Yandal holds 123,529,413 shares, 50.95% ([7 Oct notice][czr-supp], [annual report][czr-ar]). With more than 19% for six months, Yandal can creep 3 points every six months. It could bid for the rest at any time, and it would need 90% to compulsorily acquire. At the AGM on 26 Nov 2026 a holder has nominated Aleksandar Mihajlovic as a director against the board's advice ([AGM notice][czr-agm]). The board has also asked for the usual 10% placement capacity.

**Price and values.** A$0.19 (about 0.75 times cash). Before the deal it closed at A$0.22 on 19 Jun 2026 with A$65.1m of cash, about 0.82 times cash ([prices][px]); the market was flat over the period.

- Nothing happens: A$0.19 (0%). That is where it has traded since the vote (A$0.175 to A$0.185 closes); cash is falling by about 1.5c a share a quarter.
- Deal: A$0.25 (+32%). That is the cash backing, if the surplus cash were returned or Yandal bid for the rest at cash.

**Next event and liquidity.** The AGM on 26 Nov 2026. Liquidity is A$33,375 a day.

**Why B, not A.** It's a holder situation with a floor near the price, but no proposal is on the table. The controlling holder has just tried to use the cash on a related-party deal, so a return of the cash isn't something any dated event is set to bring.

### ASX:HUM Humm Group: grade B

**Where it stands.** No proposal is open, after two failed ones:

- TAG, the family company of then-chair Andrew Abercrombie, offered A$0.58 cash for the shares it didn't hold on 23 Jun 2025, against a A$0.43 close ([25 Jun 2025][hum-tag]). It withdrew on 6 Nov 2025, saying several key holders didn't support it ([6 Nov 2025][hum-tagend]).
- Credit Corp proposed a A$0.77 scheme, or a A$0.72 takeover bid needing 50.1% acceptances, on 19 Nov 2025 ([17 Dec 2025][hum-ccp], [Credit Corp][hum-ccp2]). After due diligence it cut its price "materially" on 19 Jun 2026, and both sides ended talks on 22 Jun 2026 ([Humm][hum-ccpend], [Credit Corp][hum-ccpend2]). Credit Corp said it raised "a number of matters" it couldn't get comfort on.
- The Takeovers Panel found Humm's December 2025 announcement misleading. Abercrombie had already decided to reject the Credit Corp proposal when the board said it was "carefully evaluating" it ([18 Mar 2026][hum-panel]).

**The players.** TAG and associates hold 31.84% as of 13 Jul 2026 ([annual report][hum-ar], [13 Jul notice][hum-tag-jul]). TAG bought about 11.6 million shares on market between 26 Jun and 9 Jul 2026, at about A$0.46 to A$0.48, starting four days after Credit Corp walked ([9 Jul notice][hum-tag-jul9], [13 Jul notice][hum-tag-jul]). TAG had said on 1 May it was unlikely to support Credit Corp at A$0.77 and didn't intend to accept A$0.72 ([1 May][hum-may]).

The other substantial holders are AKAT Investments (TAG Family No. 2 Trust, 10.18%, the party whose application led to the Panel's declaration) and Renaissance Smaller Companies (7.16%) ([annual report][hum-ar], [Panel][hum-panel]). Jeremy Raper and Rangeley Capital crossed 5% on 5 Nov 2026 with 6.44% ([6 Nov notice][hum-raper]). In December 2025 Raper and Collins Street Value Fund served a notice seeking to remove Abercrombie and two other directors ([17 Dec 2025][hum-ccp]).

**The rules.** TAG has used its 3-point creep for now. It went from 29.19% (its December 2025 notice) to 31.84% by 13 July ([9 Jul notice][hum-tag-jul9], [13 Jul notice][hum-tag-jul]), so more creep waits for the six-month window to roll. At 31.84%, TAG can block any scheme it opposes.

**The AGM.** It is on 20 Nov 2026 ([7 Oct][hum-agmdate]). The 2025 remuneration report drew 55.5% against, a first strike ([2025 AGM result][hum-2025agm]), so a conditional spill resolution is on the agenda ([notice][hum-agm]).

**The business.** Net assets are about A$535m, about A$1.05 a share ([company data][data]), so the price is about 0.46 times book. The 1Q27 update showed volume up 13.7% and the underlying cost-to-income ratio 350 basis points lower ([2 Nov][hum-1q]).

**Price and values.** A$0.48. It was A$0.415 on 30 Oct and rose after the update and Raper's buying. The pre-Credit Corp undisturbed price was A$0.64 (15 Dec 2025), but it no longer guides: after the walk-away the shares closed at A$0.455 (22 Jun 2026) ([prices][px]).

- Nothing happens: A$0.45 (-6%). That is A$0.455 less the 0.5c dividend since, with a flat market.
- Deal: A$0.58 (+21%). That is TAG's own price; the A$0.77 was cut after due diligence and can't be used.

**Next event and liquidity.** The AGM on 20 Nov 2026. Liquidity is A$160,228 a day.

**Why B.** It's live as a holder contest, but the AGM can change the board, not deliver a bid, and the floor is 6% below.

### ASX:MVF Monash IVF: grade B

**Where it stands.** A consortium of Genesis Capital and Soul Patts offered A$0.80 by scheme on 24 Nov 2025, which the board rejected ([24 Nov 2025][mvf-1]). The consortium withdrew it on 24 Dec 2025 ([24 Dec 2025][mvf-wd]). It came back at A$0.90 on 13 Apr 2026, calling it "the highest amount" absent a rival, valid to 21 Apr ([13 Apr][mvf-2]). The board rejected that on 20 Apr 2026, citing comparable IVF deals, its new CEO and feedback from other holders, and said it is open to a higher offer ([20 Apr][mvf-rej]).

**The business.** FY26 underlying NPAT was A$16.1m, below the A$17m to A$18m guidance given in June ([31 Aug][mvf-fy26], [12 Jun][mvf-tu]).

**The players.** The consortium holds up to 76,367,969 shares, 19.60% (Genesis and Soul Patts about half each) ([Genesis notice][mvf-gen], [Soul Patts notice][mvf-sol]). There has been no consortium holding notice since November 2025 ([announcement list][data]).

**The rules.** Having held more than 19% for six months, the consortium has been able to creep 3 points every six months since about May 2026 and hasn't. Its 19.6% would weigh heavily against any rival scheme.

**Price and values.** A$0.74, against an undisturbed A$0.665 on 10 Apr 2026 (A$0.61 before the first approach) ([prices][px]).

- Nothing happens: A$0.66 (-11%). That is A$0.665 moved by the market's 1.1% fall since and the 1.3c dividend, with the FY26 miss.
- Deal: A$0.90 (+22%).
- The shares have held between A$0.655 and A$0.82 since the rejection (median A$0.715), so the market still prices some bid.

**Next event and liquidity.** The AGM on 26 Nov 2026 ([notice][mvf-agm]); a director resigned on 26 Oct ([26 Oct][mvf-dir]). Liquidity is A$146,800 a day.

**Why B.** The bidders still hold their stake and the board invited a higher price, but no dated event brings them back and the floor is 11% below.

### ASX:EOL Energy One: grade C

**Where it stands.** Volue made a non-binding A$16.50 cash proposal on 6 Jul 2026 and A$17.00 on 22 Jul. Energy One rejected it on 30 Jul ([30 Jul][eol-resp]). On 19 Aug Energy One agreed to buy GMSL from Fluxys for 7,089,780 new shares (implied enterprise value A$99.8m), which it said would raise FY26 pro forma EPS by about 35% ([19 Aug][eol-gmsl]). Holders approved the share issue with 85.68% ([15 Oct][eol-egm]), and it completed on 30 Oct 2026 ([30 Oct][eol-comp]). Volue said on 3 Sep 2026 it won't proceed "at this time": the board hadn't engaged, the Fluxys exclusivity got in the way, and GMSL doesn't fit its strategy ([Volue][volue]).

**The players.** Fluxys holds 18.26%, escrowed for 12 months to 30 Oct 2027, with exceptions to accept a takeover or scheme ([Fluxys notice][eol-flux]). The other holders are Ian Ferrier (12.87%, [3 Nov][eol-fer]), Regal (8.15%, [3 Nov][eol-regal]), Wilson Asset Management (7.68%, [2 Nov][eol-wam]) and founder Vaughan Busby (7.70% before the new shares, [annual report][eol-ar]). Directors and Fluxys together can block any scheme.

**Price and values.** A$14.09, against an undisturbed A$10.85 (29 Jul 2026) ([prices][px]).

- Nothing happens: A$14.40 (+2%). That is A$10.85 lifted by the stated 35% EPS gain and moved by the market. Since Volue stood down the shares have traded A$13.80 to A$16.00.
- Low case: valuing GMSL only at its price gives about A$11.30.
- Deal: A$16.47 (+17%). That is Volue's A$17.00 on the old 31.75m shares plus A$99.8m for GMSL, spread over 38.84m shares. But no bidder is interested.

**Next event and liquidity.** The H1 FY27 result, about late Feb 2027. Liquidity is A$321,772 a day.

**Why C.** Dead: the bidder has gone, a blocking holder is in place, and the price sits on the nothing-happens value.

### ASX:MXI MaxiPARTS: grade C

**Where it stands.** Ares proposed A$2.50 cash by scheme on 3 Sep 2026, against a A$1.71 close, and got four weeks' exclusivity ([3 Sep][mxi-ares]). It withdrew on 22 Sep 2026, partway through due diligence ([22 Sep][mxi-wd]).

**The business.** On the same day as the proposal, MaxiPARTS agreed to buy Air Brake Systems for A$11.2m, which it said adds 17% to EPS ([3 Sep][mxi-ares]). The deal completed on 19 Oct ([19 Oct][mxi-abs]). First-quarter operating profit before tax rose 26.5%, and the company expects higher capital returns in FY27 ([23 Oct][mxi-tu]).

**The players.** NAOS (27.50%), HGT Investments (13.00%) and James Curtis (10.40%) ([annual report][mxi-ar]), plus Perpetual (10.65%, [27 Oct][mxi-ppt]). Any scheme needs NAOS.

**Price and values.** A$2.00 ([company data][data]).

- Nothing happens: A$1.95 (-2.5%). That is A$1.71 moved by the market and lifted by the stated 17% EPS gain. The post-withdrawal range was A$1.74 to A$1.99.
- Deal: A$2.50 (+25%). But the bidder walked.

**Next event and liquidity.** The AGM on 26 Nov 2026 ([notice][mxi-agm]). Liquidity is A$59,623 a day.

**Why C.** Dead, and the price already reflects the better business.

### ASX:PPM Pepper Money: grade C

**Where it stands.** Pepper Money confirmed on 9 Feb 2026 a A$2.60 proposal from Challenger, with Pepper Group buying alongside ([9 Feb][ppm-1]). Challenger cut it to A$2.25 "best and final", including the 7.8c final dividend, on 17 Mar ([17 Mar][ppm-2]). The independent committee ended talks on 25 Mar 2026, finding the proposal "not reasonably capable of execution" ([25 Mar][ppm-end], [Challenger][ppm-cgf]).

**The players.** Pepper Group (KKR-controlled) holds 59.91% ([annual report][ppm-ar]). AustralianSuper holds 13.33% and bought about 2.2 million more shares on 25 and 26 Mar, after talks ended ([30 Mar notice][ppm-as]).

**The rules.** Pepper Group can creep 3 points every six months. A take-private by scheme would put the vote with the minority, where AustralianSuper holds about a third. AustralianSuper's 13.33% alone blocks compulsory acquisition after a bid.

**Price and values.** A$1.775, against an undisturbed A$1.76 (6 Feb 2026) ([prices][px]).

- Nothing happens: A$1.70 (-4%). That is A$1.76 moved by the market and less the 15c of dividends paid since. The post-talks median was A$1.71.
- Deal: A$2.10 (+18%). That is A$2.25 less the 7.8c and 7.2c dividends since.

**Next event and liquidity.** The CY2026 result, about Feb 2027. Liquidity is A$238,517 a day.

**Why C.** Dead: the controlling holder hasn't moved, and nothing dated could bring a deal.

### ASX:NVA Nova Minerals: grade C

The "Scheme Booklet" on the watch list was for schemes that put Nova Minerals under a new US parent, Nova Minerals Corp. They took effect on 3 Jun 2026 ([3 Jun][nva-eff]), at one US share for every 12 Australian shares, and the ASX line is now CDIs ([1 Jul][nva-cap]). There is no bid, proposal or holder situation. It is also a pre-production explorer, which the ranking would otherwise drop as having no business to value yet.

Price A$0.51. Nothing happens is the price; there is no deal value. Liquidity is A$300,427 a day.

### ASX:PLA Pacific Lime and Cement: grade C

The strategic review is of one asset, the Star Mountains copper-gold project ([28 Apr amended announcement][pla-sr]), not of the company. The PNG Government took 13% of the Central Lime Project company for US$16.3m in July ([27 Jul][pla-png]). Maybank Securities holds 8.81% ([14 May][pla-may]).

PLA went into a trading halt on 5 Nov 2026 "pending announcements in relation to a material capital raising and a material financing transaction", to end by the open on 9 Nov ([5 Nov][pla-halt]). A raising is the opposite of a takeover premium. If PLA reopens 5% or more lower on heavy volume, rulebook section 9 (test 9g) bars a new position for 30 sessions.

Price A$0.38, the last trade before the halt. Liquidity is A$56,923 a day.

### ASX:KME Kip McGrath Education Centres: deal sleeve

Crimson Australia (part of New Zealand's Crimson Consulting) bid A$0.73 cash on 30 Jul 2026, against a A$0.45 close on 29 Jul ([bidder's statement][kme-bs]). It raised the bid to A$0.75 on 12 Oct ([variation][kme-var]) and declared it unconditional and last and final the same day ([third supplementary][kme-3s]). Holders entitled to the 6.0c of KME dividends (ex 1 Oct, [company data][data]) have them deducted, so they get A$0.69 from Crimson and A$0.75 in all ([third supplementary][kme-3s]).

The offer closed on 4 Nov 2026 with Crimson at 93.88% ([5 Nov][kme-close]). It started compulsory acquisition on 4 Nov on the same terms, and expects the remaining holders' money to reach KME about six weeks after that date, around mid-December 2026 ([4 Nov][kme-ca]).

Price A$0.69. The spread is 0% at A$0.69 net. It would be +8.7% if a buyer after the record date isn't subject to the dividend deduction; the deal sleeve should check section 9.6(c) of the bidder's statement before any use. Liquidity is A$70,009 a day, until KME is suspended.

## Checked afterwards

This section was added after the triage above was written, when the desk's existing files were checked for missed facts. No grade changes. No separate special situations brief was found in the repository.

- Pepper Money: the desk's Resimac fact sheet ([RMC.md](../research/facts/RMC.md)) puts book value at A$1.974 a share (equity A$886.9m over 449.38m shares). At A$1.775 that is 0.90 times book, which supports a nothing-happens value near the price.
- MaxiPARTS: the Capral deep dive ([CAA.md](../research/picks/CAA.md)) has MaxiPARTS at about 1.57 times net tangible assets and about 14% on tangible equity, an ordinary rating for a distributor. The deep-dive index had already flagged the Ares withdrawal as a special situation not yet looked at ([INDEX.md](../research/picks/INDEX.md)).
- CZR: the Fenix fact sheet ([FEX.md](../research/facts/FEX.md)) notes that Fenix's own bid for CZR lapsed in April 2025. That fits the history behind CZR's cash. The Robe River joint venture (Rio Tinto, Mitsui and Nippon Steel) made a binding A$75m cash offer for CZR's Robe Mesa iron ore project in April 2025 ([11 Apr 2025][czr-robe]). The sale completed on 9 Sep 2025, with about A$70.5m received ([9 Sep 2025][czr-robe2]). CZR has been sitting on the proceeds since.

[data]: ../data/research_data/asx_company.json
[px]: ../data/norgate/universe/prices_2026.csv.gz
[pac-review]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03130926
[pac-update]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03136508
[pac-agm]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03150414
[pac-fy26]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03131032
[pac-fum]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03160352
[pac-ar]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03147167
[pac-river-jun]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03103596
[pac-river-apr]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03082877
[czr-merge]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03108098
[czr-rom]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03156677
[czr-cond]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03157061
[czr-wd]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03160227
[czr-supp]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03149423
[czr-q]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03159930
[czr-ar]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03143598
[czr-agm]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03157600
[czr-robe]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=02937127
[czr-robe2]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=02993146
[hum-tag]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=02961915
[hum-tagend]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03021918
[hum-ccp]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03042216
[hum-ccp2]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03042241
[hum-ccpend]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03106259
[hum-ccpend2]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03106183
[hum-panel]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03073469
[hum-may]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03089570
[hum-ar]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03129651
[hum-tag-jul9]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03113672
[hum-tag-jul]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03114495
[hum-raper]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03162855
[hum-agmdate]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03149367
[hum-agm]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03154173
[hum-2025agm]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03024510
[hum-1q]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03161040
[mvf-1]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03030652
[mvf-wd]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03045237
[mvf-2]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03081777
[mvf-rej]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03084087
[mvf-fy26]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03132881
[mvf-tu]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03103409
[mvf-gen]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03030766
[mvf-sol]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03031179
[mvf-agm]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03156106
[mvf-dir]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03156877
[eol-resp]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03120002
[eol-gmsl]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03126590
[eol-egm]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03152849
[eol-comp]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03159740
[eol-flux]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03160693
[eol-fer]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03161516
[eol-regal]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03161621
[eol-wam]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03161266
[eol-ar]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03134571
[volue]: https://volue.com/news/volue-confirms-decision-not-to-pursue-energy-one-acquisition
[mxi-ares]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03135247
[mxi-wd]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03142046
[mxi-abs]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03153792
[mxi-tu]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03156123
[mxi-ar]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03156387
[mxi-ppt]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03157889
[mxi-agm]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03156388
[ppm-1]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03057971
[ppm-2]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03072991
[ppm-end]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03075571
[ppm-cgf]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03075576
[ppm-ar]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03062026
[ppm-as]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03078635
[nva-eff]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03100702
[nva-cap]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03109937
[pla-sr]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03087054
[pla-png]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03118238
[pla-may]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03094913
[pla-halt]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03162268
[kme-bs]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03119914
[kme-var]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03151106
[kme-3s]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03151104
[kme-close]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03162361
[kme-ca]: https://www.asx.com.au/asx/v2/statistics/displayAnnouncement.do?display=pdf&idsId=03161875
