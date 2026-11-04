# Agentic AI (`NCP-AAI` / `AAIF` `MCP` & `A2A` / `OWASP ASI`) — Curriculum Outline & Blueprint Crosswalk

**Baseline:** `November 2026`  
**Structure:** `6` Full-Length Mock Exams × `100` Questions = `600` Unique Production Scenarios (`0` artificial case-study blocks)  
**Item Mix per Exam:** `76` Single-Choice (`S`) + `8` Ordered 4-Step Sequences (`O`, exported as `multiple-choice` with `→`) + `13` Two-Answer Multi-Select (`M2`) + `3` Three-Answer Multi-Select (`M3`) = `84 multiple-choice` (`21 A / 21 B / 21 C / 21 D`) + `16 multi-select`

---

## 1. Crosswalk to Official 2026 Blueprints & Standards

| Consolidated Course Domain | Weight / Set | Official NVIDIA `NCP-AAI` (10 Domains = `100%`) | Linux Foundation `AAIF` & `OWASP` Standards |
| :--- | :---: | :--- | :--- |
| **Domain 1:** Agentic Architectures, Reasoning Loops & Multi-Agent Topologies | `18%` (`18` Qs) | Agent Architecture & Design (`15%`), Cognition/Planning (`3%`) | `A2A v1.0` (`RFC 7515`/`8785`), `AGENTS.md`, `Agent Skills` |
| **Domain 2:** Agent Development, Tool Contracts, MCP & Durable State Graphs | `20%` (`20` Qs) | Agent Development (`15%`), NVIDIA NeMo Agent Toolkit (`2%`), Platform (`3%`) | `MCP 2026-07-28`, `RFC 9207`, `CIMD`, `LangGraph 1.x`, `OpenSandbox` |
| **Domain 3:** Memory Systems, Context Engineering & Agentic RAG | `16%` (`16` Qs) | Knowledge Integration & Data Handling (`10%`), Cognition & Memory (`6%`) | `NeMo Retriever`, `CRAG`, `Self-RAG`, `GraphRAG`, `Presidio` |
| **Domain 4:** Agent Evaluation, Trajectory Grading & Model Optimization | `16%` (`16` Qs) | Evaluation and Tuning (`13%`), NeMo Customizer (`2%`), Planning (`1%`) | `OpenEnv`, `Pass^k` (`tau-bench`), `DSPy`, `SFT`/`DPO`/`RFT` |
| **Domain 5:** Inference Acceleration, Scaling & Agent Observability | `15%` (`15` Qs) | Deployment & Scaling (`13%`), Run/Monitor/Maintain (`5%`), NVIDIA NIM/TRT-LLM | `NVIDIA NIM`, `TensorRT-LLM`, `vLLM`, `KEDA`, `agentgateway`, `OTel GenAI` |
| **Domain 6:** Agentic Security, Guardrails, Governance & Human Oversight | `15%` (`15` Qs) | Safety, Ethics & Compliance (`5%`), Human-AI Interaction & Oversight (`5%`) | `OWASP ASI01–ASI10`, `NeMo Guardrails`, `RFC 8693 OBO`, `NIST AI RMF`, `EU AI Act` |

---

## 2. Skill-Level Syllabus (`34` Skills `1.1`–`6.5`)

### Domain 1 — Agentic Architectures, Reasoning Loops, and Multi-Agent Topologies (`18` Qs/set · `108` total)
- **`1.1` (`3` Qs/set: `2 S + 1 M2`):** Distinguish deterministic workflows (`Prompt Chaining`, `Routing`, `Parallelization`) from autonomous agents (`Orchestrator-Workers`, capped `Evaluator-Optimizer`) and avoid premature multi-agent overhead.
- **`1.2` (`3` Qs/set: `3 S`):** Select reasoning and planning loops (`ReAct`, `Plan-and-Execute`, validator-grounded `Reflexion`, and `Tree-of-Thoughts`) under strict latency and token-budget constraints.
- **`1.3` (`3` Qs/set: `1 O + 2 S`):** Design task decomposition, dynamic replanning, bounded self-correction caps, and isolated sub-agent `Pydantic` handoffs (`avoiding raw scratchpad pollution`).
- **`1.4` (`3` Qs/set: `2 S + 1 M2`):** Architect multi-agent topologies (`Hierarchical Supervisor`, `Swarm Handoff` with hop filters, `DAG` pipelines, and versioned `Shared Blackboard` schemas).
- **`1.5` (`3` Qs/set: `3 S`):** Implement horizontal peer-agent interoperability via **`A2A v1.0`** (`JWS`-signed `Agent Card`s at `/.well-known/agent-card.json`, stateful `Task` lifecycles, `SSE`, and authenticated webhooks vs vertical `MCP`).
- **`1.6` (`3` Qs/set: `2 S + 1 M2`):** Standardize repository context with **`AGENTS.md`** and progressive **`Agent Skills`** (`SKILL.md`), backed by `max_steps`, cycle-breaker, and USD budget ceilings.

