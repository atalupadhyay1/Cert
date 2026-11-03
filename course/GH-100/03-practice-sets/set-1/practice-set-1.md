# Microsoft / GitHub Exam GH-100: GitHub Enterprise Administrator — Full-Length Mock Exam 1

**Theme:** Multi-Org Enterprise Identity & Access — EMUs vs Personal Accounts, SAML/SCIM, Enterprise Teams, Custom Roles & Rulesets  
**Credential:** `GitHub Administration` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `July 2026 (Last updated May 5, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-100 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Enterprise documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Manage GitHub identities and access (15–20% official weight · 19 questions)

### 1. A payments enterprise (`KestrelPay`) adopts **GitHub Enterprise Cloud with Enterprise Managed Users (`EMUs`)** and onboards 40 external QA contractors who must not browse company-wide `Internal` repositories. Which two identity controls meet this requirement? Select two.

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **D.** Provision user accounts exclusively via your corporate IdP (`SAML`/`OIDC` + `SCIM`), blocking personal public repos, Gists, and external OSS contributions
- **E.** Assign external contractors the IdP **Guest Collaborator** role so they cannot browse `Internal` enterprise repositories unless explicitly granted access

### 2. During an **EMU** deployment for `KestrelPay` (`shortcode: kpay`), an architect asks how managed usernames (`____`) are formatted and whether existing personal `github.com` accounts can be converted in place. What is accurate?

- **A.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **B.** Enterprise Managed Users (`EMUs`) provisioned by your corporate IdP (`<handle>_<shortcode>`), isolated from public repo creation, Gists, and external OSS pushes
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 3. Before switching an existing personal-account GHEC Enterprise from optional SAML test mode to **Enforced SAML SSO**, what critical credential must the Enterprise Owner download and vault (`Enterprise Settings -> Authentication security -> ____`) to prevent total lockout during an IdP outage?

- **A.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **B.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Enterprise/Organization SAML 2.0 SSO paired with mandatory GitHub `2FA` (with SAML recovery codes stored safely and PAT/SSH credential authorization enforced)

### 4. On a personal-account **GitHub Enterprise Cloud** organization, if an Organization Owner checks **`Require two-factor authentication for everyone in your organization`**, what happens immediately to current members and outside collaborators who have **not** enabled GitHub `2FA`?

- **A.** Enterprise/Organization SAML 2.0 SSO paired with mandatory GitHub `2FA` (with SAML recovery codes stored safely and PAT/SSH credential authorization enforced)
- **B.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **C.** EMU **Guest Collaborator** role provisioned via the IdP to grant contractors private/internal repo access only where explicitly added (blocking broad org `Internal` browse)
- **D.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing

### 5. An IAM team provisions a brand-new **GitHub Enterprise Cloud with EMUs** tenant integrated with Okta. Which four-step implementation sequence applies?

- **A.** Sync IdP groups to Enterprise teams → enable SCIM provisioning → configure SAML/OIDC SSO → create the EMU enterprise account last
- **B.** Enable SCIM without configuring SAML/OIDC SSO → share one setup password across engineers → skip recovery codes → assign everyone Enterprise Owner
- **C.** Invite employees personal GitHub.com accounts → convert personal accounts into EMUs in place → enable SCIM → disable 2FA on the IdP
- **D.** Create EMU enterprise & save recovery codes → configure SAML/OIDC SSO with admin setup user → enable SCIM user/group provisioning in IdP → sync IdP groups to Enterprise/Org teams

### 6. An enterprise runs **GHEC with personal accounts** (non-EMU) backed by Microsoft Entra ID. An admin adds 15 newly hired engineers into an Entra ID group mapped via **Team Synchronization** to `@kestrelpay/payments-dev`, without sending organization invitations or configuring SCIM user provisioning. Proposed solution: Rely on personal-account Team Synchronization alone to add those 15 brand-new users into the `@kestrelpay` GitHub Organization. Does the solution work?

- **A.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **B.** No — on GHEC with personal accounts, IdP **Team Synchronization** only updates Organization team membership for existing org members and **cannot** invite or provision brand-new users into the organization
- **C.** No — **Enterprise teams** (`@/ent:<slug>`) currently do **not** support `CODEOWNERS` assignment, nested child teams, Secret visibility, or Team maintainers; use an **Organization team** for `CODEOWNERS`
- **D.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement

### 7. Which **Identity Provider (`IdP`)** and protocol combination (`____` SSO for EMUs) supports paved-path setup on GHEC with automatic enforcement of corporate **Conditional Access Policies (`CAP`)** for device compliance and IP location?

- **A.** OIDC SSO for Enterprise Managed Users with **Microsoft Entra ID**, automatically enforcing Entra **Conditional Access Policies (`CAP`)** including IP and device compliance
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 8. A defense subsidiary running self-hosted **GitHub Enterprise Server (`GHES`)** needs to authenticate engineers directly against an on-premises Active Directory directory tree without a cloud SAML broker (`ghe-config secrets.____.*`). Which GHES-native authentication mode supports direct directory binding alongside SAML and CAS?

- **A.** Supported IdPs (`Microsoft Entra ID`, `Okta`, `PingFederate` with paved-path OIDC/SAML+SCIM for EMUs; or `LDAP`/`CAS`/`SAML` on self-hosted `GHES`)
- **B.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **C.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 9. An administrator enforces SAML SSO on a personal-account GHEC organization where 200 developers already push daily using SSH keys and Fine-grained/classic PATs. Which two practices preserve admin resilience and uninterrupted developer CLI access? Select two.

- **A.** Download and vault **Enterprise/Org SAML recovery codes** before enforcing SAML SSO so Owners can recover access during an IdP outage
- **B.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **C.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **D.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **E.** Require developers on personal-account GHEC to **authorize** approved Fine-grained/classic PATs and SSH keys for SAML SSO before accessing org repositories

### 10. A developer on personal-account GHEC runs `git push` over HTTPS using a valid, non-expired classic PAT with `repo` scope (`HTTP 401/403: Resource protected by organization SAML enforcement. You must grant your Personal Access token access to this organization`). Did **authentication** fail or did **authorization** fail?

- **A.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **B.** Authentication verifies *who* the caller is (`SAML`/`OIDC`, `2FA`, Passkey, SSH key, PAT), while authorization governs *what* resources they may access (roles, teams, scopes, SAML SSO token authorization)
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing

### 11. On **GitHub Enterprise Cloud**, QA release leads need `Triage` capabilities plus permission to trigger workflow runs and manage environments—**without** granting full `Write` code-push privileges. Which feature (`Organization Settings -> Repository roles -> ____`) satisfies least privilege?

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **C.** 5 built-in repository roles (`Read`, `Triage`, `Write`, `Maintain`, `Admin`), built-in org roles (`Owner`, `Member`, `Moderator`, `Billing manager`, `Security Manager`), plus GHEC **Custom repository/org roles**
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 12. Internal SOX auditors need read-only access to the **Enterprise Audit Log** across 12 organizations in `KestrelPay` **without** receiving full `Enterprise Owner` control over SAML or billing. Which feature (`Enterprise -> Settings -> Admins -> ____`) grants least-privilege enterprise delegation?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Custom **Enterprise roles** (such as `Audit Log Reader`, `Billing Viewer`, or `Enterprise Actions Admin`) assigned to individuals or **Enterprise teams** to avoid over-granting `Enterprise Owner`

### 13. An Enterprise Owner designs multi-organization access and license governance across 30 organizations in an EMU enterprise using **Enterprise teams**. Which three capabilities and best practices apply? Select three.

- **A.** Sync a single 12,000-member Entra ID group into one Enterprise team alongside 15 manually added contractor accounts
- **B.** Grant **Copilot Business** seats, **custom/predefined enterprise roles**, and **Repository Ruleset bypass** rights directly to **Enterprise teams** (`@/ent:<slug>`)
- **C.** Add **Enterprise teams** across up to 1,000 organizations where org admins can grant additional repo access without removing enterprise-granted permissions
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **E.** Set Organization **`Base permissions = None`** and grant repository access strictly through IdP-synced Teams and least-privilege Custom Repository Roles
- **F.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step

### 14. An Enterprise Owner creates an **Enterprise team** named `Platform Security` (`slug: @/ent:platform-security`) and adds `@kestrelpay/ent:platform-security` to `.github/CODEOWNERS` expecting mandatory Code Owner merge blocking. Proposed solution: Use an **Enterprise team** directly inside `.github/CODEOWNERS` instead of an Organization team. Does the solution enforce Code Owner reviews?

- **A.** No — **Enterprise teams** (`@/ent:<slug>`) currently do **not** support `CODEOWNERS` assignment, nested child teams, Secret visibility, or Team maintainers; use an **Organization team** for `CODEOWNERS`
- **B.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **C.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **D.** No — on GHEC with personal accounts, IdP **Team Synchronization** only updates Organization team membership for existing org members and **cannot** invite or provision brand-new users into the organization

### 15. An EMU Enterprise team is synced to an Entra ID security group of `4,800` users, and HR merges another division adding `400` more users (`5,200` total, exceeding the `____`-user Enterprise team cap). What happens to team synchronization?

- **A.** Sync a single 12,000-member Entra ID group into one Enterprise team alongside 15 manually added contractor accounts
- **B.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **C.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **D.** **Enterprise teams** (`@/ent:<slug>`, up to 5,000 EMU IdP-synced users across up to 1,000 orgs) for centralized org membership, Copilot seats, custom enterprise roles, and ruleset bypass

### 16. During a quarterly access review, a security analyst spots a suspicious `repo.destroy` event in the **Enterprise Audit Log** executed via API and wants to trace **which specific Personal Access Token or GitHub App token** performed the call. Which Audit Log JSON field (`____`) uniquely fingerprints the programmatic credential without exposing the raw secret?

- **A.** Exporting enterprise/organization membership & repository permission inventories plus auditing `org.*`, `team.*`, `repo.*`, and token metadata (`hashed_token`, `programmatic_access_type`) in the Audit Log
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 17. Where in the **GitHub Enterprise Cloud** UI can an Enterprise Owner export a complete CSV/JSON inventory of every member across all organizations, their roles (`Owner`, `Member`, `Outside collaborator`), `2FA` status, and SAML `NameID` linkage?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Exporting enterprise/organization membership & repository permission inventories plus auditing `org.*`, `team.*`, `repo.*`, and token metadata (`hashed_token`, `programmatic_access_type`) in the Audit Log

### 18. Instead of maintaining hardcoded lists of 180 PCI repository names, an Organization Owner defines a required **Custom Property** (`pci_scope = true`) on repositories and configures an Organization **Repository Ruleset** targeting `____`. How does GitHub evaluate overlapping Rulesets?

- **A.** Repository **Custom Properties** (e.g., `compliance_tier=pci`, `data_class=restricted`) targeted dynamically by Organization/Enterprise **Repository Rulesets** (`most restrictive wins`)
- **B.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step

### 19. Before flipping a brand-new Enterprise **Repository Ruleset** to **`Active`** across 400 repositories, which Ruleset enforcement mode (`____`) lets admins audit every push/merge that *would* have violated the rule inside **Rule Insights** without blocking developers?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **D.** Enterprise **Member privileges** (`Base permissions = None`, repo creation/forking/visibility locks) combined with **Organization/Enterprise Repository Rulesets** (`Active` vs `Evaluate` dry-run mode)

---

## Domain 2 — Administer GitHub Enterprise environment (10–15% official weight · 14 questions)

### 20. A developer opens an internal IT ticket stating their `git push` to a private GHEC repository was rejected with `GH006: Protected branch update failed` because status check `build-linux` failed. Should this be resolved by an **internal GitHub Admin / Maintainer** or escalated to **GitHub Enterprise Support**?

- **A.** Enterprise Admins resolve IdP/SAML lockouts, RBAC grants, runner sizing, and webhook configs; **GitHub Enterprise Support** handles platform outages, cached PR commit purges, and repo restore escalations
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 21. On **GitHub Enterprise Cloud**, how many organization/enterprise members can an Enterprise Owner grant the **`Support` entitlement** (`Enterprise Settings -> Support`) so designated platform engineers can open and track tickets in the **GitHub Support Portal** without holding full `Enterprise Owner`?

- **A.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **B.** Enterprise Admins resolve IdP/SAML lockouts, RBAC grants, runner sizing, and webhook configs; **GitHub Enterprise Support** handles platform outages, cached PR commit purges, and repo restore escalations
- **C.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **D.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

### 22. A secondary subsidiary running self-hosted **GitHub Enterprise Server (`GHES`)** encounters intermittent `502 Bad Gateway` errors on Git pushes (`port 443`). Which four-step diagnostic escalation sequence applies?

- **A.** Confirm admin-side checks & note exact incident UTC timestamps → SSH/console in and run ghe-support-bundle -x (or Management Console) → review/sanitize sensitive log data if required → upload bundle to GitHub Enterprise Support portal
- **B.** Post raw /data/user/common/secrets.conf in a public GitHub Discussion → tag @github → upgrade three major GHES versions mid-outage → skip support bundle generation
- **C.** File a GitHub Support ticket asking GitHub to reset a developer corporate Active Directory password → wait 48 hours → run git gc locally → close ticket
- **D.** Restart all GHES services with ghe-config-apply --force → wipe /data/user/logs to save disk → open a ticket with no timestamps or bundle → grant Support SSH access to internal VPC

### 23. Which two administrative practices ensure fast, secure resolution when escalating production **GHES** or **GHEC** incidents to **GitHub Enterprise Support**? Select two.

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Designate up to 20–25 entitled **Support** members (or `Enterprise Support` custom role holders) authorized to open and manage enterprise support tickets
- **C.** Generate an extended diagnostic archive via `ghe-support-bundle -x` (or Management Console `:8443`) and upload it to the **GitHub Enterprise Support** portal
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **E.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 24. To standardize `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and YAML Issue Forms across 95 repositories in `@kestrelpay-core` without duplicating files in every repo, which special repository (`@kestrelpay-core/____`) provides organization-wide defaults?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Standardizing **Template repositories**, organization-wide `.github` community health defaults, **`Internal`** InnerSource discovery, and ADR/Issue Form intake across teams
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 25. Where inside an organization's `.github` repository (`____/*.yml` paired with matching `.properties.json` metadata files) do platform admins publish custom **CI Starter Workflows** so squads see them in `Actions -> New workflow`?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **D.** Publishing reusable **Starter Workflows** inside the organization’s `.github` repository (`workflow-templates/*.yml` + `.properties.json`) to standardize onboarding CI pipelines

