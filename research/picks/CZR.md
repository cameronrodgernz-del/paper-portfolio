# CZR Resources (ASX:CZR): special situation deep dive. Not a value pick: the "nothing happens" value (A$0.170) is 10.5% below the price and the middling case (A$0.193) only 1.6% above it

Written 2026-11-08 by the research desk. Price at writing: A$0.19 (last trade on Friday 6 November 2026, a single trade of 50 shares, bid A$0.18, ask A$0.195; the session before closed at A$0.195; ASX company data in data/research_data/asx_company.json, fetched 7 November 2026 [D1]. Norgate's last close in the repo is A$0.175 on 30 October [D2]). Market value: A$46.1m (242,447,887 shares on issue, AGM notice of 27 October 2026 [C3]).
Status: finished. This is a simulation and not financial advice.
Verdict: **Wait for a named event**: the AGM on 26 November 2026 (and anything the board says there about the cash), then the December quarterly report (due by 31 January 2027). Exact reopen conditions are under "What would make this wrong". Not a card now. It is a special situation under rulebook section 5a (a controlling holder after a failed bid of its own), not a value pick, and on the chances below the expected gain after costs is about -10%, against a minimum of +3.4% to the 30 April 2027 resolve date.
Fact sheet: none. The starting point was the special situations triage (reports/special_situations_triage_asx.md, CZR section, grade B). Its question: CZR trades at about three quarters of its cash with a 51% holder and a board that offered a 27c buy-back; is there a dated way for holders to get the cash? Its anchors: A$0.19 if nothing happens, A$0.25 (cash backing) if the surplus cash were returned or Yandal bid at cash.

Order of work. The brief quoted the price, so it was in view from the start. The filings, the cash and the valuation were worked from CZR's own reports, the independent expert's report and the technical valuer's report; CZR's share price enters only through the market multiple of cash in method 2, which is the measure the market itself uses for a company like this, and in "Why the market is wrong" and "Outcomes and chances". Arithmetic was run in `python3 -I` from scratch scripts (model.py, calc.py, px.py), not committed; the key lines are shown below.

> In one paragraph: the kill check comes first and it half kills the case. There is no business here to value on earnings: CZR has no revenue, spends A$3m to A$4m a quarter exploring five projects that all sit in joint ventures with Mark Creasy, and holds A$61.4m of cash from the 2025 sale of Robe Mesa. After the A$3.57m of income tax it still owes and its payables, net cash is about A$57.0m, 23.5c a share; the exploration ground is worth A$10.2m to A$17.0m on the independent valuer's August 2026 figures. So it is a cash shell with exploration ground, and the only route to the value is cash coming back to holders or a buyout by the controlling holder. That route is in one person's hands. Creasy's companies hold 50.95%, he can carry any ordinary resolution alone, and his interests point the other way: he keeps a 30% free-carried share of Croydon, where most of CZR's exploration money goes, he tried to fold CZR's cash into his other controlled explorer (Zuleika) only four months ago, and in the 14 months since the cash arrived (19 since it first said it might return capital) CZR has returned nothing. The minority's one lever, the related-party vote that killed the Zuleika deal, is a veto, not a way to get cash out. The market prices the shares at 0.81 times net cash after tax, about the multiple just before the Zuleika deal (0.79 on 25 June 2026); Creasy's other cash-rich company, Zuleika, trades at 0.69 to 0.74 times its cash and listed shares. With the cash shrinking by about 1.2c a share a quarter, the "nothing happens" value at the March 2027 quarterly is A$0.170. Weighting a 20% chance of partial capital management (A$0.193, because a partial return leaves the discount on the rest) and a 10% chance of a full return, a buyout or a drilling re-rating (A$0.225) gives an expected price of A$0.180, about 5% below the price before costs. The triage's A$0.25 "deal" value was gross cash per share; after tax, payables and six months of spending, a full return by April 2027 is worth about A$0.21 to A$0.23.

Corrections to the triage (there is no fact sheet), for the red team:
1. Yandal does not hold 50.95%. Mark Creasy's relevant interest is 50.95% (123,529,413 shares), held through Yandal Investments Pty Ltd (105,244,433, 43.41%) and Motwil Pty Ltd (18,284,980, 7.54%), both his companies [C1 substantial holders and top 20; C23 notice of 10 July 2026]. The brief repeats the triage on this.
2. "A$0.25 cash backing" is gross cash per share (A$61.4m over 242.4m shares). The A$3.57m of current income tax recorded at 30 June 2026 had not been paid by 30 September (Appendix 5B line 1.6 is nil for the quarter and the FY26 cash flow shows no tax paid) [C1 note 8 and cash flow; C2]. Net of the tax and about A$0.85m of net payables, cash is 23.5c a share; by the March 2027 quarterly it is about 21.0c at the recent spending rate. The independent expert used A$4.54m of tax, the December 2025 figure [C12 table 31].
3. The buyers of Robe Mesa named in CZR's filings are North Mining Limited (Rio Tinto), Robe River Mining Co Pty Ltd (60% Rio Tinto, 40% Mitsui Iron Ore Development) and Mitsui Iron Ore Development Pty Ltd [C1 p.22; C21]. The triage's "Rio Tinto, Mitsui and Nippon Steel" names a party CZR's filings don't.
4. The pre-deal reference close of A$0.22 on 19 June 2026 was on 22,705 shares. The last close before the announcement was A$0.20 on 25 June 2026 [D2]; against net cash after tax at 30 June (25.3c a share on the 239.4m shares then on issue) that is 0.79 times, about the same multiple as today (0.81), so the failed bid did not change how the market prices the cash.
5. The buy-back proposed on 7 October 2026 was capped at 42,529,950 shares, 10% of the shares expected after the Zuleika deal, and A$15m [C9]; Creasy's companies said they would not take part and would abstain at the meeting [C7].

## The company in plain words
CZR Resources (formerly Coziron) is a Perth explorer. It made its money in one move: the sale of its 85% of the Robe Mesa iron ore project in the West Pilbara to the Robe River joint venture (Rio Tinto and Mitsui) for A$75m cash, agreed on 17 April 2025, approved by holders on 29 May 2025 and completed on 9 September 2025, when CZR received A$70,488,534 after the exclusivity fee and the repayment of a Robe River loan [C1 p.5; C21]. An earlier A$102m sale of the same project to Miracle Iron, agreed in January 2024, was terminated on 24 February 2025 [C1 note 8; C29], and an all-scrip takeover by Fenix Resources (0.85 Fenix shares a CZR share, about 26.2c), which Creasy had said he intended to accept, lapsed on 29 April 2025 after the Robe River offer won [C22; C21].

What is left is cash and ground. CZR held A$61.4m of cash and term deposits at 30 September 2026 and no debt [C2]. It has five exploration projects, "all in joint-venture with its major shareholder, the Creasy Group": Croydon gold in the Pilbara (CZR 70%, Creasy 30%), Yarraloola iron ore (85%), Yarrie iron ore (70% to 100%), Buddadoo copper, zinc and vanadium (85% to 100%) and Shepherds Well (70%) [C1 p.3 to 5; C2 p.3; C12 MinVal table 16]. None has a mineral resource. The September quarter's money went mostly to Croydon (A$2.56m of A$3.17m), where diamond holes at Top Camp returned 3.66m at 13.6 g/t gold among weaker holes [C2].

Who runs it: chair Russell Clark (a director since September 2021, chair since November 2021); Alexander Neuling, an independent director appointed 7 May 2026; Annie Guo, a director since February 2021, who is Mark Creasy's spouse, the Group General Manager of the Creasy Group and the executive chair of Zuleika Gold. Stefan Murphy, the managing director since 2021, resigned on 7 May 2026; Milan Jerkovic has been acting chief executive since, on a A$30,000 a month consulting agreement [C1 p.25 to 27; C16].

Who owns it, at 21 September 2026 [C1 p.82 to 83]: Creasy's companies 50.95% (Yandal 43.41%, Motwil 7.54%); then Creabird Pty Ltd <EM A/C> 3.28%, Norfolk Enchants Pty Ltd <Trojan Retirement Fund> 2.06%, FMG Pilbara 1.36% (shares issued for a tenement in 2023), Rebecca Shalala 1.23%, Stefan Murphy 1.11%; the top 20 hold 68.60%; 2,286 holders; no other substantial holder.

Five years, at 30 June each year (consolidation-adjusted, from the FY26 directors' report): 25.5c (2022), 17.5c (2023), 28.5c (2024), 24.0c (2025), 20.5c (2026) [C1 p.22]. Since the Robe Mesa cash arrived the price has swung widely: 27c in September 2025, a peak of 49.5c on 5 January 2026 on the Croydon drilling, back to 20c by June 2026, and 17.5c to 19.5c since the vote [D2].

## Why big investors may be overlooking it
- Size and trading: A$46m market value; median traded value A$33,375 a day over the 20 sessions to 30 October 2026 (close times volume, Norgate) [D2]; on 6 November only 50 shares traded [D1].
- Not in the S&P/ASX 300 (the AGM notice says CZR is eligible for the 10% placement facility, which requires being outside the index and under A$300m [C3 s.7.1]).
- One holder owns 50.95% and the top 20 own 68.6%, so the free float is about A$22.6m.
- No analyst coverage turned up in the filings or the searches I ran; the only commentary found was press and promoter sites (Business News, Stockhead) [W1, W2].
- A messy history: a failed A$102m sale, a lapsed takeover, a 2021 boardroom dispute reported in the press, years of related-party loans from Creasy's Yandal at 12% a year (25% if repayment ran late, under the facility as the 2024 AGM notice described it), and now a failed related-party merger [C1 note 18; C26; W4].

## What the filings show
**Profit and cash flow.** FY26 profit after tax was A$54.9m, almost all of it the A$65.1m gain on Robe Mesa; other income was A$2.47m, mostly interest [C1 p.22]. Without the sale it is a loss-making explorer: operating cash outflow was A$4.13m in FY26, including A$3.62m of exploration [C1 cash flow]. Quarterly operating cash flow has worsened as drilling stepped up [C17; C2]:

| Quarter | Exploration | Staff | Admin and corporate | Interest received | Net operating | Cash and term deposits at end |
| --- | --- | --- | --- | --- | --- | --- |
| Sep 2025 | A$0.39m | A$0.13m | A$0.67m | A$0.07m | +A$6.14m (incl. A$7.44m GST received on the sale) | A$76.3m (incl. that GST) |
| Dec 2025 | A$0.82m | A$0.03m | A$0.30m | A$0.22m | -A$8.37m (incl. the A$7.44m GST paid on) | A$67.3m |
| Mar 2026 | A$1.00m | A$0.02m | A$0.25m | A$1.01m | -A$0.26m | A$66.9m |
| Jun 2026 | A$1.41m | A$0.06m | A$0.33m | A$0.16m | -A$1.64m | A$65.1m |
| Sep 2026 | A$3.17m | A$0.28m | A$0.93m | A$0.67m | -A$3.70m | A$61.4m |

The September quarter's corporate costs include the failed Zuleika bid (a meeting, an independent expert at A$37,500, a technical valuer, registry and media) [C2; C12 appendix A].

**The cash, and how much of it is free** (all at 30 September 2026 unless stated) [C1, C2]:
- Cash and term deposits A$61.4m: A$5.8m at call, A$5.2m in deposits under three months, A$50.4m in deposits of three to nine months.
- Less current income tax payable A$3,574,137 (recorded at 30 June 2026, not yet paid at 30 September). Old tax losses and timing differences cut FY26 tax by A$11.46m (tax effect) against the Robe Mesa gain; the unrecognised tax losses left are worth only A$0.51m of tax [C1 note 8].
- Less net payables: receivables A$1.14m against payables and provisions A$1.99m at 30 June 2026, A$0.85m net (the September figure isn't published).
- Net cash after tax: **A$56.98m, 23.5c a share**.
- Exploration commitments: A$1.40m in all, A$0.96m within a year [C1 note 31]. Free cash after commitments: A$55.6m, 22.9c a share.
- No guarantees, contingent liabilities or debt [C1 notes 18, 30]. Nothing is owed from the Robe Mesa sale: the Robe River loan was netted at completion, the Yandal loan was repaid on 11 September 2025, and Creasy's companies released their royalty and pre-emption rights over the sold tenements [C1 note 18; C21 board recommendation, Annexure C]. The sale agreement has the usual warranties and indemnities; their limits were not disclosed [C21].
- Option and rights holders: 12.3m options at 40c to 65.3c (all far out of the money) and 5.83m performance rights at nil cost [C1 p.39]. The directors' options and rights adjust for any return of capital or special dividend, so a return doesn't cost them [C28 clause 20; C18].

**What the company has said it will do with the cash.**
- April 2025, on the Robe Mesa sale: cash of about A$68m after tax "will enable CZR to develop its Retained Projects without the need for dilutive capital raisings ... while allowing it to assess new business opportunities and/or consider a return of capital to shareholders" [C21 board recommendation]; the notice of meeting repeated that "the Company may consider a return of capital to Shareholders from any surplus cash" [C21 notice, s.(d)].
- September 2025 (annual report), December 2025 (investor presentation) and March 2026 (half-year): "actively assessing capital management strategies"; "the results of these intensive exploration programs will dictate CZR's future capital requirements" [C19 likely developments; C20 corporate snapshot slide; C18].
- June to October 2026: the board proposed instead to merge with Zuleika, saying "in the world of high-risk, high-cost exploration ... we will ultimately need more money" and that the merged group, with more than A$100m, could explore "without having to tap shareholders" [C11; C10].
- 7 October 2026: an A$15m buy-back (10% of each holding at 27c, then on-market), "in response to Shareholder feedback", but only if the merger went ahead [C9; C10].
- The FY26 annual report (24 September 2026) no longer mentions capital management; the AGM notice asks for a higher directors' fee pool (A$350,000 to A$600,000, citing "expected continued growth") and the 10% placement facility "for working capital and the exploration and development of its existing projects and any future project acquisitions" [C1; C3 s.6, 7].

**The record on returning cash.** None. CZR's announcement lists from 2019 to 2026 contain no dividend, capital return or completed buy-back; the only buy-back item is the conditional one of October 2026 [C29]. In FY26 CZR paid A$798,894 to settle directors' and executives' options and rights in cash [C1 cash flow; C27].

**The failed bid.** On 26 June 2026 CZR agreed an all-scrip bid for Zuleika Gold at 0.1742 CZR shares a Zuleika share (about 182.9m new CZR shares), recommended by both independent boards [C13]. Because Yandal (526.1m Zuleika shares) and Annie Guo (92.7m) would receive CZR shares, ASX Listing Rule 10.1 required approval by CZR's non-associated holders. CZR's expert (RSM) found it fair and reasonable to them [C12]. On 23 October 2026 the holders voted it down [C4]:

| Resolution | For | Against | Abstain | Result |
| --- | --- | --- | --- | --- |
| 1. Buy Yandal's Zuleika shares | 11,223,045 (20.25%) | 44,188,824 (79.75%) | 105,256,198 | Not carried |
| 2. Buy Annie Guo's Zuleika shares | 9,703,910 (18.01%) | 44,190,883 (81.99%) | 106,773,274 | Not carried |
| 3. Buy-back (conditional on 1 and 2) | 16,595,494 (74.03%) | 5,821,498 (25.97%) | 105,577,010 | Carried, but lapsed |

The 105m abstentions are Yandal's registered shares, as it had said [C7]; Motwil's 18.3m were not voted. About 46.6% of the 118.9m shares outside Creasy's companies voted on resolution 1, and the 44.2m against are 37% of that free float. A lawyer (James Nicholls of Hamilton Locke) was appointed a director for the day to chair the meeting [C14]. CZR said the condition could not be met (26 October) and, with ASIC's consent under s652B, withdrew the bid at 8pm on 30 October 2026 [C5, C6].

**Director dealings (on-market only).** Stefan Murphy bought 100,285 shares on 12 and 13 February 2026 for A$31,075 (about 31c) [C27]. Alexander Neuling bought 272,025 shares on 26 June 2026, the day the merger was announced, for A$51,140 (about 18.8c) [C27]. Annie Guo's 266,781 shares on 17 April 2026 were an off-market trade (A$53,356) and don't count [C27]. No director sales were found in 2026.

## Valuation
Done from the filings. The question is what a holder can get for a share, so each method is a value per share at the March 2027 quarterly (31 March 2027, published by 30 April 2027), the resolve date.

**The cash at the resolve date.** Net cash after tax was A$56.98m at 30 September 2026. Net quarterly spending (exploration, staff and corporate, less interest) was A$3.70m in the September quarter with deal costs, and A$1.6m to A$2.5m a quarter before drilling stepped up. I take A$3.0m a quarter (range A$2.5m to A$3.7m), which keeps the current drilling pace and drops the deal costs:

```
net cash per share: 31 Dec 2026  22.26c (range 21.97c to 22.47c)
                    31 Mar 2027  21.03c (range 20.45c to 21.44c)
                    30 Jun 2027  19.79c
                    30 Jun 2028  14.84c
```

**Method 1: sum of the parts (what the assets are worth to an owner who controls them).** Net cash plus the exploration ground. MinVal, the independent technical valuer engaged for the Zuleika deal, valued CZR's mineral assets in August 2026 at A$10.2m to A$17.0m, preferred A$13.6m (geoscientific method; Croydon A$3.3m to A$8.5m, Yarraloola A$2.1m to A$5.1m, Yarrie A$1.0m to A$3.2m, Buddadoo A$0.9m to A$2.6m, Shepherds Well A$0.1m to A$0.4m), supported by a prospectivity-multiplier method at A$9.2m to A$11.5m [C12 MinVal tables 16 to 18].

```
at 30 Sep 2026: A$56.98m + A$10.2m to A$17.0m = A$67.2m to A$74.0m
              = 27.7c to 30.5c a share (27.1c to 29.8c with the 5.83m rights)
after RSM's 15% minority discount: 23.6c to 25.9c
at 31 Mar 2027: 21.0c cash + 4.2c to 7.0c ground = 25.2c to 28.0c
```

RSM's own sum of the parts for the merged group used the same 15% discount for a minority stake in a mainly-cash company, and its quoted-price method came out lower, which it put down to "the low liquidity in trading of CZR Shares, and the controlling interest held by Mark Creasy Entities" [C12 s.7.1 to 7.3]. Two cautions on the ground value: every project is in joint venture with Creasy's companies, so a buyer of the ground needs his cooperation; and the market has never paid for it steadily (market value less net cash after tax was about +A$56m at A$0.495 on 5 January 2026 and about -A$13m at A$0.20 on 25 June 2026, D2 against C17 and C18). Method 1 is reachable only if the cash comes back or someone buys the whole company: it is the good case, not the middle one.

**Method 2: what the market pays for cash controlled by one holder.** The measure the market uses for a cash shell is the multiple of cash per share. Three readings:
- CZR before the Zuleika deal: A$0.20 on 25 June 2026 against 25.3c of net cash after tax (A$60.7m over the 239.4m shares then on issue), 0.79 times [D2; C17 June quarterly].
- CZR now: A$0.19 against 23.5c, 0.81 times (0.75 times gross cash).
- Zuleika Gold, the other company Creasy controls (50.59%), against its cash and Catalyst Metals shares [Z2, Z3; D2]:

| Date | Zuleika price | Market value | Cash and listed shares | Multiple |
| --- | --- | --- | --- | --- |
| 31 Dec 2025 | A$0.046 | A$42.6m | A$45.9m | 0.93 |
| 31 Mar 2026 | A$0.032 | A$29.7m | A$40.7m | 0.73 |
| 30 Jun 2026 | A$0.043 (CZR bid announced) | A$39.9m | A$37.0m | 1.08 |
| 29 Sep 2026 | A$0.030 (under CZR's bid) | A$31.2m | A$42.1m | 0.74 |
| 23 Oct 2026 | A$0.028 | A$29.1m | A$42.1m | 0.69 |

Zuleika's multiple is before counting its own gold resources (MinVal: A$7.6m to A$12.7m) [C12].

So the market pays 0.69 to 0.93 times net cash for these two companies when no bid or return is in prospect, with most readings between 0.73 and 0.81. On the March 2027 cash (0.88 is shown as a high reading):

```
0.70 x 21.03c = 14.7c     0.75 x 21.03c = 15.8c
0.81 x 21.03c = 17.0c     0.88 x 21.03c = 18.5c
```

**Range.** 14.7c to 18.5c, centred on 17.0c, if the cash stays in the company (method 2, depending on the multiple and the spending); 21c to 23c if the surplus cash is returned in full or the minority is bought out at about cash (method 1 less the ground discount and costs); 25c to 28c only if someone pays for the ground at MinVal's figures as well, which no one has offered.

## The players and what the rules allow
**Mark Creasy (Yandal Investments and Motwil), 123,529,413 shares, 50.95%.** The stake has not moved by a single purchase or sale in the last two years; every change since February 2023 is dilution from option exercises and rights conversions (52.12% in July 2025, 50.95% in July 2026) [C23]. How it was built, from his notices [C23, C24, C25]:

| Date | Event | Voting power after |
| --- | --- | --- |
| Before Aug 2019 | | 72.49% |
| 9 Aug 2019 | Diluted by a placement | 62.58% |
| 24 Dec 2019 | 281.4m pre-consolidation shares issued to Yandal under 2018 and 2019 loan agreements | 66.42% |
| 18 Sep 2020 | 40m shares (and 200m options) for selling 70% of Croydon to CZR; A$498,000 in a placement at 1.2c | 58.41% |
| Jun to Jul 2021 | A$3.0m in a placement at 1.15c | 55.28% |
| Nov 2022 | A$2.07m in a 1-for-5 entitlement offer at 1.2c, then a 17-for-1 consolidation | 55.1% |
| Feb 2023 | Diluted by a shortfall placement at 20.4c | 53.15% |

What he paid: his three cash subscriptions of 2020 to 2022 (about 28m shares after consolidation) were at the equivalent of 19.6c to 20.4c; the cost of the rest (about 93m shares, besides the 2.35m received for Croydon) isn't in the notices I read. He carries the stake in private companies whose accounts aren't public. At A$0.19 his stake is worth A$23.5m; his share of the net cash is A$29.0m.

What he can afford: buying the other 118.9m shares at 22.5c would cost A$26.8m. His private company's profit was A$19.8m in FY25 (secondary [W3]); he paid A$4.26m in cash to exercise Zuleika options in November 2025 and August 2026 [Z2]. A selective buy-back (below) would use CZR's own cash instead of his.

What he wants, on the record:
1. Exploration of ground he identified, on terms that favour him. In 2020 his company Colchis Resources sold CZR 70% of Croydon for shares and options and kept 30% "free carried": CZR pays all exploration costs until a bankable feasibility study, after which Colchis can contribute, sell, or take a 2% royalty [C24 s.4.2 and terms (e) to (k)]. So when CZR spends A$2.56m a quarter on Croydon, 30% of what it finds is his outright, on top of his 51% of the rest: his economic share of Croydon is about 66% while he bears 51% of the cost. The other projects are also in joint venture with his group (Yarraloola 85/15); their carry terms weren't checked.
2. Consolidation of his companies. The Zuleika deal would have put both his cash-rich explorers under one roof with him at 50.59% and Annie Guo at 4.15% [C9 s.2.6]. He declined the buy-back and abstained [C7].
3. A sale to a strategic buyer when one comes: he said he would accept Fenix's scrip bid in February 2025 and backed the A$75m Robe River sale in April 2025, releasing his own royalty and pre-emption rights to make it work [C22; C21].
4. Cheap ways to add to his stakes rather than buying on market: loan conversions and placements at CZR; at Zuleika, 213m options exercised at 2c in November 2025 and August 2026, taking him from 42.5% to 50.59% [C23; Z2].

His record at his other controlled company: Zuleika settled its Plutonic litigation with Catalyst Metals in November 2025 for A$48m (cash and Catalyst shares, paid December 2025 to May 2026), held A$42.1m of cash and listed shares at 30 September 2026, and has returned none of it; its announcement lists for 2024 to 2026 show no dividend, capital return or buy-back [Z1, Z3]. It trades at 0.69 to 0.74 times that money. A 2025 press list of his holdings showed no other listed company above 50% [W1]; Zuleika passed 50% in August 2026.

**The board.** Clark (440,000 shares, 4.35m options, 0.6m rights) and Neuling (311,143 shares) are the independent directors; Guo (1,517,076 shares through Auracle Group, plus options and rights) is Creasy's spouse [C1 directors' interests and remuneration report; C27]. The board can buy back up to 10% of the smallest number of shares on issue in the last 12 months (about 24m shares) on market or by an equal-access offer without a holder vote; above that, or for a capital return, it needs an ordinary resolution, which Creasy's companies can carry alone [C9 s.2.1; L3]. It recommends against the nominee and wants a bigger fee pool and placement capacity [C3]. It has never proposed an unconditional return.

**The minority (118.9m shares, 49.05%).** No other holder files as substantial. Its levers:
- Listing Rule 10.1: any purchase of a substantial asset from Creasy's companies needs its approval, as on 23 October. This blocks related-party deals; it can't make the company pay out cash.
- The remuneration report: Yandal's votes were apparently not counted in 2025 (only 204,238 votes against were 1.3% of the votes cast, so about 15.7m votes in all) [C1 p.38], which fits it being treated as a closely related party of Annie Guo (my reading of s250R, not stated by CZR). If so, the minority alone decides the 26 November vote; 25% against is a first strike, and a second at the 2027 AGM puts a spill resolution, which the same exclusion would leave to the minority. At any spill meeting, though, Creasy's companies vote on who the directors are.
- Requisitioning a meeting needs 5% (s249D); removing directors needs a majority that Creasy has (s203D) [L3].

**The nominee.** Aleksandar Mihajlovic was nominated on 14 October 2026 (the deadline was 15 October) by a holder, Emefa Yawo Mihajlovic, nine days before the Zuleika vote [C3 s.8; C15]. His statement is the only reason given: a former industrial and mining electrician of 15 years turned "independent investor", self-taught, offering "a fresh approach to the boardroom". The board says it knows little of him, has not been able to run the usual checks, and recommends against; the chair will vote undirected proxies against [C3 s.8]. Neither name is in the top 20 (the smallest top-20 holding is 1,000,000 shares, 0.41%) [C1]. He needs a majority of votes cast; Creasy's companies voted at the 2025 AGM on director elections (about 140m votes for Clark's re-election, against about 16m on the remuneration report, read from the results table, whose font is encoded) [C28], so his election is in Creasy's hands. Even if elected, one director of four can't move the cash.

**Zuleika and the next attempt.** Creasy owns 50.59% of Zuleika, which has A$42.1m of cash and shares [Z2, Z3]. A merger could be tried again in a form that CZR's minority doesn't vote on, for example a Zuleika bid for CZR, which Creasy's companies could accept for their 51%; Zuleika's own non-associated holders would then probably have to approve buying Yandal's CZR shares under Listing Rule 10.1 (my reading of the rule). This is a risk for CZR's minority, not a gain.

**What the rules let a 50.95% holder do** (Corporations Act sections stated from the Act; AustLII refused the pages [L3]):
- Creep: having held more than 19% for six months, Creasy's companies may buy up to 3% every six months on market (s611 item 9). They have bought none since 2022, so the full 3% (7.3m shares, about A$1.4m) is open now.
- A takeover bid at any time (s611 item 1). Compulsory acquisition needs 90% of the shares and 75% of those bid for (s661A), that is acceptances from about 89m of the 118.9m minority shares; 44.2m voted against his last proposal.
- A capital return: an equal reduction needs an ordinary resolution (s256C), which his companies carry alone, but the board has to propose it.
- An equal-access or on-market buy-back above the 10/12 limit: an ordinary resolution (s257C) [C9]. If Creasy's companies don't take part, a buy-back lifts their stake without them paying: 10% of the minority's shares would take them from 50.95% to 53.6% (s611 item 19 exempts this).
- A selective buy-back of the minority's shares: a special resolution with no votes in favour from the sellers (s257D). His 123.5m votes carry it if fewer than 41.2m minority votes are cast against. ASIC expects takeover-style disclosure and an expert's report for a buy-back that hands a holder control or 100% (RG 110, from memory, not re-read). It would let CZR's cash buy out the minority; it has not been proposed.
- Delisting (ASX Guidance Note 33, 1 December 2019 version): a special resolution, on which a 75% holder may generally vote, but ASX can exclude a holder who gains an informational or other advantage from the delisting, and removal can't happen within a month of approval [L1 s.2.7]. With 51% Creasy can't pass it alone if more than 41.2m minority votes are cast against. ASX's listing rule changes from 21 October 2026 move the delisting framework into new Listing Rules 17.11A to 17.11C; I could not read the final text [L2].

**Comparable cases and what holders received.** Zuleika (above): the same controller, cash and listed shares received in 2025 and 2026, nothing returned, 0.69 to 0.74 times. CZR in 2025: the Fenix scrip bid at an implied 26.2c (30.3c if 75% accepted) was a 27% to 33% premium to the 10 to 60-day averages and was backed by Creasy; holders ended up with the Robe River sale and the cash in the company instead [C22]. CZR in late 2025: with the cash in hand the shares ran to 1.6 to 1.9 times cash on drilling news, then gave it all back [D2]. I could not build a list of other ASX cash shells controlled by one holder with years of prices and cash from primary sources in the time; the claim that such shells trade below cash for years rests here on Zuleika (ten months) and CZR's own record, and the red team should test it.

**The "nothing happens" value** is method 2 at CZR's own multiple on the March 2027 cash: A$0.170. At Zuleika's multiple it would be A$0.147 to A$0.158.

## Why the market is wrong
It isn't, on the evidence. The market pays 0.81 times net cash after tax, about what it paid before the Zuleika deal (0.79), more than it pays for Zuleika, and close to what method 2 says a cash shell controlled by one holder is worth. The gap to cash (about 4.5c) is the market's estimate of the cash that won't come back: spent on joint-venture ground in which Creasy has a separate carried interest, used in another related-party deal, or simply held. The minority can block a related-party deal but can't force a return, and the controller who can force one has a record and an incentive that point the other way. A partial return doesn't close the gap either, because the discount stays on what's left (the arithmetic is under "Outcomes and chances"). The case would need a reason to think Creasy now wants his cash back or wants the rest of the company; nothing filed so far says so.

## Outcomes and chances
| Outcome | What happens by 30 April 2027 | Chance | Price by resolve date |
| --- | --- | --- | --- |
| Bad | Nothing happens: CZR keeps exploring at about A$3m a quarter, no return of capital, possibly a new plan with Creasy's companies; the March 2027 quarterly shows about 21.0c of net cash after tax | 70% | A$0.170 |
| Middling | Partial capital management: an unconditional buy-back (for example 10% of each holding at about 27c, Creasy not taking part, as proposed in October) or a partial return of 8c to 15c, with the market lifting its multiple on the remaining cash to 0.85 to 0.90 | 20% | A$0.193 |
| Good | A full return of the surplus cash, or a buyout of the minority by Creasy (a bid or a selective buy-back) at about net cash plus a little for the ground, or a drilling result at Croydon that re-rates the shares | 10% | A$0.225 |

Chances add to 100%. Which valuation figure each uses: bad is method 2 at today's 0.81 multiple on the March 2027 net cash of 21.03c. Middling is the cash paid out plus method 2 at 0.85 to 0.90 on what's left:

```
27c buy-back of 10% of the minority's shares (A$3.21m): stub cash 20.72c
   0.1 x 27c + 0.9 x (0.85 to 0.90) x 20.72c = 18.5c to 19.5c
return of 8c, 10c or 15c, stub at 0.80 to 0.90:  18.4c to 19.7c, 18.8c to 19.9c, 19.8c to 20.4c
middling used: 19.3c
```

Good is method 1: the March 2027 net cash (21.03c) plus a quarter of MinVal's preferred ground value (1.4c), 22.4c; a full return keeping 2.5c a share for a slimmer explorer gives 21.6c to 23.0c. I use 22.5c.

Why these chances. Bad, 70%: in the 14 months it has held A$61m to A$76m of cash (and 19 months after first saying it might return capital), CZR has returned nothing; its controller's interests (the free carry, the merger attempt, adding to his stakes cheaply) favour spending and consolidation; the AGM notice points to growth (a higher fee pool, placement capacity); the board's last word on the cash was that "we will ultimately need more money". Middling, 20%: the independent directors have already designed a buy-back and know the minority wants one; a buy-back that Creasy declines raises his stake at no cost to him, so he has a reason to allow it; a first strike on the remuneration report on 26 November would add pressure. Good, 10%: about half for a full return or buyout (no sign in any filing; a buyout only makes sense if he wants 100%, and the cheapest route, a selective buy-back with CZR's own cash, needs a special resolution he can't be sure of), and half for drilling (Croydon carried the shares to 49.5c in January 2026, but the wet season limits Pilbara field work from December to March).

Expected price: 0.70 x 0.170 + 0.20 x 0.193 + 0.10 x 0.225 = A$0.1801, 5.2% below A$0.19.

Round-trip costs on a position of A$2,016 (NZ$2,500 at NZ$1 = A$0.8064 on 6 November 2026 [D3]): one 0.5c price step as the spread, half charged each way (2.6% in all; the quoted spread on 6 November was 1.5c); size cost of daily volatility (2.77% over 20 sessions) times the square root of A$2,016 over the 20-session average of A$45,078, 0.6% each way (1.2%); A$15 brokerage on the sale (0.74%) and on the buy if the plan's monthly cover is used up (0.74%); 0.5% to convert to Australian dollars. Total 5.1% to 5.8%.

Expected gain after costs: about -10.3% to -11.0%. The minimum (rulebook section 5a): the cash rate of 2.13% plus 5% a year over the 172 days from 9 November 2026 to 30 April 2027, 3.36%. Far below it.

What it would take: an expected price of A$0.206; with the rest at the bad price, a 65% chance of the good outcome. Or, at these chances, an entry price of A$0.166 or less (about 0.70 times the March 2027 net cash). Sensitivities, before costs: chances of 55/30/15, -2.6%; 40/30/30, +1.8%; the bad case at Zuleika's multiple (A$0.155), -10.7%.

## Dated events
- 19 November 2026: last day for written questions to the auditor [C3].
- 24 November 2026: proxies close, 11am AWST; register date for voting [C3].
- **26 November 2026: AGM**, 11am AWST, West Perth [C3]. Resolutions: remuneration report (a first strike if 25% vote against), election of Neuling, re-election of Guo, directors' fee pool to A$600,000, 10% placement facility (special resolution), and the nominee Mihajlovic. Watch for anything the chair says about the cash.
- 28 November 2026: 4,117,648 options at 47.6c expire [C1].
- By 1 December 2026 or soon after (my reading of the ATO's timing, not confirmed): payment of the A$3.57m tax, which will show in the December quarterly.
- **By 31 January 2027: December quarterly** (cash after the tax payment and any capital management decision) [C17 pattern: 15 January 2026 last year].
- About mid-March 2027: half-year accounts (11 March 2026 last year) [C18].
- **By 30 April 2027: March 2027 quarterly** (29 April 2026 last year) [C17]. Resolve by: 30 April 2027.
- Any time: a Yandal or Motwil Form 604 (creep), a proposal from Creasy, a board announcement on capital management, or a new Zuleika-related proposal.
- Outside the window: FY27 annual report (late September 2027) and the 2027 AGM (about November 2027), where a second strike would put a spill resolution.

## What would make this wrong
What would make the wait verdict wrong (that is, the shares go up):
1. Creasy decides to take the cash back or take the company private: a full capital return, or a buyout of the minority by bid or selective buy-back at about net cash. Either would put the shares at about A$0.21 to A$0.23. Nothing filed points to it, but nothing stops it either, and he is the only one who can do it.
2. Drilling. Croydon took the shares to 49.5c in January 2026; a large hit or a maiden resource at Top Camp could re-rate them whatever happens to the cash.
3. The multiple. If the market starts to price the cash at 0.9 times or more without any announcement, the bad case is too low.

What would make it worse for anyone holding: a new related-party deal (a Zuleika bid for CZR would not need CZR holders' votes), a large acquisition paid with the cash, a delisting attempt, or faster spending.

Exit rule: no position is taken. Reopen with a fresh note on any of:
1. A board announcement of an unconditional return of capital, special dividend or buy-back that, on the arithmetic above, leaves a holder with at least A$0.21 by the resolve date (roughly: a return of 15c a share or more, or a buy-back at 25c or more for at least 15% of the minority's shares).
2. Any proposal from Creasy's companies to buy the rest (a bid, a scheme or a selective buy-back). A binding one goes to the deal sleeve.
3. A Form 604 showing Yandal or Motwil buying on market.
4. A new proposal involving Creasy's companies or Zuleika, to be assessed as a separate situation.
5. The price at or below A$0.165 (about 0.70 times the latest net cash after tax) with no new related-party proposal, when the "nothing happens" value sits above the price; re-run the arithmetic on the cash in the latest quarterly before acting.

## Checks
- Not on Cam's excluded list (config/judgement_excluded.csv has no entries yet). Not a gaming, wagering, racing, lottery or casino company: a mineral explorer.
- No placement-pattern reopening in the last 30 sessions: no trading halt in 2026 (the 2026 announcement list has none [C29]), and no share issue since July 2026 [C29]; the fall from A$0.19 to A$0.175 after the vote was not a halt and reopening.
- Liquidity (section 3): median traded value A$33,375 a day over the 20 sessions to 30 October 2026 (close times volume, Norgate), which matches the triage; two sessions at 10% is A$6,675, above the research cap of 2.5% (NZ$2,500, about A$2,016) and above the A$1,500 minimum ASX order [D2, D3]. Thin days happen: 50 shares traded on 6 November.
- CZR isn't in data/prices/ASX, so the nightly price fetch would need a line before any card.
- Franking: CZR will have about A$3.57m of franking credits once it pays its tax, enough to frank about A$10.7m of dividends at its 25% rate [C1 note 8]. This is worth nothing to this portfolio (New Zealand holders can't use Australian franking credits) but could shape how any return is paid.

What I couldn't verify:
- The text of the Corporations Act sections cited (s203D, s249D, s250R, s250V, s256C, s257B to s257D, s606, s611 items 1, 9 and 19, s661A) and ASIC RG 110: AustLII refused the pages (HTTP 403). They are stated from the Act and the guide as I know them; the 10/12 buy-back limit and the ordinary resolution above it are confirmed by CZR's own notice [C9].
- ASX's new delisting rules (Listing Rules 17.11A to 17.11C, proposed to start 21 October 2026): I read only a submission on them [L2] and the 2019 Guidance Note 33 [L1].
- Who Emefa Yawo Mihajlovic is and how many shares she holds; whether any large holder (for example Creabird Pty Ltd, 3.28%) organised the vote against the merger. The "misleading and quite simply wrong information" that the chairman's letter of 7 September 2026 complained of [C11] was not found.
- Why Yandal's votes were not counted on the 2025 remuneration report; the closely-related-party reading is mine.
- The due date of the A$3.57m tax payment, and net payables at 30 September 2026 (the June figures were used).
- The carry terms of the Yarraloola, Yarrie, Buddadoo and Shepherds Well joint ventures (only Croydon's were read).
- Creasy's cost for his pre-2019 holdings, the terms of the 2018 and 2019 loan conversions, and his private companies' accounts (the FY25 profit is from a press headline [W3]).
- A longer list of controlled ASX cash shells with years of prices against cash, from primary sources.
- The Creasy notices of 2019 to 2026 and Zuleika's Yandal notices are scanned images, read by OCR; the figures used were checked against the totals in later notices and the annual report.

## Sources
CZR announcements (ASX; lists at https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=CZR&timeframe=Y&year=2026, and the same address with year=2019 to 2025):
- [C1] Annual Report 2026, 24 Sep 2026 (03143598): https://announcements.asx.com.au/asxpdf/20260924/pdf/074h88x1t2vq55.pdf (directors' report p.3 to 5 and 22 to 28; remuneration report; balance sheet; cash flow; notes 8, 11, 12, 18, 30, 31; shareholder information p.82 to 84)
- [C2] September 2026 Quarterly Activities Report and Appendix 5B, 30 Oct 2026 (03159930): https://announcements.asx.com.au/asxpdf/20261030/pdf/0760sq9r3pg00p.pdf
- [C3] Notice of Annual General Meeting, 27 Oct 2026 (03157600): https://announcements.asx.com.au/asxpdf/20261027/pdf/075tpqrh7twg18.pdf
- [C4] Results of General Meeting, 23 Oct 2026 (03156677): https://announcements.asx.com.au/asxpdf/20261023/pdf/075qhcwydly5gb.pdf
- [C5] Takeover Offer, Shareholder Approval Condition Not Satisfied, 26 Oct 2026 (03157061): https://announcements.asx.com.au/asxpdf/20261026/pdf/075s6mmdy9nqlj.pdf
- [C6] Takeover Offer for Zuleika, Notice of Withdrawal, 30 Oct 2026 (03160227): https://announcements.asx.com.au/asxpdf/20261030/pdf/0761hdyb768vwv.pdf
- [C7] Shareholder Meeting and Buy Back Intention Statements, 15 Oct 2026 (03152725): https://announcements.asx.com.au/asxpdf/20261015/pdf/075c1bpxdnyskh.pdf
- [C8] Takeover Update, Offer Declared Best and Final, 15 Oct 2026 (03152735): https://announcements.asx.com.au/asxpdf/20261015/pdf/075c2237b8w90y.pdf
- [C9] Supplementary Notice of General Meeting (buy-back), 7 Oct 2026 (03149423): https://announcements.asx.com.au/asxpdf/20261007/pdf/07515fnlnp0qg4.pdf
- [C10] Letter to Shareholders, 12 Oct 2026 (03151056): https://announcements.asx.com.au/asxpdf/20261012/pdf/0756dhmkk98f0b.pdf
- [C11] Chairman's Letter, 7 Sep 2026 (03136416): https://announcements.asx.com.au/asxpdf/20260907/pdf/073stzbhjkq9bj.pdf
- [C12] Notice of General Meeting with RSM's Independent Expert's Report and MinVal's technical valuation, 20 Aug 2026 (03127567): https://announcements.asx.com.au/asxpdf/20260820/pdf/072zlgyp7x9wv6.pdf (RSM s.7 to 9, tables 28 to 38; MinVal tables 16 to 18)
- [C13] CZR and Zuleika to Merge via Recommended Takeover Offer, 26 Jun 2026 (03108098): https://announcements.asx.com.au/asxpdf/20260626/pdf/07113k8dtv5mbs.pdf ; Bidder's Statement, 20 Aug 2026 (03127413): https://announcements.asx.com.au/asxpdf/20260820/pdf/072z7rbj8wplbt.pdf
- [C14] Appointment of Independent Director to Chair Shareholder Meeting, 23 Oct 2026 (03156449): https://announcements.asx.com.au/asxpdf/20261023/pdf/075pxmch058xpd.pdf ; Initial and Final Director's Interest Notices, J. Nicholls (03156450, 03156681): https://announcements.asx.com.au/asxpdf/20261023/pdf/075pxpl2wjcsjg.pdf , https://announcements.asx.com.au/asxpdf/20261023/pdf/075qhp23dp5y86.pdf
- [C15] Date of AGM and Closing Date for Director Nominations, 8 Oct 2026 (03149994): https://announcements.asx.com.au/asxpdf/20261008/pdf/0752rddnlzy72m.pdf
- [C16] Management and Board Changes, 8 May 2026 (03091969): https://announcements.asx.com.au/asxpdf/20260508/pdf/06zd27cmf9l9lz.pdf
- [C17] Quarterly reports: Sep 2025 (03011408) https://announcements.asx.com.au/asxpdf/20251017/pdf/06qnv64shln8j5.pdf ; Dec 2025 (03050080) https://announcements.asx.com.au/asxpdf/20260115/pdf/06v8vdk8wpmzpm.pdf ; Mar 2026 (03087564) https://announcements.asx.com.au/asxpdf/20260429/pdf/06yzlb8x7zkyl4.pdf ; Jun 2026 (03120433) https://announcements.asx.com.au/asxpdf/20260731/pdf/0728g84wwt0jfx.pdf
- [C18] Half Year Accounts to 31 Dec 2025, 11 Mar 2026 (03071027): https://announcements.asx.com.au/asxpdf/20260311/pdf/06x9zrj48jphfx.pdf
- [C19] Annual Report 2025, 25 Sep 2025 (03000341): https://announcements.asx.com.au/asxpdf/20250925/pdf/06pp6tlgs7ytlj.pdf
- [C20] Resources Rising Stars Summer Series Investor Presentation, 2 Dec 2025 (03035522): https://announcements.asx.com.au/asxpdf/20251202/pdf/06stc9jk6lktnl.pdf
- [C21] Robe Mesa sale: binding offer, 11 Apr 2025 (02937127) https://announcements.asx.com.au/asxpdf/20250411/pdf/06hms6dhsppm2f.pdf ; board recommends the Robe River offer, 17 Apr 2025 (02939544) https://announcements.asx.com.au/asxpdf/20250417/pdf/06hvwfc5k647f0.pdf ; notice of general meeting, 29 Apr 2025 (02942026) https://announcements.asx.com.au/asxpdf/20250429/pdf/06j4shkk916m9m.pdf ; results of meeting, 29 May 2025 (02953491) https://announcements.asx.com.au/asxpdf/20250529/pdf/06k7nw2zvt83t5.pdf ; conditions satisfied, 2 Sep 2025 (02990039) https://announcements.asx.com.au/asxpdf/20250902/pdf/06nqt4blhrkjl7.pdf ; completion, 9 Sep 2025 (02993146) https://announcements.asx.com.au/asxpdf/20250909/pdf/06p0qpqy965jbp.pdf
- [C22] Fenix to Acquire CZR, 25 Feb 2025 (02918306): https://announcements.asx.com.au/asxpdf/20250225/pdf/06fwvhzglrkz52.pdf ; Lapse of Fenix Takeover Offer, 30 Apr 2025 (02942860): https://announcements.asx.com.au/asxpdf/20250430/pdf/06j6w4tbg3v5kc.pdf
- [C23] Creasy, Yandal and Motwil substantial holding notices (scanned, read by OCR): 23 Aug 2019 (02137732) https://announcements.asx.com.au/asxpdf/20190823/pdf/447stblp8y5010.pdf ; 24 Dec 2019 (02189197) https://announcements.asx.com.au/asxpdf/20191224/pdf/44cwjmbj7trph2.pdf ; 22 Sep 2020 (02283894) https://announcements.asx.com.au/asxpdf/20200922/pdf/44mwj1lc0ypmw0.pdf ; 26 Jul 2021 (02399171) https://announcements.asx.com.au/asxpdf/20210726/pdf/44yn95f27h55hg.pdf ; 7 Feb 2023 (02628928) https://announcements.asx.com.au/asxpdf/20230207/pdf/45lcw6fgfxyk6t.pdf ; 18 Jul 2025 (02970398) https://announcements.asx.com.au/asxpdf/20250718/pdf/06lx7v763lxzws.pdf ; 10 Jul 2026 (03114003) https://announcements.asx.com.au/asxpdf/20260710/pdf/071lngk0563x8v.pdf
- [C24] Notice of General Meeting, Croydon (Colchis) purchase from the Creasy Group, 13 Aug 2020 (02266542): https://announcements.asx.com.au/asxpdf/20200813/pdf/44lh2p2gg1zwwy.pdf (s.4, joint venture terms (e) to (k))
- [C25] Entitlement Offer Closes, 10 Nov 2022 (02596330) https://announcements.asx.com.au/asxpdf/20221110/pdf/45hft6jllvtg7d.pdf ; Completion of Consolidation, 1 Dec 2022 (02607120) https://announcements.asx.com.au/asxpdf/20221201/pdf/45jblwldl8stmb.pdf ; Shortfall Placement, 6 Feb 2023 (02628265) https://announcements.asx.com.au/asxpdf/20230206/pdf/45lb5vg6kvm018.pdf ; Placement, 7 Jun 2021 (02382290) https://announcements.asx.com.au/asxpdf/20210607/pdf/44x5d6dvdwjr9n.pdf
- [C26] 2024 AGM notice, resolution 9 (Yandal subscription) (02873416) https://announcements.asx.com.au/asxpdf/20241028/pdf/069n66cxm43ny1.pdf ; withdrawal of resolution 9, 26 Nov 2024 (02887094) https://announcements.asx.com.au/asxpdf/20241126/pdf/06bvy4ygf6b92x.pdf
- [C27] Director's interest notices: S. Murphy 23 Jan 2026 (03052557) https://announcements.asx.com.au/asxpdf/20260123/pdf/06vjwrfbbhjk5r.pdf and 16 Feb 2026 (03060804) https://announcements.asx.com.au/asxpdf/20260216/pdf/06wcfg42b5n5mg.pdf ; A. Guo 23 Apr 2026 (03085758) https://announcements.asx.com.au/asxpdf/20260423/pdf/06ystnxlp0kb66.pdf ; A. Neuling 26 Jun 2026 (03108450) https://announcements.asx.com.au/asxpdf/20260626/pdf/0711zmg06rn3k9.pdf ; R. Clark and A. Guo 9 Jul 2026 (03113466) https://announcements.asx.com.au/asxpdf/20260709/pdf/071k1vftwwvkpv.pdf ; S. Murphy 28 Nov 2025 (03034442) https://announcements.asx.com.au/asxpdf/20251128/pdf/06spwbw3q1g2m2.pdf
- [C28] 2025 AGM notice (03013642) https://announcements.asx.com.au/asxpdf/20251022/pdf/06qw7c9ycmbpg4.pdf ; results of 2025 AGM (03033365) https://announcements.asx.com.au/asxpdf/20251127/pdf/06sm6qmwltfc5t.pdf
- [C29] ASX announcement lists for CZR, 2019 to 2026 (searched for dividends, returns, buy-backs and halts), as above.
- [C30] Postponement of General Meeting, 22 Sep 2026 (03141997): https://announcements.asx.com.au/asxpdf/20260922/pdf/074bzf2r9bmgst.pdf

Zuleika Gold (ASX:ZAG):
- [Z1] ASX announcement lists for ZAG, 2024 to 2026: https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=ZAG&timeframe=Y&year=2026
- [Z2] Yandal and Creasy notices for ZAG (scanned, read by OCR): 20 Nov 2025 (03029096) https://announcements.asx.com.au/asxpdf/20251120/pdf/06s7p2hs9smhkc.pdf ; 18 Dec 2025 (03043007) https://announcements.asx.com.au/asxpdf/20251218/pdf/06thpjq54xrk8b.pdf ; 10 Aug 2026 (03123588) https://announcements.asx.com.au/asxpdf/20260810/pdf/072lnzdz98nlqg.pdf ; 3 Nov 2026 (03161541) https://announcements.asx.com.au/asxpdf/20261103/pdf/0765pvpylbchvl.pdf ; CZR ceasing to be a substantial holder in ZAG, 30 Oct 2026 (03160574) https://announcements.asx.com.au/asxpdf/20261030/pdf/07629xqmck5pc0.pdf
- [Z3] ZAG quarterly reports: Dec 2025 (03054851) https://announcements.asx.com.au/asxpdf/20260130/pdf/06vrzzkpnj3w9j.pdf ; Mar 2026 (03089004) https://announcements.asx.com.au/asxpdf/20260430/pdf/06z34hvbl1w08v.pdf ; Jun 2026 (03120701) https://announcements.asx.com.au/asxpdf/20260731/pdf/072937j3rf97nb.pdf ; Sep 2026 (03160662) https://announcements.asx.com.au/asxpdf/20261030/pdf/0762jbpp0frfxn.pdf
- [Z4] Annie Guo notices for ZAG: 17 Dec 2025 (03042549) https://announcements.asx.com.au/asxpdf/20251217/pdf/06tgfff2jf5jdr.pdf ; 20 Mar 2026 (03074569) https://announcements.asx.com.au/asxpdf/20260320/pdf/06xnkmk0rt9rrc.pdf

Rules:
- [L1] ASX Listing Rules Guidance Note 33, Removal of Entities from the ASX Official List (1 December 2019): https://www.asx.com.au/documents/rules/gn33_removal_of_entities.pdf (s.2.7, 2.10)
- [L2] Law Council of Australia, submission of 29 July 2026 on ASX's listing rule amendments from 21 October 2026 (published 18 September 2026): https://www.asx.com.au/content/dam/asx/about/regulations/public-consultations/2026/law-council-of-australia-20260918.pdf
- [L3] Corporations Act 2001 (Cth) sections listed under "What I couldn't verify": AustLII returned HTTP 403 for each page, e.g. https://www.austlii.edu.au/cgi-bin/viewdoc/au/legis/cth/consol_act/ca2001172/s257d.html

Data:
- [D1] data/research_data/asx_company.json (CZR header and key statistics, fetched 7 November 2026 UTC)
- [D2] Norgate Data in this repository, data/norgate/universe/prices_2019.csv.gz to prices_2026.csv.gz (CZR.au, ZAG.au), to 30 October 2026
- [D3] data/fx/fx_daily.csv (NZ$1 = A$0.806387 on 6 November 2026)

Secondary (named because no primary source was found for these points):
- [W1] Stockhead, "Who is the next multi-bagger on Mark Creasy's roster?" (2025, undated page): https://stockhead.com.au/resources/who-is-the-next-multi-bagger-on-mark-creasys-roster
- [W2] Business News, "Mark Creasy backed CZR, Zuleika to merge", 26 June 2026 (paywalled; headline and summary only): https://www.businessnews.com.au/article/Mark-Creasy-backed-CZR-Zuleika-to-merge
- [W3] Business News, "Mining billionaire Mark Creasy's private company reports sharp profit fall", 3 November 2025 (paywalled; A$19.8m FY25 profit from the visible text): https://www.businessnews.com.au/article/Mining-billionaire-Mark-Creasy-s-private-company-reports-sharp-profit-fall
- [W4] MiningNews.net, "Mass resignation at Creasy-controlled CZR" (undated, paywalled; the managing director and two directors resigned over Robe Mesa plans): https://www.miningnews.net/leadership/news/1417042/mass-resignation-creasy-controlled-czr
