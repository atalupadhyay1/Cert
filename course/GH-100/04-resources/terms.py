"""Canonical option & distractor dictionary (`TERMS`) for Exam GH-100: GitHub Enterprise Administrator.

Every label is strictly <= 240 chars and every explanation note <= 480 chars, with zero banned phrases.
"""

from sequences import SEQUENCES

_ATOMIC_TERMS = {
    # =========================================================================
    # Domain 1: Manage GitHub identities and access (1.1 - 1.9)
    # =========================================================================
    'iam_emu_vs_personal': (
        'Enterprise Managed Users (`EMUs`) provisioned by your corporate IdP (`<handle>_<shortcode>`), isolated from public repo creation, Gists, and external OSS pushes',
        'EMUs give enterprises full lifecycle ownership over user accounts via SAML/OIDC + SCIM while preventing public code/Gist creation and external repository contributions.',
    ),
    'iam_personal_accounts_ghec': (
        'GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO',
        'In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.',
    ),
    'iam_guest_collaborator_emu': (
        'EMU **Guest Collaborator** role provisioned via the IdP to grant contractors private/internal repo access only where explicitly added (blocking broad org `Internal` browse)',
        'In EMU enterprises, Guest Collaborators are IdP-provisioned accounts restricted from automatic `Internal` repository visibility across organizations unless granted explicit access.',
    ),
    'iam_saml_sso_2fa': (
        'Enterprise/Organization SAML 2.0 SSO paired with mandatory GitHub `2FA` (with SAML recovery codes stored safely and PAT/SSH credential authorization enforced)',
        'Enforcing SAML SSO at the Enterprise level centralizes IdP authentication across all member organizations, requires credential authorization for PATs/SSH keys, and pairs with `2FA` on personal-account GHEC.',
    ),
    'iam_scim_vs_teamsync': (
        'SCIM provisions/deprovisions user accounts across EMUs (or org invitations), whereas IdP Team Sync on personal-account GHEC (`Entra ID`/`Okta`) only updates org-team membership for existing org members',
        'SCIM manages account lifecycle (creating/suspending EMUs), while personal-account Team Sync only maps IdP groups to Organization teams and cannot invite non-members into an organization.',
    ),
    'iam_idp_selection': (
        'Supported IdPs (`Microsoft Entra ID`, `Okta`, `PingFederate` with paved-path OIDC/SAML+SCIM for EMUs; or `LDAP`/`CAS`/`SAML` on self-hosted `GHES`)',
        'GHEC EMUs support Entra ID (OIDC or SAML), Okta, and PingFederate (plus custom SAML+SCIM API integration), while GHES adds native LDAP, Active Directory, and CAS authentication.',
    ),
    'iam_oidc_cap_emu': (
        'OIDC SSO for Enterprise Managed Users with **Microsoft Entra ID**, automatically enforcing Entra **Conditional Access Policies (`CAP`)** including IP and device compliance',
        'Configuring OIDC between Entra ID and GHEC EMUs validates Entra Conditional Access Policies during browser sign-in and token refresh Flows.',
    ),
    'iam_authn_vs_authz': (
        'Authentication verifies *who* the caller is (`SAML`/`OIDC`, `2FA`, Passkey, SSH key, PAT), while authorization governs *what* resources they may access (roles, teams, scopes, SAML SSO token authorization)',
        'Even a valid personal PAT or SSH key (`authenticated`) is blocked from accessing a SAML-enforced GHEC organization until explicitly **authorized** for SAML SSO (`authorized`).',
    ),
    'iam_org_repo_roles': (
        '5 built-in repository roles (`Read`, `Triage`, `Write`, `Maintain`, `Admin`), built-in org roles (`Owner`, `Member`, `Moderator`, `Billing manager`, `Security Manager`), plus GHEC **Custom repository/org roles**',
        'GitHub layers additive repository roles (`most permissive wins`) with least-privilege built-in and custom organization/enterprise roles.',
    ),
    'iam_enterprise_teams': (
        '**Enterprise teams** (`@/ent:<slug>`, up to 5,000 EMU IdP-synced users across up to 1,000 orgs) for centralized org membership, Copilot seats, custom enterprise roles, and ruleset bypass',
        'Enterprise teams simplify multi-org governance, Copilot licensing, custom enterprise role delegation, and ruleset bypasses—though they do not support `CODEOWNERS`, nesting, Secret visibility, or non-EMU Team Sync.',
    ),
    'iam_audit_access_perms': (
        'Exporting enterprise/organization membership & repository permission inventories plus auditing `org.*`, `team.*`, `repo.*`, and token metadata (`hashed_token`, `programmatic_access_type`) in the Audit Log',
        'Admins audit effective access via People exports, repository Manage Access filters, REST/GraphQL permission queries, and Audit Log token attribution fields.',
    ),
    'iam_policies_rulesets': (
        'Enterprise **Member privileges** (`Base permissions = None`, repo creation/forking/visibility locks) combined with **Organization/Enterprise Repository Rulesets** (`Active` vs `Evaluate` dry-run mode)',
        'Enterprise policies set hard guardrails across all organizations, while Repository Rulesets layer additive branch/tag/push protections (`most restrictive wins`) with auditable bypasses.',
    ),

    # =========================================================================
    # Domain 2: Administer GitHub Enterprise environment (2.1 - 2.7)
    # =========================================================================
    'env_admin_vs_support': (
        'Enterprise Admins resolve IdP/SAML lockouts, RBAC grants, runner sizing, and webhook configs; **GitHub Enterprise Support** handles platform outages, cached PR commit purges, and repo restore escalations',
        'Admins handle internal identity, permissions, and pipeline configs, while GitHub Support handles cloud infrastructure incidents, server-side cache purges, and backend appliance/cloud escalations.',
    ),
    'env_support_bundles_diag': (
        'Running `ghe-diagnostics` and `ghe-support-bundle -x` via SSH (or GHES Management Console `:8443`) to attach extended logs and cluster telemetry to a GitHub Enterprise Support ticket',
        'On GHES, `ghe-support-bundle -x` packages sanitized system, service, and recent diagnostic logs over an extended window so GitHub Support can diagnose appliance issues rapidly.',
    ),
    'env_dev_process_standards': (
        'Standardizing **Template repositories**, organization-wide `.github` community health defaults, **`Internal`** InnerSource discovery, and ADR/Issue Form intake across teams',
        'Enterprise developer standards combine golden template repositories, an org `.github` repo for default templates/policies, and `Internal` InnerSource visibility.',
    ),
    'env_workflow_branch_release': (
        'Enforcing trunk-based **GitHub Flow**, protected `main` with **`CODEOWNERS`**, **Merge Queue** (`gh-readonly-queue`) for busy monorepos, linear squash merges, and immutable signed SemVer **Releases**',
        'Standardizing short-lived branches, Code Owner reviews, Merge Queue CI batching, and protected `v*` release tags keeps enterprise delivery predictable and auditable.',
    ),
    'env_deployment_scenarios': (
        'Comparing the 4 Enterprise models: **GHEC + personal accounts**, **GHEC + EMU**, **GHEC with Data Residency (`<ent>.ghe.com`) + EMU**, and self-hosted **GitHub Enterprise Server (`GHES`)**',
        'GHEC with Data Residency (`<ent>.ghe.com`) always uses EMUs and pins code/metadata in a chosen region (EU/US/AU/JP), while GHES runs self-hosted in your own datacenter or sovereign cloud VPC.',
    ),
    'env_licensing_billing': (
        'Per-user **GitHub Enterprise** seat licensing (deduplicating unique users across orgs + synced `GHES` via **GitHub Connect**, plus linked **Visual Studio Enterprise/Pro with GitHub Enterprise** benefits) alongside metered add-ons',
        'One Enterprise user consumes a single seat across unlimited organizations in the enterprise (and synced GHES instances via GitHub Connect), while Actions, Packages, Codespaces, GHAS, and Copilot meter separately.',
    ),
    'env_license_monitoring': (
        'Inspecting `Enterprise -> Billing & Licensing -> Licensing` (and exported `consumed-licenses` JSON/CSV) to track assigned seats, pending invitations, outside collaborators, VS subscriptions, and `GHES` sync files',
        'Pending org invitations, outside collaborators on private repos, enterprise members, and unsynced duplicate emails across GHES/GHEC all impact Enterprise license counts and must be audited regularly.',
    ),

    # =========================================================================
    # Domain 3: Implement secure software development and compliance (3.1 - 3.10)
    # =========================================================================
    'sec_enterprise_policies': (
        'Enforcing **Enterprise Policies** (`Enforced` vs `No policy` delegated to orgs) and **Custom Security Configurations** (`GitHub Secret Protection` + `GitHub Code Security` / `GHAS`) across organizations',
        'Enterprise Policies lock repository creation, forking, visibility changes, and Pages access globally, while enforced Security Configurations standardize GHAS/Dependabot settings across repositories.',
    ),
    'sec_posture_data_prot': (
        'Hardening access with **Organization/Enterprise IP allow lists**, **SSH Certificate Authorities (`SSH CAs`)** issuing short-lived developer SSH certs, and least-privilege repo-scoped **Deploy keys**',
        'SSH CAs eliminate unrotated static personal SSH keys by requiring short-lived certificates signed by the corporate CA, paired with IP allow lists (or Entra CAPs).',
    ),
    'sec_audit_log_streaming': (
        'Streaming the **Enterprise Audit Log** (including optional `git.clone`/`git.fetch`/`git.push` events) in real time to **Azure Event Hubs / Blob Storage, AWS S3, Splunk, Datadog, or GCS**, plus REST/GraphQL queries',
        'Because UI/REST audit retention is time-bounded (180 days standard; shorter for high-volume Git events), compliance teams stream immutable audit events continuously to external SIEM/WORM storage.',
    ),
    'sec_codeql_secret_scan': (
        'Enabling **CodeQL code scanning** (`Default setup` or custom `Advanced setup` SARIF workflows) plus **Secret scanning** with **Push protection**, **Validity checks**, custom regex patterns, and delegated bypass review',
        'CodeQL analyzes code semantically for CWE/OWASP flaws, while Secret Scanning Push Protection blocks credential commits pre-receive and verifies live token status via partner validity checks.',
    ),
    'sec_dependabot_advisories': (
        'Configuring **Dependency graph**, **Dependabot alerts**, **Dependabot security & version updates** (`dependabot.yml` + private registry access), **Dependency Review Action** on PRs, and **Repository Security Advisories**',
        'Dependabot flags known CVEs, opens automated upgrade PRs (authenticating to private registries when configured), blocks vulnerable PR dependencies via Dependency Review, and pairs with private Security Advisories.',
    ),
    'sec_incident_response': (
        'Executing the **Security Response Plan**: immediately revoke/rotate leaked secrets, scrub Git refs via **`git filter-repo`**, force-push cleaned history, and ask **GitHub Support** to purge unreachable cached PR/commit views',
        'Rewriting Git history never un-compromises an exposed credential; rotation comes first, followed by `git filter-repo`, force-pushing, collaborator re-cloning, and a Support cache purge.',
    ),
    'sec_pat_governance': (
        'Enforcing **Enterprise Fine-Grained PAT Policies**: restricting or blocking **PATs (classic)**, requiring mandatory expiration lifetimes (e.g., <=30–90 days), requiring **Admin approval** before Fine-grained PATs activate, and revoking tokens',
        'Enterprise PAT policies curb broad non-expiring classic PATs and require organization owner approval, repo scoping, and short lifetimes on Fine-grained PATs.',
    ),
    'sec_api_rate_limits': (
        'REST rate limits: **`5,000 req/hr`** per personal PAT user vs **`15,000 req/hr`** for a **GitHub App installation** (and `GITHUB_TOKEN` per repo) on **GHEC** (`up to 12,500 req/hr` scaled on non-GHEC; GraphQL `5,000` vs `10,000` pts/hr)',
        'On GHEC, GitHub App installations get 15,000 REST req/hr (and 10,000 GraphQL pts/hr) isolated from human users, whereas user PATs share one 5,000 req/hr personal bucket and hit secondary concurrency caps faster.',
    ),
    'sec_github_vs_oauth_apps': (
        '**GitHub Apps** act as independent actors scoped to selected repos + granular permissions using **1-hour installation tokens**, whereas **OAuth Apps** act as the authorizing human user with broad scopes and long-lived tokens',
        'GitHub Apps survive employee offboarding, consume zero user seats, grant fine-grained repo/resource permissions, and use short-lived tokens—outperforming both OAuth Apps and seat-consuming machine users.',
    ),
    'sec_app_approval_policy': (
        'Enabling **OAuth App access restrictions** and **GitHub App installation approval workflows** so developer-requested integrations stay blocked on private org data until vetted and approved by an Organization/Enterprise Owner',
        'With OAuth App access restrictions active, unapproved third-party OAuth apps can read public data only and cannot touch organization private repos until an Owner explicitly approves the request.',
    ),

    # =========================================================================
    # Domain 4: Manage GitHub Actions (4.1 - 4.8)
    # =========================================================================
    'act_enterprise_reuse': (
        'Sharing reusable workflows (`on: workflow_call`) and composite actions in **`Internal`** or **`Private`** repositories with `Settings -> Actions -> General -> Access` enabled for organization/enterprise workflows',
        'Without publishing proprietary actions to the public internet, enterprises host golden `workflow_call` workflows and actions inside `Internal`/`Private` repos with cross-repo enterprise workflow access enabled.',
    ),
    'act_org_policies_sha': (
        'Enforcing **Allowed actions and reusable workflows** (`GitHub-created`, `Verified creators`, internal patterns) plus **`Require actions to be pinned to a full-length commit SHA`**, `Read-only` default `GITHUB_TOKEN`, and fork PR approval',
        'Pinning third-party actions to immutable 40-char commit SHAs blocks tag-mutation supply-chain attacks, while `permissions: read-all` / read-only `GITHUB_TOKEN` defaults enforce least privilege.',
    ),
    'act_runner_groups_arc': (
        'Organizing **Enterprise & Organization Runner Groups** restricted to selected repos and workflows, scaling **Larger GitHub-hosted runners** or ephemeral (`--ephemeral`) self-hosted runners via **Actions Runner Controller (`ARC`)** on Kubernetes',
        'Runner groups isolate sensitive self-hosted or Larger runners to approved repositories and reusable workflow refs, while `--ephemeral` JIT / ARC pods ensure clean single-job runner state.',
    ),
    'act_azure_private_net': (
        'Binding **Linux/Windows Larger GitHub-hosted runners** to an **Azure Virtual Network (`VNet`)** via `GitHub.Network/networkSettings` and Enterprise/Org **Network Configurations** (plus proxy vars / IP allow lists for self-hosted runners)',
        'Azure Private Networking gives GitHub-hosted Larger runners private RFC1918 VNet egress to internal registries/databases and satisfies organization IP allow lists without maintaining self-hosted VMs.',
    ),
    'act_runner_diagnostics': (
        'Inspecting self-hosted runner **`_diag/Runner_*.log`** (registration, listener, network/proxy errors) and **`_diag/Worker_*.log`** (job step execution), `svc.sh status`, tool-cache disk usage, and Actions queue time metrics',
        '`Runner_*.log` records control-plane polling/TLS/proxy failures on the self-hosted agent, whereas `Worker_*.log` captures per-job execution details when jobs fail or stall.',
    ),
    'act_secret_scope_hierarchy': (
        'Scoping encrypted secrets across **Organization -> Repository -> Environment** where **most specific wins (`Environment > Repository > Organization`)**, gated by Environment **Required reviewers** and **Deployment branches/rulesets**',
        'Production cloud secrets belong in protected Deployment Environments (`environment: production`) gated by human/custom deployment protection rules and branch filters, overriding broader repo/org secrets.',
    ),
    'act_org_repo_secrets_cfg': (
        'Configuring Organization secrets restricted to **`Selected repositories`** (or `Private and internal`), encrypting REST API secret uploads with the org/repo **LibSodium public key**, and separating non-sensitive **`vars`** from `secrets`',
        'Organization secrets never pass to public repos unless explicitly permitted, API writes require LibSodium sealed-box encryption (`48 KB` max per secret), and plain-text config belongs in `vars` context.',
    ),
    'act_third_party_vaults_oidc': (
        'Federating GitHub Actions (`permissions: id-token: write`) via **OpenID Connect (`OIDC`)** with **HashiCorp Vault**, **Azure Key Vault**, or **AWS Secrets Manager** using strict `sub` (`repo:`/`environment:`) and `aud` claims',
        'OIDC exchanges a job-scoped JWT signed by `https://token.actions.githubusercontent.com` for short-lived dynamic vault credentials at runtime—eliminating static secrets stored in GitHub.',
    ),

    # =========================================================================
    # Domain 5: Monitor and optimize GitHub usage (5.1 - 5.5)
    # =========================================================================
    'mon_audit_api_insights': (
        'Querying the **Enterprise Audit Log** (`action:`, `actor:`, `hashed_token:`) and **Organization API Insights** (`time-series requests, rate-limited callers, top GitHub Apps, OAuth Apps, and PATs`) to pinpoint noisy/failing integrations',
        'API Insights visualizes hourly/daily REST consumption and `403`/`429` rate-limit hits broken down by specific App or PAT user so admins fix runaway polling loops quickly.',
    ),
    'mon_admin_vs_support_diag': (
        'Using GHES **Management Console / Grafana / `ghe-diagnostics` / Activity Dashboard** (or `githubstatus.com` + Enterprise Support portal with `Support Admin` entitlement on GHEC) to separate local misconfiguration from platform incidents',
        'Admins first inspect `githubstatus.com`, SAML/webhook delivery logs, and `ghe-diagnostics` CPU/memory/queue health, escalating to GitHub Support via entitled Enterprise Support members with bundles attached.',
    ),
    'mon_adoption_usage_metrics': (
        'Evaluating **Copilot Metrics API / Usage Dashboard** (active vs assigned seats, IDE/Chat/PR adoption), **Security Overview** coverage/MTTR, **Actions Usage Metrics**, and **GHES Dormant Users** reports to find underutilized features',
        'Comparing assigned seats against 7/28/90-day active usage across Copilot, GHAS Security Overview, and Actions workflows highlights teams needing enablement or license reclamation.',
    ),
    'mon_metered_billing_reports': (
        'Analyzing **Enhanced Billing Platform** usage exports, **Cost Centers**, **Budgets & 75/90/100% alerts**, OS runner minute multipliers (`Linux < Windows < macOS`), shared **Actions/Packages storage**, and **90-day unique GHAS committers**',
        'Metered billing tracks included enterprise quotas first (for standard hosted runners and Packages/Artifacts storage) and bills overages or Larger runners/Copilot/GHAS against assigned Cost Centers and Budgets.',
    ),
    'mon_cost_license_opt': (
        'Reclaiming **dormant GHES/GHEC seats** & stale pending invitations, enabling **GitHub Connect** license deduplication, caching dependencies (`actions/cache`), shortening artifact retention days, and right-sizing `ubuntu` vs `macos` runners',
        'Suspending dormant users, cancelling expired invitations, syncing GHEC+GHES via GitHub Connect, trimming artifact retention (`retention-days: 7`), and moving non-Apple jobs off macOS runners cut spend immediately.',
    ),

    # Additional High-Specificity Enterprise Admin Keys Across Domains 1 - 5
    'iam_custom_enterprise_roles': (
        'Custom **Enterprise roles** (such as `Audit Log Reader`, `Billing Viewer`, or `Enterprise Actions Admin`) assigned to individuals or **Enterprise teams** to avoid over-granting `Enterprise Owner`',
        'Custom enterprise roles delegate narrow slices of enterprise administration without exposing full owner control over SAML, billing, or organization deletion.',
    ),
    'iam_custom_properties_rulesets': (
        'Repository **Custom Properties** (e.g., `compliance_tier=pci`, `data_class=restricted`) targeted dynamically by Organization/Enterprise **Repository Rulesets** (`most restrictive wins`)',
        'Organization and Enterprise admins enforce schema-validated Custom Properties on repos and bind Rulesets to property queries (`compliance_tier:pci`) automatically.',
    ),
    'iam_ssh_deploy_keys': (
        'Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories',
        'A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.',
    ),
    'env_ghes_ha_backup_utils': (
        'Deploying **GHES High Availability** (`ghe-repl-setup` active/passive failover replica) paired with incremental off-appliance snapshots via **`github/backup-utils`** (`ghe-backup` / `ghe-restore`)',
        'HA replication protects against primary VM hardware failure, while scheduled `backup-utils` snapshots on a separate host provide point-in-time disaster recovery.',
    ),
    'env_ghes_maintenance_mode': (
        'Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing',
        'Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.',
    ),
    'env_starter_workflows_dotgithub': (
        'Publishing reusable **Starter Workflows** inside the organization’s `.github` repository (`workflow-templates/*.yml` + `.properties.json`) to standardize onboarding CI pipelines',
        'Workflow templates in `<org>/.github/workflow-templates/` appear automatically in the `Actions -> New workflow` gallery for every repository in the organization.',
    ),
    'sec_push_rulesets_paths': (
        'Configuring **Push Rulesets** to block oversized binaries, forbidden file extensions (`.pem`, `.pfx`, `.key`), restricted file paths (`.github/workflows/**`), and path-traversal commits pre-receive',
        'Push rulesets evaluate file paths, extensions, and blob sizes on `git push` before commits land on any branch in targeted repositories.',
    ),
    'sec_security_overview_org': (
        'Using **Enterprise/Organization Security Overview** (`Risk` and `Coverage` dashboards) to audit GHAS enablement gaps, open critical `CodeQL`/Secret/Dependabot alerts, and remediation MTTR',
        'Security Overview aggregates alert risk, push-protection metrics, and tool coverage across thousands of repositories for CISOs and Security Managers.',
    ),
    'sec_custom_secret_patterns': (
        'Defining **Custom Secret Scanning Patterns** (with before/after context expressions and dry-run historical backtesting) at the Organization or Enterprise level to catch internal proprietary token formats',
        'Dry-running custom regex patterns at the org/enterprise level validates false-positive rates before publishing push-protection enforcement across repositories.',
    ),
    'sec_dependabot_private_runner': (
        'Configuring **Dependabot** with encrypted `dependabot` private-registry secrets (`Settings -> Code security -> Global settings`) and running updates on **Actions runners / ARC** when private VNet access is required',
        'Granting Dependabot private-registry credentials (and running Dependabot on VNet-connected Actions/ARC runners) lets Dependabot resolve internal Artifactory/NuGet/npm packages securely.',
    ),
    'sec_github_app_jwt_flow': (
        'Signing a short-lived **RS256 JWT** (`<=10 minutes`) with the **GitHub App private key** to call `POST /app/installations/{installation_id}/access_tokens` and mint a **1-hour** installation token',
        'GitHub Apps never send their `.pem` private key over the network; they sign a <=10-minute JWT locally and exchange it for a scoped 1-hour installation access token.',
    ),
    'sec_secondary_rate_limits': (
        'Mitigating **Secondary (abuse) rate limits** by capping concurrent API requests, serializing write mutations (`>=1 sec` spacing), using **webhooks / GraphQL / Conditional `ETag` (`304 Not Modified`)**, and honoring `Retry-After`',
        '`304 Not Modified` conditional requests do not count against primary REST rate limits, while webhook-driven architectures and `Retry-After` backoff prevent secondary `403` throttling.',
    ),
    'act_ephemeral_jit_runners': (
        'Provisioning **ephemeral self-hosted runners** (`./config.sh --ephemeral` or REST **JIT runner** configs via **Actions Runner Controller `ARC`**) that execute **exactly one job** and self-destruct cleanly',
        'Single-use ephemeral runners prevent cross-job workspace contamination, lingering credentials, or persistent malware across CI builds.',
    ),
    'act_proxy_self_hosted': (
        'Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls',
        'Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.',
    ),
    'act_custom_deploy_prot_rules': (
        'Enforcing **Custom Deployment Protection Rules** (backed by a GitHub App checking ServiceNow change tickets or Datadog SLOs) alongside human Required Reviewers on `production` Environments',
        'Custom deployment protection rules gate `environment: production` jobs automatically via webhook callbacks to external ITSM or observability systems.',
    ),
    'mon_ghes_prometheus_snmp': (
        'Scraping **GHES Prometheus `/metrics`** (or forwarding `syslog` + `SNMP` health traps) to alert platform SREs proactively on disk IOPS saturation, Redis/MySQL replication lag, and CPU load',
        'GHES exposes native Prometheus metrics, SNMP, and syslog forwarding so enterprise monitoring stacks catch resource pressure before outages occur.',
    ),
    'mon_copilot_metrics_api': (
        'Querying the **GitHub Copilot User Management & Metrics REST APIs** (`last_activity_at`, `last_activity_editor`, acceptance/chat telemetry) to automate seat reclamation for inactive assignees',
        'Tracking `last_activity_at` per Copilot seat lets enterprise admins automatically reclaim unused seats after a defined inactivity window (e.g., 30–60 days).',
    ),
    'mon_ghas_90day_committer': (
        'Understanding that **GitHub Advanced Security (`GHAS`)** bills per **unique active committer** over a rolling **90-day** window across enabled private/internal repos (free on public repos!)',
        'If an engineer pushes to 15 GHAS-enabled private repos across 4 orgs in the same enterprise, deduplicated enterprise billing counts only **1** GHAS committer license.',
    ),

    # =========================================================================
    # Proposed Solution Evaluation Keys (sol_yes & sol_no_*)
    # =========================================================================
    'sol_yes': (
        'Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement',
        'Every technical requirement, permission boundary, and GitHub Enterprise platform rule in the scenario is satisfied cleanly.',
    ),
    'sol_no_team_sync_invites': (
        'No — on GHEC with personal accounts, IdP **Team Synchronization** only updates Organization team membership for existing org members and **cannot** invite or provision brand-new users into the organization',
        'Personal-account Team Sync (`Entra ID`/`Okta`) never adds non-members into an organization; users must join the org via SAML/SCIM invitation first (or deploy GHEC with EMUs).',
    ),
    'sol_no_ent_team_codeowners': (
        'No — **Enterprise teams** (`@/ent:<slug>`) currently do **not** support `CODEOWNERS` assignment, nested child teams, Secret visibility, or Team maintainers; use an **Organization team** for `CODEOWNERS`',
        'While Enterprise teams excel at cross-org access, Copilot licensing, custom enterprise roles, and ruleset bypasses, `CODEOWNERS` requires Organization teams or individual users with Write+ access.',
    ),
    'sol_no_transferred_repo_secconfig': (
        'No — an organization’s default **Security Configuration** auto-attaches only to **newly created** repositories; repositories **transferred** into the organization must have the Security Configuration attached manually or via API',
        'GitHub applies default Security Configurations when a repository is newly created in the org, not when an existing repository is transferred in.',
    ),
    'sol_no_git_rm_keeps_history': (
        'No — committing `git rm` (or archiving the repo) leaves the leaked secret intact in prior Git commits and cached PR diffs; you must **revoke/rotate the secret immediately**, run **`git filter-repo`**, force-push, and contact GitHub Support',
        'Deleting a file in a new commit never purges prior blob SHAs, and any exposed secret must be considered compromised and rotated immediately.',
    ),
    'sol_no_pat_shared_rate_limit': (
        'No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)',
        'Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.',
    ),
    'sol_no_macos_arm_azure_vnet': (
        'No — **Azure Private Networking** (`VNet` integration) and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, NOT on standard free runners or `arm64` macOS Larger runners',
        'Standard hosted runners cannot join customer Azure VNets, and arm64 macOS Larger runners do not support Azure private networking or static IP assignment.',
    ),
    'sol_no_org_secret_overrides_env': (
        'No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret',
        'Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.',
    ),
    'sol_no_dormant_deletes_commits': (
        'No — suspending a dormant GHES user or removing/SCIM-deprovisioning a GHEC member **frees their Enterprise license seat** while **preserving all historical commits, Issues, and Pull Request audit trails**',
        'Offboarding or suspending inactive accounts reclaims per-user licenses cleanly without breaking repository Git history or compliance review logs.',
    ),

    # =========================================================================
    # Plausible Admin Anti-Pattern Distractors (bad_*)
    # =========================================================================
    'bad_convert_personal_to_emu': (
        'Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists',
        'Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.',
    ),
    'bad_saml_replaces_pat_authz': (
        'Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step',
        'Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.',
    ),
    'bad_ent_team_over_5000': (
        'Sync a single 12,000-member Entra ID group into one Enterprise team alongside 15 manually added contractor accounts',
        'IdP-synced Enterprise teams require zero manually added members and pause synchronization whenever the linked IdP group exceeds 5,000 users.',
    ),
    'bad_support_ssh_into_ghes': (
        'Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages',
        'GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.',
    ),
    'bad_double_pay_ghec_ghes': (
        'Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated',
        'Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.',
    ),
    'bad_audit_ui_7_years': (
        'Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming',
        'GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.',
    ),
    'bad_ghas_billed_all_readers': (
        'Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository',
        'GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.',
    ),
    'bad_actions_tag_pin_v1': (
        'Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability',
        'Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.',
    ),
    'bad_self_hosted_public_repo': (
        'Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions',
        'Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!',
    ),
    'bad_oidc_wildcard_repo': (
        'Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly',
        'Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!',
    ),
    'bad_store_secrets_in_vars': (
        'Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly',
        '`vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.',
    ),
    'bad_macos_for_linux_containers': (
        'Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges',
        '`macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.',
    ),

    # =========================================================================
    # Multi-Select Atomic Options (`ms_*`) Across Domains 1 - 5
    # =========================================================================
    # Domain 1 MS
    'ms_d1_emu_idp_lifecycle': (
        'Provision user accounts exclusively via your corporate IdP (`SAML`/`OIDC` + `SCIM`), blocking personal public repos, Gists, and external OSS contributions',
        'EMUs ensure corporate lifecycle control and eliminate accidental public repo or Gist leakage under managed handles.',
    ),
    'ms_d1_emu_guest_collab': (
        'Assign external contractors the IdP **Guest Collaborator** role so they cannot browse `Internal` enterprise repositories unless explicitly granted access',
        'Guest Collaborators prevent contractors in EMU enterprises from automatically reading all `Internal` repositories across member organizations.',
    ),
    'ms_d1_ent_team_copilot_roles': (
        'Grant **Copilot Business** seats, **custom/predefined enterprise roles**, and **Repository Ruleset bypass** rights directly to **Enterprise teams** (`@/ent:<slug>`)',
        'Enterprise teams streamline multi-org role delegation, enterprise-level Copilot seat assignment, and ruleset bypass administration.',
    ),
    'ms_d1_ent_team_org_assign': (
        'Add **Enterprise teams** across up to 1,000 organizations where org admins can grant additional repo access without removing enterprise-granted permissions',
        'Enterprise team organization assignments add members directly without invitations and protect enterprise-granted baseline access from org-level removal.',
    ),
    'ms_d1_saml_recovery_codes': (
        'Download and vault **Enterprise/Org SAML recovery codes** before enforcing SAML SSO so Owners can recover access during an IdP outage',
        'Storing SAML recovery codes offline prevents total administrative lockout if the corporate Identity Provider experiences a certificate or service outage.',
    ),
    'ms_d1_pat_ssh_saml_authz': (
        'Require developers on personal-account GHEC to **authorize** approved Fine-grained/classic PATs and SSH keys for SAML SSO before accessing org repositories',
        'SAML enforcement blocks un-authorized programmatic credentials (PATs and SSH keys) even when owned by valid organization members.',
    ),
    'ms_d1_base_perm_none': (
        'Set Organization **`Base permissions = None`** and grant repository access strictly through IdP-synced Teams and least-privilege Custom Repository Roles',
        'Setting Base permissions to `None` prevents newly added org members from automatically reading or writing every private repository in the organization.',
    ),

    # Domain 2 MS
    'ms_d2_ghe_support_bundle': (
        'Generate an extended diagnostic archive via `ghe-support-bundle -x` (or Management Console `:8443`) and upload it to the **GitHub Enterprise Support** portal',
        'Extended support bundles give GitHub Support complete service, cluster, and error telemetry without exposing your appliance to external SSH.',
    ),
    'ms_d2_entitled_support_members': (
        'Designate up to 20–25 entitled **Support** members (or `Enterprise Support` custom role holders) authorized to open and manage enterprise support tickets',
        'Enterprise Owners explicitly grant support-portal entitlement to designated engineers rather than sharing a single Enterprise Owner login.',
    ),
    'ms_d2_ghec_data_residency': (
        'Deploy **GHEC with Data Residency (`<enterprise>.ghe.com`) + EMUs** when regulations require pinning cloud source code and metadata in a specific geographic region (`EU`, `US`, `AU`, `JP`)',
        'GHEC with Data Residency hosts code and metadata on a dedicated regional `.ghe.com` cloud stamp and always requires Enterprise Managed Users.',
    ),
    'ms_d2_github_connect_dedup': (
        'Enable **GitHub Connect** license synchronization between `GHES` and `GHEC` (plus link **Visual Studio Subscriptions**) so hybrid users consume a single Enterprise seat',
        'GitHub Connect correlates verified email addresses across GHES and GHEC and reconciles Visual Studio Enterprise/Pro with GitHub Enterprise entitlements.',
    ),

    # Domain 3 MS
    'ms_d3_sec_config_enforce': (
        'Create and **Enforce** an Enterprise/Organization **Security Configuration** (setting it as default for newly created repos and manually attaching transferred repos)',
        'Enforced Security Configurations prevent repository admins from disabling mandatory Secret Protection, CodeQL, or Dependabot controls.',
    ),
    'ms_d3_secret_push_validity': (
        'Enable **Secret Scanning Push Protection**, **Partner Validity Checks**, custom regex patterns, and **Delegated Bypass** reviewer groups',
        'Push Protection blocks secrets pre-receive, validity checks highlight live active credentials, and delegated bypass routes false-positive overrides through security reviewers.',
    ),
    'ms_d3_codeql_dependabot_pr': (
        'Enable **CodeQL default/advanced setup**, **Dependabot security updates**, and the **Dependency Review Action** inside required Pull Request Rulesets',
        'Combining CodeQL semantic analysis, Dependabot remediation PRs, and PR-time Dependency Review stops vulnerable code and packages before merge.',
    ),
    'ms_d3_audit_stream_siem': (
        'Configure real-time **Enterprise Audit Log Streaming** (with optional Git events) to encrypted SIEM/WORM storage (`Azure Event Hubs`, `Blob`, `S3`, `Splunk`)',
        'Continuous Audit Log Streaming preserves tamper-evident compliance records far beyond GitHub’s interactive 180-day UI retention window.',
    ),
    'ms_d3_incident_revoke_first': (
        'Immediately **revoke and rotate** leaked credentials at the target cloud/API provider before assuming Git history rewrites reduce exposure',
        'Publicly or internally pushed secrets can be scraped within seconds by bots or clones; credential revocation/rotation is always step #1.',
    ),
    'ms_d3_filter_repo_support_purge': (
        'Scrub sensitive blobs across all refs with **`git filter-repo`**, force-push cleaned branches/tags, and send commit SHAs to **GitHub Support** to purge cached PR views',
        '`git filter-repo` rewrites Git history cleanly, and GitHub Support purges unreachable commit objects and cached Pull Request diffs on GitHub servers.',
    ),
    'ms_d3_fine_grained_pat_policy': (
        'Block or restrict **classic PATs** enterprise-wide while requiring **Organization Owner approval** and max expiration lifetimes (`<=30–90 days`) on **Fine-grained PATs**',
        'Enterprise PAT policies replace broad non-expiring classic tokens with short-lived, repo-scoped, admin-approved Fine-grained PATs.',
    ),
    'ms_d3_github_app_15k_ghec': (
        'Migrate org automation from personal PATs (`5,000 req/hr`) to **GHEC GitHub App installation tokens** (`15,000 REST req/hr`, 1-hour expiry, zero seat cost)',
        'GitHub App installations on GHEC provide 3x higher REST throughput, short-lived 1-hour credentials, and complete decoupling from employee turnover.',
    ),

    # Domain 4 MS
    'ms_d4_internal_reusable_wf': (
        'Host reusable workflows (`workflow_call`) and composite actions in **`Internal`** enterprise repositories with cross-organization workflow `Access` enabled',
        'Enterprise teams reuse vetted CI/CD templates privately across all member organizations without exposing proprietary workflows publicly.',
    ),
    'ms_d4_sha_pin_readonly_token': (
        'Enforce **`Require actions to be pinned to a full-length commit SHA`**, restrict allowed actions to verified/internal sources, and default `GITHUB_TOKEN` to **`Read-only`**',
        '40-char SHA pinning neutralizes upstream tag hijacking while read-only `GITHUB_TOKEN` defaults enforce job-level least privilege.',
    ),
    'ms_d4_runner_group_scoping': (
        'Isolate **Larger** and **ephemeral (`--ephemeral` / `ARC`) self-hosted runners** inside **Runner Groups** restricted to selected repositories and trusted reusable workflows',
        'Runner group repository and workflow restrictions prevent untrusted repos or ad-hoc branches from scheduling jobs onto privileged runners.',
    ),
    'ms_d4_azure_vnet_netconfig': (
        'Connect **Linux/Windows Larger GitHub-hosted runners** to an **Azure VNet** via `GitHub.Network/networkSettings` and Enterprise **Network Configurations**',
        'Azure Private Networking gives managed GitHub-hosted Larger runners private VNet egress to internal endpoints and predictable firewall/NAT egress IPs.',
    ),
    'ms_d4_oidc_vault_env_gate': (
        'Protect production deployments using **Environment Required Reviewers** + **OIDC (`id-token: write`)** federated to **HashiCorp Vault / Azure Key Vault** with strict `sub` claims',
        'Combining protected Deployment Environments with narrow OIDC subject claims (`repo:<org>/<repo>:environment:production`) delivers zero-standing-secret CD security.',
    ),

    # Domain 5 MS
    'ms_d5_api_audit_analytics': (
        'Correlate **Organization API Insights** (`rate-limited callers, top Apps/PATs`) with **Enterprise Audit Log** queries (`hashed_token`, `action:org.*`) to isolate noisy tokens',
        'API Insights pinpoints which App or PAT user is exhausting rate limits while Audit Log `hashed_token` traces exact administrative/API actions.',
    ),
    'ms_d5_dormant_ghas_reclaim': (
        'Suspend/offboard **dormant users**, cancel stale pending org invitations, and audit **90-day active GHAS committers** plus **Copilot Metrics API** active-seat ratios',
        'Proactive seat hygiene reclaims idle Enterprise, Copilot, and GHAS licenses before renewal or monthly metered billing cycles.',
    ),
    'ms_d5_cost_centers_runner_opt': (
        'Assign orgs/repos to **Cost Centers** with **75/90/100% Budget alerts**, add `actions/cache`, shorten artifact `retention-days`, and move Linux workloads off `macos` runners',
        'Cost Centers and Budgets enforce FinOps accountability while caching, shorter artifact retention, and right-sized OS runners cut metered overages.',
    ),
}

TERMS = {**_ATOMIC_TERMS, **SEQUENCES}
