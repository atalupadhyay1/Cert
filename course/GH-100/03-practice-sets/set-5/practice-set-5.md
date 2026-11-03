# Microsoft / GitHub Exam GH-100: GitHub Enterprise Administrator — Full-Length Mock Exam 5

**Theme:** Sovereign Data Residency & Audit Compliance — GHE.com + EMUs, Audit Log Streaming, Fine-Grained PAT Policies, GitHub Apps & ARC Runners  
**Credential:** `GitHub Administration` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `July 2026 (Last updated May 5, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-100 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Enterprise documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Manage GitHub identities and access (15–20% official weight · 19 questions)

### 1. An aerospace manufacturer (`ZephyrAero`) runs **GHEC with EMUs** (`shortcode: zaero`) for flight-control software and invites FAA certification auditors to inspect four DO-178C repositories without browsing 450 `Internal` avionics repos. Which two controls enforce this boundary? Select two.

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Provision user accounts exclusively via your corporate IdP (`SAML`/`OIDC` + `SCIM`), blocking personal public repos, Gists, and external OSS contributions
- **D.** Assign external contractors the IdP **Guest Collaborator** role so they cannot browse `Internal` enterprise repositories unless explicitly granted access
- **E.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 2. Can an **EMU** user in `ZephyrAero` (`maya_zaero`) create a personal secret Gist (`____.github.com`) or create repositories directly under their personal `@maya_zaero` user namespace?

- **A.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **B.** Enterprise Managed Users (`EMUs`) provisioned by your corporate IdP (`<handle>_<shortcode>`), isolated from public repo creation, Gists, and external OSS pushes
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

### 3. During a personal-account GHEC SAML rollout on `@zephyraero-sim`, 12 engineers forgot to link their SAML `NameID` before the admin switched SAML SSO to **`Enforce`**. Were their historical commits deleted, and how do those 12 engineers regain membership?

- **A.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Enterprise/Organization SAML 2.0 SSO paired with mandatory GitHub `2FA` (with SAML recovery codes stored safely and PAT/SSH credential authorization enforced)
- **D.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step

### 4. In a SAML 2.0 assertion sent from Okta or PingFederate to GitHub (`NameID` + `AttributeStatement`), why must the IdP **`NameID`** attribute be **persistent, unique, and immutable** (`e.g., immutable employee GUID rather than mutable display email`)?

- **A.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **B.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **C.** Enterprise/Organization SAML 2.0 SSO paired with mandatory GitHub `2FA` (with SAML recovery codes stored safely and PAT/SSH credential authorization enforced)
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 5. `ZephyrAero` stands up a dedicated **GHEC with Data Residency (`zephyraero.ghe.com`) + EMUs** instance connected to Microsoft Entra ID. Which four-step identity bootstrap order applies?

- **A.** Create EMU enterprise & save recovery codes → configure SAML/OIDC SSO with admin setup user → enable SCIM user/group provisioning in IdP → sync IdP groups to Enterprise/Org teams
- **B.** Invite employees personal GitHub.com accounts → convert personal accounts into EMUs in place → enable SCIM → disable 2FA on the IdP
- **C.** Sync IdP groups to Enterprise teams → enable SCIM provisioning → configure SAML/OIDC SSO → create the EMU enterprise account last
- **D.** Enable SCIM without configuring SAML/OIDC SSO → share one setup password across engineers → skip recovery codes → assign everyone Enterprise Owner

### 6. An aerospace supplier subsidiary runs **GHEC with personal accounts** and maps Okta group `Avionics-Contractors` via **Team Synchronization** to `@zaero-supplier/radar-team`. An admin adds 8 brand-new external contractors to `Avionics-Contractors` in Okta without sending GitHub org invites. Proposed solution: Expect personal-account **Team Synchronization** to automatically create org memberships for those 8 non-members. Will they be added to `@zaero-supplier`?

- **A.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **B.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **C.** No — on GHEC with personal accounts, IdP **Team Synchronization** only updates Organization team membership for existing org members and **cannot** invite or provision brand-new users into the organization
- **D.** No — **Enterprise teams** (`@/ent:<slug>`) currently do **not** support `CODEOWNERS` assignment, nested child teams, Secret visibility, or Team maintainers; use an **Organization team** for `CODEOWNERS`

### 7. Why do security architects prefer **Microsoft Entra ID with OIDC** over legacy SAML when deploying **GHEC with EMUs** on a single Entra tenant?

- **A.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **D.** OIDC SSO for Enterprise Managed Users with **Microsoft Entra ID**, automatically enforcing Entra **Conditional Access Policies (`CAP`)** including IP and device compliance

### 8. On a self-hosted **GHES** instance bound to Active Directory via **LDAP**, what does enabling **`LDAPSync` (`Synchronize LDAP groups`)** accomplish for Organization teams?

- **A.** Supported IdPs (`Microsoft Entra ID`, `Okta`, `PingFederate` with paved-path OIDC/SAML+SCIM for EMUs; or `LDAP`/`CAS`/`SAML` on self-hosted `GHES`)
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 9. Which two operational controls belong in every personal-account GHEC SAML SSO runbook? Select two.

- **A.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Require developers on personal-account GHEC to **authorize** approved Fine-grained/classic PATs and SSH keys for SAML SSO before accessing org repositories
- **D.** Download and vault **Enterprise/Org SAML recovery codes** before enforcing SAML SSO so Owners can recover access during an IdP outage
- **E.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

### 10. An Organization Owner revokes SAML SSO authorization for developer Priya's Fine-grained PAT under `Organization Settings -> Personal access tokens` (`or SAML authorized credentials`). Can Priya still use that token against her **personal** public hobby repos, or is it blocked only from `@zaero-supplier`?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Authentication verifies *who* the caller is (`SAML`/`OIDC`, `2FA`, Passkey, SSH key, PAT), while authorization governs *what* resources they may access (roles, teams, scopes, SAML SSO token authorization)
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 11. An avionics FinOps lead needs read/write access to **Cost Centers, Budgets, and Metered Usage exports** across the `ZephyrAero` Enterprise—with **zero** read access to source code in private flight-deck repositories. Which built-in Enterprise role (`Enterprise Settings -> Admins -> ____`) enforces this separation of duties?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Custom **Enterprise roles** (such as `Audit Log Reader`, `Billing Viewer`, or `Enterprise Actions Admin`) assigned to individuals or **Enterprise teams** to avoid over-granting `Enterprise Owner`
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 12. Inside an organization, if `Base permissions` was historically left at `Write` (`legacy anti-pattern!`), what risk exists the moment any new contractor becomes an Organization Member?

- **A.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **B.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** 5 built-in repository roles (`Read`, `Triage`, `Write`, `Maintain`, `Admin`), built-in org roles (`Owner`, `Member`, `Moderator`, `Billing manager`, `Security Manager`), plus GHEC **Custom repository/org roles**

### 13. `ZephyrAero` scales access governance across 28 engineering organizations using **Enterprise teams**. Which three design rules apply? Select three.

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Sync a single 12,000-member Entra ID group into one Enterprise team alongside 15 manually added contractor accounts
- **C.** Set Organization **`Base permissions = None`** and grant repository access strictly through IdP-synced Teams and least-privilege Custom Repository Roles
- **D.** Add **Enterprise teams** across up to 1,000 organizations where org admins can grant additional repo access without removing enterprise-granted permissions
- **E.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **F.** Grant **Copilot Business** seats, **custom/predefined enterprise roles**, and **Repository Ruleset bypass** rights directly to **Enterprise teams** (`@/ent:<slug>`)

### 14. An IAM architect designs a 3-level nested hierarchy of **Enterprise teams** (`@/ent:engineering` -> `@/ent:avionics` -> `@/ent:flight-controls`) and assigns `@/ent:flight-controls` a `Team Maintainer`. Proposed solution: Use nested parent/child **Enterprise teams** with delegated `Team Maintainers`. Does GitHub support parent/child nesting or Team Maintainers on Enterprise teams?

- **A.** No — on GHEC with personal accounts, IdP **Team Synchronization** only updates Organization team membership for existing org members and **cannot** invite or provision brand-new users into the organization
- **B.** No — **Enterprise teams** (`@/ent:<slug>`) currently do **not** support `CODEOWNERS` assignment, nested child teams, Secret visibility, or Team maintainers; use an **Organization team** for `CODEOWNERS`
- **C.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **D.** No — **Azure Private Networking** (`VNet` integration) and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, NOT on standard free runners or `arm64` macOS Larger runners

### 15. When an Enterprise Owner adds an **Enterprise team** (`@/ent:security-champions`) to an Enterprise **Repository Ruleset's `Bypass list`** with bypass mode **`Exempt` vs `Pull request bypass`**, what does `Pull request bypass` allow?

- **A.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **B.** **Enterprise teams** (`@/ent:<slug>`, up to 5,000 EMU IdP-synced users across up to 1,000 orgs) for centralized org membership, Copilot seats, custom enterprise roles, and ruleset bypass
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Sync a single 12,000-member Entra ID group into one Enterprise team alongside 15 manually added contractor accounts

### 16. Which REST API endpoint (`GET /repos/{owner}/{repo}/collaborators/{username}/____`) returns a user's exact computed effective permission level (`admin`, `maintain`, `write`, `triage`, `read`, or `none`) on a repository for automated SOX access scripts?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Exporting enterprise/organization membership & repository permission inventories plus auditing `org.*`, `team.*`, `repo.*`, and token metadata (`hashed_token`, `programmatic_access_type`) in the Audit Log
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 17. In `Organization Settings -> Member privileges`, disabling **`Allow repository administrators to invite outside collaborators`** enforces what governance control?

- **A.** Exporting enterprise/organization membership & repository permission inventories plus auditing `org.*`, `team.*`, `repo.*`, and token metadata (`hashed_token`, `programmatic_access_type`) in the Audit Log
- **B.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 18. To ensure every **newly created** repository in `@zephyraero-flight` starts with `dal_level = DAL-A` unless explicitly classified otherwise by an Org Owner, what setting on the Organization **Custom Property** (`dal_level`, type `Single select`) enforces this?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Repository **Custom Properties** (e.g., `compliance_tier=pci`, `data_class=restricted`) targeted dynamically by Organization/Enterprise **Repository Rulesets** (`most restrictive wins`)

### 19. Which **Repository Ruleset** branch/tag naming rule (`Restrict ____`) enforces corporate Git hygiene so developers can create feature branches **only** matching `^(feat|fix|chore|release)/[a-z0-9-]+$`?

- **A.** Enterprise **Member privileges** (`Base permissions = None`, repo creation/forking/visibility locks) combined with **Organization/Enterprise Repository Rulesets** (`Active` vs `Evaluate` dry-run mode)
- **B.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

---

## Domain 2 — Administer GitHub Enterprise environment (10–15% official weight · 14 questions)

### 20. An Enterprise Owner wants to rename their GHEC Enterprise URL slug (`github.com/enterprises/zephyr-old` -> `zephyr-aero`) or request an architectural evaluation of EMU migration blockers. Which channel handles enterprise slug/backend account operations vs day-to-day repository Ruleset edits?

- **A.** Enterprise Admins resolve IdP/SAML lockouts, RBAC grants, runner sizing, and webhook configs; **GitHub Enterprise Support** handles platform outages, cached PR commit purges, and repo restore escalations
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 21. A developer complains `git push` of a `250 MB` compiled flight-simulator binary failed on GHEC with `remote: error: File sim.bin is 250.00 MB; this exceeds GitHub's file size limit of 100.00 MB`. Should you open a GitHub Support ticket asking GitHub to raise `100 MB`?

- **A.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **B.** Enterprise Admins resolve IdP/SAML lockouts, RBAC grants, runner sizing, and webhook configs; **GitHub Enterprise Support** handles platform outages, cached PR commit purges, and repo restore escalations
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

### 22. An ITAR-restricted simulator lab running self-hosted **GHES** observes slow `git fetch` latencies (`>45s`) during shift changes. Which four-step support escalation workflow applies?

- **A.** Post raw /data/user/common/secrets.conf in a public GitHub Discussion → tag @github → upgrade three major GHES versions mid-outage → skip support bundle generation
- **B.** Confirm admin-side checks & note exact incident UTC timestamps → SSH/console in and run ghe-support-bundle -x (or Management Console) → review/sanitize sensitive log data if required → upload bundle to GitHub Enterprise Support portal
- **C.** File a GitHub Support ticket asking GitHub to reset a developer corporate Active Directory password → wait 48 hours → run git gc locally → close ticket
- **D.** Restart all GHES services with ghe-config-apply --force → wipe /data/user/logs to save disk → open a ticket with no timestamps or bundle → grant Support SSH access to internal VPC

### 23. Which two practices ensure uninterrupted **GitHub Enterprise Support** coverage across a 24x7 global avionics SRE rotation? Select two.

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Generate an extended diagnostic archive via `ghe-support-bundle -x` (or Management Console `:8443`) and upload it to the **GitHub Enterprise Support** portal
- **C.** Designate up to 20–25 entitled **Support** members (or `Enterprise Support` custom role holders) authorized to open and manage enterprise support tickets
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **E.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 24. In `zephyraero-flight/.github/workflow-templates/misra-c.properties.json`, which JSON field (`"____": ["\\.c$", "CMakeLists\\.txt$"]`) tells GitHub to highlight the MISRA-C starter workflow **primarily** on C/CMake repositories?

- **A.** Publishing reusable **Starter Workflows** inside the organization’s `.github` repository (`workflow-templates/*.yml` + `.properties.json`) to standardize onboarding CI pipelines
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 25. To forbid blank one-word Pull Requests across avionics repositories and prompt authors automatically for `DO-178C Requirement ID`, `Hazard Analysis Link`, and `Verification Evidence`, which file (`.github/____.md`) pre-populates every new Pull Request body?

- **A.** Standardizing **Template repositories**, organization-wide `.github` community health defaults, **`Internal`** InnerSource discovery, and ADR/Issue Form intake across teams
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 26. In **GitHub Merge Queue**, `Build concurrency` is set to `5` and `Minimum group size` = `3` (`with a 5-minute wait`). What happens if `4` queued PRs are batched together and the combined `merge_group` CI run **fails**?

- **A.** Enforcing trunk-based **GitHub Flow**, protected `main` with **`CODEOWNERS`**, **Merge Queue** (`gh-readonly-queue`) for busy monorepos, linear squash merges, and immutable signed SemVer **Releases**
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 27. To ensure developers cryptographically prove commit authorship without managing local PGP keyrings on Windows/macOS laptops, which two modern commit-signing methods (`git config gpg.format ____`) does GitHub verify as **`Verified`** alongside GPG?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Enforcing trunk-based **GitHub Flow**, protected `main` with **`CODEOWNERS`**, **Merge Queue** (`gh-readonly-queue`) for busy monorepos, linear squash merges, and immutable signed SemVer **Releases**
- **C.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 28. `ZephyrAero` runs commercial cabin infotainment repos on **GHEC with Data Residency (`zephyraero.ghe.com`)** and classified defense programs on an air-gapped **GHES** appliance. Which two architectural properties apply? Select two.

