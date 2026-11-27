# Research candidates, 28 November 2026

The weekly research sweep (rulebook section 5a, docs/RESEARCH_TASK.md). Places to look for the next company, not buy signals: one company is chosen in chat, then the case for, the case against, the debate and Cam's decision. This is a simulation and not financial advice.

Data dates:
- ASX screen: Norgate's whole-market export as of 30 October 2026 (29 days old, inside the six-week limit). It passes six weeks on 11 December, so it needs refreshing before the sweep of 12 December. ASIC share counts and shorts come with it.
- NZX screen: closes to 13 November 2026. The exchanges' company data was fetched again on 28 November (tools/research_company_data.py, 472 ASX companies and 76 NZX instruments, no refusals).
- Prices quoted below: the ASX's own company data (last trade at 27 November) and NZX closes of 27 November. The stored closes in data/prices still stop at 16 November because the nightly job has failed its rate test since 17 November.
- Sweep: reports/research_sweep.md, run dated 28 November so that this week's headlines count: 599 on the screen, 242 tagged. Ranking: reports/research_rank.md (250 ranked, 35 special situations). Substantial holder builds are from the last run of tools/holder_notices.py, not refreshed this week.
- Announcements read from the ASX announcements pages and the NZX announcements API on 28 November 2026 (NZ time). The same sixteen NZX company lists as last week returned HTTP 403 and were not retried (research/picks/INDEX.md, note 14).

