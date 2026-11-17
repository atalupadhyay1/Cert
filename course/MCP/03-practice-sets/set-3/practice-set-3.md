# MCP: Model Context Protocol: Servers, Clients, Transports & Security — Full-Length Mock Exam 3 — AtlasCloud Platform Ops (Cloud Infra & DevTools)

**Theme:** JSON-RPC Framing, Tools vs Resources, OAuth 2.1 PKCE & Inspector CI Gates  
**Credential alignment:** `Model Context Protocol (MCP 2025-11-25) — Tool & Context Standard`  
**Blueprint baseline:** `November 2026 (MCP Specification 2025-11-25 · MCP Registry & Inspector · OAuth 2.1 + RFC 8707/9207 + CIMD · OWASP MCP Security Checklist)` (https://modelcontextprotocol.io/introduction · https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation · https://genai.owasp.org/resource/mcp-security-checklist/)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `120 minutes` (`72 seconds/question` full-endurance pacing; aligns with `120 minutes` on NVIDIA NCP-AAI & GitHub GH-600)

> **Disclaimer:** Independent educational practice material authored from public engineering specifications and open-protocol documentation — not affiliated with, sponsored by, or endorsed by NVIDIA, the Linux Foundation, Anthropic, OpenAI, Google, Microsoft, GitHub, LangChain, or OWASP. Practice scores do not guarantee passing any third-party certification exam.

## Questions

---

## Domain 1 — MCP Foundations, Architecture & Lifecycle (16–20% blueprint weight · 18 questions)

### 1. Proposed solution: skip issuer validation and accept bearer tokens from any alg:none issuer for platform telemetry at AtlasCloud Platform Ops. Does this meet the goal? Incident 7090: deprecated `/sse` + `/messages` split endpoint still in prod. [1.1 #1]

- **A.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **B.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`
- **C.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **D.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation

### 2. For platform telemetry at AtlasCloud Platform Ops, token storage uses plaintext `config.json`. The secure alternative is to ____. Case 3441: `structuredContent` missing despite `outputSchema` declared. [1.1 #2]

- **A.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **B.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **C.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **D.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation

### 3. For platform telemetry at AtlasCloud Platform Ops, the MCP Inspector UI must validate tool schemas. Which approach is correct? Incident MCP-2026-3918 shows Misconfigured `Mcp-Session-Id` routing. [1.1 #3]

- **A.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **B.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **C.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **D.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)

### 4. Which two behaviors correctly describe MCP platform telemetry handling at AtlasCloud Platform Ops? Select two. Incident 1614: OAuth PKCE verifier omitted for public client. [1.2 #4]

- **A.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`
- **B.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **C.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **D.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks
- **E.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively

### 5. The AtlasCloud Platform Ops MCP configuration for platform telemetry shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Trace 5979: 200-tool batch exceeds advertised `maxBatchSize`. [1.2 #5]

- **A.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **B.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **C.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **D.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`

### 6. For platform telemetry, AtlasCloud Platform Ops must choose between stdio and Streamable HTTP transports. The correct choice is to ____. Trace 1789 reveals truncated cursor pagination at 50 entries. [1.2 #6]

- **A.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **B.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **C.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **D.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent

### 7. For platform telemetry at AtlasCloud Platform Ops, two best practices align with MCP 2025-11-25. Which two should be implemented? Select two. Incident 7033: tool logic changed post-approval (rug-pull) undetected. [1.3 #7]

- **A.** Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation
- **B.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **C.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **D.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **E.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging

### 8. AtlasCloud Platform Ops wants to bridge platform telemetry MCP tools into an A2A task mesh. The correct layer definition is ____. Log 6685: SSE stream without `eventId` loses progress on reconnect. [1.3 #8]

- **A.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **B.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **C.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **D.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways

### 9. Complete the missing MCP field: In the AtlasCloud Platform Ops platform telemetry server, `____` must be set to the MCP-required value to enable platform telemetry correctly. Alert 2772: `progressToken` mismatch across concurrent tool calls. [1.3 #9]

- **A.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **B.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **C.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification
- **D.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs

### 10. For platform telemetry at AtlasCloud Platform Ops, which ordered flow correctly implements the MCP 2025-11-25 requirement? Alert 8254: `Mcp-Session-Id` reused across tenants. Scenario 1.4-3-10.

- **A.** Client hardcodes `protocolVersion: "1.0"` forever → ignore server `protocolVersion` echo → send duplicate `initialize` on every ping → cache capabilities indefinitely
- **B.** Server sends `initialize` to client → client negotiates logging level first → exchange OAuth tokens inside `initialize` params → begin sampling without capability check
- **C.** Client sends `initialize` with `protocolVersion` & `capabilities` → server replies with negotiated version & capabilities → client sends `notifications/initialized` → normal `tools/list` & `resources/list` calls begin
- **D.** Client calls `tools/call` immediately → server returns capability list on tool error → client sends `initialize` afterward → skip `notifications/initialized`

### 11. For platform telemetry at AtlasCloud Platform Ops, the Host must reconcile `protocolVersion` negotiation after an upgrade. Which action is correct? Trace 7716 reveals truncated cursor pagination at 50 entries. [1.4 #11]

- **A.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets
- **B.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **C.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **D.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414

### 12. An platform telemetry MCP gateway at AtlasCloud Platform Ops strips `Accept` negotiation headers. The fix is to ____. Trace 9747: 200-tool batch exceeds advertised `maxBatchSize`. [1.4 #12]

- **A.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **B.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **C.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **D.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke

### 13. At AtlasCloud Platform Ops, platform telemetry MCP tool descriptions are concatenated into system prompts. Which safeguard is needed? Incident 9429: deprecated `/sse` + `/messages` split endpoint still in prod. [1.5 #13]

- **A.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **B.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **C.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **D.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`

### 14. For AtlasCloud Platform Ops platform telemetry server to advertise new capabilities after a deploy, the correct notification is ____. Ticket 7052: `roots/list` poll floods client every 10 ms. [1.5 #14]

- **A.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **B.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **C.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **D.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets

### 15. At AtlasCloud Platform Ops, engineers building an MCP server for platform telemetry need to ____. Which configuration correctly implements the MCP specification? Log 9027: `prompt/get` uses client-side interpolation without validation. [1.5 #15]

- **A.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs
- **B.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **C.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation
- **D.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes

### 16. The AtlasCloud Platform Ops team documents the platform telemetry MCP flow. Which sequence of actions is spec-compliant? Ticket 6622: plaintext `config.json` holds refresh token. Scenario 1.6-3-16.

- **A.** Client calls undefined tool name → server creates tool on-the-fly → skip inputSchema validation → stream 50-MB blob as single text content block
- **B.** Server exposes 200 tools without descriptions → client guesses arguments via prompt → server executes shell with raw LLM string → return HTML page inside isError=false
- **C.** Server declares tool with `name`, `description`, `inputSchema` (JSON Schema) → client `tools/list` discovers it → model calls `tools/call` with validated args → server validates, executes idempotently & returns `content` + `isError`
- **D.** Server returns tool result before validation → client retries with doubled args → disable tools/list_changed notifications → cache tool names forever

### 17. Which two logging/observability actions are correct for platform telemetry MCP at AtlasCloud Platform Ops? Select two. Review 9712: `completion/complete` implemented as heavy tool call. [1.6 #17]

- **A.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **B.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **C.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **D.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`
- **E.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**

### 18. During platform telemetry review at AtlasCloud Platform Ops, the MCP server emits debug logs at `error` level. The proper level is ____. Ticket 9652: `roots/list` poll floods client every 10 ms. [1.6 #18]

- **A.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **B.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **C.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **D.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure

---

## Domain 2 — Tools, Resources & Resource Templates (18–22% blueprint weight · 20 questions)

### 19. AtlasCloud Platform Ops must fix its platform telemetry MCP integration. Which two changes bring it into spec compliance? Select two. Incident 9396: OAuth PKCE verifier omitted for public client. [2.1 #19]

- **A.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **B.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **C.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **D.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **E.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions

### 20. An platform telemetry MCP gateway at AtlasCloud Platform Ops strips `Accept` negotiation headers. The fix is to ____. Audit 2238: auto-approve bypasses human consent for destructive tool. [2.1 #20]

- **A.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **B.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **C.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **D.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`

### 21. At AtlasCloud Platform Ops, engineers building an MCP server for platform telemetry need to ____. Which configuration correctly implements the MCP specification? Log entry 6510 shows `Method not found -32601` without capability check. [2.1 #21]

- **A.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **B.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **C.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **D.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**

### 22. For platform telemetry at AtlasCloud Platform Ops, token storage uses plaintext `config.json`. The secure alternative is to ____. Trace 6903 reveals truncated cursor pagination at 50 entries. [2.1 #22]

- **A.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure
- **B.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **C.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **D.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**

### 23. For platform telemetry at AtlasCloud Platform Ops, which ordered flow correctly implements the MCP 2025-11-25 requirement? Audit 4823 flags `alg:none` token acceptance in staging. Scenario 2.2-3-23.

- **A.** Server returns resources without uri fields → client stores resource content in tool history → server omits page cursors for 10k items → skip mimeType declaration
- **B.** Server advertises `resources` capability → client calls `resources/list` or `resources/templates/list` → client reads `resources/read` with `uri` → server returns `contents` with `mimeType`, handling pagination cursors
- **C.** Client guesses file URIs without list → server returns OS absolute paths as uri → embed 10-MB binary as base64 JSON string → skip uri validation
- **D.** Server lists resources without capability flag → client polls `resources/list` every 10 ms in loop → ignore `resources/list_changed` notifications → request resources via tools/call

### 24. At AtlasCloud Platform Ops, engineers building an MCP server for platform telemetry need to ____. Which configuration correctly implements the MCP specification? Incident 8595: OAuth PKCE verifier omitted for public client. [2.2 #24]

- **A.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets
- **B.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **C.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **D.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle

### 25. AtlasCloud Platform Ops wants platform telemetry MCP completions for enum arguments. The valid method is ____. Ticket 7654 reports `Last-Event-ID` replay mismatch after gateway restart. [2.2 #25]

- **A.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **B.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs
- **C.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **D.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean

### 26. The MCP Inspector highlights `____` as missing for platform telemetry at AtlasCloud Platform Ops. Which completion is spec-correct? Ticket 2438: `notifications/roots/list_changed` ignored after folder add. [2.2 #26]

- **A.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure
- **B.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **C.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **D.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs

### 27. During platform telemetry rollout at AtlasCloud Platform Ops, canary hosts skip capability re-validation after reconnect. They should ____. Ticket 6827: `roots/list` poll floods client every 10 ms. [2.3 #27]

- **A.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **B.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **C.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **D.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways

### 28. Proposed solution: To handle platform telemetry, AtlasCloud Platform Ops plans to cache roots forever and ignore notifications/roots/list_changed events. Does this satisfy the MCP specification? Log 1390: `prompt/get` uses client-side interpolation without validation. [2.3 #28]

- **A.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **B.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **C.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **D.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking

### 29. AtlasCloud Platform Ops needs to secure platform telemetry tool calls that mutate production data. The right control is to ____. Trace 2427 reveals truncated cursor pagination at 50 entries. [2.3 #29]

- **A.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **B.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **C.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **D.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414

### 30. The MCP Inspector highlights `____` as missing for platform telemetry at AtlasCloud Platform Ops. Which completion is spec-correct? Audit 9594 flags `alg:none` token acceptance in staging. Scenario 2.4-3-30.

- **A.** Server declares client roots unilaterally → client trusts arbitrary server-provided paths → skip roots/list → ignore list_changed notifications
- **B.** Server hardcodes `roots/list` response → client polls filesystem without notification channel → skip name/uri validation → cache roots forever
- **C.** Client exposes entire `C:\` without consent → server walks parent directories above declared roots → disable path canonicalization → follow symlinks blindly
- **D.** Client declares `roots` capability with `file://` allowlist → server calls `roots/list` to learn boundaries → server restricts `resources/read` & tool file ops to those roots → handle `notifications/roots/list_changed`

### 31. AtlasCloud Platform Ops engineers designing an MCP system for platform telemetry must evaluate two correct controls. Which two statements are correct? Select two. Review 5579: sampling loop lacks depth cap and cost budget. [2.4 #31]

- **A.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **B.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **C.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **D.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **E.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks

### 32. An external auditor flags that AtlasCloud Platform Ops MCP deployment for platform telemetry stores bearer tokens insecurely. The correction is to ____. Log 6391: SSE stream without `eventId` loses progress on reconnect. [2.4 #32]

- **A.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs
- **B.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **C.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **D.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`

### 33. A AtlasCloud MCP client for platform telemetry must ____ to satisfy the protocol. What is the correct implementation approach? Review 7532: sampling loop lacks depth cap and cost budget. [2.5 #33]

- **A.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **B.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **C.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **D.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes

### 34. An external auditor flags that AtlasCloud Platform Ops MCP deployment for platform telemetry stores bearer tokens insecurely. The correction is to ____. Case 4036: `structuredContent` missing despite `outputSchema` declared. [2.5 #34]

- **A.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **B.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **C.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **D.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**

### 35. At AtlasCloud Platform Ops, engineers building an MCP server for platform telemetry need to ____. Which configuration correctly implements the MCP specification? Ticket 5360: `roots/list` poll floods client every 10 ms. [2.5 #35]

- **A.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **B.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **C.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **D.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request

### 36. Which three statements accurately describe MCP platform telemetry transport and security semantics for AtlasCloud Platform Ops? Select three. Ticket 9313: plaintext `config.json` holds refresh token. [2.6 #36]

- **A.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **B.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **C.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)
- **D.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **E.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **F.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent

### 37. AtlasCloud Platform Ops observes its platform telemetry MCP server failing `tools/call` with `Invalid params -32602`. The fix is to ____. Case 6288: `structuredContent` missing despite `outputSchema` declared. [2.6 #37]

- **A.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **B.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **C.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **D.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs

### 38. The MCP Inspector highlights `____` as missing for platform telemetry at AtlasCloud Platform Ops. Which completion is spec-correct? Ticket 5060: plaintext `config.json` holds refresh token. [2.6 #38]

- **A.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **B.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **C.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **D.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change

---

## Domain 3 — Prompts, Sampling, Roots & Elicitation (14–18% blueprint weight · 16 questions)

### 39. AtlasCloud Platform Ops MCP server for platform telemetry requires two valid security hardening steps. Which two should you apply? Select two. Incident 5281: OAuth PKCE verifier omitted for public client. [3.1 #39]

- **A.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **B.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **C.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **D.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **E.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`

### 40. Proposed solution: grant admin:write scope to every read-only docs search server by default is suggested for platform telemetry at AtlasCloud Platform Ops. Does this meet the goal? Log 6887: `prompt/get` uses client-side interpolation without validation. [3.1 #40]

- **A.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **B.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **C.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **D.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects

### 41. AtlasCloud Platform Ops needs to bound platform telemetry sampling loops that fan out recursively. Which limit is appropriate? Log 1069: `initialize` skipped before `tools/list`. [3.1 #41]

- **A.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification
- **B.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **C.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **D.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`

### 42. During platform telemetry at AtlasCloud Platform Ops, the MCP server responds with SSE without `eventId`. Which correction is required? Log 5560: `prompt/get` uses client-side interpolation without validation. [3.2 #42]

- **A.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **B.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **C.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **D.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`

### 43. For AtlasCloud Platform Ops platform telemetry server to advertise new capabilities after a deploy, the correct notification is ____. Alert 7334: `isError:false` with HTML error page masks failure. [3.2 #43]

- **A.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **B.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds
- **C.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **D.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`

### 44. At AtlasCloud Platform Ops, platform telemetry MCP tool descriptions are concatenated into system prompts. Which safeguard is needed? Alert 5369: `isError:false` with HTML error page masks failure. [3.2 #44]

- **A.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **B.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **C.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **D.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`

### 45. To implement platform telemetry correctly for AtlasCloud Platform Ops, which 4-step sequence satisfies the MCP spec? Trace 4074: `resource` audience binding missing per RFC 8707. Scenario 3.3-3-45.

- **A.** Server advertises sampling need → checks client `sampling` capability → sends `sampling/createMessage` with `messages`, `maxTokens`, `modelPreferences` → client applies human-in-loop gating & returns generation
- **B.** Client exposes sampling by default without opt-in → server loops sampling/createMessage recursively → ignore modelPreferences hints → return raw chain-of-thought as tool output
- **C.** Server mixes sampling messages into tool descriptions → client forwards without isolation → skip cost tracking → cache sampling results as facts
- **D.** Server sends sampling without capability check → include raw customer PII in messages → skip maxTokens limits → client auto-executes without user consent

### 46. Two statements about MCP platform telemetry correctly reflect the specification for AtlasCloud Platform Ops. Which two are true? Select two. Review 1645: sampling loop lacks depth cap and cost budget. [3.3 #46]

- **A.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **B.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **C.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **D.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`
- **E.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions

### 47. AtlasCloud Platform Ops wants its MCP server to support both local and remote clients for platform telemetry. The architecture should ____. Case 5072: registry installs via `curl¦bash` without signature check. [3.3 #47]

- **A.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`
- **B.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **C.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **D.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`

### 48. For platform telemetry at AtlasCloud Platform Ops, two MCP primitives are required to enable the scenario. Which two are needed? Select two. Audit 4820: `includeContext=allServers` exfiltrates cross-server data. [3.4 #48]

- **A.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **B.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **C.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **D.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`
- **E.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them

### 49. For platform telemetry at AtlasCloud Platform Ops, the MCP Inspector UI must validate tool schemas. Which approach is correct? Log entry 3119 shows `Method not found -32601` without capability check. [3.4 #49]

- **A.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **B.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **C.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **D.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks

### 50. During platform telemetry at AtlasCloud Platform Ops, the MCP server responds with SSE without `eventId`. Which correction is required? Case 9378: `structuredContent` missing despite `outputSchema` declared. [3.4 #50]

- **A.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **B.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **C.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **D.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`

### 51. For AtlasCloud Platform Ops platform telemetry server to advertise new capabilities after a deploy, the correct notification is ____. Incident 4979: deprecated `/sse` + `/messages` split endpoint still in prod. [3.5 #51]

- **A.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **B.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)
- **C.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **D.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets

### 52. AtlasCloud Platform Ops sees its platform telemetry MCP tool return large binary blobs inline. The spec-compliant return is to ____. Trace 8299: batch of 200 tool calls timed out. [3.5 #52]

- **A.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **B.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **C.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **D.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage

### 53. For platform telemetry, AtlasCloud Platform Ops must choose between stdio and Streamable HTTP transports. The correct choice is to ____. Log 7771: `initialize` skipped before `tools/list`. [3.6 #53]

- **A.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean
- **B.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets
- **C.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **D.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`

### 54. In `AtlasCloud Platform Ops` `platform telemetry` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Log 8564: `initialize` skipped before `tools/list`. [3.6 #54]

- **A.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **B.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **C.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **D.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request

---

## Domain 4 — Transports, Sessions & Protocol Evolution (14–18% blueprint weight · 16 questions)

### 55. For platform telemetry at AtlasCloud Platform Ops, two MCP primitives are required to enable the scenario. Which two are needed? Select two. Incident 8249: tool logic changed post-approval (rug-pull) undetected. [4.1 #55]

- **A.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **B.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **C.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **D.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)
- **E.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads

### 56. When AtlasCloud Platform Ops connects its VS Code host to an MCP server for platform telemetry, the `roots/list` workflow should ____. Alert 8727: `progressToken` mismatch across concurrent tool calls. [4.1 #56]

- **A.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **B.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **C.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **D.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke

### 57. Proposed solution: To handle platform telemetry, AtlasCloud Platform Ops plans to embed static client_secret inside the shipped desktop binary for all tenants. Does this satisfy the MCP specification? Review 3890 notes `resources/list_changed` never fired after ingest. [4.1 #57]

- **A.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **B.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **C.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **D.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure

### 58. AtlasCloud Platform Ops handles platform telemetry via MCP sampling delegation. To enforce least privilege, the server should ____. Trace 6149: 200-tool batch exceeds advertised `maxBatchSize`. [4.2 #58]

- **A.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`
- **B.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **C.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **D.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets

### 59. During platform telemetry incident triage at AtlasCloud Platform Ops, audit logs lack `requestId` correlation. The correction is to ____. Incident 8948: deprecated `/sse` + `/messages` split endpoint still in prod. [4.2 #59]

- **A.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **B.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)
- **C.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **D.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation

### 60. At AtlasCloud Platform Ops, platform telemetry MCP gateway logs show `Last-Event-ID` replay gaps. The team should ____. Log 4681: `prompt/get` uses client-side interpolation without validation. [4.2 #60]

- **A.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **B.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **C.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **D.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`

