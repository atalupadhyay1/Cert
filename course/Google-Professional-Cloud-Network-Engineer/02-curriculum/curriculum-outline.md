# Curriculum outline — Professional Cloud Network Engineer practice course

**Six 100-item mock exams · 600 original questions · a two-hour rehearsal that runs slower than the live paper**

This outline turns the bank into a study sequence. Every exam is blueprint-weighted **21 / 20 / 16 / 16 / 14 / 13** — the published weights themselves, which total exactly 100% — so the order below is about decision difficulty and topic reinforcement, not about weighting.

Google publishes a **50–60 question range**, a **two-hour** length, **no prerequisites**, and **no case-study component**. A 100-item exam is deliberately larger, which has one consequence worth stating plainly: **the bank runs slower than the live exam per item.** 100 items in two hours is about **72 seconds per item**; the live 50–60 item paper allows roughly **120–144 seconds** each. Practise here under the two-hour clock and you will be training at a more generous pace than the appointment itself — useful for building explanation habits, not for simulating time pressure.

## Learning arc

| Phase | Exam | What it stresses | Study goal |
|---|---|---|---|
| Design | 1 | Tiers, HA and DR, DNS topology, load balancer choice, GKE and IP planning | State the constraint before naming a product |
| Build | 2 | Subnets, peering, Shared VPC, routing, next hops, NCC, GKE networking | Predict which object carries the packet |
| Services | 3 | Backend configuration, NEGs, traffic management, CDN, DNS policies | Choose the front door that matches the protocol |
| Connect | 4 | Interconnect, VPN, BGP attributes, advertisements, BFD | Separate the circuit from the session from the route |
| Operate | 5 | Logging, metrics, Connectivity Tests, insight tools, draining | Reach for evidence instead of a hypothesis |
| Secure | 6 | Cloud Armor, NGFW tiers and scope, segmentation, NAT, inspection | Bound the blast radius deliberately |

## Exam-by-exam study plan

### Exam 1 — VPC design, IP planning, and load balancer choice (100 items)
- Official split: 21 / 20 / 16 / 16 / 14 / 13.
- Focus: Premium versus Standard tier; HA, failover and DR design; hybrid DNS topology; load balancer selection from protocol, scope and backend; GKE address and control-plane planning; IAM for network roles including Shared VPC subnet use; private service connectivity through private services access, PSC and Serverless VPC Access; Shared VPC versus peering versus Network Connectivity Center; IPAM including IPv6, BYOIP, privately used public ranges and Private NAT; MTU sizing; third-party appliance insertion.
- Target skill: for every scenario, write the requirement as a constraint — latency, residency, overlap, budget — before naming a service.

### Exam 2 — VPC implementation, routing, and GKE networking (100 items)
- Focus: creating networks and subnets, peering options including custom route import and export, Shared VPC attachment, Private Google Access, subnet expansion, VPC Service Controls; static and dynamic routing, global versus regional dynamic routing, route priority, policy-based routes, an internal load balancer as next hop; Network Connectivity Center spokes and CIDR filters; GKE pod and service ranges, Dataplane V2, IP masquerade, network policy.
- Target skill: name the object that decides the packet — route, rule, proxy or peering — and then the setting inside it.

### Exam 3 — Load balancing, Cloud CDN, and Cloud DNS (100 items)
- Focus: backend services, health checks, balancing methods, affinity, draining; zonal, internet and serverless NEGs with autoscaling; URL maps, splitting, mirroring, rewrites; GKE Ingress and Gateway controllers; CDN origins, TTLs and invalidation; DNS zones, forwarding, peering, inbound policies, cross-project binding, geolocation, failover, DNSSEC and the external-dns operator.
- Target skill: choose the front door from the protocol and the backend type, then choose where the answer is cached or resolved.

### Exam 4 — Interconnect, VPN, and Cloud Router (100 items)
- Focus: Dedicated, Partner and Cross-Cloud Interconnect with VLAN attachments; MACsec and HA VPN over Interconnect; HA VPN and Classic VPN; BGP ASN, MED, custom advertisements, best path selection; BFD; 99.9% versus 99.99% topologies; NCC hybrid spokes and router appliances.
- Target skill: separate layer 1/2 (circuit and attachment) from layer 3 (session and route) before changing anything.

