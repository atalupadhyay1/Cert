# MCP: Model Context Protocol: Servers, Clients, Transports & Security — Full-Length Mock Exam 2 — HelixMed Clinical Research Hub (Healthcare & Trials)

**Theme:** Initialization Handshake, Resource Templates, Streamable HTTP Sessions & Elicitation  
**Credential alignment:** `Model Context Protocol (MCP 2025-11-25) — Tool & Context Standard`  
**Blueprint baseline:** `November 2026 (MCP Specification 2025-11-25 · MCP Registry & Inspector · OAuth 2.1 + RFC 8707/9207 + CIMD · OWASP MCP Security Checklist)` (https://modelcontextprotocol.io/introduction · https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation · https://genai.owasp.org/resource/mcp-security-checklist/)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `120 minutes` (`72 seconds/question` full-endurance pacing; aligns with `120 minutes` on NVIDIA NCP-AAI & GitHub GH-600)

> **Disclaimer:** Independent educational practice material authored from public engineering specifications and open-protocol documentation — not affiliated with, sponsored by, or endorsed by NVIDIA, the Linux Foundation, Anthropic, OpenAI, Google, Microsoft, GitHub, LangChain, or OWASP. Practice scores do not guarantee passing any third-party certification exam.

## Questions

---

## Domain 1 — MCP Foundations, Architecture & Lifecycle (16–20% blueprint weight · 18 questions)

### 1. HelixMed Clinical Research Hub MCP server for clinical trial data requires two valid security hardening steps. Which two should you apply? Select two. Review 8004: `completion/complete` implemented as heavy tool call. [1.1 #1]

- **A.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **B.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **C.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **D.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **E.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**

### 2. Proposed solution: grant admin:write scope to every read-only docs search server by default for clinical trial data at HelixMed Clinical Research Hub. Does this meet the goal? Alert 1407: `Mcp-Session-Id` reused across tenants. [1.1 #2]

- **A.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation
- **B.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **C.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **D.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`

### 3. Proposed solution: poll resources/list every 10 ms instead of subscribing to list_changed for clinical trial data at HelixMed Clinical Research Hub. Does this meet the goal? Log entry 6652 shows `Method not found -32601` without capability check. [1.1 #3]

- **A.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **B.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **C.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation
- **D.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`

### 4. HelixMed Clinical Research Hub engineers designing an MCP system for clinical trial data must evaluate two correct controls. Which two statements are correct? Select two. Case 4657: Host passes full env block to untrusted calendar server. [1.2 #4]

- **A.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **B.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **C.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **D.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`
- **E.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways

### 5. In `HelixMed Clinical Research Hub` `clinical trial data` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Alert 6121: `Mcp-Session-Id` reused across tenants. [1.2 #5]

- **A.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **B.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **C.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively
- **D.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`

### 6. Proposed solution: To handle clinical trial data, HelixMed Clinical Research Hub plans to auto-approve every tool without re-consent and treat descriptions as executable policy. Does this satisfy the MCP specification? Incident MCP-2026-1990 shows Misconfigured `Mcp-Session-Id` routing. [1.2 #6]

- **A.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **B.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets
- **C.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **D.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`

### 7. The MCP Inspector highlights `____` as missing for clinical trial data at HelixMed Clinical Research Hub. Which completion is spec-correct? Incident MCP-2026-3073 shows Misconfigured `Mcp-Session-Id` routing. Scenario 1.3-2-7.

- **A.** Server sends `initialize` to client → client negotiates logging level first → exchange OAuth tokens inside `initialize` params → begin sampling without capability check
- **B.** Client sends `initialize` with `protocolVersion` & `capabilities` → server replies with negotiated version & capabilities → client sends `notifications/initialized` → normal `tools/list` & `resources/list` calls begin
- **C.** Client hardcodes `protocolVersion: "1.0"` forever → ignore server `protocolVersion` echo → send duplicate `initialize` on every ping → cache capabilities indefinitely
- **D.** Client calls `tools/call` immediately → server returns capability list on tool error → client sends `initialize` afterward → skip `notifications/initialized`

### 8. During clinical trial data load testing at HelixMed Clinical Research Hub, Streamable HTTP sessions terminate behind an ALB idle timeout. The team should ____. Trace 5409: batch of 200 tool calls timed out. [1.3 #8]

- **A.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **B.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **C.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **D.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`

### 9. HelixMed Clinical Research Hub wants to add prompt packs for clinical trial data. The MCP-compliant way is to ____. Review 3954: `completion/complete` implemented as heavy tool call. [1.3 #9]

- **A.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **B.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **C.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **D.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`

### 10. For clinical trial data, HelixMed Clinical Research Hub must enforce three hardening measures. Which three are correct? Select three. Alert 8760: `progressToken` mismatch across concurrent tool calls. [1.4 #10]

- **A.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **B.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **C.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **D.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **E.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **F.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`

### 11. At HelixMed Clinical Research Hub, clinical trial data MCP server batch returns timeout for 200 calls. The team should ____. Incident 4018: tool `inputSchema` validation skipped, injection observed. [1.4 #11]

- **A.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **B.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **C.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **D.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`

### 12. HelixMed Clinical Research Hub sees its clinical trial data MCP tool return large binary blobs inline. The spec-compliant return is to ____. Incident MCP-2026-9589 shows Misconfigured `Mcp-Session-Id` routing. [1.4 #12]

- **A.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **B.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **C.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **D.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization

### 13. For clinical trial data at HelixMed Clinical Research Hub, which ordered flow correctly implements the MCP 2025-11-25 requirement? Log entry 6467 shows `Method not found -32601` without capability check. Scenario 1.5-2-13.

- **A.** Server declares tool with `name`, `description`, `inputSchema` (JSON Schema) → client `tools/list` discovers it → model calls `tools/call` with validated args → server validates, executes idempotently & returns `content` + `isError`
- **B.** Server returns tool result before validation → client retries with doubled args → disable tools/list_changed notifications → cache tool names forever
- **C.** Server exposes 200 tools without descriptions → client guesses arguments via prompt → server executes shell with raw LLM string → return HTML page inside isError=false
- **D.** Client calls undefined tool name → server creates tool on-the-fly → skip inputSchema validation → stream 50-MB blob as single text content block

### 14. For clinical trial data at HelixMed Clinical Research Hub, the MCP Inspector UI must validate tool schemas. Which approach is correct? Log 8337: `prompt/get` uses client-side interpolation without validation. [1.5 #14]

- **A.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **B.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **C.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs
- **D.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes

### 15. At HelixMed Clinical Research Hub, clinical trial data MCP tool descriptions are concatenated into system prompts. Which safeguard is needed? Incident MCP-2026-2989 shows Misconfigured `Mcp-Session-Id` routing. [1.5 #15]

- **A.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **B.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **C.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **D.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`

### 16. At HelixMed Clinical Research Hub, clinical trial data MCP tool descriptions are concatenated into system prompts. Which safeguard is needed? Alert 8851: `Mcp-Session-Id` reused across tenants. [1.6 #16]

- **A.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **B.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **C.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks
- **D.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping

### 17. For clinical trial data at HelixMed Clinical Research Hub, token storage uses plaintext `config.json`. The secure alternative is to ____. Incident MCP-2026-7693 shows Misconfigured `Mcp-Session-Id` routing. [1.6 #17]

- **A.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **B.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification
- **C.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **D.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks

### 18. You are reviewing an MCP implementation for HelixMed Clinical Research Hub that handles clinical trial data. Which statement about ____ is accurate under MCP 2025-11-25? Case 8298: registry installs via `curl¦bash` without signature check. [1.6 #18]

- **A.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **B.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **C.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **D.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token

---

## Domain 2 — Tools, Resources & Resource Templates (18–22% blueprint weight · 20 questions)

### 19. For clinical trial data at HelixMed Clinical Research Hub, two MCP primitives are required to enable the scenario. Which two are needed? Select two. Ticket 7802 reports `Last-Event-ID` replay mismatch after gateway restart. [2.1 #19]

- **A.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **B.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **C.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **D.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **E.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping

### 20. The HelixMed Clinical Research Hub clinical trial data Host caches `roots/list` forever and misses workspace changes. The fix is to ____. Trace 4071: `resource` audience binding missing per RFC 8707. [2.1 #20]

- **A.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **B.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **C.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **D.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks

### 21. When HelixMed Clinical Research Hub connects its VS Code host to an MCP server for clinical trial data, the `roots/list` workflow should ____. Audit 8779: `includeContext=allServers` exfiltrates cross-server data. [2.1 #21]

- **A.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **B.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **C.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **D.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes

### 22. A HelixMed MCP client for clinical trial data must ____ to satisfy the protocol. What is the correct implementation approach? Ticket 6417: `notifications/roots/list_changed` ignored after folder add. [2.1 #22]

- **A.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification
- **B.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **C.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **D.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible

### 23. For HelixMed Clinical Research Hub clinical trial data server to advertise new capabilities after a deploy, the correct notification is ____. Incident 1126: tool logic changed post-approval (rug-pull) undetected. [2.2 #23]

- **A.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **B.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **C.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure
- **D.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails

### 24. HelixMed Clinical Research Hub handles clinical trial data via MCP sampling delegation. To enforce least privilege, the server should ____. Ticket 5049: `roots/list` poll floods client every 10 ms. [2.2 #24]

- **A.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **B.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **C.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **D.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes

### 25. The MCP Inspector highlights `____` as missing for clinical trial data at HelixMed Clinical Research Hub. Which completion is spec-correct? Log entry 5769 shows `Method not found -32601` without capability check. [2.2 #25]

- **A.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **B.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **C.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **D.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`

### 26. Complete the missing MCP field: In the HelixMed Clinical Research Hub clinical trial data server, `____` must be set to the MCP-required value to enable clinical trial data correctly. Incident 3961: OAuth PKCE verifier omitted for public client. [2.2 #26]

- **A.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request
- **B.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **C.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **D.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`

### 27. The HelixMed Clinical Research Hub MCP configuration for clinical trial data shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Audit 2793 flags `alg:none` token acceptance in staging. Scenario 2.3-2-27.

- **A.** Server advertises `resources` capability → client calls `resources/list` or `resources/templates/list` → client reads `resources/read` with `uri` → server returns `contents` with `mimeType`, handling pagination cursors
- **B.** Server returns resources without uri fields → client stores resource content in tool history → server omits page cursors for 10k items → skip mimeType declaration
- **C.** Client guesses file URIs without list → server returns OS absolute paths as uri → embed 10-MB binary as base64 JSON string → skip uri validation
- **D.** Server lists resources without capability flag → client polls `resources/list` every 10 ms in loop → ignore `resources/list_changed` notifications → request resources via tools/call

### 28. For clinical trial data at HelixMed Clinical Research Hub, the Host must reconcile `protocolVersion` negotiation after an upgrade. Which action is correct? Incident MCP-2026-9832 shows Misconfigured `Mcp-Session-Id` routing. [2.3 #28]

- **A.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **B.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **C.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **D.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`

### 29. HelixMed Clinical Research Hub MCP Host for clinical trial data must handle `elicitation/create` versus chat parsing. Which is spec-correct? Incident 6067: OAuth PKCE verifier omitted for public client. [2.3 #29]

- **A.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **B.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **C.** Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation
- **D.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization

### 30. At HelixMed Clinical Research Hub, clinical trial data MCP tool descriptions are concatenated into system prompts. Which safeguard is needed? Incident 5655: tool logic changed post-approval (rug-pull) undetected. [2.4 #30]

- **A.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **B.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **C.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **D.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing

### 31. An clinical trial data MCP gateway at HelixMed Clinical Research Hub strips `Accept` negotiation headers. The fix is to ____. Review 9029: sampling loop lacks depth cap and cost budget. [2.4 #31]

- **A.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **B.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **C.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **D.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token

### 32. Proposed solution: HelixMed Clinical Research Hub will use the deprecated HTTP+SSE split endpoint for all new greenfield remote servers for clinical trial data. Does this meet the MCP 2025-11-25 goal? Trace 2527: `resource` audience binding missing per RFC 8707. [2.4 #32]

- **A.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds
- **B.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **C.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **D.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI

### 33. HelixMed Clinical Research Hub engineers designing an MCP system for clinical trial data must evaluate two correct controls. Which two statements are correct? Select two. Audit 8969: auto-approve bypasses human consent for destructive tool. [2.5 #33]

- **A.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **B.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **C.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **D.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`
- **E.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks

### 34. HelixMed Clinical Research Hub MCP server serving clinical trial data returns `isError:false` with an HTML error page. The proper fix is to ____. Trace 5461 reveals truncated cursor pagination at 50 entries. [2.5 #34]

- **A.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **B.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **C.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **D.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params

### 35. The HelixMed Clinical Research Hub MCP configuration for clinical trial data shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Case 1041: Host passes full env block to untrusted calendar server. [2.5 #35]

- **A.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **B.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **C.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **D.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics

### 36. The HelixMed Clinical Research Hub team documents the clinical trial data MCP flow. Which sequence of actions is spec-compliant? Incident MCP-2026-2041 shows Misconfigured `Mcp-Session-Id` routing. Scenario 2.6-2-36.

- **A.** Client exposes entire `C:\` without consent → server walks parent directories above declared roots → disable path canonicalization → follow symlinks blindly
- **B.** Client declares `roots` capability with `file://` allowlist → server calls `roots/list` to learn boundaries → server restricts `resources/read` & tool file ops to those roots → handle `notifications/roots/list_changed`
- **C.** Server declares client roots unilaterally → client trusts arbitrary server-provided paths → skip roots/list → ignore list_changed notifications
- **D.** Server hardcodes `roots/list` response → client polls filesystem without notification channel → skip name/uri validation → cache roots forever

### 37. Which two behaviors correctly describe MCP clinical trial data handling at HelixMed Clinical Research Hub? Select two. Ticket 9132: `notifications/roots/list_changed` ignored after folder add. [2.6 #37]

- **A.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **B.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **C.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **D.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **E.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively

### 38. Complete the missing MCP field: In the HelixMed Clinical Research Hub clinical trial data server, `____` must be set to the MCP-required value to enable clinical trial data correctly. Incident 8672: OAuth PKCE verifier omitted for public client. [2.6 #38] through Spanner stale read (variant alpha 479).

- **A.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **B.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)
- **C.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **D.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs

