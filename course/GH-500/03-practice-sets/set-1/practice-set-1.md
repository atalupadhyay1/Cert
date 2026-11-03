# Microsoft / GitHub Exam GH-500: GitHub Advanced Security — Full-Length Mock Exam 1

**Theme:** Security Suites Ecosystem, Security Overview, Prevention-First SDLC & Alert Governance  
**Credential:** `GitHub Advanced Security` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `July 2026 (Last updated May 14, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-500 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Advanced Security documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Describe GitHub Security suites, features, and ecosystem (15–20% official weight · 18 questions)

### 1. CinderVault Payments runs 45 private repositories on a `GitHub Team` plan (`vault-ledger-api`, `ach-wire-gateway`) and wants Push Protection immediately without upgrading the entire company to GitHub Enterprise or buying SAST seats yet. How are GitHub Security SKUs structured for this need?

- **A.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Standalone `GitHub Secret Protection` and `GitHub Code Security` SKUs (`purchasable separately or together on GitHub Team and GitHub Enterprise`, alongside legacy bundled GHAS)
- **D.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses

### 2. A new PCI-DSS auditor at CinderVault Payments asks which GitHub Security pillar covers leaked Stripe API tokens, custom SQL injection flaws in `card-token-vault`, and vulnerable npm packages in `kyc-onboarding-portal`. How do the three pillars map to those risks?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** `Secret Protection` (`secret scanning + push protection`), `Code Security` (`CodeQL/SARIF SAST + Copilot Autofix`), and `Supply Chain Security` (`Dependency Graph, Dependabot, Dependency Review & SBOMs`)
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 3. CinderVault Payments is splitting its FY27 AppSec budget between standalone `GitHub Secret Protection` and `GitHub Code Security` licenses across private settlement microservices. Which capabilities belong to each respective SKU? Select two.

- **A.** `GitHub Secret Protection` prevents and detects leaked credentials via `Push Protection`, `secret scanning`, `validity checks`, custom patterns, and AI generic secret detection
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** `GitHub Code Security` finds and fixes code and dependency risks via `CodeQL` / `SARIF` code scanning, `Copilot Autofix`, `Dependency Review` on private repos, and `Security Campaigns`
- **E.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 4. CinderVault Payments maintains an open-source SDK (`cindervault-js-sdk`) in a public GitHub.com repository alongside 80 private ledger repositories. Which security capabilities run free on the public SDK repository versus requiring paid SKUs on private repositories?

- **A.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Core features (`secret scanning, push protection, Dependency Graph, Dependabot, CodeQL default setup & Dependency Review`) are free on `public` GitHub.com repos; `private/internal` repos require licensed SKUs where applicable

### 5. CinderVault Payments' VP of Security needs a single organization plane showing enablement gaps across 120 payment repositories, open risk trends filtered by custom property `pci_scope:cde`, and active remediation sprint progress. Which native hub should they open (`Organization -> Security -> ____`)?

- **A.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **B.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`
- **C.** `Security Overview` (`Organization & Enterprise Risk, Coverage, Campaigns, Code scanning, Secret scanning & Dependabot dashboards` filterable by team, topic, or custom property)
- **D.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations

### 6. Before purchasing committer seats for CinderVault Payments' subsidiary org, the CISO wants empirical baseline counts of leaked credentials across private repos and sample CodeQL findings. Which built-in Organization Security Overview option provides this pre-purchase visibility (`____`)?

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Organization `free security risk assessment` (`scanning org repos for leaked secrets and up to 20 active repositories for CodeQL vulnerabilities + Copilot Autofix preview`)

### 7. During an incident review on `merchant-webhook-relay`, an engineer asks why Secret Protection flagged an HMAC key inside a `.properties` file while CodeQL flagged a cleartext password variable passed into a custom crypto cipher in `.java` code. What explains the interplay between the two suites?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** `Secret Protection` matches structured/high-entropy/AI secret tokens across Git history & pushes, whereas `Code Security (CodeQL)` traces semantic AST/dataflow vulnerabilities (`including hardcoded-credential sinks`)
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 8. CinderVault Payments must block developers from pushing live acquiring-bank keys to `ach-wire-gateway` before commits enter Git history and also detect SSRF flaws on pull requests. Proposed solution: Commit `.github/secret_scanning.yml` with `paths-ignore: ["src/**"]` while leaving Push Protection and CodeQL disabled. Does this meet the goal?

- **A.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **B.** No — `.github/secret_scanning.yml` `paths-ignore` only auto-closes post-push user alerts (`<=1,000` paths / `<=1 MB`) and neither revokes keys nor replaces Push Protection / public partner alerts
- **C.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)
- **D.** No — `actions/dependency-review-action` forbids specifying `allow-licenses` and `deny-licenses` together, and fails to block merges unless marked as a required status check on `pull_request`

### 9. CinderVault Payments wants Secret Protection, Supply Chain Security, and Code Security working together on every developer pull request to `settlement-reconciler` before code reaches `main`. Which combined control pattern achieves full-lifecycle coverage?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Layer `Push Protection` (`pre-receive`), `actions/dependency-review-action` (`PR manifest/license gate`), and `CodeQL` PR checks (`with Copilot Autofix`) so secrets, vulnerable packages, and taint flaws fail pre-merge
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 10. CinderVault Payments is replacing a quarterly pre-release penetration-test bottleneck on `vault-ledger-api` with a prevention-first secure SDLC across GitHub Security suites. In which chronological order should controls execute from local push through post-merge monitoring?

- **A.** Apply Copilot Autofix before running CodeQL → run Push Protection only after merging to main → skip Dependency Review on lockfiles → delete Security Overview roles
- **B.** Dismiss all PR alerts automatically → merge vulnerable dependencies → run Dependency Review only on archived branches → rely on gitignore to revoke leaked API tokens
- **C.** Block secrets pre-receive via Push Protection → run Dependency Review & CodeQL on the PR → apply Copilot Autofix or patch vulnerable packages before merge → monitor default-branch advisories in Security Overview
- **D.** Merge PRs without checks to main → run weekly manual secret scans → disable Push Protection to avoid developer friction → export CSVs quarterly without remediating open alerts

### 11. Historically, CinderVault Payments ran a single SAST gate 24 hours before quarterly PCI releases, forcing emergency hotfixes across 30 merged feature branches. Why does GitHub recommend a prevention-first strategy over late gate-only checks?

- **A.** Prevention-first (`Push Protection + IDE/PR Dependency Review + PR CodeQL with Copilot Autofix`) stops defects before Git history/merge, whereas late release-only gates cause expensive rework
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 12. CinderVault Payments inherited 640 historical SQL-injection and path-traversal alerts on default branches after acquiring a regional processor. Which GitHub Code Security feature lets AppSec group up to `____` (`1,000`) default-branch alerts with a due date, security contact, and Copilot Autofix support?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **C.** `Security Campaigns` (`targeted, time-bound initiatives grouping up to 1,000 default-branch alerts with a named security contact and Copilot Autofix support`)
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 13. A tech lead on `chargeback-worker` wants to close a CodeQL alert triggered solely inside a mock unit-test harness while satisfying CinderVault Payments' external PCI audit trail. How does GitHub govern alert dismissals?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **C.** Dismissing an alert requires a structured closure reason (`False positive`, `Used in tests`, `Won't fix`) plus an audit-logged justification comment—and never deletes commits or revokes keys
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 14. A developer accidentally pushed a live database password into `pos-terminal-firmware` and received a Secret Protection alert. Proposed solution: Dismiss the alert as `Won't fix` in the Security tab and delete the password line in a new commit without rotating the credential. Does this remediate the exposure?

- **A.** No — Code Scanning rejects gzip-compressed SARIF files larger than `10 MB` (`and overwrites prior alerts when multiple matrix uploads share an identical SARIF category on one commit`)
- **B.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **C.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **D.** No — dismissing a Secret Protection alert or deleting the line in a new commit leaves the live credential active and exposed in prior Git history (`revoke & rotate first, then purge history`)

### 15. CinderVault Payments' compliance committee is drafting an alert-hygiene SOP so developers never silently hide unresolved vulnerabilities in `pci-audit-exporter`. Which two practices enforce accountable dismissal governance? Select two.

- **A.** Monitor dismissed and open alert trends centrally in `Security Overview` and `Audit Logs` (`repository_vulnerability_alert`, `secret_scanning_alert`, `code_scanning_alert`)
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Require an accurate dismissal reason (`False positive`, `Used in tests`, or `Won't fix`) with a reviewer-auditable justification comment whenever dismissing an alert
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **E.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 16. CinderVault Payments is defining RACI boundaries across Platform Engineering, Application Security, and Product Squads for its GitHub Enterprise rollout. Which responsibility split aligns with GitHub's operational model?

- **A.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **B.** Shared security model: `Admins` govern licensing/Security Configurations, `Security Managers` monitor Security Overview/campaigns/policies, and `Developers` remediate PR & campaign findings
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 17. Why must CinderVault Payments restrict raw Secret Protection alert viewing on `card-token-vault` to least-privilege roles while pairing Push Protection with delegated bypass reviewers?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **C.** Least-privilege alert access (`Write/Maintain/Admin/Security Manager` or custom roles) paired with `delegated bypass` so designated reviewers audit push-protection exceptions
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 18. CinderVault Payments' architecture board is reviewing cross-functional onboarding guidelines covering role governance, push-exception control, and complete transitive supply-chain visibility for Gradle payment services. Which three statements are accurate? Select three.

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Shared security model: `Admins` govern licensing/Security Configurations, `Security Managers` monitor Security Overview/campaigns/policies, and `Developers` remediate PR & campaign findings
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **E.** Least-privilege alert access (`Write/Maintain/Admin/Security Manager` or custom roles) paired with `delegated bypass` so designated reviewers audit push-protection exceptions
- **F.** `Dependency Graph` (`parsing committed manifests and lockfiles`, augmented by the `Dependency Submission API` for build-time resolved transitive graphs in Maven/Gradle/C++/containers)

---

## Domain 2 — Configure and use Secret Protection (formerly secret scanning) (15–20% official weight · 18 questions)

### 19. CinderVault Payments creates 8 new private microservice repositories every month and wants Secret Protection plus Push Protection enabled automatically on both existing and newly created repositories. Where should administrators configure this (`Organization Settings -> Code security -> ____`)?

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Enable `GitHub Secret Protection` (`secret scanning + push protection`) via Organization/Enterprise `Security Configurations` (`with Apply to new repositories`) or Repository `Settings -> Advanced Security`
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 20. An engineer commits an AWS access key to CinderVault Payments' public `cindervault-docs` repo and another test key to the private `vault-ledger-api` repo. How does GitHub Secret Protection handle notifications differently between the two repositories?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** On `public` repos, partner patterns run free and auto-notify token providers for revocation; on `private/internal` repos (`with Secret Protection`), alerts notify repo/org users (`plus optional validity checks`)

### 21. CinderVault Payments' Enterprise Owner disables the enterprise policy `Repository administrators can enable or disable GitHub Secret Protection` to stop unbudgeted seat usage. What happens to the 45 payment repositories that already had Secret Protection enabled?

- **A.** Enforce Enterprise Advanced Security policies (`restricting repo admins while preserving Org Owner/Security Manager control`), scope ruleset/push-protection bypass actors, and stream `security_configuration.*` / alert audit logs
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **D.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations

### 22. A developer at CinderVault Payments runs `git push origin feat/stripe-payouts` containing a live Stripe secret key in `ach-wire-gateway`, and the remote rejects the push with a `GH013: Repository rule violations` secret trace. Which mechanism intercepted the credential (`____`)?

- **A.** `Push Protection` intercepts supported high-confidence and published custom secrets pre-receive during `git push` (`CLI, IDE, web editor & REST API`), blocking the secret from entering Git history
- **B.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)

### 23. CinderVault Payments wants Secret Protection on `fraud-scoring-svc` to catch unstructured PostgreSQL connection passwords and custom bearer phrases that lack vendor prefixes (`like sk_live_`). Which settings extend detection, and what limitation applies?

- **A.** `Non-provider / generic pattern scanning` (`private keys, DB connection strings`) plus `Copilot AI generic secret detection` (`unstructured passwords/keys`, consuming `Secret Protection AI credits` on push)
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses

### 24. CinderVault Payments' incident-response lead wants both pre-commit history prevention and rapid prioritization of historical credential findings across `card-token-vault`. Which two Secret Protection capabilities directly address those goals? Select two.

- **A.** `Push Protection` blocks high-confidence partner and published custom secrets pre-receive during `git push` before commits land on GitHub
- **B.** `Validity checks` verify supported partner tokens (`Active` vs `Inactive`) so responders remediate live exploitable credentials immediately
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **E.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config

### 25. Secret Protection reports an `Active` production acquiring-bank API token committed two hours ago to `settlement-reconciler`. In which order should CinderVault Payments execute incident response and cleanup?

