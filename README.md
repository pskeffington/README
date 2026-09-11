# Skeffington Repository Status

This public repository provides a sanitized portfolio status surface for current research, software, public-health, infrastructure-resilience, and scholarly projects.

## Current status

Last status refresh: 2026-09-11

| Area | Current state |
|---|---|
| Accessible repositories scanned | 55 |
| Public repositories | 13 |
| Private repositories | 42 |
| Public operational flags | 0 detected |
| Portfolio posture | Active, evidence-preserving development |

## Portfolio direction

The portfolio is organized around evidence-preserving systems for public health, infrastructure resilience, clinical-data research, document analysis, geospatial work, and controlled local sensing. Each project has its own scope and review boundary; work is not automatically promoted between projects.

Private projects are summarized below at the group level. Sensitive implementation details, credentials, raw source material, operational procedures, and internal repository identifiers are intentionally excluded from this public page.

## Active private project groups

| Group | Public-safe summary | Current focus |
|---|---|---|
| Local sensing and resilient communications | Local-first, receive-only dashboards for authorized RF, aviation metadata, SDR, environmental inputs, and network-disjointed field use. | Aircraft/map presentation, source health, provenance, local history, and disconnected-operation validation. |
| Evidence and document intelligence | A multi-stage evidence workflow for source admission, visual/page evidence, bounded text processing, independent review, release validation, and downstream reporting. | Reproducibility, identity-bound handoffs, human review, fail-closed release boundaries, and browser-validated operator views. |
| Municipal health and continuity | Public-health, GIS, continuity-of-operations, environmental, communications, and accessibility planning for municipal decision support. | Data freshness, owner verification, emergency-continuity evidence, accessibility, and public-safe reporting. |
| Global public-health analytics | A separate dashboard lane for governed public-health source ingestion and regional analytical presentation. | Source freshness, bounded normalization, ingest monitoring, and production/browser validation. |
| Systems and hardware research | Private technical research into local compute, edge devices, signal processing, and reproducible hardware/software interfaces. | Hardware-grounded experiments, documentation, and validation before any release claim. |

## Selected active public projects

- [WASH](https://github.com/pskeffington/WASH) — alternative-water systems and locally repairable treatment architectures.
- [CART-TRACE](https://github.com/pskeffington/CART-TRACE) — synthetic-first reconstruction of post-infusion CAR-T hospital care trajectories.
- [Best-Practices-Git](https://github.com/pskeffington/Best-Practices-Git) — auditable learning, citation integrity, and evidence-ready AI research.
- [ECG-denoising](https://github.com/pskeffington/ECG-denoising) — reproducible biomedical signal-denoising review and benchmark.
- [pet-noise-radiomics-robustness](https://github.com/pskeffington/pet-noise-radiomics-robustness) — PET image-noise, radiomics stability, and model-reliability research.
- [cancer-eol-death-place-typologies](https://github.com/pskeffington/cancer-eol-death-place-typologies) — open-data cancer end-of-life geography research.
- [CV-Public-Facing](https://github.com/pskeffington/CV-Public-Facing) — public-facing professional profile and resume surface.

Older, dormant, exploratory, and primarily archival repositories are intentionally excluded from this active-project summary. Their existence does not imply current development or maintained release status.

## Research and safety boundary

Public repositories contain only intentionally public documentation, scholarly artifacts, demonstrations, or sanitized research material. Private repositories may contain controlled implementation work, but private status alone does not authorize collection, retention, publication, or operational use.

Analytical outputs are research or decision-support artifacts unless a project explicitly documents a separate authority, validation, and release process. They do not independently establish identity, authorship, incident status, legal authority, clinical advice, infrastructure readiness, or operational direction.

## Storyboard

Storyboard notes are maintained in [`docs/storyboard.md`](docs/storyboard.md). Weekly snapshots are written under [`docs/weekly/`](docs/weekly/).

## Automation

The weekly scan is defined in [`.github/workflows/weekly-repo-scan.yml`](.github/workflows/weekly-repo-scan.yml).

The default `GITHUB_TOKEN` authenticates the public owner scan. To include private repositories, add an explicit repository secret named `REPO_SCAN_TOKEN` with permission to read the target repositories. The scanner uses the authenticated `/user/repos` endpoint only when that explicit token is present.
