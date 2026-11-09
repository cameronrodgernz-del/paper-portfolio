# The case against Nuix (ASX:NXL), from a second model

Run by Cam in ChatGPT on 9 November 2026, from the prompt filed on the same day (research/against/NXL_prompt.md). Saved as received, with the prompt at the top (docs/RESEARCH_PROCESS.md step 4). The model didn't see the case for (research/picks/NXL.md). Its PDF (linked in the answer) sits in Cam's ChatGPT library and isn't in this repo; the text below is the full answer as pasted. Claude's reply is in research/debate/NXL.md. This is a simulation and not financial advice.

## The prompt

I'd like you to write the strongest honest case against buying shares in Nuix Limited (ASX: NXL) today, as an independent analyst. Another analyst has written the case for buying. You haven't seen it, and that's deliberate: I want your own view, worked from the evidence. Afterwards the two cases will be put side by side and argued out, so be specific enough that each of your points can be checked.

The setting:
- Today is 9 November 2026. Nuix last traded at A$1.925, with about 343.5 million shares on issue, a market value of about A$661m. It reported net cash of A$49.9m at 30 June 2026.
- It's for a simulated portfolio. The position would be small (about A$2,250), bought to hold for up to three years, and judged on what it's worth by 31 August 2028, after the FY28 result.
- The portfolio's rules only allow a buy if all of these hold:
  - the bad case is no more than 30% below today's price;
  - the middling case is above today's price by at least 1.5 times the bad case's fall, and never by less than 15%;
  - the expected gain after costs beats about 12.9% over the period (the cash rate plus 5% a year).

What I need from you:
1. What today's price assumes about Nuix's future. Work it out from the price, the cash and the company's own figures and FY27 guidance, and show the arithmetic.
2. The strongest reasons not to buy at A$1.925. Look for reasons growth may stall, may be weaker than it looks, or is already fully in the price. Cover:
   - how much of the growth in Nuix Neo is old customers moving across rather than new money, and what happens when that move is finished;
   - competition and the effect of AI on eDiscovery and investigations software;
   - the shareholder class action over the 2020 float (tried in the Supreme Court of Victoria from August 2026, judgment reserved) and ASIC's appeal;
   - Macquarie's stake of about 28%;
   - management's record on forecasts;
   - anything in the accounts, such as capitalised development, revenue from multi-year deals booked early, or share-based pay, that makes the business look better than it is.

   Weigh the obvious arguments for buying, such as net cash, the low multiple of revenue and the growth in Nuix Neo, and say why they're weaker than they look, where they are.
3. Your bad, middling and good outcomes for the share price by 31 August 2028, including any dividends paid before then. Give each a chance (they should add to 100%), and say what has to happen in each. Then say plainly whether Nuix passes the three rules above at A$1.925.
4. The price, or the event, that would change your mind.
5. Every fact with its source and link.

Some ground rules:
- Use primary sources wherever you can:
  - Nuix's ASX announcements, annual and half-year reports and results presentations (all at asx.com.au and announcements.asx.com.au);
  - the court records (the Federal Court's judgment in ASIC v Nuix [2026] FCA 490, and the Supreme Court of Victoria's group proceeding page);
  - the substantial holder notices;
  - competitors' filings, such as Cellebrite's.

  Use broker notes and press only as pointers, and say when you have.
- Be fair. If the case against turns out to be weak at this price, say so. I'd rather have an honest "the bear case is thin" than a one-sided brief.
- Write in plain English, with figures in Australian dollars. Keep it to about 2,000 words, plus a sources list.

## The answer

**I would not buy Nuix at A$1.925 under these portfolio rules.** The plausible downside exceeds 30%, while my middling outcome provides too little upside to compensate.

The valuation-only bear case is fairly thin: Nuix generates cash and trades at a moderate operating earnings multiple. The stronger objection is the combination of uncertain growth quality, legal exposure and your fixed August 2028 assessment date. My expected return narrowly passes the hurdle, but the other two rules fail.

