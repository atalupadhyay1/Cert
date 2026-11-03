# Microsoft / GitHub Exam GH-100: GitHub Enterprise Administrator — Full-Length Mock Exam 3

**Theme:** Secure Software Development & App Governance — Enforced Security Configurations, CodeQL/Secret Push Protection, git filter-repo & API Rate Limits  
**Credential:** `GitHub Administration` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `July 2026 (Last updated May 5, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-100 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Enterprise documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Manage GitHub identities and access (15–20% official weight · 19 questions)

### 1. A utility grid operator (`VanguardGrid`) runs **GHEC with Enterprise Managed Users (`EMUs`)** and invites external NERC-CIP penetration testers to three SCADA audit repositories only. Which two EMU controls isolate external testers? Select two.

- **A.** Assign external contractors the IdP **Guest Collaborator** role so they cannot browse `Internal` enterprise repositories unless explicitly granted access
- **B.** Provision user accounts exclusively via your corporate IdP (`SAML`/`OIDC` + `SCIM`), blocking personal public repos, Gists, and external OSS contributions
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **E.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 2. In an **EMU** enterprise (`VanguardGrid`), who owns the managed user accounts (`e.g., priya_vgrid`), and can an EMU account follow external users or star public repositories outside the enterprise (`on github.com`)?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **C.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **D.** Enterprise Managed Users (`EMUs`) provisioned by your corporate IdP (`<handle>_<shortcode>`), isolated from public repo creation, Gists, and external OSS pushes

### 3. On a personal-account **GitHub Enterprise Cloud** organization with **SAML SSO** enabled in permissive (non-enforced) test mode, how does a current Organization Member link their personal GitHub handle to their corporate SAML `NameID`?

- **A.** Enterprise/Organization SAML 2.0 SSO paired with mandatory GitHub `2FA` (with SAML recovery codes stored safely and PAT/SSH credential authorization enforced)
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 4. Which stronger phishing-resistant **`2FA`** factor (`WebAuthn / ____`) should GitHub Enterprise Admins mandate over SMS/TOTP codes where supported?

- **A.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **B.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Enterprise/Organization SAML 2.0 SSO paired with mandatory GitHub `2FA` (with SAML recovery codes stored safely and PAT/SSH credential authorization enforced)

### 5. Grid security architects stand up a greenfield **GHEC with EMUs** tenant federated with PingFederate (`SAML 2.0 + SCIM 2.0`). Which four-step rollout order applies?

- **A.** Invite employees personal GitHub.com accounts → convert personal accounts into EMUs in place → enable SCIM → disable 2FA on the IdP
- **B.** Create EMU enterprise & save recovery codes → configure SAML/OIDC SSO with admin setup user → enable SCIM user/group provisioning in IdP → sync IdP groups to Enterprise/Org teams
- **C.** Sync IdP groups to Enterprise teams → enable SCIM provisioning → configure SAML/OIDC SSO → create the EMU enterprise account last
- **D.** Enable SCIM without configuring SAML/OIDC SSO → share one setup password across engineers → skip recovery codes → assign everyone Enterprise Owner

### 6. An admin on **GHEC with personal accounts** removes departed contractor Sam from the Entra ID group synced via **Team Synchronization** to `@vanguardgrid/substation-firmware`. Proposed solution: Assume removing Sam from that single synced Entra ID group automatically kicks Sam out of the entire `@vanguardgrid` GitHub Organization and revokes all direct collaborator access. Does Team Sync remove Sam from the Organization?

- **A.** No — suspending a dormant GHES user or removing/SCIM-deprovisioning a GHEC member **frees their Enterprise license seat** while **preserving all historical commits, Issues, and Pull Request audit trails**
- **B.** No — on GHEC with personal accounts, IdP **Team Synchronization** only updates Organization team membership for existing org members and **cannot** invite or provision brand-new users into the organization
- **C.** No — **Enterprise teams** (`@/ent:<slug>`) currently do **not** support `CODEOWNERS` assignment, nested child teams, Secret visibility, or Team maintainers; use an **Organization team** for `CODEOWNERS`
- **D.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement

### 7. When an enterprise configures **OIDC SSO** with **Microsoft Entra ID** for **GHEC EMUs**, how many EMU enterprises can link to a **single Entra ID tenant** using the native OIDC integration (`versus SAML`)?

- **A.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** OIDC SSO for Enterprise Managed Users with **Microsoft Entra ID**, automatically enforcing Entra **Conditional Access Policies (`CAP`)** including IP and device compliance

### 8. On self-hosted **GHES** configured with **SAML 2.0** authentication, if you want GHES to automatically suspend users whose corporate directory status becomes inactive without manual `/stafftools` clicks, which mechanism can pair with SAML on GHES?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Supported IdPs (`Microsoft Entra ID`, `Okta`, `PingFederate` with paved-path OIDC/SAML+SCIM for EMUs; or `LDAP`/`CAS`/`SAML` on self-hosted `GHES`)

### 9. An enterprise switches SAML SSO from permissive mode to **Enforced** across `@vanguardgrid-ot`. Which two operational safeguards prevent emergency lockouts and broken CLI pushes? Select two.

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **C.** Download and vault **Enterprise/Org SAML recovery codes** before enforcing SAML SSO so Owners can recover access during an IdP outage
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **E.** Require developers on personal-account GHEC to **authorize** approved Fine-grained/classic PATs and SSH keys for SAML SSO before accessing org repositories

### 10. On an **EMU** enterprise (`where GitHub itself does not hold user passwords; authentication is delegated 100% to the corporate IdP`), do EMU users still have to select `Configure SSO -> Authorize` on newly created PATs and SSH keys the way personal-account GHEC users do?

- **A.** Authentication verifies *who* the caller is (`SAML`/`OIDC`, `2FA`, Passkey, SSH key, PAT), while authorization governs *what* resources they may access (roles, teams, scopes, SAML SSO token authorization)
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO

### 11. NERC-CIP compliance managers need permission to view **Enterprise Security Overview**, manage **Audit Log Streaming**, and view **Enterprise Rulesets** across `VanguardGrid`—with zero ability to delete organizations or alter SAML SSO. Which capability (`Enterprise Settings -> Admins -> ____`) fits?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Custom **Enterprise roles** (such as `Audit Log Reader`, `Billing Viewer`, or `Enterprise Actions Admin`) assigned to individuals or **Enterprise teams** to avoid over-granting `Enterprise Owner`
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges

### 12. In GitHub's five built-in repository role tiers (`Read`, `____`, `Write`, `____`, `Admin`), which two intermediate roles were specifically created so Issue triagers and project release managers do not need `Write` or `Admin`?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** 5 built-in repository roles (`Read`, `Triage`, `Write`, `Maintain`, `Admin`), built-in org roles (`Owner`, `Member`, `Moderator`, `Billing manager`, `Security Manager`), plus GHEC **Custom repository/org roles**

### 13. `VanguardGrid` manages 22 regional grid organizations under one EMU enterprise. Which three practices follow GitHub's multi-org **Enterprise team** and base-permission architecture? Select three.

- **A.** Add **Enterprise teams** across up to 1,000 organizations where org admins can grant additional repo access without removing enterprise-granted permissions
- **B.** Set Organization **`Base permissions = None`** and grant repository access strictly through IdP-synced Teams and least-privilege Custom Repository Roles
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **E.** Sync a single 12,000-member Entra ID group into one Enterprise team alongside 15 manually added contractor accounts
- **F.** Grant **Copilot Business** seats, **custom/predefined enterprise roles**, and **Repository Ruleset bypass** rights directly to **Enterprise teams** (`@/ent:<slug>`)

### 14. An Enterprise Owner manually adds 3 test users to a brand-new **Enterprise team** (`@/ent:scada-ops`) and then wants to map an Entra ID SCIM group to that Enterprise team (`____ manual members required before linking an IdP group`). What must they do first?

- **A.** No — **Enterprise teams** (`@/ent:<slug>`) currently do **not** support `CODEOWNERS` assignment, nested child teams, Secret visibility, or Team maintainers; use an **Organization team** for `CODEOWNERS`
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** **Enterprise teams** (`@/ent:<slug>`, up to 5,000 EMU IdP-synced users across up to 1,000 orgs) for centralized org membership, Copilot seats, custom enterprise roles, and ruleset bypass
- **D.** Sync a single 12,000-member Entra ID group into one Enterprise team alongside 15 manually added contractor accounts

### 15. What are the published scale limits for **Enterprise teams** in a GitHub Enterprise (`up to ____ Enterprise teams per enterprise`, `up to ____ users per Enterprise team`, and `up to ____ organizations assigned per Enterprise team`)?

- **A.** **Enterprise teams** (`@/ent:<slug>`, up to 5,000 EMU IdP-synced users across up to 1,000 orgs) for centralized org membership, Copilot seats, custom enterprise roles, and ruleset bypass
- **B.** Sync a single 12,000-member Entra ID group into one Enterprise team alongside 15 manually added contractor accounts
- **C.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 16. During an access recertification audit, an Organization Owner spots 14 external vendors listed under `People -> ____ collaborators` who still retain direct `Write` access to three substation repositories despite not belonging to any team. Which tab surfaces them?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Exporting enterprise/organization membership & repository permission inventories plus auditing `org.*`, `team.*`, `repo.*`, and token metadata (`hashed_token`, `programmatic_access_type`) in the Audit Log
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 17. Which Enterprise Audit Log event category (`repo.access`, `org.add_member`, `____.add_member`, `role.create`) should compliance analysts monitor to detect privilege escalation across teams and custom roles?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Exporting enterprise/organization membership & repository permission inventories plus auditing `org.*`, `team.*`, `repo.*`, and token metadata (`hashed_token`, `programmatic_access_type`) in the Audit Log

### 18. Who can modify the value of an Organization **Custom Property** (`nerc_cip_tier = high`) on a repository if the Organization Owner leaves `Allow repository actors to set values` **unchecked**?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Repository **Custom Properties** (e.g., `compliance_tier=pci`, `data_class=restricted`) targeted dynamically by Organization/Enterprise **Repository Rulesets** (`most restrictive wins`)
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 19. Repository `vanguardgrid/ems-core` matches **two** active Rulesets: an Enterprise Ruleset requiring **`1` approving review** and an Organization Ruleset requiring **`2` approving reviews + signed commits**. What effective rule applies when merging to `main`?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Enterprise **Member privileges** (`Base permissions = None`, repo creation/forking/visibility locks) combined with **Organization/Enterprise Repository Rulesets** (`Active` vs `Evaluate` dry-run mode)

---

## Domain 2 — Administer GitHub Enterprise environment (10–15% official weight · 14 questions)

### 20. A repository maintainer reports that a sensitive internal hostname (`scada-db01.vgrid.local`) remains visible in a cached orphaned Pull Request diff on **GitHub Enterprise Cloud** even after `git filter-repo` and force-pushing. Who performs the server-side PR cache purge?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Enterprise Admins resolve IdP/SAML lockouts, RBAC grants, runner sizing, and webhook configs; **GitHub Enterprise Support** handles platform outages, cached PR commit purges, and repo restore escalations
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 21. On self-hosted **GHES**, `ghe-storage-usage` alerts that `/data/user` disk utilization hit `88%`. Does **GitHub Support** log in to expand your VMware/AWS EBS virtual disks, or whose responsibility is storage capacity expansion?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **D.** Enterprise Admins resolve IdP/SAML lockouts, RBAC grants, runner sizing, and webhook configs; **GitHub Enterprise Support** handles platform outages, cached PR commit purges, and repo restore escalations

### 22. An air-gapped substation **GHES** appliance experiences Redis queue saturation after a webhook storm. Which four-step support diagnostic escalation sequence applies?

- **A.** Confirm admin-side checks & note exact incident UTC timestamps → SSH/console in and run ghe-support-bundle -x (or Management Console) → review/sanitize sensitive log data if required → upload bundle to GitHub Enterprise Support portal
- **B.** Post raw /data/user/common/secrets.conf in a public GitHub Discussion → tag @github → upgrade three major GHES versions mid-outage → skip support bundle generation
- **C.** Restart all GHES services with ghe-config-apply --force → wipe /data/user/logs to save disk → open a ticket with no timestamps or bundle → grant Support SSH access to internal VPC
- **D.** File a GitHub Support ticket asking GitHub to reset a developer corporate Active Directory password → wait 48 hours → run git gc locally → close ticket

### 23. Which two actions ensure smooth **GHES** troubleshooting during a midnight outage when the sole primary Enterprise Owner is on vacation? Select two.

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Generate an extended diagnostic archive via `ghe-support-bundle -x` (or Management Console `:8443`) and upload it to the **GitHub Enterprise Support** portal
- **C.** Designate up to 20–25 entitled **Support** members (or `Enterprise Support` custom role holders) authorized to open and manage enterprise support tickets
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **E.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 24. Wait—what is the exact difference on GHES between running `ghe-support-bundle` with **no flags** (`standard bundle`) versus passing **`-x`** (`ghe-support-bundle -x` — **extended bundle**) when troubleshooting an incident that happened **14 hours ago**?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Running `ghe-diagnostics` and `ghe-support-bundle -x` via SSH (or GHES Management Console `:8443`) to attach extended logs and cluster telemetry to a GitHub Enterprise Support ticket
- **D.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

### 25. To replace unstructured free-text bug reports with validated dropdowns, required input fields, and automatic Issue labels across `@vanguardgrid`, what format should admins commit inside `.github/ISSUE_TEMPLATE/*.yml`?

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Standardizing **Template repositories**, organization-wide `.github` community health defaults, **`Internal`** InnerSource discovery, and ADR/Issue Form intake across teams
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 26. A firmware repository contains `/drivers/relay/` (`owned by @vanguardgrid/relay-safety`) and `/ui/dashboard/` (`owned by @vanguardgrid/web-ux`). How do you force PRs touching `/drivers/relay/**` to wait for `@vanguardgrid/relay-safety` approval while leaving `/ui/**`-only PRs unblocked by firmware engineers?

- **A.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Enforcing trunk-based **GitHub Flow**, protected `main` with **`CODEOWNERS`**, **Merge Queue** (`gh-readonly-queue`) for busy monorepos, linear squash merges, and immutable signed SemVer **Releases**
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 27. In `.github/CODEOWNERS`, if **both** `* @vanguardgrid/general-devs` on line 1 **and** `/scada/auth/ @vanguardgrid/ot-security` on line 20 match `/scada/auth/token.go`, which team becomes the required Code Owner?

- **A.** Enforcing trunk-based **GitHub Flow**, protected `main` with **`CODEOWNERS`**, **Merge Queue** (`gh-readonly-queue`) for busy monorepos, linear squash merges, and immutable signed SemVer **Releases**
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 28. `VanguardGrid` evaluates hosting corporate IT workloads in a sovereign regional cloud while keeping substation OT repos on a local datacenter **GHES** cluster. Which two deployment facts guide this hybrid architecture? Select two.

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Deploy **GHEC with Data Residency (`<enterprise>.ghe.com`) + EMUs** when regulations require pinning cloud source code and metadata in a specific geographic region (`EU`, `US`, `AU`, `JP`)
- **C.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **D.** Enable **GitHub Connect** license synchronization between `GHES` and `GHEC` (plus link **Visual Studio Subscriptions**) so hybrid users consume a single Enterprise seat
- **E.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 29. On a self-hosted **GHES High Availability (`HA`)** active/passive pair (`configured with ghe-repl-setup and ghe-repl-start`), if the primary datacenter loses power, what single CLI command on the passive replica promotes it to active (`____`) before updating DNS/load-balancer VIPs?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Deploying **GHES High Availability** (`ghe-repl-setup` active/passive failover replica) paired with incremental off-appliance snapshots via **`github/backup-utils`** (`ghe-backup` / `ghe-restore`)
- **C.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **D.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

### 30. In an Enterprise account with **GitHub Copilot Enterprise** (`$39/user/month`) assigned to 120 Principal Engineers and **GitHub Copilot Business** (`$19/user/month`) assigned to 400 Software Engineers across multiple orgs, what happens if one engineer belongs to **two** orgs that both grant Copilot?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Per-user **GitHub Enterprise** seat licensing (deduplicating unique users across orgs + synced `GHES` via **GitHub Connect**, plus linked **Visual Studio Enterprise/Pro with GitHub Enterprise** benefits) alongside metered add-ons
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 31. How are **GitHub Enterprise** user licenses billed for an **Enterprise Owner** who manages enterprise settings and SAML SSO (`Enterprise Settings -> Admins`)?

- **A.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Per-user **GitHub Enterprise** seat licensing (deduplicating unique users across orgs + synced `GHES` via **GitHub Connect**, plus linked **Visual Studio Enterprise/Pro with GitHub Enterprise** benefits) alongside metered add-ons
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 32. Where can an Enterprise Owner download a machine-readable JSON or CSV breakdown showing every consumed Enterprise seat, each user's member organizations, ` GHES` server matches, pending invitations, and Visual Studio license type?

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Inspecting `Enterprise -> Billing & Licensing -> Licensing` (and exported `consumed-licenses` JSON/CSV) to track assigned seats, pending invitations, outside collaborators, VS subscriptions, and `GHES` sync files
- **D.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls

### 33. An Enterprise Admin notices 22 unaccepted **pending organization invitations** sitting for 3 weeks and holding 22 Enterprise license seats while new hires wait for licenses. Proposed solution: Cancel stale pending invitations under `Organization -> People -> Pending invitations` to immediately return all 22 reserved seats to the available pool. Does the solution free those 22 seats immediately?

- **A.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **B.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **C.** No — on GHEC with personal accounts, IdP **Team Synchronization** only updates Organization team membership for existing org members and **cannot** invite or provision brand-new users into the organization
- **D.** No — suspending a dormant GHES user or removing/SCIM-deprovisioning a GHEC member **frees their Enterprise license seat** while **preserving all historical commits, Issues, and Pull Request audit trails**

---

## Domain 3 — Implement secure software development and compliance (25–30% official weight · 29 questions)

### 34. Grid AppSec rolls out an enforced **Enterprise Security Configuration** across 22 organizations so no maintainer can disable `Push protection` or `CodeQL`. Which four-step workflow applies?

- **A.** Ask 400 repository admins to toggle checkboxes manually in every repo → disable Dependency graph → turn off push protection → audit annually by spreadsheet
- **B.** Enable Enforce configuration with every setting left as Not set → expect Not set fields to lock repository admins → delete Organization Security Managers → skip default policy
- **C.** Apply a GHAS Security Configuration with 0 available licenses → assume transferred repos inherit new-repo defaults automatically → disable GitHub Actions on CodeQL repos → leave unenforced
- **D.** Verify available GHAS / Secret Protection / Code Security committers → create custom Security Configuration at Enterprise/Org level → attach to existing & transferred repos plus default for new repos → set policy to Enforce configuration

### 35. Which two capabilities establish tamper-proof secret scanning governance across all repositories in `@vanguardgrid`? Select two.

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Create and **Enforce** an Enterprise/Organization **Security Configuration** (setting it as default for newly created repos and manually attaching transferred repos)
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **E.** Enable **Secret Scanning Push Protection**, **Partner Validity Checks**, custom regex patterns, and **Delegated Bypass** reviewer groups

### 36. A subsidiary transfers 8 substation telemetry repositories from `@vgrid-labs` into `@vgrid-production`, where a custom **Security Configuration** is marked `Default for newly created repositories`. Proposed solution: Do nothing after the repository transfer, expecting `@vgrid-production`'s new-repo default Security Configuration to attach automatically upon transfer. Will the transferred repositories receive `@vgrid-production`'s Security Configuration automatically?

- **A.** No — committing `git rm` (or archiving the repo) leaves the leaked secret intact in prior Git commits and cached PR diffs; you must **revoke/rotate the secret immediately**, run **`git filter-repo`**, force-push, and contact GitHub Support
- **B.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **C.** No — an organization’s default **Security Configuration** auto-attaches only to **newly created** repositories; repositories **transferred** into the organization must have the Security Configuration attached manually or via API
- **D.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret

### 37. Developers occasionally commit massive `400 MB` substation oscilloscope `.pcap` dumps directly into Git instead of Git LFS, bloating clone times. Which **Repository Ruleset** push rule blocks oversized blobs **below** GitHub's hard `100 MB` limit (`e.g., capping regular Git blobs at 10 MB`)?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Configuring **Push Rulesets** to block oversized binaries, forbidden file extensions (`.pem`, `.pfx`, `.key`), restricted file paths (`.github/workflows/**`), and path-traversal commits pre-receive
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 38. To prevent an accidental UI toggle from turning a confidential SCADA repository `Public` on `github.com`, which **Enterprise Repository Management policy** should an Enterprise Owner lock?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Hardening access with **Organization/Enterprise IP allow lists**, **SSH Certificate Authorities (`SSH CAs`)** issuing short-lived developer SSH certs, and least-privilege repo-scoped **Deploy keys**

### 39. When configuring **GitHub Apps** alongside an **Enterprise IP allow list**, how can a SaaS-hosted GitHub App whose webhook/API egress uses fixed published CIDRs interact with your IP-restricted enterprise without opening your whole org IP list to third-party networks manually?

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Hardening access with **Organization/Enterprise IP allow lists**, **SSH Certificate Authorities (`SSH CAs`)** issuing short-lived developer SSH certs, and least-privilege repo-scoped **Deploy keys**
- **D.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step

### 40. NERC-CIP auditors mandate streaming every `VanguardGrid` Enterprise administrative **and** `git.clone`/`git.push` event into Amazon S3 (`Object Lock WORM`) + Splunk SIEM for 5 years. Which four-step setup order applies?

- **A.** Stream audit logs from a single repository Settings tab → expect enterprise-wide SAML and billing events to appear → disable SAML SSO → delete historical SIEM buckets
- **B.** Provision encrypted SIEM/storage sink (Event Hubs, Blob, S3, Splunk) → configure credentials in Enterprise Audit Log Streaming → verify test event & optional Git toggle → set SIEM retention & alerts
- **C.** Enable Git read/clone event streaming to a public unauthenticated HTTP webhook → skip test verification → grant all Organization Members Enterprise Owner to view logs
- **D.** Rely solely on the 180-day web UI audit search for 7-year regulatory retention → skip log streaming → poll REST API every 50 ms until rate-limited → store logs in a public Gist

### 41. Which cloud storage and SIEM destinations are natively supported targets inside **GitHub Enterprise Cloud Audit Log Streaming** (`Enterprise Settings -> Audit log -> Log streaming`)?

- **A.** Streaming the **Enterprise Audit Log** (including optional `git.clone`/`git.fetch`/`git.push` events) in real time to **Azure Event Hubs / Blob Storage, AWS S3, Splunk, Datadog, or GCS**, plus REST/GraphQL queries
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 42. If an attacker or rogue Organization Owner deletes a repository, can that Organization Owner delete or tamper with the `repo.destroy` entry inside the **Enterprise Audit Log** or external **Audit Log Stream**?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Streaming the **Enterprise Audit Log** (including optional `git.clone`/`git.fetch`/`git.push` events) in real time to **Azure Event Hubs / Blob Storage, AWS S3, Splunk, Datadog, or GCS**, plus REST/GraphQL queries
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls

### 43. A utility CISO mandates defense-in-depth AppSec across 140 Go, Python, and C# microservices. Which three controls complete this standard? Select three.

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Enable **CodeQL default/advanced setup**, **Dependabot security updates**, and the **Dependency Review Action** inside required Pull Request Rulesets
- **D.** Create and **Enforce** an Enterprise/Organization **Security Configuration** (setting it as default for newly created repos and manually attaching transferred repos)
- **E.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **F.** Enable **Secret Scanning Push Protection**, **Partner Validity Checks**, custom regex patterns, and **Delegated Bypass** reviewer groups

### 44. Does **GitHub Secret Scanning** scan **only** `.py`/`.json` source code commits on `main`, or can **non-provider / extended secret scanning** also detect leaked passwords inside **GitHub Issues, Pull Request descriptions, PR review comments, and Discussions**?

- **A.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **B.** Defining **Custom Secret Scanning Patterns** (with before/after context expressions and dry-run historical backtesting) at the Organization or Enterprise level to catch internal proprietary token formats
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges

### 45. In **CodeQL code scanning**, what is the difference between the **`Default`** query suite and the **`Security-extended`** (`or Security-and-quality`) query suite?

- **A.** Enabling **CodeQL code scanning** (`Default setup` or custom `Advanced setup` SARIF workflows) plus **Secret scanning** with **Push protection**, **Validity checks**, custom regex patterns, and delegated bypass review
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO

### 46. When `VanguardGrid` enables **Dependabot on GitHub Actions runners** (`Settings -> Code security -> Dependabot -> Run Dependabot on GitHub Actions runners`) paired with VNet-connected Larger runners or `ARC` self-hosted runners, what network advantage does Dependabot gain?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Configuring **Dependabot** with encrypted `dependabot` private-registry secrets (`Settings -> Code security -> Global settings`) and running updates on **Actions runners / ARC** when private VNet access is required

### 47. If an external security researcher discovers a zero-day flaw in an open-source library maintained by `@vanguardgrid-oss`, which repository feature (`Settings -> Code security -> ____`) lets the researcher disclose it privately and lets maintainers collaborate in a hidden temporary fork and request a CVE?

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **C.** Configuring **Dependency graph**, **Dependabot alerts**, **Dependabot security & version updates** (`dependabot.yml` + private registry access), **Dependency Review Action** on PRs, and **Repository Security Advisories**
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 48. Which repository setting (`____ graph`) parses `package-lock.json`, `poetry.lock`, `go.mod`, `pom.xml`, and `.csproj` manifests—and can also ingest runtime SBOMs via the **Dependency Submission API**—as the prerequisite for Dependabot alerts?

- **A.** Configuring **Dependency graph**, **Dependabot alerts**, **Dependabot security & version updates** (`dependabot.yml` + private registry access), **Dependency Review Action** on PRs, and **Repository Security Advisories**
- **B.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 49. An engineer pushes an Azure Service Bus SAS connection string into `vanguardgrid/telemetry-ingest` and opens a PR. Secret scanning alerts fire 10 seconds later. Which two steps form the mandatory remediation? Select two.

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Scrub sensitive blobs across all refs with **`git filter-repo`**, force-push cleaned branches/tags, and send commit SHAs to **GitHub Support** to purge cached PR views
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Immediately **revoke and rotate** leaked credentials at the target cloud/API provider before assuming Git history rewrites reduce exposure
- **E.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

### 50. An engineer commits `scada_root_ca.key`, pushes to `develop`, realizes the mistake, runs `git revert HEAD`, and pushes the revert commit without rotating the CA key or rewriting history. Proposed solution: Rely on `git revert HEAD` to remove `scada_root_ca.key` from repository clones. Does `git revert` purge the private key from Git?

- **A.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **B.** No — committing `git rm` (or archiving the repo) leaves the leaked secret intact in prior Git commits and cached PR diffs; you must **revoke/rotate the secret immediately**, run **`git filter-repo`**, force-push, and contact GitHub Support
- **C.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **D.** No — an organization’s default **Security Configuration** auto-attaches only to **newly created** repositories; repositories **transferred** into the organization must have the Security Configuration attached manually or via API

### 51. On self-hosted **GHES** (unlike cloud GHEC), after a team rewrites repository history with `git filter-repo` and force-pushes, which administrative CLI command (`____ <owner>/<repo>`) can a GHES Site Administrator run directly via SSH port `122` to prune unreachable Git objects and clear caches?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **C.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **D.** Executing the **Security Response Plan**: immediately revoke/rotate leaked secrets, scrub Git refs via **`git filter-repo`**, force-push cleaned history, and ask **GitHub Support** to purge unreachable cached PR/commit views

### 52. Which two token-governance controls eliminate standing organization-wide `repo`-scoped personal credentials across `VanguardGrid`? Select two.

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **C.** Migrate org automation from personal PATs (`5,000 req/hr`) to **GHEC GitHub App installation tokens** (`15,000 REST req/hr`, 1-hour expiry, zero seat cost)
- **D.** Block or restrict **classic PATs** enterprise-wide while requiring **Organization Owner approval** and max expiration lifetimes (`<=30–90 days`) on **Fine-grained PATs**
- **E.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step

### 53. Compare how a **classic PAT** with `repo` scope and a **Fine-grained PAT** scope repository access when a developer belongs to **5** organizations (`Org-A` through `Org-E`).

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Enforcing **Enterprise Fine-Grained PAT Policies**: restricting or blocking **PATs (classic)**, requiring mandatory expiration lifetimes (e.g., <=30–90 days), requiring **Admin approval** before Fine-grained PATs activate, and revoking tokens
- **D.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step

### 54. Where in the **Enterprise Settings** (`Enterprise -> Policies -> Personal access tokens -> ____`) can an Enterprise Owner inspect every active Fine-grained PAT currently granted access across any member organization and revoke compromised tokens centrally?

- **A.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Enforcing **Enterprise Fine-Grained PAT Policies**: restricting or blocking **PATs (classic)**, requiring mandatory expiration lifetimes (e.g., <=30–90 days), requiring **Admin approval** before Fine-grained PATs activate, and revoking tokens
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 55. What happens to your REST API **primary rate limit** quota when you send `GET /repos/vanguardgrid/ems-core/releases/latest` with `If-None-Match: "a8f92..."` and GitHub responds **`HTTP 304 Not Modified`**?

- **A.** REST rate limits: **`5,000 req/hr`** per personal PAT user vs **`15,000 req/hr`** for a **GitHub App installation** (and `GITHUB_TOKEN` per repo) on **GHEC** (`up to 12,500 req/hr` scaled on non-GHEC; GraphQL `5,000` vs `10,000` pts/hr)
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 56. According to GitHub REST API documentation on **Secondary rate limits**, roughly how many **concurrent requests** (`exceeding ~____ concurrent requests`) or rapid content-creating mutations (`creating Issues/comments/PRs in parallel bursts`) risk triggering `403` / `429` secondary throttling?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **C.** Mitigating **Secondary (abuse) rate limits** by capping concurrent API requests, serializing write mutations (`>=1 sec` spacing), using **webhooks / GraphQL / Conditional `ETag` (`304 Not Modified`)**, and honoring `Retry-After`
- **D.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO

### 57. An integration team installs **one single GitHub App** on `@vanguardgrid` (GHEC) and spawns **three** microservices that each mint their own 1-hour installation access token for that **same App installation ID**. Proposed solution: Expect three separate installation tokens from the **same** GitHub App installation on `@vanguardgrid` to give `3 × 15,000 = 45,000 requests/hour`. Does minting extra tokens for the same App installation multiply its `15,000/hr` quota?

- **A.** No — on GHEC with personal accounts, IdP **Team Synchronization** only updates Organization team membership for existing org members and **cannot** invite or provision brand-new users into the organization
- **B.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **C.** No — suspending a dormant GHES user or removing/SCIM-deprovisioning a GHEC member **frees their Enterprise license seat** while **preserving all historical commits, Issues, and Pull Request audit trails**
- **D.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)

### 58. An OT change-management squad replaces a legacy service user's `repo` classic PAT with a least-privilege **GitHub App**. Which four-step implementation sequence applies?

- **A.** Create an OAuth App with full repo scope on the CEO account → hardcode the non-expiring OAuth token in YAML → disable OAuth App restrictions → delete audit logs
- **B.** Register a GitHub App → commit its .pem private key to a public repo → use the 10-minute JWT directly as a REST bearer token for 30 days → keep classic PATs unrestricted
- **C.** Create an org-owned GitHub App with least-privilege permissions → store the App private key in a vault & install on selected repos → generate a short-lived JWT to exchange for a 1-hour installation access token → revoke the legacy classic PAT
- **D.** Create 50 paid machine-user seats → share one classic PAT with admin:org across 50 scripts → turn off 2FA → ignore 5,000 req/hr shared user rate limits

### 59. Which two governance choices harden bot automation and developer CLI tokens simultaneously? Select two.

- **A.** Migrate org automation from personal PATs (`5,000 req/hr`) to **GHEC GitHub App installation tokens** (`15,000 REST req/hr`, 1-hour expiry, zero seat cost)
- **B.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **E.** Block or restrict **classic PATs** enterprise-wide while requiring **Organization Owner approval** and max expiration lifetimes (`<=30–90 days`) on **Fine-grained PATs**

### 60. Why is an **OAuth App** inferior to a **GitHub App** when a tool needs permission **only** to post commit status checks on **one single repository** (`vanguardgrid/grid-sim`)?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** **GitHub Apps** act as independent actors scoped to selected repos + granular permissions using **1-hour installation tokens**, whereas **OAuth Apps** act as the authorizing human user with broad scopes and long-lived tokens
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 61. Can a regular repository Maintainer (`non-Organization Owner`) install a brand-new third-party **GitHub App** onto `vanguardgrid/grid-sim` without Organization Owner review?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Enabling **OAuth App access restrictions** and **GitHub App installation approval workflows** so developer-requested integrations stay blocked on private org data until vetted and approved by an Organization/Enterprise Owner
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 62. In `Organization Settings -> GitHub Apps` (or `Enterprise -> Settings -> GitHub Apps`), how do you designate a DevSecOps lead as an **`App manager`** so they can rotate `.pem` keys and webhook URLs for organization-owned GitHub Apps **without** granting `Organization Owner`?

- **A.** Enabling **OAuth App access restrictions** and **GitHub App installation approval workflows** so developer-requested integrations stay blocked on private org data until vetted and approved by an Organization/Enterprise Owner
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

---

## Domain 4 — Manage GitHub Actions (20–25% official weight · 24 questions)

### 63. `VanguardGrid` centralizes SBOM signing and NERC-CIP compliance workflows for 22 organizations. Which two practices enable secure cross-org sharing? Select two.

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Enforce **`Require actions to be pinned to a full-length commit SHA`**, restrict allowed actions to verified/internal sources, and default `GITHUB_TOKEN` to **`Read-only`**
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **E.** Host reusable workflows (`workflow_call`) and composite actions in **`Internal`** enterprise repositories with cross-organization workflow `Access` enabled

### 64. Up to how many levels of nested **Reusable Workflows** (`A -> B -> C -> D ...`) and total reusable workflow calls per single workflow run does GitHub Actions support (`preventing infinite recursion loops`)?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Sharing reusable workflows (`on: workflow_call`) and composite actions in **`Internal`** or **`Private`** repositories with `Settings -> Actions -> General -> Access` enabled for organization/enterprise workflows

### 65. On **GitHub Enterprise Cloud**, where can platform engineers publish an organization's private custom Docker/JavaScript/Composite Actions so internal developers browse and discover them in a curated **Internal Marketplace / Enterprise Actions catalog** (`without publishing to the public GitHub Marketplace`)?

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Sharing reusable workflows (`on: workflow_call`) and composite actions in **`Internal`** or **`Private`** repositories with `Settings -> Actions -> General -> Access` enabled for organization/enterprise workflows

### 66. Which two enterprise policies harden GitHub Actions against compromised upstream action tags and lateral movement across self-hosted runners? Select two.

- **A.** Enforce **`Require actions to be pinned to a full-length commit SHA`**, restrict allowed actions to verified/internal sources, and default `GITHUB_TOKEN` to **`Read-only`**
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Isolate **Larger** and **ephemeral (`--ephemeral` / `ARC`) self-hosted runners** inside **Runner Groups** restricted to selected repositories and trusted reusable workflows
- **E.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

### 67. Under `Settings -> Actions -> General -> Workflow permissions`, why should **`Allow GitHub Actions to create and approve pull requests`** remain **unchecked** by default in regulated organizations that enforce required PR reviews?

- **A.** Enforcing **Allowed actions and reusable workflows** (`GitHub-created`, `Verified creators`, internal patterns) plus **`Require actions to be pinned to a full-length commit SHA`**, `Read-only` default `GITHUB_TOKEN`, and fork PR approval
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 68. An Enterprise CISO wants to ensure **no** repository in any of the 22 organizations can execute unvetted community Actions, while allowing official `actions/*` from GitHub and internal `vanguardgrid-sec/*` actions pinned to immutable commits. Proposed solution: Set the Enterprise Actions policy to **`Allow select actions and reusable workflows`**, allow GitHub-created actions + `vanguardgrid-sec/*`, and enable **`Require actions to be pinned to a full-length commit SHA`**. Does the solution enforce this across all 22 orgs?

- **A.** No — **Azure Private Networking** (`VNet` integration) and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, NOT on standard free runners or `arm64` macOS Larger runners
- **B.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **C.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret
- **D.** No — an organization’s default **Security Configuration** auto-attaches only to **newly created** repositories; repositories **transferred** into the organization must have the Security Configuration attached manually or via API

### 69. An architecture review board approves a zero-standing-secret production deployment pipeline for `VanguardGrid` hitting internal Azure Kubernetes clusters. Which three controls combine cleanly? Select three.

- **A.** Isolate **Larger** and **ephemeral (`--ephemeral` / `ARC`) self-hosted runners** inside **Runner Groups** restricted to selected repositories and trusted reusable workflows
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Connect **Linux/Windows Larger GitHub-hosted runners** to an **Azure VNet** via `GitHub.Network/networkSettings` and Enterprise **Network Configurations**
- **E.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **F.** Protect production deployments using **Environment Required Reviewers** + **OIDC (`id-token: write`)** federated to **HashiCorp Vault / Azure Key Vault** with strict `sub` claims

### 70. Which GitHub REST API endpoint (`POST /orgs/{org}/actions/runners/generate-____`) mints a single-use, base64-encoded **Just-In-Time (`JIT`)** runner configuration blob so custom VM autoscalers boot clean ephemeral runners with zero persistent registration token on disk?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Provisioning **ephemeral self-hosted runners** (`./config.sh --ephemeral` or REST **JIT runner** configs via **Actions Runner Controller `ARC`**) that execute **exactly one job** and self-destruct cleanly

### 71. In a workflow YAML file, how does a job target a specific **Runner Group** (`ot-linux-runners`) AND custom labels (`[self-hosted, linux, x64, scada]`) explicitly (`runs-on: ____`)?

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Organizing **Enterprise & Organization Runner Groups** restricted to selected repos and workflows, scaling **Larger GitHub-hosted runners** or ephemeral (`--ephemeral`) self-hosted runners via **Actions Runner Controller (`ARC`)** on Kubernetes

### 72. Grid telemetry CI pipelines need **Windows Larger GitHub-hosted runners** to run integration tests against an internal SQL Server Managed Instance (`10.80.12.5`) inside Azure without opening SQL to the internet. Which four-step sequence applies?

- **A.** Delegate Azure VNet subnet to GitHub.Network & create NetworkSettings → create GitHub Network Configuration → attach it to a Linux/Windows Larger runner group → scope runner group to approved repos/workflows
- **B.** Have an Organization Owner create a new Network Configuration while Enterprise policy blocks org configs → skip Azure resource ID linkage → assign to repository secrets → test
- **C.** Whitelist only Microsoft Azure IP ranges on standard Linux hosted runners → skip Azure VNet configuration → disable outbound access to github.com endpoints → run workflows
- **D.** Attach Azure VNet directly to free standard ubuntu-latest runners or macOS arm64 larger runners → skip GitHub.Network subnet delegation → allow all public fork PRs onto the private VNet runner group

### 73. Which two controls govern network isolation when connecting **Larger GitHub-hosted runners** into your corporate **Azure Virtual Network**? Select two.

- **A.** Isolate **Larger** and **ephemeral (`--ephemeral` / `ARC`) self-hosted runners** inside **Runner Groups** restricted to selected repositories and trusted reusable workflows
- **B.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **E.** Connect **Linux/Windows Larger GitHub-hosted runners** to an **Azure VNet** via `GitHub.Network/networkSettings` and Enterprise **Network Configurations**

### 74. When delegating an Azure VNet subnet to **`GitHub.Network/networkSettings`** for GitHub-hosted Larger runners, how does Azure enforce outbound firewalling (`e.g., permitting private 10.80.12.5 SQL access plus required GitHub Actions control-plane endpoints while blocking arbitrary internet egress`)?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Binding **Linux/Windows Larger GitHub-hosted runners** to an **Azure Virtual Network (`VNet`)** via `GitHub.Network/networkSettings` and Enterprise/Org **Network Configurations** (plus proxy vars / IP allow lists for self-hosted runners)
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 75. A self-hosted Linux runner behind a corporate TLS-inspecting proxy (`Zscaler` / `Palo Alto` custom Root CA) fails step `actions/checkout@v4` with `UNABLE_TO_VERIFY_LEAF_SIGNATURE`. Which environment variable (`____=1`) tells the Node.js-based runner to trust certificates installed in the OS system CA store?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 76. What network protocol and direction do self-hosted runners use to receive jobs from GitHub Enterprise Cloud (`inbound ports opened on your firewall, or outbound ____ long-polling on port 443`)?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Inspecting self-hosted runner **`_diag/Runner_*.log`** (registration, listener, network/proxy errors) and **`_diag/Worker_*.log`** (job step execution), `svc.sh status`, tool-cache disk usage, and Actions queue time metrics

### 77. On a Linux self-hosted runner VM, a workflow fails with `permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock`. What host-level configuration is missing (and what security tradeoff does it carry)?

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Inspecting self-hosted runner **`_diag/Runner_*.log`** (registration, listener, network/proxy errors) and **`_diag/Worker_*.log`** (job step execution), `svc.sh status`, tool-cache disk usage, and Actions queue time metrics

### 78. In a **`production` Deployment Environment**, an admin enables **`Prevent self-review`** alongside `Required reviewers: @vanguardgrid/grid-release-leads`. What happens when Alice (a member of `@vanguardgrid/grid-release-leads`) triggers the deployment run herself?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Scoping encrypted secrets across **Organization -> Repository -> Environment** where **most specific wins (`Environment > Repository > Organization`)**, gated by Environment **Required reviewers** and **Deployment branches/rulesets**
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 79. Besides `Required reviewers` and `Custom deployment protection rules`, which built-in **Deployment Environment** protection rule (`____ timer`, `0` to `43,200` minutes / `30` days) enforces a mandatory 60-minute soak window after staging passes before production deploys?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Enforcing **Custom Deployment Protection Rules** (backed by a GitHub App checking ServiceNow change tickets or Datadog SLOs) alongside human Required Reviewers on `production` Environments
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

### 80. A repository defines `API_ENDPOINT = https://dev.vgrid.io` as a **Repository secret** and `API_ENDPOINT = https://prod.vgrid.io` inside the **`production` Environment**. A workflow job runs **without** specifying `environment: production` in YAML. Proposed solution: Assume the job automatically picks up `https://prod.vgrid.io` from the `production` Environment even without `environment: production` on the job. Which value will the job actually receive?

- **A.** No — **Azure Private Networking** (`VNet` integration) and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, NOT on standard free runners or `arm64` macOS Larger runners
- **B.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret
- **C.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **D.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)

### 81. When a fork Pull Request is opened by an untrusted external user against a public repository (`on: pull_request`), does GitHub Actions expose **`secrets.*`** or a write-capable **`GITHUB_TOKEN`** to that fork PR workflow run?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Configuring Organization secrets restricted to **`Selected repositories`** (or `Private and internal`), encrypting REST API secret uploads with the org/repo **LibSodium public key**, and separating non-sensitive **`vars`** from `secrets`
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 82. Which secret naming prefix (`____*`) is strictly reserved by GitHub and rejected if you try to create an Actions secret or variable starting with it?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Configuring Organization secrets restricted to **`Selected repositories`** (or `Private and internal`), encrypting REST API secret uploads with the org/repo **LibSodium public key**, and separating non-sensitive **`vars`** from `secrets`
- **C.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 83. How can a DevSecOps script verify **when** all 85 Repository secrets in `vanguardgrid/ems-core` were last rotated without reading secret values (`GET /repos/vanguardgrid/ems-core/actions/secrets`)?

- **A.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Configuring Organization secrets restricted to **`Selected repositories`** (or `Private and internal`), encrypting REST API secret uploads with the org/repo **LibSodium public key**, and separating non-sensitive **`vars`** from `secrets`

### 84. `VanguardGrid` replaces static AWS IAM access keys across 60 Terraform repositories with **GitHub Actions OIDC** federation (`aws-actions/configure-aws-credentials@v4`). Which four-step sequence applies?

- **A.** Export static cloud admin keys into a public repository → commit .env to main → skip OIDC subject claim validation → rotate keys every 5 years
- **B.** Configure OIDC trust policy in Vault/Azure/AWS with strict sub/aud claims → set job permissions id-token: write → exchange OIDC JWT at runtime for dynamic secret → delete static GitHub secrets
- **C.** Request an OIDC JWT first without configuring any Federated Identity Credential in Azure/Vault → hardcode client secrets when OIDC fails → grant write-all to fork PRs
- **D.** Trust wildcard sub: repo:* in AWS/Vault with no org filter → leave id-token: none in workflow YAML → store root Vault token in plain-text Actions vars → echo token in logs

### 85. In an AWS IAM OIDC trust policy for `token.actions.githubusercontent.com`, what is the standard expected **`aud`** (`audience`) claim (`sts.amazonaws.com` when using `aws-actions/configure-aws-credentials`), and why must `StringEquals` check **both** `aud` and `sub`?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Federating GitHub Actions (`permissions: id-token: write`) via **OpenID Connect (`OIDC`)** with **HashiCorp Vault**, **Azure Key Vault**, or **AWS Secrets Manager** using strict `sub` (`repo:`/`environment:`) and `aud` claims
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

### 86. An iOS mobile field-crew lead at `VanguardGrid` asks whether **`macos-15` (`arm64` Apple Silicon) Larger GitHub-hosted runners** support **Azure Private Networking (`VNet`)** so Xcode jobs can talk over private IP `10.12.0.9` to an internal CocoaPods mirror. Proposed solution: Attach an Enterprise Azure VNet Network Configuration to an `arm64` macOS Larger runner group. Does GitHub support this?

- **A.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret
- **B.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **C.** No — committing `git rm` (or archiving the repo) leaves the leaked secret intact in prior Git commits and cached PR diffs; you must **revoke/rotate the secret immediately**, run **`git filter-repo`**, force-push, and contact GitHub Support
- **D.** No — **Azure Private Networking** (`VNet` integration) and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, NOT on standard free runners or `arm64` macOS Larger runners

---

## Domain 5 — Monitor and optimize GitHub usage (10–15% official weight · 14 questions)

### 87. Grid SOC analysts want to trace every REST mutation back to its exact token fingerprint and alert in Microsoft Sentinel within 60 seconds whenever an admin modifies a Repository Ruleset. Which two capabilities meet this requirement? Select two.

- **A.** Correlate **Organization API Insights** (`rate-limited callers, top Apps/PATs`) with **Enterprise Audit Log** queries (`hashed_token`, `action:org.*`) to isolate noisy tokens
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Configure real-time **Enterprise Audit Log Streaming** (with optional Git events) to encrypted SIEM/WORM storage (`Azure Event Hubs`, `Blob`, `S3`, `Splunk`)
- **E.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 88. In **Organization API Insights** (`Time period: Last 24h / 7d / 30d / 90d`), if you drill into a specific noisy **GitHub App** actor, which route-level details are shown to pinpoint the offending microservice endpoint?

- **A.** Querying the **Enterprise Audit Log** (`action:`, `actor:`, `hashed_token:`) and **Organization API Insights** (`time-series requests, rate-limited callers, top GitHub Apps, OAuth Apps, and PATs`) to pinpoint noisy/failing integrations
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 89. When exporting audit events directly from the **Enterprise Audit Log UI**, which two file formats (`____` and `____`) does GitHub offer for offline forensic analysis (`up to 100,000 events per export, or unlimited via Audit Log Streaming`)?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Querying the **Enterprise Audit Log** (`action:`, `actor:`, `hashed_token:`) and **Organization API Insights** (`time-series requests, rate-limited callers, top GitHub Apps, OAuth Apps, and PATs`) to pinpoint noisy/failing integrations
- **D.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO

### 90. On self-hosted **GHES**, modern observability teams want Grafana + Prometheus to scrape CPU, memory, queue depth, Git performance, and cluster health metrics directly over HTTPS rather than legacy SNMPv2/v3. Which built-in GHES feature supports this?

- **A.** Scraping **GHES Prometheus `/metrics`** (or forwarding `syslog` + `SNMP` health traps) to alert platform SREs proactively on disk IOPS saturation, Redis/MySQL replication lag, and CPU load
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 91. When generating a **GHES** support bundle from the CLI over SSH port `122` on an appliance that **does** have outbound HTTPS access to `support.github.com`, which command (`ghe-support-bundle -x | ____ -t <ticket_id>` or `ghe-support-upload`) uploads the bundle straight to your open Support ticket without downloading a `2 GB` file to your laptop?

- **A.** Using GHES **Management Console / Grafana / `ghe-diagnostics` / Activity Dashboard** (or `githubstatus.com` + Enterprise Support portal with `Support Admin` entitlement on GHEC) to separate local misconfiguration from platform incidents
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 92. A self-hosted **GHES** webhook targeting an internal Jenkins controller (`https://jenkins.vgrid.internal:8443/github-webhook/`) fails with `Peer certificate cannot be authenticated with given CA certificates`. Is this a GitHub Support bug or an internal GHES Admin task?

- **A.** Using GHES **Management Console / Grafana / `ghe-diagnostics` / Activity Dashboard** (or `githubstatus.com` + Enterprise Support portal with `Support Admin` entitlement on GHEC) to separate local misconfiguration from platform incidents
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 93. Across `VanguardGrid`'s 22 organizations, leadership notices 190 repositories have had **zero commits, Issues, or Pull Requests in 24 months** yet still trigger weekly scheduled `cron:` Actions workflows (`consuming 14,000 Linux minutes/month`). What administrative action stops wasted CI runs while preserving full read-only history?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Evaluating **Copilot Metrics API / Usage Dashboard** (active vs assigned seats, IDE/Chat/PR adoption), **Security Overview** coverage/MTTR, **Actions Usage Metrics**, and **GHES Dormant Users** reports to find underutilized features
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 94. Why does the **GitHub Copilot Metrics API** (`/enterprises/{enterprise}/copilot/metrics`) omit daily breakdown metrics for an Enterprise team that has only **3** active Copilot users on a given day?

- **A.** Querying the **GitHub Copilot User Management & Metrics REST APIs** (`last_activity_at`, `last_activity_editor`, acceptance/chat telemetry) to automate seat reclamation for inactive assignees
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO

### 95. At the repository level, which built-in tab (`____ -> Pulse / Contributors / Traffic / Dependency graph`) lets maintainers inspect 14-day `git clone` counts, unique visitors, and PR merge velocity?

- **A.** Evaluating **Copilot Metrics API / Usage Dashboard** (active vs assigned seats, IDE/Chat/PR adoption), **Security Overview** coverage/MTTR, **Actions Usage Metrics**, and **GHES Dormant Users** reports to find underutilized features
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 96. Which two practices let `VanguardGrid`'s FinOps controller charge back metered GitHub spend accurately to `Transmission`, `Distribution`, and `Renewables` business units while curbing waste? Select two.

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Assign orgs/repos to **Cost Centers** with **75/90/100% Budget alerts**, add `actions/cache`, shorten artifact `retention-days`, and move Linux workloads off `macos` runners
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **E.** Suspend/offboard **dormant users**, cancel stale pending org invitations, and audit **90-day active GHAS committers** plus **Copilot Metrics API** active-seat ratios

### 97. Developer Omar pushed commits during the last 90 days to **14 different private repositories** across **3 organizations** inside `VanguardGrid`—all 14 repositories have **GitHub Advanced Security (`GHAS`)** enabled. How many **GHAS committer seats** does Omar consume?

- **A.** Understanding that **GitHub Advanced Security (`GHAS`)** bills per **unique active committer** over a rolling **90-day** window across enabled private/internal repos (free on public repos!)
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 98. In an Enterprise **Usage Report CSV** (`Billing & Licensing -> Usage -> Get usage report`), which columns let FinOps scripts aggregate metered spend by department (`product`, `sku`, `quantity`, `unit_type`, `____`, `organization`, `repository`)?

- **A.** Analyzing **Enhanced Billing Platform** usage exports, **Cost Centers**, **Budgets & 75/90/100% alerts**, OS runner minute multipliers (`Linux < Windows < macOS`), shared **Actions/Packages storage**, and **90-day unique GHAS committers**
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges

### 99. Quarterly FinOps telemetry shows `VanguardGrid`'s Enterprise seats at `99%` capacity and Actions spend `35%` over forecast. Which four-step optimization workflow applies?

- **A.** Hard-delete departing employees personal GitHub accounts via Support → break PR review audit history → turn off Dependabot and CodeQL everywhere → cancel Enterprise support
- **B.** Delete historical employee Git commits to free GHAS seats immediately → disable GitHub Connect so GHEC+GHES users are billed twice → set unlimited Actions spending limits → skip budgets
- **C.** Export consumed-licenses & verify GitHub Connect GHES sync → audit dormant users, duplicate emails, and 90-day GHAS committers → reclaim idle seats & right-size budgets → enforce SCIM offboarding & alerts
- **D.** Assign every contractor Enterprise Owner and Copilot Enterprise on day one → run Linux CI jobs on 10x-multiplier macOS runners → store 500 GB build artifacts for 400 days → review bills annually

### 100. A Python monorepo runs 400 CI jobs/day that each spend **4 minutes** downloading `1.2 GB` of unchanged `pip` wheels and `npm` tarballs on `ubuntu-latest` (`1,600 wasted minutes/day`). Which official GitHub Action (`actions/____@v4` — or built-in `setup-python`/`setup-node` `cache:` input) cuts dependency install time to 12 seconds?

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Reclaiming **dormant GHES/GHEC seats** & stale pending invitations, enabling **GitHub Connect** license deduplication, caching dependencies (`actions/cache`), shortening artifact retention days, and right-sizing `ubuntu` vs `macos` runners
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

---

## Answer Key and Explanations

### Question 1 — `A, B` (Manage GitHub identities and access)

Correct answers: A and B (are correct). IdP-governed **EMUs** disable public repos/Gists and external collaboration, while assigning external testers the **Guest Collaborator** IdP role hides company-wide `Internal` repositories. [Skill 1.1: Describe differences between managed users and personal accounts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: About Enterprise Managed Users vs personal accounts (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users)]

- **A:** Correct. Guest Collaborators prevent contractors in EMU enterprises from automatically reading all `Internal` repositories across member organizations.
- **B:** Correct. EMUs ensure corporate lifecycle control and eliminate accidental public repo or Gist leakage under managed handles.
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **E:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 2 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). The **Enterprise** owns every EMU account via its IdP; while EMUs can view public `github.com` pages if network policy permits, they **cannot** push, open Issues/PRs, fork, or create content outside their enterprise! [Skill 1.1: Describe differences between managed users and personal accounts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: About Enterprise Managed Users vs personal accounts (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **C:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **D:** Correct. EMUs give enterprises full lifecycle ownership over user accounts via SAML/OIDC + SCIM while preventing public code/Gist creation and external repository contributions.

### Question 3 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). Each member visits the organization's SSO URL (`https://github.com/orgs/<org>/sso`), authenticates through the corporate IdP, and links an active SAML session + `NameID` record! [Skill 1.2: Configure and enforce SAML SSO and 2FA | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing SAML single sign-on and two-factor authentication (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise)]

- **A:** Correct. Enforcing SAML SSO at the Enterprise level centralizes IdP authentication across all member organizations, requires credential authorization for PATs/SSH keys, and pairs with `2FA` on personal-account GHEC.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 4 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Hardware **FIDO2 / WebAuthn security keys** or platform **passkeys** prevent real-time phishing proxy attacks against developer and administrator accounts! [Skill 1.2: Configure and enforce SAML SSO and 2FA | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing SAML single sign-on and two-factor authentication (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise)]

- **A:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **B:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. Enforcing SAML SSO at the Enterprise level centralizes IdP authentication across all member organizations, requires credential authorization for PATs/SSH keys, and pairs with `2FA` on personal-account GHEC.

### Question 5 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). Provision the EMU enterprise and vault recovery codes for `<shortcode>_admin`, configure SAML SSO using the setup user, enable SCIM 2.0 user/group provisioning in PingFederate, and map IdP groups to teams. [Skill 1.3: Understand SCIM and team synchronization: implementation and key differences | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring SCIM provisioning vs IdP team synchronization (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim/provisioning-users-and-groups-with-scim-using-the-rest-api)]

- **A:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMU accounts; EMUs are brand-new IdP-provisioned accounts.
- **B:** Correct. Correct order: establish the EMU enterprise and offline recovery codes, wire SAML/OIDC SSO using the initial setup user, turn on SCIM user/group provisioning, and map IdP groups to teams.
- **C:** Incorrect. Reverses prerequisite dependencies: SCIM and IdP group synchronization cannot run before the EMU enterprise exists and SAML/OIDC SSO is configured.
- **D:** Incorrect. SCIM on EMUs requires SAML or OIDC SSO first, and sharing setup credentials or granting universal Enterprise Owner violates least privilege.

### Question 6 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). No — on personal-account GHEC, **Team Synchronization** only removes Sam from that mapped **Organization team** (`@vanguardgrid/substation-firmware`); you must remove Sam from the **Organization** (or revoke SAML/SCIM identity) to terminate org membership! [Skill 1.3: Understand SCIM and team synchronization: implementation and key differences | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring SCIM provisioning vs IdP team synchronization (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim/provisioning-users-and-groups-with-scim-using-the-rest-api)]

- **A:** Incorrect. Offboarding or suspending inactive accounts reclaims per-user licenses cleanly without breaking repository Git history or compliance review logs.
- **B:** Correct. Personal-account Team Sync (`Entra ID`/`Okta`) never adds non-members into an organization; users must join the org via SAML/SCIM invitation first (or deploy GHEC with EMUs).
- **C:** Incorrect. While Enterprise teams excel at cross-org access, Copilot licensing, custom enterprise roles, and ruleset bypasses, `CODEOWNERS` requires Organization teams or individual users with Write+ access.
- **D:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — on personal-account GHEC, **Team Synchronization** only removes Sam from that mapped **Organization team** (`@vanguardgrid/substation-firmware`); you must remove Sam from the **Organization** (or revoke SAML/SCIM identity) to terminate org membership!

### Question 7 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Keep architectural tenant limits in mind: Entra ID **OIDC** paved-path binds cleanly to your tenant with automatic **Conditional Access Policy (`CAP`)** evaluation (`whereas multiple EMU enterprises in one Entra tenant typically use separate SAML enterprise gallery apps`)! [Skill 1.4: Choose and configure identity providers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Choosing and configuring Identity Providers (Entra ID, Okta, PingFederate, CAS/LDAP) (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-identity-and-access-management)]

- **A:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Correct. Configuring OIDC between Entra ID and GHEC EMUs validates Entra Conditional Access Policies during browser sign-in and token refresh Flows.

### Question 8 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Use **GHES SAML attribute/SCIM or LDAP sync** (or automated REST `PUT /users/{username}/suspended` offboarding hooks driven by your IdP lifecycle workflow) to suspend deactivated users promptly! [Skill 1.4: Choose and configure identity providers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Choosing and configuring Identity Providers (Entra ID, Okta, PingFederate, CAS/LDAP) (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-identity-and-access-management)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Correct. GHEC EMUs support Entra ID (OIDC or SAML), Okta, and PingFederate (plus custom SAML+SCIM API integration), while GHES adds native LDAP, Active Directory, and CAS authentication.

### Question 9 — `C, E` (Manage GitHub identities and access)

Correct answers: C and E (are correct). Download and vault **Enterprise/Org SAML recovery codes** beforehand, and ensure developers **authorize** their SSH keys and PATs (`Configure SSO`) for `@vanguardgrid-ot`. [Skill 1.5: Explain GitHub’s authentication and authorization model | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub authentication and authorization model (SSH, PAT, OAuth, SAML, OIDC) (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **C:** Correct. Storing SAML recovery codes offline prevents total administrative lockout if the corporate Identity Provider experiences a certificate or service outage.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **E:** Correct. SAML enforcement blocks un-authorized programmatic credentials (PATs and SSH keys) even when owned by valid organization members.

### Question 10 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). Note the subtle admin distinction: even on EMUs where SSO governs identity, if **Entra ID OIDC Conditional Access (`CAP`) IP validation** or **PAT approval policy** is active, tokens remain subject to enterprise PAT/IP authorization policies! [Skill 1.5: Explain GitHub’s authentication and authorization model | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub authentication and authorization model (SSH, PAT, OAuth, SAML, OIDC) (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)]

- **A:** Correct. Even a valid personal PAT or SSH key (`authenticated`) is blocked from accessing a SAML-enforced GHEC organization until explicitly **authorized** for SAML SSO (`authorized`).
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.

### Question 11 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). Define a **Custom enterprise role** combining only granular audit, ruleset-read, and security-overview permissions, then assign it to the compliance **Enterprise team**! [Skill 1.6: Configure organization and repository roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization roles, custom roles, and repository roles (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-organization-roles)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Correct. Custom enterprise roles delegate narrow slices of enterprise administration without exposing full owner control over SAML, billing, or organization deletion.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.

### Question 12 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). **`Triage`** (manage Issues/PRs/labels without pushing code) and **`Maintain`** (manage repository settings, branches, and releases without destructive `Admin` actions like deleting the repo or managing access)! [Skill 1.6: Configure organization and repository roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization roles, custom roles, and repository roles (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-organization-roles)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. GitHub layers additive repository roles (`most permissive wins`) with least-privilege built-in and custom organization/enterprise roles.

### Question 13 — `A, B, F` (Manage GitHub identities and access)

Correct answers: A, B, and F (are correct). Bind **Enterprise teams** to Copilot seats, custom enterprise roles, and ruleset bypasses; assign Enterprise teams across up to 1,000 orgs; and enforce **`Base permissions = None`** on every organization. [Skill 1.7: Define and manage enterprise teams | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining and managing Enterprise teams across organizations (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise)]

- **A:** Correct. Enterprise team organization assignments add members directly without invitations and protect enterprise-granted baseline access from org-level removal.
- **B:** Correct. Setting Base permissions to `None` prevents newly added org members from automatically reading or writing every private repository in the organization.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **E:** Incorrect. IdP-synced Enterprise teams require zero manually added members and pause synchronization whenever the linked IdP group exceeds 5,000 users.
- **F:** Correct. Enterprise teams streamline multi-org role delegation, enterprise-level Copilot seat assignment, and ruleset bypass administration.

### Question 14 — `C` (Manage GitHub identities and access)

Correct answer: C (is correct). Remove all **manual members** (`0` direct members) before binding an IdP group—an Enterprise team cannot mix manual members and IdP-synced group members simultaneously! [Skill 1.7: Define and manage enterprise teams | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining and managing Enterprise teams across organizations (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise)]

- **A:** Incorrect. While Enterprise teams excel at cross-org access, Copilot licensing, custom enterprise roles, and ruleset bypasses, `CODEOWNERS` requires Organization teams or individual users with Write+ access.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. Enterprise teams simplify multi-org governance, Copilot licensing, custom enterprise role delegation, and ruleset bypasses—though they do not support `CODEOWNERS`, nesting, Secret visibility, or non-EMU Team Sync.
- **D:** Incorrect. IdP-synced Enterprise teams require zero manually added members and pause synchronization whenever the linked IdP group exceeds 5,000 users.

### Question 15 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). Up to **`2,500`** Enterprise teams per enterprise, **`5,000`** users per Enterprise team, and **`1,000`** organizations assigned per Enterprise team! [Skill 1.7: Define and manage enterprise teams | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining and managing Enterprise teams across organizations (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise)]

- **A:** Correct. Enterprise teams simplify multi-org governance, Copilot licensing, custom enterprise role delegation, and ruleset bypasses—though they do not support `CODEOWNERS`, nesting, Secret visibility, or non-EMU Team Sync.
- **B:** Incorrect. IdP-synced Enterprise teams require zero manually added members and pause synchronization whenever the linked IdP group exceeds 5,000 users.
- **C:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 16 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). The **`Outside collaborators`** view (`Organization -> People -> Outside collaborators`) lists every non-member holding direct access to one or more organization repositories! [Skill 1.8: Audit access and permissions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Auditing repository, organization, and enterprise access permissions (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/identifying-audit-log-events-performed-by-an-access-token)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Correct. Admins audit effective access via People exports, repository Manage Access filters, REST/GraphQL permission queries, and Audit Log token attribution fields.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 17 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Filtering `team.*`, `org.*`, `repo.*`, and `role.*` events in the **Enterprise Audit Log** (alongside periodic `People -> Export` snapshots) surfaces every membership and role elevation! [Skill 1.8: Audit access and permissions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Auditing repository, organization, and enterprise access permissions (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/identifying-audit-log-events-performed-by-an-access-token)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. Admins audit effective access via People exports, repository Manage Access filters, REST/GraphQL permission queries, and Audit Log token attribution fields.

### Question 18 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). Only **Organization Owners** (or actors granted the `Edit custom property values` custom organization permission) can set or change that Custom Property—preventing repository admins from downgrading `nerc_cip_tier` to escape Rulesets! [Skill 1.9: Manage settings, policies, rulesets, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing enterprise member privileges, policies, repository rulesets, and bypass roles (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Correct. Organization and Enterprise admins enforce schema-validated Custom Properties on repos and bind Rulesets to property queries (`compliance_tier:pci`) automatically.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 19 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Because GitHub evaluates overlapping Rulesets by **layering (`most restrictive wins`)**, merges into `main` require **`2` approving reviews AND signed commits**! [Skill 1.9: Manage settings, policies, rulesets, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing enterprise member privileges, policies, repository rulesets, and bypass roles (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. Enterprise policies set hard guardrails across all organizations, while Repository Rulesets layer additive branch/tag/push protections (`most restrictive wins`) with auditable bypasses.

### Question 20 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). Open a ticket with **GitHub Enterprise Support** supplying the repository URL, Pull Request number, and exact unreachable commit SHAs—only GitHub Support can purge cached unreachable commit views on GHEC! [Skill 2.1: Identify issues resolvable by admins vs GitHub Support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Identifying issues resolvable by Enterprise Admins vs GitHub Enterprise Support (https://docs.github.com/en/enterprise-cloud@latest/support/learning-about-github-support/about-github-support)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Correct. Admins handle internal identity, permissions, and pipeline configs, while GitHub Support handles cloud infrastructure incidents, server-side cache purges, and backend appliance/cloud escalations.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 21 — `D` (Administer GitHub Enterprise environment)

Correct answer: D (is correct). Your internal **GHES Infrastructure / Platform Administrator** provisions hypervisor/cloud block storage and runs GHES storage expansion (`in maintenance mode`)—GitHub Support never administers customer hypervisors or SSHes into GHES! [Skill 2.1: Identify issues resolvable by admins vs GitHub Support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Identifying issues resolvable by Enterprise Admins vs GitHub Enterprise Support (https://docs.github.com/en/enterprise-cloud@latest/support/learning-about-github-support/about-github-support)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **D:** Correct. Admins handle internal identity, permissions, and pipeline configs, while GitHub Support handles cloud infrastructure incidents, server-side cache purges, and backend appliance/cloud escalations.

### Question 22 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). Run local admin triage (`ghe-diagnostics`) and note exact UTC timestamps, generate an extended bundle with `ghe-support-bundle -x`, sanitize sensitive hostnames if required by NERC-CIP policy, and upload the `.tgz` bundle to the GitHub Enterprise Support portal. [Skill 2.2: Generate support bundles and diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Generating GHES support bundles, ghe-diagnostics, and ticket diagnostics (https://docs.github.com/en/enterprise-server@latest/support/contacting-github-support/providing-data-to-github-support)]

- **A:** Correct. Correct escalation workflow: verify local admin triage and timestamps, generate an extended support bundle (`ghe-support-bundle -x`), verify compliance hygiene, and attach it on the Support portal.
- **B:** Incorrect. Never expose appliance secrets publicly or perform multi-version upgrades mid-incident without diagnostics.
- **C:** Incorrect. Wiping logs destroys root-cause evidence before capturing a support bundle, and GitHub Support never SSHes directly into customer GHES appliances.
- **D:** Incorrect. Corporate IdP/Active Directory password resets are strictly an internal administrator responsibility, not a GitHub Support issue.

### Question 23 — `B, C` (Administer GitHub Enterprise environment)

Correct answers: B and C (are correct). Designate multiple SREs as entitled **Support** portal members in Enterprise Settings, and document generating extended `24h+` logs via **`ghe-support-bundle -x`** (`rather than standard -b` `1h–8h` window). [Skill 2.2: Generate support bundles and diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Generating GHES support bundles, ghe-diagnostics, and ticket diagnostics (https://docs.github.com/en/enterprise-server@latest/support/contacting-github-support/providing-data-to-github-support)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Correct. Extended support bundles give GitHub Support complete service, cluster, and error telemetry without exposing your appliance to external SSH.
- **C:** Correct. Enterprise Owners explicitly grant support-portal entitlement to designated engineers rather than sharing a single Enterprise Owner login.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **E:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 24 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). A standard bundle captures recent current logs, whereas **`-x` (`extended bundle`)** includes older rotated log archives (`typically up to 7–8 days of historical logs`) needed when the outage occurred hours or days earlier! [Skill 2.3: Recommend standards for developer processes | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending enterprise standards for developer collaboration and InnerSource (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-best-practices/organize-work)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Correct. On GHES, `ghe-support-bundle -x` packages sanitized system, service, and recent diagnostic logs over an extended window so GitHub Support can diagnose appliance issues rapidly.
- **D:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 25 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). Use YAML **Issue Forms** (`.github/ISSUE_TEMPLATE/bug_report.yml`), which render structured schema-validated inputs (`dropdown`, `input`, `textarea`, `checkboxes`) on web Issue creation! [Skill 2.3: Recommend standards for developer processes | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending enterprise standards for developer collaboration and InnerSource (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-best-practices/organize-work)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Correct. Enterprise developer standards combine golden template repositories, an org `.github` repo for default templates/policies, and `Internal` InnerSource visibility.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 26 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). Define path-based ownership entries in **`.github/CODEOWNERS`** (`/drivers/relay/ @vanguardgrid/relay-safety`) and enable **`Require review from Code Owners`** in your `main` Repository Ruleset! [Skill 2.4: Define standards for workflows, branching, reviews, and releases | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining standards for workflows, branching, CODEOWNERS reviews, merge queues, and releases (https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)]

- **A:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Correct. Standardizing short-lived branches, Code Owner reviews, Merge Queue CI batching, and protected `v*` release tags keeps enterprise delivery predictable and auditable.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 27 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). Like `.gitignore`, **the last matching pattern wins** in `CODEOWNERS` (`order goes general -> specific`), so line 20 (`@vanguardgrid/ot-security`) governs `/scada/auth/token.go`! [Skill 2.4: Define standards for workflows, branching, reviews, and releases | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining standards for workflows, branching, CODEOWNERS reviews, merge queues, and releases (https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)]

- **A:** Correct. Standardizing short-lived branches, Code Owner reviews, Merge Queue CI batching, and protected `v*` release tags keeps enterprise delivery predictable and auditable.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 28 — `B, D` (Administer GitHub Enterprise environment)

Correct answers: B and D (are correct). **GHEC with Data Residency (`<enterprise>.ghe.com`)** stores cloud assets in your chosen region and requires **EMUs**, while **GitHub Connect** unifies user license deduplication across `GHEC` and `GHES`. [Skill 2.5: Describe GitHub Enterprise deployment scenarios (GHEC with EMU, GHEC with Data Residency + EMU, GHEC with personal accounts, GHES) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise deployment models (GHEC+EMU, GHEC Data Residency ghe.com, GHEC personal, GHES) (https://docs.github.com/en/enterprise-cloud@latest/admin/overview/about-github-for-enterprises)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Correct. GHEC with Data Residency hosts code and metadata on a dedicated regional `.ghe.com` cloud stamp and always requires Enterprise Managed Users.
- **C:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **D:** Correct. GitHub Connect correlates verified email addresses across GHES and GHEC and reconciles Visual Studio Enterprise/Pro with GitHub Enterprise entitlements.
- **E:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 29 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). Running **`ghe-repl-promote`** on the healthy passive replica stops replication and promotes the replica appliance into the writable active primary! [Skill 2.5: Describe GitHub Enterprise deployment scenarios (GHEC with EMU, GHEC with Data Residency + EMU, GHEC with personal accounts, GHES) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise deployment models (GHEC+EMU, GHEC Data Residency ghe.com, GHEC personal, GHES) (https://docs.github.com/en/enterprise-cloud@latest/admin/overview/about-github-for-enterprises)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Correct. HA replication protects against primary VM hardware failure, while scheduled `backup-utils` snapshots on a separate host provide point-in-time disaster recovery.
- **C:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **D:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 30 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). Within the same Enterprise account, GitHub **deduplicates** Copilot seat billing per unique user (`charging only once per user across member organizations at the highest assigned tier`)! [Skill 2.6: Explain licensing and billing models | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise licensing, metered user-based billing, and Visual Studio subscriptions (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/about-per-user-pricing)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Correct. One Enterprise user consumes a single seat across unlimited organizations in the enterprise (and synced GHES instances via GitHub Connect), while Actions, Packages, Codespaces, GHAS, and Copilot meter separately.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 31 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). **Enterprise Owners** consume **1** GitHub Enterprise user license seat (`unlike standalone Billing Managers who hold zero org/owner access`). [Skill 2.6: Explain licensing and billing models | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise licensing, metered user-based billing, and Visual Studio subscriptions (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/about-per-user-pricing)]

- **A:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Correct. One Enterprise user consumes a single seat across unlimited organizations in the enterprise (and synced GHES instances via GitHub Connect), while Actions, Packages, Codespaces, GHAS, and Copilot meter separately.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 32 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). Navigate to `Enterprise -> Billing & Licensing -> Licensing` and select **`Export license usage`** (`CSV` / `JSON` — or query the Enterprise Consumed Licenses REST API)! [Skill 2.7: Monitor license usage and consumption | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring enterprise license consumption and GitHub Connect license sync (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/viewing-license-usage-for-github-enterprise)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. Pending org invitations, outside collaborators on private repos, enterprise members, and unsynced duplicate emails across GHES/GHEC all impact Enterprise license counts and must be audited regularly.
- **D:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.

### Question 33 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). Yes — canceling pending organization invitations immediately releases the reserved GitHub Enterprise seats back into your available pool! [Skill 2.7: Monitor license usage and consumption | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring enterprise license consumption and GitHub Connect license sync (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/viewing-license-usage-for-github-enterprise)]

- **A:** Correct. Every technical requirement, permission boundary, and GitHub Enterprise platform rule in the scenario is satisfied cleanly.
- **B:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **C:** Incorrect. Personal-account Team Sync (`Entra ID`/`Okta`) never adds non-members into an organization; users must join the org via SAML/SCIM invitation first (or deploy GHEC with EMUs).
- **D:** Incorrect. Offboarding or suspending inactive accounts reclaims per-user licenses cleanly without breaking repository Git history or compliance review logs.

### Question 34 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Verify available GHAS/Secret Protection/Code Security committer seats, author the custom Enterprise Security Configuration, apply it to existing/transferred repos plus new-repo defaults, and set policy to `Enforce configuration`. [Skill 3.1: Define organization and enterprise policies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining organization and enterprise security policies and security configurations (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/about-security-configurations)]

- **A:** Incorrect. Manual per-repository toggling drifts immediately and misses centralized Security Configurations and enforcement.
- **B:** Incorrect. Settings left as `Not set` in a Security Configuration are explicitly not enforced against repository overrides.
- **C:** Incorrect. GHAS enablement fails if active-committer seats are exhausted, transferred repos require manual attachment, and disabling Actions breaks CodeQL default setup.
- **D:** Correct. Correct rollout: confirm active-committer license headroom, define the custom Security Configuration, apply it to existing/transferred repos and new-repo defaults, and enforce it.

### Question 35 — `B, E` (Implement secure software development and compliance)

Correct answers: B and E (are correct). Enforce an Enterprise/Org **Security Configuration** (remembering to attach transferred repos explicitly), and enable **Secret Scanning Push Protection + Validity Checks + Delegated Bypass**. [Skill 3.1: Define organization and enterprise policies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining organization and enterprise security policies and security configurations (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/about-security-configurations)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Correct. Enforced Security Configurations prevent repository admins from disabling mandatory Secret Protection, CodeQL, or Dependabot controls.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **E:** Correct. Push Protection blocks secrets pre-receive, validity checks highlight live active credentials, and delegated bypass routes false-positive overrides through security reviewers.

### Question 36 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). No — `Default for newly created repositories` triggers **only** on repository creation, **not** on repository transfer; attach `@vgrid-production`'s Security Configuration to the 8 transferred repos via UI or REST API! [Skill 3.1: Define organization and enterprise policies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining organization and enterprise security policies and security configurations (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/about-security-configurations)]

- **A:** Incorrect. Deleting a file in a new commit never purges prior blob SHAs, and any exposed secret must be considered compromised and rotated immediately.
- **B:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — `Default for newly created repositories` triggers **only** on repository creation, **not** on repository transfer; attach `@vgrid-production`'s Security Configuration to the 8 transferred repos via UI or REST API!
- **C:** Correct. GitHub applies default Security Configurations when a repository is newly created in the org, not when an existing repository is transferred in.
- **D:** Incorrect. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.

### Question 37 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). Enable the **`Restrict max file size`** Push rule (`e.g., 10 MB`) inside an enforced Organization/Enterprise **Repository Ruleset**! [Skill 3.2: Strengthen enterprise security posture and data protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Strengthening enterprise security posture, SSH CAs, IP allow lists, and data protection (https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Correct. Push rulesets evaluate file paths, extensions, and blob sizes on `git push` before commits land on any branch in targeted repositories.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 38 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Enforce **`Repository visibility change`** = **`Disabled`** (or restrict repository creation/visibility strictly to `Private` and `Internal` only across the enterprise)! [Skill 3.2: Strengthen enterprise security posture and data protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Strengthening enterprise security posture, SSH CAs, IP allow lists, and data protection (https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Correct. SSH CAs eliminate unrotated static personal SSH keys by requiring short-lived certificates signed by the corporate CA, paired with IP allow lists (or Entra CAPs).

### Question 39 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Configure the **IP allow list directly on the GitHub App's registration** and enable **`Automatically allow IP addresses inherited from GitHub Apps`** in the Enterprise/Org IP allow list settings! [Skill 3.2: Strengthen enterprise security posture and data protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Strengthening enterprise security posture, SSH CAs, IP allow lists, and data protection (https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Correct. SSH CAs eliminate unrotated static personal SSH keys by requiring short-lived certificates signed by the corporate CA, paired with IP allow lists (or Entra CAPs).
- **D:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.

### Question 40 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). Create an encrypted S3 bucket / Splunk HEC token, configure sink credentials in Enterprise Audit Log Streaming, verify the test check and enable `Stream Git events`, and enforce SIEM WORM retention + anomaly alerts. [Skill 3.3: Implement audit logging and reporting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Implementing audit logging, audit log streaming, and compliance reporting (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)]

- **A:** Incorrect. Audit log streaming is configured at the **Enterprise** level (capturing enterprise and member-organization events), not on an individual repository tab.
- **B:** Correct. Correct audit-streaming setup: prepare the target sink, configure credentials in Enterprise Settings -> Audit log -> Log streaming, validate the test check, and enforce SIEM retention/alerting.
- **C:** Incorrect. Audit log streams support vetted encrypted sinks with strict verification, and audit access should use least-privilege custom roles rather than Enterprise Owner.
- **D:** Incorrect. GitHub retains non-Git audit events in the UI/API for a rolling window (up to 180 days; Git events shorter), so multi-year retention requires Audit Log Streaming.

### Question 41 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). **Amazon S3**, **Azure Blob Storage**, **Azure Event Hubs**, **Google Cloud Storage**, **Datadog**, and **Splunk** (`HTTP Event Collector`) are natively supported streaming sinks! [Skill 3.3: Implement audit logging and reporting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Implementing audit logging, audit log streaming, and compliance reporting (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)]

- **A:** Correct. Because UI/REST audit retention is time-bounded (180 days standard; shorter for high-volume Git events), compliance teams stream immutable audit events continuously to external SIEM/WORM storage.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 42 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). No — GitHub Audit Log entries are **append-only and immutable** inside GitHub (neither Org Owners nor Enterprise Owners can edit or delete audit log records), and streaming immediately replicates events to external WORM storage! [Skill 3.3: Implement audit logging and reporting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Implementing audit logging, audit log streaming, and compliance reporting (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Correct. Because UI/REST audit retention is time-bounded (180 days standard; shorter for high-volume Git events), compliance teams stream immutable audit events continuously to external SIEM/WORM storage.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.

### Question 43 — `C, D, F` (Implement secure software development and compliance)

Correct answers: C, D, and F (are correct). Roll out an **Enforced Security Configuration**, activate **Secret Scanning Push Protection + Validity Checks + Delegated Bypass**, and require **CodeQL + Dependabot security updates + PR Dependency Review**. [Skill 3.4: Configure vulnerability alerts, secret scanning, and CodeQL | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring vulnerability alerts, secret scanning push protection, and CodeQL code scanning (https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Correct. Combining CodeQL semantic analysis, Dependabot remediation PRs, and PR-time Dependency Review stops vulnerable code and packages before merge.
- **D:** Correct. Enforced Security Configurations prevent repository admins from disabling mandatory Secret Protection, CodeQL, or Dependabot controls.
- **E:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **F:** Correct. Push Protection blocks secrets pre-receive, validity checks highlight live active credentials, and delegated bypass routes false-positive overrides through security reviewers.

### Question 44 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). Secret scanning inspects **full Git commit history across all branches** **plus** Issue titles/bodies, Pull Request descriptions/comments, and Discussions (`and AI/non-provider patterns catch generic high-entropy passwords too`)! [Skill 3.4: Configure vulnerability alerts, secret scanning, and CodeQL | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring vulnerability alerts, secret scanning push protection, and CodeQL code scanning (https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)]

- **A:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **B:** Correct. Dry-running custom regex patterns at the org/enterprise level validates false-positive rates before publishing push-protection enforcement across repositories.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.

### Question 45 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). The **`Default`** suite runs high-precision, low-false-positive security queries, whereas **`Security-extended`** adds medium-precision/broader security queries to catch subtle vulnerabilities in high-assurance codebases! [Skill 3.4: Configure vulnerability alerts, secret scanning, and CodeQL | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring vulnerability alerts, secret scanning push protection, and CodeQL code scanning (https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)]

- **A:** Correct. CodeQL analyzes code semantically for CWE/OWASP flaws, while Secret Scanning Push Protection blocks credential commits pre-receive and verifies live token status via partner validity checks.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.

### Question 46 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Dependabot jobs execute inside your **Azure VNet Larger runners or self-hosted runners**, reaching internal air-gapped Nexus/Artifactory registries behind corporate firewalls! [Skill 3.5: Manage Dependabot and security advisories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing Dependabot alerts, security/version updates, private registries, and advisories (https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. Granting Dependabot private-registry credentials (and running Dependabot on VNet-connected Actions/ARC runners) lets Dependabot resolve internal Artifactory/NuGet/npm packages securely.

### Question 47 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Enabling **Private vulnerability reporting** (`Repository Security Advisories`) creates a confidential advisory report, private remediation fork, and streamlined CVE issuance workflow! [Skill 3.5: Manage Dependabot and security advisories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing Dependabot alerts, security/version updates, private registries, and advisories (https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **C:** Correct. Dependabot flags known CVEs, opens automated upgrade PRs (authenticating to private registries when configured), blocks vulnerable PR dependencies via Dependency Review, and pairs with private Security Advisories.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 48 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Enabling the **Dependency graph** builds the repository's Software Bill of Materials (`SBOM`, exportable in SPDX JSON format) and powers both Dependabot alerts and Dependency Review! [Skill 3.5: Manage Dependabot and security advisories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing Dependabot alerts, security/version updates, private registries, and advisories (https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Correct. Dependabot flags known CVEs, opens automated upgrade PRs (authenticating to private registries when configured), blocks vulnerable PR dependencies via Dependency Review, and pairs with private Security Advisories.
- **B:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 49 — `B, D` (Implement secure software development and compliance)

Correct answers: B and D (are correct). Treat the SAS key as compromised and **revoke/rotate it immediately in Azure**, then purge history across all refs with **`git filter-repo`**, force-push, and submit the unreachable SHAs to **GitHub Support** for cache eviction! [Skill 3.6: Define and implement a security response plan | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining a security response plan and purging sensitive data from Git history (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Correct. `git filter-repo` rewrites Git history cleanly, and GitHub Support purges unreachable commit objects and cached Pull Request diffs on GitHub servers.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. Publicly or internally pushed secrets can be scraped within seconds by bots or clones; credential revocation/rotation is always step #1.
- **E:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 50 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). No — `git revert` merely appends a new commit deleting the file in `HEAD` while leaving the full `scada_root_ca.key` blob intact in the previous commit for anyone who runs `git log -p`; **revoke the CA key immediately** and scrub history with `git filter-repo`! [Skill 3.6: Define and implement a security response plan | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining a security response plan and purging sensitive data from Git history (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — `git revert` merely appends a new commit deleting the file in `HEAD` while leaving the full `scada_root_ca.key` blob intact in the previous commit for anyone who runs `git log -p`; **revoke the CA key immediately** and scrub history with `git filter-repo`!
- **B:** Correct. Deleting a file in a new commit never purges prior blob SHAs, and any exposed secret must be considered compromised and rotated immediately.
- **C:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **D:** Incorrect. GitHub applies default Security Configurations when a repository is newly created in the org, not when an existing repository is transferred in.

### Question 51 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). A GHES Site Administrator can run **`ghe-repo-gc`** (after removing lingering PR refs if applicable) directly on the GHES appliance to garbage-collect unreachable objects! [Skill 3.6: Define and implement a security response plan | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining a security response plan and purging sensitive data from Git history (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **C:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **D:** Correct. Rewriting Git history never un-compromises an exposed credential; rotation comes first, followed by `git filter-repo`, force-pushing, collaborator re-cloning, and a Support cache purge.

### Question 52 — `C, D` (Implement secure software development and compliance)

Correct answers: C and D (are correct). Block **`PAT (classic)`** access while enforcing max expiration + **Owner approval** on **Fine-grained PATs**, and migrate automated services to **GitHub App installation access tokens**. [Skill 3.7: Configure personal access tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring fine-grained and classic Personal Access Token (PAT) enterprise policies (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **C:** Correct. GitHub App installations on GHEC provide 3x higher REST throughput, short-lived 1-hour credentials, and complete decoupling from employee turnover.
- **D:** Correct. Enterprise PAT policies replace broad non-expiring classic tokens with short-lived, repo-scoped, admin-approved Fine-grained PATs.
- **E:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.

### Question 53 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). A **classic PAT** (`repo`) spans **every** non-SAML/authorized repository the user can touch across organizations with coarse read/write power, whereas a **Fine-grained PAT** binds to **one single target resource owner** (`e.g., Org-A only`), **selected repositories**, and **50+ granular read/write permissions**! [Skill 3.7: Configure personal access tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring fine-grained and classic Personal Access Token (PAT) enterprise policies (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Correct. Enterprise PAT policies curb broad non-expiring classic PATs and require organization owner approval, repo scoping, and short lifetimes on Fine-grained PATs.
- **D:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.

### Question 54 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). The **`Active tokens`** inventory inside Enterprise/Organization Personal Access Token settings lists token owners, target repositories, granted permissions, expiration dates, and `last used` timestamps with instant **`Revoke`** controls! [Skill 3.7: Configure personal access tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring fine-grained and classic Personal Access Token (PAT) enterprise policies (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise)]

- **A:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. Enterprise PAT policies curb broad non-expiring classic PATs and require organization owner approval, repo scoping, and short lifetimes on Fine-grained PATs.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 55 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Conditional requests returning **`304 Not Modified`** consume **zero** primary REST API rate-limit requests, making `ETag` / `Last-Modified` caching a top optimization technique! [Skill 3.8: Understand rate limits for PATs and GitHub Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Understanding REST and GraphQL API rate limits for PATs, GitHub Apps, and GITHUB_TOKEN (https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api)]

- **A:** Correct. On GHEC, GitHub App installations get 15,000 REST req/hr (and 10,000 GraphQL pts/hr) isolated from human users, whereas user PATs share one 5,000 req/hr personal bucket and hit secondary concurrency caps faster.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 56 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Sending more than roughly **`100` concurrent requests** (or >`80` content-generating requests/minute without `>=1` second spacing between mutating POST/PUT/PATCH/DELETE calls) triggers Secondary rate limits! [Skill 3.8: Understand rate limits for PATs and GitHub Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Understanding REST and GraphQL API rate limits for PATs, GitHub Apps, and GITHUB_TOKEN (https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **C:** Correct. `304 Not Modified` conditional requests do not count against primary REST rate limits, while webhook-driven architectures and `Retry-After` backoff prevent secondary `403` throttling.
- **D:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.

### Question 57 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). No — the **`15,000 requests/hour`** GHEC REST limit applies **per GitHub App installation** on the organization (shared across all tokens minted for that installation), **not** per individual token string! [Skill 3.8: Understand rate limits for PATs and GitHub Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Understanding REST and GraphQL API rate limits for PATs, GitHub Apps, and GITHUB_TOKEN (https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api)]

- **A:** Incorrect. Personal-account Team Sync (`Entra ID`/`Okta`) never adds non-members into an organization; users must join the org via SAML/SCIM invitation first (or deploy GHEC with EMUs).
- **B:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — the **`15,000 requests/hour`** GHEC REST limit applies **per GitHub App installation** on the organization (shared across all tokens minted for that installation), **not** per individual token string!
- **C:** Incorrect. Offboarding or suspending inactive accounts reclaims per-user licenses cleanly without breaking repository Git history or compliance review logs.
- **D:** Correct. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.

### Question 58 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Register an org-owned GitHub App with minimal permissions, store its `.pem` key in Key Vault/Vault and install on target repos, sign a `<=10m` RS256 JWT to mint `1h` installation tokens, and revoke the legacy PAT. [Skill 3.9: Describe GitHub Apps and OAuth Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Comparing GitHub Apps, OAuth Apps, deploy keys, and machine users (https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)]

- **A:** Incorrect. OAuth Apps use broad user-tied scopes and long-lived tokens rather than actor-independent 1-hour installation tokens.
- **B:** Incorrect. App `.pem` keys must never be committed, and a GitHub App JWT (max 10 minutes) only authenticates App endpoints to mint a 1-hour installation token.
- **C:** Correct. Correct migration: register a fine-grained GitHub App, safeguard its private key and scope installation repos, mint 1-hour installation tokens via signed JWT, and retire the classic PAT.
- **D:** Incorrect. Machine users consume paid Enterprise seats and share a 5,000 req/hr user rate limit instead of GHEC GitHub App installation scaling (15,000 req/hr).

### Question 59 — `A, E` (Implement secure software development and compliance)

Correct answers: A and E (are correct). Deploy **GitHub Apps** (`1-hour installation tokens, 15,000 req/hr on GHEC, fine-grained permissions`) for bots, and enforce **Fine-grained PAT** approval + expiration while blocking classic PATs. [Skill 3.9: Describe GitHub Apps and OAuth Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Comparing GitHub Apps, OAuth Apps, deploy keys, and machine users (https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)]

- **A:** Correct. GitHub App installations on GHEC provide 3x higher REST throughput, short-lived 1-hour credentials, and complete decoupling from employee turnover.
- **B:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **E:** Correct. Enterprise PAT policies replace broad non-expiring classic tokens with short-lived, repo-scoped, admin-approved Fine-grained PATs.

### Question 60 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). OAuth Apps use coarse legacy OAuth scopes (`status` / `repo`) spanning **every** repository the authorizing user can access and issue long-lived user-tied tokens, whereas a **GitHub App** scopes strictly to `grid-sim` with `Commit statuses: Write` only! [Skill 3.9: Describe GitHub Apps and OAuth Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Comparing GitHub Apps, OAuth Apps, deploy keys, and machine users (https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Correct. GitHub Apps survive employee offboarding, consume zero user seats, grant fine-grained repo/resource permissions, and use short-lived tokens—outperforming both OAuth Apps and seat-consuming machine users.
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 61 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). No — non-owners can only **request** installation of a GitHub App on repositories they administer; an **Organization Owner** (or delegated App Manager) must review permissions and approve installation! [Skill 3.10: Approve or deny app usage based on policy | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Approving, denying, and governing OAuth Apps and GitHub App installations (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Correct. With OAuth App access restrictions active, unapproved third-party OAuth apps can read public data only and cannot touch organization private repos until an Owner explicitly approves the request.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 62 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Assign the user or team the **GitHub App manager** role (either across all org-owned GitHub Apps or on one specific GitHub App registration)! [Skill 3.10: Approve or deny app usage based on policy | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Approving, denying, and governing OAuth Apps and GitHub App installations (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions)]

- **A:** Correct. With OAuth App access restrictions active, unapproved third-party OAuth apps can read public data only and cannot touch organization private repos until an Owner explicitly approves the request.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 63 — `C, E` (Manage GitHub Actions)

Correct answers: C and E (are correct). Host `workflow_call` workflows and composite actions in **`Internal`** repositories with enterprise workflow `Access` enabled, and mandate **40-character SHA pinning** + `Read-only` `GITHUB_TOKEN`. [Skill 4.1: Configure and manage reuse of actions and workflows to the enterprise repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Sharing reusable workflows and actions privately across enterprise organizations (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Correct. 40-char SHA pinning neutralizes upstream tag hijacking while read-only `GITHUB_TOKEN` defaults enforce job-level least privilege.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **E:** Correct. Enterprise teams reuse vetted CI/CD templates privately across all member organizations without exposing proprietary workflows publicly.

### Question 64 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). GitHub Actions supports nesting reusable workflows up to **`4` levels** deep (`and up to 50 reusable workflow calls in a single workflow run`, or `10` on older GHES releases)! [Skill 4.1: Configure and manage reuse of actions and workflows to the enterprise repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Sharing reusable workflows and actions privately across enterprise organizations (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Correct. Without publishing proprietary actions to the public internet, enterprises host golden `workflow_call` workflows and actions inside `Internal`/`Private` repos with cross-repo enterprise workflow access enabled.

### Question 65 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). Tag releases in **`Internal`** repositories (`with action.yml` + `Access = Accessible from repositories in the enterprise`), making vetted internal actions discoverable across all enterprise organizations! [Skill 4.1: Configure and manage reuse of actions and workflows to the enterprise repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Sharing reusable workflows and actions privately across enterprise organizations (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Correct. Without publishing proprietary actions to the public internet, enterprises host golden `workflow_call` workflows and actions inside `Internal`/`Private` repos with cross-repo enterprise workflow access enabled.

### Question 66 — `A, D` (Manage GitHub Actions)

Correct answers: A and D (are correct). Enforce **`Require actions to be pinned to a full-length commit SHA`** + `Read-only` `GITHUB_TOKEN`, and lock runners inside **Runner Groups** restricted to selected repos and workflows. [Skill 4.2: Apply organizational policies for GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing enterprise and organization GitHub Actions policies and SHA pinning (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Correct. 40-char SHA pinning neutralizes upstream tag hijacking while read-only `GITHUB_TOKEN` defaults enforce job-level least privilege.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Correct. Runner group repository and workflow restrictions prevent untrusted repos or ad-hoc branches from scheduling jobs onto privileged runners.
- **E:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 67 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). If enabled, a compromised or buggy workflow using `GITHUB_TOKEN` could open **and** self-approve Pull Requests (`undermining human separation-of-duties review controls`)! [Skill 4.2: Apply organizational policies for GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing enterprise and organization GitHub Actions policies and SHA pinning (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Correct. Pinning third-party actions to immutable 40-char commit SHAs blocks tag-mutation supply-chain attacks, while `permissions: read-all` / read-only `GITHUB_TOKEN` defaults enforce least privilege.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 68 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Yes — Enterprise-level `Allow select actions and reusable workflows` combined with `Require actions to be pinned to a full-length commit SHA` blocks unapproved actions and mutable tags across every organization! [Skill 4.2: Apply organizational policies for GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing enterprise and organization GitHub Actions policies and SHA pinning (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. Standard hosted runners cannot join customer Azure VNets, and arm64 macOS Larger runners do not support Azure private networking or static IP assignment.
- **B:** Correct. Every technical requirement, permission boundary, and GitHub Enterprise platform rule in the scenario is satisfied cleanly.
- **C:** Incorrect. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.
- **D:** Incorrect. GitHub applies default Security Configurations when a repository is newly created in the org, not when an existing repository is transferred in.

### Question 69 — `A, D, F` (Manage GitHub Actions)

Correct answers: A, D, and F (are correct). Scope runners inside repository/workflow-restricted **Runner Groups**, connect Linux Larger runners via **Azure Private Networking** (`VNet`), and authenticate via **OIDC (`id-token: write`)** gated by a **`production` Deployment Environment**. [Skill 4.3: Manage runner groups and administer GitHub-hosted vs. self-hosted runner options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing runner groups, Larger runners, self-hosted runners, and Actions Runner Controller (ARC) (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Correct. Runner group repository and workflow restrictions prevent untrusted repos or ad-hoc branches from scheduling jobs onto privileged runners.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. Azure Private Networking gives managed GitHub-hosted Larger runners private VNet egress to internal endpoints and predictable firewall/NAT egress IPs.
- **E:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **F:** Correct. Combining protected Deployment Environments with narrow OIDC subject claims (`repo:<org>/<repo>:environment:production`) delivers zero-standing-secret CD security.

### Question 70 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). Calling `generate-jitconfig` produces a pre-bound, single-job **JIT runner configuration** (`./run.sh --jitconfig <encoded>`) that auto-deregisters the runner as soon as one job completes! [Skill 4.3: Manage runner groups and administer GitHub-hosted vs. self-hosted runner options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing runner groups, Larger runners, self-hosted runners, and Actions Runner Controller (ARC) (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Correct. Single-use ephemeral runners prevent cross-job workspace contamination, lingering credentials, or persistent malware across CI builds.

### Question 71 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). Use the structured `runs-on:` mapping (`runs-on: { group: ot-linux-runners, labels: [self-hosted, linux, x64, scada] }`) so jobs route strictly to that Runner Group! [Skill 4.3: Manage runner groups and administer GitHub-hosted vs. self-hosted runner options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing runner groups, Larger runners, self-hosted runners, and Actions Runner Controller (ARC) (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. Runner groups isolate sensitive self-hosted or Larger runners to approved repositories and reusable workflow refs, while `--ephemeral` JIT / ARC pods ensure clean single-job runner state.

### Question 72 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). Delegate an Azure VNet subnet to `GitHub.Network` and create `NetworkSettings`, create a GitHub Network Configuration, attach it to a Windows Larger runner group, and restrict the runner group to approved repos/workflows. [Skill 4.4: Apply IP allow lists and configure networking (including Azure private networking) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring IP allow lists, proxies, and Azure private networking (VNet) for runners (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization)]

- **A:** Correct. Correct sequence: prepare the delegated Azure VNet + `GitHub.Network/networkSettings` resource, register the GitHub Network Configuration, bind it to a Larger runner group, and restrict repo/workflow access.
- **B:** Incorrect. By default Enterprise policy restricts org-created Network Configurations unless enabled by an Enterprise Owner, and Azure NetworkSettings linkage is mandatory.
- **C:** Incorrect. Standard Linux runners use a multi-cloud pool beyond Azure IPs, and VNet-integrated runners still require outbound access to required GitHub endpoints.
- **D:** Incorrect. Azure private networking requires Linux/Windows Larger runners (not macOS arm64 larger runners), subnet delegation, and strict runner-group access controls.

### Question 73 — `A, E` (Manage GitHub Actions)

Correct answers: A and E (are correct). Deploy `GitHub.Network/networkSettings` + GitHub **Network Configurations** on **Linux/Windows Larger runners**, and isolate those runners inside a **Runner Group** restricted to approved repositories/workflows. [Skill 4.4: Apply IP allow lists and configure networking (including Azure private networking) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring IP allow lists, proxies, and Azure private networking (VNet) for runners (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization)]

- **A:** Correct. Runner group repository and workflow restrictions prevent untrusted repos or ad-hoc branches from scheduling jobs onto privileged runners.
- **B:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **E:** Correct. Azure Private Networking gives managed GitHub-hosted Larger runners private VNet egress to internal endpoints and predictable firewall/NAT egress IPs.

### Question 74 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Attach **Azure Firewall** / **Network Security Groups (`NSGs`)** and User-Defined Routes (`UDRs`) to the delegated runner subnet (while keeping GitHub's documented Actions broker/cache/storage endpoints reachable over HTTPS `443`)! [Skill 4.4: Apply IP allow lists and configure networking (including Azure private networking) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring IP allow lists, proxies, and Azure private networking (VNet) for runners (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Correct. Azure Private Networking gives GitHub-hosted Larger runners private RFC1918 VNet egress to internal registries/databases and satisfies organization IP allow lists without maintaining self-hosted VMs.
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 75 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Setting **`NODE_EXTRA_CA_CERTS=/etc/ssl/certs/corp-root-ca.pem`** or **`ACTIONS_RUNNER_TLS_NO_VERIFY` (never in prod!) -> properly `GITHUB_ACTIONS_RUNNER_EXTRA_CA_CERTS` / OS CA store + `NODE_EXTRA_CA_CERTS`** inside `.env` lets Node.js Actions trust your internal Root CA cleanly! [Skill 4.5: Monitor and troubleshoot runner performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring and troubleshooting runner _diag logs, queues, and performance (https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Correct. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 76 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). Self-hosted runners require **zero inbound firewall ports**—the runner initiates **outbound HTTPS (`TCP 443`)** long-polling connections (`50-second poll intervals`) to GitHub's Actions service! [Skill 4.5: Monitor and troubleshoot runner performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring and troubleshooting runner _diag logs, queues, and performance (https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Correct. `Runner_*.log` records control-plane polling/TLS/proxy failures on the self-hosted agent, whereas `Worker_*.log` captures per-job execution details when jobs fail or stall.

### Question 77 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). The unprivileged runner service user is missing membership in the `docker` group (`or rootless Docker/Podman setup`); remember `docker.sock` is root-equivalent on the VM, which is why **ephemeral (`--ephemeral` / `ARC`)** isolation is critical! [Skill 4.5: Monitor and troubleshoot runner performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring and troubleshooting runner _diag logs, queues, and performance (https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Correct. `Runner_*.log` records control-plane polling/TLS/proxy failures on the self-hosted agent, whereas `Worker_*.log` captures per-job execution details when jobs fail or stall.

### Question 78 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Because **`Prevent self-review`** is enabled, Alice **cannot** approve her own triggered deployment—a *different* member of `@vanguardgrid/grid-release-leads` must review and approve! [Skill 4.6: Define scope and access for secrets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining secret scope, hierarchy precedence, and deployment environment access controls (https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Correct. Production cloud secrets belong in protected Deployment Environments (`environment: production`) gated by human/custom deployment protection rules and branch filters, overriding broader repo/org secrets.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 79 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Configuring a **Wait timer** (`60` minutes) pauses the environment job automatically for the specified bake window before releasing environment secrets! [Skill 4.6: Define scope and access for secrets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining secret scope, hierarchy precedence, and deployment environment access controls (https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Correct. Custom deployment protection rules gate `environment: production` jobs automatically via webhook callbacks to external ITSM or observability systems.
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 80 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). No — **Environment secrets** are injected **only** into jobs that explicitly declare `environment: <name>` (and pass all environment protection gates); a job omitting `environment:` receives the **Repository secret** (`https://dev.vgrid.io`)! [Skill 4.6: Define scope and access for secrets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining secret scope, hierarchy precedence, and deployment environment access controls (https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. Standard hosted runners cannot join customer Azure VNets, and arm64 macOS Larger runners do not support Azure private networking or static IP assignment.
- **B:** Correct. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.
- **C:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — **Environment secrets** are injected **only** into jobs that explicitly declare `environment: <name>` (and pass all environment protection gates); a job omitting `environment:` receives the **Repository secret** (`https://dev.vgrid.io`)!
- **D:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.

### Question 81 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). No — for `pull_request` events from external forks, GitHub **withholds all `secrets.*`** and downgrades `GITHUB_TOKEN` strictly to **`Read-only`** (`never pass untrusted fork code checkout into pull_request_target with secrets`)! [Skill 4.7: Configure secrets at organization and repository levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization and repository encrypted secrets and variables via UI and REST API (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/creating-secrets-for-an-organization)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Correct. Organization secrets never pass to public repos unless explicitly permitted, API writes require LibSodium sealed-box encryption (`48 KB` max per secret), and plain-text config belongs in `vars` context.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 82 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Secret and variable names **cannot** start with the **`GITHUB_`** prefix (`and are case-insensitive alphanumeric + underscore, never starting with a number`)! [Skill 4.7: Configure secrets at organization and repository levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization and repository encrypted secrets and variables via UI and REST API (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/creating-secrets-for-an-organization)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Correct. Organization secrets never pass to public repos unless explicitly permitted, API writes require LibSodium sealed-box encryption (`48 KB` max per secret), and plain-text config belongs in `vars` context.
- **C:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 83 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). Inspect the **`updated_at`** timestamp returned on each secret metadata entry by the Actions Secrets REST API (`alerting whenever updated_at exceeds your 90-day rotation SLA`)! [Skill 4.7: Configure secrets at organization and repository levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization and repository encrypted secrets and variables via UI and REST API (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/creating-secrets-for-an-organization)]

- **A:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Correct. Organization secrets never pass to public repos unless explicitly permitted, API writes require LibSodium sealed-box encryption (`48 KB` max per secret), and plain-text config belongs in `vars` context.

### Question 84 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Create the AWS IAM OIDC provider + role bound to strict `sub`/`aud` claims, grant job `permissions: id-token: write`, exchange the OIDC JWT at runtime for short-lived STS credentials, and delete static AWS secrets from GitHub. [Skill 4.8: Integrate third-party vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Integrating third-party secret vaults (HashiCorp Vault, Azure Key Vault, AWS) via OIDC (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. Storing static admin keys in repositories creates catastrophic credential exposure instead of ephemeral OIDC federation.
- **B:** Correct. Correct passwordless vault flow: lock down cloud/vault OIDC subject claims first, grant `id-token: write`, exchange the ephemeral OIDC token at runtime, and remove static secrets.
- **C:** Incorrect. The external vault/cloud IdP must trust `https://token.actions.githubusercontent.com` and exact subject claims before OIDC exchange can succeed.
- **D:** Incorrect. Wildcard `repo:*` subject claims let any GitHub repository assume your cloud role, and `id-token: write` is required to request an OIDC token.

### Question 85 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Checking `aud` (`sts.amazonaws.com`) prevents confused-deputy token replay across audiences, while strict `StringEquals`/`StringLike` on **`sub`** (`repo:vanguardgrid/infra:environment:production`) blocks any other repo or branch from assuming the IAM role! [Skill 4.8: Integrate third-party vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Integrating third-party secret vaults (HashiCorp Vault, Azure Key Vault, AWS) via OIDC (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Correct. OIDC exchanges a job-scoped JWT signed by `https://token.actions.githubusercontent.com` for short-lived dynamic vault credentials at runtime—eliminating static secrets stored in GitHub.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 86 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). No — **Azure Private Networking** (`GitHub.Network/networkSettings`) is supported only on **Linux and Windows Larger GitHub-hosted runners**, **not** on `arm64` macOS Larger runners! [Skill 4.8: Integrate third-party vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Integrating third-party secret vaults (HashiCorp Vault, Azure Key Vault, AWS) via OIDC (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.
- **B:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — **Azure Private Networking** (`GitHub.Network/networkSettings`) is supported only on **Linux and Windows Larger GitHub-hosted runners**, **not** on `arm64` macOS Larger runners!
- **C:** Incorrect. Deleting a file in a new commit never purges prior blob SHAs, and any exposed secret must be considered compromised and rotated immediately.
- **D:** Correct. Standard hosted runners cannot join customer Azure VNets, and arm64 macOS Larger runners do not support Azure private networking or static IP assignment.

### Question 87 — `A, D` (Monitor and optimize GitHub usage)

Correct answers: A and D (are correct). Correlate **API Insights** with **Enterprise Audit Log `hashed_token`** attributes, and stream **Enterprise Audit Logs** continuously to Azure Event Hubs / Microsoft Sentinel. [Skill 5.1: Analyze audit logs and API usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Analyzing enterprise audit logs, Git events, and API Insights / REST/GraphQL metrics (https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-your-team/apicenter/viewing-api-insights-for-your-organization)]

- **A:** Correct. API Insights pinpoints which App or PAT user is exhausting rate limits while Audit Log `hashed_token` traces exact administrative/API actions.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Correct. Continuous Audit Log Streaming preserves tamper-evident compliance records far beyond GitHub’s interactive 180-day UI retention window.
- **E:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 88 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). API Insights breaks down that actor's **HTTP method + REST route patterns** (`e.g., GET /repos/{owner}/{repo}/commits`), total requests, and **rate-limited request counts** over time! [Skill 5.1: Analyze audit logs and API usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Analyzing enterprise audit logs, Git events, and API Insights / REST/GraphQL metrics (https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-your-team/apicenter/viewing-api-insights-for-your-organization)]

- **A:** Correct. API Insights visualizes hourly/daily REST consumption and `403`/`429` rate-limit hits broken down by specific App or PAT user so admins fix runaway polling loops quickly.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 89 — `C` (Monitor and optimize GitHub usage)

Correct answer: C (is correct). **JSON** (`newline-delimited JSON`) and **CSV** exports are built directly into the Enterprise and Organization Audit Log UI! [Skill 5.1: Analyze audit logs and API usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Analyzing enterprise audit logs, Git events, and API Insights / REST/GraphQL metrics (https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-your-team/apicenter/viewing-api-insights-for-your-organization)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Correct. API Insights visualizes hourly/daily REST consumption and `403`/`429` rate-limit hits broken down by specific App or PAT user so admins fix runaway polling loops quickly.
- **D:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.

### Question 90 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). Enable the native **GHES Prometheus metrics endpoint** (`bearer-token / scraping configuration in Management Console`) to export real-time OpenMetrics/Prometheus time-series telemetry! [Skill 5.2: Distinguish admin responsibilities vs. GitHub Support and generate diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Distinguishing admin vs GitHub Support responsibilities and generating appliance/cloud diagnostics (https://docs.github.com/en/enterprise-server@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/activity-dashboard)]

- **A:** Correct. GHES exposes native Prometheus metrics, SNMP, and syslog forwarding so enterprise monitoring stacks catch resource pressure before outages occur.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 91 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). Using **`ghe-support-upload`** (`e.g., ghe-support-upload -t <ticket_id> -f bundle.tgz` or piping `ghe-support-bundle -x -o -`) transmits diagnostics directly from GHES to GitHub Enterprise Support! [Skill 5.2: Distinguish admin responsibilities vs. GitHub Support and generate diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Distinguishing admin vs GitHub Support responsibilities and generating appliance/cloud diagnostics (https://docs.github.com/en/enterprise-server@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/activity-dashboard)]

- **A:** Correct. Admins first inspect `githubstatus.com`, SAML/webhook delivery logs, and `ghe-diagnostics` CPU/memory/queue health, escalating to GitHub Support via entitled Enterprise Support members with bundles attached.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 92 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). Internal **GHES Admin** task—install your internal Enterprise Root CA certificate in the GHES Management Console (`Privacy / TLS -> Custom CA certificates`) or fix Jenkins's TLS chain! [Skill 5.2: Distinguish admin responsibilities vs. GitHub Support and generate diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Distinguishing admin vs GitHub Support responsibilities and generating appliance/cloud diagnostics (https://docs.github.com/en/enterprise-server@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/activity-dashboard)]

- **A:** Correct. Admins first inspect `githubstatus.com`, SAML/webhook delivery logs, and `ghe-diagnostics` CPU/memory/queue health, escalating to GitHub Support via entitled Enterprise Support members with bundles attached.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 93 — `C` (Monitor and optimize GitHub usage)

Correct answer: C (is correct). **Archive** inactive repositories (`Settings -> Archive this repository`, making them read-only and stopping scheduled/new workflow runs—or note GitHub also auto-disables scheduled `cron` workflows after `60 days` of repo inactivity on public/applicable repos)! [Skill 5.3: Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Evaluating enterprise adoption, Copilot/Actions metrics, and dormant or underutilized features (https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. Comparing assigned seats against 7/28/90-day active usage across Copilot, GHAS Security Overview, and Actions workflows highlights teams needing enablement or license reclamation.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 94 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). To protect individual developer privacy, GitHub suppresses aggregated daily Copilot usage/acceptance breakdowns whenever fewer than **`5`** users with active Copilot licenses were active in that scope! [Skill 5.3: Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Evaluating enterprise adoption, Copilot/Actions metrics, and dormant or underutilized features (https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api)]

- **A:** Correct. Tracking `last_activity_at` per Copilot seat lets enterprise admins automatically reclaim unused seats after a defined inactivity window (e.g., 30–60 days).
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.

### Question 95 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). Repository **`Insights`** surfaces `Pulse`, `Contributors`, `Traffic` (`14-day clones & views`), `Commits`, and `Community Standards` health checklists. [Skill 5.3: Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Evaluating enterprise adoption, Copilot/Actions metrics, and dormant or underutilized features (https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api)]

- **A:** Correct. Comparing assigned seats against 7/28/90-day active usage across Copilot, GHAS Security Overview, and Actions workflows highlights teams needing enablement or license reclamation.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 96 — `B, E` (Monitor and optimize GitHub usage)

Correct answers: B and E (are correct). Audit **dormant seats, pending invites, and 90-day GHAS active committers**, and assign orgs/repos to **Cost Centers** with **75/90/100% Budgets**, `actions/cache`, short artifact retention, and Linux default runners. [Skill 5.4: Interpret usage reports for metered products | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Interpreting metered usage reports, spending limits, and cost centers for Actions, Packages, GHAS & Copilot (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-billing/using-the-billing-platform)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Correct. Cost Centers and Budgets enforce FinOps accountability while caching, shorter artifact retention, and right-sized OS runners cut metered overages.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **E:** Correct. Proactive seat hygiene reclaims idle Enterprise, Copilot, and GHAS licenses before renewal or monthly metered billing cycles.

### Question 97 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). Exactly **`1`** GHAS committer license—unique active committers are **deduplicated across all GHAS-enabled repositories and organizations** within the same Enterprise! [Skill 5.4: Interpret usage reports for metered products | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Interpreting metered usage reports, spending limits, and cost centers for Actions, Packages, GHAS & Copilot (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-billing/using-the-billing-platform)]

- **A:** Correct. If an engineer pushes to 15 GHAS-enabled private repos across 4 orgs in the same enterprise, deduplicated enterprise billing counts only **1** GHAS committer license.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 98 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). The **`cost_center`** column (alongside `organization`, `repository`, `sku`, and `net_amount`) maps every metered Actions minute, GB-hour of storage, Codespace hour, and Copilot/GHAS unit to its assigned Cost Center! [Skill 5.4: Interpret usage reports for metered products | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Interpreting metered usage reports, spending limits, and cost centers for Actions, Packages, GHAS & Copilot (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-billing/using-the-billing-platform)]

- **A:** Correct. Metered billing tracks included enterprise quotas first (for standard hosted runners and Packages/Artifacts storage) and bills overages or Larger runners/Copilot/GHAS against assigned Cost Centers and Budgets.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.

### Question 99 — `C` (Monitor and optimize GitHub usage)

Correct answer: C (is correct). Across `VanguardGrid`'s 22 utility orgs, export consumed-licenses and verify GitHub Connect GHES sync first, audit dormant substation users and 90-day GHAS committers, reclaim idle seats while right-sizing Actions budgets, and automate SCIM offboarding + alerts. [Skill 5.5: Recommend strategies for license and resource optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending strategies for dormant seat reclamation, caching, and runner/storage cost optimization (https://docs.github.com/en/enterprise-server@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/managing-dormant-users)]

- **A:** Incorrect. Admins remove/suspend org or EMU memberships (preserving PR/commit audit trails) rather than deleting security controls.
- **B:** Incorrect. GHAS seats release automatically 90 days after a user’s last push (or when GHAS is disabled on the repo), and disabling GitHub Connect causes double-billing across GHEC and GHES.
- **C:** Correct. Correct optimization loop: inspect unified license data, pinpoint duplicate identities/dormant users/GHAS committers, reclaim unused seats and cap metered budgets, and automate SCIM hygiene.
- **D:** Incorrect. macOS hosted runners carry a higher per-minute cost than Linux runners, long artifact retention inflates storage charges, and unmonitored seat grants waste licenses.

### Question 100 — `C` (Monitor and optimize GitHub usage)

Correct answer: C (is correct). Enabling **`actions/cache@v4`** (`or cache: 'pip' / 'npm'` inside `actions/setup-*`, up to `10 GB` free cache space per repository) slashes billable runner minutes and external registry bandwidth! [Skill 5.5: Recommend strategies for license and resource optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending strategies for dormant seat reclamation, caching, and runner/storage cost optimization (https://docs.github.com/en/enterprise-server@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/managing-dormant-users)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Correct. Suspending dormant users, cancelling expired invitations, syncing GHEC+GHES via GitHub Connect, trimming artifact retention (`retention-days: 7`), and moving non-Apple jobs off macOS runners cut spend immediately.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