- **A.** Add paths-ignore in .github/secret_scanning.yml to auto-close the live production key alert → keep the credential unrotated → merge to main → archive the audit log
- **B.** Run git filter-repo first while leaving the production key active for 30 days → disable Secret Protection to clear UI banners → rotate the key only if an outage occurs → skip audit notes
- **C.** Confirm alert validity & blast radius → revoke and rotate the compromised credential at the provider → purge commit history (`git filter-repo`) & contact Support if cached PRs remain → resolve the alert as Revoked
- **D.** Dismiss the alert as Won't fix → delete the line in a new commit while keeping the live key active → add the file to .gitignore → assume old commits are unreadable

### 26. After enabling validity checks on `merchant-webhook-relay`, CinderVault Payments sees 4 alerts marked `Active`, 19 marked `Inactive`, and 6 marked `Unknown`. How should on-call responders interpret `Active` and on-demand re-checks?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **C.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)
- **D.** `Validity checks` query partner token endpoints (`displaying Active, Inactive, or Unknown`) so responders prioritize live `Active` credentials first

### 27. Why does CinderVault Payments' runbook forbid closing a leaked key alert until both provider rotation and `git filter-repo` history cleanup finish—even if a follow-up commit already deleted `.env.prod`?

- **A.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Treat every committed secret as compromised: `revoke & rotate at the issuing provider immediately`, rewrite Git history (`git filter-repo`), purge cached views via Support if needed, and resolve as `Revoked`
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 28. CinderVault Payments wants developers blocked by Push Protection on `vault-ledger-api` to submit a structured exception request approved by the Payment Security team rather than self-bypassing immediately. Which feature enforces this (`____`)?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** `Delegated bypass for push protection` (`granting Specific roles, visible teams, or custom roles with "Review and manage secret scanning bypass requests" authority—never secret teams`)
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 29. CinderVault Payments wants three senior regional security leads to approve or deny Push Protection bypass requests across repositories without making them Organization Owners or full Security Managers. Which fine-grained custom organization role permission should be granted (`____`)?

- **A.** `permissions: { security-events: write, contents: read, actions: read }` on `github/codeql-action/upload-sarif@v3`
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** `Review and manage secret scanning bypass requests` (`fine-grained organization role permission for Push Protection delegated bypass`)

### 30. CinderVault Payments is auditing its Push Protection delegated bypass configuration before a PCI QSA assessment. Which two rules govern valid bypass approver groups and audit telemetry? Select two.

- **A.** Assign `Specific roles, visible teams, or custom org roles` (`never secret teams`) to the Push Protection delegated bypass list to review and approve contributor bypass requests
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Audit every Push Protection bypass request, approval, and exemption via `secret_scanning_push_protection_bypass` audit events, alert timelines, and webhooks
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **E.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations

### 31. Every test run in `kyc-onboarding-portal` uses synthetic Stripe test fixtures under `tests/fixtures/mock-keys/**`, generating noisy user alerts. Which repository file and YAML key (`____`) suppresses user alerts in that directory, and what limits apply?

- **A.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)
- **D.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)

### 32. CinderVault Payments' public `cindervault-sandbox-examples` repository includes `.github/secret_scanning.yml` with `paths-ignore: ["examples/**"]`. What happens if a contributor accidentally commits a real partner-format cloud token inside `examples/demo.ts`?

- **A.** `.github/secret_scanning.yml` with `paths-ignore:` (`up to 1,000 glob entries and <= 1 MB file size`) auto-closing user alerts in test/docs paths (`without suppressing public-repo partner revocation alerts`)
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 33. Who receives Secret Protection alert notifications by default on CinderVault Payments' private `chargeback-worker` repository, and what happens when a Security Manager assigns one specific secret alert to a developer with `Write` access?

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)

### 34. CinderVault Payments issues internal settlement tokens formatted as `CVLT_LIVE_[A-Z0-9]{32}` and wants org-wide Push Protection without flooding 80 repositories with false-positive alerts. What is the exact lifecycle to roll out this custom pattern?

- **A.** Define pattern name, regex & test strings (`or Generate with AI`) → run `Save and dry run` across representative repos → refine regex/context to eliminate false positives → `Publish pattern` & enable Push Protection
- **B.** Enable Push Protection before publishing the pattern → publish an untested `.*` wildcard regex org-wide → review 50,000 live developer alerts → run a dry run afterward
- **C.** Commit custom regexes into .gitignore → skip dry runs because AI regexes are deterministic → assign secret teams to delegated bypass → expect partner validity checks on custom tokens
- **D.** Publish the pattern on a personal Free repo → expect Enterprise-wide enforcement automatically → edit the pattern assuming prior version alerts stay open → skip test strings

### 35. Six months after publishing CinderVault Payments' `CVLT_LIVE_` custom organization pattern (`one of 500 allowed org patterns`), an AppSec engineer edits its post-match regex to tighten entropy rules and saves the update. What happens to historical alerts created by the previous version of that pattern?

- **A.** Custom regex patterns (`up to 100/repo or 500/org-or-enterprise`, optional `Generate with AI` & `before`/`after` context) validated via `Save and dry run` (`<=1,000` sample hits) before `Publish pattern` & Push Protection
- **B.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 36. CinderVault Payments is standardizing custom secret patterns and fixture exclusions across `vault-ledger-api` and `pci-audit-exporter`. Which three platform rules should AppSec include in its engineering runbook? Select three.

- **A.** Custom regex patterns (`up to 100/repo or 500/org-or-enterprise`, optional `Generate with AI` & `before`/`after` context) validated via `Save and dry run` (`<=1,000` sample hits) before `Publish pattern` & Push Protection
- **B.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **C.** `Push Protection` intercepts supported high-confidence and published custom secrets pre-receive during `git push` (`CLI, IDE, web editor & REST API`), blocking the secret from entering Git history
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **E.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **F.** `.github/secret_scanning.yml` with `paths-ignore:` (`up to 1,000 glob entries and <= 1 MB file size`) auto-closing user alerts in test/docs paths (`without suppressing public-repo partner revocation alerts`)

---

## Domain 3 — Configure and use supply chain security (formerly Dependabot/Dependency Review) (15–20% official weight · 18 questions)

### 37. CinderVault Payments' `ach-wire-gateway` builds Maven artifacts with dynamic BOM property interpolation in CI, so static `pom.xml` parsing misses transitive JAR versions. How should the team populate complete transitive dependencies into GitHub's Dependency Graph?

- **A.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **D.** `Dependency Graph` (`parsing committed manifests and lockfiles`, augmented by the `Dependency Submission API` for build-time resolved transitive graphs in Maven/Gradle/C++/containers)

### 38. A banking regulator requests an automated nightly Software Bill of Materials in `SPDX` JSON format for `vault-ledger-api`. Which GitHub REST API endpoint (`____`) exports this inventory?

- **A.** `codeql github upload-results --repository=<org/repo> --ref=<refs/heads/main> --commit=<sha> --sarif=<results.sarif>`
- **B.** `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`attaching a Security Configuration across selected or all org repos via REST`)

### 39. Product leadership asks whether exporting the SPDX SBOM from `cindervault-js-sdk` will list all external merchant repositories that depend on CinderVault's SDK. What does the exported SPDX SBOM actually contain?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **D.** Export an `SPDX` JSON Software Bill of Materials (`SBOM`) via `Insights -> Dependency graph -> Export SBOM`, `GET /repos/{owner}/{repo}/dependency-graph/sbom`, or `actions/attest-sbom` (`excluding dependents`)

### 40. `settlement-reconciler` has 95 open Dependabot alerts: one `High` CVSS alert has an `EPSS` score of `0.91` and is marked `Reachable` in production runtime code, while four `Critical` CVSS alerts have `EPSS < 0.002` in `Unreachable` dev helpers. How should AppSec prioritize?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **C.** Prioritize `Dependabot alerts` combining `EPSS` (`30-day exploitation probability`), `CVSS` severity, `Reachability` call-path analysis (`Reachable` vs `Unreachable`), `runtime` scope, and `patch availability`
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 41. CinderVault Payments enabled GitHub's preset rule `Dismiss low impact issues for development-scoped dependencies` across its org and now needs to audit every suppressed finding during PCI review. Which Dependabot alert search qualifier (`____`) isolates those alerts?

- **A.** `queries: security-extended` (`executing default high-precision CodeQL security rules plus medium-precision security queries without style/quality rules`)
- **B.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **C.** `has:deployment runtime-risk:internet-exposed` (`Security Overview and alert search qualifiers powered by ingested deployment metadata`)
- **D.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)

### 42. CinderVault Payments wants to cut Dependabot alert fatigue by 60% on `kyc-onboarding-portal` without missing actively exploited vulnerabilities. Which two Dependabot prioritization and auto-triage behaviors apply? Select two.

- **A.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **B.** Combine `EPSS` (`30-day exploitation probability`) and static `Reachability` call-path verdicts with `CVSS` severity and `runtime` dependency scope
- **C.** Use `Dependabot auto-triage rules` to auto-dismiss or snooze low-impact dev/unpatched alerts (`resolution:auto-dismiss`) **before** alert notifications fire
- **D.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **E.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 43. New engineers on `fraud-scoring-svc` confuse `Dependabot security updates` with `Dependabot version updates`. What is the core functional difference between the two?

- **A.** `Dependabot security updates` (`alert-driven PRs patching vulnerable versions to the minimum fixed version`) vs `.github/dependabot.yml` `Dependabot version updates` (`scheduled ecosystem/Actions freshness PRs`)
- **B.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **C.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **D.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step

### 44. CinderVault Payments wants Dependabot to open automatic security pull requests on `chargeback-worker` **only** when `EPSS >= 0.10` and severity is `Critical`, leaving lower-risk alerts without PR noise. Proposed solution: Keep repository-wide `Dependabot security updates` enabled in Settings and add a custom Dependabot auto-triage rule set to `Open a pull request` for `EPSS >= 0.10`. Does this meet the goal?

- **A.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **B.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **C.** No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs
- **D.** No — `actions/dependency-review-action` forbids specifying `allow-licenses` and `deny-licenses` together, and fails to block merges unless marked as a required status check on `pull_request`

### 45. CinderVault Payments' internal npm package `@cindervault/ledger-types` collides with a public typosquatted malware advisory across `*` versions. Why does Dependabot never open an automated upgrade PR for malware advisories, and which preset handles benign internal name collisions?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** `Dependabot auto-triage rules` (`GitHub presets or custom rules on EPSS/CVE/CWE/scope/patch` setting `resolution:auto-dismiss` before notifications; disable global `Dependabot security updates` for custom PR-trigger rules)
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions

### 46. CinderVault Payments wants every pull request to `vault-ledger-api` blocked before merge if a developer introduces a `High`/`Critical` vulnerable package or an `AGPL-3.0` dependency. What is the complete setup sequence?

- **A.** Add SPDX license names to `.github/dependabot.yml` → expect Dependabot version updates to block developer PR merges → skip required status checks → disable lockfiles
- **B.** Trigger `dependency-review-action` only on weekly cron `schedule` → pass both `allow-licenses` and `deny-licenses` simultaneously → disable the Dependency Graph → leave main unprotected
- **C.** Run `dependency-review-action` on an unlicensed private Free repo → grant `write-all` permissions to untrusted fork code → ignore `fail-on-scopes` → merge failing checks freely
- **D.** Enable the Dependency Graph (`and Code Security on private repos`) → add an `on: pull_request` workflow running `actions/dependency-review-action@v4` → configure `fail-on-severity` & `deny-licenses` → mark the check required in a branch ruleset

### 47. CinderVault Payments' legal team wants `merchant-webhook-relay` pull requests to permit `MIT` and `Apache-2.0` packages while rejecting `GPL-3.0` packages. Proposed solution: Configure `actions/dependency-review-action@v4` with both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0` in the same step. Does this work?

- **A.** No — `actions/dependency-review-action` forbids specifying `allow-licenses` and `deny-licenses` together, and fails to block merges unless marked as a required status check on `pull_request`
- **B.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **C.** No — Code Scanning rejects gzip-compressed SARIF files larger than `10 MB` (`and overwrites prior alerts when multiple matrix uploads share an identical SARIF category on one commit`)
- **D.** No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs

### 48. CinderVault Payments is hardening pull-request supply-chain gates across its private `GitHub Code Security`-licensed settlement repositories. Which two steps are required so `dependency-review-action@v4` actually blocks non-compliant merges to `main`? Select two.

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Mark the `Dependency Review` workflow job as a **required status check** in a repository or organization Branch Ruleset targeting `main`
- **C.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **E.** Configure `actions/dependency-review-action@v4` with `fail-on-severity`, `fail-on-scopes`, and either `allow-licenses` OR `deny-licenses` (`SPDX` IDs)

### 49. `kyc-onboarding-portal` receives 40 separate weekly Dependabot PRs for `@babel/*` and `@types/*` packages and fails authenticating to CinderVault's private JFrog npm feed. Which `.github/dependabot.yml` configuration (`____`) solves both issues?

