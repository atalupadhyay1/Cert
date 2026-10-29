# 🚀 Claude Certified Architect – Professional (CCAR-P) — Practice Test Landing Page

Six 63-item full-length mock exams · 378 original questions · every option explained · multiple-choice & multiple-response (`Select two.` / `Select three.`) · suitability, sound-practice & `Pre-Processing / Model Stage / Post-Processing` layer-mapping patterns · 120-minute live exam pace

This package is an independent study aid for the **Claude Certified Architect – Professional (`CCAR-P`)** certification from Anthropic, built for systems architects, AI platform engineers, and technical leads preparing to design, integrate, evaluate, govern, and scale production Claude architectures.

---

## 📋 Udemy Course Metadata (copy/paste into the course creation form)

### 1. Course Title

```text
Claude Certified Architect – Professional (CCAR-P) Practice Tests — 6 Exams, 378 Questions
```

Alternative shorter title: Anthropic CCAR-P Architect Professional: 378 Practice Questions

### 2. Course Subtitle

```text
Six exact-length 63-question CCAR-P mock exams with every option explained — workflows vs. agents, caching, MCP, defer_loading, RAG, evals, and governance.
```

### 3. Course Description

```text
This course contains 378 original practice questions for the Anthropic Claude Certified Architect – Professional (CCAR-P) exam, organized as six full-length 63-question mock exams timed at 120 minutes each (~114 seconds per item). Every exam follows the official seven-domain CCAR-P blueprint — 17% Solution Design & Architecture, 13% Claude Models, Prompting & Context Engineering, 19% Integration, 16% Evaluation, Testing & Optimization, 14% Governance, Safety & Risk Management, 14% Stakeholder Communication & Lifecycle Management, and 7% Developer Productivity & Operational Enablement — with integer domain counts of 11 / 8 / 12 / 10 / 9 / 9 / 4 across all six sets.

Every question mirrors the architect-level decision style of CCAR-P: realistic enterprise constraints (bursty ingestion queues, p95 latency budgets, 60+ tool catalogs, multi-tenant ACL boundaries, post-refresh RAG regressions, EU GDPR / HIPAA / FedRAMP compliance mandates, segmented stakeholder SLAs, and team-wide Claude Code governance) determine which pattern wins and why tempting alternatives fail.

WHAT MAKES THIS DIFFERENT
• Exact live exam length and pacing: 63 scored items in 120 minutes per mock exam, matching the published Pearson VUE CCAR-P specification and domain weights within 0.41 items per domain.
• Realistic CCAR-P question patterns: each exam pairs 48 four-option single-answer trade-off scenarios with 15 multiple-response items (12 five-option "Select two." and 3 six-option "Select three." items), including structured adaptations of candidate use-case suitability, sound architectural practice at scale, and Pre-Processing / Model Stage / Post-Processing execution-layer classification.
• Current Anthropic platform mechanics: covers deterministic workflows vs. orchestrator-workers subagent isolation, ephemeral prompt caching prefix order, server-side compaction vs. preserved thinking blocks, progressive tool discovery (`defer_loading: true` + Tool Search Tool `tool_reference` blocks), Contextual Retrieval + hybrid BM25/vector reranking, `pass^k` vs. `pass@k` agent reliability, Message Batches async economics, Zero Data Retention (ZDR), native Citations, and Claude Code (`CLAUDE.md`, Skills, Subagents, `PreToolUse`/`PostToolUse` hooks, Plan Mode, and MCP scopes).
• Every option explained: correct choices state why they satisfy the binding constraint in the stem, and every distractor names the real capability it represents and why it misfires under that constraint.

WHAT YOU GET
• Six full-length mock exams of 63 questions each (378 original questions total across six distinct enterprise verticals).
• Per-option explanations, an overall architectural rationale, mapped official domain, 38-skill study-map reference, and official Anthropic documentation links on every item.
• Curriculum outline, six-week architect study plan, 120-minute pacing strategy, and domain diagnostic guide.

EXAM FACTS & UPCOMING VERSION NOTICE
Verified against the official CCAR-P Exam Guide (Version 1.0, Effective July 2026) and Anthropic Partner Academy certification pages on October 29, 2026: CCAR-P delivers 63 scored multiple-choice and multiple-response items in 120 minutes via Pearson VUE (online proctored or test center) in English and Japanese, priced at $175 USD (Claude Partner Network organization email required; partner-tier discounts apply), with a criterion-referenced scaled passing score of 720 on a 100–1,000 scale and 12-month credential validity. Anthropic Partner Academy has announced that certification exams update on December 7, 2026, with updated exam guides available on November 17, 2026; this course baselines strictly against Version 1.0 (July 2026) and makes no claim about unpublished future blueprint changes.

IMPORTANT DISCLOSURES
• Independent educational material — not affiliated with, endorsed by, or sponsored by Anthropic or Pearson VUE.
• Interactive Pearson VUE Hotspot / matrix table widgets cannot render natively in Udemy's multiple-choice / multi-select CSV player and are adapted here into structured MC and multi-select stems.
• Practice percentages are not scaled scores; a raw percentage on Udemy is not a conversion to Anthropic's 720 / 1,000 scaled cut score.
```

