# Official sources and coverage notes

Reviewed October 2026 against the exam guide and the certification page. Product names, preview status, and prices change, so re-check before publishing or scheduling.

## Primary references

| Purpose | URL |
|---|---|
| Certification page (length, fee, format, languages, prerequisites, renewal pointer) | https://cloud.google.com/learn/certification/cloud-devops-engineer |
| Exam guide (five sections and their weights) | https://services.google.com/fh/files/misc/professional_cloud_devops_engineer_exam_guide_english.pdf |
| Resource hierarchy | https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy |
| Organization policy constraints | https://cloud.google.com/resource-manager/docs/organization-policy/overview |
| Shared VPC | https://cloud.google.com/vpc/docs/shared-vpc |
| Private Service Connect | https://cloud.google.com/vpc/docs/private-service-connect |
| VPC Network Peering | https://cloud.google.com/vpc/docs/vpc-peering |
| Terraform on Google Cloud | https://cloud.google.com/docs/terraform |
| Infrastructure Manager | https://cloud.google.com/infrastructure-manager/docs |
| Config Connector | https://cloud.google.com/config-connector/docs |
| Cloud Foundation Toolkit | https://cloud.google.com/docs/terraform/blueprints/terraform-blueprints |
| Cloud Build | https://cloud.google.com/build/docs |
| Cloud Deploy | https://cloud.google.com/deploy/docs |
| Artifact Registry | https://cloud.google.com/artifact-registry/docs |
| Artifact Analysis | https://cloud.google.com/artifact-analysis/docs |
| Binary Authorization | https://cloud.google.com/binary-authorization/docs |
| GKE release channels | https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels |
| GKE fleets | https://cloud.google.com/kubernetes-engine/fleet-management/docs |
| Cloud Workstations | https://cloud.google.com/workstations/docs |
| Gemini Code Assist | https://cloud.google.com/gemini/docs/codeassist/overview |
| Gemini Cloud Assist | https://cloud.google.com/gemini/docs/cloud-assist/overview |
| Cloud KMS | https://cloud.google.com/kms/docs |
| Secret Manager | https://cloud.google.com/secret-manager/docs |
| Certificate Manager | https://cloud.google.com/certificate-manager/docs |
| Parameter Manager | https://cloud.google.com/parameter-manager/docs |
| Workload Identity Federation | https://cloud.google.com/iam/docs/workload-identity-federation |
| Cloud Service Mesh | https://cloud.google.com/service-mesh/docs |
| Ops Agent | https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent |
| OpenTelemetry on Google Cloud | https://cloud.google.com/stackdriver/docs/instrumentation/opencensus-migration |
| Google Cloud Managed Service for Prometheus | https://cloud.google.com/stackdriver/docs/managed-prometheus |
| Cloud Logging routing and sinks | https://cloud.google.com/logging/docs/routing/overview |
| Logging query language | https://cloud.google.com/logging/docs/view/query-library |
| Logs-based metrics | https://cloud.google.com/logging/docs/logs-based-metrics |
| Cloud Monitoring alerting | https://cloud.google.com/monitoring/alerts |
| Uptime checks | https://cloud.google.com/monitoring/uptime-checks |
| Cloud Trace | https://cloud.google.com/trace/docs |
| SRE workbook: implementing SLOs | https://sre.google/workbook/implementing-slos |
| Error budgets | https://sre.google/workbook/error-budget-policy |
| Dynamic Workload Scheduler | https://cloud.google.com/compute/docs/instances/dws |
| Spot VMs | https://cloud.google.com/compute/docs/instances/spot |
| Committed use discounts | https://cloud.google.com/docs/cuds |
| Network service tiers | https://cloud.google.com/network-tiers/docs/overview |
| Active Assist | https://cloud.google.com/active-assist/docs |
| Recommenders | https://cloud.google.com/recommender/docs |
| Cloud Billing reports and exports | https://cloud.google.com/billing/docs/how-to/reports |

## Verified exam facts

| Fact | Value |
|---|---|
| Domains and weights | 1) Bootstrapping and maintaining a Google Cloud organization ~20%; 2) Building and implementing CI/CD pipelines, including continuous testing, for application, infrastructure and machine-learning workloads ~25%; 3) Applying site reliability engineering practices ~18%; 4) Implementing observability practices and troubleshooting ~25%; 5) Optimizing performance and cost ~12% |
| Length | Two hours |
| Fee | $200 USD plus applicable tax |
| Question count | 50–60 multiple-choice and multiple-select questions (Google's published range) |
| Languages | English, Japanese |
| Prerequisites | None; Google recommends 3+ years of industry experience including 1+ year designing and managing production systems on Google Cloud |
| Case studies | None — the published format has no case-study component |
| Passing score | Not published by Google |
| Renewal | Described by Google only by reference to its Renewal FAQs; no duration or fee is restated here |
| Configuration objective | Present — the guide asks about CI/CD design, deployment strategy, alerting policy, log routing, cost control and IAM boundaries |

## Coverage mapping

| Official section | Local domain | Local skills | Items per exam | Items in bank |
|---|---|---:|---:|---:|
| 1. Bootstrapping and maintaining a Google Cloud organization (~20%) | 1 | 1.1–1.14 | 20 | 120 |
| 2. Building and implementing CI/CD pipelines (~25%) | 2 | 2.1–2.14 | 25 | 150 |
| 3. Applying site reliability engineering practices (~18%) | 3 | 3.1–3.9 | 18 | 108 |
| 4. Implementing observability practices and troubleshooting (~25%) | 4 | 4.1–4.16 | 25 | 150 |
| 5. Optimizing performance and cost (~12%) | 5 | 5.1–5.6 | 12 | 72 |
| **Total** | | **59 skills** | **100** | **600** |

The weights are approximate in Google's wording but total exactly 100%, so the item counts are the weights themselves. No rounding correction was applied and no tolerance band exists in the build: a revision that breaks the 100% total fails the build.

## What is deliberately not covered

- **Case studies.** Not part of the published format.
- **Console walkthroughs.** Configuration judgement is tested, but as a decision and its consequence, never as a click path. Nothing here needs a live project.
- **Hands-on labs and interactive item formats.** Not representable in a CSV, and not part of the published format.
- **Renewal-exam calibration.** This bank targets the standard exam; Google's renewal instrument is a separate paper with its own scope.

## Source discipline

- No question, option, or explanation is copied from any question-sharing site, braindump collection, or community forum. The ExamTopics listing for this exam was used only to check how items are *presented* — scenario length, "which should the team do" phrasing, and the multiple-select convention — never as a source of item text.
- Community statistics from such sites — question counts, self-reported pass rates, "same as the real exam" claims — are **not** used as evidence, benchmarks, or marketing claims anywhere in this course.
- Where Google publishes a range (50–60 questions) or declines to publish a value (the passing score), this course repeats the range or says the value is unpublished. It never fills the gap with an estimate of its own.
- Product names follow the October 2026 guide. Terms were not invented for products that do not exist, and older names were not carried forward in place of current ones.
