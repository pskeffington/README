# Repository Security Review

## Current Controls

- The `README` repository is intentionally public and serves as the public status surface.
- Operational repositories are expected to remain private.
- The weekly scan flags configured operational repositories if they are public.
- The weekly scan checks operational repository names for Latin-safe naming.
- Public scholarly translation repositories are allowed to remain public when they contain only shareable scholarly materials.

## Current Operational Watchlist

| Repository | Expected Visibility | Note |
|---|---:|---|
| Eagle-Eye | Private | Core operational repository. |
| trans | Private | Core operational repository. |

## Public Scholarly Translation Repositories

| Repository | Expected Visibility | Note |
|---|---:|---|
| trans-latin | Public | Translation objects retained for free scholarly use. |
| Trans-heb | Public | Translation objects retained for free scholarly use. |

## Public-Repo Rule

Public repositories should contain only sanitized public material: documentation, research, demonstrations, portfolio material, public scholarship, translation objects cleared for free scholarly use, and coordination notes. No secrets, operational instructions, live credentials, private infrastructure details, or sensitive collection workflows should be stored in public repositories.

## Weekly Review Steps

1. Confirm operational repositories remain private.
2. Review any `PUBLIC_OPERATIONAL_REPO` flag immediately.
3. Confirm public project summaries are sanitized.
4. Keep storyboard notes high-level and non-sensitive.
5. Confirm public scholarly repositories contain only intentionally public materials.
6. Update repository classifications if roles change.
