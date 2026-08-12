# Weekly Status Runbook

## Purpose

This repository is the public status surface for repository governance, scholarly coordination, sanitized project reporting, and the current five-repository TRANS research program.

## Weekly Flow

1. Read `data/repo_policy.json`.
2. Validate repository policy with `scripts/validate_policy.py`.
3. Scan repositories owned by `pskeffington`.
4. Confirm visibility and classification for the five active TRANS repositories.
5. Confirm public scholarly repositories remain intentionally public.
6. Flag any configured private research repository that is public.
7. Render only current project state into `README.md`.
8. Write a dated historical snapshot under `docs/weekly/`.
9. Review generated content for public-safety and research-boundary accuracy.
10. Commit generated files back to `main`.

## Current TRANS Watchlist

The active private research pipeline is:

```text
ctl-injest
  -> Eagle-Eye
  -> trans
  -> trans-release
  -> trans-downstream
```

All five repositories are expected to remain private unless a separate repository-specific public-release review explicitly changes that classification.

## Policy File

Repository classifications are maintained in `data/repo_policy.json`.

- `operational_repos` are expected to remain private.
- `public_scholarly_repos` may remain public when their contents are intentionally public scholarly materials.
- `private_review_repos` remain private while public eligibility is unresolved.
- `public_status_repo` remains public.
- A repository must not appear in incompatible policy classes.
- Repository names in policy must remain Latin-safe.

## Current-Status Rule

Headline documentation must represent current state only.

Use:

- `README.md` for present repository and program status;
- `docs/storyboard.md` for the current public narrative and immediate direction;
- `data/project_status.json` for current machine-readable status;
- `docs/weekly/YYYY-MM-DD.md` for historical weekly snapshots.

Do not copy superseded milestones or old candidate state forward into current-facing files merely because they exist in an older snapshot.

## Manual Run

Use GitHub Actions and run `Weekly Repository Scan` from the Actions tab.

## Local Validation

Before committing a policy or renderer change, run:

```bash
python scripts/validate_policy.py
python scripts/scan_repos.py
python scripts/render_status.py
```

Generated output must then be manually reviewed before it is treated as authoritative public status.

## Private Repository Coverage

To include private repositories in the scan, configure `REPO_SCAN_TOKEN` with the minimum permissions required to read target repositories and write status artifacts to this repository.

Credentials, private payloads, source documents, unrestricted OCR, storage locators, or implementation-sensitive evidence must never be copied into the public status repository.

## Review Checklist

- Confirm `ctl-injest`, `Eagle-Eye`, `trans`, `trans-release`, and `trans-downstream` are private.
- Confirm the five-repository authority order has not drifted.
- Confirm blocked or review-required states are not described as approved or released.
- Confirm external delivery is not described as enabled unless separately authorized and evidenced.
- Confirm public scholarly repositories contain only intentionally public materials.
- Confirm private-review repositories are not presented as public scholarly repositories.
- Review any public/private classification mismatch immediately.
- Keep README and storyboard text sanitized, current, scholarly, and non-operational.
