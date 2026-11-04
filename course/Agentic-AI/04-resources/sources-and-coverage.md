# Authoritative Sources & Skill Coverage (`Agentic-AI`)

All `600` questions and `139` canonical option/sequence rationales in `course/Agentic-AI/` are authored originally from public specifications, standards, and engineering documentation verified as of **November 2026**. Zero recalled exam items or proprietary vendor sample-company names are used.

## 1. Primary Certification & Standards Baselines

1. **NVIDIA-Certified Professional: Agentic AI (`NCP-AAI`):** Official 10-domain exam guide (`60–70` questions, `120` minutes, Certiverse remote proctoring, 2-year validity) — <https://www.nvidia.com/en-us/learn/certification/agentic-ai-professional/>
2. **Linux Foundation Agentic AI Foundation (`AAIF`):** Open-governance umbrella hosting `MCP`, `A2A`, `AGENTS.md`, `Agent Skills`, `OpenSandbox`, `OpenEnv`, `agentgateway`, `goose`, `Agent Router`, and `OpenResponses` — <https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation>
3. **Model Context Protocol (`MCP`, `2026-07-28` specification) & IETF `RFC 9207` / `RFC 8707`:** Tools, Resources, Prompts, `stdio` vs stateless `Streamable HTTP` (`_meta`, `Mcp-Method` & `Mcp-Name`), OAuth 2.1 + `PKCE` + `iss` validation + Client ID Metadata Documents (`CIMD`), `Roots`, `Sampling`, and `Elicitation` — <https://modelcontextprotocol.io/introduction> & <https://datatracker.ietf.org/doc/html/rfc9207>
4. **Agent2Agent Protocol (`A2A v1.0` / `v1.0.1`):** Cryptographically signed `Agent Card`s (`JWS RFC 7515` + `JCS RFC 8785`), stateful `Task` lifecycles, `Message`/`Part`/`Artifact`, `JSON-RPC`/`gRPC`/`HTTP+JSON` bindings, `SSE`, and push webhooks — <https://a2a-protocol.org/latest/>
5. **`AGENTS.md` & `Agent Skills`:** Progressive context disclosure for coding and enterprise ops agents — <https://agents.md/>
6. **OWASP Top 10 for Agentic Applications (`ASI01:2026`–`ASI10:2026`):** Autonomous threat taxonomy and architectural mitigations — <https://genai.owasp.org/>
7. **Anthropic Engineering Research:** *Building Effective Agents* & *Effective Context Engineering for AI Agents* — <https://www.anthropic.com/research/building-effective-agents> & <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>
8. **LangGraph `1.x` Documentation:** StateGraph reducers, `Send()`, `PostgresSaver` persistence, `interrupt()`, and `Command(resume=...)` node-replay idempotency rules — <https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/>
9. **NVIDIA Platform Stack:** `NVIDIA NIM`, `TensorRT-LLM`, `NeMo Agent Toolkit`, `NeMo Retriever`, `NeMo Customizer`, and `NeMo Guardrails` — <https://docs.nvidia.com/nim/large-language-models/latest/introduction.html> & <https://docs.nvidia.com/nemo/guardrails/latest/index.html>
10. **Evaluation, Observability & Governance:** `tau-bench` (`Pass^k` consistency, <https://arxiv.org/abs/2406.12045>), `CRAG` (<https://arxiv.org/abs/2401.15884>), `GraphRAG` (<https://microsoft.github.io/graphrag/>), `OpenTelemetry` GenAI Agent Spans (<https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/>), `KEDA` (<https://keda.sh/docs/latest/>), `RFC 8693` OAuth 2.0 Token Exchange (<https://datatracker.ietf.org/doc/html/rfc8693>), `NIST AI RMF 1.0` (<https://www.nist.gov/itl/ai-risk-management-framework>), and `EU AI Act` (<https://artificialintelligenceact.eu/>).

## 2. Coverage Matrix Across All `34` Skills (`600` Questions)

Every exam set (`Set 1` through `Set 6`) enforces the exact `SKILL_PLAN` in `04-resources/bank.py`:
- **Domain 1 (`18`/set · `108` total):** `1.1` (`3`), `1.2` (`3`), `1.3` (`3`), `1.4` (`3`), `1.5` (`3`), `1.6` (`3`)
- **Domain 2 (`20`/set · `120` total):** `2.1` (`3`), `2.2` (`4`), `2.3` (`4`), `2.4` (`3`), `2.5` (`3`), `2.6` (`3`)
- **Domain 3 (`16`/set · `96` total):** `3.1` (`3`), `3.2` (`3`), `3.3` (`3`), `3.4` (`3`), `3.5` (`2`), `3.6` (`2`)
- **Domain 4 (`16`/set · `96` total):** `4.1` (`3`), `4.2` (`3`), `4.3` (`3`), `4.4` (`3`), `4.5` (`2`), `4.6` (`2`)
- **Domain 5 (`15`/set · `90` total):** `5.1` (`3`), `5.2` (`3`), `5.3` (`3`), `5.4` (`3`), `5.5` (`3`)
- **Domain 6 (`15`/set · `90` total):** `6.1` (`3`), `6.2` (`3`), `6.3` (`3`), `6.4` (`3`), `6.5` (`3`)
