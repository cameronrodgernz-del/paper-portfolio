# ACCC reviews of ASX deals, 2015 to 2025

Data file: `data/regulators/accc_deals.csv`, one row for each of the 271 ASX deals in the deal database with an announce date from 2015 to 2025 (`deals/all_deals.csv` plus `deals/au/au_deals_2025_2026.csv`, one row per deal_id). Built 1 Nov 2026. No share prices were looked at.

## How it was built

- Each deal was looked up on accc.gov.au by target and bidder name (web search limited to the ACCC site), and every matching matter page was opened and read: the informal merger reviews register (2002 to 2025), the merger authorisations register, and the new acquisitions register.
- The ACCC statements of issues list was used as a cross-check. Three of its pages were read: they cover every statement of issues from September 2018 to October 2025.
- Deal outcomes and conditions in the deal database were used to spot reviews that never appeared on the public register.
- A bulk crawl from GitHub Actions was tried first. The ACCC site refused it (an Akamai "Access Denied" 403 on the first request), so the crawl was stopped and the workflow removed. Everything was then read page by page with the web fetch tool.

## Column meanings

- `accc_reviewed`: Y means the ACCC looked at the deal, either on a public register or, from the deal database, in a confidential review that left no public record. N means it was searched for and no review was found. `unknown` means it could not be settled (see below).
- `soi_dates`: statements of issues, plus their equivalents on the authorisation route: the AP Eagers market feedback letter, and the Origin transparency letters.
- `delay_events`: only events where a decision date was moved later, a timeline was suspended, a statutory deadline was extended, or the ACCC asked for more information. Decision dates that were brought forward are noted in `match_note`, not here.
- `route`: informal review, authorisation, or other.

## Headline counts

- Deals checked: 271. Searched one by one: 236. Not searched: 35 (see "Gaps").
- ACCC reviewed (Y): 41.
  - 31 have a public record: 27 informal reviews (one of which, Tatts, went on to the Australian Competition Tribunal), 2 ACCC merger authorisations, 1 notification under the new regime, and 1 deal known only from an ACCC media release (M2).
  - 10 were confidential reviews known only from the deal database.
- Not reviewed (N): 191.
- Unknown: 39 (35 not searched, plus 4 where the deal had an ACCC condition but no record was found).
- Deals with a statement of issues or equivalent: 14 (12 formal statements of issues and 2 on the authorisation route).
- Deals with at least one delay event: 20. In 18 of them a date moved or a timeline was suspended; in the other 2 the ACCC only asked for more information (Intecq, AP Eagers).
- The deal database flagged 41 deals with ACCC. This file adds 4 public reviews the database had missed:
  - Brookfield for Asciano (AU-2015-08)
  - the Qube consortium for Asciano (AU-2016-02)
  - Sydney Airport (AU-2021-34)
  - Dye & Durham for Link (AU-2021-40)

## Outcomes, the 31 deals with a public record

| Outcome | Count | Deals |
|---|---|---|
| Not opposed | 14 | iiNet, M2, Asciano consortium, Intecq, Pulse Health, Mantra, Tox Free, Fairfax, Xenith (QANTM), Xenith (IPH), API, Sydney Airport, MyDeal, Seven West Media |
| Not opposed subject to undertakings | 7 | Novion, Recall, APA (CK), Ruralco, Apollo Tourism, Link (Dye & Durham), Capitol Health |
| Opposed | 3 | TPG Telecom (VHA merger), Alliance Aviation (Qantas), Healius (ACL) |
| Withdrawn | 1 | oOh!media (APN Outdoor) |
| No decision, review discontinued | 2 | Asciano (Brookfield), Asciano (Qube consortium); both were overtaken by the joint bid |
| Authorised by the Tribunal | 1 | Tatts. The informal review ended with no decision after its statement of issues; the Tribunal authorised the deal in Jun 2017, the Federal Court set that aside, and the Tribunal authorised again on 22 Nov 2017. |
| Authorised with conditions (ACCC) | 2 | Automotive Holdings Group (AP Eagers), Origin (Brookfield and MidOcean) |
| Approved, new regime | 1 | RPMGlobal (Caterpillar), phase 1 |