### Domain 2 — Agent Development, Tool Contracts, MCP, and Durable State Graphs (`20` Qs/set · `120` total)
- **`2.1` (`3` Qs/set: `3 S`):** Design ergonomic, grammar-constrained `Pydantic` v2 tool contracts, parallel read fan-out + keyed idempotent mutations, and structured credential-scrubbed error hints.
- **`2.2` (`4` Qs/set: `1 O + 2 S + 1 M2`):** Architect **`MCP 2026-07-28`** servers (`Tools` vs `Resources` vs `Prompts`, `stdio` vs stateless `Streamable HTTP` with `_meta` and `Mcp-Method`/`Mcp-Name` headers, OAuth 2.1 + `PKCE` + `RFC 8707` `aud` + `RFC 9207` `iss` + `CIMD`, `Roots`, human-approved `Sampling`, and non-secret `Elicitation`).
- **`2.3` (`4` Qs/set: `1 O + 3 S`):** Build durable cyclic state graphs in **`LangGraph 1.x`** (`Annotated` channel reducers, dynamic `Send()` map-reduce, `PostgresSaver` checkpoint time-travel, deterministic multi-interrupt index order, and pure pre-`interrupt()` replay safety on `Command(resume=...)`).
- **`2.4` (`3` Qs/set: `2 S + 1 M2`):** Match framework strengths across `LangGraph`, `AutoGen / AG2`, `CrewAI Flows + Crews`, and `NVIDIA NeMo Agent Toolkit`, plus server-backed `MCP` Tool Annotations.
- **`2.5` (`3` Qs/set: `3 S`):** Isolate untrusted generated Python/shell/browser execution inside ephemeral microVMs (`OpenSandbox`, `Firecracker`, `gVisor`) with blocked `169.254.169.254` metadata and deny-by-default egress (`preventing OWASP ASI05 RCE`).
- **`2.6` (`3` Qs/set: `2 S + 1 M3`):** Coordinate multi-system agent mutations via durable compensating sagas (`Temporal` / checkpointed graphs), transactional outboxes, server-side idempotency ledgers, and monitored `DLQ`s.

### Domain 3 — Memory Systems, Context Engineering, and Agentic RAG (`16` Qs/set · `96` total)
- **`3.1` (`3` Qs/set: `2 S + 1 M2`):** Separate **working**, **episodic**, **semantic**, and **procedural** memory tiers, distill verified episodic outcomes into playbooks, and enforce storage-layer `(tenant_id, user_id, scope)` isolation.
- **`3.2` (`3` Qs/set: `3 S`):** Mitigate context rot (`lost-in-the-middle`) via addressable artifact URIs, structured sub-goal compaction, contextualized chunk headers, and parallel query decomposition.
- **`3.3` (`3` Qs/set: `1 O + 2 S`):** Combine **`Adaptive RAG`**, **`Corrective RAG` (`CRAG`)**, and **`Self-RAG`** relevance/support grading with deterministic post-generation `[doc_id:span]` citation verification.
- **`3.4` (`3` Qs/set: `2 S + 1 M2`):** Pair hybrid `BM25` + dense vector search (`RRF` + `NeMo Retriever` cross-encoder reranking) with **`GraphRAG`** entity-community synthesis for corpus-wide multi-hop reasoning.
- **`3.5` (`2` Qs/set: `2 S`):** Preserve numeric tables and diagrams with layout-aware multimodal extraction, parent-child hierarchical chunking, and bitemporal `effective_from`/`superseded_by` lineage.
- **`3.6` (`2` Qs/set: `1 S + 1 M2`):** Enforce pre-retrieval `OBO` ACL trimming, `Presidio` PII/PHI scrubbing, provenance-gated memory writes (`blocking ASI06`), timestamp conflict supersession, and `TTL`/GDPR erasure APIs.