---

## Domain 3 — Prompts, Sampling, Roots & Elicitation (14–18% blueprint weight · 16 questions)

### 39. HelixMed Clinical Research Hub MCP onboarding for clinical trial data must follow the correct 4-step lifecycle. Which ordered sequence is correct? Audit 6399: auto-approve bypasses human consent for destructive tool. Scenario 3.1-2-39.

- **A.** Client exposes sampling by default without opt-in → server loops sampling/createMessage recursively → ignore modelPreferences hints → return raw chain-of-thought as tool output
- **B.** Server sends sampling without capability check → include raw customer PII in messages → skip maxTokens limits → client auto-executes without user consent
- **C.** Server advertises sampling need → checks client `sampling` capability → sends `sampling/createMessage` with `messages`, `maxTokens`, `modelPreferences` → client applies human-in-loop gating & returns generation
- **D.** Server mixes sampling messages into tool descriptions → client forwards without isolation → skip cost tracking → cache sampling results as facts

### 40. HelixMed Clinical Research Hub plans to publish its clinical trial data MCP server to the registry. The publishing step should ____. Review 7739: `outputSchema` mismatched to `structuredContent` shape. [3.1 #40]

- **A.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **B.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request
- **C.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **D.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`

### 41. At HelixMed Clinical Research Hub, the MCP client code handling clinical trial data leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Review 5462: sampling loop lacks depth cap and cost budget. [3.1 #41]

- **A.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean
- **B.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **C.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`
- **D.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context

### 42. Which two behaviors correctly describe MCP clinical trial data handling at HelixMed Clinical Research Hub? Select two. Trace 8731: `resource` audience binding missing per RFC 8707. [3.2 #42]

- **A.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **B.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **C.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks
- **D.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **E.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle

### 43. HelixMed Clinical Research Hub observes its clinical trial data MCP server failing `tools/call` with `Invalid params -32602`. The fix is to ____. Audit 2848 flags `alg:none` token acceptance in staging. [3.2 #43]

- **A.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **B.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **C.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **D.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals

### 44. The MCP Inspector highlights `____` as missing for clinical trial data at HelixMed Clinical Research Hub. Which completion is spec-correct? Alert 3616: `isError:false` with HTML error page masks failure. [3.2 #44]

- **A.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **B.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **C.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **D.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately

### 45. For clinical trial data, HelixMed Clinical Research Hub must enforce three hardening measures. Which three are correct? Select three. Log 3631: `initialize` skipped before `tools/list`. [3.3 #45]

- **A.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **B.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **C.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **D.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`
- **E.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **F.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them

### 46. At HelixMed Clinical Research Hub, the MCP client code handling clinical trial data leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Log entry 7926 shows `Method not found -32601` without capability check. [3.3 #46]

- **A.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`
- **B.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **C.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **D.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke

### 47. HelixMed Clinical Research Hub wants to bridge clinical trial data MCP tools into an A2A task mesh. The correct layer definition is ____. Trace 3616: 200-tool batch exceeds advertised `maxBatchSize`. [3.3 #47]

- **A.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)
- **B.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **C.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **D.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing

### 48. HelixMed Clinical Research Hub handles clinical trial data via MCP sampling delegation. To enforce least privilege, the server should ____. Log 9512: `prompt/get` uses client-side interpolation without validation. [3.4 #48]

- **A.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **B.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **C.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **D.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)

### 49. At HelixMed Clinical Research Hub, engineers building an MCP server for clinical trial data need to ____. Which configuration correctly implements the MCP specification? Review 8078: sampling loop lacks depth cap and cost budget. [3.4 #49]

- **A.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **B.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **C.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **D.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`

### 50. During clinical trial data load testing at HelixMed Clinical Research Hub, Streamable HTTP sessions terminate behind an ALB idle timeout. The team should ____. Trace 2614: batch of 200 tool calls timed out. [3.4 #50] via Linkerd mTLS strict (variant delta 160). through Cedar policy evaluation (variant delta 527).

- **A.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **B.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **C.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **D.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`

