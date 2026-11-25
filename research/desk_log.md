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

## 2026-11-13, Nightly job started by the desk a fifth night running; valuation in; FIRB clears oOh!media (OML); new deal Big River (BRI) A$1.62 cash scheme added; ASG hit its watch price, waiting on the 20 Nov AGM; nothing placed

Checked:
- All 19 test files in tests/ pass under python3 -I (before and after tonight's changes).
- The scheduled 8:17pm nightly run did not start again (GitHub Actions: no scheduled run for 13 Nov; the last scheduled run was the late one at 5:50am NZDT on 13 Nov, which found 12 Nov already valued). The desk wrote "Desk run 2026-11-13 21:52 NZ: the 8:17pm job had not landed" to config/run_now.txt and pushed it (05904c2); Actions run 26 committed "Nightly data 2026-11-13" (0409ed8) about seven minutes later. Fifth weeknight running the schedule has not fired at 8:17pm; the workflow's cron and gate still need a look.
- Practice valuation for 13 Nov: NZ$100,452.34, 0.20% below the 12 Nov peak (NZ$100,652.99), no limit flags; ledger chain ok (all eight files). src/actions.py practice check: nothing missing.
- reports/data_checks.md (13 Nov): no price flags. Deal file findings: OML's FIRB deadline (13 Nov) passed since its file was checked, dealt with below. The other ten (AX1, BET, AUC, SDF, RWC, MEI, CWY, FPR, RTH, GL1) are "last checked 11 or 12 days ago" with no key date passed; the ASX announcement pages still can't be opened from the desk, so their files keep their dates.
- Scan of the live ASX deals since the 12 Nov entry, by news searches. Nothing new found for AX1, VAU (court 16 Nov), BET, AUC, SDF, PPC, RWC, MEI (no CIMCE filing or ruling), CWY, FPR, A11, RTH or GL1. No NZX control deal found. US leads watched only (test 9b not passed).

Changed:
- OML (oOh!media, I Squared scheme): FIRB approval received on 13 Nov 2026, the extended statutory deadline. BidCo told oOh! the Treasurer has no objection under the FATA, satisfying SIA clause 3.1(a); no conditions reported. Still subject to Court approval at the second hearing on 18 Nov and the usual conditions; no new timetable or Permitted Dividend dates seen (effective 19 Nov, record 3 Dec, implementation 10 Dec stand). Sources: Kalkine Media, 13 Nov 2026 (https://kalkinemedia.com/au/news/announcements/firb-approves-i-squared-capitals-acquisition-scheme-for-oohmedia); TipRanks (https://www.tipranks.com/news/company-announcements/firb-approval-received-for-proposed-oohmedia-scheme); the ASX release itself could not be opened. Deal file: FIRB moved to conditions met, line added under Recent announcements, last_checked 13 Nov. Stage stays vote_passed until the Court approves. Carried into config/live_deals.csv with src/deal_files.py --add.
- New deal, BRI (Big River Industries): binding Scheme Implementation Deed announced 13 Nov 2026 with CTL (Aust) Pty Ltd (private; sole director Shan Kanji) at A$1.62 cash a share, about A$156m equity (A$216m enterprise value), above the A$100m floor. A franked special dividend of up to A$0.21 may be paid and deducted from the A$1.62. CTL already holds 19.9%; Anacacia (about 28.8%) and NAOS (about 30.7%) intend to vote in favour; board unanimous, subject to the expert (not yet named) and no superior proposal. Conditions: holder vote, Court, expert, ACCC clearance or waiver, no MAC, some contract consents; no financing condition. Reciprocal A$1.56m break fees. Indicative: meeting early Feb 2027, implementation late Feb 2027; End Date 7 months from announcement (about 13 Jun 2027, to confirm). Undisturbed price A$1.11, the 12 Nov close (45.9% premium; 1-month VWAP A$1.10, 3-month A$1.20). The deal followed unsolicited non-binding CTL proposals and exclusivity, but no dates were given and no earlier public disclosure or rival bid was found, so the undisturbed date stays 12 Nov; to recheck against the primary. Sources: SureStone summary of the release (https://surestone.com.au/news/asx/bri/big-river-agrees-162-cash-scheme-with-ctl-2026-11-13); Small Caps (https://smallcaps.com.au/article/big-river-industries-agrees-to-dollar156m-ctl-takeover-proposal); Discovery Alert (https://discoveryalert.com/asx-stock-news/mining/bri-big-river-industries-ctl-takeover-november-2026/); MarketScreener (its "80.10% from Anacacia and NAOS" and A$120m framing conflicts with the others and was not used). The ASX release could not be opened. Deal file research/deals/BRI.md written first; src/deal_files.py --add added the live row (AU-2026-28), the deal database row and BRI to the nightly fetch; the desk set the undisturbed price and date by hand in config/live_deals.csv and the premium, equity value, break fee, stake and intentions in deals/au/au_deals_2025_2026.csv. No BRI price yet, so it is not in tonight's monitor.
- src/deal_files.py --add again reports AUC's file (default all scrip) differs from the row (the all-elect-cash mix); kept the row as decided on 1 Nov. EUR and RCT stay off the live list (only payment left).
- Deal database changed, so src/history/deal_base_rates.py (ASX 232 of 284 paid, 82%; NZX 28 of 37) and src/history/deal_odds.py were rerun. Deal monitor rerun on 13 Nov closes.

Research watch list (reports/watch_triggers.md, 13 Nov):
- Hit: ASX:ASG (Autosports Group) closed at A$0.995, at its A$1.00 trigger. The other condition in research/picks/ASG.md is the AGM on 20 Nov giving H1 FY27 guidance of A$20m or more (or no figure) with the order bank timing unchanged; the AGM hasn't happened, so it can't be met yet. Not reopened tonight; the desk checks it on 20 Nov (watch_events row already set).
- Hit: ASX:AWJ (Auric Mining) at A$0.195: same as 12 Nov, the A$17m placement before the Ore Reserve fails its condition. Not reopened; section 9 placement bar also applies.
- Near: MAD (+1.9%).
Events dated today (research/watch_events.csv):
- ASX:CAF annual meeting: no AGM address or guidance change found from any source the desk could open. Closed A$0.395, above the A$0.35 reopen price. Not reopened; the research desk should read the address for whether SEQ sits inside FY27 guidance.
- ASX:EVZ AGM (10% placement facility vote): no result found. Closed A$0.39, above the A$0.295 reopen price. Not reopened.

Analysed, in order of expected_yearly: GL1 (+155%), A11 (+70%), MEI (+57%), RWC (+29%), BET (+16%); the rest below zero at the base rate (OML -18% after FIRB, the price having already closed the gap), AX1 and PPC with no figure, BRI not yet priced. GL1, A11, RWC, BET, OML and BRI are cash deals, barred while test 9c has failed. MEI's card (research/cards/2026-11-02-MEI.json) stays "waiting": no CIMCE filing or ruling announced. No special situation type has passed; no research card is "ready" and none is held. No card reached the red team or decide.py tonight.

Placed: nothing.

## 2026-11-16, Nightly job started by the desk a sixth night running; valuation in; new NZX deal Metro Glass (MPG) NZ$1.65 cash takeover notice added; BetMakers ACCC date moves to 3 Dec; Atlantic Lithium booklet out; nothing placed

Checked:
- All 19 test files in tests/ pass under python3 -I (before and after tonight's changes).
- The scheduled 8:17pm nightly run did not start (GitHub Actions: no run for 16 Nov by 9:46pm NZ; the last scheduled run was 13 Nov at 5:27am NZ, which found 13 Nov already valued). The desk wrote "Desk run 2026-11-16 21:47 NZ: the 8:17pm job had not landed" to config/run_now.txt and pushed it (196dba5); Actions run 29 committed "Nightly data 2026-11-16" (2463faa) within about ten minutes. Sixth weeknight running the schedule has not fired at 8:17pm; the workflow's cron and gate still need a look.
- Practice valuation for 16 Nov: NZ$100,387.46, 0.26% below the peak, no limit flags; ledger chain ok (all eight tables). src/actions.py practice check: nothing missing.
- reports/data_checks.md (16 Nov): no price flags (BRI's +41% is the deal). Deal file findings: VAU's second court hearing (16 Nov) passed since its file was checked, dealt with below; BET and A11 updated below; the other nine (AX1, AUC, SDF, RWC, MEI, CWY, FPR, RTH, GL1) are "last checked 15 days ago" with no key date passed. The ASX and NZX announcement pages still can't be opened from the desk (permission refusals again tonight), so the scan used news searches and the ACCC register.
- Scan of the live ASX deals since the 13 Nov entry: nothing new found for AX1, AUC (election closes 20 Nov, meeting 27 Nov), SDF, PPC, RWC, MEI (no CIMCE filing or ruling), CWY, FPR, RTH, GL1, BRI or OML (court 18 Nov). US leads watched only (test 9b not passed).

Changed:
- VAU (Vault, Genesis scheme): second court hearing listed for 2.15pm AWST today (7.15pm NZ). No release on the outcome found by about 10pm NZ. VAU traded normally (A$5.75, 11.5m shares). Stage stays vote_passed until approval is seen; if approved, 17 Nov is the effective date and last trading day, record 19 Nov, implementation 26 Nov. Deal file: line added, last_checked 16 Nov.
- BET (BetMakers, Tabcorp scheme): the ACCC register shows the Phase 1 timeline was extended by 5 business days at the parties' request on 9 Nov 2026, so the determination period now ends 3 Dec 2026 (was 26 Nov). Still "Under assessment", no notice of competition concerns. Source: ACCC register MN-20040, https://www.accc.gov.au/public-registers/acquisitions-and-mergers-registers/acquisitions-register/tabcorp-betmakers. Deal file and the row's terms note updated.
- A11 (Atlantic Lithium, Huayou scheme): booklet dispatch completed 13 Nov 2026; indicative meeting 14 Dec, Second Court Date 17 Dec, Effective 18 Dec 2026, Implementation 12 Jan 2027. Expert's conclusion not yet read from the booklet. Stage announced -> booklet_out. Source: ShareCafe summary of the release, https://www.sharecafe.com.au/2026/11/13/atlantic-lithium-completes-dispatch-of-scheme-booklet-for-proposed-huayou-acquisition/ (ASX release not opened).
- New deal, MPG (Metro Performance Glass, NZX): takeover notice under Takeovers Code rule 41, announced Monday 16 Nov 2026, from Amari Metals Australia, related to Metro's 51% holder Metro Glass Investments: a full offer at NZ$1.65 cash a share (about NZ$40.6m for the company, above the NZ$20m floor), also covering options and performance rights. Metro Glass Investments will accept within one working day of dispatch, which meets the only condition reported (more than 50%). Metro has formed an independent committee; no recommendation or adviser yet. The offer must be sent 14 to 30 days after the notice. Amari says it won't support resuming dividends. Undisturbed price NZ$1.005, the 13 Nov close in the feed (articles round it to NZ$1.01; 64% premium). No earlier approach or rival bid found, so the undisturbed date stays 13 Nov, but MPG rose from NZ$0.74 (27 Oct) to NZ$1.005 (13 Nov) before the notice; a TipRanks item "Amari Discloses Relevant Interest in Metro Shares" is undated and unread, to recheck against the NZX notice. Traded about NZ$1.52 on 16 Nov (The Bottom Line). Sources: TipRanks (https://www.tipranks.com/news/company-announcements/metro-glass-receives-takeover-notice-from-amari; https://tipranks.com/news/company-announcements/trading-halt-applied-to-metro-performance-glass-ordinary-shares), The Bottom Line (https://www.thebottomline.co.nz/nzx-50-at-record-outperforms-most-of-asia-as-serko-rallies-on-clear-step-up/), b2bnews (https://b2bnews.co.nz/news/metro-glass-takeover-amari-offers-1-point-65-a-64-percent-premium/). The NZX notice (announcements.nzx.com/attachment/481508.pdf) could not be opened. Deal file research/deals/NZ_MPG.md written first; src/deal_files.py --add added the live row (NZ-2026-04), the deal database row and MPG to the nightly fetch. Payment date 15 Jan 2027 is the desk's estimate.
- src/deal_files.py --add again reports AUC's file (default all scrip) differs from the row (the all-elect-cash mix); kept the row as decided on 1 Nov.
- Deal database changed, so src/history/deal_base_rates.py (ASX 232 of 284 paid, 82%; NZX 28 of 37) and src/history/deal_odds.py were rerun. Deal monitor rerun on 16 Nov closes.

Research watch list (reports/watch_triggers.md, 16 Nov):
- Hit: ASX:AWJ (Auric Mining) at A$0.19: same as 12 and 13 Nov, the A$17m placement before the Ore Reserve fails its condition. Not reopened; section 9 placement bar also applies.
- ASG is no longer a hit; its 20 Nov AGM check stands.
Events dated today (research/watch_events.csv):
- NZX:PGW, Elders FY26 result (16 Nov): underlying EBIT A$187.7m (+43%), NPAT A$100.5m, dividend 36c; management indicated no material deals on the horizon. Nothing found on the PGW stake (no move above 13.47%, no sale or review). Source: Investing.com summary of the results slides, https://www.investing.com/news/company-news/elders-fy26-slides-ebit-surges-43-on-delta-ag-synergies-93CH-5028237. Not reopened; the Elders meeting on 17 Dec is the next check.

Analysed, in order of expected_yearly: GL1 (+207%), A11 (+100%), MEI (+68%), RWC (+37%), BET (+24%), FPR (+1%); the rest below zero at the base rate; AX1, VAU and PPC with no figure; MPG priced at the pre-notice close (no 16 Nov NZX price in the feed yet). GL1, A11, RWC, BET and FPR are ASX cash deals, barred while test 9c has failed. MEI's card (research/cards/2026-11-02-MEI.json) stays "waiting": no CIMCE filing or ruling announced. MPG is an NZX cash deal, which 9c does not bar, but no card tonight: the offer document and the target company statement don't exist yet, so its conditions (financing, any OIO consent, any other) are unread, the deal file rests on secondary sources, and the feed has no post-notice price. It is the first candidate once the offer is sent and the NZX notice can be read (a position would be capped at NZ$2,500 by the NZX order rule). No special situation type has passed; no research card is "ready" and none is held. No card reached the red team or decide.py tonight.

Placed: nothing.

## 2026-11-17, Nightly job started by the desk but failed its engine checks (a stale test), so no valuation and nothing placed; Vault court approved; new ASX deal Mayne Pharma (MYX) A$6.40 cash scheme added; Peet ACCC cleared; SMG watch-list share reopened

Checked:
- All 19 test files in tests/ pass under python3 -I on the repository's data (before and after tonight's changes).
- The scheduled 8:17pm run did not start (no run for 17 Nov by 9:47pm NZ; the two scheduled runs of 16 Nov fired at 6:07am and 7:35am NZ on 17 Nov, both finding 16 Nov done). The desk wrote "Desk run 2026-11-17 21:49 NZ: the 8:17pm job had not landed" to config/run_now.txt and pushed it (4781519). Actions run 32 started at once and failed at "Engine checks" after about two minutes, so nothing was saved: no "Nightly data 2026-11-17" commit, no 17 Nov valuation, data checks, watch report or trial run. The hub snapshot step still posted.
- Why it failed: tests/test_hedges.py, "NZ monthly average is not used before its month ends" (1 of 13 checks). The nightly fetch brought in FRED's October NZ three-month average (3.25%, usable from 15 Nov), and the check compares the 30 Sep rate with the second-last entry in the series, which is now the September average instead of the August one. The rate code is right (on 30 Sep it uses the August average, 2.98%, known from 15 Sep); the test is pinned to the end of the series and broke when a new month arrived. Reproduced in a scratch copy: with tonight's rate files only this check fails; with it pinned to the dated entries (30 Sep equals the 15 Sep entry, 15 Oct equals the 15 Oct entry) all 19 files pass on both the old and the new data. The desk did not push that change: it is a change to the job's safety checks, so it waits for Cam. Until it is fixed every nightly run (scheduled or desk-started) will stop at the same check.
- Under DAILY_RUN step 1 the desk started the job once and did not start it again; the failed run cannot come good by waiting, so the 45-minute wait was cut short. No orders, nothing entered in the ledger; watching only tonight.
- reports/data_checks.md is still the 16 Nov one (tonight's data check didn't run): no price flags; the nine "last checked 15 days ago" findings (AX1, AUC, SDF, RWC, MEI, CWY, FPR, RTH, GL1) have no key date passed and carry over. The ASX and NZX announcement pages still can't be opened from the desk, so the scan used news searches and secondary summaries of the releases (marked as such in the deal files).

Changed:
- VAU (Vault, Genesis scheme): Supreme Court of WA (Lundberg J) approved the scheme on 16 Nov; orders lodged, effective 17 Nov; VAU suspended from the close on 17 Nov; record 19 Nov; implementation 26 Nov 2026. Stage vote_passed -> court_approved; conditions left: implementation, performance rights, quotation of the new Genesis shares. Stays on the list until paid. Source: Kalkine Media summary of the release, 17 Nov 2026, https://kalkinemedia.com/au/news/announcements/supreme-court-approval-finalizes-genesis-minerals-and-vault-minerals-merger-scheme.
- PPC (Peet, Ingenia scheme): the ACCC determined on 13 Nov that the Peet acquisition and the Flagstone JV may be put into effect (MN-60048); a Tribunal review can be sought until 27 Nov, so the ACCC conditions count as met only after that. For Ingenia, AVID matched Warburg Pincus on 15 Nov at A$5.55 plus up to 5c (non-binding); the AVID process deed was ended and both bidders now have non-exclusive process deeds, with binding offers due 8 Dec, the day after the Peet vote. Neither is a Bidder Superior Proposal under the Peet deed, which Ingenia says it keeps to. Row's terms note and the deal file updated. Source: StockWire X, 16 Nov 2026, https://stockwirex.com/asx-stock-news/real-estate-reits/ina-ingenia-communities-avid-matching-proposal-november-2026/ (secondary; ACCC register entry to confirm).
- MPG (Metro Glass, Amari notice): the NZX announcement page was read (https://www.nzx.com/announcements/483704). It confirms NZ$1.65 cash, Amari and the 51% holder MGI in the same group, MGI would accept, and the independent committee (Beck, Mayne, Khatri). Options get nil; performance rights get NZ$1.65 only if Amari reaches 90%. The page puts the offer window at 10 to 20 working days after the notice (about 27 Nov to 11 Dec), not the 14 to 30 days written last night; to settle from the notice PDF, which still can't be opened. Conditions, financing and OIO are still unread. No row terms changed.
- New deal, MYX (Mayne Pharma, ASX): scheme implementation deed with Gedeon Richter Plc announced 17 Nov 2026 at A$6.40 cash a share, about A$604m (above the A$100m floor), 99.4% above the 16 Nov close of A$3.21 (the undisturbed price, matching the feed). Board unanimous subject to the expert and no superior proposal; Funicular, Mathieson and Trium (about 22.14%) support. Conditions: vote, Court, expert, customary regulatory approvals (FIRB and US antitrust reported, to confirm) and completion of Mayne's sale of its international business to Evaris Pharma, which needs the ACCC. No earlier Richter approach found; the failed 2025 Cosette scheme (AU-2025-03) is a separate deal, so the undisturbed date stays 16 Nov. Traded about A$5.71 to A$5.81 on 17 Nov. Deal file research/deals/MYX.md written first (secondary sources: TipRanks summary of the release, Investing.com, Inside FMCG, Motley Fool, Dealroom); src/deal_files.py --add added the live row (AU-2026-29), the deal database row (filled in by hand: trade bidder, Hungary, 99.4% premium, A$604m, FIRB and overseas competition, board for, 22.14% intentions) and MYX to the nightly fetch. Payment 31 Mar 2027 is the desk's placeholder for "early 2027". MYX is also on the research watch list (Cosette claim); a binding deal puts it in the deal sleeve instead.
- Not added: Noumi (NOU, Arrovest scheme announced 21 Jul 2026): equity about A$34m, below the A$100m floor.
- src/deal_files.py --add again reports AUC's file (default all scrip) differs from the row (all-elect-cash mix); kept the row as decided on 1 Nov.
- Deal database changed, so src/history/deal_base_rates.py (ASX 232 of 284 paid, 82%; NZX 28 of 37) and src/history/deal_odds.py were rerun; src/deal_monitor.py rerun on the 16 Nov closes (no 17 Nov prices stored).
- Nothing new found tonight for AX1, AUC (election closes 20 Nov, meeting 27 Nov), BET (ACCC 3 Dec), OML (second court hearing 18 Nov), SDF, RWC, MEI, CWY, FPR, A11, RTH, GL1 or BRI. US leads watched only (test 9b not passed).

Research watch list (reports/watch_triggers.md from the 16 Nov data; tonight's wasn't written):
- Hit: ASX:SMG (Seven Media Group, formerly SXL) closed A$0.44 on 16 Nov, at its A$0.44 trigger. Its other condition is "nothing else changed": the only recent news is the 5 Nov AGM trading update (TV down, audio flat, publishing down, the A$150m cost program's full benefit in FY28, net debt A$363m), which the 8 Nov deep dive already used, and no later announcement was found (TV Central, 5 Nov 2026, https://www.tvcentral.com.au/free-to-air/7_news/seven-media-group-agm-smg-ticker-trading-update/). Marked "reopened: 2026-11-17" in research/picks/INDEX.md for the research desk to re-run the deep dive. Nothing is placed from the watch list.
- Hit: ASX:AWJ (Auric Mining) at A$0.19, as on 12, 13 and 16 Nov: the A$17m placement fails its "no placement" condition, and the section 9 placement bar applies. Not reopened.
- Event today: NZX:SAN FY26 result and notice of meeting (17 Nov): no FY26 release found in the news searches tonight (only the May 2026 interim result came up). Not reopened; to look again tomorrow.

Analysed: no card tonight. With no 17 Nov valuation in the ledger, section 3 bars any card. In expected_yearly order GL1 (+212%), A11 (+103%), MEI (+69%), RWC (+39%) and BET (+24%) lead; GL1, A11, RWC and BET are ASX cash deals, barred while test 9c has failed, and MEI's card stays "waiting" (no CIMCE filing or ruling). MYX and MPG are priced at their pre-deal closes in the monitor until post-announcement prices land. No research card is "ready" and none is held; no special situation type has passed.

Placed: nothing.

## 2026-11-18, Nightly job started by the desk and failed the same stale rate test again, so no valuation and nothing placed; oOh!media (OML) court approved; Meteoric (MEI) Brazil filing reported for January 2027; SAN result read, not reopened

Checked:
- All 19 test files in tests/ pass under python3 -I on the repository's data (the rate files still hold 16 Nov's series, as no nightly run has saved since).
- The scheduled 8:17pm run did not start (no run created for 18 Nov by 9:46pm NZ). Overnight, scheduled run 33 (5:56am NZ, 18 Nov) failed at "Engine checks" on the same test as last night, and run 34 (6:38am NZ) stopped at the gate. The desk wrote "Desk run 2026-11-18 21:46 NZ: the 8:17pm job had not landed" to config/run_now.txt and pushed it (b3956db). Actions run 35 started at once and failed at "Engine checks" at 9:48pm NZ: tests/test_hedges.py, "NZ monthly average is not used before its month ends", the stale check described in last night's entry (the October NZ three-month average, 3.25%, now in FRED's series moves the second-last entry). Nothing saved: no "Nightly data 2026-11-18" commit, no 18 Nov valuation, data checks, watch report or trial run. The hub snapshot step still posted.
- The desk again did not change the test: it is the job's own safety check, so the fix waits for Cam. Every nightly run will keep stopping at it until it is fixed; the ledger has now missed 17 and 18 Nov. The failed run can't come good by waiting, so the 45-minute wait was cut short. No orders, nothing entered in the ledger; watching only.
- reports/data_checks.md is still the 16 Nov one: no price flags; the nine "last checked 15 days ago" findings carry over with no key date passed (OML's file is now checked). ASX and NZX release pages still can't be opened directly; secondary summaries are marked as such.

Changed:
- OML (oOh!media, I Squared scheme): the Supreme Court of NSW approved the scheme at the second hearing on 18 Nov. Stage vote_passed -> court_approved. Timetable as of 30 Oct still stands as far as seen: effective and last trading 19 Nov, record 3 Dec, implementation 10 Dec 2026; the A$0.10 Permitted Dividend dates are still not seen. Row terms note and deal file updated; src/deal_files.py --add carried the stage, conditions and check date into config/live_deals.csv. Source: TipRanks summary of the release, updated 18 Nov 2026 10:57am AEDT, https://www.tipranks.com/news/company-announcements/nsw-court-approves-proposed-oohmedia-share-acquisition (secondary).
- MEI (Meteoric, Lynas scheme): Agencia iNFRA (13 Nov, updated 14 Nov) quotes Meteoric Brasil's executive director that the change-of-control request to Brazil will be filed in January 2027, with approval expected within 45 days. Brazil's critical-minerals council (Cimce) put rare earths in its high-priority group on 5 Nov and was to set its foreign-investment screening rules at a 20 Nov meeting. That puts approval about late February to mid-March 2027, against the row's 5 Mar payment and the 1 Apr 2027 end date: the late case is the likelier one. A press interview, not a release, so the row's dates are unchanged until Meteoric announces; logged under Recent announcements in research/deals/MEI.md. Source: https://agenciainfra.com/blog/terras-raras-meteoric-deve-protocolar-venda-a-lynas-em-janeiro-de-2027/ (secondary).
- Not added: Nuix (NXL), Haveli A$2.75 cash proposal (18 Nov) is non-binding and indicative under a process and exclusivity deed, so it is not a deal-sleeve deal; Macquarie (28%) reported supportive. Source: Rask Media, 18 Nov 2026, https://www.raskmedia.com.au/2026/11/18/nuix-asxnxl-share-price-soars-49-on-2-75-per-share-takeover-offer/. A candidate for the research desk as a special situation.
- src/deal_files.py --add again reports AUC's file (default all scrip) differs from the row (all-elect-cash mix); kept the row as decided on 1 Nov.
- Deal database unchanged, so base rates and odds were not rerun. src/deal_monitor.py rerun on the 16 Nov closes.
- Nothing new found tonight for AX1, VAU (implementation 26 Nov), BET (ACCC 3 Dec), AUC (election closes 20 Nov), SDF (meeting 27 Nov), PPC, RWC, CWY, FPR, A11, RTH, GL1, BRI, MPG or MYX. US leads watched only (test 9b not passed).

Research watch list (reports/watch_triggers.md is still the 16 Nov one; SMG reopened and AWJ not reopened last night, unchanged):
- NZX:SAN: the FY26 result was released on 16 Nov at 7:30pm NZ (NZX announcement 483771), not 17 Nov; date corrected in research/watch_events.csv. Adjusted EBIT NZ$116.6m, NPAT NZ$74.5m (record), operating cash NZ$89.6m (down 34%), net debt NZ$53.6m, final dividend 5c (record 24 Nov, paid 1 Dec). Mussels fell to NZ$10.3m from NZ$34.8m. The chair is to retire at this year's meeting; nothing on Umios, a nominee or a notice. Not reopened: two conditions fail, operating cash (NZ$89.6m against NZ$90m or more) and price (last stored close NZ$7.00 on 13 Nov against NZ$6.60 or below); the NZ$6.00 route fails on price too. Source: https://www.nzx.com/announcements/483771.
- Today's events: EML AGM, MGX AGM, WJL half-year, ARG interim and the HLO creep date in Webjet. No release or report of any of them was found tonight; not reopened; to look again tomorrow.

Analysed: no card tonight. With no 18 Nov valuation in the ledger, section 3 bars any card. No research card is "ready" and none is held; no special situation type has passed.

Placed: nothing.

## 2026-11-19, Nightly job started by the desk and failed the same stale rate test a third night, so no valuation and nothing placed; no live deal news found; Argosy (ARG) interim read, not reopened

Checked:
- All 19 test files in tests/ pass under python3 -I on the repository's data (the rate files still hold 16 Nov's series, as no nightly run has saved since).
- The scheduled 8:17pm run did not start (no run created for 19 Nov by 9:45pm NZ). Overnight, scheduled run 36 (5:30am NZ, 19 Nov) failed at "Engine checks" and run 37 (6:16am NZ) stopped at the gate. The desk wrote "Desk run 2026-11-19 21:46 NZ: the 8:17pm job had not landed" to config/run_now.txt and pushed it (f9b28cd). Actions run 38 started at once; rates, SEC, prices and NZX prices all fetched, then it failed at "Engine checks" at 9:49pm NZ on the same check: tests/test_hedges.py, "NZ monthly average is not used before its month ends" (the 30 Sep rate, 2.98%, is compared with the second-last entry in FRED's series, now the October average of 3.13% dated 15 Oct, since the November entry of 3.25% arrived). Every other check passed, including the ledger chain. Nothing saved: no "Nightly data 2026-11-19" commit, no 19 Nov valuation, data checks, watch report or trial run. The hub snapshot step still posted.
- The desk again did not change the test: it is the job's own safety check, so the fix waits for Cam (the pinned-date fix is described in the 17 Nov entry). The ledger has now missed 17, 18 and 19 Nov, and every run will stop here until the test is fixed. The failed run can't come good by waiting, so the 45-minute wait was cut short. No orders, nothing entered in the ledger; watching only.
- reports/data_checks.md is still the 16 Nov one: no price flags; the "last checked 15 days ago" findings carry over with no key date passed (AUC's election closes 20 Nov). src/deal_files.py reports no changes and again AUC's file (default all scrip) against the row (all-elect-cash mix); row kept as decided on 1 Nov. ASX release pages still can't be opened from the desk; news searches tonight turned up nothing new.

Changed:
- No live deal changes found tonight for AX1, VAU (record 19 Nov, implementation 26 Nov), BET (ACCC 3 Dec), OML (effective 19 Nov, implementation 10 Dec), AUC (election closes 20 Nov, meeting 27 Nov), SDF (meeting 27 Nov), PPC (Tribunal window to 27 Nov, meeting 7 Dec), RWC, MEI (Cimce's 20 Nov meeting is tomorrow), CWY, FPR, A11, RTH, GL1, BRI, MYX or MPG. MPG: the NZX notice page was read again (https://www.nzx.com/announcements/483704); no offer yet, the window runs about 27 Nov to 11 Dec. No new binding ASX or NZX control deal of A$100m (NZ$20m) or more found.
- Deal database unchanged, so base rates and odds were not rerun. src/deal_monitor.py rerun on the 16 Nov closes. US leads watched only (test 9b not passed).
- research/watch_events.csv: ARG's interim result date corrected to 17 Nov (released 7:31pm NZ) and the row moved into date order.

Research watch list (reports/watch_triggers.md is still the 16 Nov one; no new hits):
- NZX:ARG interim (NZX 483878, 17 Nov): distributable income NZ$31.1m (3.56c), NTA NZ$1.58, interim dividend 3.325c, FY27 guidance held at 6.65c, gearing 36.6%. The Taupo non-core sale went unconditional at NZ$11.4m, 8.6% above book, but the money is not being returned; the board is only "considering" a buyback, with no decision. CEO Mence to step down and chair Morrison to retire at the 2027 meeting. Not reopened: no buyback or capital return announced, no sale with money returned, no 10% holder or approach, and the price is not near NZ$0.88. A buyback announcement would reopen it. Source: https://www.nzx.com/announcements/483878.
- Yesterday's events (EML AGM, MGX AGM, WJL half-year, HLO creep date) and today's (AAC half-year, CCV AGM, BRW AGM, MFB 1H27 and chair change, OCA 1H27): no release or report of any was found in tonight's searches; not reopened; to look again tomorrow.

Analysed: no card tonight. With no 19 Nov valuation in the ledger, section 3 bars any card. No research card is "ready" and none is held; no special situation type has passed.

Placed: nothing.

## 2026-11-20, Nightly job started by the desk and failed the same stale rate test a fourth night, so no valuation and nothing placed; Global Lithium (GL1) booklet out with expert support; oOh!media dividend dates set; Accent second strike; no watch-list share reopened

Checked:
- All 19 test files in tests/ pass under python3 -I on the repository's data (before and after tonight's changes; the rate files still hold 16 Nov's series).
- The scheduled 8:17pm run did not start (no run created for 20 Nov by 9:46pm NZ). Overnight, scheduled run 39 (5:37am NZ, 20 Nov) failed and run 40 (6:23am NZ) stopped at the gate. The desk wrote "Desk run 2026-11-20 21:46 NZ: the 8:17pm job had not landed" to config/run_now.txt and pushed it (6a515a1). Actions run 41 started at once; rates, SEC, prices (ASX and US, no problems) and NZX prices (16 to 18 Nov) fetched, then it failed at "Engine checks" at 9:49pm NZ on the same check: tests/test_hedges.py, "NZ monthly average is not used before its month ends" (the 30 Sep rate, 2.98%, compared with the second-last entry in FRED's series, now 3.13% dated 15 Oct, since the 3.25% entry dated 15 Nov arrived). Every other check passed, including the ledger chain. Nothing saved: no "Nightly data 2026-11-20" commit, no 20 Nov valuation, data checks, watch report or trial run. The hub snapshot step still posted.
- The desk again did not change the test: it is the job's own safety check, so the fix waits for Cam (the pinned-date fix is in the 17 Nov entry). The ledger has now missed 17, 18, 19 and 20 Nov, and every run will stop here until the test is fixed. The failed run can't come good by waiting, so the 45-minute wait was cut short. No orders, nothing entered in the ledger; watching only.
- reports/data_checks.md is still the 16 Nov one: no price flags. Its "last checked" findings: AX1, SDF, FPR and GL1 files checked tonight; the rest carry over with no key date passed except AUC (cash election closed 20 Nov, see below). ASX and NZX release pages still can't be opened from the desk, so tonight's facts come from secondary summaries of the releases unless marked primary.

Changed:
- GL1 (Global Lithium, Titan scheme): the Supreme Court of WA ordered the meeting on 17 Nov and ASIC registered the booklet about 18 Nov. Meeting 10am AWST 22 Dec 2026. Independent expert BDO: in the best interests of shareholders. FIRB and ACCC still open; no funding update. Stage announced -> booklet_out, booklet date 18 Nov, expert condition moved to met. Deal file and row (stage, booklet date, conditions, terms note) updated; src/deal_files.py --add carried the header. Sources: Kalkine Media, https://kalkinemedia.com/au/news/announcements/global-lithium-resources-secures-court-approval-for-shareholder-scheme-meeting-on-titan-australia-mining-takeover-set-for-22-december-2026 ; TipRanks, https://www.tipranks.com/news/company-announcements/asic-registers-booklet-for-proposed-titan-acquisition-of-global-lithium (secondary).
- OML (oOh!media, I Squared scheme): effective 19 Nov, suspended from that close. The A$0.10 fully franked Permitted Dividend is declared: record 25 Nov, paid 2 Dec 2026 (ex-date not stated). Scheme record 3 Dec, implementation 10 Dec unchanged; A$1.58 scheme cash plus the A$0.10 dividend, A$1.68 in all, so no change to cash_per_share. Deal file dates_basis and the row's terms note updated. Source: Kalkine Media summary of the 19 Nov release, https://kalkinemedia.com/au/news/announcements/oohmedia-scheme-legally-effective-following-supreme-court-approval-of-i-squared-capital-acquisition-010-fully-franked-dividend-declared (secondary).
- AX1 (Accent, Frasers on-market bid): 20 Nov AGM gave a second strike (remuneration report 43.7% against) but the spill failed (59.45% against); directors re-elected. Frasers' substantial holder notice of 20 Nov shows about 25% after buying 6.38m shares at A$0.65 on market from 30 Oct to 19 Nov. Bid terms unchanged. Logged in the deal file; no row terms changed. Sources: https://www.ragtrader.com.au/news/accent-board-survives-spill-vote-despite-second-strike ; https://www.tipranks.com/news/company-announcements/accent-group-agm-backs-directors-as-remuneration-report-draws-second-strike (secondary).
- SDF (Steadfast scheme): logged in the deal file that the ACCC set an effective notification date of 10 Nov with Phase 1 running to 22 Dec 2026, the planned implementation day, so a Phase 2 would push completion into 2027 (reported 13 Nov). Meeting 27 Nov unchanged. Source: https://www.insurancebusinessmag.com/au/news/breaking-news/accc-review-leaves-no-room-in-steadfast-takeover-timetable-597257.aspx (secondary; ACCC register to confirm).
- FPR (FleetPartners scheme): logged that the 16 Nov FY26 result puts the first court hearing in December 2026 and the meeting around February 2027, with any special dividend (up to 26c, out of the A$5.30) decided nearer implementation. Row unchanged (31 Mar 2027 payment stands). Source: https://stockwirex.com/?p=56332 (secondary).
- AUC: the cash election closed 7pm 20 Nov; no release on the result found yet. Meeting 27 Nov. src/deal_files.py again reports the file (default all scrip) against the row (all-elect-cash mix); row kept as decided on 1 Nov, to revisit once the election outcome is announced.
- BET: ACCC register MN-20040 read tonight (primary): still Phase 1, "Under assessment", determination due 3 Dec. RTH: 20 Nov AGM carried all (ordinary business only). MEI: Brazil's Cimce meeting on 20 Nov (Brasilia time) had not happened by 10pm NZ; look tomorrow. Nothing new found for VAU (implementation 26 Nov), PPC (Tribunal window to 27 Nov, no binding Ingenia bid found), RWC, CWY, A11, BRI, MYX or MPG (no offer dispatch or target company statement yet).
- No new binding ASX or NZX control deal of A$100m (NZ$20m) or more found. Not added: Metals X's recommended 16.5p cash offer for First Tin (20 Nov; London-listed target); Challenger's rejection of TAL Daiichi's revised non-binding proposal (reported A$12.20); Nuix (Haveli A$2.75) and G8 (A$0.26) remain non-binding. The search was not exhaustive with the announcement lists closed to the desk.
- Deal database unchanged (no deal completed or ended), so base rates and odds were not rerun. src/deal_monitor.py rerun on the 16 Nov closes. US leads watched only (test 9b not passed).
- research/watch_events.csv: HUM's AGM moved to 30 Nov (it opened on 20 Nov and was adjourned to 30 Nov 11am; https://kalkinemedia.com/au/news/announcements/humm-group-reschedules-2026-annual-general-meeting-to-30-november-at-herbert-smith-freehills-kramer-sydney).

Research watch list (reports/watch_triggers.md is still the 16 Nov one; no new hits; SMG reopened on 17 Nov, its only release since is a 20 Nov Appendix 3H cancelling 252,404 performance rights):
- EML (AGM 18 Nov): Q1 underlying EBITDA A$7.1m against the A$8m needed; FY27 guidance A$50m to A$54m affirmed. Not reopened. Source (primary): https://announcements.asx.com.au/asxpdf/20261118/pdf/076qx8b01nljyn.pdf
- MGX (AGM 18 Nov): all resolutions carried; no buyback or capital return. Not reopened.
- WJL (half-year): underlying EBITDA A$7.0m (A$14.4m), statutory loss A$2.7m, A$66.5m net unrestricted cash, 0.3c interim, no guidance; nothing on control. Not reopened. Reported as published 17 Nov; date left at 18 Nov until the ASX date is confirmed.
- HLO (creep date in Webjet): no change of holding notice found; price A$1.395 against about A$1.30. Not reopened.
- AAC (first half, 19 Nov): operating profit A$64.8m, core free cash flow minus A$3.0m, NTA A$3.04; no dividend, buyback, return, sale or review. Not reopened.
- CCV (AGM 19 Nov): only Q1 revenue (A$112.4m, +12.3%) found; the Cashies book, Personal Finance revenue and 1H profit tests unread, and price A$0.27 fails A$0.245. Not reopened; the address to read.
- BRW (AGM 19 Nov): all resolutions passed; nothing on Mangawhai. Stays rejected.
- MFB (1H27, released 18 Nov 7:31pm NZ): NPAT NZ$3.0m, ingredient margin 48.7%, revenue +4.3%, debt repaid, 0.9c interim, no capital return yet; customers not reported. Not reopened: the in-line route also needs a price of 29c or less (32c on 13 Nov); strong route fails. Source: https://www.nzx.com/announcements/483956
- OCA (1H27, released 18 Nov 7:30pm NZ): CFEO plus NZ$0.4m on the new definition (about minus NZ$3.7m on the old one, per today's research/positions/NZ_OCA.md), resale gains NZ$24.3m, NTA NZ$1.63, gearing 29.6%, no interim dividend. Not reopened: the DMF-plus-resale test is unread and the repayment question waits for the 27 Nov election. The research desk's 20 Nov position note covers it. Source: https://www.nzx.com/announcements/483941
- ASG, BOL (AGMs 20 Nov): resolutions carried (BOL extended its buyback, size not found); ASG's H1 profit guidance and BOL's FY27 figure not found. Price fails BOL's A$1.85 trigger; ASG's routes unverified. Not reopened; to read the addresses tomorrow.
- EVZ: no 1H27 guidance yet; GDF: no settlement release yet; HIT (AGM 20 Nov): all six resolutions passed, no Hudson figures. None reopened.
- AWJ: placement completed (18 Nov), SPP offer out (19 Nov), no Ore Reserve. Still fails; not reopened.

Analysed: no card tonight. With no 20 Nov valuation in the ledger, section 3 bars any card. In expected_yearly order GL1 (+226%), A11 (+111%), MEI (+71%), RWC (+44%), BET (+25%), FPR (+1%) lead; all but MEI are ASX cash deals, barred while test 9c has failed, and MEI's card stays "waiting". No research card is "ready" and none is held; no special situation type has passed.

Placed: nothing.

## 2026-11-23, Nightly job started by the desk and failed the same stale rate test a fifth night, so no valuation and nothing placed; two live_deals.csv rows repaired; GL1 implementation now 29 Jan 2027; no watch-list share reopened

Checked:
- All 19 test files in tests/ pass under python3 -I on the repository's data (the rate files still hold 16 Nov's series).
- No scheduled run of the nightly job since run 43 (Sat 21 Nov, 5:58am NZ, stopped at the gate); none created for 23 Nov by 9:46pm NZ. The desk wrote "Desk run 2026-11-23 21:46 NZ: the 8:17pm job had not landed" to config/run_now.txt and pushed it (c427bbf). Actions run 44 started at once; rates, SEC, prices and NZX prices (16 to 20 Nov; 23 Nov not yet published) fetched, then it failed at "Engine checks" at 9:50pm NZ on the same check: tests/test_hedges.py, "NZ monthly average is not used before its month ends" (0.0298 compared with FRED's ('2026-10-15', 0.0313), ('2026-11-15', 0.0325)). Every other check in that file passed, including the ledger chain. Nothing saved: no "Nightly data 2026-11-23" commit, no 23 Nov valuation, data checks, watch report or trial run. The hub snapshot step still posted.
- The desk again did not change the test: it is the job's own safety check, so the fix waits for Cam (the pinned-date fix is in the 17 Nov entry). The practice ledger has now missed 17, 18, 19, 20 and 23 Nov, and every run will stop here until the test is fixed. The failed run can't come good by waiting, so the 45-minute wait was cut short. No orders, nothing entered in the ledger; watching only.
- reports/data_checks.md is still the 16 Nov one: no price flags; GL1's file checked tonight; the other "last checked" findings carry over with no key date passed (VAU pays 26 Nov; AUC and SDF meet 27 Nov).
- Found and fixed a data fault: in config/live_deals.csv the OML and GL1 rows had an unquoted comma in terms_note (written on 20 Nov), so each row had 23 fields and every column after terms_note was shifted by one for those two deals. src/deal_files.py --add crashed on it tonight and truncated the file mid-write; the file was restored from git, the two terms notes re-quoted (text unchanged), and --add then ran cleanly. 20 Nov's deal monitor read those two rows shifted; tonight's rerun reads them correctly. The nightly job hasn't saved since 16 Nov, so nothing else used the broken rows. Worth a guard in deal_files.py (write to a temporary file, then swap) so a bad row can't empty the file.

Changed:
- GL1 (Global Lithium, Titan scheme): the booklet's indicative timetable (ASX release of 18 Nov): booklet to holders 23 Nov, meeting 22 Dec 2026, second court 13 Jan 2027, effective 14 Jan, record 21 Jan, implementation 29 Jan 2027 (was mid-January). Deal file header and Recent announcements updated; --add carried court_date 2027-01-13 and expected_payment 2027-01-15 -> 2027-01-29 into the row. Titan's A$40m Tranche 4 becomes drawable if not complete before 2 Feb 2027, just after the new date. Source: https://announcements.asx.com.au/asxpdf/20261118/pdf/076rt19h37fhr3.pdf (primary, found by search).
- AX1: the 20 Nov AGM figures confirmed (remuneration report 56.30% for, a second strike; spill 40.55% for, failed; directors re-elected with 57% to 60%); the chair repeated Frasers' "best and final" 65c. Bloomberg (20 Nov, headline only) reports Frasers' CFO attacking the Accent board. No change to terms. Sources: https://kalkine.com.au/news/announcements/accent-group-2026-agm-passes-director-re-elections-but-records-second-strike-on-remuneration-report ; https://www.bloomberg.com/news/articles/2026-11-20/frasers-cfo-unleashes-on-accent-as-australian-bid-turns-personal (secondary).
- VAU: State Street ceased to be a substantial holder on 18 Nov (index selling into the scheme); implementation 26 Nov unchanged. Source: https://kalkinemedia.com/au/news/announcements/state-street-bank-and-trust-company-ends-substantial-holding-in-vault-minerals-as-of-18-november-2026 (secondary).
- A11: AGM on 20 Nov carried all four resolutions; scheme meeting 14 Dec as in the row. Source: https://kalkinemedia.com/au/news/announcements/atlantic-lithium-secures-unanimous-approval-for-all-four-agm-resolutions-on-20-november-2026 (secondary).
- MEI: no report yet of what Brazil's Cimce decided at its 20 Nov meeting; Plantao Brasil (18 Nov) says the screening decree is expected before the end of 2026. Row unchanged.
- AUC: no cash election result or scale-back found yet; meeting 27 Nov. src/deal_files.py again reports the file (default all scrip) against the row (all-elect-cash mix); row kept as decided on 1 Nov, to revisit when the election outcome is out.
- Nothing new found for BET (ACCC 3 Dec), OML (record 3 Dec, implementation 10 Dec), SDF (meeting 27 Nov), PPC (Tribunal window to 27 Nov, meeting 7 Dec), RWC (meeting 4 Dec), CWY, FPR, RTH, BRI, MYX or MPG (no offer dispatch or target company statement yet). Several announcement pages again could not be opened, so "nothing found" is a search result, not proof.
- No new binding ASX or NZX control deal of A$100m (NZ$20m) or more found. Below the bar: WA Gold (WAU) agreed a Leeuwin Metals scrip scheme on 23 Nov (about A$26m). Nuix (Haveli A$2.75) remains non-binding.
- Deal database unchanged (no deal completed or ended), so base rates and odds were not rerun. src/deal_monitor.py rerun on the 16 Nov closes. US leads watched only (test 9b not passed).

Research watch list (reports/watch_triggers.md is still the 16 Nov one; no new hits; SMG, ATG and ASG stay reopened as marked):
- HIT (AGM 20 Nov): all six resolutions carried; no trading update or first Hudson result found. Not reopened.
- EVZ (1H27 guidance, about 20 Nov): none found yet. Not reopened; look again.
- GDF (seven property settlements due 20 Nov): no settlement release found. Not reopened; look again.
- BOL and ASG: covered by the 21 Nov research sweep (INDEX note 13); nothing since.
- MVF (Genesis total return swap unwind, about 24 Nov) and MAD (AGM 24 Nov): nothing early found.

Analysed: no card tonight. With no 23 Nov valuation in the ledger, section 3 bars any card. No research card is "ready" and none is held; no special situation type has passed.

Placed: nothing.

## 2026-11-25, Nightly job started by the desk and failed the same stale rate test a seventh night, so no valuation and nothing placed; SDF second court hearing moved to 22 Dec with implementation in January; KMD's Bluestar talks end 2 Dec; IGL guidance kept; no watch-list share reopened

Checked:
- All 19 test files in tests/ pass under python3 -I on the repository's data (the rate files still hold 16 Nov's series).
- No "Nightly data" commit for 25 Nov. The scheduled runs keep starting about 12 hours late: run 48 (created 7:56am NZ 25 Nov) failed at Engine checks and run 49 (8:30am NZ) stopped at the gate. The desk wrote "Desk run 2026-11-25 21:46 NZ: the 8:17pm job had not landed" to config/run_now.txt and pushed it (d7a2402). Actions run 50 started at once (8:46 UTC); rates, SEC, prices and NZX prices fetched, then it failed at "Engine checks" at 9:49pm NZ on the same check as the last six nights: tests/test_hedges.py, "NZ monthly average is not used before its month ends" (0.0298 against FRED's ('2026-10-15', 0.0313), ('2026-11-15', 0.0325)). Every other check passed, including the ledger chain. Nothing saved: no 25 Nov valuation, data checks, watch report or trial run. The hub snapshot step still posted.
- The desk again did not change the test (the job's own safety check; the fix waits for Cam, see the 17 Nov entry). The practice ledger has now missed 17, 18, 19, 20, 23, 24 and 25 Nov. The run can't come good by waiting, so the 45-minute wait was cut short. No orders, nothing entered in the ledger; watching only.
- reports/data_checks.md is still the 16 Nov one: no price flags. Key dates in its "last checked" findings: VAU pays 26 Nov; AUC and SDF meet 27 Nov. SDF's file is updated tonight (below).

Live deals:
- SDF: "Update on Scheme of Arrangement", ASX 24 Nov (https://www.listcorp.com/asx/sdf/steadfast-group/news/update-on-scheme-of-arrangement-3441421.html). Meeting goes ahead 10am 27 Nov. NZ OIO and Texas Department of Insurance approvals in; ACCC, FIRB and MAS still open, FCA progressing. Second court hearing moved from 1 Dec to 22 Dec 2026 because ACCC and FIRB approvals won't come before 1 Dec; implementation now expected in January 2027. The 7.25c fully franked special dividend is now declared, conditional on the scheme becoming effective (no DRP), so the A$5.8725 total stands. Deal file header, conditions, key dates and announcements updated; src/deal_files.py --add carried court date 22 Dec, expected payment 29 Jan 2027 (the desk's reading of "during January", last business day) and the Texas condition into the row; terms_note rewritten by hand. Terms unchanged. The file's 35% chance of a timing slip has now happened; the slip is about five weeks at an unchanged price, which lowers the yearly return.
- AUC: src/deal_files.py again reports the file (default all scrip) against the row (all-elect-cash mix); row kept as decided on 1 Nov, until the election outcome is out. No result found tonight.
- Nothing new found for AX1, VAU (pays 26 Nov), BET (ACCC 3 Dec), OML, PPC, RWC, MEI, CWY, FPR, A11, RTH, GL1, BRI, MYX or MPG. Searches only; several ASX and NZX pages could not be opened, so "nothing found" is a search result, not proof.
- No new binding ASX or NZX control deal of A$100m (NZ$20m) or more found. Deal database unchanged; base rates and odds not rerun. src/deal_monitor.py rerun on the stored 16 Nov closes. US leads watched only (test 9b not passed).

Research watch list (reports/watch_triggers.md is still the 16 Nov one; no new hits; SMG, ATG and ASG stay reopened as marked):
- IGL (AGM 25 Nov): ShareCafe's 25 Nov round-up says IVE kept FY27 guidance at the AGM: underlying NPAT before AASB 16 expected stable, before Motio's contribution; revenue to October up about 4%; capex to fall; payout back to 55% to 65%, about 19c to 22c fully franked (https://www.sharecafe.com.au/2026/11/25/daily-special-ive-group-iperionx-emyria-conneqt-health-terrain-minerals/). The ASX release itself was not read. Guidance intact, so the case stays open, but the red team's entry is about A$2.12 or below and no current price could be read (the last found was A$2.33 on 29 Sep). Not reopened; the desk should check the price against A$2.12 once the nightly job stores closes again.
- KMD (AGM 25 Nov): StockWire X reports a KMD release of 24 Nov 11:21am AEDT, "update on discussions with Bluestar Alliance": Bluestar would go on only with a much longer period in which KMD can't take a better offer, or cover for its costs if the deal fails; the board refused both, and exclusivity ends 5pm NZ time on 2 Dec, not extended; the board will look at other credible interest (https://stockwirex.com/asx-stock-news/consumer-discretionary/kmd-brands-bluestar-alliance-talks-november-2026/). The NZX release was not read (the page could not be opened). This is the "talks end" branch of research/picks/NZ_KMD.md: a value pick only at about NZ$1.54 or below. No current price could be read. Not reopened; watch_events.csv long stop row changed to 2 Dec with this reason. Material for the KMD watch, so Cam is told.
- MAD (AGM 24 Nov): InvestSMART lists the Chair's and CEO's addresses, AGM presentation, results of meeting and a final director's interest notice, all 24 Nov; the PDFs could not be opened tonight, so guidance and whether the final notice shows a sale are unknown. Not reopened; read again tomorrow.
- IPL and SPG: IPL's 1H27 came out on 17 Nov (note 13); no SPG HY27 result found yet. Neither qualifies as a case anyway. Not reopened.
- Tomorrow: AQZ, CZR, DUR, EDU, GDF, MVF, MXI AGMs and SCT annual meeting.

Analysed: no card tonight. With no 25 Nov valuation in the ledger, section 3 bars any card. No research card is "ready" and none is held; no special situation type has passed.

Placed: nothing.

## 2026-11-24, Nightly job started by the desk and failed the same stale rate test a sixth night, so no valuation and nothing placed; no live deal news found; no watch-list share reopened

Checked:
- All 19 test files in tests/ pass under python3 -I on the repository's data (the rate files still hold 16 Nov's series).
- No "Nightly data" commit for 24 Nov. The scheduled 8:17pm NZ run was not created on time: run 45 (the 23 Nov 07:17 UTC schedule) only started at 8:18am NZ on 24 Nov, about 12 hours late, and failed at Engine checks; run 46 (9:16am NZ) stopped at the gate. The desk wrote "Desk run 2026-11-24 21:48 NZ: the 8:17pm job had not landed" to config/run_now.txt and pushed it (170fd63). Actions run 47 started at once (8:46 UTC); rates, SEC, prices and NZX prices (16 to 20 Nov, 12 shares for 23 Nov, 24 Nov not yet published) fetched, then it failed at "Engine checks" at 9:49pm NZ on the same check as the last five nights: tests/test_hedges.py, "NZ monthly average is not used before its month ends" (0.0298 against FRED's ('2026-10-15', 0.0313), ('2026-11-15', 0.0325)). Every other check passed, including the ledger chain. Nothing saved: no 24 Nov valuation, data checks, watch report or trial run. The hub snapshot step still posted.
- The desk again did not change the test (the job's own safety check; the fix waits for Cam, see the 17 Nov entry). The practice ledger has now missed 17, 18, 19, 20, 23 and 24 Nov. The run can't come good by waiting, so the 45-minute wait was cut short. No orders, nothing entered in the ledger; watching only.
- reports/data_checks.md is still the 16 Nov one: no price flags; its "last checked" findings carry over with no key date passed (VAU pays 26 Nov; AUC and SDF meet 27 Nov).

Scan of live deals (news and announcement searches; several ASX, InvestSMART and Market Index pages again could not be opened, so "nothing found" is a search result, not proof):
- Nothing new found since the 23 Nov entry for AX1, VAU, BET, OML, AUC (no cash election result yet), SDF, PPC (Tribunal window to 27 Nov), RWC, MEI (no Cimce decision reported), CWY, FPR, A11, RTH, GL1, BRI, MYX or MPG (no offer dispatch or target company statement; under the Takeovers Code the offer falls due about 30 Nov to 14 Dec). File check dates left as they were.
- No new binding ASX or NZX control deal of A$100m (NZ$20m) or more found.
- No deal file, live deal row or database row changed; base rates and odds not rerun. src/deal_monitor.py rerun on the stored 16 Nov closes. US leads watched only (test 9b not passed).

Research watch list (reports/watch_triggers.md is still the 16 Nov one; no new hits; SMG, ATG and ASG stay reopened as marked):
- MAD (AGM 24 Nov): only a buy-back notice of 23 Nov found (https://www.aspecthuntley.com.au/asxdata/20261123/pdf/03164864.pdf, via InvestSMART); no AGM address, trading update or guidance change found yet, and no block sale. Not reopened; look again tomorrow.
- MVF (Genesis swap unwind, about 24 Nov): nothing found. Not reopened.
- EVZ (1H27 guidance) and GDF (settlements): still nothing found. Not reopened.
- Tomorrow: IGL AGM and trading update, IPL and SPG results, KMD AGM.

Analysed: no card tonight. With no 24 Nov valuation in the ledger, section 3 bars any card. No research card is "ready" and none is held; no special situation type has passed.

Placed: nothing.