### 61. For platform telemetry at AtlasCloud Platform Ops, two best practices align with MCP 2025-11-25. Which two should be implemented? Select two. Ticket 7230: plaintext `config.json` holds refresh token. [4.3 #61]

- **A.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **B.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **C.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **D.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **E.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`

### 62. In `AtlasCloud Platform Ops` `platform telemetry` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Review 1275: `outputSchema` mismatched to `structuredContent` shape. [4.3 #62]

- **A.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **B.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **C.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **D.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification

### 63. Proposed solution: To handle platform telemetry, AtlasCloud Platform Ops plans to hardcode protocolVersion to 2024-11-05 forever and ignore server capability updates. Does this satisfy the MCP specification? Case 6490: registry installs via `curl¦bash` without signature check. [4.3 #63]

- **A.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **B.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **C.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **D.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways

### 64. A third-party platform telemetry MCP server at AtlasCloud Platform Ops silently changes tool logic after approval. The defense is to ____. Incident MCP-2026-9500 shows Misconfigured `Mcp-Session-Id` routing. [4.4 #64]

- **A.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **B.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **C.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **D.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent

### 65. The AtlasCloud Platform Ops MCP configuration for platform telemetry shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Review 4762: sampling loop lacks depth cap and cost budget. [4.4 #65]

- **A.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **B.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **C.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **D.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle

### 66. For platform telemetry at AtlasCloud Platform Ops, the client must handle `resources/subscribe` vs polling. Which is efficient? Trace 2549: 200-tool batch exceeds advertised `maxBatchSize`. [4.4 #66]

- **A.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean
- **B.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **C.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **D.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds

### 67. AtlasCloud Platform Ops platform telemetry MCP `initialize` handshake omits `capabilities`. The next step is to ____. Case 3454: Host passes full env block to untrusted calendar server. [4.5 #67]

- **A.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **B.** Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation
- **C.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **D.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets

### 68. At AtlasCloud Platform Ops, platform telemetry MCP tool descriptions are concatenated into system prompts. Which safeguard is needed? Review 5151 notes `resources/list_changed` never fired after ingest. [4.5 #68]

- **A.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **B.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **C.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **D.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`

### 69. For platform telemetry at AtlasCloud Platform Ops, which ordered flow correctly implements the MCP 2025-11-25 requirement? Ticket 3745 reports `Last-Event-ID` replay mismatch after gateway restart. Scenario 4.6-3-69.

- **A.** Client POSTs JSON-RPC to single `mcp` endpoint with `Content-Type: application/json` & `Accept: text/event-stream, application/json` → server may respond with single JSON or SSE stream → client honors `Mcp-Session-Id` & `Last-Event-ID` for resumability
- **B.** Client sends batched 100 requests without server batch ack → server streams without event IDs → skip session expiry handling → leak session IDs across tenants
- **C.** Server returns 200 OK with HTML error page → client retries without backoff → disable idempotency on non-idempotent tool calls → omit Content-Type validation
- **D.** Client opens separate GET /sse and POST /message SSE endpoints → send JSON without Accept header → ignore Mcp-Session-Id → close stream after each chunk without Last-Event-ID

### 70. In `AtlasCloud Platform Ops` `platform telemetry` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Alert 7490: `isError:false` with HTML error page masks failure. [4.6 #70]

- **A.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **B.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`
- **C.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **D.** Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation

---

## Domain 5 — Authorization, Security, Trust & Registry (13–17% blueprint weight · 15 questions)

### 71. Which three statements accurately describe MCP platform telemetry transport and security semantics for AtlasCloud Platform Ops? Select three. Alert 3777: `isError:false` with HTML error page masks failure. [5.1 #71]

- **A.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **B.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **C.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **D.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **E.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **F.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification

### 72. An external auditor flags that AtlasCloud Platform Ops MCP deployment for platform telemetry stores bearer tokens insecurely. The correction is to ____. Ticket 6328 reports `Last-Event-ID` replay mismatch after gateway restart. [5.1 #72]

- **A.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds
- **B.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **C.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`
- **D.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414

### 73. AtlasCloud Platform Ops MCP server for platform telemetry uses static API keys in `Authorization`. The OAuth 2.1 migration is to ____. Log 1101: `initialize` skipped before `tools/list`. [5.1 #73]

- **A.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **B.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **C.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **D.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure

### 74. A platform telemetry MCP extension at AtlasCloud Platform Ops leaks `Mcp-Session-Id` across tenants. The team must ____. Case 1172: Host passes full env block to untrusted calendar server. [5.2 #74]

- **A.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **B.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **C.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **D.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks

### 75. In `AtlasCloud Platform Ops` `platform telemetry` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Ticket 1380: `roots/list` poll floods client every 10 ms. [5.2 #75]

- **A.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **B.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs
- **C.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **D.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`

### 76. Proposed solution: AtlasCloud Platform Ops will embed static client_secret inside the shipped desktop binary for all tenants for platform telemetry. Does this meet the MCP 2025-11-25 goal? Alert 2381: `Mcp-Session-Id` reused across tenants. [5.2 #76]

- **A.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **B.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **C.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **D.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`

### 77. AtlasCloud Platform Ops must fix its platform telemetry MCP integration. Which two changes bring it into spec compliance? Select two. Log 5579: `prompt/get` uses client-side interpolation without validation. [5.3 #77]

- **A.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **B.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **C.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **D.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **E.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**

### 78. AtlasCloud Platform Ops sees its platform telemetry MCP tool return large binary blobs inline. The spec-compliant return is to ____. Alert 6575: `Mcp-Session-Id` reused across tenants. [5.3 #78]

- **A.** Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation
- **B.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **C.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **D.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions

### 79. The MCP Inspector highlights `____` as missing for platform telemetry at AtlasCloud Platform Ops. Which completion is spec-correct? Case 4220: `structuredContent` missing despite `outputSchema` declared. [5.3 #79]

- **A.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **B.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **C.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **D.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)

### 80. AtlasCloud Platform Ops wants to bridge platform telemetry MCP tools into an A2A task mesh. The correct layer definition is ____. Ticket 8348: `roots/list` poll floods client every 10 ms. [5.4 #80]