### 26. On `kestrelpay-monorepo`, 60 engineers merge approved PRs daily; two PRs that each pass CI individually occasionally break `main` when combined semantically. Which GitHub branch/ruleset capability validates queued PRs **together** on temporary `____` branches before updating `main`?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Enforcing trunk-based **GitHub Flow**, protected `main` with **`CODEOWNERS`**, **Merge Queue** (`gh-readonly-queue`) for busy monorepos, linear squash merges, and immutable signed SemVer **Releases**
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 27. To prevent accidental deletion or force-moving of production SemVer release tags (`v1.0.0`, `v2.3.1`), what should an administrator configure alongside protected `main` branches?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Enforcing trunk-based **GitHub Flow**, protected `main` with **`CODEOWNERS`**, **Merge Queue** (`gh-readonly-queue`) for busy monorepos, linear squash merges, and immutable signed SemVer **Releases**
- **D.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO

### 28. An enterprise architect compares **GitHub Enterprise** deployment topologies across regulated regions and legacy datacenters. Which two architectural statements are accurate? Select two.

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Enable **GitHub Connect** license synchronization between `GHES` and `GHEC` (plus link **Visual Studio Subscriptions**) so hybrid users consume a single Enterprise seat
- **C.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **E.** Deploy **GHEC with Data Residency (`<enterprise>.ghe.com`) + EMUs** when regulations require pinning cloud source code and metadata in a specific geographic region (`EU`, `US`, `AU`, `JP`)

### 29. Compare all four **GitHub Enterprise** deployment options: `GHEC + personal accounts`, `GHEC + EMU`, `GHEC with Data Residency + EMU`, and `GHES`. Which option runs on **GitHub-managed regional cloud infrastructure** (`e.g., EU` or `Australia`) under a dedicated `https://<enterprise>.____.com` subdomain?

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **C.** Comparing the 4 Enterprise models: **GHEC + personal accounts**, **GHEC + EMU**, **GHEC with Data Residency (`<ent>.ghe.com`) + EMU**, and self-hosted **GitHub Enterprise Server (`GHES`)**
- **D.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

### 30. Developer Elena belongs to **6** separate Organizations inside `KestrelPay`'s GitHub Enterprise Cloud account and also holds an account with the same verified email on `KestrelPay`'s **GitHub Connect**-synced `GHES` appliance. How many **GitHub Enterprise user seats** does Elena consume?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Per-user **GitHub Enterprise** seat licensing (deduplicating unique users across orgs + synced `GHES` via **GitHub Connect**, plus linked **Visual Studio Enterprise/Pro with GitHub Enterprise** benefits) alongside metered add-ons
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 31. If your company already assigns **Visual Studio Enterprise** (or **Visual Studio Professional**) subscriptions with the **GitHub Enterprise** benefit linked in the Visual Studio Admin Portal, how does GitHub bill those linked users?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Per-user **GitHub Enterprise** seat licensing (deduplicating unique users across orgs + synced `GHES` via **GitHub Connect**, plus linked **Visual Studio Enterprise/Pro with GitHub Enterprise** benefits) alongside metered add-ons
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 32. While reviewing `Enterprise -> Billing & Licensing -> Licensing`, an admin notices `Consumed licenses` is 18 seats higher than active Organization Members. Which two often-overlooked categories consume a **GitHub Enterprise** seat immediately?

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Inspecting `Enterprise -> Billing & Licensing -> Licensing` (and exported `consumed-licenses` JSON/CSV) to track assigned seats, pending invitations, outside collaborators, VS subscriptions, and `GHES` sync files
- **D.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls

### 33. If a disconnected air-gapped **GHES** instance cannot use automatic live **GitHub Connect** license sync, how does an Enterprise Admin reconcile combined `GHEC` + `GHES` license consumption?

- **A.** Inspecting `Enterprise -> Billing & Licensing -> Licensing` (and exported `consumed-licenses` JSON/CSV) to track assigned seats, pending invitations, outside collaborators, VS subscriptions, and `GHES` sync files
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

---

## Domain 3 — Implement secure software development and compliance (25–30% official weight · 29 questions)

### 34. CISO leadership mandates standardized `Secret Protection`, `Dependabot`, and `CodeQL` settings across all 300 repositories in `KestrelPay` with zero local tampering by repo admins. Which four-step rollout sequence applies?

- **A.** Ask 400 repository admins to toggle checkboxes manually in every repo → disable Dependency graph → turn off push protection → audit annually by spreadsheet
- **B.** Apply a GHAS Security Configuration with 0 available licenses → assume transferred repos inherit new-repo defaults automatically → disable GitHub Actions on CodeQL repos → leave unenforced
- **C.** Verify available GHAS / Secret Protection / Code Security committers → create custom Security Configuration at Enterprise/Org level → attach to existing & transferred repos plus default for new repos → set policy to Enforce configuration
- **D.** Enable Enforce configuration with every setting left as Not set → expect Not set fields to lock repository admins → delete Organization Security Managers → skip default policy

### 35. Which two enterprise-scale controls guarantee uniform secret and vulnerability protection across existing, newly created, and transferred repositories? Select two.

- **A.** Enable **Secret Scanning Push Protection**, **Partner Validity Checks**, custom regex patterns, and **Delegated Bypass** reviewer groups
- **B.** Create and **Enforce** an Enterprise/Organization **Security Configuration** (setting it as default for newly created repos and manually attaching transferred repos)
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **E.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 36. An Organization Owner configures a custom **Security Configuration** with `Use as default for newly created repositories = All repositories` and `Enforce = Enforced`. Next week, an acquired team **transfers** 12 existing private repositories into the organization. Proposed solution: Assume those 12 **transferred** repositories automatically inherit the organization's default Security Configuration without manual or API attachment. Does the solution secure the 12 transferred repositories?

- **A.** No — committing `git rm` (or archiving the repo) leaves the leaked secret intact in prior Git commits and cached PR diffs; you must **revoke/rotate the secret immediately**, run **`git filter-repo`**, force-push, and contact GitHub Support
- **B.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **C.** No — an organization’s default **Security Configuration** auto-attaches only to **newly created** repositories; repositories **transferred** into the organization must have the Security Configuration attached manually or via API
- **D.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement

### 37. To stop developers from accessing private repositories from unmanaged home networks using personal SSH keys that never expire, an Enterprise Owner uploads a corporate **SSH Certificate Authority (`SSH CA`)** public key and checks `Require SSH Certificates`. What does this enforce?

- **A.** Hardening access with **Organization/Enterprise IP allow lists**, **SSH Certificate Authorities (`SSH CAs`)** issuing short-lived developer SSH certs, and least-privilege repo-scoped **Deploy keys**
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 38. Which **Repository Ruleset** rule type (`____` rules, available on GHEC/GHES) blocks developers from pushing `.pem`/`.pfx` private keys, files exceeding `50 MB`, or unauthorized edits to `.github/workflows/**` **before** commits enter any branch?

- **A.** Configuring **Push Rulesets** to block oversized binaries, forbidden file extensions (`.pem`, `.pfx`, `.key`), restricted file paths (`.github/workflows/**`), and path-traversal commits pre-receive
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO

### 39. When you enable an **Enterprise IP allow list** on GitHub Enterprise Cloud, why might standard `ubuntu-latest` GitHub-hosted Actions workflows suddenly fail with `IP address is not permitted` when checking out your private repository unless handled properly?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **D.** Hardening access with **Organization/Enterprise IP allow lists**, **SSH Certificate Authorities (`SSH CAs`)** issuing short-lived developer SSH certs, and least-privilege repo-scoped **Deploy keys**

### 40. How long does GitHub retain standard non-Git administrative events inside the interactive **Web UI / REST Audit Log** (`____ days`), and why is **Audit Log Streaming** mandatory for multi-year PCI-DSS/SOX compliance?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **D.** Streaming the **Enterprise Audit Log** (including optional `git.clone`/`git.fetch`/`git.push` events) in real time to **Azure Event Hubs / Blob Storage, AWS S3, Splunk, Datadog, or GCS**, plus REST/GraphQL queries

### 41. By default in the GitHub Enterprise Audit Log, are high-volume **`git.clone`**, **`git.fetch`**, and **`git.push`** transport events visible in the standard web UI search, or how must an Enterprise Owner capture them on GHEC?

- **A.** Streaming the **Enterprise Audit Log** (including optional `git.clone`/`git.fetch`/`git.push` events) in real time to **Azure Event Hubs / Blob Storage, AWS S3, Splunk, Datadog, or GCS**, plus REST/GraphQL queries
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 42. Which centralized dashboard (`Organization / Enterprise -> ____ -> Risk & Coverage`) lets CISOs filter critical open `CodeQL`, `Dependabot`, and `Secret scanning` alerts across 500 repositories by Custom Property or Team?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **C.** Using **Enterprise/Organization Security Overview** (`Risk` and `Coverage` dashboards) to audit GHAS enablement gaps, open critical `CodeQL`/Secret/Dependabot alerts, and remediation MTTR
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 43. An AppSec director rolls out **GitHub Advanced Security (`GHAS`)** across `KestrelPay` payment microservices. Which three controls belong in the target baseline? Select three.

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Enable **CodeQL default/advanced setup**, **Dependabot security updates**, and the **Dependency Review Action** inside required Pull Request Rulesets
- **D.** Enable **Secret Scanning Push Protection**, **Partner Validity Checks**, custom regex patterns, and **Delegated Bypass** reviewer groups
- **E.** Create and **Enforce** an Enterprise/Organization **Security Configuration** (setting it as default for newly created repos and manually attaching transferred repos)
- **F.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 44. Compare **CodeQL `Default setup`** and **CodeQL `Advanced setup`** when enabling code scanning on a polyglot Python/TypeScript repository vs a custom C/C++ firmware repo requiring bespoke `cmake` flags.

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Enabling **CodeQL code scanning** (`Default setup` or custom `Advanced setup` SARIF workflows) plus **Secret scanning** with **Push protection**, **Validity checks**, custom regex patterns, and delegated bypass review

### 45. Internal services at `KestrelPay` issue proprietary bearer tokens prefixed with `kpay_live_[A-Za-z0-9]{40}`. How should an Enterprise Security Manager block commits containing `kpay_live_` tokens **without** triggering false-positive storms on day one?

- **A.** Defining **Custom Secret Scanning Patterns** (with before/after context expressions and dry-run historical backtesting) at the Organization or Enterprise level to catch internal proprietary token formats
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

### 46. What is the functional difference between **Dependabot security updates** (configured in Repository/Org Security settings) and **Dependabot version updates** (configured by committing `.github/____.yml`)?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Configuring **Dependency graph**, **Dependabot alerts**, **Dependabot security & version updates** (`dependabot.yml` + private registry access), **Dependency Review Action** on PRs, and **Repository Security Advisories**
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 47. Dependabot fails to resolve internal `@kestrelpay/*` npm packages hosted on a JFrog Artifactory instance inside a private VNet. Which two settings let Dependabot update private dependencies cleanly?

- **A.** Configuring **Dependabot** with encrypted `dependabot` private-registry secrets (`Settings -> Code security -> Global settings`) and running updates on **Actions runners / ARC** when private VNet access is required
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 48. Which official GitHub Action (`actions/____-action@v4`) runs on Pull Requests to fail the CI check whenever a contributor introduces a new package version carrying a `High`/`Critical` vulnerability **or** a forbidden `AGPL-3.0` license?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Configuring **Dependency graph**, **Dependabot alerts**, **Dependabot security & version updates** (`dependabot.yml` + private registry access), **Dependency Review Action** on PRs, and **Repository Security Advisories**
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls

### 49. An engineer accidentally commits and pushes a live production Stripe secret key into `kestrelpay-checkout` three commits ago (`referenced in an open Pull Request`). Which four-step **Security Response Plan** applies?

- **A.** Revoke & rotate the exposed secret at the provider → scrub all branches/tags via git filter-repo → force-push cleaned refs & have devs re-clone → send commit SHAs to GitHub Support to purge cached views
- **B.** Archive the repository to hide the leaked key → rotate the key next quarter → use deprecated git filter-branch without force-pushing → tell devs to git pull --merge old history back
- **C.** Contact GitHub Support first to rotate your AWS IAM key → wait before revoking in AWS → delete the entire GitHub Organization → recreate repos from developer zip files
- **D.** Run git rm secrets.env in a new commit and push → assume historical commits are erased → keep the production API key active → skip GitHub Support cache purge

### 50. Why does committing `git rm prod.key` fail during a secret-leak incident, and which two remediation steps are mandatory? Select two.

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Immediately **revoke and rotate** leaked credentials at the target cloud/API provider before assuming Git history rewrites reduce exposure
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **E.** Scrub sensitive blobs across all refs with **`git filter-repo`**, force-push cleaned branches/tags, and send commit SHAs to **GitHub Support** to purge cached PR views

### 51. A developer pushes `aws_credentials.json` to `feature/s3-export` on GHEC and opens a Pull Request. Five minutes later, they run `git rm aws_credentials.json`, commit `"Remove creds"`, push, and do **not** rotate the AWS IAM key or rewrite history. Proposed solution: Rely on `git rm` to erase `aws_credentials.json` from Git history and protect AWS. Does the solution remediate the leak?

- **A.** No — an organization’s default **Security Configuration** auto-attaches only to **newly created** repositories; repositories **transferred** into the organization must have the Security Configuration attached manually or via API
- **B.** No — committing `git rm` (or archiving the repo) leaves the leaked secret intact in prior Git commits and cached PR diffs; you must **revoke/rotate the secret immediately**, run **`git filter-repo`**, force-push, and contact GitHub Support
- **C.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **D.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement

### 52. An enterprise security audit uncovers 90 non-expiring **classic PATs** (`repo`, `admin:org`) used across developer laptops and CI bots. Which two policies modernize token security? Select two.

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** Block or restrict **classic PATs** enterprise-wide while requiring **Organization Owner approval** and max expiration lifetimes (`<=30–90 days`) on **Fine-grained PATs**
- **E.** Migrate org automation from personal PATs (`5,000 req/hr`) to **GHEC GitHub App installation tokens** (`15,000 REST req/hr`, 1-hour expiry, zero seat cost)

### 53. Under `Enterprise Settings -> Policies -> Personal access tokens`, when an Enterprise Owner enables **`Require approval of fine-grained personal access tokens`**, what can a newly created Fine-grained PAT access inside `@kestrelpay` **before** an Organization Owner approves it?

- **A.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **B.** Enforcing **Enterprise Fine-Grained PAT Policies**: restricting or blocking **PATs (classic)**, requiring mandatory expiration lifetimes (e.g., <=30–90 days), requiring **Admin approval** before Fine-grained PATs activate, and revoking tokens
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 54. If an employee's laptop is stolen and an Organization Owner navigates to `Organization Settings -> Personal access tokens -> Active tokens`, can the Organization Owner immediately **revoke** that user's access to the organization for active Fine-grained PATs (and revoke SAML SSO authorization on classic PATs)?

