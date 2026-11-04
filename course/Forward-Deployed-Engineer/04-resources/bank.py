"""Question bank loader and blueprint constants for Forward Deployed Engineer (6 x 100 = 600 questions).

Aligned to the 2026 Forward Deployed Engineer credential & competency landscape:
- GSDC Certified Forward Deployed Engineer (CFDE) 13-Module Syllabus (40 MCQs, 90 min, 65% pass, closed-book, 5-year validity)
- AWS Partner Forward Deployed Engineer (FDE) Pathways: Ground, Orchestrate, Prove (Oct 2026; FDE Validated / FDE Advanced)
- Anthropic Claude Frontier Academy (Frontier Deployed Engineer / Claude Resident Engineer, Oct 2026)
- NIST AI RMF 1.0, OWASP Top 10 for LLM Applications (2025), MCP Specification, OpenTelemetry GenAI Semantic Conventions
"""

import re
from pathlib import Path

from sources import (
    AWS_FDE_URL as AWS_FDE_PATHWAYS_URL,
    GSDC_CFDE_URL as CERT_OVERVIEW_URL,
    SKILL_SOURCES,
)
from terms import TERMS

COURSE_SLUG = 'Forward-Deployed-Engineer'
EXAM_CODE = 'CFDE / FDE'
EXAM_TITLE = 'Forward Deployed Engineer: Enterprise AI & Agentic Systems Delivery'
CREDENTIAL_TITLE = 'Certified Forward Deployed Engineer (CFDE) & Enterprise FDE Pathways'
STUDY_GUIDE_DATE = 'November 2026 (GSDC CFDE 13-Module Syllabus · AWS Partner FDE Ground/Orchestrate/Prove · Anthropic Frontier Academy)'
PREREQUISITES = (
    'Strong production Python/API fluency + cloud fundamentals '
    '(GSDC CFDE: no formal exam prerequisite; AWS FDE Validated/Advanced: active AWS cert + hands-on pathway validation)'
)

ITEM_TOTAL = 100

TOPICS = {
    1: 'Full-Length Mock Exam 1 — KestrelFreight Global (Supply Chain & Customs)',
    2: 'Full-Length Mock Exam 2 — VeridianCare Health (Regulated Clinical & Claims)',
    3: 'Full-Length Mock Exam 3 — AureliaBank Markets (Financial Services & Credit)',
    4: 'Full-Length Mock Exam 4 — CinderPeak Manufacturing (Semiconductor & ERP Ontology)',
    5: 'Full-Length Mock Exam 5 — SolaraGrid Utilities (Energy Grid & Field Service)',
    6: 'Full-Length Mock Exam 6 — BorealAero Defense & Maintenance (Air-Gapped MRO)',
}

SUBTITLES = {
    1: 'Embedded Discovery, Legacy EDI/AS400 Strangler Integration, Hybrid Customs RAG & FastAPI/Bedrock Delivery',
    2: 'HIPAA/BAA Scoping, HL7 FHIR Anti-Corruption Layers, Principal-Trimmed Clinical RAG & Azure PrivateLink Ops',
    3: 'Model Risk Governance, Core-Banking Idempotent Sagas, Temporal Citation Grounding & On-Prem vLLM Deployment',
    4: 'Shop-Floor Shadowing, SAP/Historian Semantic Ontologies, Orchestrator-Workers & Snowflake/Kubernetes Rollouts',
    5: 'Dispatch ROI Baselines, Kafka Event-Driven Ingestion, OBO-Scoped MCP Field Tools & OpenTelemetry SLO Triage',
    6: 'Air-Gapped Sovereign VPCs, Technical-Manual Multimodal RAG, HITL Safety Gates, Red-Teaming & SRE Handover',
}

DOMAINS = {
    1: 'Client Discovery, Problem Structuring, and Engagement Scoping',
    2: 'Production Software, APIs, and Enterprise System Integration',
    3: 'Enterprise Data Engineering, Ontologies, and Grounded RAG',
    4: 'LLM Workflows, Tool Design, and Agentic Orchestration',
    5: 'Cloud/Hybrid Deployment, CI/CD, Observability, and Reliability',
    6: 'AI Security, Evaluation Harnesses, Governance, and Production Handover',
}

OFFICIAL_RANGES = {
    1: (13, 17),  # 15 per set (15.0%)
    2: (14, 18),  # 16 per set (16.0%)
    3: (16, 20),  # 18 per set (18.0%)
    4: (18, 22),  # 20 per set (20.0%)
    5: (13, 17),  # 15 per set (15.0%)
    6: (14, 18),  # 16 per set (16.0%)
}