- **A.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`
- **B.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)
- **C.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **D.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)

### 50. CinderVault Payments pins major upgrades of `spring-boot` on `ach-wire-gateway` for manual quarterly architecture testing while capping concurrent Dependabot PRs per ecosystem at 5. Which `.github/dependabot.yml` keys control this?

- **A.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **B.** Configure `.github/dependabot.yml` with `groups:` (`batching patch/minor updates into single PRs`), `ignore:` (`version/dependency exclusions`), `open-pull-requests-limit`, and `registries:` (`authenticated via Dependabot secrets`)
- **C.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 51. CinderVault Payments wants automatic PRs whenever third-party Actions like `actions/checkout` or `docker/build-push-action` release patched versions in `.github/workflows/`. Which `package-ecosystem` entry must be added to `.github/dependabot.yml` (`package-ecosystem: "____"`)?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** `Dependabot security updates` (`alert-driven PRs patching vulnerable versions to the minimum fixed version`) vs `.github/dependabot.yml` `Dependabot version updates` (`scheduled ecosystem/Actions freshness PRs`)

### 52. Why did a CI job on `card-token-vault` triggered by a `dependabot[bot]` pull request fail when trying to read a repository `Actions secret` and push a tag using the default `GITHUB_TOKEN`?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Govern Dependabot PR workflows (`read-only GITHUB_TOKEN` & `Dependabot secrets`), fine-grained alert roles, `dependabot_alert` webhooks, and production-context filters (`has:deployment`, `runtime-risk:internet-exposed`)
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 53. CinderVault Payments connected Microsoft Defender for Cloud and its container registry to GitHub so Security Overview knows which container images run live in production AKS clusters. Which filter qualifiers (`____`) isolate internet-reachable deployed alerts?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)
- **C.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)
- **D.** `has:deployment runtime-risk:internet-exposed` (`Security Overview and alert search qualifiers powered by ingested deployment metadata`)

### 54. CinderVault Payments' platform security team is reviewing CI runner safety for Dependabot PRs and runtime alert enrichment via external integrations. Which two statements accurately describe GitHub's supply-chain architecture? Select two.

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Workflows triggered by `dependabot` PRs receive a **read-only `GITHUB_TOKEN`** by default and access credentials stored in **`Dependabot secrets`** (`not standard Actions secrets on untrusted triggers`)
- **C.** Ingest deployment metadata (`from Microsoft Defender for Cloud, JFrog Artifactory, or CI/CD APIs`) to filter `has:deployment` and `runtime-risk:internet-exposed` alerts
- **D.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **E.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

---

## Domain 4 — Configure and use Code Security (formerly Code Scanning with CodeQL) (10–15% official weight · 14 questions)

### 55. CinderVault Payments runs `CodeQL` for Java/TypeScript services and `Trivy` + `Checkov` for Terraform/Dockerfile IaC checks on `vault-ledger-api`. How do CodeQL and third-party tools complement each other inside GitHub Code Scanning?

- **A.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **B.** `CodeQL` (`compiling/extracting code into a queryable relational AST/CFG/dataflow database`) paired with third-party SAST/IaC/container scanners uploading `SARIF 2.1.0` into unified Code Scanning alerts
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

### 56. `settlement-reconciler` runs four third-party scanners in one matrix workflow; one produces a `14 MB` gzip-compressed SARIF file, and the other three upload without setting `category:`. Proposed solution: Upload all four files as-is via `github/codeql-action/upload-sarif@v3` with `contents: read` only. Does this work?

- **A.** No — Code Scanning rejects gzip-compressed SARIF files larger than `10 MB` (`and overwrites prior alerts when multiple matrix uploads share an identical SARIF category on one commit`)
- **B.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **C.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)
- **D.** Yes — this configuration satisfies every security, licensing, and governance requirement

### 57. CinderVault Payments is onboarding a custom PCI static analyzer exporting `SARIF 2.1.0` across 6 monorepo payment modules. Which two technical requirements ensure clean alert ingestion and deduplication? Select two.

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Assign a unique `category` per tool/language/monorepo target and preserve stable `ruleId` + `partialFingerprints` so alerts deduplicate cleanly without overwriting sibling scans
- **C.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **D.** Ensure each uploaded `SARIF 2.1.0` file is `<= 10 MB` gzip-compressed and `<= 25,000` results (`knowing GitHub displays only the top 5,000 results prioritized by severity`)
- **E.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage

### 58. CinderVault Payments builds `pos-terminal-firmware` (`C/C++`) on dedicated self-hosted hardware-HSM Jenkins servers outside GitHub Actions and must publish CodeQL alerts to GitHub Code Scanning. What is the exact `CodeQL CLI` command lifecycle?

- **A.** Enable Default Setup simultaneously for the same language/category → upload SARIF with a read-only `contents: read` token → strip `partialFingerprints` → expect >25,000 results to render without truncation
- **B.** Install the CodeQL CLI bundle on the CI agent → run `codeql database create` (`tracing compiled builds`) → run `codeql database analyze --format=sarif-latest` → run `codeql github upload-results` (`--sarif`, `--ref`, `--commit`)
- **C.** Run `codeql github upload-results` on raw `.java` source files → run `codeql database analyze` before `codeql database create` → upload an uncompressed 45 MB XML report → omit `--ref` and `--commit`
- **D.** Create one shared SARIF file without `--sarif-category` across 6 monorepo services → overwrite prior language alerts on every upload → disable GitHub Code Security on private repos → view alerts in Actions cache

### 59. `ach-wire-gateway` (`C++` and `Java` with custom protobuf code generation) currently uses CodeQL `Default Setup`, which fails on missing generated headers. Proposed solution: Keep `Default Setup` enabled and commit a second `.github/workflows/codeql.yml` workflow for the same languages. Does this work?

- **A.** No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs
- **B.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **C.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)
- **D.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)

### 60. In `pos-terminal-firmware` (`ARM C++` cross-compiled via custom `cmake -DTOOLCHAIN=arm-none-eabi`), `autobuild` fails and `build-mode: none` is unsupported for C/C++. Which `github/codeql-action/init@v3` setting (`____`) must CinderVault Payments configure?

- **A.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **B.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`
- **C.** `build-mode: manual` (`paired with explicit compiler commands prior to github/codeql-action/analyze@v3`)
- **D.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)

### 61. On a pull request to `card-token-vault`, CodeQL reports `Uncontrolled data used in path expression` and displays a 6-step `Show paths` trace alongside a `Copilot Autofix` diff. How do dataflow components and classic Copilot Autofix licensing work?

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Inspect CodeQL `source -> step -> sink` path-problem dataflow traces and apply `Copilot Autofix` (`enabled by default on CodeQL PRs & default branch without requiring a Copilot seat for classic Autofix`)

### 62. CinderVault Payments hardened `.github/workflows/codeql.yml` on `merchant-webhook-relay` by setting workflow default permissions to `permissions: {}`. Which exact job-level `permissions:` block (`____`) is required so `codeql-action/analyze` or `upload-sarif` succeeds?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** `Review and manage secret scanning bypass requests` (`fine-grained organization role permission for Push Protection delegated bypass`)
- **C.** `permissions: { security-events: write, contents: read, actions: read }` on `github/codeql-action/upload-sarif@v3`
- **D.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)

### 63. CinderVault Payments' developers are reviewing `Copilot Autofix` proposals for SQL injection and XSS findings on `kyc-onboarding-portal` pull requests. Which two statements reflect GitHub's recommended remediation workflow and licensing? Select two.

- **A.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **B.** Inspect CodeQL `source -> step -> sink` path-problem dataflow traces and apply `Copilot Autofix` (`enabled by default on CodeQL PRs & default branch without requiring a Copilot seat for classic Autofix`)
- **C.** Validate every `Copilot Autofix` suggestion by inspecting dataflow context, running full CI unit/integration tests + re-scanning with `CodeQL`, and completing human PR review
- **D.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **E.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 64. A developer on `fraud-scoring-svc` asks why an alert labeled `Warning` under rule `problem.severity` still blocked their PR under a ruleset configured to block `High` or `Critical` security alerts. What explains the two severity fields in Code Scanning?

- **A.** Distinguish `security-severity` (`Critical/High/Medium/Low` mapped from CVSS `0.0–10.0`) from rule `problem.severity` (`error/warning/note`), use `category` per matrix leg, and record audited dismissal reasons
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **D.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)

### 65. After refactoring 40 lines at the top of `LedgerDao.java` in `vault-ledger-api`, an existing open CodeQL alert stayed tracked as the same alert ID instead of closing and opening a duplicate. Which SARIF mechanism enables line-shift tracking?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **C.** `SARIF 2.1.0` ingestion rules: `<= 10 MB` gzip-compressed upload limit, `<= 25,000` results/run (`top 5,000` displayed by severity), `partialFingerprints` deduplication, distinct `category` tags, and `security-events: write`
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 66. If a developer dismisses a CodeQL alert as `False positive` on `main` in `chargeback-worker`, under what condition will Code Scanning automatically reopen that alert on a future commit?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Dismissing an alert requires a structured closure reason (`False positive`, `Used in tests`, `Won't fix`) plus an audit-logged justification comment—and never deletes commits or revokes keys

### 67. CinderVault Payments uses an internal Java sanitization library (`com.cindervault.sec.SqlSafe.clean`) that standard CodeQL queries do not recognize, causing false-positive SQLi alerts, and also wants `vendor/**` excluded. Where should AppSec configure custom `packs`, `paths-ignore`, and YAML data-extension `model packs` (`____`)?

