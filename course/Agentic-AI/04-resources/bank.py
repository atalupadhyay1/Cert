"""Question bank loader and blueprint constants for Agentic AI (6 x 100 = 600 questions).

Synthesizes the 2026 Agentic AI certification & open-standard ecosystem:
- NVIDIA-Certified Professional: Agentic AI (NCP-AAI: 60-70 Qs, 120 min, $200, 10 official domains, 2-year validity)
- Linux Foundation Agentic AI Foundation (AAIF: MCP 2026-07-28, A2A v1.0, AGENTS.md, Agent Skills, OpenSandbox, OpenEnv, agentgateway)
- OWASP Top 10 for Agentic Applications (ASI01:2026 - ASI10:2026) & GitHub Certified: Agentic AI Developer (GH-600)
- Production Orchestration & Observability: LangGraph 1.x, AutoGen/AG2, CrewAI, NVIDIA NIM/NeMo, OpenTelemetry GenAI Agent Spans
"""

import re
from pathlib import Path

from sources import (
    AAIF_URL,
    MCP_SPEC_URL,
    NCP_AAI_URL as CERT_OVERVIEW_URL,
    OWASP_ASI_URL,
    SKILL_SOURCES,
)
from terms import TERMS

COURSE_SLUG = 'Agentic-AI'
EXAM_CODE = 'NCP-AAI / AAIF'
EXAM_TITLE = 'Agentic AI: Autonomous Multi-Agent Systems, MCP, A2A & Security'
CREDENTIAL_TITLE = 'NVIDIA-Certified Professional: Agentic AI (NCP-AAI) & Open Agentic AI Standards'
STUDY_GUIDE_DATE = (
    'November 2026 (NVIDIA NCP-AAI 10-Domain Blueprint · Linux Foundation AAIF MCP 2026-07-28 & A2A v1.0 · '
    'OWASP Top 10 for Agentic Applications ASI01–ASI10)'
)
PREREQUISITES = (
    'Production Python/TypeScript fluency, LLM/RAG fundamentals, and distributed API experience '
    '(NCP-AAI recommends 1–2 years of AI/ML & production agentic engineering experience)'
)

ITEM_TOTAL = 100

TOPICS = {
    1: 'Full-Length Mock Exam 1 — QuantaPay Autonomous Disputes (Fintech & Card Networks)',
    2: 'Full-Length Mock Exam 2 — HelixVax Discovery Labs (Biopharma & Clinical Literature)',
    3: 'Full-Length Mock Exam 3 — CloudPulse Autonomous SRE (Cloud Infrastructure & Incident Ops)',
    4: 'Full-Length Mock Exam 4 — StrataLaw Contract Intelligence (Legal M&A & Regulatory Audit)',
    5: 'Full-Length Mock Exam 5 — VeloceCart Commerce Concierge (Global Retail & Supply Chain)',
    6: 'Full-Length Mock Exam 6 — AegisCyber SOC Copilot (Autonomous Threat Hunting & SOAR)',
}

SUBTITLES = {
    1: 'ReAct vs Plan-and-Execute, MCP 2026-07-28 OAuth 2.1, LangGraph interrupt() Sagas & OWASP ASI01/ASI09 Controls',
    2: 'Hierarchical Supervisor + A2A v1.0 Cards, Corrective GraphRAG, Pass^k Trajectory Evals & ZDR/HIPAA Guardrails',
    3: 'Swarm vs DAG Topologies, OpenSandbox MicroVMs, NVIDIA NIM / vLLM Prefix Caching, KEDA & OTel GenAI Spans',
    4: 'Evaluator-Optimizer Loops, Bitemporal ACL-Trimmed RAG, Calibrated LLM-as-Judge, EU AI Act & WORM Provenance',
    5: 'Adaptive Routing, Parallel Idempotent Tools, 4-Tier Episodic/Semantic Memory, SFT/DPO/RFT & Pareto Routing',
    6: 'AGENTS.md & Agent Skills, MCP Rug-Pull Pinning, Speculative Decoding, Circuit Breakers & Kill-Switch Containment',
}

DOMAINS = {
    1: 'Agentic Architectures, Reasoning Loops, and Multi-Agent Topologies',
    2: 'Agent Development, Tool Contracts, MCP, and Durable State Graphs',
    3: 'Memory Systems, Context Engineering, and Agentic RAG',
    4: 'Agent Evaluation, Trajectory Grading, and Model Optimization',
    5: 'Inference Acceleration, Scaling, and Agent Observability',
    6: 'Agentic Security, Guardrails, Governance, and Human Oversight',
}