### 51. HelixMed Clinical Research Hub engineers designing an MCP system for clinical trial data must evaluate two correct controls. Which two statements are correct? Select two. Log 6240: `initialize` skipped before `tools/list`. [3.5 #51]

- **A.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)
- **B.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **C.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request
- **D.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **E.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**

### 52. HelixMed Clinical Research Hub MCP server serving clinical trial data returns `isError:false` with an HTML error page. The proper fix is to ____. Review 6272: sampling loop lacks depth cap and cost budget. [3.5 #52]

- **A.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **B.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request
- **C.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **D.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`

### 53. In `HelixMed Clinical Research Hub` `clinical trial data` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Ticket 3099 reports `Last-Event-ID` replay mismatch after gateway restart. [3.6 #53]

- **A.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **B.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **C.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **D.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files

### 54. At HelixMed Clinical Research Hub, clinical trial data MCP tool descriptions are concatenated into system prompts. Which safeguard is needed? Alert 8843: `Mcp-Session-Id` reused across tenants. [3.6 #54] through Spanner stale read (variant alpha 476).

- **A.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks
- **B.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **C.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **D.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets

---

## Domain 4 — Transports, Sessions & Protocol Evolution (14–18% blueprint weight · 16 questions)

### 55. For clinical trial data at HelixMed Clinical Research Hub, two best practices align with MCP 2025-11-25. Which two should be implemented? Select two. Trace 6828: `resource` audience binding missing per RFC 8707. [4.1 #55]

- **A.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **B.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **C.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **D.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **E.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI

### 56. Proposed solution: HelixMed Clinical Research Hub will grant admin:write scope to every read-only docs search server by default for clinical trial data. Does this meet the MCP 2025-11-25 goal? Incident MCP-2026-1801 shows Misconfigured `Mcp-Session-Id` routing. [4.1 #56]

- **A.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **B.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **C.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **D.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)

### 57. You are reviewing an MCP implementation for HelixMed Clinical Research Hub that handles clinical trial data. Which statement about ____ is accurate under MCP 2025-11-25? Case 1511: registry installs via `curl¦bash` without signature check. [4.1 #57] across CloudFront edge cache (variant beta 697).

- **A.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **B.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)
- **C.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **D.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults

### 58. The MCP Inspector highlights `____` as missing for clinical trial data at HelixMed Clinical Research Hub. Which completion is spec-correct? Review 3497: `completion/complete` implemented as heavy tool call. [4.2 #58]

- **A.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **B.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **C.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **D.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect

### 59. At HelixMed Clinical Research Hub, engineers building an MCP server for clinical trial data need to ____. Which configuration correctly implements the MCP specification? Trace 2432: `resource` audience binding missing per RFC 8707. [4.2 #59]

- **A.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **B.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request
- **C.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **D.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively

### 60. Complete the missing MCP field: In the HelixMed Clinical Research Hub clinical trial data server, `____` must be set to the MCP-required value to enable clinical trial data correctly. Log 5390: SSE stream without `eventId` loses progress on reconnect. [4.2 #60]

- **A.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **B.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **C.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **D.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization

### 61. HelixMed Clinical Research Hub MCP server for clinical trial data requires two valid security hardening steps. Which two should you apply? Select two. Alert 8587: `isError:false` with HTML error page masks failure. [4.3 #61]

- **A.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **B.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **C.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **D.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **E.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`

### 62. The MCP Inspector highlights `____` as missing for clinical trial data at HelixMed Clinical Research Hub. Which completion is spec-correct? Ticket 6346: plaintext `config.json` holds refresh token. [4.3 #62]

- **A.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **B.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **C.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **D.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics

### 63. Proposed solution: HelixMed Clinical Research Hub will disable TLS and send OAuth tokens over plain HTTP to reduce latency for clinical trial data. Does this meet the MCP 2025-11-25 goal? Review 2008: sampling loop lacks depth cap and cost budget. [4.3 #63]

- **A.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively
- **B.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **C.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **D.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`

### 64. Complete the missing MCP field: In the HelixMed Clinical Research Hub clinical trial data server, `____` must be set to the MCP-required value to enable clinical trial data correctly. Alert 4736: `isError:false` with HTML error page masks failure. Scenario 4.4-2-64.

- **A.** Server returns 200 OK with HTML error page → client retries without backoff → disable idempotency on non-idempotent tool calls → omit Content-Type validation
- **B.** Client POSTs JSON-RPC to single `mcp` endpoint with `Content-Type: application/json` & `Accept: text/event-stream, application/json` → server may respond with single JSON or SSE stream → client honors `Mcp-Session-Id` & `Last-Event-ID` for resumability
- **C.** Client sends batched 100 requests without server batch ack → server streams without event IDs → skip session expiry handling → leak session IDs across tenants
- **D.** Client opens separate GET /sse and POST /message SSE endpoints → send JSON without Accept header → ignore Mcp-Session-Id → close stream after each chunk without Last-Event-ID

### 65. HelixMed Clinical Research Hub needs to bound clinical trial data sampling loops that fan out recursively. Which limit is appropriate? Trace 9668: `resource` audience binding missing per RFC 8707. [4.4 #65]

- **A.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **B.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **C.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **D.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle

### 66. At HelixMed Clinical Research Hub, clinical trial data MCP server batch returns timeout for 200 calls. The team should ____. Alert 4939: `Mcp-Session-Id` reused across tenants. [4.4 #66]

- **A.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **B.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **C.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **D.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414

### 67. In `HelixMed Clinical Research Hub` `clinical trial data` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Incident MCP-2026-4595 shows Misconfigured `Mcp-Session-Id` routing. [4.5 #67]

- **A.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **B.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **C.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **D.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation

### 68. HelixMed Clinical Research Hub MCP Host for clinical trial data must handle `elicitation/create` versus chat parsing. Which is spec-correct? Log 1262: SSE stream without `eventId` loses progress on reconnect. [4.5 #68]

- **A.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **B.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **C.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **D.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation

### 69. The MCP Inspector highlights `____` as missing for clinical trial data at HelixMed Clinical Research Hub. Which completion is spec-correct? Log 7021: `prompt/get` uses client-side interpolation without validation. [4.6 #69]

- **A.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **B.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **C.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **D.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle

### 70. HelixMed Clinical Research Hub observes its clinical trial data MCP server failing `tools/call` with `Invalid params -32602`. The fix is to ____. Case 7951: Host passes full env block to untrusted calendar server. [4.6 #70]

- **A.** Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation
- **B.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **C.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **D.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets

---

## Domain 5 — Authorization, Security, Trust & Registry (13–17% blueprint weight · 15 questions)

### 71. HelixMed Clinical Research Hub must fix its clinical trial data MCP integration. Which two changes bring it into spec compliance? Select two. Review 9611: `outputSchema` mismatched to `structuredContent` shape. [5.1 #71]

- **A.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **B.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **C.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **D.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **E.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals

### 72. A clinical trial data MCP extension at HelixMed Clinical Research Hub leaks `Mcp-Session-Id` across tenants. The team must ____. Ticket 4198 reports `Last-Event-ID` replay mismatch after gateway restart. [5.1 #72]

- **A.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **B.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **C.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **D.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token

### 73. For clinical trial data at HelixMed Clinical Research Hub, the client must handle `resources/subscribe` vs polling. Which is efficient? Case 6476: registry installs via `curl¦bash` without signature check. [5.1 #73]

- **A.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **B.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets
- **C.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **D.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`

### 74. The MCP Inspector highlights `____` as missing for clinical trial data at HelixMed Clinical Research Hub. Which completion is spec-correct? Alert 5505: `isError:false` with HTML error page masks failure. [5.2 #74] using Great Expectations suite (variant alpha 146). through Cortex query sharding (variant alpha 529).

- **A.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **B.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **C.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **D.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation

### 75. An clinical trial data MCP gateway at HelixMed Clinical Research Hub strips `Accept` negotiation headers. The fix is to ____. Trace 4771: 200-tool batch exceeds advertised `maxBatchSize`. [5.2 #75]

- **A.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **B.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **C.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **D.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions

### 76. Complete the missing MCP field: In the HelixMed Clinical Research Hub clinical trial data server, `____` must be set to the MCP-required value to enable clinical trial data correctly. Review 2581 notes `resources/list_changed` never fired after ingest. [5.2 #76]

- **A.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **B.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **C.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`
- **D.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**

### 77. Select three correct MCP clinical trial data behaviors that HelixMed Clinical Research Hub should enforce for its MCP fleet. Select three. Audit 7533: `includeContext=allServers` exfiltrates cross-server data. [5.3 #77]

- **A.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **B.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **C.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **D.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **E.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **F.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token

### 78. During clinical trial data at HelixMed Clinical Research Hub, the MCP server responds with SSE without `eventId`. Which correction is required? Alert 2746: `progressToken` mismatch across concurrent tool calls. [5.3 #78]

- **A.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **B.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **C.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **D.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**

### 79. At HelixMed Clinical Research Hub, engineers building an MCP server for clinical trial data need to ____. Which configuration correctly implements the MCP specification? Alert 6075: `progressToken` mismatch across concurrent tool calls. [5.3 #79]

- **A.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **B.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **C.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **D.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle

### 80. During clinical trial data review at HelixMed Clinical Research Hub, the MCP server emits debug logs at `error` level. The proper level is ____. Incident 9796: tool `inputSchema` validation skipped, injection observed. [5.4 #80]

- **A.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **B.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **C.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **D.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`

