# Official sources and coverage notes

Reviewed October 2026. All facts below were verified against the pages listed; service behaviour, quotas, preview status, and prices change, so re-check before publishing or scheduling.

## Primary references

| Purpose | URL |
|---|---|
| AI-200 study guide (skills measured as of October 7, 2026) | https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200 |
| AI-200 certification page | https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-cloud-developer-associate/ |
| AI-200T00 training course | https://learn.microsoft.com/en-us/training/courses/ai-200t00/ |
| Exam duration and experience | https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience |
| Exam sandbox | https://aka.ms/examdemo |
| Container Registry | https://learn.microsoft.com/en-us/azure/container-registry/ |
| Container Apps | https://learn.microsoft.com/en-us/azure/container-apps/ |
| Azure Kubernetes Service | https://learn.microsoft.com/en-us/azure/aks/ |
| Cosmos DB vector search | https://learn.microsoft.com/en-us/azure/cosmos-db/vector-database |
| pgvector on Azure Database for PostgreSQL | https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/how-to-use-pgvector |
| Azure Managed Redis | https://learn.microsoft.com/en-us/azure/redis/ |
| Service Bus messaging | https://learn.microsoft.com/en-us/azure/service-bus-messaging/ |
| Event Grid | https://learn.microsoft.com/en-us/azure/event-grid/ |
| Azure Functions | https://learn.microsoft.com/en-us/azure/azure-functions/ |
| Key Vault | https://learn.microsoft.com/en-us/azure/key-vault/ |
| App Configuration | https://learn.microsoft.com/en-us/azure/azure-app-configuration/ |
| OpenTelemetry on Azure | https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-overview |
| KQL reference | https://learn.microsoft.com/en-us/kusto/query/ |

## Verified exam facts

| Fact | Value |
|---|---|
| Domains and weights | 1) Develop containerized solutions on Azure 20–25%; 2) Develop AI solutions by using Azure data management services 25–30% (heading) and 30–35% (skills-at-a-glance); 3) Connect to and consume Azure services 20–25%; 4) Secure, monitor, troubleshoot Azure solutions 20–25% |
| Typical question count | 40–60 |
| Time | 120 minutes, proctored, possible interactive components |
| Passing score | 700 / 1000 scaled |
| Price | $165 USD |
| Languages | English plus Arabic (Saudi Arabia), Chinese (Simplified), Chinese (Traditional), French, German, Indonesian, Italian, Japanese, Korean, Portuguese (Brazil), Russian, Spanish |
| Retake | 24 hours after the first attempt; later retakes follow the published policy |
| Validity | 1 year, with a free renewal assessment |
| Study guide baseline | Skills measured as of October 7, 2026 |
| Audience profile | Contributing to all phases of implementing AI solutions on Azure, with emphasis on back-end services |

Not claimed anywhere in this package: that the practice exams contain the live item count, that they reproduce interactive components, that a practice percentage maps to 700/1000, that completing the course earns the credential, or that any other exam has been retired or replaced.

### The weighting discrepancy, handled explicitly

The study guide contains two different statements about the data-management domain:

- The section heading reads **"Develop AI solutions by using Azure data management services (25–30%)"**.
- The "Skills at a glance" list reads **"Develop AI solutions by using Azure data management services (30–35%)"**.
- The change log records that this skill area's **"% of exam increased"** in the October 7, 2026 revision.

Only **30%** satisfies both statements. Every exam in this package therefore allocates 24 / 30 / 24 / 22 questions (24 / 30 / 24 / 22 percent), and the `bank.py` file encodes the weight as `(30, 30)` with this reasoning recorded in a comment. Re-check the guide before publishing; if Microsoft harmonises the two statements, revisit the allocation deliberately rather than silently.

## Domain coverage and package weights

| Domain | Official range | Per exam | Percent | Package total |
|---|---:|---:|---:|---:|
| 1. Develop containerized solutions on Azure | 20–25% | 24 | 24% | 144 |
| 2. Develop AI solutions by using Azure data management services | 25–30% and 30–35% | 15 | 30% | 90 |
| 3. Connect to and consume Azure services | 20–25% | 24 | 24% | 144 |
| 4. Secure, monitor, troubleshoot Azure solutions | 20–25% | 22 | 22% | 132 |

Because all six exams share the same allocation, every exam is a self-contained mock exam and the aggregate cannot drift.

## Coverage against the published sub-objectives

The study guide's sub-objectives were read directly and mapped into 30 local study areas. Counts describe this bank, not official weighting.

