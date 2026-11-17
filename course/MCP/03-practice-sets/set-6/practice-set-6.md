# MCP: Model Context Protocol: Servers, Clients, Transports & Security — Full-Length Mock Exam 6 — Sentinel Cyber Fusion (Security & SOC Automation)

**Theme:** SSE Deprecation → Streamable HTTP, Batching, Reconnect Resumability & Gateway Mesh  
**Credential alignment:** `Model Context Protocol (MCP 2025-11-25) — Tool & Context Standard`  
**Blueprint baseline:** `November 2026 (MCP Specification 2025-11-25 · MCP Registry & Inspector · OAuth 2.1 + RFC 8707/9207 + CIMD · OWASP MCP Security Checklist)` (https://modelcontextprotocol.io/introduction · https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation · https://genai.owasp.org/resource/mcp-security-checklist/)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `120 minutes` (`72 seconds/question` full-endurance pacing; aligns with `120 minutes` on NVIDIA NCP-AAI & GitHub GH-600)

> **Disclaimer:** Independent educational practice material authored from public engineering specifications and open-protocol documentation — not affiliated with, sponsored by, or endorsed by NVIDIA, the Linux Foundation, Anthropic, OpenAI, Google, Microsoft, GitHub, LangChain, or OWASP. Practice scores do not guarantee passing any third-party certification exam.

## Questions

---

## Domain 1 — MCP Foundations, Architecture & Lifecycle (16–20% blueprint weight · 18 questions)

### 1. Sentinel Cyber Fusion MCP onboarding for SOC automation must follow the correct 4-step lifecycle. Which ordered sequence is correct? Log entry 5598 shows `Method not found -32601` without capability check. Scenario 1.1-6-1.

- **A.** Server sends `initialize` to client → client negotiates logging level first → exchange OAuth tokens inside `initialize` params → begin sampling without capability check
- **B.** Client sends `initialize` with `protocolVersion` & `capabilities` → server replies with negotiated version & capabilities → client sends `notifications/initialized` → normal `tools/list` & `resources/list` calls begin
- **C.** Client calls `tools/call` immediately → server returns capability list on tool error → client sends `initialize` afterward → skip `notifications/initialized`
- **D.** Client hardcodes `protocolVersion: "1.0"` forever → ignore server `protocolVersion` echo → send duplicate `initialize` on every ping → cache capabilities indefinitely

### 2. Three best practices for SOC automation under MCP 2025-11-25 apply to Sentinel Cyber Fusion. Which three should be chosen? Select three. Ticket 7370: plaintext `config.json` holds refresh token. [1.1 #2]

- **A.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **B.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **C.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **D.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **E.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)
- **F.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**

### 3. During SOC automation load testing at Sentinel Cyber Fusion, Streamable HTTP sessions terminate behind an ALB idle timeout. The team should ____. Ticket 4784: `roots/list` poll floods client every 10 ms. [1.1 #3]

- **A.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **B.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation
- **C.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **D.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults

### 4. Which two logging/observability actions are correct for SOC automation MCP at Sentinel Cyber Fusion? Select two. Log 3508: SSE stream without `eventId` loses progress on reconnect. [1.2 #4]

- **A.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **B.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **C.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **D.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **E.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively

### 5. The MCP Inspector highlights `____` as missing for SOC automation at Sentinel Cyber Fusion. Which completion is spec-correct? Ticket 7726: `roots/list` poll floods client every 10 ms. [1.2 #5]

- **A.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **B.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`
- **C.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)
- **D.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`

### 6. At Sentinel Cyber Fusion, SOC automation MCP gateway logs show `Last-Event-ID` replay gaps. The team should ____. Ticket 9836: `roots/list` poll floods client every 10 ms. [1.2 #6]

- **A.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **B.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`
- **C.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **D.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them

### 7. Sentinel Cyber Fusion MCP SOC automation SDK server omits `outputSchema`. The typed result approach is to ____. Log 3961: `initialize` skipped before `tools/list`. [1.3 #7]

- **A.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **B.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params
- **C.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **D.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics

### 8. Sentinel Cyber Fusion wants to bridge SOC automation MCP tools into an A2A task mesh. The correct layer definition is ____. Log entry 3376 shows `Method not found -32601` without capability check. [1.3 #8]

- **A.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **B.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **C.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **D.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure

### 9. Sentinel Cyber Fusion reports intermittent `Method not found -32601` errors when accessing SOC automation. To fix this, the team should ____. Trace 4700: 200-tool batch exceeds advertised `maxBatchSize`. [1.3 #9]

- **A.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **B.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **C.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **D.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan

### 10. Sentinel Cyber Fusion MCP onboarding for SOC automation must follow the correct 4-step lifecycle. Which ordered sequence is correct? Log 3017: `initialize` skipped before `tools/list`. Scenario 1.4-6-10.

- **A.** Client calls undefined tool name → server creates tool on-the-fly → skip inputSchema validation → stream 50-MB blob as single text content block
- **B.** Server declares tool with `name`, `description`, `inputSchema` (JSON Schema) → client `tools/list` discovers it → model calls `tools/call` with validated args → server validates, executes idempotently & returns `content` + `isError`
- **C.** Server returns tool result before validation → client retries with doubled args → disable tools/list_changed notifications → cache tool names forever
- **D.** Server exposes 200 tools without descriptions → client guesses arguments via prompt → server executes shell with raw LLM string → return HTML page inside isError=false

### 11. Sentinel Cyber Fusion MCP server for SOC automation requires two valid security hardening steps. Which two should you apply? Select two. Ticket 2771: `notifications/roots/list_changed` ignored after folder add. [1.4 #11]

- **A.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **B.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs
- **C.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **D.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **E.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization

### 12. Sentinel Cyber Fusion sees its SOC automation MCP tool return large binary blobs inline. The spec-compliant return is to ____. Log 6970: SSE stream without `eventId` loses progress on reconnect. [1.4 #12]

- **A.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **B.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **C.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **D.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads

### 13. At Sentinel Cyber Fusion, SOC automation MCP gateway logs show `Last-Event-ID` replay gaps. The team should ____. Case 9879: Host passes full env block to untrusted calendar server. [1.5 #13]

- **A.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request
- **B.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **C.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **D.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways

### 14. For SOC automation at Sentinel Cyber Fusion, the Host must reconcile `protocolVersion` negotiation after an upgrade. Which action is correct? Alert 3048: `Mcp-Session-Id` reused across tenants. [1.5 #14]

- **A.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **B.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **C.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **D.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`

### 15. Sentinel Cyber Fusion sees its SOC automation MCP tool return large binary blobs inline. The spec-compliant return is to ____. Trace 8044: `resource` audience binding missing per RFC 8707. [1.5 #15]

- **A.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs
- **B.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **C.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **D.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle

### 16. Complete the missing MCP field: In the Sentinel Cyber Fusion SOC automation server, `____` must be set to the MCP-required value to enable SOC automation correctly. Alert 6469: `isError:false` with HTML error page masks failure. [1.6 #16]

- **A.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`
- **B.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`
- **C.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **D.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**

### 17. The MCP Inspector highlights `____` as missing for SOC automation at Sentinel Cyber Fusion. Which completion is spec-correct? Log entry 8332 shows `Method not found -32601` without capability check. [1.6 #17]

- **A.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **B.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **C.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **D.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**

### 18. For SOC automation at Sentinel Cyber Fusion, token storage uses plaintext `config.json`. The secure alternative is to ____. Audit 7838: auto-approve bypasses human consent for destructive tool. [1.6 #18]