- **A.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **B.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **C.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **D.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603

### 81. AtlasCloud Platform Ops platform telemetry MCP `initialize` handshake omits `capabilities`. The next step is to ____. Log 8247: `prompt/get` uses client-side interpolation without validation. [5.4 #81]

- **A.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **B.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **C.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **D.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token

### 82. AtlasCloud Platform Ops wants platform telemetry MCP completions for enum arguments. The valid method is ____. Ticket 2451: `notifications/roots/list_changed` ignored after folder add. [5.4 #82]

- **A.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **B.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **C.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **D.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails

### 83. What is the correct 4-step order for platform telemetry workflow at AtlasCloud Platform Ops under MCP 2025-11-25? Ticket 4535: plaintext `config.json` holds refresh token. Scenario 5.5-3-83.

- **A.** Server embeds client_secret in JS bundle → disable PKCE as optional → return tokens over plain HTTP → cache discovery doc forever without TLS
- **B.** Server exposes `/.well-known/oauth-authorization-server` with PRM & CIMD → client fetches RS metadata with `resource` indicator (RFC 8707) → PKCE + state + RFC 9207 iss validation → audience-bound token issued per resource server
- **C.** Client trusts token from any issuer → skip RFC 9207 iss equality check → ignore RFC 7591 dynamic registration → reuse single token across all resource servers
- **D.** Client sends static API key in Authorization header → server skips issuer discovery → accept tokens with alg:none → grant org-admin scope by default

### 84. AtlasCloud Platform Ops wants platform telemetry MCP completions for enum arguments. The valid method is ____. Ticket 9181: `notifications/roots/list_changed` ignored after folder add. [5.5 #84] using Helm chart provenance (variant delta 606).

- **A.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **B.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **C.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)
- **D.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping

### 85. AtlasCloud Platform Ops needs to secure platform telemetry tool calls that mutate production data. The right control is to ____. Alert 9982: `progressToken` mismatch across concurrent tool calls. [5.5 #85]

- **A.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **B.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **C.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **D.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)

---

## Domain 6 — SDKs, Deployment, Observability & Ecosystem (13–17% blueprint weight · 15 questions)

### 86. AtlasCloud Platform Ops needs to secure platform telemetry tool calls that mutate production data. The right control is to ____. Case 6532: Host passes full env block to untrusted calendar server. [6.1 #86]

- **A.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **B.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **C.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **D.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`

### 87. AtlasCloud Platform Ops needs to bound platform telemetry sampling loops that fan out recursively. Which limit is appropriate? Trace 7652 reveals truncated cursor pagination at 50 entries. [6.1 #87]

- **A.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **B.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **C.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **D.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions

### 88. In `AtlasCloud Platform Ops` `platform telemetry` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Review 2785: `outputSchema` mismatched to `structuredContent` shape. [6.1 #88] using Vault KV v2 unseal (variant delta 990).

- **A.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **B.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **C.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **D.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token

### 89. The AtlasCloud Platform Ops MCP configuration for platform telemetry shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Audit 7648: `includeContext=allServers` exfiltrates cross-server data. [6.2 #89]

- **A.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **B.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **C.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **D.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them

### 90. A AtlasCloud MCP client for platform telemetry must ____ to satisfy the protocol. What is the correct implementation approach? Audit 3441: auto-approve bypasses human consent for destructive tool. [6.2 #90]

- **A.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **B.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **C.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)
- **D.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**

### 91. The AtlasCloud Platform Ops MCP configuration for platform telemetry shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Case 3431: Host passes full env block to untrusted calendar server. [6.2 #91]

- **A.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **B.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively
- **C.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **D.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan

### 92. The AtlasCloud Platform Ops team documents the platform telemetry MCP flow. Which sequence of actions is spec-compliant? Trace 9608: batch of 200 tool calls timed out. Scenario 6.3-3-92.

- **A.** Install random GitHub MCP servers via curl|bash → grant full filesystem + network + env scopes → disable log redaction → store tokens in plaintext
- **B.** Exfiltrate tool arguments to third-party analytics silently → skip rate limiting on tool calls → omit provenance tags → hide tool calls from audit UI
- **C.** Pin server versions & verify registry signatures → isolate tool descriptions from executable logic → prompt user before first tool approval & high-risk actions → log tool provenance & monitor for description drift
- **D.** Auto-approve all tools without review → trust tool description text as system prompt → allow server to change tool logic post-approval → skip signature verification

### 93. Three best practices for platform telemetry under MCP 2025-11-25 apply to AtlasCloud Platform Ops. Which three should be chosen? Select three. Incident 2285: OAuth PKCE verifier omitted for public client. [6.3 #93]

- **A.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **B.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification
- **C.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)
- **D.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **E.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **F.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping

### 94. The AtlasCloud Platform Ops MCP configuration for platform telemetry shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Review 8909: sampling loop lacks depth cap and cost budget. [6.3 #94] via Temporal workflow replay (variant delta 682). through Crossplane composition (variant gamma 874).

- **A.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **B.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **C.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure
- **D.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`

### 95. For platform telemetry at AtlasCloud Platform Ops, two MCP primitives are required to enable the scenario. Which two are needed? Select two. Case 9835: Host passes full env block to untrusted calendar server. [6.4 #95]

- **A.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **B.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **C.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **D.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)
- **E.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation

### 96. The AtlasCloud Platform Ops MCP configuration for platform telemetry shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Review 8340 notes `resources/list_changed` never fired after ingest. [6.4 #96]

- **A.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **B.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **C.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **D.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change

### 97. For platform telemetry, AtlasCloud Platform Ops must handle `notifications/progress` vs polling. The correct pattern is to ____. Incident 9383: deprecated `/sse` + `/messages` split endpoint still in prod. [6.4 #97]

- **A.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively
- **B.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)
- **C.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **D.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)

### 98. AtlasCloud Platform Ops engineers designing an MCP system for platform telemetry must evaluate two correct controls. Which two statements are correct? Select two. Alert 9006: `progressToken` mismatch across concurrent tool calls. [6.5 #98]

- **A.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **B.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **C.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively
- **D.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **E.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side

### 99. AtlasCloud Platform Ops wants its MCP server to support both local and remote clients for platform telemetry. The architecture should ____. Alert 5328: `progressToken` mismatch across concurrent tool calls. [6.5 #99]

