# Research picks: one company at a time

From 9 November 2026 (rulebook section 5a). This replaces the funnel of 2 November and the red team review.

## The steps
1. Choose. Claude proposes the next company, usually from reports/research_candidates.md (the weekly sweep),
   and agrees it with Cam in chat. One company is worked at a time.
2. The angle (added 9 Nov 2026, before any deep dive). Write three lines: what the market believes, in a sentence
   (from the price, the company's own story and broker targets); the one fact that would show it's wrong; and how we'll
   get that fact from outside the company's filings, which everyone covering it reads. Ways to get it: competitors',
   suppliers' and customers' own filings read across; government and industry data; prices, stock and job ads tracked
   over time on websites; and people Cam can ask (customers, staff, suppliers). If there's no way to test the fact
   other than the filings, the company only goes ahead if it's small and uncovered enough that a careful read of the
   filings is itself the edge.
3. The case for buying. Claude writes the deep dive in research/picks/<TICKER>.md (NZ_<TICKER>.md for NZX) in
   the format of research/picks/TEMPLATE.md, from primary sources only. It starts from what today's price
   assumes, then states in one sentence the thing the market is missing, with the evidence. If that sentence
   can't be written, the company is a reject and the work stops there.
4. The case against. Claude writes a prompt for a second model (Cam runs it, for example in ChatGPT), giving the
   company, the date and the price, the rulebook's value test and what a good case against looks like, but not
   the deep dive. Its answer is saved as research/against/<TICKER>.md, with the prompt at the top.
5. The debate. Each side answers the other's strongest points, in rounds, until nothing new comes up: Claude
   answers the case against, the second model answers the deep dive (Cam passes the files across), and so on.
   It's saved as research/debate/<TICKER>.md, with a short summary at the top of where the two still disagree
   and what evidence would settle it.
6. Cam's decision. The debate file ends with a section headed "## Cam's decision", whose first line is one of:
   "Buy, <date>: <his reason>", "Wait for <a named event or a price>", or "No". Only a buy becomes a card.
7. The card. research/cards/<TICKER>.json, checked with python3 -I src/decide.py practice <card> --dry-run and
   placed by the evening desk:
   {"sleeve": "research", "market": "ASX" or "NZX", "ticker": ..., "company": ..., "side": "buy",
    "kind": "value" or "special", "thesis": "...", "outcomes": [[chance, price] for bad, middling, good],
    "resolve_by": "YYYY-MM-DD" (at most 36 months out), "exit_rule": "what would show the reason for buying is
    wrong", "industry": "...", "deep_dive": "research/picks/<TICKER>.md",
    "case_against": "research/against/<TICKER>.md", "debate": "research/debate/<TICKER>.md",
    "catalysts": [optional dated events], "source": "desk" or "cam", "status": "ready", "price_at_writing": ...}

## The tests a card must pass (src/decide.py)
- The deep dive, the case against, and the debate ending in Cam's decision to buy.
- Three outcomes, each with a chance and a price by the resolve date, dividends counted as rulebook section 5a sets
  out.
- The value test (not for special situations): the bad case no more than 30% below the price, and the middling
  case above it by at least 1.5 times the bad case's fall, never less than 15%.
- An expected gain after costs of at least the cash rate plus 5% a year over the holding period.
- An exit rule. Held picks are sold on it, at the resolve date, or when Cam decides, not on the portfolio's fall
  from peak. A close 25% or more below the buy price means a review and a message to Cam, not a sale.
- The usual limits: 2.5% of the portfolio, five companies, 15% in one industry outside the core, and five
  sessions' trading at 10% of volume.
