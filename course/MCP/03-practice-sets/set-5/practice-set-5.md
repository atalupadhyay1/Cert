# MCP: Model Context Protocol: Servers, Clients, Transports & Security — Full-Length Mock Exam 5 — OmniCart Commerce Ops (Retail & Supply Chain)

**Theme:** Progress & Cancellation, Sampling Delegation, Roots Boundaries & Env Isolation  
**Credential alignment:** `Model Context Protocol (MCP 2025-11-25) — Tool & Context Standard`  
**Blueprint baseline:** `November 2026 (MCP Specification 2025-11-25 · MCP Registry & Inspector · OAuth 2.1 + RFC 8707/9207 + CIMD · OWASP MCP Security Checklist)` (https://modelcontextprotocol.io/introduction · https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation · https://genai.owasp.org/resource/mcp-security-checklist/)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `120 minutes` (`72 seconds/question` full-endurance pacing; aligns with `120 minutes` on NVIDIA NCP-AAI & GitHub GH-600)

> **Disclaimer:** Independent educational practice material authored from public engineering specifications and open-protocol documentation — not affiliated with, sponsored by, or endorsed by NVIDIA, the Linux Foundation, Anthropic, OpenAI, Google, Microsoft, GitHub, LangChain, or OWASP. Practice scores do not guarantee passing any third-party certification exam.

## Questions

---

## Domain 1 — MCP Foundations, Architecture & Lifecycle (16–20% blueprint weight · 18 questions)

### 1. OmniCart Commerce Ops MCP onboarding for commerce checkout flow must follow the correct 4-step lifecycle. Which ordered sequence is correct? Trace 4215: 200-tool batch exceeds advertised `maxBatchSize`. Scenario 1.1-5-1.

- **A.** Client hardcodes `protocolVersion: "1.0"` forever → ignore server `protocolVersion` echo → send duplicate `initialize` on every ping → cache capabilities indefinitely
- **B.** Server sends `initialize` to client → client negotiates logging level first → exchange OAuth tokens inside `initialize` params → begin sampling without capability check
- **C.** Client calls `tools/call` immediately → server returns capability list on tool error → client sends `initialize` afterward → skip `notifications/initialized`
- **D.** Client sends `initialize` with `protocolVersion` & `capabilities` → server replies with negotiated version & capabilities → client sends `notifications/initialized` → normal `tools/list` & `resources/list` calls begin

### 2. OmniCart Commerce Ops must fix its commerce checkout flow MCP integration. Which two changes bring it into spec compliance? Select two. Ticket 1891: plaintext `config.json` holds refresh token. [1.1 #2]

- **A.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **B.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **C.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **D.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **E.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets

### 3. For commerce checkout flow, OmniCart Commerce Ops must handle `notifications/progress` vs polling. The correct pattern is to ____. Log 9248: SSE stream without `eventId` loses progress on reconnect. [1.1 #3]

- **A.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **B.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **C.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets
- **D.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification

### 4. The OmniCart Commerce Ops MCP configuration for commerce checkout flow shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Ticket 6801 reports `Last-Event-ID` replay mismatch after gateway restart. [1.2 #4]

- **A.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **B.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **C.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **D.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs

### 5. The OmniCart Commerce Ops MCP configuration for commerce checkout flow shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Log entry 4289 shows `Method not found -32601` without capability check. [1.2 #5]

- **A.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **B.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **C.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **D.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent

### 6. At OmniCart Commerce Ops, engineers building an MCP server for commerce checkout flow need to ____. Which configuration correctly implements the MCP specification? Case 2974: `structuredContent` missing despite `outputSchema` declared. [1.2 #6]

- **A.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **B.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **C.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **D.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default

### 7. In `OmniCart Commerce Ops` `commerce checkout flow` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Trace 6659 reveals truncated cursor pagination at 50 entries. [1.3 #7]

- **A.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **B.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean
- **C.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation
- **D.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects

### 8. During an commerce checkout flow workflow audit at OmniCart Commerce Ops, you notice the MCP server exposes file paths without proper checks. The team must ____. Log 7288: `initialize` skipped before `tools/list`. [1.3 #8]

- **A.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **B.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **C.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **D.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible

### 9. Proposed solution: To handle commerce checkout flow, OmniCart Commerce Ops plans to grant admin:write scope to every read-only docs search server by default. Does this satisfy the MCP specification? Trace 4119 reveals truncated cursor pagination at 50 entries. [1.3 #9]

- **A.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **B.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **C.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **D.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`

### 10. OmniCart Commerce Ops MCP server for commerce checkout flow requires two valid security hardening steps. Which two should you apply? Select two. Log 4313: `initialize` skipped before `tools/list`. [1.4 #10]

- **A.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **B.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **C.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **D.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **E.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs

### 11. Proposed solution: OmniCart Commerce Ops will batch 200 tool calls beyond advertised maxBatchSize in a single request for commerce checkout flow. Does this meet the MCP 2025-11-25 goal? Trace 1052: 200-tool batch exceeds advertised `maxBatchSize`. [1.4 #11]

- **A.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **B.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **C.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **D.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)

### 12. OmniCart Commerce Ops needs to bound commerce checkout flow sampling loops that fan out recursively. Which limit is appropriate? Audit 6027 flags `alg:none` token acceptance in staging. [1.4 #12]

- **A.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **B.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **C.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **D.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan

### 13. At OmniCart Commerce Ops, the MCP client code handling commerce checkout flow leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Log 7887: SSE stream without `eventId` loses progress on reconnect. Scenario 1.5-5-13.

- **A.** Client calls undefined tool name → server creates tool on-the-fly → skip inputSchema validation → stream 50-MB blob as single text content block
- **B.** Server exposes 200 tools without descriptions → client guesses arguments via prompt → server executes shell with raw LLM string → return HTML page inside isError=false
- **C.** Server declares tool with `name`, `description`, `inputSchema` (JSON Schema) → client `tools/list` discovers it → model calls `tools/call` with validated args → server validates, executes idempotently & returns `content` + `isError`
- **D.** Server returns tool result before validation → client retries with doubled args → disable tools/list_changed notifications → cache tool names forever

### 14. OmniCart Commerce Ops handles commerce checkout flow via MCP sampling delegation. To enforce least privilege, the server should ____. Trace 6564: batch of 200 tool calls timed out. [1.5 #14]

- **A.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **B.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **C.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **D.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization

### 15. When OmniCart Commerce Ops connects its VS Code host to an MCP server for commerce checkout flow, the `roots/list` workflow should ____. Alert 9407: `progressToken` mismatch across concurrent tool calls. [1.5 #15]

- **A.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets
- **B.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`
- **C.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **D.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes

### 16. For commerce checkout flow at OmniCart Commerce Ops, two best practices align with MCP 2025-11-25. Which two should be implemented? Select two. Trace 8233: batch of 200 tool calls timed out. [1.6 #16]

- **A.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **B.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`
- **C.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **D.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **E.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks

### 17. At OmniCart Commerce Ops, commerce checkout flow MCP gateway logs show `Last-Event-ID` replay gaps. The team should ____. Alert 4272: `progressToken` mismatch across concurrent tool calls. [1.6 #17]

- **A.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **B.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`
- **C.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **D.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization

### 18. For commerce checkout flow at OmniCart Commerce Ops, token storage uses plaintext `config.json`. The secure alternative is to ____. Incident MCP-2026-4038 shows Misconfigured `Mcp-Session-Id` routing. [1.6 #18]

- **A.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **B.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **C.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **D.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`

---

## Domain 2 — Tools, Resources & Resource Templates (18–22% blueprint weight · 20 questions)

### 19. Which two logging/observability actions are correct for commerce checkout flow MCP at OmniCart Commerce Ops? Select two. Case 2706: registry installs via `curl¦bash` without signature check. [2.1 #19]

- **A.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **B.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **C.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **D.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **E.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately

### 20. In OmniCart Commerce Ops production, an MCP server for commerce checkout flow must ____ to prevent tool poisoning attacks. Review 5477: `outputSchema` mismatched to `structuredContent` shape. [2.1 #20]

- **A.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)
- **B.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **C.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **D.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**

### 21. The MCP Inspector highlights `____` as missing for commerce checkout flow at OmniCart Commerce Ops. Which completion is spec-correct? Alert 2523: `Mcp-Session-Id` reused across tenants. [2.1 #21]

- **A.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **B.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`
- **C.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **D.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`

### 22. The OmniCart Commerce Ops team debugging commerce checkout flow sees truncated `resources/list` results at 50 items. They should ____. Trace 9006: 200-tool batch exceeds advertised `maxBatchSize`. [2.1 #22]

- **A.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **B.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **C.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **D.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke

### 23. Complete the missing MCP field: In the OmniCart Commerce Ops commerce checkout flow server, `____` must be set to the MCP-required value to enable commerce checkout flow correctly. Ticket 3561: `notifications/roots/list_changed` ignored after folder add. [2.2 #23]

- **A.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **B.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **C.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation
- **D.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure

### 24. OmniCart Commerce Ops needs to bound commerce checkout flow sampling loops that fan out recursively. Which limit is appropriate? Trace 9005: `resource` audience binding missing per RFC 8707. [2.2 #24]

- **A.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **B.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **C.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **D.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke

### 25. At OmniCart Commerce Ops, the MCP client code handling commerce checkout flow leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Log 4963: `initialize` skipped before `tools/list`. [2.2 #25]

- **A.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **B.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **C.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean
- **D.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI

### 26. OmniCart Commerce Ops MCP server for commerce checkout flow is deployed as root container with `:latest`. The secure packaging is to ____. Review 4428: `completion/complete` implemented as heavy tool call. [2.2 #26]

- **A.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks
- **B.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure
- **C.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **D.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping

### 27. The OmniCart Commerce Ops MCP configuration for commerce checkout flow shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Trace 2622 reveals truncated cursor pagination at 50 entries. Scenario 2.3-5-27.

- **A.** Server returns resources without uri fields → client stores resource content in tool history → server omits page cursors for 10k items → skip mimeType declaration
- **B.** Client guesses file URIs without list → server returns OS absolute paths as uri → embed 10-MB binary as base64 JSON string → skip uri validation
- **C.** Server advertises `resources` capability → client calls `resources/list` or `resources/templates/list` → client reads `resources/read` with `uri` → server returns `contents` with `mimeType`, handling pagination cursors
- **D.** Server lists resources without capability flag → client polls `resources/list` every 10 ms in loop → ignore `resources/list_changed` notifications → request resources via tools/call

### 28. OmniCart Commerce Ops engineers designing an MCP system for commerce checkout flow must evaluate two correct controls. Which two statements are correct? Select two. Log 9430: SSE stream without `eventId` loses progress on reconnect. [2.3 #28]

- **A.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **B.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **C.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **D.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **E.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files

### 29. An commerce checkout flow MCP gateway at OmniCart Commerce Ops strips `Accept` negotiation headers. The fix is to ____. Log entry 7147 shows `Method not found -32601` without capability check. [2.3 #29]

- **A.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **B.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **C.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request
- **D.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`

### 30. An external auditor flags that OmniCart Commerce Ops MCP deployment for commerce checkout flow stores bearer tokens insecurely. The correction is to ____. Review 2814: sampling loop lacks depth cap and cost budget. [2.4 #30]

- **A.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **B.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification
- **C.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **D.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)

