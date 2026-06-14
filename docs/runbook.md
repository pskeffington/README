# Weekly Status Runbook

## Purpose

This repository is the public status surface for repository governance, public scholarly translation objects, and high-level project coordination.

## Weekly Flow

1. Read `data/repo_policy.json`.
2. Scan repositories owned by `pskeffington`.
3. Classify repositories as operational, public scholarly, public, or private support.
4. Flag operational repositories that are public.
5. Render `README.md`.
6. Write a dated snapshot under `docs/weekly/`.
7. Commit the generated files back to `main`.

## Policy File

Repository classifications are maintained in `data/repo_policy.json`.

- `operational_repos` must remain private.
- `public_scholarly_repos` may remain public for free scholarly use.
- `public_status_repo` should remain public.

## Manual Run

Use GitHub Actions and run `Weekly Repository Scan` from the Actions tab.

## Private Repository Coverage

To include private repositories in the scan, add a repository secret named `REPO_SCAN_TOKEN` with read access to the target repositories and write access to this repository.

## Review Checklist

- Confirm `Eagle-Eye` is private.
- Confirm `trans` is private.
- Confirm public scholarly translation repositories contain only intentionally public materials.
- Review any `PUBLIC_OPERATIONAL_REPO` flag immediately.
- Keep public README text sanitized and high-level.
