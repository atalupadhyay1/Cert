"""Comprehensive technical option & distractor library for Exam AZ-400 (July 27, 2026 study guide).

Covers all 5 official functional groups and 34 local skills across Azure DevOps, GitHub Enterprise,
YAML pipelines, progressive deployments, Bicep/DSC/ADE IaC, DevSecOps (GHAS/GHAzDO/Defender/OIDC),
and Azure Monitor / Application Insights / KQL instrumentation.
"""

from sequences import SEQUENCES

TERMS = dict(SEQUENCES)


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term key: {key}')
    if len(label) > 255:
        raise ValueError(f'{key}: label exceeds 255 chars ({len(label)})')
    TERMS[key] = (label, meaning)


# ==============================================================================
# DOMAIN 1: DESIGN AND IMPLEMENT PROCESSES AND COMMUNICATIONS (10–15%)
# ==============================================================================
# 1.1 Traceability & flow of work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)
t('proc_basic',
  'Azure Boards `Basic` process (`Epic`, `Issue`, `Task`)',
  'The `Basic` process is the simplest Azure Boards model with three work item types (`Epic`, `Issue`, `Task`) for lightweight teams.')
t('proc_agile',
  'Azure Boards `Agile` process (`Epic`, `Feature`, `User Story`, `Task`, `Bug`)',
  '`Agile` tracks User Stories in story points alongside separate `Bug` items configurable on backlogs or taskboards.')
t('proc_scrum',
  'Azure Boards `Scrum` process (`Epic`, `Feature`, `Product Backlog Item`, `Task`, `Bug`, `Impediment`)',
  '`Scrum` uses Product Backlog Items (PBIs) estimated in Effort, dedicated `Impediment` tracking, and Commitment/Done workflow states.')
t('proc_cmmi',
  'Azure Boards `CMMI` process (`Epic`, `Feature`, `Requirement`, `Task`, `Bug`, `Change Request`, `Review`, `Risk`)',
  '`CMMI` adds formal `Requirement`, `Change Request`, `Risk`, and `Review` work item types required by regulated audit frameworks.')
t('gh_flow',
  'GitHub Flow: create short-lived branch from `main`, open PR early for CI/review, deploy/verify, and merge to `main`',
  'GitHub Flow keeps `main` always deployable using short-lived topic branches, pull-request collaboration, automated checks, and rapid merges.')
t('gh_projects_v2',
  'GitHub Projects (table/board/roadmap views with custom iteration/priority fields and built-in workflow automations)',
  'GitHub Projects links Issues and PRs across repositories with custom fields, iteration planning, and automated status transitions.')
t('gh_issue_forms',
  'YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforcing required structured inputs and auto-labels',
  'YAML Issue Forms validate required dropdown/input fields before submission so bug and feedback reports arrive with reproducible metadata.')
t('boards_trace_e2e',
  'Link commits/PRs to Azure Boards work items, enable Build/Release work-item integration, and associate automated tests with Requirements',
  'End-to-end traceability in Azure DevOps connects Requirements -> branches/PRs -> CI builds -> TRX test results -> deployed release stages.')
t('boards_github_ab',
  'Azure Boards app for GitHub using `AB#<ID>` / `Fixes AB#<ID>` syntax in commits or pull request descriptions',
  '`AB#<ID>` creates a Development link on the Azure Boards work item, and `Fixes AB#<ID>` transitions it to Resolved/Done upon merge to default branch.')
t('boards_gh_pat_bad',
  'Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App',
  'Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App.')
t('boards_bug_as_task',
  'Configure team `Working with bugs` setting to `Bugs are managed with tasks` so bugs appear on sprint taskboards under stories',
  'Azure Boards lets each team choose whether Bugs behave as backlog requirements, sprint sub-tasks, or outside backlogs altogether.')
t('boards_bug_as_req',
  'Configure team `Working with bugs` setting to `Bugs are managed with requirements` so bugs are prioritized and estimated on the product backlog',
  'Managing bugs with requirements places defects directly on the product backlog and velocity chart alongside stories/PBIs.')

# 1.2 Metrics, dashboards, and WIQL / Analytics queries
t('met_cycle_time',
  'Cycle Time widget (elapsed time from when work actively begins in `Active`/`In Progress` until `Closed`/`Done`)',
  'Cycle Time measures engineering execution speed once work starts on an item, excluding time spent sitting unstarted in `New`.')
t('met_lead_time',
  'Lead Time widget (total elapsed time from work item creation in `New` until `Closed`/`Done`)',
  'Lead Time measures customer-perceived wait time from initial request creation (`New`) through completion (`Closed`/`Done`).')
t('met_cfd',
  'Cumulative Flow Diagram (CFD) tracking work item counts per workflow column over time to expose WIP bottlenecks',
  'Widening bands in a Cumulative Flow Diagram immediately reveal stages where work-in-progress (WIP) accumulates faster than completion.')
t('met_velocity',
  'Velocity widget measuring completed vs planned Story Points / Effort across sprints',
  'Velocity helps Scrum/Agile teams forecast sprint capacity from historical completed Effort/Story Points — not active-to-closed item duration.')
t('met_burndown',
  'Sprint Burndown widget plotting remaining work hours or story points against the ideal trend line within an iteration',
  'Sprint Burndown tracks intra-sprint progress toward the sprint goal rather than end-to-end lead or cycle time distributions.')
t('met_dora_mttr',
  'Mean Time to Recovery / Restore (MTTR): average elapsed time from production incident/failure detection until service restoration',
  'MTTR is a core DORA stability metric quantifying how rapidly teams recover from production incidents via rollback or hotfix.')
t('met_dora_cfr',
  'Change Failure Rate: percentage of production deployments causing degraded service, hotfix, or rollback',
  'Change Failure Rate tracks release quality alongside deployment frequency, lead time for changes, and MTTR.')
t('wiql_query_tile',
  'Shared WIQL Work Item Query (`State`, `Tags`, `Severity`) pinned to an Azure Dashboards Query Tile with conditional color rules',
  'Shared queries (saved under `Shared Queries`, not `My Queries`) drive dashboard tiles and charts visible to the whole project team.')
t('analytics_odata',
  'Azure DevOps Analytics Views / OData (`Analytics` service) feeding Power BI for cross-project historical trend reporting',
  'Analytics Views and OData endpoints are optimized for aggregated historical reporting without throttling operational REST APIs.')
t('wiql_my_queries_bad',
  'Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki',
  'Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions.')

# 1.3 Collaboration, Wikis, Mermaid, Release Notes, Webhooks & Microsoft Teams
t('wiki_code_publish',
  'Publish Code as Wiki from a Git repository branch so Markdown docs and Mermaid (`::: mermaid` / ```` ```mermaid ````) diagrams follow PR reviews',
  'Publishing Markdown from Git as Wiki keeps architecture docs versioned alongside code branches, pull requests, and branch policies.')
t('wiki_mermaid',
  'Embed Mermaid diagram syntax directly inside Azure DevOps Wiki or GitHub Markdown files for text-diffable sequence/flow diagrams',
  'Both Azure DevOps Wiki (`::: mermaid`) and GitHub Markdown (```` ```mermaid ````) render Mermaid diagrams natively from plain versioned text.')
t('rel_notes_gh_auto',
  'Configure `.github/release.yml` category/label mappings and run `gh release create --generate-notes` (or GitHub auto-generated release notes)',
  'GitHub automatically groups merged pull requests and contributors into categorized Markdown release notes using `.github/release.yml`.')
t('rel_notes_openapi',
  'Generate OpenAPI/Swagger JSON during CI builds and publish versioned static API reference docs alongside pipeline release notes',
  'Automating OpenAPI extraction in CI prevents documentation drift between shipped endpoints and published developer portals.')