- **A.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **B.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **C.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **D.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`

### 100. In AtlasCloud Platform Ops production, an MCP server for platform telemetry must ____ to prevent tool poisoning attacks. Ticket 5242: plaintext `config.json` holds refresh token. [6.5 #100]

- **A.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **B.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **C.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **D.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle

---

## Answer Key and Explanations

### Question 1 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). Selecting this honors Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 1.1 validation S3Q001. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **B:** Incorrect. parsing free-form chat replies as structured data instead of typed elicitation invites format errors and injection.
- **C:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.
- **D:** Correct. correctly separates trust boundaries: Hosts own UI/policy, Clients speak MCP, Servers expose capabilities behind capability negotiation.

### Question 2 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). Per MCP 2025-11-25, Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model ensures spec-compliant lifecycle and isolation for platform telemetry. Skill 1.1 validation S3Q002. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **B:** Correct. maps transport to deployment topology: stdio gives OS-level isolation locally; Streamable HTTP enables remote multi-tenant scale.
- **C:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **D:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.

### Question 3 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). This follows the MCP specification for Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model, correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 1.1 validation S3Q003. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **B:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.
- **C:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.
- **D:** Correct. maps transport to deployment topology: stdio gives OS-level isolation locally; Streamable HTTP enables remote multi-tenant scale.

### Question 4 — `B, C` (MCP Foundations, Architecture & Lifecycle)

Correct answers: B and C (are correct). Per MCP 2025-11-25, Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake ensures spec-compliant lifecycle and isolation for platform telemetry. Skill 1.2 validation S3Q004. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.
- **B:** Correct. lets each party call only negotiated features, avoiding methodNotFound and silent fallback hallucinations.
- **C:** Correct. provides spec-guaranteed failure detection where OS TCP keepalives are invisible to application-level SSE/stdio proxies.
- **D:** Incorrect. treating MCP as a replacement for A2A agent discovery and task lifecycles conflates vertical tool attachment with peer delegation.
- **E:** Incorrect. skipping Inspector and relying only on unit mocks misses real transport framing and pagination/cancellation bugs.

### Question 5 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). MCP 2025-11-25 requires Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake; the alternative breaks capability negotiation or security for platform telemetry. Skill 1.2 validation S3Q005. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **B:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **C:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.
- **D:** Correct. guarantees version and capability compatibility before feature calls, satisfying the MCP lifecycle invariant.

### Question 6 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). Selecting this honors Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 1.2 validation S3Q006. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.
- **B:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **C:** Correct. enables forwards-compatible evolution without breaking older Hosts or Servers on version skew.
- **D:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.

### Question 7 — `B, D` (MCP Foundations, Architecture & Lifecycle)

Correct answers: B and D (are correct). This follows the MCP specification for Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy, correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 1.3 validation S3Q007. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Incorrect. batching 200 unrelated tool calls into one HTTP request beyond advertised limits times out the whole batch.
- **B:** Correct. separates best-effort telemetry from correlated RPC state per JSON-RPC 2.0, preventing notification ID collisions.
- **C:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **D:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.
- **E:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.

### Question 8 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). Selecting this honors Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 1.3 validation S3Q008. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.
- **B:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.
- **C:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **D:** Correct. provides spec-guaranteed failure detection where OS TCP keepalives are invisible to application-level SSE/stdio proxies.

### Question 9 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). Per MCP 2025-11-25, Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy ensures spec-compliant lifecycle and isolation for platform telemetry. Skill 1.3 validation S3Q009. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **B:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.
- **C:** Incorrect. distributing servers as raw GitHub tarballs without server.json or publisher proof hides supply-chain compromise.
- **D:** Correct. separates best-effort telemetry from correlated RPC state per JSON-RPC 2.0, preventing notification ID collisions.

### Question 10 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). MCP 2025-11-25 requires Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging); the alternative breaks capability negotiation or security for platform telemetry. Reference 1.4 S3Q010. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Incorrect. hardcoding protocol versions and duplicate initialize pings breaks forward compatibility and lifecycle idempotency.
- **B:** Incorrect. reversing the initialize direction and mixing OAuth into initialize params conflates lifecycle with authorization.
- **C:** Correct. follows MCP lifecycle spec: version/capability negotiation via initialize exchange completed by initialized notification before any feature calls.
- **D:** Incorrect. invoking tools before initialize negotiation bypasses version checks and omits the required initialized signal.

### Question 11 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). MCP 2025-11-25 requires Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging); the alternative breaks capability negotiation or security for platform telemetry. Skill 1.4 validation S3Q011. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.
- **B:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.
- **C:** Correct. allows safe iteration on draft specs like Tasks and elicitation without polluting the stable capability surface.
- **D:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.

### Question 12 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). This choice correctly implements Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 1.4 validation S3Q012. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Correct. lets each party call only negotiated features, avoiding methodNotFound and silent fallback hallucinations.
- **B:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.
- **C:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **D:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.

### Question 13 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). Selecting this honors Manage keepalive pings, progress notifications, cancellation, and shutdown semantics and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 1.5 validation S3Q013. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. provides spec-guaranteed failure detection where OS TCP keepalives are invisible to application-level SSE/stdio proxies.
- **B:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.
- **C:** Incorrect. enabling experimental tasks by default without capability checks forces unready clients into breaking draft methods.
- **D:** Incorrect. calling tools before the initialized handshake completes races capability discovery and throws methodNotFound errors.

### Question 14 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). Selecting this honors Manage keepalive pings, progress notifications, cancellation, and shutdown semantics and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 1.5 validation S3Q014. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **B:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **C:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.
- **D:** Correct. gracefully aborts model-driven tool storms while freeing server resources and meeting JSON-RPC cancellation semantics.

### Question 15 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). This choice correctly implements Manage keepalive pings, progress notifications, cancellation, and shutdown semantics for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 1.5 validation S3Q015. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. survives AWS ALB 60s idle timeout and Kubernetes GFE that silently drops idle SSE streams.
- **B:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **C:** Incorrect. collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.
- **D:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.

### Question 16 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). Selecting this honors Differentiate MCP from function calling, A2A, and experimental capability progression and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Reference 1.6 S3Q016. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Incorrect. ad-hoc tool creation without validation and massive single-block responses break type safety and token budgets.
- **B:** Incorrect. missing inputSchema and raw shell interpolation from unvalidated LLM strings creates prompt-injection and RCE risk.
- **C:** Correct. matches MCP Tools spec: declarative schema, client discovery, validated execution, and structured content/error signaling.
- **D:** Incorrect. responding before validation and ignoring list_changed events leaves clients with stale, unvalidated tool catalogs.

### Question 17 — `C, E` (MCP Foundations, Architecture & Lifecycle)

Correct answers: C and E (are correct). This choice correctly implements Differentiate MCP from function calling, A2A, and experimental capability progression for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 1.6 validation S3Q017. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.
- **B:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.
- **C:** Correct. allows safe iteration on draft specs like Tasks and elicitation without polluting the stable capability surface.
- **D:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.
- **E:** Correct. clarifies layer boundaries: MCP standardizes context attachment; function calling is inline model schema; A2A negotiates task handoffs.

### Question 18 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). This follows the MCP specification for Differentiate MCP from function calling, A2A, and experimental capability progression, correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 1.6 validation S3Q018. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.
- **B:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **C:** Correct. clarifies layer boundaries: MCP standardizes context attachment; function calling is inline model schema; A2A negotiates task handoffs.
- **D:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.

### Question 19 — `C, E` (Tools, Resources & Resource Templates)

Correct answers: C and E (are correct). Selecting this honors Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 2.1 validation S3Q019. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.
- **B:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **C:** Correct. uses typed server helpers that auto-wire tools/list/call handlers and JSON Schema validation from Zod objects.
- **D:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **E:** Correct. signals cost/safety posture without hard-coding policy; models prefer readOnly before destructive in multi-step plans.

### Question 20 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). This choice correctly implements Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 2.1 validation S3Q020. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **B:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.
- **C:** Correct. gives models complete, machine-validated contracts for tool selection and argument generation.
- **D:** Incorrect. parsing free-form chat replies as structured data instead of typed elicitation invites format errors and injection.

### Question 21 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). Per MCP 2025-11-25, Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints ensures spec-compliant lifecycle and isolation for platform telemetry. Skill 2.1 validation S3Q021. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. preserves user/model agency and auditability; every mutation traces to an explicit model decision with tool audit event.
- **B:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **C:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.
- **D:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.

### Question 22 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Selecting this honors Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 2.1 validation S3Q022. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.
- **B:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **C:** Correct. signals cost/safety posture without hard-coding policy; models prefer readOnly before destructive in multi-step plans.
- **D:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.

### Question 23 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). This follows the MCP specification for Control model-controlled tool execution, list discovery, validation, and structured content output, correcting the insecure/incompatible anti-pattern for platform telemetry. Reference 2.2 S3Q023. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. omitting uri and mimeType fields and ignoring pagination cursors makes resources unaddressable and unfilterable.
- **B:** Correct. follows Resources spec: capability advertisement, list/template discovery, uri-addressed reads with mime-typed contents and pagination.
- **C:** Incorrect. guessing URIs and exposing raw OS paths without scheme checks violates resource discovery and isolation.
- **D:** Incorrect. tight polling without subscription to list_changed notifications defeats MCP push efficiency and protocol layering.

### Question 24 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). This follows the MCP specification for Control model-controlled tool execution, list discovery, validation, and structured content output, correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 2.2 validation S3Q024. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.
- **B:** Correct. bridges LLM reasoning with downstream code that consumes validated JSON, not regex scraped prose.
- **C:** Incorrect. assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.
- **D:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.

### Question 25 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). MCP 2025-11-25 requires Control model-controlled tool execution, list discovery, validation, and structured content output; the alternative breaks capability negotiation or security for platform telemetry. Skill 2.2 validation S3Q025. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.
- **B:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.
- **C:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.
- **D:** Correct. lets clients render multimodal results safely while distinguishing success from app-level errors without parsing text.

### Question 26 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). This choice correctly implements Control model-controlled tool execution, list discovery, validation, and structured content output for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 2.2 validation S3Q026. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Correct. defends against LLM hallucinated args and preserves typed error handling via isError flag versus exception propagation.
- **B:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **C:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.
- **D:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.

### Question 27 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). MCP 2025-11-25 requires Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed; the alternative breaks capability negotiation or security for platform telemetry. Skill 2.3 validation S3Q027. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **B:** Correct. enables complete catalog sync for hosts that cache tool lists and paginate beyond 50 items without omission.
- **C:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.
- **D:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.

### Question 28 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Per MCP 2025-11-25, Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed ensures spec-compliant lifecycle and isolation for platform telemetry. Skill 2.3 validation S3Q028. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **B:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.
- **C:** Correct. keeps prompt pickers fresh without re-listing on every keystroke, matching resource/tool change notification pattern.
- **D:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.

### Question 29 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). Per MCP 2025-11-25, Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed ensures spec-compliant lifecycle and isolation for platform telemetry. Skill 2.3 validation S3Q029. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.
- **B:** Correct. handles 10k-file workspaces without truncation or timeout, matching MCP pagination contract for both lists.
- **C:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.
- **D:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.

### Question 30 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). This choice correctly implements Address direct resources vs templated resources with URI schemes, names, and mimeTypes for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Reference 2.4 S3Q030. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. letting servers dictate client filesystem boundaries inverts MCP trust and breaks host isolation.
- **B:** Incorrect. hardcoding roots and ignoring list_changed notifications leaves stale boundaries after user permission changes.
- **C:** Incorrect. exposing full drive without consent and walking above root boundaries with symlink following enables directory traversal.
- **D:** Correct. implements Roots spec: client-owned boundary declaration, server-enforced confinement, and dynamic list_changed handling.

### Question 31 — `A, E` (Tools, Resources & Resource Templates)

Correct answers: A and E (are correct). Selecting this honors Address direct resources vs templated resources with URI schemes, names, and mimeTypes and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 2.4 validation S3Q031. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. signals cost/safety posture without hard-coding policy; models prefer readOnly before destructive in multi-step plans.
- **B:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.
- **C:** Incorrect. deploying greenfield on the deprecated dual-endpoint SSE transport incurs future migration cost and lacks session IDs.
- **D:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **E:** Correct. delivers typed content blocks that render correctly in Host UIs with binary vs text handling pre-decided by mimeType.

### Question 32 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). MCP 2025-11-25 requires Address direct resources vs templated resources with URI schemes, names, and mimeTypes; the alternative breaks capability negotiation or security for platform telemetry. Skill 2.4 validation S3Q032. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.
- **B:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.
- **C:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.
- **D:** Correct. provides stable, scheme-scoped addressing that survives renames and scopes authZ per resource origin.

### Question 33 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). Per MCP 2025-11-25, Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows ensures spec-compliant lifecycle and isolation for platform telemetry. Skill 2.5 validation S3Q033. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **B:** Correct. handles 10k-file workspaces without truncation or timeout, matching MCP pagination contract for both lists.
- **C:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.
- **D:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.

### Question 34 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). This choice correctly implements Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 2.5 validation S3Q034. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.
- **B:** Correct. pushes freshness efficiently after external ingestion jobs create new datasets, without constant re-list overhead.
- **C:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.
- **D:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.

### Question 35 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). This follows the MCP specification for Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows, correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 2.5 validation S3Q035. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.
- **B:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.
- **C:** Correct. pushes freshness efficiently after external ingestion jobs create new datasets, without constant re-list overhead.
- **D:** Incorrect. generating random progressTokens server-side with no binding to request id mixes streams across concurrent tasks.

### Question 36 — `A, B, E` (Tools, Resources & Resource Templates)

Correct answers: A, B, and E (are correct). This choice correctly implements Declare prompts and completions for argument typeahead and parameterized prompt expansion for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 2.6 validation S3Q036. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. powers low-latency autocomplete dropdowns directly from server-side datasets without tool execution overhead.
- **B:** Correct. turns curated prompt packs into discoverable UX shortcuts argument-by-argument with typed validation.
- **C:** Incorrect. installing random `curl | bash` MCP servers without registry signature verification imports unvetted RCE into the IDE.
- **D:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.
- **E:** Correct. keeps prompt pickers fresh without re-listing on every keystroke, matching resource/tool change notification pattern.
- **F:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.

### Question 37 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Per MCP 2025-11-25, Declare prompts and completions for argument typeahead and parameterized prompt expansion ensures spec-compliant lifecycle and isolation for platform telemetry. Skill 2.6 validation S3Q037. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **B:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.
- **C:** Correct. turns curated prompt packs into discoverable UX shortcuts argument-by-argument with typed validation.
- **D:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.

### Question 38 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Selecting this honors Declare prompts and completions for argument typeahead and parameterized prompt expansion and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 2.6 validation S3Q038. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **B:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **C:** Correct. powers low-latency autocomplete dropdowns directly from server-side datasets without tool execution overhead.
- **D:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.

### Question 39 — `C, E` (Prompts, Sampling, Roots & Elicitation)

Correct answers: C and E (are correct). MCP 2025-11-25 requires Expose and expand prompts via prompts/list, prompts/get, and argument validation; the alternative breaks capability negotiation or security for platform telemetry. Skill 3.1 validation S3Q039. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **B:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **C:** Correct. compiles parameterized prompt templates server-side with validated args, keeping prompt injection surface server-controlled.
- **D:** Incorrect. labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.
- **E:** Correct. powers low-latency autocomplete dropdowns directly from server-side datasets without tool execution overhead.

### Question 40 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). This choice correctly implements Expose and expand prompts via prompts/list, prompts/get, and argument validation for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 3.1 validation S3Q040. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.
- **B:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **C:** Correct. keeps prompt pickers fresh without re-listing on every keystroke, matching resource/tool change notification pattern.
- **D:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.

### Question 41 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). MCP 2025-11-25 requires Expose and expand prompts via prompts/list, prompts/get, and argument validation; the alternative breaks capability negotiation or security for platform telemetry. Skill 3.1 validation S3Q041. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. distributing servers as raw GitHub tarballs without server.json or publisher proof hides supply-chain compromise.
- **B:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **C:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **D:** Correct. powers low-latency autocomplete dropdowns directly from server-side datasets without tool execution overhead.

### Question 42 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). This choice correctly implements Enforce client-owned filesystem boundaries via roots/list and roots/list_changed for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 3.2 validation S3Q042. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.
- **B:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **C:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.
- **D:** Correct. gives users explicit allowlist control over which directories a server may touch, enforced server-side.

### Question 43 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). This follows the MCP specification for Enforce client-owned filesystem boundaries via roots/list and roots/list_changed, correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 3.2 validation S3Q043. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **B:** Incorrect. reimplementing a Postgres MCP server from scratch when a registry-verified one already exists wastes review cycles.
- **C:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.
- **D:** Correct. prevents `../` and symlink hop attacks that would escape the user’s approved `file://` allowlist.

