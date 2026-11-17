"""Ordered 4-step sequence terms (kind='O') for MCP 6x100 practice sets.

Each group defines 1 `_ok` key and 3 plausible `_w1.._w3` sequence distractors (<= 240 chars per label).
"""

SEQUENCE_TERMS = {
    # 1.2 — MCP Initialization Handshake
    'seq_mcp_init_ok': (
        'Client sends `initialize` with `protocolVersion` & `capabilities` → server replies with negotiated version & capabilities → client sends `notifications/initialized` → normal `tools/list` & `resources/list` calls begin',
        'follows MCP lifecycle spec: version/capability negotiation via initialize exchange completed by initialized notification before any feature calls.',
        'calling tools before the initialize/initialized handshake completes violates MCP lifecycle ordering and capability discovery.',
    ),
    'seq_mcp_init_w1': (
        'Client calls `tools/call` immediately → server returns capability list on tool error → client sends `initialize` afterward → skip `notifications/initialized`',
        'never correct: tool calls require prior capability negotiation and the initialized notification marks handshake completion.',
        'invoking tools before initialize negotiation bypasses version checks and omits the required initialized signal.',
    ),
    'seq_mcp_init_w2': (
        'Server sends `initialize` to client → client negotiates logging level first → exchange OAuth tokens inside `initialize` params → begin sampling without capability check',
        'never correct: only clients initiate initialize, auth is orthogonal to lifecycle, and sampling requires explicit capability advertisement.',
        'reversing the initialize direction and mixing OAuth into initialize params conflates lifecycle with authorization.',
    ),
    'seq_mcp_init_w3': (
        'Client hardcodes `protocolVersion: \"1.0\"` forever → ignore server `protocolVersion` echo → send duplicate `initialize` on every ping → cache capabilities indefinitely',
        'never correct: clients must negotiate versions dynamically, re-initialize only on reconnection, and respect server capability changes.',
        'hardcoding protocol versions and duplicate initialize pings breaks forward compatibility and lifecycle idempotency.',
    ),

    # 2.1 — Tool Definition & Execution Flow
    'seq_mcp_tool_exec_ok': (
        'Server declares tool with `name`, `description`, `inputSchema` (JSON Schema) → client `tools/list` discovers it → model calls `tools/call` with validated args → server validates, executes idempotently & returns `content` + `isError`',
        'matches MCP Tools spec: declarative schema, client discovery, validated execution, and structured content/error signaling.',
        'exposing tools without JSON Schema or returning raw stack traces without isError and structured content violates the Tools contract.',
    ),
    'seq_mcp_tool_exec_w1': (
        'Server exposes 200 tools without descriptions → client guesses arguments via prompt → server executes shell with raw LLM string → return HTML page inside isError=false',
        'never correct: undeclared schemas, guessed args, and raw shell execution invite injection and unparseable outputs.',
        'missing inputSchema and raw shell interpolation from unvalidated LLM strings creates prompt-injection and RCE risk.',
    ),
    'seq_mcp_tool_exec_w2': (
        'Client calls undefined tool name → server creates tool on-the-fly → skip inputSchema validation → stream 50-MB blob as single text content block',
        'never correct: servers must pre-declare tools, validate against inputSchema, and chunk large outputs via Resources or pagination.',
        'ad-hoc tool creation without validation and massive single-block responses break type safety and token budgets.',
    ),
    'seq_mcp_tool_exec_w3': (
        'Server returns tool result before validation → client retries with doubled args → disable tools/list_changed notifications → cache tool names forever',
        'never correct: results must follow validation, retries need idempotency keys, and dynamic tool changes require list_changed notifications.',
        'responding before validation and ignoring list_changed events leaves clients with stale, unvalidated tool catalogs.',
    ),

    # 2.4 — Resource Discovery & Reading
    'seq_mcp_resource_ok': (
        'Server advertises `resources` capability → client calls `resources/list` or `resources/templates/list` → client reads `resources/read` with `uri` → server returns `contents` with `mimeType`, handling pagination cursors',
        'follows Resources spec: capability advertisement, list/template discovery, uri-addressed reads with mime-typed contents and pagination.',
        'returning file paths without URI schemes or mimeTypes and omitting capability negotiation breaks MCP resource addressing.',
    ),
    'seq_mcp_resource_w1': (
        'Client guesses file URIs without list → server returns OS absolute paths as uri → embed 10-MB binary as base64 JSON string → skip uri validation',
        'never correct: clients must discover via list/templates, URIs need scheme validation, and large binaries need proper mimeType handling.',
        'guessing URIs and exposing raw OS paths without scheme checks violates resource discovery and isolation.',
    ),
    'seq_mcp_resource_w2': (
        'Server lists resources without capability flag → client polls `resources/list` every 10 ms in loop → ignore `resources/list_changed` notifications → request resources via tools/call',
        'never correct: resource access requires capability, aggressive polling wastes cycles, and resources have dedicated read methods.',
        'tight polling without subscription to list_changed notifications defeats MCP push efficiency and protocol layering.',
    ),
    'seq_mcp_resource_w3': (
        'Server returns resources without uri fields → client stores resource content in tool history → server omits page cursors for 10k items → skip mimeType declaration',
        'never correct: resources are uri-addressed with typed contents and large listings require cursor-based pagination.',
        'omitting uri and mimeType fields and ignoring pagination cursors makes resources unaddressable and unfilterable.',
    ),

    # 3.2 — Roots Boundary Enforcement
    'seq_mcp_roots_ok': (
        'Client declares `roots` capability with `file://` allowlist → server calls `roots/list` to learn boundaries → server restricts `resources/read` & tool file ops to those roots → handle `notifications/roots/list_changed`',
        'implements Roots spec: client-owned boundary declaration, server-enforced confinement, and dynamic list_changed handling.',
        'allowing servers to invent filesystem boundaries or ignore roots/list violates client-controlled sandboxing.',
    ),
    'seq_mcp_roots_w1': (
        'Server declares client roots unilaterally → client trusts arbitrary server-provided paths → skip roots/list → ignore list_changed notifications',
        'never correct: roots are client-declared boundaries; servers must discover and respect them via roots/list subscriptions.',
        'letting servers dictate client filesystem boundaries inverts MCP trust and breaks host isolation.',
    ),
    'seq_mcp_roots_w2': (
        'Client exposes entire `C:\\` without consent → server walks parent directories above declared roots → disable path canonicalization → follow symlinks blindly',
        'never correct: exposure needs user consent, servers must canonicalize and block traversal/symlink escape beyond roots.',
        'exposing full drive without consent and walking above root boundaries with symlink following enables directory traversal.',
    ),
    'seq_mcp_roots_w3': (
        'Server hardcodes `roots/list` response → client polls filesystem without notification channel → skip name/uri validation → cache roots forever',
        'never correct: roots come live from client, changes push via notifications, and both name/uri need validation.',
        'hardcoding roots and ignoring list_changed notifications leaves stale boundaries after user permission changes.',
    ),

    # 3.3 — Sampling (Server-to-Client LLM Request)
    'seq_mcp_sampling_ok': (
        'Server advertises sampling need → checks client `sampling` capability → sends `sampling/createMessage` with `messages`, `maxTokens`, `modelPreferences` → client applies human-in-loop gating & returns generation',
        'follows Sampling spec: capability-checked server-initiated LLM delegation with explicit modelPreferences and human approval gating.',
        'issuing sampling without capability checks or modelPreferences and auto-approving without human review breaks spec and safety.',
    ),
    'seq_mcp_sampling_w1': (
        'Server sends sampling without capability check → include raw customer PII in messages → skip maxTokens limits → client auto-executes without user consent',
        'never correct: sampling requires capability, PII minimization, bounded tokens, and user-mediated approval before forwarding to LLM.',
        'unbounded PII-laden sampling without capability or consent bypasses privacy and authorization boundaries.',
    ),
    'seq_mcp_sampling_w2': (
        'Client exposes sampling by default without opt-in → server loops sampling/createMessage recursively → ignore modelPreferences hints → return raw chain-of-thought as tool output',
        'never correct: sampling is opt-in client capability, loops need depth caps, and preferences guide model selection responsibly.',
        'default-exposed sampling and uncapped recursive loops risk token runaway and expose internal reasoning inappropriately.',
    ),
    'seq_mcp_sampling_w3': (
        'Server mixes sampling messages into tool descriptions → client forwards without isolation → skip cost tracking → cache sampling results as facts',
        'never correct: sampling messages are distinct delegation calls requiring isolation, accounting, and non-cacheability guarantees.',
        'confusing sampling payloads with tool metadata conflates delegation layers and breaks cost attribution.',
    ),

    # 4.2 — Streamable HTTP Transport
    'seq_mcp_streamhttp_ok': (
        'Client POSTs JSON-RPC to single `mcp` endpoint with `Content-Type: application/json` & `Accept: text/event-stream, application/json` → server may respond with single JSON or SSE stream → client honors `Mcp-Session-Id` & `Last-Event-ID` for resumability',
        'matches 2025-11-25 Streamable HTTP spec: single endpoint, dual Accept, session ID management, and resumable SSE stream option.',
        'using two separate endpoints for SSE/POST, ignoring Accept negotiation, or dropping session IDs breaks Streamable HTTP resumability.',
    ),
    'seq_mcp_streamhttp_w1': (
        'Client opens separate GET /sse and POST /message SSE endpoints → send JSON without Accept header → ignore Mcp-Session-Id → close stream after each chunk without Last-Event-ID',
        'never correct: Streamable HTTP unified to one POST endpoint, requires Accept negotiation, and uses session IDs with resumability IDs.',
        'splitting endpoints and ignoring session/resumability headers reverts to pre-March 2025 deprecated SSE transport.',
    ),
    'seq_mcp_streamhttp_w2': (
        'Server returns 200 OK with HTML error page → client retries without backoff → disable idempotency on non-idempotent tool calls → omit Content-Type validation',
        'never correct: JSON-RPC errors need structured error objects, retries must be bounded with backoff and idempotency awareness.',
        'returning HTML instead of JSON-RPC errors and retrying without backoff causes parsing failures and duplicate mutations.',
    ),
    'seq_mcp_streamhttp_w3': (
        'Client sends batched 100 requests without server batch ack → server streams without event IDs → skip session expiry handling → leak session IDs across tenants',
        'never correct: batches need server-acknowledged limits, streams require event IDs for replay, and session IDs must be tenant-isolated.',
        'unbounded batching and cross-tenant session ID reuse breaks rate limiting and tenant isolation guarantees.',
    ),

    # 5.2 — OAuth 2.1 / Authorization Flow
    'seq_mcp_oauth_ok': (
        'Server exposes `/.well-known/oauth-authorization-server` with PRM & CIMD → client fetches RS metadata with `resource` indicator (RFC 8707) → PKCE + state + RFC 9207 iss validation → audience-bound token issued per resource server',
        'follows MCP auth spec evolution: OAuth 2.1 with PKCE, protected resource metadata, RFC 8707 audience binding, and RFC 9207 issuer checks.',
        'accepting bearer tokens without iss or audience checks and skipping PKCE leaves token substitution and mix-up vulnerabilities.',
    ),
    'seq_mcp_oauth_w1': (
        'Client sends static API key in Authorization header → server skips issuer discovery → accept tokens with alg:none → grant org-admin scope by default',
        'never correct: MCP authorization uses OAuth 2.1 discovery, mandatory issuer/audience validation, and least-privilege scopes.',
        'hardcoded keys and alg:none tokens with blanket admin grants violate OAuth 2.1 and privilege separation.',
    ),
    'seq_mcp_oauth_w2': (
        'Client trusts token from any issuer → skip RFC 9207 iss equality check → ignore RFC 7591 dynamic registration → reuse single token across all resource servers',
        'never correct: RFC 9207 requires exact iss match to metadata, and RFC 8707 demands per-resource-server audience-bound tokens.',
        'reusing a single audience-less token across resource servers enables cross-server token replay and mix-up attacks.',
    ),
    'seq_mcp_oauth_w3': (
        'Server embeds client_secret in JS bundle → disable PKCE as optional → return tokens over plain HTTP → cache discovery doc forever without TLS',
        'never correct: public clients must not ship secrets, PKCE is required, tokens require TLS, and discovery needs fresh validated fetches.',
        'exposing secrets in client bundles and downgrading PKCE/TLS undermines OAuth confidentiality and channel binding.',
    ),

    # 5.4 — MCP Security Threat Model (Tool Poisoning, Rug Pull, etc.)
    'seq_mcp_security_ok': (
        'Pin server versions & verify registry signatures → isolate tool descriptions from executable logic → prompt user before first tool approval & high-risk actions → log tool provenance & monitor for description drift',
        'applies MCP security checklist: supply-chain pinning, description-vs-logic separation, consent gating, and provenance monitoring against poison/rug-pull.',
        'auto-approving all tools and trusting description text as safe instructions enables tool poisoning and silent post-approval logic swaps.',
    ),
    'seq_mcp_security_w1': (
        'Auto-approve all tools without review → trust tool description text as system prompt → allow server to change tool logic post-approval → skip signature verification',
        'never correct: descriptions are untrusted, approvals need explicit consent, and post-approval logic changes without re-consent equal rug pulls.',
        'blind auto-approval and treating descriptions as trusted instructions invites prompt injection and supply-chain compromise.',
    ),
    'seq_mcp_security_w2': (
        'Install random GitHub MCP servers via curl|bash → grant full filesystem + network + env scopes → disable log redaction → store tokens in plaintext',
        'never correct: servers need registry vetting, least-privilege sandboxing, redacted logs, and secure token storage via OS keychain.',
        'unvetted curl-piped installs with maximal scopes and plaintext token storage maximizes blast radius from a single malicious server.',
    ),
    'seq_mcp_security_w3': (
        'Exfiltrate tool arguments to third-party analytics silently → skip rate limiting on tool calls → omit provenance tags → hide tool calls from audit UI',
        'never correct: tool calls handle sensitive data needing purpose limitation, rate limits, provenance tagging, and transparent audit trails.',
        'silent exfiltration without rate limits or audit visibility breaks data minimization and incident-response traceability.',
    ),

    # 6.3 — Inspector & Server Development Workflow
    'seq_mcp_inspector_ok': (
        'Scaffold via TS/Python SDK `create-server` template → test with `npx @modelcontextprotocol/inspector` (UI + CLI) → validate `tools/list` & `tools/call` against JSON Schema → publish to registry with server.json & signed attestation',
        'matches official build flow: SDK scaffold, Inspector interactive validation, schema conformance checks, and registry publication with metadata.',
        'publishing without Inspector validation or server.json metadata and hardcoding secrets in repo skips verification and supply-chain hygiene.',
    ),
    'seq_mcp_inspector_w1': (
        'Write server without SDK types → skip Inspector testing → hand-edit server.json without schema validation → commit secrets in repo for CI',
        'never correct: SDKs provide typed handlers, Inspector catches lifecycle/capability bugs, and server.json needs schema validation.',
        'bypassing typed SDKs and Inspector validation ships lifecycle mismatches and credential leaks undetected.',
    ),
    'seq_mcp_inspector_w2': (
        'Test only with mocked client → ignore tools/list_changed events → skip pagination tests → push container with :latest & root user',
        'never correct: real transports matter, dynamic listings need pagination coverage, and containers need pinned tags with non-root users.',
        'ignoring dynamic list_changed and pagination paths leaves 90% of protocol surface untested.',
    ),
    'seq_mcp_inspector_w3': (
        'Copy paste tool schemas from blog post → never check protocolVersion negotiation → disable capability advertisement → run Inspector without auth context',
        'never correct: versioned capability negotiation and auth-scoped testing are required to catch compatibility and permission regressions.',
        'skipping version/capability advertisement and auth-context testing hides negotiation and authorization failures.',
    ),
}