t('teams_azpipelines_app',
  'Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe <pipeline-url>`) with stage failure and approval cards',
  'The official Azure Pipelines Teams app posts real-time stage status notifications and lets approvers approve/reject directly in Teams.')
t('teams_azboards_app',
  'Azure Boards app for Microsoft Teams creating work items from channel messages and subscribing to work item event notifications',
  'The Azure Boards Teams app links channels to area paths/events and turns Teams discussions into tracked work items.')
t('teams_gh_app',
  'GitHub app for Microsoft Teams (`@GitHub subscribe owner/repo`) delivering PR, deployment, check-failure, and issue notifications',
  'The GitHub app for Teams streams repository PR reviews, CI workflow failures, and deployment approvals into Microsoft Teams channels.')
t('service_hook_webhook',
  'Azure DevOps Service Hooks (Webhooks / Azure Service Bus) or GitHub repository Webhooks secured with an HMAC `X-Hub-Signature-256` secret',
  'Webhooks push event-driven JSON payloads on push, PR, build, or work-item changes without polling, verified via HMAC shared secret.')

# ==============================================================================
# DOMAIN 2: DESIGN AND IMPLEMENT A SOURCE CONTROL STRATEGY (10–15%)
# ==============================================================================
# 2.1 Branching strategies
t('branch_trunk',
  'Trunk-based development with short-lived branches (<24h) merging frequently to `main` behind feature flags',
  'Trunk-based development minimizes merge hell, accelerates CI feedback, and relies on feature flags to hide incomplete features in production.')
t('branch_release',
  'Release branching (`release/1.4`) cut from `main` for stabilization while `main` continues accepting next-release features; cherry-pick/merge fixes back',
  'Release branches isolate versioned stabilization and hotfixes (`v1.4.x`) when multiple major/minor versions must be supported concurrently.')
t('branch_gitflow_heavy',
  'Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags',
  'Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows.')
t('hotfix_tag_branch',
  'Create a `hotfix/*` branch directly from the production release Git tag (e.g., `v2.3.0`), ship the tested patch `v2.3.1`, and cherry-pick/PR the fix to `main`',
  'Branching from the exact deployed tag guarantees unfinished commits on `main` never leak into an emergency production hotfix.')

# 2.2 PR workflows, Branch Policies, GitHub Rulesets & CODEOWNERS
t('azrepos_policy_suite',
  'Azure Repos branch policies on `main`: minimum reviewers (disallow self-approval, reset votes on new push), Build Validation, Linked Work Items, and Comment Resolution',
  'Azure Repos protects branches by blocking direct pushes and enforcing PR build validation, work item linkage, reviewer resets, and resolved comments.')
t('azrepos_merge_squash',
  'Enforce `Squash merge` in branch policy so each feature PR condenses noisy WIP commits into a single clean commit on `main`',
  'Squash merge produces a linear one-commit-per-PR history on `main` while deleting or retiring the source topic branch.')
t('azrepos_merge_noff',
  'Enforce `Basic merge (no fast-forward)` to preserve every individual topic-branch commit plus an explicit two-parent merge commit',
  'No-fast-forward keeps granular feature commit history intact and records exact PR merge boundaries.')
t('azrepos_merge_semilinear',
  'Enforce `Semi-linear merge` so PR commits are rebased onto latest `main` first and then joined via an explicit merge commit',
  'Semi-linear merge combines rebased up-to-date commit linearity with explicit PR merge commit grouping.')
t('azrepos_path_reviewer',
  'Configure `Automatically included reviewers` on Azure Repos branch policy with path filter `/infra/**; /payments/**` Marked as `Required`',
  'Path-scoped required reviewers in Azure Repos ensure security or platform owners must sign off whenever protected directories change.')
t('gh_codeowners',
  'Define `.github/CODEOWNERS` mapping sensitive paths (e.g., `/checkout/** @org/sec-team`) and enable `Require review from Code Owners` in branch protection / rulesets',
  '`CODEOWNERS` alone only requests reviews; combining it with `Require review from Code Owners` in branch protection/rulesets enforces mandatory sign-off.')
t('gh_rulesets',
  'GitHub Repository / Organization Rulesets enforcing required status checks, linear history, signed commits, and bypass lists across multiple repos',
  'GitHub Rulesets layer organization-wide and repository-level governance with dry-run (`Evaluate`) mode and explicit bypass actors.')
t('gh_merge_queue',
  'GitHub Merge Queue (`merge_group` trigger) validating stacked PR batches sequentially against latest `main` before merging',
  'Merge queues prevent semantic conflicts where two PRs pass CI individually against stale `main` but break `main` when combined.')

# 2.3 Git LFS, Scalar, Sparse-Checkout, Partial Clone, Submodules
t('git_lfs',
  'Configure `Git LFS` (`git lfs install` and `git lfs track "*.psd" "*.bin"`, committing `.gitattributes`) to store large binaries as lightweight pointers',
  'Git LFS stores binary blobs on remote LFS object storage and downloads only blobs needed for the checked-out commit, keeping Git packfiles small.')
t('git_scalar',
  'Use `scalar clone <repo-url>` (enabling background maintenance, commit-graph, filesystem monitor, partial clone, and cone sparse-checkout)',
  'Microsoft `Scalar` optimizes massive Git monorepos via GVFS/partial-clone object virtualization, `fsmonitor`, multi-pack-index, and sparse-checkout.')
t('git_sparse_partial',
  '`git clone --filter=blob:none --sparse <url>` followed by `git sparse-checkout set <service-folder>`',
  'Blobless partial clone (`--filter=blob:none`) fetches trees/commits first and downloads file blobs lazily only for sparse-checked-out directories.')
t('git_shallow_ci',
  'Set shallow fetch (`fetchDepth: 1` in Azure Pipelines `checkout: self` or `fetch-depth: 1` in `actions/checkout@v4`) for CI builds',
  'Fetching only the single target commit (`fetchDepth: 1`) drastically cuts network transfer and checkout time on large repositories.')
t('git_full_depth_sonar',
  'Set `fetchDepth: 0` (full history) when pipeline tasks like GitVersion, SonarQube blame, or `git diff` require full commit/tag ancestry',
  'Tools calculating SemVer from historical tags (GitVersion) or SCM blame fail or miscalculate on `fetchDepth: 1` shallow clones.')
t('git_submodule_vs_pkg',
  'Publish versioned libraries to Azure Artifacts / GitHub Packages instead of nesting mutable Git submodules when consumers only need compiled SDKs',
  'Package feeds decouple consumer build lifecycles with clean SemVer dependency resolution, whereas Git submodules couple source trees tightly.')
t('git_submodule_pin',
  'Git Submodules (`git submodule add` / `.gitmodules`) pinning an external repository to an exact commit SHA inside a parent repository',
  'Git submodules mount an external repo at a fixed commit pointer, requiring `submodules: true`/`recursive` during pipeline checkout.')

# 2.4 Permissions, Tags, Recovery & History Purging
t('git_annotated_tag',
  'Annotated signed Git tag (`git tag -a v2.4.0 -s -m "Release 2.4.0"`) storing tagger identity, timestamp, message, and GPG/SSH signature',
  'Annotated tags are full immutable Git objects ideal for auditable production releases, unlike lightweight tags which are bare commit pointers.')
t('git_revert_shared',
  'Run `git revert <commit-sha>` to create a new inverse commit safely undoing changes on a shared protected branch without rewriting history',
  '`git revert` preserves immutable branch history on shared branches (`main`), whereas `git reset --hard` + force-push breaks collaborator trees.')
