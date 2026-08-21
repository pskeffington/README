# Repository and Evidence Architecture

## Purpose

This document defines how the `pskeffington` GitHub estate should be interpreted and maintained as a coherent scholarly portfolio. Repository count is not itself a portfolio objective. The goal is to preserve a small number of clear public anchors, a bounded set of supporting studies, private research systems where appropriate, and explicit consolidation or archival candidates.

## Classification model

Every repository should eventually receive one of five dispositions:

1. **Anchor** — a principal public research or portfolio surface that demonstrates a major capability and should receive active maintenance when substantive work advances.
2. **Supporting study** — a bounded research project that contributes evidence, methods, or a specific scientific domain to an anchor.
3. **Private research system** — a restricted or multi-repository workflow whose public representation should remain sanitized and non-operational.
4. **Utility / administrative repository** — supports CV generation, job tracking, contacts, websites, or internal workflow but should not be counted as scientific evidence.
5. **Consolidation / archive candidate** — experimental, duplicate, tiny, superseded, or weakly differentiated work that should not receive activity-only commits.

## Tier 1 — Public anchors

### CART-TRACE

**Role:** principal translational-health data-science anchor.

Demonstrates longitudinal patient-data modeling, treatment-relative episode reconstruction, provenance, missingness, care transitions, utilization measures, synthetic validation, and research governance around CAR T-cell therapy.

Expected evidence objects include episode schemas, synthetic trajectories, transformation rules, transition/utilization outputs, validation reports, provenance artifacts, and research-method documentation.

### README

**Role:** public portfolio governance and status surface.

Demonstrates repository governance, research classification, evidence boundaries, current program state, and portfolio-level documentation. It should not become a duplicate technical repository.

### CV-Public-Facing

**Role:** public professional evidence surface.

Should synthesize verified credentials, research projects, publications/presentations, and demonstrable technical capabilities from authoritative private or public evidence sources. It should not become an independent research program.

## Tier 2 — Supporting biomedical and public-health studies

These repositories should remain independently interpretable but feed validated evidence into the broader portfolio rather than competing to be primary anchors.

| Repository | Evidence lane | Primary reusable evidence object |
|---|---|---|
| `ECG-denoising` | biomedical signal evaluation | `benchmark_result` |
| `pet-noise-radiomics-robustness` | imaging robustness | `radiomics_stability_result` |
| `cancer-eol-death-place-typologies` | health-services research | `county_year_typology` |
| `Public-Health-Emergency-Preparedness---Dartmouth-Health` | preparedness systems research | `preparedness_evidence_record` |
| `Gaza-WASH` | humanitarian secondary-data research | `source_bounded_indicator` |
| `Haiti-nippes` | regional public-health systems research | `regional_evidence_record` |
| `WASH` | environmental health and spatial equity | `wash_system_indicator` |

These objects should share a small common evidence envelope wherever practical:

```text
repository
research_question
object_type
object_id
source_provenance
observation_period
transformation_version
validation_status
uncertainty_or_missingness
claim_boundary
artifact_path
```

The common envelope is portfolio metadata, not a requirement that all scientific domains use the same analytic schema.

## Tier 3 — Private research systems

### TRANS

```text
ctl-injest
  -> Eagle-Eye
  -> trans
  -> trans-release
  -> trans-downstream
```

This remains a private, human-reviewed document-intelligence research system. Its public contribution is architectural and methodological evidence about provenance, review states, bounded evidence, release validation, and reproducibility. Private implementation details and source payloads should not migrate to public portfolio repositories.

Related repositories such as `trans-latin` and `Trans-heb` should be evaluated as supporting scholarly modules based on their current dependency role.

### Active private supporting research and civic systems

These repositories have substantive recent development and should **not** be treated as archive candidates solely because they are private or previously small:

| Repository | Current role | Public treatment |
|---|---|---|
| `Plymouth` | municipal GIS, provenance, civic-planning, and continuity research workspace | reference only at a generalized civic/GIS research level unless content is separately approved for public release |
| `Control` | portfolio validation, contract, state-transition, and bounded automation-policy research | expose only approved architecture/method summaries |
| `ml-lab` | pre-pilot ML-assisted, human-adjudicated healthcare-document review research | describe as proposed/pre-pilot research; do not imply empirical or clinical validation |
| `cipher-topology-lab` | reproducible computational-topology, randomness-diagnostic, and provenance research | preserve diagnostic/research boundaries; no cryptanalysis or security-certification claims |