The 10 confidential reviews:

- Investa Office Fund: cleared 19 Jan 2016.
- OneVue: ACCC position released 7 Sep 2020.
- Reef Casino Trust: no objection given before the bid.
- Webster, Blackmores, SILK Laser, Alumina, Insignia, Infomedia and Apiam: each had an ACCC condition and completed, but no public decision was found.

## Every deal with a statement of issues (or equivalent)

| Deal | Target | Bidder | Announced | Review began | Statement of issues | Outcome |
|---|---|---|---|---|---|---|
| AU-2015-03 | iiNet (IIN) | TPG Telecom | 2015-03-13 | 2015-04-02 | 2015-06-11 | Not opposed, 2015-08-20 |
| AU-2015-08 | Asciano (AIO) | Brookfield consortium | 2015-08-18 | 2015-08-06 | 2015-10-15 | No decision, 2016-03-30 |
| AU-2015-06 | Recall (REC) | Iron Mountain | 2015-06-08 | 2015-08-25 | 2015-11-05 | Not opposed with undertakings, 2016-03-31 |
| AU-2016-04 | Asciano (AIO) | Brookfield, Qube and others | 2016-03-15 | 2016-03-30 | 2016-05-26 | Not opposed, 2016-07-21 |
| AU-2016-15 | Tatts (TTS) | Tabcorp | 2016-10-19 | 2016-11-25 | 2017-03-09 | Tribunal authorised, 2017-11-22 |
| AU-2016-18 | oOh!media (OML) | APN Outdoor | 2016-12-14 | 2016-12-16 | 2017-05-04 | Withdrawn, 2017-05-19 |
| AU-2018-F07 | TPG Telecom (TPM) | Vodafone Hutchison Australia | 2018-08-30 | 2018-09-24 | 2018-12-13 | Opposed, 2019-05-08 |
| AU-2019-F01 | Ruralco (RHL) | Nutrien (Landmark) | 2019-02-27 | 2019-03-22 | 2019-06-13 | Not opposed with undertakings, 2019-08-22 |
| AU-2019-07 | AHG (AHG) | AP Eagers | 2019-04-05 | 2019-04-29 (authorisation) | 2019-06-24 (market feedback letter) | Authorised with conditions, 2019-07-25 |
| AU-2021-36 | Apollo Tourism (ATL) | THL | 2021-12-10 | 2022-01-28 | 2022-04-28 | Not opposed with undertakings, 2022-09-29 |
| AU-2021-40 | Link (LNK) | Dye & Durham | 2021-12-22 | 2022-03-01 | 2022-06-16 | Not opposed with undertakings, 2022-09-08 |
| AU-2022-09 | Alliance Aviation (AQZ) | Qantas | 2022-05-05 | 2022-05-17 | 2022-08-18 | Opposed, 2023-04-20 |
| AU-2023-02 | Healius (HLS) | Australian Clinical Labs | 2023-03-20 | 2023-04-12 | 2023-07-20 | Opposed, 2023-12-15 |
| AU-2023-03 | Origin (ORG) | Brookfield and MidOcean | 2023-03-27 | 2023-06-05 (authorisation) | 2023-07-19 and 2023-08-29 (transparency letters) | Authorised with conditions, 2023-10-10 |

Notes on the table:

- For Origin, the 19 Jul 2023 transparency letter was read: it sets out the lines of inquiry into competition concerns. The 29 Aug 2023 letter was not read.
- The Qube consortium's separate Asciano review (AU-2016-02) may also have had a statement of issues. Its register page was not found.

## Matters that could not be matched or read fully

- **Qube consortium for Asciano (AU-2016-02):** register page not found. Its dates come from two ACCC media releases (5 Feb and 23 Feb 2016); the start date is missing.
- **Vocus for M2 (AU-2015-11):** only the "not opposed" media release (5 Nov 2015) was found, so there is no start date and no timeline.
- **Pulse Health (AU-2016-16):** the register page lists its timeline without dates. The outcome date (23 Mar 2017) comes from the deal database.
- **No record found, although the deal had an ACCC condition:**
  - G8 for Affinity (AU-2015-07)
  - McMillan Shakespeare for Eclipx (AU-2018-14)
  - CRH for Adbri (AU-2024-06)
  - betr for PointsBet (AU-2025-13)