- **A.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **B.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **C.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **D.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`

---

## Domain 2 — Tools, Resources & Resource Templates (18–22% blueprint weight · 20 questions)

### 19. Which two logging/observability actions are correct for SOC automation MCP at Sentinel Cyber Fusion? Select two. Audit 4999: auto-approve bypasses human consent for destructive tool. [2.1 #19]

- **A.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **B.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **C.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **D.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **E.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**

### 20. In `Sentinel Cyber Fusion` `SOC automation` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Incident 6213: tool `inputSchema` validation skipped, injection observed. [2.1 #20]

- **A.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **B.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **C.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **D.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan

### 21. When Sentinel Cyber Fusion connects its VS Code host to an MCP server for SOC automation, the `roots/list` workflow should ____. Incident 1620: tool logic changed post-approval (rug-pull) undetected. [2.1 #21]

- **A.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **B.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **C.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation
- **D.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly

### 22. At Sentinel Cyber Fusion, the MCP client code handling SOC automation leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Log 3628: SSE stream without `eventId` loses progress on reconnect. [2.1 #22]

- **A.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean
- **B.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **C.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **D.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes

### 23. For SOC automation at Sentinel Cyber Fusion, which ordered flow correctly implements the MCP 2025-11-25 requirement? Case 9868: registry installs via `curl¦bash` without signature check. Scenario 2.2-6-23.

- **A.** Server lists resources without capability flag → client polls `resources/list` every 10 ms in loop → ignore `resources/list_changed` notifications → request resources via tools/call
- **B.** Server returns resources without uri fields → client stores resource content in tool history → server omits page cursors for 10k items → skip mimeType declaration
- **C.** Server advertises `resources` capability → client calls `resources/list` or `resources/templates/list` → client reads `resources/read` with `uri` → server returns `contents` with `mimeType`, handling pagination cursors
- **D.** Client guesses file URIs without list → server returns OS absolute paths as uri → embed 10-MB binary as base64 JSON string → skip uri validation

### 24. Proposed solution: To handle SOC automation, Sentinel Cyber Fusion plans to grant admin:write scope to every read-only docs search server by default. Does this satisfy the MCP specification? Trace 2115 reveals truncated cursor pagination at 50 entries. [2.2 #24]

- **A.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification
- **B.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **C.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **D.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible

### 25. During SOC automation rollout at Sentinel Cyber Fusion, canary hosts skip capability re-validation after reconnect. They should ____. Audit 6561: auto-approve bypasses human consent for destructive tool. [2.2 #25]

- **A.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **B.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **C.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean
- **D.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes

### 26. At Sentinel Cyber Fusion, the MCP client code handling SOC automation leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Trace 5224: batch of 200 tool calls timed out. [2.2 #26]

- **A.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **B.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively
- **C.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure
- **D.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage

### 27. Three best practices for SOC automation under MCP 2025-11-25 apply to Sentinel Cyber Fusion. Which three should be chosen? Select three. Incident 8189: OAuth PKCE verifier omitted for public client. [2.3 #27]

- **A.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **B.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **C.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **D.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **E.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **F.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`

### 28. At Sentinel Cyber Fusion, the MCP client code handling SOC automation leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Log entry 9077 shows `Method not found -32601` without capability check. [2.3 #28]

- **A.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **B.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation
- **C.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request
- **D.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent

### 29. Sentinel Cyber Fusion MCP SOC automation SDK server omits `outputSchema`. The typed result approach is to ____. Ticket 8689 reports `Last-Event-ID` replay mismatch after gateway restart. [2.3 #29]

- **A.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **B.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **C.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **D.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics

### 30. Proposed solution: Sentinel Cyber Fusion will store refresh tokens in world-readable config.json and log Authorization headers for SOC automation. Does this meet the MCP 2025-11-25 goal? Incident 7640: tool logic changed post-approval (rug-pull) undetected. [2.4 #30]

- **A.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **B.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **C.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **D.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways

### 31. Sentinel Cyber Fusion observes its SOC automation MCP server failing `tools/call` with `Invalid params -32602`. The fix is to ____. Review 8506 notes `resources/list_changed` never fired after ingest. [2.4 #31]

- **A.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **B.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **C.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **D.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways

### 32. Sentinel Cyber Fusion observes its SOC automation MCP server failing `tools/call` with `Invalid params -32602`. The fix is to ____. Ticket 5741: plaintext `config.json` holds refresh token. [2.4 #32]

- **A.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **B.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **C.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **D.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`

### 33. Proposed solution: Sentinel Cyber Fusion will run the MCP server as root with host-network and skip session ID tracking for SOC automation. Does this meet the MCP 2025-11-25 goal? Incident 9195: tool logic changed post-approval (rug-pull) undetected. [2.5 #33]

- **A.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **B.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **C.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **D.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes

### 34. The MCP Inspector highlights `____` as missing for SOC automation at Sentinel Cyber Fusion. Which completion is spec-correct? Case 9047: Host passes full env block to untrusted calendar server. [2.5 #34]

- **A.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **B.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation
- **C.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **D.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`

### 35. In Sentinel Cyber Fusion production, an MCP server for SOC automation must ____ to prevent tool poisoning attacks. Trace 4597: batch of 200 tool calls timed out. [2.5 #35]

- **A.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`
- **B.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **C.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **D.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent

### 36. To implement SOC automation correctly for Sentinel Cyber Fusion, which 4-step sequence satisfies the MCP spec? Ticket 3481: plaintext `config.json` holds refresh token. Scenario 2.6-6-36.

- **A.** Server declares client roots unilaterally → client trusts arbitrary server-provided paths → skip roots/list → ignore list_changed notifications
- **B.** Client declares `roots` capability with `file://` allowlist → server calls `roots/list` to learn boundaries → server restricts `resources/read` & tool file ops to those roots → handle `notifications/roots/list_changed`
- **C.** Server hardcodes `roots/list` response → client polls filesystem without notification channel → skip name/uri validation → cache roots forever
- **D.** Client exposes entire `C:\` without consent → server walks parent directories above declared roots → disable path canonicalization → follow symlinks blindly

### 37. Which two logging/observability actions are correct for SOC automation MCP at Sentinel Cyber Fusion? Select two. Alert 6510: `progressToken` mismatch across concurrent tool calls. [2.6 #37]

- **A.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **B.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **C.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **D.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **E.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`

### 38. Sentinel Cyber Fusion wants SOC automation MCP completions for enum arguments. The valid method is ____. Log 3397: `initialize` skipped before `tools/list`. [2.6 #38]

- **A.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **B.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **C.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **D.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible

---

## Domain 3 — Prompts, Sampling, Roots & Elicitation (14–18% blueprint weight · 16 questions)

### 39. At Sentinel Cyber Fusion, the MCP client code handling SOC automation leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Ticket 4134: plaintext `config.json` holds refresh token. Scenario 3.1-6-39.

- **A.** Server mixes sampling messages into tool descriptions → client forwards without isolation → skip cost tracking → cache sampling results as facts
- **B.** Server advertises sampling need → checks client `sampling` capability → sends `sampling/createMessage` with `messages`, `maxTokens`, `modelPreferences` → client applies human-in-loop gating & returns generation
- **C.** Server sends sampling without capability check → include raw customer PII in messages → skip maxTokens limits → client auto-executes without user consent
- **D.** Client exposes sampling by default without opt-in → server loops sampling/createMessage recursively → ignore modelPreferences hints → return raw chain-of-thought as tool output

### 40. For SOC automation at Sentinel Cyber Fusion, two MCP primitives are required to enable the scenario. Which two are needed? Select two. Review 5936: `outputSchema` mismatched to `structuredContent` shape. [3.1 #40]

- **A.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **B.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **C.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **D.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **E.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`

### 41. In `Sentinel Cyber Fusion` `SOC automation` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Alert 6942: `progressToken` mismatch across concurrent tool calls. [3.1 #41]

- **A.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **B.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **C.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **D.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes

### 42. Sentinel Cyber Fusion handles SOC automation via MCP sampling delegation. To enforce least privilege, the server should ____. Audit 1747: auto-approve bypasses human consent for destructive tool. [3.2 #42]

- **A.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **B.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **C.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **D.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**

### 43. Proposed solution: allow servers to self-declare client filesystem roots without user consent is suggested for SOC automation at Sentinel Cyber Fusion. Does this meet the goal? Case 4320: registry installs via `curl¦bash` without signature check. [3.2 #43]

- **A.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **B.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **C.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **D.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking

### 44. Sentinel Cyber Fusion observes its SOC automation MCP server failing `tools/call` with `Invalid params -32602`. The fix is to ____. Log 9654: SSE stream without `eventId` loses progress on reconnect. [3.2 #44]

- **A.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **B.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure
- **C.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **D.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect

### 45. Which two behaviors correctly describe MCP SOC automation handling at Sentinel Cyber Fusion? Select two. Incident 6358: OAuth PKCE verifier omitted for public client. [3.3 #45]

- **A.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **B.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **C.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **D.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **E.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`

### 46. You are reviewing an MCP implementation for Sentinel Cyber Fusion that handles SOC automation. Which statement about ____ is accurate under MCP 2025-11-25? Audit 5240 flags `alg:none` token acceptance in staging. [3.3 #46]

- **A.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **B.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **C.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **D.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking

### 47. Sentinel Cyber Fusion handles SOC automation via MCP sampling delegation. To enforce least privilege, the server should ____. Ticket 7877 reports `Last-Event-ID` replay mismatch after gateway restart. [3.3 #47]

- **A.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **B.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **C.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **D.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure

### 48. The Sentinel Cyber Fusion team debugging SOC automation sees truncated `resources/list` results at 50 items. They should ____. Alert 7217: `isError:false` with HTML error page masks failure. [3.4 #48]

- **A.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **B.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`
- **C.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **D.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`

### 49. Proposed solution: To handle SOC automation, Sentinel Cyber Fusion plans to grant admin:write scope to every read-only docs search server by default. Does this satisfy the MCP specification? Log 2993: SSE stream without `eventId` loses progress on reconnect. [3.4 #49]

- **A.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`
- **B.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **C.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **D.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**

### 50. Proposed solution: skip issuer validation and accept bearer tokens from any alg:none issuer is suggested for SOC automation at Sentinel Cyber Fusion. Does this meet the goal? Review 8551 notes `resources/list_changed` never fired after ingest. [3.4 #50]

- **A.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **B.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **C.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **D.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`

