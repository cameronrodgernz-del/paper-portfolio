"""Append-only ledger. Each table is a JSON-lines file; every record carries the hash of
the record before it, so any edit to the past breaks the chain and shows up in verify().
Mistakes are fixed by a new 'reversal' record, never by editing.

Tables: decisions, orders, fills, cash, corporate_actions, valuations, calls.
"""
import hashlib
import json
import os
from datetime import datetime, timezone

TABLES = ("decisions", "orders", "fills", "cash", "corporate_actions", "valuations", "calls")


def _canon(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


class Ledger:
    def __init__(self, root: str):
        self.root = root
        os.makedirs(root, exist_ok=True)

    def _path(self, table: str) -> str:
        if table not in TABLES:
            raise ValueError(f"unknown table {table}")
        return os.path.join(self.root, f"{table}.jsonl")

    def _last(self, table: str):
        p = self._path(table)
        if not os.path.exists(p):
            return 0, "genesis"
        last = None
        with open(p, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    last = json.loads(line)
        return (last["seq"], last["hash"]) if last else (0, "genesis")

    def append(self, table: str, payload: dict, ts: str | None = None) -> dict:
        seq, prev = self._last(table)
        rec = {"seq": seq + 1, "ts_utc": ts or datetime.now(timezone.utc).isoformat(timespec="seconds"),
               "table": table, "payload": payload, "prev_hash": prev}
        rec["hash"] = hashlib.sha256((prev + _canon({k: rec[k] for k in ("seq", "ts_utc", "table", "payload")})).encode()).hexdigest()
        with open(self._path(table), "a", encoding="utf-8") as f:
            f.write(_canon(rec) + "\n")
        return rec

    def records(self, table: str) -> list[dict]:
        p = self._path(table)
        if not os.path.exists(p):
            return []
        with open(p, encoding="utf-8") as f:
            return [json.loads(l) for l in f if l.strip()]

    def verify(self) -> dict:
        """Returns {table: 'ok' | 'broken at seq N'}."""
        out = {}
        for t in TABLES:
            prev, status = "genesis", "ok"
            for r in self.records(t):
                body = {k: r[k] for k in ("seq", "ts_utc", "table", "payload")}
                h = hashlib.sha256((prev + _canon(body)).encode()).hexdigest()
                if r["prev_hash"] != prev or r["hash"] != h:
                    status = f"broken at seq {r['seq']}"
                    break
                prev = r["hash"]
            out[t] = status
        return out
