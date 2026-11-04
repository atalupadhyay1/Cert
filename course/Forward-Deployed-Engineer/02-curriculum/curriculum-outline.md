# Curriculum Outline — Forward Deployed Engineer (`CFDE` / Enterprise `FDE`)

**Blueprint Baseline:** November 2026 (*GSDC Certified Forward Deployed Engineer 13-Module Syllabus · AWS Partner FDE `Ground / Orchestrate / Prove` Pathways · Anthropic Claude Frontier Academy · NIST AI RMF 1.0 · OWASP Top 10 for LLM Applications*)  
**Course Structure:** `6` Full-Length Practice Exams × `100` Questions = `600` Original Customer-Embedded Scenarios (`0` Artificial Case Studies)

---

## Domain & Skill Map (`37` Skills · `100` Questions per Set)

### Domain 1 — Client Discovery, Problem Structuring, and Engagement Scoping (`15%` · `15` Qs/Set · `90` Total)
- **1.1 (`2 Qs/set`):** Distinguish Forward Deployed Engineering (`FDE`) from core SWE, pre-sales Solutions Engineering (`SE`), and advisory consulting
- **1.2 (`2 Qs/set`):** Conduct frontline operator shadowing and decompose ambiguous customer pain into `MECE` issue trees and counterfactual baseline KPIs
- **1.3 (`3 Qs/set`, incl. `1 M2`):** Select the right paradigm across deterministic SQL/rules, calibrated classical ML (`XGBoost`/`LightGBM`), `RAG`, `LoRA/PEFT` fine-tuning, fixed workflows, and autonomous agents
- **1.4 (`3 Qs/set`, incl. `1 O`):** Define `PoC -> Pilot -> Production` exit criteria, Solution Design Documents (`SDD`s) with explicit `non-goals`, and anti-scope-creep boundaries
- **1.5 (`2 Qs/set`):** Build enterprise AI unit-economics (`tokens + retries + rerank + infra + HITL labor`), TCO, `SLI/SLO/SLA` distinctions, and risk-adjusted CFO business cases
- **1.6 (`3 Qs/set`, incl. `1 M2`):** Navigate Week 1 multi-stakeholder alignment across executive sponsors, CISOs, privacy/export-control counsel (`DPA/BAA/ZDR/ITAR/CEII`), IT owners, and frontline users

### Domain 2 — Production Software, APIs, and Enterprise System Integration (`16%` · `16` Qs/Set · `96` Total)
- **2.1 (`2 Qs/set`):** Write production-grade typed Python/TypeScript services with `Pydantic` v2 validation, `mypy`/`ruff`, structured trace-correlated JSON logging, and recorded `pytest` contract fixtures
- **2.2 (`3 Qs/set`, incl. `1 M2`):** Design resilient `FastAPI` non-blocking async concurrency, `SSE` progressive streaming, `OpenAPI 3.1` contracts, `RFC 9457` problem details, and rate-limited endpoints
- **2.3 (`3 Qs/set`, incl. `1 O`):** Integrate brownfield enterprise systems (`AS/400`, `HL7 FHIR / X12`, `CICS COBOL`, `SAP IDoc/OData`, `OMS/Maximo`, `AMOS`) via Anti-Corruption Layers (`ACL`s), `12-Factor` `SIGTERM` draining, and `Strangler Fig` migrations
- **2.4 (`3 Qs/set`, incl. `1 M2`):** Implement enterprise `OIDC`/`SAML` federation, `OAuth 2.0 On-Behalf-Of` (`OBO`, `RFC 8693`) delegation, and keyless cloud `Workload Identity Federation` (`IRSA` / Azure / GKE)
- **2.5 (`2 Qs/set`):** Enforce deterministic `Idempotency-Key`s, transactional outboxes, bounded exponential backoff with full jitter, and dead-letter queues (`DLQ`s)
- **2.6 (`3 Qs/set`, incl. `1 M3`):** Build citation-highlighted `HITL` operator interfaces, `HMAC-SHA256` webhook verification, half-open circuit breakers, and seamless prototype-to-production architectures

