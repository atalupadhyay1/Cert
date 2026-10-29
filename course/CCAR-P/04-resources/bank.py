"""Load 378 authored Claude Certified Architect – Professional (CCAR-P) items.

Anthropic's CCAR-P Exam Guide (Version 1.0, Effective July 2026) publishes 63
scored multiple-choice and multiple-response items in 120 minutes across seven
weighted content domains (17 / 13 / 19 / 16 / 14 / 14 / 7 = 100%) and includes
no multi-question case-study split-screen component. Every practice set in this
package matches the live 63-item length with integer domain counts 11 / 8 / 12 /
10 / 9 / 9 / 4 (each within 0.41 items of its exact blueprint share).
"""
from pathlib import Path
from terms import TERMS

HERE = Path(__file__).resolve().parent

DOMAINS = {
    1: 'Solution Design & Architecture',
    2: 'Claude Models, Prompting & Context Engineering',
    3: 'Integration',
    4: 'Evaluation, Testing & Optimization',
    5: 'Governance, Safety & Risk Management',
    6: 'Stakeholder Communication & Lifecycle Management',
    7: 'Developer Productivity & Operational Enablement',
}

DOMAIN_NOTES = {
    1: 'End-to-End Pipelines, Workflows vs. Agents, Multi-Agent Orchestration, Decomposition, and SLAs',
    2: 'Model Trade-Offs, System Prompts, Prompting Strategies, Context Optimization, Caching, and Skills',
    3: 'Least-Privilege Tooling, AuthN/AuthZ Boundaries, RAG Indexing & Retrieval, MCP, and Progressive Discovery',
    4: 'Evaluation Metrics, Mixed-Methodology Datasets, A/B Testing, Root-Cause Diagnosis, and Cost-Latency Tuning',
    5: 'Layered Guardrails, Failure Modes, Human-in-the-Loop Controls, Regulatory Compliance, and Responsible AI',
    6: 'Structured Discovery, Trade-Off Communication, SLA Alignment, Architecture Handoff, and Lifecycle Governance',
    7: 'Claude Code Team Configuration, AI-Assisted Engineering Workflows, and Operational Debugging',
}

TOPICS = {
    1: 'Full-Length Mock Exam 1',
    2: 'Full-Length Mock Exam 2',
    3: 'Full-Length Mock Exam 3',
    4: 'Full-Length Mock Exam 4',
    5: 'Full-Length Mock Exam 5',
    6: 'Full-Length Mock Exam 6',
}

SUBTITLES = {
    1: 'Regulated Financial Services, Wealth Advisory, and Credit Operations',
    2: 'Healthcare Clinical Operations, Payer Claims, and Life Sciences',
    3: 'Global E-Commerce, Retail Supply Chain, and Omnichannel Customer Care',
    4: 'B2B SaaS Platform, Cloud Infrastructure, and Site Reliability Operations',
    5: 'Legal Tech, M&A Due Diligence, Insurance Underwriting, and Contract Lifecycle',
    6: 'Public Sector, Utilities Grid Operations, Manufacturing Quality, and Telecom',
}

# Local study-map IDs mapped 1-to-1 to the 38 objectives in Section 6 of the CCAR-P Exam Guide v1.0.
SKILLS = {
    '1.1': 'Translate Business Problems into Technical Claude-Based Solutions',
    '1.2': 'Design End-to-End Architectures Across Pre-Processing, Model Stage, Post-Processing, and Feedback Loops',
    '1.3': 'Select Appropriate Architectural Patterns: Workflows vs. Agentic Systems vs. Augmented LLMs',
    '1.4': 'Design Multi-Agent Systems, Subagent Context Isolation, and Orchestration Patterns',
    '1.5': 'Apply Task Decomposition Techniques to Complex Multi-Step Workflows',
    '1.6': 'Align Solutions to Business Value Pillars (Efficiency, Innovation, Risk Reduction) and SLAs',
    '2.1': 'Select Claude Models Across Capability, Cost, Latency, and Complexity Trade-Offs',
    '2.2': 'Design System Prompts, Structured Templates, and Behavioral Guardrails',
    '2.3': 'Apply Zero-Shot, Few-Shot, Chain-of-Thought, and Extended Thinking Strategies',
    '2.4': 'Optimize Context Windows and Token Usage via Compaction, Editing, and Just-in-Time Retrieval',
    '2.5': 'Implement Prompt Reuse and Modularity with Prompt Caching, Modular Prompts, and Skills',
    '3.1': 'Evaluate Capability Bloat and Enforce Least Privilege in Tool and Agent Design',
    '3.2': 'Identify Authentication, Authorization, and Network Boundary Gaps Across Integrated Systems',
    '3.3': 'Balance Accuracy vs. Latency in Synchronous and Asynchronous Integration Workflows',
    '3.4': 'Design Production-Scale Observability, Distributed Tracing, and Telemetry Pipelines',
    '3.5': 'Select Chunking, Contextual Enrichment, and Indexing Strategies for RAG Pipelines',
    '3.6': 'Match Dense, Lexical, Hybrid, Reranked, and Structured Retrieval to Data and Query Shapes',
    '3.7': 'Evaluate MCP vs. Direct REST/CLI vs. Agent-to-Agent Protocols and Integration Boundaries',
    '3.8': 'Evaluate Progressive Tool and Skill Discovery (defer_loading / Tool Search) vs. Monolithic Context',
    '4.1': 'Define Multi-Dimensional Evaluation Metrics Across Accuracy, Latency, Cost, Safety, and Security',
    '4.2': 'Design Golden Datasets and Mixed-Methodology Evaluation Frameworks (Code Graders, LLM Rubrics, Human Calibration)',
    '4.3': 'Conduct Controlled A/B Testing, Shadow Traffic Trials, and Iterative Releases',
    '4.4': 'Diagnose Prompt Failures, Retrieval Drift, Hallucinations, Context Pollution, and Model Mismatch',
    '4.5': 'Optimize Token Consumption, Time-to-First-Token, Batch Throughput, and Cost-Performance Trade-Offs',
    '4.6': 'Monitor Production Drift, Cache Efficiency, Refusal Spikes, and Quality Regressions',
    '5.1': 'Implement Layered Input, Tool-Execution, and Output Guardrails and Safety Classifiers',
    '5.2': 'Identify Prompt Injection, Confused-Deputy, Over-Reliance, and Compounding Agent Failure Modes',
    '5.3': 'Design Risk-Tiered Human-in-the-Loop Escalation, Approval Gates, and Calibration Workflows',
    '5.4': 'Satisfy GDPR, HIPAA, FedRAMP, Data Residency, and Zero-Data-Retention Compliance Controls',
    '5.5': 'Address Bias Auditing, Fairness Across Cohorts, Citation Grounding, and AI Transparency',
    '6.1': 'Conduct Structured Discovery, Data Readiness Audits, and Constraint Gathering',
    '6.2': 'Communicate Architectural Trade-Offs to Executive, Security, Legal, and Engineering Stakeholders',
    '6.3': 'Manage Stakeholder Feedback Loops and Segment-Specific Accuracy/Latency Expectation Alignment (SLAs)',
    '6.4': 'Author Architecture Decision Records, Runbooks, Interface Contracts, and Implementation Guidance',
    '6.5': 'Govern Lifecycle Phases Across Discovery, Pilot Gateways, Production Handoff, Monitoring, and Deprecation',
    '7.1': 'Configure Claude Code, CLAUDE.md Hierarchies, Permissions, Hooks, and MCP Scopes for Teams',
    '7.2': 'Accelerate Software Delivery Workflows with Skills, Subagents, Plan Mode, and Headless CI Automation',
    '7.3': 'Support Operational Incident Debugging, Root-Cause Triage, and Safe Remediation Workflows',
}
VALID_TASKS = set(SKILLS)