No watch-list company was newly reopened this week (INDEX.md note 14). Closest: Stride (SPG) set out a plan on 26 November to sell assets to prove its NZ$1.67 NTA against a NZ$1.06 price and to consider a capital return ([NZX 484462](https://www.nzx.com/announcements/484462)); its file reopens on a sale near book, a buyback or a return, and a plan is none of those yet. Monash IVF (MVF) closed below its A$0.665 trigger but said FY27 profit will be "materially below FY26", the exception in its file ([CEO address, 26 Nov](https://announcements.asx.com.au/asxpdf/20261126/pdf/0773m0202y9nh2.pdf)).

Left out on the rules or on reading: live deal targets (the deal sleeve's list), Cam's excluded list (empty, confirmed 8 Nov), software, and companies deep-dived since late August unless reopened or moved 15% or more. Most of the top 30 are again explorers, developers and drug companies that have raised money while losing it (Lotus, True North Copper, Kalamazoo, Caspin, Recce, Starpharma, Forrestania); their bad case is another raising and there's no floor. This week's director notices in the top 50 were mostly plan issues, not buys: Starpharma ([Maley, performance rights](https://announcements.asx.com.au/asxpdf/20261124/pdf/076zy4gvwskmm2.pdf)), Airtasker ([rights for fees](https://announcements.asx.com.au/asxpdf/20261123/pdf/076yp62dx7l3b5.pdf)), Orthocell ([performance rights](https://announcements.asx.com.au/asxpdf/20261127/pdf/0775z4f16vh39l.pdf)) and Cettire (below). Murray Cod (MCA) drops off: its AGM showed operating cash burn of A$26.6m in FY26 against A$4.1m of cash at June ([AGM presentation, 26 Nov](https://announcements.asx.com.au/asxpdf/20261126/pdf/0774289f7swkw1.pdf)), so its bad case is another raising whatever the director paid. Steel & Tube (NZX:STU, NZ$0.26) returned to a small positive normalised EBIT in July to October, but net debt of NZ$55.8m at 31 October is more than the shares are worth ([ASM presentation, 23 Nov](https://www.nzx.com/announcements/484243)); not kept for now.

One to watch next week: Ramsay Health Care's demerger of its 52.79% of Ramsay Santé became effective on 27 November, and Ramsay Santé CDIs trade on the ASX from 1 December, normally from 10 December ([RHC, 27 Nov](https://announcements.asx.com.au/asxpdf/20261127/pdf/07756g38jcw7x5.pdf)). Australian holders receiving a French hospital group's CDIs are classic forced sellers. It isn't kept yet: it has no ASX price, and its net financial debt was €3.73bn (€1.79bn before leases, 5.1 times EBITDA) at September ([1Q FY27 update](https://announcements.asx.com.au/asxpdf/20261106/pdf/0769knrwdgrtdp.pdf)), so a bad case with no floor is likely. The Paul Ramsay Foundation also sold RHC shares in a block trade, down to 9.32% ([26 Nov](https://announcements.asx.com.au/asxpdf/20261126/pdf/07734lcwfh3p85.pdf)).

## 1. ASX:ATG, Articore Group (reopened)

- Price A$0.33, market value about A$97m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/ATG/header)).
- Where found: the watch list. It closed at its A$0.345 trigger on 10 November and the evening desk marked it reopened (research/picks/INDEX.md). There has still been no announcement since 14 November (the ASX's 2026 list for ATG); the price is up 5% on the week but below the trigger.
- Why the price could be wrong: on the deep dive's own outcomes (A$0.22, A$0.39, A$0.55 at 30%, 50%, 20%) the expected price is about A$0.37, some 12% above today's before costs, with no company news behind the fall.
- Hard floor: none. The A$40.5m of cash is all float (free cash about minus A$5.2m at June 2026, research/picks/ATG.md). At A$0.33 the bad case is 33% below the price, still just outside the value test.
- What Cam might read better: an online marketplace (Redbubble, TeePublic) whose profit comes from cost cuts rather than sales; whether cutting paid marketing is shrinking the customer base.
- The question: is gross profit after paid marketing holding at -4% to +3% in constant currency through the Christmas quarter? The reopen means the deep dive is re-run against today's price and the file's conditions; it is not re-run here.

## 2. ASX:SMG, Seven Media Group, formerly Southern Cross Media (reopened)

- Price A$0.415, market value about A$192m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/SMG/header)).
- Where found: the watch list. It closed A$0.44 on 16 November, at its trigger, and the evening desk marked it reopened on 17 November (research/desk_log.md). Nothing has been announced since the plan paperwork of 20 November ([Appendix 3Y, 20 Nov](https://announcements.asx.com.au/asxpdf/20261120/pdf/076vwsc9ndzv0l.pdf)).
- Why the price could be wrong: the deep dive's outcomes (A$0.30, A$0.46, A$0.66 at 30%, 45%, 25%) give an expected price of about A$0.46, about 11% above today's before costs, with the Stokes group at 23.19% and able to buy another 3% from about 17 February 2027 (research/picks/SXL.md).
- Hard floor: none. Net debt is about A$363m against the A$192m market value, so each A$10m of EBITDA is worth about 8.4c a share either way.
- What Cam might read better: radio and regional TV under the limits on wagering advertising from 1 January 2027, a rule change in Cam's own field.
- The question: does the cost programme hold first-half EBITDA at A$96m or more (the file's close-out level) against a shrinking TV ad market and the end of Google news payments?

## 3. ASX:ASG, Autosports Group (reopened)

- Price A$0.88, market value about A$190m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/ASG/header)).
- Where found: the watch list, reopened on 21 November when the AGM gave H1 FY27 revenue of A$1.70bn to A$1.75bn and no profit figure ([AGM addresses, 20 Nov](https://announcements.asx.com.au/asxpdf/20261120/pdf/076ty2jd0cjwxt.pdf)). The price fell 9% this week with no ASG announcement. What changed is a peer: on 23 November Peter Warren said it expects an underlying loss before tax of A$9.5m to A$11.5m for the same half, from lower new-car gross profit per unit as new brands cut prices, over-stocking, buyers trading down and A$3m more interest ([PWR trading update](https://announcements.asx.com.au/asxpdf/20261123/pdf/076xmwpxsn7x5v.pdf)).
- Why the price could be wrong: on the file's cautious chances (40% A$0.60, 45% A$1.23, 15% A$1.88) the expected price is about A$1.08, some 23% above today's before costs, if prestige brands hold up better than the volume dealers Peter Warren mostly sells.
- Hard floor: none, and debt is the risk: each 0.25% on rates costs about A$3m a year in interest (the AGM addresses).
- What Cam might read better: a multi-site prestige car dealership network, his own ground: whether Peter Warren's problem (Chinese entrants pricing hard, stock building up) reaches the prestige end, and whether ASG's stock clearance at "temporary gross margin costs" is the same disease.
- The question: is H1 normalised profit above or below A$20m? Below it, the file's kill condition applies, and Peter Warren's warning makes below more likely than it was a week ago.

## 4. ASX:CTT, Cettire

- Price A$0.23, market value about A$82m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/CTT/header)).
- Where found: the sweep's third name (director buying after a 66% fall; the founder building a stake). Four months to October: sales revenue A$246.2m (+15%), delivered margin 17.1% (15.3%), adjusted EBITDA A$6.9m (A$4.6m), net cash A$27m and no debt ([trading update, 18 Nov](https://announcements.asx.com.au/asxpdf/20261118/pdf/076qrvvjkh5s12.pdf)). Founder Dean Mintz bought 11,437,140 shares on market on 30 September at about A$0.239 ([Appendix 3Y](https://announcements.asx.com.au/asxpdf/20261001/pdf/074t79swqmz54w.pdf)), taking him to about 39%. This week's notice is a plan issue, not a buy: 30,499,056 performance rights approved by holders, his 148,620,065 shares unchanged ([Appendix 3Y, 27 Nov](https://announcements.asx.com.au/asxpdf/20261127/pdf/077611tncg58wx.pdf)).
- Why the price could be wrong: the shares sit below what the founder paid two months ago, after an update showing higher margins and profit, with net cash about a third of the market value.
- Hard floor: net cash A$27m (33% of the market value), plus a non-binding term sheet to factor €16.1m of VAT receivable for at least €13.7m, about A$22m ([market update, 29 Sep](https://announcements.asx.com.au/asxpdf/20260929/pdf/074p9zw6s7pq29.pdf)); the founder's own price, about A$0.239.
- What Cam might read better: online luxury retail and how far discounting, returns and duties eat margin, now with US sales down 3% and paid acquisition up to 5.9% of sales.
- The question: did the market sell on the cash (A$41m a year earlier, A$27m now) and the US, and is Mintz, at 39% and allowed to add 3% from about April 2027, the likely buyer of the company at a low price?

## 5. ASX:GEM, G8 Education (a special situation)

- Price A$0.165, market value about A$121m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/GEM/header)).
- Where found: the news of 12 November, still the biggest gap on the list. G8 received a non-binding A$0.26 cash scheme proposal from Majority Capital Partners with a scrip option, bank and equity commitment letters and up to six weeks' exclusivity, and the directors intend to recommend a binding deal ([process deed](https://announcements.asx.com.au/asxpdf/20261112/pdf/076j2yjqrjg2r6.pdf)); Allan Gray, manager of 19.59%, supports it ([13 Nov](https://announcements.asx.com.au/asxpdf/20261113/pdf/076kwhtf32hxfv.pdf)). Nothing has been announced since. Not binding, so not in the deal sleeve.
- Why the price could be wrong: at A$0.165 against A$0.26 the market prices roughly a 45% chance of a binding deal (taking the 8 Nov deep dive's middling A$0.09 as "nothing happens"), with the board and the largest holder on side and exclusivity running to about 24 December.
- Hard floor: none in the assets (A$0.04 to A$0.20 on its own, research/picks/GEM.md). The deep dive is within three months, but the price is about 65% above the A$0.10 it was written at, so it qualifies.
- What Cam might read better: a regulated childcare network with a Fair Work Ombudsman case and covenant waivers: what a buyer's due diligence will find in occupancy, wages and the regulator's view.
- The question: what are the odds Majority Capital signs at or near A$0.26 by the end of exclusivity, and where does G8 trade if it walks away?

## 6. NZX:WHS, The Warehouse Group

- Price NZ$0.705, market value about NZ$244m (NZX close of 27 November; about 346m shares).
- Where found: NZX announcements and Cam's own ground. The Q1 FY27 update showed group sales NZ$678.8m (+0.7%) and gross margin 33.5% (+110 points) ([NZX 483608, 13 Nov](https://www.nzx.com/announcements/483608)). This week's annual meeting added the full-year base and the plans for cash: FY26 operating profit NZ$22.6m (from NZ$1.3m) on NZ$3,027.6m of sales, cost of doing business down NZ$29.8m, a new dividend policy and the intention to consider resuming dividends for FY27, with imputation credits able to fully impute about 80 cents a share of future dividends ([NZX 484561, 27 Nov](https://www.nzx.com/announcements/484561)).
- Why the price could be wrong: the market values a NZ$3bn-a-year retailer at about 8% of sales on a thin profit, while each point of gross margin on that sales base is worth roughly NZ$30m a year before costs, and its imputation credits could fully impute about 80 cents a share of future dividends, more than the share price.
- Hard floor: none found yet; owned property and the balance sheet are for a deep dive.
- What Cam might read better: whether store discipline and range changes are lasting margin gains through the festive quarter, or promotional timing; the CEO expects "highly competitive" conditions through Christmas with sales the priority.
- The question: does the margin recovery carry FY27 operating profit well above FY26's NZ$22.6m once wages, rent and interest are counted, so that dividends actually resume?

## 7. ASX:AIS, Aeris Resources

- Price A$0.305, market value about A$443m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/AIS/header)).
- Where found: the sweep's top name (substantial holders left; a demerger; this week a restructuring headline). Tribeca ceased to be a substantial holder on 9 November ([form 605](https://announcements.asx.com.au/asxpdf/20261109/pdf/076dll92yq5s9q.pdf)), after two others in September. On 23 November Aeris replaced Washington H. Soul Pattinson's A$60m guarantee facility with a cheaper two-year A$50m facility from Swiss Re, which with Queensland's financial provisioning scheme should release about A$20m of restricted cash ([23 Nov](https://announcements.asx.com.au/asxpdf/20261123/pdf/076xqvp4080t27.pdf)).
- Why the price could be wrong: funds are leaving a debt-free copper and gold producer while it spends on Constellation, so the selling may be about the spending, not the value.
- Hard floor: cash A$128m and no debt at the AGM ([AGM presentation, 19 Nov](https://announcements.asx.com.au/asxpdf/20261119/pdf/076sn4h724wzb4.pdf)), plus about A$20m of bond cash to be freed, together about a third of the market value.
- What Cam might read better: nothing in particular.
- The question: what are Tritton, Cracow and Constellation worth after the build spend, and does the cash last until Constellation produces?

## 8. ASX:MMI, Metro Mining

- Price A$0.88, market value about A$255m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/MMI/header)).
- Where found: the sweep (a substantial holder left; director buying after a 55% fall). Pinnacle ceased to be a substantial holder on 28 October ([form 605](https://announcements.asx.com.au/asxpdf/20261030/pdf/07623kdqt2n0sb.pdf)); four directors then bought about A$190,000 on market at about A$0.80 ([Ritchie](https://announcements.asx.com.au/asxpdf/20261103/pdf/0765mhh2f458nf.pdf), [Purdie and others](https://announcements.asx.com.au/asxpdf/20261106/pdf/0769lps1kzkzd8.pdf)). On 27 November it moved the larger US$17.8m tranche of its Nebari loan to interest only until a bullet payment, saving about US$7.6m (A$11.5m) of cash to June 2027 ([senior debt update](https://announcements.asx.com.au/asxpdf/20261127/pdf/077550sjrqs950.pdf)). Up 8% on the week.
- Why the price could be wrong: a fund sold out after a weather and channel problem that looks temporary, and the directors bought just after; the debt change reads two ways, room to recover or a sign cash was tight.
- Hard floor: none in assets; the directors' price, about A$0.80, now 9% below the market. Cash A$16.8m and secured debt US$24.8m at 30 September ([quarterly](https://announcements.asx.com.au/asxpdf/20261029/pdf/075y30tpq2d987.pdf)).
- What Cam might read better: little; a single-mine bauxite exporter.
- The question: what does Bauxite Hills earn in a normal 7m-tonne year at today's bauxite price, and was 2026's shortfall a one-off or the reason the lender had to give ground?

## 9. ASX:NTD, NTAW Holdings

- Price A$0.195, market value about A$33m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/NTD/header)).
- Where found: the sweep (holders that aren't funds building a stake). Tony Young went from 16.80% to 21.25% and Ryan Young from 15.10% to 19.40% over four notices to 21 September ([form 604, 22 Sep](https://announcements.asx.com.au/asxpdf/20260922/pdf/074cmsbmk8fvsq.pdf); reports/holder_builds.md). Director John Cunningham bought 250,000 on market at A$0.20 on 28 September ([Appendix 3Y](https://announcements.asx.com.au/asxpdf/20261002/pdf/074vysg6k0hn3t.pdf)). No announcement this week.
- Why the price could be wrong: two holders named Young, together about 40%, keep buying a tyre distributor that is shrinking to its core and paying down debt (bank debt down A$13.9m in FY26, [FY26 presentation](https://announcements.asx.com.au/asxpdf/20260827/pdf/073b8lm3vrb5hx.pdf)), which is either a cheap creep toward control or a read on value.
- Hard floor: none; net debt with leases is about A$126m (sweep, from the exchange's data), more than the shares, so the bad case may be a raising.
- What Cam might read better: tyre wholesale and retail networks in Australia and New Zealand (Tyres4U New Zealand, a new NZ wheel business, Carter's Tyre), multi-site and partly NZ, his ground.
- The question: are the two Youngs associated, and if so how close are they to a control threshold, and can the business carry its debt without a raising at this price?

## 10. ASX:DBF, Duxton Farms (new this week)

- Price A$0.32, market value about A$34m ([ASX company data](https://asx.api.markitdigital.com/asx-research/1.0/companies/DBF/header)).
- Where found: the sweep (director notices after a 64% fall, latest 26 November). The notice is not an on-market buy: director Ed Peter took A$1,482,088 of the convertible notes left over from the September entitlement offer ([Appendix 3Y, 26 Nov](https://announcements.asx.com.au/asxpdf/20261126/pdf/0773nwdgy74rdk.pdf)), with a meeting called to approve shortfall notes for him and Richard Magides ([notice of meeting, 20 Nov](https://announcements.asx.com.au/asxpdf/20261120/pdf/076vd9488fcp9v.pdf)). The notes run four years to September 2030, pay 12% capitalised or 7.5% cash, and convert at 90% of the lowest 30-day VWAP, with a A$0.20 floor (the same notice).
- Why the price could be wrong: the shares trade at about 30% of statutory net assets of A$1.07 a share at June 2026, after independent farm valuations had already been written down ([FY26 preliminary report](https://announcements.asx.com.au/asxpdf/20260828/pdf/073dywp8vlcfd1.pdf)).
- Hard floor: land, water and orchards at June 2026 independent valuations, inside net assets of A$115.1m (land alone A$46.6m); but borrowings and overdraft of about A$104m against cash of A$1.2m (same report), so the floor sits behind the banks and the noteholders.
- What Cam might read better: a regulated primary producer (water entitlements, dairy, apples sold) where the question is what the land and water would fetch if sold, not what the farms earn.
- The question: can asset sales cut the debt before the banks or the notes force a raising or conversion near A$0.20, and are the directors funding the company at terms that favour them over other holders?

## Last week's list

None of the ten was chosen for a deep dive this week (no new file in research/picks, research/against, research/debate or research/cards since 21 November). Price moves are from the quotes used on 21 and 28 November.

- ATG, Articore: reopened, not yet re-run; A$0.315 to A$0.33 (+5%), no news. Kept, first.
- SMG, Seven Media: reopened, not yet re-run; A$0.41 to A$0.415 (+1%), no news. Kept.
- ASG, Autosports: reopened, not yet re-run; A$0.97 to A$0.88 (-9%) after Peter Warren's warning. Kept, with the warning.
- CTT, Cettire: passed over; A$0.225 to A$0.23 (+2%); the only notice was the founder's performance rights. Kept.
- GEM, G8 Education: passed over; A$0.17 to A$0.165 (-3%), no news. Kept.
- MCA, Murray Cod: passed over; A$0.14 to A$0.15 (+7%). Dropped: FY26 operating cash burn of A$26.6m against A$4.1m of cash.
- NTD, NTAW: passed over; A$0.19 to A$0.195 (+3%), no news. Kept.
- MMI, Metro Mining: passed over; A$0.815 to A$0.88 (+8%); senior debt moved to interest only. Kept.
- AIS, Aeris: passed over; A$0.31 to A$0.305 (-2%); guarantee facility refinanced. Kept.
- WHS, The Warehouse: passed over; NZ$0.71 to NZ$0.705 (-1%); annual meeting on 27 Nov. Kept, higher.
