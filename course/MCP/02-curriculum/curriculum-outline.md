# Model Context Protocol (MCP 2025-11-25) — Curriculum Outline & Blueprint Crosswalk

**Baseline:** `November 2026`  
**Structure:** `6` Full-Length Mock Exams × `100` Questions = `600` Unique Production Scenarios (`0` artificial case-study blocks)  
**Item Mix per Exam:** `76` Single-Choice (`S`) + `8` Ordered 4-Step Sequences (`O`, exported as `multiple-choice` with `→`) + `13` Two-Answer Multi-Select (`M2`) + `3` Three-Answer Multi-Select (`M3`) = `84 multiple-choice` (`21 A / 21 B / 21 C / 21 D`) + `16 multi-select`

---

## 1. Crosswalk to Official 2026 MCP Standards

| Consolidated Course Domain | Weight / Set | MCP 2025-11-25 Primitives | Adjacent Standards & Tooling |
| :--- | :---: | :--- | :--- |
| **Domain 1:** MCP Foundations, Architecture & Lifecycle | `18%` (`18` Qs) | Host/Client/Server triad, `initialize`, `capabilities`, JSON-RPC 2.0, `ping`/`progress`/`cancelled` | JSON-RPC 2.0, AAIF governance, experimental capabilities |
| **Domain 2:** Tools, Resources & Resource Templates | `20%` (`20` Qs) | Tools (`inputSchema`/`outputSchema`, `isError`), Resources (`uri`/`mimeType`, templates, pagination, `subscribe`) | TypeScript/Python SDKs, MCP Inspector |
| **Domain 3:** Prompts, Sampling, Roots & Elicitation | `16%` (`16` Qs) | Prompts, `completion/complete`, `roots/list`, `sampling/createMessage`, `elicitation/create`, `logging/setLevel` | VS Code/Claude Desktop Host configs |
| **Domain 4:** Transports, Sessions & Protocol Evolution | `16%` (`16` Qs) | `stdio` vs `Streamable HTTP`, `Mcp-Session-Id`, `Last-Event-ID`, SSE deprecation (`2025-03-26`) | L7 gateways, resumability, batching |
| **Domain 5:** Authorization, Security, Trust & Registry | `15%` (`15` Qs) | OAuth 2.1 + PKCE, PRM/AS discovery, `RFC 7591` DCR, `RFC 8707` audience, `RFC 9207` `iss`, `CIMD`, `RFC 9728` | OWASP MCP Checklist, MCP Registry signing |
| **Domain 6:** SDKs, Deployment, Observability & Ecosystem | `15%` (`15` Qs) | TS `McpServer`+Zod, Python `FastMCP`+Pydantic, Inspector, `server.json`, OTel spans, gateway mesh | A2A bridge, registry search, `AGENTS.md` |

---

## 2. Skill-Level Syllabus (`34` Skills `1.1`–`6.5`)

### Domain 1 — MCP Foundations, Architecture & Lifecycle (`18` Qs/set · `108` total)
- **`1.1` (`3` Qs/set: `3 S`):** Distinguish Host, Client, and Server roles and the `1:1` Client-Server isolation model.
- **`1.2` (`3` Qs/set: `1 O + 2 S`):** Execute the `initialize → capabilities negotiation → notifications/initialized` lifecycle handshake.
- **`1.3` (`3` Qs/set: `3 S`):** Frame JSON-RPC 2.0 messages, notifications, request IDs, batching, and error code taxonomy (`-32700` to `-32603`).
- **`1.4` (`3` Qs/set: `2 S + 1 M2`):** Advertise and gate features via `capabilities` objects (`tools`, `resources`, `prompts`, `sampling`, `roots`, `logging`).
- **`1.5` (`3` Qs/set: `2 S + 1 M2`):** Manage keepalive `ping`, `progress` notifications, `cancellation`, and `shutdown` semantics.
- **`1.6` (`3` Qs/set: `2 S + 1 M2`):** Differentiate MCP from function calling, A2A, and `experimental` capability progression.

### Domain 2 — Tools, Resources & Resource Templates (`20` Qs/set · `120` total)
- **`2.1` (`4` Qs/set: `3 S + 1 M2`):** Declare tools with `name`, `title`, `description`, `inputSchema`, `outputSchema`, and `readOnly/destructive/idempotent/openWorld` hints.
- **`2.2` (`4` Qs/set: `3 S + 1 M2`):** Control model-controlled tool execution, `list` discovery, validation, and typed `content` + `structuredContent` output.
- **`2.3` (`3` Qs/set: `3 S`):** Evolve tool catalogs dynamically via `tools/list` pagination and `notifications/tools/list_changed`.
- **`2.4` (`3` Qs/set: `2 S + 1 M2`):** Address direct resources vs templated resources with `uri` schemes, `name`, `mimeType`, and `annotations`.
- **`2.5` (`3` Qs/set: `2 S + 1 M2`):** Paginate, read, and subscribe to resources via `list`, `read`, `subscribe`, and `list_changed` flows.
- **`2.6` (`3` Qs/set: `3 S`):** Declare prompts and completions for argument typeahead and parameterized prompt expansion (`prompts/list`, `prompts/get`, `completion/complete`).

