# Skeffington Repository Status

This repository is public by design. It provides a sanitized weekly status surface for project coordination, storyboard tracking, and repository governance.

## Status

Last automated update: pending first weekly scan.

| Area | Current State |
|---|---|
| Repository scan | Pending |
| Project status | Pending |
| Storyboard | Initialized |
| Security review | Pending |

## Active Workstreams

The weekly scanner updates this section from `data/project_status.json`.

| Project | Visibility | Status | Last Activity | Notes |
|---|---:|---:|---:|---|
| README | Public | Active | Initial setup | Public weekly status surface. |

## Storyboard

Storyboard notes are maintained in [`docs/storyboard.md`](docs/storyboard.md). Weekly snapshots are written under [`docs/weekly/`](docs/weekly/).

## Repository Governance

Operational repositories should remain private. Public repositories should contain only sanitized documentation, demonstrations, research material, or public-facing coordination notes. If a repository is classified as operational and is found public, the weekly scanner flags it in the security section of the generated report.

## Automation

The weekly scan is defined in [`.github/workflows/weekly-repo-scan.yml`](.github/workflows/weekly-repo-scan.yml).

To scan private repositories, add a repository secret named `REPO_SCAN_TOKEN` with permission to read the target repositories and write contents to this repository. Without that secret, the workflow can only report on repositories visible to the default token.
