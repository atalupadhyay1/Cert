"""Twelve four-step ordered sequence groups (`O` items) for Exam AZ-401.

Adapts multi-step Agentic DevOps `DRAG DROP` workflows (MCP servers, Copilot setup steps,
gh-aw compilation, gh-ado2gh migration, OIDC, Azure SRE Agent, and Observability Agent)
into four explicit `Step 1 → Step 2 → Step 3 → Step 4` options under `multiple-choice`.
All labels stay <= 240 characters and length-balanced across options.
"""

SEQUENCES = {}


def s(key, label, meaning):
    if key in SEQUENCES:
        raise ValueError(f'Duplicate sequence key: {key}')
    if label.count('→') != 3:
        raise ValueError(f'{key}: expected 4 steps separated by 3 arrows')
    if len(label) > 240:
        raise ValueError(f'{key}: sequence label exceeds 240 chars ({len(label)})')
    SEQUENCES[key] = (label, meaning)


# 1. Azure DevOps MCP server with GitHub Copilot cloud agent
s('seq_ado_mcp_ok',
  'Configure Entra OIDC for the `copilot` environment → run `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` → register `@azure-devops/mcp` (`-a azcli`) with scoped `tools` → invoke Copilot on tasks',
  'Copilot cloud agent authenticates to Azure in `copilot-setup-steps.yml` (`copilot` environment OIDC) before starting `@azure-devops/mcp` with scoped tool allowlists.')
s('seq_ado_mcp_b1',
  'Commit a 5-year classic PAT inside `README.md` → skip `copilot-setup-steps.yml` → grant `tools: ["*"]` on prod DBs → disable branch protection on `main`',
  'Plaintext PATs in Git violate secret hygiene, and skipping `copilot-setup-steps.yml` leaves the cloud agent unauthenticated to Azure CLI.')
s('seq_ado_mcp_b2',
  'Rename the job `setup-env` instead of `copilot-setup-steps` → omit `id-token: write` → install `@azure-devops/mcp` globally on prod VMs → merge unreviewed',
  'Copilot cloud agent ignores `.github/workflows/copilot-setup-steps.yml` unless the job is named `copilot-setup-steps` on the default branch.')
s('seq_ado_mcp_b3',
  'Disable the cloud agent firewall completely → paste org admin passwords in `.vscode/settings.json` → delete Azure Boards → run manual SQL edits in prod',
  'Disabling network guardrails and hardcoding admin passwords create severe data-exfiltration and privilege-escalation risks.')

# 2. GitHub Agentic Workflows (gh-aw) authoring & safe-outputs lifecycle
s('seq_gh_aw_ok',
  'Install `github/gh-aw` extension → author `.github/workflows/<name>.md` with `permissions: read-all` and `safe-outputs` → run `gh aw compile` generating `<name>.lock.yml` → commit `.md` and `.lock.yml` via PR',
  '`gh aw compile` validates YAML frontmatter and emits a hardened `.lock.yml` with read-only sandboxed agent execution and separate `safe-outputs` write jobs.')
s('seq_gh_aw_b1',
  'Hand-edit `.lock.yml` directly without `.md` source → set `permissions: write-all` on the agent job → merge Dependabot `.lock.yml` pin PRs directly → skip `gh aw compile`',
  '`.lock.yml` is compiler-managed and must never be hand-edited or updated without `gh aw compile` / `gh aw update-actions`, and `write-all` breaks sandboxing.')
s('seq_gh_aw_b2',
  'Replace all deterministic `dotnet build` and prod deploy YAML with uncompiled `.md` prose → grant prod secrets to untrusted issue comments → skip PR review → deploy directly',
  'GitHub Agentic Workflows complement rather than replace deterministic build/deploy pipelines, and untrusted inputs require read-only + `safe-outputs` isolation.')
s('seq_gh_aw_b3',
  'Commit `.md` under `/docs` without `.lock.yml` → disable Actions runners → store OpenAI keys in plaintext frontmatter → push straight to `main`',
  'GitHub Actions executes the compiled `.github/workflows/<name>.lock.yml` file, and model keys belong in encrypted repository/environment secrets.')

# 3. Repository migration from Azure DevOps to GitHub Enterprise Cloud (gh ado2gh)
s('seq_ado2gh_ok',
  'Run `gh ado2gh inventory-report` with scoped `ADO_PAT`/`GH_PAT` → run `gh ado2gh generate-script --all` and test in sandbox → freeze source writes (`lock-ado-repo`) → run cutover script and `download-logs`',
  'GitHub Enterprise Importer (`gh ado2gh`) does not support delta migrations, so inventory -> sandbox trial -> write freeze -> scripted cutover + log review is best practice.')
