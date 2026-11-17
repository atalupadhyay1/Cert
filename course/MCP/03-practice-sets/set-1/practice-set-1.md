# MCP: Model Context Protocol: Servers, Clients, Transports & Security — Full-Length Mock Exam 1 — Meridian Capital Trading Desk (Finance & Risk)

**Theme:** Host-Client-Server Triad, SDK Scaffolds, Tool Poisoning Defense & Registry Trust  
**Credential alignment:** `Model Context Protocol (MCP 2025-11-25) — Tool & Context Standard`  
**Blueprint baseline:** `November 2026 (MCP Specification 2025-11-25 · MCP Registry & Inspector · OAuth 2.1 + RFC 8707/9207 + CIMD · OWASP MCP Security Checklist)` (https://modelcontextprotocol.io/introduction · https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation · https://genai.owasp.org/resource/mcp-security-checklist/)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `120 minutes` (`72 seconds/question` full-endurance pacing; aligns with `120 minutes` on NVIDIA NCP-AAI & GitHub GH-600)

> **Disclaimer:** Independent educational practice material authored from public engineering specifications and open-protocol documentation — not affiliated with, sponsored by, or endorsed by NVIDIA, the Linux Foundation, Anthropic, OpenAI, Google, Microsoft, GitHub, LangChain, or OWASP. Practice scores do not guarantee passing any third-party certification exam.

## Questions

---

## Domain 1 — MCP Foundations, Architecture & Lifecycle (16–20% blueprint weight · 18 questions)

### 1. For trading risk at Meridian Capital Trading Desk, two best practices align with MCP 2025-11-25. Which two should be implemented? Select two. Alert 6080: `Mcp-Session-Id` reused across tenants. [1.1 #1]

- **A.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **B.** Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation
- **C.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **D.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **E.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks

### 2. Meridian Capital Trading Desk needs to secure trading risk tool calls that mutate production data. The right control is to ____. Incident MCP-2026-2609 shows Misconfigured `Mcp-Session-Id` routing. [1.1 #2]

- **A.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **B.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **C.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **D.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke

### 3. At Meridian Capital Trading Desk, engineers building an MCP server for trading risk need to ____. Which configuration correctly implements the MCP specification? Ticket 2648: `notifications/roots/list_changed` ignored after folder add. [1.1 #3]

- **A.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **B.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation
- **C.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **D.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs

### 4. Meridian Capital Trading Desk engineers designing an MCP system for trading risk must evaluate two correct controls. Which two statements are correct? Select two. Ticket 8289: `roots/list` poll floods client every 10 ms. [1.2 #4]

- **A.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **B.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **C.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **D.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **E.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`

### 5. An trading risk MCP gateway at Meridian Capital Trading Desk strips `Accept` negotiation headers. The fix is to ____. Ticket 1252: `notifications/roots/list_changed` ignored after folder add. [1.2 #5]

- **A.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **B.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **C.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **D.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage

### 6. At Meridian Capital Trading Desk, the MCP client code handling trading risk leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Trace 6124: 200-tool batch exceeds advertised `maxBatchSize`. [1.2 #6]

- **A.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **B.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`
- **C.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **D.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets

### 7. For trading risk at Meridian Capital Trading Desk, which ordered flow correctly implements the MCP 2025-11-25 requirement? Trace 9705 reveals truncated cursor pagination at 50 entries. Scenario 1.3-1-7.

- **A.** Scaffold via TS/Python SDK `create-server` template → test with `npx @modelcontextprotocol/inspector` (UI + CLI) → validate `tools/list` & `tools/call` against JSON Schema → publish to registry with server.json & signed attestation
- **B.** Write server without SDK types → skip Inspector testing → hand-edit server.json without schema validation → commit secrets in repo for CI
- **C.** Copy paste tool schemas from blog post → never check protocolVersion negotiation → disable capability advertisement → run Inspector without auth context
- **D.** Test only with mocked client → ignore tools/list_changed events → skip pagination tests → push container with :latest & root user

### 8. For trading risk at Meridian Capital Trading Desk, two best practices align with MCP 2025-11-25. Which two should be implemented? Select two. Log 3106: `prompt/get` uses client-side interpolation without validation. [1.3 #8]

- **A.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **B.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **C.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **D.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **E.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`

### 9. During trading risk incident triage at Meridian Capital Trading Desk, audit logs lack `requestId` correlation. The correction is to ____. Alert 2210: `Mcp-Session-Id` reused across tenants. [1.3 #9]

- **A.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **B.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **C.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **D.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`

### 10. Complete the missing MCP field: In the Meridian Capital Trading Desk trading risk server, `____` must be set to the MCP-required value to enable trading risk correctly. Ticket 5978 reports `Last-Event-ID` replay mismatch after gateway restart. [1.4 #10]

- **A.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **B.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **C.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **D.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token

### 11. During trading risk review at Meridian Capital Trading Desk, the MCP server emits debug logs at `error` level. The proper level is ____. Incident 7713: tool logic changed post-approval (rug-pull) undetected. [1.4 #11]

- **A.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **B.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **C.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **D.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks

### 12. Proposed solution: Meridian Capital Trading Desk will run the MCP server as root with host-network and skip session ID tracking for trading risk. Does this meet the MCP 2025-11-25 goal? Case 3055: registry installs via `curl¦bash` without signature check. [1.4 #12]

- **A.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **B.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **C.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **D.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)

### 13. During trading risk incident triage at Meridian Capital Trading Desk, audit logs lack `requestId` correlation. The correction is to ____. Alert 7549: `progressToken` mismatch across concurrent tool calls. [1.5 #13]

- **A.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **B.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **C.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets
- **D.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect

### 14. Meridian Capital Trading Desk handles trading risk via MCP sampling delegation. To enforce least privilege, the server should ____. Review 3849 notes `resources/list_changed` never fired after ingest. [1.5 #14]

- **A.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **B.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **C.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **D.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets

### 15. An external auditor flags that Meridian Capital Trading Desk MCP deployment for trading risk stores bearer tokens insecurely. The correction is to ____. Review 5531: `completion/complete` implemented as heavy tool call. [1.5 #15]

- **A.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **B.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets
- **C.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **D.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**

### 16. The Meridian Capital Trading Desk team documents the trading risk MCP flow. Which sequence of actions is spec-compliant? Audit 3032: auto-approve bypasses human consent for destructive tool. Scenario 1.6-1-16.

- **A.** Server exposes 200 tools without descriptions → client guesses arguments via prompt → server executes shell with raw LLM string → return HTML page inside isError=false
- **B.** Server returns tool result before validation → client retries with doubled args → disable tools/list_changed notifications → cache tool names forever
- **C.** Server declares tool with `name`, `description`, `inputSchema` (JSON Schema) → client `tools/list` discovers it → model calls `tools/call` with validated args → server validates, executes idempotently & returns `content` + `isError`
- **D.** Client calls undefined tool name → server creates tool on-the-fly → skip inputSchema validation → stream 50-MB blob as single text content block

### 17. Meridian Capital Trading Desk MCP server for trading risk uses static API keys in `Authorization`. The OAuth 2.1 migration is to ____. Log 9212: SSE stream without `eventId` loses progress on reconnect. [1.6 #17]

- **A.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **B.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **C.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **D.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**

### 18. When Meridian Capital Trading Desk connects its VS Code host to an MCP server for trading risk, the `roots/list` workflow should ____. Audit 3850: `includeContext=allServers` exfiltrates cross-server data. [1.6 #18]

