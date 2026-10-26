# Sources and coverage — Professional Cloud Developer

Everything in this folder is original writing. The sources below were used to establish the exam's **published format and scope**, never as a source of item text.

## Primary sources

| Purpose | Reference |
|---|---|
| Certification page (length, fee, format, languages, prerequisites, renewal pointer) | https://cloud.google.com/learn/certification/cloud-developer |
| Exam guide (four sections, objectives, and their weights) | https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf |
| Cloud Run documentation | https://cloud.google.com/run/docs |
| Cloud Run service configuration (concurrency, instances, CPU, ingress) | https://cloud.google.com/run/docs/configuring |
| Cloud Run jobs | https://cloud.google.com/run/docs/create-jobs |
| Direct VPC egress | https://cloud.google.com/run/docs/configuring/vpc-direct-vpc |
| Cloud Run source deploys and buildpacks | https://cloud.google.com/docs/buildpacks/build-application |
| GKE documentation | https://cloud.google.com/kubernetes-engine/docs |
| GKE Autopilot | https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview |
| Kubernetes probes (startup, readiness, liveness) | https://cloud.google.com/kubernetes-engine/docs/how-to/configure-probes |
| Horizontal Pod Autoscaling on GKE | https://cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling |
| Pod disruption budgets | https://cloud.google.com/kubernetes-engine/docs/how-to/configure-pdb |
| Rolling updates and surge settings | https://cloud.google.com/kubernetes-engine/docs/how-to/updating-apps |
| Workload Identity Federation for GKE | https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity |
| Cloud Build | https://cloud.google.com/build/docs |
| Cloud Build triggers | https://cloud.google.com/build/docs/automating-builds/create-manage-triggers |
| Artifact Registry | https://cloud.google.com/artifact-registry/docs |
| Artifact Analysis | https://cloud.google.com/artifact-analysis/docs |
| Binary Authorization | https://cloud.google.com/binary-authorization/docs |
| SLSA and build provenance | https://cloud.google.com/build/docs/securing-builds/use-provenance-and-slsa-to-satisfy-supply-chain-requirements |
| Eventarc | https://cloud.google.com/eventarc/docs |
| Pub/Sub (push and pull, dead-letter topics, BigQuery subscriptions) | https://cloud.google.com/pubsub/docs |
| Cloud Tasks | https://cloud.google.com/tasks/docs |
| Cloud Scheduler | https://cloud.google.com/scheduler/docs |
| Workflows | https://cloud.google.com/workflows/docs |
| API Gateway | https://cloud.google.com/api-gateway/docs |
| Apigee API management | https://cloud.google.com/apigee/docs |
| Cloud Load Balancing | https://cloud.google.com/load-balancing/docs |
| Cloud CDN | https://cloud.google.com/cdn/docs |
| Memorystore | https://cloud.google.com/memorystore/docs |
| Cloud Storage (lifecycle, retention, signed URLs) | https://cloud.google.com/storage/docs |
| Cloud SQL connectors and the Auth Proxy | https://cloud.google.com/sql/docs/postgres/connect-connectors |
| AlloyDB Auth Proxy | https://cloud.google.com/alloydb/docs/connect-auth-proxy |
| Private Service Connect | https://cloud.google.com/vpc/docs/private-service-connect |
| Firestore | https://cloud.google.com/firestore/docs |
| Spanner | https://cloud.google.com/spanner/docs |
| Bigtable and row-key design | https://cloud.google.com/bigtable/docs/schema-design |
| BigQuery streaming inserts and exports | https://cloud.google.com/bigquery/docs/streaming-data-into-bigquery |
| Secret Manager | https://cloud.google.com/secret-manager/docs |
| Cloud KMS and CMEK | https://cloud.google.com/kms/docs/cmek |
| Identity-Aware Proxy | https://cloud.google.com/iap/docs |
| Identity Platform | https://cloud.google.com/identity-platform/docs |
| Application Default Credentials | https://cloud.google.com/docs/authentication/application-default-credentials |
| Service accounts and least privilege | https://cloud.google.com/iam/docs/service-account-overview |
| Cloud Workstations | https://cloud.google.com/workstations/docs |
| Cloud Shell | https://cloud.google.com/shell/docs |
| Cloud Code | https://cloud.google.com/code/docs |
| Cloud Service Mesh | https://cloud.google.com/service-mesh/docs |
| Gemini Cloud Assist | https://cloud.google.com/gemini/docs/cloud-assist/overview |
| Model Context Protocol servers for Google Cloud | https://cloud.google.com/gemini/docs/codeassist/use-mcp-servers |
| Cloud Logging structured logging | https://cloud.google.com/logging/docs/structured-logging |
| Log-based metrics | https://cloud.google.com/logging/docs/logs-based-metrics |
| Cloud Monitoring alerting policies | https://cloud.google.com/monitoring/alerts |
| Cloud Trace and context propagation | https://cloud.google.com/trace/docs |
| Error Reporting | https://cloud.google.com/error-reporting/docs |
| Cloud Profiler | https://cloud.google.com/profiler/docs |
| Emulators for local development | https://cloud.google.com/sdk/gcloud/reference/emulators |

