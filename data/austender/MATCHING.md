# AusTender matches to ASX-listed companies

Written by `tools/austender_match.py` from `contracts_YYYY.csv.gz` and Norgate's list of every ASX security since 2010 (`data/norgate/universe/securities.csv`). Hand checks are in `match_checks.csv`. No share prices were read for this work.

## Counts by year

| year | notices | of which contracts | matched notices | of which contracts | high confidence |
|---|---|---|---|---|---|
| 1999 | 1 | 1 | 0 | 0 | 0 |
| 2002 | 3 | 3 | 0 | 0 | 0 |
| 2003 | 32 | 32 | 0 | 0 | 0 |
| 2004 | 466 | 451 | 0 | 0 | 0 |
| 2005 | 1,575 | 1,523 | 0 | 0 | 0 |
| 2006 | 5,972 | 5,851 | 0 | 0 | 0 |
| 2007 | 41,884 | 39,595 | 0 | 0 | 0 |
| 2008 | 88,152 | 81,206 | 0 | 0 | 0 |
| 2009 | 93,878 | 82,485 | 0 | 0 | 0 |
| 2010 | 96,389 | 79,955 | 6,692 | 5,661 | 6,178 |
| 2011 | 92,444 | 79,416 | 6,555 | 5,491 | 6,160 |
| 2012 | 88,167 | 73,933 | 5,925 | 4,888 | 5,554 |
| 2013 | 82,315 | 68,358 | 3,873 | 3,205 | 3,585 |
| 2014 | 81,904 | 67,193 | 5,182 | 3,975 | 4,856 |
| 2015 | 88,988 | 71,698 | 4,507 | 3,552 | 4,218 |
| 2016 | 87,217 | 68,875 | 3,805 | 2,900 | 3,496 |
| 2017 | 83,309 | 65,587 | 3,615 | 2,834 | 3,271 |
| 2018 | 78,056 | 63,259 | 3,458 | 2,776 | 3,058 |
| 2019 | 80,800 | 65,554 | 3,306 | 2,611 | 2,892 |
| 2020 | 72,405 | 64,431 | 3,095 | 2,713 | 2,533 |
| 2021 | 70,624 | 70,624 | 3,119 | 3,119 | 2,551 |
| 2022 | 66,440 | 66,440 | 2,994 | 2,994 | 2,510 |
| 2023 | 79,540 | 58,778 | 3,839 | 2,658 | 3,674 |
| 2024 | 83,509 | 62,522 | 4,042 | 2,746 | 3,876 |
| 2025 | 96,602 | 57,978 | 4,530 | 1,982 | 4,362 |
| 2026 | 88,801 | 46,524 | 3,496 | 1,487 | 3,365 |
| total | 1,649,473 | 1,342,272 | 72,033 | 55,592 | 66,139 |

Matched notices by confidence: high 66,139, medium 4,499, low 1,395. Distinct listed securities matched: 469, under 468 company names (322 securities with at least one high-confidence match). Hand-checked notices: 46,794, covering 140 supplier and company pairs. Notices before 2010 cannot match: Norgate's list starts in 2010.

## The 40 largest matched contracts

Contracts only (amendments left out), by value.