s('seq_ado2gh_b1',
  'Delete Azure Repos immediately before migrating → allow heavy concurrent pushes expecting automatic delta sync → paste PATs into source files → skip trial org testing',
  'Deleting source repos destroys code, and GEI has no delta sync so mid-migration pushes are missed unless frozen or manually re-applied.')
s('seq_ado2gh_b2',
  'Copy `.git` folders over email ZIPs → recreate all branches manually without PR metadata → hardcode expired PATs → skip pipeline and Boards rewiring',
  'Emailing ZIP archives loses pull request history, review comments, branch protections, and automated Azure Boards/Pipelines rewiring (`--all`).')
s('seq_ado2gh_b3',
  'Run production cutover first without inventory → leave `ADO_PAT` empty → migrate into public personal accounts → audit permissions next quarter',
  'Migrating enterprise code into personal public repos leaks IP, and `gh ado2gh` requires scoped `ADO_PAT` and `GH_PAT` credentials.')

# 4. Deploying & configuring Azure SRE Agent with Incident Response Plans
s('seq_sre_agent_ok',
  'Provision Azure SRE Agent and connect one incident platform → link GitHub/ADO repos for commit correlation → create an Incident Response Plan with `Review` mode and cooldown → test with a `[TEST]` alert',
  'Azure SRE Agent requires a connected incident platform and at least one Incident Response Plan (with autonomy mode and cooldown) before scanning/triaging alerts.')
s('seq_sre_agent_b1',
  'Connect ServiceNow without specifying an `assignment_group` → connect PagerDuty simultaneously on the same agent → skip creating any response plan → disable RBAC',
  'ServiceNow indexing requires an `assignment_group`, each agent connects to one incident platform at a time, and zero response plans means zero incident scanning.')
s('seq_sre_agent_b2',
  'Disable alert reinvestigation cooldown on noisy 1-minute rules → grant `Autonomous` prod deletion without testing → skip repo links → delete Log Analytics',
  'Disabling cooldown on noisy alerts spawns duplicate investigations every minute, and untested autonomous actions risk unintended production changes.')
s('seq_sre_agent_b3',
  'Select unsupported native Microsoft IcM in the dropdown → skip Azure Monitor Action Group webhooks → omit response plans → turn off Application Insights',
  'Azure SRE Agent natively connects to Azure Monitor, PagerDuty, or ServiceNow (one at a time) and requires at least one response plan.')

# 5. Enabling autonomous operations in Azure Copilot Observability Agent
s('seq_obs_agent_ok',
  'Verify Azure Copilot access and telemetry RBAC → associate the subscription with an Azure Monitor Workspace (AMW) → provision an Observability Agent resource with instructions → enable autonomous Issues',
  'While on-demand chat works setup-free, autonomous alert correlation requires an AMW subscription association and an Observability Agent resource.')
s('seq_obs_agent_b1',
  'Delete all Log Analytics workspaces → expect the agent to bypass caller Azure RBAC and locks → skip AMW association → auto-execute unreviewed prod deletions',
  'Observability Agent strictly honors caller Azure RBAC, PIM, Policy, and locks, and requires an AMW association to persist Azure Monitor Issues.')
s('seq_obs_agent_b2',
  'Export prompts to train public foundation models → deploy retired OMS/MMA agents → skip Observability Agent resource for autonomous mode → ignore Issues tab',
  'Observability Agent never trains foundation models on customer prompts/data, and autonomous background correlation requires an Observability Agent resource.')
s('seq_obs_agent_b3',
  'Provision Observability Agent in an unsupported region without Azure Copilot access → unlink subscriptions from AMW → disable all alert rules → expect issues',
  'Users need Azure Copilot access, supported regional availability, active alerts, and AMW association for autonomous Issue creation.')

# 6. Standardizing & governing GitHub Copilot coding agent across Enterprise repos
s('seq_copilot_gov_ok',
  'Author `.github/copilot-instructions.md` and `SKILL.md` → commit `copilot-setup-steps.yml` on default branch → enable agent firewall allowlists → protect agent/MCP files and enforce human PR review in Rulesets',
  'Layered instructions + deterministic `copilot-setup-steps.yml` + network allowlisting + Ruleset protection/human sign-off secure enterprise agentic coding.')