### 81. During an clinical trial data workflow audit at HelixMed Clinical Research Hub, you notice the MCP server exposes file paths without proper checks. The team must ____. Log entry 1213 shows `Method not found -32601` without capability check. [5.4 #81]

- **A.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **B.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **C.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **D.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`

### 82. At HelixMed Clinical Research Hub, engineers building an MCP server for clinical trial data need to ____. Which configuration correctly implements the MCP specification? Incident 8448: OAuth PKCE verifier omitted for public client. [5.4 #82]

- **A.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **B.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **C.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **D.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change

### 83. What is the correct 4-step order for clinical trial data workflow at HelixMed Clinical Research Hub under MCP 2025-11-25? Ticket 7943: `notifications/roots/list_changed` ignored after folder add. Scenario 5.5-2-83.

- **A.** Server embeds client_secret in JS bundle → disable PKCE as optional → return tokens over plain HTTP → cache discovery doc forever without TLS
- **B.** Server exposes `/.well-known/oauth-authorization-server` with PRM & CIMD → client fetches RS metadata with `resource` indicator (RFC 8707) → PKCE + state + RFC 9207 iss validation → audience-bound token issued per resource server
- **C.** Client trusts token from any issuer → skip RFC 9207 iss equality check → ignore RFC 7591 dynamic registration → reuse single token across all resource servers
- **D.** Client sends static API key in Authorization header → server skips issuer discovery → accept tokens with alg:none → grant org-admin scope by default

### 84. HelixMed Clinical Research Hub plans to publish its clinical trial data MCP server to the registry. The publishing step should ____. Log 6160: `initialize` skipped before `tools/list`. [5.5 #84]

- **A.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs
- **B.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **C.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **D.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files

### 85. HelixMed Clinical Research Hub MCP server for clinical trial data uses static API keys in `Authorization`. The OAuth 2.1 migration is to ____. Audit 4631: `includeContext=allServers` exfiltrates cross-server data. [5.5 #85]

- **A.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **B.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **C.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`
- **D.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs

---

## Domain 6 — SDKs, Deployment, Observability & Ecosystem (13–17% blueprint weight · 15 questions)

### 86. The HelixMed Clinical Research Hub team documents the clinical trial data MCP flow. Which sequence of actions is spec-compliant? Review 6828: `outputSchema` mismatched to `structuredContent` shape. Scenario 6.1-2-86.

- **A.** Exfiltrate tool arguments to third-party analytics silently → skip rate limiting on tool calls → omit provenance tags → hide tool calls from audit UI
- **B.** Install random GitHub MCP servers via curl|bash → grant full filesystem + network + env scopes → disable log redaction → store tokens in plaintext
- **C.** Auto-approve all tools without review → trust tool description text as system prompt → allow server to change tool logic post-approval → skip signature verification
- **D.** Pin server versions & verify registry signatures → isolate tool descriptions from executable logic → prompt user before first tool approval & high-risk actions → log tool provenance & monitor for description drift

### 87. For clinical trial data at HelixMed Clinical Research Hub, two best practices align with MCP 2025-11-25. Which two should be implemented? Select two. Trace 1747: 200-tool batch exceeds advertised `maxBatchSize`. [6.1 #87]

- **A.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **B.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **C.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **D.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **E.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs

### 88. A clinical trial data MCP extension at HelixMed Clinical Research Hub leaks `Mcp-Session-Id` across tenants. The team must ____. Trace 1386: batch of 200 tool calls timed out. [6.1 #88]

- **A.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **B.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **C.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs
- **D.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)

### 89. Which two logging/observability actions are correct for clinical trial data MCP at HelixMed Clinical Research Hub? Select two. Alert 4276: `Mcp-Session-Id` reused across tenants. [6.2 #89]

- **A.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`
- **B.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **C.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively
- **D.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **E.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default

### 90. HelixMed Clinical Research Hub MCP server for clinical trial data is deployed as root container with `:latest`. The secure packaging is to ____. Alert 2839: `Mcp-Session-Id` reused across tenants. [6.2 #90]

- **A.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **B.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **C.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **D.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly

### 91. The HelixMed Clinical Research Hub team debugging clinical trial data sees truncated `resources/list` results at 50 items. They should ____. Ticket 5817: `notifications/roots/list_changed` ignored after folder add. [6.2 #91]

- **A.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **B.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **C.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **D.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect

### 92. HelixMed Clinical Research Hub MCP Host for clinical trial data must handle `elicitation/create` versus chat parsing. Which is spec-correct? Review 1189: `outputSchema` mismatched to `structuredContent` shape. [6.3 #92]

- **A.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification
- **B.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **C.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **D.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads

### 93. The MCP Inspector highlights `____` as missing for clinical trial data at HelixMed Clinical Research Hub. Which completion is spec-correct? Review 5979: `completion/complete` implemented as heavy tool call. [6.3 #93] amidst Prometheus alert flapping (variant delta 819).

- **A.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks
- **B.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **C.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **D.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging

### 94. HelixMed Clinical Research Hub reports intermittent `Method not found -32601` errors when accessing clinical trial data. To fix this, the team should ____. Incident 9153: deprecated `/sse` + `/messages` split endpoint still in prod. [6.3 #94]

- **A.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **B.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **C.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **D.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification

### 95. HelixMed Clinical Research Hub engineers designing an MCP system for clinical trial data must evaluate two correct controls. Which two statements are correct? Select two. Ticket 4696: `notifications/roots/list_changed` ignored after folder add. [6.4 #95]

- **A.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **B.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **C.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **D.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **E.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes

### 96. At HelixMed Clinical Research Hub, clinical trial data MCP tool descriptions are concatenated into system prompts. Which safeguard is needed? Review 4118: `outputSchema` mismatched to `structuredContent` shape. [6.4 #96]

- **A.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **B.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **C.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **D.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads

### 97. HelixMed Clinical Research Hub observes its clinical trial data MCP server failing `tools/call` with `Invalid params -32602`. The fix is to ____. Trace 7550: `resource` audience binding missing per RFC 8707. [6.4 #97]

- **A.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **B.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **C.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **D.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603

### 98. For clinical trial data at HelixMed Clinical Research Hub, the Host must reconcile `protocolVersion` negotiation after an upgrade. Which action is correct? Incident MCP-2026-1592 shows Misconfigured `Mcp-Session-Id` routing. [6.5 #98] across IAM policy boundary (variant gamma 773).

- **A.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **B.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks
- **C.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **D.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds

### 99. The MCP Inspector highlights `____` as missing for clinical trial data at HelixMed Clinical Research Hub. Which completion is spec-correct? Alert 7245: `progressToken` mismatch across concurrent tool calls. [6.5 #99]

- **A.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **B.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **C.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **D.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side

### 100. A clinical trial data MCP extension at HelixMed Clinical Research Hub leaks `Mcp-Session-Id` across tenants. The team must ____. Log 6017: `prompt/get` uses client-side interpolation without validation. [6.5 #100]

- **A.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`
- **B.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **C.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **D.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle

---

## Answer Key and Explanations

### Question 1 — `C, E` (MCP Foundations, Architecture & Lifecycle)

Correct answers: C and E (are correct). Per MCP 2025-11-25, Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 1.1 validation S2Q001. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **B:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **C:** Correct. maps transport to deployment topology: stdio gives OS-level isolation locally; Streamable HTTP enables remote multi-tenant scale.
- **D:** Incorrect. assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.
- **E:** Correct. clarifies layer boundaries: MCP standardizes context attachment; function calling is inline model schema; A2A negotiates task handoffs.

### Question 2 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). This follows the MCP specification for Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 1.1 validation S2Q002. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Correct. correctly separates trust boundaries: Hosts own UI/policy, Clients speak MCP, Servers expose capabilities behind capability negotiation.
- **B:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.
- **C:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.
- **D:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.

### Question 3 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). MCP 2025-11-25 requires Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model; the alternative breaks capability negotiation or security for clinical trial data. Skill 1.1 validation S2Q003. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **B:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **C:** Correct. correctly separates trust boundaries: Hosts own UI/policy, Clients speak MCP, Servers expose capabilities behind capability negotiation.
- **D:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.

### Question 4 — `B, E` (MCP Foundations, Architecture & Lifecycle)

Correct answers: B and E (are correct). This follows the MCP specification for Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 1.2 validation S2Q004. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.
- **B:** Correct. enables forwards-compatible evolution without breaking older Hosts or Servers on version skew.
- **C:** Incorrect. requiring clients to poll list on a timer to detect new resources defeats MCP push efficiency.
- **D:** Incorrect. parsing free-form chat replies as structured data instead of typed elicitation invites format errors and injection.
- **E:** Correct. provides spec-guaranteed failure detection where OS TCP keepalives are invisible to application-level SSE/stdio proxies.

