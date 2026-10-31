"""Read the deal terms out of a US merger proxy or tender offer response, for the live US leads.

From the filing's text (tags and entities stripped):
- the cash paid per share, preferring the merger agreement's own wording ("converted into the right
  to receive $X in cash", "Merger Consideration of $X", "Offer Price of $X");
- whether any stock is paid too (an exchange ratio, or parent shares per share), which makes it not a
  cash deal;
- a contingent value right (an extra payment that depends on an event);
- the special meeting date, or the date a tender offer expires;
- when the parties expect it to close, as written.
Each lead keeps the sentence the price came from, so the analyst can check it against the filing.
This is separate from the pattern the US deal history test (rulebook 9b) uses, which stays as it was
registered.
"""
import html
import re
from collections import Counter

MONTHS = r"(?:January|February|March|April|May|June|July|August|September|October|November|December)"
MONEY = r"\$\s?(\d{1,4}(?:,\d{3})*\.\d{2})"
STRONG = [re.compile(p, re.I) for p in (
    r"right to receive\s+(?:an amount in cash equal to\s+)?" + MONEY + r"(?:\s+per share)?,?\s+in cash",
    r"(?:Merger|Per Share Merger|Per Share) Consideration[\"”)\s]*(?:\)|of|equal to|means)?\s*" + MONEY,
    r"(?:Offer Price|offer price)[\"”)\s]*(?:\)|of|equal to)?\s*" + MONEY + r"\s+per\s+(?:share|Share)",
    r"(?:at|for)\s+(?:a price of\s+)?" + MONEY + r"\s+per\s+(?:share|Share)[^.]{0,40}?\bin cash",
)]
WEAK = re.compile(MONEY + r"\s+per\s+share(?:,)?\s+in cash", re.I)
# stock in the consideration: looked for in the sentence the cash price came from, so an exchange
# ratio for employee awards elsewhere in the proxy doesn't count
STOCK = re.compile(r"exchange ratio|\d+\.\d+\s+(?:of\s+a\s+)?(?:validly issued\s+)?(?:fully paid\s+)?shares?\s+of|"
                   r"a fraction of a share|shares of (?:Parent|parent)[^.]{0,30}common stock", re.I)
CVR = re.compile(r"contingent value right", re.I)
MEETING = re.compile(r"special meeting[^.]{0,300}?(?:will be held|to be held|is scheduled)[^.]{0,120}?(" + MONTHS + r"\s+\d{1,2},\s+20\d\d)", re.I)
EXPIRY = re.compile(r"(?:offer|Offer)[^.]{0,120}?(?:expire|expiration)[^.]{0,160}?(" + MONTHS + r"\s+\d{1,2},\s+20\d\d)")
CLOSE = re.compile(r"expect(?:s|ed)?\s+(?:that\s+)?(?:the\s+)?(?:merger|transaction|offer|closing)?[^.]{0,60}?(?:to\s+(?:be\s+)?(?:completed|close|consummated)|will\s+(?:be\s+completed|close))"
                   r"[^.]{0,60}?((?:in\s+)?(?:the\s+)?(?:first|second|third|fourth|1st|2nd|3rd|4th)\s+(?:calendar\s+)?(?:quarter|half)\s+of\s+(?:calendar\s+(?:year\s+)?|fiscal\s+(?:year\s+)?)?20\d\d|"
                   r"(?:early|mid|late|end of)[-\s]20\d\d|" + MONTHS + r"\s+20\d\d|(?:by\s+)?the\s+end\s+of\s+(?:calendar\s+)?20\d\d)", re.I)


def clean(raw: str) -> str:
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = html.unescape(t).replace("\xa0", " ")
    return re.sub(r"\s+", " ", t)


def terms(raw: str, limit: int = 1_500_000) -> dict:
    t = clean(raw[:limit])
    found, quote = Counter(), {}
    for p in STRONG:
        for m in p.finditer(t):
            v = m.group(1).replace(",", "")
            found[v] += 3
            quote.setdefault(v, t[max(0, m.start() - 80): m.end() + 40].strip())
    for m in WEAK.finditer(t):
        v = m.group(1).replace(",", "")
        found[v] += 1
        quote.setdefault(v, t[max(0, m.start() - 80): m.end() + 40].strip())
    cash = None
    if found:
        cash, score = found.most_common(1)[0]
        cash = float(cash)
    head = t[:400_000]
    ev = quote.get(f"{cash:.2f}" if cash is not None else "", "")
    sentence = ev
    if ev:
        k = t.find(ev)
        end = t.find(". ", k + len(ev) - 40)
        sentence = t[max(0, k): (end if end > 0 else k + len(ev) + 300)]
    stock = bool(STOCK.search(sentence))
    m1, m2, m3 = MEETING.search(t), EXPIRY.search(t), CLOSE.search(head)
    return {"cash": cash, "evidence": quote.get(f"{cash:.2f}" if cash is not None else "", "")[:260],
            "strength": "strong" if cash is not None and found[f"{cash:.2f}"] >= 3 else ("weak" if cash is not None else ""),
            "stock": stock, "cvr": bool(CVR.search(head)), "meeting": m1.group(1) if m1 else "",
            "expires": m2.group(1) if m2 else "", "expected_close": m3.group(1).strip() if m3 else ""}
