# Repository Security Review

## Current Controls

- The `README` repository is intentionally public and serves as the sanitized public status surface.
- The five active TRANS research repositories are expected to remain private.
- The weekly scan should flag a configured private research repository if it is public.
- Public scholarly repositories may remain public only when they contain intentionally shareable scholarly material.
- Repositories whose public eligibility is unresolved remain private-review repositories until explicitly reclassified.
- Public status artifacts must exclude credentials, private source payloads, unrestricted OCR, source images, private storage locations, and implementation-sensitive evidence.

## Current Private Research Watchlist

| Repository | Expected Visibility | Current Role |
|---|---:|---|
| `ctl-injest` | Private | source admission, classification, governed run planning, orchestration receipts |
| `Eagle-Eye` | Private | source facts, page/frame identity, bounded visual observations |
| `trans` | Private | reconciliation, transcript/document packets, handwriting processing, review projection |
| `trans-release` | Private | QA, independent approval correlation, release eligibility |
| `trans-downstream` | Private | bounded projection, destination planning, dry-run delivery receipts |

## Public Scholarly Repositories

| Repository | Expected Visibility | Note |
|---|---:|---|
| `trans-latin` | Public | Intentionally public scholarly translation objects. |

## Private Review Repositories

| Repository | Expected Visibility | Note |
|---|---:|---|
| `Trans-heb` | Private | Public scholarly eligibility remains unresolved; do not present it as public until separately reviewed and reclassified. |

## Public-Repo Rule

Public repositories should contain only sanitized public material: documentation, research summaries, demonstrations, portfolio material, public scholarship, intentionally public translation objects, and coordination notes.

Public repositories should not contain:

- secrets or credentials;
- private source documents or page images;
- unrestricted OCR or transcripts;
- private storage pointers or signed URLs;
- sensitive collection workflows;
- private infrastructure details;
- operational instructions that exceed the public research boundary;
- claims of automated authority, identity, authorship, authenticity, approval, or delivery that are not supported by the current repository contracts.

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
2. Review any public/private classification mismatch immediately.
3. Confirm public project summaries remain sanitized and current.
4. Confirm public scholarly repositories contain only intentionally public materials.
5. Confirm private-review repositories remain private until separately cleared.
6. Confirm headline docs do not carry forward superseded milestones as current state.
7. Confirm raw payload retention and external delivery are not described as enabled unless separately authorized and evidenced.
8. Update classifications when repository roles genuinely change.