### 4. What will students learn in your course?

```text
• Choose deterministic workflows, RAG calls, or multi-agent loops.
• Map components to Pre-Processing, Model Stage, and Post-Processing.
• Order prompt-cache prefixes, Skills, and server-side compaction.
• Enforce least privilege, OBO auth, MCP governance, and defer_loading.
• Design Contextual Retrieval, hybrid BM25+vector search, and traces.
• Build mixed code/LLM-judge evals, `pass^k` gates, and A/B canaries.
• Layer prompt-injection guardrails, HITL gates, and ZDR compliance.
• Configure team Claude Code hooks, subagents, and segmented SLAs.
```

### 5. What are the requirements or prerequisites for taking your course?

```text
• No formal prerequisite certification is required for CCAR-P.
• Three-plus years in systems, cloud, or platform architecture helps.
• Hands-on experience with the Claude Messages API and tool use helps.
• Familiarity with REST APIs, OAuth, RAG indexing, and CI/CD basics.
• Note: live CCAR-P registration requires a Claude Partner Network email.
```

### 6. Who is this course for?

```text
• Solution and enterprise architects preparing for Anthropic CCAR-P.
• Partner engineers building production Claude systems for clients.
• AI platform leads governing MCP gateways, RAG, and guardrails.
• Staff engineers configuring Claude Code and Agent SDK for teams.
• Technical leads translating LLM trade-offs and SLAs for executives.
```

---

## practice-test-1 — Full-Length Mock Exam 1: Regulated Financial Services, Wealth Advisory, and Credit Operations

### Full description

Sixty-three blueprint-weighted CCAR-P questions set in commercial lending, wealth advisory, brokerage surveillance, and payment operations: hybrid deterministic DSCR math plus narrative covenant synthesis, retail-bank candidate workflow suitability, `Pre-Processing / Model Stage / Post-Processing` loan-pipeline mapping, prompt-chaining compliance gates, orchestrator-workers equity research across 400k+ tokens, tiered Haiku/Sonnet/Opus routing, static-first prompt caching, least-privilege removal of wire/closure tools, advisor-scoped OBO OAuth, Chinese-wall pre-retrieval ACL filtering, `defer_loading: true` across 68 back-office tools, post-refresh Fed circular RAG debugging, ACH human-in-the-loop gates, GDPR/BaFin ZDR residency and vector erasure lineage, segmented K-1 mortgage SLAs, and PCI-DSS Claude Code managed hooks. Includes 48 multiple-choice and 15 multiple-response (`Select two.` / `Select three.`) items with every option explained. Allocates 11 / 8 / 12 / 10 / 9 / 9 / 4 items across Domains 1–7.

### Trimmed description

63 CCAR-P questions on financial services, wealth, and credit architectures — caching, MCP, `defer_loading`, RAG, guardrails, every option explained.

---

## practice-test-2 — Full-Length Mock Exam 2: Healthcare Clinical Operations, Payer Claims, and Life Sciences

### Full description

Sixty-three blueprint-weighted CCAR-P questions set in hospital networks, health-plan prior authorization, EHR FHIR R4 gateways, and pharmacovigilance: combining deterministic member-coverage math with clinical medical-necessity synthesis, clinical candidate use-case suitability, `Pre-Processing / Model Stage / Post-Processing` prior-auth pipeline mapping, evaluator-optimizer readability/dosage loops, preserving assistant thinking blocks across multi-turn clinical tool calls, batched computer-use screenshot pruning for RCM portals, SMART-on-FHIR OBO token scoping, 42 CFR Part 2 pre-retrieval ACL filtering, Contextual Retrieval for FDA drug-label dosage tables, hybrid BM25+vector CPT/HCPCS search, HIPAA BAA + Zero Data Retention endpoints, licensed medical-director HITL gates on adverse determinations, and HIPAA-compliant Claude Code team policies. Includes 48 multiple-choice and 15 multiple-response items with every option explained.

