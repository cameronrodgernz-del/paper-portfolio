# Prompt for an independent deep dive on Sports Entertainment Group (ASX:SEG)

Written 2026-11-10 for a second model, at Cam's request. We have no deep dive of our own on SEG yet. The other model works the whole case from the filings to its own verdict. Best run with deep research switched on. Cam pastes everything below the line. The answer is saved as research/against/SEG_deepdive.md, with this prompt at the top, and Claude gives its view on each point before anything is decided.

For us, not in the prompt:
- **Where it came from.** SEG was on the 8 November ranking (reports/research_rank.csv): A$84m, "profit more than halved last year", "a share raising in the last six months". The profit fall is the capital gains tax on the Perth Wildcats sale; normalised NPAT rose.
- **What's changed.** On 1 October 2026 SEG completed a NZ$130m debt-funded purchase of MediaWorks, which roughly doubles the business. The shares now trade below the A$0.28 placement price.
- **Liquidity.** The 20-session median to 30 October was about A$12,000 a day. Five sessions at 10% is about A$6,100, so a A$2,250 position passes, but the 2026 median is only about A$4,800 a day.
- **Excluded list.** SEG bought RWWA's racing audio assets in October 2025 and produces TV for racing and sporting bodies (HRV is named in its FY26 results). RWWA and HRV are Evergreen clients. config/judgement_excluded.csv is empty (Cam, 8 November). Cam to confirm he holds nothing about SEG that isn't public.
- **Lessons built in from the GDI and Mader runs.**
  - Both outside reports kept a deep "worse" case outside the rule tests. This prompt asks for three outcomes, with any worse case folded into the bad one.
  - Our Mader card counted net cash twice. This prompt asks for valuation on enterprise value, less net debt.
  - The Mader report put a different chance on falling profit in its text than in its outcomes. This prompt asks for the two to match.

---

I'd like a deep dive on Sports Entertainment Group Limited (ASX: SEG), done to the standard of a professional analyst who goes well past the news. That means the company's filings and the notes to its accounts, the MediaWorks acquisition documents, substantial holder and directors' interest notices, and published industry data. I want your own view, worked from the evidence. Others will look at SEG separately. Your answer will be checked point by point, so be specific, show your working and source every fact.

## The setting

- Today is 10 November 2026. SEG last traded at A$0.25 (bid A$0.235, ask A$0.25). There are about 336.9 million shares on issue, a market value of about A$84m. Over the past year the shares have traded between about A$0.19 and A$0.38. Trading is thin: a median of roughly A$12,000 a day over the last 20 sessions.
- What SEG is:
  - SEN sports radio and digital in Australia, including SEN Track racing radio and racing audio assets bought from Racing Victoria (RSN) and RWWA in 2025;
  - TV production (Rainmaker);
  - events, hospitality and talent management;
  - three women's sports teams (Bendigo Spirit, Perth Lynx and Melbourne Mavericks).

  It sold its last Perth Wildcats shares in January 2026.
- On 1 October 2026 SEG completed the purchase of MediaWorks, New Zealand's largest commercial radio business (with the rova digital audio app), for an enterprise value of NZ$130m (about A$107m), from Quadrant Private Equity and others.
  - Funding: a new CBA debt facility (a term loan plus a A$31m bridge repayable within 90 days of completion), about A$15m of new shares at A$0.28 (a placement in August and October, and a share purchase plan that raised about A$0.33m of a A$2m target), and existing cash.
  - The company says net debt was about A$79m on 1 October.
  - It says combined last-12-months EBITDA to September 2026 was about A$37.9m before A$5m of targeted savings, pre-AASB 16.
  - It also says MediaWorks has NZ$50m of tax losses.
- FY26 (year to June 2026), from the company:
  - revenue A$152.9m;
  - underlying EBITDA (pre-AASB 16) A$18.2m;
  - profit before tax A$8.6m;
  - a tax charge of A$7.1m, much of it on the Wildcats sale;
  - "normalised" net profit A$6.6m.

  Dividends are paused to pay down debt.
- Substantial holders include, by recent notices:
  - Viburnum Funds (about 15%);
  - Craig Hutchison, the co-founder and chief executive (about 15.5%);
  - Oceania Capital Partners (about 10.5%);
  - the Rothfield family's Chase Properties (about 8%);
  - Ron Hall's Rosh Hagiborim (about 6%).

  The register had 874 holders in August 2026.