t('git_reflog_recover',
  'Inspect `git reflog` on the local clone (or Azure Repos PR/Push ref history) to locate the orphaned commit SHA and restore the deleted branch/commits',
  '`git reflog` records local HEAD/branch tip movements even after accidental `git reset --hard` or branch deletion prior to garbage collection.')
t('git_filter_repo',
  'Rewrite repository history with `git filter-repo --path <secret-file> --invert-paths` (plus rotating the compromised secret and force-pushing)',
  'Git project documentation recommends `git filter-repo` (or BFG Repo-Cleaner) over deprecated `git filter-branch` to purge blobs across all commits.')
t('azrepos_force_push_deny',
  'Keep `Force push (rewrite history, delete branches and tags)` set to `Deny` / `Not set` for standard contributors on protected branches',
  'Disallowing `Force push` in Azure Repos repository permissions prevents accidental history destruction on shared branches.')

# ==============================================================================
# DOMAIN 3: DESIGN AND IMPLEMENT BUILD AND RELEASE PIPELINES (50–55%)
# ==============================================================================
# 3.1 – 3.3 Package Management (Azure Artifacts, GitHub Packages, Upstream, Views, SemVer)
t('pkg_azure_artifacts',
  'Azure Artifacts single multi-protocol feed supporting NuGet, npm, Maven, Python (PyPI), Cargo, and Universal Packages',
  'A single Azure Artifacts feed natively hosts NuGet, npm, Maven, PyPI, Cargo, and Azure-specific Universal Packages with RBAC and views.')
t('pkg_universal',
  'Azure Artifacts Universal Packages (`UniversalPackages@0`) storing large non-language binaries/bundles up to terabytes with deduplication',
  'Universal Packages efficiently deduplicate and version multi-gigabyte cross-platform toolchains, game assets, or firmware drops.')
t('pkg_gh_packages',
  'GitHub Packages (`ghcr.io` Container Registry, npm, NuGet, Maven, RubyGems) scoped to repository/organization permissions and `GITHUB_TOKEN`',
  'GitHub Packages integrates natively with GitHub Actions using `packages: write` on `GITHUB_TOKEN` without managing external registry credentials.')
t('pkg_upstream_sources',
  'Enable Upstream Sources (`nuget.org`, `npmjs.com`, `PyPI`, `Maven Central`) on the internal Azure Artifacts feed so resolved public packages are cached immutably',
  'Upstream sources let developers configure a single feed URL while caching public package versions inside the enterprise feed against public registry outages.')
t('pkg_feed_views',
  'Promote tested package versions from `@Local` to `@Prerelease` and `@Release` feed views (`feed@Release`) without recompiling binaries',
  'Azure Artifacts views (`@Local`, `@Prerelease`, `@Release`) filter package visibility by quality readiness while preserving binary immutability.')
t('pkg_semver',
  'Semantic Versioning (`Major.Minor.Patch-prerelease`, e.g., `2.1.0` -> `3.0.0` for breaking API changes, `2.2.0` for backward-compatible features, `2.1.1` for patches)',
  'SemVer communicates compatibility guarantees: increment `MAJOR` on breaking changes, `MINOR` on additive features, `PATCH` on bug fixes, `-rc.1` for prereleases.')
t('pkg_calver',
  'Calendar Versioning (`YYYY.0M.Patch`, e.g., `2026.10.2`) for date-driven platform drops, OS images, or time-boxed compliance bundles',
  'CalVer encodes release chronology directly into version identifiers when release cadence matters more than library API compatibility.')
t('pkg_immutability',
  'Once a `name@version` (e.g., `Core.Auth@1.4.0`) is published to Azure Artifacts, that exact version number is permanently immutable even if deleted',
  'Immutability prevents supply-chain cache poisoning; fixes must always publish a new incremented version (`1.4.1`).')

# 3.4 – 3.6 Testing Strategy (Quality/Release Gates, Load Testing, Test Results & Coverage)
t('gate_az_monitor',
  'Azure Pipelines Environment `Query Azure Monitor alerts` check verifying zero active Sev0/Sev1 alerts during a post-deploy stabilization window',
  'Automated Azure Monitor checks halt ring promotion when newly deployed builds trigger production error or latency alerts.')
t('gate_rest_fn',
  'Azure Pipelines Environment `Invoke Azure Function` or `Invoke REST API` check polling an external health/ServiceNow change endpoint',
  'Custom REST API / Azure Function checks integrate external ITSM change tickets (ServiceNow), synthetic probes, or compliance APIs into YAML gates.')
t('gate_wiql',
  'Azure Pipelines `Query Work Items` check blocking production promotion whenever active `Severity 1` bugs exist for the release area',
  'Work Item Query checks enforce zero critical open defects automatically before promoting stages.')
t('test_shift_left',
  'Run fast isolated unit tests + static linters on every PR commit, service/container integration tests post-merge, and Azure Load Testing on staging',
  'Test-pyramid staging keeps PR feedback under minutes while catching contract and scale bottlenecks before production.')
t('test_az_load',
  'Azure Load Testing (`AzureLoadTest@1` / `azure/load-testing@v1`) with YAML `failureCriteria` (`p90(response_time_ms) > 400`, `percentage(error) > 1`)',
  'Managed Azure Load Testing executes JMeter/Locust scripts at cloud scale and fails the pipeline automatically when declarative `failureCriteria` breach.')
t('test_publish_results',
  '`PublishTestResults@2` (`condition: succeededOrFailed()`) publishing JUnit/VSTest `.trx` files so test failures still populate the Azure Pipelines Tests tab',
  'Using `succeededOrFailed()` (not default `succeeded()`) guarantees test failure reports upload even when the test runner exits non-zero.')
t('test_code_coverage',
  '`PublishCodeCoverageResults@2` (Cobertura/JaCoCo/xml) paired with Azure Repos `buildpolicy.yml` or PR status policy enforcing >= 80% diff coverage',
  'Publishing Cobertura/JaCoCo reports plus PR diff coverage checks stops untested code paths from merging silently.')
t('test_parallel_slicing',
  '`VSTest@2` / job `strategy: parallel: 4` slicing test assemblies dynamically across parallel agents based on historical execution duration',
  'Distributing large test suites across parallel agent jobs cuts wall-clock test time nearly linearly.')

# 3.7 – 3.12 Design and Implement Pipelines (Runners/Agents, Triggers, Multi-stage YAML, Templates, Environments)
t('pipe_gha_vs_azdo',
  'Use GitHub Actions for GitHub-native workflows/marketplace ecosystems, or Azure Pipelines when Azure Boards/Test Plans/Classic/Environment-gate governance is central',
  'Both support multi-stage YAML and OIDC; Azure Pipelines adds deep Azure Boards/Test Plans/Environments integration while GitHub Actions unifies repo-native automation.')
t('agent_managed_devops_pool',
  'Managed DevOps Pools: Microsoft-managed scale-set agents injected into your private Azure VNet using Azure Pipelines / custom images and stateless mode',
  'Managed DevOps Pools combine zero VM patching/maintenance overhead of Microsoft-hosted agents with private VNet connectivity and custom SKUs.')
t('agent_vmss',
  'Azure Virtual Machine Scale Set (VMSS) agent pool configured to tear down / reimage instances after every job and autoscale down to zero idle VMs',
  'VMSS pools autoscale self-hosted capacity inside private VNets and optionally reimage each VM per job for clean-room builds.')
t('agent_self_hosted_stateful_risk',
  'Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs',
  'Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage.')
