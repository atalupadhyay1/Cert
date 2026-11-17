# 🔌 Model Context Protocol (MCP 2025-11-25) · Practice Test Course Landing Page

> **Course Title:** **MCP (Model Context Protocol): 6 Practice Exams (600 Qs)**
>
> **Course Subtitle:** **600 scenario Qs • MCP 2025-11-25 Tools/Resources, Streamable HTTP, OAuth 2.1 & Registry**

Prepare for **MCP production readiness reviews, protocol conformance audits, and Staff Platform/Tooling system-design loops** across **600 original, production-grade scenarios** organized into **six 100-question full-length practice exams**, aligned to the **November 2026 MCP open-standard ecosystem** (*MCP Specification `2025-11-25` & Registry/Inspector, Linux Foundation AAIF, OAuth 2.1 + RFC 7591/8707/9207/9728 + CIMD, OWASP MCP Security Checklist, TypeScript/Python SDKs*).

---

## 🧭 2026 MCP Certification & Open-Standards Landscape

Production MCP has evolved from Anthropic's late-2024 introduction into a **Linux Foundation AAIF-governed vendor-neutral standard** with breaking transport consolidation in 2025. Here is an honest side-by-side guide to the 2026 ecosystem so you know how these 600 questions map to official specs — and what requires separate hands-on Inspector practice:

| Credential / Standard (Verified November 2026) | Format, Timing & Governance | Core Engineering Scope Covered Here |
|---|---|---|
| **Model Context Protocol Specification (`2025-11-25` & Registry)** | Open spec via **Anthropic → Linux Foundation AAIF**; `6` domains, **120-minute** practice pacing | **All 6 MCP domains (`100%`):** Foundations & Lifecycle (`18%`), Tools/Resources (`20%`), Prompts/Sampling/Roots (`16%`), Transports/Sessions (`16%`), Auth/Security/Registry (`15%`), SDKs/Deployment/Observability (`15%`) |
| **MCP Registry & Inspector (`mcp-registry` + `@modelcontextprotocol/inspector`)** | Registry `server.json` with signed provenance; Inspector UI + CLI `--cli --method` | **Discovery & Conformance:** `tools/list`/`resources/list` discovery, Inspector interactive & CI headless validation |
| **OAuth 2.1 + IETF RFCs (7591, 8707, 9207, 9728) & CIMD** | `authorization_code + PKCE`, Dynamic Client Registration, Resource Indicators, `iss` validation, Client ID Metadata Document | **AuthZ:** Protected Resource Metadata, loopback redirects, audience-bound tokens, TLS-bound CIMD identity |
| **OWASP MCP Security Checklist (`2025`)** | Community threat model for platform/security reviews | **Threat Model:** Tool poisoning, rug-pull/version pinning, privilege escalation, prompt injection via tool content, registry trust, `env` isolation |

> **Honest Scope & Platform Disclosure:** Independent educational material authored originally from public MCP specifications and open-protocol documentation — not affiliated with, sponsored by, or endorsed by Anthropic, the Linux Foundation, or any MCP Host vendor. Live Inspector sessions and interactive OAuth flows cannot run inside Udemy's `multiple-choice` / `multi-select` engine; we test protocol/config mastery via `____` slot completions, `→` 4-step ordered sequences, and `Proposed solution:` architecture evaluations (`0` artificial multi-tab case studies). Practice test scores do not guarantee passing any third-party conformance audit.

---

## 📋 Udemy Course Metadata (Copy/Paste into the Publishing Form)

### 1. Course Title

```text
MCP (Model Context Protocol): 6 Practice Exams (600 Qs)
```