- **A.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`
- **D.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)

### 68. CinderVault Payments' monorepo CodeQL job on `vault-ledger-api` (`Java + TypeScript + Python`) hits `exit code 137` (`Out of Memory`) on standard 2-core 7 GB GitHub-hosted runners after 95 minutes. What are the recommended remediation steps?

- **A.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **B.** Customize `.github/codeql/codeql-config.yml` (`paths-ignore`, `packs`, `queries`, `threat-models`) & `CodeQL model packs` (`YAML data extensions`), and fix OOM/slow scans via Larger runners or split language matrices
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

---

## Domain 5 — Security operations: best practices, prioritization, and remediation (15–20% official weight · 18 questions)

### 69. An external researcher reports an authentication-bypass zero-day against CinderVault Payments' open-source `cindervault-js-sdk` via Private Vulnerability Reporting. What is the proper end-to-end `GHSA` remediation and coordinated disclosure sequence?

- **A.** Open a temporary private fork and run GitHub Actions workflows directly inside that advisory fork → auto-merge without review → delete the GHSA after release so downstream Dependabot alerts never fire
- **B.** Publish the unpatched exploit details in a public GitHub Issue immediately → ask developers to commit fixes on a public feature branch → request a CVE before confirming the bug → create a draft advisory last
- **C.** Triage the report via Private Vulnerability Reporting (`draft GHSA`) → open a temporary private fork from the advisory to develop & verify the fix → request a `CVE` & prepare patched versions → merge the fix & publish the advisory
- **D.** Dismiss the researcher report without reading it → rotate unrelated SSH keys → add the vulnerable source folder to `secret_scanning.yml` → expect CVEs to assign without advisory metadata

### 70. During post-incident documentation at CinderVault Payments, a junior analyst mixes up `CWE-89`, `CVE-2026-41822`, and `GHSA-xxxx-xxxx-xxxx`. How do `CWE`, `CVE`, and `GHSA` differ?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** `CWE` classifies weakness types (`e.g., CWE-89 SQLi`), `CVE` identifies a publicly disclosed vulnerability instance, and `GHSA` (`Repository Security Advisories` + Private Reporting) coordinates private patches & CVEs
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions

### 71. Maintainers of `cindervault-js-sdk` open a temporary private fork inside a draft `GHSA` to fix a critical signature-forgery bug and want automated CI tests. Proposed solution: Trigger standard `.github/workflows/ci.yml` GitHub Actions runs directly inside the temporary private advisory fork, or push the branch to the public upstream repo to trigger CI before release. Does this work safely?

- **A.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **B.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)
- **C.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)
- **D.** Yes — this configuration satisfies every security, licensing, and governance requirement

### 72. CinderVault Payments has 1,400 legacy CodeQL and Dependabot alerts across 80 repositories and wants zero net-new `Critical`/`High` regressions on `main` while burning down live internet-facing payment services first. Which strategy achieves both?

- **A.** Prioritize using `has:deployment` + `runtime-risk:internet-exposed` (`Defender for Cloud / artifact registries`), `EPSS`, and `Reachability`, while blocking new regressions via `Require code scanning results` rulesets
- **B.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 73. In a CinderVault Payments branch ruleset, `Require code scanning results` is set to `Security alerts: High or higher` and `All alerts: Errors`. Which pull-request findings will fail the merge gate?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Distinguish `security-severity` (`Critical/High/Medium/Low` mapped from CVSS `0.0–10.0`) from rule `problem.severity` (`error/warning/note`), use `category` per matrix leg, and record audited dismissal reasons
- **C.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **D.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses

### 74. CinderVault Payments is rolling out cross-repository severity rulesets and runtime prioritization across its 80 payment repositories without breaking Friday settlement deployments. Which two practices should AppSec combine? Select two.

- **A.** Ingest deployment metadata (`from Microsoft Defender for Cloud, JFrog Artifactory, or CI/CD APIs`) to filter `has:deployment` and `runtime-risk:internet-exposed` alerts
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Pilot cross-repository `Rulesets` in **`Evaluate` mode** to measure would-be blocked PRs via Ruleset Insights before switching enforcement to **`Active`**
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **E.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect

### 75. CinderVault Payments' AppSec lead wants to eliminate 180 default-branch `CWE-79` XSS and `CWE-89` SQLi alerts across 12 merchant portals over a 30-day sprint. What is the end-to-end Security Campaign workflow?

- **A.** Filter high-risk default-branch alerts in Security Overview → create a Security Campaign (`<=1,000` alerts) with due date & contact → trigger Copilot Autofix (`or assign <=25 alerts to @copilot`) → verify CI checks & track burndown
- **B.** Export alerts to a static spreadsheet with no GitHub links → disable CodeQL so open counts fall to zero → bulk-dismiss every alert without comments → report 100% remediation
- **C.** Create a campaign containing 50,000 unmerged fork-branch alerts with no contact owner → auto-merge Copilot suggestions bypassing CI tests → revoke developer write access → close the campaign with alerts still open
- **D.** Assign 500 alerts in one batch to `@copilot` without AI credits or branch protection → skip human PR review → disable Security Overview → expect secret campaigns to auto-rotate AWS IAM keys

### 76. CinderVault Payments enabled `Code Security AI credits` so AppSec managers can delegate Security Campaign alerts directly to the `@copilot` cloud coding agent to open draft PRs automatically. Up to how many alerts (`____`) can be assigned to `@copilot` in a single batch?

- **A.** Run `Security Campaigns` (`<=1,000` default-branch alerts, named security lead, developer notifications, Copilot Autofix, or assigning `<=25` alerts per batch to `@copilot` cloud agent) with audited dismissal comments
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 77. CinderVault Payments' CFO asks why standard PR `Copilot Autofix` suggestions on `vault-ledger-api` incurred `$0` in metered AI overages last month whereas `@copilot` Security Campaign batches and `AI Scan` consumed `Code Security AI credits`. What is the billing distinction?

- **A.** Monitor `Code Security AI credits` (`AI Scan / agentic autofix`) and `Secret Protection AI credits` (`AI push scanning`), setting **hard metered budgets** to cap spend
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 78. CinderVault Payments wants `card-token-vault` (`Tier-0 PCI`) scanned with both high-precision default CodeQL security queries and lower-threshold medium-precision security queries—without noisy code-formatting or maintainability warnings. Which suite (`queries: ____`) should be set?

- **A.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** `queries: security-extended` (`executing default high-precision CodeQL security rules plus medium-precision security queries without style/quality rules`)
- **D.** `has:deployment runtime-risk:internet-exposed` (`Security Overview and alert search qualifiers powered by ingested deployment metadata`)

### 79. After discovering a novel deserialization gadget in `ach-wire-gateway`, CinderVault Payments' threat hunter writes a custom `.ql` query and wants to scan 350 organization repositories simultaneously from VS Code without editing 350 workflows. Which capability supports this (`____`)?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Select CodeQL query suites (`default` high-precision, `security-extended` broader lower-confidence security, `security-and-quality` adds maintainability) and run `Multi-Repository Variant Analysis (MRVA)` in VS Code
- **C.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

### 80. By default, CodeQL focuses on `remote` HTTP/network taint sources, missing vulnerabilities in `pos-terminal-firmware` CLI utilities that parse untrusted local USB files and environment variables. Which `codeql-config.yml` setting expands local input sources?

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Customize `.github/codeql/codeql-config.yml` (`paths-ignore`, `packs`, `queries`, `threat-models`) & `CodeQL model packs` (`YAML data extensions`), and fix OOM/slow scans via Larger runners or split language matrices

### 81. CinderVault Payments appoints one developer per squad as a "Security Champion" who needs permission to view and triage Code Scanning and Dependabot alerts on their squad's repos without `Admin` repository settings access. What is the cleanest least-privilege role design?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **C.** Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 82. During a P1 production settlement outage on `vault-ledger-api`, an on-call engineer needs an emergency temporary exception to merge past a branch ruleset check with full post-incident auditability. How should bypass governance be structured?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** `Delegated bypass for push protection` (`granting Specific roles, visible teams, or custom roles with "Review and manage secret scanning bypass requests" authority—never secret teams`)
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 83. CinderVault Payments is aligning AppSec and 18 product squads on shared alert ownership and zero-downtime policy rollouts. Which two governance practices follow GitHub's operational model? Select two.

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Pilot cross-repository `Rulesets` in **`Evaluate` mode** to measure would-be blocked PRs via Ruleset Insights before switching enforcement to **`Active`**
- **C.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **D.** Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)
- **E.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations

### 84. CinderVault Payments wants developers on `merchant-webhook-relay` to get security feedback at the earliest technically feasible moment for secrets, open-source packages, and custom TypeScript code. Which three-layer preventive stack achieves this?

- **A.** Layer `Push Protection` (`pre-receive`), `actions/dependency-review-action` (`PR manifest/license gate`), and `CodeQL` PR checks (`with Copilot Autofix`) so secrets, vulnerable packages, and taint flaws fail pre-merge
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 85. A developer opens a PR on `fraud-scoring-svc` upgrading `axios` while accidentally pulling in a transitive `High`-severity vulnerable sub-package in `package-lock.json` that does not yet exist on `main`. Which tool catches this *before* merge (`____`)?

- **A.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **B.** `actions/dependency-review-action@v4` on `pull_request` (`with fail-on-severity, mutually exclusive allow-licenses OR deny-licenses SPDX lists, fail-on-scopes, and allow-ghsas`) enforced as a required check
- **C.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 86. CinderVault Payments' Engineering Excellence charter mandates three preventive shift-left gates across all PCI-scoped repositories before any pull request can merge to `main`. Which three controls belong in that baseline? Select three.

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Configure `actions/dependency-review-action@v4` with `fail-on-severity`, `fail-on-scopes`, and either `allow-licenses` OR `deny-licenses` (`SPDX` IDs)
- **C.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **D.** Validate every `Copilot Autofix` suggestion by inspecting dataflow context, running full CI unit/integration tests + re-scanning with `CodeQL`, and completing human PR review
- **E.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **F.** `Push Protection` blocks high-confidence partner and published custom secrets pre-receive during `git push` before commits land on GitHub

---

## Domain 6 — GitHub Security suites administration (10–15% official weight · 14 questions)

### 87. CinderVault Payments is rolling out standardized Secret Protection, Dependabot, and CodeQL Default Setup across 120 repositories in three PCI tiers (`cde`, `internal`, `sandbox`). What is the recommended Security Configuration rollout sequence?

- **A.** Apply an `Enforced` configuration across 2,000 private repos with zero available committer seats → set every feature to `Not set` expecting strict locks → leave new repositories uncovered → disable audit logs
- **B.** Manually toggle Settings on 2,000 repositories one by one → grant every developer Organization Owner permissions → disable Push Protection globally → rely on `.gitignore` for enterprise governance
- **C.** Enable cloud-only Copilot Autofix on an air-gapped GHES instance with metered billing → skip GitHub Connect → expect transferred external repos to inherit new-repo defaults automatically without policy checks
- **D.** Verify committer license headroom (`or metered budget`) → create/select a Security Configuration → attach to tiered repos (`custom properties`) & enable `Apply to new repositories` → set `Enforced` to lock baseline controls

### 88. CinderVault Payments runs most workloads on `GitHub Enterprise Cloud (GHEC)` plus an on-premises `GitHub Enterprise Server (GHES)` appliance for central-bank clearing. What are the key Security Suite differences between `GHEC` and `GHES`?

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Roll out org/enterprise `Security Configurations` (`GitHub-recommended` or custom, `Apply to new repositories`), contrasting `GHEC` (`metered or volume + cloud AI features`) with `GHES` (`volume-only + GitHub Connect Advisory sync`)

### 89. CinderVault Payments configured an organization Security Configuration with `Apply to new repositories` enabled and then **transferred** an existing private repository (`legacy-iso8583-parser`) in from an acquired org. Was the Security Configuration automatically attached upon transfer?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** `Enforced` Security Configurations lock enabled/disabled settings (`except fields set to "Not set"`), while private/internal repos consume `90-day unique active committer` seats (`plus metered AI credits for AI Scan/generic secrets`)
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners

### 90. CinderVault Payments' Security Manager attaches an `Enforced` Security Configuration to `vault-ledger-api` with `Secret scanning = Enabled`, `Push protection = Enabled`, and `Dependabot security updates = Not set`, expecting repo admins to be locked out of changing Dependabot security updates. Proposed solution: Leave `Dependabot security updates` as `Not set` under `Enforced` mode. Does this lock the setting?

- **A.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)
- **B.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **C.** No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs
- **D.** Yes — this configuration satisfies every security, licensing, and governance requirement

### 91. CinderVault Payments has 200 volume seats for `GitHub Code Security`. Developer Priya pushed commits to 14 private enabled repos in the last 60 days, Developer Mateo last committed 115 days ago, and `dependabot[bot]` opened 90 PRs yesterday. How many seats do Priya, Mateo, and `dependabot[bot]` consume (`____`)?

- **A.** `Enforced` Security Configurations lock enabled/disabled settings (`except fields set to "Not set"`), while private/internal repos consume `90-day unique active committer` seats (`plus metered AI credits for AI Scan/generic secrets`)
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners

### 92. CinderVault Payments' FinOps and AppSec leads are modeling FY27 costs for hybrid `GHEC + GHES` committers and AI-powered security capabilities. Which two billing and governance rules are accurate? Select two.

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Monitor `Code Security AI credits` (`AI Scan / agentic autofix`) and `Secret Protection AI credits` (`AI push scanning`), setting **hard metered budgets** to cap spend
- **D.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **E.** Count `90-day unique active committers` across private/internal repos (`deduplicating each human user once across the enterprise, plus GitHub Connect sync between GHEC and GHES`)

### 93. CinderVault Payments' PCI QSA asks how to prove that no repository admin detached the `PCI-CDE-Enforced` Security Configuration or secretly bypassed Push Protection during Q3. Which enterprise governance control provides tamper-evident proof?

- **A.** Enforce Enterprise Advanced Security policies (`restricting repo admins while preserving Org Owner/Security Manager control`), scope ruleset/push-protection bypass actors, and stream `security_configuration.*` / alert audit logs
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 94. If CinderVault Payments' Enterprise Owner sets an enterprise-enforced Security Configuration across all `pci_scope:cde` organizations, can an individual Organization Owner detach that enterprise configuration from `vault-ledger-api`?

- **A.** Enforce Enterprise Advanced Security policies (`restricting repo admins while preserving Org Owner/Security Manager control`), scope ruleset/push-protection bypass actors, and stream `security_configuration.*` / alert audit logs
- **B.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners

### 95. CinderVault Payments wants an enterprise-wide standard ensuring no single engineer can push a matched live secret or merge a Critical CodeQL regression into `main` unreviewed. Which paired exception policy achieves this?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** `Delegated bypass for push protection` (`granting Specific roles, visible teams, or custom roles with "Review and manage secret scanning bypass requests" authority—never secret teams`)

### 96. CinderVault Payments hired four AppSec engineers who need read/write access to all security alerts across 120 organization repositories plus permission to manage Security Configurations—**without** billing-owner access or permission to push code to repositories. Which built-in organization role fits (`____`)?

- **A.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **B.** Separate `Enterprise/Org Owners` (`billing & global policy`), `Security Managers` (`org-wide alert read/write & security config management, without code-write`), and custom repository roles (`granular view/dismiss per tool`)
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 97. An external PCI auditor needs read-only visibility into Code Scanning alerts on `pci-audit-exporter` for two weeks, with **no** ability to dismiss alerts, view raw Secret Protection tokens, or push code. How should CinderVault Payments configure access?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **C.** Separate `Enterprise/Org Owners` (`billing & global policy`), `Security Managers` (`org-wide alert read/write & security config management, without code-write`), and custom repository roles (`granular view/dismiss per tool`)
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 98. On a private repository at CinderVault Payments with default role settings, which minimum standard repository role can view **Code Scanning** and **Dependabot** alerts (`Write`) versus viewing **Secret Protection** alerts (`Admin` / `Security Manager`)?

- **A.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **B.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **C.** Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 99. CinderVault Payments' Terraform/backstage repo-provisioning service creates private payment microservices via API and must attach Security Configuration `config_id=42` programmatically. Which REST endpoint (`____`) performs this attachment?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`attaching a Security Configuration across selected or all org repos via REST`)
- **C.** `codeql github upload-results --repository=<org/repo> --ref=<refs/heads/main> --commit=<sha> --sarif=<results.sarif>`
- **D.** `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)

### 100. CinderVault Payments wants to guarantee that none of its 40 custom-built `C++` and `Java` payment repos can alter `.github/workflows/codeql.yml` to weaken scan rules, while exporting weekly org-wide alert metrics to Power BI without making 120 per-repo API calls. Which two platform mechanisms solve this? Select two.

- **A.** Enforce approved CodeQL scanning via Org/Enterprise `Rulesets` (`Require code scanning results` + Required Workflows) and automate governance via REST/GraphQL (`code-security/configurations`, org alert endpoints & billing APIs)
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Pilot cross-repository `Rulesets` in **`Evaluate` mode** to measure would-be blocked PRs via Ruleset Insights before switching enforcement to **`Active`**
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **E.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners

---

## Answer Key and Explanations

