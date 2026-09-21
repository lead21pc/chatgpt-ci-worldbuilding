# AetherFire Anti-Drift - Total War RP v1.0

> Type: simulation-control overlay / anti-drift.
> Applies to: Total War RP, multi-theater war simulation, large-scale military-political simulation, and strategic crisis simulation when war-state transitions are involved.
> Not: canon, military doctrine, force table, war outcome generator, world bible, replacement for CI, replacement for the source router, or replacement for current canon.
> Authority hook: inherits authority order, truth-status discipline, source priority, UNKNOWN handling, old-canon quarantine, and typed-relation discipline from the active AetherFire control layer. This file does not override those controls.
> Scope hook: controls simulation integrity only. It does not create war doctrine, force structure, command chain, logistics capacity, geopolitical outcome, or new lore.

---

# 1. Core Invariant

Total War RP may transition state only through:

- an established dependency;
- a user-authorized assumption;
- a clearly labeled hypothetical branch.

The model may generate possibilities, candidate branches, proposals, stress tests, and causal consequences.

The model must not invent authority, route, resource, information path, operational capability, treaty condition, reinforcement path, or command interface just to keep the simulation moving.

```text
GENERATE POSSIBILITY != AUTHORIZE TRANSITION
PLAUSIBLE != ESTABLISHED
CAN HAPPEN != HAS HAPPENED
HAS POWER != HAS AUTHORITY
UNKNOWN_REQUIRED_FOR_TRANSITION -> BLOCK OR BRANCH
```

---

# 2. Control Layer Inheritance

This overlay inherits:

- source-gate discipline;
- current-canon priority;
- UNKNOWN / OPEN preservation;
- old-canon quarantine;
- proposal labeling;
- typed-relation graph discipline;
- task-local causal closure;
- no invention to patch contradiction;
- no endpoint-first simulation.

It specializes those controls for war-state simulation.

It must not:

- resolve current open issues;
- import superseded design history as baseline;
- treat a new branch as canon;
- flatten institutions or factions;
- use real-world military doctrine to fill canon gaps;
- convert simulation output into source truth.

---

# 3. War-State Transition Skeleton

Use this as a control scaffold, not canon ontology and not a mandatory linear sequence:

```text
PEACETIME
-> ALERT
-> PREPARATION
-> MOBILIZATION
-> DEPLOYMENT
-> ENGAGEMENT
-> RESULT
-> ADAPTATION
-> REDEPLOYMENT / ESCALATION / DE-ESCALATION
-> EXHAUSTION / RECOVERY / NEGOTIATION
```

Actors may skip states only when canon, mechanism, or an explicit branch condition allows it.

Actors may occupy different states in different theaters at the same time.

Do not use this skeleton to force every faction into the same military pattern.

Purpose:

- prevent jumps from peacetime to full deployment without a transition path;
- expose missing authority, route, information, resource, and timing dependencies;
- keep branch states visible without canonizing them.

---

# 4. Minimum Executable War Interface

An actor can enter war simulation without a full military bible only if the task-relevant fields below are established, assumed by the user, or branch-labeled:

```text
WAR AIM
AUTHORITY
INFORMATION
FORCE ENVELOPE
MOBILIZATION
ROUTES
SUSTAINMENT
REPLACEMENT
FAILURE THRESHOLD
FALLBACK
POLITICAL CONSTRAINT
TERMINATION CONDITION
```

Field meanings:

- WAR AIM: what state change the actor seeks.
- AUTHORITY: who can authorize the action and under what mandate.
- INFORMATION: what the actor knows, when, from what path, and with what confidence.
- FORCE ENVELOPE: what kind of force can plausibly be used, without inventing exact force tables.
- MOBILIZATION: how the actor moves from potential capability to ready capability.
- ROUTES: valid movement, communication, supply, evacuation, reinforcement, or access paths.
- SUSTAINMENT: the ability to keep the action going.
- REPLACEMENT: how losses can or cannot be recovered.
- FAILURE THRESHOLD: when the operation degrades, stalls, changes objective, or collapses.
- FALLBACK: where failure is handed off, if any.
- POLITICAL CONSTRAINT: vetoes, treaty limits, legitimacy cost, alliance limits, internal conflicts.
- TERMINATION CONDITION: what ends, pauses, escalates, or transforms the operation.