- **A.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **B.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **C.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **D.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`

---

## Domain 2 — Tools, Resources & Resource Templates (18–22% blueprint weight · 20 questions)

### 19. To implement trading risk correctly for Meridian Capital Trading Desk, which 4-step sequence satisfies the MCP spec? Trace 3194: `resource` audience binding missing per RFC 8707. Scenario 2.1-1-19.

- **A.** Server lists resources without capability flag → client polls `resources/list` every 10 ms in loop → ignore `resources/list_changed` notifications → request resources via tools/call
- **B.** Client guesses file URIs without list → server returns OS absolute paths as uri → embed 10-MB binary as base64 JSON string → skip uri validation
- **C.** Server returns resources without uri fields → client stores resource content in tool history → server omits page cursors for 10k items → skip mimeType declaration
- **D.** Server advertises `resources` capability → client calls `resources/list` or `resources/templates/list` → client reads `resources/read` with `uri` → server returns `contents` with `mimeType`, handling pagination cursors

### 20. During trading risk rollout at Meridian Capital Trading Desk, canary hosts skip capability re-validation after reconnect. They should ____. Trace 5541: batch of 200 tool calls timed out. [2.1 #20]

- **A.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **B.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **C.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **D.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke

### 21. The Meridian Capital Trading Desk MCP configuration for trading risk shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Case 2703: Host passes full env block to untrusted calendar server. [2.1 #21]

- **A.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **B.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **C.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **D.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan

### 22. During trading risk rollout at Meridian Capital Trading Desk, canary hosts skip capability re-validation after reconnect. They should ____. Ticket 4180: plaintext `config.json` holds refresh token. [2.1 #22]

- **A.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **B.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **C.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **D.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke

### 23. For trading risk at Meridian Capital Trading Desk, two best practices align with MCP 2025-11-25. Which two should be implemented? Select two. Ticket 1246: `roots/list` poll floods client every 10 ms. [2.2 #23]

- **A.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation
- **B.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **C.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **D.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **E.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure

### 24. Meridian Capital Trading Desk wants its MCP server to support both local and remote clients for trading risk. The architecture should ____. Audit 4747: auto-approve bypasses human consent for destructive tool. [2.2 #24]

- **A.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **B.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **C.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **D.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke

### 25. For trading risk at Meridian Capital Trading Desk, the MCP Inspector UI must validate tool schemas. Which approach is correct? Audit 7168: auto-approve bypasses human consent for destructive tool. [2.2 #25]

- **A.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **B.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification
- **C.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **D.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking

### 26. The MCP Inspector highlights `____` as missing for trading risk at Meridian Capital Trading Desk. Which completion is spec-correct? Case 8931: `structuredContent` missing despite `outputSchema` declared. [2.2 #26]

- **A.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **B.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean
- **C.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **D.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)

### 27. Which three statements accurately describe MCP trading risk transport and security semantics for Meridian Capital Trading Desk? Select three. Incident MCP-2026-6903 shows Misconfigured `Mcp-Session-Id` routing. [2.3 #27]

- **A.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)
- **B.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **C.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **D.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **E.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **F.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent

### 28. For trading risk, Meridian Capital Trading Desk must handle `notifications/progress` vs polling. The correct pattern is to ____. Trace 5117 reveals truncated cursor pagination at 50 entries. [2.3 #28]

- **A.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **B.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **C.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **D.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds

### 29. In `Meridian Capital Trading Desk` `trading risk` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Ticket 3538: `roots/list` poll floods client every 10 ms. [2.3 #29]

- **A.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **B.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **C.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **D.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`

### 30. Meridian Capital Trading Desk engineers designing an MCP system for trading risk must evaluate two correct controls. Which two statements are correct? Select two. Incident 6523: OAuth PKCE verifier omitted for public client. [2.4 #30]

- **A.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **B.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean
- **C.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **D.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **E.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**

### 31. An external auditor flags that Meridian Capital Trading Desk MCP deployment for trading risk stores bearer tokens insecurely. The correction is to ____. Case 5162: Host passes full env block to untrusted calendar server. [2.4 #31]

- **A.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **B.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **C.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **D.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`

### 32. During an trading risk workflow audit at Meridian Capital Trading Desk, you notice the MCP server exposes file paths without proper checks. The team must ____. Log entry 6326 shows `Method not found -32601` without capability check. [2.4 #32]

- **A.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **B.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **C.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **D.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping

### 33. A Meridian Capital MCP client for trading risk must ____ to satisfy the protocol. What is the correct implementation approach? Trace 7320: `resource` audience binding missing per RFC 8707. [2.5 #33]

- **A.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure
- **B.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **C.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **D.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible

### 34. Meridian Capital Trading Desk needs to secure trading risk tool calls that mutate production data. The right control is to ____. Review 6747: `completion/complete` implemented as heavy tool call. [2.5 #34]

- **A.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **B.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **C.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **D.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible

### 35. Meridian Capital Trading Desk wants trading risk MCP completions for enum arguments. The valid method is ____. Trace 8744 reveals truncated cursor pagination at 50 entries. [2.5 #35]

- **A.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **B.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation
- **C.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **D.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`

### 36. In `Meridian Capital Trading Desk` `trading risk` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Incident 9015: OAuth PKCE verifier omitted for public client. Scenario 2.6-1-36.

- **A.** Server declares client roots unilaterally → client trusts arbitrary server-provided paths → skip roots/list → ignore list_changed notifications
- **B.** Client declares `roots` capability with `file://` allowlist → server calls `roots/list` to learn boundaries → server restricts `resources/read` & tool file ops to those roots → handle `notifications/roots/list_changed`
- **C.** Server hardcodes `roots/list` response → client polls filesystem without notification channel → skip name/uri validation → cache roots forever
- **D.** Client exposes entire `C:\` without consent → server walks parent directories above declared roots → disable path canonicalization → follow symlinks blindly

### 37. You are reviewing an MCP implementation for Meridian Capital Trading Desk that handles trading risk. Which statement about ____ is accurate under MCP 2025-11-25? Audit 1573 flags `alg:none` token acceptance in staging. [2.6 #37]

- **A.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **B.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **C.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **D.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan

### 38. Complete the missing MCP field: In the Meridian Capital Trading Desk trading risk server, `____` must be set to the MCP-required value to enable trading risk correctly. Alert 9158: `progressToken` mismatch across concurrent tool calls. [2.6 #38]

- **A.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **B.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **C.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **D.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages

---

## Domain 3 — Prompts, Sampling, Roots & Elicitation (14–18% blueprint weight · 16 questions)

### 39. For trading risk at Meridian Capital Trading Desk, two best practices align with MCP 2025-11-25. Which two should be implemented? Select two. Log 8129: `initialize` skipped before `tools/list`. [3.1 #39]

- **A.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **B.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **C.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **D.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **E.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping

### 40. Complete the missing MCP field: In the Meridian Capital Trading Desk trading risk server, `____` must be set to the MCP-required value to enable trading risk correctly. Incident 6466: tool logic changed post-approval (rug-pull) undetected. [3.1 #40]

- **A.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **B.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`
- **C.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean
- **D.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs

### 41. Meridian Capital Trading Desk reports intermittent `Method not found -32601` errors when accessing trading risk. To fix this, the team should ____. Log 7116: `prompt/get` uses client-side interpolation without validation. [3.1 #41]

- **A.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **B.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **C.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **D.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds

### 42. For trading risk at Meridian Capital Trading Desk, two best practices align with MCP 2025-11-25. Which two should be implemented? Select two. Trace 6586 reveals truncated cursor pagination at 50 entries. [3.2 #42]

- **A.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **B.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **C.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **D.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **E.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`

### 43. In `Meridian Capital Trading Desk` `trading risk` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Review 5417: `outputSchema` mismatched to `structuredContent` shape. [3.2 #43]

- **A.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **B.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **C.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **D.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes

### 44. During trading risk load testing at Meridian Capital Trading Desk, Streamable HTTP sessions terminate behind an ALB idle timeout. The team should ____. Incident 8376: tool logic changed post-approval (rug-pull) undetected. [3.2 #44]

- **A.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`
- **B.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **C.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **D.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads

### 45. The MCP Inspector highlights `____` as missing for trading risk at Meridian Capital Trading Desk. Which completion is spec-correct? Review 3784: `outputSchema` mismatched to `structuredContent` shape. [3.3 #45]

- **A.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **B.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`
- **C.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **D.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`

### 46. Meridian Capital Trading Desk plans to publish its trading risk MCP server to the registry. The publishing step should ____. Incident 9080: deprecated `/sse` + `/messages` split endpoint still in prod. [3.3 #46]

- **A.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **B.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **C.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs
- **D.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation

### 47. A trading risk MCP extension at Meridian Capital Trading Desk leaks `Mcp-Session-Id` across tenants. The team must ____. Audit 2265: `includeContext=allServers` exfiltrates cross-server data. [3.3 #47]

- **A.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`
- **B.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **C.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **D.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect

### 48. Meridian Capital Trading Desk sees its trading risk MCP tool return large binary blobs inline. The spec-compliant return is to ____. Trace 3447 reveals truncated cursor pagination at 50 entries. [3.4 #48]

- **A.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`
- **B.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **C.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params
- **D.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization

### 49. For trading risk at Meridian Capital Trading Desk, the MCP Inspector UI must validate tool schemas. Which approach is correct? Log 5046: SSE stream without `eventId` loses progress on reconnect. [3.4 #49]

- **A.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **B.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **C.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **D.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`

### 50. Proposed solution: Meridian Capital Trading Desk will poll resources/list every 10 ms instead of subscribing to list_changed for trading risk. Does this meet the MCP 2025-11-25 goal? Incident 8209: tool logic changed post-approval (rug-pull) undetected. [3.4 #50]

- **A.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **B.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **C.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **D.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`

### 51. Meridian Capital Trading Desk MCP server for trading risk requires two valid security hardening steps. Which two should you apply? Select two. Log 3163: `prompt/get` uses client-side interpolation without validation. [3.5 #51]

- **A.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request
- **B.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`
- **C.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`
- **D.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **E.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads

### 52. During an trading risk workflow audit at Meridian Capital Trading Desk, you notice the MCP server exposes file paths without proper checks. The team must ____. Trace 4701 reveals truncated cursor pagination at 50 entries. [3.5 #52]

- **A.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **B.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **C.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **D.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request

### 53. What is the correct 4-step order for trading risk workflow at Meridian Capital Trading Desk under MCP 2025-11-25? Review 4113: sampling loop lacks depth cap and cost budget. Scenario 3.6-1-53.