s('seq_copilot_gov_b1',
  'Place `copilot-setup-steps.yml` only on an unmerged feature branch → let the requester self-approve agent PRs → disable agent firewall → leave `mcp.json` unprotected',
  '`copilot-setup-steps.yml` is ignored until merged to the default branch, and unprotected `mcp.json` or self-approved agent PRs create governance gaps.')
s('seq_copilot_gov_b2',
  'Use `workflow_call` reusable workflows inside `copilot-setup-steps.yml` → set `timeout-minutes: 180` → hardcode secrets in `AGENTS.md` → bypass all status checks',
  '`copilot-setup-steps.yml` does not support reusable workflows (use composite actions instead) and caps `timeout-minutes` at 59.')
s('seq_copilot_gov_b3',
  'Grant Copilot direct push rights to `main` → turn off CodeQL/secret pre-checks → delete session log links from commits → disable branch rulesets',
  'Copilot cloud agent works on isolated `copilot/*` branches and opens draft PRs requiring human review and status checks before merging to `main`.')

# 7. Secretless OIDC deployment from GitHub Actions / Azure Pipelines to Azure
s('seq_oidc_deploy_ok',
  'Assign least-privilege Azure RBAC to a Managed Identity → configure federated subject `repo:<org>/<repo>:environment:production` → set `id-token: write` on the job → run `azure/login@v2` with zero secrets',
  'Exact `environment:production` federated subject matching + `id-token: write` enables short-lived OIDC token exchange without static client secrets.')
s('seq_oidc_deploy_b1',
  'Create a 24-month client secret → omit `id-token: write` → allow wildcard `*` federated subjects → grant subscription `Owner` to all PR branches',
  'Client secrets reintroduce rotation risk, Entra blocks wildcard `*` subjects, and `Owner` on PR branches violates least privilege.')
s('seq_oidc_deploy_b2',
  'Set `permissions: contents: write` only → commit `.pfx` files to Git → run `az login` interactively → add federated credentials after prod fails',
  '`contents: write` cannot mint OIDC tokens, and interactive logins or committed `.pfx` files fail secure automation.')
s('seq_oidc_deploy_b3',
  'Use `pull_request_target` checking out untrusted fork code → inject prod OIDC environment → skip reviewer approvals → push straight to prod',
  'Executing untrusted fork code inside privileged contexts exposes environment tokens to supply-chain attacks.')

# 8. Purging leaked credentials from Git history & preventing recurrence
s('seq_secret_purge_ok',
  'Immediately revoke and rotate the leaked credential → rewrite history across all refs with `git filter-repo` → force-push cleaned branches and reclone → enable Secret Scanning Push Protection',
  'Credential rotation neutralizes live exploitation first; `git filter-repo` erases historical blobs; push protection blocks future leaks synchronously.')
s('seq_secret_purge_b1',
  'Run `git rm credentials.json` in a new commit → leave the live key unrotated → push normally → close the security ticket',
  '`git rm` only removes the file from `HEAD` while leaving cleartext secrets accessible in prior commit trees.')
s('seq_secret_purge_b2',
  'Run `git revert HEAD` → wait 60 days to rotate the key → disable secret scanning → keep collaborator clones unrefreshed',
  '`git revert` adds a new commit without rewriting history, leaving the exposed credential valid and downloadable.')
s('seq_secret_purge_b3',
  'Delete only the GitHub Release note → reuse the identical secret string → archive the issue → grant contributors `Force push = Allow` permanently',
  'Reusing a compromised secret value leaves infrastructure exposed regardless of Git cleanup.')

# 9. Progressive ring deployment with AI/MCP-authored Azure Monitor release gates
s('seq_ring_rollout_ok',
  'Build once and publish one `@sha256` artifact → deploy to `Canary` (5%) with Release Annotations → evaluate automated Azure Monitor alert/KQL gates over bake window → promote same digest to `Global`',
  'Promoting a single immutable artifact across widening rings gated by live Azure Monitor telemetry limits blast radius and guarantees provenance.')
s('seq_ring_rollout_b1',
  'Deploy straight to 100% of `Global` users → rebuild source from `HEAD` in every stage → check telemetry manually next week → deploy `Canary` last',
  'Rebuilding per stage breaks binary equivalence, and deploying 100% first eliminates progressive blast-radius protection.')
