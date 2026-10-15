# Frequency ↔ Open Evidence Lab: narrow claim comparison

Reference comparison is against the Lab's pinned [REMORA effect bridge](https://github.com/probityai/agent-evidence-observer/blob/b8ec935107385177ac3fd04772b8962899eb9d6f/docs/REMORA-EFFECT-BRIDGE.md), not a claim of identical test harnesses.

| Frequency synthetic row | Lab effect bridge | Relationship | Critical boundary |
| --- | --- | --- | --- |
| AR-00, authorized/current effect confirmed | Permitted local file write with matching subsequent read | **Semantically comparable**, not equivalent provenance | Frequency receives a claimed observation string; Lab executes a protected local file write and read |
| AR-05, historical execution reported/current effect contradicted | Successful write followed by later file change, then fresh read | **Semantically comparable**, not equivalent provenance | Both preserve historical reporting when present state differs; Frequency does not independently validate that a write occurred |
| AR-01–AR-04, refusal rows | Changed path/identity/tool/policy denial cases | **Not equivalent** | Lab attempts to verify no write occurred; Frequency only compares supplied synthetic state strings, and cannot prove a store remained untouched |
| Remaining cross-product combinations | No direct case in this pinned reference | **No mapping claimed** | Enumerating logical states is not a live execution evidence contract |

## Gap-First review

- **Scope:** This mapping is human-readable only. It does not change the Lab reader, contracts, expected statuses, or published vectors.
- **Provenance:** Frequency fixture inputs are assertions, not cryptographically verified receipts. The Lab reference records a local dispatch/write/read under one operator, not independent external attestation.
- **Adversarial distinction:** A missing `observation` field is invalid input; an explicit JSON `null` is unavailable evidence and yields `NOT_ESTABLISHED`. The checker has a regression test for this.
- **No uplift:** `CONFIRMED` means equal strings, `CONTRADICTED` means unequal strings; neither alone establishes causation, authorized historical execution, or persistent effects.
- **Attribution:** Frequency synthetic claim-model fixture © Valentyn Rukhaylo / Altru.dev, MIT. The Lab's REMORA effect bridge and reader remain credited separately to their respective authors; no part of the Lab implementation is relicensed here.
- **Next acceptance:** a maintainer can accept this scoped table, reject the correspondence, or request a second independently implemented reader over the same pinned inputs. A genuine retained-run integration remains NOT EVALUATED.