### Trimmed description

63 CCAR-P questions on healthcare, FHIR MCP, payer claims, and life-sciences architectures — HIPAA ZDR, RAG, evals, every option explained.

---

## practice-test-3 — Full-Length Mock Exam 3: Global E-Commerce, Retail Supply Chain, and Omnichannel Customer Care

### Full description

Sixty-three blueprint-weighted CCAR-P questions set in global marketplaces, supply-chain control towers, and peak-holiday customer care: supplier chargeback math vs. carrier-remark synthesis, retail candidate workflow suitability, `Pre-Processing / Model Stage / Post-Processing` multilingual catalog enrichment mapping, parallel voting on counterfeit/hazmat listings, asynchronous Message Batches for 420k-SKU seasonal refreshes, XML seller-listing injection isolation, shopper-scoped OAuth vs. shared admin tokens, `defer_loading: true` across 64 freight/customs tools, carrier tracking enum drift detection, deterministic pre-tool refund-cap hooks against social-media jailbreaks, CCPA/GDPR shopper embedding purge lineage, and storefront Claude Code skills and subagents. Includes 48 multiple-choice and 15 multiple-response items with every option explained.

### Trimmed description

63 CCAR-P questions on global e-commerce, supply chain, and omnichannel care — peak concurrency, caching, tool search, every option explained.

---

## practice-test-4 — Full-Length Mock Exam 4: B2B SaaS Platform, Cloud Infrastructure, and Site Reliability Operations

### Full description

Sixty-three blueprint-weighted CCAR-P questions set in multi-tenant B2B SaaS, cloud infrastructure, and SRE incident response: deterministic Prometheus SLA math plus postmortem synthesis, cloud-vendor candidate use-case suitability, `Pre-Processing / Model Stage / Post-Processing` alert-enrichment mapping, parallel sectioning on 150-question security RFPs, server-side compaction on 140k-token war-room sessions, read-only Kubernetes diagnostic least privilege, multi-tenant pre-retrieval `tenant_id` filtering, rejecting 4ms-hot-path gateway LLM calls in favor of deterministic code, `pass^5` vs. `pass@5` Terraform remediation reliability, cache-read-ratio drop alerts after CI deploys, indirect injection defense on public GitHub issue triage, and monorepo Claude Code managed hooks plus Plan Mode. Includes 48 multiple-choice and 15 multiple-response items with every option explained.

### Trimmed description

63 CCAR-P questions on multi-tenant SaaS, cloud infrastructure, and SRE operations — multi-agent RCA, compaction, security, every option explained.

---

## practice-test-5 — Full-Length Mock Exam 5: Legal Tech, M&A Due Diligence, Insurance Underwriting, and Contract Lifecycle

### Full description

Sixty-three blueprint-weighted CCAR-P questions set in corporate law firms, virtual data rooms, specialty insurance underwriting, and CLM platforms: actuarial rating-table math plus loss-control narrative synthesis, legal/Lloyd's candidate use-case suitability, `Pre-Processing / Model Stage / Post-Processing` M&A diligence mapping, evaluator-optimizer defined-term redline verification, 24k-token Contracting Playbook prefix caching plus jurisdictional Skills, strict law-firm ethical-wall pre-retrieval ACL filtering, Contextual Retrieval on 300-page reinsurance treaties, hybrid BM25+vector search for ISO endorsement forms (`HO-00-03`) and statutes, verbatim quote substring + calibrated partner-rubric mixed evaluation, dataroom PDF white-text indirect injection defense, deal-termination destruction lineage, and SOC 2 Claude Code team configuration. Includes 48 multiple-choice and 15 multiple-response items with every option explained.

### Trimmed description

63 CCAR-P questions on legal tech, M&A diligence, insurance underwriting, and CLM — ethical walls, citations, hybrid RAG, every option explained.

---

## practice-test-6 — Full-Length Mock Exam 6: Public Sector, Utilities Grid Operations, Manufacturing Quality, and Telecom

### Full description

Sixty-three blueprint-weighted CCAR-P questions set in electric utilities, semiconductor/aerospace manufacturing, telecom NOCs, and public-sector agencies: historian dissolved-gas math plus technician-log synthesis, OT/telecom candidate use-case suitability, `Pre-Processing / Model Stage / Post-Processing` field work-order mapping, parallel safety voting on public emergency advisories, batched GIS computer-use screenshot pruning, strict IT/OT least-privilege removal of breaker-actuation tools, NERC-CIP CEII pre-retrieval clearance filtering, `defer_loading: true` across 70 telecom NOC tools, preserving thinking blocks in factory fault-tree loops, FedRAMP High + CUI Zero Data Retention boundaries, multilingual tariff fairness/citation audits, and legacy COBOL/ADA modernization with Claude Code Plan Mode and subagents. Includes 48 multiple-choice and 15 multiple-response items with every option explained.

