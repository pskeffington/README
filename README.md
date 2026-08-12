# Skeffington Repository Status

This repository is the public, sanitized status surface for active research, scholarly coordination, repository governance, and portfolio-level documentation.

## Current Status

Last manual update: 2026-08-12

The primary active research program is the five-repository TRANS document-intelligence pipeline:

```text
ctl-injest
  -> Eagle-Eye
  -> trans
  -> trans-release
  -> trans-downstream
```

Current program state:

- five repository authority boundaries are documented and cross-aligned;
- installed-wheel Python 3.11 ecosystem proofs are available;
- exact adjacent artifact correlation is preserved across the pipeline;
- the active `trans` research candidate remains human-review gated;
- release approval is independently correlated rather than inferred from candidacy or interface state;
- downstream projection remains dry-run by default;
- bounded evidence receipts do not retain unrestricted source payloads;
- external delivery remains disabled unless separately authorized and evidenced;
- Python 3.12, exact-candidate remote CI, independent handwriting benchmarking, and hosted staging remain current validation gates.

## Active TRANS Research Repositories

| Repository | Visibility | Current Role | Status |
|---|---|---|---|
| `ctl-injest` | private | source admission, classification, governed run planning, orchestration receipts | Active research |
| `Eagle-Eye` | private | source facts, page/frame identity, bounded visual observations | Active research |
| `trans` | private | reconciliation, transcript/document packets, handwriting processing, review projection | Active research |
| `trans-release` | private | QA, independent approval correlation, release eligibility | Active research |
| `trans-downstream` | private | bounded projection, destination planning, dry-run delivery receipts | Active research |

A later layer may narrow eligibility but must not silently promote an earlier blocked, review-required, blank, negative, or held state.

## Current Research Direction

The present scholarly focus is **auditable, provenance-preserving, human-reviewed document processing** rather than generalized OCR performance.

Current work includes:

- handwriting and printed-text processing;
- page- and region-level provenance;
- bounded glyph and text candidates;
- explicit uncertainty and review states;
- reproducible source-to-output traceability;
- independent release approval correlation;
- dry-run downstream projection;
- exact software/version provenance for research evidence.

The program does not claim universal handwriting recognition, writer identity, authorship, authenticity, legal certification, clinical authority, or autonomous institutional decision-making.

## Current Validation Work

The next research candidate must reproduce bounded behavior across:

1. Python 3.11 installed-wheel execution;
2. Python 3.12 installed-wheel execution;
3. remote CI for the exact sealed five-repository candidate;
4. adjacent artifact-join checks;
5. blocked, malformed, mismatched, changed-hash, missing-approval, and conflicting-retry cases;
6. independent handwriting review and error analysis;
7. deployment-owned hosted staging controls where deployment behavior is evaluated.

## Public Scholarly Repositories

Public scholarly repositories may remain public when they contain intentionally public, permissioned, or otherwise appropriate scholarly material and do not expose private operational evidence.

`trans-latin` remains a public scholarly translation repository. Other translation repositories should be evaluated independently before any visibility change.

## Security and Public-Interest Boundary

This public repository does not reproduce private implementation details, credentials, raw source media, unrestricted OCR, governed source text, private storage locations, or restricted records.

Public-facing documentation may describe:

- research goals;
- architecture and authority boundaries;
- validation status;
- reproducibility methods;
- limitations;
- scholarly publication direction;
- sanitized aggregate evidence.

Private operational or research repositories should remain private unless a separate review determines that a repository is intentionally suitable for public release.

## Storyboard and Weekly Status

The current project narrative is maintained in [`docs/storyboard.md`](docs/storyboard.md).

Current weekly snapshot: [`docs/weekly/2026-08-12.md`](docs/weekly/2026-08-12.md).

Older weekly snapshots remain historical records and are not the source of current project status.

## Repository Governance

Current-facing README material should describe only present project state. Historical baselines, superseded architecture, older milestones, and prior weekly activity belong in dated documentation rather than on headline repository pages.

Cross-repository research documentation should preserve the same authority model:

```text
admission
  -> visual/source evidence
  -> bounded document processing and review
  -> independent release validation
  -> bounded downstream projection
```

No downstream repository should create authority that belongs to an upstream or independent review layer.

## Automation

The weekly scan is defined in [`.github/workflows/weekly-repo-scan.yml`](.github/workflows/weekly-repo-scan.yml).

Automated scans should be treated as repository-observation aids rather than substitutes for manual research-status review. Public outputs must remain sanitized even when private repositories are included in the scan source.
