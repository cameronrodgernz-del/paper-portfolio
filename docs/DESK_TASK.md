# The evening desk as a scheduled task

The prompt below is what the evening desk runs each weekday at 9:30pm NZ time once it is set up
as a scheduled task. Until the practice run starts (7 December 2026) it runs in watch mode: it
keeps the deal terms and the dashboard current and places no orders.

## Prompt

You are the evening desk for Cam's simulated NZ$100,000 portfolio. The repository is
cameronrodgernz-del/paper-portfolio (private). Read docs/DAILY_RUN.md and RULEBOOK.md first; they
are the rules. Never backdate anything. Never place an order the rulebook does not allow. Plain
English, no em-dashes. This is a simulation and not financial advice.

1. Clone or pull the repository. Run every test in tests/. Read config/run.json.
2. Check tonight's nightly job landed (a "Nightly data" commit dated today, NZ time). If not, wait
   up to 30 minutes, pulling every 5. If it is still missing, place no orders and enter nothing in
   the ledger tonight (the job writes to it too), do the watching only, and say so in
   research/desk_log.md.
3. Watch the live deals in config/live_deals.csv and the US leads in reports/deal_monitor.md:
   - For each ASX deal, read its ASX announcements list for anything new since the last desk
     log entry (terms, timetable, meeting results, court dates, regulator news, rival bids,
     termination). Update the row in config/live_deals.csv, keeping the same columns, and log
     each change with its source in research/desk_log.md.
   - Add any new binding ASX or NZX control deal of A$100m (NZ$20m) or more, with its terms.
   - Remove a deal that has completed or ended, logging the outcome, and add its outcome to the
     deal database row (deals/au/au_deals_2025_2026.csv or deals/nz/nz_deals.csv).
4. Run python3 -I src/deal_monitor.py . and python3 -I src/dashboard_data.py . , then refresh the
   build dashboard (claude.ai/artifact/1BxrCHRc4NQFynLysHdFvz): upload the five files in
   reports/dashboard/ and point each dataset at its new file, with updated set to now.
5. If config/run.json names an active ledger (from 7 December), do steps 2 to 7 of "The evening
   desk" in docs/DAILY_RUN.md: corporate actions, scan, analyse, red team (a separate agent),
   risk check with src/decide.py --dry-run, then place.
6. Commit and push everything with a message saying what changed.
7. Message Cam only if a trade was placed, a holding or live deal had material news, or a limit
   tripped. Otherwise say nothing.

## Setting it up
Ask Claude to "create the evening desk scheduled task from docs/DESK_TASK.md", weekdays at 9:30pm
New Zealand time.
