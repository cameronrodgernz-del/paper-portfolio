# Follow-up pass: outcomes work list (started 1 Nov 2026, 00:35 NZDT)

## Method
- Read FOLLOWUP_BRIEF.md, SCHEMA.md, AU_HISTORY_BRIEF.md and the NOTES.md for each year folder before fetching.
- WebSearch not used at all (budget assumed spent). Everything below is WebFetch on addresses built by hand.
- Main source: financialfilings.com. Company year pages (`/companies/<slug>/<year>/`) list dated titles; filing pages (`/filings/<slug>/<category>/<year>/<id>/`) give the full ASX text. Slugs vary: some use `-limited`, some `-ltd` (Japara, Gold Road), some have no filings indexed at all. The site's own search page is disallowed by robots, so slugs were guessed.
- Mirror title dates are UTC, so an Australian morning release can show a day early. Where the document text gave a date it was used; timetable dates taken from titles alone say so in the patch note.
- Each patch row reads the old value straight from the CSV named in the work list (checked identical to the copy under /home/claude/paper_portfolio/deals/au_hist).
- Conventions kept from the year files: outcome_date for a completed scheme is the implementation date; for a takeover it is the offer close; special dividends paid out of the headline price are inside the offer price.

## Progress log
- Priority 1 (18 rows with no outcome), first sweep 00:36 to 01:00:
  - Resolved from filings on financialfilings.com: rhipe, Japara, Youfoodz, Huon, iCar Asia, Senex, PayGroup, ELMO (all completed schemes, with implementation releases), Apollo Tourism (completed, via Tourism Holdings' own releases), DGO Gold (completed takeover, via Gold Road's completion release), E&P (first 360 proposal withdrawn 11 Dec 2020 and replaced by a re-bid, built as new row AU-2020-F01, which lapsed at 20.22% on 31 Mar 2021).
  - rhipe and Japara: the row's announce_date was the non-binding proposal date. Corrected to the SID release date and the old date moved to first_approach_date.
  - Senex: the SIA is dated 11 Dec 2021 and was released 12-13 Dec 2021, so the row stays in 2021 (resolves the doubt in the 2021-22 NOTES).
  - Irongate: price terms from the SIA release (on Charter Hall's page). Holders approved on 29 Jun 2022 and implementation was scheduled for 15 Jul 2022 (360 Capital release), but no implementation release was found, so outcome stays blank.
  - MACA: no MACA or Thiess filings indexed. NRW's own releases give Thiess's opening A$1.025 offer, NRW's rival non-binding proposal (11-18 Aug 2022, withdrawn 30 Aug 2022) and that Thiess raised its offer. rival_bid corrected N to Y, price_raised Y. Outcome not confirmed.
  - Not indexed or slug not found on financialfilings: 1300 Smiles (tried 1300-smiles-limited, -ltd), Intega (page exists, 0 filings), ResApp (resapp-health-limited, -ltd, resapp-health), PTB Group (0 filings), MSL Solutions (0 filings). Bidders are unlisted, so no bidder page either. Corrs 2023 appendix has no status column; G+T's 2022 market-activity page does not name these deals.
- Priority 2 (undisturbed and initial prices), newest first, from 01:00:
  - 2024 rows: the mirror holds only results-call transcripts for PSC, SG Fleet, Nearmap-type late targets (no ASX text), and Alumina's 2024 page has only the H2 2023 call. Bigtincan's and SG Fleet's ASX PDFs already in the row do not state an undisturbed price. Alumina's H2 2023 presentation shows the 26 Feb 2024 announcement was non-binding (first_approach_date patched; binding SID date not found, so announce_date is a known error left for a later pass).
  - 2022 rows done from listed bidders' pages: OZ Minerals (BHP page; final price corrected to A$28.25), Warrego x3 (Strike page, incl. Warrego's target's statement), Norwest (MinRes page; offer close corrected to 29 Apr 2023), Genesis/St Barbara and Dacian (Genesis page), Pendal (Perpetual page, incl. completion 23 Jan 2023), MyDeal (Woolworths page), Vimy (Deep Yellow page; implementation corrected to 4 Aug 2022).
  - Not reachable: Nitro (only transcripts), Nearmap (transcripts), Tassal (0 filings), Uniti, Crown, Virtus (slugs not found), Alliance (Qantas page lacks the AQZ releases).
- 2021 and earlier rows (01:10 to 01:35): listed bidders' pages carry the target releases back to at least 2018-2019 (IGO 2019, Wesfarmers 2019, Integral 2018, Nine 2018, Ramelius 2020, Iress 2020, TerraCom 2020). Done: Bardoc, Over the Wire, Apollo Consolidated (Ramelius and Gold Road rows), Aventus, Class, Gascoyne, Empired, Templeton (NTA-based value only), APN Property, Mortgage Choice, Primewest, Vocus, Redflex, Saracen (break fee only), Spectrum, OneVue, Universal Coal, Panoramic, Kidman, MOD, Xenith, Echo, Pioneer Credit, CML/COG, Integral/Capitol (IER and last value only).
  - Targets delisted in 2020 or earlier are not indexed on financialfilings (Village Roadshow page exists with 0 filings; DWS, Cardinal, Galaxy, Crown, Link, Mainstream, Sydney Airport slugs fail), so 2015-2020 rows with unlisted bidders could not be reached.
  - Westoz and Ozgrowth: WAM's merger release sets scrip by an NTA formula and states no per-share value or premium, so nothing to fill.
  - Oil Search, Afterpay, Saracen, Fairfax: releases give the exchange ratio but no implied A$ value or premium, so prices stay blank.
- Last stretch (01:35 to 01:57): Alliance (Alliance's own page, still listed), ALE (Charter Hall Long WALE REIT page), McPherson's (own page), AOF/Starwood (AOF's own page: lapse date 20 Mar 2020), 3P Learning (own page, still listed), Talon (amended SID did not change terms), Afterpay (Block's 8-K on its ASX page: closed 1 Feb 2022 in Australia), Primewest and Apollo Consolidated offer closes, Dacian offer close (20 Feb 2023), Asciano/Qube bid (Qube page). Irongate marked completed from Charter Hall's FY22 annual report ("successful in privatising the listed Irongate REIT"); ResApp marked completed from G+T's 2022 timing review (listed among schemes that took over 120 days to implement); neither has an outcome date.

## Totals (from patches.csv: 529 rows across 59 deals, checked by script against the CSVs named in the work list; 0 old_value mismatches, 0 duplicate deal/field pairs)
- Fields filled (blank before), 483: offer_price_initial 42, premium_pct_announced 40, undisturbed_basis 36, undisturbed_price 36, board_recommendation 34, offer_price_final 34, consideration_type 31, break_fee_m 28, price_raised 25, days_to_outcome 19, outcome_date 19, financing_condition 16, implementation_date 14, due_diligence_condition 13, intentions_pct 13, outcome 13, court_date 11, pre_bid_stake_pct 10, ier_name 9, meeting_date 9, regulators 9, min_acceptance_pct 7, first_approach_date 6, booklet_date 3, equity_value_m 1, failure_reason 1, ier_high 1, ier_low 1, ier_verdict 1, related_deal_ids 1.
- Fields corrected (non-blank before), 46: equity_value_m 20, days_to_outcome 5, outcome_date 5, notes 4, announce_date 3, bidder_type 3, implementation_date 2, offer_price_final 1, rival_bid 1, undisturbed_basis 1, undisturbed_price 1. Equity values: a filing figure replaces a law-firm list figure. Notes: appended, never cut.
- Against the work list's `missing` items: outcome 13 of 18, outcome_date 19 of 53, undisturbed_price 36 of 149, offer_price_initial 42 of 112, offer_price_final 34 of 105, consideration_type 31 of 48, equity_value_m 1 of 26 (176 of 511 in all).
- New rows: 1 (AU-2020-F01, E&P re-bid by 360 Capital, 2020, lapsed).

## Contradictions with existing rows (all patched, with the filing in the patch row)
- rhipe (AU-2021-16) and Japara (AU-2021-10): announce_date was the non-binding proposal date; SID dates are 6 Jul 2021 and 27 Jul 2021.
- Hancock/Warrego (AU-2022-23): Hancock's offer was announced 30 Nov 2022, not 1 Dec.
- OZ Minerals (AU-2022-27): final price A$28.25 (A$1.75 special dividend plus A$26.50), not the Mayne Report's A$28.50.
- Norwest (AU-2022-25): bid closed 29 Apr 2023; 12 May 2023 was only the release date. Strike/Warrego (AU-2022-26): Strike's bid closed 13 Feb 2023, not 15 Feb.
- Vimy (AU-2022-04) implemented 4 Aug 2022, not 5 Aug; Redflex (AU-2021-01) implemented 18 Jun 2021, not 17 Jun.
- Spectrum (AU-2020-03): offer closed 29 May 2020; the row used the 18 Mar 2020 unconditional date.
- MACA (AU-2022-13): NRW made a rival non-binding proposal during the Thiess bid and Thiess raised its price, so rival_bid N is wrong (now Y) and price_raised is Y.
- E&P (AU-2020-20): the 27 Oct 2020 proposal was withdrawn on 11 Dec 2020 when its pre-condition failed; G+T's A$162m matches the A$0.69 re-bid (new row), not the A$0.61 first offer (A$143.1m computed).
- Alumina (AU-2024-04): 26 Feb 2024 was a non-binding proposal with exclusivity. The binding SID came later (date not found), so announce_date is wrong but was left for a later pass; first_approach_date was filled.
- Qube/Asciano (AU-2016-02): the bid release measured its premium against a A$6.65 close, not the A$6.58 VWAP in the row.
- bidder_type changed to existing_holder for iCar Asia (Carsome 19.9%), Echo (Northern Star 21.7%) and Universal Coal (TerraCom 19.995%), to match each file's own convention.
- Equity values differ from the law-firm lists in about 20 rows, by up to 12% (Class A$386m vs Corrs A$346.3m; Apollo Consolidated A$163.3m at the first offer vs A$181.3m at the improved one; Gascoyne A$104.8m vs A$124.3m).
- Senex (AU-2021-37): the SIA is dated 11 Dec 2021, so the row correctly stays in 2021.
- Templeton (AU-2021-15): size now confirmed above A$100m (198.1m shares at about A$1.70 NTA).

## Not resolved, and why
- 1300 Smiles, Intega, PTB Group, MSL Solutions: no filings indexed on financialfilings (Intega, PTB and MSL pages exist with 0 filings; 1300 Smiles slug not found) and the bidders are unlisted. The mirror's company profiles state Intega and iCar outcomes, but profile text is not a filing, so it was not used for Intega.
- MACA: outcome and final price not found (no MACA or Thiess filings; NRW's releases stop at 30 Aug 2022).
- Irongate and ResApp: completed, but implementation dates not found.
- Price fields left blank where the filing states only an exchange ratio or premium: Oil Search, Afterpay, Saracen, Fairfax, Westoz, Ozgrowth, Apollo Tourism, Genesis/St Barbara, Strike/Warrego, Vimy and Panoramic undisturbed, MOD and Xenith undisturbed.
- Unreachable: 2020-or-earlier delisted targets (Village Roadshow page has 0 filings; DWS, Citadel, Wameja, Cardinal, Galaxy fail), Nitro, Nearmap, Spark, Sydney Airport, SG Fleet, PSC, Alumina 2024 (transcripts only), Tassal (0 filings), Uniti, Crown, Virtus, Link, Mainstream, Bingo, Boral, Seven Group, AP Eagers, AusNet (slugs fail), Milton's merger release (absent from its own page).
- Blocked: https://gtlaw.com.au/knowledge/transaction-timing-public-ma-2021 (permission prompt not answered; not retried).
- Possible missing row for another pass: Xenith IP's binding merger scheme with QANTM (announced about 27 Nov 2018), superseded by IPH in Apr 2019 (seen in IPH's 2019 releases). It belongs in the 2017-18 file.
- WebSearch was never used.

## Left for a later pass
- Alumina (AU-2024-04): find the binding SID date (Alcoa's or Alumina's March 2024 release) and move announce_date.
- Irongate and ResApp implementation dates; MACA's final Thiess price, close and outcome; 1300 Smiles, Intega, PTB and MSL outcomes (need a source other than financialfilings, such as KWM's or HSF's deal lists with status, or ASX PDFs found by search).
- Undisturbed prices for rows where the filing gives only a premium (most 2015-2019 rows): the scheme booklets usually state the price.
- Xenith/QANTM 2018 scheme as a possible new row in the 2017-18 file.

Stopped at about 02:00 NZDT (about 85 minutes of work). The reachable sources were largely used up, so more time would not have added much.
