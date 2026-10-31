# NZ deal database: notes

Built 31 October 2026. Files in this folder:

- `nz_deals.csv`: 46 qualifying control transactions for NZX-listed targets, binding announcement between 1 Jan 2015 and 31 Oct 2026, equity value at the offer of NZ$20m or more. Header exactly as in `../SCHEMA.md`, sorted by announce_date.
- `nz_candidates.csv`: 87 deals and register entries looked at and left out, with the reason.

## How the deals were found

1. **Takeovers Panel transactions register.** The register page itself is rendered by script and shows no list, but the HTML sitemap (`/html-sitemap/`) lists every register entry by company and year (about 250 entries back to 2001). Entries added since late 2025 (Rakon 2026, Bremworth, Accordant, Goodman NZ) only appear in the XML sitemap (`/sitemap.xml/sitemap/SilverStripe-CMS-Model-SiteTree/2`). Each register page gives the transaction type (takeover full or partial, scheme, company meeting for an allotment, acquisition or buyback), parties, price, key dates, adviser and links to the published documents. Page slugs are not consistent (Trade Me sits at `restaurant-brands-new-zealand-limited-2`, Tilt 2021 at `tilt-renewables-limited-3`), so several pages were found by web search rather than by guessing the address.
2. **Gaps in the register.** The Panel says it is still backfilling. Diligent (a Delaware company, outside the Code) and both Tower schemes (Fairfax and Vero, 2017) are not on it and were found through law-firm deal reviews (Chapman Tripp 2018 and 2019 reports) and then sourced from filings.
3. **2025 and 2026.** Found by searching NZX announcement titles ("Receipt of Takeover Notice", "Scheme Implementation Agreement") through the NZX and BusinessDesk mirrors of NZX announcements.
4. **Panel annual reports** give only counts of Code transactions by year (for example 4 takeovers and 2 to 4 schemes in 2015/16; 7 takeovers and 4 schemes in 2016/17), not names, and the counts include unlisted Code companies, so they were used only as a rough check.

## Year-by-year check against the register

Every register entry dated 2015 to 2026 was classified. Qualifying rows by year: 2015: 5; 2016: 5; 2017: 9; 2018: 6; 2019: 3; 2020: 2; 2021: 2; 2022: 1; 2023: 1; 2024: 2; 2025: 7; 2026: 3. Register entries for each year that are takeovers or schemes of NZX companies are all in the database except: Finzsoft 2020 and Vital 2025 (below NZ$20m), King Country Energy and Blue Sky Meats (Unlisted/USX platforms, not NZX), CIP Holdings (unlisted). The rest of each year's entries are company meetings (allotments, buybacks, stake approvals) or unlisted Code companies; they are in the candidates file. About 40 small or unlisted register entries were excluded on the register title and what is known of the company without opening the page; they are marked "excluded without full check" in the candidates file. None of them is a known takeover of an NZX company over NZ$20m, but they were not each verified.

The 2019 to 2024 years are thin (11 deals in six years). That matches the register, which has few NZX takeovers or schemes in those years. The brief's expectation of 50 to 100 deals was not met: I found 46 at the NZ$20m threshold.

## Which sources had which data

- **Target company statements and scheme booklets** (on the Panel site where the parties consented): undisturbed price and premium, shares on issue, conditions, break fees, board recommendation, independent adviser range, pre-bid stake, lock-ups and voting intentions, meeting dates. These were the main source.
- **Register pages**: final prices, price variations, key dates including meeting, final orders, implementation, close and delisting, and outcomes. Best source for outcome and timing.
- **NZX announcements**: announcement dates, premiums, equity values, implementation notices and later events (vote results, rival proposals). NZX page timestamps are in UTC, so an 8:30am NZ release shows as the previous day; register dates were preferred where they differ.
- **Other**: SEC filings (Diligent), Fairfax, Suncorp, EQT, Centuria and Bapcor releases, Commerce Commission media releases (Tower/Vero decline), LINZ OIO decision (Scott/JBS). Two rows lean on secondary material for numbers, flagged in their notes: MHM (Forsyth Barr note summarising the NZX release) and the Vero price for Tower (interest.co.nz report).