- **A.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Enforcing **Enterprise Fine-Grained PAT Policies**: restricting or blocking **PATs (classic)**, requiring mandatory expiration lifetimes (e.g., <=30–90 days), requiring **Admin approval** before Fine-grained PATs activate, and revoking tokens

### 55. A build engineer hits GitHub's `5,000 requests/hour` REST API rate limit on a personal PAT belonging to `@ci-bot-user`. Proposed solution: Generate **four additional Fine-grained PATs** under the exact same `@ci-bot-user` account expecting `4 × 5,000 = 20,000 requests/hour`. Does the solution increase the hourly REST quota?

- **A.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **B.** No — on GHEC with personal accounts, IdP **Team Synchronization** only updates Organization team membership for existing org members and **cannot** invite or provision brand-new users into the organization
- **C.** No — **Enterprise teams** (`@/ent:<slug>`) currently do **not** support `CODEOWNERS` assignment, nested child teams, Secret visibility, or Team maintainers; use an **Organization team** for `CODEOWNERS`
- **D.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)

### 56. What is the primary REST API rate limit for a **GitHub App installation access token** installed on a **GitHub Enterprise Cloud (`GHEC`)** organization (`____ requests/hour`) versus on a non-GHEC organization (`5,000` base scaling up to a cap of `____ requests/hour`)?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** REST rate limits: **`5,000 req/hr`** per personal PAT user vs **`15,000 req/hr`** for a **GitHub App installation** (and `GITHUB_TOKEN` per repo) on **GHEC** (`up to 12,500 req/hr` scaled on non-GHEC; GraphQL `5,000` vs `10,000` pts/hr)
- **C.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 57. An internal compliance script still has `4,200` remaining requests in `x-ratelimit-remaining` yet suddenly receives `HTTP 403 Forbidden` with `"You have exceeded a secondary rate limit"` and a `Retry-After: 60` header. What triggered this and how should the script behave?

- **A.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **B.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **C.** Mitigating **Secondary (abuse) rate limits** by capping concurrent API requests, serializing write mutations (`>=1 sec` spacing), using **webhooks / GraphQL / Conditional `ETag` (`304 Not Modified`)**, and honoring `Retry-After`
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 58. Platform engineering replaces a fragile personal `admin:org` PAT powering an internal release bot with an enterprise **GitHub App**. Which four-step lifecycle sequence applies?

- **A.** Create an org-owned GitHub App with least-privilege permissions → store the App private key in a vault & install on selected repos → generate a short-lived JWT to exchange for a 1-hour installation access token → revoke the legacy classic PAT
- **B.** Create an OAuth App with full repo scope on the CEO account → hardcode the non-expiring OAuth token in YAML → disable OAuth App restrictions → delete audit logs
- **C.** Create 50 paid machine-user seats → share one classic PAT with admin:org across 50 scripts → turn off 2FA → ignore 5,000 req/hr shared user rate limits
- **D.** Register a GitHub App → commit its .pem private key to a public repo → use the 10-minute JWT directly as a REST bearer token for 30 days → keep classic PATs unrestricted

### 59. Compare **GitHub Apps**, **OAuth Apps**, and **Machine users** for enterprise automation. Which two administrative advantages favor **GitHub Apps** + strict PAT policies? Select two.

- **A.** Block or restrict **classic PATs** enterprise-wide while requiring **Organization Owner approval** and max expiration lifetimes (`<=30–90 days`) on **Fine-grained PATs**
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **E.** Migrate org automation from personal PATs (`5,000 req/hr`) to **GHEC GitHub App installation tokens** (`15,000 REST req/hr`, 1-hour expiry, zero seat cost)

### 60. In the **GitHub App** authentication flow, what is the maximum allowed expiration lifetime of the locally signed **RS256 JSON Web Token (`JWT`)** (`____ minutes`), and how long does the resulting **installation access token** remain valid (`____ hour`)?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **C.** Signing a short-lived **RS256 JWT** (`<=10 minutes`) with the **GitHub App private key** to call `POST /app/installations/{installation_id}/access_tokens` and mint a **1-hour** installation token
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 61. When **OAuth App access restrictions** are enabled on `@kestrelpay` (`default on new organizations`), a developer clicks `Authorize` on an unvetted third-party diagramming OAuth App and submits an approval request. Until an Organization Owner approves or denies it, what `@kestrelpay` data can that OAuth App read?

- **A.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Enabling **OAuth App access restrictions** and **GitHub App installation approval workflows** so developer-requested integrations stay blocked on private org data until vetted and approved by an Organization/Enterprise Owner

### 62. A read-only documentation mirror server needs SSH `git fetch` access to **one single repository** (`kestrelpay/api-specs`) without consuming a paid Enterprise seat or seeing any other repository in the org. Which credential fits best?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **C.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

---

## Domain 4 — Manage GitHub Actions (20–25% official weight · 24 questions)

### 63. A central DevSecOps guild builds golden CI/CD workflows (`sast-scan.yml`, `container-sign.yml`) to share privately across all 30 organizations in `KestrelPay` without making them public on the internet. Which two configurations achieve secure enterprise reuse? Select two.

- **A.** Enforce **`Require actions to be pinned to a full-length commit SHA`**, restrict allowed actions to verified/internal sources, and default `GITHUB_TOKEN` to **`Read-only`**
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **E.** Host reusable workflows (`workflow_call`) and composite actions in **`Internal`** enterprise repositories with cross-organization workflow `Access` enabled

### 64. An `Internal` repository `kestrelpay-shared/ci-templates` defines `.github/workflows/deploy.yml` with `on: ____`. Even though the repo is `Internal`, sibling organization `kestrelpay-mobile` receives `workflow file was not accessible` until which repository setting is toggled?

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Sharing reusable workflows (`on: workflow_call`) and composite actions in **`Internal`** or **`Private`** repositories with `Settings -> Actions -> General -> Access` enabled for organization/enterprise workflows
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 65. What is the key structural difference between a **Reusable Workflow** (`uses: org/repo/.github/workflows/ci.yml@<sha>`) and a **Composite Action** (`uses: org/repo/my-action@<sha>` with `runs: using: "composite"`)?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Sharing reusable workflows (`on: workflow_call`) and composite actions in **`Internal`** or **`Private`** repositories with `Settings -> Actions -> General -> Access` enabled for organization/enterprise workflows

### 66. Following a supply-chain audit of third-party GitHub Actions, which two enterprise/organization Actions policies block mutable tag hijacking and unauthorized runner execution? Select two.

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Isolate **Larger** and **ephemeral (`--ephemeral` / `ARC`) self-hosted runners** inside **Runner Groups** restricted to selected repositories and trusted reusable workflows
- **C.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **E.** Enforce **`Require actions to be pinned to a full-length commit SHA`**, restrict allowed actions to verified/internal sources, and default `GITHUB_TOKEN` to **`Read-only`**

### 67. Under `Enterprise -> Policies -> Actions -> General`, an admin selects **`Allow select actions and reusable workflows`**, checks `Allow actions created by GitHub`, and checks **`Require actions to be pinned to a full-length commit SHA`**. What happens if a workflow references `uses: thirdparty/lint@v2.4.0`?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Enforcing **Allowed actions and reusable workflows** (`GitHub-created`, `Verified creators`, internal patterns) plus **`Require actions to be pinned to a full-length commit SHA`**, `Read-only` default `GITHUB_TOKEN`, and fork PR approval

### 68. What should `Workflow permissions` for the automatic **`GITHUB_TOKEN`** be set to at the Enterprise/Organization policy level (`____`), requiring individual jobs that genuinely need write access to declare `permissions: contents: write` or `pull-requests: write` explicitly?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Enforcing **Allowed actions and reusable workflows** (`GitHub-created`, `Verified creators`, internal patterns) plus **`Require actions to be pinned to a full-length commit SHA`**, `Read-only` default `GITHUB_TOKEN`, and fork PR approval
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

### 69. A platform team designs hybrid compute for `KestrelPay` combining **Larger GitHub-hosted runners** and Kubernetes-orchestrated **Actions Runner Controller (`ARC`)** pods. Which three architectural controls belong in this design? Select three.

- **A.** Connect **Linux/Windows Larger GitHub-hosted runners** to an **Azure VNet** via `GitHub.Network/networkSettings` and Enterprise **Network Configurations**
- **B.** Isolate **Larger** and **ephemeral (`--ephemeral` / `ARC`) self-hosted runners** inside **Runner Groups** restricted to selected repositories and trusted reusable workflows
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **E.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **F.** Enforce **`Require actions to be pinned to a full-length commit SHA`**, restrict allowed actions to verified/internal sources, and default `GITHUB_TOKEN` to **`Read-only`**

### 70. Why does GitHub strongly recommend running self-hosted runners in **ephemeral mode** (`./config.sh --____` or Kubernetes **Actions Runner Controller (`ARC`)** `RunnerScaleSet` pods) rather than long-lived stateful VMs shared across dozens of repos?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Provisioning **ephemeral self-hosted runners** (`./config.sh --ephemeral` or REST **JIT runner** configs via **Actions Runner Controller `ARC`**) that execute **exactly one job** and self-destruct cleanly

### 71. Inside an Organization **Runner Group** (`prod-deploy-runners`), even if repository `kestrelpay/checkout` is allowed to use the runner group, how can admins stop a developer on an unreviewed `feat/test` branch from modifying `.github/workflows/ci.yml` to steal access to `prod-deploy-runners`?

- **A.** Organizing **Enterprise & Organization Runner Groups** restricted to selected repos and workflows, scaling **Larger GitHub-hosted runners** or ephemeral (`--ephemeral`) self-hosted runners via **Actions Runner Controller (`ARC`)** on Kubernetes
- **B.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 72. Network security requires GitHub-hosted CI builds to reach a private Azure Container Registry (`10.24.0.15`) inside an Azure Virtual Network without self-hosting VMs. Which four-step configuration sequence applies?

- **A.** Delegate Azure VNet subnet to GitHub.Network & create NetworkSettings → create GitHub Network Configuration → attach it to a Linux/Windows Larger runner group → scope runner group to approved repos/workflows
- **B.** Whitelist only Microsoft Azure IP ranges on standard Linux hosted runners → skip Azure VNet configuration → disable outbound access to github.com endpoints → run workflows
- **C.** Have an Organization Owner create a new Network Configuration while Enterprise policy blocks org configs → skip Azure resource ID linkage → assign to repository secrets → test
- **D.** Attach Azure VNet directly to free standard ubuntu-latest runners or macOS arm64 larger runners → skip GitHub.Network subnet delegation → allow all public fork PRs onto the private VNet runner group

### 73. Which two capabilities work together to let managed GitHub-hosted runners access internal corporate subnets while blocking unauthorized repositories from riding that private link? Select two.

- **A.** Connect **Linux/Windows Larger GitHub-hosted runners** to an **Azure VNet** via `GitHub.Network/networkSettings` and Enterprise **Network Configurations**
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Isolate **Larger** and **ephemeral (`--ephemeral` / `ARC`) self-hosted runners** inside **Runner Groups** restricted to selected repositories and trusted reusable workflows
- **E.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

### 74. An iOS build lead wants `macos-latest-xlarge` (`arm64` Apple Silicon Larger GitHub-hosted runners) to join the corporate **Azure Private Network (`VNet`)** configuration and receive static egress IPs. Proposed solution: Attach the Enterprise Azure VNet Network Configuration to an `arm64` macOS Larger runner group. Is Azure Private Networking supported on `arm64` macOS Larger runners?

- **A.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **B.** No — **Azure Private Networking** (`VNet` integration) and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, NOT on standard free runners or `arm64` macOS Larger runners
- **C.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **D.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret

### 75. A newly registered Linux self-hosted runner appears `Offline` in `Settings -> Actions -> Runners`. Which log file inside the runner installation directory (`_diag/____`) records listener startup, HTTPS long-polling, TLS certificate errors, and proxy failures?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Inspecting self-hosted runner **`_diag/Runner_*.log`** (registration, listener, network/proxy errors) and **`_diag/Worker_*.log`** (job step execution), `svc.sh status`, tool-cache disk usage, and Actions queue time metrics
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 76. In a locked-down enterprise subnet where outbound internet port `443` must traverse `http://proxy.kestrelpay.internal:8080`, where should admins define `https_proxy` and `no_proxy` on a Linux self-hosted runner running as a `systemd` service (`./svc.sh`)?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls

### 77. Developers complain self-hosted Docker builds fail intermittently with `ENOSPC: no space left on device` after 200 runs. What causes this on persistent self-hosted runners and how should admins remediate it?

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Inspecting self-hosted runner **`_diag/Runner_*.log`** (registration, listener, network/proxy errors) and **`_diag/Worker_*.log`** (job step execution), `svc.sh status`, tool-cache disk usage, and Actions queue time metrics
- **D.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing

### 78. An Organization Owner creates an Organization secret `PAYMENT_API_URL = https://prod.kestrelpay.io`, while repository `kestrelpay/checkout` already defines a `staging` **Environment** secret `PAYMENT_API_URL = https://stage.kestrelpay.io`. Proposed solution: Assume the **Organization** secret automatically overrides the `staging` **Environment** secret during a job targeting `environment: staging`. Which value actually wins at runtime?

- **A.** No — an organization’s default **Security Configuration** auto-attaches only to **newly created** repositories; repositories **transferred** into the organization must have the Security Configuration attached manually or via API
- **B.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret
- **C.** No — **Azure Private Networking** (`VNet` integration) and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, NOT on standard free runners or `arm64` macOS Larger runners
- **D.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement

### 79. To ensure a workflow job can read production deployment secrets **only** when triggered from `refs/heads/main` **and** after two SREs from `@kestrelpay/sre-oncall` approve, which GitHub Actions construct must hold those secrets?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Scoping encrypted secrets across **Organization -> Repository -> Environment** where **most specific wins (`Environment > Repository > Organization`)**, gated by Environment **Required reviewers** and **Deployment branches/rulesets**
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 80. Beyond human Required Reviewers and wait timers, which GHEC **Deployment Environment** feature (`____`) calls a registered GitHub App webhook to verify an approved ServiceNow Change Request (`CHG004912`) before unlocking `production` secrets?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Enforcing **Custom Deployment Protection Rules** (backed by a GitHub App checking ServiceNow change tickets or Datadog SLOs) alongside human Required Reviewers on `production` Environments
- **C.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **D.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO

### 81. When automating rotation of an Organization Actions secret via the GitHub REST API (`PUT /orgs/{org}/actions/secrets/{secret_name}`), how must the secret value be prepared client-side before sending the HTTPS request?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Configuring Organization secrets restricted to **`Selected repositories`** (or `Private and internal`), encrypting REST API secret uploads with the org/repo **LibSodium public key**, and separating non-sensitive **`vars`** from `secrets`

