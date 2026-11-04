"""Ordered 4-step sequence terms (O items) for Forward Deployed Engineer (6x100)."""

SEQUENCE_TERMS = {
    # 1.4 — Discovery -> PoC -> Pilot -> Production Gate Progression
    'seq_fde_discovery_scope_ok': (
        'Shadow live operator workflows & baseline current KPIs → decompose bottlenecks via MECE & bind SLI/SLO targets → run a time-boxed PoC on sanitized client slices → validate CISO/eval exit gates in a Pilot before Production rollout',
        'grounds problem selection in measured operator baselines before staging PoC, Pilot, and Production exit gates.',
        'starting with executive slide decks or model fine-tuning before shadowing operators and baselining KPIs builds unshippable demoware.',
    ),
    'seq_fde_discovery_scope_w1': (
        'Fine-tune a custom LLM on all client PDFs first → demo to executives → shadow live operator workflows & define KPIs afterward → deploy directly to Production without a Pilot',
        'fine-tunes prematurely before problem discovery, operator shadowing, baseline measurement, or Pilot safety gates.',
        'fine-tunes prematurely before problem discovery, operator shadowing, baseline measurement, or Pilot safety gates.',
    ),
    'seq_fde_discovery_scope_w2': (
        'Deploy directly to 100% Production traffic → collect SLA breach tickets to discover workflows → add SLI/SLO metrics retroactively → run a CISO security review after launch',
        'ships unverified AI to production before discovery, SLO definition, or CISO security clearance.',
        'ships unverified AI to production before discovery, SLO definition, or CISO security clearance.',
    ),
    'seq_fde_discovery_scope_w3': (
        'Shadow live operator workflows → sign commercial SLA penalty contracts on an untested PoC → skip Pilot evaluation gates → rewrite the architecture after Production cutover',
        'commits legally binding SLA penalties on an unvalidated PoC and skips Pilot evaluation gates.',
        'commits legally binding SLA penalties on an unvalidated PoC and skips Pilot evaluation gates.',
    ),

    # 2.3 — Brownfield Legacy Enterprise Integration (Strangler Fig + ACL + Outbox)
    'seq_fde_legacy_strangler_ok': (
        'Place an Anti-Corruption Layer (`ACL`) in front of legacy ERP/SOAP → persist writes via transactional outbox + idempotency key → shadow-test parity against legacy outputs → cut traffic over slice-by-slice (`Strangler Fig`)',
        'isolates legacy domain models behind an ACL, guarantees at-least-once idempotent writes, verifies shadow parity, and migrates incrementally.',
        'big-bang legacy rewrites or dual-writing without transactional outbox/idempotency cause silent split-brain data corruption.',
    ),
    'seq_fde_legacy_strangler_w1': (
        'Freeze all client ERP changes for 9 months → rewrite the entire legacy database schema in one weekend cutover → add idempotency keys after duplicate invoices appear → build an ACL later',
        'attempts a high-risk big-bang cutover without incremental Strangler Fig parity or up-front idempotency.',
        'attempts a high-risk big-bang cutover without incremental Strangler Fig parity or up-front idempotency.',
    ),
    'seq_fde_legacy_strangler_w2': (
        'Expose raw legacy COBOL/SOAP column names directly inside LLM tool schemas → dual-write to SQL and Kafka without an outbox → skip shadow parity → cut over 100% of users',
        'leaks cryptic legacy schemas into agent prompts and risks dual-write inconsistency without a transactional outbox.',
        'leaks cryptic legacy schemas into agent prompts and risks dual-write inconsistency without a transactional outbox.',
    ),
    'seq_fde_legacy_strangler_w3': (
        'Cut 100% of production writes to the new FastAPI service first → disable legacy ERP backups → add an Anti-Corruption Layer (`ACL`) after schema drift breaks callers → test idempotency in production',
        'switches production write traffic before ACL isolation, shadow parity testing, or rollback readiness.',
        'switches production write traffic before ACL isolation, shadow parity testing, or rollback readiness.',
    ),

    # 3.5 — ACL-Aware Grounded Enterprise RAG Pipeline ("Ground")
    'seq_fde_acl_rag_ground_ok': (
        'Ingest documents with source lineage & principal ACL metadata → enforce caller identity pre-filtering across hybrid BM25 + vector retrieval → rerank top candidates with a cross-encoder → generate answers citing chunk IDs & verify groundedness',
        'enforces authorization before chunks ever enter LLM context, improves precision via hybrid + reranking, and verifies citations.',
        'filtering permissions after LLM generation or stripping source ACL metadata during ingestion leaks restricted documents.',
    ),
    'seq_fde_acl_rag_ground_w1': (
        'Retrieve top-20 chunks across all tenants without ACL filters → pass all 20 chunks into the LLM prompt → ask the system prompt to hide unauthorized facts → append unverified citations',
        'exposes unauthorized tenant chunks inside the LLM context window where prompt injection can exfiltrate them.',
        'exposes unauthorized tenant chunks inside the LLM context window where prompt injection can exfiltrate them.',
    ),
    'seq_fde_acl_rag_ground_w2': (
        'Strip ACL metadata during chunking to shrink index size → run dense-only search without lexical BM25 → skip cross-encoder reranking → check user permissions only when the user clicks a citation link',
        'discards document ACLs at index time so restricted text is already synthesized into the generated answer.',
        'discards document ACLs at index time so restricted text is already synthesized into the generated answer.',
    ),
    'seq_fde_acl_rag_ground_w3': (
        'Generate an ungrounded draft answer from base LLM memory first → search the vector index to find any superficially similar paragraph → attach that URL as a citation → log completion',
        'fabricates post-hoc citations for ungrounded LLM memory rather than grounding generation on ACL-filtered evidence.',
        'fabricates post-hoc citations for ungrounded LLM memory rather than grounding generation on ACL-filtered evidence.',
    ),

    # 4.3 — Safe Enterprise MCP Server & Tool Execution Lifecycle ("Orchestrate")
    'seq_fde_mcp_tool_safe_ok': (
        'Define narrow typed `MCP` schemas separating read vs mutating tools → exchange caller auth for a short-lived `OBO` token → validate arguments, idempotency & step caps server-side → gate risky writes on `HITL` approval + audit log',
        'combines narrow tool contracts, per-user least-privilege OBO tokens, server-side validation, and human approval on risky writes.',
        'sharing one static admin API key across all agent users or trusting LLM-generated SQL/arguments unvalidated invites LLM06 Excessive Agency.',
    ),
    'seq_fde_mcp_tool_safe_w1': (
        'Bind one shared root database service account to all `MCP` tools → expose a generic `run_raw_sql(query)` tool → let the LLM enforce RBAC in its system prompt → log tool calls asynchronously next day',
        'violates least privilege (`LLM06 Excessive Agency`) by exposing raw SQL over a shared superuser credential.',
        'violates least privilege (`LLM06 Excessive Agency`) by exposing raw SQL over a shared superuser credential.',
    ),
    'seq_fde_mcp_tool_safe_w2': (
        'Auto-execute mutating financial/clinical writes immediately → ask human operators for retroactive review after external APIs commit → add OBO token scoping later → omit idempotency keys on retries',
        'executes irreversible external writes before human approval and duplicates mutations during retry storms.',
        'executes irreversible external writes before human approval and duplicates mutations during retry storms.',
    ),
    'seq_fde_mcp_tool_safe_w3': (
        'Dump all 250 internal OpenAPI endpoints verbatim into a single agent context → return 5 MB raw JSON blobs from tools → skip step/token budgets → retry failed `500` calls infinitely',
        'overwhelms tool-selection accuracy, exhausts context windows with 5 MB payloads, and triggers unbounded retry loops.',
        'overwhelms tool-selection accuracy, exhausts context windows with 5 MB payloads, and triggers unbounded retry loops.',
    ),

    # 4.5 — Durable Stateful Agent / Workflow Saga & Recovery
    'seq_fde_durable_saga_ok': (
        'Persist workflow input & correlation ID to durable state → execute each external side effect with an idempotency key & checkpoint → run bounded backoff or compensating saga actions on failure → route unrecoverable runs to `DLQ`',
        'ensures crash-resilient state replay, duplicate-safe external calls, clean rollback/compensation, and operator visibility.',
        'holding multi-step state solely in process RAM loses partial progress on pod restarts and leaves orphaned external mutations.',
    ),
    'seq_fde_durable_saga_w1': (
        'Hold multi-step agent state only in Python local variables → re-run the entire workflow from step 1 without idempotency keys after a pod restart → ignore partial downstream writes → silence timeout alerts',
        'loses in-flight state on restart and double-charges or double-books non-idempotent downstream systems.',
        'loses in-flight state on restart and double-charges or double-books non-idempotent downstream systems.',
    ),
    'seq_fde_durable_saga_w2': (
        'Wrap 45 seconds of external LLM and third-party REST calls inside one `SERIALIZABLE` SQL transaction lock → block all concurrent table reads → roll back DB rows while leaving external REST side effects uncompensated',
        'exhausts DB connection pools by holding locks across slow LLM calls and fails to compensate committed external REST side effects.',
        'exhausts DB connection pools by holding locks across slow LLM calls and fails to compensate committed external REST side effects.',
    ),
    'seq_fde_durable_saga_w3': (
        'Fire all interdependent mutation steps concurrently without ordering → skip step checkpoints → swallow `HTTP 429` errors as empty `200 OK` strings → mark the workflow succeeded',
        'corrupts causal ordering and silently masks upstream throttling as false workflow success.',
        'corrupts causal ordering and silently masks upstream throttling as false workflow success.',
    ),

    # 5.2 (odd sets) — Progressive Enterprise AI Deployment (Shadow -> Canary -> Rollout)
    'seq_fde_canary_rollout_ok': (
        'Gate container build on CI golden evals + `SBOM`/CVE scan → replay live traffic side-effect-free in `Shadow` mode → shift `5%` `Canary` traffic with automated SLO/eval rollback gates → promote progressively to `100%`',
        'validates offline quality/security first, proves live distribution behavior safely in shadow mode, and bounds blast radius via SLO-gated canaries.',
        'swapping models or prompts directly to 100% traffic without offline gates, shadow replay, or automated rollback exposes every user to regressions.',
    ),
    'seq_fde_canary_rollout_w1': (
        'Edit production system prompts directly in the live cloud console → route `100%` of customer traffic immediately → wait for executive escalations to detect regressions → build an offline eval set next sprint',
        'pushes unversioned prompt edits straight to 100% traffic with zero CI eval gate or blast-radius containment.',
        'pushes unversioned prompt edits straight to 100% traffic with zero CI eval gate or blast-radius containment.',
    ),
    'seq_fde_canary_rollout_w2': (
        'Run Shadow mode while allowing shadow workers to execute real mutating `POST` calls against production ERP → skip Canary `5%` SLO monitoring → promote to `100%` without rollback automation',
        'causes duplicate real-world ERP mutations from shadow traffic that must remain strictly side-effect-free.',
        'causes duplicate real-world ERP mutations from shadow traffic that must remain strictly side-effect-free.',
    ),
    'seq_fde_canary_rollout_w3': (
        'Deploy an unsigned `:latest` container tag manually via `kubectl edit` → test only 3 happy-path prompts by hand → shift `100%` traffic → disable OpenTelemetry tracing to save CPU',
        'bypasses immutable IaC/digest traceability, statistical CI evals, progressive canarying, and production observability.',
        'bypasses immutable IaC/digest traceability, statistical CI evals, progressive canarying, and production observability.',
    ),

    # 5.5 (even sets) — Production Latency / Cost / Quality Incident Triage
    'seq_fde_incident_triage_ok': (
        'Stabilize impact via feature flag, canary rollback, or deterministic fallback → inspect `OpenTelemetry` span waterfalls (`TTFT, TPOT, RAG, tools, 429s`) → isolate root cause (`prompt bloat, index lag, quota`) → ship eval-gated fix',
        'prioritizes immediate SLO stabilization before span-level diagnosis and permanent regression-gated remediation.',
        'debugging live for hours while customers suffer `HTTP 504` timeouts violates enterprise incident response discipline.',
    ),
    'seq_fde_incident_triage_w1': (
        'Leave broken `P99` timeouts serving live users for 4 hours while experimenting with prompt tweaks in prod → skip span waterfall inspection → double retry counts on `429` errors → omit postmortem tests',
        'prolongs customer outage and amplifies `429` quota exhaustion via aggressive retry storms.',
        'prolongs customer outage and amplifies `429` quota exhaustion via aggressive retry storms.',
    ),
    'seq_fde_incident_triage_w2': (
        'Delete production OpenTelemetry logs to free disk space → upgrade to a 5x larger frontier model during a `TPM` quota outage → remove circuit breakers → redeploy without staging verification',
        'destroys diagnostic telemetry and worsens token-per-minute (`TPM`) saturation during an active incident.',
        'destroys diagnostic telemetry and worsens token-per-minute (`TPM`) saturation during an active incident.',
    ),
    'seq_fde_incident_triage_w3': (
        'Blame the model vendor publicly without checking trace spans → raise client HTTP timeouts to 10 minutes → hold database locks open during retries → close the incident without adding golden eval cases',
        'masks root causes, exhausts upstream worker threads with 10-minute timeouts, and leaves the regression untested.',
        'masks root causes, exhausts upstream worker threads with 10-minute timeouts, and leaves the regression untested.',
    ),

    # 6.1 — Production Evaluation Flywheel ("Prove")
    'seq_fde_eval_flywheel_ok': (
        'Curate a stratified golden set from sanitized client edge cases & SME labels → pair code graders with human-calibrated `LLM-as-judge` rubrics → gate CI/CD merges on regressions → harvest live operator overrides into new golden cases',
        'closes the continuous evaluation loop across offline CI gating, calibrated judges, and production failure harvesting.',
        'relying on vibe checks or uncalibrated LLM judges that never ingest real production failure modes misses domain drift.',
    ),
    'seq_fde_eval_flywheel_w1': (
        'Inspect 5 cherry-picked demo prompts manually (`vibe check`) → use the exact same prompt/model to grade itself without human calibration → skip CI gating → ignore production operator overrides',
        'suffers from tiny sample size, self-preference judge bias, zero CI regression protection, and blindness to live overrides.',
        'suffers from tiny sample size, self-preference judge bias, zero CI regression protection, and blindness to live overrides.',
    ),
    'seq_fde_eval_flywheel_w2': (
        'Copy raw unredacted production PII into public GitHub test fixtures → optimize solely for BLEU/ROUGE n-gram overlap on agent tool calls → disable online trace sampling after launch',
        'leaks regulated PII into Git, uses lexical metrics poorly suited to tool-calling semantics, and drops post-launch drift monitoring.',
        'leaks regulated PII into Git, uses lexical metrics poorly suited to tool-calling semantics, and drops post-launch drift monitoring.',
    ),
    'seq_fde_eval_flywheel_w3': (
        'Write 500 synthetic happy-path questions with zero adversarial or null cases → set CI pass threshold to `50%` → never measure human-judge Cohen kappa agreement → delete rejected operator drafts',
        'omits adversarial/edge distributions, tolerates 50% error rates, leaves judge drift unchecked, and discards rich human feedback signals.',
        'omits adversarial/edge distributions, tolerates 50% error rates, leaves judge drift unchecked, and discards rich human feedback signals.',
    ),

    # 6.5 — PoC-to-Production Handover & Sustainable Ownership Transfer
    'seq_fde_handover_prod_ok': (
        'Document architecture, SLO dashboards & failure runbooks → run shadowed on-call & game-day drills with client SREs → reinforce operator adoption (`ADKAR`) → transfer paging/IAM ownership & extract reusable patterns to core product',
        'eliminates FDE hero-dependency through operational readiness, joint game-days, operator reinforcement, and clean platform extraction.',
        'handing over undocumented scripts on the final Friday of an engagement guarantees post-handover abandonment.',
    ),
    'seq_fde_handover_prod_w1': (
        'Keep production deployments running under the FDE personal laptop credentials → email a slide deck on the final afternoon → skip client SRE game-days → hardcode client-specific `if customer == "X"` branches into core product',
        'creates dangerous FDE credential/hero dependency, leaves client SREs unprepared, and pollutes core product with bespoke forks.',
        'creates dangerous FDE credential/hero dependency, leaves client SREs unprepared, and pollutes core product with bespoke forks.',
    ),
    'seq_fde_handover_prod_w2': (
        'Transfer pager duty to client SREs on day 1 without runbooks or dashboards → mandate operator usage via executive email without workflow training → revoke FDE support immediately → abandon feedback loops',
        'dumps unobservable systems onto client SREs and triggers operator resistance by skipping ADKAR Knowledge/Ability/Reinforcement.',
        'dumps unobservable systems onto client SREs and triggers operator resistance by skipping ADKAR Knowledge/Ability/Reinforcement.',
    ),
    'seq_fde_handover_prod_w3': (
        'Fork the entire core platform repository per customer account → disable upstream security patches to avoid merge conflicts → keep the FDE permanently on call for every client → skip ROI measurement',
        'creates unmaintainable per-client repo sprawl that misses security patches and prevents scalable FDE leverage.',
        'creates unmaintainable per-client repo sprawl that misses security patches and prevents scalable FDE leverage.',
    ),
}