### Question 1 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). GitHub unbundled Advanced Security into standalone `GitHub Secret Protection` and `GitHub Code Security` SKUs available on both GitHub Team and GitHub Enterprise, billed per 90-day active committer. [Skill 1.1: Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)]

- **A:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Correct. GitHub offers standalone Secret Protection and Code Security products on both GitHub Team and GitHub Enterprise, billed by unique 90-day active committers on private/internal repos
- **D:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions

### Question 2 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Secret Protection governs credential leaks, Code Security (`CodeQL`/SARIF + Copilot Autofix) analyzes first-party code flaws, and Supply Chain Security governs open-source dependency and license risks. [Skill 1.1: Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Correct. each pillar targets a distinct risk surface: leaked credentials, first-party source vulnerabilities, and third-party open-source dependency/license exposure
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 3 — `A, D` (Describe GitHub Security suites, features, and ecosystem)

Correct answers: A and D (are correct). Standalone Secret Protection delivers push protection, secret scanning, validity checks, custom patterns, and AI generic detection, while standalone Code Security delivers CodeQL/SARIF scanning, Copilot Autofix, private-repo Dependency Review, and Security Campaigns. [Skill 1.1: Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)]

- **A:** Correct. Secret Protection focuses specifically on credential exposure in pushes and Git history
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Correct. Code Security covers first-party SAST, Copilot Autofix, and private-repository Dependency Review enforcement
- **E:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 4 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). Public GitHub.com repositories receive core secret scanning, push protection, Dependency Graph, Dependabot, CodeQL default setup, and Dependency Review at no cost, whereas private/internal repositories require Secret Protection or Code Security licenses for advanced capabilities. [Skill 1.2: Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-overview/about-security-overview)]

- **A:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Correct. GitHub provides core security scanning free to open-source public repositories on GitHub.com while requiring Secret Protection / Code Security licenses for advanced private/internal repo coverage

### Question 5 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Security Overview provides Risk, Coverage, Campaigns, and tool-specific posture views filterable by team, topic, or repository custom properties across an organization or enterprise. [Skill 1.2: Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-overview/about-security-overview)]

- **A:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **B:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets
- **C:** Correct. Security Overview aggregates posture, enablement gaps, alert trends, and campaign burndown across hundreds of repositories from a single org/enterprise plane
- **D:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges

### Question 6 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). GitHub's free organization security risk assessment scans private org repositories for exposed secrets and evaluates up to 20 active repositories with CodeQL and Copilot Autofix previews prior to licensing. [Skill 1.2: Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-overview/about-security-overview)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Correct. organizations on GitHub Team or Enterprise can run free secret and code risk assessments before purchasing full rollout licenses

### Question 7 — `B` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: B (is correct). Secret Protection scans text and Git blobs for structured/high-entropy/AI credential tokens at push and in history, whereas CodeQL builds a semantic AST/dataflow database to trace taint paths and hardcoded-credential sinks in source code. [Skill 1.3: Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Correct. Secret Protection catches leaked tokens in any text/config file at push time, while CodeQL models how untrusted inputs or hardcoded values flow into sensitive code sinks
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 8 — `B` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: B (is correct). Adding `src/**` to `.github/secret_scanning.yml` suppresses secret alerts in production source paths instead of blocking pushes pre-receive with Push Protection or scanning PRs with CodeQL. [Skill 1.3: Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. Adding `src/**` to `.github/secret_scanning.yml` suppresses secret alerts in production source paths instead of blocking pushes pre-receive with Push Protection or scanning PRs with CodeQL.
- **B:** Correct. secret_scanning.yml suppresses user notifications in excluded folders rather than blocking pushes or cancelling public-repo partner revocations
- **C:** Incorrect. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts
- **D:** Incorrect. allow-licenses and deny-licenses are mutually exclusive inputs in dependency-review-action, and branch rulesets must require the check to block merging

### Question 9 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Combining pre-receive Push Protection, PR `dependency-review-action` checks, and PR CodeQL analysis with Copilot Autofix prevents leaked secrets, vulnerable packages, and code taint defects from landing on `main`. [Skill 1.3: Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Correct. combining all three shift-left controls prevents new security debt from ever landing on the default branch
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 10 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). A prevention-first workflow intercepts secrets pre-receive via Push Protection, runs Dependency Review and CodeQL on PRs, applies Copilot Autofix or dependency upgrades pre-merge, and monitors default-branch advisories continuously in Security Overview. [Skill 1.4: Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns)]

- **A:** Incorrect. Copilot Autofix requires an upstream CodeQL finding first, and Push Protection intercepts secrets during git push rather than post-merge
- **B:** Incorrect. auto-dismissing unreviewed PR findings defeats shift-left prevention, and .gitignore never revokes already-exposed credentials
- **C:** Correct. a prevention-first secure SDLC stops secrets at git push, blocks vulnerable PR code/dependencies with pre-merge checks and Autofix, and continuously monitors post-merge advisories
- **D:** Incorrect. deferring secret and code checks until after merge exposes live credentials in Git history and turns security into high-cost reactive firefighting

### Question 11 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). Catching secrets at `git push` and surfacing CodeQL/Dependency Review findings with Copilot Autofix directly in feature PRs eliminates Git history rewrites and late release-blocking rework. [Skill 1.4: Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns)]

- **A:** Correct. shifting detection to git push and pull requests prevents secret sprawl and vulnerable merges before release cutoffs
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 12 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Security Campaigns group up to 1,000 default-branch alerts into time-bound remediation initiatives backed by a designated security contact, developer notifications, and Copilot Autofix. [Skill 1.4: Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **C:** Correct. Security Campaigns turn overwhelming alert backlogs into manageable, developer-friendly remediation sprints with clear ownership
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 13 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Dismissing an alert requires selecting a structured reason (`False positive`, `Used in tests`, or `Won't fix`), recording a justification comment, and preserving the event in REST/GraphQL APIs, webhooks, and audit logs without altering Git history. [Skill 1.5: Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/vulnerability-exposure)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **C:** Correct. alert dismissals remain visible in REST/GraphQL APIs, webhooks, and audit logs, so teams must document rationale rather than hiding unverified risk
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 14 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). Dismissing an alert or deleting a line in a subsequent commit leaves the live credential exposed in prior Git commit blobs and never revokes access at the database or cloud provider. [Skill 1.5: Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/vulnerability-exposure)]

- **A:** Incorrect. each gzipped SARIF upload must be <=10 MB with a distinct category per language/tool/component and security-events: write permission
- **B:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. Dismissing an alert or deleting a line in a subsequent commit leaves the live credential exposed in prior Git commit blobs and never revokes access at the database or cloud provider.
- **C:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **D:** Correct. alert dismissal only updates GitHub UI/API triage status; attackers can still extract unrotated keys from earlier commits, clones, or reflogs

### Question 15 — `A, C` (Describe GitHub Security suites, features, and ecosystem)

Correct answers: A and C (are correct). Requiring structured dismissal reasons with documented comments and auditing dismissal events through Security Overview, webhooks, REST APIs, and enterprise audit logs ensures transparent risk sign-off. [Skill 1.5: Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/vulnerability-exposure)]

- **A:** Correct. Security Overview and org audit logs surface anomalous dismissal spikes or unpatched high-risk repositories
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Correct. structured dismissal reasons and comments create an auditable compliance trail in webhooks and GraphQL/REST APIs
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **E:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 16 — `B` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: B (is correct). Organization/Enterprise Admins manage licensing and baseline Security Configurations, Security Managers monitor Security Overview, campaigns, and triage policies, and Developers remediate PR and campaign findings in code. [Skill 1.6: Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)]

- **A:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **B:** Correct. effective DevSecOps distributes enablement, posture prioritization, and code-level patching cleanly across Admin, AppSec, and Developer roles
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 17 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Secret alerts expose sensitive token values and commit locations, and delegated bypass forces push exceptions through designated reviewers rather than silent developer self-overrides. [Skill 1.6: Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **C:** Correct. restricting sensitive secret/vulnerability details and routing bypass requests through designated security reviewers preserves accountability without halting urgent releases
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 18 — `B, E, F` (Describe GitHub Security suites, features, and ecosystem)

Correct answers: B, E, and F (are correct). Separating Admin/Security Manager/Developer duties, enforcing least-privilege alert access with delegated bypass reviewers, and combining committed lockfiles with Dependency Submission API build snapshots establish end-to-end governance. [Skill 1.6: Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Correct. effective DevSecOps distributes enablement, posture prioritization, and code-level patching cleanly across Admin, AppSec, and Developer roles
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **E:** Correct. restricting sensitive secret/vulnerability details and routing bypass requests through designated security reviewers preserves accountability without halting urgent releases
- **F:** Correct. committing lockfiles plus submitting build-resolved snapshots gives GitHub complete direct and transitive dependency visibility

### Question 19 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). Attaching an Organization or Enterprise Security Configuration with `Apply to new repositories` enabled scales Secret Protection and Push Protection consistently across current and future repositories. [Skill 2.1: Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Correct. Security Configurations scale Secret Protection across existing and newly created repositories consistently, while single-repo toggles suit isolated pilots
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 20 — `D` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: D (is correct). Public repositories run partner secret scanning free and automatically forward matched tokens to the issuing partner vendor for revocation/alerting, whereas private/internal repositories generate internal repository/org alerts without automatic public partner revocation notices. [Skill 2.1: Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Correct. partner notification automatically reports exposed public-repo tokens to the issuing cloud/SaaS vendor, whereas private-repo findings stay internal unless validity checks query the provider

### Question 21 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). Disabling repository-admin toggle rights leaves Secret Protection active on already-enabled repositories and preserves Organization Owner and Security Manager configuration control while blocking repo admins from toggling states. [Skill 2.1: Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)]

- **A:** Correct. enterprise policies prevent uncontrolled repo-admin license consumption while audit log streaming preserves tamper-evident compliance records across configuration and bypass events
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **D:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges

### Question 22 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). Secret Protection Push Protection evaluates commits pre-receive across CLI, IDE, web editor, and REST pushes, blocking high-confidence secrets before refs update in Git history. [Skill 2.2: Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)]

- **A:** Correct. blocking leaked credentials before the remote ref updates avoids costly key rotation, incident response, and Git history rewrites
- **B:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories

### Question 23 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). Enabling non-provider generic patterns and Copilot AI generic secret detection (`consuming Secret Protection AI credits on push`) detects unstructured secrets, though non-provider patterns cannot perform partner validity checks. [Skill 2.2: Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)]

- **A:** Correct. enabling non-provider and AI generic secret detection catches unstructured passwords and connection strings missed by vendor-prefix regexes (noting non-provider patterns lack partner validity checks)
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions

### Question 24 — `A, B` (Configure and use Secret Protection (formerly secret scanning))

Correct answers: A and B (are correct). Push Protection stops high-confidence secrets pre-receive before Git history exposure, and partner validity checks surface `Active` vs `Inactive` token status so responders rotate live keys first. [Skill 2.2: Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)]

- **A:** Correct. stopping secrets pre-receive prevents Git history contamination and emergency credential rotation
- **B:** Correct. Active validation status gives AppSec teams high-signal prioritization during incident triage
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **E:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement

### Question 25 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). Responders must confirm scope, immediately revoke and rotate the live credential at the provider, purge Git commit history (`git filter-repo` plus Support cache purge if needed), and close the alert as `Revoked`. [Skill 2.3: Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts)]

- **A:** Incorrect. using secret_scanning.yml to silence an active production credential leak hides the alert without revoking or rotating the compromised secret
- **B:** Incorrect. delaying credential revocation leaves attackers able to exploit copies harvested from webhooks, clones, or cached diffs while history is rewritten
- **C:** Correct. once a secret reaches Git history, revoking/rotating the live key comes first, followed by history rewrite/cache purge and marking the alert Revoked for auditability
- **D:** Incorrect. deleting a secret in a follow-up commit leaves the active credential exposed in prior Git commits, reflogs, and clones without revoking access

### Question 26 — `D` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: D (is correct). `Active` confirms the issuing partner verified the credential is still live right now and must be rotated immediately, after which responders can trigger an on-demand validity check to verify revocation. [Skill 2.3: Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **C:** Incorrect. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules
- **D:** Correct. knowing a leaked AWS, Stripe, or Slack token is still Active lets incident responders triage live compromises ahead of already-revoked tokens

### Question 27 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). Deleting `.env.prod` in a later commit leaves the secret intact inside earlier Git commits, clones, forks, and cached pull-request diffs, so immediate provider revocation remains mandatory. [Skill 2.3: Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts)]

- **A:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Correct. merely deleting a secret in a later commit leaves it readable in earlier commits; immediate revocation and rotation is mandatory
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 28 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). Delegated bypass for Push Protection restricts bypass approvals to designated visible teams, roles, or custom organization roles while logging every request, decision, and comment. [Skill 2.4: Configure role-based and delegated bypass policies in Secret Protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Correct. delegated bypass replaces ad-hoc writer self-bypasses with a structured request-and-approval workflow audited via webhooks and logs
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 29 — `D` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: D (is correct). Granting `Review and manage secret scanning bypass requests` in a custom organization role scopes Push Protection bypass approval rights with least privilege. [Skill 2.4: Configure role-based and delegated bypass policies in Secret Protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)]

- **A:** Incorrect. uploading CodeQL or third-party SARIF 2.1.0 findings from GitHub Actions requires least-privilege security-events: write permission
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Correct. granting Review and manage secret scanning bypass requests creates least-privilege Push Protection approvers without full Org Owner access

### Question 30 — `A, C` (Configure and use Secret Protection (formerly secret scanning))

Correct answers: A and C (are correct). Delegated bypass reviewers must be visible organization teams, standard admin/maintain roles, or custom roles (`never secret teams`), and every bypass event streams to `secret_scanning_alert_location` / bypass webhooks and audit logs. [Skill 2.4: Configure role-based and delegated bypass policies in Secret Protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)]

