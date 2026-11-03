# Microsoft / GitHub Exam GH-100: GitHub Enterprise Administrator — Full-Length Mock Exam 2

**Theme:** Hybrid GHEC + GHES Appliance Operations — Support Bundles (ghe-support-bundle), HA/Backups, Merge Queues & GitHub Connect Licensing  
**Credential:** `GitHub Administration` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `July 2026 (Last updated May 5, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-100 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Enterprise documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Manage GitHub identities and access (15–20% official weight · 19 questions)

### 1. A genomics enterprise (`HelioBio`) operates **GitHub Enterprise Cloud with EMUs** for clinical R&D and invites external university statisticians to two specific repositories only. Which two EMU capabilities protect clinical IP? Select two.

- **A.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Provision user accounts exclusively via your corporate IdP (`SAML`/`OIDC` + `SCIM`), blocking personal public repos, Gists, and external OSS contributions
- **D.** Assign external contractors the IdP **Guest Collaborator** role so they cannot browse `Internal` enterprise repositories unless explicitly granted access
- **E.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 2. Why might an enterprise that maintains 60 high-profile **public open-source** SDKs on `github.com` choose **GHEC with personal accounts** (or a separate non-EMU public OSS enterprise) rather than a single `GHEC with EMUs` tenant alone?

- **A.** EMU **Guest Collaborator** role provisioned via the IdP to grant contractors private/internal repo access only where explicitly added (blocking broad org `Internal` browse)
- **B.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **C.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 3. When configuring **SAML 2.0 SSO** at the **Enterprise account** level (`Enterprise Settings -> Authentication security`) instead of separately on 18 individual Organizations, what happens to all 18 member Organizations?

- **A.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **B.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** Enterprise/Organization SAML 2.0 SSO paired with mandatory GitHub `2FA` (with SAML recovery codes stored safely and PAT/SSH credential authorization enforced)

### 4. During SAML SSO setup on `HelioBio`, which HTTP endpoint on GitHub (`https://github.com/enterprises/heliobio/saml/____`) receives the signed SAML `Response` assertion posted back from Okta or Entra ID?

- **A.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **B.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Enterprise/Organization SAML 2.0 SSO paired with mandatory GitHub `2FA` (with SAML recovery codes stored safely and PAT/SSH credential authorization enforced)

### 5. An IAM engineer delegates cross-organization membership, Copilot Business seats, and custom Audit Reader roles across `HelioBio` using an **Enterprise team**. Which four-step workflow applies?

- **A.** Create an Organization team in one org → expect it to grant Enterprise Audit Log roles across 50 orgs → sync via SCIM without an IdP → bypass Enterprise Owner policies
- **B.** Create an Enterprise team under People → remove manual members & link an EMU IdP group (<=5,000 users) → grant org memberships, Copilot seats, or custom enterprise roles → reference @org/ent:slug or ruleset bypass
- **C.** Assign CODEOWNERS to an Enterprise team first → nest three child Enterprise teams underneath it → mark the Enterprise team Secret → add a Team maintainer
- **D.** Add 20 manual members to the Enterprise team → simultaneously attach an IdP group while keeping manual members → add 8,000 IdP users → list @/ent:slug in CODEOWNERS

### 6. Compare **SCIM user provisioning** and **IdP Team Synchronization** on GitHub Enterprise Cloud. What happens immediately when HR deactivates an employee in Okta if **SCIM** is configured on an **EMU** enterprise?

- **A.** SCIM provisions/deprovisions user accounts across EMUs (or org invitations), whereas IdP Team Sync on personal-account GHEC (`Entra ID`/`Okta`) only updates org-team membership for existing org members
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Sync a single 12,000-member Entra ID group into one Enterprise team alongside 15 manually added contractor accounts
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 7. Which three Identity Providers have official **paved-path** partner applications for **GHEC Enterprise Managed Users (`EMUs`)** (`plus documented custom SAML 2.0 + SCIM 2.0 support for other compliant IdPs`)?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Supported IdPs (`Microsoft Entra ID`, `Okta`, `PingFederate` with paved-path OIDC/SAML+SCIM for EMUs; or `LDAP`/`CAS`/`SAML` on self-hosted `GHES`)
- **C.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 8. On self-hosted **GHES**, if you enable **`Built-in authentication`** fallback (`for emergency admin accounts outside LDAP/SAML`), where do site administrators manage built-in emergency accounts while SAML is primary?

- **A.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **B.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **C.** Supported IdPs (`Microsoft Entra ID`, `Okta`, `PingFederate` with paved-path OIDC/SAML+SCIM for EMUs; or `LDAP`/`CAS`/`SAML` on self-hosted `GHES`)
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 9. When migrating a personal-account GHEC organization to enforced SAML SSO, which two steps prevent developer `git clone`/`git push` outages and admin lockouts? Select two.

- **A.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Download and vault **Enterprise/Org SAML recovery codes** before enforcing SAML SSO so Owners can recover access during an IdP outage
- **D.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **E.** Require developers on personal-account GHEC to **authorize** approved Fine-grained/classic PATs and SSH keys for SAML SSO before accessing org repositories

### 10. In GitHub's authorization model, if an Organization Member belongs to Team Alpha (`Read` on `heliobio/lims`), Team Beta (`Maintain` on `heliobio/lims`), and holds a direct collaborator grant of `Write`, what effective role do they receive on `heliobio/lims`?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** Authentication verifies *who* the caller is (`SAML`/`OIDC`, `2FA`, Passkey, SSH key, PAT), while authorization governs *what* resources they may access (roles, teams, scopes, SAML SSO token authorization)

### 11. Which built-in GitHub **Organization role** (`____`) grants AppSec engineers read/write control over `CodeQL`, `Dependabot`, `Secret scanning`, and **Security Overview** across **all** repositories in the organization without granting `Organization Owner`?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **C.** 5 built-in repository roles (`Read`, `Triage`, `Write`, `Maintain`, `Admin`), built-in org roles (`Owner`, `Member`, `Moderator`, `Billing manager`, `Security Manager`), plus GHEC **Custom repository/org roles**
- **D.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories

### 12. On **GitHub Enterprise Cloud**, how many **Custom repository roles** can an organization create (`up to ____ custom repository roles`) to tailor fine-grained permissions between `Read`, `Triage`, `Write`, `Maintain`, and `Admin`?

- **A.** 5 built-in repository roles (`Read`, `Triage`, `Write`, `Maintain`, `Admin`), built-in org roles (`Owner`, `Member`, `Moderator`, `Billing manager`, `Security Manager`), plus GHEC **Custom repository/org roles**
- **B.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls

### 13. A platform team standardizes **Enterprise teams** across `HelioBio`'s 12 R&D organizations. Which three statements reflect valid Enterprise team governance? Select three.

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Add **Enterprise teams** across up to 1,000 organizations where org admins can grant additional repo access without removing enterprise-granted permissions
- **C.** Sync a single 12,000-member Entra ID group into one Enterprise team alongside 15 manually added contractor accounts
- **D.** Grant **Copilot Business** seats, **custom/predefined enterprise roles**, and **Repository Ruleset bypass** rights directly to **Enterprise teams** (`@/ent:<slug>`)
- **E.** Set Organization **`Base permissions = None`** and grant repository access strictly through IdP-synced Teams and least-privilege Custom Repository Roles
- **F.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 14. In an Pull Request comment inside organization `heliobio-genomics`, what exact `@mention` syntax (`@heliobio-genomics/____:biosec-reviewers`) notifies an assigned **Enterprise team** named `BioSec Reviewers`?

- **A.** **Enterprise teams** (`@/ent:<slug>`, up to 5,000 EMU IdP-synced users across up to 1,000 orgs) for centralized org membership, Copilot seats, custom enterprise roles, and ruleset bypass
- **B.** No — **Enterprise teams** (`@/ent:<slug>`) currently do **not** support `CODEOWNERS` assignment, nested child teams, Secret visibility, or Team maintainers; use an **Organization team** for `CODEOWNERS`
- **C.** Sync a single 12,000-member Entra ID group into one Enterprise team alongside 15 manually added contractor accounts
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 15. An admin on **GHEC with personal accounts** (non-EMU) tries to sync an Okta group directly to an **Enterprise team** (`People -> Enterprise teams`) and also mark that Enterprise team `Secret`. Proposed solution: Sync the Okta group to an **Enterprise team** on personal-account GHEC and set its visibility to `Secret`. Does GitHub support this?

- **A.** No — on GHEC with personal accounts, IdP **Team Synchronization** only updates Organization team membership for existing org members and **cannot** invite or provision brand-new users into the organization
- **B.** No — **Enterprise teams** (`@/ent:<slug>`) currently do **not** support `CODEOWNERS` assignment, nested child teams, Secret visibility, or Team maintainers; use an **Organization team** for `CODEOWNERS`
- **C.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **D.** No — **Azure Private Networking** (`VNet` integration) and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, NOT on standard free runners or `arm64` macOS Larger runners

### 16. On a self-hosted **GHES** appliance, a Site Administrator needs an instant comprehensive view of every organization, repository, team, SSH key, and user session across the appliance (`https://<hostname>/____`). Which administrative console path provides instance-wide user and permission inspection?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Exporting enterprise/organization membership & repository permission inventories plus auditing `org.*`, `team.*`, `repo.*`, and token metadata (`hashed_token`, `programmatic_access_type`) in the Audit Log
- **D.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges

### 17. When auditing why a user still has `Write` access to `heliobio/sequencing` after being removed from `@heliobio/seq-devs`, where should the repository `Admin` or `Organization Owner` inspect all access sources (`Direct`, `Team`, `Organization base`, `Enterprise team`)?

- **A.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Exporting enterprise/organization membership & repository permission inventories plus auditing `org.*`, `team.*`, `repo.*`, and token metadata (`hashed_token`, `programmatic_access_type`) in the Audit Log

### 18. Under `Enterprise -> Policies -> Repository management`, an Enterprise Owner sets `Repository forking` of private/internal repositories to **`Disabled`** (`Enforced`). Can an individual Organization Owner inside that enterprise re-enable private forking for their org?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Enterprise **Member privileges** (`Base permissions = None`, repo creation/forking/visibility locks) combined with **Organization/Enterprise Repository Rulesets** (`Active` vs `Evaluate` dry-run mode)
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 19. In an Enterprise or Organization **Repository Ruleset**, you want an emergency hotfix bot (`GitHub App`) to merge hotfixes during P1 incidents while still blocking human `Repository Admins` from bypassing required reviews. Which Ruleset section (`____ list`) configures exact exempt roles/Apps?

- **A.** Enterprise **Member privileges** (`Base permissions = None`, repo creation/forking/visibility locks) combined with **Organization/Enterprise Repository Rulesets** (`Active` vs `Evaluate` dry-run mode)
- **B.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

---

## Domain 2 — Administer GitHub Enterprise environment (10–15% official weight · 14 questions)

### 20. An Organization Owner accidentally deleted a critical private repository `heliobio/clinical-trial-v2` 4 hours ago, and internal self-service `Settings -> Deleted repositories -> Restore` fails because the repo had active forks in a complex network. Who can assist within the **90-day** purge window?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Enterprise Admins resolve IdP/SAML lockouts, RBAC grants, runner sizing, and webhook configs; **GitHub Enterprise Support** handles platform outages, cached PR commit purges, and repo restore escalations

### 21. A developer reports that their SAML login to `@heliobio` fails with `"AADB2C / AADSTS50105: Your administrator has configured the application HelioBio-GitHub to block users unless assigned"`. Who resolves this error?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **D.** Enterprise Admins resolve IdP/SAML lockouts, RBAC grants, runner sizing, and webhook configs; **GitHub Enterprise Support** handles platform outages, cached PR commit purges, and repo restore escalations

### 22. During a **GHES** `3.16 -> 3.17` upgrade rehearsal in `HelioBio`'s staging lab, background Elasticsearch indexing stalls. Which four-step support diagnostic workflow applies?

- **A.** Confirm admin-side checks & note exact incident UTC timestamps → SSH/console in and run ghe-support-bundle -x (or Management Console) → review/sanitize sensitive log data if required → upload bundle to GitHub Enterprise Support portal
- **B.** File a GitHub Support ticket asking GitHub to reset a developer corporate Active Directory password → wait 48 hours → run git gc locally → close ticket
- **C.** Post raw /data/user/common/secrets.conf in a public GitHub Discussion → tag @github → upgrade three major GHES versions mid-outage → skip support bundle generation
- **D.** Restart all GHES services with ghe-config-apply --force → wipe /data/user/logs to save disk → open a ticket with no timestamps or bundle → grant Support SSH access to internal VPC

### 23. A regulated biotech runs self-hosted **GHES** on AWS EC2 alongside **GHEC**. Which two support-readiness practices should platform administrators maintain? Select two.

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Designate up to 20–25 entitled **Support** members (or `Enterprise Support` custom role holders) authorized to open and manage enterprise support tickets
- **D.** Generate an extended diagnostic archive via `ghe-support-bundle -x` (or Management Console `:8443`) and upload it to the **GitHub Enterprise Support** portal
- **E.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 24. Bioinformatics squads across 6 `HelioBio` organizations keep reinventing Python package parsers from scratch because every repo defaults to `Private`. Which enterprise collaboration standard unlocks cross-org code reuse without exposing IP outside the enterprise?

- **A.** Standardizing **Template repositories**, organization-wide `.github` community health defaults, **`Internal`** InnerSource discovery, and ADR/Issue Form intake across teams
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 25. Before expanding the `/data/user` block volume or installing a feature release upgrade on self-hosted **GHES**, which administrative command (`____ -s` on port `122`) gracefully drains active Git pushes and displays a custom banner to developers?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **C.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **D.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 26. Under GxP clinical software validation, every Pull Request merged into `main` must carry a **cryptographically signed commit**, linear history, and approval from a reviewer **other than** the last person who pushed code. Which three Ruleset toggles enforce this?

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Enforcing trunk-based **GitHub Flow**, protected `main` with **`CODEOWNERS`**, **Merge Queue** (`gh-readonly-queue`) for busy monorepos, linear squash merges, and immutable signed SemVer **Releases**
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 27. To standardize release changelogs across 120 repositories without manual copy-paste errors, which file (`.github/____.yml`) configures categories (`breaking-changes`, `security`, `enhancements` mapped by PR labels) for GitHub's **`Generate release notes`** button and API?

- **A.** Enforcing trunk-based **GitHub Flow**, protected `main` with **`CODEOWNERS`**, **Merge Queue** (`gh-readonly-queue`) for busy monorepos, linear squash merges, and immutable signed SemVer **Releases**
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 28. Compare enterprise deployment choices for `HelioBio`'s European clinical division (needing EU cloud data residency) and its air-gapped Wet-Lab sequencer network. Which two architectural pairings fit? Select two.

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Deploy **GHEC with Data Residency (`<enterprise>.ghe.com`) + EMUs** when regulations require pinning cloud source code and metadata in a specific geographic region (`EU`, `US`, `AU`, `JP`)
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Enable **GitHub Connect** license synchronization between `GHES` and `GHEC` (plus link **Visual Studio Subscriptions**) so hybrid users consume a single Enterprise seat
- **E.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists

### 29. Which **GHES** topology (`Single-instance`, `High Availability`, **`____`**, or `Clustering`) deploys read-only Git/web mirror replicas in Tokyo and Frankfurt so distributed global engineers run fast low-latency `git fetch`/`git clone` operations while writes route to the primary?

- **A.** Convert existing personal GitHub.com accounts in place into Enterprise Managed Users (`EMUs`) while preserving personal public followers and Gists
- **B.** Comparing the 4 Enterprise models: **GHEC + personal accounts**, **GHEC + EMU**, **GHEC with Data Residency (`<ent>.ghe.com`) + EMU**, and self-hosted **GitHub Enterprise Server (`GHES`)**
- **C.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