### Question 44 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). MCP 2025-11-25 requires Enforce client-owned filesystem boundaries via roots/list and roots/list_changed; the alternative breaks capability negotiation or security for platform telemetry. Skill 3.2 validation S3Q044. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.
- **B:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.
- **C:** Correct. prevents `../` and symlink hop attacks that would escape the user’s approved `file://` allowlist.
- **D:** Incorrect. setting includeContext=allServers by default fans sensitive data from every connected server into one sampling call.

### Question 45 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). Per MCP 2025-11-25, Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls ensures spec-compliant lifecycle and isolation for platform telemetry. Reference 3.3 S3Q045. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. follows Sampling spec: capability-checked server-initiated LLM delegation with explicit modelPreferences and human approval gating.
- **B:** Incorrect. default-exposed sampling and uncapped recursive loops risk token runaway and expose internal reasoning inappropriately.
- **C:** Incorrect. confusing sampling payloads with tool metadata conflates delegation layers and breaks cost attribution.
- **D:** Incorrect. unbounded PII-laden sampling without capability or consent bypasses privacy and authorization boundaries.

### Question 46 — `B, D` (Prompts, Sampling, Roots & Elicitation)

Correct answers: B and D (are correct). Per MCP 2025-11-25, Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls ensures spec-compliant lifecycle and isolation for platform telemetry. Skill 3.3 validation S3Q046. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.
- **B:** Correct. maps server intent to Host model fleet tiers without hardcoding vendor model IDs into server code.
- **C:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.
- **D:** Correct. limits what prior server context flows into delegated sampling calls, preventing cross-server data exfiltration.
- **E:** Incorrect. labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.

### Question 47 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). Selecting this honors Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 3.3 validation S3Q047. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. limits what prior server context flows into delegated sampling calls, preventing cross-server data exfiltration.
- **B:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **C:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.
- **D:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.

### Question 48 — `D, E` (Prompts, Sampling, Roots & Elicitation)

Correct answers: D and E (are correct). MCP 2025-11-25 requires Collect human input via elicitation/create with requestedSchema and form round-trips; the alternative breaks capability negotiation or security for platform telemetry. Skill 3.4 validation S3Q048. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.
- **B:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.
- **C:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **D:** Correct. turns server data needs into typed Host-rendered forms rather than chat text parsing, with explicit schema validation.
- **E:** Correct. separates fact acquisition (user-filled forms) from subjective generation (model-composed prose) for audit clarity.

### Question 49 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). This choice correctly implements Collect human input via elicitation/create with requestedSchema and form round-trips for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 3.4 validation S3Q049. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **B:** Correct. separates fact acquisition (user-filled forms) from subjective generation (model-composed prose) for audit clarity.
- **C:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.
- **D:** Incorrect. treating MCP as a replacement for A2A agent discovery and task lifecycles conflates vertical tool attachment with peer delegation.

### Question 50 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). Selecting this honors Collect human input via elicitation/create with requestedSchema and form round-trips and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 3.4 validation S3Q050. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.
- **B:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **C:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.
- **D:** Correct. lets servers delegate LLM sub-tasks (summarization, critique) back to the Host model under explicit preference caps.

### Question 51 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). Per MCP 2025-11-25, Regulate verbosity via logging/setLevel and notifications/message level filtering ensures spec-compliant lifecycle and isolation for platform telemetry. Skill 3.5 validation S3Q051. [Skill 3.5: Regulate verbosity via logging/setLevel and notifications/message level filtering | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/logging/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **B:** Incorrect. installing random `curl | bash` MCP servers without registry signature verification imports unvetted RCE into the IDE.
- **C:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.
- **D:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.

### Question 52 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). Selecting this honors Regulate verbosity via logging/setLevel and notifications/message level filtering and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 3.5 validation S3Q052. [Skill 3.5: Regulate verbosity via logging/setLevel and notifications/message level filtering | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/logging/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.
- **B:** Incorrect. requiring clients to poll list on a timer to detect new resources defeats MCP push efficiency.
- **C:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **D:** Incorrect. assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.

