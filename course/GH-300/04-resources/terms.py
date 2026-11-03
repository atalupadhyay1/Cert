"""Canonical option bank (TERMS) for Microsoft / GitHub Exam GH-300: GitHub Copilot (August 7, 2026 study guide)."""

TERMS = {
    # =========================================================================
    # DOMAIN 1: Use GitHub Copilot responsibly (15-20% -> 18 items, 3 MS)
    # =========================================================================
    "rai_genai_risks_limits": (
        "Generative AI models predict statistically probable token sequences (`not proven correctness`), risking hallucinated APIs, outdated idioms, training-data bias, and subtle security bugs",
        "Generative AI risks and limitations (`1.1`) address probabilistic next-token prediction, hallucinations, outdated APIs, and bias—not IDE installation or REST seat billing.",
    ),
    "rai_slopsquatting_pkg_risk": (
        "Verify every AI-suggested package name, publisher, and version in your trusted registry (`preventing slopsquatting / hallucinated dependency attacks`) before installing",
        "Package hallucination / slopsquatting verification (`1.1`, `1.4`) protects dependency supply chains—not Markdown PR summaries or status badges.",
    ),
    "rai_automation_complacency": (
        "Guard against **automation bias / complacency** (`over-trusting plausible-looking AI completions`) by reviewing edge cases, error paths, and security invariants manually",
        "Automation bias (`1.1`, `1.4`) occurs when developers accept syntactically clean completions without verifying business logic or security invariants.",
    ),
    "rai_six_core_principles": (
        "Apply the six Responsible AI principles—**Fairness**, **Reliability & Safety**, **Privacy & Security**, **Inclusiveness**, **Transparency**, and **Accountability**",
        "Microsoft/GitHub Responsible AI (`1.2`) centers on Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, and human Accountability.",
    ),
    "rai_ethical_transparency": (
        "Maintain **Transparency** and **Accountability** by disclosing AI assistance per team norms, honoring open-source licenses, and ensuring humans own every committed line",
        "Ethical AI governance (`1.2`) requires human ownership, license respect, and transparent review—never treating Copilot as an autonomous merge authority.",
    ),
    "rai_inclusiveness_fairness": (
        "Evaluate AI-generated UI copy, validation rules, and domain models for **Fairness** and **Inclusiveness** (`avoiding demographic stereotyping, exclusionary naming, or accessibility regressions`)",
        "Fairness and Inclusiveness (`1.2`, `1.3`) ensure AI-assisted software serves diverse users equitably and meets accessibility standards.",
    ),
    "rai_harms_bias_mitigation": (
        "Mitigate AI harms (`historical dataset bias, weak crypto/SQL defaults, PII exposure, and insecure scaffolding`) using RAI filters, `CodeQL` SAST, secret scanning, and diverse test suites",
        "Harm mitigation (`1.3`) combines RAI safety filters, bias testing, SAST scanning, and privacy controls—not disabling code review.",
    ),
    "rai_prompt_injection_indirect": (
        "Treat untrusted external content (`issues, PR bodies, web pages, third-party MCP tool outputs`) as **indirect prompt injection** risks and require human approval on tool actions",
        "Indirect prompt-injection defense (`1.3`, `1.5`) guards Agent Mode and MCP tool invocations against malicious instructions hidden in external data.",
    ),
    "rai_validate_output_checks": (
        "Treat Copilot as a **pair-programming assistant (`not an oracle`)**: review diffs line-by-line, execute unit/integration/edge-case tests, and scan with `CodeQL` and Dependabot",
        "Validating AI output (`1.4`) requires human code review, automated tests, and security scanning before merge.",
    ),
    "rai_non_determinism_review": (
        "Because LLM sampling is **stochastic (`non-deterministic`)**, identical prompts can yield varying implementations whose runtime behavior, complexity, and thread safety must be verified",
        "Non-determinism (`1.4`, `3.5`) means syntactic plausibility never guarantees functional equivalence across repeated prompts.",
    ),
    "rai_operate_responsibly_ops": (
        "Operate Copilot responsibly by keeping `Suggestions matching public code = Block`, configuring Content Exclusions, omitting PII/secrets from prompts, and enforcing human PR review",
        "Responsible Copilot operation (`1.5`) pairs duplication filtering, Content Exclusions, zero-PII prompting, and mandatory human PR review.",
    ),

    # =========================================================================
    # DOMAIN 2: Use GitHub Copilot features (25-30% -> 28 items, 5 MS)
    # =========================================================================
    "feat_ide_enable_auth": (
        "Install the official GitHub Copilot extension in a supported IDE (`VS Code, Visual Studio, JetBrains, Xcode, Eclipse, or Neovim`), sign in via GitHub OAuth, and verify an active seat",
        "Enabling Copilot in the IDE (`2.1`) requires installing the IDE extension, authenticating with GitHub, and holding an active Copilot plan.",
    ),
    "feat_plans_individual_tiers": (
        "Choose **Copilot Free** for capped monthly completions/chats or **Copilot Pro / Pro+** for individual developers needing unlimited completions, higher premium-model quotas, and **GitHub Spark**",
        "Individual Copilot tiers (`2.1`, `2.15`) serve single accounts without Organization policy management or Org Content Exclusions.",
    ),
    "feat_plans_business_enterprise": (
        "Choose **Copilot Business** (`Org policies, Content Exclusions, IP Indemnity, zero model training`) or **Copilot Enterprise** (`adds GHEC Copilot Spaces/Knowledge Bases & org-wide GitHub.com grounding`)",
        "Organization/Enterprise Copilot tiers (`2.1`, `2.15`, `6.2`) add centralized governance, Content Exclusions, audit logs, and IP Indemnity.",
    ),
    "feat_trigger_inline_nes": (
        "Use **Inline ghost-text completions** (`Tab` to accept, `Alt+]` / `Option+]` to cycle) and **Next Edit Suggestions (`NES`)** to predict subsequent ripple edits across nearby lines",
        "Inline completions and Next Edit Suggestions (`2.2`, `5.1`) accelerate localized cursor-level coding and follow-on edits.",
    ),
    "feat_trigger_modes_four": (
        "Match interaction surfaces to scope: **Inline Chat (`Ctrl+I` / `Cmd+I`)** for in-place file edits, **Chat `Ask`** for Q&A, **Copilot Edits** for multi-file working sets, and **Agent Mode / CLI** for autonomous loops",
        "Triggering Copilot across surfaces (`2.2`) matches Inline Chat, `Ask`, `Edit`, Agent Mode, and Copilot CLI to task complexity.",
    ),
    "feat_ide_app_exclusions": (
        "Configure Repository or Organization **Content Exclusions** (`Settings -> Copilot -> Content exclusion`) so IDEs omit matched sensitive files across completions, Chat, and code review",
        "IDE/repo content exclusion awareness (`2.3`) prevents specified paths from being read into Copilot prompts on Business and Enterprise plans.",
    ),
    "cli_define_agentic_terminal": (
        "GitHub Copilot CLI (`copilot`) is a terminal-native AI coding agent that understands shell context, edits files, executes commands with approval prompts, and automates multi-step repo workflows",
        "GitHub Copilot CLI (`2.4`) brings agentic file editing, command execution, and GitHub workflow integration directly to the terminal.",
    ),
    "cli_install_onboarding": (
        "Install `@github/copilot` via `npm install -g @github/copilot` (`Node.js 22+`), `winget install GitHub.Copilot`, or Homebrew, launch `copilot` in your repo, run `/login`, and confirm folder trust",
        "Installing GitHub Copilot CLI (`2.5`) uses `@github/copilot` (`Node 22+`), WinGet, or Homebrew, followed by `/login` OAuth and directory trust confirmation.",
    ),
    "cli_commands_flags": (
        "Use `copilot -p \"...\"` for non-interactive runs (`-s` for clean stdout, `--output-format=json` for JSONL), `--available-tools` / `--deny-tool` for tool scoping, and `--fleet` for parallel subagents",
        "Copilot CLI programmatic flags (`2.6`) control non-interactive scripting (`-p`, `-s`, `--output-format=json`), tool permissions, and `--fleet` parallelism.",
    ),
    "cli_slash_permissions_model": (
        "Inside interactive Copilot CLI, use `/permissions show` or `/permissions manual` to inspect/set approval mode, `--model` to pin a model, and `~/.copilot/settings.json` for user preferences",
        "Copilot CLI interactive slash commands and `~/.copilot/settings.json` (`2.6`, `2.8`) govern tool approvals and model selection (`config.json` is internal runtime state).",
    ),
    "cli_interactive_sessions": (
        "Use Copilot CLI **infinite sessions** (auto-compaction under `~/.copilot/session-state/{id}/`), inspect `/session plan`, `/session checkpoints`, and `/session files`, and resume via `--resume` or `--continue`",
        "Interactive Copilot CLI sessions (`2.7`) persist plans, compaction checkpoints, and artifacts in `~/.copilot/session-state/` for `--resume`.",
    ),
    "cli_scripts_file_mgmt": (
        "Generate scripts and edit files safely in Copilot CLI via interactive **permission prompts** (`write`, `commands`), `--add-dir` for extra paths, `--secret-env-vars` redaction, and `--share` / `--share-gist`",
        "Copilot CLI file and script management (`2.8`) enforces explicit write/command approval, `--add-dir` path boundaries, and secret redaction (`GITHUB_TOKEN` redacted by default).",
    ),
    "agent_mode_edits_mcp": (
        "Use **Agent Mode** with `.vscode/mcp.json` **Model Context Protocol (`MCP`)** servers to query external tools, edit multiple files, read compiler/terminal diagnostics, and self-heal until tests pass",
        "Agent Mode + MCP (`2.9`) connects Copilot to external tools/APIs via `.vscode/mcp.json` and iterates across edits and terminal runs autonomously.",
    ),
    "agent_sessions_subagents": (
        "Monitor local IDE, CLI, and cloud coding agents from the unified **Agent Sessions** view (`steering mid-run via chat editors`) and delegate noisy codebase research to **`#runSubagent`** for isolated context",
        "Agent Sessions and `#runSubagent` (`2.9`) provide unified multi-agent orchestration and isolated sub-agent context windows.",
    ),
    "agent_cloud_coding_agent": (
        "Assign a GitHub Issue or PR comment (`@copilot`) to the **Copilot coding agent (`cloud agent`)**, which runs in an ephemeral Actions sandbox, pushes to `copilot/*`, and opens a draft PR for human review",
        "Copilot coding agent (`2.9`) executes asynchronous repository tasks in an isolated cloud sandbox and opens a draft PR without merging autonomously.",
    ),
    "feat_code_review_assist": (
        "Run **Copilot Code Review** locally on uncommitted IDE diffs or on GitHub.com PRs (`with Automatic Copilot code review, Review new pushes, and Review draft pull requests`), paired with human approval",
        "Copilot Code Review (`2.10`) posts `Comment` reviews with `suggestion` blocks—never counting toward required human merge approvals.",
    ),
    "feat_copilot_spaces": (
        "Curate **Copilot Spaces** on GitHub.com (`grouping specific repositories, files, PRs, issues, free-text notes, and custom instructions`) to ground team Q&A and IDE MCP queries on authoritative org context",
        "Copilot Spaces (`2.11`) organize shareable, always-synced multi-repo project context so responses stay grounded in team architecture.",
    ),
    "feat_github_spark": (
        "Use **GitHub Spark** to build, iterate on, and share AI-powered full-stack micro-apps (`with natural-language prompts, live preview, managed KV persistence, and optional GitHub repository sync`)",
        "GitHub Spark (`2.11`) accelerates full-stack micro-app prototyping and deployment directly from natural language and visual controls.",
    ),
    "feat_pr_summary_instructions": (
        "Generate **Copilot Pull Request Summaries** on GitHub.com and enforce coding/review standards via `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` (`applyTo:`, `excludeAgent:`), and `AGENTS.md`",
        "PR Summaries and custom instruction files (`2.11`) automate reviewer context and tailor Copilot code generation/review (`without affecting raw inline ghost text where unsupported`).",
    ),
    "feat_chat_commands_participants": (
        "Scope Copilot Chat with participants (`@workspace`, `@github`, `@vscode`, `@terminal`), slash commands (`/explain`, `/fix`, `/tests`, `/doc`, `/new`, `/clear`), `#file:`/`#codebase` variables, and thumbs feedback",
        "Copilot Chat participants, slash commands, `#` context variables, and feedback ratings (`2.12`) focus intent and report quality signals.",
    ),
    "feat_prompt_files_reuse": (
        "Enable `\"chat.promptFiles\": true` and commit reusable `.github/prompts/*.prompt.md` files (`YAML frontmatter: description, agent, model, tools` + Markdown `#file:` links) invoked via `/prompt-name`",
        "Workspace `.prompt.md` prompt files (`2.12`) standardize repeatable task prompts across VS Code and JetBrains teams.",
    ),
    "org_policy_governance": (
        "Enforce Enterprise/Org Copilot policies (`Enabled`, `Disabled`, `No policy`), Branch Ruleset automatic Copilot Code Review (`authorized users only`), and Enterprise `AI controls -> Agents` repo-wide blocks",
        "Organization/Enterprise Copilot policy management (`2.13`) governs IDE/GitHub.com features, CLI/MCP access, and repo-level agent blocks.",
    ),
    "org_audit_logs_metrics": (
        "Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage",
        "Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.",
    ),
    "org_rest_seat_billing": (
        "Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)",
        "Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.",
    ),

    # =========================================================================
    # DOMAIN 3: Understand GitHub Copilot data and architecture (10-15% -> 14 items, 2 MS)
    # =========================================================================
    "arch_data_flow_retention": (
        "On **Copilot Business & Enterprise**, prompts and completions travel over `TLS 1.2+`, process ephemerally in memory for inline completions, and are **never retained to train foundational models**",
        "Copilot Business/Enterprise data handling (`3.1`) guarantees `TLS 1.2+` encryption and zero foundational-model training on customer code (`Free/Pro provide a training opt-out toggle`).",
    ),
    "arch_engagement_telemetry_vs_code": (
        "Distinguish **user engagement telemetry** (`acceptance/dismissal counts, latency, IDE version, encrypted at rest`) from **source-code prompts/suggestions** (`discarded after inline inference on Business/Enterprise`)",
        "Data flow architecture (`3.1`) separates operational/metrics telemetry from ephemeral prompt/completion payloads.",
    ),
    "arch_input_fim_prompt_build": (
        "The IDE extension constructs prompts from **Fill-in-the-Middle (`FIM`)** cursor prefix + suffix, language/filepath metadata, Jacobi/Jaccard-ranked snippets from open tabs, and custom instructions",
        "Input processing and prompt building (`3.2`) combines cursor prefix + suffix (`FIM`), relevant open-tab snippets, and repository instructions.",
    ),
    "arch_rag_workspace_indexing": (
        "For `@workspace` and GitHub.com repository chat, Copilot uses **lexical and semantic (`embedding`) retrieval (`RAG`)** to inject top-ranked code chunks into the prompt rather than sending entire gigabyte repos",
        "Retrieval-augmented generation (`RAG`, `3.2`) selects the highest-relevance code slices that fit within the model's context token budget.",
    ),
    "arch_proxy_rai_postfilter": (
        "The Copilot **cloud proxy** validates entitlement tokens, applies inbound/outbound **RAI safety filters** (`hate speech, violence, sexual content, PII, prompt injection`), and runs the `~150-char` public-code filter",
        "Proxy filtering and post-processing (`3.3`) enforces auth, RAI moderation, public-code duplication checks, and stop-token trimming.",
    ),
    "arch_suggestion_lifecycle": (
        "Suggestion lifecycle: typing debounce -> IDE FIM/tab context assembly -> `TLS` request to Copilot proxy -> RAI pre-filter & LLM generation -> post-filter & duplication check -> ghost-text render -> telemetry",
        "Code suggestion lifecycle (`3.4`) traces a completion from keystroke pause through IDE context assembly, cloud proxy inference/filtering, and ghost-text display.",
    ),
    "arch_llm_copilot_limits": (
        "Account for LLM & Copilot architectural limits: **finite context windows**, **pre-training knowledge cutoffs**, **stochastic sampling**, **no runtime execution** during inline completion, and unseen unindexed external systems",
        "LLM and Copilot limitations (`3.5`) explain why models hallucinate post-cutoff APIs, vary across runs, truncate overflow tokens, and need tests/MCP.",
    ),

    # =========================================================================
    # DOMAIN 4: Apply prompt engineering and context crafting (10-15% -> 13 items, 2 MS)
    # =========================================================================
    "prm_structure_four_pillars": (
        "Structure effective prompts with **Role/Goal**, **Grounded Context** (`#file`, `#selection`, versions), **Explicit Constraints** (`security, error handling, edge cases`), and **Output Format** (`types, signatures`)",
        "Prompt structure (`4.1`) combines clear intent, grounded workspace context, explicit constraints, and expected output format.",
    ),
    "prm_code_comments_signatures": (
        "Guide inline completions directly inside source files using **top-of-file architecture comments**, **explicit parameter/return type annotations**, and **domain-specific function/variable names**",
        "In-editor context signals (`4.1`, `4.4`) anchor Fill-in-the-Middle inline completions without leaving the code buffer.",
    ),
    "prm_context_determination": (
        "Curate Copilot's active context: open target interface/DTO tabs (`closing unrelated files`), attach `#file:`, `#selection`, `#sym:`, or **Copilot Spaces**, and scope `.instructions.md` with `applyTo:` globs",
        "Context determination (`4.2`) controls which open tabs, `#` chat variables, workspace indexes, and path-matched instructions enter the prompt.",
    ),
    "prm_zeroshot_vs_fewshot": (
        "Use **zero-shot prompting** for standard algorithms/APIs, and **few-shot prompting** (`1–3 concrete input -> output examples`) when teaching proprietary schemas, custom DSLs, or bespoke test conventions",
        "Zero-shot vs few-shot prompting (`4.3`) reserves token-heavier exemplars for custom team patterns that general pretraining cannot infer.",
    ),
    "prm_crafting_best_practices": (
        "Decompose complex epics into small, testable steps, state exact framework/SDK versions (`preventing pre-cutoff API drift`), and iterate in follow-up turns using compiler or test output",
        "Prompt-crafting best practices (`4.4`) favor incremental decomposition, version pinning, and feedback-driven iteration.",
    ),
    "prm_engineering_principles": (
        "Write **positive, specific constraints** (`'use parameterized pg queries with $1 parameters'`) rather than vague negations, ground domain rules via `#file:`, and codify standards in `.prompt.md` / `.instructions.md`",
        "Prompt engineering principles (`4.5`) emphasize specificity, positive constraints, authoritative grounding, and reusable templates.",
    ),
    "prm_history_token_budget": (
        "Copilot Chat appends prior turns from the active thread up to its **token context limit**; run `/clear` (or open a new chat) on topic switches and use `#runSubagent` to keep noisy exploration out of history",
        "Prompt process flow and chat history management (`4.6`) prevent context drift and token-window eviction across unrelated tasks.",
    ),

    # =========================================================================
    # DOMAIN 5: Improve developer productivity with GitHub Copilot (10-15% -> 14 items, 2 MS)
    # =========================================================================
    "prod_codegen_refactor_docs": (
        "Use `Inline Chat`, `Copilot Edits`, **Next Edit Suggestions**, and `/doc` to scaffold repetitive DTOs/validators, extract pure functions to reduce cyclomatic complexity, and generate JSDoc/OpenAPI/Mermaid docs",
        "Code generation, refactoring, and documentation (`5.1`) accelerates boilerplate, structural cleanup, and API docs while preserving behavior.",
    ),
    "prod_learn_context_switch": (
        "Minimize context switching by running `/explain` on complex regexes/SQL/legacy modules, `@terminal` + `/fix` (`or Copilot CLI`) on shell/build errors, and `@workspace` / **Spaces** for repo onboarding",
        "Accelerating learning and reducing context switching (`5.2`) keeps developers productive inside the IDE and terminal.",
    ),
    "prod_synthetic_data_modernize": (
        "Generate schema-valid **synthetic test fixtures** (`zero real customer PII`) and modernize legacy code (`e.g., Java 8 -> 21, Python 2 -> 3.12, callbacks -> async/await`) incrementally behind characterization tests",
        "Sample data generation and legacy modernization (`5.3`) combine synthetic non-PII fixtures with test-backed incremental upgrades.",
    ),
    "prod_unit_integration_tests": (
        "Use `/tests` (paired with testing `.instructions.md` conventions) to generate unit and integration tests with isolated I/O mocks/stubs, parameterized table cases, and deterministic teardown",
        "Generating unit and integration tests (`5.4`) automates test scaffolding, dependency isolation, and parameterized coverage.",
    ),
    "prod_edge_cases_assertions": (
        "Prompt explicitly for **boundary and adversarial edge cases** (`null/empty, 0/-1/MAX_INT, leap-year/DST timestamps, Unicode, timeouts, race conditions`) and assert concrete outputs/errors (`never tautologies`)",
        "Edge-case identification and assertion quality (`5.5`) ensures tests catch real boundary defects rather than inflating superficial coverage.",
    ),
    "prod_security_perf_autofix": (
        "Use Copilot Chat and **CodeQL Copilot Autofix** to remediate vulnerabilities (`SQLi -> parameterized queries, XSS -> encoding, path traversal, SSRF`) and eliminate `O(n^2)` loops or `N+1` ORM queries",
        "Security and performance optimization (`5.6`) pairs Copilot/Autofix patches with profiler benchmarks and SAST re-scans.",
    ),

    # =========================================================================
    # DOMAIN 6: Configure privacy, content exclusions, and safeguards (10-15% -> 13 items, 2 MS)
    # =========================================================================
    "priv_content_exclusion_cfg": (
        "Configure **Content Exclusions** (`Copilot Business & Enterprise`) in Repo/Org settings with YAML `fnmatch` globs (`- \"/secrets/**\"`); rules combine additively (`Repo cannot weaken Org`) and sync in `<=30 min`",
        "Content Exclusion configuration (`6.1`) enforces additive Org + Repo `fnmatch` path exclusions across Business and Enterprise seats.",
    ),
    "priv_exclusion_scope_limits": (
        "Excluded files are omitted from inline completions, IDE Chat, and Copilot Code Review, **but** IDE language-server (`LSP`) hover types from imported symbols can still surface, and `git`/`CodeQL`/Actions are unaffected",
        "Content Exclusion scope limits (`2.3`, `6.1`) distinguish Copilot prompt blocking from IDE LSP type inference, Git ACLs, and CI scanners.",
    ),
    "priv_editor_privacy_settings": (
        "On Individual plans (`Copilot Free / Pro / Pro+`), disable `Allow GitHub to use my code snippets from the code editor for product improvements` in GitHub Copilot settings to opt out of model training",
        "Individual privacy settings (`3.1`, `6.1`) govern optional snippet training on personal plans (`whereas Business/Enterprise disable code-snippet training by default`).",
    ),
    "priv_ownership_ip_indemnity": (
        "Customers retain ownership of their code (`GitHub claims no copyright over suggestions`), and **Copilot Business / Enterprise** provide **IP Indemnity** when `Suggestions matching public code` is set to **`Block`**",
        "Output ownership and IP Indemnity (`6.2`) require Business/Enterprise licensing with the public-code duplication filter enabled (`Block`).",
    ),
    "priv_public_code_duplication": (
        "Set **`Suggestions matching public code = Block`** to suppress `~150+` char matches against public GitHub repos; when set to **`Allow`**, **Code Referencing** logs matched repo URLs and licenses in the IDE",
        "Public-code duplication filtering and Code Referencing (`6.3`) either block `~150+` char verbatim public matches or surface repo/license provenance.",
    ),
    "priv_troubleshoot_diagnostics": (
        "Diagnose missing completions or unexpected exclusions via **Copilot Diagnostics / Output logs**: verify seat assignment, filetype toggle, active exclusion icon (`most restrictive org wins`), and TLS proxy allowlists (`*.githubcopilot.com`)",
        "Troubleshooting Copilot (`6.4`) checks multi-org policy precedence (`most restrictive wins`), Content Exclusion icons, filetype settings, and proxy/TLS trust.",
    ),

    # =========================================================================
    # MULTI-SELECT COMPLEMENTARY OPTIONS (ms_d1_* .. ms_d6_*)
    # =========================================================================
    "ms_d1_human_accountability": (
        "Require a human engineer to review, test, and approve every AI-assisted pull request—never delegating final merge accountability to an LLM",
        "Human-in-the-loop accountability (`1.2`, `1.4`) ensures engineers remain responsible for correctness, security, and license compliance.",
    ),
    "ms_d1_sast_secret_gate": (
        "Enforce automated CI guardrails (`CodeQL` code scanning, Secret Scanning Push Protection, and Dependabot) on every branch containing AI-generated code",
        "Automated security gates (`1.3`, `1.4`) catch vulnerable patterns, leaked credentials, and known CVEs introduced during rapid AI code generation.",
    ),
    "ms_d1_no_pii_secrets_prompt": (
        "Never paste live customer PII, PHI, production database dumps, or active credentials/private keys into Copilot prompts or sample fixtures",
        "Data minimization in prompts (`1.3`, `1.5`) prevents accidental exposure of regulated personal data or live secrets.",
    ),
    "ms_d2_cli_permission_scopes": (
        "Scope non-interactive Copilot CLI automation with `--available-tools` / `--deny-tool`, `--secret-env-vars` redaction, and single-run `--trust-folder` rather than blanket `--allow-all`",
        "Least-privilege Copilot CLI flags (`2.6`, `2.8`) restrict tool execution, path writes, and secret exposure in automated scripts.",
    ),
    "ms_d2_subagent_isolated_ctx": (
        "Invoke `#runSubagent` in VS Code Agent Mode so multi-file exploration runs in an isolated context window and returns only a concise summary to main chat",
        "Sub-Agent delegation (`2.9`) prevents raw search results from bloating and confusing the primary Agent Mode conversation.",
    ),
    "ms_d2_instructions_applyto": (
        "Create modular `.github/instructions/*.instructions.md` files with YAML frontmatter `applyTo:` globs (`and optional excludeAgent: \"code-review\" | \"cloud-agent\"`) for path-specific standards",
        "Path-scoped `.instructions.md` files (`2.11`) automatically inject targeted coding and review rules only when matching files are touched.",
    ),
    "ms_d2_prompt_files_slash": (
        "Store reusable `.github/prompts/*.prompt.md` templates (`enabled via \"chat.promptFiles\": true`) with `agent`, `model`, and `tools` frontmatter for on-demand `/prompt-name` invocation",
        "Workspace `.prompt.md` files (`2.12`) turn repeatable scaffolding, review, and migration workflows into version-controlled slash commands.",
    ),
    "ms_d2_enterprise_block_agents": (
        "Use Enterprise `AI controls -> Agents` (`Block Copilot cloud agent` / `Block Copilot code review`) and `Only allow Copilot code review to be triggered by authorized users` to govern enterprise repos",
        "Enterprise repository-level agent blocks (`2.13`) protect enterprise repos even when a contributor holds an external personal Copilot plan.",
    ),
    "ms_d3_fim_prefix_suffix": (
        "Include both code **before** the cursor (`prefix`) and code **after** the cursor (`suffix`) via Fill-in-the-Middle (`FIM`) alongside matching open-tab symbols",
        "Fill-in-the-Middle (`FIM`, `3.2`) enables inline completions to align return types and variable names with surrounding downstream lines.",
    ),
    "ms_d3_proxy_rai_dup_check": (
        "Pass generated tokens through cloud-proxy Responsible AI toxicity/harm classifiers and the `~150-character` public-code duplication filter before IDE rendering",
        "Cloud-proxy post-processing (`3.3`, `3.4`) enforces both RAI content safety and public-code matching policies prior to displaying ghost text.",
    ),
    "ms_d4_close_irrelevant_tabs": (
        "Close unrelated editor tabs and open the exact target interfaces/DTOs (`or pin them via #file:`) so neighbor-tab ranking injects clean, relevant types",
        "Curating open tabs and `#file:` attachments (`4.2`, `4.4`) directly improves prompt signal-to-noise ratio.",
    ),
    "ms_d4_clear_chat_on_switch": (
        "Run `/clear` or start a new Chat session when pivoting to an unrelated module so stale conversation turns do not consume token budget or bias new answers",
        "Resetting chat history on task switches (`4.6`) avoids context confusion and token-window truncation.",
    ),
    "ms_d5_characterization_tests": (
        "Lock existing legacy behavior with characterization and boundary-value unit tests **before** refactoring idioms with Copilot Edits or Agent Mode",
        "Characterization testing (`5.3`, `5.4`) guarantees legacy modernization preserves subtle business edge cases.",
    ),
    "ms_d5_parameterized_autofix": (
        "Validate that security fixes (`such as CodeQL Copilot Autofix`) replace string-concatenated queries/commands with parameterized APIs and pass full regression + SAST checks",
        "Verified security remediation (`5.6`) confirms Autofix patches eliminate root-cause injection sinks without breaking callers.",
    ),
    "ms_d6_most_restrictive_org": (
        "When a user receives Copilot policies from multiple Organizations (or Enterprise + Org), GitHub enforces the **most restrictive** policy (`Block overrides Allow; Disabled overrides Enabled`)",
        "Multi-organization policy resolution (`2.13`, `6.4`) always applies the strictest safeguard across a user's active memberships.",
    ),
    "ms_d6_tls_firewall_allowlist": (
        "Allow outbound `HTTPS (TCP 443)` with valid TLS trust (`NODE_EXTRA_CA_CERTS` / OS trust store for SSL-inspecting proxies) to GitHub's documented `*.githubcopilot.com` and `github.com` endpoints",
        "Network & SSL-proxy configuration (`6.4`) resolves connection blocks and certificate trust errors in corporate IDEs.",
    ),

    # =========================================================================
    # PROPOSED SOLUTION (YES / NO) CANONICAL OPTIONS (sol_yes & sol_no_*)
    # =========================================================================
    "sol_yes": (
        "Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements",
        "Evaluate whether every stated plan tier, CLI/IDE mechanism, context scope, and Enterprise/Org policy requirement is genuinely met.",
    ),
    "sol_no_free_pro_no_exclusions": (
        "No — Repository and Organization **Content Exclusions** require **Copilot Business or Copilot Enterprise**; personal Copilot Free/Pro/Pro+ plans do not support Org Content Exclusions",
        "Content Exclusions (`2.3`, `6.1`) are only enforced for seats governed under Copilot Business or Copilot Enterprise.",
    ),
    "sol_no_gitignore_not_exclusion": (
        "No — `.gitignore` only prevents untracked files from being staged by Git; excluding tracked repository files from Copilot requires **Copilot Content Exclusions** (`Settings -> Copilot -> Content exclusion`)",
        "Adding a tracked path to `.gitignore` (`6.1`) does NOT stop Copilot from reading that file in the IDE or on GitHub.com.",
    ),
    "sol_no_review_not_human_approval": (
        "No — **Copilot Code Review** posts `Comment` reviews (`never Approve` reviews that satisfy required human branch-protection approver counts); a human reviewer must still approve",
        "Copilot Code Review (`1.4`, `2.10`) supplements—never replaces—required human pull-request approvals.",
    ),
    "sol_no_exclude_agent_blocks_review": (
        "No — setting `excludeAgent: \"code-review\"` in `.instructions.md` frontmatter explicitly **prevents** Copilot Code Review from using that file (`use applyTo: without excluding code-review`)",
        "`excludeAgent: \"code-review\"` (`2.11`) tells GitHub.com to omit that instruction file during Copilot Code Review.",
    ),
    "sol_no_indemnity_needs_block": (
        "No — GitHub's **Copilot IP Indemnity** on Business/Enterprise ceases to cover suggestions when `Suggestions matching public code` is set to **`Allow`**; set the filter to **`Block`**",
        "Enabling `Block` on public-code duplication (`6.2`, `6.3`) is a mandatory condition for GitHub Copilot IP Indemnity protection.",
    ),
    "sol_no_metrics_not_per_user": (
        "No — `GET /orgs/{org}/copilot/metrics` returns **aggregated, anonymized** team/org usage (`requiring >=5 active users`), NOT per-developer `last_activity_at` usernames; query `GET /orgs/{org}/copilot/billing/seats`",
        "Per-seat dormancy audits (`2.14`, `2.15`) require `/copilot/billing/seats`, whereas `/copilot/metrics` aggregates anonymized adoption stats.",
    ),
    "sol_no_ask_mode_no_autonomous_edits": (
        "No — Copilot Chat **`Ask` mode** only answers questions and proposes snippets in chat; autonomous multi-file workspace edits with iterative terminal test execution require **Agent Mode** (`or Copilot CLI`)",
        "Only **Agent Mode** (or **Copilot CLI**, `2.2`, `2.9`) autonomously edits multiple files and runs terminal verification loops.",
    ),
    "sol_no_lsp_hover_cross_file": (
        "No — while Content Exclusions block direct file reads, IDE **language-server (`LSP`) type/signature hover metadata** from symbols imported out of an excluded file can still surface in non-excluded open files",
        "GitHub documents that IDE semantic/LSP hover information (`6.1`) is outside direct Content Exclusion file-read blocking when symbols are imported.",
    ),
    "sol_no_monolithic_marathon_chat": (
        "No — keeping dozens of unrelated tabs open and reusing one marathon chat thread across unrelated tasks causes **context pollution and token truncation**; close stale tabs and use `/clear` or `#runSubagent`",
        "Clean editor tabs, `/clear` between topics, and `#runSubagent` isolation (`4.2`, `4.6`) prevent context confusion.",
    ),
    "sol_no_repo_cannot_weaken_org": (
        "No — Repository administrators **cannot delete or override** Organization-level Content Exclusions (`Repo and Org exclusions combine additively, and the most restrictive policy wins`)",
        "Organization Content Exclusions (`6.1`, `6.4`) establish a floor that repository settings can only expand, never weaken.",
    ),

    # =========================================================================
    # HIGH-PLAUSIBILITY DISTRACTOR-ONLY MISCONCEPTIONS (bad_*)
    # =========================================================================
    "bad_copilot_trains_on_business": (
        "Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models",
        "False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).",
    ),
    "bad_offline_local_llm_default": (
        "GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic",
        "False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).",
    ),
    "bad_deterministic_zero_bugs": (
        "Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free",
        "False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).",
    ),
    "bad_instructions_override_exclusions": (
        "Listing `- \"!/secrets/**\"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files",
        "False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).",
    ),
    "bad_exclusions_block_git_actions": (
        "Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files",
        "False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).",
    ),
    "bad_prompt_file_wrong_path": (
        "Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke",
        "False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with \"chat.promptFiles\": true`) and invoked on-demand (`2.12`).",
    ),
    "bad_cli_legacy_node14_root": (
        "GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`",
        "False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).",
    ),
    "bad_subagent_shares_full_chat": (
        "`#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read",
        "False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).",
    ),
    "bad_cloud_agent_auto_merges_main": (
        "When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review",
        "False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).",
    ),
    "bad_allow_filter_grants_indemnity": (
        "Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits",
        "False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).",
    ),
    "bad_permissive_org_wins": (
        "When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins",
        "False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).",
    ),
    "bad_paste_prod_pii_for_tests": (
        "Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions",
        "False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).",
    ),
    "bad_vague_one_word_prompt": (
        "Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically",
        "False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).",
    ),
    "bad_tautological_mock_tests": (
        "Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases",
        "False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).",
    ),
}

from sequences import SEQUENCES  # noqa: E402

for _k, _v in SEQUENCES.items():
    assert _k not in TERMS, f"Duplicate key {_k}"
    TERMS[_k] = _v

for _k, _v in TERMS.items():
    assert len(_v[0]) <= 245, f"{_k} label len {len(_v[0])} > 245"
    assert len(_v[1]) <= 240, f"{_k} note len {len(_v[1])} > 240"

assert len(set(v[0] for v in TERMS.values())) == len(TERMS), "Duplicate option label detected!"

