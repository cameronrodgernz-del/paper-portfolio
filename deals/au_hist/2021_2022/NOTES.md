# Australian deal database, 2021 and 2022: notes (built 31 October 2026)

## What is in the files

- `au_deals_2021_2022.csv` holds 69 rows covering 62 ASX-listed targets, with binding announcements between 1 January 2021 and 31 December 2022 and equity value at the offer of A$100m or more. There are 42 rows (39 targets) for 2021 and 27 rows (23 targets) for 2022. The header matches SCHEMA.md and the pilot exactly.
- `au_candidates_2021_2022.csv` holds 66 entries that were considered and left out, each with a reason and the source opened.
- Every URL in `sources` was opened while the row was built.

## Read this first: the rows are much thinner than the pilot

The database is complete as a list of deals for these two years, but not as a set of fields. Three limits hit during the build:

1. **Web search ran out early.** The 200-search budget is shared by all five agents in this run. It was used up after about 25 of my searches, before most deals had been looked up. After that, only URLs already seen in the conversation could be opened.
2. **New websites needed approval that never came.** Company and bidder websites that hadn't been opened before (for example santos.com, Wikipedia and the Federal Court index) were blocked pending a permission prompt that wasn't answered. Wesfarmers and IGO pages opened before the block started, so those two deals have full primary data.
3. **ASX PDFs couldn't be opened from the ASX listing pages.** The ASX announcement list (asx.com.au/asx/v2/statistics/announcements.do) still worked for any company that is listed today. It gives the date, time and title of every filing, but its PDF links open a terms page instead of the PDF. An hourly fetch limit was also hit once.

Rows therefore come in three grades:

- **Full rows (filings opened):** Redflex, the three Mainstream rows, Australian Pharmaceutical Industries (Wesfarmers), Western Areas (IGO) and AusNet. These have prices, premiums, break fees, intentions and timetables from the SID announcement, booklet, court judgment or implementation release.
- **Title rows (about 30):** a still-listed bidder or target let me read the ASX record of filing titles and dates. These rows have reliable dates (SID, booklet, meeting, court approval, implementation, offer close, termination). Prices and terms are often missing because the PDFs couldn't be opened.
- **Thin rows (about 30):** the target is delisted and the bidder isn't ASX-listed, so no filing could be read. These rest on the Corrs M&A Outlook deal appendices (date, value and structure, with a status column for deals announced before 30 Sep 2021), the G+T reviews, the Mayne Report's list of companies that left the ASX (some prices and completion months), and a few trade-press pieces. Each thin row says so in `notes` ("Built from secondary deal lists only").

A second pass should go back to the SID announcement and implementation release for every thin row. The pilot's routes (search for the asxpdf link, then open it) will work once search is available again.

## How the deals were found

1. **Mayne Report tracker.** The page now covers only 2024 to 2026 (about 86,000 characters with nothing before 2024). Its "companies that disappeared from the ASX" list (maynereport.com/articles/2023/07/04-1222-9708.html) was used for completions and some prices of A$1bn+ deals.
2. **Corrs M&A Outlook deal appendices (the main spine).** Corrs publishes every Australian takeover and scheme over A$25m in its survey year (1 October to 30 September) with date, bidder, value and structure. Three editions were read: 2022 (Oct 2020 to Sep 2021, 52 deals), 2023 (Oct 2021 to Sep 2022, 56 deals) and 2024 (Oct 2022 to Sep 2023, 56 deals, of which rows 1 to 49 could be read). Corrs is not complete: it misses Oil Search, Templeton Global Growth Fund and the Warrego contest, for example. Its dates are sometimes the first non-binding approach rather than the SID (Vocus, Spark, OZ Minerals), and I corrected these where an ASX record or press report showed the binding date.
3. **G+T Takeovers and Schemes Reviews (2021 and 2022)**, including the 2021 half-year update and the timing, structure and technology chapters. These were used for counts, values, contest outcomes (Virtus, Nitro, Warrego, Apollo) and named non-binding approaches.
4. **ASX announcement records** of still-listed bidders and targets: WES, IGO, STO, RMS, SBM, HUB, DXS, CNI, CLW, CHC, HDN, SOL, REA, WAM, WGB, ABB, WGX, MCP, DYL, QAN, WOW, GMD, PPT, BHP, MIN, STX, BPT, ZIP, APA, THL and PXA. These gave dated titles, and for cross-tagged filings, the target's own releases too.
5. **delisted.com.au** yearly archives are now behind a paywall (A$15), so they couldn't be used. The **Takeovers Panel** media-release page shows only 2026 and its year filter couldn't be driven by URL, so Panel matters come only from titles in ASX records (AusNet 01, Gascoyne, PAF).

## Rules applied (same as the pilot unless stated)

