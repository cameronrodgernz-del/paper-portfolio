# Jumbo Interactive (ASX:JIN): deep dive. Not a value pick at A$6.31: over two years the bad case is 13% below the price with dividends counted. Wait for the 1H FY27 result (about 25 February 2027) and the Dream UK earn-out

Written 2026-11-08 by the research desk. Price at writing: A$6.31 (last trade on Friday 6 November 2026; the close on 5 November was A$6.37; ASX company data in data/research_data/asx_company.json, fetched 7 November 2026 [M1]; Norgate's last close in the repo is A$6.01 on 30 October [M2]). Market value: A$395.7m (62,709,839 shares on issue after the 3 November 2026 cancellation, Appendix 3H [J14]).
Status: finished. Verdict: **wait for a named event**: the 1H FY27 result, due about 25 February 2027 (a preliminary came three weeks early last year, on 4 February 2026 [J6]), which will also carry the Dream UK earn-out outcome (payable after 31 December 2026). No card, no red team. Not a value pick at A$6.31: to 30 September 2028, with dividends counted, the bad case (A$5.52) is 12.6% below the price, against the 10% the rule allows, though the middling case (A$8.12) is 28.7% above it. As an ordinary pick to 31 March 2027 the expected gain is +3.5% before costs and +0.7% after them, against a minimum of +2.8%. The exact conditions and prices that reopen it are under "Dated events". This is a simulation and not financial advice.
Fact sheet: research/facts/JIN.md (8 November 2026), grade B on Tabcorp's multiple and C at the company's own discount rates. Its question: at about five times FY27 EBITDA, is the market right to price Jumbo as if the TLC reseller agreements (47% of revenue) might not be renewed when they end on 25 August 2030, and do the other businesses carry the value? Its "our way" anchor: A$8.33 (Tabcorp's 5.96 times on A$101.3m of EBITDA); "against us" A$4.60.

Value pick (rulebook section 5a): tested both ways, as the brief asked. Not a value pick at A$6.31 (bad case -12.6% with dividends, middling +28.7%). It would pass every value-pick test at A$6.13 or below with nothing else changing, and at up to about A$6.95 if the 1H FY27 result confirms the middle earnings path (conditions under "Dated events").

Order of work. The brief and the fact sheet quoted the price, so it was in view from the start. The filings, the earnings paths, both valuation methods and the peer multiples were worked from Jumbo's, TLC's and ZEAL's own documents first; Jumbo's price enters only in one line that backs out what the market is paying, in "Why the market is wrong" and in "Outcomes and chances". Arithmetic was run in `python3 -I` from scratch scripts (not committed); the key lines are shown.

> In short. Liquidity passes easily (median A$847,504 traded a day over the 20 sessions to 30 October [M2]). The peer the brief asked for, the multiple the market pays for an online lottery reseller, is **ZEAL Network SE (XETRA:TIMA)**, Germany's listed online lottery broker (LOTTO24 and Tipp24), which earns commissions from the state lottery companies for the tickets it sells online, the same job Oz Lotteries does for TLC. ZEAL trades at about 11 to 12 times this year's EBITDA (about 10 times next year's) [Z1][Z3][Z5]. Jumbo trades at 4.9 times FY27 EBITDA on the middle of its guidance. The gap is not an oversight. ZEAL sells under a licence from the German states' joint gambling regulator, under a State Treaty with no expiry date, for the German state lottery companies, whose moves against brokers its own risk report says are subject to competition law [Z1]. Jumbo sells under four linked contracts with one counterparty, TLC, that end on 25 August 2030; TLC can end them on 30 days' notice if Jumbo changes hands [J13]; and since July 2026 TLC's own digital unit runs with a mandate to grow a digital share from which reseller sales are excluded [T1]. So ZEAL's multiple belongs only to the part of Oz Lotteries' value that comes after a renewal. Valued that way (Method 1), with my odds of 25% renewal on similar terms, 45% renewal at a worse fee and 30% no renewal, the business is worth about A$8.83 a share; on the company's own impairment-test discount rates (Method 2) it is worth about A$6.26. The price, A$6.31, is exactly Method 2's central value. The fact sheet's A$8.33 anchor needs FY25-level jackpot earnings and the top of international guidance, both together, and no bidder can be the mechanism because of the change-of-control clause: it is the good case, not the middle. Two things the fact sheet underplays cut the middle: HM Treasury said on 17 February 2026 that paid prize-draw entries "will be subject to VAT at the standard rate of 20%", HMRC wrote to operators in July 2026, and Jumbo's FY27 Dream UK guidance assumes the old exempt treatment [U1][U2][J1 note 32][J2]; and ZEAL bought SevenCanyon, a UK prize-draw business of about Dream UK's size, for about 3.5 to 4 times EBITDA in July 2026, against the 6.5 times Jumbo paid for Dream UK nine months earlier [Z4][J9]. What decides the next move is the 1H FY27 result: whether the jackpot recovery (nine large jackpots worth A$430m in July to October, against seven and A$300m a year earlier [J3]) lifts Australia onto the middle path, what happens to Dream UK's VAT and how much of the £12m earn-out is paid.

Corrections and additions to the fact sheet, for the record:
- The right peer is ZEAL (online lottery reseller, about 11 to 12 times EBITDA), not Tabcorp (wagering). The brief asked for this; Tabcorp's 5.96 times is used nowhere below.
- The 2020 renewal was not "on similar terms". It was signed about three years before the then expiry of May 2023, cost Jumbo a A$15m upfront fee, and raised the service fee from 1.5% to 4.65% of the ticket price [J13]. That is the precedent for 2030: an early renewal is possible, and so is a worse fee.
- Missing from the fact sheet: the 2020 binding terms let TLC (then Tabcorp) end each reseller agreement on 30 days' notice on a change of control of Jumbo [J13]. A takeover is therefore not a realistic route to value unless TLC consents or is the buyer. The 2026 annual report describes the cross-default between the four agreements but does not repeat this clause, so I can't confirm it survived into the long-form agreements [J1].
- The "reseller era" quote on TLC's investor-day slide 34 is a history timeline (mid-2000s reseller era, early 2010s digital launched in-house, FY17 to FY26 embedded era, standalone digital unit from FY27) [T1]. It is not a statement about Jumbo's renewal. What matters more is the footnote: under TLC's new structure reseller sales sit in Lotteries and are excluded from Digital's turnover and digital mix [T1], so TLC's Digital unit gains nothing from Jumbo's sales and a lot from taking them over ("each 1% lift in digital share = c.$6m in EBITDA").
- Dream UK VAT is more than "uncertain". Jumbo's own annual report says Dream UK has treated its entries as VAT-exempt, puts the exposure for October 2025 to June 2026 at A$2.9m to A$3.9m of profit, and says periods before the purchase are covered by insurance [J1 note 32]. HM Treasury and HMRC have both stated the opposite view [U1][U2].
- The fact sheet's Dream values have no market check. ZEAL's SevenCanyon purchase (about £35m upfront for 100%-equivalent, earn-out up to £4.8m, EBITDA "more than £10m") is about 3.5 to 4 times EBITDA [Z4]; SevenCanyon then contributed only €1.4m of EBITDA in its first quarter in ZEAL [Z3].
- Small ones: the founders of Dream UK run it only through the earn-out period ending 31 December 2026 [J9]; 2.75m of the CEO's 8.99m shares are held by LGT Crestone "as custodian for a secured financing arrangement" [J15]; FY26 free cash flow on the company's own definition was A$47.0m after interest [J2 slide 21], and the lease payments (A$2.1m) come off that.

## The company in plain words
Jumbo has four businesses [J1][J2]:
- Lottery Retailing (Oz Lotteries): an authorised online reseller of TLC's national draw games (Powerball, Oz Lotto, Saturday Lotto) in every state and territory except Queensland and Western Australia, under four reseller agreements with TLC subsidiaries that run to 25 August 2030 "with renewal negotiations 9 months prior to expiry" [J1]. It also sells charity lotteries and its own products (Daily Winners). FY26: ticket sales (TTV) A$419.8m, revenue A$103.5m (A$90.2m from TLC games, A$13.3m from charity and other products), underlying EBITDA A$33.2m. It pays TLC a service fee of 4.65% of the ticket price [J2 slide 37]. About 736,000 active players, down from 1,091,000 in FY22 [J2 slide 7].
- SaaS: licenses the Jumbo Lottery Platform to 11 charity and government lotteries, including Lotterywest's "Lotterywest by OzLotteries" channel, and charges Lottery Retailing for running Oz Lotteries. FY26 revenue A$42.5m, of which A$30.7m was the internal charge and A$11.8m came from outside clients; EBITDA A$26.7m. RSL Queensland went live on 15 August 2026 (about A$200m of ticket sales a year) [J2 slides 8, 17][J3].
- Managed Services: runs charity lotteries end to end, Gatherwell and StarVale in the UK and Stride in Canada. FY26 revenue A$28.4m, EBITDA A$8.4m [J2 slide 18]. Stride is buying Raffle Management Group in Ontario for C$3.95m upfront plus up to C$2.5m, about 4.4 times EBITDA, completing about January 2027 [J4 slide 12].
- Dream Giveaways: online prize draws for cars, cash and houses, Dream UK (bought 14 October 2025) and Dream US (bought 30 October 2025). FY26 (8 to 8.5 months) net revenue A$53.6m, EBITDA A$21.8m [J2 slide 19].

Who runs it: Mike Veverka, founder (1995), managing director and CEO; Susan Forrester, chair; Jatin Khosla, CFO, leaving at the end of 2026 with no successor named [J3][J19]. Brad Board, COO, oversees Dream [J3].

Who owns it: no institution is now a substantial holder; Macquarie, Citigroup, First Sentier and MUFG filed ceasing notices between 10 and 28 September 2026, and Pinnacle in June [J17]. The largest registered holders at 31 July 2026 were custodians (HSBC 14.83%, Citicorp 13.05%, J P Morgan 11.83%) and Veverka's Vesteon Pty Ltd (8.53%) [J1 shareholder information]. Veverka's total interest after his 21 September purchase is about 8.99m shares (14.3%): 5,541,422 in Vesteon, 2,750,000 with LGT Crestone for a secured financing arrangement, and about 0.7m in his super fund [J15].

The last three years, with the share price over five:

| | FY24 | FY25 | FY26 |
| --- | --- | --- | --- |
| Revenue (A$m) | 159.3 | 145.3 | 193.6 |
| Underlying EBITDA (A$m) | 76.6 | 68.3 | 85.2 |
| Statutory NPAT (A$m) | 43.3 | 40.2 | 34.6 |
| Australia underlying EBITDA (A$m) | 69.7 | 61.1 | 55.0 |
| Large jackpots (A$30m or more) / their total (A$m) | 32 / 1,930 | 31 / 1,530 | 23 / 960 |
| Dividend (c) | 54.5 | 54.5 | 27.0 |

Share price at 30 June: A$17.77 (2021), A$14.22 (2022), A$14.26 (2023), A$17.29 (2024), A$9.80 (2025), A$6.50 (2026).

Sources [J2][J12][M2]. The company gives five-year growth rates from FY21 to FY26 of 18% a year for revenue, 10% for EBITDA and 8% for operating cash flow [J4 slide 4]. The share price was A$11.39 on 2 January 2026 and fell to a low of A$5.64 on 18 September 2026, the last day before its removal from the S&P/ASX 300 [M2][J16].

## Why big investors may be overlooking it
- Index exit: removed from the S&P/ASX 300 effective 21 September 2026 [J16]. On 18 September, the rebalance day, 6.29m shares traded (about 10% of the company) and the close was A$5.64, down 13.4% [M2]. Every institution still on file as a substantial holder filed a ceasing notice that month [J17].
- Size: A$396m market value; about A$0.85m traded a day.
- A messy year: two acquisitions funded with A$118m of new debt, the dividend payout cut from 65% to 85% of profit to 30% to 50%, a 42.27% vote against the CEO's one-off retention grant at the 6 November AGM, and the CFO leaving [J2][J5][J19].
- A sector out of favour: gambling, plus Citi's "AI risk discount" on software in March 2026 (price target cut from A$11.80 to A$9.90; Stockopedia report, secondary) [S1].
- Not overlooked by analysts: Citi, Morgans, Macquarie and Morningstar all publish on it (press reports, secondary) [S1].
So the index exit and the sector apply; neglect doesn't. A 17.3% fall on 25 June 2026 on 1.33m shares [M2] has no Jumbo or TLC announcement behind it that I could find [J17][T2].

## What the filings show
Profit and cash, FY26 (year to 30 June 2026) [J1][J2]:
- Revenue A$193.6m (+33%), underlying EBITDA A$85.2m (+25%), underlying NPATA A$50.6m (80.2c a share); statutory NPAT A$34.6m (54.8c). The A$8.7m of pre-tax one-offs were A$3.3m of deal costs, A$3.8m of Dream US deferred revenue written off in the acquisition accounts, a A$0.9m TLC service fee catch-up for past periods and smaller items [J2 slide 34]. Amortisation of acquired intangibles was A$11.5m in FY26 and the company shows A$16m a year for FY27 and FY28 [J2 slides 35, 42].
- Operating cash flow A$51.1m after A$22.2m of tax, A$4.4m of bank interest and A$0.8m of lease interest; capital spending A$7.8m (A$6.9m software, A$0.8m equipment); lease principal A$1.3m [J1 cash flow statement]. The company's free cash flow (operating cash before deal costs, less capex and interest) was A$47.0m; less lease principal, about A$45.7m, or 72c a share [J2 slide 21].
- Balance sheet at 30 June 2026: A$78.6m drawn on a A$120m ANZ facility due October 2028 (covenants: net leverage no more than 3 times, interest cover at least 2 times); cash A$48.1m, of which A$12.1m is customer money, so A$36.0m is Jumbo's own; net debt A$42.6m; lease liabilities A$16.6m; the Dream UK earn-out carried at A$22.4m [J1 notes 16, 21, 23][J2 slide 20]. Inventories jumped to A$16.2m (prize cars). Net tangible assets are negative: A$226.9m of the A$325.9m of assets are intangibles, A$92.1m of them goodwill [J1].

What is committed, not free:
- The Dream UK earn-out: up to £12m (about A$23m) in cash "post 31 December 2026" if "certain revenue growth and earnings hurdles are met". It was valued at acquisition at £11.16m, a probability-weighted estimate discounted at 6%, so Jumbo expected to pay nearly all of it [J1 note 23][J9].
- Raffle Management Group: C$3.95m upfront about January 2027 and up to C$2.5m after 31 December 2027 [J4 slide 12].
- The FY26 final dividend (15c, about A$9.4m) was paid on 17 September; FY27 buy-backs so far about A$4.3m, and A$1.12m went on a minimum-holding buy-back on 3 November [J2 slide 20][J3][J14].
- Possible VAT on Dream UK: A$2.9m to A$3.9m for October 2025 to June 2026 on Jumbo's own estimate, plus penalties and interest it can't estimate, and a further amount each year if HMRC's view stands [J1 note 32].

Capital raisings: none for cash in two years. 1,012,161 shares were issued at about A$9.80 as part of the Dream UK price (out of escrow 15 October 2026) [J9][fact sheet]. Buy-backs: 1,643,882 shares since 2022 for A$15.78m, the lowest at A$5.64 on 18 September 2026 [J14]. Director trades in the last three months are on-market buys: Veverka 34,000 at an average A$5.86 (21 September) and Malone 10,950 at A$5.89 (30 September) [J15].

The TLC agreements, from the documents:
- Four agreements, signed August 2020 for ten years to 25 August 2030, with renewal negotiations 9 months before expiry; a material breach or unremedied default under one lets TLC end all four; TLC audits Jumbo every year; 47% of FY26 group revenue [J1].
- History: Jumbo has resold TLC's games (Tabcorp's before TLC was demerged) since 2005, and the agreements "have been renewed on several occasions" [J1]. The last renewal was agreed on 28 June 2020, about three years before the then expiry, for a A$15m fee plus a service fee rising from 1.5% to 4.65% [J13]. On about A$400m of tickets the fee step alone is about A$12.6m a year. Tabcorp called the new terms "more sustainable commercial terms" [J13].
- Change of control: the 2020 terms let TLC end each agreement on 30 days' notice if Jumbo "fails to perform its obligations, enters into similar arrangements with third parties, or there is a change of control of Jumbo" [J13].
- TLC's stance: from FY27 its Digital unit is standalone "with its own mandate", and reseller sales are "excluded from Digital turnover and digital mix" [T1 slides 33 to 34]. TLC put out no announcement about resellers in 2026 [T2].
- Jumbo's impairment test assumes the agreements "continue beyond current agreement periods" [J1 note 10]. The board's case for the CEO's one-off grant (vesting only if he stays to 30 June 2030) names the TLC renewal as one reason [J3].

The other contracts and risks:
- Lotterywest gave its new gaming and digital system to Brightstar in December 2025, go-live targeted for the third quarter of 2027; Jumbo could not agree terms on the player account part, talks on the website and app part continue, and its existing Lotterywest SaaS agreement is unchanged [J11][J2 slide 8]. From the annual report's growth figures (outside SaaS ticket sales +15.1% overall, +18.6% without Lotterywest, Lotterywest -2.1%; revenue +12.3% and +20.1%), Lotterywest is about 17% of outside SaaS ticket sales and, if its revenue fell about 2%, about a third of outside SaaS revenue, roughly A$3.5m a year (my estimate) [J1].
- Dream UK VAT: above. Jumbo's guidance assumes "existing VAT treatment continues to apply" [J2 slide 26][J4 slide 15].
- Dream UK's founders stay only to 31 December 2026 [J9]; Jumbo hired a commercial leader in July and a marketing head in August 2026 [J2 slide 13].

FY27 guidance (27 August, reaffirmed 6 November 2026): Australia underlying EBITDA margin 46% to 50%; International (Managed Services and Dream) A$36m to A$40m, made up of Dream UK £11.3m to £11.8m, Dream US US$5.6m to US$6.2m and mid single digit growth in Managed Services, at A$1 = £0.52, US$0.72, C$0.99; payout 30% to 50% of statutory NPAT [J2 slide 26][J3][J4]. Record: in FY26 4 of 5 guidance measures were met; Dream UK hit its original range but missed the February upgrade [J2 slide 5].

Trading since June: the first four months of FY27 had nine large jackpots with A$430m of Division 1 prizes, against seven and A$300m a year earlier, including a A$100m Powerball in October, the first in 16 months [J3]. For scale, the whole of 1H FY26 had 10 and A$410m [J6].

## Valuation
### The earnings paths
Three paths for FY27 and after, from the guidance and the history above. Australia's revenue is Lottery Retailing (A$101m like FY26's jackpots, A$108m like FY25's, A$118m between FY25 and FY24's A$123.4m) plus outside SaaS (A$15.5m to A$16.7m: FY26's A$11.8m plus RSL Queensland, at the guided 3.25% to 3.5% of about A$480m of outside tickets) plus Dream US's platform fee (A$1.2m to A$1.4m); times the guided margin.

| A$m | Low | Middle | High |
| --- | --- | --- | --- |
| FY27 Australia revenue x margin = EBITDA | 117.7 x 46% = 54.1 | 125.3 x 48% = 60.1 | 136.1 x 50% = 68.0 |
| FY27 International (guidance), less VAT | 36.0 - 1.5 = 34.5 | 38.0 - 1.0 = 37.0 | 40.0 |
| FY27 group EBITDA | 88.6 | 97.1 | 108.0 |
| Australia from FY28 (grows 2% a year) | 55.0 | 60.0 | 64.0 |
| Lotterywest channel lost from FY29 | -3.0 | -1.5 | 0 |
| International growth FY28 to FY30 | 0% | 4% | 7% |
| Dream UK VAT from FY28, net of price rises; back VAT in FY28 | -7.0; -4.0 | -4.0; -3.5 | 0 |
| FY29 group EBITDA | 82.1 | 96.8 | 111.1 |

Free cash flow each year: EBITDA, less capex (A$6.5m Australia, A$1.8m International), leases (A$2.5m), tax at 30% on Australian and 25% on International EBITDA less depreciation; in FY27 also the earn-out at its £12m face (A$23.1m) and RMG's A$3.95m. FY27 free cash before those two: A$55.7m, A$61.8m, A$69.6m (before interest of about A$3.5m).

What happens at 25 August 2030 (FY31 counts 10 of 12 months):
- renewed on similar terms: nothing changes;
- renewed with a squeeze: Australian EBITDA falls A$15m a year (A$20m low path, A$10m high), about one more 2020-sized fee step;
- not renewed: Australian EBITDA falls to what the platform's outside clients and charity products earn after cutting costs (A$2m, A$4m, A$6m), with A$5m of restructuring.

My odds: 25% similar, 45% squeeze, 30% not renewed. Reasons: 21 years of renewals and a TLC that keeps a 4.65% fee plus its game margin on about A$400m of Jumbo's sales; against that, 2020 was renewed only at a much higher price, and TLC's Digital unit now has every reason to want those players. I also show a "market" view (15/35/50) and a "worse" view (12/28/60).

### Method 1: the online lottery reseller multiple (ZEAL Network)
ZEAL Network SE (XETRA:TIMA) brokers German state lottery tickets online and is paid commissions by the state lottery companies; since July 2026 it also owns SevenCanyon, a UK prize-draw business [Z1][Z4]. Its multiple:
```
shares 21,681,785 - 581,832 treasury = 21.10m (31 Dec 2025) x EUR39.90 (4 Nov 2026) = EUR841.9m
net debt: 31 Dec 2025 loans 86.5 + leases 1.5 - (cash 118.6 - customer money 17.7) = -12.8 (net cash);
  30 Jun 2026 about 1 (Stock Analysis); after the SevenCanyon purchase (GBP33.8m, EUR40m loan) about 15 to 40
EV EUR857m to EUR882m
/ 2026 EBITDA guidance midpoint 72.5            = 11.8x to 12.2x
/ 77.5 (before the mid-single-digit EURm deal costs in the guidance) = 11.1x to 11.4x
/ about 85 for 2027 (SevenCanyon for a full year) = 10.1x to 10.4x
normalised free cash yield: (68.8 EBITDA - 30% tax on 60.1 EBIT - capex 1.0 - leases 1.0 - interest 4.1) / 841.9 = 5.3%
```
Sources [Z1][Z2][Z3][Z5][Z6]. I use **11 times** EBITDA as the online lottery reseller multiple. ZEAL's price implies a return of roughly 8% to 9% a year (5.3% cash yield plus 3% growth); I discount Jumbo's cash at 10%.

Why ZEAL's multiple can't be applied to Oz Lotteries today: ZEAL brokers under a licence from the German states' joint gambling authority (13 private brokers held one), under a State Treaty that "has no expiry date and can be terminated by individual federal states no sooner than 31 December 2028"; it sells for the German state lottery companies, and its own risk report says moves by them against brokers "are subject to antitrust restrictions and may be reviewed by the courts" [Z1]. Oz Lotteries has one counterparty and a fixed end date. So in Method 1 the Australian business earns its cash to August 2030, and is then valued at 11 times EBITDA (mid-2032) only if TLC renews, or at 6 times what is left if it doesn't. Dream is valued at 5 times EBITDA (between SevenCanyon's 3.5 to 4 times [Z4] and the 4.7 to 6.1 times Jumbo paid on FY27 guidance [J9][J10]); Managed Services at 6 times (RMG 4.4 times upfront, 7.2 times with its earn-out [J4]).

| Method 1, A$ a share | renewed, similar | renewed, squeeze | not renewed | my odds | market odds | worse odds |
| --- | --- | --- | --- | --- | --- | --- |
| Low path | 9.76 | 7.45 | 3.38 | 6.81 | 5.76 | 5.28 |
| Middle path | 11.72 | 9.99 | 4.68 | **8.83** | 7.60 | 7.01 |
| High path | 13.65 | 12.50 | 6.08 | 10.86 | 9.46 | 8.79 |

Sensitivity, middle path, my odds: reseller multiple 9 times A$8.13, 12 times A$9.18; Dream at 3.75 times A$8.50, 6 times A$9.10; discount rate 9% A$9.23, 12.5% A$7.92.

For scale, if Oz Lotteries' access were as secure as ZEAL's, a plain sum of the parts on FY27 would be: Australia A$60.1m x 11 = A$662m, Dream UK (A$22.2m less A$4m VAT) x 5 = A$91m, Dream US A$8.2m x 5.5 = A$45m, Managed Services A$8.8m x 6 = A$53m; EV A$850m, less A$82.3m of net debt, leases and earn-out, about A$12.2 a share. That number is not on offer to anyone while the 2030 date stands.

### Method 2: cash-flow value at the company's own discount rates
The same cash flows, discounted at the rates in Jumbo's own impairment test [J1 note 10]: Lottery Retailing and SaaS 17.5% before tax (12.25% after tax at 30%); Dream UK 22.8%, Dream US 27.6%, Managed Services UK 19.3% and Canada 16.1% before tax, about 15.5% after tax blended for International; growth 2% after FY32.

| Method 2, A$ a share | renewed, similar | renewed, squeeze | not renewed | my odds | market odds | worse odds |
| --- | --- | --- | --- | --- | --- | --- |
| Low path | 6.46 | 4.99 | 2.63 | 4.65 | 4.03 | 3.75 |
| Middle path | 8.00 | 6.90 | 3.86 | **6.26** | 5.54 | 5.21 |
| High path | 9.54 | 8.80 | 5.18 | 7.90 | 7.10 | 6.72 |

On the middle path Australia is worth A$363m if renewed on similar terms, A$297m with a squeeze and A$115m if not; International A$174m in every case.

### Cross-check: cash yield
FY27 free cash to shareholders on the middle path, before the earn-out and RMG and after interest: about A$59.3m, or 95c a share. ZEAL's normalised cash yield is 5.3%. NPATA on the middle path is about A$58.8m (94c), and a 45% payout of statutory profit would be about 33c.

### Range
What the business is worth, before looking at the price: **A$6.26 (Method 2) to A$8.83 (Method 1) on the middle path with my odds, midpoint about A$7.55**; low path about A$4.65 to A$6.81; high path about A$7.90 to A$10.86. The answer depends mostly on two inputs no filing settles: the odds TLC renews (the not-renewed values are 40% to 60% below the renewed ones) and the discount rate (Method 2's rates are 3 to 7 points above what ZEAL's price implies).

Only now the price. A$6.31 is A$395.7m; adding net debt of about A$36.8m (A$42.6m at 30 June, plus A$14.8m paid out since, less about four months of free cash), leases of A$16.6m and the earn-out of A$23.1m gives an EV of about A$472m: **4.86 times middle-path FY27 EBITDA** (5.54 times FY26's actual). Method 2's middle-path value with my odds implies 4.83 times. Method 1's implies 6.49 times. ZEAL trades at 11 to 12 times.

## Why the market is wrong
It mostly isn't, at A$6.31. The price equals Method 2's central value: on the company's own discount rates, with a 30% chance TLC walks away, the shares are fairly priced. To call the market wrong I would have to say either that Jumbo's Australian cash deserves something nearer ZEAL's rate of return (Method 1, about A$8.8), or that the market is pricing the low path. Neither is shown by any dated event inside two years: TLC's renewal talks start about November 2029, and the one thing that could settle it earlier, a 2020-style early renewal, has no sign in either company's announcements [J17][T2].

What the market may be getting wrong, and what would show it:
1. The earnings path. If the market is pricing the low path (more years like FY26, VAT taken in full by Dream UK, Lotterywest gone), the price sits near Method 1's low-path value with market odds (A$5.76) or Method 2's low path with my odds (A$4.65); a 1H FY27 result on the middle path would move fair value up by A$1.60 to A$2.00 a share. The first four months' jackpots point that way [J3].
2. Forced selling has passed. The index exit is done, the institutions that were going have gone, and the directors bought at A$5.86 and A$5.89 [J15][J16][J17].
3. The cash carries the wait. At A$6.31 the shares cost about 6.7 years of the middle path's free cash to shareholders (95c a share), and the buy-back has about A$9m left. If nothing changes, a holder earns roughly the company's own discount rate (about 13% a year) from cash, debt repayment and dividends while the renewal question stays open.

Point 3 is what makes the value-pick test close; points 1 and 2 are what the 1H result can test.

## Outcomes and chances
Prices come from EBITDA on each path times the multiple that path supports in the valuation above, less net debt and leases at the resolve date (from each path's cash flows, dividends and buy-backs), plus dividends received in the window. The multiples: 4.86 times is Method 2's middle-path value with my odds (and today's market multiple); the bad cases use 4.3 times (six months) and 4.0 times (two years), between Method 2's low-path values with my odds (4.15 times) and market odds (3.71 times), and lower over two years because the 2030 date is closer; the two-year good case uses 5.66 times, the midpoint of Methods 1 and 2 on the middle path with my odds.

### As an ordinary pick, resolve by 31 March 2027 (143 days; after the 1H FY27 result, the earn-out outcome and the interim dividend, ex about 3 March)
| Outcome | What happens | Chance | Price by resolve date |
| --- | --- | --- | --- |
| Bad | The 1H shows the low path: Australia near the bottom of its margin range on softer revenue, Dream UK books VAT or misses its range, a small or no earn-out because Dream UK missed its hurdles, guidance trimmed. FY27 EBITDA A$88.6m at 4.3 times | 25% | A$5.02, plus a 12c interim: A$5.14 (-18.5%) |
| Middling | In line: Australia about A$29m for the half on the jackpot run, International on guidance, earn-out paid at or near £12m, VAT still disputed. FY27 EBITDA A$97.1m at 4.86 times (Method 2, middle path, my odds) | 50% | A$6.55, plus 13c: A$6.68 (+5.8%) |
| Good | The high path: FY24-like jackpot earnings in the half (Australia A$32m or more), Dream ahead and VAT settled in Jumbo's favour. FY27 EBITDA A$108.0m at 4.86 times | 25% | A$7.48, plus 14c: A$7.62 (+20.8%) |

Expected value A$6.53: **+3.5% before costs, +0.7% after**. Minimum (rulebook section 5a): (2.13% + 5%) x 143 / 365 = 2.79%. Fails. It would pass at A$6.19 or below (6.53 / 1.0554).

### As a value pick, resolve by 30 September 2028 (692 days; FY27 and FY28 results, two AGMs, four dividends)
| Outcome | What happens | Chance | Price by resolve date |
| --- | --- | --- | --- |
| Bad | Low path: VAT on Dream UK with little passed on, Lotterywest channel lost, Australia stuck at about A$53m, no TLC news as the expiry nears. FY29 EBITDA A$82.1m at 4.0 times; net debt and leases A$20.7m | 25% | A$5.02, plus 50c of dividends: A$5.52 (-12.6%) |
| Middling | Middle path, renewal still open, market keeps today's multiple. FY29 EBITDA A$96.8m at 4.86 times; net debt and leases A$12.2m | 50% | A$7.47, plus 65c: A$8.12 (+28.7%) |
| Good | Middle path and the market moves halfway to the reseller value (an early renewal, as in 2020, or TLC signalling it wants resellers). FY29 EBITDA A$96.8m at 5.66 times | 25% | A$8.73, plus 65c: A$9.38 (+48.7%) |

Expected value A$7.79 (price alone A$7.17): **+23.4% before costs, +20.7% after**, against a minimum of (2.13% + 5%) x 692 / 365 = 13.5%. The middling leg passes (+28.7% against +15%); the bad leg fails (-12.6% against -10%). Both legs and the minimum pass at **A$6.13 or below** (bad leg 5.52 / 0.9 = 6.13; middling leg 8.12 / 1.15 = 7.06; minimum leg 7.79 / 1.163 = 6.70). With 30/50/20 chances instead, the expected gain after costs is still about +17.5%.

The bad leg is the weak point and it is sensitive: at 4.5 times the bad case is about -3%; at 3.5 times about -24%. I use 4.0 times because Method 2's low-path values sit at 3.7 to 4.2 times today, and the market will have less time before 2030 by then.

Round-trip costs: a 2.5% position is about A$2,016. Half the spread each way (Corwin and Schultz, 0.72% over 21 sessions and 0.96% over 60, about 0.8% in all), size cost 0.08% each way (daily volatility 1.76%, average day A$972,533), brokerage A$15 each way (0.74%) unless the plan's monthly cover applies, and 0.5% each way to buy Australian dollars if none are held. That is 1.0% to 3.5%; I use 2.75%. Liquidity limit (section 3): 2 sessions x 10% x A$847,504 = A$169,501, far above the position.

## Dated events
- Dream UK earn-out: the period ends 31 December 2026; payment "post 31 December 2026", likely shown in the 1H FY27 accounts as paid or remeasured [J1 note 23][J9]. Dream UK's founders leave at the same time.
- CFO change at the end of 2026; successor to be named [J3][J19].
- 1 January 2027: Australia's gambling reforms take effect; Jumbo calls them a net positive [J3].
- About January 2027: RMG completes [J4].
- Possible preliminary 1H result in early February 2027 (4 February in 2026) [J6]; the 1H FY27 result about 25 February 2027 (25 February 2026, 21 February 2025); interim dividend ex about 3 March, paid about 18 March [J7].
- Third quarter of 2027: Lotterywest's Brightstar system goes live [J11]. About late August 2027 and 2028: FY27 and FY28 results; AGMs in early November.
- October 2028: ANZ facility matures [J1]. About 25 November 2029: TLC renewal talks; 25 August 2030: expiry [J1].

What reopens it:
1. Before the result, on price alone, with no new announcement from Jumbo, TLC, HMRC or the UK Treasury: a close at or below **A$6.13** reopens it as a value pick to 30 September 2028 (re-run the outcomes first; subtract the interim dividend from the trigger once it goes ex). A close at or below A$6.19 before 25 February would also clear the ordinary-pick minimum, but the value pick is the better frame.
2. After the 1H FY27 result, reopen as a value pick if it shows all of: Australia underlying EBITDA for the half of A$29m or more at a margin of 47% or more; Dream UK half EBITDA of £5.4m or more, with VAT either still treated as exempt and no HMRC assessment disclosed, or accounted for with FY27 Dream UK guidance still at £10m or more after it; the earn-out paid or provided at £10m or more; bank debt less own cash at 31 December 2026 of A$40m or less before the earn-out is paid; FY27 guidance kept; no change to the TLC agreements. On those figures the bad case moves up to about A$6.29 with dividends (FY29 EBITDA of A$89.5m, halfway between the low and middle paths, at 4.0 times), and both value legs pass at a price up to about **A$6.95**. Re-run the outcomes with the reported figures before any card.
3. It closes (a value pick only at about A$4.97 or below, where the middling leg binds) if the result shows the low path: Australia below A$27m for the half, Dream UK guidance cut by more than 15%, a VAT assessment or settlement that takes Dream UK below £9m a year, or the earn-out largely unpaid because Dream UK missed its hurdles. Any announcement by TLC about reseller terms, early talks or its intentions for 2030 makes it a fresh deep dive whichever way it points.

## What would make this wrong
1. TLC. Everything above Method 2's not-renewed value (A$3.86 on the middle path) rests on a renewal. TLC's Digital unit now runs without credit for reseller sales; TLC put the value of each point of digital share at about A$6m of EBITDA; and in 2020 the price of a renewal was A$15m plus a fee three times higher [T1][J13]. If TLC signals before 2028 that it won't renew, or will only renew at terms that take A$20m or more a year out of Australia, the shares go to about A$4 to A$5 and no dividend stream makes that up. The change-of-control clause also means no bidder is likely to put a floor under the price.
2. Dream UK. The second leg of the business was bought at 6.5 times EBITDA, and the market price for a UK prize-draw business nine months later was 3.5 to 4 times [J9][Z4]. HMRC's view on VAT is plain, Jumbo's guidance assumes it wins that argument, the founders leave in December, and the UK's new subscription rules arrive in 2027 [J1][U1][U2]. VAT with no price rise would take about A$6m to A$8m a year off International EBITDA (Jumbo's own A$2.9m to A$3.9m after tax for 8.5 months of FY26, scaled to a full year before tax); a write-down of Dream UK would not hit cash but would hit the board's credibility.
3. Luck. Jackpots drive Oz Lotteries; FY26 was, in the company's words, a 1-in-45-year outcome [J3]. Active players fell from 1.09m to 0.74m in four years and new accounts from 423,000 to 144,000 in two [J2 slide 7]; if that is structural rather than jackpot-driven, the middle path is too high.

Exit rule, if it is ever picked: sell on any TLC announcement that shortens, worsens or puts in doubt Jumbo's access; on a Dream UK guidance cut of more than 15% or a VAT assessment above A$10m; on Australia's half-year margin below 46%; otherwise at the resolve date.

## Checks
- Not on Cam's excluded list: config/judgement_excluded.csv has no entries; the 8 November 2026 confirmation line opens gaming, wagering and racing names.
- No placement-pattern reopening in the last 30 sessions (rulebook section 9): no trading halt and no share issue for cash in 2026; the September and October quotations were 1,786 to 6,055 shares at a time from rights and options converting (Appendix 2A, e.g. 16 Sep 2026, 03140100) [J17].
- Liquidity: median value traded over the 20 sessions 5 to 30 October 2026 A$847,504 a day (lowest A$591,701), from data/norgate/universe/prices_2026.csv.gz [M2]. Under section 3 the most the position can be is A$169,501; a 2.5% position (about A$2,016) is about 0.2% of a day.
- Could not verify: ZEAL's net debt at 30 September 2026 (its nine-month release doesn't give it; I used Stock Analysis's 30 June figure plus the SevenCanyon loan, a range of €15m to €40m); ZEAL's closing price on Xetra (I used €39.90 from a 4 November report, secondary); whether the change-of-control right survived into the 2020 long-form agreements; the exact earn-out hurdles; Lotterywest's share of SaaS revenue (my estimate from the annual report's growth figures); why the shares fell 17% on 25 June 2026; exchange rates since August.

## Sources
Jumbo (ASX:JIN)
- J1. 2026 Annual Report, 27 Aug 2026 (03130890): operating and financial review, material contract risk, notes 10 (impairment), 16 (leases), 21 (borrowings), 23 (business combinations, earn-out), 32 (contingencies, VAT), cash flow statement, shareholder information: https://announcements.asx.com.au/asxpdf/20260827/pdf/073941lldwlrxd.pdf
- J2. Amended FY26 Results Investor Presentation, 27 Aug 2026 (03131490), slides 3 to 8, 15 to 21, 26, 34 to 42: https://announcements.asx.com.au/asxpdf/20260827/pdf/073bj6554g6qn2.pdf
- J3. AGM Chair and CEO Addresses, 6 Nov 2026 (03162871): https://announcements.asx.com.au/asxpdf/20261106/pdf/0769kjffsf3v6g.pdf
- J4. 2026 AGM Presentation, 6 Nov 2026 (03162875), slides 4, 12, 14, 15: https://announcements.asx.com.au/asxpdf/20261106/pdf/0769kt3b9gz5h0.pdf
- J5. Results of Meeting, 6 Nov 2026 (03163048): https://announcements.asx.com.au/asxpdf/20261106/pdf/076b0lkqhl4c2g.pdf
- J6. Preliminary 1H26 Financial Results, 4 Feb 2026 (03056506): https://announcements.asx.com.au/asxpdf/20260204/pdf/06vy4jt4f68wsl.pdf
- J7. 1H26 Results Presentation, 25 Feb 2026 (03064561): https://announcements.asx.com.au/asxpdf/20260225/pdf/06wqb9qk2cgwhd.pdf ; 1H26 dividend notice (03064553), ex 3 Mar 2026, paid 18 Mar 2026: https://announcements.asx.com.au/asxpdf/20260225/pdf/06wq9rpg5rxlwy.pdf
- J9. Acquisition of Dream Car Giveaways, 15 Oct 2025 (03009981): https://announcements.asx.com.au/asxpdf/20251015/pdf/06qk424rq1496z.pdf ; investor presentation (03009984): https://announcements.asx.com.au/asxpdf/20251015/pdf/06qk48cv9gmndl.pdf
- J10. Strategic acquisition of Dream Giveaway (USA), 30 Oct 2025 (03017973): https://announcements.asx.com.au/asxpdf/20251030/pdf/06r821q51fq749.pdf
- J11. Lotterywest contract awarded to Brightstar Lottery, 18 Dec 2025 (03043015): https://announcements.asx.com.au/asxpdf/20251218/pdf/06thq7p89d7vyr.pdf
- J12. FY25 Results Investor Presentation, 26 Aug 2025 (02985266), Australia segment and Lottery Retailing tables with FY24, consolidated results: https://announcements.asx.com.au/asxpdf/20250826/pdf/06nbb433rngn98.pdf
- J13. Jumbo, "Long running channel partnership with Tabcorp extended for 10 years to 2030", 29 Jun 2020 (02248933): https://announcements.asx.com.au/asxpdf/20200629/pdf/44k107sphmdf1r.pdf ; Tabcorp, "Changes to reseller arrangements with Jumbo", 29 Jun 2020 (02248888): https://announcements.asx.com.au/asxpdf/20200629/pdf/44k0xffv12rhm9.pdf
- J14. Appendix 3H, 3 Nov 2026 (03161589), 62,709,839 shares: https://announcements.asx.com.au/asxpdf/20261103/pdf/0765v998b9ljyf.pdf ; buy-back update, 6 Nov 2026 (03162757): https://announcements.asx.com.au/asxpdf/20261106/pdf/07699b6gncwrjw.pdf
- J15. Appendix 3Y M Veverka, 25 Sep 2026 (03144053): https://announcements.asx.com.au/asxpdf/20260925/pdf/074jjpymvsn694.pdf ; Appendix 3Y M Malone, 1 Oct 2026 (03147181): https://announcements.asx.com.au/asxpdf/20261001/pdf/074t9tjhr4sb98.pdf
- J16. S&P DJI September 2026 Quarterly Rebalance, 4 Sep 2026 (03136141), S&P/ASX 300 removals effective 21 Sep 2026: https://announcements.asx.com.au/asxpdf/20260904/pdf/073rbz4q8nrckg.pdf
- J17. ASX announcement list for JIN, 2026 (substantial holder notices, share issues, no trading halts): https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=JIN&timeframe=Y&year=2026
- J19. Jumbo announces CFO transition, 29 Sep 2026 (03145475): https://announcements.asx.com.au/asxpdf/20260929/pdf/074p09s60xkwwh.pdf

The Lottery Corporation (ASX:TLC)
- T1. 2026 Investor Day Presentation, 3 Jun 2026 (03100430), slides 33 to 35: https://announcements.asx.com.au/asxpdf/20260603/pdf/0707xf20nl0lwz.pdf
- T2. ASX announcement list for TLC, 2026: https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=TLC&timeframe=Y&year=2026

ZEAL Network SE (XETRA:TIMA)
- Z1. Annual Report 2025 (shares and treasury shares, balance sheet, cash and customer balances, cash flow, State Treaty, risk report): https://mailing-ircockpit.eqs.com/crm-mailing/5b80569d-ea7c-11e8-902f-2c44fd856d8c/3ba0ddfc-1858-4e5a-8eaf-105eaa4b9fda/3d303913-c983-49b9-b599-47f2dc0b0874/ZEAL_Network_Annual+Report_2025_EN.pdf
- Z2. H1 2026 release, 5 Aug 2026 (EQS, as carried by gettex): https://www.gettex.de/en/news-overview/newsdetail/eqs-news-zeal-continues-its-growth-trajectory-and-reports-highest-first-half-revenue-in-the-companys-history/
- Z3. Nine-month 2026 release, 4 Nov 2026 (as carried by webdisclosure): https://www.webdisclosure.com/press-release/zeal-increases-nine-month-revenues-by-22-and-successfully-diversifies-into-new-markets-3Ut2rTET2rX
- Z4. "ZEAL acquires SevenCanyon and enters the highly attractive UK prize draw market", 9 Jul 2026 (EQS, as carried by gettex): https://www.gettex.de/en/news-overview/newsdetail/eqs-news-zeal-acquires-sevencanyon-and-enters-the-highly-attractive-uk-prize-draw-market/
- Z5. Share price €39.90 on 4 Nov 2026 (goldesel.de, secondary): https://goldesel.de/aktien/news/zeal-network-aktie-umsatzprognose-2026-steigt-nach-starkem-q3-auf-bis-zu-280-millionen-euro
- Z6. Stock Analysis, ZEAL statistics as at 28 Sep 2026: 21.10m shares, debt €82.47m, cash €98.95m (secondary): https://stockanalysis.com/quote/etr/TIMA/statistics/

UK VAT on prize draws
- U1. Written answer by the Exchequer Secretary, 17 Feb 2026 (Parallel Parliament, secondary copy of the UK Parliament record): https://parallelparliament.co.uk/question/111960/prize-money-vat
- U2. HMRC One to Many letter on VAT and prize draws, July 2026 (ICAEW copy): https://www.icaew.com/-/media/corporate/files/insights/tax-news/2026/august-2026/hmrc-one-to-many-campaign-vat-and-prize-draws-july-2026.ashx ; ICAEW news item: https://www.icaew.com/insights/tax-news/2026/aug-2026/hmrc-writes-to-businesses-running-prize-draws

Other
- S1. Citi price target cut, 8 Mar 2026 (Stockopedia, secondary): https://www.stockopedia.com/share-prices/jumbo-interactive-ASX:JIN/news/australia-apos-s-jumbo-interactive-falls-as-citi-cuts-pt-on-ai-valuation-risks-019e6a12-d630-794f-b617-3d5162b4261e/ ; Motley Fool Australia JIN news list (Morgans, Macquarie mentions, secondary): https://fool.com.au/tickers/asx-jin/page/2
- M1. data/research_data/asx_company.json (fetched 7 Nov 2026): last trade A$6.31 on 6 Nov 2026, prior close A$6.37, 62,709,839 shares.
- M2. data/norgate/universe/prices_2021.csv.gz to prices_2026.csv.gz (Norgate): prices, volumes, 20-session liquidity, spread and volatility to 30 Oct 2026.
- Fact sheet: research/facts/JIN.md (8 Nov 2026).
