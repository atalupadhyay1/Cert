"""Question bank loader and blueprint constants for MCP (6 x 100 = 600 questions).

Synthesizes the 2026 Model Context Protocol open-standard ecosystem:
- MCP Specification 2025-11-25 (and 2025-06-18, 2025-03-26 evolution)
- Linux Foundation AAIF (MCP + Registry, Inspector, SDKs)
- OAuth 2.1 + RFC 7591/8707/9207/9728, PKCE, CIMD
- OWASP MCP Security Checklist & A2A interoperability
"""

import re
from pathlib import Path

from sources import (
    AAIF_URL,
    MCP_GITHUB_URL,
    MCP_INTRO_URL as CERT_OVERVIEW_URL,
    MCP_SPEC_URL,
    OWASP_MCP_URL as OWASP_ASI_URL,
    SKILL_SOURCES,
)
from terms import TERMS

COURSE_SLUG = 'MCP'
EXAM_CODE = 'MCP'
EXAM_TITLE = 'Model Context Protocol: Servers, Clients, Transports & Security'
CREDENTIAL_TITLE = 'Model Context Protocol (MCP 2025-11-25) — Tool & Context Standard'
STUDY_GUIDE_DATE = (
    'November 2026 (MCP Specification 2025-11-25 · MCP Registry & Inspector · '
    'OAuth 2.1 + RFC 8707/9207 + CIMD · OWASP MCP Security Checklist)'
)
PREREQUISITES = (
    'TypeScript/Python fluency, JSON-RPC & HTTP fundamentals, OAuth 2 basics, '
    'and familiarity with LLM tool-use or VS Code / Claude Desktop extensibility'
)

ITEM_TOTAL = 100

TOPICS = {
    1: 'Full-Length Mock Exam 1 — Meridian Capital Trading Desk (Finance & Risk)',
    2: 'Full-Length Mock Exam 2 — HelixMed Clinical Research Hub (Healthcare & Trials)',
    3: 'Full-Length Mock Exam 3 — AtlasCloud Platform Ops (Cloud Infra & DevTools)',
    4: 'Full-Length Mock Exam 4 — Veridian Legal Vault (Legal & Compliance Docs)',
    5: 'Full-Length Mock Exam 5 — OmniCart Commerce Ops (Retail & Supply Chain)',
    6: 'Full-Length Mock Exam 6 — Sentinel Cyber Fusion (Security & SOC Automation)',
}

SUBTITLES = {
    1: 'Host-Client-Server Triad, SDK Scaffolds, Tool Poisoning Defense & Registry Trust',
    2: 'Initialization Handshake, Resource Templates, Streamable HTTP Sessions & Elicitation',
    3: 'JSON-RPC Framing, Tools vs Resources, OAuth 2.1 PKCE & Inspector CI Gates',
    4: 'Capabilities Negotiation, Completions API, Logging Levels & Audit Provenance',
    5: 'Progress & Cancellation, Sampling Delegation, Roots Boundaries & Env Isolation',
    6: 'SSE Deprecation → Streamable HTTP, Batching, Reconnect Resumability & Gateway Mesh',
}

DOMAINS = {
    1: 'MCP Foundations, Architecture & Lifecycle',
    2: 'Tools, Resources & Resource Templates',
    3: 'Prompts, Sampling, Roots & Elicitation',
    4: 'Transports, Sessions & Protocol Evolution',
    5: 'Authorization, Security, Trust & Registry',
    6: 'SDKs, Deployment, Observability & Ecosystem',
}

OFFICIAL_RANGES = {
    1: (16, 20),  # 18 per set
    2: (18, 22),  # 20 per set
    3: (14, 18),  # 16 per set
    4: (14, 18),  # 16 per set
    5: (13, 17),  # 15 per set
    6: (13, 17),  # 15 per set
}

PER_SET_ALLOC = {1: 18, 2: 20, 3: 16, 4: 16, 5: 15, 6: 15}
ALLOCATIONS = {n: dict(PER_SET_ALLOC) for n in range(1, 7)}

SKILLS = {
    # Domain 1: Foundations, Architecture & Lifecycle (18)
    '1.1': 'Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model',
    '1.2': 'Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake',
    '1.3': 'Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy',
    '1.4': 'Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging)',
    '1.5': 'Manage keepalive pings, progress notifications, cancellation, and shutdown semantics',
    '1.6': 'Differentiate MCP from function calling, A2A, and experimental capability progression',

    # Domain 2: Tools, Resources & Resource Templates (20)
    '2.1': 'Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints',
    '2.2': 'Control model-controlled tool execution, list discovery, validation, and structured content output',
    '2.3': 'Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed',
    '2.4': 'Address direct resources vs templated resources with URI schemes, names, and mimeTypes',
    '2.5': 'Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows',
    '2.6': 'Declare prompts and completions for argument typeahead and parameterized prompt expansion',

    # Domain 3: Prompts, Sampling, Roots & Elicitation (16)
    '3.1': 'Expose and expand prompts via prompts/list, prompts/get, and argument validation',
    '3.2': 'Enforce client-owned filesystem boundaries via roots/list and roots/list_changed',
    '3.3': 'Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls',
    '3.4': 'Collect human input via elicitation/create with requestedSchema and form round-trips',
    '3.5': 'Regulate verbosity via logging/setLevel and notifications/message level filtering',
    '3.6': 'Correlate progress and completion flows with progressToken and completion/complete semantics',

    # Domain 4: Transports, Sessions & Protocol Evolution (16)
    '4.1': 'Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle',
    '4.2': 'Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response)',
    '4.3': 'Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay',
    '4.4': 'Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP',
    '4.5': 'Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation',
    '4.6': 'Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival',

    # Domain 5: Authorization, Security, Trust & Registry (15)
    '5.1': 'Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata',
    '5.2': 'Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings',
    '5.3': 'Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality',
    '5.4': 'Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model',
    '5.5': 'Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging',

    # Domain 6: SDKs, Deployment, Observability & Ecosystem (15)
    '6.1': 'Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic)',
    '6.2': 'Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates',
    '6.3': 'Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation',
    '6.4': 'Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation',
    '6.5': 'Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns',
}

SKILL_PLAN = {
    # Domain 1 (18)
    '1.1': 3, '1.2': 3, '1.3': 3, '1.4': 3, '1.5': 3, '1.6': 3,
    # Domain 2 (20)
    '2.1': 4, '2.2': 4, '2.3': 3, '2.4': 3, '2.5': 3, '2.6': 3,
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
SAMPLE_TOTAL = 18  # 3 items (2 MC + 1 MS) per domain across all 6 domains

assert sum(MULTI_PLAN.values()) == 16
assert CERT_OVERVIEW_URL and AAIF_URL and MCP_SPEC_URL and OWASP_ASI_URL
assert len(TERMS) >= 100

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
