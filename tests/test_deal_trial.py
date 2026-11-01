"""Checks for the deal size trial (src/deal_trial.py) on made-up prices and deals.
Usage: python3 -I tests/test_deal_trial.py
"""
import csv
import os
import shutil
import sys
import tempfile
from datetime import date, datetime, timedelta, timezone

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
import deal_trial as T  # noqa: E402


class FakeRates:
    def three_month(self, ccy, d):
        return 0.04


def days(a, b):
    d = date.fromisoformat(a)
    while d <= date.fromisoformat(b):
        if d.weekday() < 5:
            yield d.isoformat()
        d += timedelta(days=1)


def write(path, header, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(header); w.writerows(rows)


def setup(root):
    H = ["date", "open", "high", "low", "close", "volume", "adj_close", "dividend", "split", "source"]
    rows = []
    for d in days("2026-09-01", "2026-12-31"):
        px = 0.95 if d < "2026-11-20" else 0.93
        rows.append([d, px, px + 0.01, px - 0.01, px, 5_000_000, px, "", "", "t"])
    write(f"{root}/data/prices/ASX/TGT.csv", H, rows)
    rows = []
    for d in days("2026-09-01", "2026-12-31"):
        px = 2.0 if d <= "2026-11-10" else 1.6
        rows.append([d, px, px + 0.02, px - 0.02, px, 3_000_000, px, "", "", "t"])
    write(f"{root}/data/prices/ASX/BRK.csv", H, rows)
    rows = [[d, 0.5, 0.5, 0.5, 0.5, 2_000_000 if d < "2026-10-30" else 0, 0.5, "", "", "t"] for d in days("2026-09-01", "2026-12-31")]
    write(f"{root}/data/prices/ASX/THN.csv", H, rows)
    write(f"{root}/data/fx/fx_daily.csv", ["date", "nzd_usd", "nzd_aud"],
          [[datetime.fromisoformat(d).strftime("%d-%b-%Y"), 0.58, 0.90] for d in days("2026-09-01", "2026-12-31")])
    live_h = ["deal_id", "target_market", "target_ticker", "structure", "cash_per_share", "cash_ccy", "scrip_ratio", "acquirer_market",
              "acquirer_ticker", "undisturbed", "announce_date", "expected_payment", "terms_note", "stage"]
    write(f"{root}/config/live_deals.csv", live_h, [
        ["AU-1", "ASX", "TGT", "scheme", "1.00", "AUD", "0", "", "", "0.70", "2026-10-01", "2026-12-15", "", "booklet_out"],
        ["AU-2", "ASX", "BRK", "scheme", "2.20", "AUD", "0", "", "", "1.60", "2026-10-01", "2027-01-31", "", "announced"],
        ["AU-3", "ASX", "THN", "scheme", "0.55", "AUD", "0", "", "", "0.40", "2026-10-01", "2027-01-31", "", "announced"],
        ["AU-4", "ASX", "TGT", "scheme", "0.951", "AUD", "0", "", "", "0.70", "2026-10-01", "2027-06-30", "", "announced"]])
    write(f"{root}/deals/all_deals.csv", ["deal_id", "outcome", "outcome_date", "implementation_date", "related_deal_ids", "offer_price_final"],
          [["AU-1", "pending", "", "", "", ""], ["AU-2", "pending", "", "", "", ""], ["AU-3", "pending", "", "", "", ""], ["AU-4", "pending", "", "", "", ""]])


def monitor(root, d):
    h = ["deal_id", "price", "offer_value", "break_price", "base_rate", "as_of"]
    write(f"{root}/reports/deal_monitor.csv", h, [["AU-1", 0.95, 1.00, 0.70, 0.95, d], ["AU-2", 2.0, 2.2, 1.6, 0.85, d],
                                                  ["AU-3", 0.5, 0.55, 0.40, 0.9, d], ["AU-4", 0.95, 0.951, 0.70, 0.95, d]])


def night(root, d, divs=None):
    now = datetime.fromisoformat(d + "T08:00:00+00:00")
    tr = T.Trial(root, d, now, rates=FakeRates(), dividends=divs or (lambda t, s: [{"ex": "2026-11-20", "per_share": 0.02}] if t == "TGT" else []))
    tr.run()
    return tr


def main():
    root = tempfile.mkdtemp()
    try:
        setup(root)
        monitor(root, "2026-11-02")
        tr = night(root, "2026-11-02")
        P = tr.st["positions"]
        assert set(P) == {"AU-1", "AU-2", "AU-3"}, P.keys()                 # AU-4: a 0.1% spread doesn't beat cash
        assert "AU-4" in tr.st["watch"]
        assert P["AU-1"]["books"]["large"]["qty_ordered"] == int(10000 / 0.95)
        assert P["AU-1"]["books"]["small"]["qty_ordered"] == int(3000 / 0.95)
        assert P["AU-1"]["status"] == "ordered" and not P["AU-1"]["books"]["large"]["fills"]   # nothing fills on the decision night
        # next night: fills at the 3 Nov open (volume is large, so in one go)
        night(root, "2026-11-03")
        tr = night(root, "2026-11-04")
        P = tr.st["positions"]
        f = P["AU-1"]["books"]["large"]["fills"]
        assert f and f[0]["date"] == "2026-11-03" and f[0]["price"] > 0.95 and f[0]["fee"] == 15.0, f
        assert P["AU-1"]["books"]["small"]["fills"][0]["fee"] == 15.0
        assert P["AU-1"]["status"] == "open"
        # the thin share stopped trading: its order lapses after 10 business days with nothing filled
        for d in days("2026-11-05", "2026-11-17"):
            tr = night(root, d)
        assert tr.st["positions"]["AU-3"]["status"] == "lapsed", tr.st["positions"]["AU-3"]["status"]
        # the BRK deal breaks on 10 Nov: sold from the next session
        write(f"{root}/deals/all_deals.csv", ["deal_id", "outcome", "outcome_date", "implementation_date", "related_deal_ids", "offer_price_final"],
              [["AU-1", "pending", "", "", "", ""], ["AU-2", "terminated", "2026-11-10", "", "", ""], ["AU-3", "pending", "", "", "", ""],
               ["AU-4", "pending", "", "", "", ""]])
        for d in days("2026-11-18", "2026-11-20"):
            tr = night(root, d)
        b = tr.st["positions"]["AU-2"]["books"]["large"]
        assert b["exit"] and b["exit"]["how"] == "sold after the deal broke" and b["sells"][0]["date"] == "2026-11-11", b
        r = tr.result(tr.st["positions"]["AU-2"], b)
        assert r["pct"] < -0.15, r                                     # 2.0 down to 1.6, less costs
        # the dividend goes ex on 20 Nov: credited to the shares held before it
        tr = night(root, "2026-11-23")
        assert tr.st["positions"]["AU-1"]["books"]["large"]["divs"][0]["amount"] == round(int(10000 / 0.95) * 0.02, 2)
        # AU-1 completes on 15 Dec: paid A$1.00 a share, no brokerage
        write(f"{root}/deals/all_deals.csv", ["deal_id", "outcome", "outcome_date", "implementation_date", "related_deal_ids", "offer_price_final"],
              [["AU-1", "completed", "2026-12-15", "2026-12-15", "", "1.00"], ["AU-2", "terminated", "2026-11-10", "", "", ""],
               ["AU-3", "pending", "", "", "", ""], ["AU-4", "pending", "", "", "", ""]])
        tr = night(root, "2026-12-16")
        pos = tr.st["positions"]["AU-1"]
        assert pos["status"] == "closed"
        lg, sm = tr.result(pos, pos["books"]["large"]), tr.result(pos, pos["books"]["small"])
        assert lg["value"] == round(int(10000 / 0.95) * 1.00, 2) + round(int(10000 / 0.95) * 0.02, 2), lg
        assert lg["pct"] > sm["pct"], (lg, sm)                       # the same deal, less brokerage per dollar
        assert lg["pct"] > 0
        rep = open(f"{root}/reports/deal_size_trial.md").read()
        assert "Deal size trial" in rep and "AU-1" in rep and "AU-4" in rep
        print("deal trial checks passed")
    finally:
        shutil.rmtree(root)


if __name__ == "__main__":
    main()
