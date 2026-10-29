"""Reusable option catalog for Exam AZ-401 (Agentic DevOps Solutions).

Every entry maps a short key to `(option_label, concise_explanation)` so build.py can
compose 100% per-option rationales explaining why each correct answer succeeds and why
every distractor fails. Zero banned UI phrases; all labels <= 245 chars.
"""

from sequences import SEQUENCES

TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term key: {key}')
    if len(label) > 255:
        raise ValueError(f'{key}: label exceeds 255 chars ({len(label)})')
    if len(meaning) > 390:
        raise ValueError(f'{key}: meaning exceeds 390 chars ({len(meaning)})')
    TERMS[key] = (label, meaning)


# ==============================================================================
# DOMAIN 1: Design and implement processes and communications (15-20%)
# ==============================================================================
# 1.1 Traceability & flow of work
t('ab_fixes_link',
  'Include `Fixes AB#<WorkItemID>` in the GitHub pull request description or commit message with the Azure Boards GitHub App connected',
  '`Fixes AB#<ID>` links the GitHub commit/PR to the Azure Boards work item and automatically transitions its state when merged to the default branch.')
t('copilot_cloud_agent_boards',
  'Assign or invoke GitHub Copilot cloud agent directly from an Azure Boards work item linked to the GitHub repository so it opens a traceable draft PR',
  'GitHub Copilot Cloud Agent for Azure Boards reads work-item acceptance criteria, works on a `copilot/*` branch, and links its draft PR back to the work item.')
t('boards_process_agile',
  'Azure Boards Agile process (`Epic -> Feature -> User Story -> Task` and `Bug` tracked on backlogs or tasks)',
  'The Agile process models User Stories estimated in Story Points alongside Tasks and configurable Bug backlog behavior.')
t('boards_process_scrum',
  'Azure Boards Scrum process (`Epic -> Feature -> Product Backlog Item / Bug -> Task` committed per Sprint)',
  'The Scrum process tracks PBIs and Bugs directly on the Product Backlog with effort points and sprint burndown velocity.')
t('boards_process_cmmi',
  'Azure Boards CMMI process (`Requirement`, formal `Change Request`, `Review`, and `Risk` work item types)',
  'CMMI provides formal Requirements, Change Requests, Risks, and Reviews required by regulated compliance audits.')
t('boards_rollup_analytics',
  'Azure Boards Backlog Rollup columns backed by Analytics linking `Epic -> Feature -> Story/PBI -> Task` hierarchies',
  'Analytics-backed Rollup columns aggregate child completion percentages and story-point totals directly onto parent Features and Epics.')
t('service_hooks_webhook',
  'Configure an Azure DevOps Service Hook (`Work item updated` / `Build completed`) posting signed JSON payloads to external receivers',
  'Service Hooks push event-driven JSON notifications immediately without brittle polling loops.')
t('teams_boards_connector',
  'Install the official Azure Boards app for Microsoft Teams to create work items from chat messages and unfurl live `AB#` cards',
  'The Azure Boards app for Teams turns discussion threads into linked work items and renders live status cards inside channels.')
t('teams_pipelines_app',
  'Subscribe a Microsoft Teams channel using the Azure Pipelines app filtered to `Run stage waiting for approval` and `Run stage state changed (Failed)`',
  'Targeted Azure Pipelines Teams subscriptions surface actionable Adaptive Cards for pending approvals and failed stages without noise.')
t('pr_issue_autolink',
  'Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability',
  'Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge.')
t('dor_dod_criteria',
  'Enforce explicit Definition of Ready (testable acceptance criteria) and Definition of Done (automated tests, security scans, telemetry, docs) on Boards states',
  'Clear DoR and DoD policies give both human engineers and coding agents unambiguous quality thresholds across Plan, Build, Deploy, and Operate phases.')
t('traceability_matrix_req_test',
  'Link Azure Boards Requirements to Test Cases (`Tested By`), GitHub PRs (`AB#`), build runs, and release stages for end-to-end auditability',
  'End-to-end work-item, test, PR, artifact, and deployment links let auditors trace every production change back to an approved requirement and test run.')

# 1.2 Success metrics & AI-assisted queries
t('dora_lead_time',
  'Lead Time for Changes (elapsed duration from first commit or PR creation to successful production deployment)',
  'Lead Time for Changes measures delivery pipeline velocity from code commit to running in production.')
t('dora_deploy_freq',
  'Deployment Frequency (how often an engineering team successfully releases changes into production)',
  'Deployment Frequency quantifies batch size agility and release cadence stability.')
t('dora_cfr',
  'Change Failure Rate (percentage of production deployments causing degraded service, rollback, or emergency hotfix)',
  'Change Failure Rate measures release quality and pre-production validation effectiveness.')
t('dora_mttr',
  'Mean Time to Restore / Failed Deployment Recovery Time (average elapsed time from production incident detection to full service restoration)',
  'MTTR measures operational resilience, observability speed, and rollback/remediation responsiveness.')
t('flow_cycle_time',
  'Cycle Time widget (`Active`/`In Progress` work start until `Closed`/`Done`) paired with `85th` percentile trend lines',
  'Cycle Time measures active engineering execution duration once work starts, complementing total Lead Time.')
t('flow_cfd_wip',
  'Cumulative Flow Diagram (CFD) combined with explicit Kanban column Work-in-Progress (WIP) limits to expose bottleneck queues',
  'Widening CFD bands highlight stage queues, and WIP limits prevent context-switching overload.')
t('wiql_query_ai',
  'Use GitHub Copilot with the Azure DevOps MCP server (`wit` tools) to translate natural-language KPI questions into validated WIQL work-item queries',
  'Azure DevOps MCP work-item tools let Copilot generate and execute accurate WIQL queries over Boards state transitions, bugs, and cycle metrics.')
t('analytics_odata_powerbi',
  'Query Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) to build cross-project KPI scorecards in Power BI',
  'Analytics OData endpoints expose denormalized historical snapshots optimized for multi-team trend reporting without throttling operational REST APIs.')
t('copilot_metrics_api',
  'Query the GitHub Copilot Usage & Metrics API alongside PR lead-time and CI pass-rate telemetry to correlate AI adoption with delivery outcomes',
  'Pairing Copilot adoption/acceptance telemetry with DORA and quality metrics prevents vanity metrics (such as raw lines of code) from distorting evaluation.')

# 1.3 AI documentation & agentic primitives/guardrails
t('copilot_instructions_repo',
  'Create `.github/copilot-instructions.md` at the repository root containing concise build, test, architecture, and security conventions',
  '`.github/copilot-instructions.md` automatically injects repository-wide guidance into GitHub Copilot Chat, code review, and cloud coding agent sessions.')
t('path_instructions_applyto',
  'Create `.github/instructions/<topic>.instructions.md` files with YAML frontmatter `applyTo: "**/*.bicep"` (or path globs) for language-specific rules',
  'Path-scoped `.instructions.md` files apply targeted coding and security rules only when Copilot edits matching file globs, avoiding context bloat.')
t('agents_md_file',
  'Maintain `AGENTS.md` files (at repository root or nested service directories) defining build/lint commands and boundaries for coding agents',
  'GitHub Copilot coding agent and cross-tool CLI agents honor `AGENTS.md` instructions, with nested `AGENTS.md` files scoping rules to specific subdirectories.')