### Question 53 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). MCP 2025-11-25 requires Correlate progress and completion flows with progressToken and completion/complete semantics; the alternative breaks capability negotiation or security for platform telemetry. Skill 3.6 validation S3Q053. [Skill 3.6: Correlate progress and completion flows with progressToken and completion/complete semantics | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/prompts]

- **A:** Incorrect. dumping base64 blobs as plain text without typed content blocks loses mimeType and forces heuristic parsing.
- **B:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.
- **C:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **D:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.

### Question 54 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). Per MCP 2025-11-25, Correlate progress and completion flows with progressToken and completion/complete semantics ensures spec-compliant lifecycle and isolation for platform telemetry. Skill 3.6 validation S3Q054. [Skill 3.6: Correlate progress and completion flows with progressToken and completion/complete semantics | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/prompts]

- **A:** Incorrect. deploying greenfield on the deprecated dual-endpoint SSE transport incurs future migration cost and lacks session IDs.
- **B:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **C:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.
- **D:** Correct. correlates streaming progress notifications to the correct in-flight tool/resource fetch without guessing.

### Question 55 — `B, C` (Transports, Sessions & Protocol Evolution)

Correct answers: B and C (are correct). MCP 2025-11-25 requires Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle; the alternative breaks capability negotiation or security for platform telemetry. Skill 4.1 validation S3Q055. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.
- **B:** Correct. gives OS-level isolation, clean env var scoping, and automatic teardown when Host exits without port conflicts.
- **C:** Correct. prevents log interleaving from corrupting JSON-RPC framing that parsers expect line-delimited on stdout.
- **D:** Incorrect. installing random `curl | bash` MCP servers without registry signature verification imports unvetted RCE into the IDE.
- **E:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.

### Question 56 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). This choice correctly implements Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 4.1 validation S3Q056. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **B:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.
- **C:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.
- **D:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.

### Question 57 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). Selecting this honors Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 4.1 validation S3Q057. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **B:** Correct. gives OS-level isolation, clean env var scoping, and automatic teardown when Host exits without port conflicts.
- **C:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **D:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.

### Question 58 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). This follows the MCP specification for Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response), correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 4.2 validation S3Q058. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.
- **B:** Correct. preserves capability state and pagination cursors after transient network loss without re-initializing.
- **C:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.
- **D:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.

### Question 59 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). Selecting this honors Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 4.2 validation S3Q059. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.
- **B:** Incorrect. logging full tool arguments including customer PII and bearer tokens creates GDPR and credential-leak second-order risks.
- **C:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.
- **D:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.

### Question 60 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). MCP 2025-11-25 requires Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response); the alternative breaks capability negotiation or security for platform telemetry. Skill 4.2 validation S3Q060. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **B:** Correct. lets simple request/reply skip SSE overhead while enabling streaming only for long-running tool progress.
- **C:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **D:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.

### Question 61 — `A, C` (Transports, Sessions & Protocol Evolution)

Correct answers: A and C (are correct). MCP 2025-11-25 requires Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay; the alternative breaks capability negotiation or security for platform telemetry. Skill 4.3 validation S3Q061. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Correct. preserves capability state and pagination cursors after transient network loss without re-initializing.
- **B:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **C:** Correct. recovers progress streams and notifications lost during 5–30s mobile handoffs without missing tool progress events.
- **D:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.
- **E:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.

### Question 62 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). This choice correctly implements Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 4.3 validation S3Q062. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Correct. tracks spec evolution: split GET /sse + POST /messages merged into single POST with Accept-driven streaming.
- **B:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.
- **C:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.
- **D:** Incorrect. distributing servers as raw GitHub tarballs without server.json or publisher proof hides supply-chain compromise.

### Question 63 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). MCP 2025-11-25 requires Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay; the alternative breaks capability negotiation or security for platform telemetry. Skill 4.3 validation S3Q063. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Correct. preserves capability state and pagination cursors after transient network loss without re-initializing.
- **B:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.
- **C:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.
- **D:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.

### Question 64 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). This choice correctly implements Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 4.4 validation S3Q064. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Correct. avoids thundering herds after gateway restarts while ensuring exactly-once progress recovery via resumability.
- **B:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.
- **C:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **D:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.

### Question 65 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). This follows the MCP specification for Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP, correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 4.4 validation S3Q065. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.
- **B:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.
- **C:** Incorrect. labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.
- **D:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.

### Question 66 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). This follows the MCP specification for Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP, correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 4.4 validation S3Q066. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Incorrect. dumping base64 blobs as plain text without typed content blocks loses mimeType and forces heuristic parsing.
- **B:** Correct. tracks spec evolution: split GET /sse + POST /messages merged into single POST with Accept-driven streaming.
- **C:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **D:** Incorrect. reimplementing a Postgres MCP server from scratch when a registry-verified one already exists wastes review cycles.

### Question 67 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). MCP 2025-11-25 requires Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation; the alternative breaks capability negotiation or security for platform telemetry. Skill 4.5 validation S3Q067. [Skill 4.5: Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/progress/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. requiring clients to poll list on a timer to detect new resources defeats MCP push efficiency.
- **B:** Correct. exploits batching for listing throughput without overwhelming server concurrency caps or mixing response IDs.
- **C:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **D:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.

### Question 68 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). This follows the MCP specification for Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation, correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 4.5 validation S3Q068. [Skill 4.5: Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/progress/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **B:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **C:** Correct. keeps MCP semantics intact through enterprise L7 filters that otherwise strip SSE headers and session sticky state.
- **D:** Incorrect. joining user input with path concatenation without canonicalization enables classic directory traversal.

### Question 69 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). Per MCP 2025-11-25, Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival ensures spec-compliant lifecycle and isolation for platform telemetry. Reference 4.6 S3Q069. [Skill 4.6: Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/cancellation/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. matches 2025-11-25 Streamable HTTP spec: single endpoint, dual Accept, session ID management, and resumable SSE stream option.
- **B:** Incorrect. unbounded batching and cross-tenant session ID reuse breaks rate limiting and tenant isolation guarantees.
- **C:** Incorrect. returning HTML instead of JSON-RPC errors and retrying without backoff causes parsing failures and duplicate mutations.
- **D:** Incorrect. splitting endpoints and ignoring session/resumability headers reverts to pre-March 2025 deprecated SSE transport.

### Question 70 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). MCP 2025-11-25 requires Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival; the alternative breaks capability negotiation or security for platform telemetry. Skill 4.6 validation S3Q070. [Skill 4.6: Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/cancellation/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.
- **B:** Incorrect. parsing free-form chat replies as structured data instead of typed elicitation invites format errors and injection.
- **C:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.
- **D:** Correct. exploits batching for listing throughput without overwhelming server concurrency caps or mixing response IDs.

### Question 71 — `C, D, E` (Authorization, Security, Trust & Registry)

Correct answers: C, D, and E (are correct). Selecting this honors Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 5.1 validation S3Q071. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Incorrect. labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.
- **B:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.
- **C:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.
- **D:** Correct. aligns MCP with current OAuth 2.1 security posture, eliminating token leakage vectors of legacy grants.
- **E:** Correct. scales zero-touch onboarding across thousands of tenant Host instances without manual client_id provisioning.
- **F:** Incorrect. distributing servers as raw GitHub tarballs without server.json or publisher proof hides supply-chain compromise.

### Question 72 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). Per MCP 2025-11-25, Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata ensures spec-compliant lifecycle and isolation for platform telemetry. Skill 5.1 validation S3Q072. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Incorrect. reimplementing a Postgres MCP server from scratch when a registry-verified one already exists wastes review cycles.
- **B:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.
- **C:** Incorrect. setting includeContext=allServers by default fans sensitive data from every connected server into one sampling call.
- **D:** Correct. enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.

### Question 73 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). MCP 2025-11-25 requires Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata; the alternative breaks capability negotiation or security for platform telemetry. Skill 5.1 validation S3Q073. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **B:** Correct. scales zero-touch onboarding across thousands of tenant Host instances without manual client_id provisioning.
- **C:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.
- **D:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.

### Question 74 — `A` (Authorization, Security, Trust & Registry)

Correct answer: A (is correct). This choice correctly implements Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 5.2 validation S3Q074. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Correct. keeps refresh tokens survivable across restarts but invisible to process dumps, forked children, and leaked logs.
- **B:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.
- **C:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.
- **D:** Incorrect. treating MCP as a replacement for A2A agent discovery and task lifecycles conflates vertical tool attachment with peer delegation.

### Question 75 — `A` (Authorization, Security, Trust & Registry)

Correct answer: A (is correct). Selecting this honors Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 5.2 validation S3Q075. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Correct. supports desktop IDE/CLI auth via ephemeral loopback listeners while forbidding http redirects to remote hosts.
- **B:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.
- **C:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **D:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.

### Question 76 — `A` (Authorization, Security, Trust & Registry)

Correct answer: A (is correct). This choice correctly implements Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 5.2 validation S3Q076. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Correct. keeps refresh tokens survivable across restarts but invisible to process dumps, forked children, and leaked logs.
- **B:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.
- **C:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.
- **D:** Incorrect. setting includeContext=allServers by default fans sensitive data from every connected server into one sampling call.

