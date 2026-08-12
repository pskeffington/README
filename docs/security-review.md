# Repository Security Review

## Current Controls

- The `README` repository is intentionally public and serves as the sanitized public status surface.
- The five active TRANS research repositories are expected to remain private.
- `CART-TRACE` is intentionally public as a synthetic-first CAR T-cell research repository.
- The weekly scan should flag a configured private research repository if it is public.
- Public scholarly or public research repositories may remain public only when they contain intentionally shareable material appropriate to their declared research boundary.
- Repositories whose public eligibility is unresolved remain private-review repositories until explicitly reclassified.
- Public status artifacts must exclude credentials, PHI, private source payloads, unrestricted OCR, source images, private storage locations, and implementation-sensitive evidence.

## Current Private TRANS Research Watchlist

| Repository | Expected Visibility | Current Role |
|---|---:|---|
| `ctl-injest` | Private | source admission, classification, governed run planning, orchestration receipts |
| `Eagle-Eye` | Private | source facts, page/frame identity, bounded visual observations |
| `trans` | Private | reconciliation, transcript/document packets, handwriting processing, review projection |
| `trans-release` | Private | QA, independent approval correlation, release eligibility |
| `trans-downstream` | Private | bounded projection, destination planning, dry-run delivery receipts |

## Public Research Repositories

| Repository | Expected Visibility | Note |
|---|---:|---|
| `CART-TRACE` | Public | Synthetic-first CAR T-cell longitudinal care-trajectory and hospital-utilization research framework. No PHI or clinical decision-support claims. |

## Public Scholarly Repositories

| Repository | Expected Visibility | Note |
|---|---:|---|
| `trans-latin` | Public | Intentionally public scholarly translation objects. |

## Private Review Repositories

| Repository | Expected Visibility | Note |
|---|---:|---|
| `Trans-heb` | Private | Public scholarly eligibility remains unresolved; do not present it as public until separately reviewed and reclassified. |

## CART-TRACE Public Boundary

Public CART-TRACE material may include synthetic datasets, schemas, reproducible transformation logic, descriptive methods, benchmark outputs, and documentation appropriate for public research release.

Public CART-TRACE material must not include:

- PHI or patient-identifying free text;
- production credentials or institutional secrets;
- clinical alerts or treatment recommendations;
- automated CRS, ICANS, or other toxicity diagnosis from raw signals;
- unsupported claims of clinical validation or bedside authority;
- institutional data outside applicable governance and approvals.

## Public-Repo Rule

Public repositories should contain only sanitized public material: documentation, research summaries, demonstrations, portfolio material, public scholarship, intentionally public translation objects, synthetic or permissioned research artifacts, and coordination notes.

Public repositories should not contain:

- secrets or credentials;
- PHI or restricted patient data;
- private source documents or page images;
- unrestricted OCR or transcripts;
- private storage pointers or signed URLs;
- sensitive collection workflows;
- private infrastructure details;
- operational instructions that exceed the public research boundary;
- claims of automated clinical, identity, authorship, authenticity, approval, or delivery authority that are not supported by the current repository contracts.

## Current TRANS Boundary Checks

The public status surface should preserve the current authority chain:

```text
source admission
  -> bounded visual/source evidence
  -> document processing and human review
  -> independent release approval correlation
  -> bounded dry-run downstream projection
```

A later component may narrow eligibility but must not be described as silently upgrading an upstream blocked, review-required, blank, negative, or held state.

## Weekly Review Steps

1. Confirm all five active TRANS research repositories remain private.
2. Confirm `CART-TRACE` remains public only within its synthetic-first, non-clinical-authority boundary.
3. Review any public/private classification mismatch immediately.
4. Confirm public project summaries remain sanitized and current.
5. Confirm public scholarly repositories contain only intentionally public materials.
6. Confirm private-review repositories remain private until separately cleared.
7. Confirm headline docs do not carry forward superseded milestones as current state.
8. Confirm raw payload retention and external delivery are not described as enabled unless separately authorized and evidenced.
9. Update classifications when repository roles genuinely change.
