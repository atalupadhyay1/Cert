"""Architectural option catalog for the Claude Certified Architect – Professional (CCAR-P) question bank.

Every option pairs a concise, decision-grade label with an architectural explanation
of what that pattern, mechanism, or control actually solves in a production Claude
system — so distractors represent real capabilities applied to the wrong constraint.
"""
TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term key: {key}')
    TERMS[key] = (label, meaning)


# --- Domain 1: Solution Design & Architecture ---
t('arch_prompt_chain_gates',
  'Implement a deterministic prompt-chaining workflow with programmatic validation gates between fixed stages',
  'Prompt chaining fits predictable, ordered multi-step transformations where code checks intermediate outputs before advancing, bounding latency and audit risk.')
t('arch_autonomous_open_agent',
  'Deploy an open-ended autonomous agent loop that dynamically plans, branches, and chooses its own stopping criteria',
  'Open-ended autonomous agents fit unpredictable exploration where step count and tool sequence cannot be predetermined, trading higher cost, latency, and variance for flexibility.')
t('arch_augmented_single_call',
  'Use a single augmented Claude call grounded in retrieved context and constrained by a strict output schema',
  'A single retrieval-augmented call with structured output is the simplest sufficient pattern when one reasoning pass over grounded context resolves the request.')
t('arch_router_specialized',
  'Place a lightweight classification router in front of specialized downstream handlers and model tiers',
  'Routing separates distinct input intents or complexity classes upfront so simple requests hit fast deterministic or compact paths while complex cases reach specialized prompts.')
t('arch_parallel_sectioning',
  'Decompose into independent parallel subtasks (sectioning) executed concurrently and merged deterministically',
  'Parallel sectioning cuts wall-clock latency and isolates focused attention when subtasks have no sequential data dependency.')
t('arch_parallel_voting',
  'Run independent parallel evaluations (voting) with diverse rubrics and require consensus before acting',
  'Parallel voting trades higher token spend for higher precision on high-stakes binary or compliance judgments where single-pass false negatives are costly.')
t('arch_orchestrator_workers',
  'Use an orchestrator-workers architecture where a lead agent delegates dynamically scoped subtasks to isolated subagents',
  'Orchestrator-workers fits complex tasks whose decomposition depends on runtime findings and whose search/read volume would pollute a single context window.')
t('arch_evaluator_optimizer',
  'Apply an evaluator-optimizer loop with explicit rubric criteria and a hard iteration cap',
  'Evaluator-optimizer improves output quality when clear grading criteria exist and iterative refinement measurably improves drafts within a bounded retry budget.')
t('arch_deterministic_rules_engine',
  'Handle the workload in a deterministic rules/SQL engine rather than invoking an LLM',
  'Exact arithmetic, fixed schema validation, and deterministic threshold lookups belong in traditional code for zero hallucination risk, sub-millisecond latency, and audit certainty.')
t('arch_hybrid_code_plus_claude',
  'Combine deterministic code for calculations, eligibility checks, and state transitions with Claude strictly for unstructured synthesis',
  'Separating deterministic computation in application code from unstructured language reasoning in Claude eliminates arithmetic hallucinations while preserving nuanced synthesis.')
t('arch_async_queue_feedback',
  'Decouple ingestion onto a durable event queue with idempotent workers, post-processing verification, and outcome feedback capture',
  'Asynchronous event queues absorb bursty arrival spikes, isolate retryable upstream timeouts, and capture verified downstream outcomes for continuous evaluation.')
t('arch_sync_monolith_call',
  'Process the entire multi-document workflow inside one synchronous blocking HTTP request with a single giant prompt',
  'Stuffing multi-stage ingestion, reasoning, and side effects into one synchronous request risks gateway timeouts, context dilution, and all-or-nothing retry waste.')
t('arch_subagent_summary_handoff',
  'Isolate heavy search and document inspection inside subagents that return structured evidence summaries and citations to the lead agent',
  'Subagent context isolation prevents tens of thousands of exploratory tokens from accumulating in the coordinator prompt while preserving verifiable evidence.')
t('arch_shared_transcript_mesh',
  'Broadcast the full raw tool transcript of every peer agent into a shared all-to-all group conversation on every turn',
  'Broadcasting raw intermediate transcripts across all agents multiplies token cost quadratically and propagates noisy intermediate hypotheses across peers.')