### Domain 3 — Enterprise Data Engineering, Ontologies, and Grounded RAG — *"Ground"* (`18%` · `18` Qs/Set · `108` Total)
- **3.1 (`3 Qs/set`, incl. `1 M2`):** Design content-hashed incremental `CDC`/streaming ingestion pipelines with `Presidio` PII/PHI tokenization, canonical entity resolution, lineage, and quarantine `DLQ`s
- **3.2 (`2 Qs/set`):** Model governed enterprise domain ontologies, semantic metric layers, and point-in-time calibrated classical ML baselines (`eliminating target and temporal leakage`)
- **3.3 (`2 Qs/set`):** Architect layout-aware multimodal PDF/XML parsing (`preserving Markdown/HTML tables, units, and parent WARNING blocks`) and hierarchical parent-child chunking
- **3.4 (`3 Qs/set`, incl. `1 M2`):** Combine dense embeddings, sparse `BM25` lexical search, `Reciprocal Rank Fusion` (`RRF`), index-level metadata pre-filtering, cross-encoder reranking, and static prefix caching
- **3.5 (`3 Qs/set`, incl. `1 O`):** Enforce pre-retrieval document-level `ACL` security trimming, multi-tenant isolation, and bitemporal `effective_from`/`superseded_by` grounding
- **3.6 (`3 Qs/set`, incl. `1 M2`):** Mitigate `lost-in-the-middle` dilution, stale-revision drift, and ungrounded fabrication with post-generation span-verified citations and explicit abstention contracts
- **3.7 (`2 Qs/set`):** Choose cleanly between context engineering, security-trimmed `RAG`, KV prompt caching, `LoRA/PEFT` schema/terminology adaptation, and tabular ML

### Domain 4 — LLM Workflows, Tool Design, and Agentic Orchestration — *"Orchestrate"* (`20%` · `20` Qs/Set · `120` Total)
- **4.1 (`3 Qs/set`):** Apply grammar-constrained structured JSON outputs, static prompt-prefix KV-cache hygiene, and slice-validated model-tier latency/cost routing
- **4.2 (`3 Qs/set`, incl. `1 M2`):** Select deliberately among canonical patterns: `Prompt Chaining`, `Routing`, `Parallelization`, `Orchestrator-Workers`, and capped `Evaluator-Optimizer` loops
- **4.3 (`3 Qs/set`, incl. `1 O`):** Design ergonomic, token-efficient `MCP` (`Model Context Protocol`) servers with read/write separation, `OBO` least-privilege scopes, and parameterized server-side validation (`zero raw superuser SQL`)
- **4.4 (`3 Qs/set`, incl. `1 M2`):** Architect isolated sub-agent context handoffs, `mTLS`/`OAuth 2.1` `MCP` transport security, and hard step/token/cycle termination guards
- **4.5 (`3 Qs/set`, incl. `1 O`):** Implement durable stateful execution (`Temporal` / `Step Functions` / durable checkpointers), idempotent side effects, and compensating saga rollbacks
- **4.6 (`2 Qs/set`):** Design blast-radius-tiered `HITL` approval gates and architectural privilege separation against `OWASP LLM01` indirect prompt injection
- **4.7 (`3 Qs/set`, incl. `1 M3`):** Manage short-term working scratchpads, episodic session logs, governed semantic memory (`with ACLs & TTLs`), and artifact-URI context compaction

### Domain 5 — Cloud/Hybrid Deployment, CI/CD, Observability, and Reliability (`15%` · `15` Qs/Set · `90` Total)
- **5.1 (`3 Qs/set`):** Deploy across `PrivateLink` / `Private Service Connect` / air-gapped sovereign VPCs (`CMEK`), size on-prem `vLLM` GPU `VRAM` (`weights + KV-cache + PagedAttention`), and harden non-root `SBOM`-signed containers
- **5.2 (`3 Qs/set`, odd sets incl. `1 O`):** Automate `Terraform`/`Helm` GitOps, CI eval/CVE gates, side-effect-free `Shadow` replay, progressive `Canary`, and `Blue-Green` deployments (`zero per-site repo forking`)
- **5.3 (`3 Qs/set`, incl. `1 M2`):** Instrument **Four Golden Signals** and `OpenTelemetry` GenAI spans (`TTFT`, `TPOT`, `KV-cache %`, retrieval/tool waterfalls, and per-tenant `cost_usd`)
- **5.4 (`3 Qs/set`, incl. `1 M2`):** Operationalize `SLO` error-budget burn-rate freezes, contract-tested multi-region / DMZ model failover, and graceful deterministic fallback
- **5.5 (`3 Qs/set`, even sets incl. `1 O`):** Triage production `P1` latency spikes, `HTTP 429` (`TPM`/`RPM`) quota bursts, stream coalescing, memory leaks, and upstream data-ingestion drift