- The AGM is on 25 November 2026. The half-year result to December 2026, the first with MediaWorks and its strongest quarter (October to December), is due about mid-to-late February 2027.
- This is for a simulated portfolio. The position would be small (about A$2,250), held for up to about three years, and judged on what it's worth on 31 August 2028, counting any dividends received by then.
- Allow about 5% for costs in total: brokerage both ways on a small order, a bid-ask spread of one to three half-cent ticks on a 25-cent share, and a currency fee.
- The portfolio only buys if all three of these hold:
  1. the bad case is no more than 30% below today's price;
  2. the middling case is above today's price by at least 1.5 times the bad case's fall, and never by less than 15%;
  3. the expected gain after costs, weighting each outcome by its chance, is at least about 12.9% over the period to 31 August 2028.

  A "special situation" (for example a holder building toward a bid, or a sale of the company or its assets) skips the first two rules but must still pass the third, with its bad case set at the value if nothing happens.

Please check every number above against the filings and correct any that are wrong.

## What I need answered

### 1. What the price assumes
Work out SEG's enterprise value today: market value plus net debt, saying whether you include leases. Then the multiples it implies on:
- the last 12 months' EBITDA, before and after the targeted savings;
- EBIT;
- free cash flow to shareholders after interest, lease payments, capital spending, tax (allowing for the NZ tax losses, if they can be used) and the required debt repayments.

Show the arithmetic, per share. Compare with listed radio and media peers on the same basis at current prices: at least Southern Cross Media (ASX: SXL), ARN Media (ASX: A1N) and NZME (NZX/ASX: NZM), plus any recent radio or audio takeovers in Australia or New Zealand and the prices paid.

### 2. MediaWorks
- What exactly was bought: the stations, rova, transmission sites, any outdoor or other assets, and the licences, with their terms and renewal dates.
- Its owners and the prices paid for it since 2015, including Quadrant's purchase. Why would a private equity seller accept about 5 times this year's budgeted EBITDA?
- Its earnings record. The company gives EBITDA of NZ$12.4m (2024), NZ$19.9m (2025) and a 2026 budget of NZ$25.4m, all unaudited and pre-IFRS 16.
  - How much of the rise is revenue and how much cost cutting?
  - What one-off items are in it?
  - What capital spending and lease payments sit below EBITDA?
  - Is the budget being met? The company gave last-12-months EBITDA of NZ$23.3m to September 2026.
- The New Zealand radio market. Use the Radio Broadcasters Association's revenue figures, GfK audience surveys and NZME's radio segment (its revenue and earnings are published) as a check on MediaWorks' claimed 54% revenue share and 59% audience share. Is the market growing or shrinking, and how fast is audio moving to streaming?
- The NZ$50m of tax losses. Do they survive the change of ownership under New Zealand's shareholder continuity rules and the business continuity test? How much tax could they save, and when?
- The A$5m of targeted savings: what they are, when they arrive, and what they cost to achieve.
- The company says MediaWorks can reach more than NZ$38m of EBITDA by FY30. Assess that path step by step.

### 3. The Australian business
- Each segment's revenue and EBITDA for FY24 to FY26: media, TV production, complementary services and the teams. Separate what repeats from what came from one-off events: the 2026 FIFA World Cup, the Legends Game and the first NFL game in Melbourne. What did the Q1 FY27 update (EBITDA up about 10%) include?
- SEN's audiences (GfK surveys) and its share of sports and racing audio. What the RSN and RWWA racing audio purchases cost, and what they earn.
- Wagering. How much of SEG's revenue comes from wagering companies and racing bodies (advertising, sponsorship and content deals)? Where do the Australian government's proposals to restrict gambling advertising stand today, and what would each version cost SEG?
- The women's teams: what they cost each year and why SEG owns them.

### 4. Debt, cash and dividends
- The CBA facility in full: amounts, interest margin, hedging, covenants, amortisation, maturity, and how the A$31m bridge has been or will be repaid. Is any of the debt in New Zealand dollars, or is it all against the Australian earnings?
- Check the company's path from about 1.9 times net debt to EBITDA down to about 1.2 times within two years. Say what it needs, and whether a dividend can restart before August 2028.
- The capital record: the buy-back from March to June 2026 (how much was bought, and at what prices), then new shares at A$0.28 two months later; the A$19.6m of dividends paid since mid-2024; earlier raisings.

