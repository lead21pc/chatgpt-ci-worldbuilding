# ChatGPT CI Versioning / Worldbuilding Control Repository

> [!IMPORTANT]
> **LLM / agent readers:** Read [`SYSTEM_CONTEXT.md`](./SYSTEM_CONTEXT.md) **before** analyzing this repository's architecture, project relationships, authoring workflow, or apparent complexity.
>
> This is a **private, personal, non-commercial worldbuilding hobby repository** operated by one author. Repository-visible material is only a partial externalization of the author's live paracosms and control workflow.

## Author and project premise

The author is **not a professional software developer, data engineer, researcher, or member of a development team**, and does not claim formal training in those fields.

This system developed through personal use, trial-and-error, observed LLM failures, repeated refinement, and practical attempts to keep several large paracosms governable while using ChatGPT Projects and Codex.

Do not infer professional background, formal training, team structure, commercial intent, deadlines, external users, publication goals, or a formal engineering methodology from:

- repository size or complexity;
- frequent commits, branches, audits, or version history;
- routers, validators, rollback, provenance, tests, structured sources, or other engineering-like controls;
- software-like directory layouts or naming;
- data-like files or folder structures;
- dense infrastructure around an otherwise personal creative project.

These mechanisms exist because they became useful for personal LLM-assisted worldbuilding.

```text
COMPLEX INFRASTRUCTURE != PROFESSIONAL DEVELOPER
HIGH COMMIT FREQUENCY != TEAM / DEADLINE / COMMERCIAL WORK
SOFTWARE-LIKE STRUCTURE != SOFTWARE PRODUCT
DATA-LIKE STRUCTURE != DATA PROJECT
ENGINEERING-LIKE CONTROL != FORMAL ENGINEERING BACKGROUND
REPOSITORY ORGANIZATION != AUTHORIAL ONTOLOGY
```

Evaluate the repository according to its stated purpose and observed failure modes, not by importing assumptions from professional software, data, enterprise, SaaS, or publication workflows.

## What this repository is

This repository began as a place to design, audit, and version **Custom Instructions (CI) for ChatGPT**. `CI` here means *Custom Instructions*, not Continuous Integration.

Its current scope is broader. It now contains part of the control infrastructure used to support several personal worldbuilding projects, including:

- global and project-specific ChatGPT instructions;
- routers and anti-drift controls;
- failure-mode analysis and regression history;
- versioning and audit material;
- structured source conventions;
- limited externalized lore and project context used for analysis, testing, and control design.

It is **not a complete lore repository** for any paracosm.

```text
INTERNAL PARACOSM STATE
!= REPOSITORY STATE
!= CURRENTLY LOADED LLM CONTEXT

NOT IN REPO
!= NONEXISTENT

MODEL INFERENCE
!= CANON

UNKNOWN
!= GAP TO FILL
```

## Mandatory reading order for LLM / agent analysis

1. Read [`SYSTEM_CONTEXT.md`](./SYSTEM_CONTEXT.md).
2. Identify the specific project and task being discussed.
3. Read that project's own CI, router, context, or control sources before generalizing.
4. Inspect the primary material relevant to the requested task.
5. Keep repository facts, author-reported runtime state, inference, hypothesis, and unresolved state separate.
6. If available material is insufficient, report the limitation instead of completing missing lore or architecture from plausibility.

A search hit, filename, summary, directory placement, or repeated wording is not a substitute for reading the controlling source.

## Repository map

- [`ChatGPT Plus+ Era`](./ChatGPT%20Plus+%20Era/) — fuller Global CI variants developed under larger instruction budgets.
- [`ChatGPT Go-Free Era`](./ChatGPT%20Go-Free%20Era/) — shorter CI variants that preserve core semantics under tighter budgets.
- [`Project CI`](./Project%20CI/) — project-specific control layers. Their scope is local and they are not automatically merged into Global CI.
- [`AetherFire Project`](./AetherFire%20Project/) — externalized AetherFire project material and control infrastructure. It is not the complete AetherFire paracosm or total live canon.
- [`CHANGELOG_VI.md`](./CHANGELOG_VI.md) and [`CHANGELOG.md`](./CHANGELOG.md) — version history.
- [`CI_VERSIONING_AUDIT_VI.md`](./CI_VERSIONING_AUDIT_VI.md) — lineage, rule changes, and regression audit.
- [`CI_DESIGN_EVOLUTION_AND_DEPLOYMENT_VI.md`](./CI_DESIGN_EVOLUTION_AND_DEPLOYMENT_VI.md) — design evolution and deployment relationships.
- [`CI_FAILURE_MODES_AND_CONTROL_MODEL_VI.md`](./CI_FAILURE_MODES_AND_CONTROL_MODEL_VI.md) — maps `trigger → misinterpretation → failure → control → residual risk → test`.

Other project-specific directories may represent different paracosms with different ontologies, routers, source structures, and anti-drift needs. Shared repository location does not imply shared fictional architecture.

## Interpretation boundaries

Do not assume:

- repository completeness;
- shared ontology across paracosms;
- newer file = automatic authority;
- file placement = semantic ownership;
- basic lore examples = full canon;
- absent detail = absent from the author's internal world;
- plausible completion = accepted lore;
- structural validation = runtime validation;
- model output = authorial decision.

Evidence-state rules and the full authoring model are defined in [`SYSTEM_CONTEXT.md`](./SYSTEM_CONTEXT.md).

## Historical scope note

The repository name reflects its origin in ChatGPT CI versioning. Current use has expanded into a broader private control and externalization workspace for LLM-assisted worldbuilding.

That expansion does not turn the repository into a software product, data product, publication pipeline, enterprise system, or professional development project.