### 51. For SOC automation at Sentinel Cyber Fusion, three controls are required for MCP compliance. Which three are correct? Select three. Log 6482: `initialize` skipped before `tools/list`. [3.5 #51]

- **A.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **B.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **C.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **D.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **E.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **F.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request

### 52. The MCP Inspector highlights `____` as missing for SOC automation at Sentinel Cyber Fusion. Which completion is spec-correct? Ticket 7581 reports `Last-Event-ID` replay mismatch after gateway restart. [3.5 #52]

- **A.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **B.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **C.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **D.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads

### 53. Sentinel Cyber Fusion MCP SOC automation SDK server omits `outputSchema`. The typed result approach is to ____. Case 4853: `structuredContent` missing despite `outputSchema` declared. [3.6 #53]

- **A.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **B.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **C.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **D.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs

### 54. At Sentinel Cyber Fusion, SOC automation MCP server batch returns timeout for 200 calls. The team should ____. Ticket 8011: `notifications/roots/list_changed` ignored after folder add. [3.6 #54]

- **A.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**
- **B.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **C.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params
- **D.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation

---

## Domain 4 — Transports, Sessions & Protocol Evolution (14–18% blueprint weight · 16 questions)

### 55. What is the correct 4-step order for SOC automation workflow at Sentinel Cyber Fusion under MCP 2025-11-25? Case 5496: Host passes full env block to untrusted calendar server. Scenario 4.1-6-55.

- **A.** Client opens separate GET /sse and POST /message SSE endpoints → send JSON without Accept header → ignore Mcp-Session-Id → close stream after each chunk without Last-Event-ID
- **B.** Client POSTs JSON-RPC to single `mcp` endpoint with `Content-Type: application/json` & `Accept: text/event-stream, application/json` → server may respond with single JSON or SSE stream → client honors `Mcp-Session-Id` & `Last-Event-ID` for resumability
- **C.** Server returns 200 OK with HTML error page → client retries without backoff → disable idempotency on non-idempotent tool calls → omit Content-Type validation
- **D.** Client sends batched 100 requests without server batch ack → server streams without event IDs → skip session expiry handling → leak session IDs across tenants

### 56. When Sentinel Cyber Fusion connects its VS Code host to an MCP server for SOC automation, the `roots/list` workflow should ____. Incident 2995: OAuth PKCE verifier omitted for public client. [4.1 #56]

- **A.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)
- **B.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **C.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **D.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan

### 57. The MCP Inspector highlights `____` as missing for SOC automation at Sentinel Cyber Fusion. Which completion is spec-correct? Log 4680: SSE stream without `eventId` loses progress on reconnect. [4.1 #57]

- **A.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **B.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds
- **C.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **D.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)

### 58. Sentinel Cyber Fusion sees its SOC automation MCP tool return large binary blobs inline. The spec-compliant return is to ____. Trace 3437: 200-tool batch exceeds advertised `maxBatchSize`. [4.2 #58]

- **A.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **B.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **C.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **D.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect

### 59. During SOC automation review at Sentinel Cyber Fusion, the MCP server emits debug logs at `error` level. The proper level is ____. Review 3909 notes `resources/list_changed` never fired after ingest. [4.2 #59]

- **A.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **B.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **C.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **D.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke

### 60. Sentinel Cyber Fusion reports intermittent `Method not found -32601` errors when accessing SOC automation. To fix this, the team should ____. Review 3146 notes `resources/list_changed` never fired after ingest. [4.2 #60]

- **A.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **B.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **C.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **D.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`

### 61. Sentinel Cyber Fusion engineers designing an MCP system for SOC automation must evaluate two correct controls. Which two statements are correct? Select two. Log 5557: `initialize` skipped before `tools/list`. [4.3 #61]

- **A.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **B.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **C.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively
- **D.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **E.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`

### 62. The Sentinel Cyber Fusion MCP configuration for SOC automation shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Audit 5829 flags `alg:none` token acceptance in staging. [4.3 #62]

- **A.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **B.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **C.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **D.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation

### 63. The Sentinel Cyber Fusion MCP configuration for SOC automation shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Log entry 7822 shows `Method not found -32601` without capability check. [4.3 #63]

- **A.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **B.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **C.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean
- **D.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**

### 64. An external auditor flags that Sentinel Cyber Fusion MCP deployment for SOC automation stores bearer tokens insecurely. The correction is to ____. Review 4375 notes `resources/list_changed` never fired after ingest. [4.4 #64]

- **A.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **B.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **C.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **D.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`

### 65. The Sentinel Cyber Fusion SOC automation Host caches `roots/list` forever and misses workspace changes. The fix is to ____. Alert 3158: `isError:false` with HTML error page masks failure. [4.4 #65]

- **A.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **B.** Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation
- **C.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **D.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)

### 66. A Sentinel MCP client for SOC automation must ____ to satisfy the protocol. What is the correct implementation approach? Review 9179: `outputSchema` mismatched to `structuredContent` shape. [4.4 #66]

- **A.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **B.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs
- **C.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **D.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks

### 67. Sentinel Cyber Fusion wants SOC automation MCP completions for enum arguments. The valid method is ____. Ticket 4528 reports `Last-Event-ID` replay mismatch after gateway restart. [4.5 #67]

- **A.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **B.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **C.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **D.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs

### 68. Proposed solution: embed static client_secret inside the shipped desktop binary for all tenants is suggested for SOC automation at Sentinel Cyber Fusion. Does this meet the goal? Log 6004: `initialize` skipped before `tools/list`. [4.5 #68]

- **A.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **B.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params
- **C.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **D.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs

### 69. Sentinel Cyber Fusion engineers designing an MCP system for SOC automation must evaluate two correct controls. Which two statements are correct? Select two. Trace 1361: `resource` audience binding missing per RFC 8707. [4.6 #69]

- **A.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs
- **B.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **C.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **D.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **E.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect

### 70. Sentinel Cyber Fusion observes `prompt injection` payloads via SOC automation MCP resource content. The mitigation is to ____. Case 3329: Host passes full env block to untrusted calendar server. [4.6 #70]

- **A.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **B.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **C.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **D.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs

---

## Domain 5 — Authorization, Security, Trust & Registry (13–17% blueprint weight · 15 questions)

### 71. You are reviewing an MCP implementation for Sentinel Cyber Fusion that handles SOC automation. Which statement about ____ is accurate under MCP 2025-11-25? Alert 9050: `isError:false` with HTML error page masks failure. [5.1 #71]

- **A.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **B.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **C.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **D.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414

### 72. In Sentinel Cyber Fusion production, an MCP server for SOC automation must ____ to prevent tool poisoning attacks. Trace 9100: `resource` audience binding missing per RFC 8707. [5.1 #72]

- **A.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **B.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **C.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **D.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`

### 73. Proposed solution: hardcode protocolVersion to 2024-11-05 forever and ignore server capability updates is suggested for SOC automation at Sentinel Cyber Fusion. Does this meet the goal? Case 6863: `structuredContent` missing despite `outputSchema` declared. [5.1 #73]

- **A.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **B.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **C.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **D.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`

### 74. Which two logging/observability actions are correct for SOC automation MCP at Sentinel Cyber Fusion? Select two. Audit 7454: auto-approve bypasses human consent for destructive tool. [5.2 #74] through Kafka topic rebalancing (variant alpha 721).

- **A.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **B.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **C.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **D.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **E.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly

### 75. For Sentinel Cyber Fusion SOC automation server to advertise new capabilities after a deploy, the correct notification is ____. Audit 2836: `includeContext=allServers` exfiltrates cross-server data. [5.2 #75]

- **A.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **B.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **C.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params
- **D.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes

### 76. At Sentinel Cyber Fusion, the MCP client code handling SOC automation leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Review 4878: `completion/complete` implemented as heavy tool call. [5.2 #76]

- **A.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **B.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **C.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **D.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions

### 77. Sentinel Cyber Fusion MCP onboarding for SOC automation must follow the correct 4-step lifecycle. Which ordered sequence is correct? Trace 3177: 200-tool batch exceeds advertised `maxBatchSize`. Scenario 5.3-6-77.

- **A.** Server exposes `/.well-known/oauth-authorization-server` with PRM & CIMD → client fetches RS metadata with `resource` indicator (RFC 8707) → PKCE + state + RFC 9207 iss validation → audience-bound token issued per resource server
- **B.** Client trusts token from any issuer → skip RFC 9207 iss equality check → ignore RFC 7591 dynamic registration → reuse single token across all resource servers
- **C.** Client sends static API key in Authorization header → server skips issuer discovery → accept tokens with alg:none → grant org-admin scope by default
- **D.** Server embeds client_secret in JS bundle → disable PKCE as optional → return tokens over plain HTTP → cache discovery doc forever without TLS

### 78. Which two behaviors correctly describe MCP SOC automation handling at Sentinel Cyber Fusion? Select two. Ticket 5984: `roots/list` poll floods client every 10 ms. [5.3 #78]

- **A.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **B.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **C.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **D.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **E.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414

### 79. Proposed solution: To handle SOC automation, Sentinel Cyber Fusion plans to batch 200 tool calls beyond advertised maxBatchSize in a single request. Does this satisfy the MCP specification? Log entry 7759 shows `Method not found -32601` without capability check. [5.3 #79]

- **A.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **B.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **C.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **D.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token

### 80. Sentinel Cyber Fusion wants its MCP server to support both local and remote clients for SOC automation. The architecture should ____. Ticket 8178: `roots/list` poll floods client every 10 ms. [5.4 #80]

- **A.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **B.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs
- **C.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **D.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)

### 81. Sentinel Cyber Fusion wants to bridge SOC automation MCP tools into an A2A task mesh. The correct layer definition is ____. Incident 1988: tool `inputSchema` validation skipped, injection observed. [5.4 #81]

- **A.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **B.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)
- **C.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean
- **D.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging

### 82. For SOC automation at Sentinel Cyber Fusion, the Host must reconcile `protocolVersion` negotiation after an upgrade. Which action is correct? Audit 2805: auto-approve bypasses human consent for destructive tool. [5.4 #82]

- **A.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs
- **B.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`
- **C.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **D.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately

### 83. At Sentinel Cyber Fusion, engineers building an MCP server for SOC automation need to ____. Which configuration correctly implements the MCP specification? Alert 9874: `Mcp-Session-Id` reused across tenants. [5.5 #83]

- **A.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **B.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure
- **C.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)
- **D.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params

### 84. During SOC automation load testing at Sentinel Cyber Fusion, Streamable HTTP sessions terminate behind an ALB idle timeout. The team should ____. Log 1241: SSE stream without `eventId` loses progress on reconnect. [5.5 #84]

- **A.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **B.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **C.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **D.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)

### 85. A SOC automation MCP extension at Sentinel Cyber Fusion leaks `Mcp-Session-Id` across tenants. The team must ____. Case 9434: registry installs via `curl¦bash` without signature check. [5.5 #85]

- **A.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **B.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)
- **C.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **D.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals

---

## Domain 6 — SDKs, Deployment, Observability & Ecosystem (13–17% blueprint weight · 15 questions)

### 86. Sentinel Cyber Fusion engineers designing an MCP system for SOC automation must evaluate two correct controls. Which two statements are correct? Select two. Trace 3377: 200-tool batch exceeds advertised `maxBatchSize`. [6.1 #86]

- **A.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **B.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **C.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks
- **D.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **E.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`

### 87. Sentinel Cyber Fusion MCP server for SOC automation uses static API keys in `Authorization`. The OAuth 2.1 migration is to ____. Case 1105: Host passes full env block to untrusted calendar server. [6.1 #87]

- **A.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets
- **B.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **C.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **D.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files

### 88. Sentinel Cyber Fusion reports intermittent `Method not found -32601` errors when accessing SOC automation. To fix this, the team should ____. Case 5525: registry installs via `curl¦bash` without signature check. [6.1 #88]

- **A.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params
- **B.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **C.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **D.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan

### 89. Proposed solution: Sentinel Cyber Fusion will allow servers to self-declare client filesystem roots without user consent for SOC automation. Does this meet the MCP 2025-11-25 goal? Ticket 5679: plaintext `config.json` holds refresh token. [6.2 #89]

- **A.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **B.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks
- **C.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **D.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context

### 90. For SOC automation, Sentinel Cyber Fusion must handle `notifications/progress` vs polling. The correct pattern is to ____. Review 3327: `completion/complete` implemented as heavy tool call. [6.2 #90]

- **A.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **B.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **C.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **D.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics

### 91. At Sentinel Cyber Fusion, SOC automation MCP gateway logs show `Last-Event-ID` replay gaps. The team should ____. Case 3119: registry installs via `curl¦bash` without signature check. [6.2 #91]

- **A.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **B.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks
- **C.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request
- **D.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively

### 92. For SOC automation at Sentinel Cyber Fusion, two MCP primitives are required to enable the scenario. Which two are needed? Select two. Case 6202: `structuredContent` missing despite `outputSchema` declared. [6.3 #92]

- **A.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **B.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **C.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification
- **D.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **E.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI

### 93. The Sentinel Cyber Fusion team debugging SOC automation sees truncated `resources/list` results at 50 items. They should ____. Audit 2983: auto-approve bypasses human consent for destructive tool. [6.3 #93]

- **A.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **B.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **C.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **D.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping

### 94. Sentinel Cyber Fusion plans to publish its SOC automation MCP server to the registry. The publishing step should ____. Trace 9134: 200-tool batch exceeds advertised `maxBatchSize`. [6.3 #94]

- **A.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **B.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **C.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **D.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**

### 95. The Sentinel Cyber Fusion team documents the SOC automation MCP flow. Which sequence of actions is spec-compliant? Log entry 9700 shows `Method not found -32601` without capability check. Scenario 6.4-6-95.

- **A.** Pin server versions & verify registry signatures → isolate tool descriptions from executable logic → prompt user before first tool approval & high-risk actions → log tool provenance & monitor for description drift
- **B.** Auto-approve all tools without review → trust tool description text as system prompt → allow server to change tool logic post-approval → skip signature verification
- **C.** Install random GitHub MCP servers via curl|bash → grant full filesystem + network + env scopes → disable log redaction → store tokens in plaintext
- **D.** Exfiltrate tool arguments to third-party analytics silently → skip rate limiting on tool calls → omit provenance tags → hide tool calls from audit UI

### 96. Sentinel Cyber Fusion must fix its SOC automation MCP integration. Which two changes bring it into spec compliance? Select two. Alert 4706: `isError:false` with HTML error page masks failure. [6.4 #96]

- **A.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **B.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **C.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **D.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)
- **E.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)

### 97. Sentinel Cyber Fusion handles SOC automation via MCP sampling delegation. To enforce least privilege, the server should ____. Audit 5719 flags `alg:none` token acceptance in staging. [6.4 #97]

- **A.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **B.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **C.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets
- **D.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking

### 98. Complete the missing MCP field: In the Sentinel Cyber Fusion SOC automation server, `____` must be set to the MCP-required value to enable SOC automation correctly. Log 2043: `initialize` skipped before `tools/list`. [6.5 #98]

- **A.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params
- **B.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **C.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks
- **D.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`

### 99. At Sentinel Cyber Fusion, engineers building an MCP server for SOC automation need to ____. Which configuration correctly implements the MCP specification? Log 5168: `prompt/get` uses client-side interpolation without validation. [6.5 #99]

- **A.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **B.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **C.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **D.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)

### 100. Sentinel Cyber Fusion wants SOC automation MCP completions for enum arguments. The valid method is ____. Incident 4401: OAuth PKCE verifier omitted for public client. [6.5 #100]

- **A.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **B.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds
- **C.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **D.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage

---

## Answer Key and Explanations

### Question 1 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). This choice correctly implements Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Reference 1.1 S6Q001. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Incorrect. reversing the initialize direction and mixing OAuth into initialize params conflates lifecycle with authorization.
- **B:** Correct. follows MCP lifecycle spec: version/capability negotiation via initialize exchange completed by initialized notification before any feature calls.
- **C:** Incorrect. invoking tools before initialize negotiation bypasses version checks and omits the required initialized signal.
- **D:** Incorrect. hardcoding protocol versions and duplicate initialize pings breaks forward compatibility and lifecycle idempotency.

### Question 2 — `A, C, F` (MCP Foundations, Architecture & Lifecycle)

Correct answers: A, C, and F (are correct). This follows the MCP specification for Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 1.1 validation S6Q002. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Correct. allows safe iteration on draft specs like Tasks and elicitation without polluting the stable capability surface.
- **B:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.
- **C:** Correct. enforces 1:1 Client-Server lifecycle so pings, cancellations and session IDs map unambiguously without multiplexing bugs.
- **D:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.
- **E:** Incorrect. installing random `curl | bash` MCP servers without registry signature verification imports unvetted RCE into the IDE.
- **F:** Correct. clarifies layer boundaries: MCP standardizes context attachment; function calling is inline model schema; A2A negotiates task handoffs.

### Question 3 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). This follows the MCP specification for Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 1.1 validation S6Q003. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **B:** Correct. correctly separates trust boundaries: Hosts own UI/policy, Clients speak MCP, Servers expose capabilities behind capability negotiation.
- **C:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **D:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.

### Question 4 — `B, D` (MCP Foundations, Architecture & Lifecycle)

Correct answers: B and D (are correct). Selecting this honors Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 1.2 validation S6Q004. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **B:** Correct. lets each party call only negotiated features, avoiding methodNotFound and silent fallback hallucinations.
- **C:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.
- **D:** Correct. provides spec-guaranteed failure detection where OS TCP keepalives are invisible to application-level SSE/stdio proxies.
- **E:** Incorrect. skipping Inspector and relying only on unit mocks misses real transport framing and pagination/cancellation bugs.