- **A.** Client exposes sampling by default without opt-in → server loops sampling/createMessage recursively → ignore modelPreferences hints → return raw chain-of-thought as tool output
- **B.** Server advertises sampling need → checks client `sampling` capability → sends `sampling/createMessage` with `messages`, `maxTokens`, `modelPreferences` → client applies human-in-loop gating & returns generation
- **C.** Server sends sampling without capability check → include raw customer PII in messages → skip maxTokens limits → client auto-executes without user consent
- **D.** Server mixes sampling messages into tool descriptions → client forwards without isolation → skip cost tracking → cache sampling results as facts

### 54. When Meridian Capital Trading Desk connects its VS Code host to an MCP server for trading risk, the `roots/list` workflow should ____. Incident MCP-2026-7104 shows Misconfigured `Mcp-Session-Id` routing. [3.6 #54]

- **A.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params
- **B.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **C.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **D.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle

---

## Domain 4 — Transports, Sessions & Protocol Evolution (14–18% blueprint weight · 16 questions)

### 55. The Meridian Capital Trading Desk MCP configuration for trading risk shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Ticket 5020: `roots/list` poll floods client every 10 ms. [4.1 #55]

- **A.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **B.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **C.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **D.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414

### 56. During trading risk rollout at Meridian Capital Trading Desk, canary hosts skip capability re-validation after reconnect. They should ____. Log entry 4977 shows `Method not found -32601` without capability check. [4.1 #56]

- **A.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **B.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **C.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **D.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params

### 57. Meridian Capital Trading Desk wants to add prompt packs for trading risk. The MCP-compliant way is to ____. Trace 6496: `resource` audience binding missing per RFC 8707. [4.1 #57]

- **A.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **B.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **C.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **D.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`

### 58. Three best practices for trading risk under MCP 2025-11-25 apply to Meridian Capital Trading Desk. Which three should be chosen? Select three. Ticket 4923 reports `Last-Event-ID` replay mismatch after gateway restart. [4.2 #58]

- **A.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **B.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **C.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **D.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params
- **E.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **F.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`

### 59. For trading risk, Meridian Capital Trading Desk must choose between stdio and Streamable HTTP transports. The correct choice is to ____. Audit 3327: auto-approve bypasses human consent for destructive tool. [4.2 #59]

- **A.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **B.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`
- **C.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **D.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token

### 60. A third-party trading risk MCP server at Meridian Capital Trading Desk silently changes tool logic after approval. The defense is to ____. Ticket 6433: `notifications/roots/list_changed` ignored after folder add. [4.2 #60]

- **A.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **B.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **C.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **D.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent

### 61. Meridian Capital Trading Desk must fix its trading risk MCP integration. Which two changes bring it into spec compliance? Select two. Ticket 9081: `roots/list` poll floods client every 10 ms. [4.3 #61]

- **A.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **B.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **C.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **D.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **E.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`

### 62. Complete the missing MCP field: In the Meridian Capital Trading Desk trading risk server, `____` must be set to the MCP-required value to enable trading risk correctly. Log 2331: `prompt/get` uses client-side interpolation without validation. [4.3 #62]

- **A.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)
- **B.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **C.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **D.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs

### 63. Complete the missing MCP field: In the Meridian Capital Trading Desk trading risk server, `____` must be set to the MCP-required value to enable trading risk correctly. Incident 5650: tool `inputSchema` validation skipped, injection observed. [4.3 #63]

- **A.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds
- **B.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **C.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **D.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`

### 64. Proposed solution: skip issuer validation and accept bearer tokens from any alg:none issuer is suggested for trading risk at Meridian Capital Trading Desk. Does this meet the goal? Case 8493: registry installs via `curl¦bash` without signature check. [4.4 #64]

- **A.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **B.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **C.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **D.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context

### 65. Meridian Capital Trading Desk MCP server for trading risk is deployed as root container with `:latest`. The secure packaging is to ____. Incident 5425: OAuth PKCE verifier omitted for public client. [4.4 #65]

- **A.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **B.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **C.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **D.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics

### 66. At Meridian Capital Trading Desk, the MCP client code handling trading risk leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Case 6142: `structuredContent` missing despite `outputSchema` declared. [4.4 #66]

- **A.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **B.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **C.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **D.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`

### 67. Complete the missing MCP field: In the Meridian Capital Trading Desk trading risk server, `____` must be set to the MCP-required value to enable trading risk correctly. Alert 8463: `isError:false` with HTML error page masks failure. Scenario 4.5-1-67.

- **A.** Client sends batched 100 requests without server batch ack → server streams without event IDs → skip session expiry handling → leak session IDs across tenants
- **B.** Server returns 200 OK with HTML error page → client retries without backoff → disable idempotency on non-idempotent tool calls → omit Content-Type validation
- **C.** Client POSTs JSON-RPC to single `mcp` endpoint with `Content-Type: application/json` & `Accept: text/event-stream, application/json` → server may respond with single JSON or SSE stream → client honors `Mcp-Session-Id` & `Last-Event-ID` for resumability
- **D.** Client opens separate GET /sse and POST /message SSE endpoints → send JSON without Accept header → ignore Mcp-Session-Id → close stream after each chunk without Last-Event-ID

### 68. During trading risk load testing at Meridian Capital Trading Desk, Streamable HTTP sessions terminate behind an ALB idle timeout. The team should ____. Ticket 2970 reports `Last-Event-ID` replay mismatch after gateway restart. [4.5 #68]

- **A.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **B.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **C.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **D.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect

### 69. At Meridian Capital Trading Desk, engineers building an MCP server for trading risk need to ____. Which configuration correctly implements the MCP specification? Incident 9477: deprecated `/sse` + `/messages` split endpoint still in prod. [4.6 #69]

- **A.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **B.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **C.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **D.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows

### 70. Meridian Capital Trading Desk trading risk MCP `initialize` handshake omits `capabilities`. The next step is to ____. Trace 4153: `resource` audience binding missing per RFC 8707. [4.6 #70]

- **A.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **B.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **C.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **D.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation

---

## Domain 5 — Authorization, Security, Trust & Registry (13–17% blueprint weight · 15 questions)

### 71. Meridian Capital Trading Desk engineers designing an MCP system for trading risk must evaluate two correct controls. Which two statements are correct? Select two. Trace 4560 reveals truncated cursor pagination at 50 entries. [5.1 #71]

- **A.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **B.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **C.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **D.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **E.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle

### 72. Meridian Capital Trading Desk plans to publish its trading risk MCP server to the registry. The publishing step should ____. Ticket 4215: plaintext `config.json` holds refresh token. [5.1 #72]

- **A.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **B.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **C.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **D.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them

### 73. During trading risk load testing at Meridian Capital Trading Desk, Streamable HTTP sessions terminate behind an ALB idle timeout. The team should ____. Log 7797: `initialize` skipped before `tools/list`. [5.1 #73]

- **A.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **B.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **C.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **D.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation

### 74. Two statements about MCP trading risk correctly reflect the specification for Meridian Capital Trading Desk. Which two are true? Select two. Review 7174: `completion/complete` implemented as heavy tool call. [5.2 #74]

- **A.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **B.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`
- **C.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **D.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **E.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files

### 75. Proposed solution: To handle trading risk, Meridian Capital Trading Desk plans to store refresh tokens in world-readable config.json and log Authorization headers. Does this satisfy the MCP specification? Incident MCP-2026-4083 shows Misconfigured `Mcp-Session-Id` routing. [5.2 #75]

- **A.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **B.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **C.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **D.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing

### 76. For trading risk at Meridian Capital Trading Desk, token storage uses plaintext `config.json`. The secure alternative is to ____. Review 2612 notes `resources/list_changed` never fired after ingest. [5.2 #76]

- **A.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **B.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **C.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`
- **D.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan

### 77. Proposed solution: cache roots forever and ignore notifications/roots/list_changed events is suggested for trading risk at Meridian Capital Trading Desk. Does this meet the goal? Review 1742: `completion/complete` implemented as heavy tool call. [5.3 #77]

- **A.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`
- **B.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **C.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **D.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean

### 78. For trading risk at Meridian Capital Trading Desk, the MCP Inspector UI must validate tool schemas. Which approach is correct? Trace 8296: `resource` audience binding missing per RFC 8707. [5.3 #78]

- **A.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds
- **B.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **C.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **D.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`

### 79. Complete the missing MCP field: In the Meridian Capital Trading Desk trading risk server, `____` must be set to the MCP-required value to enable trading risk correctly. Ticket 5052: `notifications/roots/list_changed` ignored after folder add. [5.3 #79]

- **A.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **B.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **C.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks
- **D.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization

### 80. At Meridian Capital Trading Desk, the MCP client code handling trading risk leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Review 1998: `completion/complete` implemented as heavy tool call. [5.4 #80]

- **A.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **B.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **C.** Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation
- **D.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging

### 81. At Meridian Capital Trading Desk, the MCP client code handling trading risk leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Trace 9686: `resource` audience binding missing per RFC 8707. [5.4 #81]