t('runner_gha_ephemeral',
  'Self-hosted GitHub Actions runners registered with `--ephemeral` via Actions Runner Controller (ARC) on AKS so each pod executes at most one job',
  'Ephemeral ARC Kubernetes runners prevent malicious or leaky jobs from contaminating subsequent workflows and prohibit public-repo self-hosted runner exposure.')
t('trig_azdo_paths',
  'Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`',
  'Path filters in multi-service repos ensure Markdown edits (`docs/**`) do not waste build minutes while code changes trigger targeted CI.')
t('trig_gha_events',
  '`on: push`, `pull_request` (with `paths-ignore: ["docs/**"]`), `schedule` (`cron`), `workflow_dispatch` (manual typed inputs), and `repository_dispatch`',
  '`workflow_dispatch` adds manual parameterized UI/API runs, `repository_dispatch` accepts external webhook triggers, and `paths-ignore` skips doc-only pushes.')
t('trig_pipeline_resource',
  'Azure Pipelines `resources.pipelines` trigger (`source: CoreLib-CI`, `trigger: branches: include: [main]`) chaining downstream deployments to upstream CI completion',
  'Pipeline resource triggers decouple upstream build YAML from downstream deployment pipelines cleanly.')
t('yaml_depends_fan_in',
  'Set `dependsOn: [Deploy_EastUS, Deploy_WestEurope, Deploy_SoutheastAsia]` and `condition: succeeded()` on the final `Global_SmokeTest` stage',
  'Listing multiple upstream stages in `dependsOn` creates a fan-in barrier that runs only when all parallel regional stages succeed.')
t('yaml_matrix',
  '`strategy: matrix:` across OS/runtime combinations (`ubuntu-latest`/`windows-latest` x `net8.0`/`net9.0`) with `maxParallel` concurrency control',
  'Matrix strategies expand one job definition into concurrent platform/version permutations without duplicating YAML steps.')
t('yaml_extends_template',
  'Azure Pipelines `extends: template: security-base.yml@templates` injecting mandatory secret/SAST steps before caller `stages`/`jobs`',
  '`extends` wraps the entire pipeline inside a governed template, unlike `template:` step includes which individual repo authors could delete.')
t('yaml_gha_reusable',
  'GitHub Actions reusable workflow (`on: workflow_call`) vs Composite Action (`runs: using: "composite"` bundling multi-step shell/action sequences)',
  'Reusable workflows (`workflow_call`) encapsulate full jobs/environments/secrets, whereas composite actions bundle reusable steps inside a single job.')
t('yaml_var_syntax',
  'Compile-time `$\x7b\x7b variables.Env \x7d\x7d` (expanded before pipeline validation) vs runtime `$[variables.Env]` vs macro `$(Env)` (expanded right before task runs)',
  'Template structure (`stages`/`jobs` conditionals) requires compile-time `$\x7b\x7b \x7d\x7d`, stage/job `condition:` uses runtime `$[ ]`, and script steps use `$( )`.')
t('env_checks_suite',
  'Azure Pipelines YAML `environment:` configured with Approvals (disallow requester self-approval), Business Hours check, Branch Control (`refs/heads/main`), and Exclusive Lock (`lockBehavior: sequential` or `runLatest`)',
  'Environment checks live in Azure DevOps UI/security outside repo edit permissions so developers cannot remove production approvals via a PR.')

# 3.13 – 3.16 Deployments (Blue-Green, Canary, Rings, Slots, App Config Feature Flags, DB DACPAC/Migrations)
t('dep_blue_green',
  'Blue-Green deployment maintaining two identical production-grade environments (`Blue` live, `Green` idle/staged) and switching router/Front Door/slot VIP atomically',
  'Blue-Green eliminates in-place upgrade downtime and enables instantaneous rollback by routing traffic back to `Blue`.')
t('dep_canary',
  'Canary deployment routing a small traffic slice (e.g., 5–10% via Azure Front Door, Container Apps traffic weights, or service mesh) to the new revision while monitoring telemetry',
  'Canary limits real-user blast radius to a small percentage before shifting 100% of production traffic.')
t('dep_rings',
  'Progressive Exposure Rings (`Ring 0` internal canaries -> `Ring 1` early adopters -> `Ring 2` global customers) baking telemetry between promotions',
  'Deployment rings group user populations by risk tolerance to catch edge-case regressions progressively.')
t('dep_ab_testing',
  'A/B testing routing user cohorts to Variant A vs Variant B coupled with Application Insights custom business conversion telemetry',
  'Unlike canary (technical health validation), A/B testing measures product/business conversion outcomes across cohorts.')
t('dep_slot_auto_swap',
  'App Service `staging` deployment slot with `applicationInitialization` warm-up paths, slot-pinned connection strings, and Auto-Swap / Swap with Preview',
  'Warm-up hits internal HTTP paths before VIP swap so cold-start JIT latencies never affect live traffic.')
t('dep_db_expand_contract',
  'Backward-compatible Expand-and-Contract (Parallel Change) schema pattern: add nullable column/new table first, deploy dual-compatible app code, backfill, then remove the legacy column in a later release',
  'Zero-downtime blue-green/canary rollouts break if a DB deployment renames or removes columns still queried by active N-1 app instances.')
t('dep_db_dacpac',
  'State-based SQL deployment via `SqlAzureDacpacDeployment@1` comparing a compiled `.dacpac` model against target Azure SQL to generate a differential upgrade script',
  'State-based DACPAC deployments declare the desired end-state schema, automatically computing `ALTER` diffs against target databases.')
t('dep_db_migrations',
  'Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts',
  'Ordered migration scripts give explicit control over complex data transformations, column renames, and idempotent transactional upgrades.')
t('ff_targeting_filter',
  'Azure App Configuration Feature Manager with `Microsoft.Targeting` filter (`Users`, `Groups` staged rollout %, `DefaultRolloutPercentage`)',
  'The `Microsoft.Targeting` filter deterministically hashes user/tenant IDs so the same beta hospital or user consistently receives the enabled feature.')
t('ff_timewindow_filter',
  'Azure App Configuration Feature Manager with `Microsoft.TimeWindow` filter activating a promotional feature automatically between UTC `Start` and `End` timestamps',
  '`Microsoft.TimeWindow` enables scheduled flash-sale or cutover windows without manual toggles or redeployments.')

# 3.17 – 3.18 Infrastructure as Code (Bicep, ARM Deployment Stacks, DSC, Machine Configuration, ADE)
t('iac_bicep_whatif',
  '`az deployment group what-if` previewing `Create`, `Modify`, `Delete`, `NoChange`, and `Ignore` resource mutations against live Azure state before applying',
  'Running `what-if` in pre-deployment CI/CD surfaces unintended destructive changes or manual portal drift before `create` executes.')
t('iac_deploy_stacks',
  'Azure Resource Manager Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`)',
  'Deployment Stacks manage multi-resource lifecycles atomically with safe cleanup of detached resources and guardrails (`denySettings`) blocking manual portal drift.')
t('iac_bicep_registry',
  'Azure Container Registry Private Bicep Module Registry (`br:myacr.azurecr.io/bicep/modules/aks:v1.2.0`) sharing versioned, linted IaC building blocks',
  'Private Bicep registries distribute organization-approved, versioned infrastructure modules across application repositories.')
t('iac_automation_dsc',
  'Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)',
  'Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state.')
t('iac_machine_config',
  'Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension',
  'Azure Machine Configuration integrates desired-state OS auditing/remediation natively into Azure Policy across cloud and hybrid Arc servers.')
t('iac_ade',
  'Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage)',
  'Azure Deployment Environments lets developers self-provision governed sandbox/PR environments via Managed Identity RBAC without direct subscription Owner permissions.')