PER_SET_ALLOC = {1: 15, 2: 16, 3: 18, 4: 20, 5: 15, 6: 16}
ALLOCATIONS = {n: dict(PER_SET_ALLOC) for n in range(1, 7)}

SKILLS = {
    # Domain 1: Client Discovery, Problem Structuring, and Engagement Scoping (15)
    '1.1': 'Distinguish Forward Deployed Engineering from core SWE, pre-sales Solutions Engineering, and advisory consulting',
    '1.2': 'Conduct frontline operator shadowing and decompose ambiguous customer pain into MECE issue trees and baseline KPIs',
    '1.3': 'Select the right paradigm across deterministic rules, classical ML, RAG, fine-tuning, workflows, and autonomous agents',
    '1.4': 'Define PoC, Pilot, and Production exit criteria, Solution Design Documents (SDDs), and anti-scope-creep boundaries',
    '1.5': 'Build enterprise AI unit-economics, token/infrastructure TCO, and risk-adjusted ROI business cases',
    '1.6': 'Navigate multi-stakeholder alignment across executive sponsors, CISOs, legal/compliance, IT owners, and frontline users',

    # Domain 2: Production Software, APIs, and Enterprise System Integration (16)
    '2.1': 'Write production-grade typed Python/TypeScript services with structured JSON logging, async concurrency, and pytest suites',
    '2.2': 'Design resilient FastAPI/OpenAPI contracts, Pydantic v2 validation, streaming SSE/WebSockets, and rate-limited endpoints',
    '2.3': 'Integrate brownfield enterprise systems (ERP, CRM, EDI, SOAP/mainframe) via Anti-Corruption Layers and Strangler Fig patterns',
    '2.4': 'Implement enterprise authentication, OIDC/SAML federation, OAuth 2.0 On-Behalf-Of (OBO) delegation, and workload identity',
    '2.5': 'Enforce idempotency keys, transactional outboxes, exponential backoff with jitter, circuit breakers, and dead-letter queues',
    '2.6': 'Build outcome-driven rapid prototypes and human-review operator interfaces that bridge seamlessly to production architectures',

    # Domain 3: Enterprise Data Engineering, Ontologies, and Grounded RAG (18)
    '3.1': 'Design incremental CDC/batch/streaming ingestion pipelines with schema evolution, lineage, and quarantine validation',
    '3.2': 'Model enterprise domain ontologies, canonical entity resolution, knowledge graphs, and governed semantic metric layers',
    '3.3': 'Architect layout-aware multimodal document parsing, table/chart preservation, and hierarchical parent-child chunking',
    '3.4': 'Combine dense embeddings, sparse BM25 lexical search, Reciprocal Rank Fusion (RRF), metadata pre-filtering, and cross-encoder reranking',
    '3.5': 'Enforce document-level ACL security trimming, tenant isolation, and point-in-time temporal grounding in retrieval pipelines',
    '3.6': 'Mitigate context poisoning, stale-index drift, lost-in-the-middle degradation, and ungrounded fabrication with citation contracts',
    '3.7': 'Choose between context engineering, RAG, prompt caching, LoRA/PEFT fine-tuning, and calibrated classical ML baselines',

    # Domain 4: LLM Workflows, Tool Design, and Agentic Orchestration (20)
    '4.1': 'Apply prompt engineering, grammar-constrained structured outputs, and model-tier latency/cost routing',
    '4.2': 'Select among canonical workflow and agentic patterns: Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, and Evaluator-Optimizer',
    '4.3': 'Design narrow, deterministic MCP servers and tool schemas with least-privilege OBO scopes and server-side validation',
    '4.4': 'Architect multi-agent handoffs, context isolation, sub-agent budgets, and loop/runaway termination guards',
    '4.5': 'Implement durable stateful execution, checkpointing, event-sourced replay, and compensating saga rollbacks',
    '4.6': 'Design human-in-the-loop (HITL) approval gates, reversible vs irreversible action classification, and confidence escalation',
    '4.7': 'Manage short-term working context, episodic/semantic memory stores, compaction, and cross-session state hygiene',

    # Domain 5: Cloud/Hybrid Deployment, CI/CD, Observability, and Reliability (15)
    '5.1': 'Deploy AI systems across customer VPCs, PrivateLink/Private Service Connect, Kubernetes/vLLM, and air-gapped environments',
    '5.2': 'Automate Terraform/Helm IaC, container hardening, CI/CD eval gates, and Shadow, Canary, and Blue-Green rollouts',
    '5.3': 'Instrument OpenTelemetry GenAI traces, Four Golden Signals, TTFT/TPOT latency breakdowns, and cost-attribution tags',
    '5.4': 'Define SLIs, SLOs, SLAs, error-budget policies, multi-region/provider model fallbacks, and graceful degradation',
    '5.5': 'Triage production tail-latency spikes, HTTP 429 TPM/RPM throttling, memory leaks, and retrieval/model drift incidents',

    # Domain 6: AI Security, Evaluation Harnesses, Governance, and Production Handover (16)
    '6.1': 'Build stratified golden datasets, deterministic code graders, human-calibrated LLM-as-judge rubrics, and CI eval gates',
    '6.2': 'Evaluate RAG Triad metrics (context relevance, faithfulness, answer relevance, Recall@k) and multi-step agent trajectories',
    '6.3': 'Defend against OWASP Top 10 for LLM Applications: indirect prompt injection, insecure output handling, and excessive agency',
    '6.4': 'Operationalize PII redaction, zero-data-retention (ZDR) endpoints, NIST AI RMF 1.0, EU AI Act, and audit-log provenance',
    '6.5': 'Execute production readiness reviews, SRE runbook & game-day handover, ADKAR change enablement, and platform generalization',
    '6.6': 'Deliver executive value proof, live non-brittle stakeholder demos, continuous feedback flywheels, and post-launch governance',
}