[Nuix_Independent_Bear_Case_09Nov2026.pdf](https://chatgpt.com/library?file_id=libfile_f7d05af710cc8191a5979c9e2d90290e&account_id=personal)

All figures below are Australian dollars. Entry price, current share count and portfolio hurdle are your supplied assumptions. Forecasts, probabilities, multiples and transaction costs are my estimates.

**Today’s price requires continued earnings, rather than exceptional growth.** FY26 revenue was $263.2m, annualised contract value, or ACV, $260m, and Adjusted Management EBITDA $59.8m. FY27 guidance is ACV of $285m–$300m, with adjusted EBITDA similar to FY26 after a $15m R&D accelerator. That implies 9.6%–15.4% contract-value growth but broadly flat adjusted earnings. [announcements.asx.com.au](https://announcements.asx.com.au/asxpdf/20260824/pdf/073323hc3yb1pg.pdf?utm_source=chatgpt.com)

| Calculation at entry | Result |
|---|---:|
| Equity value: $1.925 × 343.5m shares | $661.2m |
| Enterprise value before leases: $661.2m − $49.9m | $611.3m |
| Enterprise value including $20.6m lease liabilities | $631.9m |
| EV / FY26 revenue | 2.40× |
| EV / FY26 adjusted EBITDA | 10.6× |

I include lease liabilities because EBITDA excludes lease depreciation and interest. The liability comes from the financial statements. [announcements.asx.com.au](https://announcements.asx.com.au/asxpdf/20260824/pdf/073321brtgqmph.pdf?utm_source=chatgpt.com)

Assuming a FY28 multiple of 10×, 355m diluted shares and $80m net cash after lease debt:

- Maintaining today’s price requires EBITDA of **($1.925 × 355m − $80m) / 10 = $60.3m**.
- Clearing your 12.9% hurdle, after assumed costs of 0.5% each way, requires a **$2.195 exit price and $69.9m EBITDA**.
- At an 8× multiple, the required EBITDA becomes **$87.4m**.

These are sensitivities, not uniquely implied market forecasts. The risk is that earnings grow but the multiple falls.

**Neo’s growth overstates how quickly the whole business is expanding.** Nuix identifies migration as its largest growth contributor, with typical customer spending uplifts of 30%–50%. A customer moving from $1m of legacy software to $1.4m of Neo adds $1.4m to Neo but only $0.4m to Nuix. [announcements.asx.com.au](https://announcements.asx.com.au/asxpdf/20260824/pdf/073325n21jp1yt.pdf?utm_source=chatgpt.com)

The FY26 ACV bridge is revealing:

| Movement | ACV change |
|---|---:|
| Neo | +$50.4m |
| Components | −$28.2m |
| Discover | −$2.7m |
| Other | +$0.2m |
| Acquired Linkurious | +$12.0m |
| Group, subject to rounding | **+$31.6m** |

Excluding Linkurious, growth was $19.6m, or 8.6%; at constant currency it was 11.1%. [announcements.asx.com.au](https://announcements.asx.com.au/asxpdf/20260824/pdf/073325n21jp1yt.pdf?utm_source=chatgpt.com)

The component decline offsets 56% of Neo’s increase. **That is not a measured migration percentage:** it also includes downsells and competitive losses. Nuix does not disclose a complete dollar split between transferred spending, migration uplifts, new customers and other upsells. Neo’s 179% growth therefore cannot establish the underlying customer acquisition rate. [announcements.asx.com.au](https://announcements.asx.com.au/asxpdf/20260824/pdf/073325n21jp1yt.pdf?utm_source=chatgpt.com)

When migration finishes, customers cannot buy the initial upgrade again. Growth must come from usage, modules, pricing and new accounts. However, the programme extends to FY30, so predicting a migration cliff before FY28 would be unfair. [announcements.asx.com.au](https://announcements.asx.com.au/asxpdf/20260824/pdf/073325n21jp1yt.pdf?utm_source=chatgpt.com) My nearer concern is that easier upgrades happen first, leaving later conversions requiring more selling effort or discounts. That is an inference.

**AI gives competitors the same opening.** Relativity made aiR Assist and custom document analyses standard elements of RelativityOne in June 2026. [Newsroom](https://relativity.com/news-events/relativity-expands-ai-platform-for-legal-data-intelligence-with-conversational-ai-and-no-code-custom-document-analyses/?utm_source=chatgpt.com) Summarisation, classification and document interrogation could become expected features, reducing the premium Nuix can charge. Faster review might reduce seat requirements, although increased data processing could offset this.

Adjacent competitor Cellebrite reported 21% ARR growth, 117% net retention and initial Genesis AI monetisation in Q2 2026. Yet it cut its outlook because sales cycles lengthened and migrations delivered less expansion than expected. [sec.gov](https://www.sec.gov/Archives/edgar/data/1854587/000121390026088681/ea030188001ex99-1.htm?utm_source=chatgpt.com) Its products and metrics differ from Nuix’s, but this demonstrates that strong demand and migration narratives can still disappoint commercially.

Nuix disclosed competitive displacement and pricing pressure in 1H26. Its full-year net dollar retention was 105.2%, against 107.4% in FY25: existing customers grew spending modestly despite platform upgrades. [nuix.com](https://www.nuix.com/sites/default/files/2026-02/1H26%20Investor%20Presentation.pdf?utm_source=chatgpt.com)

Conversely, auditable processing of difficult data remains useful even if AI models become interchangeable. I would question whether continual AI investment earns additional revenue or merely preserves competitiveness, rather than assume AI destroys Nuix.

**Litigation prevents confidence in a 30% downside boundary.** The shareholder proceeding concerns alleged prospectus and disclosure failures. The Supreme Court records the trial commencing on 3 August 2026; it concluded in September with judgment reserved. These remain allegations, not established misconduct. [The Supreme Court of Victoria](https://www.supremecourt.vic.gov.au/areas/group-proceedings/nuix?utm_source=chatgpt.com)

The strongest contrary evidence matters: Goodman J dismissed ASIC’s entire case on 23 April 2026, including the directors’ case, and ordered costs against ASIC. ASIC’s appeal concerns Nuix only and challenges findings about forecasts, materiality and disclosure. [download.asic.gov.au](https://download.asic.gov.au/media/q25d5iw0/26-080mr-asic-v-nuix-limited_2026-fca-490.pdf?utm_source=chatgpt.com) The ASIC victory improves Nuix’s position, but the shareholder proceeding has different claims and proof requirements.

The accounts disclose the shareholder claim and ASIC appeal without damages or penalty provisions. They also report a $10m insurance retention, rather than $2.5m, for relevant related claims under each policy following the unsuccessful insurance appeal. The $28.7m undrawn facility cannot fund litigation costs. [announcements.asx.com.au](https://announcements.asx.com.au/asxpdf/20260824/pdf/073321brtgqmph.pdf?utm_source=chatgpt.com)

Neither no provision nor insurance establishes a reliable maximum loss. Every hypothetical $50m net uninsured payment removes approximately **14.1 cents per diluted share**, before any valuation reduction. I do not claim to know eventual damages or insurance recoveries.

**Macquarie is neither an evidenced imminent seller nor a guaranteed backstop.** Its April notice separates 95.65m strategic shares from smaller managed holdings. Nuix’s October annual report says the strategic holding has remained unchanged since the IPO. That represents about 27.85% using your current share count. [newsfile.moomoo.com](https://newsfile.moomoo.com/public/NN-PersistNoticeAttachment/7781/20260413/ASX-FTP-2A1666185.PDF?utm_source=chatgpt.com) [Annual report, note 9.5](https://announcements.asx.com.au/asxpdf/20261006/pdf/07503y2vz4v0l2.pdf).

An eventual exit could depress the price, but there is no evidenced sale timetable. More concretely, Nuix recognised another $4.17m of Macquarie legal-fee indemnity claims in FY26. [announcements.asx.com.au](https://announcements.asx.com.au/asxpdf/20260824/pdf/073321brtgqmph.pdf?utm_source=chatgpt.com) I attach no takeover premium or assumed financial rescue to the relationship.

**Forecast reliability warrants a discount, with credit for improvement.** Nuix withdrew its 11%–16% constant-currency FY25 ACV growth expectation in May 2025; actual growth was 6.9%. [openbriefing.com](https://openbriefing.com/AsxDownload.aspx?pdfUrl=Report%2FComNews%2F20250506%2F02943987.pdf\&utm_source=chatgpt.com)

John Ruthven became interim CEO in November 2025 and permanent CEO in May 2026, so attributing that miss to him would be unfair. FY26 ACV met guidance. [announcements.asx.com.au](https://announcements.asx.com.au/asxpdf/20260504/pdf/06z6073fnr48vx.pdf?utm_source=chatgpt.com) The continuing concern is dependence on large contract timing. A delayed deal could materially affect the FY28 result on which your position will be judged.

**The accounts favour checking cash and ACV alongside earnings.** Longer non-cancellable licence terms can increase upfront revenue; Nuix explicitly identifies judgement in determining those terms. [nuix.com](https://www.nuix.com/sites/default/files/2026-02/Annual%20Financial%20Report.pdf?utm_source=chatgpt.com) Multi-year deals increased from 27% to 35% of revenue. [announcements.asx.com.au](https://announcements.asx.com.au/asxpdf/20260824/pdf/073323hc3yb1pg.pdf?utm_source=chatgpt.com)

That implies approximately $59.8m rising to $92.1m, a $32.3m increase against $41.7m total revenue growth. This helps explain why reported revenue grew faster than underlying contract value. It does **not** establish that all $32.3m was brought forward or that accounting was improper.

Contract assets rose from $50.9m to $75m. Capitalised development was $23.4m; operating cash flow included a $6.35m share-pay add-back. [announcements.asx.com.au](https://announcements.asx.com.au/asxpdf/20260824/pdf/073321brtgqmph.pdf?utm_source=chatgpt.com) Crucially, **Adjusted Management EBITDA already charges full development spending and share-based pay**. Subtracting either again would exaggerate the bear case. [announcements.asx.com.au](https://announcements.asx.com.au/asxpdf/20260824/pdf/073323hc3yb1pg.pdf?utm_source=chatgpt.com) Dilution still matters, hence my 355m terminal share assumption.

Adjusted EBITDA excludes $13m legal expense. My stricter FY26 cash calculation is:

**$60.7m operating cash − $21.2m development − $2.2m other capital spending − $3.9m lease principal − $1.4m interest ≈ $32m.** [announcements.asx.com.au](https://announcements.asx.com.au/asxpdf/20260824/pdf/073321brtgqmph.pdf?utm_source=chatgpt.com)

That is a **4.8% equity cash yield**. June net cash of $49.9m equates to only 14.5 cents per current share. It provides resilience, not a floor near $1.925.

**My outcomes at 31 August 2028** use FY28 earnings. Probabilities represent joint business and legal scenarios, not estimates of losing either court case. I assume 355m diluted shares, no acquisitions, no dividends and costs of 0.5% each way.

| FY28 / terminal assumption | Bad: 30% | Middling: 50% | Good: 20% |
|---|---:|---:|---:|
| Revenue | $270m | $325m | $365m |
| Adjusted EBITDA | $45m | $78m | $102m |
| EBITDA margin | 16.7% | 24.0% | 27.9% |
| EV / adjusted EBITDA | 8.0× | 9.5× | 12.0× |
| Net cash after lease debt | $0m | $80m | $110m |
| Equity value | $360m | $821m | $1,334m |
| **Share price** | **$1.014** | **$2.313** | **$3.758** |
| Dividends before assessment | $0 | $0 | $0 |
| **Return before costs** | **−47.3%** | **+20.1%** | **+95.2%** |

Equity value equals EBITDA multiplied by the valuation multiple, plus net cash after lease debt.

- **Bad:** migration slows, competitive losses offset wins, investment persists and legal outcomes consume cash.
- **Middling:** revenue grows approximately 11% annually from FY26, the accelerator ends, margins improve moderately and legal costs remain manageable.
- **Good:** new-customer wins and AI upselling support approximately 18% annual revenue growth, strong margins and favourable legal resolution.

Terminal net cash approximates $49.9m starting cash, plus $45m/$70m/$90m cumulative cash generation, less $75m/$20m/$10m net legal outgoings and $20m remaining lease debt. Cash generation is after tax, development, capital spending, interest and lease payments.

**Legal amounts are stress assumptions, not damages estimates.** Removing the entire $75m bad-case legal payment still produces a $1.225 valuation, 36.3% below entry. Outcomes below my bad-case estimate are also possible.

| Your rule | Test at $1.925 | Verdict |
|---|---|---|
| Bad-case decline no greater than 30% | 47.3% downside | **Fail** |
| Middling gain ≥1.5× downside and ≥15% | 20.1% against 71.0% required | **Fail** |
| Expected gain after costs >12.9% | 13.8% | **Narrow pass** |

Expected terminal value is:

**30% × $1.014 + 50% × $2.313 + 20% × $3.758 = $2.212.**

Using unrounded figures, expected return after costs is:

**($2.212 × 0.995) / ($1.925 × 1.005) − 1 = 13.8%.**

Moving just two probability points from good to bad reduces that to **10.9%**. Small position size limits portfolio damage but does not cure the failed entry rules.

**I would reconsider around $1.40, provided the evidence had not worsened.** On unchanged scenarios, the binding downside ceiling is $1.014 / 0.70 = $1.449, or approximately $1.434 allowing costs. At $1.40, all three tests pass.

Alternatively, favourable final legal resolution plus two reporting periods demonstrating new-customer growth, retention above 110% and cash conversion without increasing multi-year dependence could justify buying nearer today’s price. I would rebuild the downside case and require all three rules to pass.

The primary sources used are listed below. Press and announcement indexes were used only to locate originals; no broker valuation or opposing investment brief was used.

1. [FY26 results release, 24 August 2026](https://announcements.asx.com.au/asxpdf/20260824/pdf/073323hc3yb1pg.pdf): results, guidance and adjustments.
2. [FY26 results presentation](https://announcements.asx.com.au/asxpdf/20260824/pdf/073325n21jp1yt.pdf): ACV bridge, migration and cash.
3. [FY26 financial report](https://announcements.asx.com.au/asxpdf/20260824/pdf/073321brtgqmph.pdf): accounts and notes 9.5, 9.7–9.8.
4. [October 2026 annual report](https://announcements.asx.com.au/asxpdf/20261006/pdf/07503y2vz4v0l2.pdf): trial status and strategic shareholding.
5. [1H26 financial report](https://announcements.asx.com.au/asxpdf/20260223/pdf/06wlk4yt1g0wmc.pdf): revenue judgements, note 1.6.2.
6. [ASIC v Nuix [2026] FCA 490](https://download.asic.gov.au/media/q25d5iw0/26-080mr-asic-v-nuix-limited_2026-fca-490.pdf): original judgment hosted by ASIC.
7. [ASIC notice of appeal](https://download.asic.gov.au/media/gh4bpyb2/26-103mr-asic-v-nuix-notice-of-appeal.pdf).
8. [Supreme Court group proceeding](https://www.supremecourt.vic.gov.au/areas/group-proceedings/nuix) and [plaintiff solicitors’ trial-status update](https://phifinneymcdonald.com/action/nuix-class-action/).
9. [Macquarie substantial holder notice, 13 April 2026](https://announcements.asx.com.au/asxpdf/20260413/pdf/06yfcwct9gskxg.pdf).
10. [Guidance withdrawal, 6 May 2025](https://announcements.asx.com.au/asxpdf/20250506/pdf/06jgq272f649hq.pdf).
11. [FY25 results presentation](https://www.nuix.com/sites/default/files/2025-08/FY25%20Investor%20Presentation.pdf).
12. [CEO appointment, 4 May 2026](https://announcements.asx.com.au/asxpdf/20260504/pdf/06z6073fnr48vx.pdf).
13. [Relativity’s June 2026 AI announcement](https://relativity.com/news-events/relativity-expands-ai-platform-for-legal-data-intelligence-with-conversational-ai-and-no-code-custom-document-analyses/).
14. [Cellebrite Q2 2026 results, SEC filing](https://www.sec.gov/Archives/edgar/data/1854587/000121390026088681/ea030188001ex99-1.htm).
15. [Nuix 1H26 presentation](https://www.nuix.com/sites/default/files/2026-02/1H26%20Investor%20Presentation.pdf).