### 30. How does **metered user-based billing** for **GitHub Enterprise** differ from legacy prepaid annual volume seat packs when you add 30 seasonal interns for 2 months?

- **A.** Per-user **GitHub Enterprise** seat licensing (deduplicating unique users across orgs + synced `GHES` via **GitHub Connect**, plus linked **Visual Studio Enterprise/Pro with GitHub Enterprise** benefits) alongside metered add-ons
- **B.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 31. Which two paid add-on security sub-products can organizations on **GitHub Team** and **GitHub Enterprise Cloud** now license either **individually** or bundled together inside **GitHub Advanced Security (`GHAS`)**?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Per-user **GitHub Enterprise** seat licensing (deduplicating unique users across orgs + synced `GHES` via **GitHub Connect**, plus linked **Visual Studio Enterprise/Pro with GitHub Enterprise** benefits) alongside metered add-ons
- **C.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 32. An admin connects `GHES` to `GHEC` using **GitHub Connect** automated license sync (`every ____`), yet notices 25 engineers still count as **50** consumed seats instead of **25**. What is the most common root cause?

- **A.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **B.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **C.** Inspecting `Enterprise -> Billing & Licensing -> Licensing` (and exported `consumed-licenses` JSON/CSV) to track assigned seats, pending invitations, outside collaborators, VS subscriptions, and `GHES` sync files
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 33. Does a **Suspended** user on **GitHub Enterprise Server (`GHES`)** or a **Billing manager** (who is not an Organization Member or Owner) on **GHEC** consume a paid GitHub Enterprise user license seat?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Inspecting `Enterprise -> Billing & Licensing -> Licensing` (and exported `consumed-licenses` JSON/CSV) to track assigned seats, pending invitations, outside collaborators, VS subscriptions, and `GHES` sync files
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

---

## Domain 3 — Implement secure software development and compliance (25–30% official weight · 29 questions)

### 34. Biosecurity compliance requires `HelioBio` to roll out an enforced **Enterprise Security Configuration** enabling `Secret Protection` and `CodeQL` across all 12 organizations. Which four-step sequence applies?

- **A.** Apply a GHAS Security Configuration with 0 available licenses → assume transferred repos inherit new-repo defaults automatically → disable GitHub Actions on CodeQL repos → leave unenforced
- **B.** Verify available GHAS / Secret Protection / Code Security committers → create custom Security Configuration at Enterprise/Org level → attach to existing & transferred repos plus default for new repos → set policy to Enforce configuration
- **C.** Enable Enforce configuration with every setting left as Not set → expect Not set fields to lock repository admins → delete Organization Security Managers → skip default policy
- **D.** Ask 400 repository admins to toggle checkboxes manually in every repo → disable Dependency graph → turn off push protection → audit annually by spreadsheet

### 35. Which two controls prevent individual repository admins from turning off mandatory SAST and SCA checks on clinical repositories? Select two.

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Create and **Enforce** an Enterprise/Organization **Security Configuration** (setting it as default for newly created repos and manually attaching transferred repos)
- **C.** Enable **CodeQL default/advanced setup**, **Dependabot security updates**, and the **Dependency Review Action** inside required Pull Request Rulesets
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **E.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 36. In an **Enforced Security Configuration**, if an admin sets `Secret scanning = Enabled`, `Push protection = Enabled`, and leaves `Private vulnerability reporting = ____`, can individual repository admins still toggle Private vulnerability reporting on or off?

- **A.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Enforcing **Enterprise Policies** (`Enforced` vs `No policy` delegated to orgs) and **Custom Security Configurations** (`GitHub Secret Protection` + `GitHub Code Security` / `GHAS`) across organizations
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 37. On **GitHub Enterprise Cloud**, an Enterprise Owner wants internal documentation published via **GitHub Pages** on private repositories to be readable **only** by authenticated enterprise members (`never open to the anonymous public internet`). Which Enterprise policy enforces this?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Hardening access with **Organization/Enterprise IP allow lists**, **SSH Certificate Authorities (`SSH CAs`)** issuing short-lived developer SSH certs, and least-privilege repo-scoped **Deploy keys**
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 38. When configuring an **Organization IP allow list**, what format (`____` notation, e.g., `198.51.100.0/24`) specifies permitted corporate VPN/NAT egress ranges?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Hardening access with **Organization/Enterprise IP allow lists**, **SSH Certificate Authorities (`SSH CAs`)** issuing short-lived developer SSH certs, and least-privilege repo-scoped **Deploy keys**
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

### 39. An enterprise using **GHEC with EMUs** + **Entra ID OIDC** wants to enforce corporate VPN IP checks and Intune-compliant laptop checks **without** maintaining duplicate static IP allow lists inside GitHub. Proposed solution: Enforce IP and device compliance via **Entra ID Conditional Access Policies (`CAP`)** validated automatically by GitHub's OIDC integration (with optional IP claim checks for Git/API tokens). Does the solution work?

- **A.** No — committing `git rm` (or archiving the repo) leaves the leaked secret intact in prior Git commits and cached PR diffs; you must **revoke/rotate the secret immediately**, run **`git filter-repo`**, force-push, and contact GitHub Support
- **B.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)
- **C.** No — an organization’s default **Security Configuration** auto-attaches only to **newly created** repositories; repositories **transferred** into the organization must have the Security Configuration attached manually or via API
- **D.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement

### 40. FDA 21 CFR Part 11 auditors require `HelioBio` to retain 7 years of immutable GitHub Enterprise audit events (including `git.clone` and permission changes) inside Azure Blob Storage / Sentinel. Which four-step workflow applies?

- **A.** Enable Git read/clone event streaming to a public unauthenticated HTTP webhook → skip test verification → grant all Organization Members Enterprise Owner to view logs
- **B.** Stream audit logs from a single repository Settings tab → expect enterprise-wide SAML and billing events to appear → disable SAML SSO → delete historical SIEM buckets
- **C.** Rely solely on the 180-day web UI audit search for 7-year regulatory retention → skip log streaming → poll REST API every 50 ms until rate-limited → store logs in a public Gist
- **D.** Provision encrypted SIEM/storage sink (Event Hubs, Blob, S3, Splunk) → configure credentials in Enterprise Audit Log Streaming → verify test event & optional Git toggle → set SIEM retention & alerts

### 41. If your downstream Splunk HEC or Azure Event Hubs endpoint experiences a temporary 20-minute maintenance outage while **Enterprise Audit Log Streaming** is active, how does GitHub prevent dropped audit events (`and what happens after extended multi-day failures`)?

- **A.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **B.** Streaming the **Enterprise Audit Log** (including optional `git.clone`/`git.fetch`/`git.push` events) in real time to **Azure Event Hubs / Blob Storage, AWS S3, Splunk, Datadog, or GCS**, plus REST/GraphQL queries
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 42. When querying the **Enterprise Audit Log REST API** (`GET /enterprises/{enterprise}/audit-log?phrase=____&include=all`) to include both web UI events **and** API/Git events where available, which `include` query parameter value requests combined event types?

- **A.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Streaming the **Enterprise Audit Log** (including optional `git.clone`/`git.fetch`/`git.push` events) in real time to **Azure Event Hubs / Blob Storage, AWS S3, Splunk, Datadog, or GCS**, plus REST/GraphQL queries
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 43. A biotech security architect hardens 85 GxP repositories against secret leaks, SQL/command injection, and vulnerable PyPI/CRAN dependencies. Which three capabilities work together? Select three.

- **A.** Enable **Secret Scanning Push Protection**, **Partner Validity Checks**, custom regex patterns, and **Delegated Bypass** reviewer groups
- **B.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **C.** Enable **CodeQL default/advanced setup**, **Dependabot security updates**, and the **Dependency Review Action** inside required Pull Request Rulesets
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **E.** Create and **Enforce** an Enterprise/Organization **Security Configuration** (setting it as default for newly created repos and manually attaching transferred repos)
- **F.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 44. When a developer attempts to `git push` a test fixture containing a string matching a secret pattern and **Delegated bypass for push protection** is enabled, what happens when the developer submits a bypass request?

- **A.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Enabling **CodeQL code scanning** (`Default setup` or custom `Advanced setup` SARIF workflows) plus **Secret scanning** with **Push protection**, **Validity checks**, custom regex patterns, and delegated bypass review
- **D.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing

### 45. In **Secret scanning**, what does enabling **`Validity checks`** for partner patterns accomplish when triaging 200 historical secret alerts discovered in a newly onboarded legacy repository?

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **C.** Enabling **CodeQL code scanning** (`Default setup` or custom `Advanced setup` SARIF workflows) plus **Secret scanning** with **Push protection**, **Validity checks**, custom regex patterns, and delegated bypass review
- **D.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges

### 46. Where does GitHub pull curated vulnerability intelligence (including **GitHub-reviewed** ecosystem advisories for `npm`, `pip`, `Maven`, `NuGet`, `Go`, `Cargo`, `RubyGems`, and `GitHub Actions`) to trigger **Dependabot alerts**?

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Configuring **Dependency graph**, **Dependabot alerts**, **Dependabot security & version updates** (`dependabot.yml` + private registry access), **Dependency Review Action** on PRs, and **Repository Security Advisories**
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 47. In `.github/dependabot.yml`, adding `package-ecosystem: "____"` (`directory: "/"`) instructs Dependabot to automatically open Pull Requests whenever `.github/workflows/*.yml` files reference outdated versions of reusable GitHub Actions!

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Configuring **Dependency graph**, **Dependabot alerts**, **Dependabot security & version updates** (`dependabot.yml` + private registry access), **Dependency Review Action** on PRs, and **Repository Security Advisories**
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 48. On self-hosted **GHES**, what prerequisite **GitHub Connect** setting must a Site Administrator enable so `GHES` repositories receive up-to-date vulnerability data from the cloud **GitHub Advisory Database** for Dependabot alerts?

- **A.** Configuring **Dependency graph**, **Dependabot alerts**, **Dependabot security & version updates** (`dependabot.yml` + private registry access), **Dependency Review Action** on PRs, and **Repository Security Advisories**
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **D.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls

### 49. A lab scientist accidentally commits a `20 MB` CSV containing unmasked patient PII (`clinical_subjects.csv`) plus an RDS password to `heliobio/analytics` and pushes to GHEC. Which two incident-response actions are required? Select two.

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Immediately **revoke and rotate** leaked credentials at the target cloud/API provider before assuming Git history rewrites reduce exposure
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Scrub sensitive blobs across all refs with **`git filter-repo`**, force-push cleaned branches/tags, and send commit SHAs to **GitHub Support** to purge cached PR views
- **E.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages

### 50. Why does GitHub officially recommend **`git filter-repo`** instead of legacy `git filter-branch` when scrubbing sensitive files or credentials from repository history?

- **A.** Executing the **Security Response Plan**: immediately revoke/rotate leaked secrets, scrub Git refs via **`git filter-repo`**, force-push cleaned history, and ask **GitHub Support** to purge unreachable cached PR/commit views
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 51. After running `git filter-repo --path secrets.yaml --invert-paths` and force-pushing `main`, an admin notices someone who knows the old 40-character commit SHA can still view `https://github.com/heliobio/lims/commit/<old-sha>` in a browser because a Pull Request referenced it. Proposed solution: Wait 24 hours without contacting GitHub Support, assuming cached PR commit views vanish overnight. Does the solution purge cached PR views immediately?

- **A.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **B.** No — committing `git rm` (or archiving the repo) leaves the leaked secret intact in prior Git commits and cached PR diffs; you must **revoke/rotate the secret immediately**, run **`git filter-repo`**, force-push, and contact GitHub Support
- **C.** No — suspending a dormant GHES user or removing/SCIM-deprovisioning a GHEC member **frees their Enterprise license seat** while **preserving all historical commits, Issues, and Pull Request audit trails**
- **D.** No — an organization’s default **Security Configuration** auto-attaches only to **newly created** repositories; repositories **transferred** into the organization must have the Security Configuration attached manually or via API

### 52. An enterprise IAM lead designs programmatic token governance across `HelioBio`. Which two policies enforce short lifetimes, explicit repository scoping, and resilient automation? Select two.

- **A.** Migrate org automation from personal PATs (`5,000 req/hr`) to **GHEC GitHub App installation tokens** (`15,000 REST req/hr`, 1-hour expiry, zero seat cost)
- **B.** Block or restrict **classic PATs** enterprise-wide while requiring **Organization Owner approval** and max expiration lifetimes (`<=30–90 days`) on **Fine-grained PATs**
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **E.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 53. Under `Enterprise -> Policies -> Personal access tokens`, what happens if an Enterprise Owner sets **`Restrict access via personal access tokens (classic)`** to **`Block access`**?

- **A.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Enforcing **Enterprise Fine-Grained PAT Policies**: restricting or blocking **PATs (classic)**, requiring mandatory expiration lifetimes (e.g., <=30–90 days), requiring **Admin approval** before Fine-grained PATs activate, and revoking tokens

### 54. What is the maximum lifetime policy an Enterprise Owner can enforce on **Fine-grained Personal Access Tokens** (`e.g., 7, 30, 60, 90, or ____ days` — forbidding `"No expiration"` tokens)?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Enforcing **Enterprise Fine-Grained PAT Policies**: restricting or blocking **PATs (classic)**, requiring mandatory expiration lifetimes (e.g., <=30–90 days), requiring **Admin approval** before Fine-grained PATs activate, and revoking tokens

### 55. In a GitHub Actions workflow running on a **GitHub Enterprise Cloud (`GHEC`)** repository, what is the REST API primary rate limit for the built-in **`GITHUB_TOKEN`** (`____ requests/hour per repository`) compared to `1,000 requests/hour` on Free/Team repositories?

- **A.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** REST rate limits: **`5,000 req/hr`** per personal PAT user vs **`15,000 req/hr`** for a **GitHub App installation** (and `GITHUB_TOKEN` per repo) on **GHEC** (`up to 12,500 req/hr` scaled on non-GHEC; GraphQL `5,000` vs `10,000` pts/hr)

### 56. How does GitHub calculate **GraphQL API** primary rate limits (`5,000 ____/hour` for standard users vs `10,000 ____/hour` for GHEC GitHub App installations) differently from REST API request counts?

- **A.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **B.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** REST rate limits: **`5,000 req/hr`** per personal PAT user vs **`15,000 req/hr`** for a **GitHub App installation** (and `GITHUB_TOKEN` per repo) on **GHEC** (`up to 12,500 req/hr` scaled on non-GHEC; GraphQL `5,000` vs `10,000` pts/hr)

### 57. Developer Marco authorizes an enterprise-approved OAuth App (`15,000 req/hr` GHEC user cap) that makes **8,000** REST API requests on Marco's behalf in 20 minutes. Marco then runs a local CLI script using his personal Fine-grained PAT (`5,000 req/hr` cap). Proposed solution: Assume Marco's personal PAT still has all `5,000` requests remaining because the OAuth App used a separate bucket. Will Marco's PAT succeed right now?

- **A.** No — on GHEC with personal accounts, IdP **Team Synchronization** only updates Organization team membership for existing org members and **cannot** invite or provision brand-new users into the organization
- **B.** No — **Azure Private Networking** (`VNet` integration) and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, NOT on standard free runners or `arm64` macOS Larger runners
- **C.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **D.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)

### 58. A clinical LIMS team replaces a shared machine-user account (`consuming a paid Enterprise seat + classic PAT`) with an internal **GitHub App**. Which four-step migration sequence applies?

- **A.** Create an OAuth App with full repo scope on the CEO account → hardcode the non-expiring OAuth token in YAML → disable OAuth App restrictions → delete audit logs
- **B.** Create 50 paid machine-user seats → share one classic PAT with admin:org across 50 scripts → turn off 2FA → ignore 5,000 req/hr shared user rate limits
- **C.** Create an org-owned GitHub App with least-privilege permissions → store the App private key in a vault & install on selected repos → generate a short-lived JWT to exchange for a 1-hour installation access token → revoke the legacy classic PAT
- **D.** Register a GitHub App → commit its .pem private key to a public repo → use the 10-minute JWT directly as a REST bearer token for 30 days → keep classic PATs unrestricted

