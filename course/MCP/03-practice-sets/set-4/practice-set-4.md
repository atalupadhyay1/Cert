# MCP: Model Context Protocol: Servers, Clients, Transports & Security — Full-Length Mock Exam 4 — Veridian Legal Vault (Legal & Compliance Docs)

**Theme:** Capabilities Negotiation, Completions API, Logging Levels & Audit Provenance  
**Credential alignment:** `Model Context Protocol (MCP 2025-11-25) — Tool & Context Standard`  
**Blueprint baseline:** `November 2026 (MCP Specification 2025-11-25 · MCP Registry & Inspector · OAuth 2.1 + RFC 8707/9207 + CIMD · OWASP MCP Security Checklist)` (https://modelcontextprotocol.io/introduction · https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation · https://genai.owasp.org/resource/mcp-security-checklist/)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `120 minutes` (`72 seconds/question` full-endurance pacing; aligns with `120 minutes` on NVIDIA NCP-AAI & GitHub GH-600)

> **Disclaimer:** Independent educational practice material authored from public engineering specifications and open-protocol documentation — not affiliated with, sponsored by, or endorsed by NVIDIA, the Linux Foundation, Anthropic, OpenAI, Google, Microsoft, GitHub, LangChain, or OWASP. Practice scores do not guarantee passing any third-party certification exam.

## Questions

---

## Domain 1 — MCP Foundations, Architecture & Lifecycle (16–20% blueprint weight · 18 questions)

### 1. For legal compliance docs at Veridian Legal Vault, which ordered flow correctly implements the MCP 2025-11-25 requirement? Case 4176: registry installs via `curl¦bash` without signature check. Scenario 1.1-4-1.

- **A.** Server sends `initialize` to client → client negotiates logging level first → exchange OAuth tokens inside `initialize` params → begin sampling without capability check
- **B.** Client hardcodes `protocolVersion: "1.0"` forever → ignore server `protocolVersion` echo → send duplicate `initialize` on every ping → cache capabilities indefinitely
- **C.** Client calls `tools/call` immediately → server returns capability list on tool error → client sends `initialize` afterward → skip `notifications/initialized`
- **D.** Client sends `initialize` with `protocolVersion` & `capabilities` → server replies with negotiated version & capabilities → client sends `notifications/initialized` → normal `tools/list` & `resources/list` calls begin

### 2. Veridian Legal Vault engineers designing an MCP system for legal compliance docs must evaluate two correct controls. Which two statements are correct? Select two. Incident 9921: deprecated `/sse` + `/messages` split endpoint still in prod. [1.1 #2]

- **A.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **B.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **C.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **D.** Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation
- **E.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible

### 3. For legal compliance docs, Veridian Legal Vault must choose between stdio and Streamable HTTP transports. The correct choice is to ____. Trace 3410: `resource` audience binding missing per RFC 8707. [1.1 #3]

- **A.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **B.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **C.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **D.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation

### 4. Veridian Legal Vault wants legal compliance docs MCP completions for enum arguments. The valid method is ____. Ticket 3365: `notifications/roots/list_changed` ignored after folder add. [1.2 #4]

- **A.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **B.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **C.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **D.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds

### 5. Complete the missing MCP field: In the Veridian Legal Vault legal compliance docs server, `____` must be set to the MCP-required value to enable legal compliance docs correctly. Ticket 1020: plaintext `config.json` holds refresh token. [1.2 #5]

- **A.** Publish to the **MCP Registry (`server.json` with `name`, `version`, `description`, `repository`, `packages`)** with npm/PyPI provenance & publisher verification
- **B.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **C.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **D.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways

### 6. The Veridian Legal Vault MCP configuration for legal compliance docs shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Case 2000: Host passes full env block to untrusted calendar server. [1.2 #6]

- **A.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **B.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **C.** Model the MCP triad: **Host** (AI app process) spawns **Client** (1:1 per server, inside host) and **Server** (external capability) with strict process isolation
- **D.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`

### 7. At Veridian Legal Vault, the MCP client code handling legal compliance docs leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Alert 7748: `isError:false` with HTML error page masks failure. Scenario 1.3-4-7.

- **A.** Client calls undefined tool name → server creates tool on-the-fly → skip inputSchema validation → stream 50-MB blob as single text content block
- **B.** Server exposes 200 tools without descriptions → client guesses arguments via prompt → server executes shell with raw LLM string → return HTML page inside isError=false
- **C.** Server declares tool with `name`, `description`, `inputSchema` (JSON Schema) → client `tools/list` discovers it → model calls `tools/call` with validated args → server validates, executes idempotently & returns `content` + `isError`
- **D.** Server returns tool result before validation → client retries with doubled args → disable tools/list_changed notifications → cache tool names forever

### 8. For legal compliance docs at Veridian Legal Vault, three controls are required for MCP compliance. Which three are correct? Select three. Alert 8737: `Mcp-Session-Id` reused across tenants. [1.3 #8]

- **A.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **B.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **C.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **D.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **E.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **F.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly

### 9. At Veridian Legal Vault, the MCP client code handling legal compliance docs leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Case 9160: `structuredContent` missing despite `outputSchema` declared. [1.3 #9]

- **A.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **B.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **C.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **D.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage

### 10. Which two behaviors correctly describe MCP legal compliance docs handling at Veridian Legal Vault? Select two. Audit 2839 flags `alg:none` token acceptance in staging. [1.4 #10]

- **A.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **B.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **C.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **D.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **E.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle

### 11. At Veridian Legal Vault, legal compliance docs MCP gateway logs show `Last-Event-ID` replay gaps. The team should ____. Review 6813: `outputSchema` mismatched to `structuredContent` shape. [1.4 #11]

- **A.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **B.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **C.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **D.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`

### 12. In `Veridian Legal Vault` `legal compliance docs` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Trace 5060: 200-tool batch exceeds advertised `maxBatchSize`. [1.4 #12]

- **A.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **B.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **C.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **D.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`

### 13. The Veridian Legal Vault legal compliance docs Host caches `roots/list` forever and misses workspace changes. The fix is to ____. Audit 7040: `includeContext=allServers` exfiltrates cross-server data. [1.5 #13]

- **A.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **B.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **C.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **D.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**

### 14. The MCP Inspector highlights `____` as missing for legal compliance docs at Veridian Legal Vault. Which completion is spec-correct? Log 5571: `prompt/get` uses client-side interpolation without validation. [1.5 #14]

- **A.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **B.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **C.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks
- **D.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization

### 15. For legal compliance docs at Veridian Legal Vault, the Host must reconcile `protocolVersion` negotiation after an upgrade. Which action is correct? Review 6383 notes `resources/list_changed` never fired after ingest. [1.5 #15]

- **A.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **B.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params
- **C.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **D.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent

### 16. Proposed solution: To handle legal compliance docs, Veridian Legal Vault plans to pass the entire Host environment including prod secrets to every MCP server. Does this satisfy the MCP specification? Incident MCP-2026-6980 shows Misconfigured `Mcp-Session-Id` routing. [1.6 #16]

- **A.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **B.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure
- **C.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **D.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks

### 17. At Veridian Legal Vault, legal compliance docs MCP tool descriptions are concatenated into system prompts. Which safeguard is needed? Trace 7483: `resource` audience binding missing per RFC 8707. [1.6 #17]

- **A.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **B.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **C.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **D.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways

### 18. Veridian Legal Vault MCP server for legal compliance docs uses static API keys in `Authorization`. The OAuth 2.1 migration is to ____. Alert 9040: `isError:false` with HTML error page masks failure. [1.6 #18]

- **A.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **B.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **C.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **D.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions

---

## Domain 2 — Tools, Resources & Resource Templates (18–22% blueprint weight · 20 questions)

### 19. What is the correct 4-step order for legal compliance docs workflow at Veridian Legal Vault under MCP 2025-11-25? Incident 4888: OAuth PKCE verifier omitted for public client. Scenario 2.1-4-19.

- **A.** Server lists resources without capability flag → client polls `resources/list` every 10 ms in loop → ignore `resources/list_changed` notifications → request resources via tools/call
- **B.** Server returns resources without uri fields → client stores resource content in tool history → server omits page cursors for 10k items → skip mimeType declaration
- **C.** Server advertises `resources` capability → client calls `resources/list` or `resources/templates/list` → client reads `resources/read` with `uri` → server returns `contents` with `mimeType`, handling pagination cursors
- **D.** Client guesses file URIs without list → server returns OS absolute paths as uri → embed 10-MB binary as base64 JSON string → skip uri validation

### 20. At Veridian Legal Vault, the MCP client code handling legal compliance docs leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Review 8469: sampling loop lacks depth cap and cost budget. [2.1 #20]

- **A.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **B.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively
- **C.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **D.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation

### 21. Veridian Legal Vault handles legal compliance docs via MCP sampling delegation. To enforce least privilege, the server should ____. Log 4977: `prompt/get` uses client-side interpolation without validation. [2.1 #21]

- **A.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **B.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **C.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **D.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation

### 22. Veridian Legal Vault MCP Host for legal compliance docs must handle `elicitation/create` versus chat parsing. Which is spec-correct? Ticket 7537: `notifications/roots/list_changed` ignored after folder add. [2.1 #22]

- **A.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **B.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect
- **C.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **D.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization

### 23. For legal compliance docs at Veridian Legal Vault, two best practices align with MCP 2025-11-25. Which two should be implemented? Select two. Incident 3044: OAuth PKCE verifier omitted for public client. [2.2 #23]

- **A.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **B.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **C.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **D.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds
- **E.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean

### 24. Proposed solution: use the deprecated HTTP+SSE split endpoint for all new greenfield remote servers is suggested for legal compliance docs at Veridian Legal Vault. Does this meet the goal? Incident 9855: tool `inputSchema` validation skipped, injection observed. [2.2 #24]

- **A.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **B.** Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation
- **C.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **D.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean

### 25. Complete the missing MCP field: In the Veridian Legal Vault legal compliance docs server, `____` must be set to the MCP-required value to enable legal compliance docs correctly. Log 6114: `prompt/get` uses client-side interpolation without validation. [2.2 #25]

- **A.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **B.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **C.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **D.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params

### 26. During legal compliance docs review at Veridian Legal Vault, the MCP server emits debug logs at `error` level. The proper level is ____. Case 7933: `structuredContent` missing despite `outputSchema` declared. [2.2 #26]

- **A.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean
- **B.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)
- **C.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **D.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params

### 27. For legal compliance docs at Veridian Legal Vault, two best practices align with MCP 2025-11-25. Which two should be implemented? Select two. Audit 9238: `includeContext=allServers` exfiltrates cross-server data. [2.3 #27]

- **A.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **B.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **C.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **D.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **E.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling

### 28. During legal compliance docs incident triage at Veridian Legal Vault, audit logs lack `requestId` correlation. The correction is to ____. Log 2375: `prompt/get` uses client-side interpolation without validation. [2.3 #28]

- **A.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **B.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **C.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **D.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`

### 29. At Veridian Legal Vault, legal compliance docs MCP gateway logs show `Last-Event-ID` replay gaps. The team should ____. Log 2375: `prompt/get` uses client-side interpolation without validation. [2.3 #29]

- **A.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **B.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **C.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **D.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle

### 30. For legal compliance docs, Veridian Legal Vault must choose between stdio and Streamable HTTP transports. The correct choice is to ____. Review 2775: sampling loop lacks depth cap and cost budget. [2.4 #30]

- **A.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **B.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **C.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **D.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively

### 31. For legal compliance docs at Veridian Legal Vault, token storage uses plaintext `config.json`. The secure alternative is to ____. Audit 4730 flags `alg:none` token acceptance in staging. [2.4 #31]

- **A.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **B.** Package remote servers as **non-root `distroless` containers** with explicit `MCP_TRANSPORT=streamable-http` env and health `/mcp` ping
- **C.** Validate `tools/call` **`arguments` against `inputSchema`** server-side before execution; return `isError:true` with structured content on failure
- **D.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**

### 32. At Veridian Legal Vault, legal compliance docs MCP server batch returns timeout for 200 calls. The team should ____. Alert 9145: `Mcp-Session-Id` reused across tenants. [2.4 #32]

- **A.** Distinguish **direct `resources` (static URI items) from `resourceTemplates` (URI-template factories with `uriTemplate` + `list` expansion)**
- **B.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **C.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **D.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages

### 33. To implement legal compliance docs correctly for Veridian Legal Vault, which 4-step sequence satisfies the MCP spec? Log entry 7089 shows `Method not found -32601` without capability check. Scenario 2.5-4-33.

- **A.** Server declares client roots unilaterally → client trusts arbitrary server-provided paths → skip roots/list → ignore list_changed notifications
- **B.** Client exposes entire `C:\` without consent → server walks parent directories above declared roots → disable path canonicalization → follow symlinks blindly
- **C.** Server hardcodes `roots/list` response → client polls filesystem without notification channel → skip name/uri validation → cache roots forever
- **D.** Client declares `roots` capability with `file://` allowlist → server calls `roots/list` to learn boundaries → server restricts `resources/read` & tool file ops to those roots → handle `notifications/roots/list_changed`

### 34. Veridian Legal Vault MCP server for legal compliance docs requires two valid security hardening steps. Which two should you apply? Select two. Ticket 4604: `roots/list` poll floods client every 10 ms. [2.5 #34]

- **A.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **B.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **C.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **D.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **E.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks

### 35. A third-party legal compliance docs MCP server at Veridian Legal Vault silently changes tool logic after approval. The defense is to ____. Audit 4073 flags `alg:none` token acceptance in staging. [2.5 #35]

- **A.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **B.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **C.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **D.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling

### 36. The Veridian Legal Vault legal compliance docs Host caches `roots/list` forever and misses workspace changes. The fix is to ____. Log 9337: `initialize` skipped before `tools/list`. [2.6 #36]

- **A.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **B.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`
- **C.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks
- **D.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`

### 37. Proposed solution: allow servers to self-declare client filesystem roots without user consent is suggested for legal compliance docs at Veridian Legal Vault. Does this meet the goal? Ticket 8078 reports `Last-Event-ID` replay mismatch after gateway restart. [2.6 #37]

- **A.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **B.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **C.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **D.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics

### 38. Complete the missing MCP field: In the Veridian Legal Vault legal compliance docs server, `____` must be set to the MCP-required value to enable legal compliance docs correctly. Alert 3725: `isError:false` with HTML error page masks failure. [2.6 #38]

- **A.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **B.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **C.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **D.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking

---

## Domain 3 — Prompts, Sampling, Roots & Elicitation (14–18% blueprint weight · 16 questions)

### 39. Veridian Legal Vault needs to secure legal compliance docs tool calls that mutate production data. The right control is to ____. Log 2739: SSE stream without `eventId` loses progress on reconnect. [3.1 #39]

- **A.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **B.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **C.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`
- **D.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke

### 40. In `Veridian Legal Vault` `legal compliance docs` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Alert 9559: `Mcp-Session-Id` reused across tenants. [3.1 #40]

- **A.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`
- **B.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **C.** Advertise fine-grained **`capabilities`** (`tools`, `resources`, `prompts`, `roots`, `sampling`, `logging`) to gate feature usage
- **D.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`

### 41. A third-party legal compliance docs MCP server at Veridian Legal Vault silently changes tool logic after approval. The defense is to ____. Incident 3771: tool logic changed post-approval (rug-pull) undetected. [3.1 #41]

- **A.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **B.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **C.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **D.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs

### 42. For legal compliance docs at Veridian Legal Vault, two best practices align with MCP 2025-11-25. Which two should be implemented? Select two. Log entry 1479 shows `Method not found -32601` without capability check. [3.2 #42]

- **A.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **B.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **C.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **D.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **E.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)

### 43. The MCP Inspector highlights `____` as missing for legal compliance docs at Veridian Legal Vault. Which completion is spec-correct? Review 4004: `outputSchema` mismatched to `structuredContent` shape. [3.2 #43]

- **A.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **B.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **C.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **D.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways

### 44. Proposed solution: poll resources/list every 10 ms instead of subscribing to list_changed is suggested for legal compliance docs at Veridian Legal Vault. Does this meet the goal? Review 8324: `outputSchema` mismatched to `structuredContent` shape. [3.2 #44]

- **A.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **B.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **C.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **D.** Use **`outputSchema` + `structuredContent`** (2025-06-18) for machine-readable tool results alongside human-readable `content`

### 45. In `Veridian Legal Vault` `legal compliance docs` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Log entry 3541 shows `Method not found -32601` without capability check. [3.3 #45]

- **A.** Address resources by **canonical `uri` with scheme** (`file://`, `db://`, `https://`) plus `name`, `mimeType`, optional `annotations`
- **B.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **C.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds
- **D.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing

### 46. For Veridian Legal Vault legal compliance docs server to advertise new capabilities after a deploy, the correct notification is ____. Case 6639: Host passes full env block to untrusted calendar server. [3.3 #46]

- **A.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **B.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **C.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **D.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`

### 47. You are reviewing an MCP implementation for Veridian Legal Vault that handles legal compliance docs. Which statement about ____ is accurate under MCP 2025-11-25? Review 5334 notes `resources/list_changed` never fired after ingest. [3.3 #47]

- **A.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **B.** Control context leakage via **`includeContext` (none / thisServer / allServers)** in `sampling/createMessage`
- **C.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **D.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling

### 48. The Veridian Legal Vault team documents the legal compliance docs MCP flow. Which sequence of actions is spec-compliant? Ticket 3561: `notifications/roots/list_changed` ignored after folder add. Scenario 3.4-4-48.

- **A.** Server advertises sampling need → checks client `sampling` capability → sends `sampling/createMessage` with `messages`, `maxTokens`, `modelPreferences` → client applies human-in-loop gating & returns generation
- **B.** Client exposes sampling by default without opt-in → server loops sampling/createMessage recursively → ignore modelPreferences hints → return raw chain-of-thought as tool output
- **C.** Server sends sampling without capability check → include raw customer PII in messages → skip maxTokens limits → client auto-executes without user consent
- **D.** Server mixes sampling messages into tool descriptions → client forwards without isolation → skip cost tracking → cache sampling results as facts

### 49. Veridian Legal Vault must fix its legal compliance docs MCP integration. Which two changes bring it into spec compliance? Select two. Case 7446: `structuredContent` missing despite `outputSchema` declared. [3.4 #49]

- **A.** Handle **`sampling/createMessage`** from server: `messages[]`, `modelPreferences`, `systemPrompt`, `maxTokens`, `temperature`
- **B.** Return tool output as **typed `content` blocks**: `text`, `image`/`audio`, `resource`, `resource_link` with paired `isError` boolean
- **C.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`
- **D.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **E.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`

### 50. At Veridian Legal Vault, the MCP client code handling legal compliance docs leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Incident 6315: OAuth PKCE verifier omitted for public client. [3.4 #50]

- **A.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **B.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **C.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **D.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`

### 51. Two statements about MCP legal compliance docs correctly reflect the specification for Veridian Legal Vault. Which two are true? Select two. Case 8006: `structuredContent` missing despite `outputSchema` declared. [3.5 #51]

- **A.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization
- **B.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **C.** Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation
- **D.** Honor client `logging/setLevel` to filter **`notifications/message`** chatter to `debug/info/notice/warning/error` + emit structured `data` payloads
- **E.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`

### 52. Veridian Legal Vault MCP server serving legal compliance docs returns `isError:false` with an HTML error page. The proper fix is to ____. Incident 7595: tool `inputSchema` validation skipped, injection observed. [3.5 #52]

- **A.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **B.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **C.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`
- **D.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle

### 53. In `Veridian Legal Vault` `legal compliance docs` MCP message, the field `____` is blank. Which correct value satisfies MCP 2025-11-25? Alert 3547: `Mcp-Session-Id` reused across tenants. [3.6 #53] with Monte Carlo lineage alert (variant beta 676).

- **A.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **B.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **C.** Link progress streams to originating request via **`progressToken`** supplied in `_meta.progressToken` on the initial request
- **D.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`

### 54. The MCP Inspector highlights `____` as missing for legal compliance docs at Veridian Legal Vault. Which completion is spec-correct? Log 3100: SSE stream without `eventId` loses progress on reconnect. [3.6 #54]

- **A.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **B.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params
- **C.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **D.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)

---

## Domain 4 — Transports, Sessions & Protocol Evolution (14–18% blueprint weight · 16 questions)

### 55. The MCP Inspector highlights `____` as missing for legal compliance docs at Veridian Legal Vault. Which completion is spec-correct? Audit 8766: auto-approve bypasses human consent for destructive tool. [4.1 #55]

- **A.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **B.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **C.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **D.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation

### 56. The MCP Inspector highlights `____` as missing for legal compliance docs at Veridian Legal Vault. Which completion is spec-correct? Ticket 2056 reports `Last-Event-ID` replay mismatch after gateway restart. [4.1 #56]

- **A.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **B.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **C.** Frame every MCP message as **JSON-RPC 2.0** (`jsonrpc`, `id` for requests, `method`, `params`) with `error.code` 32700–32603
- **D.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**

### 57. Proposed solution: pass the entire Host environment including prod secrets to every MCP server is suggested for legal compliance docs at Veridian Legal Vault. Does this meet the goal? Incident 1408: tool `inputSchema` validation skipped, injection observed. [4.1 #57]

- **A.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **B.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **C.** React to **`notifications/roots/list_changed`** by re-calling `roots/list` and re-scoping file watchers & resource subscriptions
- **D.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails

### 58. The Veridian Legal Vault team documents the legal compliance docs MCP flow. Which sequence of actions is spec-compliant? Log 7100: SSE stream without `eventId` loses progress on reconnect. Scenario 4.2-4-58.

- **A.** Client POSTs JSON-RPC to single `mcp` endpoint with `Content-Type: application/json` & `Accept: text/event-stream, application/json` → server may respond with single JSON or SSE stream → client honors `Mcp-Session-Id` & `Last-Event-ID` for resumability
- **B.** Client opens separate GET /sse and POST /message SSE endpoints → send JSON without Accept header → ignore Mcp-Session-Id → close stream after each chunk without Last-Event-ID
- **C.** Client sends batched 100 requests without server batch ack → server streams without event IDs → skip session expiry handling → leak session IDs across tenants
- **D.** Server returns 200 OK with HTML error page → client retries without backoff → disable idempotency on non-idempotent tool calls → omit Content-Type validation

### 59. Veridian Legal Vault observes `prompt injection` payloads via legal compliance docs MCP resource content. The mitigation is to ____. Review 2913 notes `resources/list_changed` never fired after ingest. [4.2 #59]

- **A.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **B.** Reserve **stderr for human-readable logs** in stdio transport; keep stdout exclusively for JSON-RPC messages
- **C.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **D.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes

### 60. During an legal compliance docs workflow audit at Veridian Legal Vault, you notice the MCP server exposes file paths without proper checks. The team must ____. Audit 4872: `includeContext=allServers` exfiltrates cross-server data. [4.2 #60]

- **A.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly
- **B.** Expand prompts via **`prompts/get` with typed `arguments`** → server returns `messages[]` (role/content) ready to append to context
- **C.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **D.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets

### 61. Veridian Legal Vault engineers designing an MCP system for legal compliance docs must evaluate two correct controls. Which two statements are correct? Select two. Alert 6240: `isError:false` with HTML error page masks failure. [4.3 #61]

- **A.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **B.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **C.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **D.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **E.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics

### 62. For legal compliance docs, Veridian Legal Vault must handle `notifications/progress` vs polling. The correct pattern is to ____. Ticket 3961 reports `Last-Event-ID` replay mismatch after gateway restart. [4.3 #62]

- **A.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **B.** Gate unstable features under **`experimental`** capabilities (e.g., `experimental.tasks`) requiring opt-in before standardization
- **C.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **D.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails

### 63. Veridian Legal Vault wants to add prompt packs for legal compliance docs. The MCP-compliant way is to ____. Incident 6396: deprecated `/sse` + `/messages` split endpoint still in prod. [4.3 #63]

- **A.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **B.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **C.** Support **resumability via `Last-Event-ID`** on SSE streams; server replays missed events from event store after disconnect
- **D.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side

### 64. Select three correct MCP legal compliance docs behaviors that Veridian Legal Vault should enforce for its MCP fleet. Select three. Ticket 1988 reports `Last-Event-ID` replay mismatch after gateway restart. [4.4 #64]

- **A.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **B.** Enforce **model-controlled** semantics: Host/Client exposes tools, model chooses when to call via `tools/call`; never auto-invoke
- **C.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **D.** Recognize **HTTP+SSE dual-endpoint transport deprecated March 2025**; migrate to **Streamable HTTP**, preserving Last-Event-ID semantics
- **E.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **F.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414

### 65. The Veridian Legal Vault MCP configuration for legal compliance docs shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Review 5998: `outputSchema` mismatched to `structuredContent` shape. [4.4 #65]

- **A.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **B.** Perform **`initialize` → capability negotiation → `notifications/initialized`** before any `tools/list` or `resources/read`
- **C.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **D.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows

### 66. The MCP Inspector highlights `____` as missing for legal compliance docs at Veridian Legal Vault. Which completion is spec-correct? Alert 6531: `progressToken` mismatch across concurrent tool calls. [4.4 #66]

- **A.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds
- **B.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **C.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`
- **D.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect

### 67. At Veridian Legal Vault, legal compliance docs MCP server batch returns timeout for 200 calls. The team should ____. Log 4356: `initialize` skipped before `tools/list`. [4.5 #67]

- **A.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **B.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **C.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **D.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs

### 68. At Veridian Legal Vault, legal compliance docs MCP server batch returns timeout for 200 calls. The team should ____. Incident MCP-2026-2867 shows Misconfigured `Mcp-Session-Id` routing. [4.5 #68]

- **A.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **B.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **C.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **D.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle

### 69. Proposed solution: To handle legal compliance docs, Veridian Legal Vault plans to poll resources/list every 10 ms instead of subscribing to list_changed. Does this satisfy the MCP specification? Case 4793: `structuredContent` missing despite `outputSchema` declared. [4.6 #69]

- **A.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default
- **B.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **C.** Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation
- **D.** Negotiate **`protocolVersion`** (e.g., `2025-11-25`) during `initialize`; servers echo supported version, clients adapt or disconnect

### 70. Proposed solution: To handle legal compliance docs, Veridian Legal Vault plans to use the deprecated HTTP+SSE split endpoint for all new greenfield remote servers. Does this satisfy the MCP specification? Review 4213: sampling loop lacks depth cap and cost budget. [4.6 #70]

- **A.** Expose **client-owned filesystem boundaries** via `roots` capability; server discovers via `roots/list` and subscribes to `notifications/roots/list_changed`
- **B.** Validate with **`@modelcontextprotocol/inspector`** (UI + CLI) to exercise `tools/list`, `tools/call`, `resources/read` & logging streams interactively
- **C.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **D.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation

---

## Domain 5 — Authorization, Security, Trust & Registry (13–17% blueprint weight · 15 questions)

### 71. Veridian Legal Vault observes `prompt injection` payloads via legal compliance docs MCP resource content. The mitigation is to ____. Review 1138: sampling loop lacks depth cap and cost budget. [5.1 #71]

- **A.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects
- **B.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **C.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`
- **D.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs

### 72. For legal compliance docs at Veridian Legal Vault, the MCP Inspector UI must validate tool schemas. Which approach is correct? Incident 8070: OAuth PKCE verifier omitted for public client. [5.1 #72]

- **A.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **B.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **C.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`
- **D.** Declare reusable **prompts with `name`, `description`, `arguments` (required flag + schema)** via `prompts/list`

### 73. The MCP Inspector highlights `____` as missing for legal compliance docs at Veridian Legal Vault. Which completion is spec-correct? Case 3770: `structuredContent` missing despite `outputSchema` declared. [5.1 #73]

- **A.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **B.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **C.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **D.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`

### 74. Veridian Legal Vault must fix its legal compliance docs MCP integration. Which two changes bring it into spec compliance? Select two. Alert 2241: `Mcp-Session-Id` reused across tenants. [5.2 #74]

- **A.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **B.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **C.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately
- **D.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **E.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`

### 75. During legal compliance docs at Veridian Legal Vault, the MCP server responds with SSE without `eventId`. Which correction is required? Trace 3602: 200-tool batch exceeds advertised `maxBatchSize`. [5.2 #75]

- **A.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **B.** Paginate `resources/list` & `resources/templates/list` via opaque **`cursor`**; clients loop until `nextCursor` is absent
- **C.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **D.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default

### 76. For legal compliance docs, Veridian Legal Vault must handle `notifications/progress` vs polling. The correct pattern is to ____. Ticket 4895: `roots/list` poll floods client every 10 ms. [5.2 #76]

- **A.** Choose **`stdio` for local subprocess servers** (spawned by Host) and **`Streamable HTTP` for remote/network servers** (single POST endpoint, 2025-11-25)
- **B.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`
- **C.** Store tokens in **OS keychain / Credential Manager / libsecret** with DPAPI/Keychain ACLs, never plaintext env or config files
- **D.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle

### 77. Veridian Legal Vault engineers designing an MCP system for legal compliance docs must evaluate two correct controls. Which two statements are correct? Select two. Ticket 9546 reports `Last-Event-ID` replay mismatch after gateway restart. [5.3 #77]

- **A.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs
- **B.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414
- **C.** Discover servers via **MCP Registry search, categories & trust badges** (official, community, verified publisher) before custom builds
- **D.** Declare each tool with **`name` (unique), `title`, `description`, `inputSchema` (JSON Schema)**, optional `outputSchema` and `annotations`
- **E.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token

### 78. The Veridian Legal Vault MCP configuration for legal compliance docs shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Case 3294: `structuredContent` missing despite `outputSchema` declared. [5.3 #78]

- **A.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **B.** Require **OAuth 2.1 (authorization_code + PKCE)** for user-delegated MCP access; forbid implicit/ROPC/password flows
- **C.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **D.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging

### 79. Veridian Legal Vault observes `prompt injection` payloads via legal compliance docs MCP resource content. The mitigation is to ____. Log 3102: `prompt/get` uses client-side interpolation without validation. [5.3 #79]

- **A.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **B.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **C.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **D.** Publish **Protected Resource Metadata (`/.well-known/oauth-protected-resource`) & Authorization Server Metadata (`/.well-known/oauth-authorization-server`)** per RFC 9728 / RFC 8414

### 80. The Veridian Legal Vault MCP configuration for legal compliance docs shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Alert 1266: `isError:false` with HTML error page masks failure. [5.4 #80]

- **A.** Canonicalize, validate UTF-8, and block traversal/symlink escape above declared **Roots** before every file `read`/`write`
- **B.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **C.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**
- **D.** Expose tools via **`tools/list`** (with cursor pagination) and announce changes via **`notifications/tools/list_changed`**

### 81. Veridian Legal Vault wants to add prompt packs for legal compliance docs. The MCP-compliant way is to ____. Ticket 3498: `notifications/roots/list_changed` ignored after folder add. [5.4 #81]

- **A.** Propagate tool failures as **MCP `isError:true` + `content[]` payload** plus JSON-RPC `-32603 Internal error` only for infrastructure faults
- **B.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs
- **C.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **D.** Defend **tool poisoning** by treating tool `description` as untrusted UI text, never executable instruction; validate schemas separately

### 82. Veridian Legal Vault MCP server for legal compliance docs is deployed as root container with `:latest`. The secure packaging is to ____. Audit 5475 flags `alg:none` token acceptance in staging. [5.4 #82]

- **A.** Enforce **per-origin permission prompts** and block tools from invoking higher-privileged tools via confused-deputy bridging
- **B.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **C.** Handle **localhost loopback redirects** (`http://127.0.0.1:{port}/callback`) securely for native Hosts to complete OAuth code flow without custom schemes
- **D.** Differentiate **MCP (client-hosted servers exposing tools/resources to any model)** from **function calling (model-bound API contracts)** and **A2A (agent-to-agent delegation)**

### 83. To implement legal compliance docs correctly for Veridian Legal Vault, which 4-step sequence satisfies the MCP spec? Audit 7073: auto-approve bypasses human consent for destructive tool. Scenario 5.5-4-83.

- **A.** Client trusts token from any issuer → skip RFC 9207 iss equality check → ignore RFC 7591 dynamic registration → reuse single token across all resource servers
- **B.** Server exposes `/.well-known/oauth-authorization-server` with PRM & CIMD → client fetches RS metadata with `resource` indicator (RFC 8707) → PKCE + state + RFC 9207 iss validation → audience-bound token issued per resource server
- **C.** Client sends static API key in Authorization header → server skips issuer discovery → accept tokens with alg:none → grant org-admin scope by default
- **D.** Server embeds client_secret in JS bundle → disable PKCE as optional → return tokens over plain HTTP → cache discovery doc forever without TLS

### 84. Proposed solution: To handle legal compliance docs, Veridian Legal Vault plans to skip issuer validation and accept bearer tokens from any alg:none issuer. Does this satisfy the MCP specification? Audit 6716: auto-approve bypasses human consent for destructive tool. [5.5 #84]

- **A.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **B.** Use **Elicitation for deterministic human field collection** and **Sampling for LLM-generated synthesis**; never conflate them
- **C.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)
- **D.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks

