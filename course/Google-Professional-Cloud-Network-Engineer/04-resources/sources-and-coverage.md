# Sources and coverage — Professional Cloud Network Engineer

Everything in this folder is original writing. The sources below were used to establish the exam's **published format and scope**, never as a source of item text.

## Primary sources

| Purpose | Reference |
|---|---|
| Certification page (length, fee, format, languages, prerequisites, assessed abilities, renewal pointer) | https://cloud.google.com/learn/certification/cloud-network-engineer |
| Exam guide (six sections, objectives, and their weights) — 24 April 2026 revision | https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf |
| VPC overview and network tiers | https://cloud.google.com/vpc/docs/vpc |
| Network service tiers | https://cloud.google.com/network-tiers/docs/overview |
| Shared VPC | https://cloud.google.com/vpc/docs/shared-vpc |
| VPC Network Peering | https://cloud.google.com/vpc/docs/vpc-peering |
| Network Connectivity Center | https://cloud.google.com/network-connectivity/docs/network-connectivity-center |
| Private Service Connect | https://cloud.google.com/vpc/docs/private-service-connect |
| Private services access | https://cloud.google.com/vpc/docs/private-services-access |
| Serverless VPC Access and Direct VPC egress | https://cloud.google.com/vpc/docs/serverless-vpc-access |
| Private Google Access | https://cloud.google.com/vpc/docs/configure-private-google-access |
| Subnet expansion | https://cloud.google.com/vpc/docs/create-modify-vpc-networks |
| MTU sizing | https://cloud.google.com/vpc/docs/mtu |
| Bring your own IP and privately used public IPs | https://cloud.google.com/vpc/docs/ip-addresses |
| Cloud NAT | https://cloud.google.com/nat/docs/overview |
| Cloud Router and dynamic routing mode | https://cloud.google.com/network-connectivity/docs/router/concepts/overview |
| Policy-based routes | https://cloud.google.com/vpc/docs/policy-based-routes |
| Dedicated Interconnect | https://cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview |
| Partner Interconnect | https://cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview |
| Cross-Cloud Interconnect | https://cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview |
| MACsec for Interconnect | https://cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec |
| HA VPN | https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview |
| Classic VPN | https://cloud.google.com/network-connectivity/docs/vpn/concepts/classic-topologies |
| BGP and MED on Cloud Router | https://cloud.google.com/network-connectivity/docs/router/how-to/configure-bgp |
| Bidirectional Forwarding Detection | https://cloud.google.com/network-connectivity/docs/router/how-to/configure-bfd |
| Cloud Load Balancing overview | https://cloud.google.com/load-balancing/docs/load-balancing-overview |
| Backend services and health checks | https://cloud.google.com/load-balancing/docs/backend-service |
| Network endpoint groups | https://cloud.google.com/load-balancing/docs/negs |
| Traffic management on Application Load Balancer | https://cloud.google.com/load-balancing/docs/https/traffic-management |
| GKE Ingress and Gateway controllers | https://cloud.google.com/kubernetes-engine/docs/concepts/ingress |
| Cloud CDN | https://cloud.google.com/cdn/docs/overview |
| Cloud CDN cache invalidation | https://cloud.google.com/cdn/docs/invalidating-cached-content |
| Cloud DNS overview | https://cloud.google.com/dns/docs/overview |
| Cloud DNS routing policies | https://cloud.google.com/dns/docs/routing-policies-overview |
| Cloud DNS forwarding and peering | https://cloud.google.com/dns/docs/zones/forwarding-zones |
| DNSSEC | https://cloud.google.com/dns/docs/dnssec |
| GKE networking overview | https://cloud.google.com/kubernetes-engine/docs/concepts/network-overview |
| GKE Dataplane V2 | https://cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2 |
| GKE IP masquerade | https://cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent |
| VPC Flow Logs | https://cloud.google.com/vpc/docs/flow-logs |
| Firewall rules logging and Firewall Insights | https://cloud.google.com/network-intelligence-center/docs/firewall-insights |
| Network Intelligence Center | https://cloud.google.com/network-intelligence-center/docs |
| Connectivity Tests | https://cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview |
| Performance Dashboard | https://cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/overview |
| Network Analyzer | https://cloud.google.com/network-intelligence-center/docs/network-analyzer/overview |
| Flow Analyzer | https://cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview |
| Network Topology | https://cloud.google.com/network-intelligence-center/docs/network-topology/overview |
| Cloud Armor security policies | https://cloud.google.com/armor/docs/security-policy-overview |
| Cloud Armor preconfigured WAF rules | https://cloud.google.com/armor/docs/waf-rules |
| Adaptive Protection | https://cloud.google.com/armor/docs/adaptive-protection-overview |
| Bot management | https://cloud.google.com/armor/docs/bot-management |
| Cloud NGFW overview and tiers | https://cloud.google.com/firewall/docs/firewalls |
| Hierarchical firewall policies | https://cloud.google.com/vpc/docs/firewall-policies |
| Network firewall policies | https://cloud.google.com/firewall/docs/network-firewall-policies |
| Secure tags | https://cloud.google.com/iam/docs/tags-access-control |
| Secure Web Proxy | https://cloud.google.com/secure-web-proxy/docs/overview |
| Packet Mirroring | https://cloud.google.com/vpc/docs/packet-mirroring |
| VPC Service Controls | https://cloud.google.com/vpc-service-controls/docs/overview |

## Verified exam facts

