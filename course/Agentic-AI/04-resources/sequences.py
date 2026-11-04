"""Ordered 4-step sequence terms (kind='O') for Agentic AI 6x100 practice sets.

Each group defines 1 `_ok` key and 3 plausible `_w1.._w3` sequence distractors (`<= 238` chars per label).
"""

SEQUENCE_TERMS = {
    # 1.3 — Multi-Agent Supervisor / A2A Delegation & Context-Isolated Handoff
    'seq_aai_multiagent_handoff_ok': (
        'Discover specialist capabilities via signed `Agent Card` → dispatch scoped `Task` with bounded budget & `OBO` token → execute inside isolated worker state → return typed `Artifact` summary to supervisor',
        'verifies peer identity first, delegates least-privilege work into an isolated context window, and returns a compact typed artifact.',
        'sharing full raw conversation history and root credentials across unverified peer agents triggers token explosion and ASI03/ASI07 exposure.',
    ),
    'seq_aai_multiagent_handoff_w1': (
        'Broadcast full raw chat history to all peer agents → let every worker mutate global shared state concurrently → check `Agent Card` signatures post-write → return concatenated raw tool logs',
        'never correct: concurrent uncoordinated writes and raw-log dumps corrupt state and explode token budgets.',
        'broadcasting full history and mutating shared state before verifying peer cards causes race conditions, context bloat, and spoofing.',
    ),
    'seq_aai_multiagent_handoff_w2': (
        'Pass supervisor root API key to untrusted peer → run unbounded peer-to-peer chat loop → skip schema validation on returned prose → forward unverified output directly to end user',
        'never correct: forwarding root keys and uncapped peer loops invite ASI03 privilege abuse and ASI08 cascading failures.',
        'delegating root credentials into an uncapped peer chat loop violates least privilege and cascades hallucinations.',
    ),
    'seq_aai_multiagent_handoff_w3': (
        'Execute mutating external tools inside supervisor first → discover specialist `Agent Card` afterward → copy 100k-token scratchpad into every sub-agent → retry failed tasks infinitely',
        'never correct: mutating state before capability discovery and copying 100k scratchpads reverses safe orchestration order.',
        'firing external mutations prior to specialist discovery and duplicating massive scratchpads wastes tokens and corrupts state.',
    ),

    # 2.2 — MCP (2026-07-28) Stateless Streamable HTTP & OAuth 2.1 Execution Flow
    'seq_aai_mcp_streamable_auth_ok': (
        'Fetch `CIMD` / OAuth 2.1 metadata & validate `RFC 9207` `iss` → send `Streamable HTTP` request with `_meta`, `Mcp-Method` & `Mcp-Name` headers → enforce server-side JSON Schema & `OBO` scopes → return compact typed tool result',
        'follows the 2026-07-28 stateless MCP core: hardened OAuth 2.1 + RFC 9207 issuer validation, routing headers, and server-side schema/scope checks.',
        'skipping OAuth issuer validation or trusting raw unvalidated LLM arguments exposes MCP servers to token mix-up and ASI02 tool misuse.',
    ),
    'seq_aai_mcp_streamable_auth_w1': (
        'Accept unsigned bearer token without `iss` check → parse full JSON body at edge proxy without `Mcp-Method` headers → execute raw shell arguments as root → dump 50-MB response into context',
        'never correct: missing issuer checks, root shell execution, and 50-MB context dumps break MCP security and ergonomics.',
        'omitting RFC 9207 `iss` validation and running unvalidated root commands creates severe token-confusion and RCE vulnerabilities.',
    ),
    'seq_aai_mcp_streamable_auth_w2': (
        'Embed static org-admin PAT in `AGENTS.md` → pin sticky TCP sessions to one non-HA process → skip server-side input validation → rely on system prompt to restrict destructive calls',
        'never correct: secrets in repo files and prompt-only authorization violate MCP security fundamentals.',
        'storing static admin PATs in `AGENTS.md` and relying on prompt instructions for access control exposes every user to ASI03/ASI04 compromise.',
    ),
    'seq_aai_mcp_streamable_auth_w3': (
        'Invoke mutating `MCP` tool first → request OAuth 2.1 user consent after side effects complete → silently ignore schema validation errors → retry non-idempotent writes without keys',
        'never correct: authenticating after executing mutations and retrying non-idempotent writes causes unauthorized duplicate side effects.',
        'performing external mutations before OAuth consent and retrying without idempotency keys violates authorization and data integrity.',
    ),

    # 2.3 — LangGraph 1.x Durable Human-in-the-Loop (`interrupt()` + Checkpointer + `Command(resume=...)`)
    'seq_aai_langgraph_hitl_ok': (
        'Compile `StateGraph` with persistent `PostgresSaver` checkpointer → invoke with `thread_id` & keep pre-interrupt code idempotent → pause via `interrupt(payload, response_schema=...)` → resume via `Command(resume=decision)` on same `thread_id`',
        'matches LangGraph 1.x durable HITL mechanics: persistent checkpointer, thread_id correlation, idempotent pre-interrupt code, and typed Command resume.',
        'omitting a checkpointer or placing non-idempotent side effects above `interrupt()` raises runtime errors or fires duplicate writes on node replay.',
    ),
    'seq_aai_langgraph_hitl_w1': (
        'Compile `StateGraph` with `checkpointer=None` → place blocking `input()` inside async node → execute non-idempotent payment charge above `interrupt()` → resume with a brand-new `thread_id`',
        'never correct: `checkpointer=None` fails on `interrupt()`, `input()` blocks workers, pre-interrupt charges double-bill, and a new `thread_id` loses state.',
        'calling `interrupt()` without a checkpointer fails, pre-interrupt mutations re-execute on resume, and changing `thread_id` orphans the checkpoint.',
    ),
    'seq_aai_langgraph_hitl_w2': (
        'Run `while True: sleep(60)` polling inside the graph node for 48 hours → store approval state only in Python global RAM → skip `response_schema` validation → mutate state dictionary in place without reducers',
        'never correct: in-memory sleep loops vanish on pod restarts and hold worker coroutines hostage for days.',
        'holding 48-hour sleep loops in pod RAM wastes compute and loses all pending human approvals whenever containers restart.',
    ),
    'seq_aai_langgraph_hitl_w3': (
        'Execute irreversible external deletion first → call `interrupt()` afterward to notify the operator → pass unvalidated prose to `Command(resume=...)` → discard checkpoint history before audit logging',
        'never correct: pausing after an irreversible deletion defeats human-in-the-loop prevention.',
        'triggering `interrupt()` after an irreversible action turns preventive oversight into a post-mortem notification.',
    ),

    # 3.3 — Corrective / Self-Reflective Agentic RAG (`CRAG`) Grounding Pipeline
    'seq_aai_crag_grounding_ok': (
        'Pre-filter hybrid `BM25`+dense index by `OBO` ACLs & validity dates → grade chunk relevance via evaluator → rewrite query or run scoped fallback search on low relevance → synthesize with verified citations or abstain',
        'combines security-trimmed hybrid retrieval with Corrective RAG relevance grading, bounded query reformulation, and verified citations.',
        'stuffing low-relevance or unauthorized chunks directly into generation without grading or ACL pre-filtering produces hallucinated and leaky answers.',
    ),
    'seq_aai_crag_grounding_w1': (
        'Generate speculative answer from parametric memory first → search global index without ACL filters → append 40 unreranked chunks regardless of relevance → strip restricted terms via output regex',
        'never correct: global unfiltered search leaks cross-tenant data and 40 noisy chunks degrade faithfulness.',
        'post-generation regex filtering cannot undo prompt-level ACL exposure, and ungraded noisy chunks cause lost-in-the-middle errors.',
    ),
    'seq_aai_crag_grounding_w2': (
        'Run unbounded web-search rewrite loop without `max_retries` → index raw unverified web pages directly into long-term semantic memory → omit chunk citations → guess confidently when evidence is empty',
        'never correct: uncapped rewrite loops burn budgets and writing unverified web text to semantic memory causes ASI06 poisoning.',
        'persisting unverified external snippets into long-term memory invites indirect injection and self-reinforcing memory poisoning.',
    ),
    'seq_aai_crag_grounding_w3': (
        'Split multi-column tables by fixed 300-char slices → retrieve dense vectors only (`no BM25`) → skip relevance grading on mismatched results → fabricate plausible document IDs in markdown',
        'never correct: fixed character slicing breaks tables and fabricated document IDs destroy auditability.',
        'destroying table structure and inventing citation IDs produces confident, ungrounded hallucinations.',
    ),

    # 4.1 — Multi-Trial Agent Trajectory & `Pass^k` Evaluation Harness
    'seq_aai_eval_harness_ok': (
        'Curate stratified tasks in deterministic mock environments (`OpenEnv`) → grade final state, tool trajectories & calibrated `LLM-as-judge` → measure `Pass^k` multi-trial consistency → gate CI & harvest sanitized failures',
        'evaluates stateful outcomes, trajectory efficiency, and `Pass^k` multi-run reliability inside reproducible sandboxes before CI promotion.',
        'measuring single-run `Pass@1` or `BLEU` overlap against live production APIs hides flaky agent loops and causes live side effects.',
    ),
    'seq_aai_eval_harness_w1': (
        'Run agents directly against live production customer APIs in CI → evaluate `BLEU`/`ROUGE` prose similarity on a single `temperature=1.0` run → let the generator self-grade without human calibration → merge on `Pass@5` luck',
        'never correct: live-prod CI runs mutate customer data and `Pass@5` masks an agent that fails 4 out of 5 times in production.',
        'relying on `Pass@k` best-of-k luck instead of `Pass^k` every-trial consistency ships unreliable agents that fail most customer requests.',
    ),
    'seq_aai_eval_harness_w2': (
        'Commit unredacted production bearer tokens & customer PII to Git fixtures → assert only HTTP `200 OK` status → ignore redundant 30-step tool loops → skip adversarial prompt-injection slices',
        'never correct: raw secrets/PII in Git breach compliance and HTTP 200 checks miss wrong tool calls and runaway cost.',
        'checking only HTTP 200 status while committing raw PII to Git violates security and misses trajectory regressions.',
    ),
    'seq_aai_eval_harness_w3': (
        'Deploy prompt and tool-schema changes straight to `100%` prod traffic → wait for customer support complaints → eyeball 3 happy-path chats manually → tune system prompt in production console',
        'never correct: testing in production via customer complaints violates basic agent reliability engineering.',
        'shipping unvalidated tool-schema edits directly to 100% of users turns customers into unpaid QA testers.',
    ),

    # 5.3 (odd sets) — Progressive Agent Fleet Rollout (`Shadow -> Canary -> Scale`)
    'seq_aai_progressive_deploy_ok': (
        'Gate build on CI `Pass^k` evals + `AIBOM`/CVE scan → replay live traffic in side-effect-free `Shadow` mode → shift `5%` `Canary` traffic with `TTFT`/`SLO` auto-rollback → autoscale on `KV-cache %` & queue depth',
        'proves offline reliability and supply-chain safety, validates real-distribution parity without side effects, and bounds live blast radius.',
        'allowing shadow agents to fire real external writes or scaling GPU pods solely on CPU% causes duplicate mutations and `KV-cache` OOMs.',
    ),
    'seq_aai_progressive_deploy_w1': (
        'Cut `100%` of live traffic over immediately → let `Shadow` fleet execute real `POST` database mutations → autoscale `vLLM` GPUs only on host CPU% → inspect `Pass^k` evals next sprint',
        'never correct: live writes in shadow mode duplicate transactions and CPU% misses GPU KV-cache saturation.',
        'executing real mutations from a shadow agent corrupts customer records, and CPU-based autoscaling stays blind to GPU KV-cache exhaustion.',
    ),
    'seq_aai_progressive_deploy_w2': (
        'Bake static cloud admin keys into `:latest` root container → disable guardrail latency checks to boost speed → skip canary telemetry → roll back manually only after executive escalation',
        'never correct: root `:latest` images with baked secrets and disabled guardrails invite supply-chain and safety incidents.',
        'embedding credentials in `:latest` root images and stripping guardrails violates container and agentic security.',
    ),
    'seq_aai_progressive_deploy_w3': (
        'Prepend random UUIDs to line 1 of every system prompt → turn off continuous batching → deploy diverging hard-forked repos per tenant → ignore `OpenTelemetry` span errors',
        'never correct: volatile prompt prefixes destroy KV prefix caching and disabling continuous batching collapses GPU throughput.',
        'invalidating KV prefix caches and disabling continuous batching spikes `TTFT` and multiplies GPU serving cost.',
    ),

    # 5.5 (even sets) — Production Agent Runaway / Latency / Cascading-Failure Triage
    'seq_aai_incident_contain_ok': (
        'Trip scoped kill-switch, canary rollback, or read-only fallback mode → inspect `OpenTelemetry` `gen_ai.agent.*` span waterfalls (`TTFT, TPOT, KV-cache %, tool loops, 429s`) → isolate root fault → ship trajectory-eval-gated fix',
        'contains blast radius immediately (`ASI08/ASI10`), pinpoints whether loops, KV-cache, or tools stalled via agent spans, and prevents regression.',
        'leaving a looping or hallucinating multi-agent fleet active while debugging live burns thousands in tokens and cascades corrupt writes.',
    ),
    'seq_aai_incident_contain_w1': (
        'Leave runaway agents mutating production APIs while reading logs → configure 0-ms infinite retries on `HTTP 429` → double `max_steps` to 100 → hot-edit prompts directly on prod pods',
        'never correct: zero-delay retries and raising `max_steps` during a loop amplify cascading failures (`ASI08`).',
        'increasing `max_steps` and firing zero-jitter retries during a quota/loop incident turns a degradation into a total outage.',
    ),
    'seq_aai_incident_contain_w2': (
        'Delete `OpenTelemetry` trace logs to free disk space → fail over blindly to an untested model lacking tool-call support → disable `OAuth` checks → close incident without regression tests',
        'never correct: wiping traces destroys forensics and failing over to a non-tool-capable model breaks every agent step.',
        'failing over to an untested model incompatible with your JSON tool schemas causes 100% downstream parser failures.',
    ),
    'seq_aai_incident_contain_w3': (
        'Wait 4 hours for billing alerts before paging SREs → restart stateful in-memory pods (`wiping all active checkpoints`) → blame foundation model randomness → redeploy unchanged config',
        'never correct: relying on delayed billing alerts and wiping uncheckpointed in-memory state causes massive user disruption.',
        'discovering runaway loops via next-day billing dashboards instead of real-time step/cost spans leaves incidents uncontained.',
    ),

    # 6.1 — Defense-in-Depth Against OWASP Agentic Top 10 (`ASI01` Goal Hijack -> `ASI05` RCE)
    'seq_aai_owasp_defense_ok': (
        'Taint-tag & isolate untrusted external inputs → run `NeMo` input/retrieval guardrails → enforce `OBO`-scoped tool policy & zero-egress `OpenSandbox` execution → require `HITL` diff confirmation on sensitive writes',
        'layers input/retrieval rails, taint-aware privilege separation (`ASI01/ASI02`), microVM sandboxing (`ASI05`), and human verification (`ASI09`).',
        'relying solely on polite system-prompt instructions to stop indirect injection or unsandboxed `exec()` leaves RCE and exfiltration wide open.',
    ),
    'seq_aai_owasp_defense_w1': (
        'Concatenate raw untrusted emails into system instructions → grant unrestricted `bash` & outbound internet on host OS → run regex profanity check on final reply → auto-approve all external wire/email actions',
        'never correct: host-OS `bash` with outbound internet on untrusted email inputs guarantees `ASI01` hijack and `ASI05` RCE.',
        'mixing untrusted data into system instructions while exposing host shell and network egress enables trivial remote takeover.',
    ),
    'seq_aai_owasp_defense_w2': (
        'Trust third-party `MCP` servers without schema pinning (`ASI04`) → share one static superuser token across all agents (`ASI03`) → write raw untrusted outputs into global semantic memory (`ASI06`) → skip audit logs',
        'never correct: unpinned MCP servers, shared superuser tokens, and unvalidated memory writes combine `ASI03`, `ASI04`, and `ASI06`.',
        'combining unvetted MCP tools with shared admin tokens and unguarded memory writes creates persistent cross-user compromise.',
    ),
    'seq_aai_owasp_defense_w3': (
        'Disable execution guardrails to save 40 ms latency → execute LLM-generated SQL as `db_owner` → allow peer agents to override safety policies over unsigned HTTP (`ASI07`) → hide tool traces from human reviewers',
        'never correct: unsigned peer overrides and hidden traces invite `ASI07` spoofing and `ASI09` trust exploitation.',
        'hiding executed tool arguments from human reviewers while allowing unsigned inter-agent policy overrides subverts all oversight.',
    ),

    # 6.5 — Enterprise Agentic Governance, Compliance & Audit Lifecycle (`NIST AI RMF` / `EU AI Act`)
    'seq_aai_governance_audit_ok': (
        'Classify agent risk tier & register `NHI`/AIBOM inventory (`Govern/Map`) → benchmark `Pass^k`, bias & `OWASP ASI` red-team suites (`Measure`) → enforce `ZDR`, `HITL` & kill-switches (`Manage`) → persist immutable `WORM` trajectory provenance',
        'connects `NIST AI RMF 1.0` (`Govern, Map, Measure, Manage`) and `EU AI Act` Art. 14 oversight with cryptographic trajectory auditability.',
        'treating governance as a one-off pre-launch slide deck with no runtime kill-switches or trajectory logs fails regulatory examination.',
    ),
    'seq_aai_governance_audit_w1': (
        'Launch autonomous high-risk agents with anonymous shared API keys → skip `OWASP ASI` red-teaming → route regulated PII to consumer training-enabled endpoints → draft a retroactive policy PDF only when audited',
        'never correct: shared anonymous keys, consumer endpoints, and retroactive paperwork violate `NIST AI RMF`, `GDPR`, and `EU AI Act`.',
        'deploying unattributed high-risk agents onto non-ZDR endpoints without red-teaming creates immediate legal and security liability.',
    ),
    'seq_aai_governance_audit_w2': (
        'Log raw unredacted customer secrets to public SaaS dashboards → allow agents to self-modify their own `HITL` approval thresholds → delete failed trajectory traces nightly → claim `100%` autonomous compliance',
        'never correct: self-modifiable safety thresholds (`ASI10`) and deleting failed audit traces violate oversight integrity.',
        'permitting agents to lower their own HITL thresholds or purging failed traces destroys human oversight and forensic accountability.',
    ),
    'seq_aai_governance_audit_w3': (
        'Perform one manual happy-path demo before launch → disable drift and rogue-agent monitoring in production → remove human override buttons from operator UI → retain zero prompt/tool version lineage',
        'never correct: removing human override controls directly violates `EU AI Act` Article 14 and `NIST AI RMF Manage`.',
        'eliminating human intervention controls and version lineage leaves operators powerless during production drift or hijack.',
    ),
}