- NZX-primary targets were left out: Tilt Renewables, Z Energy and Pushpay. Existing-controller buy-outs were left out: CIMIC (HOCHTIEF about 78.6%) and Devine. Deals with binding dates in 2020 were left out: Asaleo Care (10 Dec 2020 per Corrs, though G+T counts it in 2021), Think Childcare, Coca-Cola Amatil, Saracen and others. Deals that became binding in 2023 were also left out: Origin, InvoCare and Slater & Gordon.
- Rivals each get their own row, linked by `related_deal_ids`: Mainstream (Vistra, SS&C, Apex), Apollo (Ramelius, Gold Road), Virtus (CapVest, BGH), Nitro (Potentia, Alludo) and Warrego (Beach, Hancock, Strike). Westoz and Ozgrowth were parallel WAM mergers, not rivals, so they aren't linked.
- `bidder_type` is `existing_holder` where the bidder held a notable stake before the bid (Wesfarmers 19.3% of API, Strike 19.9% of Warrego, Seven Group in Boral, Qantas in Alliance, MinRes in Norwest, BGH in Virtus, Potentia in Nitro, Gold Road in Apollo), following the pilot.
- `shareholder_vote`/`court_approval` are Y/Y for every scheme and N/N for every takeover, because the law requires that.
- **Takeover outcome dates** use the offer close where it was found (Norwest 12 May 2023). Where the close wasn't found (Ramelius/Apollo, Centuria/Primewest, Genesis/Dacian, Boral, Hancock/Warrego), `outcome_date` is blank and the control and compulsory-acquisition dates are in `notes`. Where a scheme's implementation date wasn't in the titles, the effective date was used and the note says so (MyDeal).
- **Unknown outcomes are left blank** rather than marked pending. This applies to 17 rows: Japara, rhipe, Youfoodz, Huon, 1300 Smiles, Intega, iCar Asia, Apollo Tourism, Senex, Irongate, ResApp, DGO Gold, PayGroup, MACA, PTB, Elmo and MSL. All are believed completed, but none could be confirmed from a source I opened.
- **`rival_bid` N on a thin row** means no rival appeared in the sources read, which is weaker evidence than on a filing-based row. For 2022 it is backed by G+T's statement that there were only three competitive bidding situations (Warrego, Virtus, Nitro).
- **Equity values** come from the filing for API, Western Areas, AusNet and Redflex. Elsewhere they are the Corrs deal value (labelled in `notes`). Corrs sometimes records the value at the final price (Western Areas: A$1,244.8m at A$3.87 against the SID's A$1,096m at A$3.36).

## Count check against independent totals

| Measure | 2021 | 2022 |
|---|---|---|
| G+T binding deals of A$50m or more | 62 | 41 |
| G+T deals of A$500m or more | 21 | 14 |
| Targets in this file (A$100m or more) | 39 | 23 |
| Same, after adding back logged A$50-100m deals, NZX-primary, controller buy-outs and other exclusions | about 55 | about 35 |

HSF counts 65 control transactions in FY22 (July 2021 to June 2022) and 59 to 60 a year on its five-year average. Corrs counts 52 deals over A$25m from Oct 2020 to Sep 2021 and 56 from Oct 2021 to Sep 2022.

After the add-backs, the file is about 7 short of G+T's 2021 count and about 6 short of its 2022 count. The A$1bn+ band reconciles exactly: 16 deals in 2021 (including Tilt and Z Energy) and 9 in 2022 (including CIMIC and Pushpay). The A$500m+ band reconciles in 2022 only if Senex's binding SID fell in 2022 (see below). So the missing deals are probably in the A$50m to A$500m band. Names I couldn't place or confirm: Webster (PSP), 3P Learning (IXL), Prime Media (Seven West), Smartgroup, 5G Networks/Webcentral (logged but not resolved), and whatever sits in Corrs 2024 rows 50 to 56 (alphabetically T to Z, Oct to Dec 2022), which couldn't be read.

## Deals I'm unsure of

- **Senex (AU-2021-37).** Corrs dates it 13 Dec 2021. Press in late 2021 describes POSCO's proposals as non-binding, and G+T's 2022 size-band counts fit better if the SID was signed in 2022. The row may need to move to 2022.
- **Spark (AU-2021-18).** The 15 Jul 2021 `announce_date` is the first (non-binding) approach. The SID date wasn't found. The year is right.
- **Templeton Global Growth Fund (AU-2021-15).** No size source was found. It is included provisionally because its net assets are believed to exceed A$100m.
- **Virtus (AU-2022-02 and -06).** The outcome rests only on G+T ("a $711 million bid by BGH Capital trumped a bid by CapVest").
- **Hancock/Warrego (AU-2022-23).** `announce_date` is the first mention of Hancock's offer in Beach's ASX record (1 Dec 2022). No value was captured for any Warrego row.
- **OZ Minerals.** The A$28.50 price is the Mayne Report's figure and may include a dividend. The SID price wasn't seen.
- **Huon.** Corrs shows a JBS scheme (6 Aug 2021) and a JBS bid (13 Aug 2021). They are kept as one row.
- **Excluded:** Sezzle (a Delaware merger, not a scheme) and Carbon Revolution (a SPAC re-domiciliation). Both are logged and could be added back.

## Fields that are thin (blanks out of 69 rows)

- Close to empty: IER fields (67 blank), pre-bid stake (67), undisturbed price and premium (66), break fee (66), intentions and blocking holders (65 to 66), financing and due diligence conditions (65 to 67), regulators (60), board recommendation (58).
- Weak: offer price initial (57) and final (53), consideration type (47), meeting date (52), court date (53), booklet date (49), implementation date (49).
- Outcome date and days to outcome are blank on 41 rows. Outcome is blank on 17.
- Good: announce date (69), equity value (65), structure (69), bidder (69), outcome where known (52).

## Base rates from this file (treat as provisional)

- **Completion:** 40 of the 52 rows with a known outcome completed (77%). Counting targets instead of rows, 40 of the 45 targets with a known outcome were acquired.
- **Days to outcome:** median 118 across the 28 rows with both dates, and 120 for the 20 completed deals. This undercounts takeovers and the large schemes, whose dates were mostly not captured. For comparison, G+T reports average schemes of 115 days (2021) and 130 days (2022) from announcement to implementation, and average takeovers of 94 days (2021) and 97 days (2022).
- **Rival bids:** 15 rows are flagged Y.
- **Price rises:** 10 rows are flagged Y. This is an undercount, because initial prices are mostly missing.
