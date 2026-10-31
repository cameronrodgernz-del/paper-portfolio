# Australian deal database, 2017 to 2018: notes (built 31 October 2026)

## Status: partial

This build is incomplete. It holds 28 sourced rows, but about 27 more deals that look in scope were identified and not built. They are listed in the candidates file and start with "Identified but NOT BUILT". Partway through the run, the shared web search budget (200 searches) ran out. After that only pages already seen could be opened. InvestSmart, the mirror used for delisted targets' announcement lists, then rate-limited, and finally the hourly web-fetch limit was used up. The missing deals include several large ones: Sirtex (two bidders), Investa Office Fund (Blackstone, then Oxford), TPG Telecom/VHA, MYOB, Mantra, APN Outdoor, Greencross, Pepper and Scottish Pacific. A follow-up pass should build these first.

## What is in the files

- `au_deals_2017_2018.csv`: 28 rows covering 23 ASX-listed targets, 13 announced in 2017 and 15 in 2018. Each has a binding announcement between 1 Jan 2017 and 31 Dec 2018 and target equity value at the offer of A$100m or more (Seymour Whyte is just over the line at HSF's A$113m). The rows are sorted by announce_date and the header matches SCHEMA.md.
- `au_candidates_2017_2018.csv`: 54 entries. These are exclusions with reasons (outside the years, existing controller, below threshold, non-binding, NZX-listed, not a scheme or bid) plus the identified-but-not-built deals.
- Every URL in `sources` was opened while the row was built. Values taken from law-firm reviews rather than filings are labelled HSF or MinterEllison in `notes`.

## How the deals were found

1. Candidate spine. The Mayne Report tracker named in the brief could not be used for these years: the live page is about 86,000 characters and now holds only 2024 to 2026 (WebFetch reports nothing past that), and the archived copy is blocked. The spine was instead the deal lists printed in the appendices of Herbert Smith Freehills' Australian Public M&A Reports for FY17 (59 deals, July 2016 to June 2017) and FY18 (56 deals, July 2017 to June 2018). These cover every control deal for an ASX-listed Australian target, of any size, by takeover or scheme. The FY19 report (July 2018 to June 2019), which would have covered the second half of 2018, could not be opened (the PDF link failed and the alternative link was refused). For that half-year the spine was MinterEllison's FY19 "Directions in M&A" review (45 deals of A$50m or more, 28 of them announced July to December 2018), which names most of the larger deals, plus deals found through the announcement lists of listed acquirers.
2. Cross-checks. MinterEllison's FY18 Deals Trilogy (37 deals of A$50m or more) was used to check FY18 and to pick up price changes and outcomes. Takeovers Panel reasons and media releases were used for Macmahon, Spotless and Asia Pacific Data Centre.
3. Deal detail. ASX announcement PDFs were read through three routes: (a) announcements.asx.com.au links found by search early on; (b) the ASX announcement list page (asx.com.au/asx/v2/statistics/announcements.do), which works only for codes still in use, so it was used for targets still listed (Macmahon, Integral, AMA, APA, Stanmore) and for listed acquirers whose lists carry the target's releases (Cleanaway, Mineral Resources, NEXTDC, SRG Global, Nine, McMillan Shakespeare, Charter Hall, Bega); and (c) InvestSmart's delisted-company announcement pages, which link to Aspect Huntley mirror copies of the ASX PDFs (aspecthuntley.com.au/asxdata/YYYYMMDD/pdf/<ASX id>.pdf). Other primary sources were Federal Court judgments (Seymour Whyte), ATO class rulings (Programmed), PERSOL's Tokyo Stock Exchange disclosures, Downer's NZX releases and Oracle's press release.
4. Values. Where a filing states equity value it is used. Otherwise the value is computed from price and stated share count ("computed" in notes), or taken from the HSF deal list (noted as HSF), which gives each deal's value in A$.

## Rules applied where SCHEMA.md leaves a choice (same as the pilot unless stated)

- Primary listing and NZ targets. Trilogy International and Trade Me are NZX-listed and left for the NZ database.
- Existing controllers. Brookfield Prime Property Fund (Brookfield about 80%) and Warrnambool Cheese and Butter (Saputo about 88%) were left out as minority buy-outs.
- Rival bidders get their own rows, linked through `related_deal_ids`: AWE (Mineral Resources scheme, CERCG bid, Mitsui bid), Atlas Iron (Mineral Resources scheme, Hancock bid) and Asia Pacific Data Centre (360 Capital and NEXTDC bids in 2017, NEXTDC's second bid in 2018).
- `bidder_type`. A bidder that already held a strategic stake of 20% or more when it bid is `existing_holder` (CIMIC 20.5% of Macmahon, NorthWest 22.7% of Generation Healthcare, NEXTDC 29.2% of APDC in 2018); bidders with less are classed by what they are.
- Mergers of equals by scheme (SRG/GCS, Fairfax/Nine) are recorded with the company being acquired under the scheme as the target. Afterpay/Touchcorp (two schemes into a new holding company) was not built; see candidates.
- Outcomes follow the pilot: a takeover that gave the bidder control is completed and its `outcome_date` is the offer close; one that closed without control is `lapsed` even if it had gone unconditional (Macmahon, NEXTDC 2017, Stanmore). A deal that lost to a rival is `superseded_by_rival`.
- `rival_bid` is Y when a competing public proposal from another bidder was live at the same time. `price_raised` is Y only for an increase by the same bidder.
- Announcement dates that are inferred are flagged: DUET's first approach, Aconex (Oracle's US-dated release), Seymour Whyte and Capilano (agreement dates), and Eclipx's first approach (SG Fleet).

## Count check

- HSF FY17 (July 2016 to June 2017) lists 59 control deals of any size. Of the A$100m-plus deals, only six were announced in January to June 2017: DUET, Macmahon, Spotless, Generation Healthcare, Seymour Whyte, and the Afterpay/Touchcorp merger (not built). The other A$100m-plus FY17 deals were announced in 2016 and are logged as outside these years.
- HSF FY18 (July 2017 to June 2018) lists 56 deals, about 35 of them at A$100m or more. This build has 18 of those 35. Pepper, Mantra, Sirtex (two bidders), Investa (Blackstone), APN Outdoor, Avanco, Billabong, Sino Gas, Realm, Tawana, Mitula, Finders, Watpac, LifeHealthcare, Tian An and Royal Wolf are not built (the last two may turn out to be exclusions).
- MinterEllison FY19 counts 28 deals of A$50m or more announced July to December 2018. This build has eight rows from that half-year (Fairfax, APA, Capilano, Folkestone, NEXTDC/APDC, Eclipx, Stanmore and SRG's later steps aside). MYOB, TPG Telecom, Greencross, Scottish Pacific, Gateway, Propertylink, Investa (Oxford), Ruralco, Villa World and Zenitas are named there and not built.
- Putting these together, the true population for 2017-18 looks like about 25 to 30 deals a year. That matches the pilot's estimate for 2025-26. The built rows cover roughly half of it, with good coverage of contested deals and listed acquirers and weak coverage of private equity buyouts of delisted targets.

## Deals I am unsure about

- Atlas Iron / Hancock (AU-2018-08): the outcome "completed" was not confirmed from a filing, and the close date and final stake are blank.
- AWE / CERCG (AU-2018-01): the opening price is uncertain (A$0.73 per AWE's release, about A$0.70 implied by HSF), and the date the bid ended was not found.
- Asia Pacific Data Centre / 360 Capital (AU-2017-07): it is completed because 360 held 67.3% by October 2018, but the offer close date and pre-bid stake were not found.
- Mineral Deposits / ERAMET (AU-2018-06): the opening price (about A$1.46) and the initial board stance come from MinterEllison, not a filing.
- Viralytics (AU-2018-03): the price and terms are blank. Only the dates come from ASX release titles; the value is HSF's.
- Capilano: completion rests on the scheduled 5 Dec 2018 implementation date plus MinterEllison listing it as successful.

## Fields most often blank (out of 28 rows)

- By design: `failure_reason` 18, `related_deal_ids` 19, `min_acceptance_pct` (schemes).
- Expert: `ier_low`/`ier_high` 26, `ier_verdict` 23, `ier_name` 20.
- Other gaps: `intentions_pct` 25, `pre_bid_stake_pct` 23, `break_fee_m` 22, `first_approach_date` 19, `court_date` and `due_diligence_condition` about 18, `financing_condition` 17, `booklet_date` 16, `undisturbed_price` 14.
- Equity value is blank for Fairfax and Eclipx (share counts not in the releases read).

## What a follow-up pass needs

Start with the not-built list in the candidates file. For delisted targets with reused codes (Sirtex SRX, Pepper PEP, Mantra MTR, Sino Gas GAS, Programmed PRG), neither the ASX list page nor InvestSmart works, so the filings have to be found by search. Aspect Huntley links (aspecthuntley.com.au/asxdata/YYYYMMDD/pdf/<ASX idsId>.pdf) open reliably once the idsId is known. The HSF FY19 report appendix would give a complete list for July to December 2018 if it can be opened.
