# Skeffington Repository Status

This repository is public by design. It provides a sanitized weekly status surface for project coordination, storyboard tracking, public scholarly translation objects, and repository governance.

## Status

Last automated update: pending first weekly scan.

| Area | Current State |
|---|---|
| Repository scan | Pending |
| Project status | Pending |
| Storyboard | Initialized |
| Security review | Pending |

## Repository Categories

The weekly scanner renders category counts after the first scan.

| Category | Current Rule |
|---|---|
| Operational | Private only. |
| Public scholarly | Public allowed when materials are intentionally shared for free scholarly use. |
| Public | Sanitized documentation, research, portfolio, demonstrations, or coordination notes only. |
| Private support | Non-operational private workspaces and drafts. |

## Operational Repositories

| Repository | Expected Visibility | Note |
|---|---:|---|
| Eagle-Eye | Private | Core operational repository. |
| trans | Private | Core operational repository. |

## Public Scholarly Translation Repositories

| Repository | Expected Visibility | Public Purpose |
|---|---:|---|
| trans-latin | Public | Translation objects retained for free scholarly use. |
| Trans-heb | Public | Translation objects retained for free scholarly use. |

## Active Workstreams

The weekly scanner updates this section from `data/project_status.json`.

| Project | Category | Visibility | Status | Last Activity | Notes |
|---|---:|---:|---:|---:|---|
| README | Public | Public | Active | Initial setup | Public weekly status surface. |

## Security Review

No public operational repository flags were detected in the last manual pass. The scheduled scan will update this after execution.

## Storyboard

Storyboard notes are maintained in [`docs/storyboard.md`](docs/storyboard.md). Weekly snapshots are written under [`docs/weekly/`](docs/weekly/).

## Repository Governance

Operational repositories should remain private. Public scholarly translation repositories may remain public for free scholarly use when they contain only intentionally public materials. Other public repositories should contain only sanitized documentation, demonstrations, research material, portfolio material, or public-facing coordination notes. If a repository is classified as operational and is found public, the weekly scanner flags it in this README and in the weekly snapshot.

## Automation

The weekly scan is defined in [`.github/workflows/weekly-repo-scan.yml`](.github/workflows/weekly-repo-scan.yml).

To scan private repositories, add a repository secret named `REPO_SCAN_TOKEN` with permission to read the target repositories and write contents to this repository. Without that secret, the workflow can only report on repositories visible to the default token.