# 3.19 – 3.20 Maintain Pipelines (Flaky Tests, Caching, Concurrency, Retention, Classic-to-YAML)
t('maint_flaky_tests',
  'Enable Azure Pipelines Flaky Test Management (detection via test reruns + optional exclusion from build failure rate until quarantined bug is fixed)',
  'Flaky test detection flags non-deterministic tests automatically and tracks resolution via linked bugs without blinding teams to deterministic regressions.')
t('maint_cache_task',
  '`Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback',
  'Hashing the dependency lockfile invalidates caches precisely when dependencies change while serving warm hits on unchanged builds.')
t('maint_gha_concurrency',
  'Configure GitHub Actions `concurrency: group: $\x7b\x7b github.workflow \x7d\x7d-$\x7b\x7b github.ref \x7d\x7d` with `cancel-in-progress: true` on non-prod PR workflows',
  '`concurrency` with `cancel-in-progress: true` immediately aborts superseded PR builds when new commits arrive on the same branch, freeing runners.')
t('maint_retention_lease',
  'Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs',
  'Tiered retention controls artifact storage costs on noisy PR runs while preserving regulated production build provenance and symbols.')
t('maint_classic_export',
  'Use Azure Pipelines `Export to YAML` / `View YAML` on Classic builds, convert Task Groups into parameterized YAML step/job templates, and replace Release stages with YAML Environments',
  'Migrating Classic pipelines brings CI/CD under Git pull-request review, branch history, and template enforcement.')

# ==============================================================================
# DOMAIN 4: DEVELOP A SECURITY AND COMPLIANCE PLAN (10–15%)
# ==============================================================================
# 4.1 Authentication & Authorization (Entra SP vs MI, GitHub Apps vs GITHUB_TOKEN vs PAT, Service Connections)
t('sec_managed_identity',
  'Azure Managed Identity (system-assigned tied to resource lifecycle, or user-assigned shared across resources/federated credentials) with zero developer-managed passwords',
  'Managed Identities eliminate secret rotation entirely on Azure compute and can serve as backing identities for Azure DevOps / GitHub OIDC Workload Identity Federation.')
t('sec_sp_secret_legacy',
  'Entra Application Service Principal authenticated via a manually rotated client secret or PFX certificate when non-OIDC legacy tooling cannot federate',
  'Service principals with client secrets require strict vault storage and rotation policies whenever OIDC workload identity federation is unavailable.')
t('sec_github_app',
  'GitHub App installed at organization/repository scope issuing short-lived (1-hour) installation tokens with granular permissions independent of individual user accounts',
  'Unlike personal access tokens tied to a human employee seat, GitHub Apps survive employee offboarding and mint short-lived scoped tokens.')
t('sec_github_token',
  'Automatic per-job `GITHUB_TOKEN` restricted to `permissions: contents: read` by default and elevated per job only as required (e.g., `packages: write`, `id-token: write`)',
  '`GITHUB_TOKEN` expires automatically when the job finishes; restricting default org/repo workflow permissions to read-only implements least privilege.')
t('sec_pat_fine_grained',
  'Fine-grained Personal Access Token scoped to specific repositories, explicit read/write resource permissions, and mandatory short expiration (`<= 30–90 days`)',
  'When a user-bound token is unavoidable, fine-grained PATs limit blast radius compared to classic `repo`-wide PATs.')
t('sec_fork_pr_safe',
  'Use `on: pull_request` (running against merge commit with read-only `GITHUB_TOKEN` and no secrets) rather than `pull_request_target` executing untrusted fork code',
  'Checking out and building untrusted fork code inside `pull_request_target` exposes write tokens and secrets to arbitrary PR script injection.')
t('sec_azdo_wif_sc',
  'Azure Resource Manager service connection using Workload Identity Federation (automatic/manual OIDC) scoped to a single Resource Group and locked via pipeline permissions',
  'Azure DevOps Workload Identity Federation service connections exchange short-lived OIDC tokens for Entra access tokens with zero stored client secrets.')

# 4.2 Access Levels, Roles & Security Groups (Azure DevOps & GitHub)
t('acc_stakeholder',
  'Azure DevOps `Stakeholder` access level (free, unlimited seats: create/edit/view Azure Boards work items, dashboards, and wikis; NO Azure Repos code access)',
  'Assigning `Stakeholder` to external business/hospital advisors grants Boards bug/backlog participation at zero license cost while blocking source repository access.')
t('acc_basic',
  'Azure DevOps `Basic` access level (first 5 free, paid thereafter; included with Visual Studio Subscriptions: Azure Boards + Azure Repos + Azure Pipelines)',
  '`Basic` grants full source control (`Azure Repos`), pipeline authoring, and boards capabilities without exploratory/manual Test Plan authoring.')
t('acc_basic_testplans',
  'Azure DevOps `Basic + Test Plans` access level (or Visual Studio Enterprise/Test Pro): required to create/manage manual test plans, test suites, and exploratory sessions',
  'While `Basic` users can execute certain tests, authoring and managing Test Plans and Test Suites requires `Basic + Test Plans`.')
t('acc_outside_collab',
  'GitHub `Outside collaborator` (or Azure DevOps custom Project-scoped security group restricted via `Project-Scoped Users` preview/repo ACLs) with access to a single repository only',
  'Outside collaborators receive repository-specific `Read`/`Triage`/`Write` roles without gaining Organization Member visibility into internal private repos.')
t('acc_azdo_deny_wins',
  'In Azure DevOps permissions, explicit `Deny` always overrides `Allow` across inherited security groups (unless the user belongs to `Project Collection Administrators`)',
  'Use `Not set` rather than blanket `Deny` on broad base groups like `Contributors` so targeted `Allow` grants on specialist subgroups still function.')

# 4.3 Secrets, Key Vault, Secure Files, OIDC & Log Masking
t('kv_var_group',
  'Link an Azure Pipelines Variable Group to Azure Key Vault (or use `AzureKeyVault@2` task) granting the WIF service connection `Key Vault Secrets User` RBAC',
  'Key Vault-linked variable groups fetch only selected secrets just-in-time at job execution and automatically register values for log masking.')
t('sec_secure_files',
  'Upload binary `.p12` / `.pfx` / `.cer` / `ssh_key` / `.tfvars` files to Azure Pipelines Library `Secure Files`, authorize per pipeline, and consume via `DownloadSecureFile@1`',
  '`Secure Files` encrypts binary files up to 10 MB at rest and deletes decrypted temp copies (`$(Agent.TempDirectory)`) automatically after the job ends.')
t('sec_log_masking',
  'Emit runtime dynamic values with `echo "##vso[task.setvariable variable=ApiToken;issecret=true]$TOKEN"` in Azure Pipelines or `echo "::add-mask::$TOKEN"` in GitHub Actions',
  'Marking dynamic variables secret (`issecret=true` / `::add-mask::`) scrubs accidental stdout appearances with `***` and blocks automatic env-var injection unless mapped explicitly.')
t('sec_oidc_env_sub',
  'Configure the Entra federated credential `subject` to `repo:org/app:environment:production` and bind the deployment job to `environment: production`',
  'Scoping the federated `subject` claim to `environment:production` ensures feature-branch PR workflows can never mint production Azure tokens.')

# 4.4 DevSecOps Scanning (GHAS, GHAzDO, CodeQL, Push Protection, Dependabot, Defender for Cloud, Containers, OSS Licenses)
t('scan_push_prot',
  'GitHub Advanced Security (or GHAzDO) Secret Scanning with Push Protection blocking `git push` synchronously when high-confidence credentials/tokens are detected',
  'Push protection stops secrets at the `git push` boundary before they ever enter remote repository history or require `git filter-repo` cleanup.')
