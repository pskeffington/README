# Skeffington Repository Status

This repository is the public, sanitized status surface for active research, scholarly coordination, repository governance, and portfolio-level documentation.

## Current Status

Last manual update: 2026-08-12

Two key research programs are currently active:

1. **CART-TRACE** — a public research framework supporting Dartmouth CAR T-cell program research on longitudinal hospital care trajectories, utilization, care transitions, and reproducible episode reconstruction around CAR T-cell therapy.
2. **TRANS** — a five-repository, human-reviewed document-intelligence research pipeline for bounded source admission, visual evidence, document processing, release validation, and downstream projection.

## Key Project — CART-TRACE

Repository: [`pskeffington/CART-TRACE`](https://github.com/pskeffington/CART-TRACE)

**CART-TRACE** reconstructs longitudinal hospital care trajectories around CAR T-cell therapy using treatment-relative episodes rather than isolated encounters.

Current research focus:

- treatment-relative time with `day 0 = infusion`;
- inpatient and outpatient encounters;
- care location and level-of-care transitions;
- high-acuity escalation and de-escalation;
- length of stay and discharge timing;
- 7-day and 30-day acute-care reuse;
- provenance, missingness, and reproducible transformation rules;
- descriptive care phenotypes without turning those phenotypes into clinical recommendations.

The current thesis-level question is how longitudinal clinical data can characterize hospital resource utilization and transitions in level of care following CAR T-cell therapy.

CART-TRACE is synthetic-first in public development and is **not** a clinical decision-support system. It does not diagnose toxicity, issue alerts, recommend transfer/discharge/treatment, or represent research associations as bedside guidance. Any future institutional-data work must occur under appropriate governance and approvals.

## TRANS Research Program

```text
ctl-injest
  -> Eagle-Eye
  -> trans
  -> trans-release
  -> trans-downstream
```

Current TRANS program state:

- five repository authority boundaries are documented and cross-aligned;
- installed-wheel Python 3.11 ecosystem proofs are available;
- exact adjacent artifact correlation is preserved across the pipeline;
- the active `trans` research candidate remains human-review gated;
- release approval is independently correlated rather than inferred from candidacy or interface state;
- downstream projection remains dry-run by default;
- bounded evidence receipts do not retain unrestricted source payloads;
- external delivery remains disabled unless separately authorized and evidenced;
- Python 3.12, exact-candidate remote CI, independent handwriting benchmarking, and hosted staging remain current validation gates.

### Active TRANS repositories

| Repository | Visibility | Current Role | Status |
|---|---|---|---|
| `ctl-injest` | private | source admission, classification, governed run planning, orchestration receipts | Active research |
| `Eagle-Eye` | private | source facts, page/frame identity, bounded visual observations | Active research |
| `trans` | private | reconciliation, transcript/document packets, handwriting processing, review projection | Active research |
| `trans-release` | private | QA, independent approval correlation, release eligibility | Active research |
| `trans-downstream` | private | bounded projection, destination planning, dry-run delivery receipts | Active research |

A later layer may narrow eligibility but must not silently promote an earlier blocked, review-required, blank, negative, or held state.

## Current Research Direction

Across the portfolio, current work emphasizes auditable evidence, provenance, reproducibility, explicit uncertainty, and human review.

For CART-TRACE, that means making the hospital care sequence transparent, reproducible, and measurable before attempting prediction or clinical implementation.

For TRANS, that means auditable, provenance-preserving, human-reviewed document processing rather than generalized OCR performance.

Neither program is presented as an autonomous clinical, legal, policy, or institutional decision system.

## Current Validation Work

### CART-TRACE

Current work is directed toward:

1. episode schema and treatment-relative timeline;
2. care-state vocabulary;
3. synthetic episode generation;
4. transition reconstruction;
5. utilization metrics;
6. provenance and missingness handling;
7. reproducible validation before any institutional-data analysis.

### TRANS

The next TRANS candidate must reproduce bounded behavior across:

1. Python 3.11 installed-wheel execution;
2. Python 3.12 installed-wheel execution;
3. remote CI for the exact sealed five-repository candidate;
4. adjacent artifact-join checks;
5. blocked, malformed, mismatched, changed-hash, missing-approval, and conflicting-retry cases;
6. independent handwriting review and error analysis;
7. deployment-owned hosted staging controls where deployment behavior is evaluated.

## Public Research and Scholarly Repositories

| Repository | Visibility | Purpose |
|---|---|---|
| `CART-TRACE` | public | CAR T-cell longitudinal care-trajectory and hospital-utilization research framework |
| `README` | public | sanitized portfolio and research-status surface |

Other repositories should be evaluated independently before any visibility change. `trans-latin` is currently private and therefore is not listed as a public scholarly repository.

## Security and Public-Interest Boundary

This public repository does not reproduce private implementation details, credentials, raw source media, unrestricted OCR, governed source text, private storage locations, PHI, or restricted records.

Public-facing documentation may describe:

- research goals;
- architecture and authority boundaries;
- validation status;
- reproducibility methods;
- limitations;
- scholarly publication direction;
- sanitized aggregate evidence.

Public CART-TRACE development must remain synthetic-first unless a separately governed institutional workflow is established. Public TRANS documentation must remain sanitized and bounded.

## Storyboard and Weekly Status

The current project narrative is maintained in [`docs/storyboard.md`](docs/storyboard.md).

Current weekly snapshot: [`docs/weekly/2026-08-12.md`](docs/weekly/2026-08-12.md).

Older weekly snapshots remain historical records and are not the source of current project status.

## Repository Governance

Current-facing README material should describe only present project state. Historical baselines, superseded architecture, older milestones, and prior weekly activity belong in dated documentation rather than on headline repository pages.

Research repositories should be classified according to their actual role and intended visibility. Public research repositories must contain only intentionally public, permissioned, synthetic, redacted, or otherwise appropriate material.

Research scaffolds should not receive cosmetic commits solely to make them appear recent. A stable repository can remain unchanged when its scope, evidence status, limitations, and next actions are still accurate.

## Automation

The weekly scan is defined in [`.github/workflows/weekly-repo-scan.yml`](.github/workflows/weekly-repo-scan.yml).

Automated scans should be treated as repository-observation aids rather than substitutes for manual research-status review. Public outputs must remain sanitized even when private repositories are included in the scan source.
