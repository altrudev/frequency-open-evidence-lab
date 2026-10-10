#!/usr/bin/env python3
"""Offline claim-separation regression fixture; synthetic assertions only."""
import json
from pathlib import Path

CASES = json.loads((Path(__file__).parent / "cases.json").read_text(encoding="utf-8"))

def assess(c):
    if not isinstance(c, dict):
        raise TypeError("case must be an object")
    for key in ("authorized", "execution_reported"):
        if type(c.get(key)) is not bool:
            raise TypeError(f"{key} must be a JSON boolean")
    if type(c.get("expected_effect")) is not str:
        raise TypeError("expected_effect must be a string")
    if c.get("observation") is not None and type(c["observation"]) is not str:
        raise TypeError("observation must be a string or null")
    authorization = "AUTHORIZED" if c["authorized"] else "DENIED"
    execution = "REPORTED" if c["execution_reported"] else "NOT_REPORTED"
    if c["observation"] is None:
        effect = "NOT_ESTABLISHED"
    elif c["observation"] == c["expected_effect"]:
        effect = "CONFIRMED"
    else:
        effect = "CONTRADICTED"
    return dict(authorization=authorization, execution=execution, current_effect=effect)

def main():
    if len(CASES) != 12 or len({c["id"] for c in CASES}) != 12:
        raise ValueError("expected exactly 12 uniquely identified cases")
    for c in CASES:
        actual = assess(c)
        if actual != c["expected"]:
            raise AssertionError(f"{c['id']}: {actual} != {c['expected']}")
        print(f"PASS {c['id']}: {actual}")
    print(f"PASS {len(CASES)}/{len(CASES)} synthetic cases")

if __name__ == "__main__":
    main()
