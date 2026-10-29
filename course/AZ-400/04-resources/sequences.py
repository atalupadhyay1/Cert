"""Twelve four-step ordered sequence groups (`O` items) for Exam AZ-400.

Adapts multi-step Azure DevOps & GitHub Actions `DRAG DROP` sequence questions into
four explicit `Step 1 → Step 2 → Step 3 → Step 4` options under `multiple-choice`.
All labels stay <= 245 characters, balanced in length, and free of banned UI phrases.
"""

SEQUENCES = {}


def s(key, label, meaning):
    if key in SEQUENCES:
        raise ValueError(f'Duplicate sequence key: {key}')
    if label.count('→') != 3:
        raise ValueError(f'{key}: expected 4 steps separated by 3 arrows')
    if len(label) > 255:
        raise ValueError(f'{key}: sequence label exceeds 255 chars ({len(label)})')
    SEQUENCES[key] = (label, meaning)


# 1. GitHub Actions secretless OIDC authentication to Azure
s('seq_gha_oidc_ok',
  'Create an Entra app or Managed Identity with Azure RBAC → add a federated credential matching the repo/environment subject → set `permissions: id-token: write` in YAML → run `azure/login@v2` with client, tenant, and subscription IDs',
  'OIDC federation requires an Entra identity with RBAC and matching `sub` claim before GitHub Actions requests an OIDC JWT (`id-token: write`) for `azure/login`.')
s('seq_gha_oidc_b1',
  'Run `azure/login@v2` without `id-token: write` → create a 5-year client secret → add federated credential → assign Azure RBAC afterward',
  'Without `id-token: write`, GitHub Actions cannot mint an OIDC JWT, and creating long-lived secrets defeats workload identity federation.')
s('seq_gha_oidc_b2',
  'Set `permissions: contents: write` only → store storage keys in plaintext YAML → run `az login --username` → add federated credential last',
  'Plaintext credentials and interactive login fail security controls; OIDC requires pre-configured federated subject matching and `id-token: write`.')
s('seq_gha_oidc_b3',
  'Add federated credential with wildcard `*` subject → run `azure/login` → create the Entra identity → grant RBAC after deployment fails',
  'Entra rejects wildcard `*` subjects in federated credentials, and identity + RBAC must exist before workflow execution.')

# 2. Azure Pipelines required YAML template enforcement on a production Environment
s('seq_env_tmpl_ok',
  'Author the hardened YAML template in a protected repository → reference that repo via `resources.repositories` and `extends` → open target Environment Approvals and checks → add a Required template check for that template path',
  'Environment Required template checks verify at deployment time that the pipeline extends the exact mandated YAML template from the specified repository/ref.')
s('seq_env_tmpl_b1',
  'Add a Required template check on an unreferenced Classic release → let developers copy-paste steps inline → delete `extends` → grant everyone Environment Admin',
  'Inline copy-pasted steps fail the Required template check because the pipeline must formally `extends` the protected YAML template.')
s('seq_env_tmpl_b2',
  'Store the template in an unprotected branch where anyone pushes → skip `extends` → add a branch filter on variable groups → run deployment',
  'An unprotected template branch allows tampering, and omitting `extends` bypasses template structure enforcement.')
s('seq_env_tmpl_b3',
  'Run production deployment first → add Required template check afterward → create the template repo → reference via `include` variable file only',
  'Variable-only `include` does not satisfy a Required template check (`extends`), and checks must precede production deployment.')

# 3. Purging an accidentally committed secret from Git history
s('seq_git_purge_ok',
  'Revoke and rotate the exposed credential in the vault/cloud immediately → rewrite history with `git filter-repo` to purge the blob → force-push cleaned refs and have collaborators reclone → enable secret push protection',
  'Once a secret touches a shared remote it must be treated as compromised and rotated first, followed by history rewrite (`git filter-repo`), ref cleanup, and push protection.')
s('seq_git_purge_b1',
  'Run `git rm secret.json` in a new commit → push normally without rotating the secret → keep old commits intact → close the incident',
  '`git rm` only removes the file from HEAD while leaving the cleartext secret readable in prior commit objects.')