t('custom_agent_profile_md',
  'Define specialized agent personas in `.github/agents/<name>.agent.md` declaring YAML frontmatter `description`, `tools`, and instructions',
  'Custom `.agent.md` profiles restrict an agent persona (such as a read-only security reviewer or docs writer) to an explicit subset of tools and prompts.')
t('skill_md_frontmatter',
  'Package reusable multi-step workflows and scripts inside `.github/skills/<skill-name>/SKILL.md` with YAML frontmatter `name` and `description`',
  'Copilot dynamically loads a repository `SKILL.md` (and bundled helper scripts) on demand when the task matches its `description`, saving baseline context tokens.')
t('copilot_setup_steps_yml',
  'Commit `.github/workflows/copilot-setup-steps.yml` on the default branch with a job named `copilot-setup-steps` to preinstall SDKs, CLIs, and auth before agent runs',
  'Copilot cloud agent executes the `copilot-setup-steps` job from the default branch in an ephemeral Actions environment before starting its coding loop.')
t('copilot_firewall_allowlist',
  'Keep the GitHub Copilot cloud agent firewall enabled and configure custom domain allowlists only for vetted package feeds and MCP endpoints',
  'The cloud agent firewall blocks arbitrary outbound internet access to mitigate prompt-injection data exfiltration while permitting approved registries.')
t('mermaid_wiki_diagram',
  'Use GitHub Copilot to generate versioned Mermaid (` ```mermaid `) sequence and architecture diagrams inside Markdown READMEs and Git-backed Wikis',
  'Mermaid diagrams-as-code render natively in GitHub Markdown and Azure DevOps Wikis and remain diffable in pull requests alongside code changes.')
t('codeowners_file',
  'Configure `.github/CODEOWNERS` mapping critical paths (`infra/**`, `.github/**`, `auth/**`) to security and platform teams with required owner review',
  '`CODEOWNERS` automatically requests and enforces domain-owner sign-off whenever human or AI pull requests touch sensitive paths.')
t('release_notes_autogen',
  'Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags',
  'Automated release configuration categorizes merged PRs and contributor notes consistently for every tagged release.')
t('agent_loop_max_turns',
  'Specify bounded verification loops (lint -> unit test -> typecheck), explicit non-goals, and `timeout-minutes` (`<= 59` in setup steps) for agent tasks',
  'Clear acceptance tests, explicit non-goals, and step timeouts prevent runaway agentic loops and wasted Actions compute minutes.')

# 1.4 MCP servers & integrations
t('ado_mcp_local_npx',
  'Configure the local Azure DevOps MCP server using `npx -y @azure-devops/mcp <org>` (`-a azcli` in cloud agent) with explicit `--domains` / scoped `tools`',
  '`@azure-devops/mcp` runs stdio MCP locally (or inside `copilot-setup-steps` after `azure/login`) exposing only enabled Azure DevOps tool domains.')
t('ado_mcp_remote_http',
  'Configure the hosted remote Azure DevOps MCP server endpoint (`"url": "https://mcp.dev.azure.com/{organization}", "type": "http"`) in `mcp.json`',
  'Microsofts remote Azure DevOps MCP server (`mcp.dev.azure.com/{org}`) provides zero-install OAuth/Entra-authenticated HTTP MCP access to Boards, Repos, and Pipelines.')
t('ado_mcp_scoped_tools',
  'Restrict the MCP server configuration `tools` array (for example `["wit-get-work-item", "pipelines-get-build-log"]`) instead of granting wildcard `["*"]` write tools',
  'Scoping MCP `tools` to least-privilege read/triage operations prevents prompt-injected agents from mutating unrelated pipelines or deleting work items.')
t('gh_mcp_builtin_readonly',
  'Rely on the built-in GitHub MCP server in Copilot cloud agent, which authenticates automatically with a read-only token scoped only to the current repository',
  'By default, Copilot cloud agent includes a built-in GitHub MCP server restricted to read-only operations on the repository where the task runs.')
t('gh_mcp_custom_pat_app',
  'Configure `ghcr.io/github/github-mcp-server` (or remote GitHub MCP) using `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment for cross-repo access',
  'When Copilot cloud agent needs cross-repository context, an installation-scoped GitHub App passed via `COPILOT_MCP_*` secrets grants auditable, short-lived access.')
t('copilot_mcp_secret_prefix',
  'Store MCP credentials in the repository `copilot` GitHub environment prefixed with `COPILOT_MCP_` so Copilot cloud agent injects them only into MCP server processes',
  'Copilot cloud agent exposes environment secrets prefixed with `COPILOT_MCP_` specifically to configured MCP servers rather than hardcoding credentials in `mcp.json`.')
t('gh_mcp_toolsets_env',
  'Set `GITHUB_TOOLSETS="repos,issues,pull_requests,actions"` (and `--read-only` when appropriate) on the GitHub MCP server to trim context overhead and attack surface',
  'Limiting `GITHUB_TOOLSETS` reduces prompt token consumption from unused tool schemas and enforces least-privilege tool boundaries.')
t('webhook_hmac_sha256',
  'Validate `X-Hub-Signature-256` HMAC-SHA256 webhook signatures using a Key Vault-stored shared secret before enqueueing downstream agent or skill jobs',
  'Cryptographic HMAC verification blocks spoofed webhook payloads from triggering unauthorized automation or prompt-injection attacks.')
t('boards_gh_app_integration',
  'Install the official Azure Boards GitHub App (authenticated via OAuth/GitHub App installation, not personal PATs) and link target repositories to the Boards project',
  'The Azure Boards GitHub App provides resilient organization-level `AB#` commit/PR linking that survives individual employee offboarding.')

# ==============================================================================
# DOMAIN 2: Design and implement a source control strategy (10-15%)
# ==============================================================================
# 2.1 Branching & Git worktrees
t('trunk_based_dev',
  'Trunk-Based Development with short-lived branches (`< 24h`) merging frequently into `main` behind Azure App Configuration feature flags',
  'Trunk-based development minimizes merge drift and pairs with runtime feature flags to decouple code integration from customer release.')
t('github_flow_branch',
  'GitHub Flow (`main` is always deployable; short-lived topic/agent branches merge via pull request after automated CI checks and review)',
  'GitHub Flow keeps a single continuously deployable default branch ideal for SaaS microservices and cloud agent PR workflows.')
t('release_branch_flow',
  'Trunk-Based Development with immutable `release/x.y` branches cut for supported minor versions and cherry-picked hotfixes from `main`',
  'Release branches isolate multi-version customer maintenance (`v2.3`, `v2.4`) without stalling continuous feature integration on `main`.')
t('git_flow_legacy',
  'Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)',
  'Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow.')
t('git_worktree_add',
  'Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store',
  '`git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents.')
t('git_worktree_prune',
  'Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`',
  'Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish.')

# 2.2 PR workflows & Copilot branch rulesets
t('ruleset_copilot_autoreview',
  'Enable `Automatically request Copilot code review` (with `Review new pushes`) inside a GitHub Organization or Repository Branch Ruleset targeting `main`',
  'Branch rulesets can automatically trigger GitHub Copilot code review on PR creation and every subsequent push before human reviewers sign off.')
t('copilot_pr_no_self_approve',
  'Enforce required pull request reviews where the human who assigned the task to GitHub Copilot cloud agent cannot approve that agent-created PR alone',
  'GitHub blocks the user who initiated a Copilot cloud agent PR from serving as the sole required approver, ensuring independent human oversight.')
