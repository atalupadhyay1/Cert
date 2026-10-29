# Official Sources, Blueprint Mapping, and Fidelity Boundaries — CCAR-P

## Primary official sources (verified October 29, 2026)

1. **Claude Certified Architect – Professional (`CCAR-P`) Official Exam Guide (Version 1.0, Effective July 2026):**
   `https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf`
2. **Anthropic Partner Academy — Certifications Overview (including December 7, 2026 update notice):**
   `https://anthropic-partners.skilljar.com/page/partner-certifications`
3. **Anthropic Partner Academy — Certifications FAQ:**
   `https://anthropic-partners.skilljar.com/page/faq-certifications`
4. **Anthropic Engineering — Building Effective Agents & Multi-Agent Research System:**
   `https://www.anthropic.com/engineering/building-effective-agents`
   `https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents`
   `https://www.anthropic.com/engineering/multi-agent-research-system`
5. **Claude Platform Documentation — Prompt Caching, Tool Use, `defer_loading`, Compaction, Evals & Guardrails:**
   `https://platform.claude.com/docs/en/build-with-claude/prompt-caching`
   `https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching`
   `https://platform.claude.com/docs/en/test-and-evaluate/develop-tests`
   `https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks`
6. **Claude Code & Agent SDK Documentation — `CLAUDE.md`, Skills, Subagents, Hooks, and MCP:**
   `https://code.claude.com/docs/en/features-overview`
   `https://code.claude.com/docs/en/agent-sdk/overview`

## Exact 63-item blueprint math

| Domain | Official title | Weight | `weight × 63` | Mock count | Delta | Multi-select |
|---:|---|---:|---:|---:|---:|---:|
| 1 | `Solution Design & Architecture` | 17% | 10.71 | 11 | +0.29 | 3 (`2 M2 + 1 M3`) |
| 2 | `Claude Models, Prompting & Context Engineering` | 13% | 8.19 | 8 | -0.19 | 2 (`2 M2`) |
| 3 | `Integration` | 19% | 11.97 | 12 | +0.03 | 3 (`2 M2 + 1 M3`) |
| 4 | `Evaluation, Testing & Optimization` | 16% | 10.08 | 10 | -0.08 | 2 (`2 M2`) |
| 5 | `Governance, Safety & Risk Management` | 14% | 8.82 | 9 | +0.18 | 2 (`1 M2 + 1 M3`) |
| 6 | `Stakeholder Communication & Lifecycle Management` | 14% | 8.82 | 9 | +0.18 | 2 (`2 M2`) |
| 7 | `Developer Productivity & Operational Enablement` | 7% | 4.41 | 4 | -0.41 | 1 (`1 M2`) |
| **Total** | | **100%** | **63.00** | **63** | **max `0.41`** | **15 (`12 M2 + 3 M3`)** |

## 1-to-1 mapping of all 38 official blueprint objectives