## Verified exam facts

| Fact | Value |
|---|---|
| Domains and weights | 1) Designing highly scalable, secure, and reliable cloud-native applications ~32%; 2) Building and testing applications ~23%; 3) Configuring cloud-native applications for deployment ~24%; 4) Integrating applications with Google Cloud services ~21% |
| Length | Two hours |
| Fee | $200 USD plus applicable tax |
| Question count | 50–60 multiple-choice and multiple-select questions (Google's published range) |
| Languages | English, Japanese |
| Prerequisites | None; Google recommends 3+ years of industry experience including 1+ year designing and managing applications on Google Cloud |
| Case studies | None — the published format has no case-study component |
| Passing score | Not published by Google |
| Renewal | Described by Google only by reference to its Renewal FAQs; no duration or fee is restated here |
| Configuration objective | Present — section 3 is entirely about configuring cloud-native applications for deployment |

## Exam-guide objectives used for the study map

| Official section | Objectives in the guide | Local skills |
|---|---|---|
| 1. Designing highly scalable, secure, and reliable cloud-native applications (~32%) | 1.1 Design high-performing applications and APIs; 1.2 Design secure applications; 1.3 Design for storing and accessing data | 1.1–1.18 |
| 2. Building and testing applications (~23%) | 2.1 Set up a development environment; 2.2 Build an application; 2.3 Test an application | 2.1–2.7 |
| 3. Configuring cloud-native applications for deployment (~24%) | 3.1 Configure Cloud Run; 3.2 Configure GKE | 3.1–3.7 |
| 4. Integrating applications with Google Cloud services (~21%) | 4.1 Connect to data and storage services; 4.2 Consume Google Cloud APIs; 4.3 Troubleshoot and observe applications | 4.1–4.7 |

Local skill IDs subdivide each objective into decision-level areas — compute choice, API protocol, caching, secrets, datastore selection, build pipelines, probes, autoscaling, connectivity, messaging, Cloud API call patterns and observability. They are study aids, not Google objective numbers, and the mapping is one-directional: every local skill belongs to exactly one official section, and the section counts match the published weights.

## Coverage mapping

| Official section | Local domain | Local skills | Items per exam | Items in bank |
|---|---|---:|---:|---:|
| 1. Designing highly scalable, secure, and reliable cloud-native applications (~32%) | 1 | 1.1–1.18 | 32 | 192 |
| 2. Building and testing applications (~23%) | 2 | 2.1–2.7 | 23 | 138 |
| 3. Configuring cloud-native applications for deployment (~24%) | 3 | 3.1–3.7 | 24 | 144 |
| 4. Integrating applications with Google Cloud services (~21%) | 4 | 4.1–4.7 | 21 | 126 |
| **Total** | | **39 skills** | **100** | **600** |

The weights are approximate in Google's wording but total exactly 100%, so the item counts are the weights themselves. No rounding correction was applied and no tolerance band exists in the build: a revision that breaks the 100% total fails the build.

## What is deliberately not covered

- **Case studies.** Not part of the published format.
- **Console walkthroughs.** Configuration judgement is tested, but as a decision and its consequence, never as a click path. Nothing here needs a live project.
- **Hands-on labs and interactive item formats.** Not representable in a CSV, and not part of the published format.
- **Prior-guide vocabulary.** The 2024 guide's older framing (including Container Analysis as the scanning product and Cloud Endpoints for API management) is not carried forward where the current guide uses current names; Artifact Analysis, API Gateway and Apigee appear instead.
- **Renewal-exam calibration.** This bank targets the standard exam; Google's renewal instrument is a separate paper with its own scope.

## Source discipline

- No question, option, or explanation is copied from any question-sharing site, braindump collection, or community forum. The ExamTopics listing for this exam was checked only for how items are *presented* — scenario length, "which should the team do" phrasing, and the multiple-select convention — never as a source of item text.
- Community statistics from such sites — question counts, self-reported pass rates, "same as the real exam" claims — are **not** used as evidence, benchmarks, or marketing claims anywhere in this course. In particular, the third-party weight splits of 36% / 20% seen on some sites were rejected in favour of the guide's 32 / 23 / 24 / 21, and no third-party pass mark is repeated.
- Where Google publishes a range (50–60 questions) or declines to publish a value (the passing score), this course repeats the range or says the value is unpublished. It never fills the gap with an estimate of its own.
- Product names follow the October 2026 guide, including Gemini Cloud Assist, AI coding assistants, MCP servers, Cloud Workstations, Direct VPC egress, Cloud Service Mesh and the AlloyDB Auth Proxy. The certification page carries a notice that the exam has been updated for recent branding changes, so names are re-checked against the guide rather than older material.