t('copilot_pr_extra_human_approval',
  'Require pull request reviews from `CODEOWNERS` plus at least one human reviewer with write access on non-human / Copilot-authored pull requests',
  'Copilot code review leaves `Comment` feedback rather than `Approve`, so required human reviews ensure accountable sign-off before merging agent PRs.')
t('ruleset_protect_agent_files',
  'Configure a GitHub Push/File-Path Ruleset + `CODEOWNERS` protecting `.github/workflows/**`, `.github/copilot-instructions.md`, `SKILL.md`, `AGENTS.md`, and `mcp.json`',
  'Protecting agent instruction, skill, MCP, and workflow files prevents unreviewed PRs or compromised branches from hijacking future agent runs.')
t('gh_merge_queue',
  'Enable GitHub Merge Queue (`merge_group` trigger) on `main` so approved PRs validate sequentially or in batches against the exact combined target state',
  'Merge Queue eliminates semantic `skew` breakage when high-velocity human and Copilot PRs pass CI individually against stale `main` commits.')
t('ado_build_validation_policy',
  'Configure an Azure Repos Branch Policy on `main` requiring Build Validation, `Minimum number of reviewers >= 2`, `Check for linked work items`, and comment resolution',
  'Azure Repos branch policies block direct pushes and enforce green CI builds, peer review, and `AB#` traceability prior to completion.')
t('squash_merge_mode',
  'Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR',
  'Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch.')
t('rebase_linear_mode',
  'Enforce `Rebase and fast-forward` (`Require linear history`) to preserve individual verified commits without merge-bubble commits',
  'Linear rebase preserves granular commit history while avoiding non-linear merge commits.')

# 2.3 Repo permissions, traceability & Git hooks
t('git_hooks_core_path',
  'Commit versioned client hooks in `.githooks/` (`pre-commit`, `commit-msg`) paired with `git config core.hooksPath .githooks` AND enforce server-side CI/Ruleset checks',
  'Versioned `.githooks/` catch formatting/secret mistakes locally in milliseconds, while server-side Rulesets/CI enforce compliance even if `--no-verify` is used.')
t('pre_commit_secret_lint_hook',
  'Run `pre-commit` hooks executing linter, secret-pattern detection, and unit smoke checks locally before commits are created',
  'Local `pre-commit` hooks shift feedback left before code ever leaves the developer workstation.')
t('commit_msg_workitem_hook',
  'Use a `commit-msg` Git hook validating Conventional Commits syntax and presence of a linked `AB#<id>` or `#<issue>` reference',
  '`commit-msg` hooks enforce structured commit metadata needed for automated changelog generation and work-item traceability.')
t('copilot_cli_pretooluse_hook',
  'Configure GitHub Copilot CLI hooks in `.github/hooks/*.json` (`preToolUse` / `userPromptSubmitted`) to block destructive shell commands and log audit events',
  'Copilot CLI lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) enforce deterministic policy checks before agent tool execution.')
t('git_signed_annotated_tag',
  'Create GPG/SSH-signed annotated Git tags (`git tag -s v2.4.0 -m "..."`) protected by Tag Rulesets so CI/CD builds immutable releases from verified refs',
  'Signed annotated tags combined with Tag Protection Rulesets prevent tag retargeting (`force-push`) and establish cryptographic release provenance.')
t('git_lfs_track',
  'Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps',
  'Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage.')
t('git_sparse_checkout',
  'Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces',
  'Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos.')
t('ado_repo_contribute_bypass',
  'Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`',
  'Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls.')

# 2.4 Repo migration (`gh ado2gh`) & Git recovery/removal
t('gh_ado2gh_install',
  'Install the official GitHub CLI extension `gh extension install github/gh-ado2gh` and authenticate via scoped `ADO_PAT` and `GH_PAT` environment variables',
  '`gh-ado2gh` (powered by GitHub Enterprise Importer) is Microsoft and GitHubs official CLI tool for migrating Azure Repos to GitHub Enterprise Cloud.')
t('gh_ado2gh_generate_script_all',
  'Run `gh ado2gh generate-script --ado-org <src> --github-org <dst> --output migrate.ps1 --all --download-migration-logs`',
  'Passing `--all` generates an auditable PowerShell migration script that migrates repos, creates teams, rewires Azure Pipelines, and integrates Azure Boards.')
t('gh_ado2gh_migrate_repo',
  'Execute `gh ado2gh migrate-repo --ado-org <src> --ado-team-project <proj> --ado-repo <repo> --github-org <dst> --github-repo <repo>` after `lock-ado-repo`',
  '`gh ado2gh migrate-repo` migrates Git commits, branches, PRs, and review history for an individual Azure DevOps repository into GitHub.')
t('gh_ado2gh_download_logs',
  'Run `gh ado2gh download-logs` (or `--download-migration-logs`) to archive detailed GitHub Enterprise Importer audit and warning logs for every migrated repo',
  'Downloading migration logs lets platform engineers verify PR metadata fidelity and troubleshoot skipped attachments or user mappings.')
t('gh_ado2gh_freeze_no_delta',
  'Freeze writes on the source Azure DevOps repository (`lock-ado-repo`) during cutover because `gh ado2gh` / GEI does not support incremental delta migrations',
  'GitHub Enterprise Importer performs a point-in-time snapshot migration with no delta sync, so locking the source repo prevents lost mid-cutover commits.')
t('git_filter_repo_purge',
  'Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches',
  '`git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs.')
t('git_reflog_recover',
  'Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch',
  '`git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly.')
t('git_revert_safe',
  'Run `git revert <commit-sha>` in a pull request to undo a faulty commit on protected `main` without rewriting shared public Git history',
  '`git revert` creates a new inverse commit preserving linear auditability and avoiding force-pushes on shared branches.')

# ==============================================================================
# DOMAIN 3: Design and implement build and release pipelines (35-40%)
# ==============================================================================
# 3.1-3.2 Package management & versioning
t('artifacts_feed_upstream',
  'Single Azure Artifacts feed with Upstream Sources enabled (`npmjs.com`, `nuget.org`, `pypi.org`) so resolved public packages are cached immutably',
  'Upstream Sources cache external OSS dependencies inside your Azure Artifacts feed, protecting CI builds if public registries suffer outages or package yanks.')
t('artifacts_view_local',
  'Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete',
  '`@Local` holds newly published internal packages prior to quality promotion.')
t('artifacts_view_prerelease',
  'Promote release-candidate builds (`1.4.0-rc.2`) to the `@Prerelease` feed view for early-adopter integration consumers',
  '`@Prerelease` exposes vetted pre-release packages to internal consumer teams without polluting production `@Release` consumers.')
t('artifacts_view_release',
  'Promote fully validated immutable packages to the `@Release` feed view and configure production builds to restore exclusively from `feed@Release`',
  'Feed views (`@Local -> @Prerelease -> @Release`) enforce artifact promotion governance without recompiling binaries.')
t('gh_packages_ghcr',
  'Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC',
  'GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls.')
t('semver_versioning',
  'Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes',
  'SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades.')
t('calver_versioning',
  'Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots',
  'CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts.')
t('universal_packages_ado',
  'Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles',
  'Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale.')
t('oci_digest_immutability',
  'Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags',
  'Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set.')
t('package_immutability_rule',
  'Increment the `PATCH` or `prerelease` version (`1.2.1`) because published `package@version` coordinates in Azure Artifacts are permanently immutable',
  'Once a version is published to Azure Artifacts, that exact version number can never be overwritten even if unlisted or deleted.')

