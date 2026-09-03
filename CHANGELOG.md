# Changelog

## v1.0

### Added

- Real-time hardware verification with missing-data disclosure.
- Three-part launch/existence validation using manufacturer data, physical identifiers, and an independent source.
- Raw specification extraction and side-by-side conflict reporting.
- Empirical Auditor role, command triggers, format precedence, exhaustive mode, and Vietnamese-only output.
- Three-source validation for important medical, legal, and technical claims.

## v2.0

### Added

- Senior Editor role with concise Vietnamese answers, short terminology definitions, and conclusion-first structure.
- Failure Scan and Expansion Options sections.
- Direct, natural, non-academic style rules.

### Changed

- Replaced the specialized empirical hardware protocol with a general compact editorial protocol.

### Removed

- Real-time hardware validation, raw-only extraction, command triggers, exhaustive output, and fixed source-count requirements.

## v2.1

### Patched

- Made conclusion-first behavior conditional on sufficient evidence.
- Made headings, lists, and Markdown conditional on readability.
- Added repetition limits, low-information reaction suppression, and terminology-precision exceptions.

### Changed

- Shifted from casual personality toward natural, dense, accuracy-first prose.

## v2.2

### Patched

- Compressed the v2 style rules.
- Added explicit fact, inference, and assumption separation.

### Changed

- Replaced detailed formatting instructions with general clarity and information-density constraints.

### Removed

- Fixed output anchor, simplification disclosure, everyday-example rule, and transition-pattern cap.

## v3.0

### Added

- Adversarial review of assumptions, contradictions, hidden costs, bias, and overengineering.
- Direct pragmatic-engineer style and explicit strength/weakness/uncertainty/trade-off separation.
- Clarification questions for unclear goals, constraints, and success criteria.

### Changed

- Replaced the Senior Editor and fixed output modules with a global critical-review architecture.

### Removed

- Sentence caps, Failure Scan, Expansion Options, and conclusion-first formatting.

## v3.1

### Patched

- Added Hybrid Architecture Reviewer + Pragmatic Engineer behavior.
- Added correctness, risk reduction, ROI, impact/likelihood ranking, and now/later/never prioritization.
- Limited clarification to missing information that could materially change the conclusion.
- Prevented unsolicited user summaries.

## v4.0

### Changed

- Limited assumption-challenging and hidden-cost analysis to material effects on a decision, conclusion, plan, or recommendation.
- Changed the role from Architecture Reviewer to Architecture Advisor + Reviewer.

## v5.0

### Added

- Evidence-first reasoning with observation, inference, assumption, and conclusion separation.
- Conditional alternatives for unresolved interpretations.
- Inform, Evaluate, and Audit response modes.
- Technical mechanism/trade-off/failure-mode handling and non-technical inference limits.
- Domain-matched style and time-sensitive verification.

### Changed

- Replaced global critical review with task-dependent response routing.
- Replaced rigid reviewer prose with natural information-dense output.

### Removed

- Hybrid Advisor persona, fixed ROI/risk ranking, and global harsh-critique behavior.

## v5.1

### Patched

- Added task scope and applicable truth scope.
- Made explicit user-defined model premises authoritative inside that model unless external evaluation is requested.
- Added conditional MECE analysis.

### Removed

- Explicit answer-first, topic-drift, and time-sensitive-verification rules.

## v6.0

### Added

- Second-brain objective focused on reasoning robustness.
- Exactly-one-mode routing with Inform/Evaluate/Audit defaults.
- Falsifying conditions for interpretations and non-trivial conclusions.
- Sentence-value and conditional-structure constraints.
- Initial Vietnamese personal-pronoun reduction rule.

### Changed

- Broadened scoped premise authority into a general stated-premise rule.

## v6.1

### Patched

- Distinguished objective claims from opinions and first-person observations.
- Added independent-chat context isolation.
- Selected response mode from the current message.
- Replaced pronoun deletion with subject-centered Vietnamese sentence construction.

### Fixed

- Removed the v6.0 conflict between independent-evidence agreement and blanket acceptance of stated premises.

### Removed

- Explicit non-trivial-conclusion falsifier, MECE, domain-style, and structure-threshold rules.

## v6.2

### Patched

- Added Vietnamese-first terminology with an exception when no real Vietnamese equivalent exists.

### Removed

- Explicit technical/non-technical handling sentence.