s('seq_git_purge_b2',
  'Delete the branch tag only → wait 90 days to rotate the credential → run `git revert HEAD` → disable secret scanning',
  '`git revert` adds another commit without erasing history, and delaying rotation leaves the leaked credential exploitable.')
s('seq_git_purge_b3',
  'Force-push an empty README → reuse the exact same secret key in Key Vault → skip collaborator reclone → archive the repo',
  'Reusing a leaked secret keeps systems vulnerable regardless of Git rewrites because clones or logs may already hold the value.')

# 4. Azure Artifacts feed promotion workflow (@Local -> @Prerelease -> @Release)
s('seq_art_views_ok',
  'Publish immutable SemVer packages from CI into the feed (`@Local`) → run automated integration tests against the candidate build → promote the validated version to `@Prerelease` / `@Release` → point prod consumers to `@Release`',
  'Feed views expose quality milestones (`@Prerelease`, `@Release`) without rebuilding binaries, ensuring production consumes only promoted immutable artifacts.')
s('seq_art_views_b1',
  'Overwrite version `1.0.0` repeatedly in `@Release` on every commit → run unit tests in production → move failed builds to `@Local` → enable upstream push',
  'Azure Artifacts versions are immutable once published; rebuilding or overwriting `1.0.0` violates artifact provenance.')
s('seq_art_views_b2',
  'Point production directly at unvalidated `@Local` → skip integration tests → recompile source code from scratch during prod release → tag `@Prerelease`',
  'Recompiling source during release breaks build-once-deploy-many integrity, and `@Local` exposes unvalidated CI builds.')
s('seq_art_views_b3',
  'Delete the feed before every release → upload ZIPs to email → manually edit DLL versions → grant anonymous public write access',
  'Manual binary edits and feed deletion destroy provenance, caching, and access governance.')

# 5. Bicep IaC CI/CD validation and gated deployment pipeline
s('seq_bicep_pipe_ok',
  'Run `az bicep build` / linter and secret scan on pull requests → authenticate via OIDC service connection in pre-deploy stage → execute `az deployment group what-if` and review resource changes → run gated `az deployment group create` into production',
  'Linting catches syntax/rule violations early, `what-if` previews destructive drift safely, and gated deployment applies declarative changes idempotently.')
s('seq_bicep_pipe_b1',
  'Run `az deployment group create --mode Complete` directly in prod from laptop → run `what-if` afterward → lint Bicep template → commit to Git',
  'Running `Complete` mode unreviewed in production risks deleting resources omitted from the template before validation occurs.')
s('seq_bicep_pipe_b2',
  'Skip `az bicep build` → export portal ARM JSON manually after prod edits → commit secrets in `parameters.json` → disable PR checks',
  'Manual portal edits and hardcoded secret parameters cause configuration drift and credential exposure.')
s('seq_bicep_pipe_b3',
  'Execute `what-if` without Azure credentials → approve prod before linting → delete resource group nightly → recompile Bicep in prod portal',
  '`what-if` requires live target-scope read/deploy permissions against Azure Resource Manager and precedes approval.')

# 6. Blue-green zero-downtime App Service slot deployment with auto-rollback
s('seq_slot_pipe_ok',
  'Pin slot-sticky settings on `Production` and `staging` → deploy the immutable artifact to the `staging` slot → run warm-up and smoke probes against `staging` → swap `staging` into `Production` (swapping back on gate failure)',
  'Deploying to `staging`, validating warm workers, and swapping VIP routing achieves zero downtime while keeping the prior build warm in `staging` for instant swap-back.')
s('seq_slot_pipe_b1',
  'Stop the `Production` web app → copy files via FTP over 10 minutes → start `Production` → create `staging` slot afterward',
  'Stopping `Production` causes an outage window that deployment slots are specifically designed to eliminate.')
s('seq_slot_pipe_b2',
  'Swap an empty `staging` slot into `Production` → deploy untested binaries directly to `Production` → run smoke tests → pin slot settings last',
  'Swapping before deploying pushes empty state to users, and pinning slot settings afterward leaks staging values.')