# 3.3-3.5 Testing strategy with GitHub Copilot & MCP servers
t('copilot_mcp_gate_author',
  'Use GitHub Copilot connected to Azure DevOps / GitHub MCP servers to inspect historical pipeline failure logs and generate automated quality/release gate definitions',
  'MCP tools give Copilot live context on pipeline definitions, build logs, and alert metrics so it scaffolds accurate quality and release gates.')
t('publish_test_results_v2',
  'Configure `PublishTestResults@2` (with `condition: succeededOrFailed()`) exporting JUnit/TRX XML so failed builds still surface test failure stack traces and Boards links',
  '`succeededOrFailed()` ensures test result XML is uploaded even when unit or integration test suites exit with non-zero status.')
t('publish_code_coverage_v2',
  'Run Cobertura/OpenCover instrumentation with `PublishCodeCoverageResults@2` and use Copilot + MCP tools to generate targeted unit tests for uncovered PR diff paths',
  'Combining coverage reporting with Copilot + MCP PR diff inspection focuses test generation on newly modified, high-risk branches.')
t('pr_diff_coverage_policy',
  'Enforce a Pull Request Status Policy requiring `>= 80%` diff code coverage on newly changed lines while ratcheting legacy baseline coverage upward',
  'Diff coverage gates stop new untested code immediately without freezing legacy repositories below global coverage targets.')
t('azure_load_testing_yaml',
  'Run `AzureLoadTest@1` (or `azure/load-testing@v1`) in staging YAML with declarative `failureCriteria` (`p90(response_time_ms) > 300`, `percentage(error) > 1`)',
  'Azure Load Testing evaluates server-side telemetry and JMeter/Locust percentile thresholds automatically as a repeatable CI/CD gate.')
t('playwright_sharded_e2e',
  'Execute headless Playwright end-to-end tests sharded across parallel matrix runners (`--shard=${{ matrix.shard }}`) capturing trace/video artifacts on failure',
  'Sharded Playwright tests compress UI regression wall-clock time while preserving rich failure traces for Copilot or human debugging.')
t('testcontainers_integration',
  'Run Ephemeral Docker `Testcontainers` integration tests inside CI jobs against real PostgreSQL/Redis containers before mocking external third-party APIs',
  'Testcontainers catch real SQL dialect, serialization, and migration defects quickly without shared brittle staging environments.')
t('flaky_test_quarantine',
  'Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs',
  'Quarantining and fixing flaky tests restores developer trust in red CI builds without blinding pipelines to genuine regressions.')
t('deployment_gate_monitor_alert',
  'Configure an Azure Pipelines Environment `Invoke REST API` / `Query Azure Monitor Alerts` check between deployment rings with `Timeout > Evaluation delay + interval`',
  'Automated post-deploy Azure Monitor checks halt ring progression automatically whenever error rate or latency alerts fire.')

# 3.6-3.7 Azure Pipelines, GitHub Actions & agent/runner infrastructure
t('managed_devops_pool_vnet',
  'Deploy Azure Managed DevOps Pools injected into your private VNet with stateless ephemeral (`Fresh agent every time`) VM images and predictive scaling',
  'Managed DevOps Pools deliver private VNet reachability and custom tool images without the OS patching burden of classic self-hosted VMs.')
t('arc_k8s_ephemeral_runners',
  'Deploy Actions Runner Controller (ARC) Runner Scale Sets on AKS creating single-use ephemeral Kubernetes runner pods inside your private network',
  'ARC autoscales zero-to-N ephemeral GitHub Actions pods inside private AKS clusters and destroys each pod cleanly after one job.')
t('gh_larger_runners_static_ip',
  'Use GitHub-hosted Larger Runners (or Azure VNet-integrated GitHub-hosted runners) when builds need high CPU/RAM, GPU, or private network egress without managing Kubernetes',
  'Larger/VNet GitHub-hosted runners combine zero runner maintenance with high compute specs and private Azure VNet connectivity.')
t('ado_vs_gha_selection',
  'Select GitHub Actions when consolidating repos, GHAS, Copilot cloud agent, and `gh-aw` on GitHub; retain or integrate Azure Pipelines when deep TFVC/classic release gates or existing Boards/Artifacts governance require it',
  'Platform selection weighs ecosystem consolidation (Copilot coding agent, GHAS, `gh-aw`) against existing Azure DevOps classic gates, TFVC, or hybrid compliance investments.')
t('yaml_extends_required_tpl',
  'Configure a Required YAML Template check on the `production` Environment verifying pipelines `extends:` your central security template (`security/prod-base.yml@templates`)',
  '`extends:` + Required Template checks enforce mandatory secret/SAST/SBOM steps at the platform layer so app repos cannot omit them.')
t('yaml_matrix_strategy',
  'Use `strategy: matrix` (`os` x `runtime` combinations) with `fail-fast: false` when full cross-platform compatibility results are needed on every PR',
  'Matrix strategies fan out builds concurrently while `fail-fast: false` collects diagnostics across all target OS/SDK combinations.')
t('yaml_stage_depends_fanin',
  'Configure regional deploy stages with `dependsOn: [Build]` to run in parallel, followed by `GlobalSmoke` with `dependsOn: [Deploy_East, Deploy_West, Deploy_EU]`',
  'Explicit `dependsOn` arrays express fan-out parallelism followed by fan-in synchronization in multi-stage YAML.')
t('yaml_variable_group_kv',
  'Link an Azure Pipelines Variable Group to Azure Key Vault with Pipeline Permissions restricted to authorized YAML pipelines and secret variables auto-masked',
  'Key Vault-backed Variable Groups fetch current secrets dynamically at runtime and restrict consumption to explicitly authorized pipelines.')
t('yaml_isoutput_crossstage',
  'Emit `##vso[task.setvariable variable=imgDigest;isOutput=true]` (or `$GITHUB_OUTPUT` in Actions) and reference `stageDependencies.<Stage>.<Job>.outputs[...]` downstream',
  '`isOutput=true` (and `$GITHUB_OUTPUT`) passes immutable build metadata cleanly across isolated jobs and deployment stages.')
t('yaml_env_approval_hours',
  'Configure YAML `environment: production` with Approvals (`approvers cannot approve their own runs`), Business Hours check, and Exclusive Lock (`runLatest`)',
  'YAML Environment checks enforce separation of duties, maintenance windows, and serialized deployment state outside repo YAML.')
t('yaml_trigger_paths_filter',
  'Scope YAML `trigger.paths.include` / `on.push.paths` to `services/payments/**` and `libs/shared/**` so unrelated monorepo commits skip unnecessary builds',
  'Path-filtered triggers dramatically cut runner queue contention and CI cost in multi-service monorepos.')
t('copilot_yaml_pipeline_gen',
  'Use GitHub Copilot with workspace/MCP context to scaffold multi-stage YAML pipelines and validate schema via the Azure Pipelines `Preview` REST API or `actionlint`',
  'Validating AI-generated YAML against the compiler/linter catches invalid task inputs and expression scoping bugs before merging.')

# 3.8 GitHub Agentic Workflows (gh-aw)
t('gh_aw_markdown_frontmatter',
  'Author a GitHub Agentic Workflow in `.github/workflows/<name>.md` combining YAML frontmatter (`on`, `permissions: read-all`, `safe-outputs`, `tools`) with natural-language instructions',
  '`gh-aw` workflows are authored in Markdown `.md` files with declarative security frontmatter rather than brittle ad-hoc prompt scripts.')
