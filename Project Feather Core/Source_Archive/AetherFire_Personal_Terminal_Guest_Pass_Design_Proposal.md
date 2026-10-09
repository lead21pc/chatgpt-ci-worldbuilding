# AetherFire — Personal Terminal & Guest Pass Design Proposal

> **Status:** DESIGN PROPOSAL / USER-DIRECTED WORKING DESIGN  
> **Scope:** personal terminal, technology extraction from Undie infrastructure, wearable body attachment, Guest Pass, prepaid guest wallet, device deposit, return/refund flow, vending/QR/service integration.  
> **Canon boundary:** This file does **not** automatically canonize unresolved AetherFire economy/access details. Existing `UNKNOWN` items remain `UNKNOWN` unless explicitly resolved by the user.

---

## 1. Design premises confirmed in this discussion

### 1.1 Undie technology can be reused as a technology source

The existing Undie subsystem already demonstrates that AetherFire can build a compact personal administrative terminal with:

- identity/user information;
- access/backend integration;
- contextual information;
- a retina-linked interface;
- low-profile/private audio;
- emergency communication;
- data/service interaction.

The current redesign should therefore treat Undie as a **technology source**, not as the ontology or policy template for the civilian/guest system.

```text
UNDIE TECHNOLOGY
→ extract useful human–system interface technologies
→ civilianize them
→ remove Undie-specific coercion/status/enforcement logic
→ reuse them in a general personal-terminal architecture
```

Important boundary:

```text
TECHNOLOGY TRANSFER
≠
POLICY TRANSFER
≠
STATUS TRANSFER
```

The following should not be imported automatically:

- Undie rank logic;
- coercive work control;
- enforcement rules;
- Credit Score;
- Credit Line;
- bare `credit` semantics;
- Undie-specific movement restrictions;
- class-specific command authority.

---

## 2. Personal Terminal

### 2.1 Core definition

The AetherFire personal terminal should not be designed as a miniature smartphone.

It is:

> **a removable body-attached personal terminal that acts as the user's interface to identity, access, payment and public/service infrastructure.**

```text
PERSONAL TERMINAL
=
hardware terminal
+ secure identity interface
+ service interface
+ private display interface
+ payment interface
+ access interface
```

The terminal itself is not the legal status, bank account, Guest Pass or access authority.

```text
TERMINAL
≠ IDENTITY SOURCE OF TRUTH
≠ STATUS
≠ ACCOUNT
≠ ACCESS AUTHORITY
```

It carries credentials and interfaces with the relevant backend systems.

---

## 3. Physical design — body-attached but removable

### 3.1 Form

The terminal must be wearable on the body, for example as:

- a wrist device;
- a bracelet;
- another compatible body mount.

The hardware should use a modular architecture:

```text
PERSONAL TERMINAL
│
├── Terminal Core
│   ├── processor
│   ├── secure credential module
│   ├── communication
│   ├── payment/service interface
│   └── private-display interface
│
└── Body Dock
    ├── wrist band
    ├── bracelet
    └── compatible alternate mount
```

The same terminal core may be transferred between compatible mounts.

### 3.2 Anti-theft requirement

The device must be removable by the legitimate wearer but should not be vulnerable to casual theft by someone passing nearby.

The design should therefore combine:

1. **physical retention**;
2. **wearer binding**;
3. **credential lock on unexpected detachment**.

Example:

```text
normal release
→ wearer authentication
→ clasp unlocks
→ device removed normally

unexpected removal / cutting / snatching
→ wearer session breaks
→ credential locks
→ payment locks
→ access credential locks
→ private information becomes unavailable
```

### 3.3 Safety breakaway

Anti-theft must not turn the device into a restraint.

If the terminal is caught by machinery, a vehicle or another dangerous force:

```text
force exceeds safety threshold
→ body dock breaks away
→ terminal detaches
→ credential immediately locks
```

Therefore:

```text
ANTI-THEFT
≠
PHYSICAL ENTRAPMENT
```

---

## 4. Technology extracted from Undie terminal infrastructure

### 4.1 Private retina interface

One of the most valuable technologies available for civilianization is the retina-linked terminal interface.

Possible civilian/guest architecture:

```text
Terminal
→ private retina interface
→ user sees personal UI
```

Suitable private information includes:

- identity data;
- route/navigation information;
- wallet balance;
- transaction confirmation;
- access permissions;
- messages;
- public-service instructions;
- emergency notices.

The public-facing part of the device can remain minimal.

