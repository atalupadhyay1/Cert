"""Authoritative primary sources for Model Context Protocol (MCP) 6x100 course."""

MCP_SPEC_URL = 'https://modelcontextprotocol.io/specification/2025-11-25'
MCP_INTRO_URL = 'https://modelcontextprotocol.io/introduction'
MCP_GITHUB_URL = 'https://github.com/modelcontextprotocol/specification'
MCP_REGISTRY_URL = 'https://github.com/modelcontextprotocol/registry'
ANTHROPIC_MCP_URL = 'https://www.anthropic.com/news/model-context-protocol'
LF_AAIF_URL = 'https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation'
AAIF_URL = LF_AAIF_URL
OWASP_MCP_URL = 'https://genai.owasp.org/resource/mcp-security-checklist/'

SKILL_SOURCES = {
    # Domain 1 — MCP Foundations, Architecture & Lifecycle (18%)
    '1.1': (MCP_INTRO_URL, 'https://modelcontextprotocol.io/docs/concepts/architecture'),
    '1.2': (MCP_SPEC_URL, 'https://spec.modelcontextprotocol.io/specification/basic/lifecycle/'),
    '1.3': (MCP_SPEC_URL, 'https://spec.modelcontextprotocol.io/specification/basic/transports/'),
    '1.4': (MCP_GITHUB_URL, 'https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle'),
    '1.5': ('https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/', MCP_SPEC_URL),
    '1.6': ('https://modelcontextprotocol.io/docs/concepts/architecture', 'https://a2a-protocol.org/latest/'),

    # Domain 2 — Tools, Resources & Resource Templates (20%)
    '2.1': ('https://spec.modelcontextprotocol.io/specification/server/tools/', MCP_SPEC_URL),
    '2.2': (MCP_SPEC_URL, 'https://modelcontextprotocol.io/docs/concepts/tools'),
    '2.3': (MCP_SPEC_URL, 'https://modelcontextprotocol.io/docs/concepts/resources'),
    '2.4': ('https://spec.modelcontextprotocol.io/specification/server/resources/', MCP_SPEC_URL),
    '2.5': ('https://spec.modelcontextprotocol.io/specification/server/resources/', 'https://modelcontextprotocol.io/docs/concepts/resources'),
    '2.6': ('https://spec.modelcontextprotocol.io/specification/server/utilities/completion/', MCP_SPEC_URL),

    # Domain 3 — Prompts, Sampling, Roots & Elicitation (16%)
    '3.1': ('https://spec.modelcontextprotocol.io/specification/server/prompts/', MCP_SPEC_URL),
    '3.2': ('https://spec.modelcontextprotocol.io/specification/client/roots/', MCP_SPEC_URL),
    '3.3': ('https://spec.modelcontextprotocol.io/specification/client/sampling/', MCP_SPEC_URL),
    '3.4': ('https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation', MCP_SPEC_URL),
    '3.5': ('https://spec.modelcontextprotocol.io/specification/server/utilities/logging/', MCP_SPEC_URL),
    '3.6': (MCP_SPEC_URL, 'https://modelcontextprotocol.io/docs/concepts/prompts'),

    # Domain 4 — Transports, Sessions & Protocol Evolution (16%)
    '4.1': ('https://spec.modelcontextprotocol.io/specification/basic/transports/', MCP_GITHUB_URL),
    '4.2': ('https://modelcontextprotocol.io/docs/concepts/transports', MCP_SPEC_URL),
    '4.3': ('https://spec.modelcontextprotocol.io/specification/basic/transports/', 'https://modelcontextprotocol.io/specification/2025-11-25/basic/transports'),
    '4.4': (MCP_GITHUB_URL, 'https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/'),
    '4.5': ('https://spec.modelcontextprotocol.io/specification/basic/utilities/progress/', MCP_SPEC_URL),
    '4.6': ('https://spec.modelcontextprotocol.io/specification/basic/utilities/cancellation/', MCP_SPEC_URL),

    # Domain 5 — Auth, Security, Trust & Registry (15%)
    '5.1': ('https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization', 'https://datatracker.ietf.org/doc/html/rfc7591'),
    '5.2': ('https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12', 'https://datatracker.ietf.org/doc/html/rfc9207'),
    '5.3': ('https://datatracker.ietf.org/doc/html/rfc8707', 'https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization'),
    '5.4': (OWASP_MCP_URL, MCP_REGISTRY_URL),
    '5.5': (OWASP_MCP_URL, 'https://genai.owasp.org/'),

    # Domain 6 — SDKs, Deployment, Observability & Ecosystem (15%)
    '6.1': ('https://github.com/modelcontextprotocol/typescript-sdk', 'https://github.com/modelcontextprotocol/python-sdk'),
    '6.2': ('https://github.com/modelcontextprotocol/inspector', MCP_INTRO_URL),
    '6.3': ('https://modelcontextprotocol.io/docs/tools/inspector', 'https://modelcontextprotocol.io/docs/develop/build-server'),
    '6.4': ('https://opentelemetry.io/docs/specs/semconv/gen-ai/', 'https://modelcontextprotocol.io/docs/concepts/transports'),
    '6.5': (MCP_REGISTRY_URL, 'https://modelcontextprotocol.io/examples'),
}