- **A:** Correct. delegated bypass centralizes exception approvals in visible accountable security teams or roles
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Correct. every bypass leaves an immutable audit trail linking the actor, commit, justification, and approver
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **E:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges

### Question 31 — `D` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: D (is correct). Creating `.github/secret_scanning.yml` with `paths-ignore:` (`up to 1,000 glob entries and <= 1 MB file size`) auto-closes user secret alerts in matching test fixture paths. [Skill 2.5: Configure Secret Protection alert recipients and path exclusions (.github/secret_scanning.yml) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning)]

- **A:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup
- **D:** Correct. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories

### Question 32 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). On public repositories, `.github/secret_scanning.yml` `paths-ignore` does not suppress partner pattern scanning—GitHub still notifies the token partner vendor for revocation—and files exceeding 1 MB ignore `secret_scanning.yml` entirely. [Skill 2.5: Configure Secret Protection alert recipients and path exclusions (.github/secret_scanning.yml) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning)]

- **A:** Correct. secret_scanning.yml silences noisy user alerts in synthetic fixture directories up to 1,000 paths / 1 MB while keeping real code paths protected
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 33 — `D` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: D (is correct). Repository Admins, Security Managers, and custom-role holders receive secret alerts by default, while assigning a secret alert (`or adding it to a secret campaign`) grants that `Write` developer temporary view access to only that assigned alert until unassigned. [Skill 2.5: Configure Secret Protection alert recipients and path exclusions (.github/secret_scanning.yml) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Correct. clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity

### Question 34 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). Administrators define the regex and sample test strings (`or Generate with AI`), run `Save and dry run` across org repos (`<=1,000` sample matches), refine surrounding context, and `Publish pattern` before enabling Push Protection. [Skill 2.6: Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning)]

- **A:** Correct. custom secret patterns require dry-run validation (up to 1,000 sample matches without creating live alerts) and publication before Push Protection can be enabled
- **B:** Incorrect. GitHub disables the Push Protection toggle until a custom pattern passes dry-run testing and is published, and broad untested regexes flood teams with false positives
- **C:** Incorrect. .gitignore does not configure Secret Protection, AI-generated regexes still require dry-run validation, and secret teams cannot be added to bypass lists
- **D:** Incorrect. Enterprise/Org custom patterns are configured in Org/Enterprise settings, and saving edits to an existing custom pattern closes alerts created by its prior version

### Question 35 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). Saving edits to a published custom secret pattern re-evaluates repositories and automatically closes alerts generated by the previous pattern version, while Enterprise-level custom patterns can only be edited by the user who created them. [Skill 2.6: Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning)]

- **A:** Correct. dry runs preview up to 1,000 historical matches without creating live alerts, and editing a published pattern automatically closes alerts generated by its previous version
- **B:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 36 — `A, C, F` (Configure and use Secret Protection (formerly secret scanning))

Correct answers: A, C, and F (are correct). Repositories support up to 100 custom patterns (`500 per org/enterprise`) validated via dry run before publishing, Push Protection can block published custom patterns pre-receive, and `.github/secret_scanning.yml` supports up to 1,000 `paths-ignore` globs under 1 MB. [Skill 2.6: Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning)]

- **A:** Correct. dry runs preview up to 1,000 historical matches without creating live alerts, and editing a published pattern automatically closes alerts generated by its previous version
- **B:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **C:** Correct. blocking leaked credentials before the remote ref updates avoids costly key rotation, incident response, and Git history rewrites
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **E:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **F:** Correct. secret_scanning.yml silences noisy user alerts in synthetic fixture directories up to 1,000 paths / 1 MB while keeping real code paths protected

### Question 37 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). Submitting resolved build-time dependency snapshots from CI via the `Dependency Submission API` (`alongside committed lockfiles where available`) populates full direct and transitive graphs for Advisory Database matching. [Skill 3.1: Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)]

- **A:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **D:** Correct. committing lockfiles plus submitting build-resolved snapshots gives GitHub complete direct and transitive dependency visibility

### Question 38 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). Calling `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`or clicking Export SBOM / running actions/attest-sbom`) exports the repository's direct and transitive dependency inventory in SPDX JSON format. [Skill 3.1: Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)]

- **A:** Incorrect. codeql github upload-results publishes externally generated SARIF 2.1.0 files to GitHub Code Scanning with exact ref and commit metadata
- **B:** Correct. the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Incorrect. the code-security configurations attach endpoint programmatically binds a Security Configuration to targeted or organization-wide repositories

### Question 39 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). A Dependency Graph SPDX SBOM lists upstream direct and transitive packages, versions, relationships, and licenses consumed *by* the repository—never external downstream `dependents`. [Skill 3.1: Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **D:** Correct. GitHub exports dependency inventories, versions, licenses, and transitive relationships in standard SPDX JSON (and never includes downstream external dependents)

### Question 40 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). Combining `EPSS` (`30-day real-world exploitation probability`), static `Reachability` call-path evidence, and `runtime` scope prioritizes the actively exploitable reachable package ahead of unreachable low-EPSS findings. [Skill 3.2: Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (auto-dismiss) rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **C:** Correct. combining EPSS exploit likelihood and static reachability with CVSS and runtime scope focuses engineering effort on genuinely exploitable dependencies
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 41 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). Filtering closed alerts with `resolution:auto-dismiss` surfaces every alert automatically dismissed by GitHub preset or custom Dependabot auto-triage rules, which also auto-reopen if dependency scope changes to runtime. [Skill 3.2: Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (auto-dismiss) rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules)]

- **A:** Incorrect. security-extended broadens vulnerability detection beyond default without adding non-security maintainability noise from security-and-quality
- **B:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **C:** Incorrect. filtering by has:deployment and runtime-risk:internet-exposed isolates alerts affecting live internet-reachable workloads
- **D:** Correct. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules

### Question 42 — `B, C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answers: B and C (are correct). Ranking alerts by `EPSS` + `Reachability` + `runtime` scope focuses remediation on exploitable code paths, and Dependabot auto-triage rules apply `resolution:auto-dismiss` *before* alert notifications fire (`with org rules overriding conflicting repo rules`). [Skill 3.2: Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (auto-dismiss) rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules)]

- **A:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **B:** Correct. high-EPSS reachable runtime vulnerabilities represent immediate real-world exploit risk compared with unreachable dev-only packages
- **C:** Correct. evaluating auto-triage rules prior to notifications eliminates alert fatigue while keeping alerts auditable and auto-reopenable
- **D:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **E:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 43 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). Dependabot security updates react to GitHub Advisory Database alerts on the default branch by opening PRs to the minimum patched version, whereas Dependabot version updates require `.github/dependabot.yml` to open scheduled freshness PRs across package ecosystems and `github-actions`. [Skill 3.3: Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Correct. security updates react to GitHub Advisory Database alerts on default-branch dependencies, whereas dependabot.yml keeps dependencies and github-actions current on a schedule
- **B:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **C:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **D:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure

### Question 44 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). When global `Dependabot security updates` stays enabled on a repository, Dependabot attempts PRs for all patchable alerts; it must be disabled so custom auto-triage `Open a pull request` rules selectively govern PR creation. [Skill 3.3: Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. When global `Dependabot security updates` stays enabled on a repository, Dependabot attempts PRs for all patchable alerts; it must be disabled so custom auto-triage `Open a pull request` rules selectively govern PR creation.
- **B:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **C:** Correct. when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules
- **D:** Incorrect. allow-licenses and deny-licenses are mutually exclusive inputs in dependency-review-action, and branch rulesets must require the check to block merging

### Question 45 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). Malware packages have no safe upgrade target (`so Dependabot never opens security PRs for malware`), and the `Dismiss package malware alerts` preset suppresses false-positive internal namespace collisions after verifying private registry pinning. [Skill 3.3: Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Correct. auto-triage rules suppress low-risk noise before notifications fire, auto-reopen if metadata/scope changes, and defer to organization rules when repo rules conflict
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names

### Question 46 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). Enable the Dependency Graph (`and Code Security on private repos`), add an `on: pull_request` workflow running `actions/dependency-review-action@v4`, configure `fail-on-severity` and `deny-licenses`, and enforce that workflow as a required status check in a branch ruleset. [Skill 3.4: Secure dependencies during development using pre-merge Dependency Review (dependency-review-action) for vulnerabilities and licenses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action)]

- **A:** Incorrect. dependabot.yml schedules dependency update PRs rather than gating developer PRs on license compliance; pre-merge gating requires dependency-review-action plus required checks
- **B:** Incorrect. dependency-review-action requires pull_request base/head diffs and an active Dependency Graph, and allow-licenses / deny-licenses are mutually exclusive
- **C:** Incorrect. private repositories require GitHub Code Security / GHAS for Dependency Review, contents: read suffices, and unenforced checks do not block merges
- **D:** Correct. Dependency Review compares PR base-vs-head manifests/lockfiles via the Dependency Graph and blocks vulnerable or non-compliant licenses when required on protected branches

### Question 47 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). `allow-licenses` and `deny-licenses` are mutually exclusive inputs in `dependency-review-action`; passing both causes the workflow step to fail validation. [Skill 3.4: Secure dependencies during development using pre-merge Dependency Review (dependency-review-action) for vulnerabilities and licenses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action)]

- **A:** Correct. allow-licenses and deny-licenses are mutually exclusive inputs in dependency-review-action, and branch rulesets must require the check to block merging
- **B:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. `allow-licenses` and `deny-licenses` are mutually exclusive inputs in `dependency-review-action`; passing both causes the workflow step to fail validation.
- **C:** Incorrect. each gzipped SARIF upload must be <=10 MB with a distinct category per language/tool/component and security-events: write permission
- **D:** Incorrect. when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules

### Question 48 — `B, E` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answers: B and E (are correct). Configure `fail-on-severity`, `fail-on-scopes`, and either `allow-licenses` OR `deny-licenses` on `pull_request`, and mark that job as a required status check inside an active branch protection rule or ruleset. [Skill 3.4: Secure dependencies during development using pre-merge Dependency Review (dependency-review-action) for vulnerabilities and licenses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Correct. without a required status check rule, a failing Dependency Review workflow warns on the PR without blocking merge
- **C:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **E:** Correct. Dependency Review blocks both vulnerable package versions and prohibited copyleft/unknown licenses on pull requests

### Question 49 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). Using `groups:` (`with patterns and update-types: [minor, patch]`) consolidates updates into single PRs, while `registries:` authenticated via `${{ secrets.<TOKEN> }}` stored in **Dependabot secrets** grants private feed access. [Skill 3.5: Configure advanced dependency update rules in dependabot.yml (grouping, ignore rules, update strategies, private registries) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference)]

- **A:** Correct. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets
- **B:** Incorrect. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup
- **C:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **D:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories

### Question 50 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). Setting `ignore:` (`with dependency-name and update-types: ["version-update:semver-major"]`) skips major bumps while `open-pull-requests-limit: 5` throttles concurrent open Dependabot PRs. [Skill 3.5: Configure advanced dependency update rules in dependabot.yml (grouping, ignore rules, update strategies, private registries) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference)]

- **A:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **B:** Correct. grouping related updates cuts CI/PR noise dramatically, while registries + Dependabot secrets authenticate Dependabot to private npm/NuGet/PyPI/Maven feeds
- **C:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 51 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). Adding `package-ecosystem: "github-actions"` with `directory: "/"` in `.github/dependabot.yml` keeps workflow action tags and pinned commit SHAs updated automatically. [Skill 3.5: Configure advanced dependency update rules in dependabot.yml (grouping, ignore rules, update strategies, private registries) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Correct. security updates react to GitHub Advisory Database alerts on default-branch dependencies, whereas dependabot.yml keeps dependencies and github-actions current on a schedule

### Question 52 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). Workflows triggered by Dependabot PRs receive a **read-only `GITHUB_TOKEN`** by default and can only read credentials stored in **`Dependabot secrets`** (`not standard Actions repository secrets on untrusted PR contexts`). [Skill 3.6: Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Correct. understanding Dependabot token/secret isolation, webhook automation, and Defender for Cloud / artifact-registry deployment context integrates supply-chain security safely into operations
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 53 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). Filtering Dependabot or Code Scanning views by `has:deployment` and `runtime-risk:internet-exposed` isolates vulnerabilities present in deployed internet-facing workloads. [Skill 3.6: Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON
- **C:** Incorrect. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules
- **D:** Correct. filtering by has:deployment and runtime-risk:internet-exposed isolates alerts affecting live internet-reachable workloads

### Question 54 — `B, C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answers: B and C (are correct). Dependabot-triggered workflows default to a read-only `GITHUB_TOKEN` with `Dependabot secrets` isolation, and Defender for Cloud / JFrog integrations enrich alerts with `has:deployment` and `runtime-risk:internet-exposed` context. [Skill 3.6: Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Correct. isolating Dependabot secrets and read-only default tokens protects repository secrets if a compromised upstream package alters build scripts
- **C:** Correct. production context pinpoints vulnerabilities actually running in internet-facing workloads rather than dead or archived repos
- **D:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **E:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 55 — `B` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: B (is correct). CodeQL extracts source code into a relational AST/CFG/dataflow database for deep interprocedural taint analysis, while third-party IaC/container scanners upload `SARIF 2.1.0` results into the same unified Code Scanning PR and alert experience. [Skill 4.1: Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)]