t('gh_aw_compile_lock_yml',
  'Compile `.github/workflows/<name>.md` using `gh aw compile` into `.github/workflows/<name>.lock.yml` and commit both files to the repository',
  'GitHub Actions executes the compiled `.lock.yml` file; editing `.lock.yml` by hand breaks integrity and is overwritten on recompilation.')
t('gh_aw_read_all_default',
  'Run the `gh-aw` AI reasoning job in a sandboxed container with `permissions: read-all` (or `contents: read`) and network firewall isolation by default',
  'Running the agent job read-only prevents prompt injection inside untrusted issue/PR text from directly mutating repository code or secrets.')
t('gh_aw_safe_outputs_pr',
  'Declare `safe-outputs: create-pull-request:` in `.md` frontmatter so code/doc updates are validated and opened as reviewable draft PRs by a separate permission-scoped job',
  '`safe-outputs` isolates GitHub write permissions into deterministic post-processing jobs with branch prefixes, title prefixes, and caps.')
t('gh_aw_safe_outputs_comment',
  'Declare `safe-outputs: add-comment:` / `add-labels:` so issue triage agents post sanitized, rate-limited comments and labels without holding `issues: write` inside the LLM container',
  'Separating read-only LLM inference from sanitized `safe-outputs` comment/label jobs enforces defense-in-depth on public and enterprise repos.')
t('gh_aw_update_actions_cmd',
  'Update pinned action SHAs inside `.lock.yml` exclusively via `gh aw update-actions` / `gh aw compile` rather than merging raw Dependabot edits to `.lock.yml`',
  'Raw edits to `.lock.yml` diverge from the `.md` source specification; `gh aw compile` / `gh aw update-actions` preserves compiler guardrails.')
t('gh_aw_complementary_cicd',
  'Use GitHub Agentic Workflows (`gh-aw`) for judgment-driven triage, doc drift sync, and CI failure root-cause reports while keeping deterministic YAML for compilation, signing, and prod deploys',
  'Agentic workflows augment deterministic CI/CD where reasoning helps, whereas reproducible compilation, artifact signing, and prod rollouts must remain deterministic.')

# 3.9 Deployments
t('deploy_blue_green_slots',
  'Blue-Green deployment using Azure App Service Deployment Slots (`staging` warmed via `applicationInitialization` + smoke tests, then instant VIP swap to `Production`)',
  'Blue-Green slot swaps shift 100% of live traffic seamlessly after warm-up while keeping the previous `Blue` build warm for instant swap-back.')
t('deploy_canary_traffic',
  'Canary deployment routing 5%-10% of live traffic via Azure Container Apps revision weights (or Front Door / Service Mesh) while evaluating p95 latency and HTTP 5xx gates',
  'Canary traffic splitting limits real-world blast radius to a small traffic slice before progressive promotion.')
t('deploy_ring_progressive',
  'Progressive Exposure Rings (`Canary Internal -> Early Adopters -> Regional Prod -> Global`) separated by bake times and automated telemetry checks',
  'Ring-based progressive exposure validates production behavior across increasingly broad user cohorts.')
t('appconfig_feature_targeting',
  'Azure App Configuration Feature Manager with `Microsoft.Targeting` filters enabling features incrementally by user IDs, Entra groups, and rollout percentages',
  '`Microsoft.Targeting` decouples code deployment from feature activation and guarantees sticky cohort assignment.')
t('appconfig_timewindow_flag',
  'Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers',
  '`Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime.')
t('ab_testing_experiment',
  'A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events',
  'A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts.')
t('slot_pinned_setting',
  'Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps',
  'Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`.')
t('slot_auto_swap_warmup',
  'Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps',
  'Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps.')
t('sql_dacpac_idempotent',
  'Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`',
  'Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates.')
t('ef_migration_bundle',
  'Generate a self-contained EF Core migration bundle (`dotnet ef migrations bundle`) in CI and execute it as an idempotent pre-deploy job using Managed Identity / OIDC',
  'Pre-compiled EF migration bundles run deterministically inside isolated deploy stages without requiring SDK source compilation on prod targets.')
t('hotfix_cherrypick_tag',
  'Branch `hotfix/*` from the production release tag (or merge to `main` + cherry-pick to `release/x.y`) through an expedited pipeline retaining mandatory security scans and smoke tests',
  'Expedited hotfix paths skip unrelated queued feature work without bypassing security scanning, peer review, or back-merge discipline.')
t('rolling_aks_maxunavailable',
  'Configure Kubernetes `RollingUpdate` (`maxUnavailable: 0, maxSurge: 25%`) paired with `readinessProbe` and `PodDisruptionBudget` on AKS deployments',
  'Zero `maxUnavailable` with readiness probes ensures new pods pass health checks before old pods drain connections.')

# 3.10 IaC & configuration management
t('bicep_what_if_preflight',
  'Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply',
  'ARM `what-if` previews live Azure state mutations against target resource groups before executing changes.')
t('bicep_deployment_stack_deny',
  'Deploy Bicep templates via Azure Deployment Stacks (`az stack group create`) with `--action-on-unmanage deleteResources` and `--deny-settings-mode denyWriteAndDelete`',
  'ARM Deployment Stacks manage multi-resource lifecycles atomically and block unauthorized manual portal drift via deny assignments.')
t('azure_deployment_environments',
  'Use Azure Deployment Environments (ADE) backed by catalog Bicep templates and per-environment Managed Identities so developers self-provision governed, auto-expiring sandboxes',
  'ADE lets developers spin up compliant dev/test infrastructure on demand without granting raw subscription `Owner` permissions.')
t('azure_machine_configuration',
  'Enforce guest OS baselines across Azure and Arc-enabled servers using Azure Policy Machine Configuration (`Guest Configuration`) packages audited continuously in Azure Resource Graph',
  'Azure Machine Configuration audits and remediates inside-VM OS/security settings natively via Azure Policy across cloud and hybrid Arc servers.')
t('bicep_acr_private_modules',
  'Publish versioned organizational Bicep modules (`br:corp.azurecr.io/bicep/aks:v2.1`) to a private Azure Container Registry (or Azure Verified Modules)',
  'Private ACR Bicep registries distribute governed, reusable infrastructure building blocks across application repositories.')
t('bicep_keyvault_reference',
  'Reference secrets dynamically via `getSecret()` on an existing Key Vault resource inside `.bicepparam` / Bicep modules with `@secure()` parameters',
  '`@secure()` + Key Vault `getSecret()` keeps sensitive values out of Git parameter files and ARM deployment history.')

# 3.11 Maintain pipelines
t('actions_cache_lockfile',
  'Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles(\'**/package-lock.json\') }}` with `restore-keys` fallback',
  'Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change.')
t('pipeline_cache_v2_task',
  'Configure `Cache@2` in Azure Pipelines keyed on `"nuget" | "$(Agent.OS)" | **/packages.lock.json` paired with `--locked-mode` restore',
  '`Cache@2` skips redundant package downloads across hosted runs when lockfiles match.')
t('gha_concurrency_cancel',
  'Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys',
  'Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments.')
t('ado_batch_true_trigger',
  'Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active',
  '`batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds.')
t('artifact_retention_lease',
  'Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases)',
  'Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production.')
t('pipeline_analytics_p95',
  'Review Azure Pipelines / GitHub Actions Workflow Insights (`Pass rate`, `p95 duration`, task timeline bottlenecks, and flaky failures) to target caching and sharding optimizations',
  'Data-driven task duration and failure analytics pinpoint slow steps and flaky tests with the highest ROI.')