| Fact | Value |
|---|---|
| Domains and weights | 1) Designing and planning a Google Cloud VPC network ~21%; 2) Implementing a VPC network ~20%; 3) Configuring managed network services ~16%; 4) Configuring and implementing hybrid and multicloud network interconnectivity ~16%; 5) Managing, monitoring, and troubleshooting network operations ~14%; 6) Configuring, implementing, and managing a cloud network security solution ~13% |
| Length | Two hours |
| Fee | $200 USD plus applicable tax |
| Question count | 50–60 multiple-choice and multiple-select questions (Google's published range) |
| Languages | English, Japanese |
| Prerequisites | None; Google recommends 3+ years of industry experience including 1+ year designing and managing solutions on Google Cloud |
| Case studies | None — the published format has no case-study component |
| Passing score | Not published by Google |
| Renewal | Described by Google only by reference to its Renewal FAQs; no duration or fee is restated here |
| Configuration objective | Present throughout — section 3 configures managed network services and section 6 configures security controls |

## Exam-guide objectives used for the study map

| Official section | Objectives in the guide | Local skills |
|---|---|---|
| 1. Designing and planning a Google Cloud VPC network (~21%) | 1.1 Designing an overall network architecture; 1.2 Designing VPC networks; 1.3 Designing a resilient and performant hybrid and multi-cloud network; 1.4 Designing for GKE | 1.1–1.11 |
| 2. Implementing a VPC network (~20%) | 2.1 Configuring VPCs; 2.2 Configuring VPC routing; 2.3 Configuring Network Connectivity Center; 2.4 Configuring and maintaining GKE clusters | 2.1–2.11 |
| 3. Configuring managed network services (~16%) | 3.1 Configuring load balancing; 3.2 Configuring Cloud CDN; 3.3 Configuring Cloud DNS | 3.1–3.8 |
| 4. Configuring and implementing hybrid and multicloud network interconnectivity (~16%) | 4.1 Configuring Cloud Interconnect; 4.2 Configuring a site-to-site IPSec VPN; 4.3 Configuring Cloud Router; 4.4 Configuring Network Connectivity Center | 4.1–4.8 |
| 5. Managing, monitoring, and troubleshooting network operations (~14%) | 5.1 Logging and monitoring with Google Cloud Observability; 5.2 Maintaining and troubleshooting connectivity issues; 5.3 Using Network Intelligence Center | 5.1–5.8 |
| 6. Configuring, implementing and managing a cloud network security solution (~13%) | 6.1 Configuring Google Cloud Armor policies; 6.2 Configuring and managing NGFW policies and VPC firewall rules; 6.3 Configuring and securing internet egress traffic using Public Cloud NAT and Secure Web Proxy; 6.4 Configuring self-managed network virtual appliance and Packet Mirroring | 6.1–6.8 |

Local skill IDs subdivide each objective into decision-level areas — tier choice, DNS topology, load balancer selection, IPAM, MTU, peering, routing, next hops, GKE networking, backend configuration, CDN, DNS policies, interconnects, BGP attributes, observability, and security controls. They are study aids, not Google objective numbers, and the mapping is one-directional: every local skill belongs to exactly one official section, and the section counts match the published weights.

## Coverage mapping

| Official section | Local domain | Local skills | Items per exam | Items in bank |
|---|---|---:|---:|---:|
| 1. Designing and planning a Google Cloud VPC network (~21%) | 1 | 1.1–1.11 | 21 | 126 |
| 2. Implementing a VPC network (~20%) | 2 | 2.1–2.11 | 20 | 120 |
| 3. Configuring managed network services (~16%) | 3 | 3.1–3.8 | 16 | 96 |
| 4. Hybrid and multicloud interconnectivity (~16%) | 4 | 4.1–4.8 | 16 | 96 |
| 5. Managing, monitoring, and troubleshooting network operations (~14%) | 5 | 5.1–5.8 | 14 | 84 |
| 6. A cloud network security solution (~13%) | 6 | 6.1–6.8 | 13 | 78 |
| **Total** | | **54 skills** | **100** | **600** |

The weights are approximate in Google's wording but total exactly 100%, so the item counts are the weights themselves. No rounding correction was applied and no tolerance band exists in the build: a revision that breaks the 100% total fails the build.

## What is deliberately not covered

- **Case studies.** Not part of the published format.
- **Console walkthroughs.** Configuration judgement is tested, but as a decision and its consequence, never as a click path. Nothing here needs a live project.
- **Hands-on labs and interactive item formats.** Not representable in a CSV, and not part of the published format.
- **Physical carrier procurement.** Circuit lead times, contracts and provider SLAs are referenced only where the exam guide tests the design choice, not as procurement advice.
- **Renewal-exam calibration.** This bank targets the standard exam; Google's renewal instrument is a separate paper with its own scope.

## Source discipline

- No question, option, or explanation is copied from any question-sharing site, braindump collection, or community forum. The ExamTopics listing for this exam was checked only for how items are *presented* — scenario length, "which should the team do" phrasing, and the multiple-select convention — never as a source of item text.
- Community statistics from such sites — question counts, self-reported pass rates, "same as the real exam" claims — are **not** used as evidence, benchmarks, or marketing claims anywhere in this course. No third-party pass mark is repeated.
- Where Google publishes a range (50–60 questions) or declines to publish a value (the passing score), this course repeats the range or says the value is unpublished. It never fills the gap with an estimate of its own.
- Product names follow the 24 April 2026 guide, including Cloud NGFW Essentials, Standard and Enterprise, Secure Web Proxy, Network Intelligence Center with Flow Analyzer, Network Connectivity Center, Private Service Connect, privately used public IP addresses and Cross-Cloud Interconnect. Names from earlier guides were not carried forward in place of current ones.