### Trimmed description

63 CCAR-P questions on public sector, grid ops, manufacturing, and telecom — IT/OT safety, FedRAMP High, NOC scaling, every option explained.

---

## 📊 Blueprint allocation (identical on all six exams)

| Official CCAR-P domain | Published weight | Exact share (×63) | Items per exam | Multi-select | Bank total |
|---|---:|---:|---:|---:|---:|
| 1. Solution Design & Architecture | 17% | 10.71 | 11 | 3 | 66 |
| 2. Claude Models, Prompting & Context Engineering | 13% | 8.19 | 8 | 2 | 48 |
| 3. Integration | 19% | 11.97 | 12 | 3 | 72 |
| 4. Evaluation, Testing & Optimization | 16% | 10.08 | 10 | 2 | 60 |
| 5. Governance, Safety & Risk Management | 14% | 8.82 | 9 | 2 | 54 |
| 6. Stakeholder Communication & Lifecycle Management | 14% | 8.82 | 9 | 2 | 54 |
| 7. Developer Productivity & Operational Enablement | 7% | 4.41 | 4 | 1 | 24 |
| **Total** | **100%** | **63.00** | **63** | **15** | **378** |

## 🗺️ 38-skill study map (1-to-1 with Section 6 of the CCAR-P Exam Guide v1.0)

| Domain | Official blueprint objectives covered in every exam | Items |
|---|---|---:|
| 1. Solution Design & Architecture | Business-to-Claude translation (`1.1`), end-to-end Pre/Model/Post + feedback pipelines (`1.2`), workflows vs. agents vs. augmented LLMs (`1.3`), multi-agent orchestration & subagent isolation (`1.4`), workflow decomposition (`1.5`), value pillars & SLA budgeting (`1.6`) | 11 |
| 2. Claude Models, Prompting & Context Engineering | Model capability/cost/latency routing (`2.1`), system prompts, XML fences & JSON schemas (`2.2`), zero/few-shot & extended thinking (`2.3`), context compaction, screenshot batching & JIT retrieval (`2.4`), prompt caching, modular prompts & Skills (`2.5`) | 8 |
| 3. Integration | Capability bloat & least privilege (`3.1`), OBO AuthN/AuthZ, pre-retrieval ACLs & network egress (`3.2`), accuracy-latency balancing (`3.3`), OpenTelemetry production observability (`3.4`), Contextual Retrieval chunking & indexing (`3.5`), hybrid BM25+vector+rerank retrieval (`3.6`), MCP vs. REST/CLI vs. agent-to-agent (`3.7`), `defer_loading` progressive discovery vs. monolithic context (`3.8`) | 12 |
| 4. Evaluation, Testing & Optimization | Multi-dimensional scorecards (`4.1`), mixed code + calibrated LLM-judge datasets & `pass^k` (`4.2`), shadow traffic & A/B canaries (`4.3`), isolating retrieval vs. prompt vs. model-mismatch issues (`4.4`), caching, routing, batch & thinking-token optimization (`4.5`), drift & cache-ratio monitoring (`4.6`) | 10 |
| 5. Governance, Safety & Risk Management | Layered input/tool/output guardrails (`5.1`), indirect prompt injection & compounding agent errors (`5.2`), risk-tiered human-in-the-loop gates (`5.3`), GDPR, HIPAA BAA, FedRAMP High, ZDR & vector erasure lineage (`5.4`), cohort fairness, Citations & AI disclosure (`5.5`) | 9 |
| 6. Stakeholder Communication & Lifecycle Management | Structured corpus/baseline discovery (`6.1`), executive/CISO/CFO trade-off matrices (`6.2`), segmented SLAs & production feedback loops (`6.3`), ADRs, schema contracts & SRE runbooks (`6.4`), stage-gated rollouts & model-deprecation migrations (`6.5`) | 9 |
| 7. Developer Productivity & Operational Enablement | Team Claude Code managed policies, `CLAUDE.md`, Hooks, Skills & Subagents (`7.1`), Plan Mode & headless CI Agent SDK workflows (`7.2`), debugging multi-tool `tool_use_id` errors & MCP timeouts (`7.3`) | 4 |

## 🎬 Welcome Message

