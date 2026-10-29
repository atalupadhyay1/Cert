# Curriculum Outline & Study Plan — Claude Certified Architect – Professional (CCAR-P)

## Package structure

| Udemy section | Deliverable | Questions | Recommended clock | Domain mix (`D1..D7`) |
|---|---|---:|---:|---|
| Practice Test 1 | Full-Length Mock Exam 1: Regulated Financial Services, Wealth Advisory, and Credit Operations | 63 | 120 min | `11 / 8 / 12 / 10 / 9 / 9 / 4` |
| Practice Test 2 | Full-Length Mock Exam 2: Healthcare Clinical Operations, Payer Claims, and Life Sciences | 63 | 120 min | `11 / 8 / 12 / 10 / 9 / 9 / 4` |
| Practice Test 3 | Full-Length Mock Exam 3: Global E-Commerce, Retail Supply Chain, and Omnichannel Customer Care | 63 | 120 min | `11 / 8 / 12 / 10 / 9 / 9 / 4` |
| Practice Test 4 | Full-Length Mock Exam 4: B2B SaaS Platform, Cloud Infrastructure, and Site Reliability Operations | 63 | 120 min | `11 / 8 / 12 / 10 / 9 / 9 / 4` |
| Practice Test 5 | Full-Length Mock Exam 5: Legal Tech, M&A Due Diligence, Insurance Underwriting, and Contract Lifecycle | 63 | 120 min | `11 / 8 / 12 / 10 / 9 / 9 / 4` |
| Practice Test 6 | Full-Length Mock Exam 6: Public Sector, Utilities Grid Operations, Manufacturing Quality, and Telecom | 63 | 120 min | `11 / 8 / 12 / 10 / 9 / 9 / 4` |
| **Total** | **Six exact-length mock exams across six enterprise verticals** | **378** | **12 hours** | **66 / 48 / 72 / 60 / 54 / 54 / 24** |

## Six-week architect preparation schedule

1. **Week 1 — Diagnostic Baseline & Domain 1–2 Foundations (Exam 1 untimed):**
   - Sit **Mock Exam 1** untimed, focusing on identifying the *binding constraint* in every stem before reading options.
   - Review Anthropic's *Building Effective Agents*, *Effective Context Engineering for AI Agents*, and *Prompt Caching* docs for any missed skills in `1.1–2.5`.
2. **Week 2 — Integration, Security Boundaries & RAG Precision (Exam 2):**
   - Study MCP server scopes, OBO OAuth propagation, pre-retrieval ACL filtering, Contextual Retrieval, hybrid BM25 + dense vector reranking, and `defer_loading: true` with Tool Search (`3.1–3.8`).
   - Sit **Mock Exam 2** in 135 minutes; audit every `Select two.` and `Select three.` miss.
3. **Week 3 — Evaluation Rigor, Root-Cause Diagnosis & Cost-Latency Optimization (Exam 3):**
   - Review mixed deterministic + human-calibrated LLM-as-judge frameworks, `pass^k` vs. `pass@k` reliability, component-isolated RAG vs. generation debugging, and Message Batches economics (`4.1–4.6`).
   - Sit **Mock Exam 3** under the live **120-minute** clock (~114 seconds/item).
4. **Week 4 — Governance, Safety, Compliance & Stakeholder Lifecycle (Exam 4):**
   - Review layered input/tool/output guardrails, indirect prompt injection via untrusted corpora, deterministic HITL gates on batched tool calls, ZDR / GDPR / HIPAA / FedRAMP boundaries, ADRs, and segmented SLAs (`5.1–6.5`).
   - Sit **Mock Exam 4** in 120 minutes closed-book.
5. **Week 5 — Claude Code Team Enablement & Cross-Domain Weak-Spot Remediation (Exam 5):**
   - Review Claude Code managed policies, `PreToolUse` / `PostToolUse` hooks, concise `CLAUDE.md` vs. on-demand `.claude/skills/` vs. isolated `.claude/agents/`, Plan Mode, headless CI Agent SDK runs, and multi-tool `tool_use_id` error handling (`7.1–7.3`).
   - Sit **Mock Exam 5** in 120 minutes closed-book.
6. **Week 6 — Dress Rehearsal & Pre-Exam Policy Check (Exam 6):**
   - Sit **Mock Exam 6** in one uninterrupted 120-minute session under proctored-room rules (single display, clear desk, no docs or translation tools).
   - If your exam date is on or after **December 7, 2026**, review the updated Exam Guide scheduled for **November 17, 2026** on the Anthropic Partner Academy before testing.

## 120-minute exam-day pacing strategy

- **Pass 1 (Minutes 0–90, ~85 seconds/item):** Answer clear single-choice and multiple-response items immediately; flag long multi-constraint trade-off or 6-option `Select three.` items after recording your best provisional choice (there is no penalty for guessing).
- **Pass 2 (Minutes 90–112):** Re-read flagged stems solely for the *disqualifying constraint* (e.g., byte-0 dynamic timestamp breaking cache, post-generation ACL leak, shared service credential, or sub-10ms latency budget).
- **Pass 3 (Minutes 112–120):** Confirm every `Select two.` item has exactly 2 selections and every `Select three.` item has exactly 3 selections before submitting.