### Domain 4 — Agent Evaluation, Trajectory Grading, and Model Optimization (`16` Qs/set · `96` total)
- **`4.1` (`3` Qs/set: `1 O + 2 S`):** Build deterministic offline agent evaluation suites in **`OpenEnv`** mock sandboxes with `HTTP 429/503` and schema fault injection.
- **`4.2` (`3` Qs/set: `2 S + 1 M2`):** Grade full tool-call trajectories and final mocked environment states alongside **`Pass^k` (`(p)^k` all-trials reliability consistency)** vs optimistic `Pass@k`.
- **`4.3` (`3` Qs/set: `3 S`):** Calibrate distinct **`LLM-as-judge`** models against blinded SME labels (`Cohen's kappa`, position-swap & verbosity debiasing) alongside **RAG Triad** (`Context Relevance`, `Faithfulness`, `Answer Relevance`) diagnostics.
- **`4.4` (`3` Qs/set: `2 S + 1 M3`):** Apply the optimization ladder: fix prompts/schemas (`DSPy`) first, distill verified teacher trajectories into compact `LoRA`/`SFT` students (`NeMo Customizer`), align preferences via `DPO`, and run `RFT`/`GRPO` strictly on verifiable `OpenEnv` outcome graders.
- **`4.5` (`2` Qs/set: `2 S`):** Gate every PR on stratified + `OWASP ASI` adversarial CI slices, side-effect-free `Shadow` replay (`write tools mocked`), and guardrail-monitored `Canary`/`A-B` rollouts.
- **`4.6` (`2` Qs/set: `2 S`):** Operate `Presidio`-scrubbed production trace-to-golden-dataset flywheels and benchmark 3D Pareto model routing (`Pass^k × P95 latency × USD/task`).

### Domain 5 — Inference Acceleration, Scaling, and Agent Observability (`15` Qs/set · `90` total)
- **`5.1` (`3` Qs/set: `3 S`):** Serve models on **`NVIDIA NIM`**, **`TensorRT-LLM`**, `Triton`, and **`vLLM`** with continuous batching, `PagedAttention`, `FP8`/`INT4-AWQ`/`NVFP4` quantization (`gated on nested JSON tool schemas`), and disaggregated prefill/decode pools.
- **`5.2` (`3` Qs/set: `2 S + 1 M2`):** Maximize cross-turn/session `KV` prefix-cache hits (`sort_keys=True`, dynamic state at prompt tail) and accelerate structured JSON `TPOT` with lossless speculative decoding (`EAGLE`/`Medusa`/draft).
- **`5.3` (`3` Qs/set: odd `1 O + 2 S`, even `3 S`):** Autoscale GPU pods via **`KEDA`** on `KV-cache %`, queue depth, and `TTFT` SLOs (`never host CPU% alone`) behind per-tenant rate-limiting **`agentgateway`** proxies and progressive `Shadow -> Canary` pipelines.
- **`5.4` (`3` Qs/set: `2 S + 1 M2`):** Instrument **`OpenTelemetry` GenAI Agent Spans** (`gen_ai.agent.id`, `execution.id`, `checkpoint.id`, `pause.id`, child LLM `TTFT`/`TPOT`/cache-read tokens, `MCP` latency, and `tenant_id` FinOps baggage).
- **`5.5` (`3` Qs/set: odd `3 S`, even `1 O + 2 S`):** Contain `HTTP 429` `TPM`/`RPM` bursts, retry storms, and live incidents via token-aware admission queues + jittered backoff, schema-validated secondary failovers, loop ceilings, and scoped kill-switches.

