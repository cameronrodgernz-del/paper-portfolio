# Desk log

Each entry starts with "## <date>, <summary>". Changes of terms on the live list, with their source.

## 2026-11-01, Deal files from primary sources for every live ASX deal; terms corrected

The deal files in research/deals/ (one per live deal, from the announcements, booklets, deeds, expert
reports and regulators' registers) were folded into config/live_deals.csv with src/deal_files.py.
Terms changed on the live list, each from its deal file:
- VAU: cash A$0.475 to A$0.5125 a share, raised to make up for the Genesis A$0.05 dividend Vault
  holders don't receive (VAU.md, scheme booklet).
- OML: A$1.70 to A$1.68; the 2c interim dividend in the headline was paid on 17 Sep, so a buyer now
  gets A$1.68 (OML.md). Payment moved to 10 Dec after the 30 Oct timetable change.
- AUC: valued as the mix a holder gets if every holder elects cash: A$0.3395 cash plus 0.02525
  OceanaGold shares (NYSE OGC), from the A$194m cash cap over the scheme shares (AUC.md). The old row
  used the A$1.36 cash alternative before scale-back, which overstated the gap to the offer
  (12.9% shown; about nil on the mix). OceanaGold added to the nightly fetch as US:OGC.
- SDF: A$6.00 to A$5.8725; the 12.75c FY26 dividend was paid on 25 Sep (SDF.md).
- PPC: cash A$0.745 to A$0.68; the 6.5c dividend was paid on 22 Sep (PPC.md). The scrip leg is
  still valued at Ingenia's price, which carries the bids for Ingenia itself; the deal file sets
  out why that value disappears if this deal goes ahead.
- Notes rewritten for AX1, BET, RWC, MEI, CWY and FPR from their files.
Added: RTH (Racing and Sports, PA Media scheme at A$1.04 cash), with its undisturbed price of
A$0.54 (the close on 16 Oct). Not added: EUR and CNB, both unconditional and paying in early
November, so only the payment is left.

## 2026-11-01, Undisturbed prices dated, and set for VAU and RWC

The live list now carries undisturbed_date, and the break price moves the undisturbed price with the
market from that date, not from the deal's own announcement.
- VAU: A$4.50 at the close on 4 May 2026, before the first (Regis) scheme; the Genesis deal of
  14 Jul followed a contest, so the price just before it already held a bid (deals database AU-2026-10).
- RWC: A$3.61 at the close on 17 Aug 2026, before the Process Deed with Brookfield was announced
  (deals database AU-2026-21; RWC.md).
- RTH: dated 16 Oct 2026, the last close before the announcement.

## 2026-11-01, Deals added from the sweep: A11 and GL1; NZX has none live

From the sweep of ASX and NZX announcements (deal files A11.md, GL1.md):
- A11 (Atlantic Lithium, Zhejiang Huayou Cobalt): US$0.25486 cash. Undisturbed A$0.280, the last
  close before the 7 May announcement. Payment indicated only as December 2026, so set to 31 Dec.
- GL1 (Global Lithium, Titan Australia Mining): A$1.15 cash. Undisturbed A$0.665, the last close
  before the 22 Sep announcement. Payment indicated as mid-January 2027, so set to 15 Jan.
- Not added: RCT (Reef Casino Trust; Iris already holds 96.5% and will compulsorily acquire; only
  the payment is left), and EUR and CNB (both effective, paying in early November).
- NZX: no live control deal at NZ$20m or more. Bremworth and 2 Cheap Cars have finished. Watching
  non-binding approaches: thl (update by the 6 Nov AGM), SkyCity (structured process since 30 Sep).
Both new deals have no stored prices yet; the nightly fetch adds them.

## 2026-11-01, Undisturbed dates filled for every live deal; Peet's undisturbed price moved to 9 Jul

The break price moves the undisturbed price with the market from its own date, so each live deal
now has that date, from the deal database's undisturbed basis: BET 7 Aug, OML 28 Apr (before the
first proposal), AUC 14 Aug, SDF 9 Jun (before the NBIO), MEI 30 Sep, CWY 12 Aug (before the NBIO)
and FPR 31 Jul (before SG Fleet's approach). PPC: A$1.81 (21 Aug) to A$1.70, the close on 9 Jul,
the undisturbed date Peet's own presentation uses, before the first approach on 10 Jul. AX1 has no
break price (an unconditional on-market bid). From the independent review of 1 Nov, finding 4.

## 2026-11-02, First practice night: oOh!media vote passed; Meteoric card held back on the red team's advice; nothing placed

Checked:
- All 16 test files in tests/ pass under python3 -I.
- Tonight's "Nightly data 2026-11-02" commit landed at 21:38 NZDT, with the practice ledger's first valuation (NZ$99,985 after the November plan fee) and the three core buys placed by rule for tomorrow's open (72 VT, 73 VAS, 125 ENZL). src/actions.py check: nothing missing.
- reports/data_checks.md: RTH's +85% on 19 Oct is the PA Media scheme announcement, not a bad price. The OML "deal file" finding (meeting on 2 Nov after the file was checked) is dealt with below.
- Scan of the 13 live ASX deals for anything new on 2 Nov. The ASX announcement list pages could not be opened from tonight's session (the fetch tool needed an approval no one was there to give), so the scan used news searches and InvestSMART's announcement lists where search returned them (OML, PPC). Nothing new found for AX1, VAU, BET, AUC, SDF, PPC, RWC, MEI, CWY, FPR, A11, RTH or GL1; their files keep their 1 Nov check date. No new binding ASX or NZX control deal of A$100m (NZ$20m) or more found. KMD Brands has takeover talk only (non-binding), so not added.

Changed:
- OML (oOh!media, I Squared scheme at A$1.68): holders approved the scheme at the 2 Nov meeting, 99.89% of votes cast (273,040,211 for, 292,222 against) and 90.53% of holders present and voting. Stage booklet_out to vote_passed; holder approval moved from open to met. Timetable unchanged: Second Court Date 18 Nov, effective 19 Nov, record 3 Dec, payment 10 Dec. FIRB still the one open approval (deadline 13 Nov). Source: oOh!'s Chair's address of 2 Nov (InvestSMART's OML list) and Kalkine's report of the results release (https://kalkinemedia.com/au/news/announcements/oohmedia-shareholders-approve-i-squared-capital-acquisition-scheme-with-9989-support); the ASX release itself couldn't be opened tonight and is to be confirmed. Carried into config/live_deals.csv with src/deal_files.py.
- src/deal_files.py again reports AUC's file (default all scrip, 0.03365) differs from the row (the all-elect-cash mix, A$0.3395 plus 0.02525 OGC). Kept the row as decided on 1 Nov.
- Deal database unchanged (no deal completed or ended), so the base rates and odds were not rerun. Deal monitor rerun.

Analysed, in order of expected_yearly:
- GL1, A11, RWC, BET, RTH, FPR, CWY, OML, SDF: cash deals, not placed (test 9c failed). No cards.
- MEI (Lynas scrip scheme, 0.0207 LYC): card research/cards/2026-11-02-MEI.json, base 95.6% cut to 78% (Brazil CIMCE -10, vote -3, expert -2, licence delay -2). decide.py dry run passed: NZ$3,999 (4% cap), 7.8% a year expected after costs against a 2.1% cash rate, no breaches. Red team (research/red_team/MEI-2026-11-02.md): wait. The gap opened only when Lynas rose 16% on 26 to 29 Oct and Meteoric didn't follow, so it is mostly Lynas price risk that can't be hedged; the CIMCE has no rules or deadline, so payment near 1 Jul 2027 is likelier than 30 Apr; Lynas is down 12% since the undisturbed date, putting the break nearer A$0.15, where a 4% stake would lose 1.27% of the portfolio, over the 1% limit. Not placed; card status "waiting". Re-test when a CIMCE filing with an expected decision date, or a ruling that the regime doesn't apply, is announced (likely around mid-December), with a A$0.15 break, a 30 Jun 2027 resolve date and at most 3%.
- AUC (OceanaGold mix): 0.5% expected over 39 days at the base rate, little above cash for the time and carrying NYSE OGC price risk; not carded.
- VAU: below zero at the base rate. PPC: no expected figure (Ingenia's price carries its own bids). AX1: price above the bid.
- US deals: watched only (9b not passed). Special situations: no type has passed. Research picks: no card is "ready" and none is held.

Placed: nothing by the desk. Only the nightly job's three core buys are waiting for tomorrow's open.

## 2026-11-03, Core buys filled; AVID matches for Ingenia, Peet deal still on foot; nothing placed

Checked:
- All 16 test files in tests/ pass under python3 -I. Ledger chain verifies (every file ok).
- Tonight's "Nightly data 2026-11-03" commit landed at 21:30 NZDT, with a practice valuation for today: NZ$99,474.86, 0.51% below the peak. The three core buys filled (72 VT and 125 ENZL on 2 Nov US time, 73 VAS on 3 Nov). src/actions.py check: nothing missing.
- reports/data_checks.md: nothing found, no deal file findings.
- Scan of the 13 live ASX deals for anything new since the 2 Nov entry. As last night, the ASX announcement pages couldn't be opened (the fetch tool needed an approval no one was there to give), so the scan used news searches. Nothing new found for AX1, VAU, BET, OML, AUC, SDF, RWC, MEI, CWY, FPR, A11, RTH or GL1; their files keep their check dates. RWC rose 2.9% to A$4.57 with no news found. Dated items still ahead: A11 first court hearing 5 Nov, CWY regulatory filings due by 10 Nov, VAU meeting 11 Nov, OML FIRB deadline 13 Nov, PPC's ACCC Phase 1 ends 20 Nov, BET ACCC Phase 1 decision 26 Nov.
- No new binding ASX or NZX control deal of A$100m (NZ$20m) or more found. First Au and Javelin Minerals signed an amended takeover deed on 2 Nov (Kalkine); both are small explorers far under A$100m, so not added. EUR (pays 5 Nov), CNB (10 Nov) and RCT (30 Nov) have only payment left; their database rows stay pending until paid.

Changed:
- PPC (Peet, Ingenia scheme): on 1 Nov AVID used its matching right, lifting its non-binding proposal for Ingenia to A$5.45 cash plus up to 5 cents of distribution (A$5.50), equal to Warburg Pincus. Ingenia's board judged it equal or superior; AVID keeps soft exclusivity and Warburg Pincus is again shut out of due diligence. Ingenia has not recommended AVID and has not determined a Bidder Superior Proposal under the Peet deed, which "remains on foot". Both proposals still need the Peet deed ended (A$10m reverse break fee). Stage and terms unchanged. Source: Ingenia's 2 Nov ASX release as reported by The Weekly Source (https://www.theweeklysource.com.au/avid-matches-warburgs-ingenia-communities-bid-and-shuts-out-rival-for-now/); the release itself is to be confirmed. Deal file updated and carried into config/live_deals.csv with src/deal_files.py (check date only).
- src/deal_files.py again reports AUC's file (default all scrip) differs from the row (the all-elect-cash mix). Kept the row as decided on 1 Nov.
- Deal database unchanged, so base rates and odds not rerun. Deal monitor rerun.

Analysed, in order of expected_yearly:
- GL1 (+123%), A11 (+99%), BET (+13%), RWC (+9%): cash deals, not placed (test 9c failed). RTH, FPR, CWY, OML, SDF: cash and below zero at the base rate anyway.
- MEI (Lynas scrip, +21% a year at the base rate, +24% if late): card stays "waiting". Its re-test trigger (a CIMCE filing with a decision date, or a ruling that the regime doesn't apply) hasn't happened. No new card.
- AUC (OceanaGold mix): -9.4% a year at the base rate. VAU: -38%. PPC: no expected figure. AX1: price above the bid.
- US deals: watched only (9b not passed). Special situations: no type has passed. Research picks: no card is "ready" and none is held.

Placed: nothing. No limit tripped.

## 2026-11-04, Warburg Pincus revises its Ingenia terms but not its price; Accent trades above the Frasers bid; nothing placed

Checked:
- All 16 test files in tests/ pass under python3 -I.
- Tonight's "Nightly data 2026-11-04" commit landed at 21:32 NZDT, with a practice valuation for today: NZ$99,651.35, 0.33% below the peak, no limit flags. src/actions.py check: nothing missing.
- reports/data_checks.md: nothing found, no deal file findings.
- Scan of the 13 live ASX deals for anything new since the 3 Nov entry. The ASX and Market Index announcement pages still couldn't be opened (the fetch tool needed an approval no one was there to give), so the scan used news searches and InvestSMART pages where search returned them (GL1, AUC). Nothing new found for VAU, BET, OML, AUC, SDF, RWC, MEI, CWY, FPR, A11, RTH or GL1; their files keep their check dates. Latest GL1 release is still the 29 Oct quarterly; latest AUC price-sensitive release is still the 21 Oct booklet.
- AX1 rose 4.6% to A$0.685 on about three times its usual volume, above the Frasers A$0.65 bid. No news found beyond Frasers' 28 Oct best and final statement (FashionUnited, 2 Nov: https://fashionunited.uk/news/business/frasers-makes-best-and-final-offer-for-accent-takeover-deal/2026110291137). The file already has the 20 Nov AGM and conditional spill meeting. No change.
- No new binding ASX or NZX control deal of A$100m (NZ$20m) or more found. Rakon (NZX) came up in search but completed in May 2026 and is already in the database.
- Dated items ahead: A11 first court hearing tomorrow (5 Nov), EUR pays 5 Nov, CWY filings due by 10 Nov, CNB pays 10 Nov, VAU meeting 11 Nov, OML FIRB deadline 13 Nov, PPC's ACCC Phase 1 ends 20 Nov, AX1 AGM 20 Nov, BET ACCC Phase 1 decision 26 Nov.

Changed:
- PPC (Peet, Ingenia scheme): Warburg Pincus sent Ingenia a revised proposal on 3 Nov at the same A$5.50, conditional on its due diligence access being restored at once, the AVID process deed being ended and an amended deed signed with Warburg by 6 Nov. Ingenia's board did not consider it superior to AVID's deed of 2 Nov and kept Warburg's access suspended. Nothing on the Peet deed, which stays on foot. Ingenia fell 3.8% to A$5.12; Peet A$1.445. Source: Reuters via Boursorama, 4 Nov (https://www.boursorama.com/bourse/actualites/warburg-modifie-son-offre-de-rachat-d-ingenia-apres-qu-avid-a-egale-son-offre-5948257c71d44d44bc22af0a6530f518); the ASX release is to be confirmed. Deal file updated and carried into config/live_deals.csv with src/deal_files.py (check date only). Stage and terms unchanged.
- src/deal_files.py again reports AUC's file (default all scrip) differs from the row (the all-elect-cash mix). Kept the row as decided on 1 Nov.
- Deal database unchanged, so base rates and odds not rerun. Deal monitor rerun.

Analysed, in order of expected_yearly:
- GL1 (+144%), A11 (+101%): cash deals, not placed (test 9c failed). RWC (+21%), BET (+13%): cash, same. FPR, RTH, CWY, OML, SDF: cash and below zero at the base rate anyway.
- MEI (Lynas scrip, +30% a year at the base rate, +33% if late): card stays "waiting". Its re-test trigger (a CIMCE filing with a decision date, or a ruling that the regime doesn't apply) hasn't happened. Lynas flat at A$11.99.
- AUC (OceanaGold mix): about 0% a year at the base rate (+14% if late) after a 2.9% fall to A$1.155; little above nothing and carrying OGC price risk, so not carded. VAU: -37%. PPC: no expected figure (below its break price). AX1: price above the bid.
- US deals: watched only (9b not passed). Special situations: no type has passed. Research picks: no card is "ready" and none is held.

Placed: nothing. No limit tripped.

## 2026-11-05, Nightly job did not run by 10:15pm, so watching only; Noumi's Arrovest scheme passed its vote but is under A$100m; nothing placed

Checked:
- All 16 test files in tests/ pass under python3 -I.
- Tonight's nightly job had not landed after the 30-minute wait (pulled at 9:45pm, then about every 5 minutes to 10:15pm NZDT). The latest commit is "History prices 2026-11-05T06:54"; GitHub Actions shows no Nightly data run at all today (the last was run 9, for 4 Nov). With no practice valuation for 5 Nov, nothing was placed and nothing was entered in the ledger, as docs/DAILY_RUN.md requires. The clerk's 5 Nov work (fills, valuation, limit flags) is still to happen. Corporate action check, card placing and research pick checks skipped for the same reason; no research card is "ready" and none is held.
- reports/data_checks.md is still last night's (4 Nov): nothing found, no deal file findings.
- Scan of the 13 live ASX deals for anything new since the 4 Nov entry, by news searches (the ASX announcement pages still can't be opened from the desk). Nothing new found for AX1, VAU, BET, OML, AUC, SDF, PPC, RWC, MEI, CWY, FPR, RTH or GL1; their files keep their check dates. OML's FIRB approval (deadline 13 Nov) not yet announced.
- A11 (Atlantic Lithium): the first court hearing was set for today, 5 Nov. No result found tonight (latest found is Kalkine's preview, https://kalkinemedia.com/au/stocks/lithium/is-atlantic-lithium-asxa11-days-away-from-its-huayou-takeover-decision). The file's first court date has now passed, so tomorrow's desk should confirm the orders and the booklet and meeting dates and update the file.
- New deals: Noumi (NOU) holders and optionholders approved Arrovest's schemes on 5 Nov (shares: 89.08% of votes cast, 78.65% of holders voting; second court 10 Nov, effective 11 Nov, implementation 27 Nov; source: Kalkine's report of the results, https://kalkinemedia.com/au/news/announcements/noumi-limited-shareholders-and-optionholders-approve-arrovest-acquisition-schemes-at-november-5-2026-meetings). The deal (A$0.1234 cash, announced about 21 Jul 2026) values Noumi's equity at about A$34.2m (Small Caps, https://smallcaps.com.au/article/noumi-enters-binding-scheme-with-major-shareholder-arrovest-to-resolve-looming-note-maturity), under the A$100m bar, so not added to the live deals or the database. No other new binding ASX or NZX control deal of A$100m (NZ$20m) or more found.
- Dated items ahead: thl AGM 6 Nov (update on the non-binding approach), CWY filings due by 10 Nov, CNB pays 10 Nov, VAU meeting 11 Nov, OML FIRB deadline 13 Nov, PPC's ACCC Phase 1 ends 20 Nov, AX1 AGM 20 Nov, BET ACCC Phase 1 decision 26 Nov. EUR was due to pay today; its database row stays pending until the payment is confirmed.

Changed:
- No deal file, live deal row or database row changed. src/deal_files.py: no changes; it again reports AUC's file (default all scrip) differs from the row (the all-elect-cash mix); kept the row as decided on 1 Nov.
- Deal monitor rerun on the stored closes (4 Nov); only the days to payment moved.

Analysed: nothing new to card. MEI's card stays "waiting" (its re-test trigger hasn't happened). Cash ASX deals stay barred (test 9c failed), US deals watched only, no special situation type has passed.

Placed: nothing (no valuation tonight). No limit could be checked without the clerk run.

## 2026-11-06, Nightly job missing a second night, so watching only; Peet's scheme booklet is out with a 7 Dec vote and Warburg lifts its Ingenia bid to A$5.55; Atlantic Lithium meeting set for 14 Dec; nothing placed

Checked:
- All 16 test files in tests/ pass under python3 -I.
- Tonight's nightly job had not landed after the 30-minute wait (pulled at 9:47pm, then about every 2 to 3 minutes to 10:18pm NZDT). The latest commit is "History prices 2026-11-06T06:54"; GitHub Actions shows no Nightly data run today (the last, run 11, ran at 5:38am NZDT on 6 Nov for 5 Nov, after last night's desk). This is the second weeknight in a row the 8:30pm run has not fired on time. With no practice valuation for 6 Nov, nothing was placed and nothing was entered in the ledger, as docs/DAILY_RUN.md requires. Corporate action check, card placing and research pick checks skipped for the same reason; no research card is "ready" and none is held.
- The 5 Nov valuation did land overnight: NZ$100,163.84, a new peak, no limit flags.
- reports/data_checks.md (5 Nov): nothing found, no deal file findings. A11's first court date had passed; dealt with below.
- Scan of the 13 live ASX deals since the 5 Nov entry, by news searches (the ASX announcement pages still can't be opened from the desk). Nothing new found for AX1, VAU, BET, OML, AUC, SDF, RWC, MEI, CWY, FPR, RTH or GL1; their files keep their check dates. OML's FIRB approval (deadline 13 Nov) not yet announced.
- No new binding ASX or NZX control deal of A$100m (NZ$20m) or more found. Forrestania Resources' bid for Zenith Minerals went unconditional on 5 Nov (Sharecafe); a small explorer deal, not added.
- NZX: Tourism Holdings (thl) said at its 6 Nov annual meeting that due diligence has largely concluded and it has revised non-binding proposals from the BGH consortium and Indie Campers; terms not disclosed, both still non-binding, so not added (Sharecafe, https://www.sharecafe.com.au/2026/11/06/tourism-holdings-thl-provides-update-on-non-binding-acquisition-offers/).
- EUR (pay date 5 Nov): payment not yet confirmed; its database row stays pending.
- Dated items ahead: CWY filings due by 10 Nov, CNB pays 10 Nov, Warburg's Ingenia deadline 10 Nov, VAU meeting 11 Nov, A11 booklet by 12 Nov, OML FIRB deadline 13 Nov, PPC's ACCC Phase 1 ends 20 Nov, AX1 AGM 20 Nov, BET ACCC Phase 1 decision 26 Nov, SDF meeting 27 Nov, PPC election deadline 28 Nov.

Changed:
- PPC (Peet, Ingenia scheme): the timetable that looked stalled is moving. The Federal Court ordered the scheme meeting on 3 Nov and ASIC registered the booklet the same day; Kroll finds the scheme fair and reasonable and in holders' best interests absent a superior proposal; the booklet went out on 5 Nov. Election deadline 28 Nov, meeting 9am (Perth) 7 Dec, second court 15 Dec, effective 16 Dec, record 18 Dec, implementation 4 Jan 2027. On 6 Nov Peet signed the Flagstone JV implementation deed with Brown-Neaves (49.9% at A$615m, conditional on the Peet deal completing), and Warburg Pincus raised its non-binding Ingenia proposal to A$5.55 plus about 5 cents (up to A$5.60), above AVID's A$5.50, asking for due diligence back by 10 Nov and exclusivity to 14 Dec. Ingenia's board has not declared it superior; the Peet deed stays on foot. Stage announced to booklet_out; expected payment 31 Dec to 4 Jan 2027. The 3 Nov court orders were missed by the 3 to 5 Nov desks. Sources: Kalkine, 3 Nov (https://kalkinemedia.com/au/news/announcements/peet-limited-receives-federal-court-approval-to-hold-shareholder-meeting-for-ingenia-acquisition-scheme) and 5 Nov (https://kalkinemedia.com/au/news/announcements/peet-limited-sends-scheme-booklet-for-ingenia-communities-acquisition-shareholders-meeting-set-for-december-7-2026); The Weekly Source, 6 Nov (https://www.theweeklysource.com.au/ingenia-receives-improved-takeover-offer-from-warburg-pincus/). The releases themselves are to be confirmed.
- A11 (Atlantic Lithium, Huayou scheme): the Supreme Court of WA ordered the scheme meeting on 5 Nov. Meeting 3pm AWST 14 Dec; booklet to be sent by 12 Nov; AIM suspension on 21 Dec (the day after the effective date) and cancellation on 13 Jan 2027 (the day after implementation) put implementation about 12 Jan 2027. Meeting date added, expected payment 31 Dec to 12 Jan 2027, terms note updated by hand. Stage stays announced until the booklet is out. PRC, ECOWAS and Ghana conditions still open. Source: Kalkine, 5 Nov (https://kalkinemedia.com/au/news/announcements/atlantic-lithium-receives-supreme-court-approval-to-hold-scheme-meeting-for-huayou-acquisition-on-december-14-2026); the release itself is to be confirmed.
- Both carried into config/live_deals.csv with src/deal_files.py --add. It again reports AUC's file (default all scrip) differs from the row (the all-elect-cash mix); kept the row as decided on 1 Nov. Terms unchanged on every deal.
- Deal database unchanged (no deal completed or ended), so base rates and odds not rerun. Deal monitor rerun on stored closes (5 Nov).

Analysed: nothing placed or carded without a valuation. For the record, in order of expected_yearly: GL1 (+146%), A11 (+76% with the later payment date), MEI (+26%), BET (+21%), RWC (+19%); cash deals stay barred (test 9c failed), MEI's card stays "waiting" (trigger not met). US deals watched only, no special situation type has passed.

Placed: nothing (no valuation tonight). No limit could be checked without the clerk run.

## 2026-11-09, Nightly job started by the desk after the 8:17pm run did not fire; valuation in; no material deal news found; nothing placed

Checked:
- All 19 test files in tests/ pass under python3 -I.
- The scheduled 8:17pm nightly run did not start at all tonight (GitHub Actions listed no scheduled run for 9 Nov; the last scheduled run was for 6 Nov). This is the third weeknight in four that the schedule has not fired on time, and the first since it was moved off the half hour on 8 Nov. At 9:47pm NZDT the desk wrote "Desk run 2026-11-09 21:47 NZ: the 8:17pm job had not landed" to config/run_now.txt and pushed it (commit c5db3c6). That run (Actions run 14) started at 9:47pm and committed "Nightly data 2026-11-09" (83705fb). If the scheduled run turns up late, it will skip the day as already valued.
- Practice valuation for 9 Nov: NZ$99,511.91, 0.65% below the peak, no limit flags. src/actions.py practice check: nothing missing.
- Note: origin/main had been force-pushed since the last local copy (the old 5 and 6 Nov nightly commits are no longer in the history, though their valuations are in the ledger). The desk worked from the remote main as it stands.
- reports/data_checks.md (9 Nov): no price flags. Eleven deal file findings, all "last checked 8 days ago" (AX1, VAU, BET, AUC, SDF, RWC, MEI, CWY, FPR, RTH, GL1); no key date has passed since any file was checked. The ASX announcement pages and the ASX data feed still can't be opened from the desk (the fetch needs an approval no one is there to give; InvestSMART and Market Index pages failed too), so the files could not be re-checked against primary sources tonight. Their last_checked dates are left as they are rather than marked checked on news searches alone; the findings stand until a desk can open the announcement lists.
- Scan of the 13 live ASX deals since the 6 Nov entry, by news searches. Nothing new found for AX1, VAU, BET, OML, AUC, SDF, PPC, RWC, MEI, CWY, FPR, A11, RTH or GL1. Ingenia (PPC's scrip leg): nothing found after Warburg Pincus's 6 Nov A$5.55 proposal; its due diligence deadline is 10 Nov. OML's FIRB approval (deadline 13 Nov) not yet announced. VAU's election outcome announcement (Genesis, "VAU indicative outcome of scheme consideration elections") exists but could not be opened; meeting still 11 Nov.
- No new binding ASX or NZX control deal of A$100m (NZ$20m) or more found. NZX: nothing new on thl or SkyCity.
- Research watch list (reports/watch_triggers.md, 9 Nov): no trigger hit. Nearest: JIN (+1.3%), MAD (+1.9%), DSK (+2.9%). No event in research/watch_events.csv fell between 7 and 9 Nov; SXL's ticker change to SMG is tomorrow.
- US leads (reports/deal_monitor.md): watched only, as test 9b has not passed.

Changed:
- Nothing on the live list or in the deal database (no deal completed or ended), so base rates and odds were not rerun. Deal monitor rerun on 9 Nov closes; no change from the nightly job's output.

Analysed, in order of expected_yearly: GL1 (+126%), A11 (+82%), MEI (+42%, late case +46%), RWC (+37%), BET (+22%); the rest are below zero at the base rate, and AX1 and PPC have no figure. Cash deals stay barred (test 9c failed). MEI's card (research/cards/2026-11-02-MEI.json) stays "waiting": its re-test trigger, a CIMCE filing with a decision date or a ruling that the regime doesn't apply, has not been announced. MEI's gap has widened to 15.8% on a 0.235 close. VAU and AUC are below zero after costs; PPC's scrip leg still carries Ingenia's own bids. No special situation type has passed; no research card is "ready" and none is held.

Placed: nothing.

## 2026-11-10, Nightly job started by the desk again; valuation in; AVID matches Warburg's A$5.55 for Ingenia (Peet's scrip leg); Carnaby paid; Articore reopened for the research desk; nothing placed

Checked:
- All 19 test files in tests/ pass under python3 -I.
- The scheduled 8:17pm nightly run did not start again (GitHub Actions showed no scheduled run for 10 Nov; the last scheduled runs were the late 9 Nov ones at 6:49am and 7:37am NZDT). The desk wrote "Desk run 2026-11-10 21:46 NZ: the 8:17pm job had not landed" to config/run_now.txt and pushed it (commit 8e8dfe7); that run (Actions run 17) committed "Nightly data 2026-11-10" (a010a56) within minutes. This is the second weeknight running that the schedule has not fired since it moved to 8:17pm.
- Practice valuation for 10 Nov: NZ$100,059.08, 0.10% below the peak, no limit flags. src/actions.py practice check: nothing missing.
- reports/data_checks.md (10 Nov): no price flags. Twelve deal file findings, all "last checked 8 or 9 days ago" (AX1, VAU, BET, OML, AUC, SDF, RWC, MEI, CWY, FPR, RTH, GL1); no key date has passed since any file was checked. The ASX announcement pages still can't be opened from the desk (Kalkine, Market Index, ListCorp and the company sites failed or needed an approval no one was there to give), so those files keep their dates; PPC and CNB were updated from news reports of the releases, as below.
- Scan of the live ASX deals since the 9 Nov entry, by news searches. Nothing new found for AX1, VAU, BET, OML, AUC, SDF, RWC, MEI, CWY, FPR, A11, RTH or GL1. VAU's meeting is tomorrow (11 Nov); its election outcome release still could not be opened. CWY's regulatory filings (due by 10 Nov) not yet reported. OML's FIRB deadline is 13 Nov.
- No new binding ASX or NZX control deal of A$100m (NZ$20m) or more found. NZX: nothing new on thl or SkyCity.
- US leads (reports/deal_monitor.md): watched only, as test 9b has not passed.

Changed:
- PPC (Peet, Ingenia scheme): on 10 Nov AVID matched Warburg Pincus with a revised non-binding A$5.55 cash per Ingenia security, plus up to 5 cents of permitted distribution (A$5.60). Ingenia's board found it equal or superior under the AVID process deed, which was amended: AVID's exclusivity runs to 14 Dec, a rival keeps due diligence access for four days after a match, and Warburg keeps access to 13 Nov. No recommendation, no binding deal, and no Bidder Superior Proposal under the Peet deed; Ingenia says it keeps working towards acquiring Peet. AVID's exclusivity now ends after Peet's vote (7 Dec) and a day before the second court date (15 Dec). Sources: Sharecafe, 10 Nov 2026 (https://www.sharecafe.com.au/2026/11/10/ingenia-communities-sees-matched-offer-from-avid-property-group/); The Weekly Source, 10 Nov 2026 (https://www.theweeklysource.com.au/ingenia-takeover-battle-reaches-3-2-billion-dollars-but-is-the-bidding-over/). Deal file updated; terms unchanged; carried into config/live_deals.csv with src/deal_files.py --add (file_checked only).
- CNB (Carnaby, Evolution scheme): implemented on 10 Nov at 0.0682 Evolution shares a share; delisting 11 Nov. Source: Kalkine's report of the implementation release (https://kalkine.com.au/news/announcements/carnaby-resources-scheme-implemented-as-evolution-mining-acquires-all-shares-on-10-november-2026); the ASX release itself could not be opened. Deal database row AU-2026-15: outcome completed, outcome date and implementation date 10 Nov 2026, 106 days. Deal file stage set to implemented. It was not on the live list (only the payment was left).
- EUR (European Lithium): implementation (5 Nov) still not confirmed from any source the desk could open; its row stays pending.
- Deal database changed, so src/history/deal_base_rates.py and src/history/deal_odds.py were rerun (ASX 232 of 284 paid, 82%). src/deal_files.py --add: it again reports AUC's file (default all scrip) differs from the row (the all-elect-cash mix); kept the row as decided on 1 Nov. Deal monitor rerun on 10 Nov closes.
- SXL is now ASX:SMG (Seven Media Group), as set for today in research/watch_events.csv: no SXL close came in tonight. The watch trigger (research/watch_triggers.csv) and the price fetch line (config/universe_watch.csv) moved to SMG, and SMG added beside SXL in src/research_rank.py's held list. Its price history stays under data/prices/ASX/SXL.csv; the SMG fetch starts tonight.

Research watch list (reports/watch_triggers.md, 10 Nov):
- Hit: ASX:ATG (Articore) closed at A$0.345 (low A$0.325, 40,313 shares), at its trigger. The other conditions in research/picks/ATG.md: before the December quarter update (due about 15 to 30 Jan 2027), yes; nothing else changed, as far as the desk could see (no announcement found since the 6 Nov bid that set the trigger, by news searches; the announcement list itself couldn't be opened, so the research desk should confirm). Marked "reopened: 2026-11-10" in research/picks/INDEX.md for the research desk to re-run the deep dive. Nothing is bought from the watch list.
- Near: MAD (+1.9%), DSK (+2.9%), GDF (+3.2%), FWD (+3.5%), JIN (+3.6%).

Analysed, in order of expected_yearly: GL1 (+117%), A11 (+80%), MEI (+63%, late case +66%), BET (+23%), RWC (+11%); the rest are below zero at the base rate, and AX1 and PPC have no figure (PPC is below its break price). GL1, A11, BET and RWC are cash deals, barred while test 9c has failed. MEI's card (research/cards/2026-11-02-MEI.json) stays "waiting": its re-test trigger (a CIMCE filing with a decision date, or a ruling that the regime doesn't apply) has not been announced. No special situation type has passed; no research card is "ready" and none is held.

Placed: nothing.

## 2026-11-11, Nightly job started by the desk a third night running; valuation in; Vault holders approve the Genesis scheme (court 16 Nov); no watch-list share reopened; nothing placed

Checked:
- All 19 test files in tests/ pass under python3 -I.
- The scheduled 8:17pm nightly run did not start again (GitHub Actions: no scheduled run for 11 Nov; the last scheduled run was the late one at 5:26am NZDT on 11 Nov, which valued 10 Nov). The desk wrote "Desk run 2026-11-11 21:46 NZ: the 8:17pm job had not landed" to config/run_now.txt and pushed it (a06da20); Actions run 20 committed "Nightly data 2026-11-11" (bd654b2) within three minutes. Third weeknight running the schedule has not fired at 8:17pm; worth a look at the workflow's cron and gate.
- Practice valuation for 11 Nov: NZ$100,113.74, 0.05% below the peak, no limit flags. src/actions.py practice check: nothing missing.
- reports/data_checks.md (11 Nov): no price flags. Deal file findings: VAU's meeting (11 Nov) passed since its file was checked, dealt with below. The other eleven (AX1, BET, OML, AUC, SDF, RWC, MEI, CWY, FPR, RTH, GL1) are "last checked 9 or 10 days ago" with no key date passed; the ASX announcement pages still can't be opened from the desk, so their files keep their dates.
- Scan of the live ASX deals since the 10 Nov entry, by news searches. Nothing new found for AX1, BET, OML (FIRB deadline 13 Nov), AUC, SDF, PPC, RWC, MEI, CWY (regulatory filings due by 10 Nov not yet reported), FPR, A11, RTH or GL1. No new binding ASX or NZX control deal of A$100m (NZ$20m) or more found. US leads watched only (test 9b not passed).

Changed:
- VAU (Vault, Genesis scheme): Vault holders approved the scheme resolution by the requisite majorities at the 11 Nov meeting; Vault has applied for the second court hearing on 16 Nov 2026 (Supreme Court of WA). Vote percentages not yet seen. Source: Genesis release as reported by TipRanks, 11 Nov 2026 (https://www.tipranks.com/news/company-announcements/vault-shareholders-approve-proposed-genesis-merger); the ASX release itself could not be opened. Deal file: stage vote_passed, holder approval moved to conditions met, line added under Recent announcements, last_checked 11 Nov. Carried into config/live_deals.csv with src/deal_files.py --add. Indicative timetable unchanged: effective 17 Nov, record 19 Nov, implementation 26 Nov.
- src/deal_files.py --add again reports AUC's file (default all scrip) differs from the row (the all-elect-cash mix); kept the row as decided on 1 Nov. EUR and RCT are unconditional with only payment left, so not on the live list. Deal database unchanged, so no rerun of base rates or odds.
- Deal monitor rerun.

Research watch list (reports/watch_triggers.md, 11 Nov): no trigger hit. Near: MAD (+1.9%), ATG (+2.9%, already reopened 10 Nov), GDF (+3.2%).
Events dated today (research/watch_events.csv):
- NZX:RAD H1 FY27 result: not found from any source the desk could open (radiuscare.co.nz investor page shows nothing for 11 Nov; ShareChat and radiushealth.co.nz needed an approval no one was there to give). Last close in the data NZ$0.42 (9 Nov). Not reopened; the research desk should read the result and test it against the reopen conditions in research/picks/NZ_RAD.md (strong result at NZ$0.44 or below would reopen it).
- ASX:MYX Cosette's High Court special leave deadline: no report found of an application or a settlement. Closed A$3.36. Not reopened (no settlement or judgment with an amount; price far above A$0.72).
- ASX:STP AGM: no AGM trading update found. Closed A$0.135, above the A$0.11 trigger. Not reopened.

Analysed, in order of expected_yearly: GL1 (+142%), A11 (+89%), MEI (+72%), BET (+16%), RWC (+4%); the rest below zero at the base rate, AX1 and PPC with no figure. GL1, A11, BET and RWC are cash deals, barred while test 9c has failed. MEI's card stays "waiting": no CIMCE filing or ruling announced. No special situation type has passed; no research card is "ready" and none is held.

Placed: nothing.

## 2026-11-12, Nightly job started by the desk a fourth night running; valuation in; Auric (AWJ) hit its watch price on a A$17m placement, so not reopened; no live deal news; nothing placed

Checked:
- All 19 test files in tests/ pass under python3 -I.
- The scheduled 8:17pm nightly run did not start again (GitHub Actions: no scheduled run for 12 Nov; the last scheduled run was the late one at 5:12am NZDT on 12 Nov, which found 11 Nov already valued). The desk wrote "Desk run 2026-11-12 21:46 NZ: the 8:17pm job had not landed" to config/run_now.txt and pushed it (cc514cd); Actions run 23 committed "Nightly data 2026-11-12" (a455ee7) within three minutes. Fourth weeknight running the schedule has not fired at 8:17pm; the workflow's cron and gate need a look.
- Practice valuation for 12 Nov: NZ$100,652.99, a new peak, no limit flags; ledger chain ok. src/actions.py practice check: nothing missing.
- reports/data_checks.md (12 Nov): no price flags. Eleven deal file findings (AX1, BET, OML, AUC, SDF, RWC, MEI, CWY, FPR, RTH, GL1), all "last checked 10 or 11 days ago"; no key date has passed since any was checked (OML's FIRB deadline is tomorrow, 13 Nov). The ASX announcement pages still can't be opened from the desk, so the files keep their dates.
- Scan of the live ASX deals since the 11 Nov entry, by news searches. Nothing new found for AX1, VAU (court 16 Nov), BET (ACCC decision due 26 Nov), OML, AUC (election closes 20 Nov), SDF, PPC (latest Ingenia reports found are the 10 Nov AVID match already logged), RWC, MEI, CWY, FPR, A11, RTH or GL1. A TipRanks item on GL1's board rejecting FIRB allegations carries a 2025 date stamp and is not new. A Kalkine headline mentions a G8 Education (GEM) takeover proposal, but the page could not be opened and no other source confirms it or that it is binding; not added. No new binding ASX or NZX control deal of A$100m (NZ$20m) or more found. US leads watched only (test 9b not passed).

Changed:
- Nothing on the live list or in the deal database, so base rates and odds were not rerun. Deal monitor rerun on 12 Nov closes; no change to the committed output.

Research watch list (reports/watch_triggers.md, 12 Nov):
- Hit: ASX:AWJ (Auric Mining) closed at A$0.20 (low A$0.195, 2.4m shares) after a trading halt on 11 Nov (no trades). The other condition in research/picks/AWJ.md fails: the trigger needs the Ore Reserve still pending and no placement, and Auric announced a A$17m two-tranche placement at A$0.185 (91.9m shares; tranche 2 subject to a mid-December meeting) plus an SPP of up to A$3m at the same price, mainly for the Union Jack and Iron Maiden acquisitions and drilling. The Munda Ore Reserve is still not released. This is the file's bad case (a placement before the reserve), though above its A$0.16 exit level. Not reopened. It also reopened from a halt more than 5% lower on heavy volume, so rulebook section 9 bars a position for 30 sessions anyway. Sources: Sharecafe, 12 Nov 2026 (https://www.sharecafe.com.au/2026/11/12/auric-mining-secures-a17-million-placement-launches-spp-to-fuel-growth-strategy/); Discovery Alert, 12 Nov 2026 (https://discoveryalert.com/asx-stock-news/mining/awj-auric-mining-burbanks-placement-november-2026/).
- Near: DSK (+1.5%), MAD (+1.9%), JIN (+2.6%), ATG (+2.9%, already reopened 10 Nov).
Events dated today (research/watch_events.csv):
- ASX:CTD AGMs with FY27 guidance: no FY27 EBITDA guidance found from any source the desk could open (the AGM reports seen give none). The Q1 FY27 update on 11 Nov, as reported by Kalkine Media, gave underlying EBITDA of A$23.5m against A$37.6m a year earlier, TTV A$2.55bn (down 3.8%), FY27 corporate costs about A$39m and capex A$30m to A$35m. Closed A$3.65, above the A$3.25 reopen price, and nothing points to A$125m of EBITDA. Not reopened; the research desk should read the AGM address for guidance. Source: https://kalkinemedia.com/au/news/announcements/corporate-travel-management-reports-q1-fy27-ttv-of-255-billion-with-97-client-retention-rate
- ASX:PAC strategic review update at the AGM: the board said due diligence on River Capital's proposal is ongoing and no decision has been made; the options are still the River proposal, a sale or delisting; the buyback stays paused. PAC is "rejected", so nothing to reopen. Source: Kalkine Media, 12 Nov 2026 (https://kalkinemedia.com/au/news/announcements/pacific-current-group-declares-debt-free-status-and-updates-on-strategic-review-at-2026-agm).
- ASX:AFG warehouse facility due: no announcement of its renewal terms found. Closed A$1.56, above the A$1.41 reopen price. Not reopened.

Analysed, in order of expected_yearly: GL1 (+153%), A11 (+90%), MEI (+63%), BET (+23%), RWC (+12%); the rest below zero at the base rate, AX1 and PPC with no figure. GL1, A11, BET and RWC are cash deals, barred while test 9c has failed. MEI's card (research/cards/2026-11-02-MEI.json) stays "waiting": no CIMCE filing or ruling announced. No special situation type has passed; no research card is "ready" and none is held.

Placed: nothing.