t('arch_external_state_checkpoint',
  'Persist the execution plan and completed phase checkpoints to external state storage so resumed or delegated runs recover cleanly',
  'Externalized state checkpoints let long-horizon workflows survive context compaction, worker restarts, and human approval pauses without losing their plan.')
t('arch_sla_tier_budgeting',
  'Partition latency and reliability budgets per pipeline stage with circuit breakers, bounded retries, and graceful fallback paths',
  'Explicit per-stage latency budgets and circuit breakers ensure end-to-end p95/p99 SLAs hold even when retrieval or downstream tools degrade.')
t('arch_unbounded_retry_loop',
  'Allow agents unlimited self-correction retries until confidence exceeds 0.99 to maximize accuracy',
  'Unbounded retry loops blow through latency SLAs and token budgets during ambiguous or malformed inputs without guaranteeing factual convergence.')

# Pipeline Execution-Layer Classification options (Pre-Processing / Model Stage / Post-Processing)
t('layer_correct_fin_pipeline',
  'Pre-Processing: OCR normalization, PII tokenization, and covenant retrieval; Model Stage: grounded clause variance synthesis; Post-Processing: deterministic DSCR ratio calculation, JSON schema check, and ledger event emission',
  'Pre-processing prepares clean, authorized, minimized inputs; the model stage performs unstructured language reasoning; post-processing runs deterministic math, validation, and side effects.')
t('layer_wrong_model_math',
  'Pre-Processing: JSON schema validation; Model Stage: raw PDF OCR, floating-point DSCR ratio math, and direct ledger mutation; Post-Processing: PII tokenization and retrieval',
  'Placing deterministic financial ratio arithmetic and direct ledger writes in the model stage while deferring PII masking and retrieval to post-processing inverts execution boundaries.')
t('layer_wrong_post_auth',
  'Pre-Processing: LLM narrative synthesis; Model Stage: deterministic regex PII masking; Post-Processing: borrower entitlement checks and initial vector indexing',
  'Running synthesis before authorization and using an LLM for regex masking wastes tokens and exposes unauthorized records to the model context.')
t('layer_wrong_all_in_model',
  'Pre-Processing: none (pass raw multipart bytes directly); Model Stage: entitlement verification, PII scrubbing, SQL balance lookup, synthesis, and wire execution; Post-Processing: none',
  'Collapsing security checks, deterministic lookups, and irreversible side effects into an unguarded model call violates defense-in-depth and least privilege.')

t('layer_correct_health_pipeline',
  'Pre-Processing: patient-consent check, Safe Harbor PHI de-identification, and clinical guideline retrieval; Model Stage: structured prior-authorization rationale drafting with citations; Post-Processing: ICD-10/CPT code allowlist validation, citation span check, and reviewer queue routing',
  'Consent verification and PHI minimization must precede model invocation, synthesis stays grounded in retrieved guidelines, and deterministic code/citation validation gates downstream routing.')
t('layer_wrong_health_swap',
  'Pre-Processing: citation span verification; Model Stage: HIPAA consent lookup and raw database export; Post-Processing: initial guideline retrieval and prompt construction',
  'Verifying citations before generation and retrieving guidelines after generation breaks data flow causality and exposes unconsented records to the model.')

t('layer_correct_retail_pipeline',
  'Pre-Processing: locale detection, SKU catalog attribute lookup, and profanity/injection screening; Model Stage: multilingual product copy generation in strict JSON; Post-Processing: banned-claim regex check, price-parity verification against ERP, and CMS staging publish',
  'Deterministic catalog lookups and input screening feed grounded generation, while deterministic price-parity and regulatory-claim checks gate CMS publication.')
t('layer_wrong_retail_swap',
  'Pre-Processing: CMS staging publication; Model Stage: ERP inventory lock and tax calculation; Post-Processing: locale detection and SKU attribute lookup',
  'Publishing before generation and delegating deterministic tax math to the model reverses pipeline stages and risks pricing errors.')