### 59. An architecture board compares **GitHub Apps** against **OAuth Apps** for internal Slack/Jira webhooks and PR status checks. Which two governance rules apply? Select two.

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Migrate org automation from personal PATs (`5,000 req/hr`) to **GHEC GitHub App installation tokens** (`15,000 REST req/hr`, 1-hour expiry, zero seat cost)
- **C.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **D.** Block or restrict **classic PATs** enterprise-wide while requiring **Organization Owner approval** and max expiration lifetimes (`<=30–90 days`) on **Fine-grained PATs**
- **E.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 60. When the engineer who originally installed an **Organization-owned GitHub App** leaves `HelioBio` and their user account is deprovisioned, what happens to the GitHub App's automated Pull Request status checks (unlike a user-authorized **OAuth App**)?

- **A.** Enable Organization SAML SSO and expect pre-existing classic PATs and SSH keys to keep working against org repos with zero SAML authorization step
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** **GitHub Apps** act as independent actors scoped to selected repos + granular permissions using **1-hour installation tokens**, whereas **OAuth Apps** act as the authorizing human user with broad scopes and long-lived tokens
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 61. Where does an **Organization Owner** inspect pending developer requests to install third-party **GitHub Apps** or authorize restricted **OAuth Apps** on `@heliobio`?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Enabling **OAuth App access restrictions** and **GitHub App installation approval workflows** so developer-requested integrations stay blocked on private org data until vetted and approved by an Organization/Enterprise Owner
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

### 62. On **GitHub Enterprise Cloud**, how can an **Enterprise Owner** prevent individual Organization Owners across 15 organizations from disabling **OAuth App access restrictions**?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Enabling **OAuth App access restrictions** and **GitHub App installation approval workflows** so developer-requested integrations stay blocked on private org data until vetted and approved by an Organization/Enterprise Owner

---

## Domain 4 — Manage GitHub Actions (20–25% official weight · 24 questions)

### 63. Bioinformatics platform engineers curate 12 compliant container-scanning Actions and `workflow_call` pipelines for internal use across all `HelioBio` organizations. Which two practices enable secure cross-org sharing? Select two.

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Enforce **`Require actions to be pinned to a full-length commit SHA`**, restrict allowed actions to verified/internal sources, and default `GITHUB_TOKEN` to **`Read-only`**
- **E.** Host reusable workflows (`workflow_call`) and composite actions in **`Internal`** enterprise repositories with cross-organization workflow `Access` enabled

### 64. Can a `Private` (non-`Internal`) repository inside a GitHub Enterprise also share its reusable workflows and composite actions with **other organizations in the same Enterprise** without switching the repository visibility to `Public`?

- **A.** Sharing reusable workflows (`on: workflow_call`) and composite actions in **`Internal`** or **`Private`** repositories with `Settings -> Actions -> General -> Access` enabled for organization/enterprise workflows
- **B.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **C.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 65. When calling a reusable workflow (`jobs.scan.uses: heliobio-sec/workflows/.github/workflows/trivy.yml@a1b2c3...`), how do you pass required organization/repository secrets cleanly if policy discourages `secrets: inherit`?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Sharing reusable workflows (`on: workflow_call`) and composite actions in **`Internal`** or **`Private`** repositories with `Settings -> Actions -> General -> Access` enabled for organization/enterprise workflows
- **C.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **D.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges

### 66. Which two **GitHub Actions** administrative controls mitigate untrusted code execution from public forks and compromised third-party Marketplace tags? Select two.

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Isolate **Larger** and **ephemeral (`--ephemeral` / `ARC`) self-hosted runners** inside **Runner Groups** restricted to selected repositories and trusted reusable workflows
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Enforce **`Require actions to be pinned to a full-length commit SHA`**, restrict allowed actions to verified/internal sources, and default `GITHUB_TOKEN` to **`Read-only`**
- **E.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 67. On a public SDK repository owned by `@heliobio-oss`, which `Fork pull request workflows from outside collaborators` setting ensures **every** external contributor's fork PR pauses for maintainer code inspection before consuming Actions runners?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Enforcing **Allowed actions and reusable workflows** (`GitHub-created`, `Verified creators`, internal patterns) plus **`Require actions to be pinned to a full-length commit SHA`**, `Read-only` default `GITHUB_TOKEN`, and fork PR approval
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 68. Under `Allow select actions and reusable workflows`, if an admin enters the allowlist pattern `heliobio-sec/*, aws-actions/configure-aws-credentials@*` **plus** enables `Require actions to be pinned to a full-length commit SHA`, which workflow `uses:` reference is accepted?

- **A.** Enforcing **Allowed actions and reusable workflows** (`GitHub-created`, `Verified creators`, internal patterns) plus **`Require actions to be pinned to a full-length commit SHA`**, `Read-only` default `GITHUB_TOKEN`, and fork PR approval
- **B.** Enabling **GHES Maintenance Mode** (`ghe-maintenance -s` or Management Console) to drain active Git/Actions jobs cleanly before applying hotpatches, upgrades, or storage resizing
- **C.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 69. An HPC genomics team runs GPU container builds on **Larger GitHub-hosted runners** and private lab tests on **Actions Runner Controller (`ARC`)** Kubernetes clusters. Which three governance layers apply? Select three.

- **A.** Enforce **`Require actions to be pinned to a full-length commit SHA`**, restrict allowed actions to verified/internal sources, and default `GITHUB_TOKEN` to **`Read-only`**
- **B.** Isolate **Larger** and **ephemeral (`--ephemeral` / `ARC`) self-hosted runners** inside **Runner Groups** restricted to selected repositories and trusted reusable workflows
- **C.** Connect **Linux/Windows Larger GitHub-hosted runners** to an **Azure VNet** via `GitHub.Network/networkSettings` and Enterprise **Network Configurations**
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **E.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **F.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 70. When an Enterprise Owner creates an **Enterprise Runner Group** (`gpu-bio-runners`), how is access delegated down to repositories inside `@heliobio-genomics` (`a two-layer boundary`)?

- **A.** Organizing **Enterprise & Organization Runner Groups** restricted to selected repos and workflows, scaling **Larger GitHub-hosted runners** or ephemeral (`--ephemeral`) self-hosted runners via **Actions Runner Controller (`ARC`)** on Kubernetes
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO

### 71. What happens by default to the **`Allow public repositories`** toggle when creating a self-hosted Runner Group, and why does GitHub display a severe security warning if an admin attempts to enable it?

- **A.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Organizing **Enterprise & Organization Runner Groups** restricted to selected repos and workflows, scaling **Larger GitHub-hosted runners** or ephemeral (`--ephemeral`) self-hosted runners via **Actions Runner Controller (`ARC`)** on Kubernetes
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 72. `HelioBio` needs 16-core Linux **Larger GitHub-hosted runners** to push artifacts privately into an internal Azure Blob Storage Private Endpoint (`10.50.4.12`) with zero public internet exposure on storage. Which four-step sequence applies?

- **A.** Attach Azure VNet directly to free standard ubuntu-latest runners or macOS arm64 larger runners → skip GitHub.Network subnet delegation → allow all public fork PRs onto the private VNet runner group
- **B.** Delegate Azure VNet subnet to GitHub.Network & create NetworkSettings → create GitHub Network Configuration → attach it to a Linux/Windows Larger runner group → scope runner group to approved repos/workflows
- **C.** Whitelist only Microsoft Azure IP ranges on standard Linux hosted runners → skip Azure VNet configuration → disable outbound access to github.com endpoints → run workflows
- **D.** Have an Organization Owner create a new Network Configuration while Enterprise policy blocks org configs → skip Azure resource ID linkage → assign to repository secrets → test

### 73. By default in a GitHub Enterprise, can an individual **Organization Owner** create a brand-new independent **Azure Private Network Configuration** for hosted runners without Enterprise Owner permission, and which two controls govern private-VNet runners? Select two.

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **C.** Isolate **Larger** and **ephemeral (`--ephemeral` / `ARC`) self-hosted runners** inside **Runner Groups** restricted to selected repositories and trusted reusable workflows
- **D.** Connect **Linux/Windows Larger GitHub-hosted runners** to an **Azure VNet** via `GitHub.Network/networkSettings` and Enterprise **Network Configurations**
- **E.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 74. A security firewall admin wants standard free/included `ubuntu-latest` GitHub-hosted runners (`non-Larger runners`) to join an **Azure Private Network (`VNet`)** configuration so they receive private `10.x` IPs without configuring Larger runner groups. Proposed solution: Attach an Enterprise Azure VNet Network Configuration directly to standard `ubuntu-latest` free/included runners rather than Linux/Windows **Larger runners**. Does GitHub support this?

- **A.** No — **Azure Private Networking** (`VNet` integration) and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, NOT on standard free runners or `arm64` macOS Larger runners
- **B.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **C.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret
- **D.** No — all Personal Access Tokens and user-authorized OAuth/GitHub App user tokens for one user **share that user’s `5,000 req/hr`** budget; migrate automation to a **GitHub App installation token** (`15,000 req/hr` on GHEC)

### 75. A self-hosted runner shows `Idle` (online) in GitHub UI, picks up a job, and fails 3 seconds into step setup before any user `run:` script executes. Which runner log file (`_diag/____`) captures job execution, workspace checkout, and step container errors?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Inspecting self-hosted runner **`_diag/Runner_*.log`** (registration, listener, network/proxy errors) and **`_diag/Worker_*.log`** (job step execution), `svc.sh status`, tool-cache disk usage, and Actions queue time metrics
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 76. To capture verbose debug step logs **and** runner diagnostic traces on a failing GitHub Actions workflow without editing `.yml` files, which two repository/organization variables or re-run checkbox (`Enable ____ logging`) can an admin set?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **C.** Inspecting self-hosted runner **`_diag/Runner_*.log`** (registration, listener, network/proxy errors) and **`_diag/Worker_*.log`** (job step execution), `svc.sh status`, tool-cache disk usage, and Actions queue time metrics
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 77. On a Kubernetes **Actions Runner Controller (`ARC`)** deployment (`gha-runner-scale-set`), queued jobs sit at `Waiting for a runner to pick up this job` for 18 minutes while `maxRunners` is set to `5` and 5 slow 40-minute genomic jobs are running. How do you verify and resolve this bottleneck?

- **A.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **B.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **C.** Inspecting self-hosted runner **`_diag/Runner_*.log`** (registration, listener, network/proxy errors) and **`_diag/Worker_*.log`** (job step execution), `svc.sh status`, tool-cache disk usage, and Actions queue time metrics
- **D.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions

### 78. Can a **Dependabot** workflow run (`triggered automatically by Dependabot opening a PR`) read normal **GitHub Actions `secrets.*`**, or where must secrets needed during Dependabot runs be configured?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Scoping encrypted secrets across **Organization -> Repository -> Environment** where **most specific wins (`Environment > Repository > Organization`)**, gated by Environment **Required reviewers** and **Deployment branches/rulesets**

### 79. Platform security updates Organization secret `SIGNING_KEY_ID` to `key-2026`, yet repository `heliobio/lims` still has an older Repository-level secret named `SIGNING_KEY_ID = key-2024` and workflows keep using `key-2024`. Proposed solution: Re-save the Organization secret expecting Organization secrets to override Repository secrets of the same name. Will the Organization secret override the Repository secret?

- **A.** Yes — the proposed administration configuration satisfies every stated identity, security, compliance, and operational requirement
- **B.** No — suspending a dormant GHES user or removing/SCIM-deprovisioning a GHEC member **frees their Enterprise license seat** while **preserving all historical commits, Issues, and Pull Request audit trails**
- **C.** No — GitHub Actions secret precedence runs from **most specific to least specific (`Environment > Repository > Organization`)**, so a Repository or Environment secret with the same name overrides the Organization secret
- **D.** No — **Azure Private Networking** (`VNet` integration) and static IPs are supported on **Linux and Windows Larger GitHub-hosted runners**, NOT on standard free runners or `arm64` macOS Larger runners

### 80. If a developer runs `echo "${{ secrets.PROD_DB_PASS }}" | base64` inside a workflow step (`encoding or transforming a secret string`), will GitHub Actions' automatic log redaction (`***`) reliably mask arbitrary base64/hex mutations?

- **A.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Scoping encrypted secrets across **Organization -> Repository -> Environment** where **most specific wins (`Environment > Repository > Organization`)**, gated by Environment **Required reviewers** and **Deployment branches/rulesets**

### 81. Up to how many **Organization-level Actions secrets** (`____`) and **Repository-level Actions secrets** (`____`) can an enterprise store, and why can't you read an existing secret's plaintext back via `GET /repos/{owner}/{repo}/actions/secrets/{name}`?

- **A.** Configuring Organization secrets restricted to **`Selected repositories`** (or `Private and internal`), encrypting REST API secret uploads with the org/repo **LibSodium public key**, and separating non-sensitive **`vars`** from `secrets`
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

### 82. A build team stores `ARTIFACTORY_HOST=packages.heliobio.internal` and `JAVA_OPTS=-Xmx4g` inside encrypted `secrets.*`, causing every occurrence of `packages.heliobio.internal` in stack traces to print as unhelpful `***`. Which Actions feature fixes this cleanly?

- **A.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **B.** Configuring Organization secrets restricted to **`Selected repositories`** (or `Private and internal`), encrypting REST API secret uploads with the org/repo **LibSodium public key**, and separating non-sensitive **`vars`** from `secrets`
- **C.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 83. If an Organization Owner changes a repository's visibility from **`Internal`** to **`Public`**, what happens automatically to Organization Actions secrets that were configured with visibility **`Private and internal repositories`**?

- **A.** Repository-scoped **Deploy keys** (read-only by default, bound to a single repository) versus **GitHub App installation tokens** when automation spans multiple repositories
- **B.** Configuring Organization secrets restricted to **`Selected repositories`** (or `Private and internal`), encrypting REST API secret uploads with the org/repo **LibSodium public key**, and separating non-sensitive **`vars`** from `secrets`
- **C.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 84. `HelioBio` migrates clinical deployment workflows from static Azure Service Principal client secrets to passwordless **Azure Key Vault** retrieval via **OIDC**. Which four-step sequence applies?

- **A.** Configure OIDC trust policy in Vault/Azure/AWS with strict sub/aud claims → set job permissions id-token: write → exchange OIDC JWT at runtime for dynamic secret → delete static GitHub secrets
- **B.** Trust wildcard sub: repo:* in AWS/Vault with no org filter → leave id-token: none in workflow YAML → store root Vault token in plain-text Actions vars → echo token in logs
- **C.** Request an OIDC JWT first without configuring any Federated Identity Credential in Azure/Vault → hardcode client secrets when OIDC fails → grant write-all to fork PRs
- **D.** Export static cloud admin keys into a public repository → commit .env to main → skip OIDC subject claim validation → rotate keys every 5 years

### 85. To harden **OIDC** subject claims across an entire GitHub Enterprise so every OIDC JWT automatically embeds repository visibility, runner environment (`github-hosted` vs `self-hosted`), and `job_workflow_ref`, what can an admin customize via REST API?

- **A.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly
- **B.** Federating GitHub Actions (`permissions: id-token: write`) via **OpenID Connect (`OIDC`)** with **HashiCorp Vault**, **Azure Key Vault**, or **AWS Secrets Manager** using strict `sub` (`repo:`/`environment:`) and `aud` claims
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly

### 86. In **HashiCorp Vault**'s JWT/OIDC auth backend configured for GitHub Actions (`issuer: https://token.actions.githubusercontent.com`), which `bound_claims` attribute ensures **only** jobs running inside the centrally governed reusable workflow `heliobio-sec/workflows/.github/workflows/deploy.yml@refs/heads/main` can read production database credentials?

- **A.** Federating GitHub Actions (`permissions: id-token: write`) via **OpenID Connect (`OIDC`)** with **HashiCorp Vault**, **Azure Key Vault**, or **AWS Secrets Manager** using strict `sub` (`repo:`/`environment:`) and `aud` claims
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Configure AWS IAM / HashiCorp Vault OIDC trust with `sub: "repo:*"` so every GitHub workflow on earth can assume your production IAM role seamlessly

---

## Domain 5 — Monitor and optimize GitHub usage (10–15% official weight · 14 questions)

### 87. Security operations investigates a spike in failed `401`/`403` REST calls and needs real-time correlation between API rate-limit spikes and administrative audit events. Which two capabilities work together? Select two.

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Configure real-time **Enterprise Audit Log Streaming** (with optional Git events) to encrypted SIEM/WORM storage (`Azure Event Hubs`, `Blob`, `S3`, `Splunk`)
- **E.** Correlate **Organization API Insights** (`rate-limited callers, top Apps/PATs`) with **Enterprise Audit Log** queries (`hashed_token`, `action:org.*`) to isolate noisy tokens

### 88. In **Organization API Insights**, an admin sees an internal Python script polling `GET /repos/heliobio/lims/pulls` every 2 seconds (`43,200 calls/day`, hitting `403` rate limits constantly). What architectural change eliminates `99%` of those polling calls?

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Querying the **Enterprise Audit Log** (`action:`, `actor:`, `hashed_token:`) and **Organization API Insights** (`time-series requests, rate-limited callers, top GitHub Apps, OAuth Apps, and PATs`) to pinpoint noisy/failing integrations
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 89. Which **GraphQL** object (`query { ____ { limit cost remaining resetAt } }`) lets an enterprise integration inspect the exact point cost of its current GraphQL query and remaining hourly point budget inline?

- **A.** Querying the **Enterprise Audit Log** (`action:`, `actor:`, `hashed_token:`) and **Organization API Insights** (`time-series requests, rate-limited callers, top GitHub Apps, OAuth Apps, and PATs`) to pinpoint noisy/failing integrations
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO

### 90. On a self-hosted **GHES** appliance, where do administrators access the browser-based **Management Console** (`port ____`) to inspect cluster health monitors, TLS certificates, SAML/LDAP settings, and generate support bundles?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **C.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **D.** Using GHES **Management Console / Grafana / `ghe-diagnostics` / Activity Dashboard** (or `githubstatus.com` + Enterprise Support portal with `Support Admin` entitlement on GHEC) to separate local misconfiguration from platform incidents

### 91. To ship self-hosted **GHES** operating-system and application logs (`github-audit.log`, `haproxy.log`, `unicorn.log`, `babeld.log`) continuously to an internal Splunk/ELK collector, which native Management Console protocol should admins enable?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **D.** Scraping **GHES Prometheus `/metrics`** (or forwarding `syslog` + `SNMP` health traps) to alert platform SREs proactively on disk IOPS saturation, Redis/MySQL replication lag, and CPU load

### 92. When opening an urgent **Ticket Priority: Urgent (`P1`)** case with **GitHub Enterprise Support**, what defines a true `Urgent` incident versus a `Normal`/`Low` question?

- **A.** Open TCP port 122 to the public internet so GitHub Support engineers can SSH directly into your GHES production appliance to debug outages
- **B.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Using GHES **Management Console / Grafana / `ghe-diagnostics` / Activity Dashboard** (or `githubstatus.com` + Enterprise Support portal with `Support Admin` entitlement on GHEC) to separate local misconfiguration from platform incidents

### 93. On self-hosted **GHES**, which built-in analytics view (`Site Admin / Stafftools or Insights -> ____`) summarizes active vs dormant users, active vs inactive repositories, push volume, and Pull Request velocity across the appliance?

- **A.** Evaluating **Copilot Metrics API / Usage Dashboard** (active vs assigned seats, IDE/Chat/PR adoption), **Security Overview** coverage/MTTR, **Actions Usage Metrics**, and **GHES Dormant Users** reports to find underutilized features
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming
- **D.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 94. Engineering leadership wants aggregate daily telemetry on **GitHub Copilot** code-completion acceptance rates, active IDE languages, and Copilot Chat engagement across 25 organizations **without** spying on individual developers' prompt text. Which GHEC endpoint/dashboard provides this?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **C.** Configuring outbound corporate proxy variables (`https_proxy`, `http_proxy`, `no_proxy` inside `.env` before registering/starting `svc.sh`) on self-hosted runners behind restricted firewalls
- **D.** Querying the **GitHub Copilot User Management & Metrics REST APIs** (`last_activity_at`, `last_activity_editor`, acceptance/chat telemetry) to automate seat reclamation for inactive assignees

### 95. An AppSec VP asks which business units paid for **GHAS** yet left `CodeQL` unconfigured on `60%` of their repositories. Where can an admin verify tool adoption gaps in 10 seconds?

- **A.** Using **Enterprise/Organization Security Overview** (`Risk` and `Coverage` dashboards) to audit GHAS enablement gaps, open critical `CodeQL`/Secret/Dependabot alerts, and remediation MTTR
- **B.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **C.** Attach non-ephemeral self-hosted runners with corporate VPC access directly to a `Public` repository with zero fork PR workflow restrictions
- **D.** Pin third-party Marketplace Actions solely to mutable major tags (`uses: vendor/action@v1`) to satisfy strict enterprise supply-chain immutability

### 96. A FinOps team audits `HelioBio`'s monthly GitHub Enterprise invoice covering Enterprise seats, GHAS, GitHub Actions, and GitHub Packages. Which two billing governance practices control costs cleanly? Select two.

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Assign orgs/repos to **Cost Centers** with **75/90/100% Budget alerts**, add `actions/cache`, shorten artifact `retention-days`, and move Linux workloads off `macos` runners
- **C.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **D.** Suspend/offboard **dormant users**, cancel stale pending org invitations, and audit **90-day active GHAS committers** plus **Copilot Metrics API** active-seat ratios
- **E.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository

### 97. On GitHub Enterprise Cloud's **Enhanced Billing Platform**, what happens by default when a Cost Center or Enterprise metered **Budget** with **`Stop usage when budget limit is reached`** hits `100%` for **GitHub Actions** or **Codespaces**?

- **A.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated
- **B.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **C.** Analyzing **Enhanced Billing Platform** usage exports, **Cost Centers**, **Budgets & 75/90/100% alerts**, OS runner minute multipliers (`Linux < Windows < macOS`), shared **Actions/Packages storage**, and **90-day unique GHAS committers**
- **D.** Rely on the built-in GitHub web Audit Log UI alone to satisfy a 7-year SEC/SOX immutable log-retention mandate without configuring Audit Log Streaming

### 98. Which two metered GitHub products **share** an Enterprise account's included monthly **storage** quota (`50 GB` included on GitHub Enterprise) and outbound data transfer allowance?

- **A.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **B.** Store production TLS private keys and database passwords inside Organization Configuration Variables (`vars.*`) so workflow logs print them clearly
- **C.** GitHub Enterprise Cloud with personal accounts, where developers link user-owned GitHub.com accounts to corporate organizations via SAML SSO
- **D.** Analyzing **Enhanced Billing Platform** usage exports, **Cost Centers**, **Budgets & 75/90/100% alerts**, OS runner minute multipliers (`Linux < Windows < macOS`), shared **Actions/Packages storage**, and **90-day unique GHAS committers**

### 99. Before signing a 3-year Enterprise Agreement true-up, `HelioBio`'s IT Asset Manager audits `GHEC` + `GHES` seats, GHAS committers, and CI storage spend. Which four-step optimization workflow applies?

- **A.** Export consumed-licenses & verify GitHub Connect GHES sync → audit dormant users, duplicate emails, and 90-day GHAS committers → reclaim idle seats & right-size budgets → enforce SCIM offboarding & alerts
- **B.** Hard-delete departing employees personal GitHub accounts via Support → break PR review audit history → turn off Dependabot and CodeQL everywhere → cancel Enterprise support
- **C.** Assign every contractor Enterprise Owner and Copilot Enterprise on day one → run Linux CI jobs on 10x-multiplier macOS runners → store 500 GB build artifacts for 400 days → review bills annually
- **D.** Delete historical employee Git commits to free GHAS seats immediately → disable GitHub Connect so GHEC+GHES users are billed twice → set unlimited Actions spending limits → skip budgets

### 100. A repository uploads `4 GB` of Playwright video artifacts on every commit with the default **`90`-day** retention period (`accumulating 1.2 TB of metered storage/month`). Which single YAML parameter on `actions/upload-artifact@v4` slashes storage spend by `90%+`?

- **A.** Assume GitHub Advanced Security (`GHAS`) consumes a paid seat for every read-only Stakeholder, Triage PM, and bot reading a private repository
- **B.** Standardize all Linux Docker container builds onto `macos-latest` GitHub-hosted runners to minimize per-minute Actions compute charges
- **C.** Reclaiming **dormant GHES/GHEC seats** & stale pending invitations, enabling **GitHub Connect** license deduplication, caching dependencies (`actions/cache`), shortening artifact retention days, and right-sizing `ubuntu` vs `macos` runners
- **D.** Purchase two separate full GitHub Enterprise seats for every engineer who uses both GHEC and GHES because licenses can never be deduplicated

---

## Answer Key and Explanations

### Question 1 — `C, D` (Manage GitHub identities and access)

Correct answers: C and D (are correct). IdP-provisioned **EMUs** prevent public repo/Gist creation and external pushes, while assigning external statisticians the **Guest Collaborator** role blocks broad `Internal` repository visibility. [Skill 1.1: Describe differences between managed users and personal accounts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: About Enterprise Managed Users vs personal accounts (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users)]

- **A:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. EMUs ensure corporate lifecycle control and eliminate accidental public repo or Gist leakage under managed handles.
- **D:** Correct. Guest Collaborators prevent contractors in EMU enterprises from automatically reading all `Internal` repositories across member organizations.
- **E:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 2 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). In a standard **EMU** enterprise on `github.com`, managed user accounts cannot create **public** repositories or contribute to external open-source repos (`whereas GHEC with personal accounts supports public OSS repositories natively`)! [Skill 1.1: Describe differences between managed users and personal accounts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: About Enterprise Managed Users vs personal accounts (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users)]

- **A:** Incorrect. In EMU enterprises, Guest Collaborators are IdP-provisioned accounts restricted from automatic `Internal` repository visibility across organizations unless granted explicit access.
- **B:** Correct. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **C:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 3 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Enterprise-level SAML SSO enforces a **single unified SAML configuration** automatically across every current and future Organization in the enterprise, eliminating 18 separate IdP app certificates! [Skill 1.2: Configure and enforce SAML SSO and 2FA | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing SAML single sign-on and two-factor authentication (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise)]

- **A:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **B:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Correct. Enforcing SAML SSO at the Enterprise level centralizes IdP authentication across all member organizations, requires credential authorization for PATs/SSH keys, and pairs with `2FA` on personal-account GHEC.

### Question 4 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). The **Assertion Consumer Service (`ACS`) URL** (`/saml/consume`) receives and validates cryptographically signed SAML assertions from the Identity Provider. [Skill 1.2: Configure and enforce SAML SSO and 2FA | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing SAML single sign-on and two-factor authentication (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise)]

- **A:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **B:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Correct. Enforcing SAML SSO at the Enterprise level centralizes IdP authentication across all member organizations, requires credential authorization for PATs/SSH keys, and pairs with `2FA` on personal-account GHEC.

### Question 5 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). Create the Enterprise team under `People -> Enterprise teams`, remove manual members and bind an EMU IdP group (`<=5,000` users), grant org memberships/Copilot/custom enterprise roles, and reference `@org/ent:slug` or ruleset bypasses. [Skill 1.3: Understand SCIM and team synchronization: implementation and key differences | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring SCIM provisioning vs IdP team synchronization (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim/provisioning-users-and-groups-with-scim-using-the-rest-api)]

- **A:** Incorrect. An Organization team is scoped to one organization and cannot hold enterprise-level administrative roles across sibling organizations.
- **B:** Correct. Correct workflow: create the Enterprise team, bind an EMU IdP group (with zero manual members and <=5,000 users), assign org/Copilot/role entitlements, and use @org/ent:slug or ruleset bypasses.
- **C:** Incorrect. Enterprise teams currently do not support CODEOWNERS, nested teams, Secret visibility, or Team maintainers.
- **D:** Incorrect. Fails three platform rules: IdP-synced Enterprise teams cannot retain manual members, IdP sync pauses above 5,000 users, and Enterprise teams do not support CODEOWNERS.

### Question 6 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). Okta sends a SCIM `PATCH`/`DELETE` deactivation call that immediately **suspends** the EMU user, terminates active browser sessions, and revokes all PATs and SSH keys across the enterprise! [Skill 1.3: Understand SCIM and team synchronization: implementation and key differences | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring SCIM provisioning vs IdP team synchronization (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim/provisioning-users-and-groups-with-scim-using-the-rest-api)]

