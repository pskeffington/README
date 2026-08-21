# Skeffington Repository Status

This repository is the public, sanitized status surface for active research, scholarly coordination, repository governance, and portfolio-level documentation.

## Current Status

Last manual update: 2026-08-21

The repository estate is maintained as a tiered research portfolio rather than as a flat list of projects. The governing classification and evidence-promotion model are documented in [`docs/repository-architecture.md`](docs/repository-architecture.md).

Two programs anchor the research narrative:

1. **CART-TRACE** — the principal public translational-health data-science anchor, focused on reproducible post-infusion CAR T-cell care trajectories, utilization, provenance, missingness, synthetic validation, and a separate synthetic administrative access-gating research extension.
2. **TRANS** — a private, human-reviewed document-intelligence research system whose public contribution is methodological evidence about provenance, review states, bounded evidence, release validation, and reproducibility.

A second tier of biomedical and public-health studies contributes bounded evidence into the broader portfolio rather than functioning as competing primary anchors. Visibility is repository-specific and may change; supporting-study status does not imply public visibility.

## Key Project — CART-TRACE

Repository: [`pskeffington/CART-TRACE`](https://github.com/pskeffington/CART-TRACE)

**CART-TRACE** is a synthetic-first research framework for reconstructing post-infusion hospital care trajectories following CAR T-cell therapy.

The current public scholarly capstone package includes a frozen canonical episode/state model, deterministic trajectory reconstruction, post-infusion utilization metrics, synthetic truth-set validation, reproducibility controls, and governed-data readiness methods. Institutional clinical-data application remains separate and conditional on appropriate approvals, data access, local mapping, and validation.

A separate synthetic research extension now models administrative access events across referral, program review, facility, network, payer, Medicare, financial-clearance, and derived access states. This extension is outside the frozen capstone scope and is maintained for retrospective methods research only. It does not determine clinical eligibility, insurance coverage, treatment readiness, or authorization decisions.

CART-TRACE is **not** a clinical decision-support system. It does not determine treatment eligibility, diagnose toxicity, issue prospective alerts, recommend transfer/discharge/treatment, adjudicate payer coverage, or treat synthetic validation as evidence of external clinical validity.

## Supporting Biomedical and Public-Health Evidence Lanes

| Repository | Evidence lane | Portfolio role | Current visibility |
|---|---|---|---|
| `ECG-denoising` | biomedical signal evaluation | supporting study | public |
| `pet-noise-radiomics-robustness` | imaging robustness | supporting study | public |
| `cancer-eol-death-place-typologies` | health-services research | supporting study | public |
| `Public-Health-Emergency-Preparedness---Dartmouth-Health` | preparedness systems research | supporting study | private |
| `Gaza-WASH` | humanitarian secondary-data research | supporting study | public |
| `Haiti-nippes` | regional public-health systems research | supporting study | public |
| `WASH` | environmental health and spatial equity | supporting study | public |

Validated outputs from these repositories should be promoted through a common portfolio evidence envelope recording provenance, transformation version, validation status, uncertainty/missingness, claim boundaries, and stable artifact paths. Repository-specific scientific schemas remain domain-specific.

### Current ECG evidence boundary

`ECG-denoising` now has an executable Phase 1 NSTDB benchmark pathway and a formal public benchmark-freeze protocol. This supports a claim of an executable, provenance-controlled non-clinical benchmark pathway. Comparative method or morphology-preservation claims remain gated on a reviewed freeze packet, reproducibility evidence, and morphology-preservation review.

## Evidence Promotion Rule

```text
raw/public source
  -> repository-specific transformation
  -> repository-specific validation
  -> bounded evidence object
  -> portfolio evidence envelope
  -> CV / public portfolio claim
```

A public CV or portfolio claim should not precede the underlying evidence object.

## Active Private Supporting Systems

Several private repositories have substantive current research roles and are not archive candidates merely because they are private:

- `Plymouth` — municipal GIS/provenance and civic-planning research workspace;
- `Control` — evidence-contract, validation, and bounded automation-policy research;
- `ml-lab` — pre-pilot ML-assisted, human-adjudicated healthcare-document review research;
- `cipher-topology-lab` — computational-topology, randomness-diagnostic, and provenance research;
- `Public-Health-Emergency-Preparedness---Dartmouth-Health` — preparedness systems research with a scholarly, explicitly non-operational boundary.

Public references to private repositories should remain generalized and claim-bounded. Private paths, sensitive materials, configurations, contact data, or implementation details should not migrate into this public status surface.

## TRANS Research Program

```text
ctl-injest
  -> Eagle-Eye
  -> trans
  -> trans-release
  -> trans-downstream
```

TRANS remains a private, human-reviewed research system. Its public-facing description should remain limited to architecture, provenance, validation, reproducibility, review-state controls, and sanitized aggregate evidence. Private source payloads and implementation details remain out of scope for public documentation.

## Repository Governance

The portfolio uses five dispositions:

1. public anchor;
2. supporting study;
3. private research system;
4. utility / administrative repository;
5. consolidation / archive candidate.

This classification is a maintenance rule, not an automatic archive/delete policy. Small, experimental, duplicate, or weakly differentiated repositories should receive dependency/content review before additional routine maintenance.

Current-facing README material should describe present project state. Historical baselines, superseded architecture, older milestones, and prior weekly activity belong in dated documentation rather than headline repository pages.

Research scaffolds should not receive cosmetic commits solely to make them appear recent. A stable repository can remain unchanged when its scope, evidence status, limitations, and next actions are still accurate.

## Public Research and Professional Surfaces

| Repository | Role |
|---|---|
| `CART-TRACE` | principal public translational-health anchor |
| `README` | sanitized portfolio governance/status surface |
| `CV-Public-Facing` | public professional evidence surface |

Other public research repositories are supporting studies as described above. `Best-Practices-Git` functions as a reusable public research-method standard. `Family_and_Economic_issues` and `St.-Bonaventure` remain independently mature scholarly projects rather than portfolio anchors. `kosher-eats-south-shore` is a non-core community-information utility.

## Security and Public-Interest Boundary

This public repository does not reproduce private implementation details, credentials, raw source media, governed source text, private storage locations, PHI, restricted records, or sensitive operational information.

Public-facing documentation may describe research goals, architecture, validation status, reproducibility methods, limitations, scholarly publication direction, and sanitized aggregate evidence.

Public biomedical, civic, and humanitarian repositories should remain scholarly, source-bounded, non-operational, and explicit about unsupported claims.

## Storyboard and Weekly Status

The current project narrative is maintained in [`docs/storyboard.md`](docs/storyboard.md).

Current weekly repository sweep: [`docs/weekly/2026-08-21.md`](docs/weekly/2026-08-21.md).

Repository classification and evidence architecture: [`docs/repository-architecture.md`](docs/repository-architecture.md).

Older weekly snapshots remain historical records and are not the source of current project status.

## Automation

The weekly scan is defined in [`.github/workflows/weekly-repo-scan.yml`](.github/workflows/weekly-repo-scan.yml).

Automated scans should prioritize anchor accuracy, evidence promotion, source/validation drift, public-private boundary correctness, and consolidation decisions rather than generating activity for every repository.
