# Australian deal database, 2019 and 2020: notes (built 31 October 2026)

## What is in the files

- `au_deals_2019_2020.csv` holds 49 rows covering 45 ASX-listed targets, with binding announcements in calendar 2019 (29 rows) and 2020 (20 rows) and target equity value at the offer of A$100m or more. Header and conventions follow SCHEMA.md and the 2025-26 pilot.
- `au_candidates_2019_2020.csv` holds 40 entries: deals considered and left out (with the reason), plus a handful of unresolved cases that may belong in this file or a neighbouring one.
- Every URL in `sources` was opened while the row was built.

## Read this first: what limited this build

This build had much thinner access to primary documents than the pilot, and the gaps are visible in the data.

1. The shared web search budget for the run ran out early, after the first round of searches, so ASX announcement PDFs could no longer be found by search. Only a handful of PDFs (Healthscope, Webster, Navitas, Pioneer Credit and Casa Systems' SEC filing for NetComm) were found before that point.
2. The ASX announcement list (asx.com.au v2) works for codes that are still listed and gives dated titles, but its links open ASX's terms page, not the PDF. It could not be used to open any filing.
3. InvestSmart's announcement lists work for delisted codes and give dated titles of every filing. They were the main source for timetables (SID, booklet, meeting, court, implementation, termination). They rate-limit hard, and deeper pages often failed, so a few SID dates could not be read. Several codes have since been reused by other companies (VRL, CRD, DRM, IFN, CCL), which buries the old history.
4. A web fetch limit per hour was hit once, which cost about ten minutes.

As a result, most rows have exact dates and outcomes from dated filing titles, but many lack the per-share price, premium, break fee and expert's range. Where a number comes from a law firm deal list rather than a filing, the row says so, marked (HSF), (Corrs) or (G+T). No figure was taken from news.

## How the deals were found

- Mayne Report tracker: not usable for these years. The page converts to about 86,000 characters and stops in July 2025, so the 2019 and 2020 sections could not be reached with offsets, and the archive copy was blocked.
- delisted.com.au: the 2019 and 2020 yearly lists need a paid login.
- Spine used instead:
  - HSF Australian Public M&A Report deal lists for FY19 (July 2018 to June 2019) and FY20 (July 2019 to June 2020). These list every deal with target, bidder, bidder region, value, structure and consideration type, but no dates. FY19 has 34 deals of A$100m or more and FY20 has 30. The FY21 list could not be found.
  - Corrs M&A Outlook 2021 appendix: 37 deals announced 1 Oct 2019 to 30 Sep 2020, with announcement dates, values and status at 1 Nov 2020.
  - G+T Takeovers and Schemes Reviews (2020 edition covering 2019; 2021 edition covering 2020): counts and named deals, plus chapters on consideration, deal protection, success factors and timing.
  - Takeovers Panel media releases (2019 and 2020 index pages) and the Panel's annual reports for 2018-19, 2019-20 and 2020-21 (complete lists of applications).
- Each candidate was then dated from filing titles (InvestSmart or the ASX list of the acquirer or target), which also settled which FY19 deals were really 2018 announcements.

## Rules applied where SCHEMA.md leaves a choice

- Same inclusion rules as the pilot. NZX-primary targets (Metlifecare, Abano, Orion Health), the TSX-primary Alacer Gold, controller buy-outs (WPP AUNZ, Macquarie Media) and an LIC restructure (Ellerston Global) are logged as exclusions.
- Targets incorporated outside Australia but listed only on ASX are kept: Highlands Pacific (PNG) and Universal Coal (UK). Credible Labs (Delaware, ASX only) would also qualify but could not be verified.
- announce_date is the date of the ASX release announcing the binding agreement or bid. Highlands Pacific's deed was released on 2 Jan 2019 after a suspension from 28 Dec 2018, so it sits in 2019.
- Two rows have a known year but no exact binding date: Nzuri Copper and Villa World. Their announce_date and days_to_outcome are blank and they are numbered last among 2019 deals. The notes explain the window.
- Rival bids get their own rows only when the rival reached a binding bid or agreement: Infigen (UAC and Iberdrola), Cardinal (Shandong and Nordgold), CML (COG and Scottish Pacific), AOF (CHAB and, later, Starwood). Non-binding rivals (OPTrust/ICG for Pacific Energy, SS&C for GBST, Aware Super for OptiComm, BYJU'S and Blake for 3P Learning, Dongshan and Engineers & Planners for Cardinal) are noted in the row and logged in candidates.
- rival_bid and price_raised follow the pilot. price_raised is left blank where terms may have changed but a rise was not confirmed: Echo, Nzuri, Infigen (both bidders), Universal Coal, 3P Learning, Wameja and E&P. Village is Y because G+T says BGH had to sweeten its terms.
- Takeover outcome dates: the offer close where known (AP Eagers/AHG, Universal Coal); otherwise the date the bidder declared the bid unconditional with control (Spectrum) or acquired control (Echo), as stated in each row. Stanmore's date is derived from HSF's 46-day figure and Cardinal/Shandong's from G+T's 214-day figure.
- Special dividends: several schemes paid a special or permitted dividend around implementation (Pacific Energy, GBST, ERM, Gazal, Citadel, Zenith, Saracen). Because the scheme documents were not read, whether each sits inside the headline price is noted as unconfirmed.

## COVID-period break and repricing cases

These are the most useful rows for the portfolio's break-case base rates:

- Pioneer Credit / Carlyle (AU-2019-26): SIA 5 Dec 2019. By April 2020 Carlyle alleged defaults, including a material adverse change, and demanded repayment of its debt facility; Pioneer refuted them and terminated the scheme (between 14 and 22 Apr 2020; exact date not confirmed). Standstill 18 May 2020, refinanced Sep 2020.
- CML Group / Scottish Pacific (AU-2020-05): SIA 2 Mar 2020 after beating COG's earlier scheme (AU-2019-25). Scottish Pacific raised a possible material adverse effect as COVID hit; terminated by mutual agreement with A$1m paid towards CML's costs (G+T). COG's 17.36% blocking stake was already a problem.
- LNG Limited / LNG-9 (AU-2020-04): recommended bid 28 Feb 2020; bridge financier refused to fund and LNG-9 withdrew on 14 Apr 2020 alleging a material adverse effect; administrators appointed 1 May 2020.
- AOF / Starwood (AU-2020-01): bid announced 29 Jan 2020 lapsed after a defeating condition was triggered by AOF's debt refinancing in the early COVID period (G+T). Two months earlier the CHAB scheme (AU-2019-19) failed its vote after CHAB sold its 19.9% stake.
- Village Roadshow / BGH (AU-2020-14): pre-COVID non-binding proposals at A$3.90 (PEP) and A$4.00 (BGH). After cinemas and theme parks closed, the binding scheme of 6 Aug 2020 was A$2.20 cash (or A$2.10 plus stub equity) with contingent uplifts tied to reopening, up to about A$2.45. BGH later sweetened the terms to win support; the final amount was not confirmed.
- Zenith Energy / PEP (AU-2020-06): signed 6 Mar 2020, just before the crash; price raised to A$1.05 in July 2020 when early proxies suggested a failed vote; completed 21 Aug 2020.
- National Veterinary Care (AU-2019-27): court approval on 25 Mar 2020, the same day as its COVID trading update; completed without repricing.
- Stanmore Coal / Golden (AU-2020-07): unconditional on-market bid launched 2 Apr 2020 into the sell-off, by a 31% holder.
- Related NZ cases (logged in candidates for the NZ file): Metlifecare / EQT and Abano / BGH, both terminated on MAC grounds and revived at lower prices.

## Count check against independent totals

- HSF FY20 (Jul 2019 to Jun 2020), 30 deals of A$100m or more: 27 are rows here. The other three are Macquarie Media (controller buy-out), the OPTrust/ICG rival for Pacific Energy (never binding) and ARA's proportional bid for Cromwell (unresolved, see below). This file has two FY20-window rows HSF does not: Universal Coal (UK-incorporated, which HSF's Australian-target list omits) and CML/COG (Corrs A$103.5m; HSF puts it below A$100m). Rows in that window: 29.
- HSF FY19 (Jul 2018 to Jun 2019), 34 deals of A$100m or more: 11 were binding from 1 Jan 2019 and are rows here (AHG, DuluxGroup, Gazal, Healthscope, Kidman, MOD, Navitas, NetComm, Nzuri, Spicers, Xenith/IPH); two are unresolved (Doray, Xenith/QANTM); the other 21 were 2018 announcements. Highlands Pacific (PNG) is an extra row HSF omits.
- Corrs (Oct 2019 to Sep 2020), 26 deals of A$100m or more: 24 are rows here (Ellerston is excluded as a restructure and Cromwell is unresolved), and Universal Coal is an extra row Corrs omits, giving 25 rows in that window.
- G+T counts 41 deals of A$50m or more announced in 2019 and 42 in 2020. Those counts include A$50m to A$100m deals, NZX targets, controller buy-outs, foreign-primary targets and non-binding proposals, so 29 and 20 rows at A$100m+ are consistent. G+T's 2020 total includes 14 deals in Q4 2020; only Saracen and E&P are rows here for Q4, and the 2020 count is the weakest part of this file (see below).

## Deals I am unsure about

- Villa World (AU-2019-29) and Nzuri Copper (AU-2019-28): binding dates not captured (windows given in notes).
- CML/COG (AU-2019-25): borderline on size; Corrs A$103.5m, HSF below A$100m.
- Highlands Pacific (AU-2019-01): deed may have been signed in late December 2018; equity value not from a filing (a press list says about A$206m).
- E&P Financial (AU-2020-20): outcome not captured; value from G+T only.
- ERM Power (AU-2019-12): the binding date is taken from a release titled "proposal"; no separate SID release appears before the booklet.
- Cardinal / Shandong (AU-2020-12): opening price unclear (Panel says A$0.70; HSF's A$300m implies about A$0.60); final price A$1.05 is the last confirmed.
- Likely missing or unresolved, logged in candidates: Coca-Cola Amatil / CCEP (SID may have been signed in late 2020), ARA's proportional bid for Cromwell (in only if full acceptance could take ARA over 50%), Credible Labs / Fox (2019, about A$585m), Doray / Silver Lake and Xenith / QANTM (either could be January 2019). If CCA and Cromwell qualify, 2020 rises to 22 rows.
- 2020 Q4 coverage: without a FY21 HSF list or search, other October to December 2020 deals of A$100m or more may be missing.

## Fields that are thin (blank counts out of 49 rows)

- Not captured for any or almost any row because scheme booklets and SID releases could not be opened: ier_low and ier_high 49, financing_condition 49, intentions_pct 49, due_diligence_condition 48, ier_verdict 48, undisturbed_price 47, premium_pct_announced 46, break_fee_m 46, ier_name 46, blocking_holders 46.
- offer_price_initial and offer_price_final 38 each. Prices from filings or Panel records: Healthscope, NetComm, Navitas, Pacific Energy, AOF/CHAB, Webster, OneVue (initial, from the release title) and Cardinal (both bidders). Prices from law firm reviews only: Stanmore (HSF), Zenith final (HSF), Citadel (G+T) and Village base price (G+T).
- first_approach_date 44, board_recommendation 44, pre_bid_stake_pct 44, regulators 30.
- Timetable fields are much fuller: court_date blank 20, meeting_date 17, implementation_date 17, booklet_date 15, outcome_date 8. equity_value_m is blank only twice, but most values are from the HSF or Corrs lists rather than filings.
- A second pass with search access, aimed at each row's SID release and booklet, would fill most of the price, premium, break fee and expert fields. The verification brief's process is the right tool for that.

## Sources that would help a second pass

- ASX announcement PDFs found by search (announcements.asx.com.au/asxpdf/...) remain the best primary source.
- InvestSmart lists (investsmart.com.au/security/asx/CODE/slug/announcements?page=N) give the full dated timeline for delisted codes; one request at a time, and an upper-case code in the URL sometimes gets past a failed lower-case request.
- HSF report PDFs are reachable on the herbertsmithfreehills.com domain (not hsfkramer.com).