### Exam 5 — Observability, troubleshooting, and traffic movement (100 items)
- Focus: firewall, flow, NAT, DNS and VPN logging; metrics, alert policies, custom and log-based metrics, SLO burn; Connectivity Tests; Performance Dashboard; Firewall Insights; Network Analyzer; Flow Analyzer and Network Topology; comparing BGP state; draining a front end or a region.
- Target skill: choose the tool that answers the specific question, rather than the tool that is already open.

### Exam 6 — Cloud Armor, Cloud NGFW, NAT, and egress security (100 items)
- Focus: Cloud Armor edge and backend policies, preconfigured WAF rules, Adaptive Protection, DDoS defence, rate-based bans, bot management, threat intelligence; VPC firewall rules versus hierarchical, global and regional NGFW policies; Essentials, Standard and Enterprise tiers; layer 7 inspection; rule priority and secure tags; micro-segmentation; Cloud NAT address and port allocation; Secure Web Proxy; multi-NIC appliances and Packet Mirroring.
- Target skill: decide where the control must act — edge, proxy, VPC or host — and what each choice cannot see.

## Item formats and how to rehearse them

| Format | Per exam | How to practise |
|---|---:|---|
| Single-answer | 84 | Name the constraint first, then eliminate options that solve a different problem |
| Multi-select | 16 | Count the required selections before reading options; reject "true but not asked" statements |
| Case study | 0 | Not part of this exam's published format, so not practised here |
| Sequencing or drag-and-drop | 0 | Not part of this exam's published format, so not practised here |

## Suggested eight-week schedule

| Week | Work | Deliverable |
|---|---|---|
| 1 | Study section 1 objectives, take Exam 1 untimed | Mistake log by local study area |
| 2 | Sections 2 and 3, take Exams 2 and 3 untimed | One table: symptom → object → setting |
| 3 | Re-read missed explanations from Exams 1–3, retake Exam 2 timed | Timed score plus error categories |
| 4 | Section 4, take Exam 4 | A routing sheet: circuit → session → route → preference |
| 5 | Section 5, take Exam 5 | A troubleshooting sheet: question → tool → evidence |
| 6 | Take Exam 6 under the two-hour clock | Timed score plus pace per item |
| 7 | Retake the weakest exam, then re-read its explanations cold | One page of the decisions that settle most questions |
| 8 | Final pass over the 54-study-area map | Readiness note, no score conversion |

## Scoring your own attempt

1. Score each item correct or incorrect; there is no partial credit for multi-select.
2. Group misses by local study area, not by exam number.
3. Classify each miss: unknown product, misread constraint, plausible-but-wrong option, or rushed guess.
4. Only the last two categories improve with more practice tests; the first two need documentation study or hands-on work.
5. Re-attempt the same exam after a week before trusting an improvement.

Google does not publish a passing score for the Professional Cloud Network Engineer exam, so no percentage here converts to a pass mark and a practice percentage is not a scaled score.

## Time budget inside a 100-item exam

| Segment | Items | Suggested time (two-hour clock) |
|---|---:|---:|
| First pass, single-answer | 84 | 80 minutes |
| Multi-select | 16 | 22 minutes |
| Review of flagged items | — | 18 minutes |

The live exam delivers 50–60 questions in two hours, which is 120–144 seconds per item — noticeably more generous than this bank's 72 seconds. A comfortable finish here therefore does **not** prove you would finish the live paper quickly; it proves you can reason steadily. If you want time pressure, shorten the clock deliberately rather than assuming the bank provides it.

## What this course does not cover, on purpose

- **No case studies.** The published format has no case-study component.
- **No console recipes.** Configuration judgement is in scope and is tested as a decision — which mechanism, why, and what it costs — not as a click path. The test suite rejects console-instruction phrasing.
- **No labs or interactive items.** They cannot exist in a CSV and are not part of the published format.
- **No passing score.** Google does not publish one, so none is stated.