s('seq_slot_pipe_b3',
  'Provision a Free F1 plan → create 5 deployment slots → run VIP swap → enable metric autoscale',
  'Free and Basic App Service plans do not support deployment slots or autoscale; Standard S1+ or Premium is required.')

# 7. Self-hosted Azure Pipelines VMSS / Managed DevOps Pool private VNet setup
s('seq_vnet_agent_ok',
  'Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/AKS → deploy a Managed DevOps Pool or VMSS pool into that subnet → enable stateless fresh-image teardown per job → target `pool:` in YAML',
  'VNet-injected Managed DevOps Pools or VMSS agents reach private ACR/AKS endpoints privately while ephemeral image resets prevent cross-build workspace contamination.')
s('seq_vnet_agent_b1',
  'Open `0.0.0.0/0` inbound SSH/443 on private AKS and ACR to the public internet → use Microsoft-hosted agents without VNet → cache credentials on disk → share root shell',
  'Opening private clusters to all internet IPs breaks network isolation when VNet-integrated agent pools solve private reachability cleanly.')
s('seq_vnet_agent_b2',
  'Target `pool:` in YAML first → block outbound port 443 to `dev.azure.com` → install agent on a developer laptop → never clean workspace',
  'Agents require outbound HTTPS 443 connectivity to Azure DevOps to poll job queues, and developer laptops violate build reproducibility.')
s('seq_vnet_agent_b3',
  'Create a Classic deployment group on public VMs → hardcode PATs expiring in 7 days → skip subnet injection → disable TLS',
  'Expired user PATs break automation and un-injected public VMs still cannot route to private endpoints.')

# 8. GitHub Advanced Security CodeQL + Dependabot rollout
s('seq_ghas_ok',
  'Enable GitHub Advanced Security and Secret Push Protection on the repo → configure Dependabot alerts and `dependabot.yml` updates → add a CodeQL workflow on `push`, `pull_request`, and weekly cron → require CodeQL pass in branch rules',
  'Combining push protection, Dependabot SCA PRs, PR/scheduled CodeQL SAST scans, and required status checks blocks vulnerable code before merge.')
s('seq_ghas_b1',
  'Require CodeQL status check first → never add a CodeQL workflow → disable branch protection so PRs merge anyway → run yearly manual review',
  'Requiring a non-existent check deadlocks PRs, and disabling branch protection eliminates merge enforcement.')
s('seq_ghas_b2',
  'Run CodeQL only after production release → ignore Dependabot alerts → commit `.env` secrets → disable push protection',
  'Scanning only post-production misses shift-left prevention and allows leaked secrets into Git history.')
s('seq_ghas_b3',
  'Enable Dependabot on an archived fork only → grant `write-all` to external forks → skip CodeQL → merge failing PRs with admin bypass',
  'Scanning an unused fork leaves production repos unprotected, and `write-all` on forks introduces severe supply-chain risk.')

# 9. Progressive ring deployment with Azure Monitor release gates
s('seq_ring_gate_ok',
  'Build once and publish one immutable artifact in CI → deploy to `Canary` targeting 5% of users → evaluate Azure Monitor alert/KQL gates over a bake window → promote the identical artifact to `EarlyAdopter` and `Global` stages',
  'Progressive exposure deploys one immutable build across widening blast-radius rings gated by automated live telemetry health checks.')
s('seq_ring_gate_b1',
  'Deploy straight to 100% of `Global` users → deploy to `Canary` afterward → rebuild from `HEAD` per ring → check Azure Monitor next week',
  'Deploying to 100% first defeats blast-radius containment, and rebuilding per ring risks shipping different commits.')
s('seq_ring_gate_b2',
  'Set gate evaluation timeout shorter than evaluation delay → skip artifact publishing → approve failed telemetry alerts manually → delete logs',
  'Azure Pipelines rejects gates whose timeout is shorter than initial delay/interval, and overriding failed health signals propagates incidents.')
s('seq_ring_gate_b3',
  'Create separate Git forks per ring → cherry-pick random commits → disable Application Insights → run load tests only on prod DB',
  'Separate forks per ring create severe code divergence instead of promoting one immutable artifact through environment rings.')