- **A.** Deploy **GHEC with Data Residency (`<enterprise>.ghe.com`) + EMUs** when regulations require pinning cloud source code and metadata in a specific geographic region (`EU`, `US`, `AU`, `JP`)
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **D.** Enable **GitHub Connect** license synchronization between `GHES` and `GHEC` (plus link **Visual Studio Subscriptions**) so hybrid users consume a single Enterprise seat
- **E.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

### 29. When scheduling **`github/backup-utils`** (`ghe-backup`) against a live self-hosted **GHES** instance every hour, does `ghe-backup` require putting GHES into offline **Maintenance Mode** (`ghe-maintenance -s`), or is `ghe-backup` vs `ghe-restore` different?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Deploying **GHES High Availability** (`ghe-repl-setup` active/passive failover replica) paired with incremental off-appliance snapshots via **`github/backup-utils`** (`ghe-backup` / `ghe-restore`)
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 30. An outside contractor is added as an **Outside collaborator** on **3** private repositories inside `@zephyraero-cabin` and **2** private repositories inside `@zephyraero-sim` (both in the same Enterprise). How many **GitHub Enterprise user seats** does that contractor consume?

- **A.** Per-user **GitHub Enterprise** seat licensing (deduplicating unique users across orgs + synced `GHES` via **GitHub Connect**, plus linked **Visual Studio Enterprise/Pro with GitHub Enterprise** benefits) alongside metered add-ons
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 31. If `ZephyrAero` purchases standalone **GitHub Secret Protection** (`without full GitHub Code Security / CodeQL`) for 10 legacy documentation organizations, how is **GitHub Secret Protection** licensed on private/internal repositories?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **D.** Per-user **GitHub Enterprise** seat licensing (deduplicating unique users across orgs + synced `GHES` via **GitHub Connect**, plus linked **Visual Studio Enterprise/Pro with GitHub Enterprise** benefits) alongside metered add-ons

### 32. Before enabling `GitHub Code Security` / `GHAS` on an organization of 180 private repositories, how can an Enterprise/Organization Owner **preview the exact additional committer seats** that enabling it would consume **before** turning it on?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Inspecting `Enterprise -> Billing & Licensing -> Licensing` (and exported `consumed-licenses` JSON/CSV) to track assigned seats, pending invitations, outside collaborators, VS subscriptions, and `GHES` sync files

### 33. On self-hosted **GHES**, when a Site Administrator imports a renewed `.____` license file (`Management Console :8443`), what happens if consumed GHES user seats ever hit `100%` of the seat cap?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Inspecting `Enterprise -> Billing & Licensing -> Licensing` (and exported `consumed-licenses` JSON/CSV) to track assigned seats, pending invitations, outside collaborators, VS subscriptions, and `GHES` sync files
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

---

## Domain 3 — Implement secure software development and compliance (25–30% official weight · 29 questions)

### 34. Avionics cybersecurity enforces `Secret Protection` + `Code Security` across all 28 `ZephyrAero` organizations via a locked **Enterprise Security Configuration**. Which four-step rollout order applies?

- **A.** Enable Enforce configuration with every setting left as Not set → expect Not set fields to lock repository admins → delete Organization Security Managers → skip default policy
- **B.** Ask 400 repository admins to toggle checkboxes manually in every repo → disable Dependency graph → turn off push protection → audit annually by spreadsheet
- **C.** Apply a GHAS Security Configuration with 0 available licenses → assume transferred repos inherit new-repo defaults automatically → disable GitHub Actions on CodeQL repos → leave unenforced
- **D.** Verify available GHAS / Secret Protection / Code Security committers → create custom Security Configuration at Enterprise/Org level → attach to existing & transferred repos plus default for new repos → set policy to Enforce configuration

### 35. Which two controls prevent accidental secret leaks across both greenfield and migrated repositories in `ZephyrAero`? Select two.

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Enable **Secret Scanning Push Protection**, **Partner Validity Checks**, custom regex patterns, and **Delegated Bypass** reviewer groups
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Create and **Enforce** an Enterprise/Organization **Security Configuration** (setting it as default for newly created repos and manually attaching transferred repos)
- **E.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 36. An Enterprise Admin detaches repository `zephyraero/legacy-fms` from the enforced Security Configuration while debugging a build issue, then transfers `legacy-fms` into `@zephyraero-archive` (`which has Default for newly created repositories enabled`). Proposed solution: Assume the transfer into `@zephyraero-archive` automatically re-attaches `@zephyraero-archive`'s default Security Configuration. Will `legacy-fms` auto-attach on transfer?

- **A.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **B.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **C.** No — committing `git rm` (or archiving the repo) leaves the leaked secret intact in prior Git commits and cached PR diffs; you must **revoke/rotate the secret immediately**, run **`git filter-repo`**, force-push, and contact GitHub Support
- **D.** No — an organization’s default **Security Configuration** auto-attaches only to **newly created** repositories; repositories **transferred** into the organization must have the Security Configuration attached manually or via API

### 37. Which **Repository Ruleset Push rule** (`Restrict file ____`) prevents developers across all branches from committing Windows executables (`.exe`, `.dll`), Java archives (`.jar`), or PKCS#12 certificates (`.p12`, `.pfx`) into source repositories?

- **A.** Configuring **Push Rulesets** to block oversized binaries, forbidden file extensions (`.pem`, `.pfx`, `.key`), restricted file paths (`.github/workflows/**`), and path-traversal commits pre-receive
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 38. On a **GHEC** enterprise using **SSH Certificate Authorities (`SSH CA`)**, what advantage do **SSH certificates** provide when an employee's laptop goes missing at an airport compared to static SSH public keys?

- **A.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **B.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **C.** Hardening access with **Organization/Enterprise IP allow lists**, **SSH Certificate Authorities (`SSH CAs`)** issuing short-lived developer SSH certs, and least-privilege repo-scoped **Deploy keys**
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 39. Under `Repository Settings -> General -> Archives`, why do strict IP-protection enterprises uncheck **`Include Git LFS objects in archives`** or restrict source ZIP downloads alongside private-fork bans?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Hardening access with **Organization/Enterprise IP allow lists**, **SSH Certificate Authorities (`SSH CAs`)** issuing short-lived developer SSH certs, and least-privilege repo-scoped **Deploy keys**
- **D.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges

### 40. DO-178C and AS9100 compliance requires `ZephyrAero` to stream all Enterprise admin and `git.clone`/`git.push` events to Azure Event Hubs -> Microsoft Sentinel with 10-year WORM archival. Which four-step workflow applies?

- **A.** Stream audit logs from a single repository Settings tab → expect enterprise-wide SAML and billing events to appear → disable SAML SSO → delete historical SIEM buckets
- **B.** Rely solely on the 180-day web UI audit search for 7-year regulatory retention → skip log streaming → poll REST API every 50 ms until rate-limited → store logs in a public Gist
- **C.** Provision encrypted SIEM/storage sink (Event Hubs, Blob, S3, Splunk) → configure credentials in Enterprise Audit Log Streaming → verify test event & optional Git toggle → set SIEM retention & alerts
- **D.** Enable Git read/clone event streaming to a public unauthenticated HTTP webhook → skip test verification → grant all Organization Members Enterprise Owner to view logs

### 41. Can an Enterprise Owner configure **two** simultaneous **Audit Log Streaming** endpoints on **GitHub Enterprise Cloud** (`for example, streaming simultaneously to Amazon S3 cold WORM archive AND Splunk real-time SOC`)?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Streaming the **Enterprise Audit Log** (including optional `git.clone`/`git.fetch`/`git.push` events) in real time to **Azure Event Hubs / Blob Storage, AWS S3, Splunk, Datadog, or GCS**, plus REST/GraphQL queries
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 42. In **Enterprise Security Overview -> Risk**, how can an AppSec manager slice open `Critical` CodeQL and Dependabot alerts specifically for **`dal_level:DAL-A`** flight-critical repositories?

- **A.** Using **Enterprise/Organization Security Overview** (`Risk` and `Coverage` dashboards) to audit GHAS enablement gaps, open critical `CodeQL`/Secret/Dependabot alerts, and remediation MTTR
- **B.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls

### 43. Which three AppSec capabilities protect `ZephyrAero`'s C++ flight-control and Python ground-telemetry repositories end-to-end? Select three.

- **A.** Enable **Secret Scanning Push Protection**, **Partner Validity Checks**, custom regex patterns, and **Delegated Bypass** reviewer groups
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Enable **CodeQL default/advanced setup**, **Dependabot security updates**, and the **Dependency Review Action** inside required Pull Request Rulesets
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **E.** Create and **Enforce** an Enterprise/Organization **Security Configuration** (setting it as default for newly created repos and manually attaching transferred repos)
- **F.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 44. In **CodeQL `Advanced setup`** for compiled C/C++20 avionics code (`github/codeql-action`), when `build-mode: autobuild` cannot guess a proprietary `bazel` cross-compiler invocation, how do you ensure accurate full dataflow analysis?

- **A.** Enabling **CodeQL code scanning** (`Default setup` or custom `Advanced setup` SARIF workflows) plus **Secret scanning** with **Push protection**, **Validity checks**, custom regex patterns, and delegated bypass review
- **B.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 45. Can third-party SAST, container, and IaC scanners (`such as Trivy, Checkov, Snyk, or Clang-Tidy`) upload findings directly into GitHub's native **Security -> Code scanning alerts** tab and **Security Overview** (`using open standard format ____ v2.1.0`)?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Enabling **CodeQL code scanning** (`Default setup` or custom `Advanced setup` SARIF workflows) plus **Secret scanning** with **Push protection**, **Validity checks**, custom regex patterns, and delegated bypass review

### 46. In `actions/dependency-review-action@v4`, which configuration option (`____-licenses: ['GPL-3.0', 'AGPL-3.0']` or `allow-licenses`) enforces legal open-source license compliance on every Pull Request before merge?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Configuring **Dependency graph**, **Dependabot alerts**, **Dependabot security & version updates** (`dependabot.yml` + private registry access), **Dependency Review Action** on PRs, and **Repository Security Advisories**

### 47. How do you export a complete **SPDX 2.3 JSON Software Bill of Materials (`SBOM`)** for `zephyraero/autopilot` demanded by an FAA customer (`GET /repos/{owner}/{repo}/dependency-graph/____`)?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Configuring **Dependency graph**, **Dependabot alerts**, **Dependabot security & version updates** (`dependabot.yml` + private registry access), **Dependency Review Action** on PRs, and **Repository Security Advisories**
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing

### 48. Why might `Dependabot security updates` open a PR bumping `urllib3`, yet the PR checks fail to push follow-up lockfile formatting commits if a custom workflow expects standard `secrets.INTERNAL_PYPI_TOKEN`?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Configuring **Dependabot** with encrypted `dependabot` private-registry secrets (`Settings -> Code security -> Global settings`) and running updates on **Actions runners / ARC** when private VNet access is required
- **D.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO

### 49. An avionics build engineer accidentally commits an internal code-signing HSM PIN (`hsm_pin.txt`) into `zephyraero/flight-loader` and pushes two branches to **GHEC**. Which four-step Security Response Plan applies?

- **A.** Run git rm secrets.env in a new commit and push → assume historical commits are erased → keep the production API key active → skip GitHub Support cache purge
- **B.** Contact GitHub Support first to rotate your AWS IAM key → wait before revoking in AWS → delete the entire GitHub Organization → recreate repos from developer zip files
- **C.** Revoke & rotate the exposed secret at the provider → scrub all branches/tags via git filter-repo → force-push cleaned refs & have devs re-clone → send commit SHAs to GitHub Support to purge cached views
- **D.** Archive the repository to hide the leaked key → rotate the key next quarter → use deprecated git filter-branch without force-pushing → tell devs to git pull --merge old history back

### 50. Which two actions are non-negotiable whenever a live production secret reaches a remote GitHub repository (even for 30 seconds on a private repo)? Select two.

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Immediately **revoke and rotate** leaked credentials at the target cloud/API provider before assuming Git history rewrites reduce exposure
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **E.** Scrub sensitive blobs across all refs with **`git filter-repo`**, force-push cleaned branches/tags, and send commit SHAs to **GitHub Support** to purge cached PR views

### 51. A maintainer squash-merges a feature PR into `main` thinking squash-merging deletes the leaked secret that existed in commit 2 of 5 on the PR branch (`and deletes the feature branch`). Proposed solution: Rely on `Squash and merge` + deleting the PR branch to erase commit 2's secret from GitHub's servers without rotating the secret or contacting Support. Is the secret gone?

- **A.** No — an organization’s default **Security Configuration** auto-attaches only to **newly created** repositories; repositories **transferred** into the organization must have the Security Configuration attached manually or via API
- **B.** No — committing `git rm` (or archiving the repo) leaves the leaked secret intact in prior Git commits and cached PR diffs; you must **revoke/rotate the secret immediately**, run **`git filter-repo`**, force-push, and contact GitHub Support
- **C.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **D.** No — suspending a dormant GHES user or removing/SCIM-deprovisioning a GHEC member **frees their Enterprise license seat** while **preserving all historical commits, Issues, and Pull Request audit trails**

### 52. Which two controls bring programmatic access into compliance with zero-standing-privilege avionics standards? Select two.

- **A.** Block or restrict **classic PATs** enterprise-wide while requiring **Organization Owner approval** and max expiration lifetimes (`<=30–90 days`) on **Fine-grained PATs**
- **B.** Migrate org automation from personal PATs (`5,000 req/hr`) to **GHEC GitHub App installation tokens** (`15,000 REST req/hr`, 1-hour expiry, zero seat cost)
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **E.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

### 53. When an Organization Owner revokes or deletes an employee's **Organization membership**, what happens immediately to **every** Fine-grained PAT and SAML-authorized classic PAT that employee previously used to access `@zephyraero-flight`?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **C.** Enforcing **Enterprise Fine-Grained PAT Policies**: restricting or blocking **PATs (classic)**, requiring mandatory expiration lifetimes (e.g., <=30–90 days), requiring **Admin approval** before Fine-grained PATs activate, and revoking tokens
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 54. If a developer leaves a **Fine-grained PAT** completely unused in a forgotten script, does GitHub also enforce automatic inactivity revocation (`in addition to your enterprise's 30/60/90-day max lifetime policy`)?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **C.** Enforcing **Enterprise Fine-Grained PAT Policies**: restricting or blocking **PATs (classic)**, requiring mandatory expiration lifetimes (e.g., <=30–90 days), requiring **Admin approval** before Fine-grained PATs activate, and revoking tokens
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 55. Compare the **Search REST API** rate limit (`GET /search/code`, `/search/issues` — **`____` requests per minute** for `/search/code` and **`30` requests per minute** for general search endpoints) against the standard `5,000/15,000 requests/hour` REST quota!