t('layer_correct_sre_pipeline',
  'Pre-Processing: alert deduplication, secret scrubbing from stack traces, and runbook chunk retrieval; Model Stage: root-cause hypothesis ranking with cited log evidence; Post-Processing: allowlisted read-only diagnostic command check and PagerDuty ticket enrichment',
  'Deduplicating alerts and scrubbing secrets before model calls protects credentials and token budgets, while command allowlist validation belongs in deterministic post-processing.')
t('layer_wrong_sre_swap',
  'Pre-Processing: PagerDuty ticket closure; Model Stage: regex secret scrubbing on raw core dumps; Post-Processing: alert deduplication and initial runbook retrieval',
  'Sending unscrubbed secrets into the model and deduplicating alerts only after model inference leaks credentials and multiplies token spend.')

t('layer_correct_legal_pipeline',
  'Pre-Processing: matter-wall ACL filtering, clause-boundary segmentation, and hybrid precedent retrieval; Model Stage: change-of-control risk extraction in schema-bound JSON; Post-Processing: cross-reference anchor verification, confidence threshold check, and counsel review queue dispatch',
  'Ethical-wall ACL filtering must happen before context assembly, clause interpretation belongs in the model stage, and deterministic anchor/threshold gates govern counsel routing.')
t('layer_wrong_legal_swap',
  'Pre-Processing: counsel review queue dispatch; Model Stage: ethical-wall ACL enforcement over all firm matters; Post-Processing: clause-boundary segmentation and hybrid retrieval',
  'Asking the model to enforce matter-level ethical walls over unauthorized documents already in context is a critical authorization flaw.')

t('layer_correct_grid_pipeline',
  'Pre-Processing: sensor telemetry downsampling, asset-ID normalization, and maintenance manual retrieval; Model Stage: fault-tree diagnostic summary and draft work-order steps; Post-Processing: lockout-tagout safety rule validation, parts-stock lookup, and CMMS draft creation',
  'High-frequency sensor streams must be downsampled deterministically before prompting, while safety-interlock validation must execute deterministically after drafting.')
t('layer_wrong_grid_swap',
  'Pre-Processing: lockout-tagout sign-off; Model Stage: raw 10-kHz waveform FFT math and breaker actuation; Post-Processing: sensor downsampling and manual retrieval',
  'Feeding raw high-frequency telemetry to an LLM for FFT math and direct breaker actuation violates both latency physics and industrial safety boundaries.')

# Candidate Use-Case Suitability options (Yes vs No patterns)
t('suit_yes_unstructured_synthesis',
  'Synthesizing conflicting clauses and exceptions across multi-document unstructured agreements with cited evidence spans',
  'Claude excels when inputs are unstructured, phrasing varies across documents, nuanced semantic comparison is required, and cited output assists human decision-makers.')
t('suit_yes_ambiguous_triage',
  'Classifying free-form inbound narratives with multi-intent ambiguity, extracting structured entities, and drafting grounded responses',
  'Ambiguous natural-language triage with structured entity extraction and grounded drafting plays directly to frontier language comprehension.')
t('suit_yes_code_legacy_comprehension',
  'Summarizing cross-module control flow in undocumented legacy repositories and drafting unit-test harnesses for human code review',
  'Code comprehension, cross-file explanation, and test scaffolding with deterministic compiler/test verification are high-value Claude workloads.')
t('suit_yes_multilingual_policy_qa',
  'Answering employee or customer policy questions across multilingual handbooks using retrieval-augmented generation with inline citations',
  'Cross-lingual grounded question answering with source citations leverages semantic understanding while keeping answers verifiable.')
t('suit_no_subms_numeric_ml',
  'Scoring 50,000 tabular telemetry or card-swipe feature vectors per second under a strict 3-millisecond p99 latency budget',
  'High-throughput, sub-10ms tabular feature scoring requires lightweight classical ML or compiled in-memory models, not autoregressive LLM inference.')
t('suit_no_exact_ledger_sql',
  'Computing exact double-entry general-ledger trial balances, tax withholdings, and amortization schedules to the cent',
  'Exact deterministic accounting and arithmetic belong in SQL or decimal financial libraries where rounding and audit rules are mathematically guaranteed.')
t('suit_no_hard_realtime_safety_plc',
  'Executing closed-loop 5-millisecond industrial PLC or medical-device actuator shutoffs without deterministic safety interlocks',
  'Hard real-time physical safety loops require deterministic certified firmware and hardware interlocks, never probabilistic model inference.')
