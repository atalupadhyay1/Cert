# Microsoft / GitHub Exam GH-100: GitHub Enterprise Administrator — Full-Length Mock Exam 4

**Theme:** Enterprise GitHub Actions & Private Runner Networking — Internal Reusable Workflows, SHA Pinning, Larger Runners, Azure VNet & OIDC Vaults  
**Credential:** `GitHub Administration` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `July 2026 (Last updated May 5, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-100 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Enterprise documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Manage GitHub identities and access (15–20% official weight · 19 questions)

### 1. A freight rail operator (`StratusRail`) provisions **GHEC with EMUs** (`shortcode: srail`) and brings in external rolling-stock IoT vendors who must collaborate on two gateway repositories without seeing 300 `Internal` rail-dispatch repos. Which two controls satisfy this? Select two.

- **A.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **B.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **C.** Provision user accounts exclusively via your corporate IdP (`SAML`/`OIDC` + `SCIM`), blocking personal public repos, Gists, and external OSS contributions
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **E.** Assign external contractors the IdP **Guest Collaborator** role so they cannot browse `Internal` enterprise repositories unless explicitly granted access

### 2. When setting up a brand-new **GHEC EMU** enterprise, what is the role of the single initial **`<shortcode>_admin`** setup user (`e.g., srail_admin`), and should human engineers use `<shortcode>_admin` for daily Git pushes?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Enterprise Managed Users (`EMUs`) provisioned by your corporate IdP (`<handle>_<shortcode>`), isolated from public repo creation, Gists, and external OSS pushes
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 3. An Enterprise Owner rotates the expiring **X.509 SAML signing certificate** in Okta for `StratusRail`. In what order should they update the certificate between Okta and `Enterprise Settings -> ____` to avoid locking out 1,500 developers?

- **A.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **B.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Enterprise/Organization SAML 2.0 SSO paired with mandatory GitHub `2FA` (with SAML recovery codes stored safely and PAT/SSH credential authorization enforced)

### 4. On personal-account GHEC, if an Organization Member's corporate SAML session expires (`default 24 hours or IdP-configured SessionNotOnOrAfter`), what happens the next time they open a private `@stratusrail` Pull Request in their browser?

- **A.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Enterprise/Organization SAML 2.0 SSO paired with mandatory GitHub `2FA` (with SAML recovery codes stored safely and PAT/SSH credential authorization enforced)
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 5. An IAM architect uses **Enterprise teams** in `StratusRail`'s EMU tenant to provision a central `Rail-SRE` cohort across 16 regional organizations with Copilot Business and custom enterprise read-audit permissions. Which four-step sequence applies?

- **A.** Assign CODEOWNERS to an Enterprise team first → nest three child Enterprise teams underneath it → mark the Enterprise team Secret → add a Team maintainer
- **B.** Create an Enterprise team under People → remove manual members & link an EMU IdP group (<=5,000 users) → grant org memberships, Copilot seats, or custom enterprise roles → reference @org/ent:slug or ruleset bypass
- **C.** Add 20 manual members to the Enterprise team → simultaneously attach an IdP group while keeping manual members → add 8,000 IdP users → list @/ent:slug in CODEOWNERS
- **D.** Create an Organization team in one org → expect it to grant Enterprise Audit Log roles across 50 orgs → sync via SCIM without an IdP → bypass Enterprise Owner policies

### 6. In an **EMU** enterprise, can an Organization Owner manually invite a personal `gmail.com` GitHub user or manually edit membership of an **IdP-synced Organization team** inside the GitHub Web UI?

- **A.** SCIM provisions/deprovisions user accounts across EMUs (or org invitations), whereas IdP Team Sync on personal-account GHEC (`Entra ID`/`Okta`) only updates org-team membership for existing org members
- **B.** Sync a single 12,000-member Entra ID group into one Enterprise team alongside 15 manually added contractor accounts
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 7. When `StratusRail` configures **Entra ID OIDC** for its **GHEC EMU** enterprise and enables **IP address validation for Conditional Access (`CAP`)**, what happens if an engineer steals a valid PAT from a corporate laptop and replays that PAT from an untrusted home ISP?

- **A.** OIDC SSO for Enterprise Managed Users with **Microsoft Entra ID**, automatically enforcing Entra **Conditional Access Policies (`CAP`)** including IP and device compliance
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 8. Compare **SAML 2.0** vs **OIDC** support on **GitHub Enterprise Cloud** today: does **personal-account GHEC** (non-EMU) support **OIDC** user SSO, or which protocol is required for personal-account GHEC SSO?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Supported IdPs (`Microsoft Entra ID`, `Okta`, `PingFederate` with paved-path OIDC/SAML+SCIM for EMUs; or `LDAP`/`CAS`/`SAML` on self-hosted `GHES`)

### 9. A subsidiary running personal-account GHEC enables SAML SSO across 90 repositories. Which two steps protect administrative continuity and CLI Git workflows? Select two.

- **A.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **B.** Download and vault **Enterprise/Org SAML recovery codes** before enforcing SAML SSO so Owners can recover access during an IdP outage
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **E.** Require developers on personal-account GHEC to **authorize** approved Fine-grained/classic PATs and SSH keys for SAML SSO before accessing org repositories

### 10. A developer runs `ssh -T git@github.com` and receives `"Hi dev-alex! You've successfully authenticated, but GitHub does not provide shell access"`, yet `git clone git@github.com:stratusrail/dispatch.git` returns `ERROR: The 'stratusrail' organization has enabled or enforced SAML SSO`. What does this prove?

- **A.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **B.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **C.** Authentication verifies *who* the caller is (`SAML`/`OIDC`, `2FA`, Passkey, SSH key, PAT), while authorization governs *what* resources they may access (roles, teams, scopes, SAML SSO token authorization)
- **D.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step

### 11. Inside `@stratusrail-freight`, release coordinators need permission to **edit repository Custom Property values** and **view organization Ruleset insights** without holding `Organization Owner`. Which feature (`Organization Settings -> Organization roles -> ____`) grants exact org-level delegation?

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** 5 built-in repository roles (`Read`, `Triage`, `Write`, `Maintain`, `Admin`), built-in org roles (`Owner`, `Member`, `Moderator`, `Billing manager`, `Security Manager`), plus GHEC **Custom repository/org roles**

### 12. When creating a **Custom repository role** on GitHub Enterprise Cloud, must you pick one of the built-in roles (`Read`, `Triage`, `Write`, or `Maintain`) as its **inherited base role** (`and can you remove permissions from the chosen base role`)?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **D.** 5 built-in repository roles (`Read`, `Triage`, `Write`, `Maintain`, `Admin`), built-in org roles (`Owner`, `Member`, `Moderator`, `Billing manager`, `Security Manager`), plus GHEC **Custom repository/org roles**

### 13. Which three governance rules apply when scaling **Enterprise teams** and Organization permissions across `StratusRail`'s 16 organizations? Select three.

- **A.** Sync a single 12,000-member Entra ID group into one Enterprise team alongside 15 manually added contractor accounts
- **B.** Set Organization **`Base permissions = None`** and grant repository access strictly through IdP-synced Teams and least-privilege Custom Repository Roles
- **C.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **D.** Add **Enterprise teams** across up to 1,000 organizations where org admins can grant additional repo access without removing enterprise-granted permissions
- **E.** Grant **Copilot Business** seats, **custom/predefined enterprise roles**, and **Repository Ruleset bypass** rights directly to **Enterprise teams** (`@/ent:<slug>`)
- **F.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 14. An Organization Owner inside `@stratusrail-east` wants to remove 5 members from `@stratusrail-east` who were granted organization membership via an **Enterprise team** (`@/ent:rail-sre`). Proposed solution: Have the `@stratusrail-east` Organization Owner delete those 5 users directly inside Organization Settings while the Enterprise team grant remains active. Can an Organization Owner override membership granted by an Enterprise team?

- **A.** No — **Enterprise teams** (`@/ent:<slug>`) currently do **not** support `CODEOWNERS` assignment, nested child teams, Secret visibility, or Team maintainers; use an **Organization team** for `CODEOWNERS`
- **B.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **C.** No — on GHEC with personal accounts, IdP **Team Synchronization** only updates Organization team membership for existing org members and **cannot** invite or provision brand-new users into the organization
- **D.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement

### 15. Inside an **Organization team** hierarchy (unlike flat Enterprise teams), `@stratusrail/backend` is the **parent team** of child team `@stratusrail/backend-payments`. If `@stratusrail/backend` is granted `Write` on `rail-billing`, what access does child team `@stratusrail/backend-payments` inherit?

- **A.** **Enterprise teams** (`@/ent:<slug>`, up to 5,000 EMU IdP-synced users across up to 1,000 orgs) for centralized org membership, Copilot seats, custom enterprise roles, and ruleset bypass
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **D.** Sync a single 12,000-member Entra ID group into one Enterprise team alongside 15 manually added contractor accounts

### 16. An external SOX auditor asks for proof of **who approved** a temporary emergency bypass of a protected `main` branch Ruleset on `stratusrail/dispatch-api` last Tuesday. Where is every Ruleset pass, block, and bypass logged with actor + timestamp?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Exporting enterprise/organization membership & repository permission inventories plus auditing `org.*`, `team.*`, `repo.*`, and token metadata (`hashed_token`, `programmatic_access_type`) in the Audit Log
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 17. To audit every SSH public key, GPG commit-signing key, and SAML `externalIdentity` linked to users across an Enterprise via **GraphQL**, which top-level GraphQL connection (`enterprise(slug: "stratusrail") { ownerInfo { ____ { edges { node { guid samlIdentity { nameId } user { login } } } } } }`) enumerates linked identities?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Exporting enterprise/organization membership & repository permission inventories plus auditing `org.*`, `team.*`, `repo.*`, and token metadata (`hashed_token`, `programmatic_access_type`) in the Audit Log
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls

### 18. Compare **legacy Branch Protection Rules** against modern **Repository Rulesets** on GitHub Enterprise Cloud. Name two major enterprise capabilities that **Repository Rulesets** support which legacy Branch Protection Rules lack!

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Repository **Custom Properties** (e.g., `compliance_tier=pci`, `data_class=restricted`) targeted dynamically by Organization/Enterprise **Repository Rulesets** (`most restrictive wins`)

### 19. Inside a **Repository Ruleset**, what does enabling **`Require status checks to pass`** with a pinned **expected integration source (`GitHub Actions` vs `any source`)** prevent?

- **A.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **B.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **C.** Enterprise **Member privileges** (`Base permissions = None`, repo creation/forking/visibility locks) combined with **Organization/Enterprise Repository Rulesets** (`Active` vs `Evaluate` dry-run mode)
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

---

## Domain 2 — Administer GitHub Enterprise environment (10–15% official weight · 14 questions)

### 20. An organization hits a hard internal object/pack corruption error (`remote: fatal: packfile ... is corrupted`) on a cloud **GHEC** repository despite clean local clones. Who resolves server-side Git storage pack corruption on `github.com`?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Enterprise Admins resolve IdP/SAML lockouts, RBAC grants, runner sizing, and webhook configs; **GitHub Enterprise Support** handles platform outages, cached PR commit purges, and repo restore escalations
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 21. A squad lead asks **GitHub Support** to design their custom `CODEOWNERS` hierarchy and write bespoke `.github/workflows/deploy-rail.yml` YAML scripts for their proprietary locomotive ERP. Is writing custom pipeline code covered by standard GitHub Support?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Enterprise Admins resolve IdP/SAML lockouts, RBAC grants, runner sizing, and webhook configs; **GitHub Enterprise Support** handles platform outages, cached PR commit purges, and repo restore escalations

### 22. A rail-yard **GHES** cluster node logs MySQL replication lag alerts after a SAN latency spike. Which four-step diagnostic escalation sequence applies?

- **A.** Post raw /data/user/common/secrets.conf in a public GitHub Discussion → tag @github → upgrade three major GHES versions mid-outage → skip support bundle generation
- **B.** Confirm admin-side checks & note exact incident UTC timestamps → SSH/console in and run ghe-support-bundle -x (or Management Console) → review/sanitize sensitive log data if required → upload bundle to GitHub Enterprise Support portal
- **C.** File a GitHub Support ticket asking GitHub to reset a developer corporate Active Directory password → wait 48 hours → run git gc locally → close ticket
- **D.** Restart all GHES services with ghe-config-apply --force → wipe /data/user/logs to save disk → open a ticket with no timestamps or bundle → grant Support SSH access to internal VPC

### 23. Which two administrative preparations cut Mean Time to Resolution (`MTTR`) when opening Severity 1 tickets with **GitHub Enterprise Support**? Select two.

- **A.** Generate an extended diagnostic archive via `ghe-support-bundle -x` (or Management Console `:8443`) and upload it to the **GitHub Enterprise Support** portal
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Designate up to 20–25 entitled **Support** members (or `Enterprise Support` custom role holders) authorized to open and manage enterprise support tickets
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **E.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

### 24. If `@stratusrail` creates `.github/PULL_REQUEST_TEMPLATE.md` inside its organization-wide **`.github`** repository, what happens in `stratusrail/locomotive-os` if that specific repo **already** has its own local `.github/PULL_REQUEST_TEMPLATE.md`?

- **A.** Publishing reusable **Starter Workflows** inside the organization’s `.github` repository (`workflow-templates/*.yml` + `.properties.json`) to standardize onboarding CI pipelines
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 25. To guide internal developers on how to report security bugs privately across all 140 repositories in `@stratusrail` without committing 140 copies of `SECURITY.md`, where should AppSec commit a single `SECURITY.md` policy?

- **A.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **B.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **C.** Standardizing **Template repositories**, organization-wide `.github` community health defaults, **`Internal`** InnerSource discovery, and ADR/Issue Form intake across teams
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 26. When configuring **GitHub Merge Queue** on `stratusrail/dispatch-monorepo`, your CI workflow currently triggers **only** on `on: [push, pull_request]`, causing queued PRs to sit forever waiting for required checks! Which workflow trigger event (`on: ____`) MUST you add to your CI `.yml`?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Enforcing trunk-based **GitHub Flow**, protected `main` with **`CODEOWNERS`**, **Merge Queue** (`gh-readonly-queue`) for busy monorepos, linear squash merges, and immutable signed SemVer **Releases**
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO

### 27. To keep `main` history clean, bisectable, and free of tangled merge commits across 90 repositories, which Pull Request merge method (`Settings -> General -> Pull Requests -> Allow ____ merging` only) + Ruleset rule (`Require linear history`) should admins standardize?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Enforcing trunk-based **GitHub Flow**, protected `main` with **`CODEOWNERS`**, **Merge Queue** (`gh-readonly-queue`) for busy monorepos, linear squash merges, and immutable signed SemVer **Releases**
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 28. Compare enterprise deployment architectures when `StratusRail` acquires a Canadian rail operator requiring data residency and an isolated depot running **GHES**. Which two statements are accurate? Select two.

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Enable **GitHub Connect** license synchronization between `GHES` and `GHEC` (plus link **Visual Studio Subscriptions**) so hybrid users consume a single Enterprise seat
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Deploy **GHEC with Data Residency (`<enterprise>.ghe.com`) + EMUs** when regulations require pinning cloud source code and metadata in a specific geographic region (`EU`, `US`, `AU`, `JP`)
- **E.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 29. When >10,000 developers + heavy monorepo CI bots saturate the vertical CPU/RAM/IOPS ceiling of a **single** self-hosted **GHES** VM (`even with High Availability`), which horizontal multi-node GHES architecture (`GHES ____`) scales Git, web, and database tiers across nodes?

- **A.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Comparing the 4 Enterprise models: **GHEC + personal accounts**, **GHEC + EMU**, **GHEC with Data Residency (`<ent>.ghe.com`) + EMU**, and self-hosted **GitHub Enterprise Server (`GHES`)**
- **D.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

### 30. Does enabling **Secret scanning**, **CodeQL**, and **Dependabot** on a **Public** open-source repository inside a GitHub Enterprise Cloud organization consume any paid **GitHub Advanced Security (`GHAS`)** committer seats?

- **A.** Per-user **GitHub Enterprise** seat licensing (deduplicating unique users across orgs + synced `GHES` via **GitHub Connect**, plus linked **Visual Studio Enterprise/Pro with GitHub Enterprise** benefits) alongside metered add-ons
- **B.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 31. Which payment models does **GitHub Enterprise** support for enterprise procurement (`credit card / PayPal self-serve vs ____ / Azure Subscription ID metered linkage`)?

- **A.** Per-user **GitHub Enterprise** seat licensing (deduplicating unique users across orgs + synced `GHES` via **GitHub Connect**, plus linked **Visual Studio Enterprise/Pro with GitHub Enterprise** benefits) alongside metered add-ons
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges

### 32. On a personal-account **GHEC** enterprise where user `alex-personal` belongs to `Org-1` (`verified email alex@stratusrail.com`) and also created a second personal handle `alex-rail` in `Org-2` (`verified email alex.ops@gmail.com`), how many Enterprise seats do those two accounts consume?

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Inspecting `Enterprise -> Billing & Licensing -> Licensing` (and exported `consumed-licenses` JSON/CSV) to track assigned seats, pending invitations, outside collaborators, VS subscriptions, and `GHES` sync files
- **D.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

### 33. Where inside `Enterprise -> Billing & Licensing` can an admin verify the exact count of **Visual Studio Enterprise / Professional** linked subscribers (`both assigned/claimed and unclaimed`) alongside regular GitHub Enterprise seats?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Inspecting `Enterprise -> Billing & Licensing -> Licensing` (and exported `consumed-licenses` JSON/CSV) to track assigned seats, pending invitations, outside collaborators, VS subscriptions, and `GHES` sync files
- **D.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls

---

## Domain 3 — Implement secure software development and compliance (25–30% official weight · 29 questions)

### 34. `StratusRail`'s CISO mandates locking `Secret Protection` and `Dependabot` on all 16 organizations using a centralized **Enterprise Security Configuration**. Which four-step rollout order applies?

- **A.** Enable Enforce configuration with every setting left as Not set → expect Not set fields to lock repository admins → delete Organization Security Managers → skip default policy
- **B.** Apply a GHAS Security Configuration with 0 available licenses → assume transferred repos inherit new-repo defaults automatically → disable GitHub Actions on CodeQL repos → leave unenforced
- **C.** Ask 400 repository admins to toggle checkboxes manually in every repo → disable Dependency graph → turn off push protection → audit annually by spreadsheet
- **D.** Verify available GHAS / Secret Protection / Code Security committers → create custom Security Configuration at Enterprise/Org level → attach to existing & transferred repos plus default for new repos → set policy to Enforce configuration

### 35. Which two enterprise controls ensure newly created microservices automatically run SAST, SCA, and PR dependency gates without manual setup by developers? Select two.

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Create and **Enforce** an Enterprise/Organization **Security Configuration** (setting it as default for newly created repos and manually attaching transferred repos)
- **D.** Enable **CodeQL default/advanced setup**, **Dependabot security updates**, and the **Dependency Review Action** inside required Pull Request Rulesets
- **E.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 36. Besides custom Security Configurations, GitHub provides a built-in **`GitHub-recommended`** Security Configuration preset. If your enterprise needs `Private vulnerability reporting` disabled on `Internal` repos while enabling `Push protection` everywhere, what should you do?

- **A.** Enforcing **Enterprise Policies** (`Enforced` vs `No policy` delegated to orgs) and **Custom Security Configurations** (`GitHub Secret Protection` + `GitHub Code Security` / `GHAS`) across organizations
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 37. To prevent compromised developer tokens from sneaking malicious CI changes into `.github/workflows/*` without security review, which **Repository Ruleset Push rule** (`Restrict ____`) blocks pushes touching `.github/workflows/**/*` from non-bypassed roles?

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Configuring **Push Rulesets** to block oversized binaries, forbidden file extensions (`.pem`, `.pfx`, `.key`), restricted file paths (`.github/workflows/**`), and path-traversal commits pre-receive

### 38. Can the **exact same SSH public key** be registered as a **Deploy key** on **two different repositories** (`stratusrail/gateway-a` and `stratusrail/gateway-b`)?

- **A.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **B.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 39. Under `Enterprise -> Policies -> Repository management`, why do regulated enterprises disable **`Allow members to delete or transfer repositories`** across member organizations?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Hardening access with **Organization/Enterprise IP allow lists**, **SSH Certificate Authorities (`SSH CAs`)** issuing short-lived developer SSH certs, and least-privilege repo-scoped **Deploy keys**

### 40. Rail safety regulators require streaming `StratusRail`'s Enterprise Audit Logs (including Git read/write transport events) into Google Cloud Storage (`Bucket Lock`) + Chronicle/SIEM. Which four-step sequence applies?

- **A.** Stream audit logs from a single repository Settings tab → expect enterprise-wide SAML and billing events to appear → disable SAML SSO → delete historical SIEM buckets
- **B.** Rely solely on the 180-day web UI audit search for 7-year regulatory retention → skip log streaming → poll REST API every 50 ms until rate-limited → store logs in a public Gist
- **C.** Provision encrypted SIEM/storage sink (Event Hubs, Blob, S3, Splunk) → configure credentials in Enterprise Audit Log Streaming → verify test event & optional Git toggle → set SIEM retention & alerts
- **D.** Enable Git read/clone event streaming to a public unauthenticated HTTP webhook → skip test verification → grant all Organization Members Enterprise Owner to view logs

### 41. When rotating the SAS token, AWS IAM key, or Splunk HEC token used by **Enterprise Audit Log Streaming**, does editing the streaming sink credentials inside `Enterprise Settings -> Audit log -> Log streaming` erase previously streamed historical archives?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Streaming the **Enterprise Audit Log** (including optional `git.clone`/`git.fetch`/`git.push` events) in real time to **Azure Event Hubs / Blob Storage, AWS S3, Splunk, Datadog, or GCS**, plus REST/GraphQL queries
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 42. Inside **Enterprise Security Overview**, which sub-view (`Security Overview -> ____ -> Secret scanning -> Push protection metrics`) shows how many secrets Push Protection **blocked before push** vs how many times developers bypassed push protection and why?

- **A.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **B.** Using **Enterprise/Organization Security Overview** (`Risk` and `Coverage` dashboards) to audit GHAS enablement gaps, open critical `CodeQL`/Secret/Dependabot alerts, and remediation MTTR
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 43. Which three AppSec controls protect `StratusRail` locomotive signaling repositories across commits and Pull Requests? Select three.

- **A.** Enable **CodeQL default/advanced setup**, **Dependabot security updates**, and the **Dependency Review Action** inside required Pull Request Rulesets
- **B.** Enable **Secret Scanning Push Protection**, **Partner Validity Checks**, custom regex patterns, and **Delegated Bypass** reviewer groups
- **C.** Create and **Enforce** an Enterprise/Organization **Security Configuration** (setting it as default for newly created repos and manually attaching transferred repos)
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **E.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **F.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 44. When **CodeQL Pull Request alerts** detect a brand-new `High`-severity SQL injection introduced in a PR diff, what automated remediation capability (`____ Autofix`) generates an explainable code patch right inside the Pull Request review comment?

- **A.** Enabling **CodeQL code scanning** (`Default setup` or custom `Advanced setup` SARIF workflows) plus **Secret scanning** with **Push protection**, **Validity checks**, custom regex patterns, and delegated bypass review
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 45. Up to how many **Custom Secret Scanning Patterns** can an Enterprise/Organization define (`up to ____ custom patterns at the enterprise/org level`), and can you attach pre/post match `Before`/`After` context regexes plus `Must not match` exclusion rules?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Defining **Custom Secret Scanning Patterns** (with before/after context expressions and dry-run historical backtesting) at the Organization or Enterprise level to catch internal proprietary token formats

### 46. In `.github/dependabot.yml`, developer teams complain that Dependabot opens 35 separate PRs every Monday morning for `@babel/*` and `@types/*` patch bumps. Which `dependabot.yml` configuration key (`____:`) bundles related dependency bumps into **one single Pull Request**?

- **A.** Configuring **Dependency graph**, **Dependabot alerts**, **Dependabot security & version updates** (`dependabot.yml` + private registry access), **Dependency Review Action** on PRs, and **Repository Security Advisories**
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 47. When triaging 80 Dependabot alerts in a large Java repository, how do **`Auto-triage rules`** (`Dependabot alert rules`) help AppSec teams focus on real production risk?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Configuring **Dependency graph**, **Dependabot alerts**, **Dependabot security & version updates** (`dependabot.yml` + private registry access), **Dependency Review Action** on PRs, and **Repository Security Advisories**

### 48. If an organization restricts public internet access on self-hosted runners used by Dependabot, how does Dependabot authenticate to an internal Azure Artifacts NuGet feed without hardcoding passwords inside `.github/dependabot.yml`?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Configuring **Dependabot** with encrypted `dependabot` private-registry secrets (`Settings -> Code security -> Global settings`) and running updates on **Actions runners / ARC** when private VNet access is required

### 49. A locomotive telemetry developer accidentally pushes an MQTT broker TLS private key (`broker.pem`) to `main` and two release tags on **GHEC**. Which four-step incident response sequence applies?

- **A.** Contact GitHub Support first to rotate your AWS IAM key → wait before revoking in AWS → delete the entire GitHub Organization → recreate repos from developer zip files
- **B.** Archive the repository to hide the leaked key → rotate the key next quarter → use deprecated git filter-branch without force-pushing → tell devs to git pull --merge old history back
- **C.** Run git rm secrets.env in a new commit and push → assume historical commits are erased → keep the production API key active → skip GitHub Support cache purge
- **D.** Revoke & rotate the exposed secret at the provider → scrub all branches/tags via git filter-repo → force-push cleaned refs & have devs re-clone → send commit SHAs to GitHub Support to purge cached views

### 50. Which two principles govern every credential-exposure incident on GitHub Enterprise? Select two.

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Immediately **revoke and rotate** leaked credentials at the target cloud/API provider before assuming Git history rewrites reduce exposure
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **E.** Scrub sensitive blobs across all refs with **`git filter-repo`**, force-push cleaned branches/tags, and send commit SHAs to **GitHub Support** to purge cached PR views

### 51. After force-pushing a `git filter-repo`-cleaned `main` branch, one team member who still had an old local clone runs `git pull` (creating a merge commit) and pushes back to `origin/main`! Proposed solution: Allow developers to run normal `git pull` on stale pre-purge clones instead of fresh `git clone` / `git rebase` cleanup. What happens if they push that merge?

- **A.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **B.** No — committing `git rm` (or archiving the repo) leaves the leaked secret intact in prior Git commits and cached PR diffs; you must **revoke/rotate the secret immediately**, run **`git filter-repo`**, force-push, and contact GitHub Support
- **C.** No — an organization’s default **Security Configuration** auto-attaches only to **newly created** repositories; repositories **transferred** into the organization must have the Security Configuration attached manually or via API
- **D.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret

### 52. Which two token-security standards minimize blast radius across `StratusRail`'s 16 organizations? Select two.

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **C.** Block or restrict **classic PATs** enterprise-wide while requiring **Organization Owner approval** and max expiration lifetimes (`<=30–90 days`) on **Fine-grained PATs**
- **D.** Migrate org automation from personal PATs (`5,000 req/hr`) to **GHEC GitHub App installation tokens** (`15,000 REST req/hr`, 1-hour expiry, zero seat cost)
- **E.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 53. Can a **Fine-grained Personal Access Token** ever grant `Enterprise Owner` administration or cross-organization blanket `write` access across **multiple** distinct organizations simultaneously?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** Enforcing **Enterprise Fine-Grained PAT Policies**: restricting or blocking **PATs (classic)**, requiring mandatory expiration lifetimes (e.g., <=30–90 days), requiring **Admin approval** before Fine-grained PATs activate, and revoking tokens

### 54. When an Enterprise Owner configures `Require approval of fine-grained personal access tokens` **except** for an exempt automation role or decides to auto-approve read-only repo metadata tokens, where are pending Fine-grained PAT requests reviewed?

- **A.** Enforcing **Enterprise Fine-Grained PAT Policies**: restricting or blocking **PATs (classic)**, requiring mandatory expiration lifetimes (e.g., <=30–90 days), requiring **Admin approval** before Fine-grained PATs activate, and revoking tokens
- **B.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 55. A build pipeline running inside GitHub Actions on a **GHEC** repository replaces `${{ secrets.GITHUB_TOKEN }}` (`15,000 req/hr per repo`) with a developer's personal **Fine-grained PAT** (`5,000 req/hr shared across all that user's scripts`) thinking a personal PAT has higher rate limits. Proposed solution: Replace `GITHUB_TOKEN` with a personal PAT to raise REST rate limits on GHEC. Does this raise the rate limit?

- **A.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **B.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **C.** No — on GHEC with personal accounts, IdP **Team Synchronization** only updates Organization team membership for existing org members and **cannot** invite or provision brand-new users into the organization
- **D.** No — **Enterprise teams** (`@/ent:<slug>`) currently do **not** support `CODEOWNERS` assignment, nested child teams, Secret visibility, or Team maintainers; use an **Organization team** for `CODEOWNERS`

### 56. Which HTTP response headers returned on every GitHub REST API call (`x-ratelimit-limit`, `x-ratelimit-remaining`, `x-ratelimit-used`, and `____`) tell a resilient client exact UTC epoch seconds when its primary quota window resets?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** REST rate limits: **`5,000 req/hr`** per personal PAT user vs **`15,000 req/hr`** for a **GitHub App installation** (and `GITHUB_TOKEN` per repo) on **GHEC** (`up to 12,500 req/hr` scaled on non-GHEC; GraphQL `5,000` vs `10,000` pts/hr)
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 57. What is the primary REST API rate limit for **unauthenticated** public API calls (`____ requests/hour per originating IP`), explaining why CI jobs downloading tool releases from `api.github.com/repos/.../releases` without `-H "Authorization: Bearer $GITHUB_TOKEN"` fail behind shared corporate NAT gateways?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **C.** REST rate limits: **`5,000 req/hr`** per personal PAT user vs **`15,000 req/hr`** for a **GitHub App installation** (and `GITHUB_TOKEN` per repo) on **GHEC** (`up to 12,500 req/hr` scaled on non-GHEC; GraphQL `5,000` vs `10,000` pts/hr)
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 58. Which two practices govern internal ChatOps bots and developer API scripting cleanly? Select two.

- **A.** Block or restrict **classic PATs** enterprise-wide while requiring **Organization Owner approval** and max expiration lifetimes (`<=30–90 days`) on **Fine-grained PATs**
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Migrate org automation from personal PATs (`5,000 req/hr`) to **GHEC GitHub App installation tokens** (`15,000 REST req/hr`, 1-hour expiry, zero seat cost)
- **E.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step

### 59. Inside a GitHub Actions workflow that needs to trigger a downstream workflow or push tags across **another** repository in `@stratusrail` (`where default GITHUB_TOKEN cannot cross repos`), which official GitHub Action (`actions/____@v1`) mints a short-lived **GitHub App installation token** cleanly?

- **A.** Signing a short-lived **RS256 JWT** (`<=10 minutes`) with the **GitHub App private key** to call `POST /app/installations/{installation_id}/access_tokens` and mint a **1-hour** installation token
- **B.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **C.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 60. Can a **GitHub App** subscribe directly to centralized **App-level Webhooks** (`receiving push/pull_request events automatically for every repository where the App is installed`) without admins manually configuring 300 individual repository webhook URLs?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** **GitHub Apps** act as independent actors scoped to selected repos + granular permissions using **1-hour installation tokens**, whereas **OAuth Apps** act as the authorizing human user with broad scopes and long-lived tokens
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges

### 61. When an Organization Owner transfers ownership of an internal **GitHub App** registration from a departing developer's personal account (`@dev-sam`) to the `@stratusrail` **Organization**, do existing installations or the App ID break?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Enabling **OAuth App access restrictions** and **GitHub App installation approval workflows** so developer-requested integrations stay blocked on private org data until vetted and approved by an Organization/Enterprise Owner
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 62. If an already-installed **GitHub App** updates its registration to request a **new elevated permission** (`e.g., adding Secrets: Read & write`), does that new permission activate silently on `@stratusrail`?

- **A.** Enabling **OAuth App access restrictions** and **GitHub App installation approval workflows** so developer-requested integrations stay blocked on private org data until vetted and approved by an Organization/Enterprise Owner
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls

---

## Domain 4 — Manage GitHub Actions (20–25% official weight · 24 questions)

### 63. `StratusRail`'s platform guild maintains reusable Terraform, Helm, and container-signing workflows for 16 organizations. Which two practices establish secure enterprise reuse? Select two.

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Host reusable workflows (`workflow_call`) and composite actions in **`Internal`** enterprise repositories with cross-organization workflow `Access` enabled
- **E.** Enforce **`Require actions to be pinned to a full-length commit SHA`**, restrict allowed actions to verified/internal sources, and default `GITHUB_TOKEN` to **`Read-only`**

### 64. When a caller workflow in `stratusrail-west/track-sensor` invokes a **Reusable Workflow** stored in `stratusrail-shared/workflows/.github/workflows/build.yml@<sha>`, under **whose repository context** (`GITHUB_REPOSITORY`, `GITHUB_TOKEN`, runner group access, and secrets) does the reusable workflow execute?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Sharing reusable workflows (`on: workflow_call`) and composite actions in **`Internal`** or **`Private`** repositories with `Settings -> Actions -> General -> Access` enabled for organization/enterprise workflows
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 65. Inside a **Composite Action** (`action.yml` with `runs: using: "composite"`), every `run:` step MUST explicitly declare which required attribute (`____: bash` or `pwsh`), unlike regular workflow `run:` steps that infer a default shell?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Sharing reusable workflows (`on: workflow_call`) and composite actions in **`Internal`** or **`Private`** repositories with `Settings -> Actions -> General -> Access` enabled for organization/enterprise workflows
- **D.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO

### 66. Which two **GitHub Actions** governance controls protect `StratusRail` against supply-chain tag poisoning and unauthorized access to privileged deployment runners? Select two.

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Enforce **`Require actions to be pinned to a full-length commit SHA`**, restrict allowed actions to verified/internal sources, and default `GITHUB_TOKEN` to **`Read-only`**
- **C.** Isolate **Larger** and **ephemeral (`--ephemeral` / `ARC`) self-hosted runners** inside **Runner Groups** restricted to selected repositories and trusted reusable workflows
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **E.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 67. Beyond `on: workflow_call` reuse, which **Enterprise / Organization Repository Ruleset** feature (`Require ____ to pass before merging` — **Required Workflows**) guarantees that `stratusrail-sec/compliance/.github/workflows/sast-gate.yml` runs automatically on **every** PR across matching repos **even if** the repo lacks a `.github/workflows` folder?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Enforcing **Allowed actions and reusable workflows** (`GitHub-created`, `Verified creators`, internal patterns) plus **`Require actions to be pinned to a full-length commit SHA`**, `Read-only` default `GITHUB_TOKEN`, and fork PR approval
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 68. On self-hosted **GHES**, how does **GitHub Connect** enable air-gapped or private enterprise workflows to use official `actions/checkout`, `actions/setup-node`, and `github/codeql-action` cleanly?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Enforcing **Allowed actions and reusable workflows** (`GitHub-created`, `Verified creators`, internal patterns) plus **`Require actions to be pinned to a full-length commit SHA`**, `Read-only` default `GITHUB_TOKEN`, and fork PR approval
- **C.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **D.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges

### 69. `StratusRail` deploys critical dispatch services onto private AKS clusters using **Larger GitHub-hosted runners** and **ARC** scale sets. Which three controls complete this architecture? Select three.

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Connect **Linux/Windows Larger GitHub-hosted runners** to an **Azure VNet** via `GitHub.Network/networkSettings` and Enterprise **Network Configurations**
- **D.** Isolate **Larger** and **ephemeral (`--ephemeral` / `ARC`) self-hosted runners** inside **Runner Groups** restricted to selected repositories and trusted reusable workflows
- **E.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **F.** Protect production deployments using **Environment Required Reviewers** + **OIDC (`id-token: write`)** federated to **HashiCorp Vault / Azure Key Vault** with strict `sub` claims

### 70. In modern **Actions Runner Controller (`ARC`)** on Kubernetes (`two Helm charts: gha-runner-scale-set-controller` and `gha-runner-scale-set`), which container mode supports running `docker build` inside ephemeral runner pods without exposing the host node's root `docker.sock`?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Organizing **Enterprise & Organization Runner Groups** restricted to selected repos and workflows, scaling **Larger GitHub-hosted runners** or ephemeral (`--ephemeral`) self-hosted runners via **Actions Runner Controller (`ARC`)** on Kubernetes

### 71. If an enterprise configures **Autoscaling Larger GitHub-hosted runners** inside a Runner Group (`setting Maximum concurrency = 40`), what happens to job #41 when 40 jobs are already executing simultaneously?

- **A.** Provisioning **ephemeral self-hosted runners** (`./config.sh --ephemeral` or REST **JIT runner** configs via **Actions Runner Controller `ARC`**) that execute **exactly one job** and self-destruct cleanly
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 72. `StratusRail` connects 8-core Linux **Larger GitHub-hosted runners** to an Azure Virtual Network in `eastus2` so Terraform pipelines can reach private Azure Key Vault and AKS API endpoints (`10.40.0.0/22`). Which four-step sequence applies?

- **A.** Have an Organization Owner create a new Network Configuration while Enterprise policy blocks org configs → skip Azure resource ID linkage → assign to repository secrets → test
- **B.** Attach Azure VNet directly to free standard ubuntu-latest runners or macOS arm64 larger runners → skip GitHub.Network subnet delegation → allow all public fork PRs onto the private VNet runner group
- **C.** Delegate Azure VNet subnet to GitHub.Network & create NetworkSettings → create GitHub Network Configuration → attach it to a Linux/Windows Larger runner group → scope runner group to approved repos/workflows
- **D.** Whitelist only Microsoft Azure IP ranges on standard Linux hosted runners → skip Azure VNet configuration → disable outbound access to github.com endpoints → run workflows

### 73. When sizing an Azure VNet subnet delegated to **`GitHub.Network/networkSettings`** for a Linux Larger runner group (`max concurrency: 50`), which two networking and governance rules apply? Select two.

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Connect **Linux/Windows Larger GitHub-hosted runners** to an **Azure VNet** via `GitHub.Network/networkSettings` and Enterprise **Network Configurations**
- **D.** Isolate **Larger** and **ephemeral (`--ephemeral` / `ARC`) self-hosted runners** inside **Runner Groups** restricted to selected repositories and trusted reusable workflows
- **E.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 74. A network engineer wants to use a **Larger GitHub-hosted runner** with **static public IP ranges** (`without setting up Azure VNet`) to whitelist CI traffic on an external rail-partner SFTP server, AND asks if standard `ubuntu-latest` (`2-core` default runners) also get dedicated static IPs. Proposed solution: Enable dedicated static public IP ranges on standard free `ubuntu-latest` runners instead of Larger runners. Does GitHub provide static public IP ranges on standard `ubuntu-latest` runners?

- **A.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **B.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret
- **C.** No — **Azure Private Networking** (`VNet` integration) and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, NOT on standard free runners or `arm64` macOS Larger runners
- **D.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)

### 75. When upgrading the self-hosted runner agent binary (`actions/runner`) across 30 disconnected air-gapped Linux VMs where automatic GitHub cloud self-updates are blocked, what happens if a runner stays more than **30 days** behind a mandatory runner release?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **D.** Inspecting self-hosted runner **`_diag/Runner_*.log`** (registration, listener, network/proxy errors) and **`_diag/Worker_*.log`** (job step execution), `svc.sh status`, tool-cache disk usage, and Actions queue time metrics

### 76. A Linux self-hosted runner configured with `https_proxy=http://proxy.srail.internal:3128` inside `.env` connects to `github.com` fine, yet fails when step scripts curl an internal test service `https://dispatch-api.srail.internal` (`proxy returns 502`). Which `.env` variable fixes internal host bypass?

- **A.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **D.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges

### 77. On a Linux self-hosted runner, admins want to enforce a mandatory pre-job security script (`verifying repo authorization and clean workspace`) before **any** workflow step runs. Which runner environment hook (`____=/opt/hooks/pre-job.sh`) executes automatically on the runner host before job steps?

- **A.** Inspecting self-hosted runner **`_diag/Runner_*.log`** (registration, listener, network/proxy errors) and **`_diag/Worker_*.log`** (job step execution), `svc.sh status`, tool-cache disk usage, and Actions queue time metrics
- **B.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 78. In a **`production` Deployment Environment**, instead of restricting `Deployment branches and tags` to a single branch `main`, release engineers tag hotfixes as `v2.4.1`, `v2.4.2`. How do you allow **only** `main` and `v*` tags to unlock `production` secrets?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Scoping encrypted secrets across **Organization -> Repository -> Environment** where **most specific wins (`Environment > Repository > Organization`)**, gated by Environment **Required reviewers** and **Deployment branches/rulesets**
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 79. When a **Custom deployment protection rule** (e.g., Datadog SLO error-budget check) is enabled on the `production` Environment and the Datadog GitHub App responds with `state: "rejected"`, what happens to the paused deployment job?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Enforcing **Custom Deployment Protection Rules** (backed by a GitHub App checking ServiceNow change tickets or Datadog SLOs) alongside human Required Reviewers on `production` Environments

### 80. An admin defines `KAFKA_BROKERS` at all three levels: Organization (`org-kafka:9092`), Repository (`repo-kafka:9092`), and Environment `uat` (`uat-kafka:9092`). A workflow job runs with `environment: uat`. Proposed solution: Expect the Organization-level `KAFKA_BROKERS` (`org-kafka:9092`) to take precedence because Enterprise/Org policies sit higher in the hierarchy. Does Organization win over Environment for secrets?

- **A.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **B.** No — committing `git rm` (or archiving the repo) leaves the leaked secret intact in prior Git commits and cached PR diffs; you must **revoke/rotate the secret immediately**, run **`git filter-repo`**, force-push, and contact GitHub Support
- **C.** No — **Azure Private Networking** (`VNet` integration) and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, NOT on standard free runners or `arm64` macOS Larger runners
- **D.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret

### 81. Does **Enterprise-level** settings on GitHub Enterprise Cloud store Actions secrets directly (`Enterprise -> Secrets`), or at which three scopes are GitHub Actions secrets configured?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **D.** Configuring Organization secrets restricted to **`Selected repositories`** (or `Private and internal`), encrypting REST API secret uploads with the org/repo **LibSodium public key**, and separating non-sensitive **`vars`** from `secrets`

### 82. If a multi-line JSON Google Cloud key or PEM certificate is stored inside a single Actions secret and printed accidentally by a buggy `cat` command, could individual unmasked lines leak if not registered carefully—and what is the cleaner alternative to storing JSON keys in `secrets.*`?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Configuring Organization secrets restricted to **`Selected repositories`** (or `Private and internal`), encrypting REST API secret uploads with the org/repo **LibSodium public key**, and separating non-sensitive **`vars`** from `secrets`
- **C.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 83. In a matrix workflow (`strategy: matrix: region: [us-east, eu-west]`), where should those non-sensitive region lists or feature flags be parameterized across 40 repositories without hardcoding YAML?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Configuring Organization secrets restricted to **`Selected repositories`** (or `Private and internal`), encrypting REST API secret uploads with the org/repo **LibSodium public key**, and separating non-sensitive **`vars`** from `secrets`
- **C.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **D.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

### 84. `StratusRail` eliminates all static cloud secrets across 16 organizations by integrating **GitHub Actions OIDC** with **CyberArk / HashiCorp Vault**. Which four-step implementation sequence applies?

- **A.** Configure OIDC trust policy in Vault/Azure/AWS with strict sub/aud claims → set job permissions id-token: write → exchange OIDC JWT at runtime for dynamic secret → delete static GitHub secrets
- **B.** Trust wildcard sub: repo:* in AWS/Vault with no org filter → leave id-token: none in workflow YAML → store root Vault token in plain-text Actions vars → echo token in logs
- **C.** Request an OIDC JWT first without configuring any Federated Identity Credential in Azure/Vault → hardcode client secrets when OIDC fails → grant write-all to fork PRs
- **D.** Export static cloud admin keys into a public repository → commit .env to main → skip OIDC subject claim validation → rotate keys every 5 years

### 85. Look closely at what a GitHub Actions **OIDC `sub` claim** switches to **automatically** as soon as a job declares `environment: production` (`versus a job with no environment:`): what exact `sub` string is emitted for `stratusrail/dispatch`?

- **A.** Federating GitHub Actions (`permissions: id-token: write`) via **OpenID Connect (`OIDC`)** with **HashiCorp Vault**, **Azure Key Vault**, or **AWS Secrets Manager** using strict `sub` (`repo:`/`environment:`) and `aud` claims
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

### 86. Why is an AWS IAM OIDC condition `"StringLike": { "token.actions.githubusercontent.com:sub": "repo:stratusrail/*:*" }` dangerous on `production` AWS roles if `@stratusrail` contains experimental sandbox repos and unreviewed feature branches?

- **A.** Federating GitHub Actions (`permissions: id-token: write`) via **OpenID Connect (`OIDC`)** with **HashiCorp Vault**, **Azure Key Vault**, or **AWS Secrets Manager** using strict `sub` (`repo:`/`environment:`) and `aud` claims
- **B.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

---

## Domain 5 — Monitor and optimize GitHub usage (10–15% official weight · 14 questions)

### 87. Which two monitoring mechanisms let `StratusRail` detect compromised automation tokens and investigate historical security incidents 14 months later? Select two.

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **D.** Correlate **Organization API Insights** (`rate-limited callers, top Apps/PATs`) with **Enterprise Audit Log** queries (`hashed_token`, `action:org.*`) to isolate noisy tokens
- **E.** Configure real-time **Enterprise Audit Log Streaming** (with optional Git events) to encrypted SIEM/WORM storage (`Azure Event Hubs`, `Blob`, `S3`, `Splunk`)

### 88. Which custom organization permission (`____`) can an Organization Owner grant to a Platform Observability team so they can inspect **Organization API Insights** without receiving full `Organization Owner` privileges?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Querying the **Enterprise Audit Log** (`action:`, `actor:`, `hashed_token:`) and **Organization API Insights** (`time-series requests, rate-limited callers, top GitHub Apps, OAuth Apps, and PATs`) to pinpoint noisy/failing integrations
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 89. In an Enterprise Audit Log record, which JSON fields record the **client IP address** (`actor_ip`, when IP disclosure is enabled in org/enterprise settings) and **user-agent / programmatic token type**?

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Querying the **Enterprise Audit Log** (`action:`, `actor:`, `hashed_token:`) and **Organization API Insights** (`time-series requests, rate-limited callers, top GitHub Apps, OAuth Apps, and PATs`) to pinpoint noisy/failing integrations

### 90. Before opening a ticket with **GitHub Enterprise Support** when a single repository's GitHub Actions job fails with `Process completed with exit code 137`, what does `exit code 137` (`128 + SIGKILL 9`) indicate and who resolves it?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Using GHES **Management Console / Grafana / `ghe-diagnostics` / Activity Dashboard** (or `githubstatus.com` + Enterprise Support portal with `Support Admin` entitlement on GHEC) to separate local misconfiguration from platform incidents
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

### 91. On self-hosted **GHES** High Availability (`HA`), which CLI command (`____`) verifies real-time replication health and lag across `mysql`, `redis`, `elasticsearch`, `git`, `pages`, and `alambic` storage subsystems?

- **A.** Scraping **GHES Prometheus `/metrics`** (or forwarding `syslog` + `SNMP` health traps) to alert platform SREs proactively on disk IOPS saturation, Redis/MySQL replication lag, and CPU load
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 92. What added operational capabilities does **GitHub Engineering Direct / Premium Support** provide beyond standard **GitHub Enterprise Support** (`24x7` P1 coverage) for mission-critical enterprises?

- **A.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Using GHES **Management Console / Grafana / `ghe-diagnostics` / Activity Dashboard** (or `githubstatus.com` + Enterprise Support portal with `Support Admin` entitlement on GHEC) to separate local misconfiguration from platform incidents
- **D.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

### 93. In **Actions Performance Metrics** (`Organization / Enterprise Insights`), `Average queue time` spiked from `4 seconds` to `22 minutes` specifically on jobs targeting `runs-on: [self-hosted, linux, rail-sim]`, while `ubuntu-latest` stays at `3 seconds`. What does this metric prove?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Evaluating **Copilot Metrics API / Usage Dashboard** (active vs assigned seats, IDE/Chat/PR adoption), **Security Overview** coverage/MTTR, **Actions Usage Metrics**, and **GHES Dormant Users** reports to find underutilized features
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 94. To evaluate whether a developer enablement workshop increased **GitHub Copilot Chat** adoption and **Pull Request Summary** usage across `@stratusrail-east`, which dashboard/API tracks IDE Chat turns, dotcom Chat usage, and PR summaries over rolling 28-day windows?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Querying the **GitHub Copilot User Management & Metrics REST APIs** (`last_activity_at`, `last_activity_editor`, acceptance/chat telemetry) to automate seat reclamation for inactive assignees
- **C.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 95. On **GitHub Enterprise Cloud**, how can an admin identify **dormant/inactive organization members** (`unlike GHES's built-in /stafftools dormancy flag`) when planning seat reclamation?

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Evaluating **Copilot Metrics API / Usage Dashboard** (active vs assigned seats, IDE/Chat/PR adoption), **Security Overview** coverage/MTTR, **Actions Usage Metrics**, and **GHES Dormant Users** reports to find underutilized features
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 96. Which two FinOps controls keep `StratusRail`'s Actions, Codespaces, and GHAS bill predictable across 16 regional rail organizations? Select two.

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Assign orgs/repos to **Cost Centers** with **75/90/100% Budget alerts**, add `actions/cache`, shorten artifact `retention-days`, and move Linux workloads off `macos` runners
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **E.** Suspend/offboard **dormant users**, cancel stale pending org invitations, and audit **90-day active GHAS committers** plus **Copilot Metrics API** active-seat ratios

### 97. How are **GitHub Codespaces** metered charges broken down into **two** distinct billing components (`____` while the VM is actively running vs `____` while a stopped codespace sits un-deleted for 3 weeks)?

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Analyzing **Enhanced Billing Platform** usage exports, **Cost Centers**, **Budgets & 75/90/100% alerts**, OS runner minute multipliers (`Linux < Windows < macOS`), shared **Actions/Packages storage**, and **90-day unique GHAS committers**

### 98. When a developer's last commit on a GHAS-enabled private repository ages past **90 days** (`day 91`, with no newer commits on any GHAS repo), what happens automatically to the **GHAS committer seat** they were consuming?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Understanding that **GitHub Advanced Security (`GHAS`)** bills per **unique active committer** over a rolling **90-day** window across enabled private/internal repos (free on public repos!)
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 99. During `StratusRail`'s post-merger integration of 3 acquired rail companies, duplicate accounts and idle Codespaces inflate monthly spend. Which four-step optimization workflow applies?

- **A.** Export consumed-licenses & verify GitHub Connect GHES sync → audit dormant users, duplicate emails, and 90-day GHAS committers → reclaim idle seats & right-size budgets → enforce SCIM offboarding & alerts
- **B.** Assign every contractor Enterprise Owner and Copilot Enterprise on day one → run Linux CI jobs on 10x-multiplier macOS runners → store 500 GB build artifacts for 400 days → review bills annually
- **C.** Hard-delete departing employees personal GitHub accounts via Support → break PR review audit history → turn off Dependabot and CodeQL everywhere → cancel Enterprise support
- **D.** Delete historical employee Git commits to free GHAS seats immediately → disable GitHub Connect so GHEC+GHES users are billed twice → set unlimited Actions spending limits → skip budgets

### 100. A Linux Node.js workflow runs on `macos-latest` (`10x` cost), while HR asks if removing 12 departed contractors from `@stratusrail` will erase their historical PR comments. Proposed solution: Switch the workflow to `ubuntu-latest` AND keep paying for all 12 departed contractors' org seats assuming removal deletes PR comments. Does removing departed users delete their PR comments?

- **A.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret
- **B.** No — suspending a dormant GHES user or removing/SCIM-deprovisioning a GHEC member **frees their Enterprise license seat** while **preserving all historical commits, Issues, and Pull Request audit trails**
- **C.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **D.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement

---

## Answer Key and Explanations

### Question 1 — `C, E` (Manage GitHub identities and access)

Correct answers: C and E (are correct). IdP-provisioned **EMUs** govern full user lifecycle and forbid public repos/Gists, while the **Guest Collaborator** IdP role blocks automatic `Internal` repository access. [Skill 1.1: Describe differences between managed users and personal accounts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: About Enterprise Managed Users vs personal accounts (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users)]

- **A:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **B:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **C:** Correct. EMUs ensure corporate lifecycle control and eliminate accidental public repo or Gist leakage under managed handles.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **E:** Correct. Guest Collaborators prevent contractors in EMU enterprises from automatically reading all `Internal` repositories across member organizations.

### Question 2 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). `<shortcode>_admin` exists **solely** to bootstrap initial SAML/OIDC SSO, SCIM provisioning, and recovery codes (`it cannot belong to organizations or push code; daily admin work uses IdP-provisioned EMU accounts`)! [Skill 1.1: Describe differences between managed users and personal accounts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: About Enterprise Managed Users vs personal accounts (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Correct. EMUs give enterprises full lifecycle ownership over user accounts via SAML/OIDC + SCIM while preventing public code/Gist creation and external repository contributions.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 3 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Coordinate the certificate rollover window with your IdP (`having Enterprise SAML recovery codes in hand`), paste the new X.509 certificate + test SAML authentication **before** enforcing/removing the old certificate! [Skill 1.2: Configure and enforce SAML SSO and 2FA | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing SAML single sign-on and two-factor authentication (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise)]

- **A:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **B:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. Enforcing SAML SSO at the Enterprise level centralizes IdP authentication across all member organizations, requires credential authorization for PATs/SSH keys, and pairs with `2FA` on personal-account GHEC.

### Question 4 — `C` (Manage GitHub identities and access)

Correct answer: C (is correct). GitHub prompts a seamless **one-step SAML re-authentication** redirect against the corporate IdP before rendering private `@stratusrail` resources! [Skill 1.2: Configure and enforce SAML SSO and 2FA | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing SAML single sign-on and two-factor authentication (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise)]

- **A:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Correct. Enforcing SAML SSO at the Enterprise level centralizes IdP authentication across all member organizations, requires credential authorization for PATs/SSH keys, and pairs with `2FA` on personal-account GHEC.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 5 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). Create the Enterprise team under `People -> Enterprise teams`, ensure zero manual members and link an EMU IdP group (`<=5,000` users), assign org access/Copilot/custom enterprise roles, and reference `@org/ent:slug` or ruleset bypasses. [Skill 1.3: Understand SCIM and team synchronization: implementation and key differences | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring SCIM provisioning vs IdP team synchronization (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim/provisioning-users-and-groups-with-scim-using-the-rest-api)]

- **A:** Incorrect. Enterprise teams currently do not support CODEOWNERS, nested teams, Secret visibility, or Team maintainers.
- **B:** Correct. Correct workflow: create the Enterprise team, bind an EMU IdP group (with zero manual members and <=5,000 users), assign org/Copilot/role entitlements, and use @org/ent:slug or ruleset bypasses.
- **C:** Incorrect. Fails three platform rules: IdP-synced Enterprise teams cannot retain manual members, IdP sync pauses above 5,000 users, and Enterprise teams do not support CODEOWNERS.
- **D:** Incorrect. An Organization team is scoped to one organization and cannot hold enterprise-level administrative roles across sibling organizations.

### Question 6 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). No — on **EMUs**, all user creation flows through **SCIM** from your IdP (`manual email invitations are disabled`), and IdP-synced team memberships are controlled strictly in the IdP! [Skill 1.3: Understand SCIM and team synchronization: implementation and key differences | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring SCIM provisioning vs IdP team synchronization (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim/provisioning-users-and-groups-with-scim-using-the-rest-api)]

- **A:** Correct. SCIM manages account lifecycle (creating/suspending EMUs), while personal-account Team Sync only maps IdP groups to Organization teams and cannot invite non-members into an organization.
- **B:** Incorrect. IdP-synced Enterprise teams require zero manually added members and pause synchronization whenever the linked IdP group exceeds 5,000 users.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 7 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). GitHub evaluates the **Entra ID Conditional Access IP claim** even on **Git and REST API PAT/SSH requests**, rejecting API/Git calls originating outside the corporate CAP-approved network! [Skill 1.4: Choose and configure identity providers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Choosing and configuring Identity Providers (Entra ID, Okta, PingFederate, CAS/LDAP) (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-identity-and-access-management)]

- **A:** Correct. Configuring OIDC between Entra ID and GHEC EMUs validates Entra Conditional Access Policies during browser sign-in and token refresh Flows.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 8 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). **OIDC** SSO on GHEC is supported specifically for **Enterprise Managed Users (`EMUs`) with Microsoft Entra ID**, whereas **personal-account GHEC** uses **SAML 2.0** SSO! [Skill 1.4: Choose and configure identity providers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Choosing and configuring Identity Providers (Entra ID, Okta, PingFederate, CAS/LDAP) (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-identity-and-access-management)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. GHEC EMUs support Entra ID (OIDC or SAML), Okta, and PingFederate (plus custom SAML+SCIM API integration), while GHES adds native LDAP, Active Directory, and CAS authentication.

### Question 9 — `B, E` (Manage GitHub identities and access)

Correct answers: B and E (are correct). Vault **SAML recovery codes** offline before enforcing SAML, and have developers **authorize** their SSH keys and Personal Access Tokens (`Configure SSO`) for the organization. [Skill 1.5: Explain GitHub’s authentication and authorization model | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub authentication and authorization model (SSH, PAT, OAuth, SAML, OIDC) (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)]

- **A:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **B:** Correct. Storing SAML recovery codes offline prevents total administrative lockout if the corporate Identity Provider experiences a certificate or service outage.
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **E:** Correct. SAML enforcement blocks un-authorized programmatic credentials (PATs and SSH keys) even when owned by valid organization members.

### Question 10 — `C` (Manage GitHub identities and access)

Correct answer: C (is correct). SSH public-key **authentication** to GitHub succeeded (`GitHub knows the caller is dev-alex`), while **SAML SSO authorization** for that specific SSH key against `@stratusrail` has not been completed! [Skill 1.5: Explain GitHub’s authentication and authorization model | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub authentication and authorization model (SSH, PAT, OAuth, SAML, OIDC) (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)]

- **A:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **B:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **C:** Correct. Even a valid personal PAT or SSH key (`authenticated`) is blocked from accessing a SAML-enforced GHEC organization until explicitly **authorized** for SAML SSO (`authorized`).
- **D:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.

### Question 11 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Create a **Custom organization role** granting only those specific fine-grained organization permissions and assign it to the `@stratusrail-freight/release-coords` team! [Skill 1.6: Configure organization and repository roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization roles, custom roles, and repository roles (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-organization-roles)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. GitHub layers additive repository roles (`most permissive wins`) with least-privilege built-in and custom organization/enterprise roles.

### Question 12 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Yes — every custom repository role **inherits** from `Read`, `Triage`, `Write`, or `Maintain` and **adds** extra fine-grained permissions (`it cannot subtract permissions from its chosen base role, so always start from the lowest base role needed`)! [Skill 1.6: Configure organization and repository roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization roles, custom roles, and repository roles (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-organization-roles)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **D:** Correct. GitHub layers additive repository roles (`most permissive wins`) with least-privilege built-in and custom organization/enterprise roles.

### Question 13 — `B, D, E` (Manage GitHub identities and access)

Correct answers: B, D, and E (are correct). Assign **Copilot**, **custom enterprise roles**, and **ruleset bypasses** to Enterprise teams; map Enterprise teams directly across organizations; and set Organization **`Base permissions = None`**. [Skill 1.7: Define and manage enterprise teams | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining and managing Enterprise teams across organizations (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise)]

- **A:** Incorrect. IdP-synced Enterprise teams require zero manually added members and pause synchronization whenever the linked IdP group exceeds 5,000 users.
- **B:** Correct. Setting Base permissions to `None` prevents newly added org members from automatically reading or writing every private repository in the organization.
- **C:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **D:** Correct. Enterprise team organization assignments add members directly without invitations and protect enterprise-granted baseline access from org-level removal.
- **E:** Correct. Enterprise teams streamline multi-org role delegation, enterprise-level Copilot seat assignment, and ruleset bypass administration.
- **F:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 14 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). No — access granted via an **Enterprise team** is governed at the **Enterprise** level; Organization Owners cannot strip enterprise-team-assigned organization membership (`update the IdP group or Enterprise team assignment instead`)! [Skill 1.7: Define and manage enterprise teams | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining and managing Enterprise teams across organizations (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise)]

- **A:** Correct. While Enterprise teams excel at cross-org access, Copilot licensing, custom enterprise roles, and ruleset bypasses, `CODEOWNERS` requires Organization teams or individual users with Write+ access.
- **B:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **C:** Incorrect. Personal-account Team Sync (`Entra ID`/`Okta`) never adds non-members into an organization; users must join the org via SAML/SCIM invitation first (or deploy GHEC with EMUs).
- **D:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — access granted via an **Enterprise team** is governed at the **Enterprise** level; Organization Owners cannot strip enterprise-team-assigned organization membership (`update the IdP group or Enterprise team assignment instead`)!

### Question 15 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). Child Organization teams **inherit** their parent team's repository permissions (`Write` on `rail-billing`), simplifying hierarchical RBAC inside an organization (`and @mentioning parent notifies child members`)! [Skill 1.7: Define and manage enterprise teams | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining and managing Enterprise teams across organizations (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise)]

- **A:** Correct. Enterprise teams simplify multi-org governance, Copilot licensing, custom enterprise role delegation, and ruleset bypasses—though they do not support `CODEOWNERS`, nesting, Secret visibility, or non-EMU Team Sync.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **D:** Incorrect. IdP-synced Enterprise teams require zero manually added members and pause synchronization whenever the linked IdP group exceeds 5,000 users.

### Question 16 — `C` (Manage GitHub identities and access)

Correct answer: C (is correct). Inspect **Repository / Organization Rule Insights** (`Insights -> Rule Insights`, filtering by `Bypassed`) alongside `repo.ruleset_bypass` records in the **Enterprise Audit Log**! [Skill 1.8: Audit access and permissions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Auditing repository, organization, and enterprise access permissions (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/identifying-audit-log-events-performed-by-an-access-token)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Correct. Admins audit effective access via People exports, repository Manage Access filters, REST/GraphQL permission queries, and Audit Log token attribution fields.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 17 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). Querying `samlIdentityProvider.externalIdentities` (or `enterprise.members` + REST SCIM/SSH endpoints) returns exact `NameID` <-> GitHub `login` bindings across the enterprise! [Skill 1.8: Audit access and permissions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Auditing repository, organization, and enterprise access permissions (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/identifying-audit-log-events-performed-by-an-access-token)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Correct. Admins audit effective access via People exports, repository Manage Access filters, REST/GraphQL permission queries, and Audit Log token attribution fields.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.

### Question 18 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). **Repository Rulesets** can be defined once at the **Enterprise or Organization** level targeting hundreds of repos dynamically via **Custom Properties / `fnmatch`**, support **`Evaluate` dry-run mode**, layer (`most restrictive wins`), and enforce **Push file/path rules**! [Skill 1.9: Manage settings, policies, rulesets, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing enterprise member privileges, policies, repository rulesets, and bypass roles (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Correct. Organization and Enterprise admins enforce schema-validated Custom Properties on repos and bind Rulesets to property queries (`compliance_tier:pci`) automatically.

### Question 19 — `C` (Manage GitHub identities and access)

Correct answer: C (is correct). Pinning each required status check's expected source (`e.g., GitHub Actions App ID 15368`) stops a rogue token or external app from spoofing a fake passing status check with the same string name (`"ci / test"`)! [Skill 1.9: Manage settings, policies, rulesets, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing enterprise member privileges, policies, repository rulesets, and bypass roles (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise)]

- **A:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **B:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **C:** Correct. Enterprise policies set hard guardrails across all organizations, while Repository Rulesets layer additive branch/tag/push protections (`most restrictive wins`) with auditable bypasses.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 20 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). Escalate immediately to **GitHub Enterprise Support** (`providing repository URL, error output, and timestamps`) because GitHub manages underlying GHEC repository storage nodes! [Skill 2.1: Identify issues resolvable by admins vs GitHub Support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Identifying issues resolvable by Enterprise Admins vs GitHub Enterprise Support (https://docs.github.com/en/enterprise-cloud@latest/support/learning-about-github-support/about-github-support)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Correct. Admins handle internal identity, permissions, and pipeline configs, while GitHub Support handles cloud infrastructure incidents, server-side cache purges, and backend appliance/cloud escalations.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 21 — `D` (Administer GitHub Enterprise environment)

Correct answer: D (is correct). No — **internal GitHub Admins / DevOps Engineers** author custom workflows and governance policies (`or engage GitHub Expert Services / Partners`), whereas **GitHub Support** handles product break/fix, platform incidents, and documented feature behavior! [Skill 2.1: Identify issues resolvable by admins vs GitHub Support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Identifying issues resolvable by Enterprise Admins vs GitHub Enterprise Support (https://docs.github.com/en/enterprise-cloud@latest/support/learning-about-github-support/about-github-support)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. Admins handle internal identity, permissions, and pipeline configs, while GitHub Support handles cloud infrastructure incidents, server-side cache purges, and backend appliance/cloud escalations.

### Question 22 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). Confirm local health status (`ghe-diagnostics` / `ghe-repl-status`) and note UTC timestamps, capture `ghe-support-bundle -x`, sanitize confidential strings if required, and upload the bundle on the GitHub Enterprise Support portal. [Skill 2.2: Generate support bundles and diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Generating GHES support bundles, ghe-diagnostics, and ticket diagnostics (https://docs.github.com/en/enterprise-server@latest/support/contacting-github-support/providing-data-to-github-support)]

- **A:** Incorrect. Never expose appliance secrets publicly or perform multi-version upgrades mid-incident without diagnostics.
- **B:** Correct. Correct escalation workflow: verify local admin triage and timestamps, generate an extended support bundle (`ghe-support-bundle -x`), verify compliance hygiene, and attach it on the Support portal.
- **C:** Incorrect. Corporate IdP/Active Directory password resets are strictly an internal administrator responsibility, not a GitHub Support issue.
- **D:** Incorrect. Wiping logs destroys root-cause evidence before capturing a support bundle, and GitHub Support never SSHes directly into customer GHES appliances.

### Question 23 — `A, C` (Administer GitHub Enterprise environment)

Correct answers: A and C (are correct). Maintain entitled **Support** portal contacts across regional on-call shifts, and capture extended diagnostics with **`ghe-support-bundle -x`** + `ghe-diagnostics` right when symptoms occur. [Skill 2.2: Generate support bundles and diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Generating GHES support bundles, ghe-diagnostics, and ticket diagnostics (https://docs.github.com/en/enterprise-server@latest/support/contacting-github-support/providing-data-to-github-support)]

- **A:** Correct. Extended support bundles give GitHub Support complete service, cluster, and error telemetry without exposing your appliance to external SSH.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Correct. Enterprise Owners explicitly grant support-portal entitlement to designated engineers rather than sharing a single Enterprise Owner login.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **E:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 24 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). A repository's **own local** template/health file always **overrides** the organization-wide default from `<org>/.github` (`organization defaults apply cleanly wherever a local file does not exist`)! [Skill 2.3: Recommend standards for developer processes | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending enterprise standards for developer collaboration and InnerSource (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-best-practices/organize-work)]

- **A:** Correct. Workflow templates in `<org>/.github/workflow-templates/` appear automatically in the `Actions -> New workflow` gallery for every repository in the organization.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 25 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). Commit `SECURITY.md` in the root (or `.github/` folder) of the organization's **`.github`** repository (`stratusrail/.github`), automatically populating the **Security -> Policy** tab across every repository lacking a local `SECURITY.md`! [Skill 2.3: Recommend standards for developer processes | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending enterprise standards for developer collaboration and InnerSource (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-best-practices/organize-work)]

- **A:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **B:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **C:** Correct. Enterprise developer standards combine golden template repositories, an org `.github` repo for default templates/policies, and `Internal` InnerSource visibility.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 26 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). Add **`merge_group`** (`on: merge_group:`) to every workflow producing required status checks so GitHub Actions executes checks on temporary `gh-readonly-queue/...` merge-queue branches! [Skill 2.4: Define standards for workflows, branching, reviews, and releases | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining standards for workflows, branching, CODEOWNERS reviews, merge queues, and releases (https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Correct. Standardizing short-lived branches, Code Owner reviews, Merge Queue CI batching, and protected `v*` release tags keeps enterprise delivery predictable and auditable.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.

### Question 27 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). Allow **Squash merging** (and/or **Rebase merging** while disabling plain Merge commits) paired with **`Require linear history`** in the `main` Repository Ruleset! [Skill 2.4: Define standards for workflows, branching, reviews, and releases | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining standards for workflows, branching, CODEOWNERS reviews, merge queues, and releases (https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Correct. Standardizing short-lived branches, Code Owner reviews, Merge Queue CI batching, and protected `v*` release tags keeps enterprise delivery predictable and auditable.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 28 — `B, D` (Administer GitHub Enterprise environment)

Correct answers: B and D (are correct). **GHEC with Data Residency (`<enterprise>.ghe.com`)** stores repository code and metadata in the chosen region using **EMUs**, and **GitHub Connect** deduplicates Enterprise user licenses across `GHEC` + `GHES`. [Skill 2.5: Describe GitHub Enterprise deployment scenarios (GHEC with EMU, GHEC with Data Residency + EMU, GHEC with personal accounts, GHES) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise deployment models (GHEC+EMU, GHEC Data Residency ghe.com, GHEC personal, GHES) (https://docs.github.com/en/enterprise-cloud@latest/admin/overview/about-github-for-enterprises)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Correct. GitHub Connect correlates verified email addresses across GHES and GHEC and reconciles Visual Studio Enterprise/Pro with GitHub Enterprise entitlements.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. GHEC with Data Residency hosts code and metadata on a dedicated regional `.ghe.com` cloud stamp and always requires Enterprise Managed Users.
- **E:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 29 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). **GHES Clustering** horizontally partitions and scales services across multiple active cluster nodes (`designed for very high-concurrency self-hosted workloads beyond vertical single-node scaling`)! [Skill 2.5: Describe GitHub Enterprise deployment scenarios (GHEC with EMU, GHEC with Data Residency + EMU, GHEC with personal accounts, GHES) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise deployment models (GHEC+EMU, GHEC Data Residency ghe.com, GHEC personal, GHES) (https://docs.github.com/en/enterprise-cloud@latest/admin/overview/about-github-for-enterprises)]

- **A:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Correct. GHEC with Data Residency (`<ent>.ghe.com`) always uses EMUs and pins code/metadata in a chosen region (EU/US/AU/JP), while GHES runs self-hosted in your own datacenter or sovereign cloud VPC.
- **D:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 30 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). No — **GitHub Advanced Security** features (`CodeQL`, `Secret scanning`, `Push protection`, `Dependency review`) are **free (`0` GHAS seats)** on **Public** repositories on `github.com`! [Skill 2.6: Explain licensing and billing models | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise licensing, metered user-based billing, and Visual Studio subscriptions (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/about-per-user-pricing)]

- **A:** Correct. One Enterprise user consumes a single seat across unlimited organizations in the enterprise (and synced GHES instances via GitHub Connect), while Actions, Packages, Codespaces, GHAS, and Copilot meter separately.
- **B:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 31 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). Enterprises can pay via **invoiced Enterprise Agreement** or link an **Azure Subscription ID** (`billing metered GitHub Enterprise, Copilot, GHAS, Actions, and Codespaces usage directly through Microsoft Azure billing / MACC commitments`)! [Skill 2.6: Explain licensing and billing models | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise licensing, metered user-based billing, and Visual Studio subscriptions (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/about-per-user-pricing)]

- **A:** Correct. One Enterprise user consumes a single seat across unlimited organizations in the enterprise (and synced GHES instances via GitHub Connect), while Actions, Packages, Codespaces, GHAS, and Copilot meter separately.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.

### Question 32 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). They consume **`2`** seats—on GHEC, two separate GitHub usernames (`alex-personal` and `alex-rail`) are two distinct cloud user accounts (`consolidate onto one account per human — or enforce EMUs where SCIM guarantees 1 corporate identity per employee`)! [Skill 2.7: Monitor license usage and consumption | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring enterprise license consumption and GitHub Connect license sync (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/viewing-license-usage-for-github-enterprise)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. Pending org invitations, outside collaborators on private repos, enterprise members, and unsynced duplicate emails across GHES/GHEC all impact Enterprise license counts and must be audited regularly.
- **D:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 33 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). Under `Enterprise -> Billing & Licensing -> Licensing`, GitHub displays separate counters and CSV exports for **GitHub Enterprise** seats and **Visual Studio subscription** bundled seats! [Skill 2.7: Monitor license usage and consumption | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring enterprise license consumption and GitHub Connect license sync (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/viewing-license-usage-for-github-enterprise)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Correct. Pending org invitations, outside collaborators on private repos, enterprise members, and unsynced duplicate emails across GHES/GHEC all impact Enterprise license counts and must be audited regularly.
- **D:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.

### Question 34 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Verify GHAS/Secret Protection committer seat headroom, create the custom Enterprise Security Configuration, apply it to existing/transferred repos plus new-repo defaults, and set `Enforce configuration`. [Skill 3.1: Define organization and enterprise policies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining organization and enterprise security policies and security configurations (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/about-security-configurations)]

- **A:** Incorrect. Settings left as `Not set` in a Security Configuration are explicitly not enforced against repository overrides.
- **B:** Incorrect. GHAS enablement fails if active-committer seats are exhausted, transferred repos require manual attachment, and disabling Actions breaks CodeQL default setup.
- **C:** Incorrect. Manual per-repository toggling drifts immediately and misses centralized Security Configurations and enforcement.
- **D:** Correct. Correct rollout: confirm active-committer license headroom, define the custom Security Configuration, apply it to existing/transferred repos and new-repo defaults, and enforce it.

### Question 35 — `C, D` (Implement secure software development and compliance)

Correct answers: C and D (are correct). Enforce an Enterprise/Org **Security Configuration** set as default for new repos (`with CodeQL Default Setup + Dependabot`), and enforce **PR Dependency Review + CodeQL status checks** via Organization **Repository Rulesets**. [Skill 3.1: Define organization and enterprise policies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining organization and enterprise security policies and security configurations (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/about-security-configurations)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Correct. Enforced Security Configurations prevent repository admins from disabling mandatory Secret Protection, CodeQL, or Dependabot controls.
- **D:** Correct. Combining CodeQL semantic analysis, Dependabot remediation PRs, and PR-time Dependency Review stops vulnerable code and packages before merge.
- **E:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 36 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Create a **Custom Security Configuration** (`or duplicate/customize the preset`) tailored to your exact repository matrix rather than using the uneditable built-in preset as-is! [Skill 3.1: Define organization and enterprise policies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining organization and enterprise security policies and security configurations (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/about-security-configurations)]

- **A:** Correct. Enterprise Policies lock repository creation, forking, visibility changes, and Pages access globally, while enforced Security Configurations standardize GHAS/Dependabot settings across repositories.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 37 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). The **`Restrict file paths`** Push rule (`blocking .github/workflows/**/*` except via approved security workflow/role governance, or pairing `CODEOWNERS` on `.github/`) protects CI workflow definitions! [Skill 3.2: Strengthen enterprise security posture and data protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Strengthening enterprise security posture, SSH CAs, IP allow lists, and data protection (https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Correct. Push rulesets evaluate file paths, extensions, and blob sizes on `git push` before commits land on any branch in targeted repositories.

### Question 38 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). No — GitHub enforces global SSH key uniqueness, so each repository **Deploy key** must be a distinct SSH keypair (`if a service needs multi-repo read/write access, use a GitHub App installation instead of 20 deploy keys`)! [Skill 3.2: Strengthen enterprise security posture and data protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Strengthening enterprise security posture, SSH CAs, IP allow lists, and data protection (https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)]

- **A:** Correct. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **B:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 39 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Disabling member/repo-admin deletion and transfer restricts destructive `repo.destroy` and cross-org `repo.transfer` actions strictly to **Organization Owners**, preventing accidental or malicious code destruction! [Skill 3.2: Strengthen enterprise security posture and data protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Strengthening enterprise security posture, SSH CAs, IP allow lists, and data protection (https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Correct. SSH CAs eliminate unrotated static personal SSH keys by requiring short-lived certificates signed by the corporate CA, paired with IP allow lists (or Entra CAPs).

### Question 40 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Create an encrypted GCS bucket with least-privilege service-account credentials, configure the GCS sink in Enterprise Audit Log Streaming, verify the test check and enable `Stream Git events`, and enforce WORM retention + SIEM alerts. [Skill 3.3: Implement audit logging and reporting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Implementing audit logging, audit log streaming, and compliance reporting (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)]

- **A:** Incorrect. Audit log streaming is configured at the **Enterprise** level (capturing enterprise and member-organization events), not on an individual repository tab.
- **B:** Incorrect. GitHub retains non-Git audit events in the UI/API for a rolling window (up to 180 days; Git events shorter), so multi-year retention requires Audit Log Streaming.
- **C:** Correct. Correct audit-streaming setup: prepare the target sink, configure credentials in Enterprise Settings -> Audit log -> Log streaming, validate the test check, and enforce SIEM retention/alerting.
- **D:** Incorrect. Audit log streams support vetted encrypted sinks with strict verification, and audit access should use least-privilege custom roles rather than Enterprise Owner.

### Question 41 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). No — historical logs remain safely inside your external S3/Blob/GCS/SIEM storage, and GitHub validates the rotated credential via a live health test before resuming streaming seamlessly! [Skill 3.3: Implement audit logging and reporting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Implementing audit logging, audit log streaming, and compliance reporting (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Correct. Because UI/REST audit retention is time-bounded (180 days standard; shorter for high-volume Git events), compliance teams stream immutable audit events continuously to external SIEM/WORM storage.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 42 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). The **Secret scanning metrics** view inside **Security Overview** tracks total pushes blocked, bypass counts, bypass reasons (`false positive`, `used in tests`, `will fix later`), and bypassed alert resolution rates! [Skill 3.3: Implement audit logging and reporting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Implementing audit logging, audit log streaming, and compliance reporting (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)]

- **A:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **B:** Correct. Security Overview aggregates alert risk, push-protection metrics, and tool coverage across thousands of repositories for CISOs and Security Managers.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 43 — `A, B, C` (Implement secure software development and compliance)

Correct answers: A, B, and C (are correct). Attach an **Enforced Security Configuration**, turn on **Secret Scanning Push Protection + Validity Checks + Delegated Bypass**, and enforce **CodeQL + Dependabot security updates + PR Dependency Review**. [Skill 3.4: Configure vulnerability alerts, secret scanning, and CodeQL | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring vulnerability alerts, secret scanning push protection, and CodeQL code scanning (https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)]

- **A:** Correct. Combining CodeQL semantic analysis, Dependabot remediation PRs, and PR-time Dependency Review stops vulnerable code and packages before merge.
- **B:** Correct. Push Protection blocks secrets pre-receive, validity checks highlight live active credentials, and delegated bypass routes false-positive overrides through security reviewers.
- **C:** Correct. Enforced Security Configurations prevent repository admins from disabling mandatory Secret Protection, CodeQL, or Dependabot controls.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **E:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **F:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 44 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). **Copilot Autofix for CodeQL** (`GitHub Code Security`) analyzes the dataflow vulnerability and proposes a ready-to-commit code fix directly on the Pull Request! [Skill 3.4: Configure vulnerability alerts, secret scanning, and CodeQL | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring vulnerability alerts, secret scanning push protection, and CodeQL code scanning (https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)]

- **A:** Correct. CodeQL analyzes code semantically for CWE/OWASP flaws, while Secret Scanning Push Protection blocks credential commits pre-receive and verifies live token status via partner validity checks.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 45 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Organizations and Enterprises can define hundreds of custom secret patterns (`up to 500 per org / 100 per repo`), complete with start/end delimiters and `Must not match` exclusion regexes to eliminate test-fixture noise! [Skill 3.4: Configure vulnerability alerts, secret scanning, and CodeQL | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring vulnerability alerts, secret scanning push protection, and CodeQL code scanning (https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Correct. Dry-running custom regex patterns at the org/enterprise level validates false-positive rates before publishing push-protection enforcement across repositories.

### Question 46 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Configuring **`groups:`** inside `.github/dependabot.yml` (`grouping minor/patch updates or @types/* patterns together`) consolidates noisy dependency PRs into one single testable PR! [Skill 3.5: Manage Dependabot and security advisories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing Dependabot alerts, security/version updates, private registries, and advisories (https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Correct. Dependabot flags known CVEs, opens automated upgrade PRs (authenticating to private registries when configured), blocks vulnerable PR dependencies via Dependency Review, and pairs with private Security Advisories.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 47 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Dependabot **auto-triage rules** (such as automatically dismissing/snoozing low-severity alerts scoped solely to `devDependencies`/`test` scope while prioritizing `Critical`/`EPSS`-exploited runtime alerts) cut alert fatigue across repositories! [Skill 3.5: Manage Dependabot and security advisories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing Dependabot alerts, security/version updates, private registries, and advisories (https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Correct. Dependabot flags known CVEs, opens automated upgrade PRs (authenticating to private registries when configured), blocks vulnerable PR dependencies via Dependency Review, and pairs with private Security Advisories.

### Question 48 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Store the feed token inside **Dependabot secrets** (`Settings -> Secrets and variables -> Dependabot`, e.g., `NUGET_FEED_TOKEN`) and reference `${{ secrets.NUGET_FEED_TOKEN }}` under `registries:` in `dependabot.yml`! [Skill 3.5: Manage Dependabot and security advisories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing Dependabot alerts, security/version updates, private registries, and advisories (https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Correct. Granting Dependabot private-registry credentials (and running Dependabot on VNet-connected Actions/ARC runners) lets Dependabot resolve internal Artifactory/NuGet/npm packages securely.

### Question 49 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Immediately revoke & rotate `broker.pem` on the MQTT broker, rewrite all branches/tags using `git filter-repo`, force-push cleaned refs and tell collaborators to re-clone, and submit unreachable SHAs to GitHub Support to purge caches. [Skill 3.6: Define and implement a security response plan | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining a security response plan and purging sensitive data from Git history (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]

- **A:** Incorrect. GitHub Support cannot rotate third-party cloud credentials; the enterprise admin must revoke/rotate the secret immediately in AWS.
- **B:** Incorrect. Archiving keeps history readable to everyone with Read access, and merging uncleaned local clones reintroduces scrubbed commits.
- **C:** Incorrect. A normal `git rm` commit leaves the secret readable in prior commits and cached PR diffs, and unrotated leaked keys remain exploitable.
- **D:** Correct. Correct incident response: treat the secret as compromised (revoke/rotate first!), scrub history with `git filter-repo`, force-push cleaned refs, and ask GitHub Support to purge unreachable cached views.

### Question 50 — `B, E` (Implement secure software development and compliance)

Correct answers: B and E (are correct). Assume any pushed credential is **already compromised** (`revoke and rotate first at the target system`), then purge history with **`git filter-repo`** and request cache eviction from **GitHub Support**. [Skill 3.6: Define and implement a security response plan | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining a security response plan and purging sensitive data from Git history (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Correct. Publicly or internally pushed secrets can be scraped within seconds by bots or clones; credential revocation/rotation is always step #1.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **E:** Correct. `git filter-repo` rewrites Git history cleanly, and GitHub Support purges unreachable commit objects and cached Pull Request diffs on GitHub servers.

### Question 51 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). No — running `git pull` on an uncleaned local clone **re-merges and re-uploads every scrubbed commit and secret right back into `origin/main`**; require collaborators to freshly `git clone` (or reset cleanly) and temporarily protect against rogue pushes! [Skill 3.6: Define and implement a security response plan | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining a security response plan and purging sensitive data from Git history (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — running `git pull` on an uncleaned local clone **re-merges and re-uploads every scrubbed commit and secret right back into `origin/main`**; require collaborators to freshly `git clone` (or reset cleanly) and temporarily protect against rogue pushes!
- **B:** Correct. Deleting a file in a new commit never purges prior blob SHAs, and any exposed secret must be considered compromised and rotated immediately.
- **C:** Incorrect. GitHub applies default Security Configurations when a repository is newly created in the org, not when an existing repository is transferred in.
- **D:** Incorrect. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.

### Question 52 — `C, D` (Implement secure software development and compliance)

Correct answers: C and D (are correct). Enforce **Fine-grained PAT** approval + short lifetimes while blocking **`PAT (classic)`**, and standardize CI/CD bots on **GitHub App installation access tokens**. [Skill 3.7: Configure personal access tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring fine-grained and classic Personal Access Token (PAT) enterprise policies (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **C:** Correct. Enterprise PAT policies replace broad non-expiring classic tokens with short-lived, repo-scoped, admin-approved Fine-grained PATs.
- **D:** Correct. GitHub App installations on GHEC provide 3x higher REST throughput, short-lived 1-hour credentials, and complete decoupling from employee turnover.
- **E:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 53 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). No — each **Fine-grained PAT** targets **exactly one** resource owner (`a single Organization or user account`), enforcing strict blast-radius containment between organizations! [Skill 3.7: Configure personal access tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring fine-grained and classic Personal Access Token (PAT) enterprise policies (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Correct. Enterprise PAT policies curb broad non-expiring classic PATs and require organization owner approval, repo scoping, and short lifetimes on Fine-grained PATs.

### Question 54 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Organization Owners (or custom roles granted **`Review and manage personal access tokens`**) review, approve, or deny pending requests under `Organization Settings -> Personal access tokens -> Pending requests`! [Skill 3.7: Configure personal access tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring fine-grained and classic Personal Access Token (PAT) enterprise policies (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise)]

- **A:** Correct. Enterprise PAT policies curb broad non-expiring classic PATs and require organization owner approval, repo scoping, and short lifetimes on Fine-grained PATs.
- **B:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 55 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). No — it actually **cuts** the rate limit from **`15,000 req/hr` per repository** (`GITHUB_TOKEN` on GHEC) down to **`5,000 req/hr` shared across the human user** (`use GITHUB_TOKEN for single-repo tasks or a GitHub App installation token for cross-repo tasks`)! [Skill 3.8: Understand rate limits for PATs and GitHub Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Understanding REST and GraphQL API rate limits for PATs, GitHub Apps, and GITHUB_TOKEN (https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — it actually **cuts** the rate limit from **`15,000 req/hr` per repository** (`GITHUB_TOKEN` on GHEC) down to **`5,000 req/hr` shared across the human user** (`use GITHUB_TOKEN for single-repo tasks or a GitHub App installation token for cross-repo tasks`)!
- **B:** Correct. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **C:** Incorrect. Personal-account Team Sync (`Entra ID`/`Okta`) never adds non-members into an organization; users must join the org via SAML/SCIM invitation first (or deploy GHEC with EMUs).
- **D:** Incorrect. While Enterprise teams excel at cross-org access, Copilot licensing, custom enterprise roles, and ruleset bypasses, `CODEOWNERS` requires Organization teams or individual users with Write+ access.

### Question 56 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). `x-ratelimit-reset` (paired with `Retry-After` on `403`/`429` responses) tells API clients the exact Unix epoch timestamp to pause until instead of blind retry-hammering! [Skill 3.8: Understand rate limits for PATs and GitHub Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Understanding REST and GraphQL API rate limits for PATs, GitHub Apps, and GITHUB_TOKEN (https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Correct. On GHEC, GitHub App installations get 15,000 REST req/hr (and 10,000 GraphQL pts/hr) isolated from human users, whereas user PATs share one 5,000 req/hr personal bucket and hit secondary concurrency caps faster.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 57 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Unauthenticated REST calls are capped at just **`60 requests/hour` per shared NAT egress IP**—always pass `GITHUB_TOKEN` (`gh release download` with `GH_TOKEN`) even when reading public releases in CI! [Skill 3.8: Understand rate limits for PATs and GitHub Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Understanding REST and GraphQL API rate limits for PATs, GitHub Apps, and GITHUB_TOKEN (https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **C:** Correct. On GHEC, GitHub App installations get 15,000 REST req/hr (and 10,000 GraphQL pts/hr) isolated from human users, whereas user PATs share one 5,000 req/hr personal bucket and hit secondary concurrency caps faster.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 58 — `A, D` (Implement secure software development and compliance)

Correct answers: A and D (are correct). Build ChatOps bots as **GitHub Apps** (`1h installation tokens, 15,000 req/hr on GHEC, webhook-driven`), and restrict human tokens to approved, short-lived **Fine-grained PATs**. [Skill 3.9: Describe GitHub Apps and OAuth Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Comparing GitHub Apps, OAuth Apps, deploy keys, and machine users (https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)]

- **A:** Correct. Enterprise PAT policies replace broad non-expiring classic tokens with short-lived, repo-scoped, admin-approved Fine-grained PATs.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Correct. GitHub App installations on GHEC provide 3x higher REST throughput, short-lived 1-hour credentials, and complete decoupling from employee turnover.
- **E:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.

### Question 59 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Use **`actions/create-github-app-token@v1`** (`pinned by 40-char SHA`, passing `app-id` and `private-key`) to mint an ephemeral repository-scoped installation token that auto-revokes in `post:` cleanup! [Skill 3.9: Describe GitHub Apps and OAuth Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Comparing GitHub Apps, OAuth Apps, deploy keys, and machine users (https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)]

- **A:** Correct. GitHub Apps never send their `.pem` private key over the network; they sign a <=10-minute JWT locally and exchange it for a scoped 1-hour installation access token.
- **B:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **C:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 60 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). Yes — **GitHub Apps** include a single built-in **centralized Webhook configuration** that automatically delivers subscribed events for every repository granted to the installation! [Skill 3.9: Describe GitHub Apps and OAuth Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Comparing GitHub Apps, OAuth Apps, deploy keys, and machine users (https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Correct. GitHub Apps survive employee offboarding, consume zero user seats, grant fine-grained repo/resource permissions, and use short-lived tokens—outperforming both OAuth Apps and seat-consuming machine users.
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.

### Question 61 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). No — transferring a GitHub App registration to the `@stratusrail` Organization **preserves** its App ID, existing installations, and webhook continuity while shifting admin ownership to the organization! [Skill 3.10: Approve or deny app usage based on policy | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Approving, denying, and governing OAuth Apps and GitHub App installations (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Correct. With OAuth App access restrictions active, unapproved third-party OAuth apps can read public data only and cannot touch organization private repos until an Owner explicitly approves the request.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 62 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). No — elevated permission changes on an installed GitHub App remain **inactive** until an **Organization Owner** explicitly reviews and clicks **Accept new permissions**! [Skill 3.10: Approve or deny app usage based on policy | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Approving, denying, and governing OAuth Apps and GitHub App installations (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions)]

- **A:** Correct. With OAuth App access restrictions active, unapproved third-party OAuth apps can read public data only and cannot touch organization private repos until an Owner explicitly approves the request.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.

### Question 63 — `D, E` (Manage GitHub Actions)

Correct answers: D and E (are correct). Centralize `workflow_call` workflows and composite actions in **`Internal`** repos with enterprise workflow `Access` enabled, and enforce **40-character SHA pinning** + `Read-only` `GITHUB_TOKEN`. [Skill 4.1: Configure and manage reuse of actions and workflows to the enterprise repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Sharing reusable workflows and actions privately across enterprise organizations (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. Enterprise teams reuse vetted CI/CD templates privately across all member organizations without exposing proprietary workflows publicly.
- **E:** Correct. 40-char SHA pinning neutralizes upstream tag hijacking while read-only `GITHUB_TOKEN` defaults enforce job-level least privilege.

### Question 64 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Reusable workflows execute in the **caller repository's context** (`stratusrail-west/track-sensor`), receiving the caller's `GITHUB_TOKEN` and explicitly passed `inputs`/`secrets`! [Skill 4.1: Configure and manage reuse of actions and workflows to the enterprise repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Sharing reusable workflows and actions privately across enterprise organizations (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Correct. Without publishing proprietary actions to the public internet, enterprises host golden `workflow_call` workflows and actions inside `Internal`/`Private` repos with cross-repo enterprise workflow access enabled.
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 65 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Every `run:` step inside a **Composite Action** must explicitly specify **`shell:`** (`e.g., shell: bash`)! [Skill 4.1: Configure and manage reuse of actions and workflows to the enterprise repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Sharing reusable workflows and actions privately across enterprise organizations (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. Without publishing proprietary actions to the public internet, enterprises host golden `workflow_call` workflows and actions inside `Internal`/`Private` repos with cross-repo enterprise workflow access enabled.
- **D:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.

### Question 66 — `B, C` (Manage GitHub Actions)

Correct answers: B and C (are correct). Mandate **40-character commit SHA pinning** + `Read-only` `GITHUB_TOKEN`, and isolate privileged compute inside repository/workflow-restricted **Runner Groups**. [Skill 4.2: Apply organizational policies for GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing enterprise and organization GitHub Actions policies and SHA pinning (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Correct. 40-char SHA pinning neutralizes upstream tag hijacking while read-only `GITHUB_TOKEN` defaults enforce job-level least privilege.
- **C:** Correct. Runner group repository and workflow restrictions prevent untrusted repos or ad-hoc branches from scheduling jobs onto privileged runners.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **E:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 67 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Configuring **`Require workflows to pass before merging`** inside an Enterprise/Organization **Repository Ruleset** injects and enforces mandatory security workflows centrally (`no local YAML opt-in needed`)! [Skill 4.2: Apply organizational policies for GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing enterprise and organization GitHub Actions policies and SHA pinning (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Correct. Pinning third-party actions to immutable 40-char commit SHAs blocks tag-mutation supply-chain attacks, while `permissions: read-all` / read-only `GITHUB_TOKEN` defaults enforce least privilege.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 68 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). GHES syncs bundled official actions (`or proxies/downloads approved actions via GitHub Connect automatic action access`, though security best practice mirrors/pins vetted internal copies on air-gapped GHES)! [Skill 4.2: Apply organizational policies for GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing enterprise and organization GitHub Actions policies and SHA pinning (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Correct. Pinning third-party actions to immutable 40-char commit SHAs blocks tag-mutation supply-chain attacks, while `permissions: read-all` / read-only `GITHUB_TOKEN` defaults enforce least privilege.
- **C:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **D:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.

### Question 69 — `C, D, F` (Manage GitHub Actions)

Correct answers: C, D, and F (are correct). Segment runners in repository/workflow-scoped **Runner Groups**, connect Linux/Windows Larger runners to **Azure VNets** via Network Configurations, and exchange **OIDC (`id-token: write`)** tokens gated by **`production` Deployment Environments**. [Skill 4.3: Manage runner groups and administer GitHub-hosted vs. self-hosted runner options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing runner groups, Larger runners, self-hosted runners, and Actions Runner Controller (ARC) (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Correct. Azure Private Networking gives managed GitHub-hosted Larger runners private VNet egress to internal endpoints and predictable firewall/NAT egress IPs.
- **D:** Correct. Runner group repository and workflow restrictions prevent untrusted repos or ad-hoc branches from scheduling jobs onto privileged runners.
- **E:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **F:** Correct. Combining protected Deployment Environments with narrow OIDC subject claims (`repo:<org>/<repo>:environment:production`) delivers zero-standing-secret CD security.

### Question 70 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). Configure `ARC` scale sets with **`dind` (`Docker-in-Docker` isolated sidecar)** or **Kubernetes container mode (`containerMode: type: "kubernetes"`)** / rootless Kaniko/BuildKit! [Skill 4.3: Manage runner groups and administer GitHub-hosted vs. self-hosted runner options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing runner groups, Larger runners, self-hosted runners, and Actions Runner Controller (ARC) (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Correct. Runner groups isolate sensitive self-hosted or Larger runners to approved repositories and reusable workflow refs, while `--ephemeral` JIT / ARC pods ensure clean single-job runner state.

### Question 71 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). Job #41 queues cleanly (`Waiting for a runner`) until one of the 40 active ephemeral VMs finishes and terminates, preventing one runaway matrix build from starving budget or private VNet subnet IPs! [Skill 4.3: Manage runner groups and administer GitHub-hosted vs. self-hosted runner options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing runner groups, Larger runners, self-hosted runners, and Actions Runner Controller (ARC) (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Correct. Single-use ephemeral runners prevent cross-job workspace contamination, lingering credentials, or persistent malware across CI builds.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 72 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Delegate the Azure VNet subnet to `GitHub.Network` and create `NetworkSettings`, create a GitHub Network Configuration, attach it to the Linux Larger runner group, and scope the runner group to approved Terraform repos/workflows. [Skill 4.4: Apply IP allow lists and configure networking (including Azure private networking) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring IP allow lists, proxies, and Azure private networking (VNet) for runners (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization)]

- **A:** Incorrect. By default Enterprise policy restricts org-created Network Configurations unless enabled by an Enterprise Owner, and Azure NetworkSettings linkage is mandatory.
- **B:** Incorrect. Azure private networking requires Linux/Windows Larger runners (not macOS arm64 larger runners), subnet delegation, and strict runner-group access controls.
- **C:** Correct. Correct sequence: prepare the delegated Azure VNet + `GitHub.Network/networkSettings` resource, register the GitHub Network Configuration, bind it to a Larger runner group, and restrict repo/workflow access.
- **D:** Incorrect. Standard Linux runners use a multi-cloud pool beyond Azure IPs, and VNet-integrated runners still require outbound access to required GitHub endpoints.

### Question 73 — `C, D` (Manage GitHub Actions)

Correct answers: C and D (are correct). Provision sufficient private IPv4 CIDR space in the `GitHub.Network`-delegated subnet + **Network Configuration** for peak concurrent **Linux/Windows Larger runners**, and restrict access via **Runner Groups**. [Skill 4.4: Apply IP allow lists and configure networking (including Azure private networking) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring IP allow lists, proxies, and Azure private networking (VNet) for runners (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Correct. Azure Private Networking gives managed GitHub-hosted Larger runners private VNet egress to internal endpoints and predictable firewall/NAT egress IPs.
- **D:** Correct. Runner group repository and workflow restrictions prevent untrusted repos or ad-hoc branches from scheduling jobs onto privileged runners.
- **E:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 74 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). No — dedicated **static public IP ranges** (like Azure Private Networking) are an exclusive capability of **Larger GitHub-hosted runners**, **not** standard `ubuntu-latest` shared-pool runners! [Skill 4.4: Apply IP allow lists and configure networking (including Azure private networking) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring IP allow lists, proxies, and Azure private networking (VNet) for runners (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — dedicated **static public IP ranges** (like Azure Private Networking) are an exclusive capability of **Larger GitHub-hosted runners**, **not** standard `ubuntu-latest` shared-pool runners!
- **B:** Incorrect. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.
- **C:** Correct. Standard hosted runners cannot join customer Azure VNets, and arm64 macOS Larger runners do not support Azure private networking or static IP assignment.
- **D:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.

### Question 75 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). GitHub's Actions service **refuses to dispatch jobs** to critically outdated self-hosted runner agents (`>30 days past mandatory deprecation`), so air-gapped teams must automate golden-image / tarball runner upgrades promptly! [Skill 4.5: Monitor and troubleshoot runner performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring and troubleshooting runner _diag logs, queues, and performance (https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **D:** Correct. `Runner_*.log` records control-plane polling/TLS/proxy failures on the self-hosted agent, whereas `Worker_*.log` captures per-job execution details when jobs fail or stall.

### Question 76 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Add **`no_proxy=localhost,127.0.0.1,.srail.internal,10.0.0.0/8`** into the runner's **`.env`** file and restart `./svc.sh` so internal corporate traffic bypasses the internet proxy! [Skill 4.5: Monitor and troubleshoot runner performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring and troubleshooting runner _diag logs, queues, and performance (https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)]

- **A:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Correct. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **D:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.

### Question 77 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). Setting **`ACTIONS_RUNNER_HOOK_JOB_STARTED`** (`and ACTIONS_RUNNER_HOOK_JOB_COMPLETED`) in the runner `.env` executes admin-owned host scripts before and after every job! [Skill 4.5: Monitor and troubleshoot runner performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring and troubleshooting runner _diag logs, queues, and performance (https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)]

- **A:** Correct. `Runner_*.log` records control-plane polling/TLS/proxy failures on the self-hosted agent, whereas `Worker_*.log` captures per-job execution details when jobs fail or stall.
- **B:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 78 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). In the `production` Environment's **`Deployment branches and tags`** rule, select **`Selected branches and tags`** and add branch pattern `main` plus tag pattern `v*` (`paired with a Tag Ruleset protecting v*`)! [Skill 4.6: Define scope and access for secrets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining secret scope, hierarchy precedence, and deployment environment access controls (https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Correct. Production cloud secrets belong in protected Deployment Environments (`environment: production`) gated by human/custom deployment protection rules and branch filters, overriding broader repo/org secrets.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 79 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). GitHub immediately **fails/blocks** the environment deployment job without ever exposing `production` Environment secrets or minting a `production`-scoped OIDC token! [Skill 4.6: Define scope and access for secrets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining secret scope, hierarchy precedence, and deployment environment access controls (https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. Custom deployment protection rules gate `environment: production` jobs automatically via webhook callbacks to external ITSM or observability systems.

### Question 80 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). No — unlike restrictive security policies, **Actions secrets and variables** follow **specificity precedence (`Environment > Repository > Organization`)**, so the job receives `uat-kafka:9092`! [Skill 4.6: Define scope and access for secrets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining secret scope, hierarchy precedence, and deployment environment access controls (https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — unlike restrictive security policies, **Actions secrets and variables** follow **specificity precedence (`Environment > Repository > Organization`)**, so the job receives `uat-kafka:9092`!
- **B:** Incorrect. Deleting a file in a new commit never purges prior blob SHAs, and any exposed secret must be considered compromised and rotated immediately.
- **C:** Incorrect. Standard hosted runners cannot join customer Azure VNets, and arm64 macOS Larger runners do not support Azure private networking or static IP assignment.
- **D:** Correct. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.

### Question 81 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). GitHub Actions secrets are configured at **three** scopes: **Organization**, **Repository**, and **Environment** (`for enterprise-wide dynamic credentials across many orgs, federate workflows directly to an external secret manager like HashiCorp Vault / Azure Key Vault via OIDC`)! [Skill 4.7: Configure secrets at organization and repository levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization and repository encrypted secrets and variables via UI and REST API (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/creating-secrets-for-an-organization)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **D:** Correct. Organization secrets never pass to public repos unless explicitly permitted, API writes require LibSodium sealed-box encryption (`48 KB` max per secret), and plain-text config belongs in `vars` context.

### Question 82 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Eliminate multi-line JSON service-account keys entirely by switching to **Google Cloud Workload Identity Federation (`OIDC`)** (`google-github-actions/auth@v2` with `id-token: write`)! [Skill 4.7: Configure secrets at organization and repository levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization and repository encrypted secrets and variables via UI and REST API (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/creating-secrets-for-an-organization)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Correct. Organization secrets never pass to public repos unless explicitly permitted, API writes require LibSodium sealed-box encryption (`48 KB` max per secret), and plain-text config belongs in `vars` context.
- **C:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 83 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Define an **Organization Configuration Variable** (`vars.DEPLOY_REGIONS_JSON`, using `fromJSON(vars.DEPLOY_REGIONS_JSON)`) scoped to selected repositories! [Skill 4.7: Configure secrets at organization and repository levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization and repository encrypted secrets and variables via UI and REST API (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/creating-secrets-for-an-organization)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Correct. Organization secrets never pass to public repos unless explicitly permitted, API writes require LibSodium sealed-box encryption (`48 KB` max per secret), and plain-text config belongs in `vars` context.
- **C:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **D:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 84 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). Configure Vault's JWT/OIDC auth role with strict `sub`/`aud` claims, set workflow job `permissions: id-token: write`, exchange the short-lived OIDC JWT at runtime to fetch dynamic secrets, and delete legacy static secrets from GitHub. [Skill 4.8: Integrate third-party vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Integrating third-party secret vaults (HashiCorp Vault, Azure Key Vault, AWS) via OIDC (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Correct. Correct passwordless vault flow: lock down cloud/vault OIDC subject claims first, grant `id-token: write`, exchange the ephemeral OIDC token at runtime, and remove static secrets.
- **B:** Incorrect. Wildcard `repo:*` subject claims let any GitHub repository assume your cloud role, and `id-token: write` is required to request an OIDC token.
- **C:** Incorrect. The external vault/cloud IdP must trust `https://token.actions.githubusercontent.com` and exact subject claims before OIDC exchange can succeed.
- **D:** Incorrect. Storing static admin keys in repositories creates catastrophic credential exposure instead of ephemeral OIDC federation.

### Question 85 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). When `environment: production` is set on the job, `sub` automatically becomes **`repo:stratusrail/dispatch:environment:production`** (instead of `repo:stratusrail/dispatch:ref:refs/heads/...`), binding cloud access directly to your Environment's review gates! [Skill 4.8: Integrate third-party vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Integrating third-party secret vaults (HashiCorp Vault, Azure Key Vault, AWS) via OIDC (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Correct. OIDC exchanges a job-scoped JWT signed by `https://token.actions.githubusercontent.com` for short-lived dynamic vault credentials at runtime—eliminating static secrets stored in GitHub.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 86 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). Because `repo:stratusrail/*:*` allows **any developer on any unreviewed feature branch in any repository** of `@stratusrail` to assume the production IAM role—always lock `sub` to exact `repo:<org>/<repo>:environment:production` (or `job_workflow_ref`)! [Skill 4.8: Integrate third-party vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Integrating third-party secret vaults (HashiCorp Vault, Azure Key Vault, AWS) via OIDC (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Correct. OIDC exchanges a job-scoped JWT signed by `https://token.actions.githubusercontent.com` for short-lived dynamic vault credentials at runtime—eliminating static secrets stored in GitHub.
- **B:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 87 — `D, E` (Monitor and optimize GitHub usage)

Correct answers: D and E (are correct). Monitor **Organization API Insights** + **Audit Log `hashed_token`** trails, and stream **Enterprise Audit Logs** continuously to an immutable SIEM / cloud archive. [Skill 5.1: Analyze audit logs and API usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Analyzing enterprise audit logs, Git events, and API Insights / REST/GraphQL metrics (https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-your-team/apicenter/viewing-api-insights-for-your-organization)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **D:** Correct. API Insights pinpoints which App or PAT user is exhausting rate limits while Audit Log `hashed_token` traces exact administrative/API actions.
- **E:** Correct. Continuous Audit Log Streaming preserves tamper-evident compliance records far beyond GitHub’s interactive 180-day UI retention window.

### Question 88 — `B` (Monitor and optimize GitHub usage)

Correct answer: B (is correct). Granting **`View organization API insights`** inside a **Custom organization role** gives platform engineers least-privilege visibility into API traffic and rate-limited callers! [Skill 5.1: Analyze audit logs and API usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Analyzing enterprise audit logs, Git events, and API Insights / REST/GraphQL metrics (https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-your-team/apicenter/viewing-api-insights-for-your-organization)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Correct. API Insights visualizes hourly/daily REST consumption and `403`/`429` rate-limit hits broken down by specific App or PAT user so admins fix runaway polling loops quickly.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 89 — `D` (Monitor and optimize GitHub usage)

Correct answer: D (is correct). Enabling **IP address disclosure in the audit log** populates `actor_ip` alongside `user_agent`, `programmatic_access_type`, and `hashed_token` for incident forensics! [Skill 5.1: Analyze audit logs and API usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Analyzing enterprise audit logs, Git events, and API Insights / REST/GraphQL metrics (https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-your-team/apicenter/viewing-api-insights-for-your-organization)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Correct. API Insights visualizes hourly/daily REST consumption and `403`/`429` rate-limit hits broken down by specific App or PAT user so admins fix runaway polling loops quickly.

### Question 90 — `B` (Monitor and optimize GitHub usage)

Correct answer: B (is correct). Exit code **`137`** means the Linux kernel **OOM-killed** (`out of memory`) the container/process (`7 GB` RAM on standard `ubuntu-latest`); **internal Admins/Developers** fix the memory leak or move the job to a **Larger runner** (`16–256 GB` RAM)! [Skill 5.2: Distinguish admin responsibilities vs. GitHub Support and generate diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Distinguishing admin vs GitHub Support responsibilities and generating appliance/cloud diagnostics (https://docs.github.com/en/enterprise-server@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/activity-dashboard)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Correct. Admins first inspect `githubstatus.com`, SAML/webhook delivery logs, and `ghe-diagnostics` CPU/memory/queue health, escalating to GitHub Support via entitled Enterprise Support members with bundles attached.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 91 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). Running **`ghe-repl-status`** (`returning OK` exit code `0`, `WARNING` `1`, or `CRITICAL` `2`) verifies every replicated data store between primary and replica nodes! [Skill 5.2: Distinguish admin responsibilities vs. GitHub Support and generate diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Distinguishing admin vs GitHub Support responsibilities and generating appliance/cloud diagnostics (https://docs.github.com/en/enterprise-server@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/activity-dashboard)]

- **A:** Correct. GHES exposes native Prometheus metrics, SNMP, and syslog forwarding so enterprise monitoring stacks catch resource pressure before outages occur.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 92 — `C` (Monitor and optimize GitHub usage)

Correct answer: C (is correct). Premium Support adds faster guaranteed response SLAs (`e.g., 15-minute Urgent SLA`), a designated **Customer Reliability Engineer / Technical Account contact**, quarterly health reviews, and expanded entitled support seats! [Skill 5.2: Distinguish admin responsibilities vs. GitHub Support and generate diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Distinguishing admin vs GitHub Support responsibilities and generating appliance/cloud diagnostics (https://docs.github.com/en/enterprise-server@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/activity-dashboard)]

- **A:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Correct. Admins first inspect `githubstatus.com`, SAML/webhook delivery logs, and `ghe-diagnostics` CPU/memory/queue health, escalating to GitHub Support via entitled Enterprise Support members with bundles attached.
- **D:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 93 — `C` (Monitor and optimize GitHub usage)

Correct answer: C (is correct). Your `rail-sim` **self-hosted runner pool** (`or ARC maxRunners ceiling`) is undersized relative to concurrent job demand—scale `ARC` `maxRunners` or burst overflow workloads onto **Larger GitHub-hosted runners**! [Skill 5.3: Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Evaluating enterprise adoption, Copilot/Actions metrics, and dormant or underutilized features (https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Correct. Comparing assigned seats against 7/28/90-day active usage across Copilot, GHAS Security Overview, and Actions workflows highlights teams needing enablement or license reclamation.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 94 — `B` (Monitor and optimize GitHub usage)

Correct answer: B (is correct). The **Copilot Usage Dashboard** and **Copilot Metrics API** report IDE completions, IDE Chat, GitHub.com Chat, and Copilot Pull Request summary engagement! [Skill 5.3: Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Evaluating enterprise adoption, Copilot/Actions metrics, and dormant or underutilized features (https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Correct. Tracking `last_activity_at` per Copilot seat lets enterprise admins automatically reclaim unused seats after a defined inactivity window (e.g., 30–60 days).
- **C:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 95 — `B` (Monitor and optimize GitHub usage)

Correct answer: B (is correct). Combine the **Enterprise Audit Log / People export**, **Copilot `last_activity_at`**, and **IdP SSO last-sign-in / Git commit telemetry** to identify accounts with zero SSO/Git/API activity over `90+` days! [Skill 5.3: Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Evaluating enterprise adoption, Copilot/Actions metrics, and dormant or underutilized features (https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Correct. Comparing assigned seats against 7/28/90-day active usage across Copilot, GHAS Security Overview, and Actions workflows highlights teams needing enablement or license reclamation.
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 96 — `C, E` (Monitor and optimize GitHub usage)

Correct answers: C and E (are correct). Continuously audit **dormant seats, pending invites, and 90-day GHAS committers**, and assign organizations/repositories to **Cost Centers** with **75/90/100% Budgets**, `actions/cache`, short artifact retention, and Linux default runners. [Skill 5.4: Interpret usage reports for metered products | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Interpreting metered usage reports, spending limits, and cost centers for Actions, Packages, GHAS & Copilot (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-billing/using-the-billing-platform)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Correct. Cost Centers and Budgets enforce FinOps accountability while caching, shorter artifact retention, and right-sized OS runners cut metered overages.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **E:** Correct. Proactive seat hygiene reclaims idle Enterprise, Copilot, and GHAS licenses before renewal or monthly metered billing cycles.

### Question 97 — `D` (Monitor and optimize GitHub usage)

Correct answer: D (is correct). Codespaces bills **compute per core-hour** (`2-core, 4-core, 8-core...` only while active) **plus** **persistent storage per GB-month** even while **stopped** (`so enforce org Prebuild/Idle timeout + Auto-delete retention policies, e.g., 7–14 days`)! [Skill 5.4: Interpret usage reports for metered products | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Interpreting metered usage reports, spending limits, and cost centers for Actions, Packages, GHAS & Copilot (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-billing/using-the-billing-platform)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. Metered billing tracks included enterprise quotas first (for standard hosted runners and Packages/Artifacts storage) and bills overages or Larger runners/Copilot/GHAS against assigned Cost Centers and Budgets.

### Question 98 — `B` (Monitor and optimize GitHub usage)

Correct answer: B (is correct). GitHub **automatically releases** that GHAS committer license back into your available pool once the rolling **90-day** commit window expires! [Skill 5.4: Interpret usage reports for metered products | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Interpreting metered usage reports, spending limits, and cost centers for Actions, Packages, GHAS & Copilot (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-billing/using-the-billing-platform)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Correct. If an engineer pushes to 15 GHAS-enabled private repos across 4 orgs in the same enterprise, deduplicated enterprise billing counts only **1** GHAS committer license.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 99 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). For `StratusRail`'s post-merger cleanup, export consumed-licenses and verify GitHub Connect deduplication first, audit duplicate rail handles and 90-day GHAS committers, reclaim idle seats + Codespace/Actions budgets, and enforce SCIM offboarding + cost-center alerts. [Skill 5.5: Recommend strategies for license and resource optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending strategies for dormant seat reclamation, caching, and runner/storage cost optimization (https://docs.github.com/en/enterprise-server@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/managing-dormant-users)]

- **A:** Correct. Correct optimization loop: inspect unified license data, pinpoint duplicate identities/dormant users/GHAS committers, reclaim unused seats and cap metered budgets, and automate SCIM hygiene.
- **B:** Incorrect. macOS hosted runners carry a higher per-minute cost than Linux runners, long artifact retention inflates storage charges, and unmonitored seat grants waste licenses.
- **C:** Incorrect. Admins remove/suspend org or EMU memberships (preserving PR/commit audit trails) rather than deleting security controls.
- **D:** Incorrect. GHAS seats release automatically 90 days after a user’s last push (or when GHAS is disabled on the repo), and disabling GitHub Connect causes double-billing across GHEC and GHES.

### Question 100 — `B` (Monitor and optimize GitHub usage)

Correct answer: B (is correct). No — while switching Node.js builds from `macos-latest` to `ubuntu-latest` rightly cuts runner spend by `90%`, removing departed contractors from the org **does NOT delete** their historical commits, Issues, or PR comments (`reclaim all 12 seats immediately`)! [Skill 5.5: Recommend strategies for license and resource optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending strategies for dormant seat reclamation, caching, and runner/storage cost optimization (https://docs.github.com/en/enterprise-server@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/managing-dormant-users)]

- **A:** Incorrect. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.
- **B:** Correct. Offboarding or suspending inactive accounts reclaims per-user licenses cleanly without breaking repository Git history or compliance review logs.
- **C:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **D:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — while switching Node.js builds from `macos-latest` to `ubuntu-latest` rightly cuts runner spend by `90%`, removing departed contractors from the org **does NOT delete** their historical commits, Issues, or PR comments (`reclaim all 12 seats immediately`)!