### Question 5 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). This follows the MCP specification for Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 1.2 validation S2Q005. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.
- **B:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.
- **C:** Incorrect. skipping Inspector and relying only on unit mocks misses real transport framing and pagination/cancellation bugs.
- **D:** Correct. guarantees version and capability compatibility before feature calls, satisfying the MCP lifecycle invariant.

### Question 6 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). This follows the MCP specification for Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 1.2 validation S2Q006. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Correct. lets each party call only negotiated features, avoiding methodNotFound and silent fallback hallucinations.
- **B:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.
- **C:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **D:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.

### Question 7 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). Per MCP 2025-11-25, Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy ensures spec-compliant lifecycle and isolation for clinical trial data. Reference 1.3 S2Q007. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Incorrect. reversing the initialize direction and mixing OAuth into initialize params conflates lifecycle with authorization.
- **B:** Correct. follows MCP lifecycle spec: version/capability negotiation via initialize exchange completed by initialized notification before any feature calls.
- **C:** Incorrect. hardcoding protocol versions and duplicate initialize pings breaks forward compatibility and lifecycle idempotency.
- **D:** Incorrect. invoking tools before initialize negotiation bypasses version checks and omits the required initialized signal.

### Question 8 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). This choice correctly implements Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 1.3 validation S2Q008. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Correct. separates best-effort telemetry from correlated RPC state per JSON-RPC 2.0, preventing notification ID collisions.
- **B:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.
- **C:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **D:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.

### Question 9 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). Selecting this honors Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy and prevents the listed failure mode in HelixMed Clinical Research Hub clinical trial data flows. Skill 1.3 validation S2Q009. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **B:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.
- **C:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **D:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.

### Question 10 — `A, C, E` (MCP Foundations, Architecture & Lifecycle)

Correct answers: A, C, and E (are correct). This choice correctly implements Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 1.4 validation S2Q010. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Correct. lets each party call only negotiated features, avoiding methodNotFound and silent fallback hallucinations.
- **B:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **C:** Correct. allows safe iteration on draft specs like Tasks and elicitation without polluting the stable capability surface.
- **D:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **E:** Correct. enables forwards-compatible evolution without breaking older Hosts or Servers on version skew.
- **F:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.

### Question 11 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). MCP 2025-11-25 requires Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging); the alternative breaks capability negotiation or security for clinical trial data. Skill 1.4 validation S2Q011. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Correct. lets each party call only negotiated features, avoiding methodNotFound and silent fallback hallucinations.
- **B:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.
- **C:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.
- **D:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.

### Question 12 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). Selecting this honors Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) and prevents the listed failure mode in HelixMed Clinical Research Hub clinical trial data flows. Skill 1.4 validation S2Q012. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **B:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **C:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **D:** Correct. allows safe iteration on draft specs like Tasks and elicitation without polluting the stable capability surface.

### Question 13 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). This follows the MCP specification for Manage keepalive pings, progress notifications, cancellation, and shutdown semantics, correcting the insecure/incompatible anti-pattern for clinical trial data. Reference 1.5 S2Q013. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. matches MCP Tools spec: declarative schema, client discovery, validated execution, and structured content/error signaling.
- **B:** Incorrect. responding before validation and ignoring list_changed events leaves clients with stale, unvalidated tool catalogs.
- **C:** Incorrect. missing inputSchema and raw shell interpolation from unvalidated LLM strings creates prompt-injection and RCE risk.
- **D:** Incorrect. ad-hoc tool creation without validation and massive single-block responses break type safety and token budgets.

### Question 14 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). Per MCP 2025-11-25, Manage keepalive pings, progress notifications, cancellation, and shutdown semantics ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 1.5 validation S2Q014. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **B:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.
- **C:** Correct. survives AWS ALB 60s idle timeout and Kubernetes GFE that silently drops idle SSE streams.
- **D:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.

### Question 15 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). MCP 2025-11-25 requires Manage keepalive pings, progress notifications, cancellation, and shutdown semantics; the alternative breaks capability negotiation or security for clinical trial data. Skill 1.5 validation S2Q015. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **B:** Incorrect. enabling experimental tasks by default without capability checks forces unready clients into breaking draft methods.
- **C:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **D:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.

### Question 16 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). Per MCP 2025-11-25, Differentiate MCP from function calling, A2A, and experimental capability progression ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 1.6 validation S2Q016. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.
- **B:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.
- **C:** Correct. uses MCP vertically for capabilities and A2A horizontally for peer negotiation, per LM-Foundation AAIF stack guidance.
- **D:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.

### Question 17 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). Selecting this honors Differentiate MCP from function calling, A2A, and experimental capability progression and prevents the listed failure mode in HelixMed Clinical Research Hub clinical trial data flows. Skill 1.6 validation S2Q017. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **B:** Incorrect. distributing servers as raw GitHub tarballs without server.json or publisher proof hides supply-chain compromise.
- **C:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **D:** Correct. uses MCP vertically for capabilities and A2A horizontally for peer negotiation, per LM-Foundation AAIF stack guidance.

### Question 18 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). This follows the MCP specification for Differentiate MCP from function calling, A2A, and experimental capability progression, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 1.6 validation S2Q018. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **B:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.
- **C:** Correct. clarifies layer boundaries: MCP standardizes context attachment; function calling is inline model schema; A2A negotiates task handoffs.
- **D:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.

### Question 19 — `A, B` (Tools, Resources & Resource Templates)

Correct answers: A and B (are correct). This choice correctly implements Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 2.1 validation S2Q019. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. uses typed server helpers that auto-wire tools/list/call handlers and JSON Schema validation from Zod objects.
- **B:** Correct. signals cost/safety posture without hard-coding policy; models prefer readOnly before destructive in multi-step plans.
- **C:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **D:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.
- **E:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.

### Question 20 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Per MCP 2025-11-25, Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 2.1 validation S2Q020. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **B:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **C:** Correct. gives models complete, machine-validated contracts for tool selection and argument generation.
- **D:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.

### Question 21 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). Per MCP 2025-11-25, Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 2.1 validation S2Q021. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. preserves user/model agency and auditability; every mutation traces to an explicit model decision with tool audit event.
- **B:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **C:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **D:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.

### Question 22 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Per MCP 2025-11-25, Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 2.1 validation S2Q022. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. distributing servers as raw GitHub tarballs without server.json or publisher proof hides supply-chain compromise.
- **B:** Incorrect. assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.
- **C:** Correct. signals cost/safety posture without hard-coding policy; models prefer readOnly before destructive in multi-step plans.
- **D:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.

### Question 23 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). MCP 2025-11-25 requires Control model-controlled tool execution, list discovery, validation, and structured content output; the alternative breaks capability negotiation or security for clinical trial data. Skill 2.2 validation S2Q023. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.
- **B:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.
- **C:** Correct. defends against LLM hallucinated args and preserves typed error handling via isError flag versus exception propagation.
- **D:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.

### Question 24 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). MCP 2025-11-25 requires Control model-controlled tool execution, list discovery, validation, and structured content output; the alternative breaks capability negotiation or security for clinical trial data. Skill 2.2 validation S2Q024. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Correct. bridges LLM reasoning with downstream code that consumes validated JSON, not regex scraped prose.
- **B:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **C:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.
- **D:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.

### Question 25 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). MCP 2025-11-25 requires Control model-controlled tool execution, list discovery, validation, and structured content output; the alternative breaks capability negotiation or security for clinical trial data. Skill 2.2 validation S2Q025. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.
- **B:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **C:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **D:** Correct. bridges LLM reasoning with downstream code that consumes validated JSON, not regex scraped prose.

### Question 26 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). This choice correctly implements Control model-controlled tool execution, list discovery, validation, and structured content output for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 2.2 validation S2Q026. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. generating random progressTokens server-side with no binding to request id mixes streams across concurrent tasks.
- **B:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **C:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **D:** Correct. bridges LLM reasoning with downstream code that consumes validated JSON, not regex scraped prose.

### Question 27 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). MCP 2025-11-25 requires Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed; the alternative breaks capability negotiation or security for clinical trial data. Reference 2.3 S2Q027. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Correct. follows Resources spec: capability advertisement, list/template discovery, uri-addressed reads with mime-typed contents and pagination.
- **B:** Incorrect. omitting uri and mimeType fields and ignoring pagination cursors makes resources unaddressable and unfilterable.
- **C:** Incorrect. guessing URIs and exposing raw OS paths without scheme checks violates resource discovery and isolation.
- **D:** Incorrect. tight polling without subscription to list_changed notifications defeats MCP push efficiency and protocol layering.

### Question 28 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). Per MCP 2025-11-25, Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 2.3 validation S2Q028. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **B:** Correct. enables complete catalog sync for hosts that cache tool lists and paginate beyond 50 items without omission.
- **C:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.
- **D:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.

### Question 29 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). This follows the MCP specification for Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 2.3 validation S2Q029. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.
- **B:** Correct. enables complete catalog sync for hosts that cache tool lists and paginate beyond 50 items without omission.
- **C:** Incorrect. batching 200 unrelated tool calls into one HTTP request beyond advertised limits times out the whole batch.
- **D:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.