### 85. During legal compliance docs review at Veridian Legal Vault, the MCP server emits debug logs at `error` level. The proper level is ____. Log 3810: `prompt/get` uses client-side interpolation without validation. [5.5 #85]

- **A.** Detect **rug-pull** (post-approval tool logic mutation) via pinned `serverVersion`, hash pinning `tools/list` & re-consent on change
- **B.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **C.** Announce catalog churn via **`notifications/resources/list_changed`** so clients proactively re-list rather than polling
- **D.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets

---

## Domain 6 — SDKs, Deployment, Observability & Ecosystem (13–17% blueprint weight · 15 questions)

### 86. At Veridian Legal Vault, the MCP client code handling legal compliance docs leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Audit 6752: auto-approve bypasses human consent for destructive tool. Scenario 6.1-4-86.

- **A.** Exfiltrate tool arguments to third-party analytics silently → skip rate limiting on tool calls → omit provenance tags → hide tool calls from audit UI
- **B.** Pin server versions & verify registry signatures → isolate tool descriptions from executable logic → prompt user before first tool approval & high-risk actions → log tool provenance & monitor for description drift
- **C.** Install random GitHub MCP servers via curl|bash → grant full filesystem + network + env scopes → disable log redaction → store tokens in plaintext
- **D.** Auto-approve all tools without review → trust tool description text as system prompt → allow server to change tool logic post-approval → skip signature verification