### Domain 6 — AI Security, Evaluation Harnesses, Governance, and Production Handover — *"Prove"* (`16%` · `16` Qs/Set · `96` Total)
- **6.1 (`3 Qs/set`, incl. `1 O`):** Build stratified SME-labeled golden datasets, deterministic code graders, human-calibrated `LLM-as-judge` rubrics (`Cohen's kappa`), and blocking CI eval gates
- **6.2 (`3 Qs/set`, incl. `1 M2`):** Diagnose **RAG Triad** metrics (`Context Relevance`, `Faithfulness`, `Answer Relevance`, `Recall@k`) and multi-step agent tool-trajectory efficiency
- **6.3 (`2 Qs/set`):** Defend against **`OWASP Top 10 for LLM Applications`**: `LLM01` indirect injection, `LLM05` improper output handling (`SQLi / XSS / shell=True / eval`), `LLM06` excessive agency, `LLM07` prompt leakage, `LLM08` vector poisoning, and `LLM10` unbounded consumption
- **6.4 (`2 Qs/set`, incl. `1 M2`):** Operationalize **`NIST AI RMF 1.0`** (`Govern`, `Map`, `Measure`, `Manage`), contractual `Zero Data Retention` (`ZDR`), and immutable `WORM` regulatory provenance logs
- **6.5 (`3 Qs/set`, incl. `1 O`):** Execute production readiness reviews, shadowed on-call + failover game-day drills with client SREs, and clean platform plugin extraction (`avoiding repo-fork sprawl`)
- **6.6 (`3 Qs/set`, incl. `1 M3`):** Drive `ADKAR` frontline champion adoption, deliver fallback-resilient live executive demos anchored to baseline ROI, and close continuous override flywheels

---

## Six Client Engagement Progression

| Set | Embedded Client Scenario | Industry & Compliance Regime | Primary Stack & Legacy Boundary |
| :---: | :--- | :--- | :--- |
| **1** | **KestrelFreight Global** | Maritime Customs & Port Brokerage (`GDPR`, WCO/CBP Rules) | Python, `FastAPI`, `AWS Bedrock`, `PrivateLink`, `AS/400` DB2/SOAP EDI |
| **2** | **VeridianCare Health** | Oncology Prior-Auth & Claims (`HIPAA`, `BAA`, `42 CFR Part 2`, `HITRUST`) | `HL7 FHIR R4`, `SMART on FHIR` OBO, `X12 278`, `Azure Private Link`, `AKS` |
| **3** | **AureliaBank Markets** | Commercial Credit & M&A (`SR 11-7` MRM, `MNPI`, `EU DORA`) | `SWIFT ISO 20022`, `XBRL`, `CICS COBOL`, `Temporal`, On-Prem `4×H100 vLLM` |
| **4** | **CinderPeak Manufacturing** | 300mm SiC Semiconductor Fab (`IEC 62443` OT/IT DMZ, `IATF 16949`) | `SAP S/4HANA` `IDoc`/`OData`, `OPC-UA`, `SEMI E10`, `Snowflake`, DMZ `vLLM` |
| **5** | **SolaraGrid Utilities** | Electric Grid Storm Dispatch (`NERC CIP`, `FERC CEII`, PUC `CAIDI`) | `Apache Kafka` `AMI`, `PostGIS`, `IBM Maximo/OMS` SOAP, `GCP PSC` + `Vertex AI` |
| **6** | **BorealAero Defense & Maintenance** | Heavy Aviation MRO (`FAA Part 145`, `ITAR` / `CMMC Level 2` GovCloud) | `S1000D` / `ATA iSpec 2200`, `Swiss-AS AMOS`, PIV `OIDC` OBO, Enclave `vLLM` |