### Question 30 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). MCP 2025-11-25 requires Address direct resources vs templated resources with URI schemes, names, and mimeTypes; the alternative breaks capability negotiation or security for clinical trial data. Skill 2.4 validation S2Q030. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **B:** Correct. delivers typed content blocks that render correctly in Host UIs with binary vs text handling pre-decided by mimeType.
- **C:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **D:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.

### Question 31 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Per MCP 2025-11-25, Address direct resources vs templated resources with URI schemes, names, and mimeTypes ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 2.4 validation S2Q031. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.
- **B:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **C:** Correct. delivers typed content blocks that render correctly in Host UIs with binary vs text handling pre-decided by mimeType.
- **D:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.

### Question 32 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Per MCP 2025-11-25, Address direct resources vs templated resources with URI schemes, names, and mimeTypes ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 2.4 validation S2Q032. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. reimplementing a Postgres MCP server from scratch when a registry-verified one already exists wastes review cycles.
- **B:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.
- **C:** Correct. delivers typed content blocks that render correctly in Host UIs with binary vs text handling pre-decided by mimeType.
- **D:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.

### Question 33 — `B, E` (Tools, Resources & Resource Templates)

Correct answers: B and E (are correct). This choice correctly implements Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 2.5 validation S2Q033. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.
- **B:** Correct. handles 10k-file workspaces without truncation or timeout, matching MCP pagination contract for both lists.
- **C:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.
- **D:** Incorrect. setting includeContext=allServers by default fans sensitive data from every connected server into one sampling call.
- **E:** Correct. delivers typed content blocks that render correctly in Host UIs with binary vs text handling pre-decided by mimeType.

### Question 34 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). MCP 2025-11-25 requires Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows; the alternative breaks capability negotiation or security for clinical trial data. Skill 2.5 validation S2Q034. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Correct. pushes freshness efficiently after external ingestion jobs create new datasets, without constant re-list overhead.
- **B:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.
- **C:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **D:** Incorrect. implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.

### Question 35 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Selecting this honors Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows and prevents the listed failure mode in HelixMed Clinical Research Hub clinical trial data flows. Skill 2.5 validation S2Q035. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.
- **B:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **C:** Correct. pushes freshness efficiently after external ingestion jobs create new datasets, without constant re-list overhead.
- **D:** Incorrect. deploying greenfield on the deprecated dual-endpoint SSE transport incurs future migration cost and lacks session IDs.

### Question 36 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). MCP 2025-11-25 requires Declare prompts and completions for argument typeahead and parameterized prompt expansion; the alternative breaks capability negotiation or security for clinical trial data. Reference 2.6 S2Q036. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. exposing full drive without consent and walking above root boundaries with symlink following enables directory traversal.
- **B:** Correct. implements Roots spec: client-owned boundary declaration, server-enforced confinement, and dynamic list_changed handling.
- **C:** Incorrect. letting servers dictate client filesystem boundaries inverts MCP trust and breaks host isolation.
- **D:** Incorrect. hardcoding roots and ignoring list_changed notifications leaves stale boundaries after user permission changes.

### Question 37 — `A, D` (Tools, Resources & Resource Templates)

Correct answers: A and D (are correct). Per MCP 2025-11-25, Declare prompts and completions for argument typeahead and parameterized prompt expansion ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 2.6 validation S2Q037. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. keeps prompt pickers fresh without re-listing on every keystroke, matching resource/tool change notification pattern.
- **B:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **C:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.
- **D:** Correct. powers low-latency autocomplete dropdowns directly from server-side datasets without tool execution overhead.
- **E:** Incorrect. skipping Inspector and relying only on unit mocks misses real transport framing and pagination/cancellation bugs.

### Question 38 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). This choice correctly implements Declare prompts and completions for argument typeahead and parameterized prompt expansion for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 2.6 validation S2Q038. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **B:** Incorrect. logging full tool arguments including customer PII and bearer tokens creates GDPR and credential-leak second-order risks.
- **C:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **D:** Correct. keeps prompt pickers fresh without re-listing on every keystroke, matching resource/tool change notification pattern.

### Question 39 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). This follows the MCP specification for Expose and expand prompts via prompts/list, prompts/get, and argument validation, correcting the insecure/incompatible anti-pattern for clinical trial data. Reference 3.1 S2Q039. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. default-exposed sampling and uncapped recursive loops risk token runaway and expose internal reasoning inappropriately.
- **B:** Incorrect. unbounded PII-laden sampling without capability or consent bypasses privacy and authorization boundaries.
- **C:** Correct. follows Sampling spec: capability-checked server-initiated LLM delegation with explicit modelPreferences and human approval gating.
- **D:** Incorrect. confusing sampling payloads with tool metadata conflates delegation layers and breaks cost attribution.

### Question 40 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). This choice correctly implements Expose and expand prompts via prompts/list, prompts/get, and argument validation for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 3.1 validation S2Q040. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.
- **B:** Incorrect. generating random progressTokens server-side with no binding to request id mixes streams across concurrent tasks.
- **C:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **D:** Correct. turns curated prompt packs into discoverable UX shortcuts argument-by-argument with typed validation.

### Question 41 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). This choice correctly implements Expose and expand prompts via prompts/list, prompts/get, and argument validation for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 3.1 validation S2Q041. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. dumping base64 blobs as plain text without typed content blocks loses mimeType and forces heuristic parsing.
- **B:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **C:** Incorrect. setting includeContext=allServers by default fans sensitive data from every connected server into one sampling call.
- **D:** Correct. compiles parameterized prompt templates server-side with validated args, keeping prompt injection surface server-controlled.

### Question 42 — `B, D` (Prompts, Sampling, Roots & Elicitation)

Correct answers: B and D (are correct). This choice correctly implements Enforce client-owned filesystem boundaries via roots/list and roots/list_changed for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 3.2 validation S2Q042. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **B:** Correct. keeps server views consistent when users add/remove workspace folders mid-session without restart.
- **C:** Incorrect. treating MCP as a replacement for A2A agent discovery and task lifecycles conflates vertical tool attachment with peer delegation.
- **D:** Correct. prevents `../` and symlink hop attacks that would escape the user’s approved `file://` allowlist.
- **E:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.

### Question 43 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). This follows the MCP specification for Enforce client-owned filesystem boundaries via roots/list and roots/list_changed, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 3.2 validation S2Q043. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.
- **B:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **C:** Correct. prevents `../` and symlink hop attacks that would escape the user’s approved `file://` allowlist.
- **D:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.

### Question 44 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). This follows the MCP specification for Enforce client-owned filesystem boundaries via roots/list and roots/list_changed, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 3.2 validation S2Q044. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. prevents `../` and symlink hop attacks that would escape the user’s approved `file://` allowlist.
- **B:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **C:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **D:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.

### Question 45 — `B, D, F` (Prompts, Sampling, Roots & Elicitation)

Correct answers: B, D, and F (are correct). MCP 2025-11-25 requires Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls; the alternative breaks capability negotiation or security for clinical trial data. Skill 3.3 validation S2Q045. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.
- **B:** Correct. lets servers delegate LLM sub-tasks (summarization, critique) back to the Host model under explicit preference caps.
- **C:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **D:** Correct. limits what prior server context flows into delegated sampling calls, preventing cross-server data exfiltration.
- **E:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **F:** Correct. separates fact acquisition (user-filled forms) from subjective generation (model-composed prose) for audit clarity.

### Question 46 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). Selecting this honors Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls and prevents the listed failure mode in HelixMed Clinical Research Hub clinical trial data flows. Skill 3.3 validation S2Q046. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. limits what prior server context flows into delegated sampling calls, preventing cross-server data exfiltration.
- **B:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.
- **C:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **D:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.

### Question 47 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). Per MCP 2025-11-25, Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 3.3 validation S2Q047. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. logging full tool arguments including customer PII and bearer tokens creates GDPR and credential-leak second-order risks.
- **B:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **C:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **D:** Correct. maps server intent to Host model fleet tiers without hardcoding vendor model IDs into server code.

### Question 48 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). This choice correctly implements Collect human input via elicitation/create with requestedSchema and form round-trips for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 3.4 validation S2Q048. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **B:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.
- **C:** Correct. lets servers delegate LLM sub-tasks (summarization, critique) back to the Host model under explicit preference caps.
- **D:** Incorrect. installing random `curl | bash` MCP servers without registry signature verification imports unvetted RCE into the IDE.

### Question 49 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). Per MCP 2025-11-25, Collect human input via elicitation/create with requestedSchema and form round-trips ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 3.4 validation S2Q049. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. joining user input with path concatenation without canonicalization enables classic directory traversal.
- **B:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **C:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.
- **D:** Correct. turns server data needs into typed Host-rendered forms rather than chat text parsing, with explicit schema validation.

### Question 50 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). MCP 2025-11-25 requires Collect human input via elicitation/create with requestedSchema and form round-trips; the alternative breaks capability negotiation or security for clinical trial data. Skill 3.4 validation S2Q050. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. separates fact acquisition (user-filled forms) from subjective generation (model-composed prose) for audit clarity.
- **B:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.
- **C:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.
- **D:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.