### 5. Management, the register and the record
- Craig Hutchison's holding and pay, the A$580,000 a year SEG pays his company for talent services, and any other related-party dealings. Board independence.
- Each substantial holder: what they've bought and sold since 2024 and at what prices (Viburnum sold in August 2026), what they tend to do, and whether any has a history of seeking control or a sale. Who bought the A$0.28 placement shares?
- How tightly held is the register, and what's the free float? Is SEG in any index?
- SEG's record on buying and selling businesses since the 2018 merger of Pacific Star Network and Crocmedia:
  - the Perth Wildcats, bought and sold;
  - Melbourne United;
  - the New Zealand media business it closed or sold;
  - the publishing write-down in FY25;
  - RSN and the RWWA racing audio assets.

  What did shareholders get from each?
- Could anyone bid for SEG, or for parts of it, and at what price? Consider the consolidation talk among Australian radio owners, and SEG's own small holdings in Southern Cross Media and ARN Media.

### 6. Opportunities the company is counting on
- New Zealand online casino advertising. MediaWorks' acquisition presentation names licensed NZ online casino operators as a new advertising category from early 2027. What does New Zealand's online casino law allow licensed operators to advertise, and from when? What's a reasonable size for that spend, and MediaWorks' likely share of it?
- rova: monthly users (540,000 claimed), revenue (about NZ$19m claimed for 2026), and the target of 800,000 users by FY30.
- Selling sport into New Zealand and selling trans-Tasman advertising: is there evidence that advertisers pay more for combined reach?

### 7. The accounts
- Underlying against statutory profit for FY24 to FY26, and every item the company adds back.
- The tax charge.
- The intangible assets and goodwill (and how the MediaWorks price will be split), the impairment tests and their assumptions.
- Share-based pay, receivables, and contingent consideration.
- The auditor's key audit matters.
- Anything that makes SEG look better or worse than it seems.

## What I want back

1. One paragraph up front: buy, wait or reject at A$0.25, and the main reason.
2. The strongest case for buying and the strongest case against, each in its best honest form. For each argument on one side, say whether the other side answers it.
3. Three outcomes for 31 August 2028 (bad, middling, good): the share price then, plus any dividends received by then.
   - For each, say what has to happen, the value and its chance. The chances should add to 100%.
   - If you think a worse case is needed, fold it into the bad case for the rule tests: the portfolio's cards have only three outcomes, so the bad case is the weighted value of everything below the middling case.
   - Make the chances match what you say elsewhere: if you put a chance on profit falling, the outcomes in which it falls should carry that chance.
   - Value on enterprise value: apply a multiple of EBITDA, EBIT or free cash flow to the business, then subtract the net debt you expect at the time. Don't apply a multiple of market value and then add or subtract cash or debt again.
   - Show the expected gain after costs, and say plainly whether SEG passes each of the three rules at A$0.25, both as an ordinary pick and as a special situation.
4. The highest price at which you'd buy, and the events that would change your mind either way, with the dates they're due. For example: the AGM on 25 November 2026, the bridge repayment, the February 2027 half-year result, Australian gambling advertising decisions, the start of NZ online casino licensing, and substantial holder notices.
5. A list of every source, with links. Use primary sources wherever you can:
   - SEG's ASX announcements (asx.com.au and announcements.asx.com.au), including the 12 and 14 August 2026 acquisition announcement and investor presentation and the 1 October 2026 completion announcement;
   - the NZ Companies Office;
   - peers' filings;
   - the Radio Broadcasters Association, Commercial Radio & Audio and GfK;
   - government and regulator documents.

   Use broker notes and press only as pointers, and say when you have. Mark anything you couldn't verify.

Some ground rules:
- Be fair. If one side's case is thin, say so.
- Show the working for every figure you calculate.
- Write in plain English, and explain any media or finance term the first time you use it. Use Australian dollars unless you say otherwise, and give the exchange rate you use for New Zealand figures.
- Aim for about 3,500 words, plus tables and the sources list.