s('seq_ring_rollout_b2',
  'Set gate timeout shorter than evaluation delay → override failing Sev1 alerts manually → maintain separate Git forks per ring → skip annotations',
  'Gate timeout must exceed delay + interval, and per-ring Git forks cause severe code divergence.')
s('seq_ring_rollout_b3',
  'Stop production App Service for 20 minutes → upload unversioned ZIPs from a laptop → skip staging warm-up → enable monitoring afterward',
  'Manual laptop uploads and cold outages violate immutable zero-downtime CI/CD principles.')

# 10. Bicep IaC validation & Deployment Stacks pipeline with Copilot/MCP
s('seq_bicep_stack_ok',
  'Run `az bicep build` linter and IaC scans on PRs → authenticate pre-deploy via OIDC → execute `az deployment group what-if` resource diff → apply `az stack group create` with `denyWriteAndDelete`',
  'Combining Bicep linting, live `what-if` diffing, and ARM Deployment Stacks prevents both destructive surprises and manual portal configuration drift.')
s('seq_bicep_stack_b1',
  'Run `az deployment group create --mode Complete` blindly in prod → inspect `what-if` afterward → export manual portal edits → commit secrets in params',
  'Blind `Complete` mode deployments risk deleting existing resources omitted from the template before any `what-if` review.')
s('seq_bicep_stack_b2',
  'Grant all developers subscription `Owner` in prod → edit NSGs manually in Azure Portal → skip Bicep linter → disable Deployment Stack deny settings',
  'Manual portal edits with broad `Owner` rights create untracked drift and bypass PR security checks.')
s('seq_bicep_stack_b3',
  'Run `az bicep decompile` in production without auth → skip `what-if` → delete resource groups nightly → store state in wiki tables',
  '`decompile` is a local JSON-to-Bicep conversion helper, not a live ARM preflight or deployment mechanism.')

# 11. Zero-downtime App Service slot swap with Expand-and-Contract DB changes
s('seq_zero_dt_ok',
  'Apply additive N-1 SQL migration (`Expand`) → deploy app build to slot-pinned `staging` → run `applicationInitialization` warm-up and smoke checks → swap `staging` VIP into `Production`',
  'Additive DB changes preserve N-1 compatibility during slot warm-up, VIP swap, and potential instant swap-back rollback.')
s('seq_zero_dt_b1',
  'Rename/remove live SQL columns first → swap an empty `staging` slot into `Production` → deploy code to `Production` → pin slot settings last',
  'Destructive pre-swap SQL changes break running `Production` instances immediately, and pinning settings last leaks staging configs.')
s('seq_zero_dt_b2',
  'Provision a Free F1 App Service plan → create 4 deployment slots → stop `Production` during deploy → run load tests on prod DB',
  'Free/Basic App Service plans do not support deployment slots; Standard S1+ or Premium is required.')
s('seq_zero_dt_b3',
  'Compile source code directly on the `Production` Kudu console → restart all workers simultaneously → skip warm-up pings → delete backups',
  'In-place compilation and cold restarts cause HTTP 5xx latency spikes and break build immutability.')

# 12. Azure Artifacts `@Release` promotion with upstream caching
s('seq_pkg_prom_ok',
  'Enable Upstream Sources and publish CI SemVer builds to `@Local` → run integration and GHAS dependency scans → promote validated immutable versions to `@Release` → restore prod strictly from `feed@Release`',
  'Upstream caching insulates against public registry outages while `@Release` view promotion guarantees production restores only verified immutable packages.')
s('seq_pkg_prom_b1',
  'Delete and re-push `1.2.0` on every commit → point prod pipelines at `@Local` → disable upstream caching → rebuild packages inside prod release',
  'Published `package@version` coordinates in Azure Artifacts are permanently immutable, and `@Local` exposes untested CI builds.')
s('seq_pkg_prom_b2',
  'Check compiled `.nupkg` binaries into Git without LFS → email DLLs between squads → skip SemVer → allow anonymous feed writes',
  'Committing compiled packages into Git bloats history and bypasses dependency vulnerability scanning and provenance.')
s('seq_pkg_prom_b3',
  'Point CI restores only at `@Release` before publishing → promote broken builds automatically → overwrite `latest` tag in NuGet → delete lockfiles',
  'NuGet uses explicit SemVer versions with lockfiles rather than mutable `latest` tags, and broken builds must never auto-promote to `@Release`.')
