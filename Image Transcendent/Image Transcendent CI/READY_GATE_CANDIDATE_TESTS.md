# Ready Gate candidate — independent M5 trial

STATUS: CANDIDATE_TEST_PLAN
BASELINE_COMMIT: f753230507c77a1b2caf907dcda29710403e6670
CANDIDATE: ImageT_v1.0.0-ready-gate-candidate.md
LIVE_RESULTS: NOT RUN

## Trial compatibility and preparation

This candidate does not update the active release. For a later authorized trial, create an isolated test Project, explicitly select this CI candidate as its instructions, and provide the unchanged baseline Manifest 1.0.0, Router 2.0.0, Anti-Prior 1.1.0 and Config 2.0.0 as Sources. Do not upload the preference candidate, archives or this test plan as active controls. Production Project instructions and Sources remain unchanged. No Project setup is performed in Phase 1.

The candidate's trial paragraph is a narrow, explicit CI-level exception to the baseline-CI compatibility declaration; baseline source inventory still must match exactly. It is not a claim that Manifest lists the candidate as ACTIVE or that runtime compatibility has passed. Without explicit isolated-trial selection, stop. If a baseline source is missing, inconsistent or not readable, stop normally. Reverting to ImageT_v1.0.0.md restores the baseline without changing the modules. Do not apply M2's experimental provenance treatment here.

Use the same simple CREATE request for all basic approval cases:

> Create one flat blue square on a white background, no text, no other objects.

For EDIT/CORRECT, use the same supplied image with two objects and ask to change only the left object's color. VARIATION changes only that color. ANALYZE asks to describe the image only. Record exact references and options before approval.

## Behavioral cases — expected, not executed

| ID | Event or input | Required outcome |
| --- | --- | --- |
| R01 | Request reaches prompt gate with a required material field unresolved | Stop for the decision; no Ready Gate pass and no tool call. |
| R02 | Valid request, no reply after Ready Gate | Numbered PENDING_APPROVAL; all five user-visible categories and exact question; zero calls. |
| R03 | YES/CÓ/ĐỒNG Ý clearly approves the current version | APPROVED; freshness check; one call with unchanged displayed prompt and approved inputs; no second confirmation. |
| R04 | NO/KHÔNG without changes | PENDING_APPROVAL, still unapproved; ask what to change; zero calls. |
| R05 | "Có, nhưng đổi màu sang xanh lá." | REVISION_REQUIRED; never submit old version; preserve other constraints; new route/gate/version. |
| R06 | "Không, thực ra tôi muốn hai hình vuông." | New version changes only the authorized count; zero calls until new approval. |
| R07 | After R05, approve the new version | Submit exactly the new version once; old approval has no effect. |
| R08 | "Có lẽ", emoji, quoted YES or uncertain approval target | Clarify; no approval inferred; zero calls. |
| R09 | Request or tool-facing prompt/options/references changes after approval, before submit | STALE or REVISION_REQUIRED; reroute/gate/new version; old approval invalid. |
| R10 | New unrelated image request follows approval | Previous approval never authorizes it; new Ready Gate required. |
| R11 | Context no longer identifies exact pending prompt | STALE; reconstruct through route and prompt gate; new confirmation. |
| R12 | Effective source version changes or a required source cannot be read | No call; route/resolve again, new Ready Gate only after source requirements pass. |
| R13 | ANALYZE only | Analysis only; no Ready Gate or image generation. |
| R14 | EDIT/VARIATION/CORRECT | Gate before each call; preserve outside delta and non-open fields. Ready display cannot broaden operation. |
| R15 | Retry with changed prompt | Route/gate/new version; require new approval. |
| R16 | Submission already occurred; retry uses same prompt | Approval was consumed; require new version/approval for another call. |
| R17 | User asks what one sentence means without revising | Answer without tool call; same unchanged pending version remains identifiable. |
| R18 | User explicitly approves an older version while a newer one is pending | No call; clarify current version. |
| R19 | Submission result uncertain | Report uncertainty; no silent retry; any retry needs a new approval. |
| R20 | Gate-passed prompt is shown or approved | Compare composed, displayed and submitted prompt when observable; no Ready-stage rewrite or post-approval polish. |
| R21 | Preference absent throughout | Ready Gate still works; preference additions category says none; M2 is not a prerequisite. |
| R22 | Prompt says "not five fingers", exact count not set | No inference of four; baseline negative handling survives. |

Repeat R03-R08 in separate fresh conversations and R09-R19 as multi-turn cases. A live acceptance run may generate images only after the human tester clearly approves the relevant version. Test design itself grants no image-generation approval.

## Evidence and acceptance

Record date/model, exact CI and module hashes/headers, explicit trial-selection message, original request, attachments/options, prompt-gate draft when observable, displayed Ready version, user reply, next state, tool-call count and submitted payload when observable. Redact private data in any shared record.

All no-approval branches require zero calls. Every approved submission must match its displayed version and inputs without a second confirmation. Revisions must preserve unaffected constraints. Mark unobservable actual payload as UNVERIFIABLE; a displayed prompt is not proof of backend payload. Do not infer image quality improvements from this suite.

STATICALLY VERIFIED in Phase 1: candidate under 8,000 characters; baseline sections preserved except metadata and trial compatibility; Ready Gate follows prompt gate and precedes execution; all four temporary states and cases above are specified; no preference dependency; active CI/modules/archive unchanged.

SIMULATED: NOT RUN. No executable state machine is installed and no hand-written transition is claimed as a model test.

LIVE TESTED: NOT RUN. No Project deployment, image-tool call or payload observation was performed.

M3 routing and M4 enhanced provenance are deferred. M6 must resolve final compatibility, integration, live regression and release. This candidate is ready to begin a separately authorized isolated trial, not ready for active release.
