"""Which Norgate price files (data/norgate/prices/<TICKER>__<announce date>.csv, exported on Cam's PC by
tools/norgate_export.py) belong to the company the deal database names.

A file counts when its security name shares its first distinctive word with the deal database's
target name (company words like Limited, Group or Ordinary are ignored). Codes are often reused on the
ASX, and the export takes the listing that traded under the code at the announcement, which for a few
renamed or reused codes is the wrong company; those are left out here.
Writes data/norgate/verified.csv. Usage: python3 -I src/history/norgate_link.py <repo_root>
"""
import csv
import os
import re
import sys

STOP = {"limited", "ltd", "group", "holdings", "the", "inc", "fund", "trust", "ordinary", "fully", "paid", "stapled",
        "securities", "units", "australia", "australian", "co", "corporation", "corp", "plc", "reit", "nl"}


def words(s: str) -> list[str]:
    return [w for w in re.sub(r"[^a-z0-9 ]", " ", (s or "").lower()).split() if w not in STOP]


def same_company(a: str, b: str) -> bool:
    x, y = words(a), words(b)
    return bool(x and y and (x[0] == y[0] or x[0] in y or y[0] in x))


def verified(root: str) -> dict:
    """(ticker, announce date) -> path of a Norgate price file that is the named company's."""
    mp = os.path.join(root, "data", "norgate", "matches.csv")
    wp = os.path.join(root, "config", "norgate_wanted.csv")
    if not (os.path.exists(mp) and os.path.exists(wp)):
        return {}
    names = {(r["ticker"], r["announce_date"]): r["name"] for r in csv.DictReader(open(wp, encoding="utf-8"))}
    out = {}
    for m in csv.DictReader(open(mp, encoding="utf-8")):
        key = (m["ticker"], m["announce_date"])
        path = os.path.join(root, "data", "norgate", "prices", f"{m['ticker']}__{m['announce_date']}.csv")
        if m["status"] == "ok" and os.path.exists(path) and same_company(names.get(key, ""), m["norgate_name"]):
            out[key] = path
    return out


def main(root: str) -> int:
    v = verified(root)
    mp = os.path.join(root, "data", "norgate", "matches.csv")
    rows = list(csv.DictReader(open(mp, encoding="utf-8")))
    with open(os.path.join(root, "data", "norgate", "verified.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ticker", "announce_date", "norgate_symbol", "norgate_name", "used"])
        for m in rows:
            k = (m["ticker"], m["announce_date"])
            w.writerow([m["ticker"], m["announce_date"], m["norgate_symbol"], m["norgate_name"],
                        "yes" if k in v else ("no: not found" if m["status"] != "ok" else "no: a different company on the code")])
    print(f"{len(v)} of {len(rows)} Norgate files are the named company")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