- **A:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **B:** Correct. CodeQL excels at deep interprocedural taint tracking across supported languages while SARIF 2.1.0 lets specialized IaC/container/linter tools report into one PR interface
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 56 — `A` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: A (is correct). Code Scanning rejects gzipped SARIF files over `10 MB`, requires `security-events: write`, and overwrites/stales sibling findings on the same commit when multiple uploads share the same SARIF `category`. [Skill 4.1: Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)]

- **A:** Correct. each gzipped SARIF upload must be <=10 MB with a distinct category per language/tool/component and security-events: write permission
- **B:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **C:** Incorrect. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts
- **D:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. Code Scanning rejects gzipped SARIF files over `10 MB`, requires `security-events: write`, and overwrites/stales sibling findings on the same commit when multiple uploads share the same SARIF `category`.

### Question 57 — `B, D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answers: B and D (are correct). Keep each gzip-compressed SARIF upload `<= 10 MB` (`<= 25,000` results, top `5,000` displayed by severity) and assign a unique `category` per module/tool while preserving `ruleId` and `partialFingerprints`. [Skill 4.1: Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Correct. distinct categories prevent multi-job uploads on the same commit from clobbering one another, while fingerprints track alerts across line shifts
- **C:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **D:** Correct. exceeding 10 MB gzipped rejects the upload outright, while noisy rule sets over 5,000 findings truncate lower-priority alerts
- **E:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)

### Question 58 — `B` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: B (is correct). Install the CodeQL CLI bundle on the CI agent, run `codeql database create` (`tracing the compiled C/C++ build`), run `codeql database analyze --format=sarif-latest`, and upload via `codeql github upload-results` with `--sarif`, `--ref`, and `--commit`. [Skill 4.2: Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (CodeQL CLI) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages)]

- **A:** Incorrect. Default Setup conflicts with custom/external CodeQL uploads, uploading SARIF requires security-events: write, and runs cap at 25,000 results (displaying top 5,000)
- **B:** Correct. external CI integrations create the semantic CodeQL database, execute query suites into SARIF 2.1.0 (`<=10 MB` gzipped), and upload results with `security_events` write auth
- **C:** Incorrect. CodeQL cannot upload raw source files or XML; a database must be created before analysis, and SARIF 2.1.0 uploads must be <=10 MB gzipped with target ref and commit SHA
- **D:** Incorrect. omitting distinct SARIF categories causes subsequent uploads for the same commit to overwrite/mark prior component results stale, and private repos require Code Security

### Question 59 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). CodeQL `Default Setup` and custom `Advanced Setup`CodeQL uploads cannot manage the same repository simultaneously; switching to `Advanced Setup` automatically disables Default Setup so `build-mode: manual` can run protobuf generation cleanly. [Skill 4.2: Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (CodeQL CLI) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages)]

- **A:** Incorrect. when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules
- **B:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. CodeQL `Default Setup` and custom `Advanced Setup`CodeQL uploads cannot manage the same repository simultaneously; switching to `Advanced Setup` automatically disables Default Setup so `build-mode: manual` can run protobuf generation cleanly.
- **C:** Incorrect. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release
- **D:** Correct. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts

### Question 60 — `C` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: C (is correct). Setting `build-mode: manual` (`and invoking the exact cmake/make build commands before codeql-action/analyze`) lets CodeQL trace custom C/C++, C#, Go, Kotlin, or Swift builds reliably, whereas `build-mode: none` only supports JS/TS, Python, Ruby, C#, and buildless Java. [Skill 4.2: Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (CodeQL CLI) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages)]

- **A:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **B:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets
- **C:** Correct. build-mode: manual traces exact custom C/C++, C#, Go, Java/Kotlin, or Swift compiler invocations when autobuild heuristics fail
- **D:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories

### Question 61 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). CodeQL traces taint from untrusted `source` through intermediate `steps` to sensitive `sink`, and classic CodeQL `Copilot Autofix` runs on pull requests and default branches under GitHub Code Security **without** requiring individual GitHub Copilot seats. [Skill 4.3: Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Correct. taint-flow paths pinpoint exact user-input sources and unvalidated sinks, while Copilot Autofix proposes context-aware diffs that must still pass CI and human review

### Question 62 — `C` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: C (is correct). Granting `permissions: { security-events: write, contents: read, actions: read }` provides least-privilege access to check out source code and publish SARIF results to Code Scanning. [Skill 4.3: Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Incorrect. granting Review and manage secret scanning bypass requests creates least-privilege Push Protection approvers without full Org Owner access
- **C:** Correct. uploading CodeQL or third-party SARIF 2.1.0 findings from GitHub Actions requires least-privilege security-events: write permission
- **D:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories

### Question 63 — `B, C` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answers: B and C (are correct). Classic CodeQL Copilot Autofix does not require paid Copilot seats or AI credits, and every Autofix diff must still be validated against the taint path (`source -> sink`), full CI test suites, a clean CodeQL re-scan, and human PR review. [Skill 4.3: Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning)]

- **A:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **B:** Correct. taint-flow paths pinpoint exact user-input sources and unvalidated sinks, while Copilot Autofix proposes context-aware diffs that must still pass CI and human review
- **C:** Correct. LLM-generated security fixes lower remediation friction dramatically, yet still require automated test and human semantic verification before merge
- **D:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **E:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 64 — `A` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: A (is correct). Code Scanning separates `security-severity` (`Critical`, `High`, `Medium`, `Low` derived from numeric `0.0–10.0` CVSS-like metadata) from non-security rule `problem.severity` (`Error`, `Warning`, `Note`), and security ruleset thresholds evaluate `security-severity`. [Skill 4.4: Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository)]

- **A:** Correct. branch protection rulesets filter security alerts by Critical/High/Medium/Low security-severity independently from non-security error/warning quality notes
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **D:** Incorrect. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules

### Question 65 — `C` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: C (is correct). CodeQL and compliant third-party scanners compute location-independent `partialFingerprints` (`primaryLocationLineHash`) alongside `ruleId` and `category` so alerts track cleanly across unrelated line movements. [Skill 4.4: Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **C:** Correct. compressing SARIF under 10 MB, preserving ruleId + partialFingerprints across runs, and setting unique category strings per tool/language/monorepo slice prevents rejected or overwritten alerts
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 66 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). If the underlying tainted code is removed (`closing the alert as fixed`) and later reintroduced—or re-triggered in a distinct untracked dataflow sink—Code Scanning opens/reopens the finding while keeping dismissal history auditable. [Skill 4.4: Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Correct. alert dismissals remain visible in REST/GraphQL APIs, webhooks, and audit logs, so teams must document rationale rather than hiding unverified risk

### Question 67 — `A` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: A (is correct). Referencing `.github/codeql/codeql-config.yml` (`paths-ignore`, `packs`, `queries`, `threat-models`) together with `CodeQL model packs` (`YAML data extensions defining custom sources, sinks, and neutral/sanitizer summaries`) teaches CodeQL internal APIs without forking standard `.ql` queries. [Skill 4.5: Optimize and troubleshoot Code Security operations with custom configurations, model packs, and build/performance diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning)]

- **A:** Correct. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets
- **D:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories

### Question 68 — `B` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: B (is correct). Split multi-language scans into parallel per-language matrix jobs, upgrade memory-intensive compiled builds to Larger GitHub-hosted or high-RAM self-hosted runners (`16–32+ GB RAM`), and exclude generated/vendor build artifacts via `paths-ignore` in `codeql-config.yml`. [Skill 4.5: Optimize and troubleshoot Code Security operations with custom configurations, model packs, and build/performance diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning)]

- **A:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **B:** Correct. model packs teach CodeQL custom internal framework sources/sanitizers/sinks without forking queries, while Adequate RAM/CPU runners and scoped paths resolve timeout/OOM failures
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 69 — `C` (Security operations: best practices, prioritization, and remediation)

Correct answer: C (is correct). Triage the report inside a draft Repository Security Advisory (`GHSA`), collaborate on and verify the patch in its temporary private fork, request a `CVE` and specify affected/patched semver ranges, then merge the release and publish the advisory. [Skill 5.1: Understand CVE, CWE, and GitHub Security Advisory (GHSA) concepts and execute end-to-end advisory remediation workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)]

- **A:** Incorrect. temporary private advisory forks intentionally disable GitHub Actions to prevent side-channel leaks, and publishing the GHSA is what powers downstream Dependabot alerts
- **B:** Incorrect. publishing zero-day exploit steps in public issues or public branches before a fix exists exposes all downstream users to active exploitation
- **C:** Correct. repository security advisories keep vulnerability details confidential in a temporary private fork until a verified patch is ready to release alongside coordinated GHSA/CVE disclosure
- **D:** Incorrect. secret_scanning.yml only filters secret-scanning paths and has nothing to do with patching or disclosing CWE/CVE code vulnerabilities

### Question 70 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). `CWE` classifies the abstract weakness category (`e.g., SQL Injection`), `CVE` uniquely identifies a publicly disclosed vulnerability instance in a specific product, and `GHSA` tracks advisories in the GitHub Advisory Database (`powering Dependabot alerts and CVE issuance as a CNA`). [Skill 5.1: Understand CVE, CWE, and GitHub Security Advisory (GHSA) concepts and execute end-to-end advisory remediation workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Correct. maintainers triage private reports inside draft GHSAs, patch silently in temporary private forks (where Actions stay disabled), request a CVE, and publish coordinated advisories
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names

### Question 71 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Temporary private advisory forks intentionally **disable GitHub Actions** (`to avoid side-channel leaks or billing surprises`), and pushing unpatched exploit tests to a public upstream branch exposes the zero-day prior to coordinated disclosure. [Skill 5.1: Understand CVE, CWE, and GitHub Security Advisory (GHSA) concepts and execute end-to-end advisory remediation workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)]

- **A:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **B:** Correct. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release
- **C:** Incorrect. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts
- **D:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. Temporary private advisory forks intentionally **disable GitHub Actions** (`to avoid side-channel leaks or billing surprises`), and pushing unpatched exploit tests to a public upstream branch exposes the zero-day prior to coordinated disclosure.

### Question 72 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). Enforce an organization branch ruleset with `Require code scanning results` blocking new `High`/`Critical` PR findings while triaging existing default-branch backlogs using `has:deployment`, `runtime-risk:internet-exposed`, `EPSS`, and `Reachability`. [Skill 5.2: Define, prioritize, and enforce severity rulesets and production-context prioritization at scale | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)]

- **A:** Correct. combining runtime deployment exposure with pre-merge High/Critical blocking stops alert growth while burning down real internet-exposed production risk first
- **B:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 73 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Any new pull-request Code Scanning alert with `security-severity` of `High` or `Critical`—or any non-security rule with `problem.severity` of `Error`—reported by the required scanning tool will block merging. [Skill 5.2: Define, prioritize, and enforce severity rulesets and production-context prioritization at scale | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Correct. branch protection rulesets filter security alerts by Critical/High/Medium/Low security-severity independently from non-security error/warning quality notes
- **C:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **D:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions

### Question 74 — `A, C` (Security operations: best practices, prioritization, and remediation)

Correct answers: A and C (are correct). Ingest deployment telemetry (`Defender for Cloud / JFrog / CI APIs`) to filter `has:deployment` + `runtime-risk:internet-exposed` alerts, and pilot new organization rulesets in `Evaluate` mode before flipping enforcement to `Active`. [Skill 5.2: Define, prioritize, and enforce severity rulesets and production-context prioritization at scale | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)]

- **A:** Correct. production context pinpoints vulnerabilities actually running in internet-facing workloads rather than dead or archived repos
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Correct. Evaluate mode surfaces missing scans or noisy rules safely without halting production releases on day one
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **E:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)

### Question 75 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). Filter high-risk default-branch alerts in Security Overview, create a Security Campaign (`<=1,000` alerts) with a target due date and named security contact, generate Copilot Autofix diffs (`or assign batches of <=25 alerts to @copilot`), and verify CI before merging. [Skill 5.3: Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/manage-security-alerts/best-practices-for-participating-in-a-security-campaign)]

- **A:** Correct. Security Campaigns group high-risk default-branch alerts around a dedicated security contact and accelerate developer burndown with Copilot Autofix or @copilot draft PRs
- **B:** Incorrect. disabling scanners or bulk-dismissing unreviewed findings hides real production vulnerabilities rather than remediating security debt
- **C:** Incorrect. code security campaigns target default-branch alerts (up to 1,000 per campaign) with a named contact, and developers need write access plus passing CI checks to merge fixes
- **D:** Incorrect. agentic @copilot campaign assignments cap at 25 alerts per batch (opening a PR for human/CI verification), and Copilot cannot rotate external cloud provider IAM credentials