- **A.** REST rate limits: **`5,000 req/hr`** per personal PAT user vs **`15,000 req/hr`** for a **GitHub App installation** (and `GITHUB_TOKEN` per repo) on **GHEC** (`up to 12,500 req/hr` scaled on non-GHEC; GraphQL `5,000` vs `10,000` pts/hr)
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 56. A telemetry dashboard runs 20 worker containers that all authenticate using PATs generated under the **same** `@zaero-bot` user account (`hitting 5,000 req/hr in 8 minutes`). Proposed solution: Keep `@zaero-bot` as a human/machine account and generate 20 separate Fine-grained PATs under `@zaero-bot` (`1 per container`). Will 20 PATs under `@zaero-bot` increase the hourly quota above `5,000`?

- **A.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **B.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret
- **C.** No — on GHEC with personal accounts, IdP **Team Synchronization** only updates Organization team membership for existing org members and **cannot** invite or provision brand-new users into the organization
- **D.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement

### 57. When GitHub returns a **Secondary rate limit** response (`403` or `429`) **without** a `Retry-After` header, yet `x-ratelimit-remaining` shows **`0`**, how long should your backoff logic wait (`versus when neither header specifies a timestamp`)?

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Mitigating **Secondary (abuse) rate limits** by capping concurrent API requests, serializing write mutations (`>=1 sec` spacing), using **webhooks / GraphQL / Conditional `ETag` (`304 Not Modified`)**, and honoring `Retry-After`

### 58. Avionics DevOps replaces a shared release-manager classic PAT with an enterprise **GitHub App** for automated DO-178C traceability tagging (`minting a ____-hour installation token via a <=10-minute RS256 JWT`). Why is this superior to a human machine-user account?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** **GitHub Apps** act as independent actors scoped to selected repos + granular permissions using **1-hour installation tokens**, whereas **OAuth Apps** act as the authorizing human user with broad scopes and long-lived tokens
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 59. Which two rules separate **machine-to-machine** authentication from **human** CLI authentication in `ZephyrAero`? Select two.

- **A.** Migrate org automation from personal PATs (`5,000 req/hr`) to **GHEC GitHub App installation tokens** (`15,000 REST req/hr`, 1-hour expiry, zero seat cost)
- **B.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Block or restrict **classic PATs** enterprise-wide while requiring **Organization Owner approval** and max expiration lifetimes (`<=30–90 days`) on **Fine-grained PATs**
- **E.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 60. When calling `POST /app/installations/{installation_id}/access_tokens` to mint a 1-hour **GitHub App installation token**, how can the caller **further down-scope** that single 1-hour token to **just 1 repository** and **`Read-only` contents** (`even if the App is installed on 50 repos with Write`)?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Signing a short-lived **RS256 JWT** (`<=10 minutes`) with the **GitHub App private key** to call `POST /app/installations/{installation_id}/access_tokens` and mint a **1-hour** installation token
- **C.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 61. How many **GitHub App private keys (`.pem`)** can exist temporarily on a GitHub App registration (`e.g., generating key #2, deploying it to Vault, verifying token minting, and deleting key #1`) to achieve **zero-downtime key rotation**?

- **A.** Enabling **OAuth App access restrictions** and **GitHub App installation approval workflows** so developer-requested integrations stay blocked on private org data until vetted and approved by an Organization/Enterprise Owner
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 62. When a GitHub App registration has **`Visibility = Private`** (`Only on this account`) vs **`Internal`** (`Any account in the ZephyrAero enterprise`), what does **`Enterprise-internal` GitHub App visibility** unlock?

- **A.** Enabling **OAuth App access restrictions** and **GitHub App installation approval workflows** so developer-requested integrations stay blocked on private org data until vetted and approved by an Organization/Enterprise Owner
- **B.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

---

## Domain 4 — Manage GitHub Actions (20–25% official weight · 24 questions)

### 63. `ZephyrAero` standardizes DO-178C static analysis and artifact attestation across 28 organizations. Which two practices enable secure cross-org workflow reuse? Select two.

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Enforce **`Require actions to be pinned to a full-length commit SHA`**, restrict allowed actions to verified/internal sources, and default `GITHUB_TOKEN` to **`Read-only`**
- **E.** Host reusable workflows (`workflow_call`) and composite actions in **`Internal`** enterprise repositories with cross-organization workflow `Access` enabled

### 64. Which built-in GitHub Actions feature (`actions/attest-build-provenance@v1` with `permissions: attestations: write, id-token: write`) generates cryptographically signed **SLSA build provenance attestations** verified via `gh attestation verify`?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Sharing reusable workflows (`on: workflow_call`) and composite actions in **`Internal`** or **`Private`** repositories with `Settings -> Actions -> General -> Access` enabled for organization/enterprise workflows
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 65. Compare the three custom **GitHub Action** execution types (`JavaScript`, `Docker container`, and `Composite`): which type runs **ONLY on Linux runners** vs natively across **Linux, Windows, and macOS**?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Sharing reusable workflows (`on: workflow_call`) and composite actions in **`Internal`** or **`Private`** repositories with `Settings -> Actions -> General -> Access` enabled for organization/enterprise workflows

### 66. Which two enterprise controls block supply-chain poisoning of community Actions and unauthorized execution on avionics hardware-in-the-loop (`HIL`) runners? Select two.

- **A.** Isolate **Larger** and **ephemeral (`--ephemeral` / `ARC`) self-hosted runners** inside **Runner Groups** restricted to selected repositories and trusted reusable workflows
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **E.** Enforce **`Require actions to be pinned to a full-length commit SHA`**, restrict allowed actions to verified/internal sources, and default `GITHUB_TOKEN` to **`Read-only`**

### 67. If an Enterprise Owner sets the Enterprise Actions policy to **`Disable Actions`** on 3 legacy document-only archive organizations while enabling **`Allow select actions and reusable workflows`** on 25 active software organizations, which Enterprise policy option supports per-org scoping?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Enforcing **Allowed actions and reusable workflows** (`GitHub-created`, `Verified creators`, internal patterns) plus **`Require actions to be pinned to a full-length commit SHA`**, `Read-only` default `GITHUB_TOKEN`, and fork PR approval
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 68. Why is combining trigger **`on: pull_request_target`** with `uses: actions/checkout@v4` configured with **`ref: ${{ github.event.pull_request.head.sha }}`** a critical `P0` vulnerability (`"Pwn Request"`) on repositories accepting fork PRs?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **C.** Enforcing **Allowed actions and reusable workflows** (`GitHub-created`, `Verified creators`, internal patterns) plus **`Require actions to be pinned to a full-length commit SHA`**, `Read-only` default `GITHUB_TOKEN`, and fork PR approval
- **D.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing

### 69. `ZephyrAero` runs real-time flight-simulator tests on **Larger GitHub-hosted runners** and **ARC** Kubernetes scale sets. Which three controls belong in this architecture? Select three.

- **A.** Isolate **Larger** and **ephemeral (`--ephemeral` / `ARC`) self-hosted runners** inside **Runner Groups** restricted to selected repositories and trusted reusable workflows
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Connect **Linux/Windows Larger GitHub-hosted runners** to an **Azure VNet** via `GitHub.Network/networkSettings` and Enterprise **Network Configurations**
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **E.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **F.** Protect production deployments using **Environment Required Reviewers** + **OIDC (`id-token: write`)** federated to **HashiCorp Vault / Azure Key Vault** with strict `sub` claims

### 70. How should the Kubernetes **`gha-runner-scale-set`** Helm chart in **Actions Runner Controller (`ARC`)** authenticate to the `ZephyrAero` GitHub Enterprise/Organization (`preferring which credential over a personal PAT`)?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Organizing **Enterprise & Organization Runner Groups** restricted to selected repos and workflows, scaling **Larger GitHub-hosted runners** or ephemeral (`--ephemeral`) self-hosted runners via **Actions Runner Controller (`ARC`)** on Kubernetes
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 71. Besides multi-core Linux/Windows/macOS **Larger runners**, which specialized hardware SKU of **GitHub-hosted Larger runners** accelerates ML model quantization, shader compilation, and CUDA avionics vision tests without managing self-hosted GPU servers?

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Provisioning **ephemeral self-hosted runners** (`./config.sh --ephemeral` or REST **JIT runner** configs via **Actions Runner Controller `ARC`**) that execute **exactly one job** and self-destruct cleanly
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges

### 72. `ZephyrAero` connects 32-core Linux **Larger GitHub-hosted runners** into a private Azure VNet (`10.90.0.0/23`) to fetch Wind River RTOS toolchains from a private internal server. Which four-step configuration sequence applies?

- **A.** Whitelist only Microsoft Azure IP ranges on standard Linux hosted runners → skip Azure VNet configuration → disable outbound access to github.com endpoints → run workflows
- **B.** Have an Organization Owner create a new Network Configuration while Enterprise policy blocks org configs → skip Azure resource ID linkage → assign to repository secrets → test
- **C.** Delegate Azure VNet subnet to GitHub.Network & create NetworkSettings → create GitHub Network Configuration → attach it to a Linux/Windows Larger runner group → scope runner group to approved repos/workflows
- **D.** Attach Azure VNet directly to free standard ubuntu-latest runners or macOS arm64 larger runners → skip GitHub.Network subnet delegation → allow all public fork PRs onto the private VNet runner group

### 73. Which two administrative requirements apply when deploying **Azure Private Networking** for GitHub-hosted runners? Select two.

- **A.** Isolate **Larger** and **ephemeral (`--ephemeral` / `ARC`) self-hosted runners** inside **Runner Groups** restricted to selected repositories and trusted reusable workflows
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **E.** Connect **Linux/Windows Larger GitHub-hosted runners** to an **Azure VNet** via `GitHub.Network/networkSettings` and Enterprise **Network Configurations**

### 74. An iPad Electronic Flight Bag (`EFB`) mobile squad creates an `arm64` `macos-15-xlarge` **Larger runner** and tries to attach `ZephyrAero`'s **Azure Private Network (`VNet`)** configuration to it so simulator tests reach `10.90.1.50`. Proposed solution: Attach the Azure VNet Network Configuration to the `arm64` macOS Larger runner. Will GitHub allow attaching Azure VNet networking to `arm64` macOS Larger runners?

- **A.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **B.** No — **Azure Private Networking** (`VNet` integration) and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, NOT on standard free runners or `arm64` macOS Larger runners
- **C.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **D.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret

### 75. A Linux self-hosted runner fails job checkout with `fatal: unable to access 'https://github.com/...': SSL certificate problem: self-signed certificate in certificate chain` even after setting `NODE_EXTRA_CA_CERTS` (`because step git CLI uses libcurl/OpenSSL, not Node TLS!`). Which runner variable or host config makes `git` inside `actions/checkout` trust the corporate Root CA?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Inspecting self-hosted runner **`_diag/Runner_*.log`** (registration, listener, network/proxy errors) and **`_diag/Worker_*.log`** (job step execution), `svc.sh status`, tool-cache disk usage, and Actions queue time metrics
- **D.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

### 76. What happens if two separate self-hosted runner VMs are accidentally cloned from a VMware snapshot that **already ran `./config.sh`** (`sharing the exact same .runner and .credentials_rsaparams identity files`)?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Inspecting self-hosted runner **`_diag/Runner_*.log`** (registration, listener, network/proxy errors) and **`_diag/Worker_*.log`** (job step execution), `svc.sh status`, tool-cache disk usage, and Actions queue time metrics
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 77. When configuring outbound firewall rules for a private self-hosted runner connecting to **GitHub Enterprise Cloud**, besides `github.com` and `api.github.com`, why must HTTPS `443` egress also allow `*.actions.githubusercontent.com` and `*.blob.core.windows.net`?

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

### 78. In a deployment pipeline (`build -> deploy-staging -> deploy-prod`), how many **Required reviewer** individuals or teams (`up to ____ reviewers/teams`, where approval from any `1` entity satisfies the gate—or combine multiple chained environments/custom rules for multi-party sign-off) can be listed on a single GitHub **Deployment Environment**?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Scoping encrypted secrets across **Organization -> Repository -> Environment** where **most specific wins (`Environment > Repository > Organization`)**, gated by Environment **Required reviewers** and **Deployment branches/rulesets**

### 79. An Organization Admin sets an Organization Configuration Variable `LOG_LEVEL = WARN`, while repository `zephyraero/radar` defines a Repository Configuration Variable `LOG_LEVEL = DEBUG`. Proposed solution: Assume `vars.LOG_LEVEL` evaluates to `WARN` because Organization Configuration Variables override Repository Configuration Variables. Which value does `${{ vars.LOG_LEVEL }}` return inside `zephyraero/radar`?

- **A.** No — an organization’s default **Security Configuration** auto-attaches only to **newly created** repositories; repositories **transferred** into the organization must have the Security Configuration attached manually or via API
- **B.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **C.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret
- **D.** No — **Azure Private Networking** (`VNet` integration) and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, NOT on standard free runners or `arm64` macOS Larger runners

### 80. Which webhook event (`____`) does GitHub send to a registered **Custom deployment protection rule** GitHub App whenever a workflow job reaches a gated Environment?

- **A.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Enforcing **Custom Deployment Protection Rules** (backed by a GitHub App checking ServiceNow change tickets or Datadog SLOs) alongside human Required Reviewers on `production` Environments
- **D.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges

### 81. Can **Dependabot** secrets and **Codespaces** secrets share the exact same secret store automatically with **GitHub Actions** secrets, or does GitHub isolate secrets into **three** separate feature stores under `Settings -> Secrets and variables`?

- **A.** Configuring Organization secrets restricted to **`Selected repositories`** (or `Private and internal`), encrypting REST API secret uploads with the org/repo **LibSodium public key**, and separating non-sensitive **`vars`** from `secrets`
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 82. Using the **GitHub CLI (`gh`)**, which command (`gh secret set DEPLOY_KEY --org zephyraero-flight --____ selected --repos autopilot,fms`) encrypts and uploads a scoped Organization secret cleanly from an automated rotation job?

- **A.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **B.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Configuring Organization secrets restricted to **`Selected repositories`** (or `Private and internal`), encrypting REST API secret uploads with the org/repo **LibSodium public key**, and separating non-sensitive **`vars`** from `secrets`

### 83. If a job generates a dynamic temporary token at runtime in Step 1 (`TOKEN=$(fetch-token)`), which workflow command (`echo "::add-____::$TOKEN"`) registers that dynamic string with the runner log masker **before** passing it to `$GITHUB_OUTPUT`?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Configuring Organization secrets restricted to **`Selected repositories`** (or `Private and internal`), encrypting REST API secret uploads with the org/repo **LibSodium public key**, and separating non-sensitive **`vars`** from `secrets`

### 84. `ZephyrAero` integrates **GitHub Actions** with **AWS Secrets Manager / STS** via **OIDC** so avionics artifact-signing jobs never touch static IAM keys. Which four-step rollout order applies?

