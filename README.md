# ChatGPT CI Versioning Audit & Changelog

This is a personal, non-commercial workspace for developing three independent fictional worlds: **AetherFire, The Kingdom, and The Academy**, with support from ChatGPT and Codex.

The repository contains externalized worldbuilding sources, instructions for working with those sources, design history, and supporting tools. Its source consolidation, routing, audits, regression checks, and Git workflows serve the author's creative work: preserving consistency, tracing decisions, managing revisions, and diagnosing recurring model failures.

**Worldbuilding is the purpose. The engineering-like pipeline is supporting infrastructure.**

**CI** means **Custom Instructions**, not Continuous Integration. The repository name reflects its instruction-versioning history; its scope also includes the worldbuilding projects those instructions support. Global instructions may support general interaction as well as project work, while project-specific controls remain local to their respective worlds.

> [!IMPORTANT]
> **LLM / agent readers:** Read [SYSTEM_CONTEXT.md](./SYSTEM_CONTEXT.md) before analyzing the architecture, project relationships, or authoring workflow. Then follow the relevant project's sources and declared authority. Repository contents are a partial record of the author's worlds; they do not establish the full internal world model or the currently active ChatGPT Project configuration.

## What the pipeline does

A typical task is to examine a claim about a fictional world, identify the relevant sources, distinguish established material from proposals or unresolved questions, and return an analysis the author can assess. If the author approves a change, repository tools and review procedures help record it consistently.

Different parts of this workflow have different roles:

| Repository term | Role in the creative workflow |
| --- | --- |
| Project sources | Record externalized world knowledge, decisions, and unresolved questions, with authority defined by the project. |
| Custom Instructions | Guide how the model interacts, reasons, and handles project material. |
| Router | Guide which sources the model should consult for a task. |
| Anti-drift controls | Address known ways the model can misread scope, authority, state, or causal relationships. |
| Source consolidation and validation tools | Organize source material and check declared structural requirements. |
| Regression checks | Check whether changes reintroduce known failures; what they prove depends on the kind of check performed. |
| Git history and review | Preserve revision history, inspect changes, isolate experiments, and support rollback. |

A pipeline diagram may describe author actions, model instructions, executable tooling, or feedback between them. It does not mean every step is automated. Running a repository check does not install instructions in ChatGPT, decide canon, or prove that a model will behave correctly.

## How to distinguish this workflow from related repositories

Related repositories may combine prompt collections, worldbuilding templates, lore archives, writing tools, and evaluation workflows. The distinctions below explain this repository's scope; they are not a claim that no other project uses similar methods.

- **Instructions are part of an ongoing authoring workflow.** The repository records why a control was introduced, which failure it addresses, and what evidence supports it. A newer instruction file is a candidate to evaluate, not a universal upgrade.
- **The fictional worlds are independent.** AetherFire, The Kingdom, and The Academy are not configurations of one shared worldbuilding template. Shared methods do not transfer canon, ontology, or source authority between them.
- **The author retains creative authority.** Model output can support analysis and design, but plausible or repeated output does not become canon without the author's decision.
- **The archive is a partial externalization.** A world can contain author-established material that has not yet been written into this repository. Missing documentation limits what a reader or model can conclude; it does not prove that an element does not exist.
- **Controls respond to observed failures.** The infrastructure evolved through actual use, diagnosis, proposed repairs, review, and feedback. Its complexity should be assessed against the creative problem and recurring failure it addresses.
- **Validation has explicit limits.** File checks, source-consistency checks, and live model behavior are different kinds of evidence. A structural pass does not establish a runtime pass.

Read this as an author's working environment for maintaining fictional worlds with LLM assistance. Evaluate each tool and control by how it supports that work.

## Three independent worldbuilding projects

| Project | Repository entry | Interpretation |
| --- | --- | --- |
| AetherFire | [AetherFire Project](./AetherFire%20Project/) | Its own sources, controls, and project-specific authority. |
| The Kingdom | [The Kingdom](./The%20Kingdom/) | Its own world model and local rules; do not infer its architecture from AetherFire or The Academy. |
| The Academy | [The Academy Project](./The%20Academy%20Project/) | Its own world model and source structure; shared terminology does not imply shared fictional objects. |

