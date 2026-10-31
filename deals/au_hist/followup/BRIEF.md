# Brief: follow-up pass on the Australian deal database, 2015 to 2024

The database is used to set base rates (how often deals complete, how long they take, how often a rival appears) for a simulated merger-arbitrage sleeve. The first pass ran out of web budget, so some deals are missing and some rows are thin. This pass fills gaps. It does not rebuild rows that are already complete.

## Read first
- `/home/claude/paper_portfolio/deals/SCHEMA.md`: columns and rules. Follow them exactly.
- `/home/claude/paper_portfolio/deals/AU_HISTORY_BRIEF.md`: the inclusion rules (ASX-primary targets, binding announcement, A$100m or more, failures included).
- The `NOTES.md` in each folder under `/home/claude/paper_portfolio/deals/au_hist/`: they record which sources worked. Read the "sources that worked" parts before fetching anything.

## Tools and limits (important)
- The shared web-search budget is probably used up. Try WebSearch at most once; if it fails or says a limit is reached, do not use it again. Work by WebFetch on addresses you can build.
- Stay on domains that worked before: financialfilings.com (full text of ASX filings, including delisted companies, at `/companies/<name-ltd or name-limited>/<year>/`; when the bidder is ASX-listed, its page often carries the target's releases), asx.com.au announcement lists (dated titles for codes still listed), aspecthuntley.com.au/asxdata/YYYYMMDD/pdf/<id>.pdf (2015-16 PDFs when the date and document number are known), and law-firm deal reviews (corrs.com.au, gtlaw.com.au, hsf.com, minterellison.com).
- If a fetch hangs waiting for approval, or a domain refuses, move on and note it. Never try to get round a block (no changed user agents, no caches or mirrors of a refused page).
- Leave a field blank rather than guess. A number comes from a filing or a law-firm review that quotes the filing, never from news alone. Put the source address for each filled field in `sources`.
- Work for about two hours of wall-clock time, then stop and report, even if the list is not finished. Save your output files as you go so nothing is lost.

## Output
Write only in your own folder (named in your prompt). Never edit the existing CSVs.
- `patches.csv` with columns `deal_id,field,old_value,new_value,source,note`: one row per field you fill or correct in an existing row.
- `new_rows.csv` with exactly the header of `/home/claude/paper_portfolio/deals/au_hist/2017_2018/au_deals_2017_2018.csv`: one row per newly built deal. Number new deals `AU-<year>-F<nn>` (F for follow-up), starting at F01 for each year.
- `log.md`: what you tried, what worked, what did not, and anything left for a later pass.

## Final message (300 words or fewer)
- How many fields filled, by field, and how many new rows, by year and outcome.
- Which items on your list you could not resolve, and why.
- Anything you found that contradicts an existing row.