- **A.** Export static cloud admin keys into a public repository → commit .env to main → skip OIDC subject claim validation → rotate keys every 5 years
- **B.** Request an OIDC JWT first without configuring any Federated Identity Credential in Azure/Vault → hardcode client secrets when OIDC fails → grant write-all to fork PRs
- **C.** Trust wildcard sub: repo:* in AWS/Vault with no org filter → leave id-token: none in workflow YAML → store root Vault token in plain-text Actions vars → echo token in logs
- **D.** Configure OIDC trust policy in Vault/Azure/AWS with strict sub/aud claims → set job permissions id-token: write → exchange OIDC JWT at runtime for dynamic secret → delete static GitHub secrets

### 85. On a **GHEC with Data Residency** instance (`https://zephyraero.ghe.com`) or a self-hosted **GHES** instance, is the OIDC token **`iss` (`issuer`)** URL identical to `https://token.actions.githubusercontent.com`, or is it tenant/instance-specific?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Federating GitHub Actions (`permissions: id-token: write`) via **OpenID Connect (`OIDC`)** with **HashiCorp Vault**, **Azure Key Vault**, or **AWS Secrets Manager** using strict `sub` (`repo:`/`environment:`) and `aud` claims
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

### 86. Why does an **Azure Key Vault / Entra ID Federated Identity Credential** reject a GitHub Actions OIDC login if your workflow runs on a Pull Request (`on: pull_request`) while the Entra credential's `Subject identifier` is configured as `repo:zephyraero/autopilot:ref:refs/heads/main`?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Federating GitHub Actions (`permissions: id-token: write`) via **OpenID Connect (`OIDC`)** with **HashiCorp Vault**, **Azure Key Vault**, or **AWS Secrets Manager** using strict `sub` (`repo:`/`environment:`) and `aud` claims
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges

---

## Domain 5 — Monitor and optimize GitHub usage (10–15% official weight · 14 questions)

### 87. Avionics SOC engineers design continuous API abuse detection and 10-year FAA compliance retention. Which two capabilities satisfy both requirements? Select two.

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Correlate **Organization API Insights** (`rate-limited callers, top Apps/PATs`) with **Enterprise Audit Log** queries (`hashed_token`, `action:org.*`) to isolate noisy tokens
- **C.** Configure real-time **Enterprise Audit Log Streaming** (with optional Git events) to encrypted SIEM/WORM storage (`Azure Event Hubs`, `Blob`, `S3`, `Splunk`)
- **D.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **E.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 88. In the **Enterprise Audit Log**, an admin searches `action:org.credential_authorization.grant` and `action:personal_access_token.request_approved`. What security lifecycle events do those two queries audit?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Querying the **Enterprise Audit Log** (`action:`, `actor:`, `hashed_token:`) and **Organization API Insights** (`time-series requests, rate-limited callers, top GitHub Apps, OAuth Apps, and PATs`) to pinpoint noisy/failing integrations

### 89. When **API Insights** shows `22%` of requests from an internal dashboard app failing with `429` / `403` during top-of-the-hour `:00` cron spikes (`every repo cron firing at 0 * * * *`), what simple YAML adjustment smooths both API rate limits and runner queue spikes?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Querying the **Enterprise Audit Log** (`action:`, `actor:`, `hashed_token:`) and **Organization API Insights** (`time-series requests, rate-limited callers, top GitHub Apps, OAuth Apps, and PATs`) to pinpoint noisy/failing integrations

### 90. On self-hosted **GHES**, which CLI command (`ghe-config app.github.collectd-____` / Management Console **Monitoring**) exports appliance CPU, disk IOPS, memory, and network counters to an external Graphite/Collectd or SNMPv3 NMS alongside Prometheus?

- **A.** Scraping **GHES Prometheus `/metrics`** (or forwarding `syslog` + `SNMP` health traps) to alert platform SREs proactively on disk IOPS saturation, Redis/MySQL replication lag, and CPU load
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 91. Before escalating a failing **SAML SSO** login to GitHub Support, which browser diagnostic artifact (`a redacted ____ capture` or decoded SAML `Response` XML showing `Issuer`, `Audience`, `Recipient`, and `NameID`) helps an admin immediately spot clock-skew (`NotBefore`/`NotOnOrAfter`) or wrong ACS URLs?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Using GHES **Management Console / Grafana / `ghe-diagnostics` / Activity Dashboard** (or `githubstatus.com` + Enterprise Support portal with `Support Admin` entitlement on GHEC) to separate local misconfiguration from platform incidents

### 92. On self-hosted **GHES**, why must **Network Time Protocol (`NTP`)** stay tightly synchronized across primary, HA replica, and IdP servers?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Using GHES **Management Console / Grafana / `ghe-diagnostics` / Activity Dashboard** (or `githubstatus.com` + Enterprise Support portal with `Support Admin` entitlement on GHEC) to separate local misconfiguration from platform incidents

### 93. Under `Enterprise -> Policies -> Copilot`, an admin wants to automatically reclaim **GitHub Copilot** seats from developers with zero activity, or audit seat utilization programmatically. Which two fields in `GET /orgs/{org}/copilot/billing/seats` reveal seat assignment date vs actual IDE/Chat usage?

- **A.** Querying the **GitHub Copilot User Management & Metrics REST APIs** (`last_activity_at`, `last_activity_editor`, acceptance/chat telemetry) to automate seat reclamation for inactive assignees
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 94. Which organization-level engineering velocity view (`Insights -> ____` or Pull Request / Actions metrics) helps platform teams spot repositories where Pull Requests wait `>6 days` for first review despite `5-minute` CI builds?

- **A.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Evaluating **Copilot Metrics API / Usage Dashboard** (active vs assigned seats, IDE/Chat/PR adoption), **Security Overview** coverage/MTTR, **Actions Usage Metrics**, and **GHES Dormant Users** reports to find underutilized features

### 95. In **Security Overview**, what is the difference between the **`Risk`** view and the **`Coverage`** view for an Enterprise Security Manager?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Using **Enterprise/Organization Security Overview** (`Risk` and `Coverage` dashboards) to audit GHAS enablement gaps, open critical `CodeQL`/Secret/Dependabot alerts, and remediation MTTR
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO

### 96. Which two FinOps practices let `ZephyrAero` allocate multi-organization cloud charges accurately across `Flight Controls`, `Propulsion`, and `Cabin Systems`? Select two.

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Assign orgs/repos to **Cost Centers** with **75/90/100% Budget alerts**, add `actions/cache`, shorten artifact `retention-days`, and move Linux workloads off `macos` runners
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Suspend/offboard **dormant users**, cancel stale pending org invitations, and audit **90-day active GHAS committers** plus **Copilot Metrics API** active-seat ratios
- **E.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 97. In GitHub's **Enhanced Billing Platform**, can a single repository belong to **two different Cost Centers** at the exact same moment, and what happens when you assign an entire **Organization** to Cost Center `CC-Avionics` while moving one shared repo `zaero/design-system` to `CC-Platform`?

- **A.** Analyzing **Enhanced Billing Platform** usage exports, **Cost Centers**, **Budgets & 75/90/100% alerts**, OS runner minute multipliers (`Linux < Windows < macOS`), shared **Actions/Packages storage**, and **90-day unique GHAS committers**
- **B.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 98. Do **self-hosted runners** (`including Kubernetes ARC pods running on your own EKS/AKS nodes`) consume any metered **GitHub Actions per-minute runner compute charges** from GitHub?

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Analyzing **Enhanced Billing Platform** usage exports, **Cost Centers**, **Budgets & 75/90/100% alerts**, OS runner minute multipliers (`Linux < Windows < macOS`), shared **Actions/Packages storage**, and **90-day unique GHAS committers**
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 99. `ZephyrAero` prepares for an annual license optimization review across `GHEC`, `GHES`, `GHAS`, `Copilot`, and `Actions`. Which four-step FinOps workflow applies?

- **A.** Export consumed-licenses & verify GitHub Connect GHES sync → audit dormant users, duplicate emails, and 90-day GHAS committers → reclaim idle seats & right-size budgets → enforce SCIM offboarding & alerts
- **B.** Hard-delete departing employees personal GitHub accounts via Support → break PR review audit history → turn off Dependabot and CodeQL everywhere → cancel Enterprise support
- **C.** Assign every contractor Enterprise Owner and Copilot Enterprise on day one → run Linux CI jobs on 10x-multiplier macOS runners → store 500 GB build artifacts for 400 days → review bills annually
- **D.** Delete historical employee Git commits to free GHAS seats immediately → disable GitHub Connect so GHEC+GHES users are billed twice → set unlimited Actions spending limits → skip budgets

### 100. A monorepo PR workflow lacks `concurrency:` cancellation (`running 6 superseded 45-minute matrix builds in parallel`), while 30 retired engineers still hold active EMU seats. Proposed solution: Add `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on PR runs AND deprovision the 30 retired EMUs via SCIM. Does this cut Actions waste while preserving DO-178C commit history?

- **A.** No — suspending a dormant GHES user or removing/SCIM-deprovisioning a GHEC member **frees their Enterprise license seat** while **preserving all historical commits, Issues, and Pull Request audit trails**
- **B.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret
- **C.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **D.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement

---

## Answer Key and Explanations

### Question 1 — `C, D` (Manage GitHub identities and access)

Correct answers: C and D (are correct). Corporate **EMUs** govern lifecycle via IdP/SCIM while forbidding public repos/Gists, and assigning FAA auditors the **Guest Collaborator** IdP role blocks `Internal` repository visibility. [Skill 1.1: Describe differences between managed users and personal accounts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: About Enterprise Managed Users vs personal accounts (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. EMUs ensure corporate lifecycle control and eliminate accidental public repo or Gist leakage under managed handles.
- **D:** Correct. Guest Collaborators prevent contractors in EMU enterprises from automatically reading all `Internal` repositories across member organizations.
- **E:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 2 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). No — in an **EMU** enterprise, user-namespace repositories and **GitHub Gists** (`both public and secret`) are completely disabled; repositories exist strictly inside Enterprise-owned Organizations! [Skill 1.1: Describe differences between managed users and personal accounts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: About Enterprise Managed Users vs personal accounts (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users)]

- **A:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **B:** Correct. EMUs give enterprises full lifecycle ownership over user accounts via SAML/OIDC + SCIM while preventing public code/Gist creation and external repository contributions.
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 3 — `C` (Manage GitHub identities and access)

Correct answer: C (is correct). Zero commits or PRs were deleted; once assigned to the corporate IdP app, removed/unlinked members authenticate via `https://github.com/orgs/zephyraero-sim/sso` (`or accept an SSO-protected org invitation`) to restore access! [Skill 1.2: Configure and enforce SAML SSO and 2FA | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing SAML single sign-on and two-factor authentication (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise)]

- **A:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Correct. Enforcing SAML SSO at the Enterprise level centralizes IdP authentication across all member organizations, requires credential authorization for PATs/SSH keys, and pairs with `2FA` on personal-account GHEC.
- **D:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.

### Question 4 — `C` (Manage GitHub identities and access)

Correct answer: C (is correct). If an employee changes their surname/email and `NameID` changes unpredictably without SCIM updating `NameID`, GitHub rejects SAML login as a mismatched identity binding! [Skill 1.2: Configure and enforce SAML SSO and 2FA | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing SAML single sign-on and two-factor authentication (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise)]

- **A:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **B:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **C:** Correct. Enforcing SAML SSO at the Enterprise level centralizes IdP authentication across all member organizations, requires credential authorization for PATs/SSH keys, and pairs with `2FA` on personal-account GHEC.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 5 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). Create the EMU enterprise and vault recovery codes for `<shortcode>_admin`, configure OIDC/SAML SSO using the setup user, enable SCIM user/group provisioning in Entra ID, and map IdP groups to teams. [Skill 1.3: Understand SCIM and team synchronization: implementation and key differences | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring SCIM provisioning vs IdP team synchronization (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim/provisioning-users-and-groups-with-scim-using-the-rest-api)]

- **A:** Correct. Correct order: establish the EMU enterprise and offline recovery codes, wire SAML/OIDC SSO using the initial setup user, turn on SCIM user/group provisioning, and map IdP groups to teams.
- **B:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMU accounts; EMUs are brand-new IdP-provisioned accounts.
- **C:** Incorrect. Reverses prerequisite dependencies: SCIM and IdP group synchronization cannot run before the EMU enterprise exists and SAML/OIDC SSO is configured.
- **D:** Incorrect. SCIM on EMUs requires SAML or OIDC SSO first, and sharing setup credentials or granting universal Enterprise Owner violates least privilege.

### Question 6 — `C` (Manage GitHub identities and access)

Correct answer: C (is correct). No — personal-account **Team Synchronization** only syncs team membership for accounts that **already belong** to the GitHub Organization (`invite them to the org first, or use EMUs with SCIM user provisioning`)! [Skill 1.3: Understand SCIM and team synchronization: implementation and key differences | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring SCIM provisioning vs IdP team synchronization (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim/provisioning-users-and-groups-with-scim-using-the-rest-api)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — personal-account **Team Synchronization** only syncs team membership for accounts that **already belong** to the GitHub Organization (`invite them to the org first, or use EMUs with SCIM user provisioning`)!
- **B:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **C:** Correct. Personal-account Team Sync (`Entra ID`/`Okta`) never adds non-members into an organization; users must join the org via SAML/SCIM invitation first (or deploy GHEC with EMUs).
- **D:** Incorrect. While Enterprise teams excel at cross-org access, Copilot licensing, custom enterprise roles, and ruleset bypasses, `CODEOWNERS` requires Organization teams or individual users with Write+ access.

### Question 7 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Entra ID **OIDC** eliminates manual X.509 SAML signing-certificate rotation and automatically enforces **Entra Conditional Access Policies (`CAP`)** across web and token flows! [Skill 1.4: Choose and configure identity providers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Choosing and configuring Identity Providers (Entra ID, Okta, PingFederate, CAS/LDAP) (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-identity-and-access-management)]

- **A:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **D:** Correct. Configuring OIDC between Entra ID and GHEC EMUs validates Entra Conditional Access Policies during browser sign-in and token refresh Flows.

### Question 8 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). GHES periodically polls mapped Active Directory LDAP Distinguished Names (`DNs`) to keep Organization team memberships synchronized automatically (`and suspends disabled AD users`)! [Skill 1.4: Choose and configure identity providers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Choosing and configuring Identity Providers (Entra ID, Okta, PingFederate, CAS/LDAP) (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-identity-and-access-management)]

- **A:** Correct. GHEC EMUs support Entra ID (OIDC or SAML), Okta, and PingFederate (plus custom SAML+SCIM API integration), while GHES adds native LDAP, Active Directory, and CAS authentication.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 9 — `C, D` (Manage GitHub identities and access)

Correct answers: C and D (are correct). Download and vault **Enterprise/Organization SAML recovery codes** prior to enforcement, and verify developers **authorize** SSH keys and PATs (`Configure SSO`) for SAML-protected orgs. [Skill 1.5: Explain GitHub’s authentication and authorization model | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub authentication and authorization model (SSH, PAT, OAuth, SAML, OIDC) (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)]

- **A:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Correct. SAML enforcement blocks un-authorized programmatic credentials (PATs and SSH keys) even when owned by valid organization members.
- **D:** Correct. Storing SAML recovery codes offline prevents total administrative lockout if the corporate Identity Provider experiences a certificate or service outage.
- **E:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 10 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). Revoking organization SAML authorization (`or revoking org Fine-grained PAT access`) immediately strips **authorization** to `@zaero-supplier` without deleting Priya's underlying personal GitHub identity! [Skill 1.5: Explain GitHub’s authentication and authorization model | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub authentication and authorization model (SSH, PAT, OAuth, SAML, OIDC) (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Correct. Even a valid personal PAT or SSH key (`authenticated`) is blocked from accessing a SAML-enforced GHEC organization until explicitly **authorized** for SAML SSO (`authorized`).
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 11 — `C` (Manage GitHub identities and access)