- **A.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **B.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **C.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **D.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`

### 82. Proposed solution: Meridian Capital Trading Desk will grant admin:write scope to every read-only docs search server by default for trading risk. Does this meet the MCP 2025-11-25 goal? Alert 3647: `progressToken` mismatch across concurrent tool calls. [5.4 #82]

- **A.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **B.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **C.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **D.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan

### 83. The Meridian Capital Trading Desk team documents the trading risk MCP flow. Which sequence of actions is spec-compliant? Trace 9275 reveals truncated cursor pagination at 50 entries. Scenario 5.5-1-83.

- **A.** Server exposes `/.well-known/oauth-authorization-server` with PRM & CIMD → client fetches RS metadata with `resource` indicator (RFC 8707) → PKCE + state + RFC 9207 iss validation → audience-bound token issued per resource server
- **B.** Client sends static API key in Authorization header → server skips issuer discovery → accept tokens with alg:none → grant org-admin scope by default
- **C.** Server embeds client_secret in JS bundle → disable PKCE as optional → return tokens over plain HTTP → cache discovery doc forever without TLS
- **D.** Client trusts token from any issuer → skip RFC 9207 iss equality check → ignore RFC 7591 dynamic registration → reuse single token across all resource servers

### 84. Meridian Capital Trading Desk needs to secure trading risk tool calls that mutate production data. The right control is to ____. Ticket 2806 reports `Last-Event-ID` replay mismatch after gateway restart. [5.5 #84]

- **A.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **B.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure
- **C.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **D.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414

### 85. An trading risk MCP gateway at Meridian Capital Trading Desk strips `Accept` negotiation headers. The fix is to ____. Log entry 7553 shows `Method not found -32601` without capability check. [5.5 #85]

- **A.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **B.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **C.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **D.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults

---

## Domain 6 — SDKs, Deployment, Observability & Ecosystem (13–17% blueprint weight · 15 questions)

### 86. The Meridian Capital Trading Desk MCP configuration for trading risk shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Trace 1068: batch of 200 tool calls timed out. Scenario 6.1-1-86.

- **A.** Install random GitHub MCP servers via curl|bash → grant full filesystem + network + env scopes → disable log redaction → store tokens in plaintext
- **B.** Auto-approve all tools without review → trust tool description text as system prompt → allow server to change tool logic post-approval → skip signature verification
- **C.** Pin server versions & verify registry signatures → isolate tool descriptions from executable logic → prompt user before first tool approval & high-risk actions → log tool provenance & monitor for description drift
- **D.** Exfiltrate tool arguments to third-party analytics silently → skip rate limiting on tool calls → omit provenance tags → hide tool calls from audit UI

### 87. Meridian Capital Trading Desk engineers designing an MCP system for trading risk must evaluate two correct controls. Which two statements are correct? Select two. Case 7797: `structuredContent` missing despite `outputSchema` declared. [6.1 #87]

- **A.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **B.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request
- **C.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **D.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **E.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`

### 88. In `Meridian Capital Trading Desk` `trading risk` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Ticket 5450: plaintext `config.json` holds refresh token. [6.1 #88]

- **A.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **B.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **C.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **D.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan

### 89. In `Meridian Capital Trading Desk` `trading risk` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Alert 4344: `progressToken` mismatch across concurrent tool calls. [6.2 #89]

- **A.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **B.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **C.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively
- **D.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects

### 90. Meridian Capital Trading Desk wants to bridge trading risk MCP tools into an A2A task mesh. The correct layer definition is ____. Incident 6023: OAuth PKCE verifier omitted for public client. [6.2 #90]

- **A.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **B.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **C.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **D.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`

### 91. Meridian Capital Trading Desk reports intermittent `Method not found -32601` errors when accessing trading risk. To fix this, the team should ____. Review 1669: `completion/complete` implemented as heavy tool call. [6.2 #91]

- **A.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **B.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **C.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **D.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`

### 92. Proposed solution: return tool errors as HTTP 500 HTML pages instead of JSON-RPC error objects is suggested for trading risk at Meridian Capital Trading Desk. Does this meet the goal? Review 4706: sampling loop lacks depth cap and cost budget. [6.3 #92]

- **A.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification
- **B.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **C.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **D.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks

### 93. Meridian Capital Trading Desk MCP trading risk SDK server omits `outputSchema`. The typed result approach is to ____. Case 4766: Host passes full env block to untrusted calendar server. [6.3 #93]

- **A.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **B.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **C.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **D.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification

### 94. In `Meridian Capital Trading Desk` `trading risk` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Ticket 1109 reports `Last-Event-ID` replay mismatch after gateway restart. [6.3 #94]

- **A.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **B.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)
- **C.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **D.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`

### 95. Select three correct MCP trading risk behaviors that Meridian Capital Trading Desk should enforce for its MCP fleet. Select three. Ticket 1915: plaintext `config.json` holds refresh token. [6.4 #95]

- **A.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification
- **B.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **C.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)
- **D.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure
- **E.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **F.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`

### 96. During trading risk at Meridian Capital Trading Desk, the MCP server responds with SSE without `eventId`. Which correction is required? Trace 4680: `resource` audience binding missing per RFC 8707. [6.4 #96]

- **A.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **B.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **C.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **D.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)

### 97. At Meridian Capital Trading Desk, the MCP client code handling trading risk leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Log 2280: `initialize` skipped before `tools/list`. [6.4 #97]

- **A.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **B.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **C.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **D.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage

### 98. Meridian Capital Trading Desk must fix its trading risk MCP integration. Which two changes bring it into spec compliance? Select two. Audit 6162: `includeContext=allServers` exfiltrates cross-server data. [6.5 #98]

- **A.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **B.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **C.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **D.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds
- **E.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks

### 99. For trading risk at Meridian Capital Trading Desk, the MCP Inspector UI must validate tool schemas. Which approach is correct? Ticket 8264 reports `Last-Event-ID` replay mismatch after gateway restart. [6.5 #99]

- **A.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **B.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **C.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **D.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent

### 100. Meridian Capital Trading Desk wants its MCP server to support both local and remote clients for trading risk. The architecture should ____. Ticket 8884: plaintext `config.json` holds refresh token. [6.5 #100]

- **A.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **B.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **C.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **D.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes

---

## Answer Key and Explanations

### Question 1 — `C, D` (MCP Foundations, Architecture & Lifecycle)

Correct answers: C and D (are correct). This follows the MCP specification for Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model, correcting the insecure/incompatible anti-pattern for trading risk. Skill 1.1 validation S1Q001. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Incorrect. assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.
- **B:** Incorrect. batching 200 unrelated tool calls into one HTTP request beyond advertised limits times out the whole batch.
- **C:** Correct. maps transport to deployment topology: stdio gives OS-level isolation locally; Streamable HTTP enables remote multi-tenant scale.
- **D:** Correct. clarifies layer boundaries: MCP standardizes context attachment; function calling is inline model schema; A2A negotiates task handoffs.
- **E:** Incorrect. treating MCP as a replacement for A2A agent discovery and task lifecycles conflates vertical tool attachment with peer delegation.

### Question 2 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). Selecting this honors Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 1.1 validation S1Q002. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Correct. allows safe iteration on draft specs like Tasks and elicitation without polluting the stable capability surface.
- **B:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.
- **C:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **D:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.

### Question 3 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). MCP 2025-11-25 requires Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model; the alternative breaks capability negotiation or security for trading risk. Skill 1.1 validation S1Q003. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **B:** Correct. correctly separates trust boundaries: Hosts own UI/policy, Clients speak MCP, Servers expose capabilities behind capability negotiation.
- **C:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **D:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.

### Question 4 — `B, E` (MCP Foundations, Architecture & Lifecycle)

Correct answers: B and E (are correct). This choice correctly implements Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 1.2 validation S1Q004. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Incorrect. deploying greenfield on the deprecated dual-endpoint SSE transport incurs future migration cost and lacks session IDs.
- **B:** Correct. lets each party call only negotiated features, avoiding methodNotFound and silent fallback hallucinations.
- **C:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.
- **D:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.
- **E:** Correct. guarantees version and capability compatibility before feature calls, satisfying the MCP lifecycle invariant.

### Question 5 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). Per MCP 2025-11-25, Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake ensures spec-compliant lifecycle and isolation for trading risk. Skill 1.2 validation S1Q005. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.
- **B:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **C:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.
- **D:** Correct. lets each party call only negotiated features, avoiding methodNotFound and silent fallback hallucinations.

### Question 6 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). Selecting this honors Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 1.2 validation S1Q006. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **B:** Incorrect. parsing free-form chat replies as structured data instead of typed elicitation invites format errors and injection.
- **C:** Correct. lets each party call only negotiated features, avoiding methodNotFound and silent fallback hallucinations.
- **D:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.