### Question 5 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). This follows the MCP specification for Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 1.2 validation S6Q005. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.
- **B:** Correct. guarantees version and capability compatibility before feature calls, satisfying the MCP lifecycle invariant.
- **C:** Incorrect. installing random `curl | bash` MCP servers without registry signature verification imports unvetted RCE into the IDE.
- **D:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.

### Question 6 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). Per MCP 2025-11-25, Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake ensures spec-compliant lifecycle and isolation for SOC automation. Skill 1.2 validation S6Q006. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **B:** Correct. guarantees version and capability compatibility before feature calls, satisfying the MCP lifecycle invariant.
- **C:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **D:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.

### Question 7 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). MCP 2025-11-25 requires Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy; the alternative breaks capability negotiation or security for SOC automation. Skill 1.3 validation S6Q007. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Correct. standardizes remediation: 32601 means check capabilities, 32602 means fix schema, unlike bespoke string matching.
- **B:** Incorrect. implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.
- **C:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.
- **D:** Incorrect. deploying greenfield on the deprecated dual-endpoint SSE transport incurs future migration cost and lacks session IDs.

### Question 8 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). Per MCP 2025-11-25, Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy ensures spec-compliant lifecycle and isolation for SOC automation. Skill 1.3 validation S6Q008. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Correct. adheres to the wire contract that underpins batching, cancellation, and error classification across both transports.
- **B:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.
- **C:** Incorrect. requiring clients to poll list on a timer to detect new resources defeats MCP push efficiency.
- **D:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.

### Question 9 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). This follows the MCP specification for Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 1.3 validation S6Q009. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **B:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **C:** Correct. standardizes remediation: 32601 means check capabilities, 32602 means fix schema, unlike bespoke string matching.
- **D:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.

### Question 10 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). This follows the MCP specification for Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging), correcting the insecure/incompatible anti-pattern for SOC automation. Reference 1.4 S6Q010. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Incorrect. ad-hoc tool creation without validation and massive single-block responses break type safety and token budgets.
- **B:** Correct. matches MCP Tools spec: declarative schema, client discovery, validated execution, and structured content/error signaling.
- **C:** Incorrect. responding before validation and ignoring list_changed events leaves clients with stale, unvalidated tool catalogs.
- **D:** Incorrect. missing inputSchema and raw shell interpolation from unvalidated LLM strings creates prompt-injection and RCE risk.

### Question 11 — `A, E` (MCP Foundations, Architecture & Lifecycle)

Correct answers: A and E (are correct). Selecting this honors Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 1.4 validation S6Q011. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Correct. enables forwards-compatible evolution without breaking older Hosts or Servers on version skew.
- **B:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.
- **C:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **D:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **E:** Correct. allows safe iteration on draft specs like Tasks and elicitation without polluting the stable capability surface.

### Question 12 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). MCP 2025-11-25 requires Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging); the alternative breaks capability negotiation or security for SOC automation. Skill 1.4 validation S6Q012. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **B:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.
- **C:** Correct. enables forwards-compatible evolution without breaking older Hosts or Servers on version skew.
- **D:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.

### Question 13 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). Selecting this honors Manage keepalive pings, progress notifications, cancellation, and shutdown semantics and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 1.5 validation S6Q013. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. generating random progressTokens server-side with no binding to request id mixes streams across concurrent tasks.
- **B:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.
- **C:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.
- **D:** Correct. provides spec-guaranteed failure detection where OS TCP keepalives are invisible to application-level SSE/stdio proxies.

### Question 14 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). MCP 2025-11-25 requires Manage keepalive pings, progress notifications, cancellation, and shutdown semantics; the alternative breaks capability negotiation or security for SOC automation. Skill 1.5 validation S6Q014. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **B:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.
- **C:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.
- **D:** Incorrect. calling tools before the initialized handshake completes races capability discovery and throws methodNotFound errors.

### Question 15 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). MCP 2025-11-25 requires Manage keepalive pings, progress notifications, cancellation, and shutdown semantics; the alternative breaks capability negotiation or security for SOC automation. Skill 1.5 validation S6Q015. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. survives AWS ALB 60s idle timeout and Kubernetes GFE that silently drops idle SSE streams.
- **B:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **C:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.
- **D:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.

### Question 16 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). Per MCP 2025-11-25, Differentiate MCP from function calling, A2A, and experimental capability progression ensures spec-compliant lifecycle and isolation for SOC automation. Skill 1.6 validation S6Q016. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Incorrect. calling tools before the initialized handshake completes races capability discovery and throws methodNotFound errors.
- **B:** Incorrect. parsing free-form chat replies as structured data instead of typed elicitation invites format errors and injection.
- **C:** Correct. allows safe iteration on draft specs like Tasks and elicitation without polluting the stable capability surface.
- **D:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.

### Question 17 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). Selecting this honors Differentiate MCP from function calling, A2A, and experimental capability progression and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 1.6 validation S6Q017. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.
- **B:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **C:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **D:** Correct. clarifies layer boundaries: MCP standardizes context attachment; function calling is inline model schema; A2A negotiates task handoffs.

### Question 18 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). MCP 2025-11-25 requires Differentiate MCP from function calling, A2A, and experimental capability progression; the alternative breaks capability negotiation or security for SOC automation. Skill 1.6 validation S6Q018. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Correct. clarifies layer boundaries: MCP standardizes context attachment; function calling is inline model schema; A2A negotiates task handoffs.
- **B:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.
- **C:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **D:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.

### Question 19 — `C, D` (Tools, Resources & Resource Templates)

Correct answers: C and D (are correct). MCP 2025-11-25 requires Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints; the alternative breaks capability negotiation or security for SOC automation. Skill 2.1 validation S6Q019. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.
- **B:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **C:** Correct. signals cost/safety posture without hard-coding policy; models prefer readOnly before destructive in multi-step plans.
- **D:** Correct. gives models complete, machine-validated contracts for tool selection and argument generation.
- **E:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.

### Question 20 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). This follows the MCP specification for Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 2.1 validation S6Q020. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. gives models complete, machine-validated contracts for tool selection and argument generation.
- **B:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **C:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.
- **D:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.

### Question 21 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). Per MCP 2025-11-25, Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints ensures spec-compliant lifecycle and isolation for SOC automation. Skill 2.1 validation S6Q021. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. uses typed server helpers that auto-wire tools/list/call handlers and JSON Schema validation from Zod objects.
- **B:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **C:** Incorrect. collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.
- **D:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.

### Question 22 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). This follows the MCP specification for Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 2.1 validation S6Q022. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. dumping base64 blobs as plain text without typed content blocks loses mimeType and forces heuristic parsing.
- **B:** Correct. preserves user/model agency and auditability; every mutation traces to an explicit model decision with tool audit event.
- **C:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **D:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.

### Question 23 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). MCP 2025-11-25 requires Control model-controlled tool execution, list discovery, validation, and structured content output; the alternative breaks capability negotiation or security for SOC automation. Reference 2.2 S6Q023. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. tight polling without subscription to list_changed notifications defeats MCP push efficiency and protocol layering.
- **B:** Incorrect. omitting uri and mimeType fields and ignoring pagination cursors makes resources unaddressable and unfilterable.
- **C:** Correct. follows Resources spec: capability advertisement, list/template discovery, uri-addressed reads with mime-typed contents and pagination.
- **D:** Incorrect. guessing URIs and exposing raw OS paths without scheme checks violates resource discovery and isolation.

### Question 24 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). This follows the MCP specification for Control model-controlled tool execution, list discovery, validation, and structured content output, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 2.2 validation S6Q024. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. distributing servers as raw GitHub tarballs without server.json or publisher proof hides supply-chain compromise.
- **B:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.
- **C:** Correct. bridges LLM reasoning with downstream code that consumes validated JSON, not regex scraped prose.
- **D:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.

### Question 25 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Per MCP 2025-11-25, Control model-controlled tool execution, list discovery, validation, and structured content output ensures spec-compliant lifecycle and isolation for SOC automation. Skill 2.2 validation S6Q025. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.
- **B:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.
- **C:** Correct. lets clients render multimodal results safely while distinguishing success from app-level errors without parsing text.
- **D:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.

### Question 26 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Per MCP 2025-11-25, Control model-controlled tool execution, list discovery, validation, and structured content output ensures spec-compliant lifecycle and isolation for SOC automation. Skill 2.2 validation S6Q026. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.
- **B:** Incorrect. skipping Inspector and relying only on unit mocks misses real transport framing and pagination/cancellation bugs.
- **C:** Correct. defends against LLM hallucinated args and preserves typed error handling via isError flag versus exception propagation.
- **D:** Incorrect. assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.

### Question 27 — `A, C, D` (Tools, Resources & Resource Templates)