# ==============================================================================
# DOMAIN 4: Design and implement a security and compliance plan (15-20%)
# ==============================================================================
# 4.1 AuthN & AuthZ
t('oidc_gha_idtoken_write',
  'Configure Entra Workload Identity Federation scoped to `repo:<org>/<repo>:environment:production` and set job `permissions: { id-token: write, contents: read }` with `azure/login@v2`',
  'OIDC Workload Identity Federation exchanges short-lived GitHub tokens for Entra access tokens with zero stored client secrets.')
t('oidc_ado_wif_connection',
  'Create an Azure Resource Manager service connection using `Workload Identity federation (automatic)` scoped to the target resource group and restricted via Pipeline Permissions',
  'Workload Identity Federation eliminates expiring service-principal secrets and secret-rotation outages in Azure DevOps.')
t('managed_identity_user_assigned',
  'Assign a User-Assigned Managed Identity to Azure compute / Managed DevOps Pools / ADE environments for secretless Azure resource authentication',
  'Managed Identities are platform-managed Entra identities with automatic credential lifecycle and zero developer-accessible secrets.')
t('service_principal_vs_mi',
  'Prefer Managed Identities for Azure-hosted resources and Workload Identity Federation for external CI/CD (GitHub Actions / ADO), avoiding secret-backed Service Principals',
  'Eliminating password/certificate-backed Service Principals removes credential theft and expiration risks across both runtime and CI/CD.')
t('github_app_short_token',
  'Authenticate cross-repository org automation with an installation-scoped GitHub App minting 1-hour installation tokens (`actions/create-github-app-token`) instead of personal PATs',
  'GitHub Apps provide bot-attributed audit trails, fine-grained repository permissions, and short-lived 1-hour tokens independent of human accounts.')
t('github_token_job_scoped',
  'Set top-level workflow `permissions: {}` (or `contents: read`) and elevate `GITHUB_TOKEN` scopes (`packages: write`, `pull-requests: write`) only on specific jobs requiring them',
  'Least-privilege job-scoped `GITHUB_TOKEN` permissions limit blast radius if a third-party action or script behaves unexpectedly.')
t('fine_grained_pat_scoped',
  'When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions',
  'Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs.')
t('ado_stakeholder_access',
  'Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access',
  'Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects.')
t('ado_basic_testplans_access',
  'Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)',
  'Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`.')
t('ado_project_scoped_build_id',
  'Enable `Limit job authorization scope to current project for non-release and release pipelines` and `Protect access to repositories in YAML pipelines` at the org level',
  'Project-scoped build tokens block compromised pipelines in one project from reading source repositories across the entire Azure DevOps organization.')

# 4.2 Sensitive information in automation
t('kv_task_runasprejob',
  'Use `AzureKeyVault@2` (`SecretsFilter: "sql-conn,signing-key"`, `RunAsPreJob: false`) or `Azure/get-keyvault-secrets` over OIDC fetching only required named secrets at deploy time',
  'Fetching named Key Vault secrets just-in-time over OIDC avoids wildcard `SecretsFilter: "*"` over-exposure and keeps secrets out of Git.')
t('ado_secure_files_cert',
  'Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)',
  'Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion.')
t('gha_environment_secrets',
  'Store production deployment secrets inside a protected GitHub Environment (`production`) gated by required human reviewers and deployment branch rules (`main` only)',
  'Environment secrets remain inaccessible to untrusted PR workflows and unlock only after environment branch/approval checks pass.')
t('mask_secret_add_mask',
  'Immediately emit `echo "::add-mask::$DYNAMIC_SECRET"` in GitHub Actions (or `##vso[task.setvariable variable=tok;issecret=true]` in ADO) before passing dynamic tokens to `$GITHUB_OUTPUT`',
  'Registering runtime-generated secrets with the runner log scrubber masks accidental stdout/trace leakage throughout the job.')
t('pull_request_target_hazard',
  'Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets',
  '`pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration.')
t('oidc_copilot_env_federation',
  'Configure the special `copilot` GitHub Environment with OIDC federated credentials and `COPILOT_MCP_*` secrets so `copilot-setup-steps` accesses private feeds/MCP without Git secrets',
  'The `copilot` environment isolates credentials needed by Copilot cloud agent setup steps and MCP servers away from source files.')
t('key_vault_rbac_officer',
  'Enable `Azure role-based access control` on Key Vault granting deploy identities `Key Vault Secrets User` (read-only) and reserving `Key Vault Secrets Officer` for rotation pipelines',
  'Key Vault RBAC separates read-only secret consumption (`Secrets User`) from secret mutation (`Secrets Officer`) at individual secret scope.')

# 4.3 Security & compliance scanning
t('ghas_codeql_sast',
  'Enable CodeQL semantic code scanning (Default or Advanced setup) on PRs and scheduled `main` runs, surfacing SARIF dataflow alerts in the GitHub/ADO `Security` tab',
  'CodeQL analyzes AST and taint dataflow to catch SQLi, SSRF, XSS, and deserialization flaws prior to merge.')
t('ghas_secret_push_protection',
  'Enable GHAS / GHAzDO Secret Scanning with Push Protection plus custom org regex patterns so commits containing credentials are rejected synchronously on `git push`',
  'Push Protection prevents high-confidence secrets from ever landing in remote repository history.')
t('ghas_dependency_review_action',
  'Run `actions/dependency-review-action@v4` on pull requests configured with `fail-on-severity: high` and `deny-licenses: [AGPL-3.0, GPL-3.0]` alongside Dependabot updates',
  'Dependency Review blocks newly introduced vulnerable packages and disallowed copyleft licenses directly inside the pull request.')
t('ghazdo_oneclick_deps',
  'Enable GitHub Advanced Security for Azure DevOps (GHAzDO) toggle-based `Dependency scanning` (or `AdvancedSecurity-Dependency-Scanning@1`) to inspect manifests without YAML edits',
  'GHAzDO supports zero-YAML toggle-enabled pipeline dependency scanning as well as explicit task placement after build restore.')
t('copilot_agent_builtin_secscan',
  'Leverage GitHub Copilot cloud agents built-in pre-PR validation (CodeQL SAST, GitHub Advisory Database dependency checks, and secret scanning) on agent-generated commits',
  'Copilot cloud agent automatically scans its own generated changes with CodeQL, Advisory DB, and secret detection before finalizing pull requests.')
t('defender_cloud_devops_connector',
  'Connect GitHub Enterprise and Azure DevOps organizations to Microsoft Defender for Cloud (DevOps Security) to correlate code/IaC/container SARIF findings with live cloud attack paths',
  'Defender for Cloud DevOps Security bridges CNAPP runtime context (internet exposure, identity privileges) with repository vulnerabilities for risk-prioritized remediation and PR annotations.')
t('container_trivy_ci_scan',
  'Scan built container images with Trivy / Defender CLI in CI (`--exit-code 1 --severity HIGH,CRITICAL`) uploading SARIF reports before pushing to ACR or `ghcr.io`',
  'Pre-push OCI image scanning stops vulnerable OS packages and application layers before registries distribute them.')
t('sbom_spdx_attestation',
  'Generate SPDX / CycloneDX SBOMs (`ManifestGeneratorTask@0` or `actions/attest-build-provenance`) signed with OIDC provenance attestations on every release build',
  'Signed SBOMs and SLSA build attestations prove artifact origin and enable rapid zero-day CVE impact queries.')