### Question 7 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). MCP 2025-11-25 requires Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy; the alternative breaks capability negotiation or security for trading risk. Reference 1.3 S1Q007. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Correct. matches official build flow: SDK scaffold, Inspector interactive validation, schema conformance checks, and registry publication with metadata.
- **B:** Incorrect. bypassing typed SDKs and Inspector validation ships lifecycle mismatches and credential leaks undetected.
- **C:** Incorrect. skipping version/capability advertisement and auth-context testing hides negotiation and authorization failures.
- **D:** Incorrect. ignoring dynamic list_changed and pagination paths leaves 90% of protocol surface untested.

### Question 8 — `B, E` (MCP Foundations, Architecture & Lifecycle)

Correct answers: B and E (are correct). Per MCP 2025-11-25, Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy ensures spec-compliant lifecycle and isolation for trading risk. Skill 1.3 validation S1Q008. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **B:** Correct. provides spec-guaranteed failure detection where OS TCP keepalives are invisible to application-level SSE/stdio proxies.
- **C:** Incorrect. enabling experimental tasks by default without capability checks forces unready clients into breaking draft methods.
- **D:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **E:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.

### Question 9 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). Selecting this honors Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 1.3 validation S1Q009. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.
- **B:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.
- **C:** Correct. standardizes remediation: 32601 means check capabilities, 32602 means fix schema, unlike bespoke string matching.
- **D:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.

### Question 10 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). This follows the MCP specification for Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging), correcting the insecure/incompatible anti-pattern for trading risk. Skill 1.4 validation S1Q010. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Incorrect. enabling experimental tasks by default without capability checks forces unready clients into breaking draft methods.
- **B:** Correct. enables forwards-compatible evolution without breaking older Hosts or Servers on version skew.
- **C:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **D:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.

### Question 11 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). Selecting this honors Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 1.4 validation S1Q011. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.
- **B:** Correct. enables forwards-compatible evolution without breaking older Hosts or Servers on version skew.
- **C:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **D:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.

### Question 12 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). MCP 2025-11-25 requires Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging); the alternative breaks capability negotiation or security for trading risk. Skill 1.4 validation S1Q012. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.
- **B:** Correct. enables forwards-compatible evolution without breaking older Hosts or Servers on version skew.
- **C:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.
- **D:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.

### Question 13 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). This choice correctly implements Manage keepalive pings, progress notifications, cancellation, and shutdown semantics for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 1.5 validation S1Q013. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.
- **B:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.
- **C:** Correct. gracefully aborts model-driven tool storms while freeing server resources and meeting JSON-RPC cancellation semantics.
- **D:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.

### Question 14 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). Selecting this honors Manage keepalive pings, progress notifications, cancellation, and shutdown semantics and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 1.5 validation S1Q014. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **B:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **C:** Incorrect. printing logs to stdout alongside JSON-RPC breaks line-delimited parsing and throws Parse error -32700.
- **D:** Correct. gracefully aborts model-driven tool storms while freeing server resources and meeting JSON-RPC cancellation semantics.

### Question 15 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). This choice correctly implements Manage keepalive pings, progress notifications, cancellation, and shutdown semantics for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 1.5 validation S1Q015. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.
- **B:** Correct. gracefully aborts model-driven tool storms while freeing server resources and meeting JSON-RPC cancellation semantics.
- **C:** Incorrect. requiring clients to poll list on a timer to detect new resources defeats MCP push efficiency.
- **D:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.

### Question 16 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). MCP 2025-11-25 requires Differentiate MCP from function calling, A2A, and experimental capability progression; the alternative breaks capability negotiation or security for trading risk. Reference 1.6 S1Q016. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Incorrect. missing inputSchema and raw shell interpolation from unvalidated LLM strings creates prompt-injection and RCE risk.
- **B:** Incorrect. responding before validation and ignoring list_changed events leaves clients with stale, unvalidated tool catalogs.
- **C:** Correct. matches MCP Tools spec: declarative schema, client discovery, validated execution, and structured content/error signaling.
- **D:** Incorrect. ad-hoc tool creation without validation and massive single-block responses break type safety and token budgets.

### Question 17 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). Per MCP 2025-11-25, Differentiate MCP from function calling, A2A, and experimental capability progression ensures spec-compliant lifecycle and isolation for trading risk. Skill 1.6 validation S1Q017. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Incorrect. printing logs to stdout alongside JSON-RPC breaks line-delimited parsing and throws Parse error -32700.
- **B:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **C:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.
- **D:** Correct. clarifies layer boundaries: MCP standardizes context attachment; function calling is inline model schema; A2A negotiates task handoffs.

### Question 18 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). This choice correctly implements Differentiate MCP from function calling, A2A, and experimental capability progression for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 1.6 validation S1Q018. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Correct. allows safe iteration on draft specs like Tasks and elicitation without polluting the stable capability surface.
- **B:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **C:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **D:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.

### Question 19 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). MCP 2025-11-25 requires Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints; the alternative breaks capability negotiation or security for trading risk. Reference 2.1 S1Q019. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. tight polling without subscription to list_changed notifications defeats MCP push efficiency and protocol layering.
- **B:** Incorrect. guessing URIs and exposing raw OS paths without scheme checks violates resource discovery and isolation.
- **C:** Incorrect. omitting uri and mimeType fields and ignoring pagination cursors makes resources unaddressable and unfilterable.
- **D:** Correct. follows Resources spec: capability advertisement, list/template discovery, uri-addressed reads with mime-typed contents and pagination.

### Question 20 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). Per MCP 2025-11-25, Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints ensures spec-compliant lifecycle and isolation for trading risk. Skill 2.1 validation S1Q020. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.
- **B:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.
- **C:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.
- **D:** Correct. preserves user/model agency and auditability; every mutation traces to an explicit model decision with tool audit event.

### Question 21 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). Selecting this honors Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 2.1 validation S1Q021. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. uses typed server helpers that auto-wire tools/list/call handlers and JSON Schema validation from Zod objects.
- **B:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.
- **C:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **D:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.

### Question 22 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). Per MCP 2025-11-25, Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints ensures spec-compliant lifecycle and isolation for trading risk. Skill 2.1 validation S1Q022. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **B:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **C:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **D:** Correct. preserves user/model agency and auditability; every mutation traces to an explicit model decision with tool audit event.

### Question 23 — `B, E` (Tools, Resources & Resource Templates)

Correct answers: B and E (are correct). Per MCP 2025-11-25, Control model-controlled tool execution, list discovery, validation, and structured content output ensures spec-compliant lifecycle and isolation for trading risk. Skill 2.2 validation S1Q023. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.
- **B:** Correct. preserves user/model agency and auditability; every mutation traces to an explicit model decision with tool audit event.
- **C:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.
- **D:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.
- **E:** Correct. defends against LLM hallucinated args and preserves typed error handling via isError flag versus exception propagation.

### Question 24 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). This follows the MCP specification for Control model-controlled tool execution, list discovery, validation, and structured content output, correcting the insecure/incompatible anti-pattern for trading risk. Skill 2.2 validation S1Q024. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. printing logs to stdout alongside JSON-RPC breaks line-delimited parsing and throws Parse error -32700.
- **B:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.
- **C:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.
- **D:** Correct. preserves user/model agency and auditability; every mutation traces to an explicit model decision with tool audit event.

### Question 25 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Selecting this honors Control model-controlled tool execution, list discovery, validation, and structured content output and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 2.2 validation S1Q025. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.
- **B:** Incorrect. distributing servers as raw GitHub tarballs without server.json or publisher proof hides supply-chain compromise.
- **C:** Correct. preserves user/model agency and auditability; every mutation traces to an explicit model decision with tool audit event.
- **D:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.

### Question 26 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). Selecting this honors Control model-controlled tool execution, list discovery, validation, and structured content output and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 2.2 validation S1Q026. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **B:** Correct. lets clients render multimodal results safely while distinguishing success from app-level errors without parsing text.
- **C:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.
- **D:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.

### Question 27 — `C, D, F` (Tools, Resources & Resource Templates)

Correct answers: C, D, and F (are correct). Selecting this honors Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 2.3 validation S1Q027. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. installing random `curl | bash` MCP servers without registry signature verification imports unvetted RCE into the IDE.
- **B:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.
- **C:** Correct. enables complete catalog sync for hosts that cache tool lists and paginate beyond 50 items without omission.
- **D:** Correct. pushes freshness efficiently after external ingestion jobs create new datasets, without constant re-list overhead.
- **E:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **F:** Correct. handles 10k-file workspaces without truncation or timeout, matching MCP pagination contract for both lists.

### Question 28 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Per MCP 2025-11-25, Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed ensures spec-compliant lifecycle and isolation for trading risk. Skill 2.3 validation S1Q028. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.
- **B:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **C:** Correct. pushes freshness efficiently after external ingestion jobs create new datasets, without constant re-list overhead.
- **D:** Incorrect. reimplementing a Postgres MCP server from scratch when a registry-verified one already exists wastes review cycles.

### Question 29 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). MCP 2025-11-25 requires Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed; the alternative breaks capability negotiation or security for trading risk. Skill 2.3 validation S1Q029. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Correct. enables complete catalog sync for hosts that cache tool lists and paginate beyond 50 items without omission.
- **B:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **C:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.
- **D:** Incorrect. calling tools before the initialized handshake completes races capability discovery and throws methodNotFound errors.