Correct answers: A, C, and D (are correct). Selecting this honors Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 2.3 validation S6Q027. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Correct. keeps prompt pickers fresh without re-listing on every keystroke, matching resource/tool change notification pattern.
- **B:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **C:** Correct. handles 10k-file workspaces without truncation or timeout, matching MCP pagination contract for both lists.
- **D:** Correct. pushes freshness efficiently after external ingestion jobs create new datasets, without constant re-list overhead.
- **E:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.
- **F:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.

### Question 28 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). This follows the MCP specification for Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 2.3 validation S6Q028. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.
- **B:** Incorrect. collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.
- **C:** Incorrect. generating random progressTokens server-side with no binding to request id mixes streams across concurrent tasks.
- **D:** Correct. handles 10k-file workspaces without truncation or timeout, matching MCP pagination contract for both lists.

### Question 29 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). This choice correctly implements Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Skill 2.3 validation S6Q029. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.
- **B:** Correct. pushes freshness efficiently after external ingestion jobs create new datasets, without constant re-list overhead.
- **C:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **D:** Incorrect. deploying greenfield on the deprecated dual-endpoint SSE transport incurs future migration cost and lacks session IDs.

### Question 30 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). This choice correctly implements Address direct resources vs templated resources with URI schemes, names, and mimeTypes for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Skill 2.4 validation S6Q030. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. signals cost/safety posture without hard-coding policy; models prefer readOnly before destructive in multi-step plans.
- **B:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.
- **C:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.
- **D:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.

### Question 31 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Per MCP 2025-11-25, Address direct resources vs templated resources with URI schemes, names, and mimeTypes ensures spec-compliant lifecycle and isolation for SOC automation. Skill 2.4 validation S6Q031. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **B:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.
- **C:** Correct. signals cost/safety posture without hard-coding policy; models prefer readOnly before destructive in multi-step plans.
- **D:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.

### Question 32 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Per MCP 2025-11-25, Address direct resources vs templated resources with URI schemes, names, and mimeTypes ensures spec-compliant lifecycle and isolation for SOC automation. Skill 2.4 validation S6Q032. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.
- **B:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **C:** Correct. delivers typed content blocks that render correctly in Host UIs with binary vs text handling pre-decided by mimeType.
- **D:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.

### Question 33 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). Selecting this honors Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 2.5 validation S6Q033. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.
- **B:** Correct. pushes freshness efficiently after external ingestion jobs create new datasets, without constant re-list overhead.
- **C:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.
- **D:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.

### Question 34 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). MCP 2025-11-25 requires Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows; the alternative breaks capability negotiation or security for SOC automation. Skill 2.5 validation S6Q034. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Correct. keeps IDE diagnostics in sync with file edits without polling, per spec subscription lifecycle.
- **B:** Incorrect. collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.
- **C:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **D:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.

### Question 35 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). Per MCP 2025-11-25, Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows ensures spec-compliant lifecycle and isolation for SOC automation. Skill 2.5 validation S6Q035. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.
- **B:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **C:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **D:** Correct. handles 10k-file workspaces without truncation or timeout, matching MCP pagination contract for both lists.

### Question 36 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). Per MCP 2025-11-25, Declare prompts and completions for argument typeahead and parameterized prompt expansion ensures spec-compliant lifecycle and isolation for SOC automation. Reference 2.6 S6Q036. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. letting servers dictate client filesystem boundaries inverts MCP trust and breaks host isolation.
- **B:** Correct. implements Roots spec: client-owned boundary declaration, server-enforced confinement, and dynamic list_changed handling.
- **C:** Incorrect. hardcoding roots and ignoring list_changed notifications leaves stale boundaries after user permission changes.
- **D:** Incorrect. exposing full drive without consent and walking above root boundaries with symlink following enables directory traversal.

### Question 37 — `D, E` (Tools, Resources & Resource Templates)

Correct answers: D and E (are correct). This choice correctly implements Declare prompts and completions for argument typeahead and parameterized prompt expansion for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Skill 2.6 validation S6Q037. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **B:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.
- **C:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.
- **D:** Correct. compiles parameterized prompt templates server-side with validated args, keeping prompt injection surface server-controlled.
- **E:** Correct. turns curated prompt packs into discoverable UX shortcuts argument-by-argument with typed validation.

### Question 38 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). MCP 2025-11-25 requires Declare prompts and completions for argument typeahead and parameterized prompt expansion; the alternative breaks capability negotiation or security for SOC automation. Skill 2.6 validation S6Q038. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **B:** Correct. keeps prompt pickers fresh without re-listing on every keystroke, matching resource/tool change notification pattern.
- **C:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.
- **D:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.

### Question 39 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). This choice correctly implements Expose and expand prompts via prompts/list, prompts/get, and argument validation for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Reference 3.1 S6Q039. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. confusing sampling payloads with tool metadata conflates delegation layers and breaks cost attribution.
- **B:** Correct. follows Sampling spec: capability-checked server-initiated LLM delegation with explicit modelPreferences and human approval gating.
- **C:** Incorrect. unbounded PII-laden sampling without capability or consent bypasses privacy and authorization boundaries.
- **D:** Incorrect. default-exposed sampling and uncapped recursive loops risk token runaway and expose internal reasoning inappropriately.

### Question 40 — `B, C` (Prompts, Sampling, Roots & Elicitation)

Correct answers: B and C (are correct). Selecting this honors Expose and expand prompts via prompts/list, prompts/get, and argument validation and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 3.1 validation S6Q040. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. enabling experimental tasks by default without capability checks forces unready clients into breaking draft methods.
- **B:** Correct. compiles parameterized prompt templates server-side with validated args, keeping prompt injection surface server-controlled.
- **C:** Correct. keeps prompt pickers fresh without re-listing on every keystroke, matching resource/tool change notification pattern.
- **D:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **E:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.

### Question 41 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). Per MCP 2025-11-25, Expose and expand prompts via prompts/list, prompts/get, and argument validation ensures spec-compliant lifecycle and isolation for SOC automation. Skill 3.1 validation S6Q041. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.
- **B:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.
- **C:** Correct. compiles parameterized prompt templates server-side with validated args, keeping prompt injection surface server-controlled.
- **D:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.

### Question 42 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). Selecting this honors Enforce client-owned filesystem boundaries via roots/list and roots/list_changed and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 3.2 validation S6Q042. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **B:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **C:** Correct. prevents `../` and symlink hop attacks that would escape the user’s approved `file://` allowlist.
- **D:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.

### Question 43 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). MCP 2025-11-25 requires Enforce client-owned filesystem boundaries via roots/list and roots/list_changed; the alternative breaks capability negotiation or security for SOC automation. Skill 3.2 validation S6Q043. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. prevents `../` and symlink hop attacks that would escape the user’s approved `file://` allowlist.
- **B:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.
- **C:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.
- **D:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.

### Question 44 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). Selecting this honors Enforce client-owned filesystem boundaries via roots/list and roots/list_changed and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 3.2 validation S6Q044. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. prevents `../` and symlink hop attacks that would escape the user’s approved `file://` allowlist.
- **B:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.
- **C:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **D:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.

### Question 45 — `B, E` (Prompts, Sampling, Roots & Elicitation)

Correct answers: B and E (are correct). This choice correctly implements Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Skill 3.3 validation S6Q045. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.
- **B:** Correct. maps server intent to Host model fleet tiers without hardcoding vendor model IDs into server code.
- **C:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.
- **D:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **E:** Correct. limits what prior server context flows into delegated sampling calls, preventing cross-server data exfiltration.

### Question 46 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). Selecting this honors Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 3.3 validation S6Q046. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **B:** Correct. lets servers delegate LLM sub-tasks (summarization, critique) back to the Host model under explicit preference caps.
- **C:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **D:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.

### Question 47 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). Per MCP 2025-11-25, Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls ensures spec-compliant lifecycle and isolation for SOC automation. Skill 3.3 validation S6Q047. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. maps server intent to Host model fleet tiers without hardcoding vendor model IDs into server code.
- **B:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.
- **C:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **D:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.

### Question 48 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). Selecting this honors Collect human input via elicitation/create with requestedSchema and form round-trips and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 3.4 validation S6Q048. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.
- **B:** Correct. turns server data needs into typed Host-rendered forms rather than chat text parsing, with explicit schema validation.
- **C:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **D:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.

### Question 49 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). This follows the MCP specification for Collect human input via elicitation/create with requestedSchema and form round-trips, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 3.4 validation S6Q049. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. turns server data needs into typed Host-rendered forms rather than chat text parsing, with explicit schema validation.
- **B:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **C:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.
- **D:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.

### Question 50 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). MCP 2025-11-25 requires Collect human input via elicitation/create with requestedSchema and form round-trips; the alternative breaks capability negotiation or security for SOC automation. Skill 3.4 validation S6Q050. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **B:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.
- **C:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.
- **D:** Correct. lets servers delegate LLM sub-tasks (summarization, critique) back to the Host model under explicit preference caps.

### Question 51 — `D, E, F` (Prompts, Sampling, Roots & Elicitation)