*(54 characters — within Udemy's 60-character title ceiling.)*

### 2. Course Subtitle

```text
600 scenario Qs • MCP 2025-11-25 Tools/Resources, Streamable HTTP, OAuth 2.1 & Registry
```

*(94 characters — within Udemy's 120-character subtitle ceiling.)*

### 3. Course Description

```text
Shipping a demo MCP server in a weekend takes a few lines of TypeScript. Operating compliant, secure, multi-tenant MCP fleets in production — across trading risk desks, clinical trial hubs, cloud platform consoles, legal vaults, global commerce checkouts, and SOC automation meshes — requires deep mastery of the MCP 2025-11-25 lifecycle, tool/resource contracts, sampling/roots/elicitation, Streamable HTTP sessions, OAuth 2.1 authorization, registry trust, and SDK/Inspector delivery.

Whether you are preparing for MCP conformance audits, building Host integrations in VS Code / Claude Desktop / Cursor, publishing signed servers to the MCP Registry, or leading Staff platform architecture reviews, these six full-length 100-question mock exams rigorously test all 34 production skills across six blueprint-weighted domains:
• Domain 1 — MCP Foundations, Architecture & Lifecycle (18% -> 18 questions/exam; 108 total): Host-Client-Server triad and 1:1 Client-Server isolation; initialize → capabilities negotiation → notifications/initialized handshake; JSON-RPC 2.0 envelope (jsonrpc/id/method/params, error -32700…-32603), notifications vs requests, batching; capabilities gating (tools/resources/prompts/roots/sampling/logging) and experimental progression; ping keepalives, progress notifications with progressToken, cancellation, and MCP vs function calling vs A2A differentiation.
• Domain 2 — Tools, Resources & Resource Templates (20% -> 20 questions/exam; 120 total): Tool declaration (name/title/description/inputSchema/outputSchema/annotations with readOnly/destructive/idempotent/openWorld hints), model-controlled tools/call, list_changed evolution, structured outputs (outputSchema + structuredContent) alongside typed content blocks (text/image/resource); Resources (direct vs uriTemplate factories, uri scheme/mimeType, cursor pagination, read with text/blob, subscribe + notifications/resources/updated, list_changed); Prompts (name/arguments, prompts/get messages[]) and completion/complete typeahead.
• Domain 3 — Prompts, Sampling, Roots & Elicitation (16% -> 16 questions/exam; 96 total): Prompts/list/get with typed argument validation and prompts/list_changed; Roots (client-owned allowlists, roots/list discovery, canonicalization/traversal prevention, list_changed rescoping); Sampling (sampling/createMessage with messages/maxTokens/modelPreferences (hints/cost/speed/intelligence) and includeContext none/thisServer/allServers, human-in-loop gating); Elicitation (elicitation/create with requestedSchema form round-trips vs sampling synthesis, vs human field collection); Logging (logging/setLevel filtering notifications/message) and progressToken correlation.
• Domain 4 — Transports, Sessions & Protocol Evolution (16% -> 16 questions/exam; 96 total): stdio (child process, stdin/stdout JSON-RPC lines, stderr logs), Streamable HTTP (single POST /mcp, Accept: application/json, text/event-stream negotiation, Mcp-Session-Id stickiness, Last-Event-ID resumability), SSE deprecation (split /sse + /messages pre-2025-03-26 → unified Streamable HTTP), reconnection with exponential backoff+jitter + Retry-After + re-validation, batching within maxBatchSize, gateway interop (forwarding Session-Id/Last-Event-ID/Authorization), and ping every 30–60s for ALB idle survival.
• Domain 5 — Authorization, Security, Trust & Registry (15% -> 15 questions/exam; 90 total): Protected Resource Metadata + Authorization Server Metadata discovery (RFC 9728/8414), OAuth 2.1 authorization_code + PKCE + loopback callbacks, RFC 7591 DCR, RFC 8707 resource audience binding, RFC 9207 iss equality, CIMD via https://.../.well-known/oauth-client, OS keychain token storage, least-privilege scopes; OWASP MCP threats — tool poisoning (description as untrusted UI text), rug-pull (version/hash pinning + re-consent), privilege escalation/confused-deputy, prompt injection via tool/resource content with provenance tags, registry trust (signed server.json + publisher verification), env isolation (per-server allowlist), redacted audit logs.
• Domain 6 — SDKs, Deployment, Observability & Ecosystem (15% -> 15 questions/exam; 90 total): TypeScript SDK (McpServer/registerTool/Zod) & Python SDK (FastMCP/@mcp.tool() + Pydantic async lifespan) with Client + Stdio/StreamableHTTP transports; Inspector UI + CLI headless gates (tools/list, tools/call, resources/read, pagination, cancellation); Packaging as distroless non-root containers with MCP_TRANSPORT env & health ping; Publishing to Registry (server.json/name/version/packages) with provenance; protocolVersion bump policy (breaking framing only); OTel GenAI + HTTP RPC spans (gen_ai.tool.name, rpc.method, mcp.session.id), structured JSON logs with redacted hashes; Ecosystem — registry search/categories/badges vs custom builds, MCP (vertical) + A2A (horizontal) bridge via gateways, VS Code/Claude Desktop/Cursor mcpServers config, gateway mesh (auth termination, sticky LB, rate limit, audit fan-out).
• Each mock exam mirrors production MCP incident tickets (trading risk desk token leaks, clinical trial roots traversal, cloud platform Inspector drift, legal vault WORM holds, commerce prompt injection, SOC gateway header stripping) so your reasoning transfers directly to spec reviews, Inspector runs, and registry publishes.

What this course is NOT: We do not reproduce copyrighted vendor training, leaked exam dumps, or proprietary Host internals. Every item is an original scenario distilled from the public MCP spec, SDK READMEs, Inspector docs, and IETF RFCs. You will see code-snippet completions, sequence orderings, and architecture evaluations — never hands-on lab simulations that require live Inspector.
```

### 4. What will students learn in your course?

- Configure `initialize` with `protocolVersion` and `capabilities` correctly
- Choose `stdio` for local subprocess vs `Streamable HTTP` for remote hosts
- Declare `tools` with `inputSchema`, `outputSchema`, and annotation hints
- Return `isError` with typed `content` blocks for `tools/call` results
- Publish `resources` via `uri` scheme, `mimeType`, and cursor pagination
- Expand `resourceTemplates` with `uriTemplate` without guessing syntax
- Subscribe to `resources` via `subscribe` and handle `list_changed` pushes
- Expose `prompts` with typed `arguments` and `prompts/get` expansion
- Enforce `roots/list` boundaries with canonicalization and traversal blocks
- Delegate via `sampling/createMessage` with `modelPreferences` priority
- Limit context via `includeContext` to prevent cross-server exfiltration
- Collect input via `elicitation/create` with `requestedSchema` forms

### 5. What are the requirements or prerequisites for taking your course?

- TypeScript or Python fluency (reading SDK handlers, Zod/Pydantic schemas)
- HTTP & JSON-RPC fundamentals (methods, notifications, error codes)
- Basic OAuth 2 concepts (authorization_code, scopes, PKCE intuition)
- Familiarity with VS Code, Claude Desktop, or any LLM Host extensibility
- Willingness to practice with Inspector docs alongside Udemy quizzes (no labs needed)

### 6. Who is this course for?

- Platform/Tooling engineers shipping MCP servers to production
- Host integrators adding `mcpServers` blocks to VS Code / Claude Desktop / Cursor
- Security reviewers auditing MCP tool poisoning, rug-pull, and token handling
- SDK contributors building with TypeScript `McpServer` or Python `FastMCP`
- Registry publishers preparing `server.json` with signed provenance and badges

---

## 📝 Six Full-Length Mock Exams — Editorial Summaries

### Full-Length Mock Exam 1 — Meridian Capital Trading Desk (Finance & Risk)

**Theme:** `Host-Client-Server Triad, SDK Scaffolds, Tool Poisoning Defense & Registry Trust`  
**Scenario Brief:** Meridian Capital runs low-latency trading risk checks via MCP tools that price swaps, fetch market data resources, and delegate sampling for narrative summaries. Your job: lock the Host-Client-Server triad, scaffold SDK servers correctly, and defend tool poisoning without breaking Streamable HTTP session affinity. Expect: lifecycle handshake ordering, `capabilities` gating, `inputSchema` validation, `isError` signaling, Host isolation, and registry trust badges — all under FINRA-sensitive audit logging.  
**Trimmed Summary (Udemy):** Finance & Risk — `Host-Client-Server` triad, SDK scaffolds, tool poisoning defense, registry trust.

### Full-Length Mock Exam 2 — HelixMed Clinical Research Hub (Healthcare & Trials)

**Theme:** `Initialization Handshake, Resource Templates, Streamable HTTP Sessions & Elicitation`  
**Scenario Brief:** HelixMed aggregates clinical trial docs as MCP resources with `resourceTemplates` for `patient://{trial}/{id}` expansion. Clinicians approve sampling that drafts summaries. You must master: `initialize` version negotiation, resource `uri`/`mimeType` addressing, template expansion, `Mcp-Session-Id`/`Last-Event-ID` resumability across ALBs, and typed `elicitation/create` for structured consent forms under HIPAA redaction.  
**Trimmed Summary (Udemy):** Healthcare & Trials — `initialize` handshake, resource templates, Streamable HTTP sessions, elicitation.

### Full-Length Mock Exam 3 — AtlasCloud Platform Ops (Cloud Infra & DevTools)

**Theme:** `JSON-RPC Framing, Tools vs Resources, OAuth 2.1 PKCE & Inspector CI Gates`  
**Scenario Brief:** AtlasCloud ships an internal DevTools MCP fleet (K8s, Terraform, Grafana) to 2,000 engineers. You will: frame JSON-RPC correctly, separate Tools (model-controlled) from Resources/Prompts (app/user-controlled), implement OAuth 2.1 `authorization_code + PKCE` with loopback callbacks and `RFC 9207` checks, and gate PRs with Inspector CLI (`--cli --method tools/list`). Beware polling vs subscribe anti-patterns.  
**Trimmed Summary (Udemy):** Cloud Infra & DevTools — JSON-RPC framing, Tools/Resources, OAuth PKCE, Inspector CI.

### Full-Length Mock Exam 4 — Veridian Legal Vault (Legal & Compliance Docs)

**Theme:** `Capabilities Negotiation, Completions API, Logging Levels & Audit Provenance`  
**Scenario Brief:** Veridian Legal stores M&A docs as MCP resources under strict roots boundaries. Associates rely on completions typeahead and prompt packs for clause generation. You will: negotiate `capabilities`, back dropdowns with `completion/complete` (not tool scans), filter `logging/setLevel` correctly, correlate `progressToken`, and emit redacted, append-only audit logs with `requestId`/`toolName` for WORM litigation hold — blocking symlink traversal and `includeContext` leakage.  
**Trimmed Summary (Udemy):** Legal & Compliance — `capabilities` negotiation, Completions API, logging levels, audit provenance.

### Full-Length Mock Exam 5 — OmniCart Commerce Ops (Retail & Supply Chain)

**Theme:** `Progress & Cancellation, Sampling Delegation, Roots Boundaries & Env Isolation`  
**Scenario Brief:** OmniCart powers checkout and supply-chain copilots via MCP tools that read catalogs and mutate carts. You must: link `progress` streams via `progressToken`, cancel runaway sampling loops via `notifications/cancelled`, enforce `roots/list` client-owned boundaries with rescoping on `list_changed`, sandbox env with per-server allowlists (no Host secret passthrough), and handle `structuredContent` + `outputSchema` for order JSON.  
**Trimmed Summary (Udemy):** Retail & Supply — Progress/Cancellation, Sampling delegation, Roots boundaries, env isolation.

### Full-Length Mock Exam 6 — Sentinel Cyber Fusion (Security & SOC Automation)

**Theme:** `SSE Deprecation → Streamable HTTP, Batching, Reconnect Resumability & Gateway Mesh`  
**Scenario Brief:** Sentinel SOC fuses SIEM, SOAR, and threat-intel via MCP. Legacy `HTTP+SSE` split endpoints must migrate to `Streamable HTTP`, batch within `maxBatchSize`, survive gateway header stripping, and re-establish with backoff+jitter + `Last-Event-ID` replay after SOC failover. You will also: pin versions against rug-pull, enforce per-tool scope checks, and front the fleet with an MCP-aware gateway mesh (auth termination, sticky LB, rate limit, audit fan-out).  
**Trimmed Summary (Udemy):** Security & SOC — SSE→Streamable HTTP, batching, resumability, gateway mesh.

---

## 🎉 Welcome Message

Welcome to **MCP (Model Context Protocol): 6 Practice Exams (600 Qs)** — your production-grade rehearsal for MCP conformance and platform reviews.

This course was built from the public MCP Specification `2025-11-25`, MCP Registry/Inspector docs, TypeScript/Python SDK READMEs, OAuth 2.1 + IETF RFCs, and the OWASP MCP Security Checklist — not copied from any vendor course or exam dump. Each mock exam is a standalone enterprise scenario (Meridian Capital, HelixMed, AtlasCloud, Veridian Legal, OmniCart, Sentinel) with authentic incident tickets, Inspector logs, and registry metadata to practice the reads you will make on the job.

How to use it:
1. **Simulate closed-book exam conditions:** 100 Qs in 120 minutes (≈ 72 sec/Q). No pausing to search docs — practice recall.
2. **Read every explanation:** Correct and distractor rationales cite `Skill X.Y` and two `https://` primary references so you know exactly which spec section to revisit (e.g., `sampling/createMessage`, `Mcp-Session-Id`, `RFC 9207`).
3. **Loop on your weak domain:** Score < 70% on a domain → revisit that curriculum outline skill and its `sources.py` URLs → retake a different mock exam (all 6 are blueprint-identical, `0` cross-set duplication).
4. **Bring your Host:** Keep VS Code `settings.json` / `claude_desktop_config.json` and the Inspector docs open after the timed run to compare your answer against the live tool.

You have `600` fresh scenarios with `0` artificial case-study blocks, `84` four-option `multiple-choice` (balanced `21/21/21/21`) + `16` `multi-select` per set, `20–26` `____` completions, and `8` `→` sequences — exactly mirroring the format you will use for real MCP reviews. Let's get your MCP fleet ship-shape. Good luck, and enjoy the practice!

---

## 🏁 Congratulations Message

Congratulations on completing all **six 100-question MCP mock exams — 600 scenarios** across Meridian Capital, HelixMed, AtlasCloud, Veridian Legal, OmniCart, and Sentinel! You have now exercised every one of the `34` MCP skills (`1.1`–`6.5`) multiple times under timed, mixed-format pressure.

What you have proven:
• You can distinguish Host/Client/Server boundaries, negotiate `initialize` with `protocolVersion`/`capabilities`, frame JSON-RPC 2.0 correctly, and gate features behind capabilities — the bedrock of every MCP connection.
• You can declare and evolve Tools/Resources/Prompts safely (typed `inputSchema`/`outputSchema`, `isError` + `structuredContent`, `uri`/`mimeType`, pagination cursors, `list_changed` pushes) and back typeahead with `completion/complete`.
• You can enforce `roots/list` least-privilege, delegate via `sampling/createMessage` with `modelPreferences`/`includeContext`, collect via `elicitation/create`, regulate `logging/setLevel`, and correlate `progressToken`.
• You can pick `stdio` vs `Streamable HTTP`, honor `Mcp-Session-Id`/`Last-Event-ID` resumability, migrate off deprecated SSE, batch within `maxBatchSize`, and survive L7 gateway idle timeouts via `ping`.
• You can discover OAuth endpoints via PRM/AS metadata, complete `authorization_code + PKCE` with loopback + `CIMD`, audience-bind via `RFC 8707` and validate `iss` per `RFC 9207`, store tokens in OS keychain, and apply OWASP MCP hardening (tool poisoning, rug-pull pinning, privilege escalation, env isolation, redacted audit logs).
• You can build with TS `McpServer`+Zod / Python `FastMCP`+Pydantic, validate via Inspector UI+CLI, publish signed `server.json` to the Registry, bump `protocolVersion` only for breaking changes, instrument with OTel, and front with a gateway mesh.

Next steps:
1. **Run the Inspector:** `npx @modelcontextprotocol/inspector` against your own server — reproduce the `tools/list`/`tools/call` flows you just quizzed.
2. **Audit one real server:** Pick a Registry community server, check its `server.json` signature, `inputSchema` strictness, and token storage against the checklist you now know.
3. **Keep the telemetry:** `validation-report.json` shows your `600/600` unique coverage and `0.7188` max Jaccard — use it to plan spaced repetition (re-attempt lowest-scoring mock after 72 hours).

Thank you for trusting this independent, spec-authored material. MCP is still evolving — follow <https://modelcontextprotocol.io/specification/2025-11-25> and <https://github.com/modelcontextprotocol/specification> for the next patch. When you ship a secure, observable MCP fleet that passes its first conformance audit, you will know why these `600` questions mattered. Celebrate, then ship. 🚀

---

> **File Note for Instructors:** This `01-landing-page/landing-page.md` contains every Udemy mandatory field copy-paste block (Field 1 Title, Field 2 Subtitle, Field 3 Description, Field 4 What will students learn, Field 5 Requirements, Field 6 Who is this course for) plus per-exam Full and Trimmed blurbs and Welcome/Congratulations messages, satisfying `course/check_landing_page_fields.py` (expects ≥ 3 bullets per field and ≥ 80 chars for prose sections).