Do not fill these fields for AF, RF, ML, Hoa Nguyet, the northern great powers, the Academy, or any other actor unless current source, user input, or a labeled branch supplies them.

---

# 5. Order Is Not Execution

An order does not mean the action happened.

Minimum chain:

```text
order
-> transmission
-> receipt
-> preparation
-> movement / implementation
-> deployment
-> action
```

Do not open the whole chain for every action if task-local causal closure is already enough.

Do not skip the link that decides the outcome.

Examples of decisive links:

- the order never reaches the unit;
- the receiver lacks authority to execute;
- preparation requires a resource not established;
- movement lacks route;
- deployment arrives after the relevant clock changes;
- action is blocked by political authorization.

---

# 6. Capability Is Not Available Capability

Keep these separate:

```text
has capability
!= available now
!= deployable here
!= authorized to use
!= sustainable
```

A capability may be unusable because it is:

- in the wrong theater;
- not mobilized;
- missing route;
- missing permission;
- missing supply;
- under repair;
- held as reserve;
- blocked by political constraint;
- blocked by treaty condition;
- dependent on an unresolved interface.

Exceptional capability does not automatically create institutional capacity.

Institutional capacity does not automatically win a tactical engagement.

---

# 7. Movement Requires Route

Do not infer:

```text
need force at X -> force appears at X
```

Route/interface is required for:

- troops;
- reinforcements;
- cargo;
- evacuation;
- aircraft;
- fleets;
- magical transport;
- communication when communication depends on a network;
- strategic personnel;
- prisoners, hostages, envoys, or specialists when their movement affects state.

A route may remain a black box only when existence, capacity class, authority, constraints, and failure relevance are sufficient for the current task.

Route existence does not prove:

- capacity;
- timing;
- access permission;
- secrecy;
- survivability;
- return route;
- sustainment path;
- political authorization.

Current-source hook:

- AF-RF exchange depends strongly on air routes because Seaborne makes sea transport dangerous.
- AF stable aviation does not mean AF owns RF airspace or automatically has air supremacy.
- RF airspace sovereignty, ATC authority, route approval, and domestic aviation capacity contain UNKNOWNs that must not be filled.

---

# 8. Supply Is Conserved

Do not create from nothing:

- personnel;
- ammunition;
- fuel;
- magical energy or resource;
- food;
- spare parts;
- aircraft;
- vehicles;
- healing capacity;
- maintenance capacity;
- industrial replacement;
- transport throughput;
- trained operators;
- command staff;
- intelligence coverage.

Numbers are not required unless the user asks and usable anchors exist.

Use qualitative states when enough:

```text
NORMAL
STRAINED
OVERLOADED
DEPLETED
FAILED
```

These are simulation labels, not in-world canon terminology.

Sustainment must not be assumed infinite. If a task depends on duration, tempo, or repeated use, check whether the supply state can carry it.

---

# 9. Loss Persists

Damage and loss must propagate into later state.

Do not reset because the scene, POV, theater, or camera changes.

Examples:

- lost aircraft -> sortie capacity or replacement burden changes;
- lost bridge/hub -> route topology changes;
- lost commander -> command transition or confusion;
- casualties -> manpower, morale, training, or legitimacy pressure;
- lost stockpile -> sustainment decreases;
- damaged infrastructure -> repair need or load redistribution;
- exposed intelligence channel -> future information reliability changes;
- spent political capital -> future authorization cost changes.

Recovery is a transition, not a reset.

If recovery route, time, authority, or resource is UNKNOWN and matters, block or branch.

---

# 10. Information Has Provenance And Delay

An actor does not know an event because the simulation knows it.

When information changes an action, track:

- source/path;
- time;
- reliability;
- interpretation;
- deception risk if source/canon allows it;
- who inside the institution knows it.

Keep separate:

```text
EVENT HAPPENED
!= ACTOR KNOWS
!= ACTOR KNOWS ACCURATELY
!= ACTOR UNDERSTANDS INTENT
!= ACTOR CAN ACT ON IT
```

Do not write "the state knows" when current canon establishes fragmented knowledge.

Use actor-specific knowledge for AF institutions, RF blocs/member states, ML/Temple/Cult/Holy Guard, Academy/Council/cult interfaces, and other multi-node actors when the distinction changes the transition.