### Question 51 — `C, D` (Prompts, Sampling, Roots & Elicitation)

Correct answers: C and D (are correct). MCP 2025-11-25 requires Regulate verbosity via logging/setLevel and notifications/message level filtering; the alternative breaks capability negotiation or security for clinical trial data. Skill 3.5 validation S2Q051. [Skill 3.5: Regulate verbosity via logging/setLevel and notifications/message level filtering | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/logging/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. installing random `curl | bash` MCP servers without registry signature verification imports unvetted RCE into the IDE.
- **B:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **C:** Correct. correlates streaming progress notifications to the correct in-flight tool/resource fetch without guessing.
- **D:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.
- **E:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.

### Question 52 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). This choice correctly implements Regulate verbosity via logging/setLevel and notifications/message level filtering for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 3.5 validation S2Q052. [Skill 3.5: Regulate verbosity via logging/setLevel and notifications/message level filtering | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/logging/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **B:** Correct. correlates streaming progress notifications to the correct in-flight tool/resource fetch without guessing.
- **C:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.
- **D:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.

### Question 53 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). Per MCP 2025-11-25, Correlate progress and completion flows with progressToken and completion/complete semantics ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 3.6 validation S2Q053. [Skill 3.6: Correlate progress and completion flows with progressToken and completion/complete semantics | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/prompts]

- **A:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **B:** Incorrect. joining user input with path concatenation without canonicalization enables classic directory traversal.
- **C:** Correct. powers low-latency autocomplete dropdowns directly from server-side datasets without tool execution overhead.
- **D:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.

### Question 54 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). This choice correctly implements Correlate progress and completion flows with progressToken and completion/complete semantics for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 3.6 validation S2Q054. [Skill 3.6: Correlate progress and completion flows with progressToken and completion/complete semantics | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/prompts]

- **A:** Incorrect. treating MCP as a replacement for A2A agent discovery and task lifecycles conflates vertical tool attachment with peer delegation.
- **B:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.
- **C:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.
- **D:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.

### Question 55 — `A, B` (Transports, Sessions & Protocol Evolution)

Correct answers: A and B (are correct). Selecting this honors Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle and prevents the listed failure mode in HelixMed Clinical Research Hub clinical trial data flows. Skill 4.1 validation S2Q055. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.
- **B:** Correct. gives OS-level isolation, clean env var scoping, and automatic teardown when Host exits without port conflicts.
- **C:** Incorrect. assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.
- **D:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **E:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.

### Question 56 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). MCP 2025-11-25 requires Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle; the alternative breaks capability negotiation or security for clinical trial data. Skill 4.1 validation S2Q056. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Correct. prevents log interleaving from corrupting JSON-RPC framing that parsers expect line-delimited on stdout.
- **B:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.
- **C:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **D:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.

### Question 57 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). Per MCP 2025-11-25, Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 4.1 validation S2Q057. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.
- **B:** Incorrect. installing random `curl | bash` MCP servers without registry signature verification imports unvetted RCE into the IDE.
- **C:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **D:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.

### Question 58 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). MCP 2025-11-25 requires Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response); the alternative breaks capability negotiation or security for clinical trial data. Skill 4.2 validation S2Q058. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **B:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **C:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **D:** Correct. recovers progress streams and notifications lost during 5–30s mobile handoffs without missing tool progress events.

### Question 59 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). This choice correctly implements Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 4.2 validation S2Q059. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. lets simple request/reply skip SSE overhead while enabling streaming only for long-running tool progress.
- **B:** Incorrect. generating random progressTokens server-side with no binding to request id mixes streams across concurrent tasks.
- **C:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.
- **D:** Incorrect. skipping Inspector and relying only on unit mocks misses real transport framing and pagination/cancellation bugs.

### Question 60 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). Selecting this honors Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) and prevents the listed failure mode in HelixMed Clinical Research Hub clinical trial data flows. Skill 4.2 validation S2Q060. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.
- **B:** Correct. recovers progress streams and notifications lost during 5–30s mobile handoffs without missing tool progress events.
- **C:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.
- **D:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.

### Question 61 — `B, C` (Transports, Sessions & Protocol Evolution)

Correct answers: B and C (are correct). Selecting this honors Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay and prevents the listed failure mode in HelixMed Clinical Research Hub clinical trial data flows. Skill 4.3 validation S2Q061. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.
- **B:** Correct. tracks spec evolution: split GET /sse + POST /messages merged into single POST with Accept-driven streaming.
- **C:** Correct. avoids thundering herds after gateway restarts while ensuring exactly-once progress recovery via resumability.
- **D:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **E:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.

### Question 62 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). This follows the MCP specification for Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 4.3 validation S2Q062. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.
- **B:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **C:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **D:** Correct. tracks spec evolution: split GET /sse + POST /messages merged into single POST with Accept-driven streaming.

### Question 63 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). Selecting this honors Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay and prevents the listed failure mode in HelixMed Clinical Research Hub clinical trial data flows. Skill 4.3 validation S2Q063. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Incorrect. skipping Inspector and relying only on unit mocks misses real transport framing and pagination/cancellation bugs.
- **B:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.
- **C:** Correct. recovers progress streams and notifications lost during 5–30s mobile handoffs without missing tool progress events.
- **D:** Incorrect. setting includeContext=allServers by default fans sensitive data from every connected server into one sampling call.

### Question 64 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). This follows the MCP specification for Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP, correcting the insecure/incompatible anti-pattern for clinical trial data. Reference 4.4 S2Q064. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Incorrect. returning HTML instead of JSON-RPC errors and retrying without backoff causes parsing failures and duplicate mutations.
- **B:** Correct. matches 2025-11-25 Streamable HTTP spec: single endpoint, dual Accept, session ID management, and resumable SSE stream option.
- **C:** Incorrect. unbounded batching and cross-tenant session ID reuse breaks rate limiting and tenant isolation guarantees.
- **D:** Incorrect. splitting endpoints and ignoring session/resumability headers reverts to pre-March 2025 deprecated SSE transport.

### Question 65 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). MCP 2025-11-25 requires Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP; the alternative breaks capability negotiation or security for clinical trial data. Skill 4.4 validation S2Q065. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **B:** Correct. avoids thundering herds after gateway restarts while ensuring exactly-once progress recovery via resumability.
- **C:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **D:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.

### Question 66 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). Per MCP 2025-11-25, Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 4.4 validation S2Q066. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.
- **B:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **C:** Correct. tracks spec evolution: split GET /sse + POST /messages merged into single POST with Accept-driven streaming.
- **D:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.

### Question 67 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). This follows the MCP specification for Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 4.5 validation S2Q067. [Skill 4.5: Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/progress/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. avoids thundering herds after gateway restarts while ensuring exactly-once progress recovery via resumability.
- **B:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **C:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.
- **D:** Incorrect. collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.

### Question 68 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). Selecting this honors Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation and prevents the listed failure mode in HelixMed Clinical Research Hub clinical trial data flows. Skill 4.5 validation S2Q068. [Skill 4.5: Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/progress/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **B:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **C:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.
- **D:** Correct. keeps MCP semantics intact through enterprise L7 filters that otherwise strip SSE headers and session sticky state.

### Question 69 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). This follows the MCP specification for Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 4.6 validation S2Q069. [Skill 4.6: Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/cancellation/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. keeps MCP semantics intact through enterprise L7 filters that otherwise strip SSE headers and session sticky state.
- **B:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.
- **C:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **D:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.

### Question 70 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). MCP 2025-11-25 requires Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival; the alternative breaks capability negotiation or security for clinical trial data. Skill 4.6 validation S2Q070. [Skill 4.6: Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/cancellation/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. exploits batching for listing throughput without overwhelming server concurrency caps or mixing response IDs.
- **B:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **C:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.
- **D:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.

### Question 71 — `B, E` (Authorization, Security, Trust & Registry)

Correct answers: B and E (are correct). This choice correctly implements Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 5.1 validation S2Q071. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **B:** Correct. aligns MCP with current OAuth 2.1 security posture, eliminating token leakage vectors of legacy grants.
- **C:** Incorrect. joining user input with path concatenation without canonicalization enables classic directory traversal.
- **D:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **E:** Correct. scales zero-touch onboarding across thousands of tenant Host instances without manual client_id provisioning.

### Question 72 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). MCP 2025-11-25 requires Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata; the alternative breaks capability negotiation or security for clinical trial data. Skill 5.1 validation S2Q072. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **B:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.
- **C:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **D:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.

### Question 73 — `A` (Authorization, Security, Trust & Registry)

Correct answer: A (is correct). Per MCP 2025-11-25, Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 5.1 validation S2Q073. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.
- **B:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.
- **C:** Incorrect. printing logs to stdout alongside JSON-RPC breaks line-delimited parsing and throws Parse error -32700.
- **D:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.

### Question 74 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). MCP 2025-11-25 requires Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings; the alternative breaks capability negotiation or security for clinical trial data. Skill 5.2 validation S2Q074. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.
- **B:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **C:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.
- **D:** Incorrect. collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.

### Question 75 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). Per MCP 2025-11-25, Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 5.2 validation S2Q075. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **B:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.
- **C:** Correct. keeps refresh tokens survivable across restarts but invisible to process dumps, forked children, and leaked logs.
- **D:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.

### Question 76 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). This choice correctly implements Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 5.2 validation S2Q076. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **B:** Correct. keeps refresh tokens survivable across restarts but invisible to process dumps, forked children, and leaked logs.
- **C:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.
- **D:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.

### Question 77 — `B, E, F` (Authorization, Security, Trust & Registry)

Correct answers: B, E, and F (are correct). MCP 2025-11-25 requires Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality; the alternative breaks capability negotiation or security for clinical trial data. Skill 5.3 validation S2Q077. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **B:** Correct. prevents token replay to unintended resource servers by audience-restricting each bearer token.
- **C:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.
- **D:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **E:** Correct. enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.
- **F:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.

### Question 78 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). This follows the MCP specification for Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 5.3 validation S2Q078. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.
- **B:** Correct. binds public client identity to TLS-verifiable origin without long-lived client secrets in distributed Hosts.
- **C:** Incorrect. deploying greenfield on the deprecated dual-endpoint SSE transport incurs future migration cost and lacks session IDs.
- **D:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.

### Question 79 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). This choice correctly implements Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 5.3 validation S2Q079. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.
- **B:** Correct. enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.
- **C:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.
- **D:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.

### Question 80 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). This follows the MCP specification for Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 5.4 validation S2Q080. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.
- **B:** Correct. displays descriptions for human review but never concatenates them into system prompts or plan steps as trusted policy.
- **C:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.
- **D:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.

### Question 81 — `A` (Authorization, Security, Trust & Registry)

Correct answer: A (is correct). MCP 2025-11-25 requires Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model; the alternative breaks capability negotiation or security for clinical trial data. Skill 5.4 validation S2Q081. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Correct. tags third-party fetched content so downstream Hosts can sandtrap it before the model treats it as instruction.
- **B:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **C:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **D:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.

### Question 82 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). MCP 2025-11-25 requires Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model; the alternative breaks capability negotiation or security for clinical trial data. Skill 5.4 validation S2Q082. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Incorrect. deploying greenfield on the deprecated dual-endpoint SSE transport incurs future migration cost and lacks session IDs.
- **B:** Incorrect. enabling experimental tasks by default without capability checks forces unready clients into breaking draft methods.
- **C:** Incorrect. requiring clients to poll list on a timer to detect new resources defeats MCP push efficiency.
- **D:** Correct. forces re-approval when a benign `get_weather` server silently rewires to `exfiltrate_files` after approval.

### Question 83 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). Selecting this honors Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging and prevents the listed failure mode in HelixMed Clinical Research Hub clinical trial data flows. Reference 5.5 S2Q083. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Incorrect. exposing secrets in client bundles and downgrading PKCE/TLS undermines OAuth confidentiality and channel binding.
- **B:** Correct. follows MCP auth spec evolution: OAuth 2.1 with PKCE, protected resource metadata, RFC 8707 audience binding, and RFC 9207 issuer checks.
- **C:** Incorrect. reusing a single audience-less token across resource servers enables cross-server token replay and mix-up attacks.
- **D:** Incorrect. hardcoded keys and alg:none tokens with blanket admin grants violate OAuth 2.1 and privilege separation.

### Question 84 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). This follows the MCP specification for Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 5.5 validation S2Q084. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.
- **B:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.
- **C:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.
- **D:** Correct. keeps refresh tokens survivable across restarts but invisible to process dumps, forked children, and leaked logs.

### Question 85 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). MCP 2025-11-25 requires Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging; the alternative breaks capability negotiation or security for clinical trial data. Skill 5.5 validation S2Q085. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **B:** Correct. forces re-approval when a benign `get_weather` server silently rewires to `exfiltrate_files` after approval.
- **C:** Incorrect. calling tools before the initialized handshake completes races capability discovery and throws methodNotFound errors.
- **D:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.

### Question 86 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). MCP 2025-11-25 requires Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic); the alternative breaks capability negotiation or security for clinical trial data. Reference 6.1 S2Q086. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Incorrect. silent exfiltration without rate limits or audit visibility breaks data minimization and incident-response traceability.
- **B:** Incorrect. unvetted curl-piped installs with maximal scopes and plaintext token storage maximizes blast radius from a single malicious server.
- **C:** Incorrect. blind auto-approval and treating descriptions as trusted instructions invites prompt injection and supply-chain compromise.
- **D:** Correct. applies MCP security checklist: supply-chain pinning, description-vs-logic separation, consent gating, and provenance monitoring against poison/rug-pull.

### Question 87 — `A, C` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: A and C (are correct). Selecting this honors Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) and prevents the listed failure mode in HelixMed Clinical Research Hub clinical trial data flows. Skill 6.1 validation S2Q087. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Correct. gives decorator-ergonomic tool/resource registration with Pydantic/JSON Schema coherence across Python Hosts.
- **B:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.
- **C:** Correct. standardizes transport selection, capability tracking, and request/notification routing behind a single Client facade.
- **D:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **E:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.

### Question 88 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). Per MCP 2025-11-25, Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 6.1 validation S2Q088. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **B:** Correct. standardizes transport selection, capability tracking, and request/notification routing behind a single Client facade.
- **C:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.
- **D:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.

### Question 89 — `C, D` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: C and D (are correct). This follows the MCP specification for Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 6.2 validation S2Q089. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.
- **B:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.
- **C:** Correct. catches lifecycle, capability, and schema mismatches before CI with real-transport conformance testing.
- **D:** Correct. standardizes transport selection, capability tracking, and request/notification routing behind a single Client facade.
- **E:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.

### Question 90 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). MCP 2025-11-25 requires Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates; the alternative breaks capability negotiation or security for clinical trial data. Skill 6.2 validation S2Q090. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **B:** Correct. automates protocol conformance as a PR check alongside lint/tests, proving list/call contracts headlessly.
- **C:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.
- **D:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.

### Question 91 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). This follows the MCP specification for Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 6.2 validation S2Q091. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **B:** Correct. automates protocol conformance as a PR check alongside lint/tests, proving list/call contracts headlessly.
- **C:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.
- **D:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.

### Question 92 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). This choice correctly implements Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 6.3 validation S2Q092. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Correct. makes servers discoverable with verifiable supply-chain metadata and semver-aware update notifications.
- **B:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.
- **C:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.
- **D:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.

### Question 93 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). This follows the MCP specification for Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation, correcting the insecure/incompatible anti-pattern for clinical trial data. Skill 6.3 validation S2Q093. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Incorrect. treating MCP as a replacement for A2A agent discovery and task lifecycles conflates vertical tool attachment with peer delegation.
- **B:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **C:** Correct. ensures reproducible, least-privilege runtime with declared transport and liveness for orchestrators.
- **D:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.

### Question 94 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). Per MCP 2025-11-25, Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 6.3 validation S2Q094. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.
- **B:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **C:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **D:** Correct. makes servers discoverable with verifiable supply-chain metadata and semver-aware update notifications.

### Question 95 — `A, B` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: A and B (are correct). Per MCP 2025-11-25, Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 6.4 validation S2Q095. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Correct. traces tool call latency through Streamable HTTP gateways into server execution with per-session correlation.
- **B:** Correct. powers per-tool SLOs and supply-chain forensics without persisting sensitive tool argument values.
- **C:** Incorrect. enabling experimental tasks by default without capability checks forces unready clients into breaking draft methods.
- **D:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.
- **E:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.

### Question 96 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). MCP 2025-11-25 requires Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation; the alternative breaks capability negotiation or security for clinical trial data. Skill 6.4 validation S2Q096. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.
- **B:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **C:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.
- **D:** Correct. respects user-selected verbosity while still flowing warnings/errors through observability pipelines.

### Question 97 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). Selecting this honors Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation and prevents the listed failure mode in HelixMed Clinical Research Hub clinical trial data flows. Skill 6.4 validation S2Q097. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.
- **B:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.
- **C:** Correct. traces tool call latency through Streamable HTTP gateways into server execution with per-session correlation.
- **D:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.

### Question 98 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). MCP 2025-11-25 requires Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns; the alternative breaks capability negotiation or security for clinical trial data. Skill 6.5 validation S2Q098. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.
- **B:** Correct. uses MCP vertically for capabilities and A2A horizontally for peer negotiation, per LM-Foundation AAIF stack guidance.
- **C:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.
- **D:** Incorrect. reimplementing a Postgres MCP server from scratch when a registry-verified one already exists wastes review cycles.

### Question 99 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). This choice correctly implements Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns for HelixMed Clinical Research Hub while the distractors violate transport/session guarantees. Skill 6.5 validation S2Q099. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **B:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **C:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **D:** Correct. prevents a read-only doc-search server from silently acquiring destructive write scopes after one-time user approval.

### Question 100 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). Per MCP 2025-11-25, Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns ensures spec-compliant lifecycle and isolation for clinical trial data. Skill 6.5 validation S2Q100. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Incorrect. setting includeContext=allServers by default fans sensitive data from every connected server into one sampling call.
- **B:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.
- **C:** Correct. prevents a read-only doc-search server from silently acquiring destructive write scopes after one-time user approval.
- **D:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