| symbol | listed name | supplier | value (A$) | publish date | confidence | checked |
|---|---|---|---|---|---|---|
| TLS.au | Telstra Group Limited | Telstra Corporation Limited | 6,380,000,000 | 2012-11-01 | high | no |
| ASB.au | Austal Limited | AUSTAL DEFENCE SHIPBUILDING AUSTRALIA | 5,231,621,478 | 2026-03-23 | high | yes |
| DOW.au | Downer EDI Limited | SPOTLESS FACILITY SERVICES PTY LTD GEMS PROJECT | 3,692,765,476 | 2025-10-20 | high | yes |
| BRS-201605.au | Broadspectrum Limited | TRANSFIELD SERVICES (AUSTRALIA) | 3,419,256,000 | 2014-08-26 | high | yes |
| CSL.au | CSL Limited | CSL Behring (Australia) Pty Ltd | 3,351,400,190 | 2018-01-10 | medium | no |
| CSL.au | CSL Limited | CSL Limited | 2,441,560,000 | 2010-02-03 | high | no |
| BRS-201605.au | Broadspectrum Limited | TRANSFIELD SERVICES (AUSTRALIA) PTY LIMITED | 2,110,422,550 | 2014-04-11 | high | yes |
| SSM.au | Service Stream Limited | Service Stream Infrastructure Services Pty Ltd | 2,038,064,430 | 2025-10-20 | high | yes |
| BRS-201605.au | Broadspectrum Limited | TRANSFIELD SERVICES (AUSTRALIA) | 1,681,414,284 | 2014-10-07 | high | yes |
| ASB.au | Austal Limited | AUSTAL DEFENCE SHIPBUILDING AUSTRALIA | 1,347,494,079 | 2026-01-22 | high | yes |
| TLS.au | Telstra Group Limited | TELSTRA SECURE BILLING | 1,203,139,833 | 2022-01-11 | high | no |
| TLS.au | Telstra Group Limited | COBS TELSTRA | 1,046,460,685 | 2013-05-14 | medium | no |
| SPO-201908.au | Spotless Group Holdings Limited | SPOTLESS FACILITY SERVICES PTY LTD | 977,792,691 | 2017-02-14 | high | yes |
| SPO-201908.au | Spotless Group Holdings Limited | SPOTLESS FACILITY SERVICES PTY LTD | 969,097,787 | 2014-09-23 | high | yes |
| MPL.au | Medibank Private Limited | MEDIBANK HEALTH SOLUTIONS PTY LTD | 907,852,922 | 2016-09-06 | medium | no |
| TLS.au | Telstra Group Limited | Telstra | 832,700,000 | 2012-07-12 | high | no |
| CSL.au | CSL Limited | CSL Behring (Australia) Pty Ltd | 806,808,906 | 2021-01-19 | medium | no |
| LLC.au | Lendlease Group | LEND LEASE BUILDING PTY LTD | 785,771,037 | 2015-01-05 | high | no |
| SPO-201908.au | Spotless Group Holdings Limited | SPOTLESS FACILITY SERVICES PTY LTD | 758,211,153 | 2017-10-03 | high | yes |
| DTL.au | Data#3 Limited | DATA#3 LIMITED. DATA 3 GROUP | 719,899,547 | 2026-08-12 | high | yes |
| VNT.au | Ventia Services Group Limited | VENTIA AUSTRALIA PTY LTD GEMS PROJECT | 645,150,336 | 2024-09-17 | high | yes |
| SIG.au | Sigma Healthcare Limited | SIGMA HEALTHCARE LIMITED | 635,495,300 | 2025-07-10 | high | yes |
| LLC.au | Lendlease Group | LENDLEASE BUILDING PTY LIMITED | 592,200,121 | 2020-09-22 | high | no |
| QAN.au | Qantas Airways Limited | Qatans Airways Limited | 560,298,919 | 2010-04-07 | medium | no |
| VEA.au | Viva Energy Group Limited | VIVA ENERGY AUSTRALIA PTY LTD | 552,977,397 | 2026-08-19 | high | yes |
| LLC.au | Lendlease Group | LENDLEASE BUILDING PTY LIMITED | 533,775,183 | 2022-02-03 | high | no |
| LLC.au | Lendlease Group | LEND LEASE BUILDING CONTRACTORS | 509,410,000 | 2018-02-13 | high | no |
| DTL.au | Data#3 Limited | DATA 3 GROUP | 495,269,787 | 2025-07-02 | high | yes |
| KKT-201912.au | Konekt Limited | Mission Providence Pty Ltd | 470,700,817 | 2015-06-19 | medium | yes |
| CTD.au | Corporate Travel Management Limited | CORPORATE TRAVEL MANAGEMENT GROUP PTY LTD | 455,293,055 | 2024-03-15 | high | yes |
| NAB.au | National Australia Bank Limited | NATIONAL AUSTRALIA BANK LIMITED | 450,278,950 | 2024-06-25 | high | no |
| CGF.au | Challenger Limited | Challenger Property Nominees | 434,406,242 | 2011-05-09 | low | no |
| LLC.au | Lendlease Group | LENDLEASE BUILDING PTY LIMITED | 427,501,466 | 2020-03-27 | high | no |
| VNT.au | Ventia Services Group Limited | VENTIA AUSTRALIA PTY LTD | 426,831,221 | 2023-08-01 | high | yes |
| ASB.au | Austal Limited | AUSTAL SHIPS P/L | 425,102,381 | 2015-08-28 | high | yes |
| NAB.au | National Australia Bank Limited | NATIONAL AUSTRALIA BANK LIMITED | 410,052,327 | 2022-02-24 | high | no |
| LLC.au | Lendlease Group | LEND LEASE BUILDING CONTRACTORS | 403,299,532 | 2018-04-03 | high | no |
| VNT.au | Ventia Services Group Limited | VENTIA AUSTRALIA PTY LTD | 400,209,974 | 2025-11-18 | high | yes |
| VEA.au | Viva Energy Group Limited | VIVA ENERGY AUSTRALIA PTY LTD | 382,519,131 | 2025-08-04 | high | yes |
| LLC.au | Lendlease Group | LEND LEASE BUILDING PTY LTD | 380,306,506 | 2016-08-02 | high | no |