Correct answers: D, E, and F (are correct). This follows the MCP specification for Regulate verbosity via logging/setLevel and notifications/message level filtering, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 3.5 validation S6Q051. [Skill 3.5: Regulate verbosity via logging/setLevel and notifications/message level filtering | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/logging/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.
- **B:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **C:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.
- **D:** Correct. respects user-selected verbosity while still flowing warnings/errors through observability pipelines.
- **E:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.
- **F:** Correct. correlates streaming progress notifications to the correct in-flight tool/resource fetch without guessing.

### Question 52 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). MCP 2025-11-25 requires Regulate verbosity via logging/setLevel and notifications/message level filtering; the alternative breaks capability negotiation or security for SOC automation. Skill 3.5 validation S6Q052. [Skill 3.5: Regulate verbosity via logging/setLevel and notifications/message level filtering | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/logging/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **B:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **C:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.
- **D:** Correct. respects user-selected verbosity while still flowing warnings/errors through observability pipelines.

### Question 53 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). This choice correctly implements Correlate progress and completion flows with progressToken and completion/complete semantics for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Skill 3.6 validation S6Q053. [Skill 3.6: Correlate progress and completion flows with progressToken and completion/complete semantics | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/prompts]

- **A:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **B:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.
- **C:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.
- **D:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.

### Question 54 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). Selecting this honors Correlate progress and completion flows with progressToken and completion/complete semantics and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 3.6 validation S6Q054. [Skill 3.6: Correlate progress and completion flows with progressToken and completion/complete semantics | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/prompts]

- **A:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.
- **B:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **C:** Correct. enables UX-level typeahead without invoking costly tools, scoped to declared completion capabilities.
- **D:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.

### Question 55 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). This follows the MCP specification for Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle, correcting the insecure/incompatible anti-pattern for SOC automation. Reference 4.1 S6Q055. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Incorrect. splitting endpoints and ignoring session/resumability headers reverts to pre-March 2025 deprecated SSE transport.
- **B:** Correct. matches 2025-11-25 Streamable HTTP spec: single endpoint, dual Accept, session ID management, and resumable SSE stream option.
- **C:** Incorrect. returning HTML instead of JSON-RPC errors and retrying without backoff causes parsing failures and duplicate mutations.
- **D:** Incorrect. unbounded batching and cross-tenant session ID reuse breaks rate limiting and tenant isolation guarantees.

### Question 56 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). This follows the MCP specification for Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 4.1 validation S6Q056. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Incorrect. installing random `curl | bash` MCP servers without registry signature verification imports unvetted RCE into the IDE.
- **B:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **C:** Correct. gives OS-level isolation, clean env var scoping, and automatic teardown when Host exits without port conflicts.
- **D:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.

### Question 57 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). This choice correctly implements Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Skill 4.1 validation S6Q057. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Correct. prevents log interleaving from corrupting JSON-RPC framing that parsers expect line-delimited on stdout.
- **B:** Incorrect. reimplementing a Postgres MCP server from scratch when a registry-verified one already exists wastes review cycles.
- **C:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **D:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.

### Question 58 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). This choice correctly implements Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Skill 4.2 validation S6Q058. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.
- **B:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **C:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **D:** Correct. recovers progress streams and notifications lost during 5–30s mobile handoffs without missing tool progress events.

### Question 59 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). This choice correctly implements Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Skill 4.2 validation S6Q059. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **B:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **C:** Correct. preserves capability state and pagination cursors after transient network loss without re-initializing.
- **D:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.

### Question 60 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). MCP 2025-11-25 requires Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response); the alternative breaks capability negotiation or security for SOC automation. Skill 4.2 validation S6Q060. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. lets simple request/reply skip SSE overhead while enabling streaming only for long-running tool progress.
- **B:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.
- **C:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.
- **D:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.

### Question 61 — `B, D` (Transports, Sessions & Protocol Evolution)

Correct answers: B and D (are correct). This follows the MCP specification for Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 4.3 validation S6Q061. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **B:** Correct. recovers progress streams and notifications lost during 5–30s mobile handoffs without missing tool progress events.
- **C:** Incorrect. skipping Inspector and relying only on unit mocks misses real transport framing and pagination/cancellation bugs.
- **D:** Correct. preserves capability state and pagination cursors after transient network loss without re-initializing.
- **E:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.

### Question 62 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). MCP 2025-11-25 requires Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay; the alternative breaks capability negotiation or security for SOC automation. Skill 4.3 validation S6Q062. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Correct. preserves capability state and pagination cursors after transient network loss without re-initializing.
- **B:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.
- **C:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **D:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.

### Question 63 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). This follows the MCP specification for Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 4.3 validation S6Q063. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.
- **B:** Correct. preserves capability state and pagination cursors after transient network loss without re-initializing.
- **C:** Incorrect. dumping base64 blobs as plain text without typed content blocks loses mimeType and forces heuristic parsing.
- **D:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.

### Question 64 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). This choice correctly implements Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Skill 4.4 validation S6Q064. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.
- **B:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.
- **C:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **D:** Correct. avoids thundering herds after gateway restarts while ensuring exactly-once progress recovery via resumability.

### Question 65 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). This follows the MCP specification for Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 4.4 validation S6Q065. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.
- **B:** Incorrect. batching 200 unrelated tool calls into one HTTP request beyond advertised limits times out the whole batch.
- **C:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.
- **D:** Incorrect. installing random `curl | bash` MCP servers without registry signature verification imports unvetted RCE into the IDE.

### Question 66 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). Per MCP 2025-11-25, Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP ensures spec-compliant lifecycle and isolation for SOC automation. Skill 4.4 validation S6Q066. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Correct. tracks spec evolution: split GET /sse + POST /messages merged into single POST with Accept-driven streaming.
- **B:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.
- **C:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **D:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.

### Question 67 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). MCP 2025-11-25 requires Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation; the alternative breaks capability negotiation or security for SOC automation. Skill 4.5 validation S6Q067. [Skill 4.5: Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/progress/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. joining user input with path concatenation without canonicalization enables classic directory traversal.
- **B:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **C:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **D:** Correct. survives AWS ALB 60s idle timeout and Kubernetes GFE that silently drops idle SSE streams.

### Question 68 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). This choice correctly implements Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Skill 4.5 validation S6Q068. [Skill 4.5: Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/progress/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **B:** Incorrect. implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.
- **C:** Incorrect. printing logs to stdout alongside JSON-RPC breaks line-delimited parsing and throws Parse error -32700.
- **D:** Correct. survives AWS ALB 60s idle timeout and Kubernetes GFE that silently drops idle SSE streams.

### Question 69 — `A, D` (Transports, Sessions & Protocol Evolution)

Correct answers: A and D (are correct). This follows the MCP specification for Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 4.6 validation S6Q069. [Skill 4.6: Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/cancellation/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. survives AWS ALB 60s idle timeout and Kubernetes GFE that silently drops idle SSE streams.
- **B:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **C:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **D:** Correct. keeps MCP semantics intact through enterprise L7 filters that otherwise strip SSE headers and session sticky state.
- **E:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.

### Question 70 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). Per MCP 2025-11-25, Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival ensures spec-compliant lifecycle and isolation for SOC automation. Skill 4.6 validation S6Q070. [Skill 4.6: Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/cancellation/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.
- **B:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.
- **C:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **D:** Correct. survives AWS ALB 60s idle timeout and Kubernetes GFE that silently drops idle SSE streams.

### Question 71 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). This follows the MCP specification for Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 5.1 validation S6Q071. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **B:** Incorrect. requiring clients to poll list on a timer to detect new resources defeats MCP push efficiency.
- **C:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **D:** Correct. enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.

### Question 72 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). Selecting this honors Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 5.1 validation S6Q072. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **B:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.
- **C:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **D:** Incorrect. parsing free-form chat replies as structured data instead of typed elicitation invites format errors and injection.

### Question 73 — `A` (Authorization, Security, Trust & Registry)

Correct answer: A (is correct). Selecting this honors Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 5.1 validation S6Q073. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Correct. enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.
- **B:** Incorrect. deploying greenfield on the deprecated dual-endpoint SSE transport incurs future migration cost and lacks session IDs.
- **C:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.
- **D:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.

### Question 74 — `B, C` (Authorization, Security, Trust & Registry)

Correct answers: B and C (are correct). Per MCP 2025-11-25, Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings ensures spec-compliant lifecycle and isolation for SOC automation. Skill 5.2 validation S6Q074. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.
- **B:** Correct. supports desktop IDE/CLI auth via ephemeral loopback listeners while forbidding http redirects to remote hosts.
- **C:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.
- **D:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **E:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.

### Question 75 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). Per MCP 2025-11-25, Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings ensures spec-compliant lifecycle and isolation for SOC automation. Skill 5.2 validation S6Q075. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **B:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **C:** Incorrect. implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.
- **D:** Correct. supports desktop IDE/CLI auth via ephemeral loopback listeners while forbidding http redirects to remote hosts.

### Question 76 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). This follows the MCP specification for Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 5.2 validation S6Q076. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **B:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **C:** Correct. aligns MCP with current OAuth 2.1 security posture, eliminating token leakage vectors of legacy grants.
- **D:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.

### Question 77 — `A` (Authorization, Security, Trust & Registry)

Correct answer: A (is correct). MCP 2025-11-25 requires Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality; the alternative breaks capability negotiation or security for SOC automation. Reference 5.3 S6Q077. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Correct. follows MCP auth spec evolution: OAuth 2.1 with PKCE, protected resource metadata, RFC 8707 audience binding, and RFC 9207 issuer checks.
- **B:** Incorrect. reusing a single audience-less token across resource servers enables cross-server token replay and mix-up attacks.
- **C:** Incorrect. hardcoded keys and alg:none tokens with blanket admin grants violate OAuth 2.1 and privilege separation.
- **D:** Incorrect. exposing secrets in client bundles and downgrading PKCE/TLS undermines OAuth confidentiality and channel binding.

### Question 78 — `C, E` (Authorization, Security, Trust & Registry)

Correct answers: C and E (are correct). Selecting this honors Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 5.3 validation S6Q078. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **B:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **C:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.
- **D:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.
- **E:** Correct. enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.

### Question 79 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). Selecting this honors Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 5.3 validation S6Q079. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.
- **B:** Incorrect. joining user input with path concatenation without canonicalization enables classic directory traversal.
- **C:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **D:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.

### Question 80 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). This choice correctly implements Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Skill 5.4 validation S6Q080. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.
- **B:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.
- **C:** Correct. stops a docs MCP server from using its tool output to call a payment MCP’s `transfer` tool via implicit ambient authority.
- **D:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.

### Question 81 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). This choice correctly implements Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Skill 5.4 validation S6Q081. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.
- **B:** Incorrect. logging full tool arguments including customer PII and bearer tokens creates GDPR and credential-leak second-order risks.
- **C:** Incorrect. dumping base64 blobs as plain text without typed content blocks loses mimeType and forces heuristic parsing.
- **D:** Correct. stops a docs MCP server from using its tool output to call a payment MCP’s `transfer` tool via implicit ambient authority.

### Question 82 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). Selecting this honors Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 5.4 validation S6Q082. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.
- **B:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.
- **C:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.
- **D:** Correct. displays descriptions for human review but never concatenates them into system prompts or plan steps as trusted policy.

### Question 83 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). This choice correctly implements Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Skill 5.5 validation S6Q083. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **B:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.
- **C:** Correct. enables post-incident forensics without persisting PII/tokens, keyed by stable tool provenance hashes.
- **D:** Incorrect. implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.

### Question 84 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). MCP 2025-11-25 requires Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging; the alternative breaks capability negotiation or security for SOC automation. Skill 5.5 validation S6Q084. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.
- **B:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.
- **C:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.
- **D:** Correct. provides supply-chain tamper evidence via package signing and publisher identity beyond raw GitHub stars.

### Question 85 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). This follows the MCP specification for Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 5.5 validation S6Q085. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **B:** Correct. provides supply-chain tamper evidence via package signing and publisher identity beyond raw GitHub stars.
- **C:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.
- **D:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.

### Question 86 — `A, B` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: A and B (are correct). Selecting this honors Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 6.1 validation S6Q086. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Correct. gives models complete, machine-validated contracts for tool selection and argument generation.
- **B:** Correct. standardizes transport selection, capability tracking, and request/notification routing behind a single Client facade.
- **C:** Incorrect. treating MCP as a replacement for A2A agent discovery and task lifecycles conflates vertical tool attachment with peer delegation.
- **D:** Incorrect. joining user input with path concatenation without canonicalization enables classic directory traversal.
- **E:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.

### Question 87 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). This choice correctly implements Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Skill 6.1 validation S6Q087. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.
- **B:** Correct. standardizes transport selection, capability tracking, and request/notification routing behind a single Client facade.
- **C:** Incorrect. enabling experimental tasks by default without capability checks forces unready clients into breaking draft methods.
- **D:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.

### Question 88 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). This choice correctly implements Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Skill 6.1 validation S6Q088. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Incorrect. implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.
- **B:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.
- **C:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **D:** Correct. gives decorator-ergonomic tool/resource registration with Pydantic/JSON Schema coherence across Python Hosts.

### Question 89 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). Selecting this honors Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 6.2 validation S6Q089. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Correct. gives OS-level isolation, clean env var scoping, and automatic teardown when Host exits without port conflicts.
- **B:** Incorrect. treating MCP as a replacement for A2A agent discovery and task lifecycles conflates vertical tool attachment with peer delegation.
- **C:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.
- **D:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.

### Question 90 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). Per MCP 2025-11-25, Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates ensures spec-compliant lifecycle and isolation for SOC automation. Skill 6.2 validation S6Q090. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **B:** Correct. standardizes transport selection, capability tracking, and request/notification routing behind a single Client facade.
- **C:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.
- **D:** Incorrect. deploying greenfield on the deprecated dual-endpoint SSE transport incurs future migration cost and lacks session IDs.

### Question 91 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). Per MCP 2025-11-25, Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates ensures spec-compliant lifecycle and isolation for SOC automation. Skill 6.2 validation S6Q091. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **B:** Incorrect. treating MCP as a replacement for A2A agent discovery and task lifecycles conflates vertical tool attachment with peer delegation.
- **C:** Incorrect. generating random progressTokens server-side with no binding to request id mixes streams across concurrent tasks.
- **D:** Correct. catches lifecycle, capability, and schema mismatches before CI with real-transport conformance testing.

### Question 92 — `B, C` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: B and C (are correct). Per MCP 2025-11-25, Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation ensures spec-compliant lifecycle and isolation for SOC automation. Skill 6.3 validation S6Q092. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.
- **B:** Correct. keeps patch/minor server releases compatible with older Hosts that simply ignore unknown capabilities.
- **C:** Correct. makes servers discoverable with verifiable supply-chain metadata and semver-aware update notifications.
- **D:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.
- **E:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.

### Question 93 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). This choice correctly implements Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Skill 6.3 validation S6Q093. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **B:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **C:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **D:** Correct. ensures reproducible, least-privilege runtime with declared transport and liveness for orchestrators.

### Question 94 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). This follows the MCP specification for Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation, correcting the insecure/incompatible anti-pattern for SOC automation. Skill 6.3 validation S6Q094. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.
- **B:** Correct. ensures reproducible, least-privilege runtime with declared transport and liveness for orchestrators.
- **C:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **D:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.

### Question 95 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). This choice correctly implements Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation for Sentinel Cyber Fusion while the distractors violate transport/session guarantees. Reference 6.4 S6Q095. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Correct. applies MCP security checklist: supply-chain pinning, description-vs-logic separation, consent gating, and provenance monitoring against poison/rug-pull.
- **B:** Incorrect. blind auto-approval and treating descriptions as trusted instructions invites prompt injection and supply-chain compromise.
- **C:** Incorrect. unvetted curl-piped installs with maximal scopes and plaintext token storage maximizes blast radius from a single malicious server.
- **D:** Incorrect. silent exfiltration without rate limits or audit visibility breaks data minimization and incident-response traceability.

### Question 96 — `C, D` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: C and D (are correct). Selecting this honors Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation and prevents the listed failure mode in Sentinel Cyber Fusion SOC automation flows. Skill 6.4 validation S6Q096. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **B:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.
- **C:** Correct. powers per-tool SLOs and supply-chain forensics without persisting sensitive tool argument values.
- **D:** Correct. enables post-incident forensics without persisting PII/tokens, keyed by stable tool provenance hashes.
- **E:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.

### Question 97 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). Per MCP 2025-11-25, Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation ensures spec-compliant lifecycle and isolation for SOC automation. Skill 6.4 validation S6Q097. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Correct. traces tool call latency through Streamable HTTP gateways into server execution with per-session correlation.
- **B:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.
- **C:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.
- **D:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.

### Question 98 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). Per MCP 2025-11-25, Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns ensures spec-compliant lifecycle and isolation for SOC automation. Skill 6.5 validation S6Q098. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Incorrect. implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.
- **B:** Incorrect. spamming debug traces at error level drowns real failures and violates MCP logging level contract.
- **C:** Correct. uses MCP vertically for capabilities and A2A horizontally for peer negotiation, per LM-Foundation AAIF stack guidance.
- **D:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.

### Question 99 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). Per MCP 2025-11-25, Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns ensures spec-compliant lifecycle and isolation for SOC automation. Skill 6.5 validation S6Q099. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.
- **B:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **C:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.
- **D:** Correct. centralizes AuthZ, session affinity, and observability without duplicating gateway logic in each MCP server.

### Question 100 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). MCP 2025-11-25 requires Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns; the alternative breaks capability negotiation or security for SOC automation. Skill 6.5 validation S6Q100. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **B:** Correct. reuses vetted categories (databases, cloud, payments) before building bespoke wrappers over public APIs.
- **C:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.
- **D:** Incorrect. assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.