OFFICIAL_RANGES = {
    1: (16, 20),  # 18 per set (18.0%)
    2: (18, 22),  # 20 per set (20.0%)
    3: (14, 18),  # 16 per set (16.0%)
    4: (14, 18),  # 16 per set (16.0%)
    5: (13, 17),  # 15 per set (15.0%)
    6: (13, 17),  # 15 per set (15.0%)
}

PER_SET_ALLOC = {1: 18, 2: 20, 3: 16, 4: 16, 5: 15, 6: 15}
ALLOCATIONS = {n: dict(PER_SET_ALLOC) for n in range(1, 7)}

SKILLS = {
    # Domain 1: Agentic Architectures, Reasoning Loops, and Multi-Agent Topologies (18)
    '1.1': 'Distinguish deterministic workflows (Prompt Chaining, Routing, Parallelization) from autonomous agents (Orchestrator-Workers, Evaluator-Optimizer)',
    '1.2': 'Select reasoning and planning loops: ReAct, Plan-and-Execute, Reflexion, and Tree-of-Thoughts under latency/budget constraints',
    '1.3': 'Design task decomposition, dynamic replanning, and bounded iterative self-correction loops',
    '1.4': 'Architect multi-agent topologies: Hierarchical Supervisor, Swarm Handoff, DAG Pipelines, and Shared Blackboard',
    '1.5': 'Implement horizontal agent-to-agent interoperability with A2A v1.0 signed Agent Cards, Task lifecycles, SSE, and webhooks',
    '1.6': 'Standardize agent context with AGENTS.md, progressive Agent Skills, max-step loop guards, and token/cost budgets',

    # Domain 2: Agent Development, Tool Contracts, MCP, and Durable State Graphs (20)
    '2.1': 'Design ergonomic, token-efficient tool contracts, grammar-constrained JSON schemas, and parallel/idempotent tool execution',
    '2.2': 'Architect Model Context Protocol (MCP 2026-07-28) servers: Tools, Resources, Prompts, Streamable HTTP, and OAuth 2.1 + CIMD',
    '2.3': 'Build durable cyclic state graphs in LangGraph 1.x with typed reducers, Send() map-reduce, checkpointers, and interrupt()/Command(resume=...)',
    '2.4': 'Select orchestration patterns across LangGraph, AutoGen/AG2, CrewAI Flows, and NVIDIA NeMo Agent Toolkit',
    '2.5': 'Isolate dynamic code, shell, and browser execution inside ephemeral microVM sandboxes (OpenSandbox, Firecracker, gVisor)',
    '2.6': 'Coordinate multi-system agent mutations with durable sagas, transactional outboxes, idempotency ledgers, and dead-letter queues',

    # Domain 3: Memory Systems, Context Engineering, and Agentic RAG (16)
    '3.1': 'Model cognitive memory tiers: working context, episodic trajectories, semantic facts, and procedural playbooks',
    '3.2': 'Engineer context compaction, addressable artifact offloading, structured state summaries, and lost-in-the-middle mitigation',
    '3.3': 'Implement Adaptive RAG, Corrective RAG (CRAG), Self-RAG relevance/support grading, and query decomposition',
    '3.4': 'Combine hybrid BM25 + dense vector search, cross-encoder reranking (NeMo Retriever), and GraphRAG community synthesis',
    '3.5': 'Parse complex tables, diagrams, and multimodal technical specs with hierarchical parent-child chunking',
    '3.6': 'Enforce pre-retrieval OBO ACL trimming, bitemporal validity, verified span citations, PII scrubbing, and memory TTL governance',

    # Domain 4: Agent Evaluation, Trajectory Grading, and Model Optimization (16)
    '4.1': 'Build deterministic offline agent evaluation harnesses and mock tool environments (OpenEnv) for multi-step benchmarking',
    '4.2': 'Measure trajectory tool precision, state-outcome assertions, and Pass^k multi-trial consistency vs Pass@k exploration',
    '4.3': 'Calibrate LLM-as-judge rubrics (Cohen’s kappa, position/verbosity debiasing) alongside RAG Triad metrics',
    '4.4': 'Apply the optimization ladder: prompt/DSPy tuning, teacher-student LoRA/SFT distillation, DPO alignment, and verifiable-reward RFT',
    '4.5': 'Gate CI/CD changes on stratified regression and OWASP ASI adversarial slices before shadow and online A/B rollouts',
    '4.6': 'Operate production trace-to-golden-dataset flywheels and 3D Pareto model routing (Pass^k quality × P95 latency × USD/task)',

    # Domain 5: Inference Acceleration, Scaling, and Agent Observability (15)
    '5.1': 'Accelerate agent serving on NVIDIA NIM, TensorRT-LLM, Triton, and vLLM with continuous batching, PagedAttention, and FP8/INT4 quantization',
    '5.2': 'Maximize KV prefix-cache hit rates, disaggregated prefill/decode throughput, and lossless speculative decoding for tool calls',
    '5.3': 'Autoscale GPU agent fleets via KEDA on KV-cache occupancy and queue depth with progressive Shadow/Canary rollouts and AI gateways',
    '5.4': 'Instrument OpenTelemetry GenAI Agent spans (gen_ai.agent.*, checkpoint/pause IDs, TTFT/TPOT, MCP latency, and FinOps tags)',
    '5.5': 'Mitigate HTTP 429 TPM/RPM saturation, cascading retry storms, tool-schema failover mismatches, and runaway fleet loops',

    # Domain 6: Agentic Security, Guardrails, Governance, and Human Oversight (15)
    '6.1': 'Defend against OWASP ASI01 Agent Goal Hijack, ASI02 Tool Misuse, and ASI05 RCE using taint tracking and NeMo Guardrails',
    '6.2': 'Enforce Non-Human Identity (NHI), OAuth 2.0 On-Behalf-Of (OBO) delegation, and Policy-as-Code against ASI03 Privilege Abuse',
    '6.3': 'Secure MCP supply chains (ASI04 rug-pull hash pinning, AIBOM) and inter-agent A2A channels (ASI07 mTLS + JWS + replay nonces)',
    '6.4': 'Prevent ASI06 Memory Poisoning, ASI08 Cascading Failures, and ASI10 Rogue Agents with circuit breakers and out-of-band kill-switches',
    '6.5': 'Design calibrated HITL parameter-diff approvals (countering ASI09), NIST AI RMF, EU AI Act oversight, ZDR, and WORM audit trails',
}