### Domain 3 — Prompts, Sampling, Roots & Elicitation (`16` Qs/set · `96` total)
- **`3.1` (`3` Qs/set: `3 S`):** Expose and expand prompts via `prompts/list`, `prompts/get`, and argument validation.
- **`3.2` (`3` Qs/set: `1 O + 2 S`):** Enforce client-owned filesystem boundaries via `roots/list` and `notifications/roots/list_changed` with path canonicalization.
- **`3.3` (`3` Qs/set: `2 S + 1 M2`):** Delegate LLM work via `sampling/createMessage` with `modelPreferences` and `includeContext` controls.
- **`3.4` (`3` Qs/set: `1 O + 2 S`):** Collect human input via `elicitation/create` with `requestedSchema` and form round-trips.
- **`3.5` (`2` Qs/set: `2 S`):** Regulate verbosity via `logging/setLevel` and `notifications/message` level filtering.
- **`3.6` (`2` Qs/set: `1 O + 1 M2`):** Correlate `progress` and `completion` flows with `progressToken` and `completion/complete` semantics.

### Domain 4 — Transports, Sessions & Protocol Evolution (`16` Qs/set · `96` total)
- **`4.1` (`3` Qs/set: `2 S + 1 M2`):** Operate `stdio` transport (`stdin`/`stdout` JSON-RPC, `stderr` logs) and child-process lifecycle.
- **`4.2` (`3` Qs/set: `1 O + 2 S`):** Operate `Streamable HTTP` (`single POST /mcp`, `Accept: application/json, text/event-stream`, SSE or JSON response).
- **`4.3` (`3` Qs/set: `1 O + 1 S + 1 M2`):** Manage session affinity and resumability via `Mcp-Session-Id` and `Last-Event-ID` replay.
- **`4.4` (`3` Qs/set: `1 O + 2 S`):** Migrate from deprecated HTTP+SSE dual endpoint (`pre-2025-03-26`) to `Streamable HTTP`.
- **`4.5` (`2` Qs/set: `2 S`):** Re-establish sessions with exponential backoff + jitter, `Retry-After`, and capability re-validation.
- **`4.6` (`2` Qs/set: `2 S`):** Tune batching, gateway interop, and `ping` keepalives for L7 proxy and idle-timeout survival.

### Domain 5 — Authorization, Security, Trust & Registry (`15` Qs/set · `90` total)
- **`5.1` (`3` Qs/set: `3 S`):** Discover OAuth endpoints via Protected Resource Metadata (`/.well-known/oauth-protected-resource`) and Authorization Server Metadata.
- **`5.2` (`3` Qs/set: `2 S + 1 M2`):** Implement OAuth 2.1 `authorization_code + PKCE` with loopback callbacks and `CIMD` bindings.
- **`5.3` (`3` Qs/set: `2 S + 1 M2`):** Audience-bind tokens via `RFC 8707` `resource` indicator and validate `RFC 9207` `iss` equality.
- **`5.4` (`3` Qs/set: `3 S`):** Defend tool poisoning, rug-pull, privilege escalation, and prompt-injection via MCP threat model and OWASP checklist.
- **`5.5` (`3` Qs/set: `1 O + 2 S`):** Establish supply-chain trust via MCP Registry signatures, sandboxing, `env` isolation, and redacted audit logging.

### Domain 6 — SDKs, Deployment, Observability & Ecosystem (`15` Qs/set · `90` total)
- **`6.1` (`3` Qs/set: `3 S`):** Build servers with TypeScript SDK (`McpServer` + Zod) and Python SDK (`FastMCP` + Pydantic) with typed validation.
- **`6.2` (`3` Qs/set: `1 O + 2 S`):** Validate interactively and in CI via Inspector UI and Inspector CLI (`--cli --method`) conformance gates.
- **`6.3` (`3` Qs/set: `2 S + 1 M2`):** Publish versioned, signed servers to the MCP Registry with `server.json`, provenance attestation, and publisher verification.
- **`6.4` (`3` Qs/set: `2 S + 1 M2`):** Instrument MCP with OpenTelemetry spans/traces, structured logs, and per-tool SLO correlation.
- **`6.5` (`3` Qs/set: `2 S + 1 M3`):** Integrate MCP with IDE hosts, A2A bridges, gateway mesh, and ecosystem discovery (registry search, `AGENTS.md`).

---

## 3. Six Enterprise Mock Exam Progression

| Mock Exam | Fictional Enterprise & Vertical | Signature Technical Challenges |
| :---: | :--- | :--- |
| **1** | **Meridian Capital Trading Desk** *(Finance & Risk)* | `Streamable HTTP` auth via `RFC 9207`, `Tool poisoning` defense, `Mcp-Session-Id` affinity, `KEDA` autoscale |
| **2** | **HelixMed Clinical Research Hub** *(Healthcare & Trials)* | `Resource templates` for trial docs, `Roots` boundary, `Sampling` with `modelPreferences`, `HIPAA` redaction |
| **3** | **AtlasCloud Platform Ops** *(Cloud Infra & DevTools)* | `stdio` subprocess isolation, `completion/complete` typeahead, `OAuth PKCE` loopback, Inspector CI |
| **4** | **Veridian Legal Vault** *(Legal & Compliance Docs)* | `Resource subscriptions`, `Elicitation` forms, `Logging` levels, `WORM` provenance for legal hold |
| **5** | **OmniCart Commerce Ops** *(Retail & Supply Chain)* | `Prompt packs`, `Progress` streaming, `Scope` least-privilege, `Registry` publish with signing |
| **6** | **Sentinel Cyber Fusion** *(Security & SOC Automation)* | `SSE deprecation` migration, `Rug-pull` hash pinning, `Audit` log provenance, `Gateway` mesh mTLS |