### Question 76 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). Security Campaign managers can assign up to `25` alerts at a time to `@copilot` (`consuming Code Security AI credits`), which opens draft pull requests for human review and CI validation. [Skill 5.3: Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/manage-security-alerts/best-practices-for-participating-in-a-security-campaign)]

- **A:** Correct. grouping related CWEs into focused campaigns builds developer remediation momentum while Copilot Autofix and @copilot PR batches cut manual toil
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 77 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). Classic CodeQL `Copilot Autofix` on PRs and default branches is included with GitHub Code Security without consuming AI credits, whereas agentic `@copilot` campaign remediation, `AI Scan`, and push-time AI generic secret detection draw from included/metered AI credit pools. [Skill 5.3: Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/manage-security-alerts/best-practices-for-participating-in-a-security-campaign)]

- **A:** Correct. classic CodeQL Copilot Autofix does not consume AI credits, whereas agentic autofix / AI Scan and AI push secret scanning draw from included or metered AI credit pools
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 78 — `C` (Security operations: best practices, prioritization, and remediation)

Correct answer: C (is correct). Configuring `queries: security-extended` runs all `default` high-precision security queries plus medium-precision security rules while omitting the non-security maintainability rules found in `security-and-quality`. [Skill 5.4: Customize CodeQL query suites, multi-repository variant analysis, and risk-profile-tailored security detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites)]

- **A:** Incorrect. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Correct. security-extended broadens vulnerability detection beyond default without adding non-security maintainability noise from security-and-quality
- **D:** Incorrect. filtering by has:deployment and runtime-risk:internet-exposed isolates alerts affecting live internet-reachable workloads

### Question 79 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). `Multi-Repository Variant Analysis (MRVA)` in the CodeQL VS Code extension dispatches custom `.ql` queries via GitHub Actions against up to 1,000 repositories with pre-built CodeQL databases. [Skill 5.4: Customize CodeQL query suites, multi-repository variant analysis, and risk-profile-tailored security detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Correct. security-extended expands vulnerability coverage beyond high-precision default rules, while MRVA hunts novel zero-day patterns across up to 1,000 org repositories simultaneously
- **C:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 80 — `D` (Security operations: best practices, prioritization, and remediation)

Correct answer: D (is correct). Adding `threat-models: [remote, local]` in `codeql-config.yml` instructs CodeQL to treat local CLI arguments, environment variables, and local file reads as untrusted taint sources alongside remote network inputs. [Skill 5.4: Customize CodeQL query suites, multi-repository variant analysis, and risk-profile-tailored security detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Correct. model packs teach CodeQL custom internal framework sources/sanitizers/sinks without forking queries, while Adequate RAM/CPU runners and scoped paths resolve timeout/OOM failures

### Question 81 — `C` (Security operations: best practices, prioritization, and remediation)

Correct answer: C (is correct). Create a custom repository role inheriting `Write` (`or Read`) with fine-grained permissions to view/dismiss Code Scanning and Dependabot alerts, while keeping org-wide posture and Security Configurations with the `Security Manager` role. [Skill 5.5: Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **C:** Correct. clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 82 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Restrict ruleset bypass actors to a tight emergency role or deploy-approver team (`or require pull-request review / delegated bypass approval`) and monitor ruleset/push bypass events continuously in the organization audit log. [Skill 5.5: Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Correct. delegated bypass replaces ad-hoc writer self-bypasses with a structured request-and-approval workflow audited via webhooks and logs
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 83 — `B, D` (Security operations: best practices, prioritization, and remediation)

Correct answers: B and D (are correct). Use `Security Manager` plus granular custom alert roles (`understanding single-alert elevation when assigning secret alerts to writers`) and validate cross-repo rulesets in `Evaluate` mode before `Active` enforcement. [Skill 5.5: Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Correct. Evaluate mode surfaces missing scans or noisy rules safely without halting production releases on day one
- **C:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **D:** Correct. clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity
- **E:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges

### Question 84 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). Enable Push Protection (`pre-receive secret block`), `actions/dependency-review-action@v4` (`PR dependency/license diff check`), and PR `CodeQL` scanning with `Copilot Autofix` (`pre-merge SAST remediation`). [Skill 5.6: Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Correct. combining all three shift-left controls prevents new security debt from ever landing on the default branch
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 85 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). `Dependency Review` (`actions/dependency-review-action@v4`) diffs base-vs-head manifests and lockfiles on the pull request to flag newly introduced transitive vulnerabilities and prohibited licenses prior to merge. [Skill 5.6: Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **B:** Correct. Dependency Review inspects PR manifest/lockfile diffs before merge and fails the check when newly introduced packages breach vulnerability or license policies
- **C:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 86 — `B, D, F` (Security operations: best practices, prioritization, and remediation)

Correct answers: B, D, and F (are correct). Blocking secrets pre-receive with Push Protection, gating PR manifest/license diffs with `dependency-review-action@v4`, and validating CodeQL `Copilot Autofix` patches through CI tests and human review complete a shift-left PR pipeline. [Skill 5.6: Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Correct. Dependency Review blocks both vulnerable package versions and prohibited copyleft/unknown licenses on pull requests
- **C:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **D:** Correct. LLM-generated security fixes lower remediation friction dramatically, yet still require automated test and human semantic verification before merge
- **E:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **F:** Correct. stopping secrets pre-receive prevents Git history contamination and emergency credential rotation

### Question 87 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). Verify active-committer license headroom (`or metered budget`), create/select Security Configurations, attach them to repository tiers via custom properties with `Apply to new repositories` enabled, and set `Enforced` to prevent drift. [Skill 6.1: Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories)]

- **A:** Incorrect. exceeding volume committer licenses blocks enablement on additional/new private repos, and features left as Not set remain editable by repository admins even under Enforced configurations
- **B:** Incorrect. manual per-repo changes do not scale or prevent configuration drift, and granting Organization Owner violates least privilege when Security Manager / Security Configurations exist
- **C:** Incorrect. standalone GHES uses volume/subscription licensing (not metered billing) and requires GitHub Connect for Advisory DB sync, while transferred repos must be explicitly targeted by configurations
- **D:** Correct. rolling out Security Configurations verifies committer license capacity first, targets repo tiers via custom properties, covers newly created repos, and locks drift with Enforced mode

### Question 88 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). `GHEC` supports both metered and volume licensing plus cloud-hosted AI features (`Copilot Autofix`, AI generic secret detection), whereas `GHES` uses volume/subscription licensing and requires `GitHub Connect` to sync the GitHub Advisory Database and deduplicate hybrid committer seats. [Skill 6.1: Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Correct. Security Configurations eliminate manual repo drift on GHEC and GHES, while hybrid enterprises link GHES to GHEC via GitHub Connect for Advisory DB updates and committer seat deduplication

### Question 89 — `B` (GitHub Security suites administration)

Correct answer: B (is correct). No—`Apply to new repositories` applies to newly created or newly forked repositories in the organization, whereas **transferred** repositories do not automatically inherit that default and must have the Security Configuration explicitly attached. [Skill 6.1: Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Correct. understanding Enforced vs Unenforced inheritance, transferred-repo gaps, 90-day active committer deduplication, and hard budgets on metered SKUs/AI credits prevents surprise overages or lockouts
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers

### Question 90 — `B` (GitHub Security suites administration)

Correct answer: B (is correct). Even inside an `Enforced` Security Configuration, any feature left as `"Not set"` remains unlocked and editable by repository administrators; only rows explicitly set to `Enabled` or `Disabled` are locked. [Skill 6.2: Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security)]

- **A:** Incorrect. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts
- **B:** Correct. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **C:** Incorrect. when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules
- **D:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. Even inside an `Enforced` Security Configuration, any feature left as `"Not set"` remains unlocked and editable by repository administrators; only rows explicitly set to `Enabled` or `Disabled` are locked.

### Question 91 — `A` (GitHub Security suites administration)

Correct answer: A (is correct). Together they consume **1** license seat (`Priya` only): licenses count unique human accounts pushing commits to at least one enabled private/internal repository within the rolling **90-day** window, deduplicated across the enterprise, excluding built-in bots like `dependabot[bot]`. [Skill 6.2: Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security)]

- **A:** Correct. understanding Enforced vs Unenforced inheritance, transferred-repo gaps, 90-day active committer deduplication, and hard budgets on metered SKUs/AI credits prevents surprise overages or lockouts
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers

### Question 92 — `C, E` (GitHub Security suites administration)

Correct answers: C and E (are correct). Active-committer seats deduplicate each unique human committer over a rolling 90-day window (`syncing GHEC + GHES via GitHub Connect`), and administrators can cap metered spend on `Code Security AI credits` and `Secret Protection AI credits` with hard budgets (`while noting 100% volume-seat exhaustion prevents auto-enabling GHAS on new repos`). [Skill 6.2: Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Correct. classic CodeQL Copilot Autofix does not consume AI credits, whereas agentic autofix / AI Scan and AI push secret scanning draw from included or metered AI credit pools
- **D:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **E:** Correct. a developer pushing to 50 GHAS-enabled repos in an enterprise consumes only one active-committer license seat over the rolling 90-day window

### Question 93 — `A` (GitHub Security suites administration)

Correct answer: A (is correct). Streaming the Enterprise Audit Log (`capturing security_configuration.*, secret_scanning_push_protection_bypass, repository_ruleset.*, and alert dismissal events`) to an immutable SIEM (`such as Microsoft Sentinel or Splunk`) provides continuous compliance evidence. [Skill 6.3: Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise)]

- **A:** Correct. enterprise policies prevent uncontrolled repo-admin license consumption while audit log streaming preserves tamper-evident compliance records across configuration and bypass events
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 94 — `A` (GitHub Security suites administration)

Correct answer: A (is correct). No—an enterprise-enforced Security Configuration locks governed settings from override by repository administrators and organization owners beneath the enterprise policy boundary. [Skill 6.3: Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise)]

- **A:** Correct. enterprise policies prevent uncontrolled repo-admin license consumption while audit log streaming preserves tamper-evident compliance records across configuration and bypass events
- **B:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers

### Question 95 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). Combine Push Protection `delegated bypass` (`requiring approval from a dedicated visible security reviewer role`) with Organization Rulesets whose bypass list is restricted to audited emergency break-glass roles. [Skill 6.3: Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Correct. delegated bypass replaces ad-hoc writer self-bypasses with a structured request-and-approval workflow audited via webhooks and logs

### Question 96 — `B` (GitHub Security suites administration)

Correct answer: B (is correct). Assigning the organization **`Security Manager`** role grants org-wide Security Overview, alert triage, and Security Configuration management without granting source-code write or Organization Owner billing privileges. [Skill 6.4: Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization)]

- **A:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **B:** Correct. Security Manager and fine-grained custom repository roles grant AppSec and security champions exact triage permissions without over-provisioning Repository Admin or code-push rights
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 97 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). Create a custom repository role (`inheriting Read`) adding only the fine-grained `View code scanning alerts` permission (`omitting dismiss and secret-scanning permissions`). [Skill 6.4: Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **C:** Correct. Security Manager and fine-grained custom repository roles grant AppSec and security champions exact triage permissions without over-provisioning Repository Admin or code-push rights
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 98 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). By default on private repositories, users with `Write` access can view Code Scanning (`and Dependabot`) alerts on PRs/branches, whereas raw Secret Protection alerts default to Repository `Admin`, `Security Manager`, Organization Owners, or granted custom roles (`plus temporary single-alert assignees`). [Skill 6.4: Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization)]

- **A:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **B:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **C:** Correct. clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 99 — `B` (GitHub Security suites administration)

Correct answer: B (is correct). Calling `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`passing scope: "selected" and selected_repository_ids`) attaches a Security Configuration programmatically at scale. [Skill 6.5: Enforce default or approved custom CodeQL workflows and automate large-scale security governance via REST and GraphQL APIs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/rest/code-security/configurations)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Correct. the code-security configurations attach endpoint programmatically binds a Security Configuration to targeted or organization-wide repositories
- **C:** Incorrect. codeql github upload-results publishes externally generated SARIF 2.1.0 files to GitHub Code Scanning with exact ref and commit metadata
- **D:** Incorrect. the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON

### Question 100 — `A, C` (GitHub Security suites administration)

Correct answers: A and C (are correct). Enforce centrally governed Required Workflows / Organization `Require code scanning results` rulesets (`piloted via Evaluate -> Active`), and query organization/enterprise-level REST endpoints (`GET /orgs/{org}/code-scanning/alerts`, `/secret-scanning/alerts`, `/dependabot/alerts`) for single-stream telemetry. [Skill 6.5: Enforce default or approved custom CodeQL workflows and automate large-scale security governance via REST and GraphQL APIs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/rest/code-security/configurations)]

- **A:** Correct. combining Rulesets with REST/GraphQL security configuration and org-level alert APIs automates compliance reporting and zero-drift enforcement across thousands of repositories
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Correct. Evaluate mode surfaces missing scans or noisy rules safely without halting production releases on day one
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **E:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
