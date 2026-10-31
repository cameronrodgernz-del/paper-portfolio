# Follow-up pass: missing deals (started 1 Nov 2026, 00:35 NZDT)

## Method
- Work list: worklist.csv (60 candidates). Order: 2017_2018 items first, then 2015_2016 priority items, then the rest.
- Sources: financialfilings.com, asx.com.au announcement lists, aspecthuntley.com.au mirror, law-firm reviews. WebSearch at most once.

## Item log
- Route tests (00:36-00:55): financialfilings.com has no filings for targets delisted before about 2019 (Mantra Ltd and MYOB Group Ltd pages exist with 0 filings indexed; Sirtex, Pepper, Avanco, Greencross, Ruralco slugs return client_error). OZ Minerals' 2018 page lists only "Completion of compulsory acquisition of Avanco" among deal items. ASX announcement list for OZL: "code does not match". Aspect Huntley has no per-date index. InvestSmart pages now show dated titles only, with no PDF links (so no Aspect Huntley document numbers); page 1 loads for GXL, MYO, APO, RHL; SRX, IOF, SCO page 1 and MYO/APO page 2 returned client_error.
- HSF FY18 and FY19 appendices re-read for values, structure and consideration of the 2017-18 items (values quoted in notes as HSF).
- Gindalbie Metals (GBG, part of item 49): HSF FY19 values the Angang scheme at A$39.0m. Below threshold, excluded.
- Australian Industrial REIT (ANI, worklist 2015_2016): OUT OF SCOPE. 360 Capital Industrial Fund (TIX) announced a formal unsolicited all-scrip off-market takeover offer on 19 Dec 2014 (filing titles 'FORMAL TAKEOVER FOR ANI' and 'ANI: Unsolicited off-market all scrip takeover offer', 19 Dec 2014; the 5 Jan 2015 amendment defines 19 Dec 2014 as the Announcement Date). Binding announcement falls before the 2015 window. Sources: https://financialfilings.com/companies/centuria-industrial-reit/2014/ ; https://financialfilings.com/filings/centuria-industrial-reit/ma-activity/2015/39247426/ . (The bid was later raised, e.g. 'TIX Increases ANI Offer to $2.47' 22 Sep 2015, and closed 26 Oct 2015 with compulsory acquisition completed 1 Dec 2015; useful if the window is ever extended to 2014.)
- Cardno (CDD, 2015_2016): BUILT. financialfilings cardno-ltd/2015 carries the full Crescent proportional bid. In scope as a partial bid for control (maximum 58.91% on full acceptance). Closed 2 Nov 2015 at 40.9%: recorded lapsed.
- Tian An Australia (TIA, 2017_2018): BUILT from the ASX list (code still listed) and Aspect Huntley PDFs. Oasis Star proportional bid (80% of each holding, 35.44% to up to 87.6%, 50.1% minimum), so in scope as a partial bid for control; equity value A$112.6m computed from the target's statement share count.
- Billabong (BBG), Zenitas (ZNT): BUILT as thin rows (dated InvestSmart titles; values HSF; Billabong prices from MinterEllison FY18).
- Devine (DVN, 2015_2016): OUT OF SCOPE, both parts. CIMIC Residential Investments held 50.63% before its A$0.75 cash bid of 9-10 Nov 2015 (controller buy-out; confirmed from the intention-to-bid release https://financialfilings.com/filings/devine-limited/ma-activity/2015/56318479/). Forum Partners' approach was a 'Confidential, Non-Binding, Indicative Proposal' (25 Nov 2015) and Devine's 2016 filing list (https://financialfilings.com/companies/devine-limited/2016/) shows no later Forum or scheme release, so it never became binding.
- Energy Developments (2015_2016): BUILT from DUET Group's financialfilings page. The ASX code was ENE, not EDE.
- Xenith/QANTM (2019_2020 item 51): BUILT as a 2018 row. QANTM SID dated 26 Nov 2018 (financialfilings QANTM page), superseded by IPH (AU-2019-08).
- Propertylink (PLG, 2017_2018): BUILT from releases re-lodged on Centuria Industrial REIT and Centuria Capital pages (PLG code now Pearl Gull). Close date not found.
- Greencross (GXL), Sino Gas (code SEH, not GAS): BUILT as thin rows from InvestSmart dated titles.
- MYOB, Scottish Pacific, Beadell, Pepper: BUILT as thin rows from InvestSmart dated titles (Scottish Pacific has no implementation title, so outcome_date is blank).
- Ruralco (RHL): BUILT as a 2019 row. The SID was announced 27 Feb 2019, not in 2018.
- TPG Telecom (TPM)/VHA: BUILT with announce_date blank. The merger agreement release is beyond the InvestSmart pages that load; financialfilings has no TPG page; the ASX list for the new TPG code has no 2018 history; the Federal Court judgment URL (judgments.fedcourt.gov.au ... 2020fca0117) hit an approval timeout and was not retried.
- Mantra (MTR): code reused by Metal Tiger on InvestSmart; financialfilings shows 0 filings. NOT BUILT.
- Investa Office Fund (IOF): InvestSmart page 1 is now an mFund (IOF01); deal filings sit beyond the pages that load. NOT BUILT (both Blackstone and Oxford).
- Sirtex (SRX): InvestSmart and financialfilings both return client_error. NOT BUILT.
- Finders (FND): code reused by Findi. NOT BUILT.
- Gindalbie: excluded (A$39m, HSF FY19).
- Cromwell (CMW, 2019_2020 item): OUT OF SCOPE. ARA's 23 Jun 2020 proportional bid sought 29% of each holding at A$0.88125 from 24.07%, a maximum of about 48.0% (or 46.1%) on full acceptance, with no minimum acceptance: not a bid for over 50%. Source: bidder's statement https://financialfilings.com/filings/cromwell-property-group/ma-activity/2020/39312605/
- Grays eCommerce (GEG, 2015_2016 'timing not checked'): BUILT as a 2017 row (SID 4 May 2017), from Eclipx/FleetPartners' financialfilings page. It was missing from the 2017-18 file.
- Royal Wolf (RWH): GFN takeover Aug-Sep 2017 (compulsory acquisition notice 26 Sep 2017, removed 6 Oct 2017, per InvestSmart page 1). GFN's pre-bid stake could not be checked: InvestSmart page 2 failed and sec.gov EDGAR search is robots-disallowed. NOT BUILT; likely a controller buy-out if GFN held over 50%.
- WebSearch used once (01:19), for Sirtex: it returned Varian's SEC 10-Q and 8-K exhibit and MinterEllison's deal note. Sirtex BUILT as two rows (Varian superseded_by_rival; CDH/China Grand completed). No further searches.
- Fantastic Holdings (FAN): BUILT as a thin 2016 row from InvestSmart dated titles (SID 14 Oct 2016); value from HSF FY17 (re-opened).
- Payce Consolidated (PAY, 2016): NOT BUILT. Dates from InvestSmart titles: 'Proposed Scheme of Arrangement' 1 Jul 2016, extended to preference shares 26 Aug, explanatory booklet 23 Sep, meeting 31 Oct, court approval 3 Nov, ordinary scheme implemented 25 Nov 2016 (HSF FY17: Bellawest, A$250.0m, cash or unsecured note). Bellawest is linked to Payce's controlling holders and their stake could not be read, so the controller test is unresolved. https://www.investsmart.com.au/security/asx/PAY/x/announcements
- Vitaco (VIT, 2016): NOT BUILT. HSF FY17 A$313.1m (Shanghai Pharma/Primavera, cash scheme); the 2017_2018 candidates file dates it Aug 2016, so it belongs in 2016 and is missing from the 2015_2016 file. VIT is now Vitura Health on InvestSmart; no financialfilings page.
- SMS Management (SMX): NOT BUILT. SMX reused (Strata Minerals); DWS financialfilings slugs (dws-ltd, dws-limited) not found. Timing (2016 or 2017) unresolved. HSF FY17: DWS A$113.8m combination; ASG A$123.4m cash.
- Useful route found late: financialfilings indexes European-listed bidders. Accor (Mantra), JCDecaux (APN Outdoor non-binding proposal of 12 Jun 2018) and Vodafone Group (TPG merger, 30 Aug 2018) all had the deal releases; CCEP (Coca-Cola Amatil) likewise. Accor-sa and steinhoff slugs failed; 'accor' worked.
- Mantra (MTR): BUILT from Accor's releases (signed 12 Oct 2017, implemented 31 May 2018).
- TPG Telecom: announce_date filled from Vodafone's 30 Aug 2018 release.
- Coca-Cola Amatil (CCL, 2019_2020 item): BUILT as a 2020 row from CCEP's releases (non-binding 25-26 Oct 2020, SID 3-4 Nov 2020, implemented 10 May 2021).
- Concentrated Leaders Fund (CLF): OUT OF SCOPE. WAM's 3 Sep 2020 bid: 2 WAM shares per 3.7 CLF shares, implied A$1.14 x 59,401,514 CLF shares = about A$67.7m (computed), below A$100m. https://financialfilings.com/filings/wam-capital-limited/ma-activity/2020/44965915/
- amaysim (AYS): UNRESOLVED. WAM bid implementation agreement 14 Dec 2020 (announced 15 Dec): A$0.695 cash or 1 WAM share per 2.7 amaysim shares, after the Optus sale, cash equal to the midpoint of expected wind-up distributions. Shares on issue not stated in the releases read, so the A$100m test could not be done. https://financialfilings.com/filings/wam-capital-limited/ma-activity/2020/44965689/
- Prime Media (PRT): OUT OF SCOPE per the 2019_2020 candidates file (Seven West scheme A$64.6m, Corrs; announced 18 Oct 2019, voted down 2020). Not re-checked.
- Villa World (VLW, 2017_2018 item): already in the 2019_2020 file as AU-2019-29 (SID between 1 and 21 Jul 2019 per that row). Not rebuilt.
- Spicers (SRS) and Nzuri (NZC) (part of item 49): already in the 2019_2020 file (AU-2019-02, AU-2019-28). Not rebuilt.
- Seymour Whyte (SWL): already AU-2017-05. Brookfield Prime Property Fund (BPA) and Warrnambool (WCB): already excluded as controller buy-outs in the 2017_2018 candidates file. Afterpay/Touchcorp: handled in the 2017_2018 candidates file. Not rebuilt.
- Doray (DRM): code reused by Demetallica on InvestSmart; Silver Lake financialfilings slugs not found. NOT BUILT.
- Realm Resources (RRP): OUT OF SCOPE. Takeovers Panel TP18/046 says the T2/Taurus group 'held over 85% of Realm's ordinary shares' at all relevant times, so the 9 Feb 2018 bid (A$0.90, raised to A$1.00 on 15 May 2018, plus a A$0.35 top-up undertaking, closed 3 Aug 2018) was a controller buy-out. Sources: https://takeovers.gov.au/media-releases/tp18-046 ; https://takeovers.gov.au/media-releases/tp18-037 ; https://takeovers.gov.au/media-releases/tp18-049
- Finders Resources (FND): BUILT as a thin 2017 row from Panel release TP18/040 (bidder's statement 23 Oct 2017, A$0.23 cash; control on 19 Mar 2018). Close date not found.
- Takeovers Panel media releases at takeovers.gov.au/media-releases/tp18-0NN load reliably (TP18/036 to 050 checked); the 2017-18 annual report PDF path did not.

## Status of every worklist item (row number = order in worklist.csv, 0-based)

| # | Item | Result |
|---|---|---|
| 0 | Aditya Birla Minerals | Not rebuilt: below threshold per HSF FY16 (A$86m); not re-checked against a filing |
| 1 | Armour Energy | Not rebuilt: below threshold per HSF FY16 (A$76m); not re-checked |
| 2 | Ausenco | Not rebuilt: below threshold per HSF FY16 (A$75m equity); the Mayne A$154m looks like EV; not re-checked |
| 3 | Gryphon Minerals | Not rebuilt: below threshold per HSF FY16 (A$83m) |
| 4 | PAS Group | Not rebuilt: below threshold per HSF FY16 (A$86m) |
| 5 | Rubik Financial | Not rebuilt: below threshold per HSF FY17 (A$70.6m) |
| 6 | Warrnambool | Excluded (controller Saputo), as in the 2017_2018 candidates file |
| 7 | Cardno | BUILT AU-2015-F02 (Crescent proportional bid, lapsed at 40.9%) |
| 8 | Devine | Excluded: CIMIC held 50.63%; Forum approach never binding |
| 9 | Coffey | BUILT AU-2015-F03 from Tetra Tech's SEC filings on financialfilings (BIA 14 Oct 2015, A$0.425 cash, control 18 Jan 2016) |
| 10 | Energy Developments | BUILT AU-2015-F01 (code ENE) |
| 11 | Skilled / Programmed | NOT RESOLVED: SKE reused; Programmed and Skilled slugs not on financialfilings |
| 12 | Pulse Health bid for Vision Eye | NOT RESOLVED: no page reaches Pulse's 2015 bid filings. Jangho's Shanghai filings gave patches for the existing Jangho row AU-2015-09 (see patches.csv) but do not describe Pulse's terms |
| 13 | SMS Management (DWS and ASG schemes) | NOT RESOLVED: SMX reused; DWS not on financialfilings; timing (2016 or 2017) unknown |
| 14 | Fantastic Holdings | BUILT AU-2016-F02 |
| 15 | Brookfield Prime Property Fund | Excluded (controller, ~80%) per the 2017_2018 candidates file |
| 16 | Seymour Whyte | Already AU-2017-05 |
| 17 | Vitaco | BUILT AU-2016-F01 from Shanghai Pharmaceuticals' HKEX filings on financialfilings (SID 3 Aug 2016, A$2.25 cash, implemented 16 Dec 2016); missing from the 2015_2016 file |
| 18 | Afterpay / Touchcorp | Handled in the 2017_2018 candidates file (Touchcorp side); not rebuilt |
| 19 | Payce Consolidated | NOT RESOLVED: 2016 dates found (see above); controller test open |
| 20 | Grays eCommerce | BUILT AU-2017-F01 (a 2017 deal, not 2016) |
| 21 | Simonds | Not rebuilt: below threshold (not in HSF's A$70m-plus list) |
| 22 | Australian Industrial REIT | Excluded: formal bid announced 19 Dec 2014 |
| 23 | CIC Australia | Not assessed: believed well below A$100m; not checked |
| 24 | Sirtex (two bidders) | BUILT AU-2018-F02 (Varian) and AU-2018-F06 (CDH/China Grand) |
| 25 | Pepper Group | BUILT AU-2017-F02 |
| 26 | Mantra | BUILT AU-2017-F04 (from Accor's releases) |
| 27 | Investa Office Fund (Blackstone, Oxford) | NOT RESOLVED: IOF reused by an mFund; no listed bidder; no financialfilings page |
| 28 | TPG Telecom / VHA | BUILT AU-2018-F07 |
| 29 | MYOB | BUILT AU-2018-F15 |
| 30 | APN Outdoor | BUILT AU-2018-F16 (announce_date blank; JCDecaux non-binding 12 Jun 2018) |
| 31 | Greencross | BUILT AU-2018-F12 |
| 32 | Scottish Pacific | BUILT AU-2018-F10 (implementation date not found) |
| 33 | Gateway Lifestyle | BUILT AU-2018-F17 (announce_date blank) |
| 34 | Propertylink | BUILT AU-2018-F13 (close date not found) |
| 35 | Ruralco | BUILT AU-2019-F01 (SID 27 Feb 2019) |
| 36 | Avanco | BUILT AU-2018-F03 (bidder's statement date used) |
| 37 | Billabong | BUILT AU-2018-F01 |
| 38 | Villa World | Already AU-2019-29 (a 2019 deal per that row) |
| 39 | Sino Gas & Energy | BUILT AU-2018-F05 (code SEH) |
| 40 | Realm Resources | Excluded: T2/Taurus held over 85% before the bid (Panel TP18/046) |
| 41 | Tawana | BUILT AU-2018-F18 (announce_date blank; year inferred) |
| 42 | Mitula | BUILT AU-2018-F04 |
| 43 | Finders Resources | BUILT AU-2017-F05 (from Panel TP18/040) |
| 44 | Watpac | BUILT AU-2018-F11 (BESIX takeover). NOT BUILT: the earlier failed BESIX proportional scheme (28.1% to 64.1%), dates not reachable |
| 45 | LifeHealthcare | NOT RESOLVED: page 1 dates found (booklet 29 Mar 2018, meeting 3 May, court 10 May, implemented 25 May 2018; HSF A$168.5m), but the SID page would not load, so the binding year (Dec 2017 or early 2018) is unknown |
| 46 | Zenitas | BUILT AU-2018-F08 |
| 47 | Tian An | BUILT AU-2017-F03 (not a controller: 35.44%) |
| 48 | Royal Wolf | Excluded: controller buy-out. General Finance's FY2017 10-K (https://financialfilings.com/filings/general-finance-corporation/annual-report/2017/50501532/) says it would be acquiring the 49.0% non-controlling interest, so GFN held about 51%. Bid announced 12 Jul 2017, bidder's statement 19 Jul, compulsory acquisition 26 Sep, removed 6 Oct 2017 |
| 49 | Beadell / Xenith / Spicers / Gindalbie / Nzuri | Beadell BUILT AU-2018-F09; Xenith (QANTM) BUILT AU-2018-F14; Spicers and Nzuri already in the 2019 file; Gindalbie excluded (A$39m) |
| 50 | Doray | NOT RESOLVED: DRM reused; Silver Lake has 0 filings on financialfilings |
| 51 | Xenith (QANTM) | BUILT AU-2018-F14 |
| 52 | Beadell | BUILT AU-2018-F09 (same as item 49) |
| 53 | Coca-Cola Amatil | BUILT AU-2020-F01 |
| 54 | Concentrated Leaders Fund | Excluded: about A$67.7m |
| 55 | amaysim | BUILT AU-2020-F02 (307,375,144 shares x A$0.695 cash = A$213.6m; completed 30 Mar 2021) |
| 56 | Credible Labs | BUILT AU-2019-F02 from Fox's SEC filings on financialfilings (merger agreement 4-5 Aug 2019, A$2.21 per CDI for 67%; closed Oct 2019, exact date not given) |
| 57 | Cromwell | Excluded: ARA's proportional bid capped at about 48% |
| 58 | Prime Media | Excluded: A$64.6m per the 2019_2020 candidates file (Corrs) |
| 59 | Base Resources | BUILT AU-2024-F01 from Energy Fuels' SEC 8-Ks on financialfilings (SID 21-22 Apr 2024, about A$375m, implemented 2 Oct 2024) |

## Routes, for a later pass
- financialfilings.com works for companies still listed after about 2019 and for European/UK bidders (Accor, JCDecaux, Vodafone, CCEP). Slugs vary (accor, not accor-sa; fleetpartners-group-limited for Eclipx). Bidder pages carry target releases when the bidder was ASX-listed (DUET, Centuria, QANTM, WAM, FleetPartners).
- InvestSmart: page 1 loads for most codes with the slug 'x'; page 2 usually loads with the exact name slug; page 3 and beyond failed almost every time (Avanco page 3 once). No PDF links are shown any more, so Aspect Huntley document numbers cannot be read from it.
- ASX announcement lists still give document numbers for codes still in use (TIA, WAM), and Aspect Huntley serves those PDFs.
- Takeovers Panel media releases (takeovers.gov.au/media-releases/tp18-0NN) load and carry bid histories.
- Blocked or refused: sec.gov browse-edgar (robots_disallowed); judgments.fedcourt.gov.au/judgments/Judgments/fca/single/2020/2020fca0117 (approval timeout); cdn.financialreports.eu PDF of Nutrien's 26 Feb 2019 news release (approval timeout; it may hold Ruralco's price); the Panel's 2017-18 annual report PDF path (client_error). None retried.
- financialfilings also indexes US, Canadian, Hong Kong/Shanghai and some other foreign filers (Tetra Tech, Energy Fuels, Fox, General Finance, Shanghai Pharmaceuticals, Jangho, Nutrien), so a bidder's SEC 8-K, 10-Q or exchange release is often the best route into a delisted ASX target. Not indexed: Great Panther, Nomura Research Institute, LIFULL, Steinhoff (slugs tried), Silver Lake (0 filings), DWS, Payce, Skilled, Programmed, LifeHealthcare.
- WebSearch: used once (Sirtex); not used again.

## Contradictions with earlier files
- Grays eCommerce: the 2017_2018 candidates file groups it with July-December 2016 deals; its SID is dated 4 May 2017, so it was missing from the 2017 file.
- Coca-Cola Amatil: the 2019_2020 candidates file left the SID year open; CCEP's release dates the binding deeds 3-4 Nov 2020.
- Vitaco: the 2015_2016 notes treat it as probably a 2017 deal; the 2017_2018 candidates file dates it Aug 2016.
- Energy Developments' code was ENE (worklist: EDE); Sino Gas's was SEH (worklist: GAS); Ruralco's SID was Feb 2019 (worklist: late 2018).
- Tian An: worklist suggested the bidder might be the controller; it held 35.44%. Realm: worklist 'likely in scope'; the bidder held over 85%.

## Stopped
Stopped at about 01:45 NZDT (1 hour 10 minutes in) because the remaining items had no reachable source on the allowed domains after the routes above were tried. Still open: Investa Office Fund (Blackstone and Oxford), LifeHealthcare (binding year), the failed BESIX proportional scheme for Watpac, Doray, Skilled/Programmed, Pulse Health's bid for Vision Eye, SMS Management (two schemes) and Payce (controller test).

## Late additions (01:30-01:45)
- Coffey, Vitaco, Credible Labs, Base Resources and amaysim BUILT from bidders' foreign filings indexed on financialfilings (see table). Royal Wolf excluded (GFN about 51%).
- patches.csv: AU-2019-08 related_deal_ids (link to the QANTM row); AU-2015-09 announce_date 2015-09-07 to 2015-08-13 and days_to_outcome 44 to 69 (Jangho's bid agreement was signed 13 Aug 2015), pre_bid_stake_pct 19.99, break_fee_m 2.0, and a bidder_type change to existing_holder flagged as a convention call.
- Helper scripts and per-row JSON drafts were kept in a scratch folder outside this folder (/home/claude/pp_scripts) and deleted at the end; all output is in new_rows.csv, patches.csv and this log. No existing CSV was edited (modification times unchanged).