### 31. The OmniCart Commerce Ops team debugging commerce checkout flow sees truncated `resources/list` results at 50 items. They should ____. Ticket 2929: plaintext `config.json` holds refresh token. [2.4 #31]

- **A.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **B.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **C.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks
- **D.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`

### 32. Complete the missing MCP field: In the OmniCart Commerce Ops commerce checkout flow server, `____` must be set to the MCP-required value to enable commerce checkout flow correctly. Log entry 5467 shows `Method not found -32601` without capability check. [2.4 #32]

- **A.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **B.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **C.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **D.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`

### 33. Proposed solution: OmniCart Commerce Ops will grant admin:write scope to every read-only docs search server by default for commerce checkout flow. Does this meet the MCP 2025-11-25 goal? Case 5696: Host passes full env block to untrusted calendar server. [2.5 #33]

- **A.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **B.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **C.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`
- **D.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals

### 34. During commerce checkout flow rollout at OmniCart Commerce Ops, canary hosts skip capability re-validation after reconnect. They should ____. Trace 2003: batch of 200 tool calls timed out. [2.5 #34]

- **A.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **B.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **C.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation
- **D.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking

### 35. Complete the missing MCP field: In the OmniCart Commerce Ops commerce checkout flow server, `____` must be set to the MCP-required value to enable commerce checkout flow correctly. Trace 9319: `resource` audience binding missing per RFC 8707. [2.5 #35]

- **A.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **B.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **C.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **D.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets

### 36. What is the correct 4-step order for commerce checkout flow workflow at OmniCart Commerce Ops under MCP 2025-11-25? Log entry 6597 shows `Method not found -32601` without capability check. Scenario 2.6-5-36.

- **A.** Client exposes entire `C:\` without consent → server walks parent directories above declared roots → disable path canonicalization → follow symlinks blindly
- **B.** Server declares client roots unilaterally → client trusts arbitrary server-provided paths → skip roots/list → ignore list_changed notifications
- **C.** Server hardcodes `roots/list` response → client polls filesystem without notification channel → skip name/uri validation → cache roots forever
- **D.** Client declares `roots` capability with `file://` allowlist → server calls `roots/list` to learn boundaries → server restricts `resources/read` & tool file ops to those roots → handle `notifications/roots/list_changed`

### 37. Two statements about MCP commerce checkout flow correctly reflect the specification for OmniCart Commerce Ops. Which two are true? Select two. Review 5310: `completion/complete` implemented as heavy tool call. [2.6 #37]

- **A.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **B.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)
- **C.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **D.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **E.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`

### 38. OmniCart Commerce Ops observes `prompt injection` payloads via commerce checkout flow MCP resource content. The mitigation is to ____. Audit 4838: `includeContext=allServers` exfiltrates cross-server data. [2.6 #38]

- **A.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **B.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **C.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **D.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails

---

## Domain 3 — Prompts, Sampling, Roots & Elicitation (14–18% blueprint weight · 16 questions)

### 39. For OmniCart Commerce Ops commerce checkout flow server to advertise new capabilities after a deploy, the correct notification is ____. Trace 3471: 200-tool batch exceeds advertised `maxBatchSize`. [3.1 #39]

- **A.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **B.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **C.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **D.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions

### 40. Complete the missing MCP field: In the OmniCart Commerce Ops commerce checkout flow server, `____` must be set to the MCP-required value to enable commerce checkout flow correctly. Trace 5235: 200-tool batch exceeds advertised `maxBatchSize`. [3.1 #40]

- **A.** Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation
- **B.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **C.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **D.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults

### 41. The MCP Inspector highlights `____` as missing for commerce checkout flow at OmniCart Commerce Ops. Which completion is spec-correct? Ticket 2886: plaintext `config.json` holds refresh token. [3.1 #41]

- **A.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **B.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request
- **C.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **D.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`

### 42. Select three correct MCP commerce checkout flow behaviors that OmniCart Commerce Ops should enforce for its MCP fleet. Select three. Review 3606: `completion/complete` implemented as heavy tool call. [3.2 #42]

- **A.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **B.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **C.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **D.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **E.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **F.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows

### 43. The OmniCart Commerce Ops MCP configuration for commerce checkout flow shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Incident 7228: tool logic changed post-approval (rug-pull) undetected. [3.2 #43]

- **A.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **B.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **C.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **D.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure

### 44. The OmniCart Commerce Ops MCP configuration for commerce checkout flow shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Audit 1071: auto-approve bypasses human consent for destructive tool. [3.2 #44]

- **A.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **B.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **C.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`
- **D.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets

### 45. Which two logging/observability actions are correct for commerce checkout flow MCP at OmniCart Commerce Ops? Select two. Alert 5262: `progressToken` mismatch across concurrent tool calls. [3.3 #45]

- **A.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **B.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **C.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **D.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **E.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request

### 46. Proposed solution: OmniCart Commerce Ops will store refresh tokens in world-readable config.json and log Authorization headers for commerce checkout flow. Does this meet the MCP 2025-11-25 goal? Incident 6011: tool `inputSchema` validation skipped, injection observed. [3.3 #46]

- **A.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **B.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **C.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **D.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs

### 47. For commerce checkout flow at OmniCart Commerce Ops, the client must handle `resources/subscribe` vs polling. Which is efficient? Ticket 8068 reports `Last-Event-ID` replay mismatch after gateway restart. [3.3 #47]

- **A.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **B.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **C.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **D.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token

### 48. The OmniCart Commerce Ops team documents the commerce checkout flow MCP flow. Which sequence of actions is spec-compliant? Audit 4733: auto-approve bypasses human consent for destructive tool. Scenario 3.4-5-48.

- **A.** Client exposes sampling by default without opt-in → server loops sampling/createMessage recursively → ignore modelPreferences hints → return raw chain-of-thought as tool output
- **B.** Server mixes sampling messages into tool descriptions → client forwards without isolation → skip cost tracking → cache sampling results as facts
- **C.** Server sends sampling without capability check → include raw customer PII in messages → skip maxTokens limits → client auto-executes without user consent
- **D.** Server advertises sampling need → checks client `sampling` capability → sends `sampling/createMessage` with `messages`, `maxTokens`, `modelPreferences` → client applies human-in-loop gating & returns generation

### 49. Which two behaviors correctly describe MCP commerce checkout flow handling at OmniCart Commerce Ops? Select two. Case 9053: Host passes full env block to untrusted calendar server. [3.4 #49]

- **A.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **B.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **C.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **D.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **E.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`