Correct answer: C (is correct). Assigning the **`Billing Manager`** enterprise role grants billing, cost-center, and budget administration without granting source-code access or consuming a paid Enterprise user seat! [Skill 1.6: Configure organization and repository roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization roles, custom roles, and repository roles (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-organization-roles)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. Custom enterprise roles delegate narrow slices of enterprise administration without exposing full owner control over SAML, billing, or organization deletion.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 12 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Every single Organization Member immediately gains `git push` **`Write` access to every private and internal repository** in the organization—always lock **`Base permissions = None`** (`or Read` strictly for open InnerSource orgs) and grant `Write` via Teams! [Skill 1.6: Configure organization and repository roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization roles, custom roles, and repository roles (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-organization-roles)]

- **A:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **B:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Correct. GitHub layers additive repository roles (`most permissive wins`) with least-privilege built-in and custom organization/enterprise roles.

### Question 13 — `C, D, F` (Manage GitHub identities and access)

Correct answers: C, D, and F (are correct). Manage **Copilot licenses**, **custom enterprise roles**, and **ruleset bypasses** via Enterprise teams; assign Enterprise teams directly across organizations; and set **`Base permissions = None`**. [Skill 1.7: Define and manage enterprise teams | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining and managing Enterprise teams across organizations (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. IdP-synced Enterprise teams require zero manually added members and pause synchronization whenever the linked IdP group exceeds 5,000 users.
- **C:** Correct. Setting Base permissions to `None` prevents newly added org members from automatically reading or writing every private repository in the organization.
- **D:** Correct. Enterprise team organization assignments add members directly without invitations and protect enterprise-granted baseline access from org-level removal.
- **E:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **F:** Correct. Enterprise teams streamline multi-org role delegation, enterprise-level Copilot seat assignment, and ruleset bypass administration.

### Question 14 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). No — **Enterprise teams** have a flat structure (**no nested parent/child Enterprise teams** and **no `Team Maintainer` role**; membership is governed via EMU IdP groups + Enterprise Owners/custom roles)! [Skill 1.7: Define and manage enterprise teams | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining and managing Enterprise teams across organizations (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise)]

- **A:** Incorrect. Personal-account Team Sync (`Entra ID`/`Okta`) never adds non-members into an organization; users must join the org via SAML/SCIM invitation first (or deploy GHEC with EMUs).
- **B:** Correct. While Enterprise teams excel at cross-org access, Copilot licensing, custom enterprise roles, and ruleset bypasses, `CODEOWNERS` requires Organization teams or individual users with Write+ access.
- **C:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — **Enterprise teams** have a flat structure (**no nested parent/child Enterprise teams** and **no `Team Maintainer` role**; membership is governed via EMU IdP groups + Enterprise Owners/custom roles)!
- **D:** Incorrect. Standard hosted runners cannot join customer Azure VNets, and arm64 macOS Larger runners do not support Azure private networking or static IP assignment.

### Question 15 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). Members of `@/ent:security-champions` can merge a Pull Request without satisfying every required review/status check during declared emergencies (`while still blocking raw direct git push bypasses outside a PR`)! [Skill 1.7: Define and manage enterprise teams | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining and managing Enterprise teams across organizations (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise)]

- **A:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **B:** Correct. Enterprise teams simplify multi-org governance, Copilot licensing, custom enterprise role delegation, and ruleset bypasses—though they do not support `CODEOWNERS`, nesting, Secret visibility, or non-EMU Team Sync.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. IdP-synced Enterprise teams require zero manually added members and pause synchronization whenever the linked IdP group exceeds 5,000 users.

### Question 16 — `C` (Manage GitHub identities and access)

Correct answer: C (is correct). Calling `GET /repos/{owner}/{repo}/collaborators/{username}/permission` resolves direct, Organization-team, Enterprise-team, and base permissions into the user's effective role! [Skill 1.8: Audit access and permissions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Auditing repository, organization, and enterprise access permissions (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/identifying-audit-log-events-performed-by-an-access-token)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. Admins audit effective access via People exports, repository Manage Access filters, REST/GraphQL permission queries, and Audit Log token attribution fields.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 17 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). Only **Organization Owners** can invite external non-member collaborators (`or add Guest Collaborators via IdP on EMUs`), stopping local repo admins from creating shadow external access paths! [Skill 1.8: Audit access and permissions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Auditing repository, organization, and enterprise access permissions (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/identifying-audit-log-events-performed-by-an-access-token)]

- **A:** Correct. Admins audit effective access via People exports, repository Manage Access filters, REST/GraphQL permission queries, and Audit Log token attribution fields.
- **B:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 18 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Mark the Custom Property **`Required`** and configure a **`Default value`** (`DAL-A`) while restricting value edits to Organization Owners! [Skill 1.9: Manage settings, policies, rulesets, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing enterprise member privileges, policies, repository rulesets, and bypass roles (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Correct. Organization and Enterprise admins enforce schema-validated Custom Properties on repos and bind Rulesets to property queries (`compliance_tier:pci`) automatically.

### Question 19 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). Configuring a **Branch naming restriction** (`regex / fnmatch pattern` inside an Organization/Enterprise Ruleset) blocks non-conforming branch names pre-receive! [Skill 1.9: Manage settings, policies, rulesets, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing enterprise member privileges, policies, repository rulesets, and bypass roles (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise)]

- **A:** Correct. Enterprise policies set hard guardrails across all organizations, while Repository Rulesets layer additive branch/tag/push protections (`most restrictive wins`) with auditable bypasses.
- **B:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 20 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). **GitHub Enterprise Support** (`and Account teams`) assist with restricted backend enterprise slug/plan operations, whereas **internal Enterprise/Org Admins** manage Rulesets, teams, and repository configurations! [Skill 2.1: Identify issues resolvable by admins vs GitHub Support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Identifying issues resolvable by Enterprise Admins vs GitHub Enterprise Support (https://docs.github.com/en/enterprise-cloud@latest/support/learning-about-github-support/about-github-support)]

- **A:** Correct. Admins handle internal identity, permissions, and pipeline configs, while GitHub Support handles cloud infrastructure incidents, server-side cache purges, and backend appliance/cloud escalations.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 21 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). No — `100 MB` is GitHub's documented hard per-blob Git object limit; **internal Admins/Developers** track large binary assets using **Git Large File Storage (`Git LFS`)** or publish build artifacts to **GitHub Packages / Releases**! [Skill 2.1: Identify issues resolvable by admins vs GitHub Support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Identifying issues resolvable by Enterprise Admins vs GitHub Enterprise Support (https://docs.github.com/en/enterprise-cloud@latest/support/learning-about-github-support/about-github-support)]

- **A:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **B:** Correct. Admins handle internal identity, permissions, and pipeline configs, while GitHub Support handles cloud infrastructure incidents, server-side cache purges, and backend appliance/cloud escalations.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 22 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). Run local admin triage (`ghe-diagnostics`) and record UTC timestamps, generate `ghe-support-bundle -x` via SSH port `122`, sanitize ITAR-controlled strings per compliance policy, and upload the bundle on the GitHub Enterprise Support portal. [Skill 2.2: Generate support bundles and diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Generating GHES support bundles, ghe-diagnostics, and ticket diagnostics (https://docs.github.com/en/enterprise-server@latest/support/contacting-github-support/providing-data-to-github-support)]

- **A:** Incorrect. Never expose appliance secrets publicly or perform multi-version upgrades mid-incident without diagnostics.
- **B:** Correct. Correct escalation workflow: verify local admin triage and timestamps, generate an extended support bundle (`ghe-support-bundle -x`), verify compliance hygiene, and attach it on the Support portal.
- **C:** Incorrect. Corporate IdP/Active Directory password resets are strictly an internal administrator responsibility, not a GitHub Support issue.
- **D:** Incorrect. Wiping logs destroys root-cause evidence before capturing a support bundle, and GitHub Support never SSHes directly into customer GHES appliances.

### Question 23 — `B, C` (Administer GitHub Enterprise environment)

Correct answers: B and C (are correct). Register regional SRE leads as entitled **Support** portal members, and standardize capturing extended historical logs with **`ghe-support-bundle -x`**. [Skill 2.2: Generate support bundles and diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Generating GHES support bundles, ghe-diagnostics, and ticket diagnostics (https://docs.github.com/en/enterprise-server@latest/support/contacting-github-support/providing-data-to-github-support)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Correct. Extended support bundles give GitHub Support complete service, cluster, and error telemetry without exposing your appliance to external SSH.
- **C:** Correct. Enterprise Owners explicitly grant support-portal entitlement to designated engineers rather than sharing a single Enterprise Owner login.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **E:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 24 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). Setting **`"filePatterns"`** inside `<template>.properties.json` recommends that starter workflow intelligently whenever a repository's root files match C/CMake patterns! [Skill 2.3: Recommend standards for developer processes | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending enterprise standards for developer collaboration and InnerSource (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-best-practices/organize-work)]

- **A:** Correct. Workflow templates in `<org>/.github/workflow-templates/` appear automatically in the `Actions -> New workflow` gallery for every repository in the organization.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 25 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). Committing **`.github/pull_request_template.md`** (in `<org>/.github` or individual repos) pre-fills structured compliance checklists in every new Pull Request! [Skill 2.3: Recommend standards for developer processes | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending enterprise standards for developer collaboration and InnerSource (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-best-practices/organize-work)]

- **A:** Correct. Enterprise developer standards combine golden template repositories, an org `.github` repo for default templates/policies, and `Internal` InnerSource visibility.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 26 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). GitHub automatically splits/bisects or evicts the offending PR from the queue without ever breaking `main`, re-testing remaining healthy PRs so `main` stays `100%` passing! [Skill 2.4: Define standards for workflows, branching, reviews, and releases | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining standards for workflows, branching, CODEOWNERS reviews, merge queues, and releases (https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)]

- **A:** Correct. Standardizing short-lived branches, Code Owner reviews, Merge Queue CI batching, and protected `v*` release tags keeps enterprise delivery predictable and auditable.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 27 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). GitHub natively verifies **SSH commit signatures** (`gpg.format = ssh`, using developer SSH signing keys) and **X.509 (`S/MIME`)** enterprise smartcard/PIV signatures (`plus automated web/API commits signed by GitHub`)! [Skill 2.4: Define standards for workflows, branching, reviews, and releases | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining standards for workflows, branching, CODEOWNERS reviews, merge queues, and releases (https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Correct. Standardizing short-lived branches, Code Owner reviews, Merge Queue CI batching, and protected `v*` release tags keeps enterprise delivery predictable and auditable.
- **C:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 28 — `A, D` (Administer GitHub Enterprise environment)

Correct answers: A and D (are correct). **GHEC with Data Residency** pins cloud storage to the selected region with mandatory **EMUs**, and hybrid `GHEC` + `GHES` Enterprise licensing deduplicates seats (`via GitHub Connect or manual license sync`). [Skill 2.5: Describe GitHub Enterprise deployment scenarios (GHEC with EMU, GHEC with Data Residency + EMU, GHEC with personal accounts, GHES) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise deployment models (GHEC+EMU, GHEC Data Residency ghe.com, GHEC personal, GHES) (https://docs.github.com/en/enterprise-cloud@latest/admin/overview/about-github-for-enterprises)]

- **A:** Correct. GHEC with Data Residency hosts code and metadata on a dedicated regional `.ghe.com` cloud stamp and always requires Enterprise Managed Users.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **D:** Correct. GitHub Connect correlates verified email addresses across GHES and GHEC and reconciles Visual Studio Enterprise/Pro with GitHub Enterprise entitlements.
- **E:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 29 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). **`ghe-backup`** runs **online** (`zero downtime`, taking incremental rsync/database snapshots while developers push), whereas **`ghe-restore`** onto a target replacement appliance requires **Maintenance Mode** on the source during final cutover! [Skill 2.5: Describe GitHub Enterprise deployment scenarios (GHEC with EMU, GHEC with Data Residency + EMU, GHEC with personal accounts, GHES) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise deployment models (GHEC+EMU, GHEC Data Residency ghe.com, GHEC personal, GHES) (https://docs.github.com/en/enterprise-cloud@latest/admin/overview/about-github-for-enterprises)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Correct. HA replication protects against primary VM hardware failure, while scheduled `backup-utils` snapshots on a separate host provide point-in-time disaster recovery.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 30 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). Exactly **`1`** GitHub Enterprise user seat—a single outside collaborator account deduplicates across all private repositories and organizations within the same Enterprise! [Skill 2.6: Explain licensing and billing models | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise licensing, metered user-based billing, and Visual Studio subscriptions (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/about-per-user-pricing)]

- **A:** Correct. One Enterprise user consumes a single seat across unlimited organizations in the enterprise (and synced GHES instances via GitHub Connect), while Actions, Packages, Codespaces, GHAS, and Copilot meter separately.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 31 — `D` (Administer GitHub Enterprise environment)

Correct answer: D (is correct). Like GHAS and Code Security, standalone **GitHub Secret Protection** on private/internal repositories is licensed per **unique active committer over the rolling 90-day window**! [Skill 2.6: Explain licensing and billing models | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise licensing, metered user-based billing, and Visual Studio subscriptions (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/about-per-user-pricing)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **D:** Correct. One Enterprise user consumes a single seat across unlimited organizations in the enterprise (and synced GHES instances via GitHub Connect), while Actions, Packages, Codespaces, GHAS, and Copilot meter separately.

### Question 32 — `D` (Administer GitHub Enterprise environment)

Correct answer: D (is correct). Inside `Organization Settings -> Code security -> Configurations` (`or Enterprise Billing & Licensing -> GitHub Advanced Security`), GitHub displays an **in-product pre-enablement seat estimator** calculating unique 90-day active committers across selected repositories! [Skill 2.7: Monitor license usage and consumption | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring enterprise license consumption and GitHub Connect license sync (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/viewing-license-usage-for-github-enterprise)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Correct. Pending org invitations, outside collaborators on private repos, enterprise members, and unsynced duplicate emails across GHES/GHEC all impact Enterprise license counts and must be audited regularly.

### Question 33 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). New user sign-ups / LDAP/SCIM provisioning are blocked once `100%` of licensed GHES seats (`.ghl`) are consumed—which is why proactive **dormant-user suspension** and threshold monitoring (`e.g., <85%`) are essential! [Skill 2.7: Monitor license usage and consumption | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring enterprise license consumption and GitHub Connect license sync (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/viewing-license-usage-for-github-enterprise)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Correct. Pending org invitations, outside collaborators on private repos, enterprise members, and unsynced duplicate emails across GHES/GHEC all impact Enterprise license counts and must be audited regularly.
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 34 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Confirm available 90-day committer seats, create the custom Enterprise Security Configuration, attach it to existing/transferred repos plus new-repo defaults, and set policy to `Enforce configuration`. [Skill 3.1: Define organization and enterprise policies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining organization and enterprise security policies and security configurations (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/about-security-configurations)]

- **A:** Incorrect. Settings left as `Not set` in a Security Configuration are explicitly not enforced against repository overrides.
- **B:** Incorrect. Manual per-repository toggling drifts immediately and misses centralized Security Configurations and enforcement.
- **C:** Incorrect. GHAS enablement fails if active-committer seats are exhausted, transferred repos require manual attachment, and disabling Actions breaks CodeQL default setup.
- **D:** Correct. Correct rollout: confirm active-committer license headroom, define the custom Security Configuration, apply it to existing/transferred repos and new-repo defaults, and enforce it.

### Question 35 — `B, D` (Implement secure software development and compliance)

Correct answers: B and D (are correct). Enforce an Enterprise/Org **Security Configuration** (`explicitly attaching migrated/transferred repos`), and enable **Secret Scanning Push Protection + Validity Checks + Delegated Bypass**. [Skill 3.1: Define organization and enterprise policies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining organization and enterprise security policies and security configurations (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/about-security-configurations)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Correct. Push Protection blocks secrets pre-receive, validity checks highlight live active credentials, and delegated bypass routes false-positive overrides through security reviewers.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Correct. Enforced Security Configurations prevent repository admins from disabling mandatory Secret Protection, CodeQL, or Dependabot controls.
- **E:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 36 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). No — default Security Configurations apply **only** to **newly created** repositories, **never** automatically to **transferred** repositories (`attach the configuration explicitly via UI or REST API`)! [Skill 3.1: Define organization and enterprise policies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining organization and enterprise security policies and security configurations (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/about-security-configurations)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — default Security Configurations apply **only** to **newly created** repositories, **never** automatically to **transferred** repositories (`attach the configuration explicitly via UI or REST API`)!
- **B:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **C:** Incorrect. Deleting a file in a new commit never purges prior blob SHAs, and any exposed secret must be considered compromised and rotated immediately.
- **D:** Correct. GitHub applies default Security Configurations when a repository is newly created in the org, not when an existing repository is transferred in.

### Question 37 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Enabling **`Restrict file extensions`** (`exe`, `dll`, `jar`, `p12`, `pfx`) inside a Repository Ruleset rejects binary/certificate commits at `git push` time! [Skill 3.2: Strengthen enterprise security posture and data protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Strengthening enterprise security posture, SSH CAs, IP allow lists, and data protection (https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)]

- **A:** Correct. Push rulesets evaluate file paths, extensions, and blob sizes on `git push` before commits land on any branch in targeted repositories.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 38 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). SSH certificates include built-in cryptographic **`valid_before` expiration timestamps** (`e.g., 8–12 hours` minted per workday SSO login), so unrenewed laptop credentials expire automatically without manual key hunting! [Skill 3.2: Strengthen enterprise security posture and data protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Strengthening enterprise security posture, SSH CAs, IP allow lists, and data protection (https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)]

- **A:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **B:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **C:** Correct. SSH CAs eliminate unrotated static personal SSH keys by requiring short-lived certificates signed by the corporate CA, paired with IP allow lists (or Entra CAPs).
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 39 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Controlling source archive/LFS bundling and disabling private forks reduces bulk unmonitored ZIP exfiltration paths outside audited Git/LFS transport logs! [Skill 3.2: Strengthen enterprise security posture and data protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Strengthening enterprise security posture, SSH CAs, IP allow lists, and data protection (https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Correct. SSH CAs eliminate unrotated static personal SSH keys by requiring short-lived certificates signed by the corporate CA, paired with IP allow lists (or Entra CAPs).
- **D:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.

### Question 40 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Provision an encrypted Azure Event Hubs namespace + least-privilege SAS credential, configure Event Hubs in Enterprise Audit Log Streaming, verify the test event and enable `Stream Git events`, and enforce WORM archival + Sentinel correlation rules. [Skill 3.3: Implement audit logging and reporting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Implementing audit logging, audit log streaming, and compliance reporting (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)]

- **A:** Incorrect. Audit log streaming is configured at the **Enterprise** level (capturing enterprise and member-organization events), not on an individual repository tab.
- **B:** Incorrect. GitHub retains non-Git audit events in the UI/API for a rolling window (up to 180 days; Git events shorter), so multi-year retention requires Audit Log Streaming.
- **C:** Correct. Correct audit-streaming setup: prepare the target sink, configure credentials in Enterprise Settings -> Audit log -> Log streaming, validate the test check, and enforce SIEM retention/alerting.
- **D:** Incorrect. Audit log streams support vetted encrypted sinks with strict verification, and audit access should use least-privilege custom roles rather than Enterprise Owner.

### Question 41 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). Yes — GitHub Enterprise Cloud supports configuring **up to two concurrent Audit Log Streaming sinks** (`e.g., cloud object storage for long-term WORM compliance + SIEM for real-time SOC alerting`)! [Skill 3.3: Implement audit logging and reporting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Implementing audit logging, audit log streaming, and compliance reporting (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Correct. Because UI/REST audit retention is time-bounded (180 days standard; shorter for high-volume Git events), compliance teams stream immutable audit events continuously to external SIEM/WORM storage.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 42 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Filter **Security Overview** directly by repository **Custom Properties** (`props.dal_level:DAL-A`), Organization, Team, Topic, or severity! [Skill 3.3: Implement audit logging and reporting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Implementing audit logging, audit log streaming, and compliance reporting (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)]

- **A:** Correct. Security Overview aggregates alert risk, push-protection metrics, and tool coverage across thousands of repositories for CISOs and Security Managers.
- **B:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.

### Question 43 — `A, C, E` (Implement secure software development and compliance)

Correct answers: A, C, and E (are correct). Enforce an Enterprise **Security Configuration**, activate **Secret Scanning Push Protection + Validity Checks + Delegated Bypass**, and run **CodeQL (`Advanced setup` for custom C++ builds, `Default` for Python) + Dependabot + PR Dependency Review**. [Skill 3.4: Configure vulnerability alerts, secret scanning, and CodeQL | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring vulnerability alerts, secret scanning push protection, and CodeQL code scanning (https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)]

- **A:** Correct. Push Protection blocks secrets pre-receive, validity checks highlight live active credentials, and delegated bypass routes false-positive overrides through security reviewers.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Correct. Combining CodeQL semantic analysis, Dependabot remediation PRs, and PR-time Dependency Review stops vulnerable code and packages before merge.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **E:** Correct. Enforced Security Configurations prevent repository admins from disabling mandatory Secret Protection, CodeQL, or Dependabot controls.
- **F:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 44 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Set `build-mode: manual` (`or omit autobuild`) between `codeql-action/init` and `codeql-action/analyze` and execute your exact `bazel build //...` command so CodeQL intercepts every compiler invocation! [Skill 3.4: Configure vulnerability alerts, secret scanning, and CodeQL | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring vulnerability alerts, secret scanning push protection, and CodeQL code scanning (https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)]

- **A:** Correct. CodeQL analyzes code semantically for CWE/OWASP flaws, while Secret Scanning Push Protection blocks credential commits pre-receive and verifies live token status via partner validity checks.
- **B:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 45 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Yes — uploading **`SARIF` (`Static Analysis Results Interchange Format` v2.1.0)** reports via `github/codeql-action/upload-sarif` unifies third-party and CodeQL findings in one Security Overview and PR gate! [Skill 3.4: Configure vulnerability alerts, secret scanning, and CodeQL | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring vulnerability alerts, secret scanning push protection, and CodeQL code scanning (https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Correct. CodeQL analyzes code semantically for CWE/OWASP flaws, while Secret Scanning Push Protection blocks credential commits pre-receive and verifies live token status via partner validity checks.

### Question 46 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Setting **`deny-licenses`** (or a strict `allow-licenses` allowlist such as `['MIT', 'Apache-2.0', 'BSD-3-Clause']`) fails the Pull Request check whenever a prohibited license enters the dependency tree! [Skill 3.5: Manage Dependabot and security advisories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing Dependabot alerts, security/version updates, private registries, and advisories (https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Correct. Dependabot flags known CVEs, opens automated upgrade PRs (authenticating to private registries when configured), blocks vulnerable PR dependencies via Dependency Review, and pairs with private Security Advisories.

### Question 47 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). Select **`Export SBOM`** inside `Insights -> Dependency graph` — or call the REST endpoint **`GET /repos/{owner}/{repo}/dependency-graph/sbom`**! [Skill 3.5: Manage Dependabot and security advisories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing Dependabot alerts, security/version updates, private registries, and advisories (https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Correct. Dependabot flags known CVEs, opens automated upgrade PRs (authenticating to private registries when configured), blocks vulnerable PR dependencies via Dependency Review, and pairs with private Security Advisories.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.

### Question 48 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Because Dependabot-triggered runs read **`Dependabot secrets`** (`not Actions secrets`) unless invoked appropriately, and `GITHUB_TOKEN` on Dependabot PRs defaults to read-only unless configured! [Skill 3.5: Manage Dependabot and security advisories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing Dependabot alerts, security/version updates, private registries, and advisories (https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Correct. Granting Dependabot private-registry credentials (and running Dependabot on VNet-connected Actions/ARC runners) lets Dependabot resolve internal Artifactory/NuGet/npm packages securely.
- **D:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.

### Question 49 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Immediately revoke & rotate the HSM PIN/credential on the HSM, scrub all refs with `git filter-repo`, force-push cleaned refs and have engineers re-clone, and submit unreachable commit SHAs to GitHub Support to purge caches. [Skill 3.6: Define and implement a security response plan | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining a security response plan and purging sensitive data from Git history (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]

- **A:** Incorrect. A normal `git rm` commit leaves the secret readable in prior commits and cached PR diffs, and unrotated leaked keys remain exploitable.
- **B:** Incorrect. GitHub Support cannot rotate third-party cloud credentials; the enterprise admin must revoke/rotate the secret immediately in AWS.
- **C:** Correct. Correct incident response: treat the secret as compromised (revoke/rotate first!), scrub history with `git filter-repo`, force-push cleaned refs, and ask GitHub Support to purge unreachable cached views.
- **D:** Incorrect. Archiving keeps history readable to everyone with Read access, and merging uncleaned local clones reintroduces scrubbed commits.

### Question 50 — `C, E` (Implement secure software development and compliance)

Correct answers: C and E (are correct). Immediately **revoke and rotate** the exposed credential at its issuing provider, then rewrite Git history with **`git filter-repo`** and ask **GitHub Support** to purge cached PR/commit views. [Skill 3.6: Define and implement a security response plan | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining a security response plan and purging sensitive data from Git history (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Correct. Publicly or internally pushed secrets can be scraped within seconds by bots or clones; credential revocation/rotation is always step #1.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **E:** Correct. `git filter-repo` rewrites Git history cleanly, and GitHub Support purges unreachable commit objects and cached Pull Request diffs on GitHub servers.

### Question 51 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). No — the original PR commits remain stored and reachable via the **Pull Request's `Commits` tab and commit SHA URL** in GitHub's cache; **revoke/rotate the credential immediately** and contact **GitHub Support** to purge cached PR commits! [Skill 3.6: Define and implement a security response plan | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining a security response plan and purging sensitive data from Git history (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]

- **A:** Incorrect. GitHub applies default Security Configurations when a repository is newly created in the org, not when an existing repository is transferred in.
- **B:** Correct. Deleting a file in a new commit never purges prior blob SHAs, and any exposed secret must be considered compromised and rotated immediately.
- **C:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — the original PR commits remain stored and reachable via the **Pull Request's `Commits` tab and commit SHA URL** in GitHub's cache; **revoke/rotate the credential immediately** and contact **GitHub Support** to purge cached PR commits!
- **D:** Incorrect. Offboarding or suspending inactive accounts reclaims per-user licenses cleanly without breaking repository Git history or compliance review logs.

### Question 52 — `A, B` (Implement secure software development and compliance)

Correct answers: A and B (are correct). Block **`PAT (classic)`** while requiring short expiration + **Owner approval** on **Fine-grained PATs**, and migrate bots/integrations to **GitHub Apps**. [Skill 3.7: Configure personal access tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring fine-grained and classic Personal Access Token (PAT) enterprise policies (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise)]

- **A:** Correct. Enterprise PAT policies replace broad non-expiring classic tokens with short-lived, repo-scoped, admin-approved Fine-grained PATs.
- **B:** Correct. GitHub App installations on GHEC provide 3x higher REST throughput, short-lived 1-hour credentials, and complete decoupling from employee turnover.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **E:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 53 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). All of that user's PATs **immediately lose access** to `@zephyraero-flight`'s private and internal resources because PAT permissions can never exceed the owner's live user permissions! [Skill 3.7: Configure personal access tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring fine-grained and classic Personal Access Token (PAT) enterprise policies (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **C:** Correct. Enterprise PAT policies curb broad non-expiring classic PATs and require organization owner approval, repo scoping, and short lifetimes on Fine-grained PATs.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 54 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Yes — GitHub automatically revokes any Personal Access Token that has gone **completely unused for 1 year**, while enterprise PAT lifetime policies enforce much tighter `7–90 day` caps! [Skill 3.7: Configure personal access tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring fine-grained and classic Personal Access Token (PAT) enterprise policies (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **C:** Correct. Enterprise PAT policies curb broad non-expiring classic PATs and require organization owner approval, repo scoping, and short lifetimes on Fine-grained PATs.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 55 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). The **Search API** enforces its own dedicated per-minute rate limits (`10 requests/minute` authenticated on `/search/code`; `30 requests/minute` on other `/search/*` endpoints) separate from your primary hourly REST quota! [Skill 3.8: Understand rate limits for PATs and GitHub Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Understanding REST and GraphQL API rate limits for PATs, GitHub Apps, and GITHUB_TOKEN (https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api)]

- **A:** Correct. On GHEC, GitHub App installations get 15,000 REST req/hr (and 10,000 GraphQL pts/hr) isolated from human users, whereas user PATs share one 5,000 req/hr personal bucket and hit secondary concurrency caps faster.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 56 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). No — all 20 PATs under `@zaero-bot` share the **exact same `5,000 req/hr`** user bucket; replace `@zaero-bot` with an org-installed **GitHub App** (`15,000 req/hr` on GHEC) + webhook/ETag caching! [Skill 3.8: Understand rate limits for PATs and GitHub Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Understanding REST and GraphQL API rate limits for PATs, GitHub Apps, and GITHUB_TOKEN (https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api)]

- **A:** Correct. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **B:** Incorrect. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.
- **C:** Incorrect. Personal-account Team Sync (`Entra ID`/`Okta`) never adds non-members into an organization; users must join the org via SAML/SCIM invitation first (or deploy GHEC with EMUs).
- **D:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — all 20 PATs under `@zaero-bot` share the **exact same `5,000 req/hr`** user bucket; replace `@zaero-bot` with an org-installed **GitHub App** (`15,000 req/hr` on GHEC) + webhook/ETag caching!

### Question 57 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Wait until **`x-ratelimit-reset`** UTC epoch time if `x-ratelimit-remaining == 0`; if neither `Retry-After` nor `0` remaining applies, wait **at least `60` seconds** and apply **exponential backoff with jitter**! [Skill 3.8: Understand rate limits for PATs and GitHub Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Understanding REST and GraphQL API rate limits for PATs, GitHub Apps, and GITHUB_TOKEN (https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Correct. `304 Not Modified` conditional requests do not count against primary REST rate limits, while webhook-driven architectures and `Retry-After` backoff prevent secondary `403` throttling.

### Question 58 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). An org-owned **GitHub App** consumes **zero** Enterprise user seats, mints ephemeral **`1`-hour** installation access tokens scoped strictly to selected repositories, and gets `15,000 req/hr` on GHEC! [Skill 3.9: Describe GitHub Apps and OAuth Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Comparing GitHub Apps, OAuth Apps, deploy keys, and machine users (https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Correct. GitHub Apps survive employee offboarding, consume zero user seats, grant fine-grained repo/resource permissions, and use short-lived tokens—outperforming both OAuth Apps and seat-consuming machine users.
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 59 — `A, D` (Implement secure software development and compliance)

Correct answers: A and D (are correct). Run machine-to-machine integrations via **GitHub App installation tokens** (`1h TTL, 15,000 req/hr on GHEC, zero user seats`), and govern human CLI tokens via approved **Fine-grained PATs** (`classic PATs blocked`). [Skill 3.9: Describe GitHub Apps and OAuth Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Comparing GitHub Apps, OAuth Apps, deploy keys, and machine users (https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)]

- **A:** Correct. GitHub App installations on GHEC provide 3x higher REST throughput, short-lived 1-hour credentials, and complete decoupling from employee turnover.
- **B:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. Enterprise PAT policies replace broad non-expiring classic tokens with short-lived, repo-scoped, admin-approved Fine-grained PATs.
- **E:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 60 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). Pass **`repositories` / `repository_ids`** AND **`permissions`** in the JSON request body of `/access_tokens` to mint a least-privilege, single-repo down-scoped token! [Skill 3.9: Describe GitHub Apps and OAuth Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Comparing GitHub Apps, OAuth Apps, deploy keys, and machine users (https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Correct. GitHub Apps never send their `.pem` private key over the network; they sign a <=10-minute JWT locally and exchange it for a scoped 1-hour installation access token.
- **C:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 61 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). GitHub Apps allow multiple active `.pem` private keys (`up to 25`) simultaneously so SREs can generate a new `.pem` key, cut over production services cleanly, and delete the old key with **zero downtime**! [Skill 3.10: Approve or deny app usage based on policy | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Approving, denying, and governing OAuth Apps and GitHub App installations (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions)]

- **A:** Correct. With OAuth App access restrictions active, unapproved third-party OAuth apps can read public data only and cannot touch organization private repos until an Owner explicitly approves the request.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 62 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Setting App visibility to **only organizations within your Enterprise** lets sibling organizations inside `ZephyrAero` install your internal GitHub App **without** making the App publicly installable on `github.com`! [Skill 3.10: Approve or deny app usage based on policy | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Approving, denying, and governing OAuth Apps and GitHub App installations (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions)]

- **A:** Correct. With OAuth App access restrictions active, unapproved third-party OAuth apps can read public data only and cannot touch organization private repos until an Owner explicitly approves the request.
- **B:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 63 — `D, E` (Manage GitHub Actions)

Correct answers: D and E (are correct). Store `workflow_call` workflows and composite actions in **`Internal`** repositories with enterprise workflow `Access` enabled, and mandate **40-character SHA pinning** + `Read-only` `GITHUB_TOKEN`. [Skill 4.1: Configure and manage reuse of actions and workflows to the enterprise repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Sharing reusable workflows and actions privately across enterprise organizations (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. 40-char SHA pinning neutralizes upstream tag hijacking while read-only `GITHUB_TOKEN` defaults enforce job-level least privilege.
- **E:** Correct. Enterprise teams reuse vetted CI/CD templates privately across all member organizations without exposing proprietary workflows publicly.

### Question 64 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). **GitHub Artifact Attestations** uses Sigstore/OIDC to bind compiled binaries and container images cryptographically to the exact source repository, commit SHA, and workflow YAML that built them! [Skill 4.1: Configure and manage reuse of actions and workflows to the enterprise repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Sharing reusable workflows and actions privately across enterprise organizations (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Correct. Without publishing proprietary actions to the public internet, enterprises host golden `workflow_call` workflows and actions inside `Internal`/`Private` repos with cross-repo enterprise workflow access enabled.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 65 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). **Docker container actions** (`using: 'docker'`) require a Linux host with Docker (`Linux runners only`), whereas **JavaScript** (`node20`) and **Composite** actions run across **Linux, Windows, and macOS**! [Skill 4.1: Configure and manage reuse of actions and workflows to the enterprise repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Sharing reusable workflows and actions privately across enterprise organizations (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Correct. Without publishing proprietary actions to the public internet, enterprises host golden `workflow_call` workflows and actions inside `Internal`/`Private` repos with cross-repo enterprise workflow access enabled.

### Question 66 — `A, E` (Manage GitHub Actions)

Correct answers: A and E (are correct). Enforce **`Require actions to be pinned to a full-length commit SHA`** + `Read-only` `GITHUB_TOKEN`, and lock HIL runners inside **Runner Groups** restricted to selected repos and workflows. [Skill 4.2: Apply organizational policies for GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing enterprise and organization GitHub Actions policies and SHA pinning (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Correct. Runner group repository and workflow restrictions prevent untrusted repos or ad-hoc branches from scheduling jobs onto privileged runners.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **E:** Correct. 40-char SHA pinning neutralizes upstream tag hijacking while read-only `GITHUB_TOKEN` defaults enforce job-level least privilege.

### Question 67 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Select **`Allow enterprise, and select non-enterprise, actions and reusable workflows`** paired with **`Enabled for selected organizations`** under `Enterprise -> Policies -> Actions`! [Skill 4.2: Apply organizational policies for GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing enterprise and organization GitHub Actions policies and SHA pinning (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Correct. Pinning third-party actions to immutable 40-char commit SHAs blocks tag-mutation supply-chain attacks, while `permissions: read-all` / read-only `GITHUB_TOKEN` defaults enforce least privilege.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 68 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Because `pull_request_target` runs in the base repository context **with access to `secrets.*` and a write-capable `GITHUB_TOKEN`**—checking out and executing untrusted fork code immediately hands secrets to the attacker! [Skill 4.2: Apply organizational policies for GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing enterprise and organization GitHub Actions policies and SHA pinning (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **C:** Correct. Pinning third-party actions to immutable 40-char commit SHAs blocks tag-mutation supply-chain attacks, while `permissions: read-all` / read-only `GITHUB_TOKEN` defaults enforce least privilege.
- **D:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.

### Question 69 — `A, C, F` (Manage GitHub Actions)

Correct answers: A, C, and F (are correct). Isolate runners in repository/workflow-scoped **Runner Groups**, connect Linux/Windows Larger runners to **Azure VNets** via Network Configurations, and exchange **OIDC (`id-token: write`)** tokens gated by **`production` Deployment Environments**. [Skill 4.3: Manage runner groups and administer GitHub-hosted vs. self-hosted runner options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing runner groups, Larger runners, self-hosted runners, and Actions Runner Controller (ARC) (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Correct. Runner group repository and workflow restrictions prevent untrusted repos or ad-hoc branches from scheduling jobs onto privileged runners.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Correct. Azure Private Networking gives managed GitHub-hosted Larger runners private VNet egress to internal endpoints and predictable firewall/NAT egress IPs.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **E:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **F:** Correct. Combining protected Deployment Environments with narrow OIDC subject claims (`repo:<org>/<repo>:environment:production`) delivers zero-standing-secret CD security.

### Question 70 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Authenticate `ARC` using a dedicated **GitHub App** (`githubConfigSecret` containing `github_app_id`, `github_app_installation_id`, and `github_app_private_key`) for `15,000 req/hr` GHEC rate limits and human-independent lifecycle! [Skill 4.3: Manage runner groups and administer GitHub-hosted vs. self-hosted runner options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing runner groups, Larger runners, self-hosted runners, and Actions Runner Controller (ARC) (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Correct. Runner groups isolate sensitive self-hosted or Larger runners to approved repositories and reusable workflow refs, while `--ephemeral` JIT / ARC pods ensure clean single-job runner state.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 71 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). **GPU-powered GitHub-hosted Larger runners** (`Linux/Windows NVIDIA Tesla T4 GPU runners`, billed per minute inside Runner Groups) run CUDA workloads on ephemeral managed VMs! [Skill 4.3: Manage runner groups and administer GitHub-hosted vs. self-hosted runner options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing runner groups, Larger runners, self-hosted runners, and Actions Runner Controller (ARC) (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Correct. Single-use ephemeral runners prevent cross-job workspace contamination, lingering credentials, or persistent malware across CI builds.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.

### Question 72 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Delegate the Azure VNet subnet to `GitHub.Network` and create `NetworkSettings`, create a GitHub Network Configuration, attach it to the Linux Larger runner group, and restrict the runner group to approved avionics repos/workflows. [Skill 4.4: Apply IP allow lists and configure networking (including Azure private networking) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring IP allow lists, proxies, and Azure private networking (VNet) for runners (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization)]

- **A:** Incorrect. Standard Linux runners use a multi-cloud pool beyond Azure IPs, and VNet-integrated runners still require outbound access to required GitHub endpoints.
- **B:** Incorrect. By default Enterprise policy restricts org-created Network Configurations unless enabled by an Enterprise Owner, and Azure NetworkSettings linkage is mandatory.
- **C:** Correct. Correct sequence: prepare the delegated Azure VNet + `GitHub.Network/networkSettings` resource, register the GitHub Network Configuration, bind it to a Larger runner group, and restrict repo/workflow access.
- **D:** Incorrect. Azure private networking requires Linux/Windows Larger runners (not macOS arm64 larger runners), subnet delegation, and strict runner-group access controls.

### Question 73 — `A, E` (Manage GitHub Actions)

Correct answers: A and E (are correct). Deploy `GitHub.Network/networkSettings` in the same Azure region supported by your GitHub **Network Configuration** on **Linux/Windows Larger runners**, and lock access inside a **Runner Group**. [Skill 4.4: Apply IP allow lists and configure networking (including Azure private networking) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring IP allow lists, proxies, and Azure private networking (VNet) for runners (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization)]

- **A:** Correct. Runner group repository and workflow restrictions prevent untrusted repos or ad-hoc branches from scheduling jobs onto privileged runners.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **E:** Correct. Azure Private Networking gives managed GitHub-hosted Larger runners private VNet egress to internal endpoints and predictable firewall/NAT egress IPs.

### Question 74 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). No — **Azure Private Networking** (`VNet` injection) is supported strictly on **Linux and Windows Larger GitHub-hosted runners**, **not** on `arm64` macOS Larger runners! [Skill 4.4: Apply IP allow lists and configure networking (including Azure private networking) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring IP allow lists, proxies, and Azure private networking (VNet) for runners (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization)]

- **A:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **B:** Correct. Standard hosted runners cannot join customer Azure VNets, and arm64 macOS Larger runners do not support Azure private networking or static IP assignment.
- **C:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — **Azure Private Networking** (`VNet` injection) is supported strictly on **Linux and Windows Larger GitHub-hosted runners**, **not** on `arm64` macOS Larger runners!
- **D:** Incorrect. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.

### Question 75 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Install the corporate Root CA into the OS trust store (`update-ca-certificates`) **and/or** set **`GIT_SSL_CAINFO`** (`plus ACTIONS_RUNNER_CA_CERT` / `NODE_EXTRA_CA_CERTS`) on the runner host! [Skill 4.5: Monitor and troubleshoot runner performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring and troubleshooting runner _diag logs, queues, and performance (https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. `Runner_*.log` records control-plane polling/TLS/proxy failures on the self-hosted agent, whereas `Worker_*.log` captures per-job execution details when jobs fail or stall.
- **D:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 76 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Both VMs fight over the **same runner session ID**, causing constant **`Runner session conflict`** disconnects and dropped jobs—always bake golden VM images **before** running `./config.sh`, and run `--ephemeral` / `generate-jitconfig` at boot! [Skill 4.5: Monitor and troubleshoot runner performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring and troubleshooting runner _diag logs, queues, and performance (https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Correct. `Runner_*.log` records control-plane polling/TLS/proxy failures on the self-hosted agent, whereas `Worker_*.log` captures per-job execution details when jobs fail or stall.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 77 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Because job orchestration tokens, live log streaming, `actions/cache`, and `actions/upload-artifact` stream directly against `*.actions.githubusercontent.com` and Azure Blob backend storage endpoints! [Skill 4.5: Monitor and troubleshoot runner performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring and troubleshooting runner _diag logs, queues, and performance (https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Correct. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 78 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). A Deployment Environment supports configuring up to **`6` users or teams** as Required Reviewers (plus `Prevent self-review`, Wait timers, and Custom deployment protection rules)! [Skill 4.6: Define scope and access for secrets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining secret scope, hierarchy precedence, and deployment environment access controls (https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. Production cloud secrets belong in protected Deployment Environments (`environment: production`) gated by human/custom deployment protection rules and branch filters, overriding broader repo/org secrets.

### Question 79 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). No — **Configuration Variables (`vars.*`)** follow the **exact same specificity hierarchy as Actions secrets (`Environment > Repository > Organization`)**, so `zephyraero/radar` evaluates `${{ vars.LOG_LEVEL }}` to **`DEBUG`**! [Skill 4.6: Define scope and access for secrets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining secret scope, hierarchy precedence, and deployment environment access controls (https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. GitHub applies default Security Configurations when a repository is newly created in the org, not when an existing repository is transferred in.
- **B:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — **Configuration Variables (`vars.*`)** follow the **exact same specificity hierarchy as Actions secrets (`Environment > Repository > Organization`)**, so `zephyraero/radar` evaluates `${{ vars.LOG_LEVEL }}` to **`DEBUG`**!
- **C:** Correct. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.
- **D:** Incorrect. Standard hosted runners cannot join customer Azure VNets, and arm64 macOS Larger runners do not support Azure private networking or static IP assignment.

### Question 80 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). GitHub dispatches the **`deployment_protection_rule`** webhook event, and the App calls `POST /repos/{owner}/{repo}/deployments/{deployment_id}/protection_rules` with `state: "approved"` or `"rejected"`! [Skill 4.6: Define scope and access for secrets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining secret scope, hierarchy precedence, and deployment environment access controls (https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. Custom deployment protection rules gate `environment: production` jobs automatically via webhook callbacks to external ITSM or observability systems.
- **D:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.

### Question 81 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). GitHub strictly isolates secrets into **three separate stores**: **`Actions`**, **`Dependabot`**, and **`Codespaces`** (`a secret stored in Actions is never automatically exposed to user Codespaces or Dependabot`)! [Skill 4.7: Configure secrets at organization and repository levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization and repository encrypted secrets and variables via UI and REST API (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/creating-secrets-for-an-organization)]

- **A:** Correct. Organization secrets never pass to public repos unless explicitly permitted, API writes require LibSodium sealed-box encryption (`48 KB` max per secret), and plain-text config belongs in `vars` context.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 82 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). Running `gh secret set <NAME> --org <org> --visibility selected --repos <r1,r2>` handles LibSodium public-key lookup and client-side sealed-box encryption automatically! [Skill 4.7: Configure secrets at organization and repository levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization and repository encrypted secrets and variables via UI and REST API (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/creating-secrets-for-an-organization)]

- **A:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **B:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Correct. Organization secrets never pass to public repos unless explicitly permitted, API writes require LibSodium sealed-box encryption (`48 KB` max per secret), and plain-text config belongs in `vars` context.

### Question 83 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). Emitting **`::add-mask::<value>`** immediately registers the dynamic runtime secret with the runner's log redactor so subsequent steps never print it in plaintext! [Skill 4.7: Configure secrets at organization and repository levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization and repository encrypted secrets and variables via UI and REST API (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/creating-secrets-for-an-organization)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. Organization secrets never pass to public repos unless explicitly permitted, API writes require LibSodium sealed-box encryption (`48 KB` max per secret), and plain-text config belongs in `vars` context.

### Question 84 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). Configure the AWS IAM OIDC provider + role bound to strict `sub`/`aud` claims, set job `permissions: id-token: write`, exchange the OIDC JWT at runtime for short-lived STS credentials, and purge static AWS secrets from GitHub. [Skill 4.8: Integrate third-party vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Integrating third-party secret vaults (HashiCorp Vault, Azure Key Vault, AWS) via OIDC (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. Storing static admin keys in repositories creates catastrophic credential exposure instead of ephemeral OIDC federation.
- **B:** Incorrect. The external vault/cloud IdP must trust `https://token.actions.githubusercontent.com` and exact subject claims before OIDC exchange can succeed.
- **C:** Incorrect. Wildcard `repo:*` subject claims let any GitHub repository assume your cloud role, and `id-token: write` is required to request an OIDC token.
- **D:** Correct. Correct passwordless vault flow: lock down cloud/vault OIDC subject claims first, grant `id-token: write`, exchange the ephemeral OIDC token at runtime, and remove static secrets.

### Question 85 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Each Data Residency / GHES environment uses its **own dedicated OIDC issuer URL** (`e.g., https://token.actions.<enterprise>.ghe.com` or `https://<ghes-hostname>/_services/token`), providing cryptographic tenant-level issuer isolation! [Skill 4.8: Integrate third-party vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Integrating third-party secret vaults (HashiCorp Vault, Azure Key Vault, AWS) via OIDC (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Correct. OIDC exchanges a job-scoped JWT signed by `https://token.actions.githubusercontent.com` for short-lived dynamic vault credentials at runtime—eliminating static secrets stored in GitHub.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 86 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). On a `pull_request` run without an `environment:`, GitHub sets `sub` to **`repo:zephyraero/autopilot:pull_request`** (`NOT refs/heads/main`), intentionally preventing unmerged PR branches from impersonating `main`! [Skill 4.8: Integrate third-party vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Integrating third-party secret vaults (HashiCorp Vault, Azure Key Vault, AWS) via OIDC (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Correct. OIDC exchanges a job-scoped JWT signed by `https://token.actions.githubusercontent.com` for short-lived dynamic vault credentials at runtime—eliminating static secrets stored in GitHub.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.

### Question 87 — `B, C` (Monitor and optimize GitHub usage)

Correct answers: B and C (are correct). Correlate **Organization API Insights** with **Enterprise Audit Log `hashed_token`** queries, and stream **Enterprise Audit Logs** continuously to WORM storage / SIEM. [Skill 5.1: Analyze audit logs and API usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Analyzing enterprise audit logs, Git events, and API Insights / REST/GraphQL metrics (https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-your-team/apicenter/viewing-api-insights-for-your-organization)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Correct. API Insights pinpoints which App or PAT user is exhausting rate limits while Audit Log `hashed_token` traces exact administrative/API actions.
- **C:** Correct. Continuous Audit Log Streaming preserves tamper-evident compliance records far beyond GitHub’s interactive 180-day UI retention window.
- **D:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **E:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 88 — `D` (Monitor and optimize GitHub usage)

Correct answer: D (is correct). They audit **every SAML SSO token/SSH key authorization** and **every Fine-grained PAT approval** granted across member organizations! [Skill 5.1: Analyze audit logs and API usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Analyzing enterprise audit logs, Git events, and API Insights / REST/GraphQL metrics (https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-your-team/apicenter/viewing-api-insights-for-your-organization)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Correct. API Insights visualizes hourly/daily REST consumption and `403`/`429` rate-limit hits broken down by specific App or PAT user so admins fix runaway polling loops quickly.

### Question 89 — `D` (Monitor and optimize GitHub usage)

Correct answer: D (is correct). Jitter/stagger scheduled workflow `cron:` expressions (`e.g., 17 * * * *, 43 * * * *`) instead of scheduling hundreds of workflows on `:00` sharp! [Skill 5.1: Analyze audit logs and API usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Analyzing enterprise audit logs, Git events, and API Insights / REST/GraphQL metrics (https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-your-team/apicenter/viewing-api-insights-for-your-organization)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Correct. API Insights visualizes hourly/daily REST consumption and `403`/`429` rate-limit hits broken down by specific App or PAT user so admins fix runaway polling loops quickly.

### Question 90 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). GHES natively supports **Prometheus `/metrics` scraping**, **`collectd` forwarding**, and **`SNMP` (`v2c`/`v3`)** traps/polling configured in the Management Console (`:8443`)! [Skill 5.2: Distinguish admin responsibilities vs. GitHub Support and generate diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Distinguishing admin vs GitHub Support responsibilities and generating appliance/cloud diagnostics (https://docs.github.com/en/enterprise-server@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/activity-dashboard)]

- **A:** Correct. GHES exposes native Prometheus metrics, SNMP, and syslog forwarding so enterprise monitoring stacks catch resource pressure before outages occur.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 91 — `D` (Monitor and optimize GitHub usage)

Correct answer: D (is correct). Inspecting the decoded **SAML Response XML / HAR trace** (`checking <Audience>, <Recipient>, signature certificate thumbprint, and IdP NTP clock skew`) resolves `95%` of SAML setup mismatches internally! [Skill 5.2: Distinguish admin responsibilities vs. GitHub Support and generate diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Distinguishing admin vs GitHub Support responsibilities and generating appliance/cloud diagnostics (https://docs.github.com/en/enterprise-server@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/activity-dashboard)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. Admins first inspect `githubstatus.com`, SAML/webhook delivery logs, and `ghe-diagnostics` CPU/memory/queue health, escalating to GitHub Support via entitled Enterprise Support members with bundles attached.

### Question 92 — `D` (Monitor and optimize GitHub usage)

Correct answer: D (is correct). Clock drift (`even >60–300 seconds`) breaks **SAML assertion `NotOnOrAfter` validation**, **GitHub App `10-minute` JWT `iat`/`exp` signatures**, **TOTP `2FA` codes**, and TLS/cluster replication timestamps! [Skill 5.2: Distinguish admin responsibilities vs. GitHub Support and generate diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Distinguishing admin vs GitHub Support responsibilities and generating appliance/cloud diagnostics (https://docs.github.com/en/enterprise-server@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/activity-dashboard)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Correct. Admins first inspect `githubstatus.com`, SAML/webhook delivery logs, and `ghe-diagnostics` CPU/memory/queue health, escalating to GitHub Support via entitled Enterprise Support members with bundles attached.

### Question 93 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). Compare **`created_at`** (`when the Copilot seat was assigned`) against **`last_activity_at`** (`null` if never used, or stale timestamp `>30–60 days`) and **`last_activity_editor`**! [Skill 5.3: Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Evaluating enterprise adoption, Copilot/Actions metrics, and dormant or underutilized features (https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api)]

- **A:** Correct. Tracking `last_activity_at` per Copilot seat lets enterprise admins automatically reclaim unused seats after a defined inactivity window (e.g., 30–60 days).
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 94 — `D` (Monitor and optimize GitHub usage)

Correct answer: D (is correct). Repository **`Pulse` / Pull Request Insights** (`and CODEOWNERS load-balancing / Team Review Assignment round-robin`) reveals human review bottlenecks distinct from CI runner bottlenecks! [Skill 5.3: Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Evaluating enterprise adoption, Copilot/Actions metrics, and dormant or underutilized features (https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api)]

- **A:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Correct. Comparing assigned seats against 7/28/90-day active usage across Copilot, GHAS Security Overview, and Actions workflows highlights teams needing enablement or license reclamation.

### Question 95 — `B` (Monitor and optimize GitHub usage)

Correct answer: B (is correct). **`Coverage`** measures **which repositories have security tools enabled** (`CodeQL`, `Secret scanning`, `Push protection`, `Dependabot`), whereas **`Risk`** ranks repositories by **open vulnerability/secret alert volume and severity**! [Skill 5.3: Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Evaluating enterprise adoption, Copilot/Actions metrics, and dormant or underutilized features (https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Correct. Security Overview aggregates alert risk, push-protection metrics, and tool coverage across thousands of repositories for CISOs and Security Managers.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.

### Question 96 — `B, D` (Monitor and optimize GitHub usage)

Correct answers: B and D (are correct). Audit **dormant seats, pending invites, and 90-day unique GHAS committers**, and map organizations/repositories into **Cost Centers** with **75/90/100% Budgets**, caching, short artifact retention, and Linux default runners. [Skill 5.4: Interpret usage reports for metered products | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Interpreting metered usage reports, spending limits, and cost centers for Actions, Packages, GHAS & Copilot (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-billing/using-the-billing-platform)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Correct. Cost Centers and Budgets enforce FinOps accountability while caching, shorter artifact retention, and right-sized OS runners cut metered overages.
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Correct. Proactive seat hygiene reclaims idle Enterprise, Copilot, and GHAS licenses before renewal or monthly metered billing cycles.
- **E:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 97 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). Each resource belongs to **at most one active Cost Center** at a time (`explicit repository assignment to CC-Platform cleanly overrides its parent organization's CC-Avionics default going forward`)! [Skill 5.4: Interpret usage reports for metered products | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Interpreting metered usage reports, spending limits, and cost centers for Actions, Packages, GHAS & Copilot (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-billing/using-the-billing-platform)]

- **A:** Correct. Metered billing tracks included enterprise quotas first (for standard hosted runners and Packages/Artifacts storage) and bills overages or Larger runners/Copilot/GHAS against assigned Cost Centers and Budgets.
- **B:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 98 — `B` (Monitor and optimize GitHub usage)

Correct answer: B (is correct). No — **self-hosted runners incur `$0` in GitHub Actions per-minute compute charges** (`you pay only your own underlying cloud/hardware infrastructure plus any metered Actions artifact/cache storage above included quotas`)! [Skill 5.4: Interpret usage reports for metered products | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Interpreting metered usage reports, spending limits, and cost centers for Actions, Packages, GHAS & Copilot (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-billing/using-the-billing-platform)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Correct. Metered billing tracks included enterprise quotas first (for standard hosted runners and Packages/Artifacts storage) and bills overages or Larger runners/Copilot/GHAS against assigned Cost Centers and Budgets.
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 99 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). For `ZephyrAero`'s avionics renewal, export consumed-licenses and verify hybrid GHES sync first, audit dormant accounts and 90-day GHAS/Copilot activity, reclaim idle seats + tune Cost Center budgets, and automate SCIM offboarding + threshold alerts. [Skill 5.5: Recommend strategies for license and resource optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending strategies for dormant seat reclamation, caching, and runner/storage cost optimization (https://docs.github.com/en/enterprise-server@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/managing-dormant-users)]

- **A:** Correct. Correct optimization loop: inspect unified license data, pinpoint duplicate identities/dormant users/GHAS committers, reclaim unused seats and cap metered budgets, and automate SCIM hygiene.
- **B:** Incorrect. Admins remove/suspend org or EMU memberships (preserving PR/commit audit trails) rather than deleting security controls.
- **C:** Incorrect. macOS hosted runners carry a higher per-minute cost than Linux runners, long artifact retention inflates storage charges, and unmonitored seat grants waste licenses.
- **D:** Incorrect. GHAS seats release automatically 90 days after a user’s last push (or when GHAS is disabled on the repo), and disabling GitHub Connect causes double-billing across GHEC and GHES.

### Question 100 — `D` (Monitor and optimize GitHub usage)

Correct answer: D (is correct). Yes — `cancel-in-progress: true` immediately aborts superseded PR runs to save Actions minutes, and SCIM-deprovisioning retired EMUs frees 30 seats while preserving 100% of historical commits and PR reviews! [Skill 5.5: Recommend strategies for license and resource optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending strategies for dormant seat reclamation, caching, and runner/storage cost optimization (https://docs.github.com/en/enterprise-server@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/managing-dormant-users)]

- **A:** Incorrect. Offboarding or suspending inactive accounts reclaims per-user licenses cleanly without breaking repository Git history or compliance review logs.
- **B:** Incorrect. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.
- **C:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **D:** Correct. Every technical requirement, permission boundary, and GitHub Enterprise platform rule in the scenario is satisfied cleanly.
