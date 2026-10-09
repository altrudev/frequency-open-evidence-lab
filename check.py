#!/usr/bin/env python3
"""Offline claim-separation regression fixture. Standard library only."""
import json
from pathlib import Path

CASES = json.loads((Path(__file__).parent / 'cases.json').read_text())

def assess(c):
    authorization = 'AUTHORIZED' if c['authorized'] else 'DENIED'
    execution = 'REPORTED' if c['execution_reported'] else 'NOT_REPORTED'
    if c['observation'] is None:
        effect = 'NOT_ESTABLISHED'
    elif c['observation'] == c['expected_effect']:
        effect = 'CONFIRMED'
    else:
        effect = 'CONTRADICTED'
    return dict(authorization=authorization, execution=execution, current_effect=effect)

def main():
    for c in CASES:
        actual = assess(c)
        assert actual == c['expected'], f"{c['id']}: {actual} != {c['expected']}"
        print(f"PASS {c['id']}: {actual}")
    print(f"PASS {len(CASES)}/{len(CASES)} synthetic cases")

if __name__ == '__main__':
    main()