### Question 30 — `A, E` (Tools, Resources & Resource Templates)

Correct answers: A and E (are correct). This choice correctly implements Address direct resources vs templated resources with URI schemes, names, and mimeTypes for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 2.4 validation S1Q030. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. signals cost/safety posture without hard-coding policy; models prefer readOnly before destructive in multi-step plans.
- **B:** Incorrect. dumping base64 blobs as plain text without typed content blocks loses mimeType and forces heuristic parsing.
- **C:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **D:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **E:** Correct. models browse concrete resources via list and expand templates param by param without guessing URI syntax.

### Question 31 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). Selecting this honors Address direct resources vs templated resources with URI schemes, names, and mimeTypes and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 2.4 validation S1Q031. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **B:** Correct. models browse concrete resources via list and expand templates param by param without guessing URI syntax.
- **C:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **D:** Incorrect. setting includeContext=allServers by default fans sensitive data from every connected server into one sampling call.

### Question 32 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). Per MCP 2025-11-25, Address direct resources vs templated resources with URI schemes, names, and mimeTypes ensures spec-compliant lifecycle and isolation for trading risk. Skill 2.4 validation S1Q032. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. delivers typed content blocks that render correctly in Host UIs with binary vs text handling pre-decided by mimeType.
- **B:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.
- **C:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.
- **D:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.

### Question 33 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). MCP 2025-11-25 requires Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows; the alternative breaks capability negotiation or security for trading risk. Skill 2.5 validation S1Q033. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.
- **B:** Correct. handles 10k-file workspaces without truncation or timeout, matching MCP pagination contract for both lists.
- **C:** Incorrect. enabling experimental tasks by default without capability checks forces unready clients into breaking draft methods.
- **D:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.

### Question 34 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). This choice correctly implements Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 2.5 validation S1Q034. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. deploying greenfield on the deprecated dual-endpoint SSE transport incurs future migration cost and lacks session IDs.
- **B:** Incorrect. printing logs to stdout alongside JSON-RPC breaks line-delimited parsing and throws Parse error -32700.
- **C:** Correct. delivers typed content blocks that render correctly in Host UIs with binary vs text handling pre-decided by mimeType.
- **D:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.

### Question 35 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). This choice correctly implements Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 2.5 validation S1Q035. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.
- **B:** Incorrect. collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.
- **C:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **D:** Correct. keeps IDE diagnostics in sync with file edits without polling, per spec subscription lifecycle.

### Question 36 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). This follows the MCP specification for Declare prompts and completions for argument typeahead and parameterized prompt expansion, correcting the insecure/incompatible anti-pattern for trading risk. Reference 2.6 S1Q036. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. letting servers dictate client filesystem boundaries inverts MCP trust and breaks host isolation.
- **B:** Correct. implements Roots spec: client-owned boundary declaration, server-enforced confinement, and dynamic list_changed handling.
- **C:** Incorrect. hardcoding roots and ignoring list_changed notifications leaves stale boundaries after user permission changes.
- **D:** Incorrect. exposing full drive without consent and walking above root boundaries with symlink following enables directory traversal.

### Question 37 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). This choice correctly implements Declare prompts and completions for argument typeahead and parameterized prompt expansion for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 2.6 validation S1Q037. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. turns curated prompt packs into discoverable UX shortcuts argument-by-argument with typed validation.
- **B:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **C:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.
- **D:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.

### Question 38 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). Per MCP 2025-11-25, Declare prompts and completions for argument typeahead and parameterized prompt expansion ensures spec-compliant lifecycle and isolation for trading risk. Skill 2.6 validation S1Q038. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. compiles parameterized prompt templates server-side with validated args, keeping prompt injection surface server-controlled.
- **B:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.
- **C:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.
- **D:** Incorrect. printing logs to stdout alongside JSON-RPC breaks line-delimited parsing and throws Parse error -32700.

### Question 39 — `C, D` (Prompts, Sampling, Roots & Elicitation)

Correct answers: C and D (are correct). Selecting this honors Expose and expand prompts via prompts/list, prompts/get, and argument validation and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 3.1 validation S1Q039. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **B:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.
- **C:** Correct. powers low-latency autocomplete dropdowns directly from server-side datasets without tool execution overhead.
- **D:** Correct. turns curated prompt packs into discoverable UX shortcuts argument-by-argument with typed validation.
- **E:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.

### Question 40 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). Selecting this honors Expose and expand prompts via prompts/list, prompts/get, and argument validation and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 3.1 validation S1Q040. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **B:** Incorrect. parsing free-form chat replies as structured data instead of typed elicitation invites format errors and injection.
- **C:** Incorrect. dumping base64 blobs as plain text without typed content blocks loses mimeType and forces heuristic parsing.
- **D:** Correct. keeps prompt pickers fresh without re-listing on every keystroke, matching resource/tool change notification pattern.

### Question 41 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). This choice correctly implements Expose and expand prompts via prompts/list, prompts/get, and argument validation for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 3.1 validation S1Q041. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **B:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **C:** Correct. keeps prompt pickers fresh without re-listing on every keystroke, matching resource/tool change notification pattern.
- **D:** Incorrect. reimplementing a Postgres MCP server from scratch when a registry-verified one already exists wastes review cycles.

### Question 42 — `D, E` (Prompts, Sampling, Roots & Elicitation)

Correct answers: D and E (are correct). Selecting this honors Enforce client-owned filesystem boundaries via roots/list and roots/list_changed and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 3.2 validation S1Q042. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.
- **B:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **C:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.
- **D:** Correct. keeps server views consistent when users add/remove workspace folders mid-session without restart.
- **E:** Correct. prevents `../` and symlink hop attacks that would escape the user’s approved `file://` allowlist.

### Question 43 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). This follows the MCP specification for Enforce client-owned filesystem boundaries via roots/list and roots/list_changed, correcting the insecure/incompatible anti-pattern for trading risk. Skill 3.2 validation S1Q043. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **B:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.
- **C:** Correct. keeps server views consistent when users add/remove workspace folders mid-session without restart.
- **D:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.

### Question 44 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). This follows the MCP specification for Enforce client-owned filesystem boundaries via roots/list and roots/list_changed, correcting the insecure/incompatible anti-pattern for trading risk. Skill 3.2 validation S1Q044. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.
- **B:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **C:** Correct. gives users explicit allowlist control over which directories a server may touch, enforced server-side.
- **D:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.

### Question 45 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). MCP 2025-11-25 requires Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls; the alternative breaks capability negotiation or security for trading risk. Skill 3.3 validation S1Q045. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **B:** Correct. limits what prior server context flows into delegated sampling calls, preventing cross-server data exfiltration.
- **C:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.
- **D:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.

### Question 46 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). Per MCP 2025-11-25, Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls ensures spec-compliant lifecycle and isolation for trading risk. Skill 3.3 validation S1Q046. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. lets servers delegate LLM sub-tasks (summarization, critique) back to the Host model under explicit preference caps.
- **B:** Incorrect. labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.
- **C:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.
- **D:** Incorrect. collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.

### Question 47 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). This choice correctly implements Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 3.3 validation S1Q047. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. limits what prior server context flows into delegated sampling calls, preventing cross-server data exfiltration.
- **B:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **C:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **D:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.

### Question 48 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). This choice correctly implements Collect human input via elicitation/create with requestedSchema and form round-trips for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 3.4 validation S1Q048. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. turns server data needs into typed Host-rendered forms rather than chat text parsing, with explicit schema validation.
- **B:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.
- **C:** Incorrect. implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.
- **D:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.

### Question 49 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). MCP 2025-11-25 requires Collect human input via elicitation/create with requestedSchema and form round-trips; the alternative breaks capability negotiation or security for trading risk. Skill 3.4 validation S1Q049. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.
- **B:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.
- **C:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **D:** Correct. lets servers delegate LLM sub-tasks (summarization, critique) back to the Host model under explicit preference caps.

### Question 50 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). MCP 2025-11-25 requires Collect human input via elicitation/create with requestedSchema and form round-trips; the alternative breaks capability negotiation or security for trading risk. Skill 3.4 validation S1Q050. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **B:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.
- **C:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.
- **D:** Correct. turns server data needs into typed Host-rendered forms rather than chat text parsing, with explicit schema validation.

### Question 51 — `A, E` (Prompts, Sampling, Roots & Elicitation)

