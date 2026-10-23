# PAA sources, coverage, and design notes

Baseline: the current official English Professional Agentic Architect exam guide (five sections; 13/17/33/22/15). The beta multiple-choice window ran September 8–30, 2026 and is closed. Google says general availability opens in mid-November 2026, with a 2-hour proctored session and the same two-part structure. The GA exam guide and format may change; this package makes no claim about an unpublished future blueprint.

## Authoritative scope

- **Certification page:** [https://cloud.google.com/learn/certification/agentic-architect](https://cloud.google.com/learn/certification/agentic-architect)
- **Exam guide (English):** [Professional Agentic Architect Certification exam guide](https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf)
- **Certification FAQ:** [Professional Agentic Architect Certification FAQs](https://support.google.com/cloud-certification/answer/18080541)
- **Learning path:** [Google Skills — Professional Agentic Architect](https://www.skills.google/paths/4525)
- **Sample questions:** [Google sample-question form](https://docs.google.com/forms/d/1fi1gqbWsNCFxm1CT9V-JNGff1lyqfU9kNWAaaQMvRi4/preview) (format familiarization only; not used as bank material)

Supporting product references used for scenario design:

- [Agent Development Kit documentation](https://google.github.io/adk-docs/)
- [Gemini Enterprise](https://cloud.google.com/gemini-enterprise)
- [Vertex AI agent platform / Agent Engine documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview)
- [Model Armor overview](https://cloud.google.com/security-command-center/docs/model-armor-overview)
- [Cloud Run](https://cloud.google.com/run/docs) and [GKE](https://cloud.google.com/kubernetes-engine/docs)
- [Model Context Protocol](https://modelcontextprotocol.io/) and [A2A protocol](https://a2a-protocol.org/)

The exam guide controls the tested blueprint. Product documentation describes evolving behavior and does not override the guide or your organization's policy.

## Exam facts used

| Item | Beta (closed) | GA (announced) |
|---|---|---|
| Availability | September 8–30, 2026 | Registration opens mid-November 2026 |
| Part 1 | Proctored multiple-choice, 3 hours, roughly 80 questions | Proctored multiple-choice, 2-hour session |
| Part 2 | Hands-on labs in Google Skills, after passing Part 1 | Same two-part structure |
| Fee | $120 (40% beta discount) | $200 USD list price |
| Language | English only | Verify current page |
| Validity | 1 year | 1 year |
| Prerequisites | None | None |
| Recommended experience | 3+ years cloud, including 1+ year agentic on Google Cloud | Same guidance published |
| Results | Late October 2026 | 7–10 business days |

**Critical format point:** passing the multiple-choice exam alone does **not** grant certification. The official FAQ states you must pass both the proctored exam and the hands-on labs. This package prepares the question portion only; it contains no lab environment, cloud project, credits, or voucher.

**Scoring:** Google does not publish a raw percentage pass threshold for this exam on the pages reviewed. The 80% practice target in this package is a custom study convention, not an official cut score, and no scaled-score conversion is implied.

## Official sections and weights

| # | Section | Weight |
|---|---|---:|
| 1 | Building agents using low-code tools | ~13% |
| 2 | Using coding agents for application development | ~17% |
| 3 | Developing custom agents | ~33% |
| 4 | Evaluating and deploying agentic workflows | ~22% |
| 5 | Securing and governing agentic workflows | ~15% |

The guide contains **11 numbered objectives** and **31 considerations**, plus a list of **28 in-scope tools**. Objectives used for mapping:

1. 1.1 Configure agentic workflows and behavior using low-code tools
2. 1.2 Connect enterprise data to Gemini Enterprise
3. 2.1 Use coding agents effectively
4. 2.2 Customize coding agents for enterprise workflows
5. 3.1 Design and build agentic workflows in code
6. 3.2 Integrate enterprise domain knowledge
7. 3.3 Orchestrate and coordinate agentic workflows
8. 4.1 Evaluate agents in development and in production
9. 4.2 Deploy and scale production workloads
10. 5.1 Configure agent security and governance
11. 5.2 Implement secure agent behavior and execution

## In-scope tools named by the guide

ADK; Agent evaluation; Agent Gateway; Agent Identity; Agent Registry; Agent Retrieval and Vector Search 1.0; Agent Runtime (formerly Agent Engine); Agent Search (formerly Vertex AI Search); agentic protocols (A2A, MCP); Agents CLI in Agent Platform; Antigravity (CLI, SDK, App); Auth Manager (OAuth 2.0); BigQuery; Cloud Run; Cloud SQL; Cloud Storage; Firestore; Gemini Enterprise; Gemini LLMs; Google Cloud Observability (Cloud Logging and Cloud Trace); GKE; Memorystore for Redis; Model Armor; MCP servers; Model Garden; RAG Engine; Sensitive Data Protection; Skill Registry.

## Package allocation

| Test | Topic | Section allocation |
|---|---|---|
| 1 | Low-Code Agents and Coding Agents | Section 1: 50, Section 2: 50 |
| 2 | Custom Agents: Models, ADK, Memory, RAG, and Retrieval | Section 3: 100 |
| 3 | Custom Agents: Identity, Orchestration, and Registry | Section 3: 100 |
| 4 | Evaluating and Deploying Agentic Workflows | Section 4: 100 |
| 5 | Securing and Governing Agentic Workflows | Section 5: 100 |
| 6 | Integrated Architect Scenarios and Final Review | Section 1: 13, Section 2: 17, Section 3: 33, Section 4: 22, Section 5: 15 |

Test 6 uses an integer approximation of the published weights: 13/17/33/22/15. Tests 1–5 are focused learning sets; Tests 2 and 3 each devote 100 questions to the 33% custom-agent section because it is the largest and most technical area.

## Coverage by section

| # | Section | Weight | Tests 1–5 | Test 6 | Package |
|---|---|---:|---:|---:|---:|
| 1 | Building Agents Using Low-Code Tools | 13% | 50 | 13 | 63 |
| 2 | Using Coding Agents for Application Development | 17% | 50 | 17 | 67 |
| 3 | Developing Custom Agents | 33% | 200 | 33 | 233 |
| 4 | Evaluating and Deploying Agentic Workflows | 22% | 100 | 22 | 122 |
| 5 | Securing and Governing Agentic Workflows | 15% | 100 | 15 | 115 |

## Local study-map skills

The guide names objectives and considerations rather than numbered skills. The IDs below are **local study-map IDs** created to make coverage and exports auditable. They are not official numbers.

| Local ID | Study area | Official section | Questions |
|---|---|---|---:|
| 1.1 | State-Based Workflow Design | Building Agents Using Low-Code Tools | 24 |
| 1.2 | Agent Instructions and Prompt Templates | Building Agents Using Low-Code Tools | 16 |
| 1.3 | Enterprise Data Connection | Building Agents Using Low-Code Tools | 11 |
| 1.4 | Low-Code Change and Release Control | Building Agents Using Low-Code Tools | 12 |
| 2.1 | Coding Agent Configuration and Tooling | Using Coding Agents for Application Development | 14 |
| 2.2 | Customization Primitives | Using Coding Agents for Application Development | 14 |
| 2.3 | Secure Sandboxes | Using Coding Agents for Application Development | 14 |
| 2.4 | Code Modernization and Vulnerability Remediation | Using Coding Agents for Application Development | 14 |
| 2.5 | Coding Agent Operations and Oversight | Using Coding Agents for Application Development | 11 |
| 3.1 | Model Selection and Tradeoffs | Developing Custom Agents | 24 |
| 3.2 | ADK Agent Construction | Developing Custom Agents | 25 |
| 3.3 | Sessions, State, and Memory | Developing Custom Agents | 23 |
| 3.4 | RAG Pipeline Design | Developing Custom Agents | 22 |
| 3.5 | Vector Search and Managed Retrieval | Developing Custom Agents | 22 |
| 3.6 | Retrieval Authorization and Evidence Quality | Developing Custom Agents | 20 |
| 3.7 | Agent Identity and Permissions | Developing Custom Agents | 19 |
| 3.8 | Registry and Capability Integration | Developing Custom Agents | 19 |
| 3.9 | Agent-to-Agent Protocols | Developing Custom Agents | 19 |
| 3.10 | Multi-Agent Workflow Patterns | Developing Custom Agents | 20 |
| 3.11 | Runtime Coordination and Policies | Developing Custom Agents | 20 |
| 4.1 | Evaluation Test Sets | Evaluating and Deploying Agentic Workflows | 20 |
| 4.2 | Evaluation Metrics and Tooling | Evaluating and Deploying Agentic Workflows | 21 |
| 4.3 | Continuous Evaluation and Regression | Evaluating and Deploying Agentic Workflows | 20 |
| 4.4 | Runtime Selection | Evaluating and Deploying Agentic Workflows | 20 |
| 4.5 | Troubleshooting Agent Failures | Evaluating and Deploying Agentic Workflows | 20 |
| 4.6 | Monitoring and Optimization | Evaluating and Deploying Agentic Workflows | 21 |
| 5.1 | Authentication and Secure Tool Execution | Securing and Governing Agentic Workflows | 19 |
| 5.2 | Principal Access Boundaries | Securing and Governing Agentic Workflows | 20 |
| 5.3 | Agent Gateway and Traffic Governance | Securing and Governing Agentic Workflows | 19 |
| 5.4 | Registry and Policy Enforcement | Securing and Governing Agentic Workflows | 19 |
| 5.5 | Guardrails and Human-in-the-Loop | Securing and Governing Agentic Workflows | 19 |
| 5.6 | Secure Data Access and Identity Propagation | Securing and Governing Agentic Workflows | 19 |

All 32 local study areas have practice. This does not establish equal depth per consideration, independent factual certification, or calibrated difficulty.

## Design emphasis

- **Architecture over trivia.** Questions ask which control, pattern, or data flow satisfies a stated constraint, rather than which menu contains a button.
- **Trajectory and side effects.** Evaluation questions test tool-call paths, not only final text, because a correct answer cannot certify a wrong action.
- **Identity and authorization.** Security questions keep authentication, authorization, and approval distinct, and place enforcement in code or platform controls rather than prompts.
- **Evidence integrity.** Retrieval questions require authorization filtering, provenance, freshness, and grounding before generation.
- **Operational realism.** Deployment questions compare managed agent hosting, serverless containers, and GKE using operational control, state, and workload shape.
- **Recurring concepts.** Terms such as least privilege, grounding, and bounded loops recur across contexts for reinforcement; unique wording is not independent coverage.

## Version and product-availability boundary

- The current published guide is the **beta English guide**. At GA, Google may revise objectives, weights, tool names, or item counts. Refresh this package against the GA guide before using it for a post-November attempt.
- The beta exam is closed; the package is study material, not a beta registration product.
- Agent Runtime and Agent Search are described with their former names where the guide does so. Interface names and navigation paths are not asserted.
- Model availability, quotas, regions, and preview status vary by project and change over time. Questions avoid fixed prices, context sizes, and version numbers.
- ADK, A2A, MCP, and Antigravity evolve quickly. Questions test concepts and contracts rather than a specific release's API signature.
- The hands-on labs are separate, are available only after passing Part 1, and are not simulated here.

## Known limitations

- Structural validation is automated; independent technical, security, legal, and accessibility review is not performed.
- No psychometric calibration, difficulty equating, or score prediction.
- No exhaustive semantic-duplicate detection; related concepts deliberately recur.
- No live Udemy import, platform preview, or publication is claimed.
- No continuous link or product-interface verification.
- Not endorsed by Google; marks belong to their owners.

## Refresh triggers

1. GA exam guide or any revised blueprint is published.
2. Item count, time, fee, language, validity, or lab requirements change.
3. Agent Runtime, Agent Gateway, Agent Identity, Agent Registry, Agent Search, RAG Engine, ADK, A2A, or MCP change materially.
4. A reviewer finds an ambiguous item, unsupported claim, or duplicated concept that weakens the bank.
5. Google publishes new sample questions or a revised learning path that changes expected emphasis.