- **A:** Correct. SCIM manages account lifecycle (creating/suspending EMUs), while personal-account Team Sync only maps IdP groups to Organization teams and cannot invite non-members into an organization.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. IdP-synced Enterprise teams require zero manually added members and pause synchronization whenever the linked IdP group exceeds 5,000 users.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 7 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). **Microsoft Entra ID**, **Okta**, and **PingFederate** provide native paved-path EMU integrations (`with Entra ID supporting both OIDC and SAML, and Okta/PingFederate using SAML + SCIM`). [Skill 1.4: Choose and configure identity providers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Choosing and configuring Identity Providers (Entra ID, Okta, PingFederate, CAS/LDAP) (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-identity-and-access-management)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Correct. GHEC EMUs support Entra ID (OIDC or SAML), Okta, and PingFederate (plus custom SAML+SCIM API integration), while GHES adds native LDAP, Active Directory, and CAS authentication.
- **C:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 8 — `C` (Manage GitHub identities and access)

Correct answer: C (is correct). Site administrators can sign in at `/login?built_in=true` (or via Management Console `:8443` / SSH port `122`) when external SAML/LDAP infrastructure is unreachable. [Skill 1.4: Choose and configure identity providers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Choosing and configuring Identity Providers (Entra ID, Okta, PingFederate, CAS/LDAP) (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-identity-and-access-management)]

- **A:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **B:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **C:** Correct. GHEC EMUs support Entra ID (OIDC or SAML), Okta, and PingFederate (plus custom SAML+SCIM API integration), while GHES adds native LDAP, Active Directory, and CAS authentication.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 9 — `C, E` (Manage GitHub identities and access)

Correct answers: C and E (are correct). Store **SAML recovery codes** in an enterprise password vault before enforcing SAML, and guide engineers to **authorize** their SSH keys and PATs for SAML SSO. [Skill 1.5: Explain GitHub’s authentication and authorization model | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub authentication and authorization model (SSH, PAT, OAuth, SAML, OIDC) (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)]

- **A:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Correct. Storing SAML recovery codes offline prevents total administrative lockout if the corporate Identity Provider experiences a certificate or service outage.
- **D:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **E:** Correct. SAML enforcement blocks un-authorized programmatic credentials (PATs and SSH keys) even when owned by valid organization members.

### Question 10 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Repository role grants are **additive (`most permissive wins`)**, so the user receives effective **`Maintain`** permissions on `heliobio/lims`! [Skill 1.5: Explain GitHub’s authentication and authorization model | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub authentication and authorization model (SSH, PAT, OAuth, SAML, OIDC) (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Correct. Even a valid personal PAT or SSH key (`authenticated`) is blocked from accessing a SAML-enforced GHEC organization until explicitly **authorized** for SAML SSO (`authorized`).

### Question 11 — `C` (Manage GitHub identities and access)

Correct answer: C (is correct). The built-in **`Security Manager`** organization role delegates org-wide security alert visibility and security configuration management under least privilege. [Skill 1.6: Configure organization and repository roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization roles, custom roles, and repository roles (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-organization-roles)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **C:** Correct. GitHub layers additive repository roles (`most permissive wins`) with least-privilege built-in and custom organization/enterprise roles.
- **D:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.

### Question 12 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). Organizations on GitHub Enterprise Cloud can define up to **`5`** custom repository roles (alongside custom organization and custom enterprise roles)! [Skill 1.6: Configure organization and repository roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization roles, custom roles, and repository roles (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-organization-roles)]

- **A:** Correct. GitHub layers additive repository roles (`most permissive wins`) with least-privilege built-in and custom organization/enterprise roles.
- **B:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.

### Question 13 — `B, D, E` (Manage GitHub identities and access)

Correct answers: B, D, and E (are correct). Assign **Copilot Business** licenses, **custom enterprise roles**, and **ruleset bypasses** to Enterprise teams; grant Enterprise teams access across organizations (where org admins cannot strip enterprise-granted access); and keep **`Base permissions = None`**. [Skill 1.7: Define and manage enterprise teams | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining and managing Enterprise teams across organizations (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Correct. Enterprise team organization assignments add members directly without invitations and protect enterprise-granted baseline access from org-level removal.
- **C:** Incorrect. IdP-synced Enterprise teams require zero manually added members and pause synchronization whenever the linked IdP group exceeds 5,000 users.
- **D:** Correct. Enterprise teams streamline multi-org role delegation, enterprise-level Copilot seat assignment, and ruleset bypass administration.
- **E:** Correct. Setting Base permissions to `None` prevents newly added org members from automatically reading or writing every private repository in the organization.
- **F:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 14 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). Enterprise teams automatically carry the **`ent:`** slug prefix, so members mention or request PR reviews from `@heliobio-genomics/ent:biosec-reviewers` (or `@/ent:biosec-reviewers`)! [Skill 1.7: Define and manage enterprise teams | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining and managing Enterprise teams across organizations (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise)]

- **A:** Correct. Enterprise teams simplify multi-org governance, Copilot licensing, custom enterprise role delegation, and ruleset bypasses—though they do not support `CODEOWNERS`, nesting, Secret visibility, or non-EMU Team Sync.
- **B:** Incorrect. While Enterprise teams excel at cross-org access, Copilot licensing, custom enterprise roles, and ruleset bypasses, `CODEOWNERS` requires Organization teams or individual users with Write+ access.
- **C:** Incorrect. IdP-synced Enterprise teams require zero manually added members and pause synchronization whenever the linked IdP group exceeds 5,000 users.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 15 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). No — IdP group sync on **Enterprise teams** requires **Enterprise Managed Users (`EMUs`)**, and Enterprise teams do **not** support `Secret` visibility, nested teams, or `CODEOWNERS`! [Skill 1.7: Define and manage enterprise teams | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining and managing Enterprise teams across organizations (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise)]

- **A:** Incorrect. Personal-account Team Sync (`Entra ID`/`Okta`) never adds non-members into an organization; users must join the org via SAML/SCIM invitation first (or deploy GHEC with EMUs).
- **B:** Correct. While Enterprise teams excel at cross-org access, Copilot licensing, custom enterprise roles, and ruleset bypasses, `CODEOWNERS` requires Organization teams or individual users with Write+ access.
- **C:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — IdP group sync on **Enterprise teams** requires **Enterprise Managed Users (`EMUs`)**, and Enterprise teams do **not** support `Secret` visibility, nested teams, or `CODEOWNERS`!
- **D:** Incorrect. Standard hosted runners cannot join customer Azure VNets, and arm64 macOS Larger runners do not support Azure private networking or static IP assignment.

### Question 16 — `C` (Manage GitHub identities and access)

Correct answer: C (is correct). Navigating to **`/stafftools`** (**Site Admin** console on GHES) lets Site Administrators audit any user's effective repository access, SSH keys, PAT fingerprints, and SAML/LDAP mappings! [Skill 1.8: Audit access and permissions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Auditing repository, organization, and enterprise access permissions (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/identifying-audit-log-events-performed-by-an-access-token)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Correct. Admins audit effective access via People exports, repository Manage Access filters, REST/GraphQL permission queries, and Audit Log token attribution fields.
- **D:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.

### Question 17 — `D` (Manage GitHub identities and access)

Correct answer: D (is correct). Check `Repository Settings -> Collaborators and teams` (**Manage access**), filtering by the username to see every direct collaborator grant, Organization team, or Enterprise team contributing access. [Skill 1.8: Audit access and permissions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Auditing repository, organization, and enterprise access permissions (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/identifying-audit-log-events-performed-by-an-access-token)]

- **A:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. Admins audit effective access via People exports, repository Manage Access filters, REST/GraphQL permission queries, and Audit Log token attribution fields.

### Question 18 — `B` (Manage GitHub identities and access)

Correct answer: B (is correct). No — when an Enterprise policy is set to **Enforced** (rather than `No policy`), Organization Owners cannot override or relax the enterprise-wide restriction! [Skill 1.9: Manage settings, policies, rulesets, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing enterprise member privileges, policies, repository rulesets, and bypass roles (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Correct. Enterprise policies set hard guardrails across all organizations, while Repository Rulesets layer additive branch/tag/push protections (`most restrictive wins`) with auditable bypasses.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 19 — `A` (Manage GitHub identities and access)

Correct answer: A (is correct). Add **only** the vetted emergency **GitHub App** (or an Enterprise team / Custom Role with `Pull request bypass` require-approval mode) to the Ruleset **`Bypass list`**, omitting `Repository admin`! [Skill 1.9: Manage settings, policies, rulesets, and roles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing enterprise member privileges, policies, repository rulesets, and bypass roles (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise)]

- **A:** Correct. Enterprise policies set hard guardrails across all organizations, while Repository Rulesets layer additive branch/tag/push protections (`most restrictive wins`) with auditable bypasses.
- **B:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 20 — `D` (Administer GitHub Enterprise environment)

Correct answer: D (is correct). Escalate immediately to **GitHub Enterprise Support** (if self-service restore under `Organization Settings -> Deleted repositories` is blocked, Support can assist with eligible repository recovery within 90 days of deletion)! [Skill 2.1: Identify issues resolvable by admins vs GitHub Support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Identifying issues resolvable by Enterprise Admins vs GitHub Enterprise Support (https://docs.github.com/en/enterprise-cloud@latest/support/learning-about-github-support/about-github-support)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Correct. Admins handle internal identity, permissions, and pipeline configs, while GitHub Support handles cloud infrastructure incidents, server-side cache purges, and backend appliance/cloud escalations.

### Question 21 — `D` (Administer GitHub Enterprise environment)

Correct answer: D (is correct). Your internal **Identity Provider (`Entra ID`) / GitHub Enterprise Administrator** must assign the user or security group to the enterprise SAML application in Entra ID—GitHub Support cannot modify customer IdP assignments! [Skill 2.1: Identify issues resolvable by admins vs GitHub Support | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Identifying issues resolvable by Enterprise Admins vs GitHub Enterprise Support (https://docs.github.com/en/enterprise-cloud@latest/support/learning-about-github-support/about-github-support)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **D:** Correct. Admins handle internal identity, permissions, and pipeline configs, while GitHub Support handles cloud infrastructure incidents, server-side cache purges, and backend appliance/cloud escalations.

### Question 22 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). Verify admin health checks and note UTC timestamps, run `ghe-support-bundle -x` over SSH port `122` (or Management Console `:8443`), sanitize regulated strings if mandated, and upload the bundle on the GitHub Enterprise Support portal. [Skill 2.2: Generate support bundles and diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Generating GHES support bundles, ghe-diagnostics, and ticket diagnostics (https://docs.github.com/en/enterprise-server@latest/support/contacting-github-support/providing-data-to-github-support)]

- **A:** Correct. Correct escalation workflow: verify local admin triage and timestamps, generate an extended support bundle (`ghe-support-bundle -x`), verify compliance hygiene, and attach it on the Support portal.
- **B:** Incorrect. Corporate IdP/Active Directory password resets are strictly an internal administrator responsibility, not a GitHub Support issue.
- **C:** Incorrect. Never expose appliance secrets publicly or perform multi-version upgrades mid-incident without diagnostics.
- **D:** Incorrect. Wiping logs destroys root-cause evidence before capturing a support bundle, and GitHub Support never SSHes directly into customer GHES appliances.

### Question 23 — `C, D` (Administer GitHub Enterprise environment)

Correct answers: C and D (are correct). Train SREs to generate extended bundles with `ghe-support-bundle -x` (or pipe direct uploads via `ghe-support-upload` where outbound HTTPS is allowed) and maintain entitled **Support** portal contacts. [Skill 2.2: Generate support bundles and diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Generating GHES support bundles, ghe-diagnostics, and ticket diagnostics (https://docs.github.com/en/enterprise-server@latest/support/contacting-github-support/providing-data-to-github-support)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Correct. Enterprise Owners explicitly grant support-portal entitlement to designated engineers rather than sharing a single Enterprise Owner login.
- **D:** Correct. Extended support bundles give GitHub Support complete service, cluster, and error telemetry without exposing your appliance to external SSH.
- **E:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 24 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). Adopt **InnerSource** using **`Internal`** enterprise repositories equipped with `README.md`, `CONTRIBUTING.md`, `CODEOWNERS`, and searchable **Repository Topics**! [Skill 2.3: Recommend standards for developer processes | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending enterprise standards for developer collaboration and InnerSource (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-best-practices/organize-work)]

- **A:** Correct. Enterprise developer standards combine golden template repositories, an org `.github` repo for default templates/policies, and `Internal` InnerSource visibility.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 25 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). Running **`ghe-maintenance -s`** enables GHES Maintenance Mode (`and ghe-maintenance -u` disables it once upgrade checks pass). [Skill 2.3: Recommend standards for developer processes | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending enterprise standards for developer collaboration and InnerSource (https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-best-practices/organize-work)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Correct. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **C:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **D:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 26 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). Enable **`Require signed commits`**, **`Require linear history`**, and **`Require approval of the most recent reviewable push`** (paired with `Dismiss stale pull request approvals when new commits are pushed`)! [Skill 2.4: Define standards for workflows, branching, reviews, and releases | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining standards for workflows, branching, CODEOWNERS reviews, merge queues, and releases (https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Correct. Standardizing short-lived branches, Code Owner reviews, Merge Queue CI batching, and protected `v*` release tags keeps enterprise delivery predictable and auditable.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 27 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). Committing **`.github/release.yml`** categorizes Pull Requests by labels and excludes bot/chore noise whenever maintainers generate GitHub Releases! [Skill 2.4: Define standards for workflows, branching, reviews, and releases | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining standards for workflows, branching, CODEOWNERS reviews, merge queues, and releases (https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)]

- **A:** Correct. Standardizing short-lived branches, Code Owner reviews, Merge Queue CI batching, and protected `v*` release tags keeps enterprise delivery predictable and auditable.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 28 — `B, D` (Administer GitHub Enterprise environment)

Correct answers: B and D (are correct). Use **GHEC with Data Residency (`heliobio.ghe.com` in EU) + EMUs** for European cloud workloads, and run self-hosted **GHES** for the wet-lab network with **GitHub Connect** / manual license deduplication. [Skill 2.5: Describe GitHub Enterprise deployment scenarios (GHEC with EMU, GHEC with Data Residency + EMU, GHEC with personal accounts, GHES) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise deployment models (GHEC+EMU, GHEC Data Residency ghe.com, GHEC personal, GHES) (https://docs.github.com/en/enterprise-cloud@latest/admin/overview/about-github-for-enterprises)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Correct. GHEC with Data Residency hosts code and metadata on a dedicated regional `.ghe.com` cloud stamp and always requires Enterprise Managed Users.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. GitHub Connect correlates verified email addresses across GHES and GHEC and reconciles Visual Studio Enterprise/Pro with GitHub Enterprise entitlements.
- **E:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.

### Question 29 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). **GHES Geo-replication** places active read-only geographic replicas close to remote offices to accelerate `git clone`/`fetch` and double as regional failover targets! [Skill 2.5: Describe GitHub Enterprise deployment scenarios (GHEC with EMU, GHEC with Data Residency + EMU, GHEC with personal accounts, GHES) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise deployment models (GHEC+EMU, GHEC Data Residency ghe.com, GHEC personal, GHES) (https://docs.github.com/en/enterprise-cloud@latest/admin/overview/about-github-for-enterprises)]

- **A:** Incorrect. Personal GitHub.com accounts can never be converted in place into EMUs; EMUs are provisioned fresh from the corporate IdP and cannot own public repos or Gists.
- **B:** Correct. GHEC with Data Residency (`<ent>.ghe.com`) always uses EMUs and pins code/metadata in a chosen region (EU/US/AU/JP), while GHES runs self-hosted in your own datacenter or sovereign cloud VPC.
- **C:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 30 — `A` (Administer GitHub Enterprise environment)

Correct answer: A (is correct). With **metered per-user billing**, seats scale dynamically month-to-month based on assigned Enterprise licenses without hitting hard prepaid seat-cap blocks when onboarding seasonal cohorts! [Skill 2.6: Explain licensing and billing models | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise licensing, metered user-based billing, and Visual Studio subscriptions (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/about-per-user-pricing)]

- **A:** Correct. One Enterprise user consumes a single seat across unlimited organizations in the enterprise (and synced GHES instances via GitHub Connect), while Actions, Packages, Codespaces, GHAS, and Copilot meter separately.
- **B:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 31 — `B` (Administer GitHub Enterprise environment)

Correct answer: B (is correct). **GitHub Secret Protection** (secret scanning, push protection, validity checks) and **GitHub Code Security** (CodeQL code scanning, Dependabot security features, dependency review)! [Skill 2.6: Explain licensing and billing models | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: GitHub Enterprise licensing, metered user-based billing, and Visual Studio subscriptions (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/about-per-user-pricing)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Correct. One Enterprise user consumes a single seat across unlimited organizations in the enterprise (and synced GHES instances via GitHub Connect), while Actions, Packages, Codespaces, GHAS, and Copilot meter separately.
- **C:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 32 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). GitHub Connect syncs weekly/periodically and matches users by **verified email address**; if an engineer's GHES primary email (`jdoe@lab.internal`) does not match any verified email on their GHEC account (`jane.doe@heliobio.com`), GitHub counts two distinct users! [Skill 2.7: Monitor license usage and consumption | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring enterprise license consumption and GitHub Connect license sync (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/viewing-license-usage-for-github-enterprise)]

- **A:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **B:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **C:** Correct. Pending org invitations, outside collaborators on private repos, enterprise members, and unsynced duplicate emails across GHES/GHEC all impact Enterprise license counts and must be audited regularly.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 33 — `C` (Administer GitHub Enterprise environment)

Correct answer: C (is correct). No — **suspended** GHES accounts and standalone **Billing managers** consume **zero** paid GitHub Enterprise user seats! [Skill 2.7: Monitor license usage and consumption | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring enterprise license consumption and GitHub Connect license sync (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/viewing-license-usage-for-github-enterprise)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Correct. Pending org invitations, outside collaborators on private repos, enterprise members, and unsynced duplicate emails across GHES/GHEC all impact Enterprise license counts and must be audited regularly.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 34 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). Confirm available GHAS/Secret Protection/Code Security committer seats, create the custom Enterprise Security Configuration, attach it to existing/transferred repos plus new-repo defaults, and set `Enforce configuration`. [Skill 3.1: Define organization and enterprise policies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining organization and enterprise security policies and security configurations (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/about-security-configurations)]

- **A:** Incorrect. GHAS enablement fails if active-committer seats are exhausted, transferred repos require manual attachment, and disabling Actions breaks CodeQL default setup.
- **B:** Correct. Correct rollout: confirm active-committer license headroom, define the custom Security Configuration, apply it to existing/transferred repos and new-repo defaults, and enforce it.
- **C:** Incorrect. Settings left as `Not set` in a Security Configuration are explicitly not enforced against repository overrides.
- **D:** Incorrect. Manual per-repository toggling drifts immediately and misses centralized Security Configurations and enforcement.

### Question 35 — `B, C` (Implement secure software development and compliance)

Correct answers: B and C (are correct). Attach an **Enforced** Enterprise/Org **Security Configuration**, and require **CodeQL**, **Dependabot**, and **Dependency Review** status checks inside enforced **Repository Rulesets**. [Skill 3.1: Define organization and enterprise policies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining organization and enterprise security policies and security configurations (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/about-security-configurations)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Correct. Enforced Security Configurations prevent repository admins from disabling mandatory Secret Protection, CodeQL, or Dependabot controls.
- **C:** Correct. Combining CodeQL semantic analysis, Dependabot remediation PRs, and PR-time Dependency Review stops vulnerable code and packages before merge.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **E:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 36 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Leaving a setting as **`Not set`** (`Keep existing settings`) means that specific feature is **not** locked by enforcement, so repository admins remain free to configure it locally! [Skill 3.1: Define organization and enterprise policies | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining organization and enterprise security policies and security configurations (https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/about-security-configurations)]

- **A:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Correct. Enterprise Policies lock repository creation, forking, visibility changes, and Pages access globally, while enforced Security Configurations standardize GHAS/Dependabot settings across repositories.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 37 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Under `Enterprise -> Policies -> Pages`, disable **Public GitHub Pages** (`restricting Pages sites on private/internal repositories strictly to authenticated access control`)! [Skill 3.2: Strengthen enterprise security posture and data protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Strengthening enterprise security posture, SSH CAs, IP allow lists, and data protection (https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. SSH CAs eliminate unrotated static personal SSH keys by requiring short-lived certificates signed by the corporate CA, paired with IP allow lists (or Entra CAPs).
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 38 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). IP allow list entries accept single IPv4/IPv6 addresses or **`CIDR`** subnet blocks (`e.g., 198.51.100.0/24`), enforced before web, Git, or API traffic reaches private org resources. [Skill 3.2: Strengthen enterprise security posture and data protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Strengthening enterprise security posture, SSH CAs, IP allow lists, and data protection (https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Correct. SSH CAs eliminate unrotated static personal SSH keys by requiring short-lived certificates signed by the corporate CA, paired with IP allow lists (or Entra CAPs).
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 39 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Yes — GHEC EMUs with Entra ID OIDC natively honor **Entra ID Conditional Access Policies (`CAP`)**, centralizing network and device posture checks in the IdP! [Skill 3.2: Strengthen enterprise security posture and data protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Strengthening enterprise security posture, SSH CAs, IP allow lists, and data protection (https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)]

- **A:** Incorrect. Deleting a file in a new commit never purges prior blob SHAs, and any exposed secret must be considered compromised and rotated immediately.
- **B:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.
- **C:** Incorrect. GitHub applies default Security Configurations when a repository is newly created in the org, not when an existing repository is transferred in.
- **D:** Correct. Every technical requirement, permission boundary, and GitHub Enterprise platform rule in the scenario is satisfied cleanly.

### Question 40 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Provision an encrypted Azure Event Hubs / Blob sink, configure sink credentials in Enterprise Audit Log Streaming, verify the test event and enable the Git events toggle, and configure SIEM WORM retention and alerts. [Skill 3.3: Implement audit logging and reporting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Implementing audit logging, audit log streaming, and compliance reporting (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)]

- **A:** Incorrect. Audit log streams support vetted encrypted sinks with strict verification, and audit access should use least-privilege custom roles rather than Enterprise Owner.
- **B:** Incorrect. Audit log streaming is configured at the **Enterprise** level (capturing enterprise and member-organization events), not on an individual repository tab.
- **C:** Incorrect. GitHub retains non-Git audit events in the UI/API for a rolling window (up to 180 days; Git events shorter), so multi-year retention requires Audit Log Streaming.
- **D:** Correct. Correct audit-streaming setup: prepare the target sink, configure credentials in Enterprise Settings -> Audit log -> Log streaming, validate the test check, and enforce SIEM retention/alerting.

### Question 41 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). GitHub automatically retries failed audit-stream deliveries with backoff and pauses/alerts Enterprise Owners by email if the sink stays unreachable for an extended period so admins can fix credentials before retention expires! [Skill 3.3: Implement audit logging and reporting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Implementing audit logging, audit log streaming, and compliance reporting (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)]

- **A:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **B:** Correct. Because UI/REST audit retention is time-bounded (180 days standard; shorter for high-volume Git events), compliance teams stream immutable audit events continuously to external SIEM/WORM storage.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 42 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Passing `include=all` (versus `include=web` or `include=git`) retrieves both web/API administrative events and eligible Git transport events in the response stream. [Skill 3.3: Implement audit logging and reporting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Implementing audit logging, audit log streaming, and compliance reporting (https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)]

- **A:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Correct. Because UI/REST audit retention is time-bounded (180 days standard; shorter for high-volume Git events), compliance teams stream immutable audit events continuously to external SIEM/WORM storage.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 43 — `A, C, E` (Implement secure software development and compliance)

Correct answers: A, C, and E (are correct). Enforce an organization **Security Configuration**, enable **Secret Scanning Push Protection + Partner Validity Checks + Delegated Bypass**, and run **CodeQL + Dependabot security updates + PR Dependency Review**. [Skill 3.4: Configure vulnerability alerts, secret scanning, and CodeQL | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring vulnerability alerts, secret scanning push protection, and CodeQL code scanning (https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)]

- **A:** Correct. Push Protection blocks secrets pre-receive, validity checks highlight live active credentials, and delegated bypass routes false-positive overrides through security reviewers.
- **B:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **C:** Correct. Combining CodeQL semantic analysis, Dependabot remediation PRs, and PR-time Dependency Review stops vulnerable code and packages before merge.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **E:** Correct. Enforced Security Configurations prevent repository admins from disabling mandatory Secret Protection, CodeQL, or Dependabot controls.
- **F:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 44 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). The push remains **blocked** until a member of the designated **Push protection bypass reviewer team/role** reviews the context and approves (or denies) the exemption! [Skill 3.4: Configure vulnerability alerts, secret scanning, and CodeQL | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring vulnerability alerts, secret scanning push protection, and CodeQL code scanning (https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)]

- **A:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Correct. CodeQL analyzes code semantically for CWE/OWASP flaws, while Secret Scanning Push Protection blocks credential commits pre-receive and verifies live token status via partner validity checks.
- **D:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.

### Question 45 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). GitHub securely queries the token provider (`e.g., AWS, Slack, Stripe, GitHub`) to classify each alert as **`Active`** (live exploitable credential — urgent P0!) vs **`Inactive`** (already revoked/expired) or `Unknown`! [Skill 3.4: Configure vulnerability alerts, secret scanning, and CodeQL | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring vulnerability alerts, secret scanning push protection, and CodeQL code scanning (https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **C:** Correct. CodeQL analyzes code semantically for CWE/OWASP flaws, while Secret Scanning Push Protection blocks credential commits pre-receive and verifies live token status via partner validity checks.
- **D:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.

### Question 46 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). The **GitHub Advisory Database** (`github.com/advisories`), combining NVD CVEs with GitHub-reviewed open-source security advisories, powers Dependabot alerts across repositories. [Skill 3.5: Manage Dependabot and security advisories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing Dependabot alerts, security/version updates, private registries, and advisories (https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Correct. Dependabot flags known CVEs, opens automated upgrade PRs (authenticating to private registries when configured), blocks vulnerable PR dependencies via Dependency Review, and pairs with private Security Advisories.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 47 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Specifying `package-ecosystem: "github-actions"` keeps pinned action tags **and even 40-character commit SHAs** (`updating both the SHA and version comment!`) automatically up to date! [Skill 3.5: Manage Dependabot and security advisories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing Dependabot alerts, security/version updates, private registries, and advisories (https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Correct. Dependabot flags known CVEs, opens automated upgrade PRs (authenticating to private registries when configured), blocks vulnerable PR dependencies via Dependency Review, and pairs with private Security Advisories.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 48 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Enable **GitHub Connect** and turn on automatic **GitHub Advisory Database synchronization** (`downloading curated advisory feeds hourly from GitHub.com without sending private source code to the cloud`)! [Skill 3.5: Manage Dependabot and security advisories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing Dependabot alerts, security/version updates, private registries, and advisories (https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Correct. Dependabot flags known CVEs, opens automated upgrade PRs (authenticating to private registries when configured), blocks vulnerable PR dependencies via Dependency Review, and pairs with private Security Advisories.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **D:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.

### Question 49 — `B, D` (Implement secure software development and compliance)

Correct answers: B and D (are correct). Immediately **revoke/rotate** the exposed RDS password (and trigger privacy incident response), then purge `clinical_subjects.csv` across all refs with **`git filter-repo`**, force-push, and ask **GitHub Support** to purge cached views! [Skill 3.6: Define and implement a security response plan | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining a security response plan and purging sensitive data from Git history (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Correct. Publicly or internally pushed secrets can be scraped within seconds by bots or clones; credential revocation/rotation is always step #1.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Correct. `git filter-repo` rewrites Git history cleanly, and GitHub Support purges unreachable commit objects and cached Pull Request diffs on GitHub servers.
- **E:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.

### Question 50 — `A` (Implement secure software development and compliance)

Correct answer: A (is correct). Because `git filter-branch` is slow, error-prone, and officially deprecated by the Git project, whereas **`git filter-repo`** rewrites large histories orders of magnitude faster and cleaner across all refs! [Skill 3.6: Define and implement a security response plan | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining a security response plan and purging sensitive data from Git history (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]

- **A:** Correct. Rewriting Git history never un-compromises an exposed credential; rotation comes first, followed by `git filter-repo`, force-pushing, collaborator re-cloning, and a Support cache purge.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 51 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). No — unreachable commits referenced in Pull Requests can remain accessible via direct SHA URL in server caches; you must open a **GitHub Support** ticket (or run `ghe-repo-gc` on GHES) providing the exact commit SHAs to purge cached views immediately! [Skill 3.6: Define and implement a security response plan | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining a security response plan and purging sensitive data from Git history (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — unreachable commits referenced in Pull Requests can remain accessible via direct SHA URL in server caches; you must open a **GitHub Support** ticket (or run `ghe-repo-gc` on GHES) providing the exact commit SHAs to purge cached views immediately!
- **B:** Correct. Deleting a file in a new commit never purges prior blob SHAs, and any exposed secret must be considered compromised and rotated immediately.
- **C:** Incorrect. Offboarding or suspending inactive accounts reclaims per-user licenses cleanly without breaking repository Git history or compliance review logs.
- **D:** Incorrect. GitHub applies default Security Configurations when a repository is newly created in the org, not when an existing repository is transferred in.

### Question 52 — `A, B` (Implement secure software development and compliance)

Correct answers: A and B (are correct). Block **`PAT (classic)`** access to org resources while enforcing max lifetimes (`<=30–90 days`) and **Owner approval** on **Fine-grained PATs**, and mandate **GitHub Apps** for shared CI/automation integrations. [Skill 3.7: Configure personal access tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring fine-grained and classic Personal Access Token (PAT) enterprise policies (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise)]

- **A:** Correct. GitHub App installations on GHEC provide 3x higher REST throughput, short-lived 1-hour credentials, and complete decoupling from employee turnover.
- **B:** Correct. Enterprise PAT policies replace broad non-expiring classic tokens with short-lived, repo-scoped, admin-approved Fine-grained PATs.
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **E:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 53 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Every **PAT (classic)**—new or existing—is immediately blocked from accessing private/internal organization resources across the enterprise, forcing users onto Fine-grained PATs, GitHub Apps, or SSH! [Skill 3.7: Configure personal access tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring fine-grained and classic Personal Access Token (PAT) enterprise policies (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise)]

- **A:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. Enterprise PAT policies curb broad non-expiring classic PATs and require organization owner approval, repo scoping, and short lifetimes on Fine-grained PATs.

### Question 54 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Enterprise and Organization PAT policies forbid non-expiring Fine-grained PATs and enforce a maximum token lifetime policy (commonly **`30`**, **`60`**, **`90`**, or up to **`365` days**)! [Skill 3.7: Configure personal access tokens | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring fine-grained and classic Personal Access Token (PAT) enterprise policies (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. Enterprise PAT policies curb broad non-expiring classic PATs and require organization owner approval, repo scoping, and short lifetimes on Fine-grained PATs.

### Question 55 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). On **GitHub Enterprise Cloud**, `GITHUB_TOKEN` receives **`15,000` REST requests/hour per repository** (and `15,000` GraphQL points/hour per repository)! [Skill 3.8: Understand rate limits for PATs and GitHub Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Understanding REST and GraphQL API rate limits for PATs, GitHub Apps, and GITHUB_TOKEN (https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api)]

- **A:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. On GHEC, GitHub App installations get 15,000 REST req/hr (and 10,000 GraphQL pts/hr) isolated from human users, whereas user PATs share one 5,000 req/hr personal bucket and hit secondary concurrency caps faster.

### Question 56 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). GraphQL calculates rate limits in **points per hour** (`5,000 points/hr` user; `10,000 points/hr` GHEC App installation) based on query node complexity rather than flat 1-point-per-HTTP-call counting! [Skill 3.8: Understand rate limits for PATs and GitHub Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Understanding REST and GraphQL API rate limits for PATs, GitHub Apps, and GITHUB_TOKEN (https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api)]

- **A:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **B:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. On GHEC, GitHub App installations get 15,000 REST req/hr (and 10,000 GraphQL pts/hr) isolated from human users, whereas user PATs share one 5,000 req/hr personal bucket and hit secondary concurrency caps faster.

### Question 57 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). No — GitHub Docs explicitly note that requests made on a user's behalf by a `15,000`-limit app **reduce the remaining budget** for lower-limit personal tokens (`consuming 8,000 requests exhausts Marco's 5,000 PAT budget until reset`)! [Skill 3.8: Understand rate limits for PATs and GitHub Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Understanding REST and GraphQL API rate limits for PATs, GitHub Apps, and GITHUB_TOKEN (https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api)]

- **A:** Incorrect. Personal-account Team Sync (`Entra ID`/`Okta`) never adds non-members into an organization; users must join the org via SAML/SCIM invitation first (or deploy GHEC with EMUs).
- **B:** Incorrect. Standard hosted runners cannot join customer Azure VNets, and arm64 macOS Larger runners do not support Azure private networking or static IP assignment.
- **C:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — GitHub Docs explicitly note that requests made on a user's behalf by a `15,000`-limit app **reduce the remaining budget** for lower-limit personal tokens (`consuming 8,000 requests exhausts Marco's 5,000 PAT budget until reset`)!
- **D:** Correct. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.

### Question 58 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). Register an org-owned GitHub App with granular permissions, store its `.pem` key in a vault and install on target repos, mint 1-hour installation access tokens via signed JWT, and decommission the machine-user PAT. [Skill 3.9: Describe GitHub Apps and OAuth Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Comparing GitHub Apps, OAuth Apps, deploy keys, and machine users (https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)]

- **A:** Incorrect. OAuth Apps use broad user-tied scopes and long-lived tokens rather than actor-independent 1-hour installation tokens.
- **B:** Incorrect. Machine users consume paid Enterprise seats and share a 5,000 req/hr user rate limit instead of GHEC GitHub App installation scaling (15,000 req/hr).
- **C:** Correct. Correct migration: register a fine-grained GitHub App, safeguard its private key and scope installation repos, mint 1-hour installation tokens via signed JWT, and retire the classic PAT.
- **D:** Incorrect. App `.pem` keys must never be committed, and a GitHub App JWT (max 10 minutes) only authenticates App endpoints to mint a 1-hour installation token.

### Question 59 — `B, D` (Implement secure software development and compliance)

Correct answers: B and D (are correct). Prefer **GitHub Apps** (`1-hour installation tokens, per-repo scoping, 15,000 REST req/hr on GHEC, actor-independent`), and enforce **Fine-grained PAT** approval + classic PAT blocks. [Skill 3.9: Describe GitHub Apps and OAuth Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Comparing GitHub Apps, OAuth Apps, deploy keys, and machine users (https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Correct. GitHub App installations on GHEC provide 3x higher REST throughput, short-lived 1-hour credentials, and complete decoupling from employee turnover.
- **C:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **D:** Correct. Enterprise PAT policies replace broad non-expiring classic tokens with short-lived, repo-scoped, admin-approved Fine-grained PATs.
- **E:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 60 — `C` (Implement secure software development and compliance)

Correct answer: C (is correct). The **GitHub App** continues running with **zero interruption** because installation access tokens belong to the App installation on the organization, not to any individual human user! [Skill 3.9: Describe GitHub Apps and OAuth Apps | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Comparing GitHub Apps, OAuth Apps, deploy keys, and machine users (https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)]

- **A:** Incorrect. Once SAML SSO is enforced on a personal-account organization, existing classic PATs and SSH keys must be explicitly authorized for SAML SSO or API/Git calls fail with 403.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. GitHub Apps survive employee offboarding, consume zero user seats, grant fine-grained repo/resource permissions, and use short-lived tokens—outperforming both OAuth Apps and seat-consuming machine users.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 61 — `B` (Implement secure software development and compliance)

Correct answer: B (is correct). Under `Organization Settings -> Third-party Access` (`GitHub Apps` -> installation requests, and `OAuth application policy`), Owners review requested permissions/repositories and approve or deny each app! [Skill 3.10: Approve or deny app usage based on policy | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Approving, denying, and governing OAuth Apps and GitHub App installations (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Correct. With OAuth App access restrictions active, unapproved third-party OAuth apps can read public data only and cannot touch organization private repos until an Owner explicitly approves the request.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 62 — `D` (Implement secure software development and compliance)

Correct answer: D (is correct). Enforce **OAuth application policy** at the Enterprise level (`or audit org.disable_oauth_app_restrictions`), ensuring third-party OAuth apps stay restricted across all member organizations! [Skill 3.10: Approve or deny app usage based on policy | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Approving, denying, and governing OAuth Apps and GitHub App installations (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Correct. With OAuth App access restrictions active, unapproved third-party OAuth apps can read public data only and cannot touch organization private repos until an Owner explicitly approves the request.

### Question 63 — `D, E` (Manage GitHub Actions)

Correct answers: D and E (are correct). Publish actions/workflows inside **`Internal`** repositories with enterprise workflow `Access` enabled, and enforce **40-character SHA pinning** + `Read-only` `GITHUB_TOKEN` defaults. [Skill 4.1: Configure and manage reuse of actions and workflows to the enterprise repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Sharing reusable workflows and actions privately across enterprise organizations (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. 40-char SHA pinning neutralizes upstream tag hijacking while read-only `GITHUB_TOKEN` defaults enforce job-level least privilege.
- **E:** Correct. Enterprise teams reuse vetted CI/CD templates privately across all member organizations without exposing proprietary workflows publicly.

### Question 64 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). Yes — on GitHub Enterprise, `Private` repositories also support setting `Settings -> Actions -> General -> Access` to **`Accessible from repositories in the '<Enterprise>' enterprise`** (while controlling human code readers separately)! [Skill 4.1: Configure and manage reuse of actions and workflows to the enterprise repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Sharing reusable workflows and actions privately across enterprise organizations (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Correct. Without publishing proprietary actions to the public internet, enterprises host golden `workflow_call` workflows and actions inside `Internal`/`Private` repos with cross-repo enterprise workflow access enabled.
- **B:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **C:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 65 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Declare explicit named inputs under `jobs.<job_id>.____:` in the caller workflow matching `on.workflow_call.secrets:` in the reusable workflow (`passing only the exact secrets that workflow needs`)! [Skill 4.1: Configure and manage reuse of actions and workflows to the enterprise repository | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Sharing reusable workflows and actions privately across enterprise organizations (https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/sharing-actions-and-workflows-with-your-enterprise)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Correct. Without publishing proprietary actions to the public internet, enterprises host golden `workflow_call` workflows and actions inside `Internal`/`Private` repos with cross-repo enterprise workflow access enabled.
- **C:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **D:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.

### Question 66 — `B, D` (Manage GitHub Actions)

Correct answers: B and D (are correct). Enforce **`Require actions to be pinned to a full-length commit SHA`** + `Read-only` `GITHUB_TOKEN` + fork PR approval gates, and isolate privileged runners in restricted **Runner Groups**. [Skill 4.2: Apply organizational policies for GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing enterprise and organization GitHub Actions policies and SHA pinning (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Correct. Runner group repository and workflow restrictions prevent untrusted repos or ad-hoc branches from scheduling jobs onto privileged runners.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Correct. 40-char SHA pinning neutralizes upstream tag hijacking while read-only `GITHUB_TOKEN` defaults enforce job-level least privilege.
- **E:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 67 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Select **`Require approval for all external contributors`** so even repeat external contributors cannot execute modified workflow steps until a maintainer reviews the diff and selects `Approve and run`! [Skill 4.2: Apply organizational policies for GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing enterprise and organization GitHub Actions policies and SHA pinning (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Correct. Pinning third-party actions to immutable 40-char commit SHAs blocks tag-mutation supply-chain attacks, while `permissions: read-all` / read-only `GITHUB_TOKEN` defaults enforce least privilege.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 68 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). Only Actions matching `heliobio-sec/*` or `aws-actions/configure-aws-credentials` that are pinned to an exact **40-character commit SHA** (`e.g., aws-actions/configure-aws-credentials@e3dd6a429d7300a6a4c196c26e071d42e0343502`)! [Skill 4.2: Apply organizational policies for GitHub Actions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Enforcing enterprise and organization GitHub Actions policies and SHA pinning (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise)]

- **A:** Correct. Pinning third-party actions to immutable 40-char commit SHAs blocks tag-mutation supply-chain attacks, while `permissions: read-all` / read-only `GITHUB_TOKEN` defaults enforce least privilege.
- **B:** Incorrect. Maintenance mode pauses normal user writes and active traffic safely during GHES upgrades or snapshot restores while preserving admin SSH access.
- **C:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 69 — `A, B, C` (Manage GitHub Actions)

Correct answers: A, B, and C (are correct). Group runners into repository/workflow-restricted **Runner Groups**, wire Larger runners to **Azure Private Networking** (`VNet`), and enforce **full-SHA action pinning** + `Read-only` `GITHUB_TOKEN`. [Skill 4.3: Manage runner groups and administer GitHub-hosted vs. self-hosted runner options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing runner groups, Larger runners, self-hosted runners, and Actions Runner Controller (ARC) (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Correct. 40-char SHA pinning neutralizes upstream tag hijacking while read-only `GITHUB_TOKEN` defaults enforce job-level least privilege.
- **B:** Correct. Runner group repository and workflow restrictions prevent untrusted repos or ad-hoc branches from scheduling jobs onto privileged runners.
- **C:** Correct. Azure Private Networking gives managed GitHub-hosted Larger runners private VNet egress to internal endpoints and predictable firewall/NAT egress IPs.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **E:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **F:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 70 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). First, the Enterprise Owner grants **`Selected organizations`** (`@heliobio-genomics`) access to the Enterprise Runner Group; second, the `@heliobio-genomics` Organization Owner scopes which **`Selected repositories`** inside that org may use it! [Skill 4.3: Manage runner groups and administer GitHub-hosted vs. self-hosted runner options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing runner groups, Larger runners, self-hosted runners, and Actions Runner Controller (ARC) (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Correct. Runner groups isolate sensitive self-hosted or Larger runners to approved repositories and reusable workflow refs, while `--ephemeral` JIT / ARC pods ensure clean single-job runner state.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.

### Question 71 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). It is **disabled by default** because allowing `Public` repositories onto self-hosted runners lets external fork PRs (`especially pull_request_target` or misconfigured triggers) compromise internal hosts and networks! [Skill 4.3: Manage runner groups and administer GitHub-hosted vs. self-hosted runner options | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Managing runner groups, Larger runners, self-hosted runners, and Actions Runner Controller (ARC) (https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups)]

- **A:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. Runner groups isolate sensitive self-hosted or Larger runners to approved repositories and reusable workflow refs, while `--ephemeral` JIT / ARC pods ensure clean single-job runner state.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 72 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Delegate an Azure VNet subnet to `GitHub.Network` and create `NetworkSettings`, create a GitHub Network Configuration, attach it to the Linux Larger runner group, and restrict the runner group to approved repos/workflows. [Skill 4.4: Apply IP allow lists and configure networking (including Azure private networking) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring IP allow lists, proxies, and Azure private networking (VNet) for runners (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization)]

- **A:** Incorrect. Azure private networking requires Linux/Windows Larger runners (not macOS arm64 larger runners), subnet delegation, and strict runner-group access controls.
- **B:** Correct. Correct sequence: prepare the delegated Azure VNet + `GitHub.Network/networkSettings` resource, register the GitHub Network Configuration, bind it to a Larger runner group, and restrict repo/workflow access.
- **C:** Incorrect. Standard Linux runners use a multi-cloud pool beyond Azure IPs, and VNet-integrated runners still require outbound access to required GitHub endpoints.
- **D:** Incorrect. By default Enterprise policy restricts org-created Network Configurations unless enabled by an Enterprise Owner, and Azure NetworkSettings linkage is mandatory.

### Question 73 — `C, D` (Manage GitHub Actions)

Correct answers: C and D (are correct). By default orgs inherit enterprise **Network Configurations** (unless Enterprise policy explicitly permits org-level configs), and **Linux/Windows Larger runners** attach to Azure VNets inside restricted **Runner Groups**! [Skill 4.4: Apply IP allow lists and configure networking (including Azure private networking) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring IP allow lists, proxies, and Azure private networking (VNet) for runners (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **C:** Correct. Runner group repository and workflow restrictions prevent untrusted repos or ad-hoc branches from scheduling jobs onto privileged runners.
- **D:** Correct. Azure Private Networking gives managed GitHub-hosted Larger runners private VNet egress to internal endpoints and predictable firewall/NAT egress IPs.
- **E:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 74 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). No — **Azure Private Networking** (`VNet` integration) and static IP ranges require **Linux or Windows Larger GitHub-hosted runners** inside a Runner Group (`standard ubuntu-latest runners use a shared multi-cloud pool`)! [Skill 4.4: Apply IP allow lists and configure networking (including Azure private networking) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring IP allow lists, proxies, and Azure private networking (VNet) for runners (https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization)]

- **A:** Correct. Standard hosted runners cannot join customer Azure VNets, and arm64 macOS Larger runners do not support Azure private networking or static IP assignment.
- **B:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — **Azure Private Networking** (`VNet` integration) and static IP ranges require **Linux or Windows Larger GitHub-hosted runners** inside a Runner Group (`standard ubuntu-latest runners use a shared multi-cloud pool`)!
- **C:** Incorrect. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.
- **D:** Incorrect. Generating five separate PATs under the same user account still draws from the same single 5,000 requests/hour authenticated-user bucket.

### Question 75 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Inspect **`_diag/Worker_<timestamp>.log`** on the runner host (`Worker_*.log` records each dispatched job's execution process, whereas `Runner_*.log` records the background listener daemon). [Skill 4.5: Monitor and troubleshoot runner performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring and troubleshooting runner _diag logs, queues, and performance (https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Correct. `Runner_*.log` records control-plane polling/TLS/proxy failures on the self-hosted agent, whereas `Worker_*.log` captures per-job execution details when jobs fail or stall.
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 76 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Check **`Enable debug logging`** when re-running the job (or set secrets/vars **`ACTIONS_STEP_DEBUG=true`** and **`ACTIONS_RUNNER_DEBUG=true`**) to emit detailed runner and step diagnostic traces! [Skill 4.5: Monitor and troubleshoot runner performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring and troubleshooting runner _diag logs, queues, and performance (https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **C:** Correct. `Runner_*.log` records control-plane polling/TLS/proxy failures on the self-hosted agent, whereas `Worker_*.log` captures per-job execution details when jobs fail or stall.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 77 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). Inspect **Actions Performance Metrics -> Queue time** alongside `ARC` controller pod logs / `maxRunners` concurrency limits, and raise `maxRunners` (plus split slow matrix steps or cache datasets)! [Skill 4.5: Monitor and troubleshoot runner performance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Monitoring and troubleshooting runner _diag logs, queues, and performance (https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners)]

- **A:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **B:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **C:** Correct. `Runner_*.log` records control-plane polling/TLS/proxy failures on the self-hosted agent, whereas `Worker_*.log` captures per-job execution details when jobs fail or stall.
- **D:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!

### Question 78 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). Workflows triggered by **Dependabot** do **not** receive standard `Actions` secrets; secrets required by Dependabot runs must be stored explicitly under **`Settings -> Secrets and variables -> Dependabot`**! [Skill 4.6: Define scope and access for secrets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining secret scope, hierarchy precedence, and deployment environment access controls (https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Correct. Production cloud secrets belong in protected Deployment Environments (`environment: production`) gated by human/custom deployment protection rules and branch filters, overriding broader repo/org secrets.

### Question 79 — `C` (Manage GitHub Actions)

Correct answer: C (is correct). No — Repository secrets override Organization secrets (`Environment > Repository > Organization`); delete the stale Repository-level `SIGNING_KEY_ID` in `heliobio/lims` so it inherits the Organization secret! [Skill 4.6: Define scope and access for secrets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining secret scope, hierarchy precedence, and deployment environment access controls (https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. The proposed configuration fails at least one stated GitHub Enterprise identity, security, or administration rule. No — Repository secrets override Organization secrets (`Environment > Repository > Organization`); delete the stale Repository-level `SIGNING_KEY_ID` in `heliobio/lims` so it inherits the Organization secret!
- **B:** Incorrect. Offboarding or suspending inactive accounts reclaims per-user licenses cleanly without breaking repository Git history or compliance review logs.
- **C:** Correct. Whenever an Environment or Repository defines a secret with the identical name as an Organization secret, the narrower Environment/Repository value wins at runtime.
- **D:** Incorrect. Standard hosted runners cannot join customer Azure VNets, and arm64 macOS Larger runners do not support Azure private networking or static IP assignment.

### Question 80 — `D` (Manage GitHub Actions)

Correct answer: D (is correct). No — GitHub masks exact registered secret values (and common derived encodings best-effort), **not** arbitrary transformations; forbid printing derived secret outputs and restrict write/PR workflow modifications via Rulesets! [Skill 4.6: Define scope and access for secrets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Defining secret scope, hierarchy precedence, and deployment environment access controls (https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)]

- **A:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Correct. Production cloud secrets belong in protected Deployment Environments (`environment: production`) gated by human/custom deployment protection rules and branch filters, overriding broader repo/org secrets.

### Question 81 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). GitHub supports up to **`1,000` Organization secrets** and **`100` Repository secrets** (`plus 100 per Environment`), and secrets are write-only in the UI/REST API (`GET` returns only metadata `name`/`updated_at`, never plaintext)! [Skill 4.7: Configure secrets at organization and repository levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization and repository encrypted secrets and variables via UI and REST API (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/creating-secrets-for-an-organization)]

- **A:** Correct. Organization secrets never pass to public repos unless explicitly permitted, API writes require LibSodium sealed-box encryption (`48 KB` max per secret), and plain-text config belongs in `vars` context.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.

### Question 82 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Move non-sensitive configuration parameters into **Actions Configuration Variables (`vars.ARTIFACTORY_HOST`)** so values remain readable in UI and build logs! [Skill 4.7: Configure secrets at organization and repository levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization and repository encrypted secrets and variables via UI and REST API (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/creating-secrets-for-an-organization)]

- **A:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **B:** Correct. Organization secrets never pass to public repos unless explicitly permitted, API writes require LibSodium sealed-box encryption (`48 KB` max per secret), and plain-text config belongs in `vars` context.
- **C:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 83 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). That newly `Public` repository **immediately loses access** to all `Private and internal` Organization secrets, preventing accidental exposure in public workflow runs! [Skill 4.7: Configure secrets at organization and repository levels | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Configuring organization and repository encrypted secrets and variables via UI and REST API (https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/creating-secrets-for-an-organization)]

- **A:** Incorrect. A Deploy key grants SSH access strictly to one repository, whereas multi-repo CI/CD automation should use a GitHub App installation token rather than managing dozens of SSH keys.
- **B:** Correct. Organization secrets never pass to public repos unless explicitly permitted, API writes require LibSodium sealed-box encryption (`48 KB` max per secret), and plain-text config belongs in `vars` context.
- **C:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 84 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). Configure an Entra ID Federated Identity Credential with strict `sub`/`aud` claims, set job `permissions: id-token: write`, authenticate via `azure/login` OIDC JWT to fetch Key Vault secrets at runtime, and delete static GitHub secrets. [Skill 4.8: Integrate third-party vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Integrating third-party secret vaults (HashiCorp Vault, Azure Key Vault, AWS) via OIDC (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Correct. Correct passwordless vault flow: lock down cloud/vault OIDC subject claims first, grant `id-token: write`, exchange the ephemeral OIDC token at runtime, and remove static secrets.
- **B:** Incorrect. Wildcard `repo:*` subject claims let any GitHub repository assume your cloud role, and `id-token: write` is required to request an OIDC token.
- **C:** Incorrect. The external vault/cloud IdP must trust `https://token.actions.githubusercontent.com` and exact subject claims before OIDC exchange can succeed.
- **D:** Incorrect. Storing static admin keys in repositories creates catastrophic credential exposure instead of ephemeral OIDC federation.

### Question 85 — `B` (Manage GitHub Actions)

Correct answer: B (is correct). Customize the **Organization/Repository OIDC subject (`sub`) claim template** (`PUT /orgs/{org}/actions/oidc/customization/sub`) to enforce rich, unforgeable identity claims (`such as job_workflow_ref`)! [Skill 4.8: Integrate third-party vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Integrating third-party secret vaults (HashiCorp Vault, Azure Key Vault, AWS) via OIDC (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!
- **B:** Correct. OIDC exchanges a job-scoped JWT signed by `https://token.actions.githubusercontent.com` for short-lived dynamic vault credentials at runtime—eliminating static secrets stored in GitHub.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.

### Question 86 — `A` (Manage GitHub Actions)

Correct answer: A (is correct). Binding Vault's role policy to **`job_workflow_ref`** (alongside `repository_owner: heliobio`) ensures ad-hoc feature-branch YAML edits cannot impersonate the approved deployment workflow! [Skill 4.8: Integrate third-party vaults | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Integrating third-party secret vaults (HashiCorp Vault, Azure Key Vault, AWS) via OIDC (https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)]

- **A:** Correct. OIDC exchanges a job-scoped JWT signed by `https://token.actions.githubusercontent.com` for short-lived dynamic vault credentials at runtime—eliminating static secrets stored in GitHub.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Incorrect. Using `repo:*` without scoping to your exact `<org>/<repo>` and `<environment>` lets any external GitHub user’s repository assume your cloud credentials!

### Question 87 — `D, E` (Monitor and optimize GitHub usage)

Correct answers: D and E (are correct). Inspect **Organization API Insights** alongside **Enterprise Audit Log `hashed_token`** filters, and stream **Enterprise Audit Logs** (including API/Git telemetry) to your SIEM. [Skill 5.1: Analyze audit logs and API usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Analyzing enterprise audit logs, Git events, and API Insights / REST/GraphQL metrics (https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-your-team/apicenter/viewing-api-insights-for-your-organization)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Correct. Continuous Audit Log Streaming preserves tamper-evident compliance records far beyond GitHub’s interactive 180-day UI retention window.
- **E:** Correct. API Insights pinpoints which App or PAT user is exhausting rate limits while Audit Log `hashed_token` traces exact administrative/API actions.

### Question 88 — `B` (Monitor and optimize GitHub usage)

Correct answer: B (is correct). Replace tight REST polling loops with event-driven **Repository/Organization Webhooks** (`pull_request` event) — or attach `If-None-Match` (`ETag`) headers so unchanged `304 Not Modified` responses consume **zero** primary rate-limit quota! [Skill 5.1: Analyze audit logs and API usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Analyzing enterprise audit logs, Git events, and API Insights / REST/GraphQL metrics (https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-your-team/apicenter/viewing-api-insights-for-your-organization)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Correct. API Insights visualizes hourly/daily REST consumption and `403`/`429` rate-limit hits broken down by specific App or PAT user so admins fix runaway polling loops quickly.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 89 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). Querying the **`rateLimit`** field inside any GraphQL request returns `cost`, `remaining`, `limit`, and `resetAt` in a single round trip! [Skill 5.1: Analyze audit logs and API usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Analyzing enterprise audit logs, Git events, and API Insights / REST/GraphQL metrics (https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-your-team/apicenter/viewing-api-insights-for-your-organization)]

- **A:** Correct. API Insights visualizes hourly/daily REST consumption and `403`/`429` rate-limit hits broken down by specific App or PAT user so admins fix runaway polling loops quickly.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.

### Question 90 — `D` (Monitor and optimize GitHub usage)

Correct answer: D (is correct). The GHES **Management Console** listens on HTTPS port **`8443`** (`https://<hostname>:8443`, protected by a separate Management Console root/operator password), while administrative SSH listens on port **`122`**! [Skill 5.2: Distinguish admin responsibilities vs. GitHub Support and generate diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Distinguishing admin vs GitHub Support responsibilities and generating appliance/cloud diagnostics (https://docs.github.com/en/enterprise-server@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/activity-dashboard)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **C:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **D:** Correct. Admins first inspect `githubstatus.com`, SAML/webhook delivery logs, and `ghe-diagnostics` CPU/memory/queue health, escalating to GitHub Support via entitled Enterprise Support members with bundles attached.

### Question 91 — `D` (Monitor and optimize GitHub usage)

Correct answer: D (is correct). Enable **Log forwarding (`syslog` over TLS/UDP/TCP)** in the GHES Management Console (`paired with Prometheus /metrics or SNMP monitoring`)! [Skill 5.2: Distinguish admin responsibilities vs. GitHub Support and generate diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Distinguishing admin vs GitHub Support responsibilities and generating appliance/cloud diagnostics (https://docs.github.com/en/enterprise-server@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/activity-dashboard)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **D:** Correct. GHES exposes native Prometheus metrics, SNMP, and syslog forwarding so enterprise monitoring stacks catch resource pressure before outages occur.

### Question 92 — `D` (Monitor and optimize GitHub usage)

Correct answer: D (is correct). **`Urgent`** priority applies when your production GitHub Enterprise environment is **down, inaccessible, severely degraded, or experiencing an active critical security breach** (`whereas general how-to configuration questions belong at Low/Normal`)! [Skill 5.2: Distinguish admin responsibilities vs. GitHub Support and generate diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Distinguishing admin vs GitHub Support responsibilities and generating appliance/cloud diagnostics (https://docs.github.com/en/enterprise-server@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/activity-dashboard)]

- **A:** Incorrect. GitHub Support never logs directly into customer GHES appliances over SSH; administrators generate and upload `ghe-support-bundle` archives instead.
- **B:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Correct. Admins first inspect `githubstatus.com`, SAML/webhook delivery logs, and `ghe-diagnostics` CPU/memory/queue health, escalating to GitHub Support via entitled Enterprise Support members with bundles attached.

### Question 93 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). The GHES **Activity dashboard** (`/dashboard` / Site Admin **Reports** CSV exports for `All users`, `Active users`, `Dormant users`, and `Suspended users`) tracks adoption and idle assets across the appliance! [Skill 5.3: Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Evaluating enterprise adoption, Copilot/Actions metrics, and dormant or underutilized features (https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api)]

- **A:** Correct. Comparing assigned seats against 7/28/90-day active usage across Copilot, GHAS Security Overview, and Actions workflows highlights teams needing enablement or license reclamation.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.
- **D:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 94 — `D` (Monitor and optimize GitHub usage)

Correct answer: D (is correct). Use the **Enterprise/Organization Copilot Usage Dashboard** and **Copilot Metrics REST API** (`/enterprises/{enterprise}/copilot/metrics`), which report privacy-preserving aggregated adoption and language metrics (for cohorts with `>=5` active users)! [Skill 5.3: Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Evaluating enterprise adoption, Copilot/Actions metrics, and dormant or underutilized features (https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **C:** Incorrect. Self-hosted runners read `https_proxy` and `no_proxy` from their `.env` file (or service environment) to establish outbound HTTPS long-polling (`port 443`) to GitHub Actions.
- **D:** Correct. Tracking `last_activity_at` per Copilot seat lets enterprise admins automatically reclaim unused seats after a defined inactivity window (e.g., 30–60 days).

### Question 95 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). Open **Enterprise Security Overview -> Coverage**, which displays exact repository percentages with `Code scanning`, `Secret scanning`, `Push protection`, and `Dependabot` enabled per organization! [Skill 5.3: Evaluate enterprise usage patterns to identify adoption, activity, and underutilized features | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Evaluating enterprise adoption, Copilot/Actions metrics, and dormant or underutilized features (https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api)]

- **A:** Correct. Security Overview aggregates alert risk, push-protection metrics, and tool coverage across thousands of repositories for CISOs and Security Managers.
- **B:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **C:** Incorrect. Attaching persistent internal self-hosted runners to public repositories allows untrusted external fork PR modifications to execute arbitrary code inside your corporate network!
- **D:** Incorrect. Mutable Git tags like `@v1` can be force-moved by a compromised upstream publisher; strict enterprise policy pins third-party actions to full 40-character commit SHAs.

### Question 96 — `B, D` (Monitor and optimize GitHub usage)

Correct answers: B and D (are correct). Reclaim **dormant seats / stale invitations** and audit **90-day unique GHAS committers**, while grouping orgs into **Cost Centers** with **Budgets**, dependency caching, short artifact retention, and `ubuntu` runner defaults. [Skill 5.4: Interpret usage reports for metered products | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Interpreting metered usage reports, spending limits, and cost centers for Actions, Packages, GHAS & Copilot (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-billing/using-the-billing-platform)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Correct. Cost Centers and Budgets enforce FinOps accountability while caching, shorter artifact retention, and right-sized OS runners cut metered overages.
- **C:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **D:** Correct. Proactive seat hygiene reclaims idle Enterprise, Copilot, and GHAS licenses before renewal or monthly metered billing cycles.
- **E:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.

### Question 97 — `C` (Monitor and optimize GitHub usage)

Correct answer: C (is correct). Once `100%` of an enforced hard-stop budget is reached, additional metered Actions runs or new Codespace launches in that scope pause (`blocking runaway spend`) while firing `75%`, `90%`, and `100%` email alerts to budget owners! [Skill 5.4: Interpret usage reports for metered products | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Interpreting metered usage reports, spending limits, and cost centers for Actions, Packages, GHAS & Copilot (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-billing/using-the-billing-platform)]

- **A:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
- **B:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **C:** Correct. Metered billing tracks included enterprise quotas first (for standard hosted runners and Packages/Artifacts storage) and bills overages or Larger runners/Copilot/GHAS against assigned Cost Centers and Budgets.
- **D:** Incorrect. GitHub’s interactive Audit Log UI retains events for a bounded rolling window (180 days), not 7 years; long-term retention requires Audit Log Streaming to WORM/SIEM storage.

### Question 98 — `D` (Monitor and optimize GitHub usage)

Correct answer: D (is correct). **GitHub Actions** (`build artifacts and caches`) and **GitHub Packages** (`container/npm/Maven/NuGet packages`) share the Enterprise account's included storage and data transfer pool! [Skill 5.4: Interpret usage reports for metered products | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Interpreting metered usage reports, spending limits, and cost centers for Actions, Packages, GHAS & Copilot (https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-billing/using-the-billing-platform)]

- **A:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **B:** Incorrect. `vars.*` stores unmasked plain-text configuration visible in logs and UI; sensitive credentials must use encrypted `secrets.*` or ephemeral OIDC vaults.
- **C:** Incorrect. In standard GHEC without EMUs, users own their personal GitHub.com accounts and authorize access to enterprise organizations through SAML SSO.
- **D:** Correct. Metered billing tracks included enterprise quotas first (for standard hosted runners and Packages/Artifacts storage) and bills overages or Larger runners/Copilot/GHAS against assigned Cost Centers and Budgets.

### Question 99 — `A` (Monitor and optimize GitHub usage)

Correct answer: A (is correct). For `HelioBio`'s hybrid true-up, export consumed-licenses and verify GitHub Connect GHES email deduplication first, audit dormant lab users/90-day GHAS committers, reclaim idle seats and right-size storage budgets, and enforce SCIM offboarding + cost alerts. [Skill 5.5: Recommend strategies for license and resource optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending strategies for dormant seat reclamation, caching, and runner/storage cost optimization (https://docs.github.com/en/enterprise-server@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/managing-dormant-users)]

- **A:** Correct. Correct optimization loop: inspect unified license data, pinpoint duplicate identities/dormant users/GHAS committers, reclaim unused seats and cap metered budgets, and automate SCIM hygiene.
- **B:** Incorrect. Admins remove/suspend org or EMU memberships (preserving PR/commit audit trails) rather than deleting security controls.
- **C:** Incorrect. macOS hosted runners carry a higher per-minute cost than Linux runners, long artifact retention inflates storage charges, and unmonitored seat grants waste licenses.
- **D:** Incorrect. GHAS seats release automatically 90 days after a user’s last push (or when GHAS is disabled on the repo), and disabling GitHub Connect causes double-billing across GHEC and GHES.

### Question 100 — `C` (Monitor and optimize GitHub usage)

Correct answer: C (is correct). Set **`retention-days: 5`** (or configure an Organization/Enterprise maximum **Artifact and log retention** policy of `7–14` days) so ephemeral test artifacts expire automatically! [Skill 5.5: Recommend strategies for license and resource optimization | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100 | Reference: Recommending strategies for dormant seat reclamation, caching, and runner/storage cost optimization (https://docs.github.com/en/enterprise-server@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/managing-dormant-users)]

- **A:** Incorrect. GHAS licenses are consumed strictly by **unique active committers** who pushed commits to at least one GHAS-enabled private/internal repository within the past **90 days**.
- **B:** Incorrect. `macos` hosted runners carry up to a 10x higher per-minute billing rate than `ubuntu-latest` Linux runners and lack native Linux kernel container execution.
- **C:** Correct. Suspending dormant users, cancelling expired invitations, syncing GHEC+GHES via GitHub Connect, trimming artifact retention (`retention-days: 7`), and moving non-Apple jobs off macOS runners cut spend immediately.
- **D:** Incorrect. Enabling **GitHub Connect** license sync deduplicates users matching verified emails across GHEC and GHES so each unique human consumes only one Enterprise seat.
