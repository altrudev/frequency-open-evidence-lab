# Frequency / Open Evidence Lab — synthetic claim-separation fixture

Copyright (c) 2026 Valentyn Rukhaylo / Altru.dev. Fixture files licensed under MIT (see LICENSE).

## Purpose

Demonstrate that **authorization**, **historical execution reporting**, and **current-effect observation** are independent claims. In particular, a changed file does not retroactively erase a historical execution report; a missing observation is `NOT_ESTABLISHED`, not `CONTRADICTED`.

## Run

```sh
python3 check.py
python3 -I -m unittest discover -v
```

Requires Python 3.8+ standard library only. The nine fixtures are in `cases.json` and the pure evaluation function is in `check.py`. No network, credentials, production actions, or external dependencies.

## Semantics and limitations

- `authorized` is a synthetic input assertion, **not cryptographic authorization verification**.
- `execution_reported` is a synthetic historical report, **not proof of execution**.
- `observation` is a synthetic read value, **not an independently collected observation**.
- `CONFIRMED` means the provided observation matches the expected string; it does **not** prove causation, actor identity, authorization compliance, or persistence.
- `DENIED` with `REPORTED` or `CONFIRMED` is deliberately representable: it flags separation of claims rather than approving an unauthorized action.
- The fixture is a claim-model regression only. It is not a live integration, production assurance, cryptographic receipt, or independent verification of Frequency.

## Non-novelty boundary

Open Evidence Lab already documents request/effect joins and post-commit divergence in [its request/effect comparison](https://github.com/probityai/agent-evidence-atlas/blob/main/docs/request-effect-join.md). These nine cases **do not introduce a new observation mechanism or independently establish any execution fact**. They are a small, dependency-free claim-separation regression that can serve as a cross-reader control, subject to maintainer agreement on field semantics.

`CONTRADICTED` means **the supplied current-state string differs from the supplied expected string**, not that the historical action was disproved. The checker does not validate a signature, event source, timestamp, causality, observer independence, target identity, or durability.

## Proposed next integration

Compare expected outputs with the Lab's published file-write example. Add a separately pinned, independent reader only after agreement on schema and evidence boundary. Keep the Lab reader/check attribution separate from Frequency claim-model authorship. A useful follow-up would be a pinned retained run with a provenance chain and deliberate stale-observation negative case. Do not promote this synthetic demonstration to that claim.

## Ownership and scope

Standalone MIT-licensed fixture only. No private Frequency implementation, credentials, production receipts, or proprietary internals are included. This repository does not grant any license to the separate Frequency project.
