# Research candidates, 21 November 2026

The weekly research sweep (rulebook section 5a, docs/RESEARCH_TASK.md). Places to look for the next company, not buy signals: one company is chosen in chat, then the case for, the case against, the debate and Cam's decision. This is a simulation and not financial advice.

Data dates:
- ASX screen: Norgate's whole-market export as of 30 October 2026 (22 days old, inside the six-week limit). It passes six weeks on 11 December, so it wants refreshing before the sweep of 12 December. ASIC share counts and shorts with it.
- NZX screen: closes to 13 November 2026 (five to 12 November). The exchanges' company data was fetched again on 21 November (tools/research_company_data.py, no refusals).
- Prices quoted below: the ASX's own company data (last trade at 20 November) and NZX closes of 20 November. The stored closes in data/prices stop at 16 November because the nightly job has failed its rate test since 17 November.
- Sweep: reports/research_sweep.md, run dated 21 November so that this week's headlines count (left to itself it dates the run by the newest screen price, 13 November, and misses them): 599 on the screen, 28 software companies left out, 241 tagged. Ranking: reports/research_rank.md (249 ranked, 35 special situations). Substantial holder builds are from the last run of tools/holder_notices.py, not refreshed this week.
- Announcements read from the ASX announcements pages and the NZX announcements API on 21 November 2026 (NZ time). Sixteen NZX company lists returned HTTP 403 and were not retried (research/picks/INDEX.md, note 13).

