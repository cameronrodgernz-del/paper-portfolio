"""Checks for the stage-aware starting odds (src/history/deal_odds.py) and their use in the deal monitor."""
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "src"))
sys.path.insert(0, os.path.join(HERE, "..", "src", "history"))
import deal_monitor as dm  # noqa: E402
import deal_odds as do  # noqa: E402

fails = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail and not ok else ""))
    if not ok:
        fails.append(name)


def row(**k):
    base = {"deal_id": "X", "market": "ASX", "structure": "scheme", "outcome": "completed", "announce_date": "2024-01-01",
            "outcome_date": "2024-05-01", "booklet_date": "", "meeting_date": "", "court_date": "", "failure_reason": "",
            "related_deal_ids": "", "offer_price_final": "1.00", "offer_price_initial": "1.00", "bidder_type": "trade",
            "regulators": "", "board_recommendation": "unanimous_for", "consideration_type": "cash"}
    base.update(k)
    return base


by = {"R1": row(deal_id="R1", outcome="completed", offer_price_final="1.20"),
      "R2": row(deal_id="R2", outcome="terminated"),
      "R3": row(deal_id="R3", outcome="pending"),
      "R4": row(deal_id="R4", outcome="completed", offer_price_final="0.90")}
check("a completed deal paid its holders", do.holder_outcome(row(), by) == 1)
check("a deal topped by a rival that completed higher paid its holders",
      do.holder_outcome(row(outcome="superseded_by_rival", related_deal_ids="R1"), by) == 1)
check("a deal topped by a rival that then failed didn't", do.holder_outcome(row(outcome="superseded_by_rival", related_deal_ids="R2"), by) == 0)
check("a rival still live leaves the deal unresolved", do.holder_outcome(row(outcome="superseded_by_rival", related_deal_ids="R3"), by) is None)
check("a rival that completed lower than the offer is a loss", do.holder_outcome(row(outcome="superseded_by_rival", related_deal_ids="R4"), by) == 0)
check("a terminated deal didn't pay", do.holder_outcome(row(outcome="terminated"), by) == 0)
check("a pending deal is unresolved", do.holder_outcome(row(outcome="pending"), by) is None)
check("a scheme voted down reached the booklet but not a passed vote",
      do.reached(row(outcome="terminated", failure_reason="vote: 60%", booklet_date="2024-02-01", meeting_date="2024-03-01"), "booklet_out") is True
      and do.reached(row(outcome="terminated", failure_reason="vote: 60%", meeting_date="2024-03-01"), "vote_passed") is False)
check("a failure after a passed vote counts at the vote stage",
      do.reached(row(outcome="terminated", failure_reason="regulator", meeting_date="2024-03-01", outcome_date="2024-06-01"), "vote_passed") is True)
check("a completed scheme reached every stage", all(do.reached(row(), s) for s in do.STAGES))

# the monitor: later stages start from higher chances, and the feature model moves less
with tempfile.TemporaryDirectory() as root:
    os.makedirs(os.path.join(root, "reports"))
    odds = {"stages": {"scheme|announced": {"rate": 0.90, "n_cautious": 200}, "scheme|booklet_out": {"rate": 0.92, "n_cautious": 190},
                       "scheme|vote_passed": {"rate": 0.99, "n_cautious": 180}, "scheme|court_approved": {"rate": 0.995, "n_cautious": 170}},
            "features": do.FEATURES, "model": {"used": True, "intercept": 2.2, "coef": {f: 0.0 for f in do.FEATURES}}}
    odds["model"]["coef"]["board_not_for"] = -2.0
    json.dump(odds, open(os.path.join(root, "reports", "deal_odds.json"), "w"))
    hostile = row(board_recommendation="against")
    a = dm.base_rate(root, "scheme", "announced", hostile)[0]
    v = dm.base_rate(root, "scheme", "vote_passed", hostile)[0]
    c = dm.base_rate(root, "scheme", "court_approved", hostile)[0]
    plain = dm.base_rate(root, "scheme", "announced", None)[0]
    check("a hostile board lowers the starting chance at announcement", a < plain - 0.1, (a, plain))
    check("past the vote the stage decides most of it", v > 0.95, v)
    check("court approved ignores the features", abs(c - 0.995) < 1e-9, c)

print("\nALL PASS" if not fails else f"\n{len(fails)} FAILED: {fails}")
sys.exit(1 if fails else 0)