### 82. What is the maximum size of a single GitHub Actions secret (`____ KB`), and where should non-sensitive plain-text values like `DEFAULT_AWS_REGION=us-east-1` or `NODE_VERSION=22` be stored instead of `secrets.*`?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Configuring Organization secrets restricted to **`Selected repositories`** (or `Private and internal`), encrypting REST API secret uploads with the org/repo **LibSodium public key**, and separating non-sensitive **`vars`** from `secrets`
- **C.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 83. When creating an **Organization secret**, which visibility policy (`All repositories`, `Private and internal repositories`, or `____`) follows least privilege for sensitive shared signing certificates?

- **A.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Configuring Organization secrets restricted to **`Selected repositories`** (or `Private and internal`), encrypting REST API secret uploads with the org/repo **LibSodium public key**, and separating non-sensitive **`vars`** from `secrets`
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

### 84. Security architects eliminate static cloud credentials in GitHub by integrating **HashiCorp Vault** with **GitHub Actions** via **OpenID Connect (`OIDC`)**. Which four-step configuration sequence applies?

- **A.** Request an OIDC JWT first without configuring any Federated Identity Credential in Azure/Vault → hardcode client secrets when OIDC fails → grant write-all to fork PRs
- **B.** Configure OIDC trust policy in Vault/Azure/AWS with strict sub/aud claims → set job permissions id-token: write → exchange OIDC JWT at runtime for dynamic secret → delete static GitHub secrets
- **C.** Trust wildcard sub: repo:* in AWS/Vault with no org filter → leave id-token: none in workflow YAML → store root Vault token in plain-text Actions vars → echo token in logs
- **D.** Export static cloud admin keys into a public repository → commit .env to main → skip OIDC subject claim validation → rotate keys every 5 years

### 85. When configuring an Azure Entra ID Federated Identity Credential or AWS IAM OIDC trust policy for `https://token.actions.githubusercontent.com`, why is validating the exact **`sub`** (`subject`) claim (`e.g., repo:kestrelpay/checkout:environment:production`) critical?

- **A.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Federating GitHub Actions (`permissions: id-token: write`) via **OpenID Connect (`OIDC`)** with **HashiCorp Vault**, **Azure Key Vault**, or **AWS Secrets Manager** using strict `sub` (`repo:`/`environment:`) and `aud` claims

### 86. A workflow step running `azure/login@v2` with OIDC fails with `Error: Unable to get ACTIONS_ID_TOKEN_REQUEST_URL env variable`. Which YAML permission block was omitted from the workflow or job?

- **A.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Federating GitHub Actions (`permissions: id-token: write`) via **OpenID Connect (`OIDC`)** with **HashiCorp Vault**, **Azure Key Vault**, or **AWS Secrets Manager** using strict `sub` (`repo:`/`environment:`) and `aud` claims

---

## Domain 5 — Monitor and optimize GitHub usage (10–15% official weight · 14 questions)

### 87. Platform SREs notice intermittent `403 API rate limit exceeded` failures across `@kestrelpay` while compliance asks for 3-year tamper-evident admin audit retention. Which two monitoring capabilities address both needs? Select two.

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Correlate **Organization API Insights** (`rate-limited callers, top Apps/PATs`) with **Enterprise Audit Log** queries (`hashed_token`, `action:org.*`) to isolate noisy tokens
- **D.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **E.** Configure real-time **Enterprise Audit Log Streaming** (with optional Git events) to encrypted SIEM/WORM storage (`Azure Event Hubs`, `Blob`, `S3`, `Splunk`)

### 88. Under `Organization -> Insights -> ____` on GitHub Enterprise Cloud, which built-in analytics view breaks down total API requests, rate-limited requests, and route hotspots by individual **GitHub App**, **OAuth App**, and **Personal Access Token** actor?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **C.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **D.** Querying the **Enterprise Audit Log** (`action:`, `actor:`, `hashed_token:`) and **Organization API Insights** (`time-series requests, rate-limited callers, top GitHub Apps, OAuth Apps, and PATs`) to pinpoint noisy/failing integrations

### 89. Which Enterprise Audit Log search qualifier (`____:repo.destroy` or `action:org.update_member`) filters events by event category/operation across all organizations in the enterprise?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **C.** Querying the **Enterprise Audit Log** (`action:`, `actor:`, `hashed_token:`) and **Organization API Insights** (`time-series requests, rate-limited callers, top GitHub Apps, OAuth Apps, and PATs`) to pinpoint noisy/failing integrations
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 90. Before opening a Severity 1 **GitHub Enterprise Cloud** outage ticket when webhooks appear delayed, which public real-time telemetry endpoint (`https://www.____.com`) should an Enterprise Admin check first alongside webhook `Recent Deliveries`?

- **A.** Using GHES **Management Console / Grafana / `ghe-diagnostics` / Activity Dashboard** (or `githubstatus.com` + Enterprise Support portal with `Support Admin` entitlement on GHEC) to separate local misconfiguration from platform incidents
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges

### 91. On a self-hosted **GHES** cluster, which CLI utility (`____`) runs automated health checks across DNS, TLS certificates, storage mounts, Elasticsearch indices, MySQL/Redis replication, and service status from an admin SSH session on port `122`?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **C.** Scraping **GHES Prometheus `/metrics`** (or forwarding `syslog` + `SNMP` health traps) to alert platform SREs proactively on disk IOPS saturation, Redis/MySQL replication lag, and CPU load
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 92. Why must a self-hosted **GHES** administrator run **`github/backup-utils`** (`ghe-backup`) onto a separate backup host **even when** a live `ghe-repl-status` High Availability passive replica is healthy?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Deploying **GHES High Availability** (`ghe-repl-setup` active/passive failover replica) paired with incremental off-appliance snapshots via **`github/backup-utils`** (`ghe-backup` / `ghe-restore`)
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 93. An enterprise purchased 800 **GitHub Copilot Business** seats six months ago and wants to identify developers who have **never** triggered an inline completion or Chat prompt in the past 45 days. Which API/report provides exact per-seat `last_activity_at` timestamps?

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Querying the **GitHub Copilot User Management & Metrics REST APIs** (`last_activity_at`, `last_activity_editor`, acceptance/chat telemetry) to automate seat reclamation for inactive assignees
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 94. On **GitHub Enterprise Server (`GHES`)**, how does GitHub define a **Dormant user** (`configurable dormancy threshold, default ____ days`) so admins can audit inactive accounts consuming licenses?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Evaluating **Copilot Metrics API / Usage Dashboard** (active vs assigned seats, IDE/Chat/PR adoption), **Security Overview** coverage/MTTR, **Actions Usage Metrics**, and **GHES Dormant Users** reports to find underutilized features
- **C.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **D.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls

### 95. Which Enterprise/Organization dashboard lets platform engineering compare **GitHub Actions** workflow run volume, total billable minutes, average queue wait time, and failure rate by repository and OS runner type?

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Evaluating **Copilot Metrics API / Usage Dashboard** (active vs assigned seats, IDE/Chat/PR adoption), **Security Overview** coverage/MTTR, **Actions Usage Metrics**, and **GHES Dormant Users** reports to find underutilized features
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 96. Finance asks the GitHub Enterprise Admin to allocate metered cloud spend across 6 business units and prevent unexpected end-of-month overage bills. Which two practices establish FinOps governance? Select two.

- **A.** Assign orgs/repos to **Cost Centers** with **75/90/100% Budget alerts**, add `actions/cache`, shorten artifact `retention-days`, and move Linux workloads off `macos` runners
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Suspend/offboard **dormant users**, cancel stale pending org invitations, and audit **90-day active GHAS committers** plus **Copilot Metrics API** active-seat ratios
- **E.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 97. In `KestrelPay`, private repository `core-ledger` has **120** engineers with `Read` access, **30** PMs with `Triage`, and **18** developers who pushed commits to `core-ledger` within the last **90 days**. When **GitHub Advanced Security (`GHAS`)** is enabled on `core-ledger`, how many GHAS committer licenses are consumed?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Understanding that **GitHub Advanced Security (`GHAS`)** bills per **unique active committer** over a rolling **90-day** window across enabled private/internal repos (free on public repos!)
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 98. When interpreting a GitHub Actions metered usage CSV export, why does a 10-minute build on a standard **`macos`** GitHub-hosted runner consume far more billable quota than the exact same 10-minute build on **`ubuntu-latest`**?

- **A.** Analyzing **Enhanced Billing Platform** usage exports, **Cost Centers**, **Budgets & 75/90/100% alerts**, OS runner minute multipliers (`Linux < Windows < macOS`), shared **Actions/Packages storage**, and **90-day unique GHAS committers**
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 99. Ahead of annual renewal, the CIO asks platform administration to eliminate wasted Enterprise, GHAS, Copilot, and Actions spend without disrupting active squads. Which four-step optimization workflow applies?

- **A.** Export consumed-licenses & verify GitHub Connect GHES sync → audit dormant users, duplicate emails, and 90-day GHAS committers → reclaim idle seats & right-size budgets → enforce SCIM offboarding & alerts
- **B.** Hard-delete departing employees personal GitHub accounts via Support → break PR review audit history → turn off Dependabot and CodeQL everywhere → cancel Enterprise support
- **C.** Assign every contractor Enterprise Owner and Copilot Enterprise on day one → run Linux CI jobs on 10x-multiplier macOS runners → store 500 GB build artifacts for 400 days → review bills annually
- **D.** Delete historical employee Git commits to free GHAS seats immediately → disable GitHub Connect so GHEC+GHES users are billed twice → set unlimited Actions spending limits → skip budgets

### 100. A compliance officer worries that **suspending** 45 dormant users on GHES (or SCIM-deprovisioning departed EMUs on GHEC) to reclaim 45 Enterprise licenses will permanently delete their past Pull Request approvals and Git commits. Proposed solution: Keep paying for all 45 departed employees' active seats forever so historical PR reviews are not erased. Is keeping departed seats active necessary to preserve audit history?

- **A.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **B.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret
- **C.** No — suspending a dormant GHES user or removing/SCIM-deprovisioning a GHEC member **frees their Enterprise license seat** while **preserving all historical commits, Issues, and Pull Request audit trails**
- **D.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement

---

## Answer Key and Explanations

### Question 1 — `D, E` (Manage GitHub identities and access)