### Domain 6 — Agentic Security, Guardrails, Governance, and Human Oversight (`15` Qs/set · `90` total)
- **`6.1` (`3` Qs/set: `1 O + 2 S`):** Defend against **`OWASP ASI01` Goal Hijack**, **`ASI02` Tool Misuse**, and **`ASI05` RCE** using provenance taint tags, **`NVIDIA NeMo Guardrails`**, read/write separation, and `OPA`/Cedar Policy-as-Code.
- **`6.2` (`3` Qs/set: `2 S + 1 M2`):** Enforce dedicated Non-Human Identity (**`NHI`**), short-lived **`OAuth 2.0 On-Behalf-Of` (`OBO`, `RFC 8693`)** token exchange, and dynamic per-node tool scoping against **`ASI03` Privilege Abuse**.
- **`6.3` (`3` Qs/set: `2 S + 1 M2`):** Secure **`MCP` supply chains** (`ASI04`: signed allowlists, SHA-256 `tools/list` rug-pull hash pinning, `AIBOM`) and horizontal **`A2A` buses** (`ASI07`: `SPIFFE/SPIRE` `mTLS`, `JWS` signatures, replay nonces).
- **`6.4` (`3` Qs/set: `3 S`):** Contain **`ASI06` Memory Poisoning**, **`ASI08` Cascading Failures**, and **`ASI10` Rogue Agents** via provenance-validated writes, inter-agent circuit breakers/bulkheads, and **out-of-band control-plane kill-switches**.
- **`6.5` (`3` Qs/set: `1 O + 1 S + 1 M3`):** Prevent **`ASI09` Human-Agent Trust Exploitation** (`automation bias`) via risk-tiered `HITL` modals rendering deterministic parameter diffs + taint flags, and operationalize **`NIST AI RMF 1.0`**, **`EU AI Act` (`Art. 14 & 50`)**, **`Zero Data Retention` (`ZDR`)**, and **`WORM`** provenance audit chains.

---

## 3. Six Enterprise Mock Exam Progression

| Mock Exam | Fictional Enterprise & Vertical | Signature Technical Challenges |
| :---: | :--- | :--- |
| **1** | **QuantaPay Autonomous Disputes** *(Fintech & Card Networks)* | Visa CE3.0 `Evaluator-Optimizer`, `MCP 2026-07-28` OAuth 2.1 + `CIMD`, `LangGraph` `interrupt()` Stripe-refund replay safety, bitemporal rulebooks, `Pass^5`, `NIM` `FP8` & `ASI09` IBAN diffs |
| **2** | **HelixVax Discovery Labs** *(Biopharma & Wet-Lab Robotics)* | `RDKit` `Tree-of-Thoughts`, `A2A v1.0` CRO tasks, `Hamilton STAR` robot `interrupt()` gates, Chinese-wall memory, Corrective `GraphRAG`, PK tables & `21 CFR Part 11` `WORM` |
| **3** | **CloudPulse Autonomous SRE** *(Cloud Infra & Incident Ops)* | `PromQL` `Reflexion`, `LangGraph` time-travel forks, `Firecracker` log forensics, `8xH100` `NIM` disaggregated serving, `KEDA` `KV-cache` scaling, `OTel` spans & `ASI08` bulkheads |
| **4** | **StrataLaw Contract Intelligence** *(Legal M&A & Regulatory)* | VDR ethical walls + 10-day deal purge, Amendment `$2M -> $10M` lineage, deterministic citation span gates, `DPO` partner tone, `ZDR` Frankfurt `NIM` & `EU AI Act` Art. 14/50 |
| **5** | **VeloceCart Commerce Concierge** *(Global Retail & Supply Chain)* | `Stylist -> Returns` Swarm handoffs, Berlin->Zurich memory supersession, `tau-bench` `Pass^8`, `8B` `LoRA` distillation + `RFT`, 4,000-session prefix cache & `OPA` refund caps |
| **6** | **AegisCyber SOC Copilot** *(Threat Hunting & SOAR)* | `KQL`/`Sigma` `Reflexion` + verifiable `RFT`, air-gapped `Firecracker` dropper decoders, `MCP` SHA-256 rug-pull pinning, syslog `ASI01` defense, out-of-band kill-switches & SWIFT CMDB `HITL` |