Correct answers: A and E (are correct). MCP 2025-11-25 requires Regulate verbosity via logging/setLevel and notifications/message level filtering; the alternative breaks capability negotiation or security for trading risk. Skill 3.5 validation S1Q051. [Skill 3.5: Regulate verbosity via logging/setLevel and notifications/message level filtering | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/logging/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. correlates streaming progress notifications to the correct in-flight tool/resource fetch without guessing.
- **B:** Incorrect. calling tools before the initialized handshake completes races capability discovery and throws methodNotFound errors.
- **C:** Incorrect. setting includeContext=allServers by default fans sensitive data from every connected server into one sampling call.
- **D:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.
- **E:** Correct. respects user-selected verbosity while still flowing warnings/errors through observability pipelines.

### Question 52 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). This choice correctly implements Regulate verbosity via logging/setLevel and notifications/message level filtering for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 3.5 validation S1Q052. [Skill 3.5: Regulate verbosity via logging/setLevel and notifications/message level filtering | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/logging/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.
- **B:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.
- **C:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.
- **D:** Correct. correlates streaming progress notifications to the correct in-flight tool/resource fetch without guessing.

### Question 53 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). This follows the MCP specification for Correlate progress and completion flows with progressToken and completion/complete semantics, correcting the insecure/incompatible anti-pattern for trading risk. Reference 3.6 S1Q053. [Skill 3.6: Correlate progress and completion flows with progressToken and completion/complete semantics | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/prompts]

- **A:** Incorrect. default-exposed sampling and uncapped recursive loops risk token runaway and expose internal reasoning inappropriately.
- **B:** Correct. follows Sampling spec: capability-checked server-initiated LLM delegation with explicit modelPreferences and human approval gating.
- **C:** Incorrect. unbounded PII-laden sampling without capability or consent bypasses privacy and authorization boundaries.
- **D:** Incorrect. confusing sampling payloads with tool metadata conflates delegation layers and breaks cost attribution.

### Question 54 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). Per MCP 2025-11-25, Correlate progress and completion flows with progressToken and completion/complete semantics ensures spec-compliant lifecycle and isolation for trading risk. Skill 3.6 validation S1Q054. [Skill 3.6: Correlate progress and completion flows with progressToken and completion/complete semantics | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/prompts]

- **A:** Correct. enables UX-level typeahead without invoking costly tools, scoped to declared completion capabilities.
- **B:** Incorrect. printing logs to stdout alongside JSON-RPC breaks line-delimited parsing and throws Parse error -32700.
- **C:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.
- **D:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.

### Question 55 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). Selecting this honors Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 4.1 validation S1Q055. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.
- **B:** Correct. gives OS-level isolation, clean env var scoping, and automatic teardown when Host exits without port conflicts.
- **C:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.
- **D:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.

### Question 56 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). Per MCP 2025-11-25, Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle ensures spec-compliant lifecycle and isolation for trading risk. Skill 4.1 validation S1Q056. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.
- **B:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.
- **C:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **D:** Incorrect. implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.

### Question 57 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). Selecting this honors Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 4.1 validation S1Q057. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.
- **B:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **C:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.
- **D:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.

### Question 58 — `A, C, E` (Transports, Sessions & Protocol Evolution)

Correct answers: A, C, and E (are correct). Selecting this honors Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 4.2 validation S1Q058. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. recovers progress streams and notifications lost during 5–30s mobile handoffs without missing tool progress events.
- **B:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **C:** Correct. preserves capability state and pagination cursors after transient network loss without re-initializing.
- **D:** Incorrect. implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.
- **E:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.
- **F:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.

### Question 59 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). Per MCP 2025-11-25, Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) ensures spec-compliant lifecycle and isolation for trading risk. Skill 4.2 validation S1Q059. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.
- **B:** Incorrect. calling tools before the initialized handshake completes races capability discovery and throws methodNotFound errors.
- **C:** Correct. preserves capability state and pagination cursors after transient network loss without re-initializing.
- **D:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.

### Question 60 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). MCP 2025-11-25 requires Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response); the alternative breaks capability negotiation or security for trading risk. Skill 4.2 validation S1Q060. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.
- **B:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.
- **C:** Correct. preserves capability state and pagination cursors after transient network loss without re-initializing.
- **D:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.

### Question 61 — `B, E` (Transports, Sessions & Protocol Evolution)

Correct answers: B and E (are correct). Per MCP 2025-11-25, Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay ensures spec-compliant lifecycle and isolation for trading risk. Skill 4.3 validation S1Q061. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **B:** Correct. recovers progress streams and notifications lost during 5–30s mobile handoffs without missing tool progress events.
- **C:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **D:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.
- **E:** Correct. avoids thundering herds after gateway restarts while ensuring exactly-once progress recovery via resumability.

### Question 62 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). MCP 2025-11-25 requires Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay; the alternative breaks capability negotiation or security for trading risk. Skill 4.3 validation S1Q062. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Incorrect. logging full tool arguments including customer PII and bearer tokens creates GDPR and credential-leak second-order risks.
- **B:** Correct. avoids thundering herds after gateway restarts while ensuring exactly-once progress recovery via resumability.
- **C:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.
- **D:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.

### Question 63 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). Selecting this honors Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 4.3 validation S1Q063. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Incorrect. reimplementing a Postgres MCP server from scratch when a registry-verified one already exists wastes review cycles.
- **B:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **C:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **D:** Correct. avoids thundering herds after gateway restarts while ensuring exactly-once progress recovery via resumability.

### Question 64 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). This follows the MCP specification for Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP, correcting the insecure/incompatible anti-pattern for trading risk. Skill 4.4 validation S1Q064. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.
- **B:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.
- **C:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **D:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.

### Question 65 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). This follows the MCP specification for Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP, correcting the insecure/incompatible anti-pattern for trading risk. Skill 4.4 validation S1Q065. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **B:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **C:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **D:** Correct. tracks spec evolution: split GET /sse + POST /messages merged into single POST with Accept-driven streaming.

### Question 66 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). MCP 2025-11-25 requires Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP; the alternative breaks capability negotiation or security for trading risk. Skill 4.4 validation S1Q066. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.
- **B:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.
- **C:** Correct. tracks spec evolution: split GET /sse + POST /messages merged into single POST with Accept-driven streaming.
- **D:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.

### Question 67 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). This choice correctly implements Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Reference 4.5 S1Q067. [Skill 4.5: Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/progress/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. unbounded batching and cross-tenant session ID reuse breaks rate limiting and tenant isolation guarantees.
- **B:** Incorrect. returning HTML instead of JSON-RPC errors and retrying without backoff causes parsing failures and duplicate mutations.
- **C:** Correct. matches 2025-11-25 Streamable HTTP spec: single endpoint, dual Accept, session ID management, and resumable SSE stream option.
- **D:** Incorrect. splitting endpoints and ignoring session/resumability headers reverts to pre-March 2025 deprecated SSE transport.

### Question 68 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). This choice correctly implements Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 4.5 validation S1Q068. [Skill 4.5: Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/progress/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.
- **B:** Correct. keeps MCP semantics intact through enterprise L7 filters that otherwise strip SSE headers and session sticky state.
- **C:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **D:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.

### Question 69 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). This choice correctly implements Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 4.6 validation S1Q069. [Skill 4.6: Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/cancellation/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. keeps MCP semantics intact through enterprise L7 filters that otherwise strip SSE headers and session sticky state.
- **B:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **C:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **D:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.

### Question 70 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). MCP 2025-11-25 requires Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival; the alternative breaks capability negotiation or security for trading risk. Skill 4.6 validation S1Q070. [Skill 4.6: Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/cancellation/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.
- **B:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.
- **C:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.
- **D:** Correct. keeps MCP semantics intact through enterprise L7 filters that otherwise strip SSE headers and session sticky state.

### Question 71 — `A, D` (Authorization, Security, Trust & Registry)

Correct answers: A and D (are correct). Selecting this honors Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 5.1 validation S1Q071. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Correct. enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.
- **B:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.
- **C:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.
- **D:** Correct. aligns MCP with current OAuth 2.1 security posture, eliminating token leakage vectors of legacy grants.
- **E:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.

### Question 72 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). Selecting this honors Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 5.1 validation S1Q072. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.
- **B:** Correct. enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.
- **C:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **D:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.

### Question 73 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). MCP 2025-11-25 requires Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata; the alternative breaks capability negotiation or security for trading risk. Skill 5.1 validation S1Q073. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.
- **B:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.
- **C:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **D:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.

### Question 74 — `C, E` (Authorization, Security, Trust & Registry)

Correct answers: C and E (are correct). Per MCP 2025-11-25, Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings ensures spec-compliant lifecycle and isolation for trading risk. Skill 5.2 validation S1Q074. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.
- **B:** Incorrect. calling tools before the initialized handshake completes races capability discovery and throws methodNotFound errors.
- **C:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.
- **D:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.
- **E:** Correct. keeps refresh tokens survivable across restarts but invisible to process dumps, forked children, and leaked logs.

### Question 75 — `A` (Authorization, Security, Trust & Registry)

Correct answer: A (is correct). Per MCP 2025-11-25, Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings ensures spec-compliant lifecycle and isolation for trading risk. Skill 5.2 validation S1Q075. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Correct. keeps refresh tokens survivable across restarts but invisible to process dumps, forked children, and leaked logs.
- **B:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.
- **C:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **D:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.

### Question 76 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). Per MCP 2025-11-25, Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings ensures spec-compliant lifecycle and isolation for trading risk. Skill 5.2 validation S1Q076. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.
- **B:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.
- **C:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.
- **D:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.

### Question 77 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). MCP 2025-11-25 requires Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality; the alternative breaks capability negotiation or security for trading risk. Skill 5.3 validation S1Q077. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Incorrect. setting includeContext=allServers by default fans sensitive data from every connected server into one sampling call.
- **B:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **C:** Correct. binds public client identity to TLS-verifiable origin without long-lived client secrets in distributed Hosts.
- **D:** Incorrect. dumping base64 blobs as plain text without typed content blocks loses mimeType and forces heuristic parsing.

### Question 78 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). This follows the MCP specification for Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality, correcting the insecure/incompatible anti-pattern for trading risk. Skill 5.3 validation S1Q078. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Incorrect. reimplementing a Postgres MCP server from scratch when a registry-verified one already exists wastes review cycles.
- **B:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **C:** Correct. enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.
- **D:** Incorrect. calling tools before the initialized handshake completes races capability discovery and throws methodNotFound errors.

### Question 79 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). Selecting this honors Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 5.3 validation S1Q079. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **B:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **C:** Incorrect. treating MCP as a replacement for A2A agent discovery and task lifecycles conflates vertical tool attachment with peer delegation.
- **D:** Correct. prevents token replay to unintended resource servers by audience-restricting each bearer token.

### Question 80 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). This choice correctly implements Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 5.4 validation S1Q080. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.
- **B:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **C:** Incorrect. batching 200 unrelated tool calls into one HTTP request beyond advertised limits times out the whole batch.
- **D:** Correct. stops a docs MCP server from using its tool output to call a payment MCP’s `transfer` tool via implicit ambient authority.

### Question 81 — `A` (Authorization, Security, Trust & Registry)

Correct answer: A (is correct). This choice correctly implements Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 5.4 validation S1Q081. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Correct. displays descriptions for human review but never concatenates them into system prompts or plan steps as trusted policy.
- **B:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.
- **C:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **D:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.

### Question 82 — `A` (Authorization, Security, Trust & Registry)

Correct answer: A (is correct). This choice correctly implements Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 5.4 validation S1Q082. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Correct. tags third-party fetched content so downstream Hosts can sandtrap it before the model treats it as instruction.
- **B:** Incorrect. enabling experimental tasks by default without capability checks forces unready clients into breaking draft methods.
- **C:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **D:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.

### Question 83 — `A` (Authorization, Security, Trust & Registry)

Correct answer: A (is correct). MCP 2025-11-25 requires Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging; the alternative breaks capability negotiation or security for trading risk. Reference 5.5 S1Q083. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Correct. follows MCP auth spec evolution: OAuth 2.1 with PKCE, protected resource metadata, RFC 8707 audience binding, and RFC 9207 issuer checks.
- **B:** Incorrect. hardcoded keys and alg:none tokens with blanket admin grants violate OAuth 2.1 and privilege separation.
- **C:** Incorrect. exposing secrets in client bundles and downgrading PKCE/TLS undermines OAuth confidentiality and channel binding.
- **D:** Incorrect. reusing a single audience-less token across resource servers enables cross-server token replay and mix-up attacks.

### Question 84 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). This follows the MCP specification for Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging, correcting the insecure/incompatible anti-pattern for trading risk. Skill 5.5 validation S1Q084. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **B:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.
- **C:** Correct. forces re-approval when a benign `get_weather` server silently rewires to `exfiltrate_files` after approval.
- **D:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.

### Question 85 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). MCP 2025-11-25 requires Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging; the alternative breaks capability negotiation or security for trading risk. Skill 5.5 validation S1Q085. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.
- **B:** Correct. prevents a malicious calendar server from harvesting `AWS_SECRET_ACCESS_KEY` and `GITHUB_PAT` from Host env dump.
- **C:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.
- **D:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.

### Question 86 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). Selecting this honors Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Reference 6.1 S1Q086. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Incorrect. unvetted curl-piped installs with maximal scopes and plaintext token storage maximizes blast radius from a single malicious server.
- **B:** Incorrect. blind auto-approval and treating descriptions as trusted instructions invites prompt injection and supply-chain compromise.
- **C:** Correct. applies MCP security checklist: supply-chain pinning, description-vs-logic separation, consent gating, and provenance monitoring against poison/rug-pull.
- **D:** Incorrect. silent exfiltration without rate limits or audit visibility breaks data minimization and incident-response traceability.

### Question 87 — `D, E` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: D and E (are correct). Selecting this honors Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 6.1 validation S1Q087. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.
- **B:** Incorrect. generating random progressTokens server-side with no binding to request id mixes streams across concurrent tasks.
- **C:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.
- **D:** Correct. uses typed server helpers that auto-wire tools/list/call handlers and JSON Schema validation from Zod objects.
- **E:** Correct. gives models complete, machine-validated contracts for tool selection and argument generation.

### Question 88 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). Selecting this honors Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 6.1 validation S1Q088. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **B:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.
- **C:** Incorrect. requiring clients to poll list on a timer to detect new resources defeats MCP push efficiency.
- **D:** Correct. gives decorator-ergonomic tool/resource registration with Pydantic/JSON Schema coherence across Python Hosts.

### Question 89 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). This choice correctly implements Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 6.2 validation S1Q089. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.
- **B:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.
- **C:** Correct. catches lifecycle, capability, and schema mismatches before CI with real-transport conformance testing.
- **D:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.

### Question 90 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). Per MCP 2025-11-25, Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates ensures spec-compliant lifecycle and isolation for trading risk. Skill 6.2 validation S1Q090. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Correct. automates protocol conformance as a PR check alongside lint/tests, proving list/call contracts headlessly.
- **B:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.
- **C:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **D:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.

### Question 91 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). Per MCP 2025-11-25, Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates ensures spec-compliant lifecycle and isolation for trading risk. Skill 6.2 validation S1Q091. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Correct. automates protocol conformance as a PR check alongside lint/tests, proving list/call contracts headlessly.
- **B:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **C:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.
- **D:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.

### Question 92 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). This follows the MCP specification for Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation, correcting the insecure/incompatible anti-pattern for trading risk. Skill 6.3 validation S1Q092. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Correct. makes servers discoverable with verifiable supply-chain metadata and semver-aware update notifications.
- **B:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **C:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.
- **D:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.

### Question 93 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). Per MCP 2025-11-25, Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation ensures spec-compliant lifecycle and isolation for trading risk. Skill 6.3 validation S1Q093. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.
- **B:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **C:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **D:** Correct. makes servers discoverable with verifiable supply-chain metadata and semver-aware update notifications.

### Question 94 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). Selecting this honors Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 6.3 validation S1Q094. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.
- **B:** Correct. provides supply-chain tamper evidence via package signing and publisher identity beyond raw GitHub stars.
- **C:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **D:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.

### Question 95 — `B, C, F` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: B, C, and F (are correct). Per MCP 2025-11-25, Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation ensures spec-compliant lifecycle and isolation for trading risk. Skill 6.4 validation S1Q095. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Incorrect. distributing servers as raw GitHub tarballs without server.json or publisher proof hides supply-chain compromise.
- **B:** Correct. respects user-selected verbosity while still flowing warnings/errors through observability pipelines.
- **C:** Correct. enables post-incident forensics without persisting PII/tokens, keyed by stable tool provenance hashes.
- **D:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.
- **E:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.
- **F:** Correct. powers per-tool SLOs and supply-chain forensics without persisting sensitive tool argument values.

### Question 96 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). This choice correctly implements Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 6.4 validation S1Q096. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Incorrect. requiring clients to poll list on a timer to detect new resources defeats MCP push efficiency.
- **B:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **C:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **D:** Correct. enables post-incident forensics without persisting PII/tokens, keyed by stable tool provenance hashes.

### Question 97 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). MCP 2025-11-25 requires Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation; the alternative breaks capability negotiation or security for trading risk. Skill 6.4 validation S1Q097. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **B:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.
- **C:** Correct. traces tool call latency through Streamable HTTP gateways into server execution with per-session correlation.
- **D:** Incorrect. assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.

### Question 98 — `D, E` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: D and E (are correct). Selecting this honors Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns and prevents the listed failure mode in Meridian Capital Trading Desk trading risk flows. Skill 6.5 validation S1Q098. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **B:** Incorrect. printing logs to stdout alongside JSON-RPC breaks line-delimited parsing and throws Parse error -32700.
- **C:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **D:** Correct. reuses vetted categories (databases, cloud, payments) before building bespoke wrappers over public APIs.
- **E:** Correct. uses MCP vertically for capabilities and A2A horizontally for peer negotiation, per LM-Foundation AAIF stack guidance.

### Question 99 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). This choice correctly implements Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns for Meridian Capital Trading Desk while the distractors violate transport/session guarantees. Skill 6.5 validation S1Q099. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **B:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **C:** Correct. distinguishes app-level tool errors (tool ran, domain said no) from protocol-level crashes clients can retry.
- **D:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.

### Question 100 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). This follows the MCP specification for Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns, correcting the insecure/incompatible anti-pattern for trading risk. Skill 6.5 validation S1Q100. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Incorrect. requiring clients to poll list on a timer to detect new resources defeats MCP push efficiency.
- **B:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **C:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **D:** Correct. standardizes cross-Host deployment via portable config blocks with scoped env and per-server enable toggles.
