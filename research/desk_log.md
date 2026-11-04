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