### 50. A OmniCart MCP client for commerce checkout flow must ____ to satisfy the protocol. What is the correct implementation approach? Incident 6604: deprecated `/sse` + `/messages` split endpoint still in prod. [3.4 #50]

- **A.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **B.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **C.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **D.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals

### 51. At OmniCart Commerce Ops, engineers building an MCP server for commerce checkout flow need to ____. Which configuration correctly implements the MCP specification? Trace 4857: `resource` audience binding missing per RFC 8707. [3.5 #51]

- **A.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **B.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request
- **C.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **D.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage

### 52. OmniCart Commerce Ops commerce checkout flow MCP `initialize` handshake omits `capabilities`. The next step is to ____. Audit 6923: auto-approve bypasses human consent for destructive tool. [3.5 #52]

- **A.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **B.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **C.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **D.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`

### 53. Proposed solution: embed static client_secret inside the shipped desktop binary for all tenants is suggested for commerce checkout flow at OmniCart Commerce Ops. Does this meet the goal? Incident 4337: OAuth PKCE verifier omitted for public client. [3.6 #53]

- **A.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **B.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **C.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **D.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle

### 54. During commerce checkout flow review at OmniCart Commerce Ops, the MCP server emits debug logs at `error` level. The proper level is ____. Alert 9617: `Mcp-Session-Id` reused across tenants. [3.6 #54]

- **A.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **B.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params
- **C.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **D.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side

---

## Domain 4 — Transports, Sessions & Protocol Evolution (14–18% blueprint weight · 16 questions)

### 55. For commerce checkout flow at OmniCart Commerce Ops, three controls are required for MCP compliance. Which three are correct? Select three. Audit 1778 flags `alg:none` token acceptance in staging. [4.1 #55]

- **A.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **B.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **C.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation
- **D.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **E.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **F.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation

### 56. For commerce checkout flow, OmniCart Commerce Ops must handle `notifications/progress` vs polling. The correct pattern is to ____. Trace 9218 reveals truncated cursor pagination at 50 entries. [4.1 #56]

- **A.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **B.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **C.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request
- **D.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation

### 57. For commerce checkout flow at OmniCart Commerce Ops, the MCP Inspector UI must validate tool schemas. Which approach is correct? Trace 9486: 200-tool batch exceeds advertised `maxBatchSize`. [4.1 #57]

- **A.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **B.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **C.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **D.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token

### 58. What is the correct 4-step order for commerce checkout flow workflow at OmniCart Commerce Ops under MCP 2025-11-25? Ticket 2059 reports `Last-Event-ID` replay mismatch after gateway restart. Scenario 4.2-5-58.

- **A.** Client sends batched 100 requests without server batch ack → server streams without event IDs → skip session expiry handling → leak session IDs across tenants
- **B.** Server returns 200 OK with HTML error page → client retries without backoff → disable idempotency on non-idempotent tool calls → omit Content-Type validation
- **C.** Client opens separate GET /sse and POST /message SSE endpoints → send JSON without Accept header → ignore Mcp-Session-Id → close stream after each chunk without Last-Event-ID
- **D.** Client POSTs JSON-RPC to single `mcp` endpoint with `Content-Type: application/json` & `Accept: text/event-stream, application/json` → server may respond with single JSON or SSE stream → client honors `Mcp-Session-Id` & `Last-Event-ID` for resumability

### 59. At OmniCart Commerce Ops, the MCP client code handling commerce checkout flow leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Trace 7867 reveals truncated cursor pagination at 50 entries. [4.2 #59]

- **A.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **B.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **C.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **D.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`

### 60. Proposed solution: OmniCart Commerce Ops will batch 200 tool calls beyond advertised maxBatchSize in a single request for commerce checkout flow. Does this meet the MCP 2025-11-25 goal? Audit 1406: `includeContext=allServers` exfiltrates cross-server data. [4.2 #60]

- **A.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **B.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **C.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **D.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context

### 61. A commerce checkout flow MCP extension at OmniCart Commerce Ops leaks `Mcp-Session-Id` across tenants. The team must ____. Ticket 4588: `notifications/roots/list_changed` ignored after folder add. [4.3 #61]

- **A.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **B.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **C.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **D.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect

### 62. For commerce checkout flow at OmniCart Commerce Ops, the Host must reconcile `protocolVersion` negotiation after an upgrade. Which action is correct? Review 8741: sampling loop lacks depth cap and cost budget. [4.3 #62]

- **A.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **B.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **C.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure
- **D.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect

### 63. You are reviewing an MCP implementation for OmniCart Commerce Ops that handles commerce checkout flow. Which statement about ____ is accurate under MCP 2025-11-25? Case 2004: registry installs via `curl¦bash` without signature check. [4.3 #63]

- **A.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **B.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **C.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **D.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics

### 64. Which two behaviors correctly describe MCP commerce checkout flow handling at OmniCart Commerce Ops? Select two. Case 6122: registry installs via `curl¦bash` without signature check. [4.4 #64]

- **A.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **B.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **C.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **D.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **E.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`

### 65. OmniCart Commerce Ops reports intermittent `Method not found -32601` errors when accessing commerce checkout flow. To fix this, the team should ____. Incident 7353: tool logic changed post-approval (rug-pull) undetected. [4.4 #65]

- **A.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **B.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **C.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **D.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions

### 66. For commerce checkout flow at OmniCart Commerce Ops, token storage uses plaintext `config.json`. The secure alternative is to ____. Incident 2970: tool `inputSchema` validation skipped, injection observed. [4.4 #66]

- **A.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **B.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **C.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **D.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`

### 67. Complete the missing MCP field: In the OmniCart Commerce Ops commerce checkout flow server, `____` must be set to the MCP-required value to enable commerce checkout flow correctly. Incident 8377: deprecated `/sse` + `/messages` split endpoint still in prod. [4.5 #67]

- **A.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively
- **B.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets
- **C.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **D.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation

### 68. When OmniCart Commerce Ops connects its VS Code host to an MCP server for commerce checkout flow, the `roots/list` workflow should ____. Incident 8971: deprecated `/sse` + `/messages` split endpoint still in prod. [4.5 #68]

- **A.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **B.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **C.** Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation
- **D.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects

### 69. During commerce checkout flow incident triage at OmniCart Commerce Ops, audit logs lack `requestId` correlation. The correction is to ____. Incident 1861: OAuth PKCE verifier omitted for public client. [4.6 #69]

- **A.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **B.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **C.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **D.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation

### 70. OmniCart Commerce Ops reports intermittent `Method not found -32601` errors when accessing commerce checkout flow. To fix this, the team should ____. Review 6726 notes `resources/list_changed` never fired after ingest. [4.6 #70]

- **A.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **B.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **C.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **D.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`

---

## Domain 5 — Authorization, Security, Trust & Registry (13–17% blueprint weight · 15 questions)

### 71. For commerce checkout flow, OmniCart Commerce Ops must enforce three hardening measures. Which three are correct? Select three. Ticket 2465: plaintext `config.json` holds refresh token. [5.1 #71]

- **A.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **B.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **C.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **D.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **E.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure
- **F.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`

### 72. In `OmniCart Commerce Ops` `commerce checkout flow` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Case 5934: registry installs via `curl¦bash` without signature check. [5.1 #72]

- **A.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **B.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **C.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **D.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways

### 73. OmniCart Commerce Ops MCP server for commerce checkout flow uses static API keys in `Authorization`. The OAuth 2.1 migration is to ____. Review 5965 notes `resources/list_changed` never fired after ingest. [5.1 #73]

- **A.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **B.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **C.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **D.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`

### 74. At OmniCart Commerce Ops, commerce checkout flow MCP server batch returns timeout for 200 calls. The team should ____. Case 4841: Host passes full env block to untrusted calendar server. [5.2 #74]

- **A.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **B.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **C.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **D.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads

### 75. Complete the missing MCP field: In the OmniCart Commerce Ops commerce checkout flow server, `____` must be set to the MCP-required value to enable commerce checkout flow correctly. Incident 5898: OAuth PKCE verifier omitted for public client. [5.2 #75]

- **A.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **B.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **C.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **D.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets

### 76. For commerce checkout flow at OmniCart Commerce Ops, token storage uses plaintext `config.json`. The secure alternative is to ____. Log entry 3126 shows `Method not found -32601` without capability check. [5.2 #76]

- **A.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **B.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **C.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **D.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603

### 77. The OmniCart Commerce Ops team documents the commerce checkout flow MCP flow. Which sequence of actions is spec-compliant? Audit 3052: auto-approve bypasses human consent for destructive tool. Scenario 5.3-5-77. through OTel collector tail sampling (variant alpha 562).

- **A.** Server embeds client_secret in JS bundle → disable PKCE as optional → return tokens over plain HTTP → cache discovery doc forever without TLS
- **B.** Client sends static API key in Authorization header → server skips issuer discovery → accept tokens with alg:none → grant org-admin scope by default
- **C.** Server exposes `/.well-known/oauth-authorization-server` with PRM & CIMD → client fetches RS metadata with `resource` indicator (RFC 8707) → PKCE + state + RFC 9207 iss validation → audience-bound token issued per resource server
- **D.** Client trusts token from any issuer → skip RFC 9207 iss equality check → ignore RFC 7591 dynamic registration → reuse single token across all resource servers

### 78. For commerce checkout flow, OmniCart Commerce Ops must enforce per-tool OAuth scope checks. Which scope design is correct? Review 9890: sampling loop lacks depth cap and cost budget. [5.3 #78]

- **A.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **B.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **C.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **D.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`