## Matches rejected

Rejected or cut back by hand checks (the notices are left out of matched.csv):

| supplier | proposed match | notices | value (A$) | why |
|---|---|---|---|---|
| ASPEN MEDICAL PTY LTD | APZ.au Aspen Group | 225 | 1,755,721,943 | Aspen Medical is a privately owned health services company (Wikipedia: Aspen Medical), not the listed Aspen Group |
| DT GLOBAL ASIA PACIFIC PTY LTD | CDD-202501.au Cardno Limited | 98 | 1,469,115,114 | kept only start to 2022-09-12: Cardno Emerging Markets (formerly Cardno ACIL) is Cardno's international development arm; aid program work for DFAT. The same ABN appears as DT Global Asia Pacific from 13 Sep 2022, so later notices are not counted (sale date taken from the notices) |
| ABACUS INNOVATIONS AUSTRALIA | ABG.au Abacus Group | 219 | 1,214,938,304 | Abacus Innovations Australia was the Lockheed Martin IT services business merged into Leidos in Aug 2016 (Wikipedia: Leidos); the same ABN later trades as Leidos Australia. Not Abacus Group, the property owner |
| AMA PROJECTS PTY LTD | AMA.au AMA Group Limited | 302 | 235,084,897 | AMA Projects Pty Ltd does building fit-outs in Canberra; AMA Group is a vehicle panel repair business, no link |
| Duxton Water Ltd | DBF.au Duxton Farms Ltd | 10 | 139,144,419 | Duxton Water Ltd is a separate ASX company (code D2O) that is not in Norgate's list; it is not Duxton Farms, though both are managed by Duxton Capital |
| VOLT LANE PTY LTD t/a THE TRUSTEE FOR THE VOLT LANE TRUST | VPR.au Volt Group Limited | 1 | 94,449,505 | Volt Lane Pty Ltd is the trustee of a family property trust leasing an ATO building in Albury; no link to Volt Group |
| A.M.A. Services (W.A.) Pty Ltd | AMA.au AMA Group Limited | 21 | 58,840,181 | A.M.A. Services (W.A.) runs an Australian Apprenticeships centre; AMA Group is a vehicle panel repair business, no link |
| PERPETUAL ENERGY PTY LTD | PPT.au Perpetual Limited | 12 | 38,159,915 | Perpetual Energy Pty Ltd is a natural gas retailer; no link to Perpetual Limited, the fund manager and trustee company |
| The Trustee for Symbio Alliance Trust | SYM-202402.au Symbio Holdings Limited | 55 | 17,298,569 | Symbio Alliance is a testing laboratory business; Norgate's SYM is the telecommunications company Symbio Holdings (formerly MNF Group), no link |
| ICD (ASIA PACIFIC) PTY LIMITED | VNT.au Ventia Services Group Limited | 7 | 12,878,746 | kept only 2023-09-01 to now: This ABN traded as ICD (Asia Pacific), a fuel engineering firm, before it appears as Ventia Engineering Services from Sept 2023; only notices from then on are counted (acquisition date taken from the notices) |
| BRAVURA ECOMMERCE SOLUTIONS PTY LTD trading as Essential Computer Systems Pty Ltd | BVA-201309.au Bravura Solutions Limited | 6 | 11,958,041 | Notices are for Essential Computer Systems, a Canberra IT hardware reseller trading through a company called Bravura eCommerce Solutions; no link to Bravura Solutions, the wealth software company |
| Symbio Laboratories Pty Ltd | SYM-202402.au Symbio Holdings Limited | 13 | 9,965,960 | Symbio Laboratories is a food and chemical testing laboratory; Norgate's SYM is the telecommunications company Symbio Holdings (formerly MNF Group), no link |
| THE COMMS STORE PTY LTD | CCG.au Comms Group Ltd | 10 | 7,231,927 | The Comms Store is a strategic communications and community engagement firm; Comms Group Ltd sells telecommunications services, no link found |
| EML Solutions Pty Ltd | EML.au EML Payments Limited | 2 | 7,094,606 | EML Solutions is the claims management arm of Employers Mutual (EML), a workers compensation manager; no link to EML Payments |
| Aspen Pharma Pty Ltd | APZ.au Aspen Group | 5 | 5,264,000 | Aspen Pharma Pty Ltd is the Australian arm of South Africa's Aspen Pharmacare, not the listed Aspen Group |
| CARDNO MBK | CDD-202501.au Cardno Limited | 2 | 3,963,750 | kept only start to 2021-12-31: Cardno (NSW/ACT) is a Cardno engineering and environmental consulting company. Cardno sold its consulting businesses to Stantec in Dec 2021 (Wikipedia: Stantec), so later notices are not counted |
| VTS Canberra Pty Ltd | CNW-202311.au Cirrus Networks Holdings Limited | 12 | 1,949,051 | kept only 2018-04-01 to now: This ABN traded as Dataflex and VTS Canberra before it appears as Cirrus Networks (Canberra) from April 2018; only notices from then on are counted (acquisition date taken from the notices) |
| CARDNO EMERGING MARKETS USA, LTD | CDD-202501.au Cardno Limited | 1 | 1,197,484 | kept only start to 2022-09-12: Cardno Emerging Markets USA is Cardno's US international development arm; DFAT aid program work. Cut at the date the Australian arm first appears as DT Global (13 Sep 2022) |
| Cardno | CDD-202501.au Cardno Limited | 2 | 430,372 | kept only start to 2021-12-31: Cardno engineering consulting company; Defence engineering assessments. Cardno sold its consulting businesses to Stantec in Dec 2021 (Wikipedia: Stantec), so later notices are not counted |

