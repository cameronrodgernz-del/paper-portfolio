# Second check of the Australian deal pilot (31 October 2026)

## What I checked

- All 50 rows in `au/au_deals_2025_2026.csv`. For 49 rows I re-opened the binding announcement (SID, SIA, bid implementation or intention-to-bid release, or the bidder's statement) and compared the core fields: ticker, bidder, structure, consideration, dates, undisturbed price, offer price, premium, equity value, regulators, fees, outcome and rival or price-rise flags. For most completed deals I also opened the booklet, the meeting result, the court or effective-date release or the implementation release to fill blanks.
- Cygnus Metals (AU-2026-12) is the exception: its SID PDF needs a login on the mirrors, so only the InvestorPA summary and CAML's deal page could be read.
- The 13 pending deals: the ASX announcement list for each code (titles and dates to 31 October 2026), the latest timetable filings, Ingenia's releases on the Warburg Pincus and AVID proposals, and the first ten pages of the ACCC acquisitions register (new regime).
- `days_to_outcome` recomputed for every resolved row. All 37 matched the dates.

Outputs in this folder: `au_deals_2025_2026_verified.csv` (same header, row order and IDs), `au_deals_2025_2026_verification_log.csv` (152 lines: 8 corrected, 115 filled, 29 flagged) and this note. Each changed row's `notes` field now ends with a "[Second check 31 Oct 2026]" passage, and the URLs I opened were added to `sources`.

## How many rows changed

- 49 of 50 rows changed in some way (notes or sources at minimum). 20 rows had at least one blank field filled, and 7 rows had a field corrected.
- Field corrections (8): booklet_date 2, blocking_holders 2, pre_bid_stake_pct 1, equity_value_m 1, undisturbed_price 1, ier_name 1 (completing "BDO" to the full name).
- Blanks filled in data fields (45): booklet_date 13, ier_name 6, ier_verdict 6, ier_low and ier_high 3 each, court_date 3, break_fee_m 3, intentions_pct 2, pre_bid_stake_pct 1, meeting_date 1, implementation_date 1, and on the CAML/New World row the undisturbed price, basis and premium.
- Blank counts for the fields the pilot found thinnest, before and after: IER range 36 to 33, pre-bid stake 36 to 35, booklet date 27 to 15, court date 23 to 20, voting intentions 22 to 20, break fee 16 to 13.

The substantive corrections:

- AU-2025-14 Kinterra / New World: pre-bid stake was 11.99%, taken from Kinterra's 16-17 June notice. The Takeovers Panel release TP25/052 shows a 23 June notice at 19.16%, filed before the 26 June bidder's statement. The CAML row's blocking holder entry is corrected to match. This is the same kind of error as the substantial holder notice caught earlier: the right holder, but the wrong (superseded) notice.
- AU-2026-02 DUI / AUI: the Ian Potter Foundation held 16.79%, not 13.07%. The 13.07% is the parcel under AUI's call option. AUI's own relevant interest was 19.90% (6.83% held directly). The break fee (A$11.66m), the expert (Kroll) and the Foundation's voting intention are now filled.
- AU-2026-17 oOh!media: the booklet date was the court convening date (28 September). The booklet was registered on 29 September.
- AU-2026-20 Peet: the booklet date of 12 October was wrong. Only a draft was lodged with ASIC (on 9 October), so the field is now blank. The note said Warburg Pincus's proposal for Ingenia was conditional on terminating the Peet SID. Ingenia's filings say instead that it asked for a board confirmation that the Warburg proposal beats the Peet deal.
- AU-2025-11 CAML / New World: the original 21 May SID release has now been opened. It gives a A$0.028 undisturbed close, a 78.6% premium, a stated A$185m equity value (the row had a computed A$185.9m), a A$1.85m break fee and directors' 2.56% intention. It also shows an A$0.055 step in the price path (23 June) that the row had missed.
- AU-2026-01 ASM: the undisturbed close is A$0.7254 per the SID (the row had A$0.725).

## Errors seen more than once

1. The booklet date was set to the court convening date or a lodgement date rather than the date the booklet bears (oOh!media and Peet corrected; Johns Lyng and Insignia flagged, since both releases say the booklet would follow ASIC registration).
2. Stakes and holdings were taken from the wrong filing or the wrong parcel (Kinterra's superseded notice, the Ian Potter Foundation's option parcel instead of its full holding).
3. Call-option relevant interests were treated unevenly. Red Hawk, Lynch and Apiam record the option stake as the pre-bid stake, but Envirosuite (Ideagen options over 14.95% to 18%, the filings disagree) and DUI did not. DUI is now filled on the option basis. Envirosuite is flagged for a decision.
4. Notes on pending deals had gone stale. Carnaby still said ACCC clearance was needed, but Evolution waived that condition in the booklet. Peet misdescribed the Warburg condition.
5. Computed figures were used where the filing states one (New World equity value).

## Pending deals: where they stand at 31 October 2026

| Deal | Status |
|---|---|
| AU-2026-11 European Lithium / CRML | Court approved 26 Oct, effective 27 Oct, final ratio 0.045, implementation 5 Nov 2026. Nothing outstanding. |
| AU-2026-15 Carnaby / Evolution | Approved 26 Oct. Second court 29 Oct and implementation 10 Nov scheduled; no court result found. ACCC condition waived. Evolution bought QIC's 13.7% after the SID. |
| AU-2026-14 Vault / Genesis | Booklet registered 6 Oct. Meeting 11 Nov, court 16 Nov, implementation 26 Nov. ACCC waiver received 27 Aug. |
| AU-2026-17 oOh!media / I Squared | ACCC determination by 24 Sep, OIO satisfied 23 Oct, FIRB status unknown. Meeting was set for 2 Nov, but a timetable update and SIA amendment were lodged on 30 Oct and could not be opened. |
| AU-2026-18 Ausgold / OceanaGold | Booklet 21 Oct. Meeting 27 Nov, court 1 Dec, implementation 11 Dec. ACCC waiver determination published 17 Sep. FIRB and TSX status not found. |
| AU-2026-19 Steadfast / KKR-Dragoneer | Booklet 23 Oct. Meeting 27 Nov, court 1 Dec, implementation 22 Dec. FIRB, ACCC, FCA, MAS and Texas all outstanding. |
| AU-2026-20 Peet / Ingenia | Draft booklet only. ACCC notified 9 Oct (Phase 1). Ingenia is weighing Warburg Pincus at A$5.45 against AVID, which holds a matching right to 1 Nov. Ingenia can walk from Peet for a superior proposal and pay the A$10m reverse fee. |
| AU-2026-16 BetMakers / Tabcorp | ACCC notified 15 Oct (Phase 1). Meeting targeted Dec 2026. |
| AU-2026-21 Reliance Worldwide / Brookfield | Go-shop ended mid-October with no rival announced. ACCC waiver determination published 19 Oct. Booklet Nov, implementation Q1 2027. |
| AU-2026-13 Accent / Frasers | Offer closes 29 Jan 2027. A$0.65 declared best and final on 28 Oct. The board still says reject. Flagged on scope: Frasers reportedly aims for at least 26%, not control. |
| AU-2026-22 Meteoric, AU-2026-23 Cleanaway, AU-2026-24 FleetPartners | No change since signing. All regulatory approvals outstanding. Meetings early 2027. |

## Scope

- Kept as is, with flags: Accent (a full on-market bid, but the bidder's stated aim is a blocking stake). Cue Energy stays excluded but unresolved at the announcement price.
- Possible missing deal: Global Uranium and Enrichment (a scheme booklet registered with ASIC appeared in a search result; not checked).
- No other row breaks the binding, size or control rules on what I read.

## Base rates

No outcome, outcome date, rival flag or price-rise flag changed. The rates stay as they were:

- Completion rate: 31 of 37 resolved deals (83.8%).
- Median days: 119 for all resolved deals, 124 for completed deals.
- Rival bids: 7 rows.
- Price rises: 9 rows.

## Rows I couldn't fully verify

- AU-2026-12 Cygnus: no filing opened. The board recommendation, expert and regulatory conditions are unconfirmed.
- AU-2025-17 Reef Casino: the initial 14 July price is still missing. The bidder's statement also suggests the bid implementation agreement terms were announced on 28 August, so the binding date needs the 14 July release.
- IER ranges still missing where the booklet text was cut off or not found: Red Hawk, Spartan, Gold Road, Johns Lyng, Lynch, RPMGlobal, Vault/Genesis, Carnaby, European Lithium (verdict flagged from legal press), Brickworks and others.
- AU-2025-03 Mayne: the outcome date of 9 December is Cosette's disputed notice. Mayne's own termination was 11 December.
- Other flags: the Red Hawk expert's name (the two filings differ), the Magnetic intentions basis, and Brickworks' equity value (a share count exists only in an ASA summary).

## Limits of this pass

- The shared web search budget ran out after about half the rows. After that I could only open URLs already in hand, so the missing-deal sweep was not repeated.
- The ASX research API route was refused by the permission system and not retried.
- InvestSmart's Accent announcement page timed out on the permission prompt.
- ASX `displayAnnouncement` links return a terms page, so recent PDFs could only be read where a direct `asxpdf` or mirror link existed.
