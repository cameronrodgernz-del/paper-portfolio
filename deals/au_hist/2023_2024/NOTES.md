# Australian deal database, 2023 and 2024: notes (built 31 October 2026)

## What is in the files

- `au_deals_2023_2024.csv` holds 37 rows: 19 with a binding announcement in 2023 and 18 in 2024. They cover 35 ASX-listed targets (OreCorp and Pacific Smiles have two rows each, one per bidder or structure). The header matches SCHEMA.md and rows are sorted by announce_date.
- `au_candidates_2023_2024.csv` holds 33 entries: exclusions with reasons, and in-scope deals that I could not build a row for (marked "recheck").
- Every URL in `sources` was opened. Numbers come from ASX filings or mirrors of them, except where `notes` names a secondary source (KWM, the Mayne Report or the mirror's company profile).
- Nothing duplicates the pilot. Every pilot row was announced in 2025 or 2026. The 2024 deals the pilot logged as outside its scope (De Grey, Latin Resources, Auswide, Hotel Property Investments, SG Fleet, Bigtincan) are rows here. Arcadium is excluded, as in the pilot.

## How the deals were found

The run was harder than the brief expected, for three reasons:

1. The Mayne Report tracker no longer has 2023 or 2024 sections. It now runs from its 2025 list onward. Its 2025 entries for 2024-announced deals still link the ASX PDFs, and those links gave me Latin, Auswide, HPI, Bigtincan, SG Fleet and De Grey.
2. The shared web search budget ran out after about 15 searches, early in the run. After that I could only fetch URLs I already had or could predict.
3. The hourly fetch limit was hit once, which cost about ten minutes.

The sources that worked:

- **financialfilings.com.** This mirror shows the full text of ASX filings, including for delisted companies, at predictable addresses (`/companies/<name-ltd or name-limited>/<year>/`). It was the main source of terms and dates. Coverage is patchy: some targets have no filings indexed (Mincor, SILK, Adbri, MMA, Tietto, OreCorp, Namoi). When the bidder is ASX-listed, though, its page carries the target's releases under the target's code prefix. That is how I reached SILK (through Wesfarmers), Musgrave and Breaker (Ramelius), OreCorp (Perseus), Talon (Strike), Essential Metals (Develop), Symbio (Aussie Broadband), Capitol Health (Integral Diagnostics) and Silver Lake (Vault).
- **ASX announcement lists** (asx.com.au v2 statistics pages) for codes still listed: Origin, Healius, and bidders such as Wesfarmers, Ramelius, Perseus, Integral, Aussie Broadband, MyState, Vault and BWP. These give dated titles only, because the linked documents are behind a terms page the fetch tool can't pass.
- **ASX PDFs on announcements.asx.com.au** that turned up in early searches: Origin, CSR, Adbri, Ansarada, Link, InvoCare, Newcrest and Estia.
- **Independent lists.** KWM's "market on a page" PDFs (to Sep 2024 and full-year 2024), HSF's FY23 and FY24 media releases, the Mayne Report's list of failed billion-dollar deals, and the Takeovers Panel annual reports for 2022-23, 2023-24 and 2024-25.

Two pages were blocked because a permission prompt was not answered in time: archive.ph (for an old copy of the Mayne tracker) and altium.com's scheme page. web.archive.org is blocked outright.

## Rules applied where SCHEMA.md leaves a choice (the pilot's conventions)

- **Controllers and foreign-primary targets are left out.** Boral (Seven Group already in control), Arcadium (NYSE primary), the Westgold/Karora deal (Karora is TSX-listed) and Pact are excluded. Pact is pending a check of Kin's starting stake.
- **Volpara is in.** It was NZ-incorporated but listed only on ASX, so it is ASX-primary, even though it used an NZ scheme.
- **Allkem is out.** Its holders took the larger share of Arcadium, so it is treated as the acquirer side, like the pilot's Soul Patts.
- **Same bidder, same row.** Azure stays one row when Hancock joined SQM, because SQM stayed the bidder and Hancock never made a rival proposal. A switch of structure, or a rival bidder, gets its own row (OreCorp: Silvercorp and Perseus; Pacific Smiles: the NDC scheme and the Genesis bid).
- **Takeover outcome dates.** The outcome date for a takeover is the offer close. Where I couldn't read the close date, I used the compulsory acquisition notice date (Breaker, Musgrave, Perseus/OreCorp). The Genesis bid for Pacific Smiles closed at 89.2% with control, so it counts as completed.
- **Prices.** Special or permitted dividends paid out of the price are counted in it (Link, InvoCare, Blackmores, CSR, Estia, SILK, HPI). For scrip deals the final price is kept at the announcement value when terms did not change.
- **Equity value.** Where only a break fee was available, I did not turn the usual 1% fee into an equity value. The inference is stated in `notes` and `equity_value_m` is left blank (Bigtincan, Symbio, Capitol, Talon).
- **Mirror dates.** The financialfilings dates are UTC, so a morning release in Australia can show a day early. I took dates from the document text wherever the text gave them. Dates that rest on a mirror title alone can be a day out.

## Count check against independent totals

- **KWM, calendar 2024.** 51 deals of A$50m or more announced in 2024 for ASX-listed targets (33 successful, 4 withdrawn, 8 current, 6 unsuccessful). My 18 rows for 2024 compare with about 25 that I would expect in scope at A$100m or more. That expectation is the 18 rows plus MMA Offshore and Tietto, which are clearly in scope but have no row, plus Base Resources, the two Namoi Cotton bids and BWP/Newmark, whose values I could not check. Boral and Arcadium are also in KWM's 51 but are excluded by rule.
- **Mayne Report, completions in 2024.** 29 completed $100m+ deals in calendar 2024. My rows include 16 deals completed in 2024 (Adbri's date is unknown but it completed in 2024). Most of the gap is Boral, MMA, Tietto, Base, Namoi and Newmark, plus mid-market deals I did not find.
- **HSF, financial years.** 56 control deals in FY23 and 70 in FY24 (ASX-listed targets, all structures, with a lower value floor and including controllers and foreign-primary targets). My rows announced from July 2023 to June 2024 number 22, about 31% of HSF's FY24 count. The pilot's ratio was about 44% (26 rows against HSF's 59 for FY25). For calendar 2023 no independent total survived: the Mayne tracker's 2023 section is gone.
- **My judgment.** The large deals are close to complete. Every A$1bn+ deal in KWM's 2024 top 10 is a row except Boral (excluded) and MMA (no filing found). Coverage in the A$100m to A$300m band is the weak spot, probably 60 to 75% complete for both years.

## Deals I am unsure about

- **PSC Insurance (AU-2024-18).** The SID release was never found, so `announce_date` is blank. The A$6.19 price and the implementation date come from the mirror's company profile, and the A$2.26bn value from KWM.
- **OreCorp and Silvercorp (AU-2023-19).** Built only from Perseus's releases. Silvercorp's initial takeover terms and its earlier scheme were not read.
- **Healius and ACL (AU-2023-02).** A hostile all-scrip bid blocked by the ACCC. The exchange ratio and value were not found.
- **Talon (AU-2023-11).** The A$100m test rests on inference from the break fee (about A$142m at 1%). The October 2023 amended deed was not read.
- **Bigtincan (AU-2024-17).** The same break-fee inference (about A$183m). The rival IAAC deal has no row.
- **Adbri (AU-2024-06).** No meeting, court or implementation date could be found. Completion is inferred from KWM and the Mayne failed-deals list.
- **Alumina (AU-2024-04).** The announce date is the 26 Feb 2024 date on a meeting slide. The binding deed may date from March 2024. The value at announcement was not read.
- **Auswide and Silver Lake.** All-scrip mergers with no implied price in the filings opened. Auswide's equity value is computed from the booklet's pro forma market capitalisation; Silver Lake's comes from KWM.

## Fields that were thin (blank counts out of 37)

- **Blank by design:** `failure_reason` 33 and `related_deal_ids` 33. `min_acceptance_pct` is blank for 32 rows, as only 7 rows are takeovers.
- **`pre_bid_stake_pct` 33:** usually nil, or not stated in what I read.
- **Expert fields:** `ier_low` and `ier_high` 32, `ier_name` and `ier_verdict` 29. Expert ranges sit deep in booklets that were rarely reachable.
- **Holder fields:** `intentions_pct` 28, `blocking_holders` 25.
- **Other thin fields:** `first_approach_date` 22, `break_fee_m` 21, `regulators` 15, `court_date` and `booklet_date` 12 each, `meeting_date` 10, `undisturbed_price` and `premium_pct_announced` 9 each.

## To finish this set (needs web search)

1. **Add rows** for MMA Offshore (Cyan), Tietto (Zhaojin), Mincor (Wyloo), the Silvercorp scheme for OreCorp, the TLEA scheme for Essential Metals, and the Healius terms.
2. **Settle the A$100m test** for Base Resources, Namoi Cotton (Louis Dreyfus and Olam) and Newmark (BWP).
3. **Check Kin's starting stake in Pact.**
4. **Look at names I never checked:** Boart Longyear (2024), Keypath Education (2024), Silk Logistics (DP World, 2024), Peak Rare Earths (Shenghe, 2024), Prospa (2024), Westoz and Ozgrowth (2023), A-Cap Energy (Lotus, 2023), Carbon Revolution (de-SPAC, 2023) and Irongate (late 2022 or 2023).
5. **For the pilot owner:** Pacific Smiles had a second Beam Dental bid in October 2025 that is not in the pilot. It would be excluded anyway, as a buy-out by a holder already at about 89%.
