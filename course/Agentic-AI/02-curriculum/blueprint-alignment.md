# Agentic AI (`NCP-AAI / AAIF`) Blueprint Alignment & Telemetry

**Baseline:** `November 2026 (NVIDIA NCP-AAI 10-Domain Blueprint · Linux Foundation AAIF MCP 2026-07-28 & A2A v1.0 · OWASP Top 10 for Agentic Applications ASI01–ASI10)`

| Domain # | Agentic AI Consolidated Domain | Weight Range | Items / Set | Multi-Select / Set | 6-Set Total |
| :---: | :--- | :---: | :---: | :---: | :---: |
| `1` | **Agentic Architectures, Reasoning Loops, and Multi-Agent Topologies** | `16–20%` | `18` (`18%`) | `3` | `108` |
| `2` | **Agent Development, Tool Contracts, MCP, and Durable State Graphs** | `18–22%` | `20` (`20%`) | `3` | `120` |
| `3` | **Memory Systems, Context Engineering, and Agentic RAG** | `14–18%` | `16` (`16%`) | `3` | `96` |
| `4` | **Agent Evaluation, Trajectory Grading, and Model Optimization** | `14–18%` | `16` (`16%`) | `2` | `96` |
| `5` | **Inference Acceleration, Scaling, and Agent Observability** | `13–17%` | `15` (`15%`) | `2` | `90` |
| `6` | **Agentic Security, Guardrails, Governance, and Human Oversight** | `13–17%` | `15` (`15%`) | `3` | `90` |
| **Total** | **All 6 Domains · 34 Competency Skills** | **100%** | **100** | **16** | **600** |

## Official NVIDIA `NCP-AAI` (10 Domains) & Standards Crosswalk

| Course Domain | Items/Set | Official NVIDIA `NCP-AAI` Domains (`100%`) | Open Standards & Security Mapping |
| :--- | :---: | :--- | :--- |
| **D1: Agentic Architectures & Multi-Agent Topologies** | `18` | Agent Architecture & Design (`15%`), Planning (`3%`) | `AAIF` `A2A v1.0`, `AGENTS.md`, `Agent Skills` |
| **D2: Agent Development, Tool Contracts, MCP & State Graphs** | `20` | Agent Development (`15%`), Platform Tooling (`5%`) | `MCP 2026-07-28`, `LangGraph 1.x`, `OpenSandbox` |
| **D3: Memory Systems, Context Engineering & Agentic RAG** | `16` | Knowledge Integration (`10%`), Cognition & Memory (`7%`) | `NeMo Retriever`, `CRAG`, `Self-RAG`, `GraphRAG` |
| **D4: Agent Evaluation, Trajectory Grading & Optimization** | `16` | Evaluation and Tuning (`13%`), Customizer (`2%`) | `OpenEnv`, `Pass^k` (`tau-bench`), `SFT`/`DPO`/`RFT` |
| **D5: Inference Acceleration, Scaling & Agent Observability** | `15` | Deployment & Scaling (`13%`), Run/Monitor (`5%`), NIM (`2%`) | `NVIDIA NIM`, `TensorRT-LLM`, `vLLM`, `OTel GenAI` |
| **D6: Agentic Security, Guardrails, Governance & Oversight** | `15` | Safety, Ethics & Compliance (`5%`), Human-AI Oversight (`5%`) | `OWASP ASI01–ASI10`, `NeMo Guardrails`, `EU AI Act` |

## Per-Set Telemetry

| Set | Enterprise Scenario Theme | MC (`S`+`O`) | MS (`M2`+`M3`) | `____` Fills | `Proposed solution:` | Case Items | Max Q Chars |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `1` | ReAct vs Plan-and-Execute, MCP 2026-07-28 OAuth 2.1, LangGraph interrupt() Sagas & OWASP ASI01/ASI09 Controls | `84` (`21/21/21/21`) | `16` | `31` | `8` | `0` | `472` |
| `2` | Hierarchical Supervisor + A2A v1.0 Cards, Corrective GraphRAG, Pass^k Trajectory Evals & ZDR/HIPAA Guardrails | `84` (`21/21/21/21`) | `16` | `25` | `6` | `0` | `430` |
| `3` | Swarm vs DAG Topologies, OpenSandbox MicroVMs, NVIDIA NIM / vLLM Prefix Caching, KEDA & OTel GenAI Spans | `84` (`21/21/21/21`) | `16` | `23` | `6` | `0` | `471` |
| `4` | Evaluator-Optimizer Loops, Bitemporal ACL-Trimmed RAG, Calibrated LLM-as-Judge, EU AI Act & WORM Provenance | `84` (`21/21/21/21`) | `16` | `30` | `6` | `0` | `448` |
| `5` | Adaptive Routing, Parallel Idempotent Tools, 4-Tier Episodic/Semantic Memory, SFT/DPO/RFT & Pareto Routing | `84` (`21/21/21/21`) | `16` | `26` | `6` | `0` | `447` |
| `6` | AGENTS.md & Agent Skills, MCP Rug-Pull Pinning, Speculative Decoding, Circuit Breakers & Kill-Switch Containment | `84` (`21/21/21/21`) | `16` | `23` | `6` | `0` | `437` |

## Bank-Wide Uniqueness & Term Coverage

- **Total authored questions:** `600` (`0` duplicate stems, `0` duplicate rationales, `0` artificial case studies)
- **Cross-course collision check:** `0` collisions across `31` sibling courses (`186` CSV files)
- **Canonical `TERMS` exercised:** `139 / 139` (`100.0%`)
- **Max pairwise stem Jaccard similarity:** `0.4118` (`E2Q045` vs `E4Q045`, ceiling `<= 0.72`)