t('scan_codeql',
  'CodeQL semantic SAST analysis building compiled languages (C#/.NET, Java, C++) or running buildless/containerized extraction and publishing SARIF findings to the Security tab',
  'CodeQL treats code as queryable data to detect SQL injection, SSRF, path traversal, and deserialization flaws across call graphs.')
t('scan_dependabot',
  'Dependabot Alerts + `.github/dependabot.yml` (`package-ecosystem: "maven"` / `"nuget"` / `"github-actions"`, `schedule: interval: "weekly"`) opening automated bump PRs',
  'Dependabot continuously compares lockfiles against the GitHub Advisory Database and opens grouped/scheduled pull requests to upgrade vulnerable transitive packages and Actions.')
t('scan_defender_devops',
  'Microsoft Defender for Cloud DevOps Security connecting GitHub Enterprise and Azure DevOps via connectors to correlate code/IaC/container vulnerabilities with live cloud runtime exposure (CSPM)',
  'Defender for Cloud DevOps Security bridges CI/CD posture (GHAS/GHAzDO SARIF, IaC misconfigurations) with cloud attack-path analysis and PR security annotations.')
t('scan_container_ci',
  'Scan container images in CI with Trivy / Microsoft Defender for Cloud CLI (`defender scan`) BEFORE `docker push` to ACR, plus continuous registry re-scanning via Defender for Containers',
  'Pre-push CI scanning blocks known High/Critical CVEs at build time, while continuous ACR scanning catches newly disclosed CVEs in already-deployed images.')
t('scan_oss_license',
  'GitHub Dependency Review Action (`actions/dependency-review-action` with `deny-licenses: [GPL-3.0, AGPL-3.0]`) failing PRs that introduce copyleft license obligations',
  'Automated SCA license checks prevent incompatible copyleft dependencies from merging into proprietary commercial software.')
t('scan_dast_zap',
  'Dynamic Application Security Testing (DAST, e.g., OWASP ZAP baseline/full scan) executed against a deployed staging App Service / ephemeral environment before production swap',
  'Unlike SAST (CodeQL reading source), DAST probes live running HTTP endpoints to uncover missing security headers, auth misconfigurations, and runtime XSS/CORS flaws.')

# ==============================================================================
# DOMAIN 5: IMPLEMENT AN INSTRUMENTATION STRATEGY (5–10%)
# ==============================================================================
# 5.1 Configure Monitoring (Azure Monitor, App Insights, VM/Container/Storage/Network Insights)
t('mon_appinsights_ws',
  'Workspace-based Application Insights backed by a central Azure Monitor Log Analytics workspace collecting requests, dependencies, exceptions, traces, and custom metrics',
  'Workspace-based Application Insights unifies app telemetry (`AppRequests`, `AppDependencies`, `AppExceptions`) with infra logs (`InsightsMetrics`, `ContainerLogV2`) in one KQL store.')
t('mon_release_annot',
  'Create Application Insights Release Annotations from CI/CD pipelines so deployment markers appear directly on Performance and Failure charts',
  'Release annotations visually correlate exact build numbers and deployment timestamps with sudden latency or error-rate shifts.')
t('mon_vm_insights_ama',
  'VM Insights using Azure Monitor Agent (AMA) + Data Collection Rules (DCRs) + Dependency Agent collecting guest OS performance and process network maps',
  'AMA with Data Collection Rules replaces the retired Log Analytics MMA agent, providing multi-homing, transformation KQL filtering, and VM Insights health.')
t('mon_container_insights',
  'Azure Monitor Container Insights (`ContainerLogV2`, `KubePodInventory`, `InsightsMetrics`) monitoring AKS/Arc pod restarts, `OOMKilled` events, and node CPU/memory throttling',
  'Container Insights captures Kubernetes control/data-plane metrics, pod lifecycle anomalies (`OOMKilled`, `CrashLoopBackOff`), and structured stdout logs.')
t('mon_storage_network',
  'Azure Monitor Storage Insights (`StorageBlobLogs` throttling/E2E vs Server latency) and Azure Monitor Network Insights (Connection Monitor, NSG/VNet Flow Logs, Traffic Analytics)',
  'Storage Insights separates client-network latency (`SuccessE2ELatency`) from backend storage latency (`SuccessServerLatency`), while Network Insights diagnoses hybrid/VNet packet drops.')

# 5.2 GitHub Insights & CI/CD Event Alerts
t('mon_gh_insights',
  'GitHub Repository/Organization Insights (Pulse, Traffic, Dependency Graph, Actions Usage Metrics & Performance) tracking workflow queue time, job runtime, and billable minutes',
  'GitHub Actions Usage & Performance metrics expose runner queue wait bottlenecks, top minute-consuming workflows, and failure rates across repositories.')
t('mon_cicd_alerts',
  'Configure Azure DevOps Service Hooks / Notifications or GitHub Webhook + Azure Monitor Action Group (Logic App / Function / PagerDuty / Teams) triggering on pipeline run or deployment failures',
  'Routing failed deployment events into Action Groups or incident webhooks shrinks detection latency when automated rollouts or nightly security scans fail.')

# 5.3 Analyze Metrics, Distributed Tracing & KQL
t('kql_p95_latency',
  '`AppRequests | where TimeGenerated > ago(1h) | summarize p95=percentile(DurationMs, 95), err=countif(Success == false) by AppVersion, bin(TimeGenerated, 5m)`',
  'KQL `summarize percentile(DurationMs, 95)` grouped by `AppVersion` and 5-minute time bins pinpoints whether a newly deployed release caused tail-latency or failure spikes.')
t('kql_vm_cpu',
  '`InsightsMetrics | where Origin == "vm.azm.ms" and Namespace == "Processor" and Name == "UtilizationPercentage" | summarize avg(Val) by Computer, bin(TimeGenerated, 5m)`',
  '`InsightsMetrics` queries AMA/VM Insights CPU utilization across fleet hosts to detect sustained compute saturation.')
t('kql_aks_oom',
  '`KubeEvents | where Reason == "OOMKilling" or Message has "OOMKilled" | project TimeGenerated, Namespace, Name, Message | order by TimeGenerated desc`',
  'Querying `KubeEvents` / `KubePodInventory` isolates memory-limit `OOMKilled` container terminations immediately after a rollout.')
t('mon_dist_tracing',
  'W3C Trace Context (`traceparent` / `OperationId`) across Application Insights Application Map & End-to-End Transaction Diagnostics correlating frontend -> API -> SQL/Service Bus calls',
  'Distributed tracing links multi-hop microservice spans under one `OperationId`, revealing exact downstream dependency bottlenecks on the Application Map.')
t('mon_smart_detection',
  'Application Insights Smart Detection & Dynamic Threshold metric alerts (`Failure Anomalies`) baselining historical seasonality to alert on sudden exception spikes',
  'Dynamic thresholds adapt to diurnal/weekly traffic patterns automatically without brittle static error-count thresholds.')

# ==============================================================================
# COMPLETION (`____`) TOKENS & DISTRACTORS FOR YAML / CLI / BICEP / GIT / KQL
# ==============================================================================
t('tok_ab_fixes', '`Fixes AB#412`', 'When linked via the Azure Boards GitHub App, `Fixes AB#<ID>` in a PR body links AND transitions work item `412` on merge to default branch.')
t('tok_gh_hash_wrong', '`Closes #412`', 'Without `AB#`, `#412` targets GitHub Issue #412 inside the repository rather than Azure Boards work item 412.')
t('tok_jira_wrong', '`AZDO-412`', 'Azure Boards requires the literal `AB#` prefix (`AB#412`), not `AZDO-`.')
t('tok_wiql_wrong', '`WI#412`', '`WI#` is not recognized by the Azure Boards GitHub App parser; `AB#` is mandatory.')

