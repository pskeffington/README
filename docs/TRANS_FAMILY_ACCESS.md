# TRANS Family Cross-Access Registry

Current as of 2026-08-22. Default branch across the active family is `main`; coordinated documentation branch is `docs/trans-family-sync-2026-08-22` in every repo.

| Repository | Role | Default | Shared status branch |
|---|---|---|---|
| `pskeffington/ctl-injest` | intake/source admission | `main` | `docs/trans-family-sync-2026-08-22` |
| `pskeffington/Eagle-Eye` | visual evidence/review handoff | `main` | `docs/trans-family-sync-2026-08-22` |
| `pskeffington/trans` | central processing/HTR | `main` | `docs/trans-family-sync-2026-08-22` |
| `pskeffington/trans-release` | QA/release eligibility | `main` | `docs/trans-family-sync-2026-08-22` |
| `pskeffington/trans-downstream` | bounded projection/dry-run delivery planning | `main` | `docs/trans-family-sync-2026-08-22` |
| `pskeffington/trans-latin` | Latin scholarly authority | `main` | `docs/trans-family-sync-2026-08-22` |
| `pskeffington/Trans-heb` | Hebrew scholarly authority | `main` | `docs/trans-family-sync-2026-08-22` |
| `pskeffington/README` | public sanitized index | `main` | `docs/trans-family-sync-2026-08-22` |

```text
ctl-injest -> Eagle-Eye -> trans -> trans-release -> trans-downstream
                         |-> trans-latin
                         `-> Trans-heb
```

Current program state: H2 model-provenance propagation is merged in `trans`. Active hardening covers canonical Bentham R0 artifact identity, pinned TrOCR identity, and provenance self-digest validation before a real benchmark is admissible. No real Bentham performance claim is frozen.

Use the shared status branch for synchronized documentation review and `main` for accepted repository state.