# 10. Azure Boards <-> GitHub Enterprise end-to-end traceability setup
s('seq_boards_gh_ok',
  'Install the Azure Boards app from GitHub Marketplace onto target repos → authorize and link repos in Azure DevOps Project Settings → reference `AB#<ID>` / `Fixes AB#<ID>` in commits and PRs → verify linked status badges on Boards cards',
  'Installing the GitHub App and linking repos enables `AB#` mention parsing and state transitions (`Fixes AB#123`) directly on Azure Boards cards.')
s('seq_boards_gh_b1',
  'Type `#123` without `AB#` prefix in unlinked repos → paste personal PATs in commit messages → export CSVs weekly → import into Excel',
  'Without the Azure Boards GitHub connection and `AB#` syntax, GitHub `#123` references GitHub Issues rather than Azure Boards work items.')
s('seq_boards_gh_b2',
  'Mirror GitHub code into TFVC nightly → disable webhooks → manually copy commit SHAs into work item comments → delete GitHub PRs',
  'Manual SHA copying and TFVC mirroring are brittle and unnecessary with native Azure Boards GitHub App integration.')
s('seq_boards_gh_b3',
  'Grant external GitHub users Project Collection Administrator → skip app installation → use `JIRA-123` syntax → disable Boards hub',
  'Over-privileged admin roles violate least privilege and non-`AB#` prefixes do not link Azure Boards items.')

# 11. Migrating Classic Azure Pipelines to versioned multi-stage YAML
s('seq_classic_yaml_ok',
  'Audit Classic tasks, variable groups, task groups, and release gates → export YAML (`View YAML`) and convert task groups to YAML templates → configure approvals/gates on YAML Environments → validate parallel runs before retiring Classic',
  'Structured migration maps task groups to YAML templates and release-stage gates to YAML Environments, verifying parity before retiring Classic definitions.')
s('seq_classic_yaml_b1',
  'Delete all Classic build and release definitions in production immediately → write untested YAML on `main` → skip Environment approvals → hardcode variable secrets',
  'Deleting working production pipelines before validating YAML parity halts emergency release capability.')
s('seq_classic_yaml_b2',
  'Export Classic JSON into Bicep → run Classic task groups directly inside GitHub Actions without refactoring → disable branch policies → skip testing',
  'Azure DevOps Classic task groups are not natively executable in YAML or GitHub Actions without converting to step/job templates.')
s('seq_classic_yaml_b3',
  'Keep release stages in Classic forever → turn off Git version control → copy YAML into wiki pages only → disable service connections',
  'Wiki pages do not execute CI/CD, and leaving releases unversioned in Classic misses code-reviewed pipeline governance.')

# 12. Azure App Configuration dynamic Feature Flag progressive rollout
s('seq_ff_rollout_ok',
  'Create the feature flag with `Microsoft.Targeting` in App Configuration → register `AddAzureAppConfiguration` (`UseFeatureFlags`) and `AddFeatureManagement` → gate code with `IFeatureManager.IsEnabledAsync` → ramp rollout % without redeploying',
  'Decoupling deployment from release via `Microsoft.FeatureManagement` lets teams toggle or ramp user cohorts dynamically without new builds.')
s('seq_ff_rollout_b1',
  'Hardcode `const bool EnableNewCheckout = true` in C# → recompile and redeploy for every 5% ramp step → restart App Service → create App Configuration later',
  'Compile-time constants require full redeployments and restarts for every cohort change or rollback.')
s('seq_ff_rollout_b2',
  'Create feature flags in Key Vault Certificates → call `IFeatureManager` without registering middleware → delete sentinel keys → redeploy Docker image per user',
  'Feature flags live in Azure App Configuration (`.appconfig.featureflag/*`), not X.509 certificates, and require `UseAzureAppConfiguration` refresh middleware.')
s('seq_ff_rollout_b3',
  'Maintain 10 long-lived Git branches per customer cohort → deploy 10 separate App Service plans → merge branches next year → skip `IFeatureManager`',
  'Branch-per-cohort explodes merge debt and infrastructure cost compared to trunk-based code behind a targeting feature flag.')