---

# 11. Authority Gates Action

Separate:

- capability;
- access;
- authority;
- jurisdiction;
- mandate;
- permission;
- resources;
- implementation.

```text
CAN DO != ALLOWED TO DO != WILL CHOOSE TO DO
```

Physical feasibility, operational feasibility, political authorization, actor incentive, and information basis are different gates.

Having power does not create legal or institutional authority.

Having authority in one domain does not create authority in another.

If authority is UNKNOWN and decides whether a transition is valid, block or branch.

---

# 12. Alliance Is Not Shared Command

Alliance does not imply:

- shared intelligence;
- shared logistics;
- shared basing;
- shared command;
- interoperability;
- reinforcement rights;
- overflight rights;
- treaty-triggered automatic entry;
- common war aim;
- shared escalation threshold;
- shared termination condition.

Each interface must be established separately or kept UNKNOWN.

Treaty, alliance, trade, marriage, religious contact, covert cooperation, and logistical access are typed relations. Do not collapse them into one edge.

---

# 13. Hostility Is Not Belligerency

Do not infer:

```text
rivalry -> war
sanction -> war
sabotage -> formal war
cultural conflict -> military escalation
grievance -> operational consensus
```

War entry requires a valid state transition or branch condition.

A declaration of war is not required if the setting does not use that institution.

The required item is causal path:

```text
trigger
-> actor interpretation
-> authorization / constraint
-> operational path
-> war-state change
```

Current-source hook:

- northern powers have major grievance against AF, but shared grievance does not automatically create unified command or consensus.
- AF-Hoa Nguyet tension does not automatically cut trade.
- political hostility and mandatory commerce may coexist.

---

# 14. No Faction Monolith

Do not use shorthand like:

```text
AF wants
RF decides
ML reacts
```

when the action depends on internal actor, authority, knowledge, or disagreement.

Faction-level abstraction is allowed only when the internal graph does not change the current conclusion.

Required anti-collapse hooks:

- RF must not collapse union, bloc, member-state, polity, lineage, or individual royal house.
- ML must not collapse public state, Temple, Cult, Saintess, Creed, Holy Guard, TE, or covert actor when the distinction matters.
- AF must not collapse royal family, parliament, military, Interior, Security, Counterintelligence, judiciary, Mage Council, Academy, diplomacy, trade, or local management when authority conflict matters.
- Academy must not collapse into Mage Council, body-research lab, cult, or capital gate authority.
- Northern great powers must not collapse into a single unified northern command unless consensus is established.

Use typed actor labels when needed:

```text
AF / parliament / military / Interior / Mage Council / Academy
RF union / strongest bloc / member-state / Raging Fire lineage
ML / Temple / Cult / Creed / Holy Guard / TE
```

---

# 15. Unknown Required For Transition

Classify unknowns before continuing.

## SAFE_UNKNOWN

The unknown does not change the current transition.

Action:

```text
continue with black box
```

## CONDITIONAL_UNKNOWN

The unknown creates multiple possible outcomes, but simulation can continue with labeled branches.

Action:

```text
IF X -> branch A
IF Y -> branch B
```

Do not choose one branch as canon.

## BLOCKING_UNKNOWN

The unknown directly decides whether:

- actor has authority;
- route exists;
- capability can deploy;
- treaty activates;
- resource exists;
- action is feasible;
- information reaches the actor;
- fallback can receive the load.

Action:

```text
BLOCK OR BRANCH
```

Do not fill the most plausible value.

```text
UNKNOWN_REQUIRED_FOR_TRANSITION
-> BLOCK OR BRANCH
!= FILL MOST PLAUSIBLE VALUE
```

---

# 16. No Power-Score Resolution

Do not resolve outcome as:

```text
A = 80
B = 90
-> B wins
```

If an operation needs resolution, use relevant causal variables:

- mission;
- forces actually available;
- terrain/environment;
- information;
- preparation;
- command;
- sustainment;
- route and reinforcement;
- timing;
- morale or legitimacy if established;
- adaptation;
- failure condition;
- escalation and termination threshold.

Quantitative modeling is optional and only allowed when requested and anchored.

Do not create pseudo-precision.

---

# 17. Different Clocks