### 79. An commerce checkout flow MCP gateway at OmniCart Commerce Ops strips `Accept` negotiation headers. The fix is to ____. Log entry 5252 shows `Method not found -32601` without capability check. [5.3 #79] through Kafka topic rebalancing (variant delta 561).

- **A.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **B.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **C.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **D.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs

### 80. OmniCart Commerce Ops wants its MCP server to support both local and remote clients for commerce checkout flow. The architecture should ____. Case 5460: Host passes full env block to untrusted calendar server. [5.4 #80]

- **A.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **B.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`
- **C.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **D.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately

### 81. During commerce checkout flow at OmniCart Commerce Ops, the MCP server responds with SSE without `eventId`. Which correction is required? Ticket 2445 reports `Last-Event-ID` replay mismatch after gateway restart. [5.4 #81]

- **A.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **B.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **C.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **D.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token

### 82. OmniCart Commerce Ops wants commerce checkout flow MCP completions for enum arguments. The valid method is ____. Alert 5297: `Mcp-Session-Id` reused across tenants. [5.4 #82]

- **A.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **B.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **C.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **D.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure

### 83. OmniCart Commerce Ops MCP server for commerce checkout flow requires two valid security hardening steps. Which two should you apply? Select two. Alert 8992: `progressToken` mismatch across concurrent tool calls. [5.5 #83]

- **A.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **B.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params
- **C.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)
- **D.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **E.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`

### 84. OmniCart Commerce Ops wants to bridge commerce checkout flow MCP tools into an A2A task mesh. The correct layer definition is ____. Trace 1525 reveals truncated cursor pagination at 50 entries. [5.5 #84]

- **A.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **B.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **C.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **D.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change

### 85. An commerce checkout flow MCP gateway at OmniCart Commerce Ops strips `Accept` negotiation headers. The fix is to ____. Incident 4029: deprecated `/sse` + `/messages` split endpoint still in prod. [5.5 #85]

- **A.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **B.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **C.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets
- **D.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)

---

## Domain 6 — SDKs, Deployment, Observability & Ecosystem (13–17% blueprint weight · 15 questions)

### 86. In `OmniCart Commerce Ops` `commerce checkout flow` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Log entry 1742 shows `Method not found -32601` without capability check. [6.1 #86]

- **A.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params
- **B.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **C.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **D.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately

### 87. During commerce checkout flow rollout at OmniCart Commerce Ops, canary hosts skip capability re-validation after reconnect. They should ____. Alert 5249: `Mcp-Session-Id` reused across tenants. [6.1 #87]

- **A.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **B.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **C.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **D.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**

### 88. At OmniCart Commerce Ops, the MCP client code handling commerce checkout flow leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Ticket 8115 reports `Last-Event-ID` replay mismatch after gateway restart. [6.1 #88]

- **A.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **B.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **C.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params
- **D.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`

### 89. Two statements about MCP commerce checkout flow correctly reflect the specification for OmniCart Commerce Ops. Which two are true? Select two. Ticket 3831: `notifications/roots/list_changed` ignored after folder add. [6.2 #89]

- **A.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **B.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request
- **C.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **D.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **E.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification

### 90. Proposed solution: hardcode protocolVersion to 2024-11-05 forever and ignore server capability updates is suggested for commerce checkout flow at OmniCart Commerce Ops. Does this meet the goal? Log entry 7687 shows `Method not found -32601` without capability check. [6.2 #90]

- **A.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **B.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **C.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **D.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively

### 91. For commerce checkout flow at OmniCart Commerce Ops, token storage uses plaintext `config.json`. The secure alternative is to ____. Review 4071 notes `resources/list_changed` never fired after ingest. [6.2 #91]

- **A.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **B.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **C.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **D.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible

### 92. You are reviewing an MCP implementation for OmniCart Commerce Ops that handles commerce checkout flow. Which statement about ____ is accurate under MCP 2025-11-25? Ticket 6962 reports `Last-Event-ID` replay mismatch after gateway restart. [6.3 #92]

- **A.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean
- **B.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **C.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **D.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603

### 93. OmniCart Commerce Ops reports intermittent `Method not found -32601` errors when accessing commerce checkout flow. To fix this, the team should ____. Log entry 5217 shows `Method not found -32601` without capability check. [6.3 #93]

- **A.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **B.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean
- **C.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **D.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping

### 94. The MCP Inspector highlights `____` as missing for commerce checkout flow at OmniCart Commerce Ops. Which completion is spec-correct? Audit 3904: auto-approve bypasses human consent for destructive tool. [6.3 #94]

- **A.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **B.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **C.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **D.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization

### 95. For commerce checkout flow at OmniCart Commerce Ops, which ordered flow correctly implements the MCP 2025-11-25 requirement? Incident 8228: deprecated `/sse` + `/messages` split endpoint still in prod. Scenario 6.4-5-95.

- **A.** Pin server versions & verify registry signatures → isolate tool descriptions from executable logic → prompt user before first tool approval & high-risk actions → log tool provenance & monitor for description drift
- **B.** Auto-approve all tools without review → trust tool description text as system prompt → allow server to change tool logic post-approval → skip signature verification
- **C.** Exfiltrate tool arguments to third-party analytics silently → skip rate limiting on tool calls → omit provenance tags → hide tool calls from audit UI
- **D.** Install random GitHub MCP servers via curl|bash → grant full filesystem + network + env scopes → disable log redaction → store tokens in plaintext

### 96. OmniCart Commerce Ops MCP server for commerce checkout flow requires two valid security hardening steps. Which two should you apply? Select two. Trace 5186: 200-tool batch exceeds advertised `maxBatchSize`. [6.4 #96]

- **A.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **B.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **C.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **D.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **E.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`

### 97. OmniCart Commerce Ops wants to bridge commerce checkout flow MCP tools into an A2A task mesh. The correct layer definition is ____. Alert 7492: `Mcp-Session-Id` reused across tenants. [6.4 #97]

- **A.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **B.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **C.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **D.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping

### 98. Which two behaviors correctly describe MCP commerce checkout flow handling at OmniCart Commerce Ops? Select two. Ticket 8751: plaintext `config.json` holds refresh token. [6.5 #98]

