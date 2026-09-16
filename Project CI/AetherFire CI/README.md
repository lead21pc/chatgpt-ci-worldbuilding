# AetherFire CI

> **Role:** independent Custom Instructions archetype and associated anti-drift routing assets for AetherFire.
>
> **Boundary:** this directory is not part of `AetherFire Project`, is not a canon/world-bible source, and does not import or merge the project's canon documents. The two directories may coexist in the same repository but remain independent artifacts with separate responsibilities.

Files in this directory define CI behavior, routing, compact instruction variants and task-scoped workflow overlays. Canon facts and reconciliation remain authoritative only within the separate `AetherFire Project` package.

## Active baseline

Updated 2026-09-16: v2.5/v3 add audit-mode routing (LOOKUP, BOUNDED_AUDIT, FULL_SOURCE_AUDIT) and require an escalation reason before loading reconciliation evidence, archives, superseded canon, or overlays.

- CI kernel: `AetherFire_CI_version_v2.5.md`
- Source router: `aetherfire_chat_anti_drift_v3.md`
- Economy/state-stabilization overlay: `aetherfire_anti_drift_interface_economy_state_stabilization.md`, loaded only for matching tasks and only after the source gate
- Canon open-issues register: `../../AetherFire Project/92_OPEN_ISSUES_CURRENT.md`

`aetherfire_chat_anti_drift.md` is an inactive historical router. Its embedded snapshot contains superseded canon and must not be used as the current baseline, fallback, or reference anchor. Old canon may be opened only for explicitly labeled provenance or comparison; current silence never reactivates it.
