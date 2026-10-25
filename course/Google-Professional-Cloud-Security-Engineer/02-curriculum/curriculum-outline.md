# Curriculum outline — Professional Cloud Security Engineer practice course

**Six 100-item mock exams · 600 original questions · 2-hour rehearsal or untimed first pass**

This outline turns the bank into a study sequence. Every exam is blueprint-weighted **25 / 22 / 23 / 19 / 11** — the published weights themselves, which total exactly 100% — so the order below is about scenario complexity and topic reinforcement, not about weighting.

Google publishes a **50–60 question range**, a **2-hour** length, **no prerequisites**, and **no case-study component**. A 100-item exam is deliberately larger, so treat the clock as a rehearsal of the published duration rather than a model of the live item count.

## Learning arc

| Phase | Exam | What it stresses | Study goal |
|---|---|---|---|
| Access | 1 | Cloud Identity, federation, service accounts, keys, impersonation, PAM, deny policies, hierarchy | Name the identity type and the scope of the grant before reading options |
| Boundary | 2 | Firewall hierarchy, layer 7, Cloud Armor, IAP, certificates, VPC-SC, VPN, PSC, NAT | Separate "who may reach this" from "what may cross the boundary" |
| Data | 3 | Sensitive Data Protection, de-identification, secret storage, CMEK/EKM, rotation, confidential computing | Decide who holds the key and what the reader is allowed to see |
| Operations | 4 | CVE scanning, admission control, patching, drift, flow logs, IDS, sinks, SCC findings | Prove a control with a record rather than a policy document |
| Compliance | 5 | Shared responsibility, Assured Workloads, Access Transparency, residency, evidence | Turn a clause into a control, an owner, and a testable artefact |
| Integration | 6 | Mixed scenarios across all five domains | Hold four constraints at once without collapsing them |

## Exam-by-exam study plan

### Exam 1 — Identity, service accounts, and the resource hierarchy (100 items)
- Official split: 25 / 22 / 23 / 19 / 11.
- Focus: Cloud Identity, third-party SSO over SAML, directory sync, the break-glass super administrator, lifecycle automation through the Admin SDK, Workforce Identity Federation, dedicated versus default service accounts, keys versus short-lived tokens, Workload Identity Federation with attribute conditions, impersonation, password and session policy, enforced 2-step verification, Privileged Access Manager, Role Recommender, IAM conditions and deny policies, Access Context Manager, folders, and organization policies.
- Target skill: decide which identity type the scenario needs before looking at the granted roles.

### Exam 2 — Firewalls, perimeters, and private connectivity (100 items)
- Focus: hierarchical firewall policy against project rules, layer 7 inspection and what layer 4 cannot see, Cloud Armor security policies and bot management, Identity-Aware Proxy, TLS termination and Certificate Authority Service, Secure Web Proxy and Cloud DNS security including DNSSEC and response policies, internal-only addressing, API restriction, Shared VPC, peering, tier isolation, VPC Service Controls with restricted virtual IPs, HA VPN, Interconnect, Private Google Access, Private Service Connect, and Cloud NAT.
- Target skill: say whether the constraint is about identity, network path, or boundary crossing — then choose the control that matches.

### Exam 3 — Sensitive data, keys, and confidential computing (100 items)
- Focus: Sensitive Data Protection discovery and saved inspect templates, redaction, pseudonymisation, format-preserving encryption and unsalted hashing, authorised views, uniform bucket-level access, IAM database authentication, Secret Manager and versioning, metadata server protection, OS Login, default encryption, CMEK, Cloud EKM, key import, rotation and revocation, Confidential VM and Confidential GKE, lifecycle rules and bucket lock.
- Target skill: separate "who may read this value" from "who can decrypt these bytes".

### Exam 4 — Automation, detection, and logging (100 items)
- Focus: CVE scanning in the pipeline versus after deployment, Binary Authorization dry-run and enforcement, hardened base images, VM Manager patching, Security Health Analytics custom modules, custom organization policy constraints, drift detection, VPC Flow Logs, Packet Mirroring, Cloud IDS, Log Analytics, dedicated log projects, Admin Activity versus Data Access logs, log sinks and aggregated sinks, Pub/Sub export to a SIEM, and Security Command Center findings with notification.
- Target skill: ask what record the control leaves behind before deciding it is effective.

### Exam 5 — Compliance controls and the shared responsibility model (100 items)
- Focus: the shared responsibility split, Assured Workloads against hand-configured regime settings, Access Transparency and Access Approval, location constraints against the multi-region default, control mapping, evidence retention, a named owner for each control, and the written scope boundary.
- Target skill: convert a regulator's sentence into one control, one owner, and one piece of evidence.

### Exam 6 — Threat detection, AI security, and regulatory evidence (100 items)
- Focus: mixed scenarios — short-lived credentials with attribute conditions, deny policies with access levels, a firewall hierarchy with local allows, perimeters with restricted VIPs, key import and rotation, in-use memory protection, CVE scanning with admission control, posture findings with prevention, a forensic timeline from Admin Activity plus Data Access logs, and a control mapping where every control has an owner.
- Recommended: attempt under a 2-hour timer with no notes, then review every explanation.
- Target skill: keep four simultaneous constraints distinct — identity, boundary, key custody, and evidence.

## Item formats and how to rehearse them

| Format | Per exam | How to practise |
|---|---:|---|
| Single-answer | 84 | Decide the constraint first, then eliminate options that solve a different problem |
| Multi-select | 16 | Count the required selections before reading options; reject "true but not asked" statements |
| Case study | 0 | Not part of this exam's published format, so not practised here |
| Sequencing | 0 | Not part of this exam's published format, so not practised here |

## Suggested eight-week schedule

| Week | Work | Deliverable |
|---|---|---|
| 1 | Study domain 1 objectives, take Exam 1 in two halves | Mistake log by local skill |
| 2 | Study domain 2 objectives, take Exam 2 untimed | One diagram: identity → boundary → workload |
| 3 | Re-read missed explanations from Exams 1–2, retake both timed | Two timed scores plus error categories |
| 4 | Domain 3, take Exam 3 | A data sheet: what is sensitive, who may read it, who holds the key |
| 5 | Domain 4, take Exam 4 | A detection sheet: control, record, who reads it |
| 6 | Domain 5, take Exam 5, then Exam 6 under a 2-hour clock | Timed score plus pace per item |
| 7 | Retake the weakest exam, re-read its explanations cold | A compliance mapping you can defend |
| 8 | Final pass over the 48-skill map | Readiness note, no score conversion |

## Scoring your own attempt

1. Score each item correct or incorrect; there is no partial credit for multi-select.
2. Group misses by local skill ID, not by exam number.
3. Classify each miss: unknown capability, misread constraint, plausible-but-wrong option, or rushed guess.
4. Only the last two categories improve with more practice tests; the first two need documentation study or hands-on work.
5. Re-attempt the same exam after a week before trusting an improvement.

Google does not publish a passing score for the Professional Cloud Security Engineer exam, so no percentage here converts to a pass mark and a practice percentage is not a scaled score.

## Time budget inside a 100-item exam

| Segment | Items | Suggested time (2-hour rehearsal) |
|---|---:|---:|
| First pass, single-answer | 84 | 75 minutes |
| Multi-select | 16 | 25 minutes |
| Review of flagged items | — | 20 minutes |

The live exam delivers 50–60 questions in 2 hours, which is a slower pace per item than this bank requires: 100 items in 2 hours is about 72 seconds each. Use the rehearsal to practise finishing early enough to review, not to model the real appointment minute for minute.
