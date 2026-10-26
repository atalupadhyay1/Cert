# Google Professional Cloud Network Engineer — practice course

**6 mock exams × 100 original questions = 600 · 84 single-answer + 16 multi-select · every option explained · no case studies, because the exam has none · configuration judged, not recited**

This package is an independent study aid for the **Google Cloud Professional Cloud Network Engineer (PCNE)** exam. It is written for the engineer who has to decide *which* VPC topology, *which* load balancer, *which* routing mode, *which* interconnect and *which* firewall control fits a stated constraint — not for someone reciting product names.

> **Version notice.** Baseline: the official PCNE exam guide (24 April 2026 revision) and the certification page, retrieved **October 2026** — six sections weighted **~21 / ~20 / ~16 / ~16 / ~14 / ~13%**, **two hours**, **$200 USD** plus tax, **50–60 multiple-choice and multiple-select questions**, English and Japanese, **no prerequisites** (3+ years of industry experience including 1+ year designing and managing solutions on Google Cloud recommended), and **no published passing score**. The published format has **no case-study component**, so this bank contains **no case studies and no case-study documents**. Each practice exam here is 100 items, a deliberate **expanded bank**, not a replica of the live length — which means a set runs **slower** per item than the live paper (about 72 seconds against 120–144). Google notes that the exam guide governs the product names used, so re-check the guide before publishing or scheduling.

Independent educational content — not actual, recalled, or copied Google exam items. No Google endorsement, no import or publication guarantee, and no passing guarantee.

---

## What is inside

| Folder | Contents |
|---|---|
| `01-landing-page/` | Ready-to-paste course metadata, per-practice-test names and descriptions (full and trimmed), welcome and congratulations messages, allocation table, 54-study-area map, FAQ |
| `02-curriculum/` | Study arc, exam-by-exam plan, eight-week schedule, scoring method, two-hour time budget |
| `03-practice-sets/set-1…6/` | Per exam: instructor CSV, Markdown review copy, and a set README |
| `04-resources/` | Authoring source (`bank.py`, `terms.py`, `sources.py`, `questions/`), tooling, format spec, publication checklist, source notes, `SUMMARY.md` |
| `05-sample-upload/` | One twelve-question mixed sample (six single-answer, six multi-select, two items per domain) to test how the platform renders the format |

## The six exams

| Exam | Emphasis | Items |
|---:|---|---:|
| 1 | VPC design, IP planning, and load balancer choice | 100 |
| 2 | VPC implementation, routing, and GKE networking | 100 |
| 3 | Load balancing, Cloud CDN, and Cloud DNS | 100 |
| 4 | Interconnect, VPN, and Cloud Router | 100 |
| 5 | Observability, troubleshooting, and traffic movement | 100 |
| 6 | Cloud Armor, Cloud NGFW, NAT, and egress security | 100 |

Every exam uses the same blueprint split (21 / 20 / 16 / 16 / 14 / 13), so the emphasis column describes which part of each scenario set is densest in vocabulary, not a different weighting. All six domains are examined in all six sets.

## No case studies

Google's published PCNE format is "50-60 multiple choice and multiple select questions" with no case-study component. Accordingly:

- there is no `cases.py`, no `case-studies.md`, no case-embedded CSV variant, and no `case-study-upload-guide.md` in this folder;
- no stem begins `Case study —` and `validate.py` fails the export if one appears;
- `build.py`'s `check_source()` refuses to build if a case phrase reaches a stem or a rationale;
- `package.py` rejects the package if a case-study document is reintroduced.

The exam does include multiple-select items, so the CSV uses a five-option layout for those (two correct indices, three distractors) and a statement of the selection count in the stem — the same 17-column contract Udemy expects.

## Configuration is in scope, and judged rather than recited

PCNE cannot avoid configuration judgement: section 3 is entirely about configuring managed network services and section 6 about configuring security controls. Items therefore describe the decision and its consequence — Premium versus Standard tier, Shared VPC versus peering versus a hub, subnet expansion in place, policy-based routes, an internal load balancer as next hop, MED and BFD, NAT port allocation, NGFW tier and policy scope, secure tags versus network tags, multi-NIC appliances. No item is a console recipe and none needs a live project — the test suite rejects console-instruction phrasing outright, so the bank cannot drift into click-path trivia.

## Blueprint allocation

