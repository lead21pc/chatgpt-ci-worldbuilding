# Worldbuilding Control Toolkit

## 1. Problems this toolkit addresses

Long-running AI-assisted worldbuilding often fails in recognizable ways:

- drafts or simulations are silently promoted into established lore;
- assumptions become canon or project state without explicit confirmation;
- accumulated instructions cause a project to drift away from earlier constraints;
- the model expands beyond the requested operation into unsolicited synthesis, redesign, or closure;
- source authority—the declared rule for which source controls when sources disagree—becomes ambiguous across notes, drafts, files, and prior conversations;
- actor knowledge, authority, capability, and access are conflated during simulation;
- repeated instruction patches create duplicate or conflicting rules;
- large instruction sets become difficult to inspect and maintain without modular control.

This toolkit addresses those failures through four mechanisms:

- **Behavioral Custom Instructions (CI):** reusable instructions that constrain how an AI handles stage, evidence, project state, scope, and proposals. Here, `CI` means *Custom Instructions*, not Continuous Integration.
- **Modular worldbuilding control:** a small required core plus optional world-model, simulation, and audit modules.
- **Source auditing:** a structured comparison of claims, provenance, unresolved conflicts, and missing evidence without inventing a source hierarchy.
- **Scoped Codex workflows:** bounded local tasks with explicit inputs, permitted changes, validation, and stop conditions.

The architecture is the mechanism used to prevent these failures. It is not the reason a reader must adopt every component.

## 2. Who this is for

> This toolkit is intended for users who maintain long-running worldbuilding projects, care about canon/state integrity and source provenance, and have encountered instruction drift, scope drift, or simulation inconsistency. It is probably unnecessary for casual one-shot worldbuilding.

No particular world ontology, genre, writing application, model, or source format is required.

## 3. Quick start

1. Start with [`core/GENERIC_WORLDBUILDING_CI_CORE.md`](core/GENERIC_WORLDBUILDING_CI_CORE.md).
2. Add only the modules required by the task:
   - [`modules/WORLD_MODEL.md`](modules/WORLD_MODEL.md) for actors, systems, relations, capability, and authority;
   - [`modules/SIMULATION.md`](modules/SIMULATION.md) for causal trajectories and second-order effects;
   - [`modules/AUDIT.md`](modules/AUDIT.md) for source or system scrutiny.
3. Use [`profiles/FULL_PROFILE.md`](profiles/FULL_PROFILE.md) only when all advanced controls are useful.
4. Declare project terminology and source policy separately. If the project has no source hierarchy, do not invent one.
5. Test the chosen configuration in controlled conversations before relying on it in a long-running project.

The files are instruction text. They do not install themselves, alter an account, or guarantee identical behavior across models.

## 4. Repository components

```text
worldbuilding-ci-kernel/
├── README.md
├── LICENSE
├── core/
│   └── GENERIC_WORLDBUILDING_CI_CORE.md
├── modules/
│   ├── WORLD_MODEL.md
│   ├── SIMULATION.md
│   └── AUDIT.md
├── profiles/
│   └── FULL_PROFILE.md
└── examples/
    ├── minimal-example.md
    └── full-example.md
```

The core owns general interaction behavior. Modules add specialized reasoning without redefining core invariants. The full profile declares a composition; it is not a second copy of every rule.

## 5. Worldbuilding CI usage levels

### Minimal — CORE only

Use for focused lore discussion, terminology clarification, project-state updates, and ordinary analysis. It does not require actor simulation, institutional modeling, a causal-chain trace, or a deep audit checklist.

### Advanced — CORE plus selected modules

Add only what the current workflow needs. Common combinations include:

- `CORE + WORLD_MODEL` for actor, institution, or system reasoning;
- `CORE + SIMULATION` for a causal question that does not require a detailed social ontology;
- `CORE + WORLD_MODEL + SIMULATION` for actor/system trajectories;
- `CORE + AUDIT` for source or consistency scrutiny.

### Full — FULL_PROFILE

The full profile composes `CORE + WORLD_MODEL + SIMULATION + AUDIT`. It preserves the strongest advanced behavior but adds cognitive and instruction load. It is not the universally recommended configuration.

## 6. Codex skills

A **Codex skill** is a reusable local instruction package that tells Codex how to perform a workflow, such as auditing sources, executing one approved milestone, or reviewing a completed change. Skills can apply the toolkit consistently across repeated repository tasks, but they are optional and are not bundled in this package.

Useful skill patterns include:

- a source-audit skill that reads declared sources, reports conflicts and unknowns, and never silently chooses authority;
- a scoped execution skill that changes only an approved unit of work and stops after verification;
- a review skill that inspects a completed package without automatically rewriting it.

CI controls model behavior inside the interaction. A skill controls how Codex carries out a local workflow. One does not replace the other.

## 7. Common workflows

### Simple lore discussion

Use `CORE`. Supply the relevant established project state and ask the focused question. See [`examples/minimal-example.md`](examples/minimal-example.md).

### Actor or system simulation

Use `CORE + WORLD_MODEL + SIMULATION`. Declare the starting state and material unknowns. The model must distinguish what actors know, what they can do, what they are authorized to do, and what effects follow.

### Source or system scrutiny

Use `CORE + AUDIT`; add `WORLD_MODEL` when the audit concerns actors, institutions, authority, or typed relations. Declare the files in scope and any project-defined source policy. The audit reports unresolved authority instead of inventing a winner.

### Full advanced configuration

Use `FULL_PROFILE` for work that repeatedly combines world modeling, simulation, and audit. See [`examples/full-example.md`](examples/full-example.md).

## 8. Advanced architecture

The package uses several terms that describe failure controls:

- **Epistemic control** means rules governing when a claim may change from assumption or inference into supported or established state.
- **Source authority** means a project-declared policy for deciding which source governs a disputed claim. The toolkit supplies no universal hierarchy.
- **Anti-drift control** means safeguards that prevent stage, scope, project state, or source authority from changing merely because instructions accumulate or a claim is repeated.
- A **router** is an optional instruction layer that selects the relevant sources or modules for a task. A router should route inputs without drawing conclusions or creating a competing source hierarchy.

Core precedence is:

1. establish whether state change is authorized;
2. identify the requested operation;
3. evaluate claim status only as that operation requires.

Modules extend this sequence. They do not grant themselves permission to activate, rewrite project state, or produce proposals.

## 9. Installation

No installer is required.

1. Copy the core into the instruction context supported by the chosen AI tool.
2. Append selected module text after the core, or provide the files together when the tool supports multiple attachments.
3. Keep project-specific source policy, terminology, and established state in separate project documents.
4. Check the tool's instruction-size limits before using the full profile.
5. Preserve the previous configuration so the change can be rolled back.

For Codex repository work, keep the package in a project directory and use scoped tasks that name the files allowed to change. This repository does not publish or install anything automatically.

## 10. Contributing

Contributions should identify the failure mode a rule prevents, its trigger, the incorrect interpretation, and the resulting behavior. A change should also state whether it affects core behavior or an optional module.

Please preserve these constraints:

- do not introduce a universal source hierarchy;
- do not add user-specific language defaults to the public core;
- do not duplicate full core rules inside modules;
- do not turn module terminology into a mandatory project schema;
- distinguish structural validation from observed model behavior;
- compare full-profile semantics with the source behavior after material changes.

The package is available under the [MIT License](LICENSE).
