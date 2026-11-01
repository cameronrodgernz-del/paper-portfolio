# Proposal: a sector judgement allowance (for Cam to decide; not in the rulebook yet)

The history tests can only test what has a long, dated record. Cam's knowledge of gaming, wagering,
racing and sports media is an edge no such record holds. This allowance lets that knowledge trade in
the practice run under limits, and judges it on how accurate the stated odds turn out to be.

## The rules, as proposed
- Size: at most 5% of the portfolio in all, at most 3 positions, at most 2% in any one.
- Where: NZX and ASX companies in gaming, wagering, racing, lotteries, sports media and their
  technology suppliers (for example SkyCity, Tabcorp, The Lottery Corporation, Aristocrat, Light & Wonder,
  BetMakers, PointsBet, Racing and Sports, Sky TV).
- Off limits: any company Evergreen advises, has pitched or is pitching, or about which Cam holds
  information that isn't public. Trading on that would be insider trading in real life, and a
  simulation built on it would teach the wrong lesson. Cam keeps the list in config/judgement_excluded.csv
  and the desk checks it before any card.
- Each call is a card like any other: the event Cam expects and the date by which it resolves (a sale
  process ending in a bid, a regulatory decision, a contract win), the chance he gives each outcome and
  the price each outcome leads to, and why, in his words. The desk adds the market's price and the
  risk check; decide.py places it under the usual limits.
- Judged on two things across the practice run: the Brier score of Cam's stated chances against the
  outcomes (lower is better, against a coin-toss score of 0.25), and the money result against the
  market. With few calls neither is proof; the test is whether the chances were honest and roughly right.
- At the 18 December readiness review, Cam decides whether it carries into the counted run, on the
  practice record.

## What it would need from Cam
- The excluded list, first.
- A short call when he sees one: the event, the date, the chances and the reason. The desk does the rest.