### Question 77 — `A, D` (Authorization, Security, Trust & Registry)

Correct answers: A and D (are correct). Per MCP 2025-11-25, Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality ensures spec-compliant lifecycle and isolation for platform telemetry. Skill 5.3 validation S3Q077. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Correct. enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.
- **B:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **C:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.
- **D:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.
- **E:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.

### Question 78 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). This follows the MCP specification for Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality, correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 5.3 validation S3Q078. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Incorrect. batching 200 unrelated tool calls into one HTTP request beyond advertised limits times out the whole batch.
- **B:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **C:** Correct. enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.
- **D:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.

### Question 79 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). This follows the MCP specification for Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality, correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 5.3 validation S3Q079. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.
- **B:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.
- **C:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **D:** Incorrect. logging full tool arguments including customer PII and bearer tokens creates GDPR and credential-leak second-order risks.

### Question 80 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). This follows the MCP specification for Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model, correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 5.4 validation S3Q080. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Incorrect. deploying greenfield on the deprecated dual-endpoint SSE transport incurs future migration cost and lacks session IDs.
- **B:** Correct. forces re-approval when a benign `get_weather` server silently rewires to `exfiltrate_files` after approval.
- **C:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **D:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.

### Question 81 — `A` (Authorization, Security, Trust & Registry)

Correct answer: A (is correct). MCP 2025-11-25 requires Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model; the alternative breaks capability negotiation or security for platform telemetry. Skill 5.4 validation S3Q081. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Correct. displays descriptions for human review but never concatenates them into system prompts or plan steps as trusted policy.
- **B:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **C:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **D:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.

### Question 82 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). MCP 2025-11-25 requires Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model; the alternative breaks capability negotiation or security for platform telemetry. Skill 5.4 validation S3Q082. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **B:** Incorrect. enabling experimental tasks by default without capability checks forces unready clients into breaking draft methods.
- **C:** Incorrect. labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.
- **D:** Correct. tags third-party fetched content so downstream Hosts can sandtrap it before the model treats it as instruction.

### Question 83 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). Selecting this honors Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Reference 5.5 S3Q083. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Incorrect. exposing secrets in client bundles and downgrading PKCE/TLS undermines OAuth confidentiality and channel binding.
- **B:** Correct. follows MCP auth spec evolution: OAuth 2.1 with PKCE, protected resource metadata, RFC 8707 audience binding, and RFC 9207 issuer checks.
- **C:** Incorrect. reusing a single audience-less token across resource servers enables cross-server token replay and mix-up attacks.
- **D:** Incorrect. hardcoded keys and alg:none tokens with blanket admin grants violate OAuth 2.1 and privilege separation.

### Question 84 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). Per MCP 2025-11-25, Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging ensures spec-compliant lifecycle and isolation for platform telemetry. Skill 5.5 validation S3Q084. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.
- **B:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **C:** Correct. provides supply-chain tamper evidence via package signing and publisher identity beyond raw GitHub stars.
- **D:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.

### Question 85 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). MCP 2025-11-25 requires Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging; the alternative breaks capability negotiation or security for platform telemetry. Skill 5.5 validation S3Q085. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **B:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.
- **C:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.
- **D:** Correct. provides supply-chain tamper evidence via package signing and publisher identity beyond raw GitHub stars.

### Question 86 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). This follows the MCP specification for Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic), correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 6.1 validation S3Q086. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **B:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **C:** Correct. uses typed server helpers that auto-wire tools/list/call handlers and JSON Schema validation from Zod objects.
- **D:** Incorrect. calling tools before the initialized handshake completes races capability discovery and throws methodNotFound errors.

### Question 87 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). This follows the MCP specification for Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic), correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 6.1 validation S3Q087. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Correct. gives models complete, machine-validated contracts for tool selection and argument generation.
- **B:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **C:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **D:** Incorrect. labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.

### Question 88 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). Selecting this honors Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 6.1 validation S3Q088. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **B:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **C:** Correct. gives models complete, machine-validated contracts for tool selection and argument generation.
- **D:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.

### Question 89 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). Selecting this honors Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Skill 6.2 validation S3Q089. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.
- **B:** Correct. gives OS-level isolation, clean env var scoping, and automatic teardown when Host exits without port conflicts.
- **C:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.
- **D:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.

### Question 90 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). This choice correctly implements Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 6.2 validation S3Q090. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **B:** Correct. gives OS-level isolation, clean env var scoping, and automatic teardown when Host exits without port conflicts.
- **C:** Incorrect. installing random `curl | bash` MCP servers without registry signature verification imports unvetted RCE into the IDE.
- **D:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.

### Question 91 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). Per MCP 2025-11-25, Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates ensures spec-compliant lifecycle and isolation for platform telemetry. Skill 6.2 validation S3Q091. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **B:** Correct. catches lifecycle, capability, and schema mismatches before CI with real-transport conformance testing.
- **C:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.
- **D:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.

### Question 92 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). Selecting this honors Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation and prevents the listed failure mode in AtlasCloud Platform Ops platform telemetry flows. Reference 6.3 S3Q092. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Incorrect. unvetted curl-piped installs with maximal scopes and plaintext token storage maximizes blast radius from a single malicious server.
- **B:** Incorrect. silent exfiltration without rate limits or audit visibility breaks data minimization and incident-response traceability.
- **C:** Correct. applies MCP security checklist: supply-chain pinning, description-vs-logic separation, consent gating, and provenance monitoring against poison/rug-pull.
- **D:** Incorrect. blind auto-approval and treating descriptions as trusted instructions invites prompt injection and supply-chain compromise.

### Question 93 — `B, E, F` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: B, E, and F (are correct). MCP 2025-11-25 requires Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation; the alternative breaks capability negotiation or security for platform telemetry. Skill 6.3 validation S3Q093. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **B:** Correct. makes servers discoverable with verifiable supply-chain metadata and semver-aware update notifications.
- **C:** Incorrect. logging full tool arguments including customer PII and bearer tokens creates GDPR and credential-leak second-order risks.
- **D:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **E:** Correct. keeps patch/minor server releases compatible with older Hosts that simply ignore unknown capabilities.
- **F:** Correct. ensures reproducible, least-privilege runtime with declared transport and liveness for orchestrators.

### Question 94 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). This choice correctly implements Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 6.3 validation S3Q094. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Correct. keeps patch/minor server releases compatible with older Hosts that simply ignore unknown capabilities.
- **B:** Incorrect. printing logs to stdout alongside JSON-RPC breaks line-delimited parsing and throws Parse error -32700.
- **C:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.
- **D:** Incorrect. joining user input with path concatenation without canonicalization enables classic directory traversal.

### Question 95 — `B, D` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: B and D (are correct). This choice correctly implements Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation for AtlasCloud Platform Ops while the distractors violate transport/session guarantees. Skill 6.4 validation S3Q095. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **B:** Correct. powers per-tool SLOs and supply-chain forensics without persisting sensitive tool argument values.
- **C:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **D:** Correct. enables post-incident forensics without persisting PII/tokens, keyed by stable tool provenance hashes.
- **E:** Incorrect. collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.

### Question 96 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). Per MCP 2025-11-25, Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation ensures spec-compliant lifecycle and isolation for platform telemetry. Skill 6.4 validation S3Q096. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Correct. powers per-tool SLOs and supply-chain forensics without persisting sensitive tool argument values.
- **B:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.
- **C:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **D:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.

### Question 97 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). This follows the MCP specification for Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation, correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 6.4 validation S3Q097. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Incorrect. skipping Inspector and relying only on unit mocks misses real transport framing and pagination/cancellation bugs.
- **B:** Incorrect. installing random `curl | bash` MCP servers without registry signature verification imports unvetted RCE into the IDE.
- **C:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.
- **D:** Correct. traces tool call latency through Streamable HTTP gateways into server execution with per-session correlation.

### Question 98 — `D, E` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: D and E (are correct). This follows the MCP specification for Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns, correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 6.5 validation S3Q098. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.
- **B:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **C:** Incorrect. skipping Inspector and relying only on unit mocks misses real transport framing and pagination/cancellation bugs.
- **D:** Correct. centralizes AuthZ, session affinity, and observability without duplicating gateway logic in each MCP server.
- **E:** Correct. prevents a read-only doc-search server from silently acquiring destructive write scopes after one-time user approval.

### Question 99 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). This follows the MCP specification for Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns, correcting the insecure/incompatible anti-pattern for platform telemetry. Skill 6.5 validation S3Q099. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.
- **B:** Correct. prevents a read-only doc-search server from silently acquiring destructive write scopes after one-time user approval.
- **C:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.
- **D:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.

### Question 100 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). MCP 2025-11-25 requires Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns; the alternative breaks capability negotiation or security for platform telemetry. Skill 6.5 validation S3Q100. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Correct. prevents a read-only doc-search server from silently acquiring destructive write scopes after one-time user approval.
- **B:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.
- **C:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.
- **D:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