t('suit_no_xsd_crypto_verify',
  'Validating cryptographic JWT signatures and deterministic ISO XML schema conformance on API gateway traffic',
  'Cryptographic verification and formal grammar validation must use deterministic standards-compliant libraries for 100% soundness and microsecond speed.')

# --- Domain 2: Claude Models, Prompting & Context Engineering ---
t('mod_tiered_haiku_sonnet_opus',
  'Route high-volume classification and extraction to Claude Haiku, standard tool workflows to Claude Sonnet, and ambiguous deep-reasoning escalations to Claude Opus',
  'Tiered model routing aligns model capability to task difficulty, preserving frontier quality on hard edge cases while keeping median latency and token cost low.')
t('mod_opus_everywhere',
  'Standardize every classification, health-check, and extraction call on the largest frontier model with maximum extended thinking',
  'Running trivial high-QPS classification through the largest model with maximal thinking inflates latency and cost by an order of magnitude without measurable lift.')
t('mod_haiku_only_complex',
  'Force multi-hop legal, architectural, or scientific synthesis onto the smallest model with zero context grounding to minimize unit token price',
  'Under-provisioning model capability on reasoning-dense tasks drives up downstream human rework, retry loops, and business error cost.')
t('mod_batch_api_async',
  'Submit non-urgent bulk workloads through the asynchronous Message Batches API to decouple rate limits and cut token cost by roughly half',
  'The Message Batches API processes large offline evaluations, backfills, and nightly document runs asynchronously within up to 24 hours at steep cost savings.')
t('prompt_xml_delimiters_hierarchy',
  'Separate trusted system instructions from untrusted user/retrieved content using distinct XML tags and explicit conflict-resolution priority rules',
  'Clear structural boundaries (such as XML tags) and explicit precedence rules help Claude distinguish authoritative system instructions from untrusted data payloads.')
t('prompt_strict_json_schema',
  'Enforce structured outputs via strict JSON schema / tool-input schema validation rather than relying on prose formatting requests alone',
  'Constrained structured outputs and strict tool schemas guarantee syntactic conformance for downstream parsers without brittle regex cleanup.')
t('prompt_fewshot_boundary_cases',
  'Include 3 to 5 curated few-shot examples targeting ambiguous boundary cases that prose instructions alone fail to disambiguate',
  'Targeted few-shot examples calibrate edge-case classification boundary behavior far more reliably than stacking redundant negative instructions.')
t('prompt_preserve_thinking_blocks',
  'Pass assistant thinking blocks back unmodified across multi-turn tool loops and tune thinking/effort budgets only for reasoning-heavy steps',
  'Preserving returned thinking blocks across tool-use turns avoids costly re-reasoning and preserves prompt/context cache validity on modern Claude models.')
t('prompt_strip_rewrite_history',
  'Rewrite earlier tool results and strip assistant thinking blocks on every turn to shave a few hundred input tokens',
  'Mutating earlier turns or dropping assistant thinking blocks invalidates prompt cache prefixes and forces Claude to regenerate prior reasoning on every step.')
t('ctx_server_compaction_summary',
  'Trigger threshold-based server-side compaction (or structured phase summaries) while persisting critical plan state to external memory',
  'Threshold compaction compresses older turns cleanly once context crosses a high-water mark, preventing context rot while keeping recent turns intact.')
t('ctx_batch_screenshot_pruning',
  'Prune stale bulky tool outputs or screenshots in periodic batches rather than dropping one item per turn so cache prefixes stay stable between compactions',
  'Dropping one old message on every single turn mutates the prompt prefix every turn and destroys prompt cache hits; batched pruning preserves cache reuse.')
t('ctx_cache_static_first',
  'Order immutable tool definitions, system instructions, and static reference documents before dynamic per-request inputs and place cache_control breakpoints at stable prefix boundaries',
  'Prompt caching matches exact byte-identical prefixes from the beginning of the request, so static content must precede per-turn dynamic content.')
t('ctx_cache_dynamic_first',
  'Inject a per-request UUID, current millisecond timestamp, and user query at line 1 of the system prompt ahead of static policy documents',
  'Placing per-request dynamic tokens at the start of the system prompt mutates byte 1 on every call and reduces prompt cache hit rates to zero.')