t('tok_lfs_track', '`git lfs track "*.psd"`', '`git lfs track` writes the `filter=lfs diff=lfs merge=lfs -text` entry into `.gitattributes` so matching binaries use Git LFS pointers.')
t('tok_git_rm_cached', '`git rm --cached "*.psd"`', '`git rm --cached` untrack files from the index without configuring Git LFS pointer storage.')
t('tok_git_gc', '`git gc --aggressive`', '`git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage.')
t('tok_git_submodule_cmd', '`git submodule update --init`', '`git submodule` manages nested repositories, not large binary files within a single repo.')

t('tok_scalar_clone', '`scalar clone`', '`scalar clone` clones into a `src/` working directory and automatically enables partial clone, sparse-checkout, commit-graph, and background maintenance.')
t('tok_git_mirror', '`git clone --mirror`', '`--mirror` creates a bare server replica downloading every object and ref, maximizing disk/network usage rather than shrinking laptop clones.')
t('tok_git_bundle', '`git bundle create`', '`git bundle` packages history into an offline archive file rather than optimizing daily developer working trees.')
t('tok_git_archive', '`git archive HEAD`', '`git archive` exports an unversioned tarball without a `.git` repository for commits or pushes.')

t('tok_filter_repo', '`git filter-repo --path certs/sign.pfx --invert-paths`', '`git filter-repo` with `--invert-paths` rewrites all reachable commits to expunge `certs/sign.pfx` completely from repository history.')
t('tok_git_revert_head', '`git revert HEAD~3`', '`git revert` appends a new commit while leaving `certs/sign.pfx` intact and downloadable in historical commit objects.')
t('tok_git_stash', '`git stash pop`', '`git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history.')
t('tok_git_cherry', '`git cherry-pick -n`', '`git cherry-pick` copies commits onto another branch rather than purging sensitive blobs from history.')

t('tok_view_release', '`MintLedgerCore@Release`', 'Appending `@Release` to the Azure Artifacts feed name restricts NuGet/npm resolution strictly to versions promoted into the `@Release` view.')
t('tok_view_local', '`MintLedgerCore@Local`', '`@Local` contains every raw CI package pushed directly to the feed before QA promotion.')
t('tok_view_prerelease', '`MintLedgerCore@Prerelease`', '`@Prerelease` includes beta/RC candidate packages not yet signed off for production.')
t('tok_view_upstream', '`MintLedgerCore@Upstream`', 'Azure Artifacts has no built-in `@Upstream` view; cached upstream packages appear in `@Local` (if configured) and must be promoted for `@Release`.')

t('tok_semver_break', '`3.0.0`', 'Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`).')
t('tok_semver_minor', '`2.5.0`', '`MINOR` (`2.5.0`) is reserved strictly for backward-compatible new functionality.')
t('tok_semver_patch', '`2.4.2`', '`PATCH` (`2.4.2`) is reserved strictly for backward-compatible bug fixes.')
t('tok_semver_pre', '`2.4.1-hotfix.1`', '`2.4.1-hotfix.1` actually sorts LOWER than `2.4.1` in SemVer precedence and does not signal a breaking API change.')

t('tok_cond_succ_fail', '`succeededOrFailed()`', '`succeededOrFailed()` executes the task whether prior tasks succeeded or failed (skipping only if the job was canceled), ideal for `PublishTestResults@2`.')
t('tok_cond_succeeded', '`succeeded()`', '`succeeded()` is the default condition and skips `PublishTestResults@2` whenever `dotnet test` exits non-zero on a failed assertion!')
t('tok_cond_failed', '`failed()`', '`failed()` skips publishing test results whenever all tests pass, leaving successful runs with empty test tabs.')
t('tok_cond_canceled', '`canceled()`', '`canceled()` runs exclusively when a user or timeout aborts the pipeline job.')

t('tok_extends_kw', '`extends:`', 'Top-level `extends:` forces the pipeline to inherit required stages/jobs/steps from a governed YAML template enforceable by Environment `Required template` checks.')
t('tok_include_kw', '`include:`', 'Azure Pipelines YAML has no top-level `include:` pipeline wrapper keyword (`template:` is used inside `steps`/`jobs`/`stages`/`variables` lists).')
t('tok_uses_kw', '`uses:`', '`uses:` is GitHub Actions syntax for invoking an action or reusable workflow, not Azure Pipelines root template inheritance.')
t('tok_import_kw', '`import:`', '`import:` is not a valid Azure Pipelines YAML keyword.')

t('tok_lock_sequential', '`lockBehavior: sequential`', '`lockBehavior: sequential` queues concurrent pipeline deployments to an Exclusive Lock environment so every run executes in FIFO order without skipping.')
t('tok_lock_runlatest', '`lockBehavior: runLatest`', '`lockBehavior: runLatest` executes only the newest queued run and cancels intermediate waiting runs — unsuitable when sequential ordered migrations must all run.')
t('tok_lock_parallel', '`lockBehavior: parallel`', '`parallel` is not a valid `lockBehavior` value on an Azure Pipelines Exclusive Lock (`sequential` and `runLatest` are the two valid modes).')
t('tok_lock_none', '`lockBehavior: bypass`', '`bypass` is invalid YAML syntax and would disable exclusive serialization.')

t('tok_what_if', '`what-if`', '`az deployment group what-if` simulates the Bicep/ARM deployment against live Azure Resource Manager state and prints predicted resource diffs without mutating infrastructure.')
t('tok_validate_only', '`validate`', '`az deployment group validate` checks syntactic/preflight ARM schema validity but does NOT calculate live resource diff mutations (`Create`/`Modify`/`Delete`).')
t('tok_export_cmd', '`export`', '`az deployment group export` downloads the template of a past deployment rather than previewing pending Bicep changes.')
t('tok_decompile_cmd', '`decompile`', '`az bicep decompile` converts legacy ARM JSON to Bicep locally without contacting Azure Resource Manager.')

t('tok_cache_task_name', '`Cache@2`', '`Cache@2` restores and saves immutable build dependency directories (NuGet, npm, pip, Gradle) keyed on lockfile hashes in Azure Pipelines.')
t('tok_pub_artifact', '`PublishPipelineArtifact@1`', '`PublishPipelineArtifact@1` uploads build outputs attached to a specific run rather than restoring keyed cross-run dependency caches.')
t('tok_copy_files', '`CopyFiles@2`', '`CopyFiles@2` copies files between directories on the same agent during a single job.')
t('tok_download_build', '`DownloadBuildArtifacts@1`', '`DownloadBuildArtifacts@1` fetches artifacts from a specified build ID rather than hash-keyed dependency caches.')

t('tok_cancel_in_prog', '`cancel-in-progress: true`', 'Inside GitHub Actions `concurrency:`, `cancel-in-progress: true` terminates any currently running or pending run in the same concurrency group when a newer commit arrives.')
t('tok_fail_fast', '`fail-fast: true`', '`fail-fast: true` belongs to `strategy:` matrix jobs (canceling sibling matrix legs when one leg fails), not superseding old workflow runs across pushes.')
t('tok_continue_err', '`continue-on-error: true`', '`continue-on-error: true` swallows step/job failures rather than canceling redundant workflow runs.')
t('tok_timeout_min', '`timeout-minutes: 5`', '`timeout-minutes` sets a hard execution wall-clock cap regardless of whether a newer commit was pushed.')