# Official blueprint weights in Section 6 of the CCAR-P Exam Guide v1.0 (sum = 100.0%).
OFFICIAL_WEIGHTS = {1: 17.0, 2: 13.0, 3: 19.0, 4: 16.0, 5: 14.0, 6: 14.0, 7: 7.0}

# Exact 63-item mock allocation: 0.17*63=10.71->11, 0.13*63=8.19->8, 0.19*63=11.97->12,
# 0.16*63=10.08->10, 0.14*63=8.82->9, 0.14*63=8.82->9, 0.07*63=4.41->4 (sum = 63).
ALLOCATIONS = {
    n: {1: 11, 2: 8, 3: 12, 4: 10, 5: 9, 6: 9, 7: 4}
    for n in range(1, 7)
}

SKILL_PLAN = {
    '1.1': 2, '1.2': 2, '1.3': 2, '1.4': 2, '1.5': 2, '1.6': 1,
    '2.1': 2, '2.2': 2, '2.3': 1, '2.4': 1, '2.5': 2,
    '3.1': 2, '3.2': 2, '3.3': 1, '3.4': 1, '3.5': 1, '3.6': 1, '3.7': 2, '3.8': 2,
    '4.1': 2, '4.2': 2, '4.3': 1, '4.4': 2, '4.5': 2, '4.6': 1,
    '5.1': 2, '5.2': 2, '5.3': 2, '5.4': 2, '5.5': 1,
    '6.1': 2, '6.2': 2, '6.3': 2, '6.4': 1, '6.5': 2,
    '7.1': 2, '7.2': 1, '7.3': 1,
}

# Multi-select items per official domain: 3 + 2 + 3 + 2 + 2 + 2 + 1 = 15 (12 M2 + 3 M3).
MULTI_PLAN = {1: 3, 2: 2, 3: 3, 4: 2, 5: 2, 6: 2, 7: 1}
KIND_PLAN = {'S': 48, 'M2': 12, 'M3': 3}
TYPE_PLAN = {'multiple-choice': 48, 'multi-select': 15}
ITEM_TOTAL = sum(TYPE_PLAN.values())

# Minimum count per exam of matrix/categorization-adapted items (use-case suitability,
# sound architectural practice evaluation, and Pre-Processing / Model Stage / Post-Processing mapping).
PATTERN_MATRIX_FLOOR = 8


def is_matrix_adapted_stem(question):
    q = question.casefold()
    return (
        ('pre-processing' in q and 'model stage' in q and 'post-processing' in q)
        or 'candidate use cases' in q
        or 'candidate workflows' in q
        or 'sound architectural practice' in q
        or 'execution layer' in q
    )


BANK = {}
for number in TOPICS:
    records = []
    path = HERE / 'questions' / f'{number}.txt'
    if path.is_file():
        for line_number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if not line.strip() or line.startswith('#'):
                continue
            parts = [x.strip() for x in line.split('|')]
            if len(parts) != 6:
                raise ValueError(f'{path.name}:{line_number}: expected 6 fields, got {len(parts)}')
            skill, kind, answers, distractors, question, reason = parts
            answer_keys = [x.strip() for x in answers.split(',') if x.strip()]
            distractor_keys = [x.strip() for x in distractors.split(',') if x.strip()]
            records.append(dict(
                id=f'T{number}-Q{len(records) + 1:03}',
                task=skill,
                domain=int(skill.split('.')[0]),
                kind=kind,
                answers=answer_keys,
                distractors=distractor_keys,
                keys=answer_keys + distractor_keys,
                question=question,
                reason=reason,
                line=line_number,
            ))
    BANK[number] = records