### 4.2 Private audio

Undie technology already establishes low-profile/private audio capability.

The civilian terminal can adapt the same technological lineage into a removable, non-coercive private audio interface.

Exact implementation remains open.

### 4.3 Contextual interface

The terminal should inherit the useful design philosophy previously identified from The Kingdom POT:

> the user interacts with a unified terminal rather than manually opening separate applications for each backend service.

Example:

```text
user approaches transit gate
→ terminal prioritizes transit

user approaches vending machine
→ terminal prioritizes purchase

user approaches checkpoint
→ terminal prioritizes identity/access

user enters public-service office
→ terminal prioritizes relevant documents and procedure
```

The terminal is the interface layer, not the owner of every subsystem.

---

## 5. Guest Pass

### 5.1 Core concept

Guest Pass is inspired by Japanese prepaid IC-card usage, but expanded into an AetherFire temporary-service credential.

```text
GUEST PASS
=
temporary identity credential
+ temporary access profile
+ temporary service profile
+ interface to guest wallet
```

It is **not** a new legal status.

```text
GUEST PASS
≠ CITIZEN
≠ CIVIL
≠ CLASS
≠ SOCIAL HIERARCHY
```

### 5.2 Guest Pass is loaded into a Guest Terminal

At entry:

```text
FOREIGN VISITOR
→ identity verification
→ Guest Profile created
→ device deposit collected
→ Guest Terminal issued
→ Guest Pass credential bound to terminal
→ Guest Wallet activated
```

The terminal can then be worn as a wrist device or bracelet.

---

## 6. Separate the three financial/access objects

The system must distinguish:

```text
DEVICE DEPOSIT
≠
GUEST WALLET
≠
ACCESS PROFILE
```

### Device Deposit

Purpose:

- secures the physical terminal;
- creates an incentive to return it;
- is refundable when the device is returned normally.

### Guest Wallet

Purpose:

- prepaid spending;
- daily purchases;
- transit;
- vending;
- compatible services;
- QR/tap payments.

### Access Profile

Purpose:

- determines which places/services the guest may access;
- is not money;
- is not legal status.

---

## 7. Device deposit

### 7.1 Entry

The visitor pays a deposit at the border/entry point.

The system creates a deposit record:

```text
DEPOSIT RECORD

guest ID
terminal ID
currency of deposit
nominal amount
issue point
issue time
refund entitlement
```

### 7.2 Currency rule

The device deposit should not be converted into normal Guest Wallet spending value.

Instead, the deposit is locked in its original denomination.

Example:

```text
entry:
deposit = 500 units of country X currency

exit:
terminal returned
→ refund = 500 units of country X currency
```

This prevents the deposit from becoming an accidental foreign-exchange instrument.

Principle:

> **Refund the nominal amount in the denomination recorded when the terminal was issued.**

The exact settlement infrastructure remains a later economic-design problem.

---

## 8. Guest Wallet

The Guest Wallet should function similarly to a prepaid IC card.

Possible uses:

- public transport;
- vending machines;
- ordinary retail;
- food and daily necessities;
- approved public services;
- QR payment;
- tap/contactless payment.

The user experience should be simple:

```text
load value
→ spend
→ reload if needed
```

The user does not need to understand the full domestic financial system.

Important:

```text
GUEST WALLET
≠
DEVICE DEPOSIT
```

Unused Guest Wallet balance at exit is still **OPEN / NOT YET DECIDED**.

Do not assume that returning the terminal automatically refunds the remaining wallet balance.

---

## 9. QR payment

QR should be treated as a payment-request format, not as the money itself.

Example:

```text
merchant
→ creates payment request
→ QR

guest terminal
→ reads QR
→ privately displays:
   recipient
   amount
   purpose
   expiry

guest
→ confirms

payment backend
→ settles transaction
```

A QR may contain:

```text
recipient
amount
transaction reference
expiry
optional transaction metadata
```

It should not contain transferable stored money.

---

## 10. Vending machines

The personal-terminal architecture allows vending machines to remain simple.

Example:

```text
vending machine
→ advertises product/service data

terminal
→ displays private selection interface

user
→ selects
→ confirms payment

backend
→ PAYMENT_OK

machine
→ dispenses item
```

The vending machine should receive only the minimum claims it needs.

Example:

```text
PAYMENT_OK?
AGE/ACCESS_OK?
ITEM_PERMISSION_OK?
```

It should not automatically receive:

