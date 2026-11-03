"""Ordered 4-step sequence options (SEQUENCES) for Microsoft / GitHub Exam GH-300 (600 Qs)."""

SEQUENCES = {
    # 1. Domain 1: Human-in-the-loop AI code verification before merge (1.4 / 1.5)
    "seq_rai_verify_merge_ok": (
        "Prompt Copilot with explicit security & type constraints → "
        "Review logic & verify suggested packages exist in trusted registries → "
        "Run unit/edge-case tests plus `CodeQL` & secret scanning → "
        "Complete human peer PR review before merging",
        "Correct order: constrained prompt -> manual logic & dependency check (`blocking slopsquatting`) -> automated tests/SAST -> human PR review.",
    ),
    "seq_rai_verify_merge_w1": (
        "Merge Copilot output directly to `main` → "
        "Run `CodeQL` weekly in production → "
        "Check package names only if builds fail → "
        "Skip human review when Copilot Code Review leaves zero comments",
        "Incorrect: merging unverified LLM output or replacing human peer review with Copilot Code Review violates Responsible AI accountability.",
    ),
    "seq_rai_verify_merge_w2": (
        "Approve an empty PR branch first → "
        "Disable `CodeQL` to speed up Copilot completions → "
        "Install unfamiliar suggested packages blindly from public registries → "
        "Deploy without unit tests",
        "Incorrect: blindly installing hallucinated package names exposes builds to dependency confusion and slopsquatting.",
    ),
    "seq_rai_verify_merge_w3": (
        "Set public-code filtering to `Allow` → "
        "Paste live customer PII into Chat as sample fixtures → "
        "Run unit tests locally → "
        "Self-approve your own pull request",
        "Incorrect: pasting real PII into prompts and bypassing human review violates privacy and Responsible AI governance.",
    ),

    # 2. Domain 2: Installing and starting GitHub Copilot CLI for the first time (2.5)
    "seq_cli_first_run_ok": (
        "Install Node.js `22+` (or WinGet/Homebrew) & `npm install -g @github/copilot` → "
        "`cd` into the project directory & launch `copilot` → "
        "Enter `/login` to complete GitHub OAuth authentication → "
        "Confirm directory trust & verify `/permissions show`",
        "Correct order: install `@github/copilot` -> `cd` to project & start `copilot` -> authenticate via `/login` -> confirm folder trust & inspect tool permissions.",
    ),
    "seq_cli_first_run_w1": (
        "Run `/login` in raw Bash before installing `@github/copilot` → "
        "Pass `--allow-all` on `/` root filesystem → "
        "Write plaintext passwords into `~/.copilot/config.json` → "
        "Downgrade to Node.js `14`",
        "Incorrect: `/login` runs inside interactive `copilot`, npm installs require Node.js `22+`, and `config.json` never stores plaintext passwords.",
    ),
    "seq_cli_first_run_w2": (
        "Install `@github/copilot` → "
        "Delete `~/.copilot/session-store.db` before signing in → "
        "Disable the Organization Copilot CLI policy → "
        "Run `copilot -p` unauthenticated",
        "Incorrect: disabling the org Copilot CLI policy blocks access, and authentication must precede non-interactive execution.",
    ),
    "seq_cli_first_run_w3": (
        "Clone the repo inside `~/.copilot/logs/` → "
        "Set `Suggestions matching public code` to `Allow` → "
        "Run `gh auth logout` → "
        "Expect silent file edits without permission prompts",
        "Incorrect: `~/.copilot/logs/` stores session logs, and Copilot CLI requires approval before modifying files in default mode.",
    ),

    # 3. Domain 2: Sub-Agent delegation & Agent Mode workflow with MCP (2.9)
    "seq_agent_mcp_subagent_ok": (
        "Register the MCP server in `.vscode/mcp.json` & verify tools → "
        "Delegate broad codebase search to isolated `#runSubagent` → "
        "Apply multi-file edits & run terminal tests in Agent Mode → "
        "Inspect working-set diffs & `Keep` verified changes",
        "Correct order: register `.vscode/mcp.json` tools -> isolate noisy research via `#runSubagent` -> iterate edits/tests in Agent Mode -> inspect & `Keep` verified diffs.",
    ),
    "seq_agent_mcp_subagent_w1": (
        "Accept (`Keep`) all generated edits before running tests → "
        "Add `.vscode/mcp.json` after closing VS Code → "
        "Attach 80 unrelated files to main chat → "
        "Switch to `Ask` mode expecting autonomous test loops",
        "Incorrect: `Ask` mode cannot autonomously edit files or execute terminal loops, and `Keep` should follow diff & test verification.",
    ),
    "seq_agent_mcp_subagent_w2": (
        "Commit plaintext MCP API keys to `.github/copilot-instructions.md` → "
        "Expect `#runSubagent` to pause mid-run for interactive Q&A → "
        "Disable all workspace tools → "
        "Auto-push unreviewed edits to `main`",
        "Incorrect: never commit secrets to `.github/copilot-instructions.md`, and `#runSubagent` runs autonomously in isolated context without pausing for user input.",
    ),
    "seq_agent_mcp_subagent_w3": (
        "Define MCP servers inside `.git/HEAD` → "
        "Run `/clear` after every single edit so Agent Mode loses its plan → "
        "Skip working-set diff inspection → "
        "Force-push to `main`",
        "Incorrect: `.git/HEAD` is Git metadata (not `.vscode/mcp.json`), and diffs must be reviewed before commit.",
    ),

    # 4. Domain 2: Customizing Copilot Code Review with path-scoped instructions & org rulesets (2.10 / 2.11 / 2.13)
    "seq_code_review_custom_ok": (
        "Add `.github/instructions/sql.instructions.md` (`applyTo: \"db/**/*.sql\"`) → "
        "Merge SQL rules to the default branch → "
        "Enable `Automatically request Copilot code review` in an Org Ruleset → "
        "Resolve Copilot comments alongside human PR approval",
        "Correct order: author path-scoped `.instructions.md` (`applyTo:`) -> merge to default branch -> enable automatic Copilot review via Ruleset -> pair with human approval.",
    ),
    "seq_code_review_custom_w1": (
        "Set `excludeAgent: \"code-review\"` in `sql.instructions.md` → "
        "Expect Copilot Code Review to apply that file anyway → "
        "Remove human approvers so Copilot unlocks merges → "
        "Leave the instructions file untracked",
        "Incorrect: `excludeAgent: \"code-review\"` excludes Copilot Code Review from reading that file, and Copilot comments never satisfy required human approvals.",
    ),
    "seq_code_review_custom_w2": (
        "Save rules in `/tmp/review.txt` without `applyTo:` frontmatter → "
        "Block Copilot Code Review in Enterprise `AI controls` → "
        "Open a draft PR with draft reviews disabled → "
        "Expect automatic Copilot comments",
        "Incorrect: blocking Copilot Code Review in Enterprise `AI controls` disables it across all enterprise repositories.",
    ),
    "seq_code_review_custom_w3": (
        "Commit a 500-page binary `.pdf` in `.github/prompts/` → "
        "Disable repository custom instructions in Settings → "
        "Trigger inline Tab completion → "
        "Expect PRs to auto-merge",
        "Incorrect: custom instructions must be concise Markdown (`.instructions.md` / `copilot-instructions.md`), not binary PDFs.",
    ),

    # 5. Domain 2: Managing Organization Copilot seats via REST API (2.15)
    "seq_org_seat_api_ok": (
        "Authorize `manage_billing:copilot` & enable selected access → "
        "`POST /orgs/{org}/copilot/billing/selected_teams` to grant seats → "
        "`GET /orgs/{org}/copilot/billing/seats` for `last_activity_at` → "
        "`DELETE .../selected_users` to reclaim idle seats",
        "Correct order: authorize `manage_billing:copilot` -> assign via `POST .../selected_teams` (or `selected_users`) -> audit `/seats` -> `DELETE` dormant assignments.",
    ),
    "seq_org_seat_api_w1": (
        "Query `GET /orgs/{org}/copilot/metrics` expecting per-user login names → "
        "Send unauthenticated `PUT /users/{u}/copilot` calls → "
        "Delete the GitHub Organization to free 3 seats → "
        "Re-invite members manually",
        "Incorrect: `/copilot/metrics` returns aggregated anonymized stats (`>=5` active users), whereas `/copilot/billing/seats` exposes per-user `last_activity_at`.",
    ),
    "seq_org_seat_api_w2": (
        "Promote all developers to Organization Owner → "
        "Have engineers buy personal Copilot Pro plans → "
        "Configure Org Content Exclusions expecting personal Pro plans to inherit them → "
        "Skip seat audits",
        "Incorrect: personal Copilot Free/Pro/Pro+ plans do NOT inherit Organization Content Exclusions.",
    ),
    "seq_org_seat_api_w3": (
        "Mint a `repo`-only PAT lacking `manage_billing:copilot` → "
        "POST CSV files to `/repos/{owner}/{repo}/issues` → "
        "Expect seats to provision automatically → "
        "Disable SAML SSO",
        "Incorrect: Copilot seat REST endpoints live under `/orgs/{org}/copilot/billing/...` and require `manage_billing:copilot` billing authorization.",
    ),

    # 6. Domain 3: End-to-end inline code suggestion lifecycle (3.2 / 3.3 / 3.4)
    "seq_arch_suggestion_flow_ok": (
        "IDE gathers FIM prefix/suffix & open tabs (minus exclusions) → "
        "Client sends `TLS 1.2+` prompt to proxy & checks seat token → "
        "Proxy runs RAI filters, LLM & `~150+` char duplication check → "
        "IDE renders ghost text & Business skips model training",
        "Correct order: IDE FIM/tab assembly (respecting exclusions) -> TLS proxy auth -> RAI + LLM + public-code filter -> ghost-text render & zero training retention.",
    ),
    "seq_arch_suggestion_flow_w1": (
        "IDE uploads your entire disk (`~/.ssh` & closed repos) over HTTP → "
        "Cloud GPUs execute your local unit tests → "
        "Copilot commits directly to `main` without ghost text → "
        "Copilot Business trains shared base LLMs on your prompt",
        "Incorrect: inline completion sends scoped editor context over TLS, never runs tests on inference GPUs, and Business/Enterprise never trains base models on customer prompts.",
    ),
    "seq_arch_suggestion_flow_w2": (
        "Public-code duplication filter runs offline with network unplugged → "
        "LLM generates code before receiving file language or cursor prefix → "
        "IDE validates seat tokens once per decade → "
        "Proxy disables TLS encryption",
        "Incorrect: Copilot LLM inference and public-code duplication checks execute in the cloud proxy over authenticated TLS.",
    ),
    "seq_arch_suggestion_flow_w3": (
        "IDE bypasses Organization Content Exclusions → "
        "Forwards raw files to unauthenticated endpoints → "
        "Skips toxicity & prompt-injection filters → "
        "Publishes prompts to public GitHub Gists",
        "Incorrect: Content Exclusions block excluded paths from entering prompts, and prompts are never published to Gists.",
    ),

    # 7. Domain 4: Reusable Prompt Files (.prompt.md) & context engineering workflow (2.12 / 4.2 / 4.5)
    "seq_prompt_file_reuse_ok": (
        "Set `\"chat.promptFiles\": true` & add `.github/prompts/api.prompt.md` → "
        "Link exemplars (`#file:`) & commit to Git → "
        "Close unrelated tabs & invoke `/api` in Chat with inputs → "
        "Run `/clear` (or open a new chat) before switching topics",
        "Correct order: create `.github/prompts/*.prompt.md` -> link few-shot exemplars -> invoke `/api` with clean tab context -> reset chat on topic switch.",
    ),
    "seq_prompt_file_reuse_w1": (
        "Place prompt templates in `.github/workflows/prompt.yml` expecting `/prompt` in Chat → "
        "Keep 45 unrelated legacy files open in tabs → "
        "Reuse one 200-turn chat thread across 12 services → "
        "Omit output types and error rules",
        "Incorrect: `.github/workflows/*.yml` defines Actions workflows (not `.github/prompts/*.prompt.md`), and stale tabs + long threads cause context drift.",
    ),
    "seq_prompt_file_reuse_w2": (
        "Save `prompt.txt` outside the workspace → "
        "Add `applyTo: \"false\"` so nothing matches → "
        "Type `@terminal` expecting inline ghost text in closed files → "
        "Commit unreviewed output",
        "Incorrect: reusable prompt files end in `.prompt.md` under `.github/prompts/` (`whereas applyTo: belongs to *.instructions.md`).",
    ),
    "seq_prompt_file_reuse_w3": (
        "Embed production PATs inside `.github/prompts/deploy.prompt.md` → "
        "Publish private prompts to public npm → "
        "Send one-word `'fix'` with zero file context → "
        "Skip code review",
        "Incorrect: never embed secrets in repository prompt files, and one-word prompts lack actionable context.",
    ),

    # 8. Domain 5: Safe legacy code modernization & characterization testing with Copilot (5.3 / 5.4 / 5.5)
    "seq_legacy_modernize_ok": (
        "Map legacy behavior & invariants via `/explain` and `@workspace` → "
        "Build characterization & boundary tests (`/tests`) until green → "
        "Refactor incrementally via Copilot Edits / Agent Mode → "
        "Re-run tests, `CodeQL` & benchmarks to verify parity",
        "Correct order: map legacy behavior -> lock behavior with characterization/edge-case tests -> refactor incrementally -> verify parity, security & performance.",
    ),
    "seq_legacy_modernize_w1": (
        "Delete the legacy repo & prompt Copilot once to rewrite 80,000 lines from scratch → "
        "Delete failing tests so CI passes → "
        "Skip null/timezone/overflow checks → "
        "Switch production traffic immediately",
        "Incorrect: monolithic rewrites exceed LLM context windows and deleting failing tests destroys regression safety.",
    ),
    "seq_legacy_modernize_w2": (
        "Paste live customer SSNs and card numbers into Chat to build fixtures → "
        "Translate raw SQL string concatenation verbatim into the new language → "
        "Disable `CodeQL` alerts → "
        "Deploy without review",
        "Incorrect: always synthesize fake test data (`never real PII/PCI`) and replace SQL concatenation with parameterized queries.",
    ),
    "seq_legacy_modernize_w3": (
        "Upgrade production servers before compiling → "
        "Generate tautological `expect(true).toBe(true)` tests → "
        "Ignore concurrency and boundary cases → "
        "Merge without running CI",
        "Incorrect: tautological assertions detect zero regressions; tests must assert real outputs and boundary conditions.",
    ),

    # 9. Domain 6: Configuring, verifying & troubleshooting Organization Content Exclusions (2.3 / 6.1 / 6.4)
    "seq_content_exclusion_ok": (
        "Add `fnmatch` globs (`- \"/secrets/**\"`) in `Content exclusion` → "
        "Allow `<=30 min` (or reload IDE) for policy sync → "
        "Verify crossed-out icon & `copilot.content_exclusion_changed` log → "
        "Avoid cross-file imports where IDE LSP hover types surface",
        "Correct order: configure YAML `fnmatch` globs -> allow `<=30 min` IDE sync -> verify crossed-out icon & audit log -> mind IDE LSP type-hover nuance.",
    ),
    "seq_content_exclusion_w1": (
        "Configure Content Exclusions on a personal Copilot Free plan → "
        "Write PCRE lookbehind regexes instead of `fnmatch` globs → "
        "Expect exclusions to block `git clone` and Actions runs → "
        "Ignore IDE status icons",
        "Incorrect: Content Exclusions require **Copilot Business or Enterprise**, use `fnmatch` globs, and govern Copilot context—not Git ACLs or Actions.",
    ),
    "seq_content_exclusion_w2": (
        "List tracked `secrets.yaml` in `.gitignore` expecting Copilot to exclude it → "
        "Set `Suggestions matching public code = Allow` → "
        "Disable IDE TLS verification → "
        "Share one seat login across 10 engineers",
        "Incorrect: `.gitignore` does not exclude already-tracked repository files from Copilot context.",
    ),
    "seq_content_exclusion_w3": (
        "Put exclusion rules in `package.json` → "
        "Wait 14 days for policy propagation → "
        "Have a Repo Admin delete Organization-level Content Exclusions → "
        "Disable Enterprise Audit Logs",
        "Incorrect: Repository admins CANNOT override or remove Organization-level Content Exclusions (`rules combine additively`), and sync takes `<=30 minutes`.",
    ),

    # 10. Domain 5/6: Remediating CodeQL security alerts with Copilot Autofix & IP safeguards (5.6 / 6.2 / 6.3)
    "seq_autofix_safeguard_ok": (
        "Set `Suggestions matching public code = Block` in Org policy → "
        "Inspect `CodeQL` PR **Copilot Autofix** diff & explanation → "
        "Validate the patch (`parameterized SQL`) & package imports → "
        "Commit fix, pass `CodeQL` + tests & get human PR approval",
        "Correct order: enforce public-code `Block` policy -> inspect CodeQL Copilot Autofix -> validate logic & dependencies -> pass CI + human PR approval.",
    ),
    "seq_autofix_safeguard_w1": (
        "Set `Suggestions matching public code = Allow` while expecting full IP indemnity on verbatim matches → "
        "Auto-commit every Copilot Autofix directly to `main` untested → "
        "Disable `CodeQL` PR checks → "
        "Skip human review",
        "Incorrect: GitHub IP indemnity requires keeping the public-code duplication filter enabled (`Block`), and Autofix patches require testing and review.",
    ),
    "seq_autofix_safeguard_w2": (
        "Paste GPL-3.0 source into `.github/copilot-instructions.md` → "
        "Treat Copilot Chat as binding legal license sign-off → "
        "Dismiss `CodeQL` SQLi alerts without patching → "
        "Deploy to production",
        "Incorrect: Copilot does not provide legal license sign-off, and dismissing real vulnerabilities leaves exploits open.",
    ),
    "seq_autofix_safeguard_w3": (
        "Delete Content Exclusions thinking they block `CodeQL` → "
        "Paste live DB passwords into PR comments to test Autofix → "
        "Merge with red integration tests → "
        "Rotate credentials next quarter",
        "Incorrect: Content Exclusions do not block `CodeQL`, and secrets must never be pasted into PR comments.",
    ),
}