Correct answers: D and E (are correct). EMUs enforce corporate IdP/SCIM lifecycle while blocking public repos and Gists, and the IdP **Guest Collaborator** role restricts contractors from automatic `Internal` repository access. [Skill 1.1: Describe differences between managed users and personal accounts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: About Enterprise Managed Users vs personal accounts (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **D:** Correct. EMUs ensure corporate lifecycle control and eliminate accidental public repo or Gist leakage under managed handles.
- **E:** Correct. Guest Collaborators prevent contractors in EMU enterprises from automatically reading all `Internal` repositories across member organizations.

### Question 2 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). EMU usernames append your enterprise shortcode (`<username>_kpay`) provisioned fresh by your IdP; existing personal `github.com` accounts can never be converted in place into EMUs. [Skill 1.1: Describe differences between managed users and personal accounts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: About Enterprise Managed Users vs personal accounts (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users)]

- **A:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **B:** Correct. EMUs give enterprises full lifecycle ownership over user accounts via SAML/OIDC + SCIM while preventing public code/Gist creation and external repository contributions.
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 3 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Download and securely store the one-time **Enterprise SAML recovery codes** so an Enterprise Owner can bypass a broken IdP and restore SAML connectivity. [Skill 1.2: Configure and enforce SAML SSO and 2FA | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing SAML single sign-on and two-factor authentication (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise)]

- **A:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **B:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Correct. Enforcing SAML SSO at the Enterprise level centralizes IdP authentication across all member organizations, requires credential authorization for PATs/SSH keys, and pairs with `2FA` on personal-account GHEC.

### Question 4 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). GitHub immediately removes any member or outside collaborator without `2FA` enabled from the organization (and offers an automated reinstatement flow once they enable `2FA`). [Skill 1.2: Configure and enforce SAML SSO and 2FA | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing SAML single sign-on and two-factor authentication (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise)]

- **A:** Correct. Enforcing SAML SSO at the Enterprise level centralizes IdP authentication across all member organizations, requires credential authorization for PATs/SSH keys, and pairs with `2FA` on personal-account GHEC.
- **B:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **C:** Incorrect. In EMU enterprises, Guest Collaborators are IdP-provisioned accounts restricted from automatic `Internal` repository visibility across organizations unless granted explicit access.
- **D:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.

### Question 5 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Create the EMU enterprise and vault recovery codes first, configure SAML/OIDC SSO using the setup user, enable SCIM user/group provisioning in Okta, and map IdP groups to teams. [Skill 1.3: Understand SCIM and team synchronization: implementation and key differences | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring SCIM provisioning vs IdP team synchronization (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim/provisioning-users-and-groups-with-scim-using-the-rest-api)]

- **A:** Incorrect. Reverses prerequisite dependencies: SCIM and IdP group synchronization cannot run before the EMU enterprise exists and SAML/OIDC SSO is configured.
- **B:** Incorrect. SCIM on EMUs requires SAML or OIDC SSO first, and sharing setup credentials or granting universal Enterprise Owner violates least privilege.
- **C:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMU accounts; EMUs are brand-new IdP-provisioned accounts.
- **D:** Correct. Correct order: establish the EMU enterprise and offline recovery codes, wire SAML/OIDC SSO using the initial setup user, turn on SCIM user/group provisioning, and map IdP groups to teams.

### Question 6 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). No — on personal-account GHEC, **Team Synchronization** only updates Organization team membership for users who **already belong** to the organization; it cannot invite or add non-members into the organization! [Skill 1.3: Understand SCIM and team synchronization: implementation and key differences | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring SCIM provisioning vs IdP team synchronization (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim/provisioning-users-and-groups-with-scim-using-the-rest-api)]

- **A:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **B:** Correct. Personal-account Team Sync (`Entra ID`/`Okta`) never adds non-members into an organization; users must join the org via SAML/SCIM invitation first (or deploy GHEC with EMUs).
- **C:** Incorrect. While Enterprise teams excel at cross-org access, Copilot licensing, custom enterprise roles, and ruleset bypasses, `CODEOWNERS` requires Organization teams or individual users with Write+ access.
- **D:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — on personal-account GHEC, **Team Synchronization** only updates Organization team membership for users who **already belong** to the organization; it cannot invite or add non-members into the organization!

### Question 7 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). **Microsoft Entra ID** paired with **OpenID Connect (`OIDC`)** on GHEC EMUs natively enforces Entra Conditional Access Policies without duplicating IP allow lists inside GitHub. [Skill 1.4: Choose and configure identity providers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Choosing and configuring Identity Providers (Entra ID, Okta, PingFederate, CAS/LDAP) (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-identity-and-access-management)]

- **A:** Correct. Configuring OIDC between Entra ID and GHEC EMUs validates Entra Conditional Access Policies during browser sign-in and token refresh Flows.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 8 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). **GHES** supports native **`LDAP`** (including Active Directory bind, TLS/StartTLS, and LDAP group sync) in addition to **SAML 2.0** and **CAS**—unlike cloud GHEC, which uses SAML/OIDC. [Skill 1.4: Choose and configure identity providers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Choosing and configuring Identity Providers (Entra ID, Okta, PingFederate, CAS/LDAP) (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-identity-and-access-management)]

- **A:** Correct. GHEC EMUs support Entra ID (OIDC or SAML), Okta, and PingFederate (plus custom SAML+SCIM API integration), while GHES adds native LDAP, Active Directory, and CAS authentication.
- **B:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **C:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 9 — `A, E` (Manage GitHub identities and access)

Correct answers: A and E (are correct). Vault **SAML recovery codes** before enforcement, and require developers to **authorize** their SSH keys and PATs for SAML SSO (`Configure SSO -> Authorize`). [Skill 1.5: Explain GitHub’s authentication and authorization model | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub authentication and authorization model (SSH, PAT, OAuth, SAML, OIDC) (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)]

- **A:** Correct. Storing SAML recovery codes offline prevents total administrative lockout if the corporate Identity Provider experiences a certificate or service outage.
- **B:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **C:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **D:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **E:** Correct. SAML enforcement blocks un-authorized programmatic credentials (PATs and SSH keys) even when owned by valid organization members.

### Question 10 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). Authentication succeeded (GitHub verified who owns the PAT), whereas **SAML SSO authorization** failed because that token has not yet been authorized against the organization's SAML IdP! [Skill 1.5: Explain GitHub’s authentication and authorization model | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub authentication and authorization model (SSH, PAT, OAuth, SAML, OIDC) (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)]

- **A:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **B:** Correct. Even a valid personal PAT or SSH key (`authenticated`) is blocked from accessing a SAML-enforced GHEC organization until explicitly **authorized** for SAML SSO (`authorized`).
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.

### Question 11 — `C` (Manage GitHub identities and access)

Correct answer: C (is correct). Create a **Custom repository role** inheriting from `Read` or `Triage` and adding only the granular Actions/Environment permissions needed. [Skill 1.6: Configure organization and repository roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization roles, custom roles, and repository roles (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-organization-roles)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **C:** Correct. GitHub layers additive repository roles (`most permissive wins`) with least-privilege built-in and custom organization/enterprise roles.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 12 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Create a **Custom enterprise role** (or assign the predefined audit/security reader permissions) to the auditor user or **Enterprise team** rather than granting `Enterprise Owner`. [Skill 1.6: Configure organization and repository roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization roles, custom roles, and repository roles (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-organization-roles)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Correct. Custom enterprise roles delegate narrow slices of enterprise administration without exposing full owner control over SAML, billing, or organization deletion.

### Question 13 — `B, C, E` (Manage GitHub identities and access)

Correct answers: B, C, and E (are correct). Assign **Copilot Business** licenses, **enterprise roles**, and **ruleset bypasses** to Enterprise teams; map Enterprise teams across up to 1,000 organizations; and keep org **`Base permissions = None`**. [Skill 1.7: Define and manage enterprise teams | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining and managing Enterprise teams across organizations (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise)]

- **A:** Incorrect. IdP-synced Enterprise teams require zero manually added members and pause synchronization whenever the linked IdP group exceeds 5,000 users.
- **B:** Correct. Enterprise teams streamline multi-org role delegation, enterprise-level Copilot seat assignment, and ruleset bypass administration.
- **C:** Correct. Enterprise team organization assignments add members directly without invitations and protect enterprise-granted baseline access from org-level removal.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **E:** Correct. Setting Base permissions to `None` prevents newly added org members from automatically reading or writing every private repository in the organization.
- **F:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.

### Question 14 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). No — **Enterprise teams** currently do **not** support `CODEOWNERS` status (nor nested teams, Secret visibility, or Team maintainers); assign an **Organization team** with `Write`+ access in `CODEOWNERS` instead! [Skill 1.7: Define and manage enterprise teams | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining and managing Enterprise teams across organizations (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise)]

- **A:** Correct. While Enterprise teams excel at cross-org access, Copilot licensing, custom enterprise roles, and ruleset bypasses, `CODEOWNERS` requires Organization teams or individual users with Write+ access.
- **B:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — **Enterprise teams** currently do **not** support `CODEOWNERS` status (nor nested teams, Secret visibility, or Team maintainers); assign an **Organization team** with `Write`+ access in `CODEOWNERS` instead!
- **C:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **D:** Incorrect. Personal-account Team Sync (`Entra ID`/`Okta`) never adds non-members into an organization; users must join the org via SAML/SCIM invitation first (or deploy GHEC with EMUs).

### Question 15 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Because an Enterprise team caps at **`5,000` users**, IdP group syncing **pauses** (leaving membership frozen at `4,800`) until group membership is reduced back to `<= 5,000` users! [Skill 1.7: Define and manage enterprise teams | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining and managing Enterprise teams across organizations (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise)]

- **A:** Incorrect. IdP-synced Enterprise teams require zero manually added members and pause synchronization whenever the linked IdP group exceeds 5,000 users.
- **B:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **C:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **D:** Correct. Enterprise teams simplify multi-org governance, Copilot licensing, custom enterprise role delegation, and ruleset bypasses—though they do not support `CODEOWNERS`, nesting, Secret visibility, or non-EMU Team Sync.

### Question 16 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). Inspecting **`hashed_token`** (alongside `programmatic_access_type` and `token_id`) correlates every audit event performed by that exact PAT, OAuth token, or GitHub App installation token! [Skill 1.8: Audit access and permissions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Auditing repository, organization, and enterprise access permissions (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/identifying-audit-log-events-performed-by-an-access-token)]

- **A:** Correct. Admins audit effective access via People exports, repository Manage Access filters, REST/GraphQL permission queries, and Audit Log token attribution fields.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 17 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Under `Enterprise -> People -> Export` (or the GraphQL `enterprise.members` / REST membership APIs), owners export full cross-organization identity and access inventories. [Skill 1.8: Audit access and permissions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Auditing repository, organization, and enterprise access permissions (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/identifying-audit-log-events-performed-by-an-access-token)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. Admins audit effective access via People exports, repository Manage Access filters, REST/GraphQL permission queries, and Audit Log token attribution fields.

### Question 18 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). Targeting repositories dynamically via Custom Properties (`pci_scope:true`) auto-enrolls matching repos, and overlapping Rulesets layer cleanly under **most restrictive wins**! [Skill 1.9: Manage settings, policies, rulesets, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing enterprise member privileges, policies, repository rulesets, and bypass roles (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise)]

- **A:** Correct. Organization and Enterprise admins enforce schema-validated Custom Properties on repos and bind Rulesets to property queries (`compliance_tier:pci`) automatically.
- **B:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.

### Question 19 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Setting Enforcement status to **`Evaluate`** runs the Ruleset in non-blocking dry-run mode and logs simulated violations in **Rule Insights**. [Skill 1.9: Manage settings, policies, rulesets, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing enterprise member privileges, policies, repository rulesets, and bypass roles (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **D:** Correct. Enterprise policies set hard guardrails across all organizations, while Repository Rulesets layer additive branch/tag/push protections (`most restrictive wins`) with auditable bypasses.

### Question 20 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). Internal Maintainers/Admins resolve workflow check failures and Repository Ruleset policies; **GitHub Support** is reserved for platform availability incidents, server-side cache purges, and backend escalations. [Skill 2.1: Identify issues resolvable by admins vs GitHub Support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Identifying issues resolvable by Enterprise Admins vs GitHub Enterprise Support (https://docs.github.com/en/enterprise-cloud@latest/support/learning-about-github-support/about-github-support)]

- **A:** Correct. Admins handle internal identity, permissions, and pipeline configs, while GitHub Support handles cloud infrastructure incidents, server-side cache purges, and backend appliance/cloud escalations.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 21 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). Enterprise Owners can add up to **20** (standard Enterprise Support; higher on Premium Support) entitled members authorized to submit and manage enterprise support tickets. [Skill 2.1: Identify issues resolvable by admins vs GitHub Support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Identifying issues resolvable by Enterprise Admins vs GitHub Enterprise Support (https://docs.github.com/en/enterprise-cloud@latest/support/learning-about-github-support/about-github-support)]

- **A:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **B:** Correct. Admins handle internal identity, permissions, and pipeline configs, while GitHub Support handles cloud infrastructure incidents, server-side cache purges, and backend appliance/cloud escalations.
- **C:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **D:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 22 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). Confirm local triage and exact UTC timestamps, run `ghe-support-bundle -x` via SSH/Management Console, sanitize sensitive strings if required by policy, and upload the bundle on the GitHub Enterprise Support portal. [Skill 2.2: Generate support bundles and diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Generating GHES support bundles, ghe-diagnostics, and ticket diagnostics (https://docs.github.com/en/enterprise-server@latest/support/contacting-github-support/providing-data-to-github-support)]

- **A:** Correct. Correct escalation workflow: verify local admin triage and timestamps, generate an extended support bundle (`ghe-support-bundle -x`), verify compliance hygiene, and attach it on the Support portal.
- **B:** Incorrect. Never expose appliance secrets publicly or perform multi-version upgrades mid-incident without diagnostics.
- **C:** Incorrect. Corporate IdP/Active Directory password resets are strictly an internal administrator responsibility, not a GitHub Support issue.
- **D:** Incorrect. Wiping logs destroys root-cause evidence before capturing a support bundle, and GitHub Support never SSHes directly into customer GHES appliances.

### Question 23 — `B, C` (Administer GitHub Enterprise environment)

Correct answers: B and C (are correct). Capture an extended diagnostic bundle via `ghe-support-bundle -x` (never opening public SSH to Support) and pre-provision entitled **Support** portal members across your platform SRE team. [Skill 2.2: Generate support bundles and diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Generating GHES support bundles, ghe-diagnostics, and ticket diagnostics (https://docs.github.com/en/enterprise-server@latest/support/contacting-github-support/providing-data-to-github-support)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Correct. Enterprise Owners explicitly grant support-portal entitlement to designated engineers rather than sharing a single Enterprise Owner login.
- **C:** Correct. Extended support bundles give GitHub Support complete service, cluster, and error telemetry without exposing your appliance to external SSH.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **E:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 24 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). Creating a public **`.github`** repository (`kestrelpay-core/.github`) supplies default community health files, Issue/PR templates, and starter workflows across the organization. [Skill 2.3: Recommend standards for developer processes | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending enterprise standards for developer collaboration and InnerSource (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-best-practices/organize-work)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Correct. Enterprise developer standards combine golden template repositories, an org `.github` repo for default templates/policies, and `Internal` InnerSource visibility.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 25 — `D` (Administer GitHub Enterprise environment)

Correct answer: D (is correct). Placing workflow YAML + `.properties.json` pairs inside `.github/workflow-templates/` surfaces approved organization starter workflows in every repository's Actions setup gallery. [Skill 2.3: Recommend standards for developer processes | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending enterprise standards for developer collaboration and InnerSource (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-best-practices/organize-work)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **D:** Correct. Workflow templates in `<org>/.github/workflow-templates/` appear automatically in the `Actions -> New workflow` gallery for every repository in the organization.

### Question 26 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). **GitHub Merge Queue** (`gh-readonly-queue/main/...`) tests each queued PR (or batch) on top of ahead-in-queue changes so `main` stays green! [Skill 2.4: Define standards for workflows, branching, reviews, and releases | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining standards for workflows, branching, CODEOWNERS reviews, merge queues, and releases (https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Correct. Standardizing short-lived branches, Code Owner reviews, Merge Queue CI batching, and protected `v*` release tags keeps enterprise delivery predictable and auditable.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 27 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). Create a **Tag Repository Ruleset** targeting `refs/tags/v*` blocking tag **deletions**, **force-updates**, and unauthorized tag creation (and optionally requiring cryptographic tag signatures). [Skill 2.4: Define standards for workflows, branching, reviews, and releases | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining standards for workflows, branching, CODEOWNERS reviews, merge queues, and releases (https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. Standardizing short-lived branches, Code Owner reviews, Merge Queue CI batching, and protected `v*` release tags keeps enterprise delivery predictable and auditable.
- **D:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.

### Question 28 — `B, E` (Administer GitHub Enterprise environment)

Correct answers: B and E (are correct). `GHEC with Data Residency (<enterprise>.ghe.com)` pins repository code/metadata in a selected cloud region and mandates **EMUs**, while **GitHub Connect** deduplicates seats across hybrid `GHEC` + `GHES` deployments. [Skill 2.5: Describe GitHub Enterprise deployment scenarios (GHEC with EMU, GHEC with Data Residency + EMU, GHEC with personal accounts, GHES) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise deployment models (GHEC+EMU, GHEC Data Residency ghe.com, GHEC personal, GHES) (https://docs.github.com/en/enterprise-cloud@latest/admin/overview/about-github-for-enterprises)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Correct. GitHub Connect correlates verified email addresses across GHES and GHEC and reconciles Visual Studio Enterprise/Pro with GitHub Enterprise entitlements.
- **C:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **E:** Correct. GHEC with Data Residency hosts code and metadata on a dedicated regional `.ghe.com` cloud stamp and always requires Enterprise Managed Users.

### Question 29 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). `**GHEC with Data Residency + EMU**` hosts your enterprise on a dedicated regional `https://<enterprise>.ghe.com` cloud stamp managed by GitHub. [Skill 2.5: Describe GitHub Enterprise deployment scenarios (GHEC with EMU, GHEC with Data Residency + EMU, GHEC with personal accounts, GHES) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise deployment models (GHEC+EMU, GHEC Data Residency ghe.com, GHEC personal, GHES) (https://docs.github.com/en/enterprise-cloud@latest/admin/overview/about-github-for-enterprises)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **C:** Correct. GHEC with Data Residency (`<ent>.ghe.com`) always uses EMUs and pins code/metadata in a chosen region (EU/US/AU/JP), while GHES runs self-hosted in your own datacenter or sovereign cloud VPC.
- **D:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 30 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). Exactly **1** GitHub Enterprise seat—per-user Enterprise licensing deduplicates membership across all member organizations and GitHub Connect-synced GHES instances! [Skill 2.6: Explain licensing and billing models | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise licensing, metered user-based billing, and Visual Studio subscriptions (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/about-per-user-pricing)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Correct. One Enterprise user consumes a single seat across unlimited organizations in the enterprise (and synced GHES instances via GitHub Connect), while Actions, Packages, Codespaces, GHAS, and Copilot meter separately.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 31 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). Linked **Visual Studio with GitHub Enterprise** subscribers receive their GitHub Enterprise Cloud/Server seat entitlement through their Visual Studio subscription at no duplicate per-seat charge! [Skill 2.6: Explain licensing and billing models | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise licensing, metered user-based billing, and Visual Studio subscriptions (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/about-per-user-pricing)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. One Enterprise user consumes a single seat across unlimited organizations in the enterprise (and synced GHES instances via GitHub Connect), while Actions, Packages, Codespaces, GHAS, and Copilot meter separately.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 32 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). Unaccepted **pending organization invitations** and **outside collaborators** granted access to private/internal repositories each reserve/consume a GitHub Enterprise user license! [Skill 2.7: Monitor license usage and consumption | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring enterprise license consumption and GitHub Connect license sync (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/viewing-license-usage-for-github-enterprise)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Correct. Pending org invitations, outside collaborators on private repos, enterprise members, and unsynced duplicate emails across GHES/GHEC all impact Enterprise license counts and must be audited regularly.
- **D:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.

### Question 33 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). Export the encrypted/JSON **GHES user license usage file** from the GHES Management Console / CLI and upload it manually under `Enterprise -> Billing & Licensing -> Licensing` on GHEC! [Skill 2.7: Monitor license usage and consumption | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring enterprise license consumption and GitHub Connect license sync (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/viewing-license-usage-for-github-enterprise)]

- **A:** Correct. Pending org invitations, outside collaborators on private repos, enterprise members, and unsynced duplicate emails across GHES/GHEC all impact Enterprise license counts and must be audited regularly.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 34 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Verify GHAS committer seat headroom, create a custom Enterprise/Org Security Configuration, attach it to existing/transferred repos plus new-repo defaults, and set policy to `Enforce configuration`. [Skill 3.1: Define organization and enterprise policies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining organization and enterprise security policies and security configurations (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/about-security-configurations)]

- **A:** Incorrect. Manual per-repository toggling drifts immediately and misses centralized Security Configurations and enforcement.
- **B:** Incorrect. GHAS enablement fails if active-committer seats are exhausted, transferred repos require manual attachment, and disabling Actions breaks CodeQL default setup.
- **C:** Correct. Correct rollout: confirm active-committer license headroom, define the custom Security Configuration, apply it to existing/transferred repos and new-repo defaults, and enforce it.
- **D:** Incorrect. Settings left as `Not set` in a Security Configuration are explicitly not enforced against repository overrides.

### Question 35 — `A, B` (Implement secure software development and compliance)

Correct answers: A and B (are correct). Enforce an Enterprise/Org **Security Configuration** (manually attaching transferred repos alongside new-repo defaults) and enable **Secret Scanning Push Protection + Validity Checks + Delegated Bypass**. [Skill 3.1: Define organization and enterprise policies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining organization and enterprise security policies and security configurations (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/about-security-configurations)]

- **A:** Correct. Push Protection blocks secrets pre-receive, validity checks highlight live active credentials, and delegated bypass routes false-positive overrides through security reviewers.
- **B:** Correct. Enforced Security Configurations prevent repository admins from disabling mandatory Secret Protection, CodeQL, or Dependabot controls.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **E:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 36 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). No — default Security Configurations auto-apply **only** when a brand-new repository is **created** inside the organization; **transferred** repositories must have the Security Configuration attached manually or via REST API! [Skill 3.1: Define organization and enterprise policies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining organization and enterprise security policies and security configurations (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/about-security-configurations)]

- **A:** Incorrect. Deleting a file in a new commit never purges prior blob SHAs, and any exposed secret must be considered compromised and rotated immediately.
- **B:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **C:** Correct. GitHub applies default Security Configurations when a repository is newly created in the org, not when an existing repository is transferred in.
- **D:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — default Security Configurations auto-apply **only** when a brand-new repository is **created** inside the organization; **transferred** repositories must have the Security Configuration attached manually or via REST API!

### Question 37 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Git over SSH rejects static personal SSH keys and accepts **only** short-lived SSH certificates signed by your corporate SSH CA (for example, minted daily after SAML/OIDC login)! [Skill 3.2: Strengthen enterprise security posture and data protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Strengthening enterprise security posture, SSH CAs, IP allow lists, and data protection (https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)]

- **A:** Correct. SSH CAs eliminate unrotated static personal SSH keys by requiring short-lived certificates signed by the corporate CA, paired with IP allow lists (or Entra CAPs).
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 38 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Configuring **Push rules** inside a Repository Ruleset (`Restrict file paths`, `Restrict file extensions`, `Restrict max file size`) rejects offending pushes pre-receive across every branch! [Skill 3.2: Strengthen enterprise security posture and data protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Strengthening enterprise security posture, SSH CAs, IP allow lists, and data protection (https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)]

- **A:** Correct. Push rulesets evaluate file paths, extensions, and blob sizes on `git push` before commits land on any branch in targeted repositories.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.

### Question 39 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Because standard Linux GitHub-hosted runners draw from a vast multi-cloud pool; either switch jobs onto **Azure VNet / Larger runners with static IPs** added to the IP allow list, or enable **`Allow GitHub Actions access`** where policy permits! [Skill 3.2: Strengthen enterprise security posture and data protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Strengthening enterprise security posture, SSH CAs, IP allow lists, and data protection (https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **D:** Correct. SSH CAs eliminate unrotated static personal SSH keys by requiring short-lived certificates signed by the corporate CA, paired with IP allow lists (or Entra CAPs).

### Question 40 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). GitHub retains standard audit events in the UI/API for **180 days** (and high-volume Git events like `git.clone` for a much shorter window), so 1–7 year immutable retention requires **Audit Log Streaming** to external SIEM/storage! [Skill 3.3: Implement audit logging and reporting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Implementing audit logging, audit log streaming, and compliance reporting (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **D:** Correct. Because UI/REST audit retention is time-bounded (180 days standard; shorter for high-volume Git events), compliance teams stream immutable audit events continuously to external SIEM/WORM storage.

### Question 41 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). High-volume Git read/transport events (`git.clone`, `git.fetch`, `git.push`) are captured by enabling **`Stream Git events`** inside **Enterprise Audit Log Streaming** (or querying the GHES audit log)! [Skill 3.3: Implement audit logging and reporting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Implementing audit logging, audit log streaming, and compliance reporting (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)]

- **A:** Correct. Because UI/REST audit retention is time-bounded (180 days standard; shorter for high-volume Git events), compliance teams stream immutable audit events continuously to external SIEM/WORM storage.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 42 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). **Security Overview** provides enterprise- and organization-wide `Overview`, `Risk`, `Coverage`, `CodeQL`, `Dependabot`, and `Secret scanning` compliance views. [Skill 3.3: Implement audit logging and reporting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Implementing audit logging, audit log streaming, and compliance reporting (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **C:** Correct. Security Overview aggregates alert risk, push-protection metrics, and tool coverage across thousands of repositories for CISOs and Security Managers.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 43 — `C, D, E` (Implement secure software development and compliance)

Correct answers: C, D, and E (are correct). Enforce a centralized **Security Configuration**, enable **Secret Scanning Push Protection + Validity Checks + Delegated Bypass**, and enable **CodeQL + Dependabot security updates + PR Dependency Review**. [Skill 3.4: Configure vulnerability alerts, secret scanning, and CodeQL | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring vulnerability alerts, secret scanning push protection, and CodeQL code scanning (https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Correct. Combining CodeQL semantic analysis, Dependabot remediation PRs, and PR-time Dependency Review stops vulnerable code and packages before merge.
- **D:** Correct. Push Protection blocks secrets pre-receive, validity checks highlight live active credentials, and delegated bypass routes false-positive overrides through security reviewers.
- **E:** Correct. Enforced Security Configurations prevent repository admins from disabling mandatory Secret Protection, CodeQL, or Dependabot controls.
- **F:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 44 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). `Default setup` auto-detects interpreted/managed languages (`Python`, `JS/TS`, `Go`, `Java`, `C#`, `Ruby`) with zero YAML maintenance, whereas `Advanced setup` emits a customizable `.github/workflows/codeql.yml` workflow for bespoke C/C++ build commands or custom query suites! [Skill 3.4: Configure vulnerability alerts, secret scanning, and CodeQL | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring vulnerability alerts, secret scanning push protection, and CodeQL code scanning (https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Correct. CodeQL analyzes code semantically for CWE/OWASP flaws, while Secret Scanning Push Protection blocks credential commits pre-receive and verifies live token status via partner validity checks.

### Question 45 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Create an Enterprise/Org **Custom Secret Scanning Pattern** (`kpay_live_[A-Za-z0-9]{40}`), run a **dry run** against historical repos to tune regex/exclusions, then publish with **Push Protection** enabled! [Skill 3.4: Configure vulnerability alerts, secret scanning, and CodeQL | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring vulnerability alerts, secret scanning push protection, and CodeQL code scanning (https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)]

- **A:** Correct. Dry-running custom regex patterns at the org/enterprise level validates false-positive rates before publishing push-protection enforcement across repositories.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 46 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). **Dependabot security updates** open PRs strictly to patch dependencies with disclosed **CVEs/advisories**, whereas **Dependabot version updates** (`.github/dependabot.yml`) proactively keep packages/Actions up to date on a schedule even when no CVE exists! [Skill 3.5: Manage Dependabot and security advisories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing Dependabot alerts, security/version updates, private registries, and advisories (https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Correct. Dependabot flags known CVEs, opens automated upgrade PRs (authenticating to private registries when configured), blocks vulnerable PR dependencies via Dependency Review, and pairs with private Security Advisories.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 47 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Configure private-registry credentials under `Settings -> Code security -> Global settings` (or `dependabot.yml` `registries:`) and run **Dependabot on Actions / self-hosted / VNet-connected runners**! [Skill 3.5: Manage Dependabot and security advisories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing Dependabot alerts, security/version updates, private registries, and advisories (https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Correct. Granting Dependabot private-registry credentials (and running Dependabot on VNet-connected Actions/ARC runners) lets Dependabot resolve internal Artifactory/NuGet/npm packages securely.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 48 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). The **`dependency-review-action`** (`actions/dependency-review-action`) diffs lockfiles on Pull Requests and blocks vulnerable or policy-violating open-source licenses before merge! [Skill 3.5: Manage Dependabot and security advisories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing Dependabot alerts, security/version updates, private registries, and advisories (https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Correct. Dependabot flags known CVEs, opens automated upgrade PRs (authenticating to private registries when configured), blocks vulnerable PR dependencies via Dependency Review, and pairs with private Security Advisories.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.

### Question 49 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Immediately revoke & rotate the Stripe key in Stripe, scrub all branches/tags using `git filter-repo`, force-push cleaned refs and have collaborators re-clone, and send commit SHAs to GitHub Support to purge cached PR views. [Skill 3.6: Define and implement a security response plan | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining a security response plan and purging sensitive data from Git history (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]

- **A:** Correct. Correct incident response: treat the secret as compromised (revoke/rotate first!), scrub history with `git filter-repo`, force-push cleaned refs, and ask GitHub Support to purge unreachable cached views.
- **B:** Incorrect. Archiving keeps history readable to everyone with Read access, and merging uncleaned local clones reintroduces scrubbed commits.
- **C:** Incorrect. GitHub Support cannot rotate third-party cloud credentials; the enterprise admin must revoke/rotate the secret immediately in AWS.
- **D:** Incorrect. A normal `git rm` commit leaves the secret readable in prior commits and cached PR diffs, and unrotated leaked keys remain exploitable.

### Question 50 — `C, E` (Implement secure software development and compliance)

Correct answers: C and E (are correct). Immediately **revoke and rotate** the leaked key at the target provider, then rewrite Git history with **`git filter-repo`** and request a server-side cache purge from **GitHub Support**. [Skill 3.6: Define and implement a security response plan | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining a security response plan and purging sensitive data from Git history (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Correct. Publicly or internally pushed secrets can be scraped within seconds by bots or clones; credential revocation/rotation is always step #1.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **E:** Correct. `git filter-repo` rewrites Git history cleanly, and GitHub Support purges unreachable commit objects and cached Pull Request diffs on GitHub servers.

### Question 51 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). No — `git rm` only removes the file from the latest commit snapshot while leaving the credential exposed in the parent commit SHA and Pull Request diff; **revoke/rotate the AWS key immediately**, run `git filter-repo`, and contact GitHub Support! [Skill 3.6: Define and implement a security response plan | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining a security response plan and purging sensitive data from Git history (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]

- **A:** Incorrect. GitHub applies default Security Configurations when a repository is newly created in the org, not when an existing repository is transferred in.
- **B:** Correct. Deleting a file in a new commit never purges prior blob SHAs, and any exposed secret must be considered compromised and rotated immediately.
- **C:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **D:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — `git rm` only removes the file from the latest commit snapshot while leaving the credential exposed in the parent commit SHA and Pull Request diff; **revoke/rotate the AWS key immediately**, run `git filter-repo`, and contact GitHub Support!

### Question 52 — `D, E` (Implement secure software development and compliance)

Correct answers: D and E (are correct). Restrict/block **classic PATs** while requiring **Owner approval** and max expiration (`<=30–90 days`) on **Fine-grained PATs**, and migrate automation bots to **GitHub App installation tokens**. [Skill 3.7: Configure personal access tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring fine-grained and classic Personal Access Token (PAT) enterprise policies (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Correct. Enterprise PAT policies replace broad non-expiring classic tokens with short-lived, repo-scoped, admin-approved Fine-grained PATs.
- **E:** Correct. GitHub App installations on GHEC provide 3x higher REST throughput, short-lived 1-hour credentials, and complete decoupling from employee turnover.

### Question 53 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). Until an Organization Owner approves the token request, that Fine-grained PAT can read **only public resources** and has zero access to private/internal `@kestrelpay` repositories! [Skill 3.7: Configure personal access tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring fine-grained and classic Personal Access Token (PAT) enterprise policies (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise)]

- **A:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **B:** Correct. Enterprise PAT policies curb broad non-expiring classic PATs and require organization owner approval, repo scoping, and short lifetimes on Fine-grained PATs.
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 54 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Yes — Organization Owners can view and immediately **revoke** active Fine-grained PAT org access and deauthorize SAML-authorized tokens/SSH keys without waiting for the user! [Skill 3.7: Configure personal access tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring fine-grained and classic Personal Access Token (PAT) enterprise policies (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise)]

- **A:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. Enterprise PAT policies curb broad non-expiring classic PATs and require organization owner approval, repo scoping, and short lifetimes on Fine-grained PATs.

### Question 55 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). No — all PATs belonging to one user share that single user's **`5,000 req/hr`** quota; migrate the automation to an org-installed **GitHub App** using installation access tokens (`15,000 req/hr` on GHEC)! [Skill 3.8: Understand rate limits for PATs and GitHub Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Understanding REST and GraphQL API rate limits for PATs, GitHub Apps, and GITHUB_TOKEN (https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — all PATs belonging to one user share that single user's **`5,000 req/hr`** quota; migrate the automation to an org-installed **GitHub App** using installation access tokens (`15,000 req/hr` on GHEC)!
- **B:** Incorrect. Personal-account Team Sync (`Entra ID`/`Okta`) never adds non-members into an organization; users must join the org via SAML/SCIM invitation first (or deploy GHEC with EMUs).
- **C:** Incorrect. While Enterprise teams excel at cross-org access, Copilot licensing, custom enterprise roles, and ruleset bypasses, `CODEOWNERS` requires Organization teams or individual users with Write+ access.
- **D:** Correct. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.

### Question 56 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). On **GHEC**, a GitHub App installation receives **`15,000` requests/hour**; on non-GHEC organizations, it starts at `5,000` (+50/repo and +50/user above 20) up to a maximum of **`12,500` requests/hour**! [Skill 3.8: Understand rate limits for PATs and GitHub Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Understanding REST and GraphQL API rate limits for PATs, GitHub Apps, and GITHUB_TOKEN (https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Correct. On GHEC, GitHub App installations get 15,000 REST req/hr (and 10,000 GraphQL pts/hr) isolated from human users, whereas user PATs share one 5,000 req/hr personal bucket and hit secondary concurrency caps faster.
- **C:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 57 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). High burst concurrency or rapid unspaced write mutations triggered **Secondary rate limits**; cap concurrent threads, space write calls (`>=1s`), use webhooks/GraphQL/Conditional `ETag` (`304`), and sleep for `Retry-After` seconds! [Skill 3.8: Understand rate limits for PATs and GitHub Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Understanding REST and GraphQL API rate limits for PATs, GitHub Apps, and GITHUB_TOKEN (https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api)]

- **A:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **B:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **C:** Correct. `304 Not Modified` conditional requests do not count against primary REST rate limits, while webhook-driven architectures and `Retry-After` backoff prevent secondary `403` throttling.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 58 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Create an org-owned GitHub App with least-privilege permissions, vault its `.pem` private key and install on selected repos, sign a short-lived JWT to mint 1-hour installation tokens, and revoke the legacy PAT. [Skill 3.9: Describe GitHub Apps and OAuth Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Comparing GitHub Apps, OAuth Apps, deploy keys, and machine users (https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)]

- **A:** Correct. Correct migration: register a fine-grained GitHub App, safeguard its private key and scope installation repos, mint 1-hour installation tokens via signed JWT, and retire the classic PAT.
- **B:** Incorrect. OAuth Apps use broad user-tied scopes and long-lived tokens rather than actor-independent 1-hour installation tokens.
- **C:** Incorrect. Machine users consume paid Enterprise seats and share a 5,000 req/hr user rate limit instead of GHEC GitHub App installation scaling (15,000 req/hr).
- **D:** Incorrect. App `.pem` keys must never be committed, and a GitHub App JWT (max 10 minutes) only authenticates App endpoints to mint a 1-hour installation token.

### Question 59 — `A, E` (Implement secure software development and compliance)

Correct answers: A and E (are correct). **GitHub App** installations on GHEC run independent of human seats with 1-hour tokens and `15,000 req/hr`, while strict **Fine-grained PAT** policies curb broad user-bound tokens. [Skill 3.9: Describe GitHub Apps and OAuth Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Comparing GitHub Apps, OAuth Apps, deploy keys, and machine users (https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)]

- **A:** Correct. Enterprise PAT policies replace broad non-expiring classic tokens with short-lived, repo-scoped, admin-approved Fine-grained PATs.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **E:** Correct. GitHub App installations on GHEC provide 3x higher REST throughput, short-lived 1-hour credentials, and complete decoupling from employee turnover.

### Question 60 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). The App's locally signed **JWT** is valid for at most **`10 minutes`**, and exchanging it at `/app/installations/{id}/access_tokens` returns an installation access token valid for **`1 hour`**! [Skill 3.9: Describe GitHub Apps and OAuth Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Comparing GitHub Apps, OAuth Apps, deploy keys, and machine users (https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **C:** Correct. GitHub Apps never send their `.pem` private key over the network; they sign a <=10-minute JWT locally and exchange it for a scoped 1-hour installation access token.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 61 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Zero private or internal `@kestrelpay` data—unapproved OAuth Apps are strictly blocked from restricted organization resources until explicitly approved by an Organization Owner! [Skill 3.10: Approve or deny app usage based on policy | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Approving, denying, and governing OAuth Apps and GitHub App installations (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions)]

- **A:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. With OAuth App access restrictions active, unapproved third-party OAuth apps can read public data only and cannot touch organization private repos until an Owner explicitly approves the request.

### Question 62 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Attach a read-only **Deploy key** (`Repository Settings -> Deploy keys`, leaving `Allow write access` unchecked) scoped exclusively to `kestrelpay/api-specs`! [Skill 3.10: Approve or deny app usage based on policy | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Approving, denying, and governing OAuth Apps and GitHub App installations (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **C:** Correct. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 63 — `A, E` (Manage GitHub Actions)

Correct answers: A and E (are correct). Store `workflow_call` workflows and composite actions in **`Internal`** repos with enterprise workflow `Access` enabled, and enforce **40-char commit SHA pinning** + `Read-only` `GITHUB_TOKEN` defaults. [Skill 4.1: Configure and manage reuse of actions and workflows to the enterprise repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Sharing reusable workflows and actions privately across enterprise organizations (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Correct. 40-char SHA pinning neutralizes upstream tag hijacking while read-only `GITHUB_TOKEN` defaults enforce job-level least privilege.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **E:** Correct. Enterprise teams reuse vetted CI/CD templates privately across all member organizations without exposing proprietary workflows publicly.

### Question 64 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Define `on: workflow_call` **and** set `Repository Settings -> Actions -> General -> Access` to **`Accessible from repositories in the 'KestrelPay' enterprise`**! [Skill 4.1: Configure and manage reuse of actions and workflows to the enterprise repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Sharing reusable workflows and actions privately across enterprise organizations (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Correct. Without publishing proprietary actions to the public internet, enterprises host golden `workflow_call` workflows and actions inside `Internal`/`Private` repos with cross-repo enterprise workflow access enabled.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 65 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). A **Reusable Workflow** orchestrates entire `jobs:` (including matrix strategies, runner selection, and `environment:` gates), whereas a **Composite Action** bundles multiple steps inside a single step of an existing job! [Skill 4.1: Configure and manage reuse of actions and workflows to the enterprise repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Sharing reusable workflows and actions privately across enterprise organizations (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Correct. Without publishing proprietary actions to the public internet, enterprises host golden `workflow_call` workflows and actions inside `Internal`/`Private` repos with cross-repo enterprise workflow access enabled.

### Question 66 — `B, E` (Manage GitHub Actions)

Correct answers: B and E (are correct). Enable **`Require actions to be pinned to a full-length commit SHA`** + `Read-only` `GITHUB_TOKEN`, and restrict **Runner Groups** to selected repositories and trusted workflow paths. [Skill 4.2: Apply organizational policies for GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing enterprise and organization GitHub Actions policies and SHA pinning (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Correct. Runner group repository and workflow restrictions prevent untrusted repos or ad-hoc branches from scheduling jobs onto privileged runners.
- **C:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **E:** Correct. 40-char SHA pinning neutralizes upstream tag hijacking while read-only `GITHUB_TOKEN` defaults enforce job-level least privilege.

### Question 67 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). GitHub immediately fails the workflow run before execution because `@v2.4.0` is a mutable Git tag rather than a full **40-character commit SHA**! [Skill 4.2: Apply organizational policies for GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing enterprise and organization GitHub Actions policies and SHA pinning (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. Pinning third-party actions to immutable 40-char commit SHAs blocks tag-mutation supply-chain attacks, while `permissions: read-all` / read-only `GITHUB_TOKEN` defaults enforce least privilege.

### Question 68 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Enforce **`Read repository contents and packages permissions`** (`Read-only`) by default so untrusted steps never inherit broad implicit write permissions! [Skill 4.2: Apply organizational policies for GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing enterprise and organization GitHub Actions policies and SHA pinning (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Correct. Pinning third-party actions to immutable 40-char commit SHAs blocks tag-mutation supply-chain attacks, while `permissions: read-all` / read-only `GITHUB_TOKEN` defaults enforce least privilege.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 69 — `A, B, F` (Manage GitHub Actions)

Correct answers: A, B, and F (are correct). Isolate runners in scoped **Runner Groups**, connect Linux/Windows Larger runners to an **Azure VNet** via Network Configurations, and enforce **SHA-pinned actions** + `Read-only` `GITHUB_TOKEN`. [Skill 4.3: Manage runner groups and administer GitHub-hosted vs. self-hosted runner options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing runner groups, Larger runners, self-hosted runners, and Actions Runner Controller (ARC) (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Correct. Azure Private Networking gives managed GitHub-hosted Larger runners private VNet egress to internal endpoints and predictable firewall/NAT egress IPs.
- **B:** Correct. Runner group repository and workflow restrictions prevent untrusted repos or ad-hoc branches from scheduling jobs onto privileged runners.
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **E:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **F:** Correct. 40-char SHA pinning neutralizes upstream tag hijacking while read-only `GITHUB_TOKEN` defaults enforce job-level least privilege.

### Question 70 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). Passing `--ephemeral` (or scaling ephemeral pods via `ARC`) destroys the runner environment after **one single job**, preventing secret remnants, poisoned `/tmp` caches, or lateral malware persistence! [Skill 4.3: Manage runner groups and administer GitHub-hosted vs. self-hosted runner options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing runner groups, Larger runners, self-hosted runners, and Actions Runner Controller (ARC) (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. Single-use ephemeral runners prevent cross-job workspace contamination, lingering credentials, or persistent malware across CI builds.

### Question 71 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). Enable **`Restrict workflows that have access to this runner group`** and list **only** vetted reusable workflows (`e.g., kestrelpay-shared/ci-templates/.github/workflows/prod-deploy.yml@<sha>`)! [Skill 4.3: Manage runner groups and administer GitHub-hosted vs. self-hosted runner options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing runner groups, Larger runners, self-hosted runners, and Actions Runner Controller (ARC) (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Correct. Runner groups isolate sensitive self-hosted or Larger runners to approved repositories and reusable workflow refs, while `--ephemeral` JIT / ARC pods ensure clean single-job runner state.
- **B:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 72 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). Delegate an Azure VNet subnet to `GitHub.Network` and create `NetworkSettings`, create a GitHub Network Configuration, attach it to a Linux/Windows Larger runner group, and scope the runner group to approved repos/workflows. [Skill 4.4: Apply IP allow lists and configure networking (including Azure private networking) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring IP allow lists, proxies, and Azure private networking (VNet) for runners (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization)]

- **A:** Correct. Correct sequence: prepare the delegated Azure VNet + `GitHub.Network/networkSettings` resource, register the GitHub Network Configuration, bind it to a Larger runner group, and restrict repo/workflow access.
- **B:** Incorrect. Standard Linux runners use a multi-cloud pool beyond Azure IPs, and VNet-integrated runners still require outbound access to required GitHub endpoints.
- **C:** Incorrect. By default Enterprise policy restricts org-created Network Configurations unless enabled by an Enterprise Owner, and Azure NetworkSettings linkage is mandatory.
- **D:** Incorrect. Azure private networking requires Linux/Windows Larger runners (not macOS arm64 larger runners), subnet delegation, and strict runner-group access controls.

### Question 73 — `A, D` (Manage GitHub Actions)

Correct answers: A and D (are correct). Bind **Linux/Windows Larger runners** to an **Azure VNet** via `GitHub.Network/networkSettings` + **Network Configurations**, and lock those runners inside a **Runner Group** scoped to selected repositories/workflows. [Skill 4.4: Apply IP allow lists and configure networking (including Azure private networking) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring IP allow lists, proxies, and Azure private networking (VNet) for runners (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization)]

- **A:** Correct. Azure Private Networking gives managed GitHub-hosted Larger runners private VNet egress to internal endpoints and predictable firewall/NAT egress IPs.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Correct. Runner group repository and workflow restrictions prevent untrusted repos or ad-hoc branches from scheduling jobs onto privileged runners.
- **E:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 74 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). No — **Azure Private Networking** and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, **not** on `arm64` macOS Larger runners (use self-hosted macOS runners on private networks if private egress is required)! [Skill 4.4: Apply IP allow lists and configure networking (including Azure private networking) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring IP allow lists, proxies, and Azure private networking (VNet) for runners (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — **Azure Private Networking** and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, **not** on `arm64` macOS Larger runners (use self-hosted macOS runners on private networks if private egress is required)!
- **B:** Correct. Standard hosted runners cannot join customer Azure VNets, and arm64 macOS Larger runners do not support Azure private networking or static IP assignment.
- **C:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **D:** Incorrect. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.

### Question 75 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). `_diag/Runner_<timestamp>.log` captures the self-hosted runner listener service lifecycle and network connectivity errors (whereas `_diag/Worker_<timestamp>.log` logs individual job step execution). [Skill 4.5: Monitor and troubleshoot runner performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring and troubleshooting runner _diag logs, queues, and performance (https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Correct. `Runner_*.log` records control-plane polling/TLS/proxy failures on the self-hosted agent, whereas `Worker_*.log` captures per-job execution details when jobs fail or stall.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 76 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). Write `https_proxy=...` and `no_proxy=...` into the **`.env`** file inside the self-hosted runner root directory before starting/restarting `./svc.sh` so both listener and worker processes inherit proxy settings! [Skill 4.5: Monitor and troubleshoot runner performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring and troubleshooting runner _diag logs, queues, and performance (https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.

### Question 77 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Stale Docker layers, `_work/` directories, and `_tool` caches accumulate on persistent disks; migrate to **ephemeral (`--ephemeral` / `ARC`) runners** or configure pre/post job cleanup hooks (`ACTIONS_RUNNER_HOOK_JOB_COMPLETED`) and disk monitoring! [Skill 4.5: Monitor and troubleshoot runner performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring and troubleshooting runner _diag logs, queues, and performance (https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Correct. `Runner_*.log` records control-plane polling/TLS/proxy failures on the self-hosted agent, whereas `Worker_*.log` captures per-job execution details when jobs fail or stall.
- **D:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.

### Question 78 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). No — GitHub Actions secret precedence runs **`Environment > Repository > Organization`** (`most specific wins`), so the `staging` **Environment** secret overrides both Repository and Organization secrets! [Skill 4.6: Define scope and access for secrets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining secret scope, hierarchy precedence, and deployment environment access controls (https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. GitHub applies default Security Configurations when a repository is newly created in the org, not when an existing repository is transferred in.
- **B:** Correct. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.
- **C:** Incorrect. Standard hosted runners cannot join customer Azure VNets, and arm64 macOS Larger runners do not support Azure private networking or static IP assignment.
- **D:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — GitHub Actions secret precedence runs **`Environment > Repository > Organization`** (`most specific wins`), so the `staging` **Environment** secret overrides both Repository and Organization secrets!

### Question 79 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Store the secrets inside a **`production` Deployment Environment** configured with **Required reviewers** (`@kestrelpay/sre-oncall`) and **Deployment branches** restricted to `main`! [Skill 4.6: Define scope and access for secrets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining secret scope, hierarchy precedence, and deployment environment access controls (https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Correct. Production cloud secrets belong in protected Deployment Environments (`environment: production`) gated by human/custom deployment protection rules and branch filters, overriding broader repo/org secrets.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 80 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). **Custom deployment protection rules** invoke an installed GitHub App (such as ServiceNow, Datadog, or Honeycomb) to programmatically approve or reject environment deployments! [Skill 4.6: Define scope and access for secrets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining secret scope, hierarchy precedence, and deployment environment access controls (https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Correct. Custom deployment protection rules gate `environment: production` jobs automatically via webhook callbacks to external ITSM or observability systems.
- **C:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **D:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.

### Question 81 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). Fetch the organization's Actions public key (`GET /orgs/{org}/actions/secrets/public-key`) and encrypt the secret client-side using **LibSodium sealed-box (`crypto_box_seal`)** before `PUT`ting `encrypted_value`! [Skill 4.7: Configure secrets at organization and repository levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization and repository encrypted secrets and variables via UI and REST API (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/creating-secrets-for-an-organization)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. Organization secrets never pass to public repos unless explicitly permitted, API writes require LibSodium sealed-box encryption (`48 KB` max per secret), and plain-text config belongs in `vars` context.

### Question 82 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Individual Actions secrets cap at **`48 KB`**; non-sensitive plain-text parameters belong in Organization/Repository/Environment **Configuration Variables (`vars.*`)** so logs remain readable without wasting secret slots! [Skill 4.7: Configure secrets at organization and repository levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization and repository encrypted secrets and variables via UI and REST API (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/creating-secrets-for-an-organization)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Correct. Organization secrets never pass to public repos unless explicitly permitted, API writes require LibSodium sealed-box encryption (`48 KB` max per secret), and plain-text config belongs in `vars` context.
- **C:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 83 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Scoping the Organization secret to **`Selected repositories`** ensures only explicitly listed repositories can reference that credential in workflows. [Skill 4.7: Configure secrets at organization and repository levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization and repository encrypted secrets and variables via UI and REST API (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/creating-secrets-for-an-organization)]

- **A:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Correct. Organization secrets never pass to public repos unless explicitly permitted, API writes require LibSodium sealed-box encryption (`48 KB` max per secret), and plain-text config belongs in `vars` context.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 84 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Configure a Vault JWT/OIDC role bound to strict `sub`/`aud` claims (`org`, `repo`, `environment`), set job `permissions: id-token: write`, exchange the OIDC JWT at runtime via `hashicorp/vault-action`, and delete static GitHub secrets. [Skill 4.8: Integrate third-party vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Integrating third-party secret vaults (HashiCorp Vault, Azure Key Vault, AWS) via OIDC (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. The external vault/cloud IdP must trust `https://token.actions.githubusercontent.com` and exact subject claims before OIDC exchange can succeed.
- **B:** Correct. Correct passwordless vault flow: lock down cloud/vault OIDC subject claims first, grant `id-token: write`, exchange the ephemeral OIDC token at runtime, and remove static secrets.
- **C:** Incorrect. Wildcard `repo:*` subject claims let any GitHub repository assume your cloud role, and `id-token: write` is required to request an OIDC token.
- **D:** Incorrect. Storing static admin keys in repositories creates catastrophic credential exposure instead of ephemeral OIDC federation.

### Question 85 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). Every GitHub customer shares the issuer `https://token.actions.githubusercontent.com`; pinning **`sub`** to your exact `org/repo` and `environment`/`ref` prevents external repositories or untrusted feature branches from assuming your cloud role! [Skill 4.8: Integrate third-party vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Integrating third-party secret vaults (HashiCorp Vault, Azure Key Vault, AWS) via OIDC (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Correct. OIDC exchanges a job-scoped JWT signed by `https://token.actions.githubusercontent.com` for short-lived dynamic vault credentials at runtime—eliminating static secrets stored in GitHub.

### Question 86 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). The workflow or job omitted **`permissions: id-token: write`** (needed alongside `contents: read` when explicit `permissions:` overrides defaults) so the runner did not expose the OIDC token endpoint! [Skill 4.8: Integrate third-party vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Integrating third-party secret vaults (HashiCorp Vault, Azure Key Vault, AWS) via OIDC (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Correct. OIDC exchanges a job-scoped JWT signed by `https://token.actions.githubusercontent.com` for short-lived dynamic vault credentials at runtime—eliminating static secrets stored in GitHub.

### Question 87 — `C, E` (Monitor and optimize GitHub usage)

Correct answers: C and E (are correct). Correlate **Organization API Insights** (`rate-limited callers, top Apps/PATs`) with **Audit Log `hashed_token`** queries, and stream **Enterprise Audit Logs** continuously to SIEM/WORM storage. [Skill 5.1: Analyze audit logs and API usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Analyzing enterprise audit logs, Git events, and API Insights / REST/GraphQL metrics (https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-your-team/apicenter/viewing-api-insights-for-your-organization)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Correct. API Insights pinpoints which App or PAT user is exhausting rate limits while Audit Log `hashed_token` traces exact administrative/API actions.
- **D:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **E:** Correct. Continuous Audit Log Streaming preserves tamper-evident compliance records far beyond GitHub’s interactive 180-day UI retention window.

### Question 88 — `D` (Monitor and optimize GitHub usage)

Correct answer: D (is correct). **API Insights** gives Organization Owners and custom-role holders granular visibility into API callers, status codes, and rate-limit bottlenecks. [Skill 5.1: Analyze audit logs and API usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Analyzing enterprise audit logs, Git events, and API Insights / REST/GraphQL metrics (https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-your-team/apicenter/viewing-api-insights-for-your-organization)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **C:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **D:** Correct. API Insights visualizes hourly/daily REST consumption and `403`/`429` rate-limit hits broken down by specific App or PAT user so admins fix runaway polling loops quickly.

### Question 89 — `C` (Monitor and optimize GitHub usage)

Correct answer: C (is correct). Using **`action:`** (combined with `actor:`, `org:`, `repo:`, `created:`, or `hashed_token:`) filters the Enterprise Audit Log to exact administrative or security operations. [Skill 5.1: Analyze audit logs and API usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Analyzing enterprise audit logs, Git events, and API Insights / REST/GraphQL metrics (https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-your-team/apicenter/viewing-api-insights-for-your-organization)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **C:** Correct. API Insights visualizes hourly/daily REST consumption and `403`/`429` rate-limit hits broken down by specific App or PAT user so admins fix runaway polling loops quickly.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 90 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). Check **`githubstatus.com`** (and subscribe to component Atom/webhook alerts for `Actions`, `API Requests`, `Webhooks`, and `Git Operations`) to confirm whether an active platform incident is already underway. [Skill 5.2: Distinguish admin responsibilities vs. GitHub Support and generate diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Distinguishing admin vs GitHub Support responsibilities and generating appliance/cloud diagnostics (https://docs.github.com/en/enterprise-server@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/activity-dashboard)]

- **A:** Correct. Admins first inspect `githubstatus.com`, SAML/webhook delivery logs, and `ghe-diagnostics` CPU/memory/queue health, escalating to GitHub Support via entitled Enterprise Support members with bundles attached.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.

### Question 91 — `C` (Monitor and optimize GitHub usage)

Correct answer: C (is correct). Running **`ghe-diagnostics`** executes comprehensive non-destructive health diagnostics across all internal GHES subsystems and prints actionable report output. [Skill 5.2: Distinguish admin responsibilities vs. GitHub Support and generate diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Distinguishing admin vs GitHub Support responsibilities and generating appliance/cloud diagnostics (https://docs.github.com/en/enterprise-server@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/activity-dashboard)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **C:** Correct. GHES exposes native Prometheus metrics, SNMP, and syslog forwarding so enterprise monitoring stacks catch resource pressure before outages occur.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 92 — `C` (Monitor and optimize GitHub usage)

Correct answer: C (is correct). High Availability (`HA`) replicates accidental repository/org deletions and logical corruption **immediately** to the passive replica; only off-appliance point-in-time **`backup-utils` snapshots** protect against logical deletion or ransomware! [Skill 5.2: Distinguish admin responsibilities vs. GitHub Support and generate diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Distinguishing admin vs GitHub Support responsibilities and generating appliance/cloud diagnostics (https://docs.github.com/en/enterprise-server@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/activity-dashboard)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Correct. HA replication protects against primary VM hardware failure, while scheduled `backup-utils` snapshots on a separate host provide point-in-time disaster recovery.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 93 — `C` (Monitor and optimize GitHub usage)

Correct answer: C (is correct). Query the **Copilot User Management / Seat Assignments API** (`/orgs/{org}/copilot/billing/seats` -> `last_activity_at` & `last_activity_editor`) alongside the **Copilot Metrics API** / Usage dashboard! [Skill 5.3: Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Evaluating enterprise adoption, Copilot/Actions metrics, and dormant or underutilized features (https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Correct. Tracking `last_activity_at` per Copilot seat lets enterprise admins automatically reclaim unused seats after a defined inactivity window (e.g., 30–60 days).
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 94 — `B` (Monitor and optimize GitHub usage)

Correct answer: B (is correct). By default, GHES classifies any user account with zero web, Git, API, or SSH activity for **`90` days** (configurable in Management Console / Site Admin) as **Dormant**. [Skill 5.3: Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Evaluating enterprise adoption, Copilot/Actions metrics, and dormant or underutilized features (https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Correct. Comparing assigned seats against 7/28/90-day active usage across Copilot, GHAS Security Overview, and Actions workflows highlights teams needing enablement or license reclamation.
- **C:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **D:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.

### Question 95 — `C` (Monitor and optimize GitHub usage)

Correct answer: C (is correct). **Actions Usage Metrics** and **Actions Performance Metrics** (`Insights -> Actions Usage Metrics` / `Performance Metrics`) reveal top compute consumers, failing workflows, and runner queue bottlenecks. [Skill 5.3: Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Evaluating enterprise adoption, Copilot/Actions metrics, and dormant or underutilized features (https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Correct. Comparing assigned seats against 7/28/90-day active usage across Copilot, GHAS Security Overview, and Actions workflows highlights teams needing enablement or license reclamation.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 96 — `A, D` (Monitor and optimize GitHub usage)

Correct answers: A and D (are correct). Audit **dormant seats, pending invitations, and 90-day GHAS committers**, and map organizations/repos to **Cost Centers** with **75/90/100% Budgets**, `actions/cache`, short artifact retention, and Linux runner defaults. [Skill 5.4: Interpret usage reports for metered products | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Interpreting metered usage reports, spending limits, and cost centers for Actions, Packages, GHAS & Copilot (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-billing/using-the-billing-platform)]

- **A:** Correct. Cost Centers and Budgets enforce FinOps accountability while caching, shorter artifact retention, and right-sized OS runners cut metered overages.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. Proactive seat hygiene reclaims idle Enterprise, Copilot, and GHAS licenses before renewal or monthly metered billing cycles.
- **E:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 97 — `B` (Monitor and optimize GitHub usage)

Correct answer: B (is correct). Exactly **`18`** GHAS licenses—GHAS bills strictly per **unique active committer** over the rolling **90-day** window on enabled private/internal repositories (`Read`/`Triage` viewers consume `0` GHAS seats)! [Skill 5.4: Interpret usage reports for metered products | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Interpreting metered usage reports, spending limits, and cost centers for Actions, Packages, GHAS & Copilot (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-billing/using-the-billing-platform)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Correct. If an engineer pushes to 15 GHAS-enabled private repos across 4 orgs in the same enterprise, deduplicated enterprise billing counts only **1** GHAS committer license.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 98 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). Standard hosted runner billing applies OS per-minute multipliers/rates where **Linux** is cheapest (`1x`), **Windows** is `2x`, and **macOS** is **`10x`** (`so 10 minutes on macOS consumes the equivalent of 100 Linux minutes`)! [Skill 5.4: Interpret usage reports for metered products | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Interpreting metered usage reports, spending limits, and cost centers for Actions, Packages, GHAS & Copilot (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-billing/using-the-billing-platform)]

- **A:** Correct. Metered billing tracks included enterprise quotas first (for standard hosted runners and Packages/Artifacts storage) and bills overages or Larger runners/Copilot/GHAS against assigned Cost Centers and Budgets.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 99 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). Export consumed-licenses and verify GitHub Connect GHES deduplication, audit dormant users/duplicate emails/90-day GHAS committers, reclaim idle seats and right-size budgets, and enforce automated SCIM offboarding + cost alerts. [Skill 5.5: Recommend strategies for license and resource optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending strategies for dormant seat reclamation, caching, and runner/storage cost optimization (https://docs.github.com/en/enterprise-server@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/managing-dormant-users)]

- **A:** Correct. Correct optimization loop: inspect unified license data, pinpoint duplicate identities/dormant users/GHAS committers, reclaim unused seats and cap metered budgets, and automate SCIM hygiene.
- **B:** Incorrect. Admins remove/suspend org or EMU memberships (preserving PR/commit audit trails) rather than deleting security controls.
- **C:** Incorrect. macOS hosted runners carry a higher per-minute cost than Linux runners, long artifact retention inflates storage charges, and unmonitored seat grants waste licenses.
- **D:** Incorrect. GHAS seats release automatically 90 days after a user’s last push (or when GHAS is disabled on the repo), and disabling GitHub Connect causes double-billing across GHEC and GHES.

### Question 100 — `C` (Monitor and optimize GitHub usage)

Correct answer: C (is correct). No — suspending a GHES user or deprovisioning/removing a GHEC user **immediately frees their Enterprise license seat** while **100% preserving** all historical commits, Issues, and Pull Request review audit trails! [Skill 5.5: Recommend strategies for license and resource optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending strategies for dormant seat reclamation, caching, and runner/storage cost optimization (https://docs.github.com/en/enterprise-server@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/managing-dormant-users)]

- **A:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **B:** Incorrect. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.
- **C:** Correct. Offboarding or suspending inactive accounts reclaims per-user licenses cleanly without breaking repository Git history or compliance review logs.
- **D:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — suspending a GHES user or deprovisioning/removing a GHEC user **immediately frees their Enterprise license seat** while **100% preserving** all historical commits, Issues, and Pull Request review audit trails!