## v7.0

### Added

- Expanded operational definitions for claims, opinions, context, modes, epistemic states, ambiguity, and falsifiability.
- Restored technical/non-technical handling, non-trivial falsifiability, and conditional structure.
- Expanded Vietnamese subject and terminology rules.

### Changed

- Inform forbids evaluative framing and recommendations.
- Audit defaults to existing decisions and objective claims.

## v7.1

### Patched

- Moved Vietnamese subject and terminology rules to the top.
- Required Vietnamese terms whenever a Vietnamese word exists, including headings and lists.
- Added evidence-based conclusion updates and propagation of corrected premises.
- Added mandatory search for plausibly time-sensitive facts.

## v7.2

### Patched

- Allowed established English terms when a Vietnamese translation would mislead or be unnaturally translated.
- Added explicit preservation and case-by-case testing of plausible causes.
- Added domain-matched output for ordinary chat, technical discussion, worldbuilding, and fiction.

### Fixed

- Protected terminology accuracy and naturalness from v7.1’s over-broad translation requirement.

## v7.3

### Patched

- Reorganized evidence, updating, epistemic state, response mode, ambiguity, freshness, context, and style into named modules.
- Declared subject-centered Vietnamese the primary invariant and terminology the supporting invariant.
- Made remaining rules context-sensitive guardrails and placed correctness above style.
- Prevented a claim alone from forcing Audit mode.
- Allowed the smallest reasonable assumption when ambiguity is immaterial.
- Required verification before using externally checkable product/runtime capabilities, limits, versions, prices, policies, or current behavior as premises.
- Preferred provider documentation or direct product state for product claims and prohibited inferring unstated capability from adjacent features or plausible architecture.

### Changed

- Changed freshness from mandatory search to verification when recency could affect the answer.
- Scoped epistemic-state display and falsifying conditions to cases where they matter.
- Allowed limited judgment in Inform when needed.

## v7.3.1

### Patched

- Normalized end-of-file formatting by removing the final newline.

### Changed

- No CI semantic, rule, precedence, or architectural behavior changed from v7.3.

## v7.4

### Added

- Added an explicit `role → mode → reasoning → stance` pipeline so the role of a claim selects the response mode before reasoning determines agreement, qualification, uncertainty, or disagreement.
- Added a separate truth scope for user-defined frameworks, architectures, fictional systems, and conceptual models.
- Expanded technical discussion to require mechanisms, causal links, assumptions, trade-offs, failure modes, useful quantitative evidence, and conditions under which important conclusions stop holding.
- Expanded the current-information rule and retained the prohibition on inferring capabilities or limits from adjacent features when direct verification is needed.
- Allowed analogies, technical metaphors, dry humor, and irony when natural and useful.

### Changed

- Merged subject structure and terminology into one language module while preserving subject-centered Vietnamese as the default construction.
- Reframed claim handling around the claim's role in the current request; a claim still does not force Audit mode.
- Expanded Evaluate and Audit while keeping one primary response mode selected from the actual ask.
- Made epistemic-state separation conditional on whether correctness or decisions are affected.

### Removed

- Removed the explicit post-hoc pronoun-deletion guard and the named primary/supporting invariant hierarchy.
- Removed the explicit rule that conclusions change only with new facts, sources, or reasoning and that premise changes must propagate.
- Removed explicit cross-chat context isolation.
- Removed the provider-documentation/direct-product-state preference while retaining direct verification requirements.

### Fixed / Regression Protection

- Preserved correctness over style, viable alternatives when useful, and the rule that the presence of a claim alone does not select Audit.

## v6.3 converted

### Added

- Rollback-safe Free/Go Major distilled from v7.3 so a plan downgrade does not restore v6.2 semantics.

### Changed

- Compressed subject structure, terminology, evidence, updating, epistemic state, response modes, ambiguity, depth, and domain style into five rule blocks.
- Allowed English when clearly more recognizable or precise, while rejecting common use alone as sufficient justification.

### Deployment trade-offs

- Omitted explicit freshness, context-isolation, technical/non-technical, jargon, discriminator/falsifier, and correctness-over-style rules to meet the narrower character budget.

### Fixed / Regression Protection

- Preserved the post-hoc pronoun guard, evidence-based conclusion updates, viable alternatives, and claim-not-forcing-Audit behavior in the converted major.
