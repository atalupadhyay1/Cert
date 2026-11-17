# Agentic AI (`MCP`) Blueprint Alignment & Telemetry

**Baseline:** `November 2026 (MCP Specification 2025-11-25 · MCP Registry & Inspector · OAuth 2.1 + RFC 8707/9207 + CIMD · OWASP MCP Security Checklist)`

| Domain # | Agentic AI Consolidated Domain | Weight Range | Items / Set | Multi-Select / Set | 6-Set Total |
| :---: | :--- | :---: | :---: | :---: | :---: |
| `1` | **MCP Foundations, Architecture & Lifecycle** | `16–20%` | `18` (`18%`) | `3` | `108` |
| `2` | **Tools, Resources & Resource Templates** | `18–22%` | `20` (`20%`) | `3` | `120` |
| `3` | **Prompts, Sampling, Roots & Elicitation** | `14–18%` | `16` (`16%`) | `3` | `96` |
| `4` | **Transports, Sessions & Protocol Evolution** | `14–18%` | `16` (`16%`) | `2` | `96` |
| `5` | **Authorization, Security, Trust & Registry** | `13–17%` | `15` (`15%`) | `2` | `90` |
| `6` | **SDKs, Deployment, Observability & Ecosystem** | `13–17%` | `15` (`15%`) | `3` | `90` |
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
| `1` | Host-Client-Server Triad, SDK Scaffolds, Tool Poisoning Defense & Registry Trust | `84` (`21/21/21/21`) | `16` | `67` | `7` | `0` | `283` |
| `2` | Initialization Handshake, Resource Templates, Streamable HTTP Sessions & Elicitation | `84` (`21/21/21/21`) | `16` | `59` | `6` | `0` | `316` |
| `3` | JSON-RPC Framing, Tools vs Resources, OAuth 2.1 PKCE & Inspector CI Gates | `84` (`21/21/21/21`) | `16` | `60` | `6` | `0` | `320` |
| `4` | Capabilities Negotiation, Completions API, Logging Levels & Audit Provenance | `84` (`21/21/21/21`) | `16` | `63` | `8` | `0` | `360` |
| `5` | Progress & Cancellation, Sampling Delegation, Roots Boundaries & Env Isolation | `84` (`21/21/21/21`) | `16` | `64` | `7` | `0` | `278` |
| `6` | SSE Deprecation → Streamable HTTP, Batching, Reconnect Resumability & Gateway Mesh | `84` (`21/21/21/21`) | `16` | `65` | `10` | `0` | `272` |

## Bank-Wide Uniqueness & Term Coverage

- **Total authored questions:** `600` (`0` duplicate stems, `0` duplicate rationales, `0` artificial case studies)
- **Cross-course collision check:** `0` collisions across `32` sibling courses (`192` CSV files)
- **Canonical `TERMS` exercised:** `120 / 120` (`100.0%`)
- **Max pairwise stem Jaccard similarity:** `0.7188` (`E2Q018` vs `E2Q057`, ceiling `<= 0.72`)