```text
Welcome to Claude Certified Architect – Professional (CCAR-P) Practice Tests.

The live CCAR-P exam delivers 63 scored multiple-choice and multiple-response items in 120 minutes (~114 seconds per item) across seven domains. Each of the six mock exams in this course matches that exact 63-question length and 11 / 8 / 12 / 10 / 9 / 9 / 4 domain allocation.

How to get the highest return from these six exams:
1. Take Exam 1 untimed first and read every option explanation — even on questions you answered right. CCAR-P rarely tests isolated definitions; almost every question turns on a concrete operational constraint (token prefix order, blast radius, network boundary, post-refresh index state, regulatory retention, or segmented SLA).
2. Log misses by domain and local skill ID (1.1 through 7.3), review the linked official Anthropic documentation before starting the next set, and sit Exams 4–6 under strict 120-minute timing with no notes or docs open.
3. Practice percentages are not scaled scores: Anthropic reports CCAR-P on a 100–1,000 scale (720 passing), and multiple-response items require selecting every correct option.
```

## 🎉 Congratulations Message

```text
Congratulations on completing all six CCAR-P full-length mock exams — 378 original architect scenarios across all 38 blueprint objectives.

Before exam day on Pearson VUE, confirm you can reason decisively through:
• Deterministic workflows vs. single augmented calls vs. orchestrator-workers subagents, plus Pre-Processing / Model Stage / Post-Processing boundaries
• Static-first prompt caching breakpoints, preserved assistant thinking blocks, server-side compaction, and on-demand Agent Skills
• Least-privilege tool removal, user-scoped OBO auth, pre-retrieval ACL filtering, MCP governance, and `defer_loading: true` with Tool Search
• Isolating post-refresh RAG retrieval regressions from prompt/model issues, measuring `pass^k` consistency, and gating releases behind shadow/canary trials
• Indirect prompt-injection defenses, deterministic pre-tool HITL gates, ZDR / GDPR / HIPAA / FedRAMP compliance, segmented SLAs, and team Claude Code hooks

Note on exam updates: Anthropic Partner Academy announced that certification exams update on December 7, 2026 (updated exam guide available November 17, 2026). Check the Anthropic Partner Academy page before your scheduled appointment for any post-November 17 guide delta. Best of luck on exam day!
```

## ❓ Frequently asked questions

**Are these real or recalled CCAR-P exam questions?**
No. All 378 questions, options, and explanations are 100% original scenarios authored from official Anthropic documentation and the public `CCAR-P` Exam Guide (Version 1.0, July 2026). No confidential live items or official sample items are reproduced.

**How does CCAR-P differ from CCAR-F (Architect – Foundations)?**
`CCAR-P` is the Partner Academy's 63-item, 120-minute, seven-domain Professional Architect exam covering enterprise architecture, model/context engineering, MCP/RAG/progressive discovery integration, evaluation, governance/compliance, stakeholder lifecycle management, and team developer enablement — delivered as 63 standalone items with no multi-question case-study split screen.

**How are interactive Pearson VUE Hotspot / matrix items handled in Udemy?**
Udemy's CSV bulk importer supports `multiple-choice` and `multi-select` only. Interactive Pearson VUE Hotspot / table-grid widgets cannot render natively in Udemy, so every exam includes **8 structured adaptations** testing those exact judgment patterns: mapping decomposed components across `Pre-Processing`, `Model Stage`, and `Post-Processing`, evaluating candidate workflows/use cases for Claude suitability, and evaluating architectural statements at production concurrency scale.

**What happens on December 7, 2026?**
As verified on the Anthropic Partner Academy certifications page on October 29, 2026, Anthropic announced that its certification exams update on **December 7, 2026**, with updated exam guides publishing on **November 17, 2026**. Candidates testing on or after December 7, 2026 should review the November 17, 2026 Exam Guide for any objective or model-lineup updates.

**Who can register for the live CCAR-P exam?**
Per Anthropic's Partner Academy FAQ, `CCAR-P` is offered through the **Claude Partner Network** (registration requires your partner organization's corporate email domain; personal email domains are not eligible). List price is **$175 USD** (partner-tier discounts apply), passing requires a **scaled score of 720** (100–1,000), and the credential is valid for **12 months**.

## ⚖️ Rights and attribution

All 378 questions and accompanying course documents are original work created for this course. Anthropic®, Claude®, Claude Code™, and Model Context Protocol (MCP) are trademarks of Anthropic, PBC; Pearson VUE® is a trademark of Pearson Education, Inc. Independent study package — not affiliated with, endorsed by, or sponsored by Anthropic or Pearson VUE.
