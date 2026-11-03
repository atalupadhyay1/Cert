"""Ordered 4-step workflow sequences for Exam GH-200 (`8 O` items/set across 10 sequence families = 40 keys)."""

SEQUENCE_GROUPS = {
    # 1. Domain 1 (1.3 / 1.14): Passing inputs, secrets, and job outputs via a Reusable Workflow (workflow_call)
    'seq_reusable_wf_call': (
        (
            'Declare `on: workflow_call` (`inputs`, `secrets`, `outputs`) in callee → '
            'Write callee step result to `$GITHUB_OUTPUT` & job `outputs` → '
            'Invoke `jobs.<id>.uses` (`@<sha>`) with `with:` & `secrets:` → '
            'Read `needs.<id>.outputs.<key>` downstream',
            'Reusable workflows map step `$GITHUB_OUTPUT` -> job `outputs` -> `on.workflow_call.outputs`, which caller jobs read via `needs.<id>.outputs`.'
        ),
        (
            'Invoke `uses:` without `on: workflow_call` in callee → '
            'Write values to `$GITHUB_ENV` hoping they cross jobs → '
            'Read `steps.ci.outputs` across separate runner VMs → '
            'Pass sensitive secrets via plaintext `with:` inputs',
            'A reusable workflow fails without `on: workflow_call`, `$GITHUB_ENV` never crosses jobs, and passing secrets in `with:` leaks plaintext.'
        ),
        (
            'Read `needs.<id>.outputs` before running the callee job → '
            'Declare `on: workflow_dispatch` only in the callee → '
            'Emit outputs with retired `::set-output` syntax → '
            'Hardcode org secrets inside YAML',
            '`workflow_dispatch` cannot be called by `uses:`, `::set-output` is retired, and downstream jobs must `needs:` the reusable workflow job.'
        ),
        (
            'Place the reusable workflow outside `.github/workflows/` → '
            'Call it inside `steps:` instead of `jobs.<id>.uses` → '
            'Omit `on.workflow_call.outputs` mapping → '
            'Expect secrets to pass implicitly without `secrets:`',
            'Reusable workflows must live in `.github/workflows/`, be invoked at `jobs.<id>.uses` (not `steps:`), and map secrets/outputs explicitly.'
        ),
    ),

    # 2. Domain 1 (1.7): Integration testing against a PostgreSQL Service Container
    'seq_service_container': (
        (
            'Define `services.postgres` with `env` & `--health-cmd pg_isready` → '
            'Map `ports: ["5432:5432"]` (host) or set job `container:` → '
            'Wait for `postgres` health probe to report `healthy` → '
            'Dial `localhost:5432` (host) or `postgres:5432` (container)',
            'Service containers run `--health-cmd` probes and connect via `localhost:<port>` on host runners or `<label>:5432` inside job containers.'
        ),
        (
            'Run integration tests before `services.postgres` starts → '
            'Omit `ports:` on a host-runner job yet query `postgres:5432` → '
            'Skip `--health-cmd` readiness checks → '
            'Declare `services:` after test steps finish',
            'Host-runner steps cannot resolve Docker bridge hostname `postgres` (`use mapped ports + localhost`), and skipping `--health-cmd` causes races.'
        ),
        (
            'Configure `services.postgres` on a `macos-latest` host without Docker → '
            'Echo raw DB passwords in step logs → '
            'Expect container data to persist into separate downstream jobs → '
            'Tear down Docker manually in `post:`',
            'Service containers require Linux Docker runner hosts and are destroyed automatically when the single job finishes.'
        ),
        (
            'Nest `services:` inside an individual `steps:` item → '
            'Run inside a job `container:` yet dial `127.0.0.1:5432` → '
            'Disable health probes completely → '
            'Store DB passwords in unencrypted `vars.*`',
            '`services:` is a job-level key (never inside `steps:`), and steps inside a job `container:` dial `postgres:5432` over the Docker bridge.'
        ),
    ),

    # 3. Domain 2 (2.2 / 2.4): Diagnosing & selectively re-running a failing matrix job variant
    'seq_debug_matrix_fail': (
        (
            'Map the failed job in the run graph to its `matrix` axes → '
            'Check step logs for the first non-zero exit / `::error::` → '
            'Run `Re-run failed jobs` with `Enable debug logging` → '
            'Push the fix and verify all matrix variants pass',
            'Selective `Re-run failed jobs` with `Enable debug logging` (`ACTIONS_STEP_DEBUG` / `ACTIONS_RUNNER_DEBUG`) isolates failures without re-billing green legs.'
        ),
        (
            'Delete `.github/workflows` to hide red checks → '
            'Re-run all 48 green matrix legs ten times without reading logs → '
            'Run `echo ${{ secrets.PROD_KEY }}` in bash → '
            'Set `continue-on-error: true` permanently on test steps',
            'Deleting workflows erases run history, printing secrets violates security rules, and re-running green matrix legs wastes billable minutes.'
        ),
        (
            'Leave `ACTIONS_STEP_DEBUG=true` enabled org-wide forever → '
            'SSH directly into standard GitHub-hosted runner VMs on port 22 → '
            'Download test artifacts before the upload step executes → '
            'Bypass branch protection to merge broken code',
            'Standard GitHub-hosted runners do not expose inbound port 22 SSH, and permanent org-wide debug logging bloats log storage.'
        ),
        (
            'Wait 90 days until workflow logs expire → '
            'Mask exit codes with `|| true` across test scripts → '
            'Fire unrelated `release` webhooks manually → '
            'Search `_diag/` logs on developer laptops',
            'Suppressing exit codes with `|| true` hides real regressions rather than diagnosing the failing matrix variant.'
        ),
    ),

    # 4. Domain 2 (2.8): Publishing a private Organization Starter Workflow template
    'seq_starter_template': (
        (
            'Create an `Internal`/`Private` `.github` repo in the org → '
            'Add `<name>.yml` in `workflow-templates/` (`$default-branch`) → '
            'Add `<name>.properties.json` (`name`, `iconName`, `filePatterns`) → '
            'Confirm repos see it in `Actions -> New workflow`',
            'Organization starter workflows live in `<org>/.github/workflow-templates/` as paired `.yml` + `.properties.json` files (`private templates require Enterprise`).'
        ),
        (
            'Put templates in `.github/workflows/` expecting copies → '
            'Omit the required `.properties.json` metadata file → '
            'Hardcode `master` instead of `$default-branch` → '
            'Expect template edits to update existing repo copies',
            'Files in `.github/workflows/` run on `<org>/.github` itself rather than appearing as templates, and `.properties.json` is mandatory.'
        ),
        (
            'Publish confidential internal templates to a `Public` personal repo → '
            'Add `on: workflow_call` expecting starter templates to run without copying → '
            'Put `action.yml` inside `workflow-templates/` → '
            'Set `Base permissions = Admin` org-wide',
            'Starter workflows copy a static `.yml` scaffold into target repos once; centralized runtime execution requires a `workflow_call` Reusable Workflow.'
        ),
        (
            'Commit `.properties.json` with no matching `.yml` file → '
            'Save SVG icons in `/tmp` on a build runner → '
            'Force squads to fork `<org>/.github` → '
            'Disable GitHub Actions across the org',
            'Every `.properties.json` requires a matching `<name>.yml` in `workflow-templates/` (plus optional `<iconName>.svg`).'
        ),
    ),

    # 5. Domain 3 (3.1 / 3.8): Authoring, bundling, and releasing a TypeScript/JavaScript custom action
    'seq_js_action_release': (
        (
            'Author `action.yml` (`using: "node20"`, `main: "dist/index.js"`) → '
            'Code with `@actions/core` & `core.setFailed()` → '
            'Bundle into `dist/index.js` (`@vercel/ncc`) & commit `dist/` → '
            'Tag `v1.0.0`, slide `v1`, and document the 40-char SHA',
            'Bundling `node20` JavaScript actions into committed `dist/index.js` gives sub-second cross-OS execution with zero consumer `npm install` step.'
        ),
        (
            'Gitignore both `dist/` and `node_modules/` in the release commit → '
            'Set `runs.using: "node12"` in `action.yml` → '
            'Exit raw processes without `@actions/core` → '
            'Tell consumers to reference floating `@main` only',
            'Omitting both `dist/` and `node_modules/` crashes immediately with `Cannot find module`, `node12` is retired, and `@main` is unsafe.'
        ),
        (
            'Place `action.yml` inside `.github/workflows/` with no root metadata → '
            'Set `runs.using: "docker"` for a macOS/Windows helper action → '
            'Log secret inputs via `console.log` → '
            'Skip SemVer tags completely',
            'Docker actions fail on macOS and Windows runners; cross-OS custom actions require JavaScript (`node20`) or Composite actions.'
        ),
        (
            'Cut release `v1.0.0` before authoring `action.yml` → '
            'Require every caller repo to run `npm install` first → '
            'Embed static caller tokens inside `dist/index.js` → '
            'Delete the Git tag right after release',
            'Bundled `dist/index.js` + `action.yml` runs standalone with zero pre-install steps in caller workflows.'
        ),
    ),

    # 6. Domain 3 (3.7): Publishing a custom action to the public GitHub Marketplace
    'seq_marketplace_pub': (
        (
            'Create a `Public` single-action repo with root `action.yml` → '
            'Add unique `name`, `description`, `README`, & `branding` → '
            'Enable `2FA` & accept the Marketplace Developer Agreement → '
            'Draft a Release (`v1.0.0`) checking `Publish to Marketplace`',
            'GitHub Marketplace requires a public single-action repo with root `action.yml`, complete branding/docs, `2FA`, and a SemVer GitHub Release.'
        ),
        (
            'Keep the action repository `Private` or `Internal` → '
            'Pack 6 actions in subfolders with no root `action.yml` → '
            'Skip `2FA` and the Marketplace Developer Agreement → '
            'Push branch `dev` without drafting a GitHub Release',
            'Private/Internal repos and multi-action monorepos cannot publish directly to GitHub Marketplace, and Releases + `2FA` are required.'
        ),
        (
            'Reuse an existing official action `name` (`actions/checkout`) → '
            'Hide `action.yml` inside `.github/workflows/` → '
            'Email a `.zip` archive to GitHub Support → '
            'Tag `0.0.0-draft` without release notes',
            'Marketplace enforces globally unique action `name` metadata and root `action.yml` validation inside the Release UI.'
        ),
        (
            'Publish from an EMU user account (`where public repos are blocked`) → '
            'Omit `description` and `runs:` from `action.yml` → '
            'Commit production `.env` secrets into the repo → '
            'Use mutable tag `latest` only',
            'EMU accounts cannot publish public repos on `github.com`, and `description`/`runs` + SemVer version tags are mandatory.'
        ),
    ),

    # 7. Domain 4 (4.4 / 4.5 / 4.6): Scaling Kubernetes ARC runners with enterprise governance
    'seq_arc_vnet_scale': (
        (
            'Create an org GitHub App (`runner` perms) & K8s Secret → '
            'Create a Runner Group (`no Public repos`; scoped repos) → '
            'Deploy `gha-runner-scale-set` controller + scale set (`min: 0`) → '
            'Allow egress to `github.com`, `*.actions...`, and `ghcr.io`',
            'GA ARC pairs `gha-runner-scale-set` + GitHub App auth inside a restricted Runner Group with Immutable Actions (`ghcr.io`) egress.'
        ),
        (
            'Authenticate ARC with a personal developer PAT → '
            'Enable `Allow public repositories` on the Runner Group → '
            'Mount host `/var/run/docker.sock` across stateful pods → '
            'Block `*.actions.githubusercontent.com` and `ghcr.io` on the firewall',
            'Personal PATs share a 5,000/hr cap, public repos expose internal clusters to fork PR attacks, and blocking `ghcr.io` breaks Immutable Actions.'
        ),
        (
            'Deploy deprecated `summerwind` webhook ARC with inbound port 443 open → '
            'Skip Runner Group scoping across all org repos → '
            'Keep persistent workspaces across unrelated jobs → '
            'Disable Kubernetes RBAC',
            'Legacy webhook ARC is deprecated; GA `gha-runner-scale-set` uses outbound long-polling and ephemeral single-job pods.'
        ),
        (
            'Bake `./config.sh` `.runner` files into a VM image cloned across 20 pods → '
            'Attach an `arm64` macOS Larger runner to Azure VNet → '
            'Store cluster kubeconfigs in plain-text `vars.*` → '
            'Ignore queue metrics',
            'Cloning `.runner` identity files triggers session conflicts; ARC mints fresh JIT runner configs per pod.'
        ),
    ),

    # 8. Domain 4 (4.8 / 4.9): Rotating an Organization Actions secret programmatically via REST API
    'seq_libsodium_secret_api': (
        (
            'Mint an App token (`organization_actions_secrets: write`) → '
            'GET `/orgs/{org}/actions/secrets/public-key` (`key_id`, `key`) → '
            'Encrypt value client-side via LibSodium `crypto_box_seal` → '
            'PUT `/orgs/{org}/actions/secrets/{name}` (`selected` repos)',
            'Actions Secrets REST API requires client-side LibSodium sealed-box encryption against the org public key before `PUT`ting `encrypted_value`.'
        ),
        (
            'POST the plaintext secret to `/orgs/{org}/actions/variables` → '
            'Base64-encode without LibSodium encryption → '
            'Set `visibility: "all"` exposing secrets to `Public` repos → '
            'Read plaintext back via `GET /orgs/{org}/actions/secrets/{name}`',
            'Plain base64 without LibSodium fails decryption, `variables` is plaintext, `all` exposes secrets to public repos, and `GET` never returns plaintext.'
        ),
        (
            'Name the secret `GITHUB_API_KEY` (`reserved GITHUB_ prefix`) → '
            'Upload a `96 KB` secret (`exceeding the 48 KB cap`) → '
            'Send unauthenticated curl calls → '
            'Expect Org secrets to override `production` Environment secrets',
            '`GITHUB_*` names and `>48 KB` payloads fail validation, and `Environment > Repository > Organization` means Env secrets win.'
        ),
        (
            'Commit the encrypted blob into `.github/workflows/rotate.yml` → '
            'Encrypt with a local AES passphrase unknown to GitHub → '
            'Issue `admin:enterprise` classic PATs everywhere → '
            'Reboot self-hosted runners to load secrets',
            'GitHub only decrypts asymmetric LibSodium sealed boxes encrypted with the `key` matching `key_id` from `/public-key`.'
        ),
    ),

    # 9. Domain 5 (5.4 / 5.1): Passwordless cloud deployment with OIDC & Environment protection gates
    'seq_oidc_deploy_gate': (
        (
            'Gate `production` Environment (`reviewers`, `main`) → '
            'Pin cloud OIDC `aud` & `sub: repo:<o>/<r>:environment:production` → '
            'Set `environment: production` & `id-token: write` → '
            'Exchange OIDC JWT at runtime & purge static keys',
            'Pairing `environment: production` with `id-token: write` gates job execution and emits the `repo:<org>/<repo>:environment:production` `sub` claim.'
        ),
        (
            'Set cloud OIDC trust `sub` to wildcard `repo:*:*` → '
            'Omit `permissions: id-token: write` on the job → '
            'Leave `environment:` unset while expecting reviewer gates to pause → '
            'Store static cloud root keys in `vars.*`',
            'Wildcard `repo:*:*` lets external repos assume your cloud role, and omitting `id-token: write` or `environment:` breaks OIDC gating.'
        ),
        (
            'Run deploy on `pull_request_target` checking out untrusted fork PR code → '
            'Set `permissions: write-all` globally → '
            'Request OIDC tokens before Environment reviewers approve → '
            'Print cloud tokens to `$GITHUB_STEP_SUMMARY`',
            'GitHub withholds Environment tokens until protection gates pass, and `pull_request_target` + fork checkout leaks credentials.'
        ),
        (
            'Save a static OIDC JWT inside `secrets.OIDC_JWT` once a month → '
            'Disable TLS verification on cloud login steps → '
            'Skip `aud` validation in Vault → '
            'Allow developers to self-approve their own `production` runs',
            'OIDC JWTs expire in minutes and are minted dynamically per job run, never stored statically.'
        ),
    ),

    # 10. Domain 5 (5.5): Generating & verifying SLSA build provenance Artifact Attestations
    'seq_slsa_attest_verify': (
        (
            'Grant `id-token: write` & `attestations: write` in reusable CI → '
            'Build artifact / immutable `sha256:` image digest → '
            'Sign SLSA provenance via `actions/attest-build-provenance` → '
            'Verify via `gh attestation verify -R <o>/<r> --signer-workflow`',
            'SLSA Build Level 3 pairs `id-token: write` + `attestations: write` in a trusted reusable workflow with `gh attestation verify` deploy gating.'
        ),
        (
            'Run `attest-build-provenance` with `permissions: read-all` only → '
            'Attest a mutable `:latest` image tag with no `sha256:` digest → '
            'Skip verification at deploy time → '
            'Edit build steps locally in caller repos',
            'Attestation signing requires `id-token: write` + `attestations: write`, container attestations require `sha256:` digests, and deploy gates must verify.'
        ),
        (
            'Compute an unsigned `md5sum` in bash → '
            'Commit private PGP signing keys into Git → '
            'Run `gh attestation verify` without `-R` / `--owner` → '
            'Disable Immutable Releases on prod artifacts',
            '`gh attestation verify` requires `-R <org>/<repo>` (or `--owner` + `--signer-workflow`) to validate the exact trusted repository/workflow signer.'
        ),
        (
            'Compile binaries on an unmonitored developer laptop outside Actions → '
            'Upload unsigned binaries to a public bucket → '
            'Pin third-party actions to floating `@main` → '
            'Delete attestation bundles prior to admission checks',
            'Sigstore certificates in Artifact Attestations cryptographically bind artifacts to a verifiable GitHub Actions workflow run.'
        ),
    ),
}

SEQUENCES = {}
for _prefix, _variants in SEQUENCE_GROUPS.items():
    assert len(_variants) == 4, _prefix
    _suffixes = ('ok', 'w1', 'w2', 'w3')
    for _suf, (_label, _note) in zip(_suffixes, _variants):
        assert len(_label) <= 245, f'{_prefix}_{_suf} label too long ({len(_label)}): {_label}'
        assert len(_note) <= 240, f'{_prefix}_{_suf} note too long ({len(_note)}): {_note}'
        SEQUENCES[f'{_prefix}_{_suf}'] = (_label, _note)

assert len(SEQUENCES) == 40