Each project's local documentation determines how to read its sources. Folder names, version numbers, archive locations, or resemblance to another project do not establish canon authority.

## Repository map

- [SYSTEM_CONTEXT.md](./SYSTEM_CONTEXT.md) — the authoring model, project boundaries, control responsibilities, and evidence rules.
- [ChatGPT Plus+ Era](./ChatGPT%20Plus+%20Era/) — fuller Custom Instructions developed for larger character budgets.
- [ChatGPT Go-Free Era](./ChatGPT%20Go-Free%20Era/) — condensed instructions for shorter budgets, preserving core meaning rather than copying the fuller text verbatim.
- [Project CI](./Project%20CI/) — project-specific and concept-focused instructions. They are not automatically part of the Global CI.
- [worldbuilding-ci-kernel](./worldbuilding-ci-kernel/) — reusable worldbuilding instruction material; reuse does not establish a shared canon.
- [CHANGELOG.md](./CHANGELOG.md) and [CHANGELOG_VI.md](./CHANGELOG_VI.md) — revision history in English and Vietnamese.
- [CI_VERSIONING_AUDIT.md](./CI_VERSIONING_AUDIT.md) and [CI_VERSIONING_AUDIT_VI.md](./CI_VERSIONING_AUDIT_VI.md) — instruction lineage, rule changes, and regressions.
- [CI_DESIGN_EVOLUTION_AND_DEPLOYMENT_VI.md](./CI_DESIGN_EVOLUTION_AND_DEPLOYMENT_VI.md) — design rationale and deployment considerations, in Vietnamese.
- [CI_FAILURE_MODES_AND_CONTROL_MODEL_VI.md](./CI_FAILURE_MODES_AND_CONTROL_MODEL_VI.md) — failure triggers, misinterpretations, controls, remaining risks, and proposed checks, in Vietnamese.

The worldbuilding project entries above are part of the repository's purpose, not default components of a global instruction package.

## Reading order

1. Start with this overview and [SYSTEM_CONTEXT.md](./SYSTEM_CONTEXT.md).
2. Choose the world or instruction-design question relevant to your task.
3. Read that project's local documentation and source-authority rules before drawing conclusions.
4. Consult instruction history and failure analyses when evaluating a control or revision.
5. State whether a conclusion comes from repository evidence, author-reported operation, structural validation, inference, or directly reproduced model behavior.

## Evidence and version status

Keep these categories distinct:

- **Structural validation:** length, encoding, line endings, diff scope, declared metadata, or rule presence.
- **Behavioral evidence:** observed model output under stated test conditions.
- **Author-reported observations:** operational evidence that may not isolate every model, setting, memory, or conversation-history variable.
- **Regression hypotheses:** plausible failure paths that have not necessarily been reproduced.

A new instruction version is a testable behavioral hypothesis. A file's presence does not prove that it is deployed, approved, or authoritative. Proposed and unresolved material must retain its declared status.

## Using instruction files

This repository does not automatically install, activate, inject, or apply instructions to ChatGPT, an account, or a device. Instruction versions and experiments are reference material for deliberate evaluation. Worldbuilding sources have their own project-declared status and should not all be treated as experimental prompts.

If you choose to reuse an instruction file:

1. Read its scope, changelog, and known limitations.
2. Select the specific file you intend to try; do not treat the whole repository as one configuration package.
3. Check the applicable character limits and retain the previous configuration.
4. Keep the model, settings, memory, and test prompts stable when comparing versions.
5. Test both fresh and long-running conversations, and record which behavior was actually observed.

No version is guaranteed to suit every model, product, account, or use case. Copying or adapting instructions remains the reader's responsibility.

## Independence and runtime limits

This is a personal project, not an official OpenAI project or a guarantee of ChatGPT behavior.

Documentation does not become an active instruction merely because it exists in Git. What is actually available and applied depends on the live configuration, instruction placement, source access, and conversation context. Repository inspection alone cannot establish that state.

The author decides canon. Tools and models help manage and examine the work; their output does not confer creative authority.