Activity alone does not establish maturity, but current substantive code/research work is sufficient to remove these repositories from the consolidation queue. Their evidence should still pass normal validation and promotion gates before entering public CV or portfolio claims.

## Tier 4 — Utility and administrative repositories

Examples include:

- `CV`;
- `Applications-Jobs`;
- `Roladex-contacts`;
- `Public-Relations`;
- `skeffington-foundation-website`;
- `Portfolio` where it serves private evidence coordination and validation rather than a public research surface.

These repositories can be operationally important without being scientific portfolio anchors. Their maintenance cadence should be driven by actual workflow needs.

## Tier 5 — Consolidation and archive review queue

The following repositories should receive explicit dependency/content review before further routine maintenance:

- `from_air`;
- `from_land`;
- `from_sea`;
- `from_space`;
- `terra_firma`;
- `sky-station`;
- `sec-inner`;
- `zodiac`;
- `imperium-aeterna`;
- `MAGNIFICA-HUMANITAS`;
- `COMPREHEND-lan`;
- `resilient`;
- `ai-abuse-intelligence-lab`;
- `identity-abuse-lab-`;
- `authentication-audit-compiler`;
- `pre-eclampsia-and-maternal-health-outcomes`.

This classification does **not** mean these repositories should be deleted or archived automatically. It means they should not receive cosmetic commits until their relationship to an active program, dependency, publication, or portfolio capability is established.

The `from_air` / `from_land` / `from_sea` / `from_space` set should be reviewed as a cluster before maintaining four separate surfaces. Likewise, small governance, identity/AI-misuse, visualization, or symbolic-computation repositories should be consolidated only after dependency and unique-evidence review.

Large, historically significant, or independently mature repositories such as `St.-Bonaventure`, `McDowell-County-Commission-on-Aging-Inc.`, `Family_and_Economic_issues`, and `Practicum-Report` should be evaluated separately rather than merged into the research-core taxonomy by name or age alone.

`Best-Practices-Git` is a reusable public research-method standard rather than a primary scientific anchor. `kosher-eats-south-shore` is a non-core public utility/community-information project and should be maintained only when its user-facing information is actively supported.

## Evidence promotion model

Supporting repositories should promote only validated, bounded evidence to portfolio-level surfaces.

```text
raw/public source
  -> repository-specific transformation
  -> repository-specific validation
  -> bounded evidence object
  -> portfolio evidence envelope
  -> CV / public portfolio claim
```

A CV or portfolio claim should not precede the underlying evidence object.

### Minimum promotion criteria

Before a repository output becomes portfolio evidence, record:

- the scientific or research question;
- source/data provenance;
- transformation or analytic version;
- validation status;
- known uncertainty, missingness, or limitations;
- the exact supported claim;
- claims that remain unsupported;
- a stable artifact or repository path.

## Maintenance policy

Weekly repository review should prioritize:

1. anchor accuracy;
2. evidence promotion from supporting studies;
3. source and validation drift;
4. public/private boundary correctness;
5. consolidation decisions for unclassified repositories.

Commit recency should not be used as a proxy for project quality. Conversely, a repository with substantive new implementation or evidence work should not remain classified as archival solely because an older portfolio snapshot labeled it that way.

## Near-term consolidation work

1. Continue the portfolio evidence-envelope schema and validation work in the private `Portfolio` repository.
2. Add bounded evidence records from mature biomedical/public-health studies as their repository-specific validation gates pass.
3. Synchronize `CV-Public-Facing` only from evidence that passes promotion criteria.
4. Review the smallest private repositories in dependency clusters before deciding whether to retain, consolidate, or archive them.
5. Treat `Plymouth`, `Control`, `ml-lab`, and `cipher-topology-lab` as active private supporting systems while keeping public references generalized and claim-bounded.
6. Keep CART-TRACE as the principal translational-health narrative tying longitudinal data, biomedical measurement, public-health evidence, and reproducible research governance together.
