"""Authoritative primary sources for Agentic AI (NCP-AAI / AAIF MCP & A2A / OWASP ASI) 6x100 course."""

NVIDIA_NCP_AAI_URL = 'https://www.nvidia.com/en-us/learn/certification/agentic-ai-professional/'
NCP_AAI_URL = NVIDIA_NCP_AAI_URL
ANTHROPIC_AGENTS_URL = 'https://www.anthropic.com/research/building-effective-agents'
MCP_SPEC_URL = 'https://modelcontextprotocol.io/introduction'
A2A_SPEC_URL = 'https://a2a-protocol.org/latest/'
OWASP_ASI_URL = 'https://genai.owasp.org/'
LF_AAIF_URL = 'https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation'
AAIF_URL = LF_AAIF_URL

SKILL_SOURCES = {
    # Domain 1 — Agentic Architectures, Reasoning Loops, and Multi-Agent Topologies (18%)
    '1.1': (ANTHROPIC_AGENTS_URL, NVIDIA_NCP_AAI_URL),
    '1.2': ('https://arxiv.org/abs/2210.03629', ANTHROPIC_AGENTS_URL),
    '1.3': (ANTHROPIC_AGENTS_URL, 'https://arxiv.org/abs/2303.11366'),
    '1.4': ('https://langchain-ai.github.io/langgraph/concepts/multi_agent/', NVIDIA_NCP_AAI_URL),
    '1.5': (A2A_SPEC_URL, LF_AAIF_URL),
    '1.6': ('https://agents.md/', LF_AAIF_URL),

    # Domain 2 — Agent Development, Tool Contracts, MCP, and Durable State Graphs (20%)
    '2.1': ('https://docs.pydantic.dev/latest/', 'https://spec.openapis.org/oas/latest.html'),
    '2.2': (MCP_SPEC_URL, 'https://datatracker.ietf.org/doc/html/rfc9207'),
    '2.3': (
        'https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/',
        'https://langchain-ai.github.io/langgraph/concepts/persistence/',
    ),
    '2.4': ('https://microsoft.github.io/autogen/stable/', 'https://docs.crewai.com/'),
    '2.5': (LF_AAIF_URL, 'https://gvisor.dev/docs/'),
    '2.6': ('https://docs.temporal.io/workflows', 'https://microservices.io/patterns/data/transactional-outbox.html'),

    # Domain 3 — Memory Systems, Context Engineering, and Agentic RAG (16%)
    '3.1': ('https://langchain-ai.github.io/langgraph/concepts/memory/', NVIDIA_NCP_AAI_URL),
    '3.2': ('https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents', ANTHROPIC_AGENTS_URL),
    '3.3': ('https://arxiv.org/abs/2401.15884', ANTHROPIC_AGENTS_URL),
    '3.4': ('https://docs.nvidia.com/nemo/retriever/latest/index.html', 'https://microsoft.github.io/graphrag/'),
    '3.5': ('https://docs.nvidia.com/nemo/retriever/latest/index.html', MCP_SPEC_URL),
    '3.6': (OWASP_ASI_URL, 'https://microsoft.github.io/presidio/'),

    # Domain 4 — Agent Evaluation, Trajectory Grading, and Model Optimization (16%)
    '4.1': (LF_AAIF_URL, NVIDIA_NCP_AAI_URL),
    '4.2': ('https://arxiv.org/abs/2406.12045', ANTHROPIC_AGENTS_URL),
    '4.3': ('https://arxiv.org/abs/2306.05685', 'https://docs.ragas.io/'),
    '4.4': ('https://docs.nvidia.com/nemo/customizer/latest/index.html', 'https://dspy.ai/'),
    '4.5': (OWASP_ASI_URL, NVIDIA_NCP_AAI_URL),
    '4.6': ('https://microsoft.github.io/presidio/', 'https://opentelemetry.io/docs/specs/semconv/gen-ai/'),

    # Domain 5 — Inference Acceleration, Scaling, and Agent Observability (15%)
    '5.1': ('https://docs.nvidia.com/nim/large-language-models/latest/introduction.html', 'https://docs.vllm.ai/en/latest/'),
    '5.2': ('https://nvidia.github.io/TensorRT-LLM/', 'https://docs.vllm.ai/en/latest/features/spec_decode.html'),
    '5.3': ('https://keda.sh/docs/latest/', 'https://istio.io/latest/docs/tasks/traffic-management/mirroring/'),
    '5.4': ('https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/', 'https://opentelemetry.io/docs/specs/semconv/gen-ai/'),
    '5.5': ('https://sre.google/sre-book/service-level-objectives/', NVIDIA_NCP_AAI_URL),

    # Domain 6 — Agentic Security, Guardrails, Governance, and Human Oversight (15%)
    '6.1': (OWASP_ASI_URL, 'https://docs.nvidia.com/nemo/guardrails/latest/index.html'),
    '6.2': ('https://datatracker.ietf.org/doc/html/rfc8693', OWASP_ASI_URL),
    '6.3': (MCP_SPEC_URL, A2A_SPEC_URL),
    '6.4': (OWASP_ASI_URL, ANTHROPIC_AGENTS_URL),
    '6.5': ('https://www.nist.gov/itl/ai-risk-management-framework', 'https://artificialintelligenceact.eu/'),
}