## Conventions

- **announce_date**: date of the takeover notice or the SIA announcement. Where a lock-up or pre-bid agreement came first, that is noted. First public non-binding approach goes in first_approach_date only where the announcement date was confirmed.
- **outcome_date**: schemes: implementation date (or final court orders where implementation was not found, noted). Takeovers: offer close date; for partial offers that went unconditional after closing, the unconditional date. Failed deals: date of lapse or termination.
- **Prices**: cash-equivalent per share. Permitted dividends that form part of the price are included (Opus, Abano 2016). Scrip deals use the basis stated in the documents (Kathmandu, Augusta, Manawa). Delay or dividend mechanics that changed the paid price are not counted as a price rise (Z Energy, Arvida, Manawa).
- **equity_value_m**: 100% of shares at the initial price, from the documents where stated, otherwise shares on issue x price (marked "own calculation").
- **rival_bid = Y** includes publicly announced non-binding competing proposals (Trade Me, Tilt 2021, Smartpay), not only binding rival offers. Binding rivals have their own rows (Tower, NZOG).
- **completed** for a takeover means the offer went unconditional and settled. In two cases the bidder stayed below full ownership: Tilt 2018 (Infratil and Mercury at about 85%) and Millennium & Copthorne 2025 (CDL at 83.9%). Count them as failures if the question is "did the bidder get 100%".
- Re-bids by the same bidder after a deal broke are separate linked rows (Abano 2019 and 2020). Metlifecare is one row because the same deal continued through litigation to a lower price.

## Deals I am least sure of

- **Tegel 2018 (NZ-2018-01)**: target statement not opened; announce date is the lock-up date, equity value, premium and recommendation blank.
- **Bremworth/Floorscape 2025 (NZ-2025-07)**: price was an estimated range (cash plus a capital return), shown as midpoints; outcome recorded as lapsed with reason "vote", though no meeting was held.
- **Scott Technology 2015 (NZ-2015-04)**: a control scheme combining an offer, rights issue and placement; announce date is the date discussions were announced, and implementation date not found.
- **2 Cheap Cars 2026 (NZ-2026-02)**: target statement not opened; equity value estimated from the 2023 share count.
- **Tower/Vero 2017 (NZ-2017-03)**: price from a news report; equity value, board recommendation and pre-bid stake not confirmed in a filing.

Also note: Nuplex implementation date not found (outcome_date and days blank); Trilogy outcome_date is the scheduled final court date.

## Fields most often blank (where the field applies)

- financing_condition (14 of 23 takeovers) and due_diligence_condition (11 of 23 takeovers): offer documents were often not opened.
- premium_pct_announced: 12 of 23 takeovers. Target statements often give the undisturbed price but no premium; implied premiums are in notes, not in the field.
- break_fee_m: 11 of 23 schemes.
- pre_bid_stake_pct: 10 of 23 schemes.
- first_approach_date: filled for only 9 rows. Approach dates were rarely confirmed to the day.
- equity_value_m: blank for 9 rows (Tower/Vero, Tegel, Tilt 2018, Methven, Z Energy, Pushpay, Comvita, both Bremworth rows).
- IER range: blank for 12 rows, mostly where the Panel did not publish the booklet (Z Energy, Pushpay, Abano 2020, MHM, Airwork).

## Not done

- Tickers for Finzsoft, Horizon Energy and Pulse Energy are not confirmed.
- Shares on issue was not looked up separately where documents did not state it.
- No AU deals; dual-listed targets (Nuplex, Tower, Trade Me, Z, Tilt, Pushpay, Smartpay and others) sit here, so remove them from the AU half to avoid double counting.