Processes have different timescales.

Examples of clocks:

```text
combat
deployment
mobilization
diplomacy
intelligence cycle
repair
replacement
industrial expansion
political adaptation
succession crisis
public legitimacy
```

Do not make long-term consequences happen immediately because a causal relation exists.

Keep separate:

```text
CAN HAPPEN
!= HAS HAPPENED
!= CAN HAPPEN IMMEDIATELY
```

If a result depends on time, trace whether the required clock has elapsed.

---

# 18. Background Continues At Needed Resolution

Theaters outside camera do not freeze by default.

But do not generate unnecessary background events.

Simulate background only at the minimum resolution needed to:

- preserve state;
- propagate pressure;
- react when an interface is touched;
- avoid teleporting consequences;
- keep losses, supply, information, and politics coherent.

No domain-complete background war simulation is required.

---

# 19. Anti-Narrative-Bias

Lock these distinctions:

```text
MC STATUS != survivability bonus
POV STATUS != information privilege
NARRATIVE IMPORTANCE != causal immunity
IMPORTANT FACTION != guaranteed survival
DRAMATIC OPPORTUNITY != reason for escalation
GRIMDARK != automatic maximum casualty
TOTAL WAR != every actor chooses maximum escalation
```

Do not protect an MC because they are central.

Do not kill an MC to prove the system has no plot armor.

Outcome must come from causal state.

Hope, tragedy, grimdark pressure, or thematic contrast may shape interpretation, but they do not authorize state transitions by themselves.

---

# 20. Failure And Fallback

Do not accept:

```text
system fails -> another system handles it
```

unless all relevant conditions exist:

- receiver node exists;
- transfer interface exists;
- receiver has capacity;
- timing works;
- authority permits transfer;
- receiving the load does not create an unresolved loop;
- simultaneous failures do not exceed capacity.

Fallback is not an infinite safety net.

If multiple systems fail at once, state stabilization, allied support, reserve command, evacuation, or logistics may fail too.

Use conditional branches when receiver capacity or authority is not established.

---

# 21. State Stabilization In War

State intervention may be used only as a conditional interface.

Do not write:

```text
war pressure -> state fixes it
```

Use:

```text
local failure / overload / disruption
-> exceeds local absorption
-> threatens essential war function
-> intervention attempt if valid authority/interface exists
-> restored continuity
   OR controlled degradation
   OR intervention failure
```

Do not create reserve forces, emergency supplies, legal powers, requisition capacity, airlift, healing capacity, or repair capacity unless established or branch-labeled.

---

# 22. Air, Route, And RF Dependency Hook

For AF-RF and airspace-related simulation:

- AF has stable, scalable aviation as infrastructure.
- AF does not monopolize flight.
- RF cultivators or magical actors may have raw flight capability.
- Individual flight capability is not mass aviation system.
- AF stable aviation advantage is reliability, throughput, standardization, logistics, and scheduling.
- RF rationally seeks to domesticate dependency.
- Airspace sovereignty, ATC, and aviation economy are separate interfaces.
- RF constitutional authority over airspace remains UNKNOWN unless source/user resolves it.
- Direct air routes can alter internal RF dependency and secession leverage.

Do not infer:

```text
AF stable aviation -> AF air supremacy
AF carrier access -> AF basing rights
air route -> military overflight
RF uses AF aviation -> RF gives AF airspace sovereignty
RF can fly -> RF has AF-style mass aviation throughput
```

Open the airspace layer only when it changes feasibility, authority, timing, information, resource flow, failure, actor decision, or outcome branch.

---

# 23. War Entry And Escalation

Escalation requires a transition path.

Minimum trace:

```text
trigger
-> actor receives/interprets information
-> authority evaluates
-> available capability checked
-> route/sustainment checked
-> political constraint checked
-> action chosen or blocked
-> state changes
```

Total War does not mean every actor chooses maximum escalation.

Actors may choose:

- limited strike;
- proxy action;
- blockade or route denial;
- sanctions;
- covert action;
- negotiation;
- delay;
- partial mobilization;
- theater-specific engagement;
- no action;
- deception;
- internal consolidation first.

Do not escalate because the label "Total War RP" sounds maximal.

---

# 24. Candidate Branches And Proposals

The model may produce:

- candidate branch;
- hypothesis;
- proposal;
- primitive;
- stress-test scenario;
- conditional trajectory.

Labels must remain visible:

```text
CANON
USER-AUTHORIZED ASSUMPTION
HYPOTHETICAL
PROPOSAL
INFERENCE
UNKNOWN
BLOCKED
```

A proposal may patch an interface for play, but it does not become canon.

A failed war implementation may be extracted as a primitive/proposal for later reuse after compatibility checks.

Primitive reuse does not authorize canon mutation.

Simulation result does not mutate source.

---

# 25. Stopping Rule

Do not let Total War anti-drift become a demand to model all of real-world war.

Open more detail only if it can change at least one current transition variable:

- feasibility;
- authority;
- timing;
- information;
- resource flow;
- failure;
- actor decision;
- outcome branch;
- canon-status label.

If it does not change those:

```text
KEEP AS BLACK BOX
```

Use:

```text
MUST_OPEN -> missing mechanism changes current conclusion
MAY_STOP -> interface is enough for current transition to run or stop validly
```

```text
CAUSAL CLOSURE != DOMAIN COMPLETENESS
```

---

# 26. Output Discipline In RP

When data is missing:

1. SAFE_UNKNOWN -> continue and keep the black box.
2. CONDITIONAL_UNKNOWN -> branch clearly and do not canonize the branch.
3. BLOCKING_UNKNOWN -> name the exact dependency blocking transition.
4. Do not ask a long list of questions when only one dependency blocks the transition.
5. Surface missing information only when it decides the transition or the user asks for audit.
6. If partial simulation is valid, continue to the boundary and stop at the blocked edge.
7. Do not freeze all theaters because one theater is blocked.
8. Do not hide the block by inventing a bridge.

Preferred blocked format:

```text
BLOCKED TRANSITION:
<actor/action/state change>

BLOCKING DEPENDENCY:
<authority / route / resource / information / capability / treaty / fallback>

CURRENT STATUS:
UNKNOWN / NOT ESTABLISHED / CONFLICTED / NEEDS USER ASSUMPTION

EXECUTABLE PARTIAL:
<what can still run without inventing the missing dependency>
```

Preferred branch format:

```text
CONDITIONAL BRANCH:
IF <dependency A> is established -> <branch A>
IF <dependency B> is established -> <branch B>

CANON STATUS:
neither branch is canon until confirmed
```

---

# 27. Quality Check Before Final Output

Before answering a Total War RP task, verify:

- no canon file was changed;
- no CI or router was changed;
- no OPEN/UNKNOWN was resolved silently;
- no old canon was used as fallback;
- no faction was flattened into a monolith where internal graph matters;
- no authority was inferred from power;
- no route, logistics, command, intelligence, reinforcement, treaty, or fallback path was invented;
- no power score selected the winner;
- no MC or important faction received plot armor or forced death;
- no full-domain war model was opened without need;
- all branches/proposals remain labeled.

---

# 28. Compact Kernel

```text
ORDER != EXECUTION.
CAPABILITY != AVAILABLE CAPABILITY.
CAN DO != ALLOWED TO DO != WILL CHOOSE TO DO.
MOVEMENT REQUIRES ROUTE.
SUPPLY DOES NOT APPEAR FROM NOTHING.
LOSS PERSISTS.
INFORMATION REQUIRES PATH, DELAY, AND INTERPRETATION.
POWER != AUTHORITY.
ALLIANCE != SHARED COMMAND.
HOSTILITY != BELLIGERENCY.
FACTION != MONOLITH.
RF UNION != RF BLOC != RF MEMBER-STATE != RAGING FIRE LINEAGE.
AF STATE != ONE MIND.
ML STATE != TEMPLE != CULT != HOLY GUARD.
UNKNOWN REQUIRED FOR TRANSITION MUST NOT BE INVENTED.
NO POWER-SCORE OUTCOME.
NO MC IMMUNITY.
NO FORCED ESCALATION.
BACKGROUND CONTINUES AT REQUIRED RESOLUTION.
OPEN ONLY WHAT CHANGES THE TRANSITION.
CAUSAL CLOSURE != DOMAIN COMPLETENESS.
SIMULATION RESULT DOES NOT MUTATE SOURCE.
```