t('tok_id_token_write', '`id-token: write`', 'GitHub Actions requires `permissions: id-token: write` to request a signed OIDC token from GitHub OIDC provider for `azure/login` workload identity federation.')
t('tok_contents_write', '`contents: write`', '`contents: write` permits pushing commits/releases to the repo but cannot mint OIDC tokens (`Unable to get ACTIONS_ID_TOKEN_REQUEST_URL`).')
t('tok_checks_write', '`checks: write`', '`checks: write` publishes check runs/annotations and does not enable OIDC token exchange.')
t('tok_sec_events_write', '`security-events: write`', '`security-events: write` uploads SARIF results (e.g., CodeQL/Trivy) to the Security tab, not Azure OIDC tokens.')

t('tok_issecret_vso', '`##vso[task.setvariable variable=SigningPwd;issecret=true]`', 'Adding `;issecret=true` instructs the Azure Pipelines agent to encrypt the runtime variable in memory and mask its value as `***` across all subsequent task logs.')
t('tok_isoutput_only', '`##vso[task.setvariable variable=SigningPwd;isoutput=true]`', '`isoutput=true` exposes the variable to downstream jobs/stages in cleartext without masking it as a secret in build logs!')
t('tok_isreadonly_only', '`##vso[task.setvariable variable=SigningPwd;isreadonly=true]`', '`isreadonly=true` prevents overwriting the variable later in the job but still logs the value in cleartext without `issecret=true`.')
t('tok_logissue_vso', '`##vso[task.logissue type=warning]`', '`task.logissue` prints a warning banner directly into the public pipeline console log!')

t('tok_secure_file_task', '`DownloadSecureFile@1`', '`DownloadSecureFile@1` retrieves an encrypted file from Azure Pipelines Secure Files into `$(Agent.TempDirectory)` for the duration of the job and purges it post-job.')
t('tok_extract_files', '`ExtractFiles@1`', '`ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files.')
t('tok_curl_uploader', '`cURLUploader@2`', '`cURLUploader@2` uploads local files to remote FTP/HTTP endpoints.')
t('tok_github_release', '`GitHubRelease@1`', '`GitHubRelease@1` manages public/repo GitHub Release assets, not encrypted pipeline signing certificates.')

t('tok_dep_ecosystem', '`package-ecosystem: "maven"`', 'In `.github/dependabot.yml`, `package-ecosystem: "maven"` with `directory: "/"` and `schedule.interval: "weekly"` configures Dependabot version/security PRs for Maven `pom.xml`.')
t('tok_dep_java_wrong', '`language: "java-spring"`', 'Dependabot schema uses `package-ecosystem` (`maven`, `gradle`, `npm`, `nuget`, `pip`, `docker`, `github-actions`), not `language: "java-spring"`.')
t('tok_dep_scanner_wrong', '`scanner: "codeql-maven"`', 'CodeQL is configured in GitHub Actions workflow YAML, not inside `.github/dependabot.yml`.')
t('tok_dep_type_wrong', '`build-tool: "mvn"`', '`build-tool` is invalid schema in `.github/dependabot.yml` and fails validation.')

t('tok_kql_percentile', '`percentile(DurationMs, 95)`', 'In KQL `summarize`, `percentile(DurationMs, 95)` computes the 95th-percentile tail latency across matching request rows.')
t('tok_kql_p95_wrong', '`p95(DurationMs)`', 'KQL has no standalone `p95()` aggregation function; `percentile(expr, 95)` or `percentiles(expr, 50, 95, 99)` is required.')
t('tok_kql_top95_wrong', '`top(DurationMs, 95)`', '`top 95 by DurationMs` is a tabular operator returning 95 individual rows, not a `summarize` 95th-percentile statistical aggregate.')
t('tok_kql_stdev_wrong', '`stdev(DurationMs, 95)`', '`stdev()` takes a single column argument to compute standard deviation, not a percentile rank.')

t('tok_dacpac_task', '`SqlAzureDacpacDeployment@1`', '`SqlAzureDacpacDeployment@1` authenticates to Azure SQL (supporting Entra / WIF service connections) and deploys `.dacpac` packages or SQL scripts via `SqlPackage.exe`.')
t('tok_mysql_task', '`MysqlDeploymentOnMachineGroup@1`', '`MysqlDeploymentOnMachineGroup@1` targets MySQL databases, not Azure SQL `.dacpac` state models.')
t('tok_arm_copy_task', '`AzureFileCopy@5`', '`AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas.')
t('tok_webapp_task', '`AzureRmWebAppDeployment@4`', '`AzureRmWebAppDeployment@4` deploys App Service web packages rather than standalone multi-stage SQL `.dacpac` schema diffs.')

# ==============================================================================
# PROPOSED SOLUTION EVALUATION PAIRS (`Proposed solution:` AZ-400 items)
# ==============================================================================
t('ps_yes_meets',
  'Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement',
  'Every functional, networking, licensing, and security constraint in the scenario is satisfied natively.')
t('ps_no_git_rm_hist',
  'No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated',
  'Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential.')
t('ps_no_stakeholder_repos',
  'No — granting `Basic` access to 120 external advisors consumes paid user seats beyond the 5 free seats and grants Azure Repos visibility by default instead of free `Stakeholder` access',
  '`Basic` seats cost money beyond 5 users and grant Azure Repos access unless explicitly stripped, whereas `Stakeholder` is free and natively blocks Repos.')
t('ps_no_fork_pr_target',
  'No — `pull_request_target` combined with checking out the untrusted fork PR HEAD exposes write `GITHUB_TOKEN` and repository secrets to arbitrary code execution',
  '`pull_request_target` runs in the context of the base repository with secret access; checking out untrusted fork code inside it creates a critical pwn-request vulnerability.')
t('ps_no_local_view_prod',
  'No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`',
  'Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores.')
t('ps_no_lead_vs_cycle',
  'No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time',
  'Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category.')
t('ps_no_ms_hosted_priv_vnet',
  'No — standard Microsoft-hosted agents run on shared public networks and cannot route to private-endpoint-only ACR/AKS without VNet-injected Managed DevOps Pools or self-hosted/VMSS agents',
  'Private-endpoint resources with `publicNetworkAccess: Disabled` reject public Microsoft-hosted agent traffic; VNet-integrated agent pools are required.')
t('ps_no_rebuild_per_stage',
  'No — recompiling source code from `HEAD` inside each deployment stage violates build-once-deploy-many and can ship untested commits to production',
  'Multi-stage YAML should compile and package ONCE in the Build stage (`PublishPipelineArtifact`), then download and deploy that exact immutable artifact in QA and Prod.')
t('ps_no_codeowners_unprotected',
  'No — adding `.github/CODEOWNERS` alone only requests reviews; without enabling `Require review from Code Owners` in branch protection or a ruleset, authors can still merge without sign-off',
  '`CODEOWNERS` enforces blocking sign-off only when paired with `Require pull request reviews` + `Require review from Code Owners` on the target branch.')

# Shared realistic distractors for crisp 4-option single-choice & 5-option multi-select items
t('dist_tfvc_locks',
  'Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts',
  'TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations.')
t('dist_classic_pat_org_owner',
  'Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables',
  'Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files.')
t('dist_public_network_enable',
  'Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault',
  'Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements.')
t('dist_manual_portal_hotfix',
  'Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal',
  'Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege.')
t('dist_mma_legacy_agent',
  'Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs',
  'Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture.')
t('dist_disable_branch_prot',
  'Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production',
  'Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code.')
t('dist_complete_mode_blind',
  'Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks',
  'ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template!')
t('dist_hardcode_conn_appsettings',
  'Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding',
  'Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files.')
