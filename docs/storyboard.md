# Storyboard

This file tracks the current public-facing research narrative without reproducing private implementation detail.

## Current Frame

The portfolio currently has two key research programs.

### CART-TRACE

`CART-TRACE` is a public, synthetic-first research framework for longitudinal hospital care trajectories around CAR T-cell therapy, supporting Dartmouth CAR T-cell program research.

Current emphasis:

- treatment-relative episode reconstruction;
- inpatient/outpatient trajectory mapping;
- care-location and level-of-care transitions;
- high-acuity escalation and de-escalation;
- length of stay and discharge timing;
- 7-day and 30-day acute-care reuse;
- provenance, missingness, and reproducible transformation rules;
- descriptive care phenotypes without clinical recommendation.

The primary unit is the CAR T-cell therapy episode rather than the isolated encounter.

CART-TRACE is not a clinical decision-support system and public development must not contain PHI, production credentials, or patient-identifying free text.

### TRANS

The TRANS program is a five-stage, human-reviewed document-intelligence research pipeline with two language-specific scholarly branches:

```text
ctl-injest
  -> Eagle-Eye
  -> trans
  -> trans-release
  -> trans-downstream
  |-> trans-latin
  `-> Trans-heb
```

Each repository has a distinct authority boundary:

- `ctl-injest` governs source admission, classification, and run planning;
- `Eagle-Eye` preserves source facts, page/frame identity, and bounded visual observations;
- `trans` performs reconciliation, bounded text/document processing, handwriting analysis, and review projection;
- `trans-release` performs QA and independent approval correlation;
- `trans-downstream` produces bounded projections and dry-run delivery receipts.
- `trans-latin` and `Trans-heb` own language-specific scholarly acceptance and publication truth.

A later layer may narrow eligibility but must not silently promote an earlier blocked, review-required, blank, negative, or held state.

## Current Research Milestones

### CART-TRACE milestone

**Milestone: reproducible CAR T-cell episode reconstruction**

Current acceptance indicators:

- episode schema defined;
- treatment-relative time represented consistently;
- care-state vocabulary defined;
- synthetic trajectories available;
- transition reconstruction reproducible;
- utilization metrics explicitly derived;
- provenance and missingness retained;
- no clinical alerts, diagnoses, treatment recommendations, or bedside authority claims.

### TRANS milestone

**Milestone: reproducible, review-gated processing candidate**

Current acceptance indicators:

- exact processing-repository version set;
- installed-wheel proof on Python 3.11 and Python 3.12;
- remote CI for the same sealed candidate;
- exact adjacent artifact joins;
- no raw source payloads in bounded proof receipts;
- mandatory handwriting review for uncertain candidates;
- explicit independent release approval correlation;
- downstream dry-run default;
- fail-closed behavior for malformed, mismatched, changed-hash, missing-approval, and conflicting-retry cases.
- checkpoint admission/resolution, bounded candidate inference, frozen calibration, and review-decision receipts;
- background-spectrum metadata used only for robustness assessment and review routing, never writer identity or authorship.

No real training corpus, approved production checkpoint, held-out CER/WER, background-robustness result, or identity claim is currently frozen.

## Current Scholarly Direction

Across both programs, the research emphasis is on transparent, auditable, reproducible evidence.

For CART-TRACE, the scholarly objective is to characterize longitudinal hospital resource utilization and transitions in level of care following CAR T-cell therapy without turning descriptive patterns into clinical directives.

For TRANS, the scholarly objective is auditable, provenance-preserving, human-reviewed document processing.

Neither program is presented as an autonomous clinical, legal, policy, or institutional decision system.

## Current Next Frame

### CART-TRACE

1. Freeze the episode schema and care-state vocabulary.
2. Expand synthetic treatment-relative trajectories.
3. Validate transition reconstruction and utilization metrics.
4. Define missingness and provenance checks.
5. Prepare reproducible descriptive analyses before institutional-data work.
6. Keep all public artifacts synthetic, permissioned, redacted, or otherwise appropriate for public release.

### TRANS

1. Prove an installed Eagle-Eye crop/background packet through the exact TRANS adapter and review-decision receipts.
2. Run installed-wheel proofs on Python 3.11 and Python 3.12.
3. Capture remote CI for the exact version set.
4. Admit real documents only after permissions, retention, de-identification, split governance, and reviewer protocol are approved.
5. Run the complete failure-state and approval-correlation matrix.
6. Build an independent background-stratified handwriting benchmark and reviewer protocol without identity or authorship claims.
7. Consolidate the evidence-room manifest and research/deployment risk register.
8. Complete hosted staging controls before making deployment claims.

## Public Narrative Boundary

Public status text may describe research goals, architecture, contracts, validation, reproducibility, limitations, and sanitized aggregate evidence.

It must not expose credentials, PHI, private payloads, unrestricted OCR or source text, private storage locations, restricted records, or unsupported claims of automated clinical or institutional authority.

Historical milestones and superseded project framing belong in dated weekly snapshots rather than this current storyboard.