### 87. Veridian Legal Vault MCP Host for legal compliance docs must handle `elicitation/create` versus chat parsing. Which is spec-correct? Log 4222: SSE stream without `eventId` loses progress on reconnect. [6.1 #87]

- **A.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**
- **B.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **C.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **D.** Negotiate response mode via **`Accept: application/json, text/event-stream`**; server chooses single JSON or SSE stream accordingly

### 88. The MCP Inspector highlights `____` as missing for legal compliance docs at Veridian Legal Vault. Which completion is spec-correct? Ticket 7992: plaintext `config.json` holds refresh token. [6.1 #88]

- **A.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **B.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets
- **C.** Build a Python server via **`mcp` (`FastMCP`, `@mcp.tool()`, `@mcp.resource()`)** with Pydantic-validated args and async lifespan
- **D.** Bind tokens to intended audiences via **RFC 8707 `resource` parameter** (`resource=https://mcp.example.com/mcp`) during authorization

### 89. Which two behaviors correctly describe MCP legal compliance docs handling at Veridian Legal Vault? Select two. Alert 5964: `progressToken` mismatch across concurrent tool calls. [6.2 #89]

- **A.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **B.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **C.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **D.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **E.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`

### 90. During legal compliance docs review at Veridian Legal Vault, the MCP server emits debug logs at `error` level. The proper level is ____. Alert 1241: `Mcp-Session-Id` reused across tenants. [6.2 #90]

- **A.** Request **least-privilege scopes** (`mcp:tools:read`, `mcp:resources:read`) and enforce per-tool scope checks server-side
- **B.** Support **RFC 7591 Dynamic Client Registration (DCR)** so Hosts auto-register as OAuth clients without manual developer portals
- **C.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **D.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle

### 91. The Veridian Legal Vault legal compliance docs Host caches `roots/list` forever and misses workspace changes. The fix is to ____. Ticket 1448: `notifications/roots/list_changed` ignored after folder add. [6.2 #91]

- **A.** Maintain strict **1 client : 1 server** association; Host may own many Clients, each bound to a single Server lifecycle
- **B.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **C.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **D.** Manage **`Mcp-Session-Id` header** (server-issued) for sticky session affinity across Streamable HTTP reconnects

### 92. The MCP Inspector highlights `____` as missing for legal compliance docs at Veridian Legal Vault. Which completion is spec-correct? Trace 2172: batch of 200 tool calls timed out. [6.3 #92]

- **A.** Specify **`modelPreferences`** (`hints` with name priority, `costPriority`, `speedPriority`, `intelligencePriority` 0–1) to steer client model routing
- **B.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **C.** Expose **Streamable HTTP at a single POST endpoint** (`/mcp`) accepting `application/json` or `text/event-stream` via `Accept` negotiation
- **D.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible

### 93. The Veridian Legal Vault MCP configuration for legal compliance docs shows `____`. Which entry correctly fills the slot for spec-compliant behavior? Ticket 1535: `roots/list` poll floods client every 10 ms. [6.3 #93]

- **A.** Bump **`protocolVersion` only for breaking framing/capability changes**; feature additions use optional capabilities to stay wire-compatible
- **B.** Mitigate **indirect prompt injection via tool/resource content** using `untrusted_source` provenance tags & output-side guardrails
- **C.** Serve **Client ID Metadata Document (CIMD, `https://client.example.com/.well-known/oauth-client`)** for client identity instead of static secrets
- **D.** Invoke **`elicitation/create`** (draft spec) to collect structured user input (form schema → `elicit` UI round-trip) with `requestedSchema`