| Local ID | Official CCAR-P Exam Guide v1.0 objective | Per exam | 6-set total |
|---|---|---:|---:|
| `1.1` | Translate business problems into technical Claude-based solutions | 2 | 12 |
| `1.2` | Design end-to-end architectures (input -> processing -> output -> feedback loops) | 2 | 12 |
| `1.3` | Select appropriate architectural patterns (workflows vs. agentic systems vs. augmented LLMs) | 2 | 12 |
| `1.4` | Design multi-agent systems and orchestration patterns | 2 | 12 |
| `1.5` | Apply decomposition techniques to break down complex workflows | 2 | 12 |
| `1.6` | Align solutions to business value pillars (efficiency, innovation, risk reduction) and SLAs | 1 | 6 |
| `2.1` | Select appropriate Claude models based on capability, cost, latency, and complexity trade-offs | 2 | 12 |
| `2.2` | Design effective system prompts, templates, and behavioral guardrails | 2 | 12 |
| `2.3` | Apply prompting strategies (zero-shot, few-shot, chain-of-thought) | 1 | 6 |
| `2.4` | Optimize context windows and token usage (chunking, compression, retrieval vs. in-context) | 1 | 6 |
| `2.5` | Implement prompt reuse and modularity (prompt caching, modular prompts, Skills) | 2 | 12 |
| `3.1` | Evaluate capability bloat and apply least privilege in tool/agent design | 2 | 12 |
| `3.2` | Identify security gaps in authentication and authorization across systems | 2 | 12 |
| `3.3` | Balance accuracy vs. latency in integration workflows | 1 | 6 |
| `3.4` | Design observability and monitoring strategies for production scale | 1 | 6 |
| `3.5` | Select appropriate chunking and indexing strategies for RAG pipelines | 1 | 6 |
| `3.6` | Choose retrieval approaches matched to data characteristics and query patterns | 1 | 6 |
| `3.7` | Evaluate connection protocols and integration patterns (MCP vs. API/CLI vs. agent-to-agent) | 2 | 12 |
| `3.8` | Evaluate progressive discovery vs. monolithic context strategy | 2 | 12 |
| `4.1` | Define evaluation metrics (accuracy, latency, cost, safety, security) | 2 | 12 |
| `4.2` | Design evaluation datasets and test frameworks using mixed methodologies | 2 | 12 |
| `4.3` | Conduct A/B testing and iterative improvements | 1 | 6 |
| `4.4` | Diagnose system issues (prompt failure, hallucinations, model mismatch) | 2 | 12 |
| `4.5` | Optimize token usage, latency, and cost-performance trade-offs | 2 | 12 |
| `4.6` | Monitor system performance using logging and observability tools | 1 | 6 |
| `5.1` | Implement guardrails and safety controls | 2 | 12 |
| `5.2` | Identify risks, limitations, and failure modes of LLM systems | 2 | 12 |
| `5.3` | Apply human-in-the-loop validation strategies | 2 | 12 |
| `5.4` | Ensure compliance with regulations (e.g., GDPR, HIPAA, FedRAMP) | 2 | 12 |
| `5.5` | Address ethical AI considerations (bias, fairness, transparency) | 1 | 6 |
| `6.1` | Conduct structured discovery and requirement gathering | 2 | 12 |
| `6.2` | Communicate architectural decisions and trade-offs | 2 | 12 |
| `6.3` | Manage stakeholder feedback loops and expectation alignment (including SLAs) | 2 | 12 |
| `6.4` | Document architectures and provide implementation guidance | 1 | 6 |
| `6.5` | Support lifecycle phases (discovery, design, handoff, monitoring, iteration) | 2 | 12 |
| `7.1` | Configure Claude tools and environments for teams (e.g., Claude Code) | 2 | 12 |
| `7.2` | Improve developer workflows using AI-assisted tooling | 1 | 6 |
| `7.3` | Support debugging and operational issue resolution | 1 | 6 |

## Format fidelity and explicit disclosures

- **Adapted Hotspot / matrix patterns:** Udemy's 17-column CSV schema supports `multiple-choice` and `multi-select` only. Interactive Pearson VUE Hotspot / matrix table items (Yes/No use-case suitability grids, Yes/No sound-architectural-practice grids, and `Pre-Processing / Model Stage / Post-Processing` dropdown grids) are adapted into 8 structured scenario items per exam (`48` across the 6 sets), verified automatically by `build.py` and `test_course.py`.
- **Policy nuance between v1.0 Guide and Partner Academy FAQ:** Section 10 of the July 2026 Exam Guide PDF states a 24-hour cancellation/reschedule window, whereas the Partner Academy Certifications FAQ page states a 48-hour window before appointment time via Pearson VUE; candidates should reschedule at least 48 hours ahead to avoid fee forfeiture.
- **Upcoming December 7, 2026 update:** Anthropic Partner Academy announces an exam update effective December 7, 2026 (updated guide publishing November 17, 2026). Re-check `04-resources/publication-checklist.md` once the November 17, 2026 guide releases.