Left out on the rules or on reading: live deal targets (the deal sleeve's 17, now including Mayne Pharma and Metro Glass), Cam's excluded list (empty, confirmed 8 Nov), software, and companies deep-dived since mid-August unless reopened or moved 15% or more. Most of the top 30 are again explorers and developers that have raised money while losing it (Kalamazoo, True North Copper, Caspin, Forrestania, Fortifai and others); their bad case is another raising and there's no floor. Lotus (LOT, A$0.155) has the forced sellers (it left the S&P/ASX 300 in September) but its Kayelekera restart produced 101.8klb in the September quarter and is selling 173klb of off-specification product at a discount ([11 Nov](https://announcements.asx.com.au/asxpdf/20261111/pdf/076grfjs7y0gk0.pdf)), so its bad case is another raising too. Mach7's 17 Nov notices are option expiries, not buys ([notice](https://announcements.asx.com.au/asxpdf/20261117/pdf/076phw87w0wjdf.pdf)); Decidr AI is an AI business Cam would likely put under his 9 Nov exclusion (not assumed: to raise with him if it ever matters). Vysarn (a director bought A$59,639 on 6 Nov, [notice](https://announcements.asx.com.au/asxpdf/20261111/pdf/076hfnlrgpf88g.pdf)) and Lark Distilling (a new director bought A$24,043, [notice](https://announcements.asx.com.au/asxpdf/20261109/pdf/076d953r2vxzs0.pdf)) are small signals. humm has a board contest (a section 203D notice from Rangeley Capital, [16 Nov](https://announcements.asx.com.au/asxpdf/20261116/pdf/076n7r761v06w8.pdf)) but was deep-dived on 8 Nov and has moved less than 15%. Steel & Tube's four-month update was better (normalised EBITDA NZ$7.1m against NZ$1.6m, facilities extended to 2028, [NZX 483879](https://www.nzx.com/announcements/483879)), but it was rejected as too thin to trade and still is.

## 1. ASX:ATG, Articore Group (reopened)

- Price A$0.315, market value about A$94m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/ATG/header)).
- Where found: the watch list. It closed at its A$0.345 trigger on 10 November, before the December quarter update, and the evening desk marked it reopened (research/picks/INDEX.md). It has fallen another 11% since last week with no announcement at all since 14 November (the ASX's 2026 list for ATG).
- Why the price could be wrong: on the deep dive's own outcomes (A$0.22, A$0.39, A$0.55 at 30%, 50%, 20%) the expected price is about A$0.37, some 18% above today's before costs, and the fall has come with no news.
- Hard floor: none. The A$40.5m of cash is all float (free cash about minus A$5.2m at June 2026, research/picks/ATG.md). At A$0.315 the bad case is 30.2% below the price, just outside the value test.
- What Cam might read better: an online marketplace (Redbubble, TeePublic) whose profit comes from cost cuts rather than sales; whether cutting paid marketing is shrinking the customer base.
- The question: is gross profit after paid marketing holding at -4% to +3% in constant currency through the Christmas quarter, or is the drift in the price someone who knows the sales decline is speeding up? The deep dive is not re-run here; the reopen means it is re-run against today's price and the file's conditions.

## 2. ASX:SMG, Seven Media Group, formerly Southern Cross Media (reopened)

- Price A$0.41, market value about A$208m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/SMG/header)).
- Where found: the watch list. It closed A$0.44 on 16 November, at its trigger, with nothing else changed since the 5 November AGM update the deep dive used, and the evening desk marked it reopened on 17 November (research/desk_log.md). The only releases since are plan paperwork: Rohan Lund's grant of 3,526,221 performance rights for nil cash on 18 November, and two notices about unquoted and cancelled securities ([Appendix 3Y, 20 Nov](https://announcements.asx.com.au/asxpdf/20261120/pdf/076vwsc9ndzv0l.pdf)).
- Why the price could be wrong: the deep dive's outcomes (A$0.30, A$0.46, A$0.66 at 30%, 45%, 25%) give an expected price of about A$0.46, about 13% above today's before costs, with the Stokes group at 23.19% and able to buy another 3% from about 17 February 2027 (research/picks/SXL.md).
- Hard floor: none. Net debt is about A$363m against the A$208m market value, so each A$10m of EBITDA is worth about 8.4c a share either way.
- What Cam might read better: radio and regional TV under the limits on wagering advertising from 1 January 2027, a rule change in Cam's own field.
- The question: does the cost programme hold first-half EBITDA at A$96m or more (the file's close-out level) against a shrinking TV ad market and the end of Google news payments?

## 3. ASX:ASG, Autosports Group (reopened today)

- Price A$0.97, market value about A$205m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/ASG/header)).
- Where found: the watch list. It closed A$0.995 on 13 November, at its A$1.00 trigger, and the 20 November AGM gave H1 FY27 revenue of A$1.70bn to A$1.75bn but no profit figure, said the order banks were maintained and that European supply arrives in H2 FY27, with new-vehicle order writing up 18% for four months ([AGM addresses, 20 Nov](https://announcements.asx.com.au/asxpdf/20261120/pdf/076ty2jd0cjwxt.pdf)). That meets the second reopen condition in research/picks/ASG.md (A$1.00 or below, A$20m or more or no figure, timing unchanged), so it is marked reopened in research/picks/INDEX.md.
- Why the price could be wrong: on the file's cautious chances (40% A$0.60, 45% A$1.23, 15% A$1.88) the expected price is about A$1.08, some 11% above today's before costs.
- Hard floor: none, and debt is the risk: each 0.25% on rates costs about A$3m a year in interest (the AGM addresses).
- What Cam might read better: a multi-site prestige car dealership network, his own ground: whether cutting stock at "temporary gross margin costs" is a sign of a bad first half or a sensible clean-up before supply arrives.
- The question: the address calls the half "challenging" and gives no profit figure where last year's AGM gave one, so is H1 normalised profit above or below A$20m? Below it, the file's kill condition applies.

## 4. ASX:CTT, Cettire

- Price A$0.225, market value about A$93m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/CTT/header)).
- Where found: the sweep's second name (director buying after a 66% fall; a holder that isn't a fund building a stake), then this week's AGM update. Four months to October: sales revenue A$246.2m (+15%), delivered margin 17.1% (15.3%), adjusted EBITDA A$6.9m (A$4.6m), net cash A$27m and no debt, after the employee share trust spent A$2.6m buying 7.0m shares on market ([trading update, 18 Nov](https://announcements.asx.com.au/asxpdf/20261118/pdf/076qrvvjkh5s12.pdf)). The price has fallen 29% since last week. Founder Dean Mintz bought 11,437,140 shares on market on 30 September at about A$0.239 ([Appendix 3Y](https://announcements.asx.com.au/asxpdf/20261001/pdf/074t79swqmz54w.pdf)), taking him to about 39%. The remuneration report passed with 93.5% ([AGM results](https://announcements.asx.com.au/asxpdf/20261118/pdf/076rr55mwybzyw.pdf)).
- Why the price could be wrong: the shares fell by almost a third on an update showing higher margins and profit, to below what the founder paid seven weeks ago.
- Hard floor: net cash A$27m (29% of the market value), plus a non-binding term sheet to factor €16.1m of VAT receivable for at least €13.7m, about A$22m ([market update, 29 Sep](https://announcements.asx.com.au/asxpdf/20260929/pdf/074p9zw6s7pq29.pdf)); the founder's own price, about A$0.239.
- What Cam might read better: online luxury retail and how far discounting, returns and duties eat margin, now with US sales down 3% and paid acquisition up to 5.9% of sales.
- The question: did the market sell on the cash (A$41m a year earlier, A$27m now) and the US, and is Mintz, already at 39% and allowed to add 3% from about April 2027, the likely buyer of the company at a low price?

## 5. ASX:GEM, G8 Education (a special situation)

- Price A$0.17, market value about A$132m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/GEM/header)).
- Where found: last week's news, still the gap of the list. On 12 November G8 received a non-binding A$0.26 cash scheme proposal from Majority Capital Partners with a scrip option, bank and equity commitment letters and up to six weeks' exclusivity, and the directors intend to recommend a binding deal ([process deed](https://announcements.asx.com.au/asxpdf/20261112/pdf/076j2yjqrjg2r6.pdf)); Allan Gray, manager of 19.59%, supports it ([13 Nov](https://announcements.asx.com.au/asxpdf/20261113/pdf/076kwhtf32hxfv.pdf)). Nothing has been announced since. Not binding, so not in the deal sleeve.
- Why the price could be wrong: at A$0.17 against A$0.26 the market prices roughly a 45% chance of a binding deal (taking the 8 Nov deep dive's middling A$0.09 as "nothing happens"), with the board and the largest holder on side and exclusivity running to about 24 December.
- Hard floor: none in the assets (A$0.04 to A$0.20 on its own, research/picks/GEM.md). The deep dive is within three months, but the price is about 70% above the A$0.10 it was written at, so it qualifies.
- What Cam might read better: a regulated childcare network with a Fair Work Ombudsman case and covenant waivers: what a buyer's due diligence will find in occupancy, wages and the regulator's view.
- The question: what are the odds Majority Capital signs at or near A$0.26 by the end of exclusivity, and where does G8 trade if it walks away?

## 6. ASX:MCA, Murray Cod Australia

- Price A$0.14, market value about A$42m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/MCA/header)).
- Where found: the sweep (12 director notices after an 87% fall, latest 16 Nov). Director Brett Paton bought on market five times from 4 to 10 November, 1,079,846 shares for about A$164,000 at A$0.146 to A$0.164, taking him to 26,278,501 shares ([4 Nov](https://announcements.asx.com.au/asxpdf/20261105/pdf/0768wwrd0ktsmf.pdf), [5 Nov](https://announcements.asx.com.au/asxpdf/20261106/pdf/076b8jb59f1szy.pdf), [6 Nov](https://announcements.asx.com.au/asxpdf/20261109/pdf/076dkr8vg1xlz6.pdf), [9 Nov](https://announcements.asx.com.au/asxpdf/20261110/pdf/076fxrj49xw9c5.pdf), [10 Nov](https://announcements.asx.com.au/asxpdf/20261116/pdf/076m72pkq1sq5x.pdf)).
- Why the price could be wrong: a director is buying with his own money at about a third of book value, A$125.1m of net assets at June 2026 ([FY26 preliminary report](https://announcements.asx.com.au/asxpdf/20260831/pdf/073gpnnfslfg2r.pdf)).
- Hard floor: land, buildings, water rights and licences carried at revalued amounts, inside net assets of A$125.1m with borrowings of about A$26.6m and cash of A$4.1m (same report). Much of the rest is fish at fair value.
- What Cam might read better: a regulated primary producer (water licences, aquaculture) whose FY26 loss of A$5.4m came on revenue of A$13.5m and a A$29.5m fair value gain on fish.
- The question: what are the water rights and land worth on their own, and is the fish valuation real or the source of the 87% fall?

## 7. ASX:NTD, NTAW Holdings

- Price A$0.19, market value about A$33m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/NTD/header)).
- Where found: the sweep (holders that aren't funds building a stake). Tony Young went from 16.80% to 21.25% and Ryan Young from 15.10% to 19.40% over four notices to 21 September ([form 604, 22 Sep](https://announcements.asx.com.au/asxpdf/20260922/pdf/074cmsbmk8fvsq.pdf); reports/holder_builds.md). Director John Cunningham bought 250,000 on market at A$0.20 on 28 September ([Appendix 3Y](https://announcements.asx.com.au/asxpdf/20261002/pdf/074vysg6k0hn3t.pdf)). A large holder ceased on 28 September and the WA assets of Black Rubber were sold in July.
- Why the price could be wrong: two holders named Young, together about 40%, keep buying a tyre distributor that is shrinking to its core and paying down debt (bank debt down A$13.9m in FY26, [FY26 presentation](https://announcements.asx.com.au/asxpdf/20260827/pdf/073b8lm3vrb5hx.pdf)), which is either a cheap creep toward control or a read on value.
- Hard floor: none; net debt with leases is about A$126m (sweep, from the exchange's data), more than the shares, so the bad case may be a raising.
- What Cam might read better: tyre wholesale and retail networks in Australia and New Zealand (Tyres4U New Zealand, a new NZ wheel business, Carter's Tyre), multi-site and partly NZ, his ground.
- The question: are the two Youngs associated, and if so how close are they to a control threshold, and can the business carry its debt without a raising at this price?

## 8. ASX:MMI, Metro Mining

- Price A$0.815, market value about A$259m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/MMI/header)).
- Where found: the sweep (a substantial holder left; director buying after a 55% fall). Pinnacle ceased to be a substantial holder on 28 October ([form 605](https://announcements.asx.com.au/asxpdf/20261030/pdf/07623kdqt2n0sb.pdf)); four directors then bought about A$190,000 on market at about A$0.80 ([Ritchie](https://announcements.asx.com.au/asxpdf/20261103/pdf/0765mhh2f458nf.pdf), [Purdie and others](https://announcements.asx.com.au/asxpdf/20261106/pdf/0769lps1kzkzd8.pdf)); October shipments were 752,000 tonnes with the channel fixed ([9 Nov](https://announcements.asx.com.au/asxpdf/20261109/pdf/076cn7kmggt56k.pdf)). No announcement since 14 November.
- Why the price could be wrong: a fund sold out after a weather and channel problem that looks temporary, and the directors bought just after at the price it trades at now.
- Hard floor: none in assets; the directors' price, about A$0.80. Cash A$16.8m and secured debt US$24.8m at 30 September ([quarterly](https://announcements.asx.com.au/asxpdf/20261029/pdf/075y30tpq2d987.pdf)).
- What Cam might read better: little; a single-mine bauxite exporter.
- The question: what does Bauxite Hills earn in a normal 7m-tonne year at today's bauxite price, and was 2026's shortfall a one-off?

## 9. ASX:AIS, Aeris Resources

- Price A$0.31, market value about A$503m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/AIS/header)).
- Where found: the sweep (substantial holders left; a demerger). Tribeca ceased to be a substantial holder on 9 November ([form 605](https://announcements.asx.com.au/asxpdf/20261109/pdf/076dll92yq5s9q.pdf)), after two others in September. The 19 November AGM showed cash of A$128m and no debt, with Constellation stripping under way ([AGM presentation](https://announcements.asx.com.au/asxpdf/20261119/pdf/076sn4h724wzb4.pdf)). The price is down 19% on the week.
- Why the price could be wrong: funds are leaving a debt-free copper and gold producer while it spends on Constellation, so the selling may be about the spending, not the value.
- Hard floor: cash A$128m and no debt, about a quarter of the market value (AGM presentation; A$178.7m of cash and receivables at 30 September, [quarterly](https://announcements.asx.com.au/asxpdf/20261029/pdf/075ymmb93f60cz.pdf)).
- What Cam might read better: nothing in particular.
- The question: what are Tritton, Cracow and Constellation worth after the build spend, and does the cash last until Constellation produces?

## 10. NZX:WHS, The Warehouse Group

- Price NZ$0.71, market value about NZ$246m, net tangible assets NZ$0.56 a share (NZX instrument data, close of 20 November).
- Where found: last week's NZX announcements and Cam's own ground. The Q1 FY27 update: group sales NZ$678.8m (+0.7%), same-store sales +0.1%, gross margin 33.5% (+110 basis points), The Warehouse +170 points to 37.1% ([NZX 483608, 13 Nov](https://www.nzx.com/announcements/483608)). No announcement since.
- Why the price could be wrong: the market values a NZ$3bn-a-year retailer at about 8% of sales on FY26's thin profit, while each point of gross margin on that sales base is worth roughly NZ$30m a year before costs.
- Hard floor: none found yet; owned property and the balance sheet are for a deep dive.
- What Cam might read better: whether store discipline and range changes are lasting margin gains through the festive quarter, or promotional timing.
- The question: does the margin recovery carry into FY27 profit well above FY26's NZ$11.2m once wages, rent and interest are counted?

## Last week's list

None of the seven was chosen for a deep dive this week (no new file in research/picks, research/against or research/debate since 14 November).

- ATG, Articore: reopened, not yet re-run; A$0.355 to A$0.315 (-11%), no news. Kept, first.
- GEM, G8 Education: passed over; A$0.18 to A$0.17 (-6%), no news since the 13 Nov Allan Gray letter. Kept.
- CTT, Cettire: passed over; A$0.315 to A$0.225 (-29%) after the 18 Nov update. Kept, higher.
- WHS, The Warehouse: passed over; NZ$0.695 to NZ$0.71 (+2%). Kept.
- MMI, Metro Mining: passed over; A$0.855 to A$0.815 (-5%), no news. Kept.
- NZL, New Zealand Rural Land: passed over; NZ$0.91 to NZ$0.93 (+2%), no announcement since the 10 Nov orchard settlement ([NZX 483425](https://www.nzx.com/announcements/483425)). Dropped this week for room; Fonterra lifted its FY27 milk price forecast to NZ$10.10 on 20 November ([NZX 484035](https://www.nzx.com/announcements/484035)), which helps its dairy farm tenants.
- AIS, Aeris: passed over; A$0.385 to A$0.31 (-19%). Kept, lower.
EOF
echo ok