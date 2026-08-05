# Storyboard

This file tracks the public-facing project narrative, milestones, and weekly direction without reproducing private implementation detail.

## Current Frame

The portfolio is moving from repository-by-repository prototypes toward governed, interoperable research components.

- `ctl-injest` remains the private intake and release-review boundary.
- `Control` remains the shared validation and routing authority.
- `Eagle-Eye` remains a private mixed-reality research surface.
- `trans` remains a private translation and document-processing workspace.
- The public `README` repository records only sanitized status, governance, and scholarly coordination information.

## Weekly Development

A secondary audio-ingestion lane has been scaffolded in `ctl-injest`. The current work is limited to transport-neutral metadata contracts, bounded transcript events, fail-closed validation, and audit-safe receipts. Capture hardware, raw-audio persistence, model execution, speaker identification, and display rendering remain outside the governance repository.

This separation establishes a research path from validated audio pointers to bounded transcript events while preserving source boundaries and human review.

## Current Milestone

**Milestone: governed multimodal intake foundation**

The immediate objective is to demonstrate that document and audio lanes can share governance principles without sharing payload handling or implementation-specific runtime dependencies.

Acceptance indicators:

- distinct document and audio intake contracts;
- no raw payloads in governance receipts;
- explicit partial, stable-partial, and final transcript states;
- bounded handoff eligibility rather than automatic downstream execution;
- synthetic tests covering accepted and rejected inputs;
- private operational repositories and sanitized public reporting.

## Next Frame

1. Review and validate draft pull request 37 in `ctl-injest`.
2. Run the audio-ingestion test suite in a normal checkout or CI environment.
3. Define a bounded transcript-event handoff contract for a simulated display adapter.
4. Keep transcription engines, microphone clients, and headset SDKs behind replaceable external adapters.
5. Expand repository classification before presenting account-wide public category totals.
6. Preserve scholarly framing, reproducibility notes, limitations, and human-review requirements in each repository README.

## Public Narrative Boundary

Public status text may describe research goals, contracts, validation, reproducibility, and governance. It must not expose credentials, private payloads, raw audio, restricted source text, personal tracking fields, implementation-sensitive runtime details, or claims of automated authority.