- full identity record;
- full status history;
- Credit Score;
- Contribution Points;
- full legal profile.

---

## 11. Return Machine

The return machine is an important part of the Guest Pass infrastructure.

Normal exit flow:

```text
Guest
→ inserts terminal into Return Machine
→ terminal ID verified
→ Guest Pass session closed
→ credentials revoked
→ local/private data sanitized
→ terminal returned to reissue pool
→ device deposit refund authorized
```

### 11.1 Atomic return principle

The process should not leave the guest in a state where:

```text
machine keeps terminal
+
refund disappears
```

The system should treat:

```text
terminal accepted
+
refund entitlement recorded/authorized
```

as one completed return transaction.

If cash/refund delivery fails temporarily, the refund claim remains recoverable through another terminal or staffed border counter.

---

## 12. Lost terminal

If a guest loses the terminal:

```text
guest reports loss
→ old device credential revoked
→ old device becomes unusable for payment/access
```

A replacement can then be issued.

Suggested logic:

```text
replacement terminal
→ new device deposit
→ Guest Profile re-bound
```

The original deposit remains attached to the original device-return condition unless later policy defines another process.

Exact lost-device accounting remains **OPEN**.

---

## 13. System architecture

```text
                     AETHERFIRE BACKEND
                            │
            ┌───────────────┼───────────────┐
            │               │               │
        IDENTITY          ACCESS          MONEY
            │               │               │
            └───────────────┼───────────────┘
                            │
                  PERSONAL TERMINAL
                            │
          ┌─────────────────┴─────────────────┐
          │                                   │
      BODY DOCK                          PRIVATE UI
   wrist / bracelet                       retina
          │
   secure removable
      anti-snatch
 emergency breakaway
          │
          ▼
       GUEST MODE
          │
          ├── Guest Pass
          │    ├── temporary identity
          │    ├── validity
          │    └── access profile
          │
          ├── Guest Wallet
          │    └── prepaid spending value
          │
          └── Device Deposit
               └── refundable on return
```

---

## 14. Exit flow

```text
visitor reaches exit point
→ Return Machine
→ verify terminal
→ terminate Guest Pass
→ revoke temporary credentials
→ sanitize terminal
→ return hardware to circulation pool
→ refund original device-deposit denomination
```

---

## 15. Explicit open points

The following are deliberately **not resolved** by this design:

1. exact physical appearance/material of the terminal;
2. exact wearer-authentication method;
3. exact retina technology implementation;
4. exact private-audio implementation;
5. exact terminal energy source;
6. exact settlement mechanism between foreign currency and AetherFire Credits;
7. exact Guest Wallet denomination;
8. treatment of unused Guest Wallet balance at exit;
9. lost/damaged-device accounting;
10. exact access matrix for foreign guests;
11. exact agencies responsible for identity, payment, access and terminal lifecycle;
12. exact privacy/data-retention law;
13. exact offline behavior;
14. exact device-deposit value by country/currency;
15. exact relationship with future revised Undie hardware.

---

## 16. Anti-drift constraints

```text
TERMINAL
≠ STATUS

GUEST PASS
≠ LEGAL CLASS

DEVICE DEPOSIT
≠ GUEST WALLET

GUEST WALLET
≠ CREDIT SCORE

ACCESS PROFILE
≠ SOCIAL HIERARCHY

UNDIE TECHNOLOGY EXTRACTION
≠ UNDIE POLICY TRANSFER

SHARED INTERFACE
≠ SHARED DATABASE
≠ SHARED AUTHORITY
```

Existing AetherFire `credit` ambiguity remains unresolved:

```text
bare "credit" on Undie terminal
≠ automatically Credits
≠ automatically Credit Score
≠ automatically Credit Line
```

The Guest Wallet should therefore use an explicitly named financial variable rather than inheriting the ambiguous Undie terminal field.

---

## 17. Design direction summary

The intended direction is:

> **AetherFire develops a general removable personal terminal by civilianizing mature human–system interface technology already demonstrated in the Undie infrastructure.**

For foreign visitors:

> **Guest Pass becomes a temporary identity/access profile loaded into a secure wearable terminal, while daily spending is handled through a prepaid Guest Wallet and the physical terminal is protected by a refundable device deposit.**

This creates a system that combines:

```text
prepaid IC-card convenience
+
temporary identity credential
+
access pass
+
personal terminal
+
private retina interface
+
QR/tap payment
+
return-and-refund lifecycle
```

without collapsing identity, access, legal status and money into a single variable.
