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

## 2026-11-01, Deals added from the sweep: A11 and GL1; NZX has none live

From the sweep of ASX and NZX announcements (deal files A11.md, GL1.md):
- A11 (Atlantic Lithium, Zhejiang Huayou Cobalt): US$0.25486 cash. Undisturbed A$0.280, the last
  close before the 7 May announcement. Payment indicated only as December 2026, so set to 31 Dec.
- GL1 (Global Lithium, Titan Australia Mining): A$1.15 cash. Undisturbed A$0.665, the last close
  before the 22 Sep announcement. Payment indicated as mid-January 2027, so set to 15 Jan.
- Not added: RCT (Reef Casino Trust; Iris already holds 96.5% and will compulsorily acquire; only
  the payment is left), and EUR and CNB (both effective, paying in early November).
- NZX: no live control deal at NZ$20m or more. Bremworth and 2 Cheap Cars have finished. Watching
  non-binding approaches: thl (update by the 6 Nov AGM), SkyCity (structured process since 30 Sep).
Both new deals have no stored prices yet; the nightly fetch adds them.

## 2026-11-01, Undisturbed dates filled for every live deal; Peet's undisturbed price moved to 9 Jul

The break price moves the undisturbed price with the market from its own date, so each live deal
now has that date, from the deal database's undisturbed basis: BET 7 Aug, OML 28 Apr (before the
first proposal), AUC 14 Aug, SDF 9 Jun (before the NBIO), MEI 30 Sep, CWY 12 Aug (before the NBIO)
and FPR 31 Jul (before SG Fleet's approach). PPC: A$1.81 (21 Aug) to A$1.70, the close on 9 Jul,
the undisturbed date Peet's own presentation uses, before the first approach on 10 Jul. AX1 has no
break price (an unconditional on-market bid). From the independent review of 1 Nov, finding 4.
