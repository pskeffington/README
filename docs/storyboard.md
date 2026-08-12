# Storyboard

This file tracks the current public-facing research narrative without reproducing private implementation detail.

## Current Frame

The portfolio is centered on a five-repository, human-reviewed document-intelligence research pipeline:

```text
ctl-injest
  -> Eagle-Eye
  -> trans
  -> trans-release
  -> trans-downstream
```

Each repository has a distinct authority boundary:

- `ctl-injest` governs source admission, classification, and run planning;
- `Eagle-Eye` preserves source facts, page/frame identity, and bounded visual observations;
- `trans` performs reconciliation, bounded text/document processing, handwriting analysis, and review projection;
- `trans-release` performs QA and independent approval correlation;
- `trans-downstream` produces bounded projections and dry-run delivery receipts.

A later layer may narrow eligibility but must not silently promote an earlier blocked, review-required, blank, negative, or held state.

## Current Research Milestone

**Milestone: reproducible, review-gated five-repository candidate**

The immediate objective is to seal and reproduce a candidate whose behavior is identical across supported Python environments and remote CI while preserving exact artifact correlation and human-review gates.

Current acceptance indicators:

- exact five-repository version set;
- installed-wheel proof on Python 3.11 and Python 3.12;
- remote CI for the same sealed candidate;
- exact adjacent artifact joins;
- no raw source payloads in bounded proof receipts;
- mandatory handwriting review for uncertain candidates;
- explicit independent release approval correlation;
- downstream dry-run default;
- fail-closed behavior for malformed, mismatched, changed-hash, missing-approval, and conflicting-retry cases.

## Current Scholarly Direction

The research contribution is framed around **auditable, provenance-preserving, human-reviewed document processing**.

The current scholarly work should evaluate:

- source/page/region traceability;
- bounded glyph and text evidence;
- confidence and review-state calibration;
- review workload and disagreement;
- false-promotion and blocking behavior;
- exact software provenance;
- end-to-end release and downstream evidence boundaries.

The program does not claim universal OCR or handwriting recognition, writer identity, authorship, authenticity, legal certification, clinical authority, or autonomous institutional decision-making.

## Current Next Frame

1. Seal the next five-repository candidate.
2. Run installed-wheel proofs on Python 3.11 and Python 3.12.
3. Capture remote CI for the exact version set.
4. Resolve review/merge status for the active `trans` candidate.
5. Run the complete failure-state and approval-correlation matrix.
6. Build the independent handwriting benchmark and reviewer protocol.
7. Consolidate the evidence-room manifest and research/deployment risk register.
8. Complete hosted staging controls before making deployment claims.
9. Prepare the institutional pilot acceptance and reproducibility package.

## Public Narrative Boundary

Public status text may describe research goals, architecture, contracts, validation, reproducibility, limitations, and sanitized aggregate evidence.

It must not expose credentials, private payloads, unrestricted OCR or source text, private storage locations, restricted records, or unsupported claims of automated authority.

Historical milestones and superseded project framing belong in dated weekly snapshots rather than this current storyboard.
