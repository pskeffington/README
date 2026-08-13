# Skeffington Repository Status

This repository is the public, sanitized status surface for active research, scholarly coordination, repository governance, and portfolio-level documentation.

## Current Status

Last manual update: 2026-08-12

The repository estate is now maintained as a tiered research portfolio rather than as a flat list of projects. The governing classification and evidence-promotion model are documented in [`docs/repository-architecture.md`](docs/repository-architecture.md).

Two programs currently anchor the research narrative:

1. **CART-TRACE** — the principal public translational-health data-science anchor, focused on longitudinal CAR T-cell care trajectories, utilization, provenance, missingness, and reproducible episode reconstruction.
2. **TRANS** — a private, human-reviewed document-intelligence research system whose public contribution is methodological evidence about provenance, review states, bounded evidence, release validation, and reproducibility.

A second tier of public biomedical and public-health studies contributes validated evidence objects into the broader portfolio rather than functioning as competing primary anchors.

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

## Supporting Biomedical and Public-Health Evidence Lanes

| Repository | Evidence lane | Portfolio role |
|---|---|---|
| `ECG-denoising` | biomedical signal evaluation | supporting study |
| `pet-noise-radiomics-robustness` | imaging robustness | supporting study |
| `cancer-eol-death-place-typologies` | health-services research | supporting study |
| `Public-Health-Emergency-Preparedness---Dartmouth-Health` | preparedness systems research | supporting study |
| `Gaza-WASH` | humanitarian secondary-data research | supporting study |
| `Haiti-nippes` | regional public-health systems research | supporting study |
| `WASH` | environmental health and spatial equity | supporting study |

Validated outputs from these repositories should be promoted through a common portfolio evidence envelope that records provenance, observation period, transformation version, validation status, uncertainty/missingness, claim boundaries, and stable artifact paths. Repository-specific scientific schemas remain domain-specific.

## Evidence Promotion Rule

```text
raw/public source
  -> repository-specific transformation
  -> repository-specific validation
  -> bounded evidence object
  -> portfolio evidence envelope
  -> CV / public portfolio claim
```

A public CV or portfolio claim should not precede the underlying validated evidence object.

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

## Repository Governance

The portfolio now uses five dispositions:

1. public anchor;
2. supporting study;
3. private research system;
4. utility / administrative repository;
5. consolidation / archive candidate.

This classification is a maintenance rule, not an automatic archive/delete policy. Small, experimental, duplicate, or weakly differentiated repositories should receive dependency/content review before additional routine maintenance.

Current-facing README material should describe only present project state. Historical baselines, superseded architecture, older milestones, and prior weekly activity belong in dated documentation rather than on headline repository pages.

Research scaffolds should not receive cosmetic commits solely to make them appear recent. A stable repository can remain unchanged when its scope, evidence status, limitations, and next actions are still accurate.

## Public Research and Professional Surfaces

| Repository | Role |
|---|---|
| `CART-TRACE` | principal public translational-health anchor |
| `README` | sanitized portfolio governance/status surface |
| `CV-Public-Facing` | public professional evidence surface |

Other public research repositories are supporting studies as described above. `trans-latin` is currently private and is not listed as a public scholarly repository.

## Security and Public-Interest Boundary

This public repository does not reproduce private implementation details, credentials, raw source media, unrestricted OCR, governed source text, private storage locations, PHI, or restricted records.

Public-facing documentation may describe research goals, architecture, validation status, reproducibility methods, limitations, scholarly publication direction, and sanitized aggregate evidence.

Public CART-TRACE development must remain synthetic-first unless a separately governed institutional workflow is established. Public TRANS documentation must remain sanitized and bounded. Public biomedical and humanitarian repositories should remain scholarly, source-bounded, non-operational, and explicit about unsupported claims.

## Storyboard and Weekly Status

The current project narrative is maintained in [`docs/storyboard.md`](docs/storyboard.md).

Current weekly snapshot: [`docs/weekly/2026-08-12.md`](docs/weekly/2026-08-12.md).

Repository classification and evidence architecture: [`docs/repository-architecture.md`](docs/repository-architecture.md).

Older weekly snapshots remain historical records and are not the source of current project status.

## Automation

The weekly scan is defined in [`.github/workflows/weekly-repo-scan.yml`](.github/workflows/weekly-repo-scan.yml).

Automated scans should prioritize anchor accuracy, evidence promotion, source/validation drift, public-private boundary correctness, and consolidation decisions rather than generating activity for every repository.