Also left out: 21,193 notices from 2010 on whose supplier matched a listed company but whose publish date falls outside that security's trading window in Norgate (before listing or after delisting) or outside the dates a hand check allows, and 15,922 notices from before 2010, which Norgate's list does not cover.

## What could weaken a test

- Coverage. Notices run from 1999 to 2026, but years before 2007 are thin (only notices carried over from the old Gazette system) and Norgate's list starts in 2010, so matches start in 2010. The last year runs only to the day of the download. 81,731 amendments have no usable publish date (see README.md) and are not matched; amendments made after June 2020 to contracts published before 2013 are missing altogether.
- Late publication. Agencies must report within 42 days of the contract starting, and many report late. Of 55,592 matched contracts, 20% were published more than 42 days after their start date and 3% more than a year after; 7% were published before their start date. Where a company announced the contract itself, the market heard first and the AusTender date is a second, later event.
- Dates only. The contract files give publish dates without times, and 0% of matched contracts carry a Saturday or Sunday date. The API time-of-day split is in README.md: most notices go up during ASX trading hours, so the publish day is partly after the event.
- Many notices are not news. Panel and standing-offer arrangements produce thousands of small orders (Data#3 alone has over 5,000 notices), and 2,204 company-days carry five or more matched contracts. Ceiling values on panels and standing offers overstate likely spend.
- Values that look wrong. 10 matched contracts have no value (contracts known only through a later amendment). 7 matched contracts of A$1 billion or more go to companies outside the ASX 100; each should be read before it is used, as keying errors and multi-year ceilings both occur.
- Weaker matches. 4,086 matched notices rest on a shared ABN rather than the name, 676 on the first words of the listed name only, and medium and low matches below the hand-check line have not been read by a person. 158 matched notices are leases where a listed fund manager or trustee holds the building for a fund, so the rent goes to the fund rather than the listed company (marked low).
- Names. Norgate holds each security under its latest name, so companies that renamed are only matched through the short rename list in tools/austender_match.py. Subsidiaries trading under a different name from the parent (for example Thiess under CIMIC) are mostly not matched, and a subsidiary sold to another owner keeps matching its old parent unless a hand check limits its dates.
- Gaps in Norgate's list. A few ASX companies are missing from it (for example XTEK and Duxton Water), so their contracts cannot be matched, and a company that renamed after a merger can carry a name that did not exist when the contract was let (Norgate's BJY, Barrenjoey Group, is Magellan Financial Group under a later name).
- ASX 100. The repository has no S&P/ASX 100 membership history, so the hand-check rule used a fixed list of clear large caps (ASX100 in tools/austender_match.py). Borderline mid caps such as Downer and Viva Energy were left off the list and checked by hand anyway.
- How the hand checks were done. Each check read the supplier names under the ABN, the agencies and the contract descriptions, and the company's history from Wikipedia where a page existed. The shared web search allowance ran out early in this work, so some checks rest on the notice data and the company name alone; their notes say so (for example Service Stream's 2025 Defence base services contract and the 2015 Mission Providence jobactive contracts).
- Joint ventures. Some suppliers are joint ventures (for example Downer EDI Works with F.K. Gardner & Sons); the listed company's share of the contract is not known.