# ==============================================================================
# DOMAIN 5: Implement an instrumentation strategy (15-20%)
# ==============================================================================
# 5.1 Monitoring for Azure DevOps & GitHub platforms
t('ado_lead_cycle_widgets',
  'Configure an Azure DevOps Dashboard combining Lead Time, Cycle Time, Cumulative Flow, Deployment Frequency, and Sprint Burndown Analytics widgets',
  'Native Analytics widgets provide real-time engineering flow and DORA visibility directly from Boards and Pipelines data.')
t('ado_audit_stream_sentinel',
  'Configure Azure DevOps Auditing Streaming (and GitHub Enterprise Audit Log Streaming) forwarding admin/permission/secret events into Azure Monitor Log Analytics / Sentinel',
  'Streaming platform audit logs to Log Analytics enables tamper-evident retention and KQL anomaly alerting on permission escalations or bypassed policies.')
t('gh_insights_metrics',
  'Use GitHub Insights, Pull Request / Actions Performance metrics, and custom Issues/Projects charts to track PR review turnaround, queue wait times, and CI failure trends',
  'GitHub Insights and Projects charts surface PR review bottlenecks and Actions runner saturation natively across repositories.')
t('pipeline_failure_alert_rule',
  'Forward Azure DevOps / GitHub Actions diagnostic and webhook events into Log Analytics and trigger an Azure Monitor Scheduled Query Alert on repeated `main` build or prod stage failures',
  'Centralizing pipeline telemetry in Log Analytics enables correlated KQL alerting when CI pass rates decline or release stages fail.')
t('gha_webhook_monitor_ingest',
  'Subscribe a GitHub Organization Webhook (`workflow_run`, `deployment_status`) to an Azure Monitor Logs Ingestion endpoint to chart enterprise-wide DORA metrics in Azure Workbooks',
  'Ingesting `workflow_run` and `deployment_status` events into Log Analytics unifies GitHub Actions and Azure runtime telemetry in one KQL workspace.')

# 5.2 Azure Copilot Observability Agent
t('obs_agent_ondemand_rbac',
  'Invoke Azure Copilot Observability Agent on-demand from Azure Copilot chat or Application Insights / AKS blades, operating strictly within the signed-in users Azure RBAC, PIM, and resource locks',
  'On-demand Observability Agent investigations require zero pre-provisioning and never bypass the callers Azure RBAC permissions, Policies, or locks.')
t('obs_agent_resource_autonomous',
  'Provision an Azure Copilot Observability Agent resource with custom topology/runbook instructions and opt in to autonomous background alert correlation',
  'While interactive chat works without setup, background autonomous alert correlation and custom operational instructions require an Observability Agent resource.')
t('obs_agent_amw_association',
  'Associate the target Azure subscription with an Azure Monitor Workspace (AMW) so Azure Copilot Observability Agent can create and persist unified Azure Monitor Issues',
  'Subscription association with an Azure Monitor Workspace (AMW) is mandatory to enable Azure Monitor Issues for Observability Agent investigations.')
t('obs_agent_monitor_issues',
  'Review unified Azure Monitor Issues (`[<AppName>]` prefix for autonomous alerts) aggregating related alerts, Golden Signals anomalies, root-cause hypotheses, and mitigation steps',
  'Observability Agent collapses correlated alert storms into an Azure Monitor Issue timeline with root-cause evidence across metrics, logs, and traces.')
t('obs_agent_privacy_no_train',
  'Rely on Microsofts enterprise data boundary guarantee that customer prompts, telemetry, and outputs in Azure Copilot Observability Agent are never used to train foundation models',
  'Azure Copilot Observability Agent keeps telemetry within enterprise compliance boundaries and never trains public/foundation LLMs on customer data.')
t('obs_agent_custom_instructions',
  'Add custom architectural context, naming conventions, and triage preferences to the Observability Agent resource so autonomous investigations reflect service-specific domain rules',
  'Custom agent instructions teach the Observability Agent your service topology, SLO priorities, and team-specific troubleshooting heuristics.')

# 5.3 Azure SRE Agent
t('sre_agent_single_incident_plat',
  'Connect Azure SRE Agent (`sre.azure.com`) to its active incident platform (`Azure Monitor`, `PagerDuty`, or `ServiceNow` — one incident platform per agent at a time)',
  'Each Azure SRE Agent instance connects natively to one primary incident management system (Azure Monitor, PagerDuty, or ServiceNow) at a time.')
t('sre_agent_servicenow_group',
  'Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents',
  'Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise.')
t('sre_agent_response_plan',
  'Create an Incident Response Plan in Azure SRE Agent specifying alert filters (service, severity, title), linked runbook instructions, and the target autonomy level',
  'Without at least one matching Incident Response Plan, Azure SRE Agent will not automatically scan or triage incoming platform incidents.')
t('sre_agent_review_vs_autonomous',
  'Configure the Incident Response Plan autonomy level to `Review` (human-in-the-loop approval before remediation) in production before graduating low-risk tasks to `Autonomous`',
  '`Review` mode lets Azure SRE Agent diagnose root cause and propose `az`/K8s mitigations while requiring explicit operator approval prior to execution.')
t('sre_agent_cooldown_3h',
  'Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations',
  'Alert reinvestigation cooldown suppresses redundant agent loops when a noisy metric alert fires repeatedly during an ongoing incident.')
t('sre_agent_repo_correlation',
  'Connect GitHub or Azure DevOps repositories to Azure SRE Agent so incident investigations correlate latency/error spikes with recent commits, PR diffs, and deployments, and open fix PRs',
  'Repository integration lets Azure SRE Agent link runtime regressions directly to suspect code changes and draft remediation pull requests.')
t('sre_agent_scheduled_tasks',
  'Configure Scheduled Tasks in Azure SRE Agent to run proactive daily drift checks, certificate expiry audits, and capacity health summaries outside active incidents',
  'Scheduled Tasks extend Azure SRE Agent beyond reactive firefighting into proactive recurring reliability checks.')
t('sre_agent_mcp_integration',
  'Connect custom internal knowledge bases or ticketing tools to Azure SRE Agent via Model Context Protocol (MCP) connectors alongside Managed Identity Azure RBAC',
  'Azure SRE Agent supports MCP server extensions so investigations query internal runbooks, feature-flag states, or custom telemetry safely.')

# 5.4 AI-assisted metric & log analysis + Copilot agent logs
t('kql_percentile_p95',
  'Run `AppRequests | where TimeGenerated > ago(1h) | summarize p95=percentile(DurationMs, 95), errRate=countif(Success == false)*100.0/count() by bin(TimeGenerated, 5m)`',
  'KQL `percentile(DurationMs, 95)` and `countif(Success == false)` accurately expose tail-latency spikes and error ratios hidden by simple `avg()` metrics.')
t('nl_to_kql_copilot_query',
  'Interrogate Log Analytics and Application Insights via natural-language prompts in Azure Copilot / Observability Agent, inspecting and executing the generated KQL query',
  'Natural-language-to-KQL translation accelerates incident triage while keeping the exact underlying KQL query transparent and verifiable.')
t('appinsights_w3c_traceparent',
  'Enable OpenTelemetry / Application Insights SDKs propagating W3C Trace Context (`traceparent`) across HTTP gateways, Service Bus queues, and AKS microservices',
  'W3C `traceparent` correlates distributed `AppRequests` and `AppDependencies` under a single `operation_Id` on the Application Map.')
t('appinsights_adaptive_sampling',
  'Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting',
  'Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts.')
