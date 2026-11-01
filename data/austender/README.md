# AusTender contract notices

Every Australian Government contract notice that the two public AusTender sources hold, contracts and their amendments, one file per calendar year of publish date (`contracts_YYYY.csv.gz`). Downloaded by `tools/austender_fetch.py` and merged by `tools/austender_build.py`, both run by `.github/workflows/austender.yml`.

Matches of these notices to ASX-listed companies are in `matched.csv`, described in `MATCHING.md` and made by `tools/austender_match.py`, with the hand checks in `match_checks.csv`.

## Columns

| column | meaning |
|---|---|
| cn_id | the notice's own ID: CN1234 for a contract, CN1234-A2 for its second amendment |
| parent_cn_id | for an amendment, the contract it changes; blank for a contract |
| amendment | 0 for a contract, n for amendment An |
| publish_date | the day the notice went up on AusTender, Canberra time. For an amendment, the day the amendment went up |
| start_date, end_date | contract period as reported, Canberra dates |
| value_aud | contract: value as published, AUD including GST, for the life of the contract. Amendment: the change in value it made (negative for a cut, 0 for a change of dates or wording only, blank if unknown) |
| agency | the buying agency |
| supplier_name, supplier_abn | as entered by the agency; the ABN is kept only when it has 11 digits |
| description | the agency's short description, HTML removed |
| unspsc | the product or service code the agency chose |
| procurement_method | Open tender, Limited tender or Prequalified tender |

De-duplicated on CN ID plus amendment number. Where a notice is in several sources, the earliest snapshot is kept (closest to what was published) and later sources only fill blank fields.

## Sources

1. data.gov.au, Historical Australian Government Contract Notice Data: https://data.gov.au/data/dataset/5c7fa69b-b0e9-4553-b8df-2a022dd2e982 (file list from the CKAN API: https://data.gov.au/data/api/3/action/package_show?id=5c7fa69b-b0e9-4553-b8df-2a022dd2e982). Files read, earliest snapshot first:

| file | snapshot | notices read |
|---|---|---|
| [2014-2015 Commonwealth Government Contract Data](https://data.gov.au/data/dataset/5c7fa69b-b0e9-4553-b8df-2a022dd2e982/resource/561a549b-5a65-450e-86cf-81d392d8fef3/download/20142015fy.csv) | 2015-10-25 | 69,236 |
| [AusTender CNs published up to 31 December 2015](https://data.gov.au/data/dataset/5c7fa69b-b0e9-4553-b8df-2a022dd2e982/resource/3ea0631b-7715-49fa-9bba-64717e22ae1b/download/austenderallcnsupto31dec15.zip) | 2016-01-01 | 645,854 |
| [2015-2016 Commonwealth Government Contract Data](https://data.gov.au/data/dataset/5c7fa69b-b0e9-4553-b8df-2a022dd2e982/resource/293b97f5-25f6-4667-aa3e-fd7ddbdec363/download/20152016-fy-austender-cns.zip) | 2016-09-02 | 70,338 |
| [AusTender CNs published up to 19 September 2016](https://data.gov.au/data/dataset/5c7fa69b-b0e9-4553-b8df-2a022dd2e982/resource/41feecdb-dcb0-46a7-bdab-f717c5ed6ca0/download/austenderallcnsupto19sep16.zip) | 2016-09-20 | 698,111 |
| [2016 Calendar Year Commonwealth Government Contract Data](https://data.gov.au/data/dataset/5c7fa69b-b0e9-4553-b8df-2a022dd2e982/resource/8ff11006-674f-4cc7-ab47-997959810f3b/download/2016calyearbypublishdate.csv) | 2017-03-03 | 68,044 |
| [AusTender CNs published up to 30 June 2017](https://data.gov.au/data/dataset/5c7fa69b-b0e9-4553-b8df-2a022dd2e982/resource/282ec907-cb25-4e34-9bae-2e20ce192df3/download/austenderallcnsupto30jun17.zip) | 2017-07-06 | 745,923 |
| [2016-2017 Australian Government Contract Data](https://data.gov.au/data/dataset/5c7fa69b-b0e9-4553-b8df-2a022dd2e982/resource/21212500-169f-4745-86b3-6ac1c1174151/download/2016-2017-australian-government-contract-data.csv) | 2017-09-11 | 64,092 |
| [2016-17 CNs published up to 11 September 2017](https://data.gov.au/data/dataset/5c7fa69b-b0e9-4553-b8df-2a022dd2e982/resource/fb1a9116-c85d-4a0b-a4e3-c54eab79efaf/download/2016-2017-austender-cns-published-to-11-sept-2017.csv) | 2017-09-14 | 77,597 |
| [AusTender CNs published up to 3 January 2018](https://data.gov.au/data/dataset/5c7fa69b-b0e9-4553-b8df-2a022dd2e982/resource/9996a9a8-0476-4dd1-a2f5-e6f0a74dcef7/download/austenderallcnupto03jan18.zip) | 2018-01-04 | 778,878 |
| [AusTender CNs published up to 28 August 2018](https://data.gov.au/data/dataset/5c7fa69b-b0e9-4553-b8df-2a022dd2e982/resource/0a15c504-f96b-4076-b18b-7b0ed4c0e5f2/download/cns-parent-and-amendments-28082018.zip) | 2018-08-28 | 853,073 |
| [2017-18 Australian Government Contract Data](https://data.gov.au/data/dataset/5c7fa69b-b0e9-4553-b8df-2a022dd2e982/resource/bc2097b7-8116-4e9d-9953-98813635892a/download/17-18-fy-dataset.csv) | 2019-01-25 | 73,458 |
| [2018-19 Australian Government Contract Data](https://data.gov.au/data/dataset/5c7fa69b-b0e9-4553-b8df-2a022dd2e982/resource/ce6b8183-e881-49d4-a367-0851bbb025bf/download/cn-parent-and-amendments-2018-19-30082019.xlsx) | 2019-08-30 | 78,150 |
| [AusTender CNs published up to 30 August 2019](https://data.gov.au/data/dataset/5c7fa69b-b0e9-4553-b8df-2a022dd2e982/resource/ec0ac429-a813-4325-bc8c-a8e37401ffc0/download/cn-parent-and-amendments-30092019-ltr.xlsx) | 2019-08-31 | 933,029 |
| [2019-20 Australian Government Contract Data](https://data.gov.au/data/dataset/5c7fa69b-b0e9-4553-b8df-2a022dd2e982/resource/06439664-bbcf-4118-a604-164006bffcaa/download/2019-20-australian-government-contract-data.xlsx) | 2021-01-31 | 81,174 |

   Left out: the 2014-15 xlsx (the same rows as the 2014-15 csv), the GaPS contracts export (the system before AusTender, 1997 to 2007, which has no CN IDs) and the UNSPSC code list.

2. AusTender OCDS API, `https://api.tenders.gov.au/ocds/findByDates/contractPublished/{start}/{end}`, paged one UTC day at a time from 1 January 2013 (the earliest it serves) to the day of the run. Documentation: https://github.com/austender/austender-ocds-api. The API returns each contract with all of its amendments, in the window of the contract's publish date.

| API year (contract publish date) | releases read | UTC days with no notices | days that failed after three tries |
|---|---|---|---|
| 2013 | 83,308 | 60 (Sat 49, Sun 5, Fri 2) | none |
| 2014 | 79,273 | 61 (Sat 51, Sun 5, Fri 3) | none |
| 2015 | 84,252 | 55 (Sat 47, Sun 4, Fri 2) | none |
| 2016 | 82,898 | 55 (Sat 48, Fri 2, Sun 2) | none |
| 2017 | 81,085 | 63 (Sat 52, Sun 6, Fri 2) | none |
| 2018 | 86,938 | 58 (Sat 47, Sun 5, Fri 2) | none |
| 2019 | 89,867 | 53 (Sat 43, Sun 4, Fri 2) | none |
| 2020 | 91,841 | 50 (Sat 43, Sun 2, Fri 2) | none |
| 2021 | 102,212 | 49 (Sat 38, Sun 4, Fri 3) | none |
| 2022 | 93,133 | 47 (Sat 36, Sun 5, Fri 2) | none |
| 2023 | 82,417 | 45 (Sat 38, Sun 4, Mon 1) | none |
| 2024 | 87,777 | 46 (Sat 37, Fri 3, Sun 2) | none |
| 2025 | 75,896 | 51 (Sat 43, Sun 3, Fri 2) | none |
| 2026 | 51,031 | 45 (Sat 39, Sun 5, Fri 1) | none |

The API answers HTTP 400 for a window with no notices. Those days are almost all UTC Saturdays (Saturday morning to Sunday morning in Canberra) and public holidays, so they are counted as empty rather than failed. As a check, the data.gov.au files hold 35 contracts with a Canberra publish date on any of those 738 dates.

Rows read: API 1,171,903, data.gov.au files 5,236,957.

## Row counts by year of publish date

| year | contracts | amendments | file size |
|---|---|---|---|
| 1999 | 1 | 0 | 0.0 MB |
| 2002 | 3 | 0 | 0.0 MB |
| 2003 | 32 | 0 | 0.0 MB |
| 2004 | 451 | 15 | 0.0 MB |
| 2005 | 1,523 | 52 | 0.1 MB |
| 2006 | 5,851 | 121 | 0.3 MB |
| 2007 | 39,595 | 2,289 | 1.8 MB |
| 2008 | 81,206 | 6,946 | 3.9 MB |
| 2009 | 82,485 | 11,393 | 4.2 MB |
| 2010 | 79,955 | 16,434 | 4.5 MB |
| 2011 | 79,416 | 13,028 | 4.3 MB |
| 2012 | 73,933 | 14,234 | 4.0 MB |
| 2013 | 68,358 | 13,957 | 3.7 MB |
| 2014 | 67,193 | 14,711 | 3.6 MB |
| 2015 | 71,698 | 17,290 | 3.7 MB |
| 2016 | 68,875 | 18,342 | 3.7 MB |
| 2017 | 65,587 | 17,722 | 3.5 MB |
| 2018 | 63,259 | 14,797 | 3.4 MB |
| 2019 | 65,554 | 15,246 | 3.5 MB |
| 2020 | 64,431 | 7,974 | 2.9 MB |
| 2021 | 70,624 | 0 | 2.8 MB |
| 2022 | 66,440 | 0 | 2.7 MB |
| 2023 | 58,778 | 20,762 | 3.1 MB |
| 2024 | 62,522 | 20,987 | 3.3 MB |
| 2025 | 57,978 | 38,624 | 3.7 MB |
| 2026 | 46,524 | 42,277 | 3.3 MB |
| total | 1,342,272 | 307,201 | |
| undated (`contracts_undated.csv.gz`) | 0 | 81,731 | |

Range: 1999 to 2026. Years before 2007 hold only the notices carried over from the old Gazette system when AusTender began, so they are thin. The current year runs to the day of the run.

## Gaps and weaknesses

- Amendment dates after June 2020. The data.gov.au files give each amendment's publish date up to 30 June 2020; the API does not. Each API amendment release carries the date of its latest change, and the move of older amendments onto the API stamped thousands with the same timestamp (2023-04-27T08:08:01Z on 157,833; 2025-05-08T07:14:12Z on 7,765; 2023-07-24T08:32:50Z on 3,188; 2023-04-27T08:08:29Z on 2,070). API amendment dates are used only when on or after 2023-04-28 and not a timestamp shared by 50 or more amendments. Amendments with no usable date are kept in `contracts_undated.csv.gz`; by year of their contract's publish date: 2011 18, 2013 4,662, 2014 2,439, 2015 2,119, 2016 2,547, 2017 4,534, 2018 7,146, 2019 12,005, 2020 17,997, 2021 16,323, 2022 8,285, 2023 2,166, 2024 1,405, 2025 85. Most will have been published between July 2020 and April 2023. After April 2023 an API amendment date can still be the date of a later correction rather than first publication.
- Amendment counts. The files give about 15,576 dated amendments a year for 2010 to 2019. The API-dated years carry 2023: 20,762, 2024: 20,987, 2025: 38,624, 2026: 42,277. The API also lists amendments that change only dates or wording, and some API dates will be the date of a later edit, so amendment dates from 2023 on are less reliable than contract dates.
- Amendments made after June 2020 to contracts published before 2013 are missing: the API only serves contracts published from 2013 and returns amendments with their contract.
- Notices only in the API: 607,411 (mostly those published after the files end). Notices from 2013 on that are in the files but not returned by the API: 33,299. They are kept.
- API amendment releases whose date is a bulk or pre-migration stamp (date not used): 178,187
- API release read twice (dropped): 25
- amendment publish date differs, file vs file (earliest kept): 2,564
- amendment publish date differs, files vs API (earliest kept): 6,469
- amendment value change unknown (blank): 12,911
- amendment value change worked out from totals: 258,038
- contract known only through an amendment (written with blank value): 733
- contract publish date differs, files vs API (earliest kept): 14
- contract value differs by more than 1%, files vs API (earliest kept): 6
  - examples (files vs API date): CN3413441 austenderallcnsupto30jun17.zip 2017-04-04 vs api 2016-09-13; CN3619513 cn-parent-and-amendments-30092019-ltr.xlsx 2019-08-13 vs api 2017-10-31; CN3556322 cn-parent-and-amendments-2018-19-30082019.xlsx 2018-12-04 vs api 2018-05-01; CN3568412 cn-parent-and-amendments-2018-19-30082019.xlsx 2019-02-01 vs api 2018-10-17; CN3638270 2019-20-australian-government-contract-data.xlsx 2019-11-04 vs api 2019-10-28; CN3658586 2019-20-australian-government-contract-data.xlsx 2020-02-10 vs api 2020-02-03
  - examples (files vs API value): CN2498341 cns-parent-and-amendments-28082018.zip 372,000 vs api 504,000; CN3293623 austenderallcnsupto31dec15.zip 23,800,000 vs api 24,783,305; CN3416694 austenderallcnsupto30jun17.zip 68,582 vs api 66,910; CN3655476 2019-20-australian-government-contract-data.xlsx 5,445,301 vs api 110,770,824; CN3658586 2019-20-australian-government-contract-data.xlsx 49,510 vs api 149,469; CN3656633 2019-20-australian-government-contract-data.xlsx 27,314 vs api 72,424
- Time of day. The files give dates only; the API gives a publish time. For contracts read from the API (2013 on), Canberra publish time was: 10:00 to 15:59 66%, 16:00 or later 14%, before 10:00 19%, weekend 0%. A notice put up during the day is public while the ASX is open, so the publish day itself is partly after the event.
- Agency names. The files carry the agency's name at the time of the notice; notices found only in the API carry the agency's current name after later machinery-of-government changes (for example Department of Home Affairs on a 2014 notice).
- Values are as agencies reported them. Panel and standing-offer notices can carry a ceiling rather than expected spend, and a few notices carry keying errors (for example values in the billions for small purchases).