t('ctx_skills_progressive_load',
  'Package domain-specific SOPs and schemas into modular Agent Skills so only lightweight descriptions load initially and full instructions load on demand',
  'Skills implement progressive disclosure: session startup pays only for short skill metadata until a task invokes the full workflow instructions.')

# --- Domain 3: Integration ---
t('int_least_priv_remove_tools',
  'Remove unneeded write, refund, and administrative delete tools entirely from the agent configuration so only role-required tools exist',
  'Least privilege eliminates unnecessary capabilities at the architectural boundary rather than relying on prompts or audit logs to deter misuse.')
t('int_detective_log_only',
  'Retain all privileged administrative tools on the agent and rely on audit logging plus system-prompt warnings never to call them',
  'Audit logs are detective after-the-fact controls and system prompts are probabilistic; neither removes the blast radius of an exposed destructive tool.')
t('int_obo_scoped_oauth',
  'Propagate short-lived, user-scoped on-behalf-of (OBO) credentials verified deterministically by the tool gateway on every call',
  'Identity propagation and server-side authorization ensure an agent can never read records or invoke actions beyond the authenticated caller permissions.')
t('int_shared_admin_apikey',
  'Authenticate every MCP server and database tool with a single static superuser API key and ask Claude in the system prompt to filter by user_id',
  'Sharing a privileged service credential and trusting prompt-level tenant filtering creates a classic confused-deputy vulnerability under prompt injection.')
t('int_pre_retrieval_acl_filter',
  'Enforce tenant and document-level ACL metadata filters inside the retrieval engine before any chunks enter Claude context',
  'Authorization filtering must happen in the query/index layer before context assembly; post-generation redaction cannot undo unauthorized context exposure.')
t('int_network_egress_allowlist',
  'Run agent tool sandboxes inside an isolated network boundary with explicit egress allowlists and brokered credential injection',
  'Network egress allowlisting and external credential brokering prevent exfiltration even if untrusted inputs hijack agent execution.')
t('int_mcp_standardized_gateway',
  'Expose shared enterprise systems through versioned MCP servers with typed schemas, centralized auth, and transport governance',
  'Model Context Protocol standardizes how multiple agents and developer tools connect to enterprise resources without bespoke N-by-M adapter glue.')
t('int_direct_rest_deterministic',
  'Invoke a single internal REST/gRPC microservice directly from deterministic application code when only one fixed endpoint is ever called',
  'When deterministic application code calls one fixed internal endpoint with no dynamic tool selection or cross-agent reuse, a direct typed API client avoids unnecessary protocol overhead.')
t('int_defer_loading_tool_search',
  'Keep 3 to 5 core tools loaded with prompt caching and mark the remaining catalog with defer_loading: true alongside the Tool Search Tool',
  'Deferred tool loading excludes infrequent schemas from the initial prefix and appends discovered tools inline as tool_reference blocks, cutting input tokens while preserving prompt cache hits.')
t('int_monolithic_60_tools',
  'Serialize all 60+ full JSON tool schemas into every single request regardless of user intent',
  'Loading dozens of large tool definitions on every turn inflates TTFT, consumes tens of thousands of tokens, and degrades tool-selection precision.')
t('int_contextual_chunking_rag',
  'Split documents along semantic section boundaries and prepend concise document/section context to each chunk before hybrid indexing (Contextual Retrieval)',
  'Structure-aware chunking plus contextual headers preserves cross-paragraph referents like pronouns, effective dates, and entity scope that naive fixed-token splits lose.')
t('int_hybrid_bm25_vector_rerank',
  'Combine lexical BM25 keyword search with dense vector similarity via reciprocal rank fusion followed by cross-encoder reranking',
  'Hybrid retrieval pairs exact SKU/part-number/statute matching from BM25 with semantic recall from embeddings, while reranking sharpens top-k precision.')
t('int_otel_distributed_tracing',
  'Emit OpenTelemetry spans correlating request ID, prompt/template version, cache read/write tokens, retrieval chunk IDs, and per-tool latency with PII redaction',
  'Structured distributed tracing links every model turn, cache event, retrieved chunk, and tool call for fast root-cause diagnosis without leaking raw PII.')