- **A.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **B.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **C.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds
- **D.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **E.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`

### 99. OmniCart Commerce Ops needs to secure commerce checkout flow tool calls that mutate production data. The right control is to ____. Log 2196: `initialize` skipped before `tools/list`. [6.5 #99]

- **A.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **B.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **C.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds
- **D.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)

### 100. When OmniCart Commerce Ops connects its VS Code host to an MCP server for commerce checkout flow, the `roots/list` workflow should ____. Review 1867: `completion/complete` implemented as heavy tool call. [6.5 #100]

- **A.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **B.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **C.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **D.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation

---

## Answer Key and Explanations

### Question 1 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). Per MCP 2025-11-25, Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model ensures spec-compliant lifecycle and isolation for commerce checkout flow. Reference 1.1 S5Q001. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Incorrect. hardcoding protocol versions and duplicate initialize pings breaks forward compatibility and lifecycle idempotency.
- **B:** Incorrect. reversing the initialize direction and mixing OAuth into initialize params conflates lifecycle with authorization.
- **C:** Incorrect. invoking tools before initialize negotiation bypasses version checks and omits the required initialized signal.
- **D:** Correct. follows MCP lifecycle spec: version/capability negotiation via initialize exchange completed by initialized notification before any feature calls.

### Question 2 — `A, D` (MCP Foundations, Architecture & Lifecycle)

Correct answers: A and D (are correct). This choice correctly implements Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model for OmniCart Commerce Ops while the distractors violate transport/session guarantees. Skill 1.1 validation S5Q002. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Correct. maps transport to deployment topology: stdio gives OS-level isolation locally; Streamable HTTP enables remote multi-tenant scale.
- **B:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.
- **C:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **D:** Correct. clarifies layer boundaries: MCP standardizes context attachment; function calling is inline model schema; A2A negotiates task handoffs.
- **E:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.

### Question 3 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). Selecting this honors Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Skill 1.1 validation S5Q003. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Correct. maps transport to deployment topology: stdio gives OS-level isolation locally; Streamable HTTP enables remote multi-tenant scale.
- **B:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.
- **C:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.
- **D:** Incorrect. distributing servers as raw GitHub tarballs without server.json or publisher proof hides supply-chain compromise.

### Question 4 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). MCP 2025-11-25 requires Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 1.2 validation S5Q004. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.
- **B:** Correct. enables forwards-compatible evolution without breaking older Hosts or Servers on version skew.
- **C:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **D:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.

### Question 5 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). MCP 2025-11-25 requires Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 1.2 validation S5Q005. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **B:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.
- **C:** Correct. provides spec-guaranteed failure detection where OS TCP keepalives are invisible to application-level SSE/stdio proxies.
- **D:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.

### Question 6 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). This follows the MCP specification for Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 1.2 validation S5Q006. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **B:** Correct. enables forwards-compatible evolution without breaking older Hosts or Servers on version skew.
- **C:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.
- **D:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.

### Question 7 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). This follows the MCP specification for Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 1.3 validation S5Q007. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Correct. separates best-effort telemetry from correlated RPC state per JSON-RPC 2.0, preventing notification ID collisions.
- **B:** Incorrect. dumping base64 blobs as plain text without typed content blocks loses mimeType and forces heuristic parsing.
- **C:** Incorrect. collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.
- **D:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.

### Question 8 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). This follows the MCP specification for Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 1.3 validation S5Q008. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.
- **B:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **C:** Correct. standardizes remediation: 32601 means check capabilities, 32602 means fix schema, unlike bespoke string matching.
- **D:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.

### Question 9 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). Per MCP 2025-11-25, Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 1.3 validation S5Q009. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.
- **B:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.
- **C:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.
- **D:** Incorrect. setting includeContext=allServers by default fans sensitive data from every connected server into one sampling call.

### Question 10 — `B, D` (MCP Foundations, Architecture & Lifecycle)

Correct answers: B and D (are correct). Per MCP 2025-11-25, Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 1.4 validation S5Q010. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **B:** Correct. allows safe iteration on draft specs like Tasks and elicitation without polluting the stable capability surface.
- **C:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **D:** Correct. lets each party call only negotiated features, avoiding methodNotFound and silent fallback hallucinations.
- **E:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.

### Question 11 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). This choice correctly implements Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) for OmniCart Commerce Ops while the distractors violate transport/session guarantees. Skill 1.4 validation S5Q011. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **B:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **C:** Correct. allows safe iteration on draft specs like Tasks and elicitation without polluting the stable capability surface.
- **D:** Incorrect. logging full tool arguments including customer PII and bearer tokens creates GDPR and credential-leak second-order risks.

### Question 12 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). Selecting this honors Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Skill 1.4 validation S5Q012. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **B:** Correct. lets each party call only negotiated features, avoiding methodNotFound and silent fallback hallucinations.
- **C:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.
- **D:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.

### Question 13 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). This follows the MCP specification for Manage keepalive pings, progress notifications, cancellation, and shutdown semantics, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Reference 1.5 S5Q013. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. ad-hoc tool creation without validation and massive single-block responses break type safety and token budgets.
- **B:** Incorrect. missing inputSchema and raw shell interpolation from unvalidated LLM strings creates prompt-injection and RCE risk.
- **C:** Correct. matches MCP Tools spec: declarative schema, client discovery, validated execution, and structured content/error signaling.
- **D:** Incorrect. responding before validation and ignoring list_changed events leaves clients with stale, unvalidated tool catalogs.

### Question 14 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). MCP 2025-11-25 requires Manage keepalive pings, progress notifications, cancellation, and shutdown semantics; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 1.5 validation S5Q014. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.
- **B:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **C:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.
- **D:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.

### Question 15 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). This follows the MCP specification for Manage keepalive pings, progress notifications, cancellation, and shutdown semantics, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 1.5 validation S5Q015. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. gracefully aborts model-driven tool storms while freeing server resources and meeting JSON-RPC cancellation semantics.
- **B:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.
- **C:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **D:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.

### Question 16 — `D, E` (MCP Foundations, Architecture & Lifecycle)

Correct answers: D and E (are correct). Selecting this honors Differentiate MCP from function calling, A2A, and experimental capability progression and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Skill 1.6 validation S5Q016. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Incorrect. printing logs to stdout alongside JSON-RPC breaks line-delimited parsing and throws Parse error -32700.
- **B:** Incorrect. calling tools before the initialized handshake completes races capability discovery and throws methodNotFound errors.
- **C:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **D:** Correct. clarifies layer boundaries: MCP standardizes context attachment; function calling is inline model schema; A2A negotiates task handoffs.
- **E:** Correct. uses MCP vertically for capabilities and A2A horizontally for peer negotiation, per LM-Foundation AAIF stack guidance.

### Question 17 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). This follows the MCP specification for Differentiate MCP from function calling, A2A, and experimental capability progression, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 1.6 validation S5Q017. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.
- **B:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.
- **C:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.
- **D:** Correct. allows safe iteration on draft specs like Tasks and elicitation without polluting the stable capability surface.

### Question 18 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). MCP 2025-11-25 requires Differentiate MCP from function calling, A2A, and experimental capability progression; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 1.6 validation S5Q018. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Correct. allows safe iteration on draft specs like Tasks and elicitation without polluting the stable capability surface.
- **B:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.
- **C:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **D:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.

### Question 19 — `B, D` (Tools, Resources & Resource Templates)

Correct answers: B and D (are correct). This follows the MCP specification for Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 2.1 validation S5Q019. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.
- **B:** Correct. uses typed server helpers that auto-wire tools/list/call handlers and JSON Schema validation from Zod objects.
- **C:** Incorrect. printing logs to stdout alongside JSON-RPC breaks line-delimited parsing and throws Parse error -32700.
- **D:** Correct. gives models complete, machine-validated contracts for tool selection and argument generation.
- **E:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.

### Question 20 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). MCP 2025-11-25 requires Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 2.1 validation S5Q020. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. logging full tool arguments including customer PII and bearer tokens creates GDPR and credential-leak second-order risks.
- **B:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.
- **C:** Correct. preserves user/model agency and auditability; every mutation traces to an explicit model decision with tool audit event.
- **D:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.

### Question 21 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). This choice correctly implements Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints for OmniCart Commerce Ops while the distractors violate transport/session guarantees. Skill 2.1 validation S5Q021. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. uses typed server helpers that auto-wire tools/list/call handlers and JSON Schema validation from Zod objects.
- **B:** Incorrect. parsing free-form chat replies as structured data instead of typed elicitation invites format errors and injection.
- **C:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.
- **D:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.

### Question 22 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). Per MCP 2025-11-25, Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 2.1 validation S5Q022. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.
- **B:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **C:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.
- **D:** Correct. preserves user/model agency and auditability; every mutation traces to an explicit model decision with tool audit event.

### Question 23 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). This follows the MCP specification for Control model-controlled tool execution, list discovery, validation, and structured content output, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 2.2 validation S5Q023. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **B:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **C:** Incorrect. collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.
- **D:** Correct. defends against LLM hallucinated args and preserves typed error handling via isError flag versus exception propagation.

### Question 24 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). This follows the MCP specification for Control model-controlled tool execution, list discovery, validation, and structured content output, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 2.2 validation S5Q024. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.
- **B:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **C:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.
- **D:** Correct. preserves user/model agency and auditability; every mutation traces to an explicit model decision with tool audit event.

### Question 25 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Selecting this honors Control model-controlled tool execution, list discovery, validation, and structured content output and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Skill 2.2 validation S5Q025. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.
- **B:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **C:** Correct. lets clients render multimodal results safely while distinguishing success from app-level errors without parsing text.
- **D:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.

### Question 26 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). Selecting this honors Control model-controlled tool execution, list discovery, validation, and structured content output and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Skill 2.2 validation S5Q026. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. treating MCP as a replacement for A2A agent discovery and task lifecycles conflates vertical tool attachment with peer delegation.
- **B:** Correct. defends against LLM hallucinated args and preserves typed error handling via isError flag versus exception propagation.
- **C:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **D:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.

### Question 27 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). This follows the MCP specification for Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Reference 2.3 S5Q027. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. omitting uri and mimeType fields and ignoring pagination cursors makes resources unaddressable and unfilterable.
- **B:** Incorrect. guessing URIs and exposing raw OS paths without scheme checks violates resource discovery and isolation.
- **C:** Correct. follows Resources spec: capability advertisement, list/template discovery, uri-addressed reads with mime-typed contents and pagination.
- **D:** Incorrect. tight polling without subscription to list_changed notifications defeats MCP push efficiency and protocol layering.

### Question 28 — `A, D` (Tools, Resources & Resource Templates)

Correct answers: A and D (are correct). This choice correctly implements Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed for OmniCart Commerce Ops while the distractors violate transport/session guarantees. Skill 2.3 validation S5Q028. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Correct. pushes freshness efficiently after external ingestion jobs create new datasets, without constant re-list overhead.
- **B:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **C:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **D:** Correct. handles 10k-file workspaces without truncation or timeout, matching MCP pagination contract for both lists.
- **E:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.

### Question 29 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). This choice correctly implements Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed for OmniCart Commerce Ops while the distractors violate transport/session guarantees. Skill 2.3 validation S5Q029. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.
- **B:** Correct. pushes freshness efficiently after external ingestion jobs create new datasets, without constant re-list overhead.
- **C:** Incorrect. generating random progressTokens server-side with no binding to request id mixes streams across concurrent tasks.
- **D:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.

### Question 30 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). Per MCP 2025-11-25, Address direct resources vs templated resources with URI schemes, names, and mimeTypes ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 2.4 validation S5Q030. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. signals cost/safety posture without hard-coding policy; models prefer readOnly before destructive in multi-step plans.
- **B:** Incorrect. distributing servers as raw GitHub tarballs without server.json or publisher proof hides supply-chain compromise.
- **C:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **D:** Incorrect. logging full tool arguments including customer PII and bearer tokens creates GDPR and credential-leak second-order risks.

### Question 31 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). This choice correctly implements Address direct resources vs templated resources with URI schemes, names, and mimeTypes for OmniCart Commerce Ops while the distractors violate transport/session guarantees. Skill 2.4 validation S5Q031. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. signals cost/safety posture without hard-coding policy; models prefer readOnly before destructive in multi-step plans.
- **B:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.
- **C:** Incorrect. treating MCP as a replacement for A2A agent discovery and task lifecycles conflates vertical tool attachment with peer delegation.
- **D:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.

### Question 32 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). This follows the MCP specification for Address direct resources vs templated resources with URI schemes, names, and mimeTypes, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 2.4 validation S5Q032. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.
- **B:** Correct. signals cost/safety posture without hard-coding policy; models prefer readOnly before destructive in multi-step plans.
- **C:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.
- **D:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.

### Question 33 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). Per MCP 2025-11-25, Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 2.5 validation S5Q033. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Correct. keeps IDE diagnostics in sync with file edits without polling, per spec subscription lifecycle.
- **B:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **C:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.
- **D:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.

### Question 34 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). This choice correctly implements Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows for OmniCart Commerce Ops while the distractors violate transport/session guarantees. Skill 2.5 validation S5Q034. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **B:** Correct. keeps IDE diagnostics in sync with file edits without polling, per spec subscription lifecycle.
- **C:** Incorrect. collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.
- **D:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.

### Question 35 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Selecting this honors Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Skill 2.5 validation S5Q035. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **B:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.
- **C:** Correct. handles 10k-file workspaces without truncation or timeout, matching MCP pagination contract for both lists.
- **D:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.

### Question 36 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). MCP 2025-11-25 requires Declare prompts and completions for argument typeahead and parameterized prompt expansion; the alternative breaks capability negotiation or security for commerce checkout flow. Reference 2.6 S5Q036. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. exposing full drive without consent and walking above root boundaries with symlink following enables directory traversal.
- **B:** Incorrect. letting servers dictate client filesystem boundaries inverts MCP trust and breaks host isolation.
- **C:** Incorrect. hardcoding roots and ignoring list_changed notifications leaves stale boundaries after user permission changes.
- **D:** Correct. implements Roots spec: client-owned boundary declaration, server-enforced confinement, and dynamic list_changed handling.

### Question 37 — `A, C` (Tools, Resources & Resource Templates)

Correct answers: A and C (are correct). Per MCP 2025-11-25, Declare prompts and completions for argument typeahead and parameterized prompt expansion ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 2.6 validation S5Q037. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. turns curated prompt packs into discoverable UX shortcuts argument-by-argument with typed validation.
- **B:** Incorrect. logging full tool arguments including customer PII and bearer tokens creates GDPR and credential-leak second-order risks.
- **C:** Correct. compiles parameterized prompt templates server-side with validated args, keeping prompt injection surface server-controlled.
- **D:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.
- **E:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.

### Question 38 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). MCP 2025-11-25 requires Declare prompts and completions for argument typeahead and parameterized prompt expansion; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 2.6 validation S5Q038. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. turns curated prompt packs into discoverable UX shortcuts argument-by-argument with typed validation.
- **B:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **C:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **D:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.

### Question 39 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). Per MCP 2025-11-25, Expose and expand prompts via prompts/list, prompts/get, and argument validation ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 3.1 validation S5Q039. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.
- **B:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.
- **C:** Correct. turns curated prompt packs into discoverable UX shortcuts argument-by-argument with typed validation.
- **D:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.

### Question 40 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). MCP 2025-11-25 requires Expose and expand prompts via prompts/list, prompts/get, and argument validation; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 3.1 validation S5Q040. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. batching 200 unrelated tool calls into one HTTP request beyond advertised limits times out the whole batch.
- **B:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **C:** Correct. compiles parameterized prompt templates server-side with validated args, keeping prompt injection surface server-controlled.
- **D:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.

### Question 41 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). MCP 2025-11-25 requires Expose and expand prompts via prompts/list, prompts/get, and argument validation; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 3.1 validation S5Q041. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.
- **B:** Incorrect. generating random progressTokens server-side with no binding to request id mixes streams across concurrent tasks.
- **C:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **D:** Correct. turns curated prompt packs into discoverable UX shortcuts argument-by-argument with typed validation.

### Question 42 — `A, B, C` (Prompts, Sampling, Roots & Elicitation)

Correct answers: A, B, and C (are correct). This choice correctly implements Enforce client-owned filesystem boundaries via roots/list and roots/list_changed for OmniCart Commerce Ops while the distractors violate transport/session guarantees. Skill 3.2 validation S5Q042. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. gives users explicit allowlist control over which directories a server may touch, enforced server-side.
- **B:** Correct. prevents `../` and symlink hop attacks that would escape the user’s approved `file://` allowlist.
- **C:** Correct. keeps server views consistent when users add/remove workspace folders mid-session without restart.
- **D:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.
- **E:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **F:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.