### 94. At Veridian Legal Vault, the MCP client code handling legal compliance docs leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Case 5960: `structuredContent` missing despite `outputSchema` declared. [6.3 #94] through Cedar policy evaluation (variant delta 577). via PagerDuty escalation window (variant beta 912).

- **A.** Batch JSON-RPC requests only within **server-advertised `maxBatchSize`**; treat each response individually by `id` correlation
- **B.** Install only **registry-published, signed MCP servers** (`mcp-registry` with `server.json`, provenance attestation, publisher verification)
- **C.** Send **periodic `ping` every 30–60s** through Streamable HTTP/stdio to prune zombie sessions behind idle-unaware LBs
- **D.** Fulfill `resources/read` by returning **`contents[]` with `uri`, `mimeType`, `text`/`blob`** (base64 for binary) chunks

### 95. Which two logging/observability actions are correct for legal compliance docs MCP at Veridian Legal Vault? Select two. Ticket 1068: `notifications/roots/list_changed` ignored after folder add. [6.4 #95]

- **A.** Provide **argument autocompletion** via `completion/complete` for prompt args, resource URI templates, and enum tool params
- **B.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`
- **C.** Annotate tools with **`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`** to guide model risk decisions
- **D.** Instrument MCP with **OpenTelemetry GenAI + HTTP RPC spans** (`gen_ai.tool.name`, `rpc.method=tools/call`, `mcp.session.id`, latency/hit tags)
- **E.** Build a TS server via **`@modelcontextprotocol/sdk` (`McpServer`, `registerTool`, `registerResource`) with Zod schema validation**

### 96. For legal compliance docs, Veridian Legal Vault must enforce per-tool OAuth scope checks. Which scope design is correct? Trace 8550: `resource` audience binding missing per RFC 8707. [6.4 #96]

- **A.** Run **Inspector CLI in CI (`--cli --method tools/list --transport stdio`)** to gate PRs on MCP conformance without interactive UI
- **B.** Cancel in-flight requests cleanly via **`notifications/cancelled`** with `requestId` + `reason` instead of socket resets
- **C.** Reconnect Streamable HTTP with **exponential backoff with jitter** + `Last-Event-ID` + capability re-validation; respect `Retry-After`
- **D.** Emit **structured JSON logs** with `sessionId`, `requestId`, `toolName`, `durationMs`, redacted args hash, and `protocolVersion`

### 97. At Veridian Legal Vault, the MCP client code handling legal compliance docs leaves `____` unfilled. Which value correctly completes the JSON-RPC / capability field per spec? Incident 5263: OAuth PKCE verifier omitted for public client. [6.4 #97] with Snowflake zero-copy clone (variant delta 634). using Helm chart provenance (variant alpha 992).

- **A.** Issue **`ping`** heartbeats to detect half-open pipes and keep Streamable HTTP sessions alive under gateways
- **B.** Stream long-running work via **`notifications/progress`** with `progressToken` linked to originating request `id`
- **C.** Emit **redacted, append-only audit logs** for every `tools/call` (caller, tool, validated args hash, response hash, token sub/jti)
- **D.** Sandbox MCP servers with **least-privilege env/secrets scoping**: per-server env allowlist, no Host-level token passthrough by default

### 98. Select three correct MCP legal compliance docs behaviors that Veridian Legal Vault should enforce for its MCP fleet. Select three. Review 9926 notes `resources/list_changed` never fired after ingest. [6.5 #98]

- **A.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks
- **B.** Front fleet with **MCP-aware gateway/mesh** (auth termination, `Mcp-Session-Id` sticky load balancing, rate limiting, audit fan-out)
- **C.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes
- **D.** Subscribe to live resources via **`resources/subscribe`** and receive **`notifications/resources/updated`** on external change, paired with `unsubscribe`
- **E.** Place **auth-aware gateways/proxies** that forward `Mcp-Session-Id`, `Last-Event-ID`, and `Authorization` + preserve `Accept` negotiation
- **F.** Back prompt/resource argument typeahead with **`completion/complete`** returning `values[]` scoped to `ref` (prompt/resource) + `argument`

### 99. An external auditor flags that Veridian Legal Vault MCP deployment for legal compliance docs stores bearer tokens insecurely. The correction is to ____. Case 1411: `structuredContent` missing despite `outputSchema` declared. [6.5 #99]

- **A.** Bridge **MCP (tool/context attachment) + A2A (agent-to-agent task delegation)** via agent gateways that wrap MCP tools into A2A-managed tasks
- **B.** Validate **RFC 9207 `iss` claim** equality (issuer URL must exactly match `oauth-authorization-server` metadata) on every token
- **C.** Spawn **stdio servers** as child processes (stdin/stdout JSON-RPC lines, stderr logs), scoped to Host process lifecycle
- **D.** Use **`notifications/*`** for fire-and-forget signals (`initialized`, `progress`, `cancelled`) and **Requests** for `id`-tracked reply pairs

### 100. Complete the missing MCP field: In the Veridian Legal Vault legal compliance docs server, `____` must be set to the MCP-required value to enable legal compliance docs correctly. Alert 5781: `progressToken` mismatch across concurrent tool calls. [6.5 #100]

- **A.** Map server failures to **JSON-RPC error codes**: `Parse error -32700`, `Invalid Request -32600`, `Method not found -32601`, `Invalid params -32602`, `Internal error -32603`
- **B.** Signal prompt catalog updates via **`notifications/prompts/list_changed`** after admin curates new prompt packs
- **C.** Connect clients via **`Client` + transport (`StdioClientTransport`, `StreamableHTTPClientTransport`)** with explicit `initialize` + notification tracking
- **D.** Configure Hosts like **VS Code, Claude Desktop/Code, Cursor (`settings.json` / `claude_desktop_config.json`)** with declared `mcpServers` blocks, env allowlists, and auto-approve scopes

---

## Answer Key and Explanations

### Question 1 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). Selecting this honors Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model and prevents the listed failure mode in Veridian Legal Vault legal compliance docs flows. Reference 1.1 S4Q001. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Incorrect. reversing the initialize direction and mixing OAuth into initialize params conflates lifecycle with authorization.
- **B:** Incorrect. hardcoding protocol versions and duplicate initialize pings breaks forward compatibility and lifecycle idempotency.
- **C:** Incorrect. invoking tools before initialize negotiation bypasses version checks and omits the required initialized signal.
- **D:** Correct. follows MCP lifecycle spec: version/capability negotiation via initialize exchange completed by initialized notification before any feature calls.

### Question 2 — `A, C` (MCP Foundations, Architecture & Lifecycle)

Correct answers: A and C (are correct). This follows the MCP specification for Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 1.1 validation S4Q002. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Correct. clarifies layer boundaries: MCP standardizes context attachment; function calling is inline model schema; A2A negotiates task handoffs.
- **B:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **C:** Correct. enforces 1:1 Client-Server lifecycle so pings, cancellations and session IDs map unambiguously without multiplexing bugs.
- **D:** Incorrect. batching 200 unrelated tool calls into one HTTP request beyond advertised limits times out the whole batch.
- **E:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.

### Question 3 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). This follows the MCP specification for Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 1.1 validation S4Q003. [Skill 1.1: Distinguish Host, Client, and Server roles and the 1:1 Client-Server isolation model | Primary Reference: https://modelcontextprotocol.io/introduction | Additional Reference: https://modelcontextprotocol.io/docs/concepts/architecture]

- **A:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **B:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **C:** Correct. clarifies layer boundaries: MCP standardizes context attachment; function calling is inline model schema; A2A negotiates task handoffs.
- **D:** Incorrect. collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.

### Question 4 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). Selecting this honors Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake and prevents the listed failure mode in Veridian Legal Vault legal compliance docs flows. Skill 1.2 validation S4Q004. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **B:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.
- **C:** Correct. enables forwards-compatible evolution without breaking older Hosts or Servers on version skew.
- **D:** Incorrect. reimplementing a Postgres MCP server from scratch when a registry-verified one already exists wastes review cycles.

### Question 5 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). Selecting this honors Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake and prevents the listed failure mode in Veridian Legal Vault legal compliance docs flows. Skill 1.2 validation S4Q005. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Incorrect. distributing servers as raw GitHub tarballs without server.json or publisher proof hides supply-chain compromise.
- **B:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **C:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **D:** Correct. provides spec-guaranteed failure detection where OS TCP keepalives are invisible to application-level SSE/stdio proxies.

### Question 6 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). Per MCP 2025-11-25, Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 1.2 validation S4Q006. [Skill 1.2: Execute the initialize → capabilities negotiation → notifications/initialized lifecycle handshake | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/lifecycle/]

- **A:** Correct. provides spec-guaranteed failure detection where OS TCP keepalives are invisible to application-level SSE/stdio proxies.
- **B:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.
- **C:** Incorrect. collapsing Host and Server into one shared process erases isolation and lets untrusted servers read Host keychains.
- **D:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.

### Question 7 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). This follows the MCP specification for Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy, correcting the insecure/incompatible anti-pattern for legal compliance docs. Reference 1.3 S4Q007. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Incorrect. ad-hoc tool creation without validation and massive single-block responses break type safety and token budgets.
- **B:** Incorrect. missing inputSchema and raw shell interpolation from unvalidated LLM strings creates prompt-injection and RCE risk.
- **C:** Correct. matches MCP Tools spec: declarative schema, client discovery, validated execution, and structured content/error signaling.
- **D:** Incorrect. responding before validation and ignoring list_changed events leaves clients with stale, unvalidated tool catalogs.

### Question 8 — `B, C, E` (MCP Foundations, Architecture & Lifecycle)

Correct answers: B, C, and E (are correct). MCP 2025-11-25 requires Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy; the alternative breaks capability negotiation or security for legal compliance docs. Skill 1.3 validation S4Q008. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.
- **B:** Correct. separates best-effort telemetry from correlated RPC state per JSON-RPC 2.0, preventing notification ID collisions.
- **C:** Correct. adheres to the wire contract that underpins batching, cancellation, and error classification across both transports.
- **D:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.
- **E:** Correct. provides spec-guaranteed failure detection where OS TCP keepalives are invisible to application-level SSE/stdio proxies.
- **F:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.

### Question 9 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). This choice correctly implements Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy for Veridian Legal Vault while the distractors violate transport/session guarantees. Skill 1.3 validation S4Q009. [Skill 1.3: Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/]

- **A:** Correct. separates best-effort telemetry from correlated RPC state per JSON-RPC 2.0, preventing notification ID collisions.
- **B:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.
- **C:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.
- **D:** Incorrect. assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.

### Question 10 — `C, D` (MCP Foundations, Architecture & Lifecycle)

Correct answers: C and D (are correct). MCP 2025-11-25 requires Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging); the alternative breaks capability negotiation or security for legal compliance docs. Skill 1.4 validation S4Q010. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **B:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.
- **C:** Correct. allows safe iteration on draft specs like Tasks and elicitation without polluting the stable capability surface.
- **D:** Correct. lets each party call only negotiated features, avoiding methodNotFound and silent fallback hallucinations.
- **E:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.

### Question 11 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). Selecting this honors Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) and prevents the listed failure mode in Veridian Legal Vault legal compliance docs flows. Skill 1.4 validation S4Q011. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Correct. lets each party call only negotiated features, avoiding methodNotFound and silent fallback hallucinations.
- **B:** Incorrect. joining user input with path concatenation without canonicalization enables classic directory traversal.
- **C:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **D:** Incorrect. letting servers directly call external LLM APIs ignoring sampling delegation bypasses Host budget and audit controls.

### Question 12 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). This choice correctly implements Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) for Veridian Legal Vault while the distractors violate transport/session guarantees. Skill 1.4 validation S4Q012. [Skill 1.4: Advertise and gate features via capabilities objects (tools, resources, prompts, sampling, roots, logging) | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle]

- **A:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **B:** Correct. enables forwards-compatible evolution without breaking older Hosts or Servers on version skew.
- **C:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.
- **D:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.

### Question 13 — `A` (MCP Foundations, Architecture & Lifecycle)

Correct answer: A (is correct). This choice correctly implements Manage keepalive pings, progress notifications, cancellation, and shutdown semantics for Veridian Legal Vault while the distractors violate transport/session guarantees. Skill 1.5 validation S4Q013. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.
- **B:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.
- **C:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **D:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.

### Question 14 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). This follows the MCP specification for Manage keepalive pings, progress notifications, cancellation, and shutdown semantics, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 1.5 validation S4Q014. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.
- **B:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.
- **C:** Incorrect. treating MCP as a replacement for A2A agent discovery and task lifecycles conflates vertical tool attachment with peer delegation.
- **D:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.

### Question 15 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). This choice correctly implements Manage keepalive pings, progress notifications, cancellation, and shutdown semantics for Veridian Legal Vault while the distractors violate transport/session guarantees. Skill 1.5 validation S4Q015. [Skill 1.5: Manage keepalive pings, progress notifications, cancellation, and shutdown semantics | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/ping/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.
- **B:** Correct. enables UX-level typeahead without invoking costly tools, scoped to declared completion capabilities.
- **C:** Incorrect. presenting all files as templates with free-form interpolation forces models to guess required path variables.
- **D:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.

### Question 16 — `D` (MCP Foundations, Architecture & Lifecycle)

Correct answer: D (is correct). Per MCP 2025-11-25, Differentiate MCP from function calling, A2A, and experimental capability progression ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 1.6 validation S4Q016. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **B:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.
- **C:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.
- **D:** Correct. uses MCP vertically for capabilities and A2A horizontally for peer negotiation, per LM-Foundation AAIF stack guidance.

### Question 17 — `C` (MCP Foundations, Architecture & Lifecycle)

Correct answer: C (is correct). MCP 2025-11-25 requires Differentiate MCP from function calling, A2A, and experimental capability progression; the alternative breaks capability negotiation or security for legal compliance docs. Skill 1.6 validation S4Q017. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.
- **B:** Incorrect. labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.
- **C:** Correct. allows safe iteration on draft specs like Tasks and elicitation without polluting the stable capability surface.
- **D:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.

### Question 18 — `B` (MCP Foundations, Architecture & Lifecycle)

Correct answer: B (is correct). Per MCP 2025-11-25, Differentiate MCP from function calling, A2A, and experimental capability progression ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 1.6 validation S4Q018. [Skill 1.6: Differentiate MCP from function calling, A2A, and experimental capability progression | Primary Reference: https://modelcontextprotocol.io/docs/concepts/architecture | Additional Reference: https://a2a-protocol.org/latest/]

- **A:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **B:** Correct. clarifies layer boundaries: MCP standardizes context attachment; function calling is inline model schema; A2A negotiates task handoffs.
- **C:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.
- **D:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.

### Question 19 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). Selecting this honors Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints and prevents the listed failure mode in Veridian Legal Vault legal compliance docs flows. Reference 2.1 S4Q019. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. tight polling without subscription to list_changed notifications defeats MCP push efficiency and protocol layering.
- **B:** Incorrect. omitting uri and mimeType fields and ignoring pagination cursors makes resources unaddressable and unfilterable.
- **C:** Correct. follows Resources spec: capability advertisement, list/template discovery, uri-addressed reads with mime-typed contents and pagination.
- **D:** Incorrect. guessing URIs and exposing raw OS paths without scheme checks violates resource discovery and isolation.

### Question 20 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). Selecting this honors Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints and prevents the listed failure mode in Veridian Legal Vault legal compliance docs flows. Skill 2.1 validation S4Q020. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. gives models complete, machine-validated contracts for tool selection and argument generation.
- **B:** Incorrect. skipping Inspector and relying only on unit mocks misses real transport framing and pagination/cancellation bugs.
- **C:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **D:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.

### Question 21 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). This follows the MCP specification for Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 2.1 validation S4Q021. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. joining user input with path concatenation without canonicalization enables classic directory traversal.
- **B:** Correct. preserves user/model agency and auditability; every mutation traces to an explicit model decision with tool audit event.
- **C:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.
- **D:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.

### Question 22 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). This follows the MCP specification for Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 2.1 validation S4Q022. [Skill 2.1: Declare tools with name, title, description, inputSchema, outputSchema, and annotation hints | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/tools/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.
- **B:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.
- **C:** Correct. signals cost/safety posture without hard-coding policy; models prefer readOnly before destructive in multi-step plans.
- **D:** Incorrect. enabling experimental tasks by default without capability checks forces unready clients into breaking draft methods.

### Question 23 — `A, E` (Tools, Resources & Resource Templates)

Correct answers: A and E (are correct). This choice correctly implements Control model-controlled tool execution, list discovery, validation, and structured content output for Veridian Legal Vault while the distractors violate transport/session guarantees. Skill 2.2 validation S4Q023. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Correct. bridges LLM reasoning with downstream code that consumes validated JSON, not regex scraped prose.
- **B:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.
- **C:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **D:** Incorrect. reimplementing a Postgres MCP server from scratch when a registry-verified one already exists wastes review cycles.
- **E:** Correct. lets clients render multimodal results safely while distinguishing success from app-level errors without parsing text.

### Question 24 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). This follows the MCP specification for Control model-controlled tool execution, list discovery, validation, and structured content output, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 2.2 validation S4Q024. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **B:** Incorrect. batching 200 unrelated tool calls into one HTTP request beyond advertised limits times out the whole batch.
- **C:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.
- **D:** Correct. lets clients render multimodal results safely while distinguishing success from app-level errors without parsing text.

### Question 25 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). This choice correctly implements Control model-controlled tool execution, list discovery, validation, and structured content output for Veridian Legal Vault while the distractors violate transport/session guarantees. Skill 2.2 validation S4Q025. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Correct. bridges LLM reasoning with downstream code that consumes validated JSON, not regex scraped prose.
- **B:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **C:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **D:** Incorrect. implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.

### Question 26 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). MCP 2025-11-25 requires Control model-controlled tool execution, list discovery, validation, and structured content output; the alternative breaks capability negotiation or security for legal compliance docs. Skill 2.2 validation S4Q026. [Skill 2.2: Control model-controlled tool execution, list discovery, validation, and structured content output | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/tools]

- **A:** Incorrect. dumping base64 blobs as plain text without typed content blocks loses mimeType and forces heuristic parsing.
- **B:** Incorrect. logging full tool arguments including customer PII and bearer tokens creates GDPR and credential-leak second-order risks.
- **C:** Correct. bridges LLM reasoning with downstream code that consumes validated JSON, not regex scraped prose.
- **D:** Incorrect. implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.

### Question 27 — `A, E` (Tools, Resources & Resource Templates)

Correct answers: A and E (are correct). Selecting this honors Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed and prevents the listed failure mode in Veridian Legal Vault legal compliance docs flows. Skill 2.3 validation S4Q027. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Correct. keeps prompt pickers fresh without re-listing on every keystroke, matching resource/tool change notification pattern.
- **B:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **C:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.
- **D:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **E:** Correct. pushes freshness efficiently after external ingestion jobs create new datasets, without constant re-list overhead.

### Question 28 — `B` (Tools, Resources & Resource Templates)

Correct answer: B (is correct). This follows the MCP specification for Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 2.3 validation S4Q028. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. deploying greenfield on the deprecated dual-endpoint SSE transport incurs future migration cost and lacks session IDs.
- **B:** Correct. keeps prompt pickers fresh without re-listing on every keystroke, matching resource/tool change notification pattern.
- **C:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.
- **D:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.

### Question 29 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). MCP 2025-11-25 requires Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed; the alternative breaks capability negotiation or security for legal compliance docs. Skill 2.3 validation S4Q029. [Skill 2.3: Evolve tool catalogs dynamically via tools/list pagination and notifications/tools/list_changed | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.
- **B:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **C:** Correct. pushes freshness efficiently after external ingestion jobs create new datasets, without constant re-list overhead.
- **D:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.

### Question 30 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). Per MCP 2025-11-25, Address direct resources vs templated resources with URI schemes, names, and mimeTypes ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 2.4 validation S4Q030. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. models browse concrete resources via list and expand templates param by param without guessing URI syntax.
- **B:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.
- **C:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **D:** Incorrect. skipping Inspector and relying only on unit mocks misses real transport framing and pagination/cancellation bugs.

### Question 31 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). This follows the MCP specification for Address direct resources vs templated resources with URI schemes, names, and mimeTypes, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 2.4 validation S4Q031. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **B:** Incorrect. shipping servers as `:latest` root containers with host network and no healthcheck risks privilege escalation and silent hang.
- **C:** Incorrect. entrusting raw LLM strings to shell interpolation without inputSchema validation creates injection and RCE.
- **D:** Correct. models browse concrete resources via list and expand templates param by param without guessing URI syntax.

### Question 32 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). Per MCP 2025-11-25, Address direct resources vs templated resources with URI schemes, names, and mimeTypes ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 2.4 validation S4Q032. [Skill 2.4: Address direct resources vs templated resources with URI schemes, names, and mimeTypes | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. models browse concrete resources via list and expand templates param by param without guessing URI syntax.
- **B:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **C:** Incorrect. joining user input with path concatenation without canonicalization enables classic directory traversal.
- **D:** Incorrect. printing logs to stdout alongside JSON-RPC breaks line-delimited parsing and throws Parse error -32700.

### Question 33 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). Selecting this honors Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows and prevents the listed failure mode in Veridian Legal Vault legal compliance docs flows. Reference 2.5 S4Q033. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. letting servers dictate client filesystem boundaries inverts MCP trust and breaks host isolation.
- **B:** Incorrect. exposing full drive without consent and walking above root boundaries with symlink following enables directory traversal.
- **C:** Incorrect. hardcoding roots and ignoring list_changed notifications leaves stale boundaries after user permission changes.
- **D:** Correct. implements Roots spec: client-owned boundary declaration, server-enforced confinement, and dynamic list_changed handling.

### Question 34 — `D, E` (Tools, Resources & Resource Templates)

Correct answers: D and E (are correct). MCP 2025-11-25 requires Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows; the alternative breaks capability negotiation or security for legal compliance docs. Skill 2.5 validation S4Q034. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **B:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **C:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **D:** Correct. pushes freshness efficiently after external ingestion jobs create new datasets, without constant re-list overhead.
- **E:** Correct. delivers typed content blocks that render correctly in Host UIs with binary vs text handling pre-decided by mimeType.

### Question 35 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). Selecting this honors Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows and prevents the listed failure mode in Veridian Legal Vault legal compliance docs flows. Skill 2.5 validation S4Q035. [Skill 2.5: Paginate, read, and subscribe to resources via list, read, subscribe, and list_changed flows | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/resources/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/resources]

- **A:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.
- **B:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.
- **C:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **D:** Correct. pushes freshness efficiently after external ingestion jobs create new datasets, without constant re-list overhead.

### Question 36 — `D` (Tools, Resources & Resource Templates)

Correct answer: D (is correct). MCP 2025-11-25 requires Declare prompts and completions for argument typeahead and parameterized prompt expansion; the alternative breaks capability negotiation or security for legal compliance docs. Skill 2.6 validation S4Q036. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **B:** Incorrect. setting includeContext=allServers by default fans sensitive data from every connected server into one sampling call.
- **C:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.
- **D:** Correct. turns curated prompt packs into discoverable UX shortcuts argument-by-argument with typed validation.

### Question 37 — `A` (Tools, Resources & Resource Templates)

Correct answer: A (is correct). Per MCP 2025-11-25, Declare prompts and completions for argument typeahead and parameterized prompt expansion ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 2.6 validation S4Q037. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. keeps prompt pickers fresh without re-listing on every keystroke, matching resource/tool change notification pattern.
- **B:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.
- **C:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **D:** Incorrect. deploying greenfield on the deprecated dual-endpoint SSE transport incurs future migration cost and lacks session IDs.

### Question 38 — `C` (Tools, Resources & Resource Templates)

Correct answer: C (is correct). This choice correctly implements Declare prompts and completions for argument typeahead and parameterized prompt expansion for Veridian Legal Vault while the distractors violate transport/session guarantees. Skill 2.6 validation S4Q038. [Skill 2.6: Declare prompts and completions for argument typeahead and parameterized prompt expansion | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/completion/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.
- **B:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **C:** Correct. powers low-latency autocomplete dropdowns directly from server-side datasets without tool execution overhead.
- **D:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.

### Question 39 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). This choice correctly implements Expose and expand prompts via prompts/list, prompts/get, and argument validation for Veridian Legal Vault while the distractors violate transport/session guarantees. Skill 3.1 validation S4Q039. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.
- **B:** Correct. powers low-latency autocomplete dropdowns directly from server-side datasets without tool execution overhead.
- **C:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.
- **D:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.

### Question 40 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). MCP 2025-11-25 requires Expose and expand prompts via prompts/list, prompts/get, and argument validation; the alternative breaks capability negotiation or security for legal compliance docs. Skill 3.1 validation S4Q040. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.
- **B:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **C:** Incorrect. assuming all peers support every method without checking capabilities triggers routine 32601 errors in the fleet.
- **D:** Correct. powers low-latency autocomplete dropdowns directly from server-side datasets without tool execution overhead.

### Question 41 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). This follows the MCP specification for Expose and expand prompts via prompts/list, prompts/get, and argument validation, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 3.1 validation S4Q041. [Skill 3.1: Expose and expand prompts via prompts/list, prompts/get, and argument validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/prompts/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. exposing every MCP server directly to the internet without gateway authZ or rate limiting multiplies attack surface.
- **B:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.
- **C:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.
- **D:** Correct. keeps prompt pickers fresh without re-listing on every keystroke, matching resource/tool change notification pattern.

### Question 42 — `A, C` (Prompts, Sampling, Roots & Elicitation)

Correct answers: A and C (are correct). This choice correctly implements Enforce client-owned filesystem boundaries via roots/list and roots/list_changed for Veridian Legal Vault while the distractors violate transport/session guarantees. Skill 3.2 validation S4Q042. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. keeps server views consistent when users add/remove workspace folders mid-session without restart.
- **B:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.
- **C:** Correct. prevents `../` and symlink hop attacks that would escape the user’s approved `file://` allowlist.
- **D:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **E:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.

### Question 43 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). This follows the MCP specification for Enforce client-owned filesystem boundaries via roots/list and roots/list_changed, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 3.2 validation S4Q043. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. keeps server views consistent when users add/remove workspace folders mid-session without restart.
- **B:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **C:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **D:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.

### Question 44 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). Per MCP 2025-11-25, Enforce client-owned filesystem boundaries via roots/list and roots/list_changed ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 3.2 validation S4Q044. [Skill 3.2: Enforce client-owned filesystem boundaries via roots/list and roots/list_changed | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/roots/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. prevents `../` and symlink hop attacks that would escape the user’s approved `file://` allowlist.
- **B:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **C:** Incorrect. disabling tracing for MCP tool calls and tracking only final LLM latency hides 80% of P95 tail from gateway/session queuing.
- **D:** Incorrect. forcing downstream apps to parse natural-language tool summaries instead of structuredContent rebuilds brittle extractors.

### Question 45 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). This follows the MCP specification for Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 3.3 validation S4Q045. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. using bare filesystem paths without URI schemes leaks OS layout and prevents scheme-aware policy enforcement.
- **B:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.
- **C:** Incorrect. reimplementing a Postgres MCP server from scratch when a registry-verified one already exists wastes review cycles.
- **D:** Correct. maps server intent to Host model fleet tiers without hardcoding vendor model IDs into server code.

### Question 46 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). This follows the MCP specification for Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 3.3 validation S4Q046. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. trusting approved servers forever without version/hash re-validation lets a compromised update hijack tool semantics.
- **B:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.
- **C:** Incorrect. omitting event IDs on streamed notifications makes reconnection blind to missed progress and list_changed pushes.
- **D:** Correct. limits what prior server context flows into delegated sampling calls, preventing cross-server data exfiltration.

### Question 47 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). Per MCP 2025-11-25, Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 3.3 validation S4Q047. [Skill 3.3: Delegate LLM work via sampling/createMessage with modelPreferences and includeContext controls | Primary Reference: https://spec.modelcontextprotocol.io/specification/client/sampling/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **B:** Correct. limits what prior server context flows into delegated sampling calls, preventing cross-server data exfiltration.
- **C:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **D:** Incorrect. requiring clients to poll list on a timer to detect new resources defeats MCP push efficiency.

### Question 48 — `A` (Prompts, Sampling, Roots & Elicitation)

Correct answer: A (is correct). This choice correctly implements Collect human input via elicitation/create with requestedSchema and form round-trips for Veridian Legal Vault while the distractors violate transport/session guarantees. Reference 3.4 S4Q048. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. follows Sampling spec: capability-checked server-initiated LLM delegation with explicit modelPreferences and human approval gating.
- **B:** Incorrect. default-exposed sampling and uncapped recursive loops risk token runaway and expose internal reasoning inappropriately.
- **C:** Incorrect. unbounded PII-laden sampling without capability or consent bypasses privacy and authorization boundaries.
- **D:** Incorrect. confusing sampling payloads with tool metadata conflates delegation layers and breaks cost attribution.

### Question 49 — `A, C` (Prompts, Sampling, Roots & Elicitation)

Correct answers: A and C (are correct). Selecting this honors Collect human input via elicitation/create with requestedSchema and form round-trips and prevents the listed failure mode in Veridian Legal Vault legal compliance docs flows. Skill 3.4 validation S4Q049. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. lets servers delegate LLM sub-tasks (summarization, critique) back to the Host model under explicit preference caps.
- **B:** Incorrect. dumping base64 blobs as plain text without typed content blocks loses mimeType and forces heuristic parsing.
- **C:** Correct. turns server data needs into typed Host-rendered forms rather than chat text parsing, with explicit schema validation.
- **D:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **E:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.

### Question 50 — `D` (Prompts, Sampling, Roots & Elicitation)

Correct answer: D (is correct). This follows the MCP specification for Collect human input via elicitation/create with requestedSchema and form round-trips, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 3.4 validation S4Q050. [Skill 3.4: Collect human input via elicitation/create with requestedSchema and form round-trips | Primary Reference: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.
- **B:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **C:** Incorrect. labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.
- **D:** Correct. turns server data needs into typed Host-rendered forms rather than chat text parsing, with explicit schema validation.

### Question 51 — `D, E` (Prompts, Sampling, Roots & Elicitation)

Correct answers: D and E (are correct). MCP 2025-11-25 requires Regulate verbosity via logging/setLevel and notifications/message level filtering; the alternative breaks capability negotiation or security for legal compliance docs. Skill 3.5 validation S4Q051. [Skill 3.5: Regulate verbosity via logging/setLevel and notifications/message level filtering | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/logging/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.
- **B:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.
- **C:** Incorrect. batching 200 unrelated tool calls into one HTTP request beyond advertised limits times out the whole batch.
- **D:** Correct. respects user-selected verbosity while still flowing warnings/errors through observability pipelines.
- **E:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.

### Question 52 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). This follows the MCP specification for Regulate verbosity via logging/setLevel and notifications/message level filtering, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 3.5 validation S4Q052. [Skill 3.5: Regulate verbosity via logging/setLevel and notifications/message level filtering | Primary Reference: https://spec.modelcontextprotocol.io/specification/server/utilities/logging/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **B:** Correct. gives UX feedback without blocking the JSON-RPC response while preserving correlation via progressToken.
- **C:** Incorrect. parsing free-form chat replies as structured data instead of typed elicitation invites format errors and injection.
- **D:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.

### Question 53 — `C` (Prompts, Sampling, Roots & Elicitation)

Correct answer: C (is correct). MCP 2025-11-25 requires Correlate progress and completion flows with progressToken and completion/complete semantics; the alternative breaks capability negotiation or security for legal compliance docs. Skill 3.6 validation S4Q053. [Skill 3.6: Correlate progress and completion flows with progressToken and completion/complete semantics | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/prompts]

- **A:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.
- **B:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **C:** Correct. correlates streaming progress notifications to the correct in-flight tool/resource fetch without guessing.
- **D:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.

### Question 54 — `B` (Prompts, Sampling, Roots & Elicitation)

Correct answer: B (is correct). Per MCP 2025-11-25, Correlate progress and completion flows with progressToken and completion/complete semantics ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 3.6 validation S4Q054. [Skill 3.6: Correlate progress and completion flows with progressToken and completion/complete semantics | Primary Reference: https://modelcontextprotocol.io/specification/2025-11-25 | Additional Reference: https://modelcontextprotocol.io/docs/concepts/prompts]

- **A:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.
- **B:** Correct. enables UX-level typeahead without invoking costly tools, scoped to declared completion capabilities.
- **C:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.
- **D:** Incorrect. logging full tool arguments including customer PII and bearer tokens creates GDPR and credential-leak second-order risks.

### Question 55 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). MCP 2025-11-25 requires Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle; the alternative breaks capability negotiation or security for legal compliance docs. Skill 4.1 validation S4Q055. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.
- **B:** Incorrect. scattering tool handlers as raw dict callbacks without FastMCP decorators or lifespan context leaks teardown resources.
- **C:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **D:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.

### Question 56 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). This follows the MCP specification for Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 4.1 validation S4Q056. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.
- **B:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.
- **C:** Incorrect. wrapping payloads in bare JSON without jsonrpc/id/method fields defeats MCP parser validation and cancellation correlation.
- **D:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.

### Question 57 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). MCP 2025-11-25 requires Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle; the alternative breaks capability negotiation or security for legal compliance docs. Skill 4.1 validation S4Q057. [Skill 4.1: Operate stdio transport (stdin/stdout JSON-RPC, stderr logs) and child-process lifecycle | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://github.com/modelcontextprotocol/specification]

- **A:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **B:** Correct. prevents log interleaving from corrupting JSON-RPC framing that parsers expect line-delimited on stdout.
- **C:** Incorrect. caching roots forever and ignoring list_changed leaves newly granted workspaces invisible and revoked ones writable.
- **D:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.

### Question 58 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). This follows the MCP specification for Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response), correcting the insecure/incompatible anti-pattern for legal compliance docs. Reference 4.2 S4Q058. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. matches 2025-11-25 Streamable HTTP spec: single endpoint, dual Accept, session ID management, and resumable SSE stream option.
- **B:** Incorrect. splitting endpoints and ignoring session/resumability headers reverts to pre-March 2025 deprecated SSE transport.
- **C:** Incorrect. unbounded batching and cross-tenant session ID reuse breaks rate limiting and tenant isolation guarantees.
- **D:** Incorrect. returning HTML instead of JSON-RPC errors and retrying without backoff causes parsing failures and duplicate mutations.

### Question 59 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). Per MCP 2025-11-25, Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 4.2 validation S4Q059. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **B:** Incorrect. printing logs to stdout alongside JSON-RPC breaks line-delimited parsing and throws Parse error -32700.
- **C:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.
- **D:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.

### Question 60 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). This follows the MCP specification for Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response), correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 4.2 validation S4Q060. [Skill 4.2: Operate Streamable HTTP transport (single POST endpoint, Accept negotiation, SSE or JSON response) | Primary Reference: https://modelcontextprotocol.io/docs/concepts/transports | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Correct. lets simple request/reply skip SSE overhead while enabling streaming only for long-running tool progress.
- **B:** Incorrect. doing client-side string interpolation of prompts without server validation reintroduces prompt injection via crafted args.
- **C:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **D:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.

### Question 61 — `A, E` (Transports, Sessions & Protocol Evolution)

Correct answers: A and E (are correct). MCP 2025-11-25 requires Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay; the alternative breaks capability negotiation or security for legal compliance docs. Skill 4.3 validation S4Q061. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Correct. avoids thundering herds after gateway restarts while ensuring exactly-once progress recovery via resumability.
- **B:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **C:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **D:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.
- **E:** Correct. tracks spec evolution: split GET /sse + POST /messages merged into single POST with Accept-driven streaming.

### Question 62 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). This follows the MCP specification for Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 4.3 validation S4Q062. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Correct. recovers progress streams and notifications lost during 5–30s mobile handoffs without missing tool progress events.
- **B:** Incorrect. enabling experimental tasks by default without capability checks forces unready clients into breaking draft methods.
- **C:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.
- **D:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.

### Question 63 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). MCP 2025-11-25 requires Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay; the alternative breaks capability negotiation or security for legal compliance docs. Skill 4.3 validation S4Q063. [Skill 4.3: Manage session affinity and resumability via Mcp-Session-Id and Last-Event-ID replay | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/transports/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports]

- **A:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.
- **B:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.
- **C:** Correct. recovers progress streams and notifications lost during 5–30s mobile handoffs without missing tool progress events.
- **D:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.

### Question 64 — `A, C, D` (Transports, Sessions & Protocol Evolution)

Correct answers: A, C, and D (are correct). This follows the MCP specification for Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 4.4 validation S4Q064. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Correct. avoids thundering herds after gateway restarts while ensuring exactly-once progress recovery via resumability.
- **B:** Incorrect. having servers push tool executions without model initiation undermines approval and provenance guarantees.
- **C:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.
- **D:** Correct. tracks spec evolution: split GET /sse + POST /messages merged into single POST with Accept-driven streaming.
- **E:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **F:** Incorrect. hardcoding token endpoints and scopes per server creates config drift when auth servers rotate URLs.

### Question 65 — `A` (Transports, Sessions & Protocol Evolution)

Correct answer: A (is correct). This follows the MCP specification for Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 4.4 validation S4Q065. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.
- **B:** Incorrect. calling tools before the initialized handshake completes races capability discovery and throws methodNotFound errors.
- **C:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.
- **D:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.

### Question 66 — `B` (Transports, Sessions & Protocol Evolution)

Correct answer: B (is correct). This follows the MCP specification for Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 4.4 validation S4Q066. [Skill 4.4: Migrate from deprecated HTTP+SSE dual endpoint (pre-2025-03-26) to Streamable HTTP | Primary Reference: https://github.com/modelcontextprotocol/specification | Additional Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports/sse/]

- **A:** Incorrect. reimplementing a Postgres MCP server from scratch when a registry-verified one already exists wastes review cycles.
- **B:** Correct. unifies remote MCP to one well-known endpoint per 2025-11-25 spec, eliminating the split SSE/POST dual-endpoint of 2024.
- **C:** Incorrect. parsing free-form chat replies as structured data instead of typed elicitation invites format errors and injection.
- **D:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.

### Question 67 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). This follows the MCP specification for Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 4.5 validation S4Q067. [Skill 4.5: Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/progress/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. editing Host configs manually per developer without schema validation introduces drift and silent capability disablement.
- **B:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.
- **C:** Incorrect. bumping protocolVersion for every tool addition forces all Hosts to re-handshake hourly and breaks rolling upgrades.
- **D:** Correct. survives AWS ALB 60s idle timeout and Kubernetes GFE that silently drops idle SSE streams.

### Question 68 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). MCP 2025-11-25 requires Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation; the alternative breaks capability negotiation or security for legal compliance docs. Skill 4.5 validation S4Q068. [Skill 4.5: Re-establish sessions with exponential backoff, jitter, Retry-After, and capability re-validation | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/progress/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.
- **B:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **C:** Correct. keeps MCP semantics intact through enterprise L7 filters that otherwise strip SSE headers and session sticky state.
- **D:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.

### Question 69 — `C` (Transports, Sessions & Protocol Evolution)

Correct answer: C (is correct). MCP 2025-11-25 requires Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival; the alternative breaks capability negotiation or security for legal compliance docs. Skill 4.6 validation S4Q069. [Skill 4.6: Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/cancellation/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.
- **B:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **C:** Correct. exploits batching for listing throughput without overwhelming server concurrency caps or mixing response IDs.
- **D:** Incorrect. hardcoding a single protocolVersion forever blocks new capabilities and breaks mixed-version fleets.

### Question 70 — `D` (Transports, Sessions & Protocol Evolution)

Correct answer: D (is correct). Per MCP 2025-11-25, Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 4.6 validation S4Q070. [Skill 4.6: Tune batching, gateway interop, and ping keepalives for L7 proxy and idle-timeout survival | Primary Reference: https://spec.modelcontextprotocol.io/specification/basic/utilities/cancellation/ | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25]

- **A:** Incorrect. letting servers self-declare their own roots and trust them ignores user consent and breaks host sandboxing.
- **B:** Incorrect. skipping Inspector and relying only on unit mocks misses real transport framing and pagination/cancellation bugs.
- **C:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **D:** Correct. keeps MCP semantics intact through enterprise L7 filters that otherwise strip SSE headers and session sticky state.

### Question 71 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). This choice correctly implements Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata for Veridian Legal Vault while the distractors violate transport/session guarantees. Skill 5.1 validation S4Q071. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.
- **B:** Correct. aligns MCP with current OAuth 2.1 security posture, eliminating token leakage vectors of legacy grants.
- **C:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.
- **D:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.

### Question 72 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). Selecting this honors Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata and prevents the listed failure mode in Veridian Legal Vault legal compliance docs flows. Skill 5.1 validation S4Q072. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Incorrect. writing refresh_token to world-readable JSON config and logging Authorization headers exposes long-lived credentials.
- **B:** Correct. enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.
- **C:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.
- **D:** Incorrect. stuffing every system prompt variant into tool descriptions instead of dedicated prompts mixes layers.

### Question 73 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). Selecting this honors Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata and prevents the listed failure mode in Veridian Legal Vault legal compliance docs flows. Skill 5.1 validation S4Q073. [Skill 5.1: Discover OAuth endpoints via Protected Resource Metadata and Authorization Server Metadata | Primary Reference: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization | Additional Reference: https://datatracker.ietf.org/doc/html/rfc7591]

- **A:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.
- **B:** Correct. enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.
- **C:** Incorrect. labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.
- **D:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.

### Question 74 — `A, D` (Authorization, Security, Trust & Registry)

Correct answers: A and D (are correct). This choice correctly implements Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings for Veridian Legal Vault while the distractors violate transport/session guarantees. Skill 5.2 validation S4Q074. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Correct. aligns MCP with current OAuth 2.1 security posture, eliminating token leakage vectors of legacy grants.
- **B:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **C:** Incorrect. copying untrusted tool descriptions directly into system instructions executes attacker-supplied prompt injection.
- **D:** Correct. binds public client identity to TLS-verifiable origin without long-lived client secrets in distributed Hosts.
- **E:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.

### Question 75 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). MCP 2025-11-25 requires Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings; the alternative breaks capability negotiation or security for legal compliance docs. Skill 5.2 validation S4Q075. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **B:** Incorrect. ignoring nextCursor and assuming one page silently drops 90% of resources in large repos.
- **C:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.
- **D:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.

### Question 76 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). Selecting this honors Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings and prevents the listed failure mode in Veridian Legal Vault legal compliance docs flows. Skill 5.2 validation S4Q076. [Skill 5.2: Implement OAuth 2.1 authorization_code + PKCE with loopback callbacks and CIMD bindings | Primary Reference: https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12 | Additional Reference: https://datatracker.ietf.org/doc/html/rfc9207]

- **A:** Incorrect. forcing stdio over the internet or Streamable HTTP for a localhost Python subprocess inverts isolation and latency trade-offs.
- **B:** Incorrect. parsing free-form chat replies as structured data instead of typed elicitation invites format errors and injection.
- **C:** Correct. keeps refresh tokens survivable across restarts but invisible to process dumps, forked children, and leaked logs.
- **D:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.

### Question 77 — `B, E` (Authorization, Security, Trust & Registry)

Correct answers: B and E (are correct). Per MCP 2025-11-25, Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 5.3 validation S4Q077. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.
- **B:** Correct. enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.
- **C:** Incorrect. reimplementing a Postgres MCP server from scratch when a registry-verified one already exists wastes review cycles.
- **D:** Incorrect. declaring tools with only a name string and no JSON Schema forces models to hallucinate argument shapes.
- **E:** Correct. blocks mix-up attacks where a malicious authorization server mints tokens that victim servers would otherwise accept.

### Question 78 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). Per MCP 2025-11-25, Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 5.3 validation S4Q078. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.
- **B:** Incorrect. using OAuth implicit flow in a single-page host leaks access tokens via URL fragment to referrers and logs.
- **C:** Correct. binds public client identity to TLS-verifiable origin without long-lived client secrets in distributed Hosts.
- **D:** Incorrect. letting any MCP tool call any other origin’s tool without separate user consent chains low-privilege to high-privilege actions.

### Question 79 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). Per MCP 2025-11-25, Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 5.3 validation S4Q079. [Skill 5.3: Audience-bind tokens via RFC 8707 resource indicator and validate RFC 9207 iss equality | Primary Reference: https://datatracker.ietf.org/doc/html/rfc8707 | Additional Reference: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization]

- **A:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.
- **B:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **C:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **D:** Correct. enables automatic discovery of scopes, token endpoints, and issuer URLs without hardcoding per server.

### Question 80 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). This choice correctly implements Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model for Veridian Legal Vault while the distractors violate transport/session guarantees. Skill 5.4 validation S4Q080. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Incorrect. joining user input with path concatenation without canonicalization enables classic directory traversal.
- **B:** Correct. forces re-approval when a benign `get_weather` server silently rewires to `exfiltrate_files` after approval.
- **C:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.
- **D:** Incorrect. returning a one-shot 500-tool dump without pagination cursors truncates discovery under default page limits.

### Question 81 — `D` (Authorization, Security, Trust & Registry)

Correct answer: D (is correct). MCP 2025-11-25 requires Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model; the alternative breaks capability negotiation or security for legal compliance docs. Skill 5.4 validation S4Q081. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Incorrect. throwing JSON-RPC errors for every business-logic rejection confuses client retry logic that should handle isError instead.
- **B:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.
- **C:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **D:** Correct. displays descriptions for human review but never concatenates them into system prompts or plan steps as trusted policy.

### Question 82 — `A` (Authorization, Security, Trust & Registry)

Correct answer: A (is correct). MCP 2025-11-25 requires Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model; the alternative breaks capability negotiation or security for legal compliance docs. Skill 5.4 validation S4Q082. [Skill 5.4: Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://github.com/modelcontextprotocol/registry]

- **A:** Correct. stops a docs MCP server from using its tool output to call a payment MCP’s `transfer` tool via implicit ambient authority.
- **B:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **C:** Incorrect. allowing arbitrary redirect_uri without loopback validation lets attackers steal authorization codes via open redirector.
- **D:** Incorrect. treating MCP as synonymous with function calling conflates external capability hosting with inline model schema binding.

### Question 83 — `B` (Authorization, Security, Trust & Registry)

Correct answer: B (is correct). This follows the MCP specification for Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging, correcting the insecure/incompatible anti-pattern for legal compliance docs. Reference 5.5 S4Q083. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Incorrect. reusing a single audience-less token across resource servers enables cross-server token replay and mix-up attacks.
- **B:** Correct. follows MCP auth spec evolution: OAuth 2.1 with PKCE, protected resource metadata, RFC 8707 audience binding, and RFC 9207 issuer checks.
- **C:** Incorrect. hardcoded keys and alg:none tokens with blanket admin grants violate OAuth 2.1 and privilege separation.
- **D:** Incorrect. exposing secrets in client bundles and downgrading PKCE/TLS undermines OAuth confidentiality and channel binding.

### Question 84 — `C` (Authorization, Security, Trust & Registry)

Correct answer: C (is correct). Per MCP 2025-11-25, Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 5.5 validation S4Q084. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **B:** Incorrect. asking the LLM to guess a user’s address via sampling instead of eliciting it via form bakes hallucinations into identity.
- **C:** Correct. enables post-incident forensics without persisting PII/tokens, keyed by stable tool provenance hashes.
- **D:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.

### Question 85 — `A` (Authorization, Security, Trust & Registry)

Correct answer: A (is correct). MCP 2025-11-25 requires Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging; the alternative breaks capability negotiation or security for legal compliance docs. Skill 5.5 validation S4Q085. [Skill 5.5: Establish supply-chain trust via MCP Registry signatures, sandboxing, and redacted audit logging | Primary Reference: https://genai.owasp.org/resource/mcp-security-checklist/ | Additional Reference: https://genai.owasp.org/]

- **A:** Correct. forces re-approval when a benign `get_weather` server silently rewires to `exfiltrate_files` after approval.
- **B:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **C:** Incorrect. requiring clients to poll list on a timer to detect new resources defeats MCP push efficiency.
- **D:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.

### Question 86 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). This choice correctly implements Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) for Veridian Legal Vault while the distractors violate transport/session guarantees. Reference 6.1 S4Q086. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Incorrect. silent exfiltration without rate limits or audit visibility breaks data minimization and incident-response traceability.
- **B:** Correct. applies MCP security checklist: supply-chain pinning, description-vs-logic separation, consent gating, and provenance monitoring against poison/rug-pull.
- **C:** Incorrect. unvetted curl-piped installs with maximal scopes and plaintext token storage maximizes blast radius from a single malicious server.
- **D:** Incorrect. blind auto-approval and treating descriptions as trusted instructions invites prompt injection and supply-chain compromise.

### Question 87 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). This choice correctly implements Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) for Veridian Legal Vault while the distractors violate transport/session guarantees. Skill 6.1 validation S4Q087. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Correct. uses typed server helpers that auto-wire tools/list/call handlers and JSON Schema validation from Zod objects.
- **B:** Incorrect. labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.
- **C:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.
- **D:** Incorrect. forcing every response through SSE with event IDs when a single JSON object suffices adds latency and parser load.

### Question 88 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). Per MCP 2025-11-25, Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 6.1 validation S4Q088. [Skill 6.1: Build servers with TypeScript SDK (McpServer + Zod) and Python SDK (FastMCP + Pydantic) | Primary Reference: https://github.com/modelcontextprotocol/typescript-sdk | Additional Reference: https://github.com/modelcontextprotocol/python-sdk]

- **A:** Incorrect. labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.
- **B:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.
- **C:** Correct. gives decorator-ergonomic tool/resource registration with Pydantic/JSON Schema coherence across Python Hosts.
- **D:** Incorrect. issuing audience-less bearer tokens replays a calendar token against the payment MCP server undetected.

### Question 89 — `A, B` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: A and B (are correct). This choice correctly implements Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates for Veridian Legal Vault while the distractors violate transport/session guarantees. Skill 6.2 validation S4Q089. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Correct. gives OS-level isolation, clean env var scoping, and automatic teardown when Host exits without port conflicts.
- **B:** Correct. automates protocol conformance as a PR check alongside lint/tests, proving list/call contracts headlessly.
- **C:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.
- **D:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **E:** Incorrect. logging only free-text “tool executed” lines without session/request correlation destroys per-tool SLI computation.

### Question 90 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). Per MCP 2025-11-25, Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 6.2 validation S4Q090. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Incorrect. bundling `admin:write` into every MCP scope grant turns a docs reader into a payment mutator after single consent.
- **B:** Incorrect. requiring manual OAuth client registration per Host instance blocks enterprise auto-scaling and CI ephemerals.
- **C:** Correct. gives OS-level isolation, clean env var scoping, and automatic teardown when Host exits without port conflicts.
- **D:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.

### Question 91 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). This choice correctly implements Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates for Veridian Legal Vault while the distractors violate transport/session guarantees. Skill 6.2 validation S4Q091. [Skill 6.2: Validate interactively and in CI via Inspector UI and Inspector CLI conformance gates | Primary Reference: https://github.com/modelcontextprotocol/inspector | Additional Reference: https://modelcontextprotocol.io/introduction]

- **A:** Incorrect. multiplexing many servers over one Client socket mixes session IDs and cancellation scopes across origins.
- **B:** Correct. automates protocol conformance as a PR check alongside lint/tests, proving list/call contracts headlessly.
- **C:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.
- **D:** Incorrect. generating a new random session ID per request loses pagination state and forces full re-handshake each call.

### Question 92 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). This follows the MCP specification for Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 6.3 validation S4Q092. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Incorrect. hardcoding `claude-3-opus` in server logic breaks portability when the Host swaps fleet to a local model.
- **B:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **C:** Incorrect. keeping separate `/sse` and `/messages` endpoints perpetuates the deprecated March 2025 SSE transport.
- **D:** Correct. keeps patch/minor server releases compatible with older Hosts that simply ignore unknown capabilities.

### Question 93 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). Per MCP 2025-11-25, Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 6.3 validation S4Q093. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Correct. keeps patch/minor server releases compatible with older Hosts that simply ignore unknown capabilities.
- **B:** Incorrect. feeding untrusted web fetches from an MCP resource straight into system context as facts executes embedded tool hijacks.
- **C:** Incorrect. embedding static client_secret in shipped desktop binaries leaks secrets via binary extraction and cannot rotate cleanly.
- **D:** Incorrect. parsing free-form chat replies as structured data instead of typed elicitation invites format errors and injection.

### Question 94 — `B` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: B (is correct). This follows the MCP specification for Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 6.3 validation S4Q094. [Skill 6.3: Publish versioned, signed servers to the MCP Registry with server.json and provenance attestation | Primary Reference: https://modelcontextprotocol.io/docs/tools/inspector | Additional Reference: https://modelcontextprotocol.io/docs/develop/build-server]

- **A:** Incorrect. batching 200 unrelated tool calls into one HTTP request beyond advertised limits times out the whole batch.
- **B:** Correct. provides supply-chain tamper evidence via package signing and publisher identity beyond raw GitHub stars.
- **C:** Incorrect. relying on TCP keepalive alone lets L7 gateways reap idle SSE streams after 60s with no client notification.
- **D:** Incorrect. returning raw file bytes without contents envelope/mimeType forces Hosts to sniff codecs and breaks rendering.

### Question 95 — `B, D` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: B and D (are correct). Selecting this honors Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation and prevents the listed failure mode in Veridian Legal Vault legal compliance docs flows. Skill 6.4 validation S4Q095. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Incorrect. implementing completions as tool calls forces side-effecting invocations just for dropdown suggestions.
- **B:** Correct. powers per-tool SLOs and supply-chain forensics without persisting sensitive tool argument values.
- **C:** Incorrect. labeling a wallet-drain tool as readOnlyHint=true tricks the model into auto-executing irreversible payments.
- **D:** Correct. traces tool call latency through Streamable HTTP gateways into server execution with per-session correlation.
- **E:** Incorrect. hand-rolling tools/list JSON handlers without SDK types and Zod misses schema edge cases and list_changed plumbing.

### Question 96 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). This follows the MCP specification for Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 6.4 validation S4Q096. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Incorrect. gating only on unit tests and never on real Inspector CLI runs ships capability/lifecycle regressions to prod.
- **B:** Incorrect. killing the process to stop one request leaks child tasks and corrupts shared Host resource locks.
- **C:** Incorrect. reconnecting with tight 10-ms loops and no Last-Event-ID hammers the server and replays duplicate side effects.
- **D:** Correct. powers per-tool SLOs and supply-chain forensics without persisting sensitive tool argument values.

### Question 97 — `C` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: C (is correct). Selecting this honors Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation and prevents the listed failure mode in Veridian Legal Vault legal compliance docs flows. Skill 6.4 validation S4Q097. [Skill 6.4: Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation | Primary Reference: https://opentelemetry.io/docs/specs/semconv/gen-ai/ | Additional Reference: https://modelcontextprotocol.io/docs/concepts/transports]

- **A:** Incorrect. relying solely on OS TCP keepalives through SSE gateways leaves dead sessions undetected for hours.
- **B:** Incorrect. polling tools/call in a loop to infer progress burns tokens and loses correlation when tasks overlap.
- **C:** Correct. enables post-incident forensics without persisting PII/tokens, keyed by stable tool provenance hashes.
- **D:** Incorrect. passing the entire Host env block including prod secrets to every MCP server violates env isolation and leaks credentials.

### Question 98 — `A, B, C` (SDKs, Deployment, Observability & Ecosystem)

Correct answers: A, B, and C (are correct). Per MCP 2025-11-25, Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns ensures spec-compliant lifecycle and isolation for legal compliance docs. Skill 6.5 validation S4Q098. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Correct. uses MCP vertically for capabilities and A2A horizontally for peer negotiation, per LM-Foundation AAIF stack guidance.
- **B:** Correct. centralizes AuthZ, session affinity, and observability without duplicating gateway logic in each MCP server.
- **C:** Correct. standardizes cross-Host deployment via portable config blocks with scoped env and per-server enable toggles.
- **D:** Incorrect. polling resources/read every 100 ms instead of subscribing wastes tokens and misses in-between change coalescing.
- **E:** Incorrect. deploying a naïve HTTP proxy that strips Accept/Session headers breaks Streamable HTTP streaming and resumability.
- **F:** Incorrect. executing a heavy DB scan tool just to populate a dropdown instead of lightweight completion causes UI jank.

### Question 99 — `A` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: A (is correct). Selecting this honors Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns and prevents the listed failure mode in Veridian Legal Vault legal compliance docs flows. Skill 6.5 validation S4Q099. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Correct. uses MCP vertically for capabilities and A2A horizontally for peer negotiation, per LM-Foundation AAIF stack guidance.
- **B:** Incorrect. skipping iss equality and only checking signature lets an attacker’s AS mint accepted tokens for your MCP fleet.
- **C:** Incorrect. running stdio servers as detached global daemons without lifecycle binding leaks zombies after Host quit.
- **D:** Incorrect. assigning `id` to notifications and awaiting replies on them deadlocks the request tracker.

### Question 100 — `D` (SDKs, Deployment, Observability & Ecosystem)

Correct answer: D (is correct). This follows the MCP specification for Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns, correcting the insecure/incompatible anti-pattern for legal compliance docs. Skill 6.5 validation S4Q100. [Skill 6.5: Integrate MCP with IDE hosts, A2A bridges, gateways, and ecosystem discovery patterns | Primary Reference: https://github.com/modelcontextprotocol/registry | Additional Reference: https://modelcontextprotocol.io/examples]

- **A:** Incorrect. returning HTTP 500 HTML bodies instead of JSON-RPC error objects hides retriability and breaks client error switches.
- **B:** Incorrect. re-listing prompts on every render without listening to list_changed wastes round trips and lags new pack visibility.
- **C:** Incorrect. mixing raw WebSocket frames with MCP JSON-RPC without Client/transport abstractions breaks reconnection and session logic.
- **D:** Correct. standardizes cross-Host deployment via portable config blocks with scoped env and per-server enable toggles.