| Official domain | Published weight | Per exam | Percent | Package total |
|---|---:|---:|---:|---:|
| Designing and planning a Google Cloud VPC network | ~21% | 21 | 21% | 126 |
| Implementing a VPC network | ~20% | 20 | 20% | 120 |
| Configuring managed network services | ~16% | 16 | 16% | 96 |
| Configuring and implementing hybrid and multicloud network interconnectivity | ~16% | 16 | 16% | 96 |
| Managing, monitoring, and troubleshooting network operations | ~14% | 14 | 14% | 84 |
| Configuring, implementing, and managing a cloud network security solution | ~13% | 13 | 13% | 78 |

**These weights already total exactly 100%**, so the published weight *is* the per-exam item count. No rounding adjustment is needed or performed, and no tolerance band is applied in the tests; every count is asserted equal to its weight, so a future Google revision that breaks the exact 100% total will fail the build instead of being silently absorbed.

## Item mix

| Format | Per exam | Options | Notes |
|---|---:|---|---|
| Single-answer (`multiple-choice`) | 84 | 4 | One correct index in slots 1–4, balanced across the bank |
| Multi-select (`multi-select`) | 16 | 5 | Two correct indices, three distractors, "Select two" in the stem; 4 / 3 / 3 / 3 / 2 / 1 across domains 1–6 |
| Sequencing or drag-and-drop | 0 | — | The published format is multiple-choice and multiple-select only |

Nothing in the export uses a format the exam does not have.

## Time pressure: this bank is slower than the live exam per item

| | Items | Clock | Seconds per item |
|---|---:|---:|---:|
| Live exam | 50–60 | two hours | ~120–144 |
| This bank | 100 | two hours | ~72 |

So a timed run here is a **comfortable** rehearsal, not a simulation of the appointment. Use it to build the habit of finishing with time to review; if you want pressure, shorten the clock deliberately rather than assuming the bank supplies it.

## Claims discipline

- **No passing score is stated.** Google does not publish one for PCNE, so nothing here converts a practice percentage into a pass mark, and practice percentages are not scaled scores.
- **100 items is an expanded bank.** The live exam samples 50–60 questions; that is stated in every set README, the landing page, and the curriculum.
- **No case studies are imitated.** The absence is documented rather than filled with plausible-looking scenarios.
- **Configuration is disclosed as in scope**, and every configuration item is a judgement question, not a walkthrough.
- **Stems are unique beyond exact wording.** `build.py` rejects any pair of stems whose content-word overlap exceeds 0.72, so a reworded repeat of the same decision cannot ship.
- **Product names follow the 24 April 2026 guide**: Premium and Standard network service tiers, Shared VPC, VPC Network Peering, Network Connectivity Center (VPC, hybrid and producer spokes), Private Service Connect, private services access, Serverless VPC Access and Direct VPC egress, Cloud NAT and Private NAT, Cloud Router with global and regional dynamic routing and policy-based routes, Dedicated, Partner and Cross-Cloud Interconnect with VLAN attachments and MACsec, HA VPN and Classic VPN, BFD, Cloud DNS with forwarding, peering, geolocation, failover and DNSSEC, load balancing with backend services, NEGs and URL maps, Cloud CDN, GKE Autopilot networking, Dataplane V2 and IP masquerade, Cloud Armor, Cloud NGFW Essentials/Standard/Enterprise with hierarchical, global and regional policies, Secure Web Proxy, Packet Mirroring, and Network Intelligence Center including Connectivity Tests, Performance Dashboard, Firewall Insights, Network Analyzer, Flow Analyzer and Network Topology.
- **No community statistics are borrowed.** Question counts, self-reported pass rates, and "same as the real exam" claims from question-sharing sites are not used as evidence, benchmarks, or marketing anywhere in this course.

## Verification

```bash
cd course/Google-Professional-Cloud-Network-Engineer/04-resources
python3 build.py
python3 make_sample.py
python3 validate.py --report validation-report.json   # PASS: 6 sets / 600 questions
python3 -m unittest test_course                       # structural and artifact tests
python3 package.py                                    # reproducible ZIP
cd ../../.. && python3 course/check_csv_upload.py --all
```

Current status: **600 items, 6 sets, all structural checks passing**. Accurate to the best of our review, but not independently fact-checked, not psychometrically calibrated, and not a substitute for hands-on work in a sandbox project.

## Rights and attribution

All 600 questions and all documentation in this folder are original work for this repository. Google, Google Cloud, and the certification names are trademarks of Google LLC; this package is independent and makes no claim of affiliation or endorsement.