# --- Domain 4: Evaluation, Testing & Optimization ---
t('eval_composite_scorecard',
  'Track a balanced scorecard pairing task accuracy and citation faithfulness with p95 TTFT/end-to-end latency, cost per successful task, and adversarial safety pass rate',
  'Production LLM readiness requires joint optimization across quality, grounding, latency percentiles, unit economics, and safety — never a single aggregate metric.')
t('eval_mixed_graders_calibrated',
  'Combine deterministic code/schema assertions for objective rules with LLM-as-judge rubrics calibrated regularly against blind human expert ratings',
  'Deterministic graders verify exact structure and invariants cheaply, while human-calibrated LLM rubrics scale nuanced quality scoring without unanchored judge drift.')
t('eval_pass_hat_k_consistency',
  'Measure multi-trial consistency (such as pass^k across repeated runs) alongside single-run accuracy on stateful tool-use benchmarks',
  'In customer-facing agent workflows, succeeding once in k tries (pass@k) masks flakiness; consistent success across all k trials (pass^k) measures operational reliability.')
t('eval_shadow_canary_ab',
  'Run offline golden regression gates first, validate latency/error invariants in shadow traffic, and ramp an online A/B canary with automated rollback thresholds',
  'Staged evaluation from offline golden sets to shadow traffic and guarded A/B ramps catches regressions before full customer exposure.')
t('eval_diag_retrieval_first',
  'Inspect retrieval recall, index freshness, and embedding-model parity between indexing and querying before altering prompts or swapping models',
  'When hallucinations spike right after a corpus refresh or re-index while model version and prompts are unchanged, broken chunking or mismatched embeddings are the primary suspect.')
t('eval_diag_stage_isolation',
  'Evaluate retrieval recall/precision independently from generation faithfulness given oracle context to isolate whether misses originate in search or prompting',
  'Component-level evaluation separates "right context was never retrieved" from "right context was retrieved but misread by the prompt/model."')
t('eval_cost_cache_route_concise',
  'Enable prefix prompt caching, apply tiered model routing, bound output verbosity/max_tokens, and shift offline jobs to Message Batches',
  'Combining cache reuse, right-sized routing, bounded output tokens, and batch execution cuts latency and spend without discarding required business context.')
t('eval_blind_context_truncation',
  'Truncate authoritative policy documents to the first 500 tokens and drop all few-shot examples without running regression evaluations',
  'Blindly chopping authoritative rules to save input tokens causes silent compliance regressions and costly downstream escalations.')
t('eval_drift_alerts_canary',
  'Monitor prompt-cache read ratios, retrieval similarity distributions, refusal spikes, and scheduled synthetic canary evaluations with automated alerts',
  'Proactive telemetry on cache hit drops, retrieval score decay, and synthetic canaries surfaces silent regressions hours before customer complaints accumulate.')

# --- Domain 5: Governance, Safety & Risk Management ---
t('gov_layered_guardrails',
  'Layer deterministic input screening, XML untrusted-data isolation, pre-execution deterministic tool policy hooks, and post-generation output/citation checks',
  'Defense-in-depth combines fast deterministic input/output filters with strict tool-execution gates so no single prompt bypass compromises downstream systems.')
t('gov_indirect_injection_defense',
  'Treat all retrieved documents, emails, and ticket bodies as untrusted data, strip or quarantine hidden instructions, and require deterministic policy checks before external tool side effects',
  'Indirect prompt injection enters through third-party data sources; isolating untrusted content and gating side-effecting tools stops data exfiltration and unauthorized actions.')
t('gov_hitl_irreversible_gate',
  'Pause execution deterministically before high-impact or irreversible tool actions (and before each consequential block in batched actions) for authenticated human approval with cited evidence',
  'Risk-tiered human-in-the-loop gates bind human sign-off to high-severity actions while letting low-risk read/draft tasks flow automatically.')
t('gov_hitl_rubberstamp_all',
  'Route 100% of routine low-risk drafts into a single unprioritized human queue showing only a thumbs-up button without source citations',
  'Flooding reviewers with trivial items and omitting source evidence induces alert fatigue and automation bias, degrading oversight on the rare high-risk cases.')