SKILL_PLAN = {
    # Domain 1 (15)
    '1.1': 2, '1.2': 2, '1.3': 3, '1.4': 3, '1.5': 2, '1.6': 3,
    # Domain 2 (16)
    '2.1': 2, '2.2': 3, '2.3': 3, '2.4': 3, '2.5': 2, '2.6': 3,
    # Domain 3 (18)
    '3.1': 3, '3.2': 2, '3.3': 2, '3.4': 3, '3.5': 3, '3.6': 3, '3.7': 2,
    # Domain 4 (20)
    '4.1': 3, '4.2': 3, '4.3': 3, '4.4': 3, '4.5': 3, '4.6': 2, '4.7': 3,
    # Domain 5 (15)
    '5.1': 3, '5.2': 3, '5.3': 3, '5.4': 3, '5.5': 3,
    # Domain 6 (16)
    '6.1': 3, '6.2': 3, '6.3': 2, '6.4': 2, '6.5': 3, '6.6': 3,
}

assert len(SKILLS) == 37
assert sum(SKILL_PLAN.values()) == 100
assert set(SKILLS) == set(SKILL_SOURCES)
for _d, _target in PER_SET_ALLOC.items():
    assert sum(v for k, v in SKILL_PLAN.items() if int(k.split('.')[0]) == _d) == _target

VALID_TASKS = set(SKILLS)

TYPE_PLAN = {'multiple-choice': 76, 'ordering': 8, 'multi-select': 16}
KIND_PLAN = {'S': 76, 'O': 8, 'M2': 13, 'M3': 3}
MULTI_PLAN = {1: 2, 2: 3, 3: 3, 4: 3, 5: 2, 6: 3}
COMPLETION_FLOOR = 20
PROPOSED_SOL_FLOOR = 6
SAMPLE_TOTAL = 18  # 3 items (2 MC + 1 MS) per domain across all 6 FDE domains

assert sum(MULTI_PLAN.values()) == 16
assert CERT_OVERVIEW_URL and AWS_FDE_PATHWAYS_URL
assert len(TERMS) >= 110

QUESTIONS_DIR = Path(__file__).resolve().parent / 'questions'
SPLIT_RE = re.compile(r'(?<!\\)\|')


def _load(number: int) -> list[dict]:
    path = QUESTIONS_DIR / f'{number}.txt'
    if not path.is_file():
        return []
    out = []
    for line_no, raw in enumerate(path.read_text(encoding='utf-8').splitlines(), start=1):
        s = raw.strip()
        if not s or s.startswith('#'):
            continue
        parts = [p.replace(r'\|', '|').strip() for p in SPLIT_RE.split(s)]
        if len(parts) != 6:
            raise ValueError(f'{path.name}:{line_no}: expected 6 pipe fields, got {len(parts)}: {raw[:90]}')
        task, kind, ans_raw, dis_raw, question, reason = parts
        if task not in VALID_TASKS:
            raise ValueError(f'{path.name}:{line_no}: unknown skill {task!r}')
        answers = [k.strip() for k in ans_raw.split(',') if k.strip()]
        distractors = [k.strip() for k in dis_raw.split(',') if k.strip()]
        out.append({
            'id': f'E{number}Q{len(out) + 1:03d}',
            'task': task,
            'domain': int(task.split('.')[0]),
            'kind': kind,
            'answers': answers,
            'distractors': distractors,
            'keys': answers + distractors,
            'question': question,
            'reason': reason,
        })
    return out


BANK = {n: _load(n) for n in range(1, 7)}