| Local ID | Study area | Domain | Items | Official sub-objectives it supports |
|---|---|---|---:|---|
| 1.1 | Container image lifecycle in Azure Container Registry | 1 | 21 | Build, store, version, and manage images |
| 1.2 | Automated image builds with ACR Tasks | 1 | 14 | Build and run images with ACR Tasks |
| 1.3 | Container deployment to Azure App Service | 1 | 27 | Deploy containers to App Service, supply environment variables and secrets |
| 1.4 | Container Apps deployment and revisions | 1 | 27 | Deploy to Container Apps with environment configuration and revision management |
| 1.5 | Event-driven scaling with KEDA | 1 | 18 | Implement KEDA-based event-driven scaling |
| 1.6 | AKS deployment with manifests | 1 | 20 | Deploy and manage AKS applications by using manifests |
| 1.7 | Container logs, events, and connectivity | 1 | 17 | Monitor and troubleshoot AKS and Container Apps |
| 2.1 | Cosmos DB SDK access and queries | 2 | 22 | Connect with the SDK and run queries |
| 2.2 | Cosmos DB indexing policies and request units | 2 | 15 | Optimize query performance and RU consumption |
| 2.3 | Cosmos DB consistency levels | 2 | 13 | Choose consistency levels against read requirements |
| 2.4 | Cosmos DB vector search and embeddings | 2 | 15 | Store embeddings and run vector similarity search |
| 2.5 | Cosmos DB change feed processing | 2 | 17 | Implement a change feed processor |
| 2.6 | PostgreSQL connection and schema modeling | 2 | 14 | Connect and query with SDKs; model schemas and indexing strategies |
| 2.7 | pgvector indexing and query latency | 2 | 24 | Optimize query latency and reduce pgvector overhead |
| 2.8 | PostgreSQL compute, memory, and storage sizing | 2 | 10 | Configure compute, memory, and storage for vector workloads |
| 2.9 | PostgreSQL RAG with metadata filters | 2 | 11 | Run similarity search and RAG patterns with metadata filters |
| 2.10 | PostgreSQL connection optimization | 2 | 13 | Implement connection optimization |
| 2.11 | Azure Managed Redis caching and invalidation | 2 | 17 | Implement caching, expiration, and invalidation |
| 2.12 | Azure Managed Redis vector indexing | 2 | 9 | Implement vector indexing for similarity search |
| 3.1 | Service Bus queues and sessions | 3 | 24 | Queue and process back-end operations, including sessions and messages |
| 3.2 | Service Bus topics, subscriptions, and filters | 3 | 20 | Implement topics, subscriptions, and filters |
| 3.3 | Service Bus dead-lettering and retries | 3 | 29 | Handle dead-letter queues and delivery limits |
| 3.4 | Event Grid filters, custom events, and retries | 3 | 29 | Implement event-driven workflows with filters, custom events, and retries |
| 3.5 | Azure Functions triggers and bindings | 3 | 18 | Build serverless APIs with triggers and bindings |
| 3.6 | Function app configuration and deployment | 3 | 24 | Configure and deploy function apps |
| 4.1 | Key Vault secret storage, rotation, and retrieval | 4 | 36 | Secure secrets, including rotation and retrieval |
| 4.2 | App Configuration settings and feature flags | 4 | 26 | Store and retrieve app configuration information |
| 4.3 | Distributed tracing with OpenTelemetry | 4 | 26 | Trace distributed systems by using OpenTelemetry SDKs |
| 4.4 | KQL queries for logs and metrics | 4 | 27 | Write KQL queries to analyze logs and metrics |
| 4.5 | Identity-based access for application services | 4 | 17 | Apply identity-based access, least privilege, and private connectivity |

Numeric IDs are local study aids. Microsoft names objectives without this numbering.

## Item-type fidelity boundary

| Real-exam format | Included here | How |
|---|---|---|
| Single-choice | Yes | `multiple-choice` with four options and one key |
| Multi-select | Yes | `multi-select` with five options, two or three keys, and a stated selection count |
| Drag-and-drop / ordering | Partially | `ordering` with four candidate sequences as options |
| Case studies | Yes | Two per exam, three scored items each, shared scenario |
| Hot-area | No | Requires image hotspots; cannot be scored in CSV |
| Labs and interactive components | No | Requires a provisioned sandbox |
| Adaptive problem-solution sets | No | Changes item order by prior answer; not representable as a fixed set |

## Editorial standards used while authoring

- Every item states one deciding constraint and one defensible best answer.
- Distractors are real services or settings that solve a different problem, not nonsense.
- Multi-select items name the required count so the learner cannot under- or over-select by accident.
- Ordering items anchor on a step that cannot move: build before push, apply before ready, receive before complete, store before rotate, extension before table before index.
- Case-study items restate their specific constraint so they still read correctly outside the shared preamble.
- Answers reflect current service behaviour, with the recurring traps handled explicitly: filter-before versus filter-after, provisioned versus autoscale, HNSW versus IVFFlat, peek-lock versus receive-and-delete, and identity versus key.
- No Microsoft sample, sandbox, or recall-derived item text is used. The sandbox link above was consulted only to understand item formats.

## Known limitations

- Automated checks verify structure, allocation, source parity, explanations, and reproducibility; they do not certify factual accuracy or difficulty.
- Counts reflect authoring emphasis, not official sub-objective weighting, which Microsoft does not publish per bullet.
- Preview features, quotas, and SDK surfaces move quickly; a question about a preview capability can age faster than one about a design principle.
- No Udemy account import, preview, or publication has been performed.