t('gov_zdr_regional_baa',
  'Deploy on contractual Zero Data Retention (ZDR) endpoints in approved regional boundaries (with HIPAA BAA / GDPR DPA / FedRAMP-authorized cloud platform as required) and scrub PII from telemetry',
  'Regulatory compliance requires matching contractual retention guarantees, sovereign regional routing, and log hygiene across every data store, cache, and trace sink.')
t('gov_vector_erasure_lineage',
  'Maintain document-to-chunk lineage keys across primary stores, vector indexes, and evaluation logs so GDPR erasure or tenant offboarding purges derived embeddings deterministically',
  'Right-to-erasure obligations extend beyond relational rows to derived chunks, embeddings, and cached evaluation artifacts.')
t('gov_citations_fairness_audit',
  'Enable native source citations for verifiable provenance, disclose AI assistance transparently, and audit error/escalation rates across demographic and language cohorts',
  'Responsible AI combines verifiable grounding via citations, transparent user disclosure, and disaggregated cohort fairness metrics.')

# --- Domain 6: Stakeholder Communication & Lifecycle Management ---
t('stk_discovery_baseline_audit',
  'Audit real production document samples, measure current human inter-rater agreement and latency baselines, and map hard regulatory/security boundaries before selecting patterns',
  'Structured discovery anchors architecture in real corpus messiness, measurable human baselines, and non-negotiable compliance constraints.')
t('stk_tradeoff_decision_matrix',
  'Present stakeholders with a quantified option matrix comparing accuracy, p95 latency, unit cost, blast radius, and engineering maintenance across candidate architectures',
  'Role-tailored trade-off matrices turn subjective debates about autonomy or model size into transparent business and risk decisions.')
t('stk_segmented_sla_alignment',
  'Disaggregate SLA reporting by document/intent complexity tier, auto-complete high-confidence tiers, route hard low-confidence segments to human review, and set a recalibration cadence',
  'Blended accuracy averages hide poor performance on high-risk minority segments; segmented SLAs with confidence routing align expectations honestly.')
t('stk_promise_100_autonomous',
  'Commit to a 99.99% hallucination-free guarantee across all unseen edge cases with zero human review from day one to secure executive sponsorship',
  'Promising near-zero LLM error without human fallback on complex edge cases guarantees stakeholder trust failure after launch.')
t('stk_adr_runbook_contracts',
  'Deliver Architecture Decision Records (ADRs), versioned prompt/tool schemas, pinned model IDs, and operational failure-mode runbooks during implementation handoff',
  'Executable interface contracts, ADRs, and incident runbooks let platform and operations teams run and evolve the system safely after architect handoff.')
t('stk_phased_lifecycle_gates',
  'Enforce explicit exit criteria across Discovery -> Offline Eval -> Shadow Pilot -> Bounded Production -> General Availability, including pinned model-upgrade regression rehearsals',
  'Stage-gated lifecycle governance prevents unproven PoCs from jumping straight to production and ensures model-version migrations never ship blind.')
t('stk_feedback_to_golden_set',
  'Capture structured user edits, thumbs-down reasons, and human-override rationales and curate recurring failure clusters into the versioned golden evaluation dataset',
  'Closing the loop from production user corrections into regression test suites turns operational feedback into compounding quality gains.')

# --- Domain 7: Developer Productivity & Operational Enablement ---
t('dev_claudemd_hooks_managed',
  'Enforce organization-wide guardrails via managed Claude Code policies and deterministic PreToolUse/PostToolUse hooks while keeping CLAUDE.md concise for repo conventions',
  'Managed policies cannot be overridden locally, hooks guarantee deterministic checks like linting or command blocking, and concise CLAUDE.md avoids session-start context bloat.')
t('dev_skills_subagents_mcp_team',
  'Check shared .mcp.json, reusable .claude/skills/ workflows, and isolated .claude/agents/ review subagents into version control with least-privilege tool allowlists',
  'Version-controlled project MCP configs, on-demand Skills, and context-isolated Subagents standardize team workflows without bloating every session.')
t('dev_plan_mode_headless_ci',
  'Use Plan Mode for human architectural review before multi-file refactors and run headless Claude Code / Agent SDK jobs in CI with read-only or sandboxed permissions',
  'Separating read-only architectural planning from code mutation and sandboxing CI agents accelerates engineering throughput without unreviewed repo drift.')
