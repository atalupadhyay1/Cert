"""Canonical option dictionary (`TERMS`) for MCP 6x100 Udemy practice sets.

Every entry is `(option_label, correct_note, distractor_note)` with `len(option_label) <= 250`.
"""

from sequences import SEQUENCE_TERMS

ATOMIC_TERMS = {
    # -------------------------------------------------------------------------
    # Domain 1 — MCP Foundations, Architecture & Lifecycle
    # -------------------------------------------------------------------------
    'arch_host_client_server': (
        'Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation',
        'correctly separates trust boundaries: Hosts own UI/policy, Clients speak MCP, Servers expose capabilities behind capability negotiation.',
        'collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.',
    ),
    'arch_client_one_to_one': (
        'Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle',
        'enforces 1:1 Client-Server lifecycle so pings, cancellations and session IDs map unambiguously without multiplexing bugs.',
        'multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.',
    ),
    'arch_stdio_vs_streamable': (
        'Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)',
        'maps transport to deployment topology: stdio gives OS-level isolation locally; Streamable HTTP enables remote multi-tenant scale.',
        'forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.',
    ),
    'lifecycle_initialize_handshake': (
        'Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`',
        'guarantees version and capability compatibility before feature calls, satisfying the MCP lifecycle invariant.',
        'calling tools before the initialized handshake completes races capability discovery and throws methodNotFound errors.',
    ),
    'lifecycle_protocol_version': (
        'Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect',
        'enables forwards-compatible evolution without breaking older Hosts or Servers on version skew.',
        'hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.',
    ),
    'lifecycle_capabilities_object': (
        'Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage',
        'lets each party call only negotiated features, avoiding methodNotFound and silent fallback hallucinations.',
        'assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.',
    ),
    'lifecycle_notification_vs_request': (
        'Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs',
        'separates best-effort telemetry from correlated RPC state per JSON-RPC 2.0, preventing notification ID collisions.',
        'assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.',
    ),
    'lifecycle_jsonrpc_envelope': (
        'Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603',
        'adheres to the wire contract that underpins batching, cancellation, and error classification across both transports.',
        'wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.',
    ),
    'lifecycle_ping_keepalive': (
        'Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways',
        'provides spec-guaranteed failure detection where OS TCP keepalives are invisible to application-level SSE/stdio proxies.',
        'relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.',
    ),
    'lifecycle_progress_notifications': (
        'Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`',
        'gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.',
        'polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.',
    ),
    'lifecycle_cancellation': (
        'Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets',
        'gracefully aborts model-driven tool storms while freeing server resources and meeting JSON-RPC cancellation semantics.',
        'killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.',
    ),
    'lifecycle_error_codes': (
        'Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`',
        'standardizes remediation: 32601 means check capabilities, 32602 means fix schema, unlike bespoke string matching.',
        'returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.',
    ),
    'lifecycle_completions': (
        'Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params',
        'enables UX-level typeahead without invoking costly tools, scoped to declared completion capabilities.',
        'implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.',
    ),
    'arch_mcp_vs_functioncall': (
        'Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**',
        'clarifies layer boundaries: MCP standardizes context attachment; function calling is inline model schema; A2A negotiates task handoffs.',
        'treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.',
    ),
    'arch_experimental_capability': (
        'Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization',
        'allows safe iteration on draft specs like Tasks and elicitation without polluting the stable capability surface.',
        'enabling experimental tasks by default without capability checks forces unready clients into breaking draft methods.',
    ),

    # -------------------------------------------------------------------------
    # Domain 2 — Tools, Resources & Resource Templates
    # -------------------------------------------------------------------------
    'tool_declaration_schema': (
        'Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`',
        'gives models complete, machine-validated contracts for tool selection and argument generation.',
        'declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.',
    ),
    'tool_annotations_hints': (
        'Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions',
        'signals cost/safety posture without hard-coding policy; models prefer readOnly before destructive in multi-step plans.',
        'labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.',
    ),
    'tool_model_controlled': (
        'Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke',
        'preserves user/model agency and auditability; every mutation traces to an explicit model decision with tool audit event.',
        'having servers push tool executions without model initiation undermines approval and provenance guarantees.',
    ),
    'tool_list_discovery': (
        'Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**',
        'enables complete catalog sync for hosts that cache tool lists and paginate beyond 50 items without omission.',
        'returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.',
    ),
    'tool_call_validation': (
        'Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure',
        'defends against LLM hallucinated args and preserves typed error handling via isError flag versus exception propagation.',
        'entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.',
    ),
    'tool_output_content': (
        'Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean',
        'lets clients render multimodal results safely while distinguishing success from app-level errors without parsing text.',
        'dumping base64 blobs as plain text without typed content blocks loses mimeType and forces heuristic parsing.',
    ),
    'tool_structured_output': (
        'Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`',
        'bridges LLM reasoning with downstream code that consumes validated JSON, not regex scraped prose.',
        'forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.',
    ),
    'resource_direct_vs_template': (
        'Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**',
        'models browse concrete resources via list and expand templates param by param without guessing URI syntax.',
        'presenting all files as templates with free-form interpolation forces models to guess required path variables.',
    ),
    'resource_uri_scheme': (
        'Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`',
        'provides stable, scheme-scoped addressing that survives renames and scopes authZ per resource origin.',
        'using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.',
    ),
    'resource_list_pagination': (
        'Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent',
        'handles 10k-file workspaces without truncation or timeout, matching MCP pagination contract for both lists.',
        'ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.',
    ),
    'resource_read_blocks': (
        'Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks',
        'delivers typed content blocks that render correctly in Host UIs with binary vs text handling pre-decided by mimeType.',
        'returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.',
    ),
    'resource_subscribe_watch': (
        'Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`',
        'keeps IDE diagnostics in sync with file edits without polling, per spec subscription lifecycle.',
        'polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.',
    ),
    'resource_list_changed': (
        'Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling',
        'pushes freshness efficiently after external ingestion jobs create new datasets, without constant re-list overhead.',
        'requiring clients to poll list on a timer to detect new resources defeats MCP push efficiency.',
    ),
    'prompt_declaration': (
        'Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`',
        'turns curated prompt packs into discoverable UX shortcuts argument-by-argument with typed validation.',
        'stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.',
    ),
    'prompt_get_expansion': (
        'Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context',
        'compiles parameterized prompt templates server-side with validated args, keeping prompt injection surface server-controlled.',
        'doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.',
    ),
    'prompt_list_changed': (
        'Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs',
        'keeps prompt pickers fresh without re-listing on every keystroke, matching resource/tool change notification pattern.',
        're-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.',
    ),
    'completion_provider': (
        'Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`',
        'powers low-latency autocomplete dropdowns directly from server-side datasets without tool execution overhead.',
        'executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.',
    ),

    # -------------------------------------------------------------------------
    # Domain 3 — Prompts, Sampling, Roots & Elicitation
    # -------------------------------------------------------------------------
    'sampling_create_message': (
        'Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`',
        'lets servers delegate LLM sub-tasks (summarization, critique) back to the Host model under explicit preference caps.',
        'letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.',
    ),
    'sampling_model_prefs': (
        'Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing',
        'maps server intent to Host model fleet tiers without hardcoding vendor model IDs into server code.',
        'hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.',
    ),
    'sampling_include_context': (
        'Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`',
        'limits what prior server context flows into delegated sampling calls, preventing cross-server data exfiltration.',
        'setting includeContext=allServers by default fans sensitive data from every connected server into one sampling call.',
    ),
    'roots_list_capability': (
        'Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`',
        'gives users explicit allowlist control over which directories a server may touch, enforced server-side.',
        'letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.',
    ),
    'roots_path_validation': (
        'Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`',
        'prevents `../` and symlink hop attacks that would escape the user’s approved `file://` allowlist.',
        'joining user input with path concatenation without canonicalization enables classic directory traversal.',
    ),
    'roots_change_notification': (
        'React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions',
        'keeps server views consistent when users add/remove workspace folders mid-session without restart.',
        'caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.',
    ),
    'elicitation_schema': (
        'Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`',
        'turns server data needs into typed Host-rendered forms rather than chat text parsing, with explicit schema validation.',
        'parsing free-form chat replies as structured data instead of typed elicitation invites format errors and injection.',
    ),
    'elicitation_vs_sampling': (
        'Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them',
        'separates fact acquisition (user-filled forms) from subjective generation (model-composed prose) for audit clarity.',
        'asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.',
    ),
    'logging_level_control': (
        'Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads',
        'respects user-selected verbosity while still flowing warnings/errors through observability pipelines.',
        'spamming debug traces at error level drowns real failures and violates MCP logging level contract.',
    ),
    'progress_token_link': (
        'Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request',
        'correlates streaming progress notifications to the correct in-flight tool/resource fetch without guessing.',
        'generating random progressTokens server-side with no binding to request id mixes streams across concurrent tasks.',
    ),

    # -------------------------------------------------------------------------
    # Domain 4 — Transports, Sessions & Protocol Evolution
    # -------------------------------------------------------------------------
    'transport_stdio_spawn': (
        'Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle',
        'gives OS-level isolation, clean env var scoping, and automatic teardown when Host exits without port conflicts.',
        'running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.',
    ),
    'transport_stdio_stderr_logs': (
        'Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages',
        'prevents log interleaving from corrupting JSON-RPC framing that parsers expect line-delimited on stdout.',
        'printing logs to stdout alongside JSON-RPC breaks line-delimited parsing and throws Parse error -32700.',
    ),
    'transport_streamable_single_endpoint': (
        'Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation',
        'unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.',
        'keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.',
    ),
    'transport_streamable_accept': (
        'Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly',
        'lets simple request/reply skip SSE overhead while enabling streaming only for long-running tool progress.',
        'forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.',
    ),
    'transport_session_id': (
        'Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects',
        'preserves capability state and pagination cursors after transient network loss without re-initializing.',
        'generating a new random session ID per request loses pagination state and forces full re-handshake each call.',
    ),
    'transport_last_event_id': (
        'Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect',
        'recovers progress streams and notifications lost during 5–30s mobile handoffs without missing tool progress events.',
        'omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.',
    ),
    'transport_sse_deprecated': (
        'Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics',
        'tracks spec evolution: split GET /sse + POST /messages merged into single POST with Accept-driven streaming.',
        'deploying greenfield on the deprecated dual-endpoint SSE transport incurs future migration cost and lacks session IDs.',
    ),
    'transport_reconnection_strategy': (
        'Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`',
        'avoids thundering herds after gateway restarts while ensuring exactly-once progress recovery via resumability.',
        'reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.',
    ),
    'transport_batching_limits': (
        'Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation',
        'exploits batching for listing throughput without overwhelming server concurrency caps or mixing response IDs.',
        'batching 200 unrelated tool calls into one HTTP request beyond advertised limits times out the whole batch.',
    ),
    'transport_gateway_interop': (
        'Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation',
        'keeps MCP semantics intact through enterprise L7 filters that otherwise strip SSE headers and session sticky state.',
        'deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.',
    ),
    'transport_ping_interval': (
        'Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs',
        'survives AWS ALB 60s idle timeout and Kubernetes GFE that silently drops idle SSE streams.',
        'relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.',
    ),

    # -------------------------------------------------------------------------
    # Domain 5 — Auth, Security, Trust & Registry
    # -------------------------------------------------------------------------
    'auth_oauth21_required': (
        'Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows',
        'aligns MCP with current OAuth 2.1 security posture, eliminating token leakage vectors of legacy grants.',
        'using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.',
    ),
    'auth_protected_resource_metadata': (
        'Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414',
        'enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.',
        'hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.',
    ),
    'auth_rfc7591_dynamic': (
        'Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals',
        'scales zero-touch onboarding across thousands of tenant Host instances without manual client_id provisioning.',
        'requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.',
    ),
    'auth_rfc8707_audience': (
        'Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization',
        'prevents token replay to unintended resource servers by audience-restricting each bearer token.',
        'issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.',
    ),
    'auth_rfc9207_iss': (
        'Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token',
        'blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.',
        'skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.',
    ),
    'auth_cimd_metadata': (
        'Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets',
        'binds public client identity to TLS-verifiable origin without long-lived client secrets in distributed Hosts.',
        'embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.',
    ),
    'auth_localhost_callback': (
        'Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes',
        'supports desktop IDE/CLI auth via ephemeral loopback listeners while forbidding http redirects to remote hosts.',
        'allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.',
    ),
    'auth_token_storage': (
        'Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files',
        'keeps refresh tokens survivable across restarts but invisible to process dumps, forked children, and leaked logs.',
        'writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.',
    ),
    'auth_scope_least_privilege': (
        'Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side',
        'prevents a read-only doc-search server from silently acquiring destructive write scopes after one-time user approval.',
        'bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.',
    ),
    'security_tool_poisoning': (
        'Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately',
        'displays descriptions for human review but never concatenates them into system prompts or plan steps as trusted policy.',
        'copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.',
    ),
    'security_rug_pull': (
        'Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change',
        'forces re-approval when a benign `get_weather` server silently rewires to `exfiltrate_files` after approval.',
        'trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.',
    ),
    'security_privilege_escalation': (
        'Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging',
        'stops a docs MCP server from using its tool output to call a payment MCP’s `transfer` tool via implicit ambient authority.',
        'letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.',
    ),
    'security_prompt_injection_mcp': (
        'Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails',
        'tags third-party fetched content so downstream Hosts can sandtrap it before the model treats it as instruction.',
        'feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.',
    ),
    'security_registry_trust': (
        'Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)',
        'provides supply-chain tamper evidence via package signing and publisher identity beyond raw GitHub stars.',
        'installing random `curl | bash` MCP servers without registry signature verification imports unvetted RCE into the IDE.',
    ),
    'security_env_isolation': (
        'Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default',
        'prevents a malicious calendar server from harvesting `AWS_SECRET_ACCESS_KEY` and `GITHUB_PAT` from Host env dump.',
        'passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.',
    ),
    'security_audit_logging': (
        'Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)',
        'enables post-incident forensics without persisting PII/tokens, keyed by stable tool provenance hashes.',
        'logging full tool arguments including customer PII and bearer tokens creates GDPR and credential-leak second-order risks.',
    ),

    # -------------------------------------------------------------------------
    # Domain 6 — SDKs, Deployment, Observability & Ecosystem
    # -------------------------------------------------------------------------
    'sdk_typescript_server': (
        'Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**',
        'uses typed server helpers that auto-wire tools/list/call handlers and JSON Schema validation from Zod objects.',
        'hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.',
    ),
    'sdk_python_server': (
        'Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan',
        'gives decorator-ergonomic tool/resource registration with Pydantic/JSON Schema coherence across Python Hosts.',
        'scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.',
    ),
    'sdk_client_connection': (
        'Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking',
        'standardizes transport selection, capability tracking, and request/notification routing behind a single Client facade.',
        'mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.',
    ),
    'inspector_validation': (
        'Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively',
        'catches lifecycle, capability, and schema mismatches before CI with real-transport conformance testing.',
        'skipping Inspector and relying only on unit mocks misses real transport framing and pagination/cancellation bugs.',
    ),
    'inspector_cli_ci': (
        'Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI',
        'automates protocol conformance as a PR check alongside lint/tests, proving list/call contracts headlessly.',
        'gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.',
    ),
    'deployment_docker_isolation': (
        'Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping',
        'ensures reproducible, least-privilege runtime with declared transport and liveness for orchestrators.',
        'shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.',
    ),
    'deployment_registry_publish': (
        'Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification',
        'makes servers discoverable with verifiable supply-chain metadata and semver-aware update notifications.',
        'distributing servers as raw GitHub tarballs without server.json or publisher proof hides supply-chain compromise.',
    ),
    'deployment_versioning_strategy': (
        'Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible',
        'keeps patch/minor server releases compatible with older Hosts that simply ignore unknown capabilities.',
        'bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.',
    ),
    'observability_otel_spans': (
        'Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)',
        'traces tool call latency through Streamable HTTP gateways into server execution with per-session correlation.',
        'disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.',
    ),
    'observability_structured_logging': (
        'Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`',
        'powers per-tool SLOs and supply-chain forensics without persisting sensitive tool argument values.',
        'logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.',
    ),
    'ecosystem_mcp_registry_search': (
        'Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds',
        'reuses vetted categories (databases, cloud, payments) before building bespoke wrappers over public APIs.',
        'reimplementing a Postgres MCP server from scratch when a registry-verified one already exists wastes review cycles.',
    ),
    'ecosystem_a2a_bridge': (
        'Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks',
        'uses MCP vertically for capabilities and A2A horizontally for peer negotiation, per LM-Foundation AAIF stack guidance.',
        'treating MCP as a replacement for A2A agent discovery and task lifecycles conflates vertical tool attachment with peer delegation.',
    ),
    'ecosystem_vscode_claude_host': (
        'Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes',
        'standardizes cross-Host deployment via portable config blocks with scoped env and per-server enable toggles.',
        'editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.',
    ),
    'sdk_error_propagation': (
        'Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults',
        'distinguishes app-level tool errors (tool ran, domain said no) from protocol-level crashes clients can retry.',
        'throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.',
    ),
    'gateway_mcp_routing': (
        'Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)',
        'centralizes AuthZ, session affinity, and observability without duplicating gateway logic in each MCP server.',
        'exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.',
    ),
}

# Overlay sequence terms (36 extra option keys across 9 pipelines)
TERMS = {**ATOMIC_TERMS, **SEQUENCE_TERMS}

# Guard: label sizes and banned patterns at import time
for _k, (_label, _ok, _bad) in TERMS.items():
    assert len(_label) <= 255, f'TERM {_k} label {len(_label)} > 255'
    assert 'drop ' not in _label.lower(), f'TERM {_k} contains banned \"drop \" phrase'
