# Desk log

Each entry starts with "## <date>, <summary>". Changes of terms on the live list, with their source.

## 2026-11-01, Deal files from primary sources for every live ASX deal; terms corrected

The deal files in research/deals/ (one per live deal, from the announcements, booklets, deeds, expert
reports and regulators' registers) were folded into config/live_deals.csv with src/deal_files.py.
Terms changed on the live list, each from its deal file:
- VAU: cash A$0.475 to A$0.5125 a share, raised to make up for the Genesis A$0.05 dividend Vault
  holders don't receive (VAU.md, scheme booklet).
- OML: A$1.70 to A$1.68; the 2c interim dividend in the headline was paid on 17 Sep, so a buyer now
  gets A$1.68 (OML.md). Payment moved to 10 Dec after the 30 Oct timetable change.
- AUC: valued as the mix a holder gets if every holder elects cash: A$0.3395 cash plus 0.02525
  OceanaGold shares (NYSE OGC), from the A$194m cash cap over the scheme shares (AUC.md). The old row
  used the A$1.36 cash alternative before scale-back, which overstated the gap to the offer
  (12.9% shown; about nil on the mix). OceanaGold added to the nightly fetch as US:OGC.
- SDF: A$6.00 to A$5.8725; the 12.75c FY26 dividend was paid on 25 Sep (SDF.md).
- PPC: cash A$0.745 to A$0.68; the 6.5c dividend was paid on 22 Sep (PPC.md). The scrip leg is
  still valued at Ingenia's price, which carries the bids for Ingenia itself; the deal file sets
  out why that value disappears if this deal goes ahead.
- Notes rewritten for AX1, BET, RWC, MEI, CWY and FPR from their files.
Added: RTH (Racing and Sports, PA Media scheme at A$1.04 cash), with its undisturbed price of
A$0.54 (the close on 16 Oct). Not added: EUR and CNB, both unconditional and paying in early
November, so only the payment is left.

## 2026-11-01, Undisturbed prices dated, and set for VAU and RWC

The live list now carries undisturbed_date, and the break price moves the undisturbed price with the
market from that date, not from the deal's own announcement.
- VAU: A$4.50 at the close on 4 May 2026, before the first (Regis) scheme; the Genesis deal of
  14 Jul followed a contest, so the price just before it already held a bid (deals database AU-2026-10).
- RWC: A$3.61 at the close on 17 Aug 2026, before the Process Deed with Brookfield was announced
  (deals database AU-2026-21; RWC.md).
- RTH: dated 16 Oct 2026, the last close before the announcement.