- **Brookfield for AusNet (AU-2021-32):** there is no matter for Brookfield's bid. The ACCC did open a review of APA's rival proposal (commenced 28 Oct 2021, discontinued with no decision on 20 Dec 2021). APA's proposal is not a row in the deal database.

## Gaps

- **35 deals were not searched** because the session's shared web search limit ran out. They are marked `unknown`:
  - AU-2017-F03, AU-2017-F05, AU-2018-F04, AU-2018-F05, AU-2019-F02
  - AU-2020-04, AU-2020-12, AU-2020-13
  - AU-2021-25, AU-2021-27, AU-2021-31, AU-2021-39, AU-2022-05
  - AU-2024-03, AU-2024-07, AU-2024-F01, AU-2024-11, AU-2024-17
  - AU-2025-01, AU-2025-02, AU-2025-03, AU-2025-05, AU-2025-06, AU-2025-07, AU-2025-08, AU-2025-09, AU-2025-10, AU-2025-11, AU-2025-12, AU-2025-14, AU-2025-16, AU-2025-19, AU-2025-21, AU-2025-25, AU-2025-26
- **What we can still say about them:**
  - Most are miners, funds or foreign buyers with no ACCC condition in the deal database.
  - None of the 31 announced after Aug 2018 has a statement of issues on the ACCC's list, so missing them should not change the statement of issues sample.
  - The other 4 (2017 to 2018) can't be checked that way, because the list pages for 2012 to Aug 2018 were not read.
- **SOI cross-check for 2015 to Aug 2018:** it rests on the deal-by-deal searches and the matter pages alone.
- **The SOI list itself is incomplete.** Qantas and Alliance's statement of issues (18 Aug 2022) is on its matter page but missing from the list. So the list is a check, not proof.
- **NZ (second priority) was not done.** That means the Commerce Commission clearance register and the Overseas Investment Office decisions on LINZ. It needs a fresh session with search available.

## Things that would weaken a test of overreaction to ACCC concerns

1. **The sample is small.**
   - There are 14 events, on 13 different targets. Asciano has two (Oct 2015 and May 2016), and they overlap with its rival-bid contest.
   - Only 3 of the reviews with a public record ended in opposition.
2. **Events overlap with other news.**
   - Asciano had rival bids running through both of its reviews.
   - Tatts had its statement of issues 4 days before Tabcorp moved to the Tribunal.
   - TPG and Vodafone was a merger of two listed sides.
   - Healius and Link had their own business news running at the same time.
3. **The market often hears early.**
   - Delays and information requests usually come before a statement of issues, and the parties often disclose the ACCC's concerns themselves.
   - The ACCC tells the parties before it publishes, and the time of day of publication is not recorded here.
   - So the publication date may not be the first day the market knew.
4. **Scrip and mixed deals.** Several of these deals pay in shares (Novion, Tatts, oOh!media, Healius, among others). The target's price then moves with the bidder's, so a target-only return mixes deal risk with bidder news.
5. **The register only shows part of the picture.**
   - Confidential reviews never produce a public statement of issues.
   - Concerns raised privately before a deal was announced are invisible.
   - So the "concerns raised" group is only the public, contested reviews.
6. **The routes differ.** Informal reviews, ACCC authorisations, a Tribunal case and one new-regime notification are not the same process:
   - The AP Eagers and Origin "equivalents" are a feedback letter and transparency letters, not statements of issues.
   - From 1 Jan 2026 the informal process no longer exists.
7. **Dates have some noise.**
   - The ACCC and the deal database disagree by a day or so in a few places (iiNet, Xenith, Tatts re-authorisation). The ACCC date is used and the difference is noted.
   - For Alliance, the register header and timeline differ by a day on the start date.
   - In four cases the review started before the binding announcement (Asciano Brookfield, APA, Sydney Airport, Xenith IPH), so "time from announcement" is not a clean clock.
8. **Outcomes are known now.** Choosing or weighting events using outcomes (opposed versus cleared) would bring in hindsight. The event dates in this file can be used without knowing outcomes, but the outcome columns are right beside them.
