# Repository Security Review

## Current Controls

- The `README` repository is intentionally public and serves as the public status surface.
- Operational repositories are expected to remain private.
- The weekly scan flags configured operational repositories if they are public.
- The weekly scan checks operational repository names for Latin-safe naming.

## Current Operational Watchlist

| Repository | Expected Visibility | Note |
|---|---:|---|
| Eagle-Eye | Private | Core operational repository. |
| trans | Private | Core operational repository. |
| trans-latin | Review required | Public at last manual check; classified as operational-adjacent until confirmed otherwise. |

## Public-Repo Rule

Public repositories should contain only sanitized public material: documentation, research, demonstrations, portfolio material, and coordination notes. No secrets, operational instructions, live credentials, private infrastructure details, or sensitive collection workflows should be stored in public repositories.

## Weekly Review Steps

1. Confirm operational repositories remain private.
2. Review any `PUBLIC_OPERATIONAL_REPO` flag immediately.
3. Confirm public project summaries are sanitized.
4. Keep storyboard notes high-level and non-sensitive.
5. Update the operational watchlist if repository roles change.