### Question 43 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). MCP 2025-11-25 requires Enforce client-owned filesystem boundaries via roots/list and roots/list_changed; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 3.2 validation S5Q043. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. gives users explicit allowlist control over which directories a server may touch, enforced server-side.
- **B:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.
- **C:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.
- **D:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.

### Question 44 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). MCP 2025-11-25 requires Enforce client-owned filesystem boundaries via roots/list and roots/list_changed; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 3.2 validation S5Q044. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **B:** Correct. keeps server views consistent when users add/remove workspace folders mid-session without restart.
- **C:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.
- **D:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.

### Question 45 — `A, C` (Prompts, Sampling, Roots & Elicitation)

Correct answers: A and C (are correct). MCP 2025-11-25 requires Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 3.3 validation S5Q045. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. lets servers delegate LLM sub-tasks (summarization, critique) back to the Host model under explicit preference caps.
- **B:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **C:** Correct. maps server intent to Host model fleet tiers without hardcoding vendor model IDs into server code.
- **D:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **E:** Incorrect. generating random progressTokens server-side with no binding to request id mixes streams across concurrent tasks.

### Question 46 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). Selecting this honors Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Skill 3.3 validation S5Q046. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **B:** Correct. maps server intent to Host model fleet tiers without hardcoding vendor model IDs into server code.
- **C:** Incorrect. enabling experimental tasks by default without capability checks forces unready clients into breaking draft methods.
- **D:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.

### Question 47 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). Selecting this honors Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Skill 3.3 validation S5Q047. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. lets servers delegate LLM sub-tasks (summarization, critique) back to the Host model under explicit preference caps.
- **B:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.
- **C:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **D:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.

### Question 48 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). Per MCP 2025-11-25, Collect human input via elicitation/create with requestedSchema and form round-trips ensures spec-compliant lifecycle and isolation for commerce checkout flow. Reference 3.4 S5Q048. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. default-exposed sampling and uncapped recursive loops risk token runaway and expose internal reasoning inappropriately.
- **B:** Incorrect. confusing sampling payloads with tool metadata conflates delegation layers and breaks cost attribution.
- **C:** Incorrect. unbounded PII-laden sampling without capability or consent bypasses privacy and authorization boundaries.
- **D:** Correct. follows Sampling spec: capability-checked server-initiated LLM delegation with explicit modelPreferences and human approval gating.

### Question 49 — `A, E` (Prompts, Sampling, Roots & Elicitation)