t('dev_bypass_permissions_root',
  'Run developer and CI coding agents as root with permission checks bypassed and paste production database credentials directly into shared CLAUDE.md files',
  'Disabling permission gates and committing live credentials into always-loaded prompt files creates severe supply-chain and production data destruction risk.')
t('dev_debug_batch_tool_use_id',
  'Ensure the agent loop returns a matching tool_result block for every tool_use_id in a parallel/batched turn and correlate request_id traces across MCP timeouts',
  'Leaving any tool_use block unanswered in a multi-tool turn triggers an immediate API invalid_request_error on the next call; full correlation tracing pinpoints the failing call.')

# Sound Architectural Practice statement options (for multi-select Yes/No adaptation items)
t('prac_yes_prefix_cache_order',
  'Place immutable tool schemas and static policy instructions ahead of per-turn user messages so ephemeral prompt cache prefixes stay byte-identical across turns',
  'Static-before-dynamic ordering is essential for prompt cache hits, reducing both time-to-first-token and input token cost.')
t('prac_yes_defer_rare_tools',
  'Mark infrequently used tools in large catalogs with defer_loading: true so dynamic discovery appends tool_reference blocks inline without invalidating cached prefixes',
  'Deferred loading scales agents to dozens of tools without paying upfront token cost or breaking prompt and strict-grammar caches.')
t('prac_yes_deterministic_hooks',
  'Enforce security invariants, command allowlists, and PII redaction in deterministic application/hook code rather than relying solely on system-prompt prohibitions',
  'Security and compliance invariants require deterministic code enforcement because prompt instructions alone remain probabilistically vulnerable to adversarial inputs.')
t('prac_yes_otel_redacted_spans',
  'Propagate correlation trace IDs across gateway, retrieval, Claude API usage metadata, and MCP tool calls while redacting raw PII before exporting telemetry',
  'Redacted end-to-end distributed traces provide latency, token, and cache diagnostics at concurrency scale without creating secondary compliance exposure.')
t('prac_yes_xml_untrusted_fence',
  'Wrap retrieved chunks and external user payloads inside dedicated XML tags with explicit instructions never to follow directives embedded inside data blocks',
  'Structural XML fencing clearly separates untrusted data payloads from authoritative system instructions.')
t('prac_yes_schema_output_check',
  'Validate model outputs deterministically against strict JSON schemas and citation source spans before committing downstream state changes',
  'Post-generation schema and citation verification catches malformed or ungrounded outputs before side effects occur.')
t('prac_no_timestamp_prefix_top',
  'Prepend a millisecond request timestamp and random session nonce to line 1 of the system prompt on every API call to aid log correlation',
  'Prepending dynamic per-call strings at byte 0 invalidates the entire prompt cache prefix on every request; trace IDs belong in HTTP/telemetry metadata instead.')
t('prac_no_prune_one_msg_turn',
  'Delete exactly the single oldest conversation turn on every request so the prompt shifts by one message per turn while keeping cache_control on the system prompt',
  'Sliding-window deletion on every single turn mutates the message prefix every turn and defeats multi-turn conversation cache reuse compared with batched compaction.')
t('prac_no_prompt_only_rbac',
  'Pass full multi-tenant database tables into Claude context and rely on a bolded system-prompt rule never to mention rows belonging to other tenants',
  'Prompt-level tenant filtering is not an access control boundary; unauthorized records must never enter context in the first place.')
t('prac_no_raw_pii_stdout_logs',
  'Write full unredacted user prompts, bearer tokens, and raw tool payloads to world-readable stdout logs across all worker pods for easier debugging',
  'Logging raw PII and bearer credentials to shared stdout violates security, HIPAA/GDPR minimization, and secret-hygiene standards.')
t('prac_no_drop_thinking_turns',
  'Strip returned assistant thinking blocks from conversation history between tool calls in a single agent loop to save context space',
  'Dropping thinking blocks mid-loop invalidates server-side reasoning continuity and forces Claude to spend output tokens regenerating prior reasoning.')
t('prac_no_single_agent_80_tools',
  'Attach all 80 heterogeneous read/write tools with overlapping prose descriptions to one agent without deferred loading or subagent scoping',
  'Overloading one agent with dozens of overlapping read/write tools bloats context and sharply increases misrouted or over-privileged tool calls.')
