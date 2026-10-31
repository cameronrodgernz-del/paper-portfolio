# Australian deal database pilot: notes (built 31 October 2026)

## What is in the files

- `au_deals_2025_2026.csv` holds 50 rows covering 46 ASX-listed targets, with binding announcements between 1 January 2025 and 31 October 2026 and equity value at the offer of A$100m or more. There are 26 rows for 2025 and 24 for 2026.
- `au_candidates_2025_2026.csv` holds 57 entries for deals that were considered and left out, each with a reason and the source that was opened.
- Every URL in the `sources` column was opened while the row was being built. News pages appear only where they pointed to a filing or confirmed a date; any number that came only from a secondary source says so in `notes`.

## How the deals were found

1. Candidate spine. The most useful single list was the Mayne Report's running takeover tracker (maynereport.com, "Tracking ASX takeovers since pre-GFC peak in 2007"). It lists completed $100m+ deals by year, agreed deals still pending, and non-binding control moves. It was cross-checked against the deals named in the KWM "Public M&A market on a page" PDFs (H1 2025 and January to September 2025), Ashurst's 2026 deal report and its H1 2026 update, MinterEllison's 2025 wrap, and the G+T and HSF Kramer report pages (which name almost no deals in their free versions).
2. Contested deals. Takeovers Panel media releases (takeovers.gov.au/media-releases, pages 1 to 3) were scanned for 2025 and 2026 matters. This turned up Dropsuite, PointsBet, New World, Elanor Commercial Property Fund, Mayne Pharma, Humm, Atlas Arteria, Accent, Cygnus, Canyon and others.
3. Gap filling. Web searches for "scheme implementation deed", "bidder's statement" and similar terms returned ASX announcement PDFs, which were opened to identify the deal. The Motley Fool takeovers RSS feed and InvestSmart announcement pages helped with 2026 names. This found Reef Casino Trust, among others.
4. Deal detail. For each deal the binding announcement (SID, BIA or bidder's statement) was opened first, then the scheme booklet or target's statement where possible, then the meeting result, court and implementation releases. For still-listed targets, the ASX announcement list page (asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=XXX&timeframe=Y&year=YYYY) gives dated titles of every filing, which made it quick to find the timetable and any rival approaches.

## Rules applied where SCHEMA.md leaves a choice

- Primary listing. Targets whose primary listing is outside ASX were left out and logged: MAC Copper (NYSE, Jersey scheme), Adriatic Metals (LSE, UK scheme), Robex (TSX-V, Canadian arrangement) and Smartpay (NZX and ASX, NZ scheme, so it belongs to the NZ database).
- Existing controllers. Bids or schemes by a holder already above 50% were left out because they do not give the bidder control (Hutchison Telecommunications 88%, Ainsworth/Novomatic 52.9%, Canyon/A2MP 55.6%, Engenco, the second Iris bid for Reef Casino Trust, Donaco). These buy-outs could be added later as a separate category; Ainsworth is a useful failed-vote case if they are.
- Re-bids and rivals. When MIXI's PointsBet scheme failed at the vote it relaunched as a takeover, so the scheme and the takeover are separate rows linked to each other and to betr's rival bid. New World (CAML and Kinterra) and Vault (Regis and Genesis) also have one row per bidder. Price increases by the same bidder stay in the same row.
- Twin-scheme merger. For Soul Patts and Brickworks only Brickworks is recorded as a target; Soul Patts' own 1:1 scheme into the new TopCo is logged as the acquirer side.
- `rival_bid` is Y when a competing public proposal from another bidder (binding or not) was live while that row's deal was live. Competition that ended before the binding deal was signed (FleetPartners and Element, oOh!media, Insignia, AVJennings and Ho Bee) is described in `notes` with `rival_bid` N.
- `price_raised` is Y when the final price per share was above the initial price because of the bidder's action, including built-in step-ups that were triggered (Red Hawk, Atlas Arteria). Gold Road's final cash was higher only because its variable component tracked Northern Star's share price, so it is N.
- Outcomes. A takeover that went unconditional and gave the bidder control is "completed" even without compulsory acquisition (Atlas Arteria at 67%, PointsBet/MIXI at 66%). For takeovers, `implementation_date` and `outcome_date` are the offer close. A bid that closed without control is "lapsed" (Elanor CPF). A deal that lost to a rival is "superseded_by_rival".
- Equity value. Where the filing gives only an enterprise value, equity value was worked out as offer price times the stated fully diluted share count, and the note says "computed".
- Pending deals. Meeting, court and implementation dates are the latest scheduled dates in filings as at 31 October 2026 and are marked indicative in `notes`. European Lithium and Carnaby had passed their meetings, and Carnaby's scheme was due to take effect on 30 October, but neither was implemented by 31 October, so both are pending.
- ACCC. Deals signed before 1 January 2026 used the old informal process. Those signed after are framed under the new mandatory regime. Determination dates were found for Vault/Genesis (ACCC said no notification needed, 27 August 2026) and Southern Cross/Seven West (informal, not opposed 13 November 2025). Qube's Phase 1 period ended 19 June 2026 and Qoria cleared under the old process using the transitional rule. All other ACCC dates are blank, with the reason in `notes`.

## Deals I am unsure about

- Cue Energy (Horizon Oil bid, 2026). Excluded as about A$98m at announcement per Ashurst, but worth about A$108m by 18 March 2026. It is a borderline case, so recheck it against the original bidder's statement.
- Reef Casino Trust. The initial Iris price under the July 2025 agreement was not found in a filing, so `offer_price_initial` and `equity_value_m` are blank. The deal is clearly above threshold (A$192.7m at the final A$3.87).
- Elanor Commercial Property Fund. The equity value (about A$278m) comes from Ashurst, not a filing, and I didn't confirm whether any condition was still unsatisfied at close.
- European Lithium. The ratio was changed to a floating 0.025 to 0.045, and the A$0.42 final value is illustrative. The expert's verdict ("not fair", per legal press) is not confirmed from a filing.
- Cygnus Metals. Terms come from summary pages, because the SID PDF needed a login. The per-share value and the board recommendation are not confirmed from a filing.
- Brickworks and Seven West Media were all-scrip mergers. Seven West's implied value was below its last close (no premium).
- DUI/AUI is a listed investment company merger at NTA. The offer value is NTA-based, not a market price.
- Gold Road, Red Hawk, Domain, National Storage, Dropsuite, Reject Shop and RPMGlobal have implementation dates taken from the scheduled date in the last release opened, cross-checked with the Mayne Report, not from the implementation release itself.

## Fields most often blank (out of 50 rows)

- By design: `failure_reason` 44 (only failed deals), `related_deal_ids` 43, `min_acceptance_pct` 42 (schemes).
- Independent expert: `ier_low` and `ier_high` 36, `ier_verdict` 32, `ier_name` 26. Expert ranges sit deep in the booklets, which often run past the 100,000-character fetch limit.
- `pre_bid_stake_pct` 35 (usually nil or not stated), `first_approach_date` 29 (many deals had no prior public proposal), `booklet_date` 27, `court_date` 23, `intentions_pct` and `blocking_holders` 22, `meeting_date` 18, `break_fee_m` 16.
- `undisturbed_price` 12. Some filings state a premium but not the price, or use the last close without calling it undisturbed.

## Which sources would scale to 2015 to 2024

- Mayne Report tracker. Its stated coverage runs from 2007 and includes ASX300 targets plus anything over $100m, so it is the best free candidate spine. The page is long, though, and the fetch tool cut the 2025 section off at entry 14 even with an offset. Earlier years may need the page saved and read in sections, or another route.
- ASX announcement PDFs (announcements.asx.com.au/asxpdf/...). These open reliably and are the primary source for nearly every field. The ASX v2 announcement list page works only for codes that are still listed, so for delisted targets the PDFs have to be found through search, company websites, weblink (wcsecure.weblink.com.au), InvestSmart or Aspect Huntley mirrors.
- Takeovers Panel media releases and reasons. These are complete back to the early 2000s and paginated, but they cover only disputed deals.
- delisted.com.au. It has yearly downloadable archives (1996 to 2025) of delistings with reasons, which would catch completed schemes and takeovers but not failed or withdrawn deals.
- Law firm reviews. The free web versions of the HSF Kramer, G+T, Ashurst, MinterEllison and Corrs reports give counts and a few named deals. KWM's "market on a page" PDFs list only the top 10. These are useful for checking totals (HSF counts 59 control deals in FY25 and 57 in FY26; Ashurst counts 40 deals over A$50m in 2025 and 21 binding deals over A$50m in H1 2026), but they are not complete deal lists. HSF's full report (with its usual appendix) needs an access request.
- The ACCC merger register (informal and new regime) and FIRB records were only needed for a few dates. They would help with regulatory timing but not with finding deals.

## Count check

The population here is smaller than the 60 to 120 expected. On the evidence above, binding control deals of A$100m or more for ASX-primary targets were roughly 25 to 30 a year in this window. That fits the Mayne Report's 30 completed $100m+ deals in calendar 2025, a figure that includes 2024-announced deals, controller buy-outs and foreign-primary targets that are excluded here. Adding back the excluded controller buy-outs and secondary-listed targets would bring the total to about 60. The most likely gaps are deals in the A$100m to A$250m band, where coverage depended on searches rather than a complete list.