Correct answers: A and E (are correct). This follows the MCP specification for Collect human input via elicitation/create with requestedSchema and form round-trips, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 3.4 validation S5Q049. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. separates fact acquisition (user-filled forms) from subjective generation (model-composed prose) for audit clarity.
- **B:** Incorrect. labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.
- **C:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **D:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.
- **E:** Correct. turns server data needs into typed Host-rendered forms rather than chat text parsing, with explicit schema validation.

### Question 50 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). This choice correctly implements Collect human input via elicitation/create with requestedSchema and form round-trips for OmniCart Commerce Ops while the distractors violate transport/session guarantees. Skill 3.4 validation S5Q050. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. lets servers delegate LLM sub-tasks (summarization, critique) back to the Host model under explicit preference caps.
- **B:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **C:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **D:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.

### Question 51 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). Per MCP 2025-11-25, Regulate verbosity via logging/setLevel and notifications/message level filtering ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 3.5 validation S5Q051. [Skill 3.5: Regulate verbosity via logging/setLevel and notifications/message level filtering | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/logging/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **B:** Correct. correlates streaming progress notifications to the correct in-flight tool/resource fetch without guessing.
- **C:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.
- **D:** Incorrect. assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.

### Question 52 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). MCP 2025-11-25 requires Regulate verbosity via logging/setLevel and notifications/message level filtering; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 3.5 validation S5Q052. [Skill 3.5: Regulate verbosity via logging/setLevel and notifications/message level filtering | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/logging/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **B:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **C:** Correct. respects user-selected verbosity while still flowing warnings/errors through observability pipelines.
- **D:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.

### Question 53 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). Per MCP 2025-11-25, Correlate progress and completion flows with progressToken and completion/complete semantics ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 3.6 validation S5Q053. [Skill 3.6: Correlate progress and completion flows with progressToken and completion/complete semantics | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/prompts]

- **A:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **B:** Correct. powers low-latency autocomplete dropdowns directly from server-side datasets without tool execution overhead.
- **C:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **D:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.

### Question 54 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). Per MCP 2025-11-25, Correlate progress and completion flows with progressToken and completion/complete semantics ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 3.6 validation S5Q054. [Skill 3.6: Correlate progress and completion flows with progressToken and completion/complete semantics | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/prompts]

- **A:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.
- **B:** Correct. enables UX-level typeahead without invoking costly tools, scoped to declared completion capabilities.
- **C:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **D:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.

### Question 55 — `D, E, F` (Transports, Sessions & Protocol Evolution)

Correct answers: D, E, and F (are correct). This follows the MCP specification for Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 4.1 validation S5Q055. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.
- **B:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **C:** Incorrect. collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.
- **D:** Correct. prevents log interleaving from corrupting JSON-RPC framing that parsers expect line-delimited on stdout.
- **E:** Correct. gives OS-level isolation, clean env var scoping, and automatic teardown when Host exits without port conflicts.
- **F:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.

### Question 56 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). This choice correctly implements Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle for OmniCart Commerce Ops while the distractors violate transport/session guarantees. Skill 4.1 validation S5Q056. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.
- **B:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **C:** Incorrect. generating random progressTokens server-side with no binding to request id mixes streams across concurrent tasks.
- **D:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.

### Question 57 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). This follows the MCP specification for Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 4.1 validation S5Q057. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **B:** Correct. gives OS-level isolation, clean env var scoping, and automatic teardown when Host exits without port conflicts.
- **C:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.
- **D:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.

### Question 58 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). MCP 2025-11-25 requires Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response); the alternative breaks capability negotiation or security for commerce checkout flow. Reference 4.2 S5Q058. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. unbounded batching and cross-tenant session ID reuse breaks rate limiting and tenant isolation guarantees.
- **B:** Incorrect. returning HTML instead of JSON-RPC errors and retrying without backoff causes parsing failures and duplicate mutations.
- **C:** Incorrect. splitting endpoints and ignoring session/resumability headers reverts to pre-March 2025 deprecated SSE transport.
- **D:** Correct. matches 2025-11-25 Streamable HTTP spec: single endpoint, dual Accept, session ID management, and resumable SSE stream option.

### Question 59 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). Selecting this honors Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Skill 4.2 validation S5Q059. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.
- **B:** Correct. lets simple request/reply skip SSE overhead while enabling streaming only for long-running tool progress.
- **C:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **D:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.

### Question 60 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). Selecting this honors Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Skill 4.2 validation S5Q060. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. lets simple request/reply skip SSE overhead while enabling streaming only for long-running tool progress.
- **B:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **C:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.
- **D:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.

### Question 61 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). Per MCP 2025-11-25, Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 4.3 validation S5Q061. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.
- **B:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **C:** Correct. recovers progress streams and notifications lost during 5–30s mobile handoffs without missing tool progress events.
- **D:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.

### Question 62 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). Per MCP 2025-11-25, Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 4.3 validation S5Q062. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **B:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.
- **C:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.
- **D:** Correct. recovers progress streams and notifications lost during 5–30s mobile handoffs without missing tool progress events.

### Question 63 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). This follows the MCP specification for Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 4.3 validation S5Q063. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **B:** Incorrect. printing logs to stdout alongside JSON-RPC breaks line-delimited parsing and throws Parse error -32700.
- **C:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **D:** Correct. tracks spec evolution: split GET /sse + POST /messages merged into single POST with Accept-driven streaming.

### Question 64 — `A, D` (Transports, Sessions & Protocol Evolution)

Correct answers: A and D (are correct). Per MCP 2025-11-25, Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 4.4 validation S5Q064. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Correct. tracks spec evolution: split GET /sse + POST /messages merged into single POST with Accept-driven streaming.
- **B:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.
- **C:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **D:** Correct. avoids thundering herds after gateway restarts while ensuring exactly-once progress recovery via resumability.
- **E:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.

### Question 65 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). Per MCP 2025-11-25, Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 4.4 validation S5Q065. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Correct. tracks spec evolution: split GET /sse + POST /messages merged into single POST with Accept-driven streaming.
- **B:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.
- **C:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.
- **D:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.

### Question 66 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). MCP 2025-11-25 requires Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 4.4 validation S5Q066. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **B:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.
- **C:** Correct. tracks spec evolution: split GET /sse + POST /messages merged into single POST with Accept-driven streaming.
- **D:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.

### Question 67 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). MCP 2025-11-25 requires Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 4.5 validation S5Q067. [Skill 4.5: Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/progress/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. skipping Inspector and relying only on unit mocks misses real transport framing and pagination/cancellation bugs.
- **B:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.
- **C:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **D:** Correct. keeps MCP semantics intact through enterprise L7 filters that otherwise strip SSE headers and session sticky state.

### Question 68 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). Per MCP 2025-11-25, Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 4.5 validation S5Q068. [Skill 4.5: Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/progress/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.
- **B:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.
- **C:** Correct. exploits batching for listing throughput without overwhelming server concurrency caps or mixing response IDs.
- **D:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.

### Question 69 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). Selecting this honors Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Skill 4.6 validation S5Q069. [Skill 4.6: Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/cancellation/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **B:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.
- **C:** Incorrect. labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.
- **D:** Correct. keeps MCP semantics intact through enterprise L7 filters that otherwise strip SSE headers and session sticky state.

### Question 70 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). MCP 2025-11-25 requires Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 4.6 validation S5Q070. [Skill 4.6: Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/cancellation/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. avoids thundering herds after gateway restarts while ensuring exactly-once progress recovery via resumability.
- **B:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **C:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **D:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.

### Question 71 — `A, B, D` (Authorization, Security, Trust & Registry)

Correct answers: A, B, and D (are correct). This choice correctly implements Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata for OmniCart Commerce Ops while the distractors violate transport/session guarantees. Skill 5.1 validation S5Q071. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.
- **B:** Correct. aligns MCP with current OAuth 2.1 security posture, eliminating token leakage vectors of legacy grants.
- **C:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **D:** Correct. scales zero-touch onboarding across thousands of tenant Host instances without manual client_id provisioning.
- **E:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.
- **F:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.

### Question 72 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). This follows the MCP specification for Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 5.1 validation S5Q072. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.
- **B:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **C:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.
- **D:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.

### Question 73 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). This choice correctly implements Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata for OmniCart Commerce Ops while the distractors violate transport/session guarantees. Skill 5.1 validation S5Q073. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **B:** Correct. scales zero-touch onboarding across thousands of tenant Host instances without manual client_id provisioning.
- **C:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.
- **D:** Incorrect. setting includeContext=allServers by default fans sensitive data from every connected server into one sampling call.

### Question 74 — `A` (Authorization, Security, Trust & Registry)

Correct answer: A (is correct). MCP 2025-11-25 requires Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 5.2 validation S5Q074. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Correct. binds public client identity to TLS-verifiable origin without long-lived client secrets in distributed Hosts.
- **B:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **C:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **D:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.

### Question 75 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). This choice correctly implements Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings for OmniCart Commerce Ops while the distractors violate transport/session guarantees. Skill 5.2 validation S5Q075. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **B:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **C:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **D:** Correct. binds public client identity to TLS-verifiable origin without long-lived client secrets in distributed Hosts.