SKILL_PLAN = {
    # Domain 1 (18)
    '1.1': 3, '1.2': 3, '1.3': 3, '1.4': 3, '1.5': 3, '1.6': 3,
    # Domain 2 (20)
    '2.1': 3, '2.2': 4, '2.3': 4, '2.4': 3, '2.5': 3, '2.6': 3,
    # Domain 3 (16)
    '3.1': 3, '3.2': 3, '3.3': 3, '3.4': 3, '3.5': 2, '3.6': 2,
    # Domain 4 (16)
    '4.1': 3, '4.2': 3, '4.3': 3, '4.4': 3, '4.5': 2, '4.6': 2,
    # Domain 5 (15)
    '5.1': 3, '5.2': 3, '5.3': 3, '5.4': 3, '5.5': 3,
    # Domain 6 (15)
    '6.1': 3, '6.2': 3, '6.3': 3, '6.4': 3, '6.5': 3,
}

assert len(SKILLS) == 34
assert sum(SKILL_PLAN.values()) == 100
assert set(SKILLS) == set(SKILL_SOURCES)
for _d, _target in PER_SET_ALLOC.items():
    assert sum(v for k, v in SKILL_PLAN.items() if int(k.split('.')[0]) == _d) == _target

VALID_TASKS = set(SKILLS)

TYPE_PLAN = {'multiple-choice': 76, 'ordering': 8, 'multi-select': 16}
KIND_PLAN = {'S': 76, 'O': 8, 'M2': 13, 'M3': 3}
MULTI_PLAN = {1: 3, 2: 3, 3: 3, 4: 2, 5: 2, 6: 3}
COMPLETION_FLOOR = 20
PROPOSED_SOL_FLOOR = 6
SAMPLE_TOTAL = 18  # 3 items (2 MC + 1 MS) per domain across all 6 Agentic AI domains

assert sum(MULTI_PLAN.values()) == 16
assert CERT_OVERVIEW_URL and AAIF_URL and MCP_SPEC_URL and OWASP_ASI_URL
assert len(TERMS) >= 130

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