t('appinsights_release_annotation',
  'Emit Application Insights Release Annotations from CD pipelines on every ring promotion so Azure SRE Agent and performance charts correlate metric shifts with exact build versions',
  'Release Annotations mark deployment timestamps directly on latency, failure, and CPU timelines.')
t('copilot_session_logs_commit',
  'Inspect GitHub Copilot cloud agent session logs via the `Copilot` tab / verified commit trailer links (or `gh agent-task view --log`) to audit reasoning, MCP tool calls, and token usage',
  'Every Copilot cloud agent session records full reasoning steps and tool invocations linked directly from its verified commits and PR timeline.')
t('copilot_cli_hooks_audit_jsonl',
  'Configure `.github/hooks/*.json` lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) writing secret-redacted JSONL audit records plus Enterprise Audit Log streaming',
  'Copilot CLI hooks capture granular local/CI prompt and tool-invocation audit trails (with regex secret redaction) for regulated compliance.')
t('aks_container_insights_oom',
  'Query AKS Container Insights (`KubePodInventory` / `ContainerInventory` / `InsightsMetrics`) via KQL or SRE Agent to detect `OOMKilled` (`exitCode 137`) and CPU throttling (`cfs_throttled`)',
  'Container Insights exposes cgroup memory working-set limits, `OOMKilled` terminations, and CPU throttling alongside node pressure metrics.')
t('ama_dcr_log_collection',
  'Deploy the Azure Monitor Agent (AMA) governed by Data Collection Rules (DCRs) with workspace transformation KQL dropping verbose `Debug` lines at ingestion',
  'AMA + DCRs replace retired MMA/OMS agents and filter noisy logs before Log Analytics ingestion charges apply.')

# ==============================================================================
# CONCISE COMPLETION TOKENS (`____` YAML / JSON / Bicep / KQL / CLI items)
# ==============================================================================
t('tok_copilot_setup_steps',
  '`copilot-setup-steps` (single job name inside `.github/workflows/copilot-setup-steps.yml` on the default branch)',
  'GitHub Copilot cloud agent executes only the job literally named `copilot-setup-steps` inside `.github/workflows/copilot-setup-steps.yml`.')
t('tok_apply_to',
  '`applyTo` (YAML frontmatter glob property inside `.github/instructions/<name>.instructions.md`, e.g., `applyTo: "**/*.bicep"`)',
  '`applyTo` scopes custom Copilot instruction files to matching repository file globs.')
t('tok_safe_outputs',
  '`safe-outputs` (declarative frontmatter block in `gh-aw` `.md` workflows isolating write actions like `create-pull-request` and `add-comment`)',
  '`safe-outputs` runs sanitized GitHub write operations in separate permission-scoped jobs outside the sandboxed LLM container.')
t('tok_gh_aw_compile',
  '`gh aw compile` (CLI command compiling `.github/workflows/<name>.md` into executable `.github/workflows/<name>.lock.yml`)',
  '`gh aw compile` validates frontmatter schemas, pins action SHAs, and generates the hardened `.lock.yml` Actions workflow.')
t('tok_ado2gh_all',
  '`--all` (flag on `gh ado2gh generate-script` that rewires pipelines, configures Azure Boards links, and maps teams/permissions)',
  '`--all` enables end-to-end migration rewiring across Repos, Boards, and Pipelines in `gh ado2gh generate-script`.')
t('tok_worktree_add',
  '`git worktree add` (creates an isolated working directory on a separate branch sharing the same local `.git` repository)',
  '`git worktree add ../agent-2 -b fix/auth` lets multiple local CLI agents edit and test independent branches simultaneously.')
t('tok_copilot_mcp_prefix',
  '`COPILOT_MCP_` (required secret/variable name prefix inside the `copilot` GitHub Environment for MCP server credentials)',
  'Copilot cloud agent passes environment secrets prefixed with `COPILOT_MCP_` into configured MCP server processes.')
t('tok_id_token_write',
  '`id-token: write` (GitHub Actions job permission required for `azure/login@v2` to request an OIDC JWT for Entra federation)',
  'Without `id-token: write`, the GitHub runner cannot mint an OIDC token for secretless Azure login.')
t('tok_add_mask',
  '`::add-mask::` (GitHub Actions workflow command registering a runtime string with the runner log scrubber)',
  '`echo "::add-mask::$VAL"` prevents dynamic secrets from printing in cleartext step logs.')
t('tok_what_if',
  '`what-if` (`az deployment group what-if` subcommand previewing ARM resource creations, modifications, and deletions)',
  '`what-if` calculates live infrastructure diffs before applying Bicep templates.')
t('tok_deny_write_delete',
  '`denyWriteAndDelete` (`--deny-settings-mode` value on `az stack group create` blocking unauthorized manual edits and deletions)',
  '`denyWriteAndDelete` enforces immutable IaC governance on resources managed by an ARM Deployment Stack.')
t('tok_assignment_group',
  '`assignment_group` (mandatory ServiceNow filter field when connecting Azure SRE Agent to a ServiceNow instance)',
  'Azure SRE Agent requires an explicit ServiceNow `assignment_group` so incident indexing stays scoped to the owning team.')
t('tok_percentile_95',
  '`percentile(DurationMs, 95)` (KQL aggregation function inside `summarize` calculating 95th-percentile request tail latency)',
  'KQL uses singular `percentile(expr, 95)` to compute a single numeric percentile column.')
t('tok_pre_tool_use',
  '`preToolUse` (GitHub Copilot CLI hook event in `.github/hooks/*.json` evaluated synchronously before any shell/MCP tool executes)',
  '`preToolUse` hooks can inspect tool arguments and return `deny` before destructive commands run.')
t('tok_azcli_auth',
  '`-a azcli` (authentication flag on `npx -y @azure-devops/mcp <org> -a azcli` reusing the OIDC Azure CLI session from `copilot-setup-steps`)',
  '`-a azcli` instructs `@azure-devops/mcp` to obtain tokens from the pre-authenticated `az login` session without interactive browser prompts.')
t('tok_filter_repo',
  '`git filter-repo` (command-line tool rewriting Git history across all refs to purge leaked credentials or large files)',
  '`git filter-repo` cleanly strips sensitive blobs from historical commits and tags.')
t('tok_extends_key',
  '`extends` (top-level Azure Pipelines YAML keyword inheriting mandatory security stages/jobs enforced by Required Template checks)',
  '`extends:` locks downstream pipelines into a governed platform template contract.')
t('tok_isoutput_true',
  '`isOutput=true` (`##vso[task.setvariable variable=x;isOutput=true]` flag exposing an Azure Pipelines variable across jobs and stages)',
  'Omitting `isOutput=true` restricts `setvariable` scope to the current job only.')
t('tok_cancel_in_progress',
  '`cancel-in-progress: true` (GitHub Actions `concurrency` property terminating older queued/running jobs on the same PR ref)',
  '`cancel-in-progress: true` stops stale PR runs automatically whenever a developer or agent pushes a newer commit.')
t('tok_release_view',
  '`@Release` (Azure Artifacts feed view suffix `feedName@Release` isolating verified production-ready immutable packages)',
  'Restoring from `feedName@Release` blocks unvetted `@Local` or `@Prerelease` packages from entering production builds.')

# Merge all 48 sequence options (`12` groups x `4` choices)
for _k, _v in SEQUENCES.items():
    if _k in TERMS:
        raise ValueError(f'Sequence key collision: {_k}')
    TERMS[_k] = _v