### Question 76 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). Per MCP 2025-11-25, Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 5.2 validation S5Q076. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Incorrect. requiring clients to poll list on a timer to detect new resources defeats MCP push efficiency.
- **B:** Correct. supports desktop IDE/CLI auth via ephemeral loopback listeners while forbidding http redirects to remote hosts.
- **C:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.
- **D:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.

### Question 77 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). This choice correctly implements Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality for OmniCart Commerce Ops while the distractors violate transport/session guarantees. Reference 5.3 S5Q077. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Incorrect. exposing secrets in client bundles and downgrading PKCE/TLS undermines OAuth confidentiality and channel binding.
- **B:** Incorrect. hardcoded keys and alg:none tokens with blanket admin grants violate OAuth 2.1 and privilege separation.
- **C:** Correct. follows MCP auth spec evolution: OAuth 2.1 with PKCE, protected resource metadata, RFC 8707 audience binding, and RFC 9207 issuer checks.
- **D:** Incorrect. reusing a single audience-less token across resource servers enables cross-server token replay and mix-up attacks.

### Question 78 — `A` (Authorization, Security, Trust & Registry)

Correct answer: A (is correct). This choice correctly implements Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality for OmniCart Commerce Ops while the distractors violate transport/session guarantees. Skill 5.3 validation S5Q078. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Correct. binds public client identity to TLS-verifiable origin without long-lived client secrets in distributed Hosts.
- **B:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **C:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.
- **D:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.

### Question 79 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). Selecting this honors Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Skill 5.3 validation S5Q079. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **B:** Correct. enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.
- **C:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.
- **D:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.

### Question 80 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). MCP 2025-11-25 requires Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 5.4 validation S5Q080. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **B:** Incorrect. calling tools before the initialized handshake completes races capability discovery and throws methodNotFound errors.
- **C:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.
- **D:** Correct. displays descriptions for human review but never concatenates them into system prompts or plan steps as trusted policy.

### Question 81 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). Selecting this honors Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Skill 5.4 validation S5Q081. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.
- **B:** Correct. stops a docs MCP server from using its tool output to call a payment MCP’s `transfer` tool via implicit ambient authority.
- **C:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.
- **D:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.

### Question 82 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). This follows the MCP specification for Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 5.4 validation S5Q082. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **B:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.
- **C:** Correct. tags third-party fetched content so downstream Hosts can sandtrap it before the model treats it as instruction.
- **D:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.

### Question 83 — `A, C` (Authorization, Security, Trust & Registry)

Correct answers: A and C (are correct). MCP 2025-11-25 requires Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 5.5 validation S5Q083. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Correct. prevents a malicious calendar server from harvesting `AWS_SECRET_ACCESS_KEY` and `GITHUB_PAT` from Host env dump.
- **B:** Incorrect. implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.
- **C:** Correct. provides supply-chain tamper evidence via package signing and publisher identity beyond raw GitHub stars.
- **D:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.
- **E:** Incorrect. setting includeContext=allServers by default fans sensitive data from every connected server into one sampling call.

### Question 84 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). MCP 2025-11-25 requires Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 5.5 validation S5Q084. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **B:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.
- **C:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.
- **D:** Correct. forces re-approval when a benign `get_weather` server silently rewires to `exfiltrate_files` after approval.

### Question 85 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). Per MCP 2025-11-25, Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 5.5 validation S5Q085. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.
- **B:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **C:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.
- **D:** Correct. enables post-incident forensics without persisting PII/tokens, keyed by stable tool provenance hashes.

### Question 86 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). This follows the MCP specification for Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic), correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 6.1 validation S5Q086. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Incorrect. implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.
- **B:** Correct. gives decorator-ergonomic tool/resource registration with Pydantic/JSON Schema coherence across Python Hosts.
- **C:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **D:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.

### Question 87 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). Per MCP 2025-11-25, Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 6.1 validation S5Q087. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.
- **B:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.
- **C:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.
- **D:** Correct. uses typed server helpers that auto-wire tools/list/call handlers and JSON Schema validation from Zod objects.

### Question 88 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). This choice correctly implements Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) for OmniCart Commerce Ops while the distractors violate transport/session guarantees. Skill 6.1 validation S5Q088. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.
- **B:** Correct. uses typed server helpers that auto-wire tools/list/call handlers and JSON Schema validation from Zod objects.
- **C:** Incorrect. implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.
- **D:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.

### Question 89 — `C, D` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: C and D (are correct). This follows the MCP specification for Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 6.2 validation S5Q089. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.
- **B:** Incorrect. generating random progressTokens server-side with no binding to request id mixes streams across concurrent tasks.
- **C:** Correct. standardizes transport selection, capability tracking, and request/notification routing behind a single Client facade.
- **D:** Correct. gives OS-level isolation, clean env var scoping, and automatic teardown when Host exits without port conflicts.
- **E:** Incorrect. distributing servers as raw GitHub tarballs without server.json or publisher proof hides supply-chain compromise.

### Question 90 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). This follows the MCP specification for Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 6.2 validation S5Q090. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Incorrect. requiring clients to poll list on a timer to detect new resources defeats MCP push efficiency.
- **B:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **C:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **D:** Correct. catches lifecycle, capability, and schema mismatches before CI with real-transport conformance testing.

### Question 91 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). Selecting this honors Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Skill 6.2 validation S5Q091. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Correct. standardizes transport selection, capability tracking, and request/notification routing behind a single Client facade.
- **B:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **C:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **D:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.

### Question 92 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). MCP 2025-11-25 requires Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 6.3 validation S5Q092. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Incorrect. dumping base64 blobs as plain text without typed content blocks loses mimeType and forces heuristic parsing.
- **B:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **C:** Correct. ensures reproducible, least-privilege runtime with declared transport and liveness for orchestrators.
- **D:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.

### Question 93 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). This follows the MCP specification for Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation, correcting the insecure/incompatible anti-pattern for commerce checkout flow. Skill 6.3 validation S5Q093. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.
- **B:** Incorrect. dumping base64 blobs as plain text without typed content blocks loses mimeType and forces heuristic parsing.
- **C:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.
- **D:** Correct. ensures reproducible, least-privilege runtime with declared transport and liveness for orchestrators.

### Question 94 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). Per MCP 2025-11-25, Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 6.3 validation S5Q094. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **B:** Correct. ensures reproducible, least-privilege runtime with declared transport and liveness for orchestrators.
- **C:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **D:** Incorrect. enabling experimental tasks by default without capability checks forces unready clients into breaking draft methods.

### Question 95 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). Selecting this honors Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Reference 6.4 S5Q095. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Correct. applies MCP security checklist: supply-chain pinning, description-vs-logic separation, consent gating, and provenance monitoring against poison/rug-pull.
- **B:** Incorrect. blind auto-approval and treating descriptions as trusted instructions invites prompt injection and supply-chain compromise.
- **C:** Incorrect. silent exfiltration without rate limits or audit visibility breaks data minimization and incident-response traceability.
- **D:** Incorrect. unvetted curl-piped installs with maximal scopes and plaintext token storage maximizes blast radius from a single malicious server.

### Question 96 — `B, C` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: B and C (are correct). Selecting this honors Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Skill 6.4 validation S5Q096. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **B:** Correct. respects user-selected verbosity while still flowing warnings/errors through observability pipelines.
- **C:** Correct. traces tool call latency through Streamable HTTP gateways into server execution with per-session correlation.
- **D:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.
- **E:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.

### Question 97 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). MCP 2025-11-25 requires Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 6.4 validation S5Q097. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Correct. powers per-tool SLOs and supply-chain forensics without persisting sensitive tool argument values.
- **B:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **C:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.
- **D:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.

### Question 98 — `C, D` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: C and D (are correct). Selecting this honors Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns and prevents the listed failure mode in OmniCart Commerce Ops commerce checkout flow flows. Skill 6.5 validation S5Q098. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **B:** Incorrect. assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.
- **C:** Correct. reuses vetted categories (databases, cloud, payments) before building bespoke wrappers over public APIs.
- **D:** Correct. centralizes AuthZ, session affinity, and observability without duplicating gateway logic in each MCP server.
- **E:** Incorrect. setting includeContext=allServers by default fans sensitive data from every connected server into one sampling call.

### Question 99 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). MCP 2025-11-25 requires Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns; the alternative breaks capability negotiation or security for commerce checkout flow. Skill 6.5 validation S5Q099. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.
- **B:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.
- **C:** Correct. reuses vetted categories (databases, cloud, payments) before building bespoke wrappers over public APIs.
- **D:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.

### Question 100 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). Per MCP 2025-11-25, Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns ensures spec-compliant lifecycle and isolation for commerce checkout flow. Skill 6.5 validation S5Q100. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **B:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.
- **C:** Correct. standardizes cross-Host deployment via portable config blocks with scoped env and per-server enable toggles.
- **D:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.
