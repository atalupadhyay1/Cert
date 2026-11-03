# Microsoft / GitHub Exam GH-500: GitHub Advanced Security — Full-Length Mock Exam 3

**Theme:** Supply Chain Security, SPDX SBOMs, EPSS, Auto-Triage Rules, dependabot.yml & Dependency Review  
**Credential:** `GitHub Advanced Security` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `July 2026 (Last updated May 14, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-500 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Advanced Security documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Describe GitHub Security suites, features, and ecosystem (15–20% official weight · 18 questions)

### 1. VerdantRx Diagnostics hosts 38 private clinical services (`hl7-fhir-broker`, `patient-consent-api`) on `GitHub Enterprise Cloud` and wants to start with Secret Protection on all 38 repos while enabling Code Security only on its 12 externally facing APIs. How do GitHub's standalone SKUs support this?

- **A.** Standalone `GitHub Secret Protection` and `GitHub Code Security` SKUs (`purchasable separately or together on GitHub Team and GitHub Enterprise`, alongside legacy bundled GHAS)
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses

### 2. VerdantRx Diagnostics' HIPAA Security Officer is mapping controls across ePHI credentials, custom `.NET` injection vulnerabilities in `assay-analyzer-dotnet`, and vulnerable Python bioinformatics packages in `crispr-pipeline-py`. How do GitHub's three security pillars divide these concerns?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** `Secret Protection` (`secret scanning + push protection`), `Code Security` (`CodeQL/SARIF SAST + Copilot Autofix`), and `Supply Chain Security` (`Dependency Graph, Dependabot, Dependency Review & SBOMs`)
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 3. VerdantRx Diagnostics is preparing a HIPAA board briefing explaining what capabilities come with `GitHub Secret Protection` versus `GitHub Code Security`. Which two descriptions are accurate? Select two.

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** `GitHub Secret Protection` prevents and detects leaked credentials via `Push Protection`, `secret scanning`, `validity checks`, custom patterns, and AI generic secret detection
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **E.** `GitHub Code Security` finds and fixes code and dependency risks via `CodeQL` / `SARIF` code scanning, `Copilot Autofix`, `Dependency Review` on private repos, and `Security Campaigns`

### 4. VerdantRx Diagnostics open-sourced a FHIR schema validator (`fhir-r4-lint`) on public GitHub.com while running `radiology-dicom-gw` as an `internal` repository in GitHub Enterprise. How do security feature entitlements compare?

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Core features (`secret scanning, push protection, Dependency Graph, Dependabot, CodeQL default setup & Dependency Review`) are free on `public` GitHub.com repos; `private/internal` repos require licensed SKUs where applicable
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners

### 5. VerdantRx Diagnostics' CISO tagged 28 repositories with custom property `hipaa_ephi:true` and wants one executive screen comparing open critical alerts, Dependabot coverage, and active campaign progress across only those ePHI repositories (`____`). Where is this available?

- **A.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **B.** `Security Overview` (`Organization & Enterprise Risk, Coverage, Campaigns, Code scanning, Secret scanning & Dependabot dashboards` filterable by team, topic, or custom property)
- **C.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`
- **D.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations

### 6. VerdantRx Diagnostics recently acquired a specialty pathology lab running a separate GitHub org without security add-ons and wants an immediate pre-license check for leaked EHR credentials and sample SAST vulnerabilities. Which native option (`____`) should the Org Owner run?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Organization `free security risk assessment` (`scanning org repos for leaked secrets and up to 20 active repositories for CodeQL vulnerabilities + Copilot Autofix preview`)
- **D.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect

### 7. On `ehr-sync-adapter`, why did Secret Protection catch an Epic OAuth client secret accidentally pasted into a Postman `.json` collection while CodeQL caught an insecure XML external entity (`XXE`) parser in `FhirXmlReader.cs`?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** `Secret Protection` matches structured/high-entropy/AI secret tokens across Git history & pushes, whereas `Code Security (CodeQL)` traces semantic AST/dataflow vulnerabilities (`including hardcoded-credential sinks`)
- **D.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config

### 8. VerdantRx Diagnostics wants to block engineers from pushing HL7 TLS keys into `hl7-fhir-broker` and automatically propose patches for XSS bugs on `pathology-viewer-ts` pull requests. Proposed solution: Create `.github/secret_scanning.yml` with `paths-ignore: ["certs/**"]` and leave Push Protection and CodeQL disabled. Does this meet the goal?

- **A.** No — `.github/secret_scanning.yml` `paths-ignore` only auto-closes post-push user alerts (`<=1,000` paths / `<=1 MB`) and neither revokes keys nor replaces Push Protection / public partner alerts
- **B.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **C.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)
- **D.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)

### 9. How do Push Protection, Dependency Review, and CodeQL work in sequence during a developer's feature workflow on `specimen-barcode-svc`?

- **A.** Layer `Push Protection` (`pre-receive`), `actions/dependency-review-action` (`PR manifest/license gate`), and `CodeQL` PR checks (`with Copilot Autofix`) so secrets, vulnerable packages, and taint flaws fail pre-merge
- **B.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step

### 10. VerdantRx Diagnostics is transitioning `reagent-lot-tracker` from an annual external HIPAA penetration test to continuous shift-left security across GitHub. Which ordered 4-step workflow implements prevention-first SDLC governance?

- **A.** Merge PRs without checks to main → run weekly manual secret scans → disable Push Protection to avoid developer friction → export CSVs quarterly without remediating open alerts
- **B.** Dismiss all PR alerts automatically → merge vulnerable dependencies → run Dependency Review only on archived branches → rely on gitignore to revoke leaked API tokens
- **C.** Apply Copilot Autofix before running CodeQL → run Push Protection only after merging to main → skip Dependency Review on lockfiles → delete Security Overview roles
- **D.** Block secrets pre-receive via Push Protection → run Dependency Review & CodeQL on the PR → apply Copilot Autofix or patch vulnerable packages before merge → monitor default-branch advisories in Security Overview

### 11. What operational failure occurs when VerdantRx Diagnostics relies solely on a pre-deployment release gate instead of running Push Protection and PR-level CodeQL/Dependency Review on `patient-consent-api`?

- **A.** Prevention-first (`Push Protection + IDE/PR Dependency Review + PR CodeQL with Copilot Autofix`) stops defects before Git history/merge, whereas late release-only gates cause expensive rework
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 12. VerdantRx Diagnostics' AppSec team wants clinical platform squads to remediate 310 legacy SSRF and deserialization findings on default branches within 6 weeks under a named security lead. Which GitHub Code Security feature (`____`) structures this?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** `Security Campaigns` (`targeted, time-bound initiatives grouping up to 1,000 default-branch alerts with a named security contact and Copilot Autofix support`)
- **D.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions

### 13. An external HITRUST assessor asks VerdantRx Diagnostics what happens when a developer dismisses a CodeQL or Dependabot alert as `Won't fix` on `clia-compliance-bot`. How does GitHub preserve auditability?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** Dismissing an alert requires a structured closure reason (`False positive`, `Used in tests`, `Won't fix`) plus an audit-logged justification comment—and never deletes commits or revokes keys

### 14. A lab-integration developer pushed a live Snowflake service-account password into `crispr-pipeline-py` and opened a PR removing the line 10 minutes later. Proposed solution: Merge the removal PR and dismiss the Secret Protection alert as `Won't fix` without rotating the Snowflake credential. Does this secure the account?

- **A.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **B.** No — Code Scanning rejects gzip-compressed SARIF files larger than `10 MB` (`and overwrites prior alerts when multiple matrix uploads share an identical SARIF category on one commit`)
- **C.** No — dismissing a Secret Protection alert or deleting the line in a new commit leaves the live credential active and exposed in prior Git history (`revoke & rotate first, then purge history`)
- **D.** No — `actions/dependency-review-action` forbids specifying `allow-licenses` and `deny-licenses` together, and fails to block merges unless marked as a required status check on `pull_request`

### 15. VerdantRx Diagnostics wants to ensure alert dismissals on ePHI microservices satisfy HIPAA audit-control standards. Which two controls belong in its alert governance policy? Select two.

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Require an accurate dismissal reason (`False positive`, `Used in tests`, or `Won't fix`) with a reviewer-auditable justification comment whenever dismissing an alert
- **E.** Monitor dismissed and open alert trends centrally in `Security Overview` and `Audit Logs` (`repository_vulnerability_alert`, `secret_scanning_alert`, `code_scanning_alert`)

### 16. In VerdantRx Diagnostics' GHEC organization, which persona should own committer license budgets and enterprise policies, which should run Security Overview campaigns, and which should author code/lockfile fixes?

- **A.** Shared security model: `Admins` govern licensing/Security Configurations, `Security Managers` monitor Security Overview/campaigns/policies, and `Developers` remediate PR & campaign findings
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 17. How does combining least-privilege alert visibility with Push Protection `delegated bypass` protect ePHI tokens on `hl7-fhir-broker`?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Least-privilege alert access (`Write/Maintain/Admin/Security Manager` or custom roles) paired with `delegated bypass` so designated reviewers audit push-protection exceptions
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 18. VerdantRx Diagnostics' clinical security charter covers DevSecOps role boundaries, controlled push-protection exceptions, and risk-based supply-chain triage. Which three statements align with official GitHub guidance? Select three.

- **A.** Prioritize `Dependabot alerts` combining `EPSS` (`30-day exploitation probability`), `CVSS` severity, `Reachability` call-path analysis (`Reachable` vs `Unreachable`), `runtime` scope, and `patch availability`
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Least-privilege alert access (`Write/Maintain/Admin/Security Manager` or custom roles) paired with `delegated bypass` so designated reviewers audit push-protection exceptions
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **E.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **F.** Shared security model: `Admins` govern licensing/Security Configurations, `Security Managers` monitor Security Overview/campaigns/policies, and `Developers` remediate PR & campaign findings

---

## Domain 2 — Configure and use Secret Protection (formerly secret scanning) (15–20% official weight · 18 questions)

### 19. VerdantRx Diagnostics wants Secret Protection (`secret scanning + push protection + validity checks`) enabled across all 38 current clinical repos and automatically applied whenever platform automation creates a new service repo. Which setting (`____`) achieves this?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Enable `GitHub Secret Protection` (`secret scanning + push protection`) via Organization/Enterprise `Security Configurations` (`with Apply to new repositories`) or Repository `Settings -> Advanced Security`
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 20. What happens if a developer pushes a Slack bot token to VerdantRx's public `fhir-r4-lint` repository versus pushing a Slack bot token to the private `ehr-sync-adapter` repository (`with Secret Protection enabled`)?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** On `public` repos, partner patterns run free and auto-notify token providers for revocation; on `private/internal` repos (`with Secret Protection`), alerts notify repo/org users (`plus optional validity checks`)

### 21. VerdantRx Diagnostics transferred a private bioinformatics repository (`ngs-demux-worker`) from a research partner's organization into `verdantrx-cloud`, where `Apply to new repositories` is enabled on the default Security Configuration. Is Secret Protection automatically attached to `ngs-demux-worker`?

- **A.** `Enforced` Security Configurations lock enabled/disabled settings (`except fields set to "Not set"`), while private/internal repos consume `90-day unique active committer` seats (`plus metered AI credits for AI Scan/generic secrets`)
- **B.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 22. A data scientist at VerdantRx Diagnostics runs `git push` from VS Code containing a hardcoded Hugging Face API token in `crispr-pipeline-py` and receives a pre-receive rejection listing the file path and commit SHA. Which Secret Protection feature (`____`) blocked the push?

- **A.** `Push Protection` intercepts supported high-confidence and published custom secrets pre-receive during `git push` (`CLI, IDE, web editor & REST API`), blocking the secret from entering Git history
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 23. `radiology-dicom-gw` connects to hospital PACS servers using custom HL7 passwords (`pacs_admin_password = "..."`) that have no cloud-vendor prefix. Which two Secret Protection features detect these credentials, and what AI credit pool applies at push time?

- **A.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **B.** `Non-provider / generic pattern scanning` (`private keys, DB connection strings`) plus `Copilot AI generic secret detection` (`unstructured passwords/keys`, consuming `Secret Protection AI credits` on push)
- **C.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 24. VerdantRx Diagnostics' HIPAA incident team wants zero new cloud keys landing in Git history and immediate confirmation of which historical leaked keys are still live. Which two Secret Protection capabilities deliver this? Select two.

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** `Push Protection` blocks high-confidence partner and published custom secrets pre-receive during `git push` before commits land on GitHub
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** `Validity checks` verify supported partner tokens (`Active` vs `Inactive`) so responders remediate live exploitable credentials immediately
- **E.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 25. Secret Protection flags an `Active` Azure Key Vault client secret committed to `patient-consent-api` on an internal feature branch. What is the correct four-step remediation sequence?

- **A.** Run git filter-repo first while leaving the production key active for 30 days → disable Secret Protection to clear UI banners → rotate the key only if an outage occurs → skip audit notes
- **B.** Dismiss the alert as Won't fix → delete the line in a new commit while keeping the live key active → add the file to .gitignore → assume old commits are unreadable
- **C.** Confirm alert validity & blast radius → revoke and rotate the compromised credential at the provider → purge commit history (`git filter-repo`) & contact Support if cached PRs remain → resolve the alert as Revoked
- **D.** Add paths-ignore in .github/secret_scanning.yml to auto-close the live production key alert → keep the credential unrotated → merge to main → archive the audit log

### 26. After VerdantRx Diagnostics rotates a leaked Stripe test-environment key flagged as `Active` in `specimen-barcode-svc`, how can the responder confirm inside GitHub that the key is now dead before resolving the alert?

- **A.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **B.** `Validity checks` query partner token endpoints (`displaying Active, Inactive, or Unknown`) so responders prioritize live `Active` credentials first
- **C.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 27. A contractor pushed a production PostgreSQL URI to `reagent-lot-tracker`, force-pushed an amended commit (`git commit --amend && git push --force`) 3 minutes later, and claims rotation is unnecessary. Why does VerdantRx's AppSec team still mandate immediate password rotation?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Treat every committed secret as compromised: `revoke & rotate at the issuing provider immediately`, rewrite Git history (`git filter-repo`), purge cached views via Support if needed, and resolve as `Revoked`
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 28. VerdantRx Diagnostics wants developers who encounter a false-positive Push Protection block on `assay-analyzer-dotnet` to submit a justification reviewed by the Clinical Security group before the push is allowed through (`for up to 7 days on approval`). Which feature (`____`) implements this?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** `Delegated bypass for push protection` (`granting Specific roles, visible teams, or custom roles with "Review and manage secret scanning bypass requests" authority—never secret teams`)
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 29. VerdantRx Diagnostics wants HIPAA Privacy Officers to review and approve/deny Push Protection bypass requests without giving them `Security Manager` power to edit CodeQL or Dependabot settings. Which custom organization role permission (`____`) should be selected?

- **A.** `Review and manage secret scanning bypass requests` (`fine-grained organization role permission for Push Protection delegated bypass`)
- **B.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **C.** `permissions: { security-events: write, contents: read, actions: read }` on `github/codeql-action/upload-sarif@v3`
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 30. While configuring Push Protection delegated bypass for `verdantrx-cloud`, an admin tries adding a hidden **secret team** (`@verdantrx/stealth-sec`) and asks how approvals are logged. Which two statements are true? Select two.

- **A.** Audit every Push Protection bypass request, approval, and exemption via `secret_scanning_push_protection_bypass` audit events, alert timelines, and webhooks
- **B.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **C.** Assign `Specific roles, visible teams, or custom org roles` (`never secret teams`) to the Push Protection delegated bypass list to review and approve contributor bypass requests
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **E.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 31. `hl7-fhir-broker` includes 180 synthetic HL7 v2 sample messages with fake bearer strings inside `test/hl7-samples/**`. Which YAML file and key (`____`) suppresses user Secret Protection alerts in that folder?

- **A.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`
- **D.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)

### 32. Why did Secret Protection still trigger an alert on `test/hl7-samples/giant_dump.hl7` (`2.4 MB`) in `hl7-fhir-broker` even though `test/hl7-samples/**` is listed under `paths-ignore` in `.github/secret_scanning.yml`?

- **A.** `.github/secret_scanning.yml` with `paths-ignore:` (`up to 1,000 glob entries and <= 1 MB file size`) auto-closing user alerts in test/docs paths (`without suppressing public-repo partner revocation alerts`)
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config

### 33. On `pathology-viewer-ts`, a Security Manager assigns Secret Protection alert `#14` to frontend developer Elena (`who has only standard Write repository access`). Which Secret Protection alerts can Elena view?

- **A.** Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 34. VerdantRx Diagnostics issues analyzer API keys formatted as `VRX_LAB_[A-HJ-NP-Z2-9]{28}` and wants org-wide Push Protection without false-positive noise. What is the exact four-step custom pattern deployment sequence?

- **A.** Commit custom regexes into .gitignore → skip dry runs because AI regexes are deterministic → assign secret teams to delegated bypass → expect partner validity checks on custom tokens
- **B.** Enable Push Protection before publishing the pattern → publish an untested `.*` wildcard regex org-wide → review 50,000 live developer alerts → run a dry run afterward
- **C.** Publish the pattern on a personal Free repo → expect Enterprise-wide enforcement automatically → edit the pattern assuming prior version alerts stay open → skip test strings
- **D.** Define pattern name, regex & test strings (`or Generate with AI`) → run `Save and dry run` across representative repos → refine regex/context to eliminate false positives → `Publish pattern` & enable Push Protection

### 35. When testing a new Enterprise-level custom secret pattern across VerdantRx Diagnostics' multi-org enterprise (`versus an Organization-level custom pattern`), how many repositories can an Enterprise dry run scan (`____`), and what happens if the creator later edits the published regex?

- **A.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Custom regex patterns (`up to 100/repo or 500/org-or-enterprise`, optional `Generate with AI` & `before`/`after` context) validated via `Save and dry run` (`<=1,000` sample hits) before `Publish pattern` & Push Protection

### 36. VerdantRx Diagnostics is combining custom lab-analyzer patterns, unstructured password detection, and test-fixture exclusions across `verdantrx-cloud`. Which three technical facts accurately guide configuration? Select three.

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** Custom regex patterns (`up to 100/repo or 500/org-or-enterprise`, optional `Generate with AI` & `before`/`after` context) validated via `Save and dry run` (`<=1,000` sample hits) before `Publish pattern` & Push Protection
- **E.** `Non-provider / generic pattern scanning` (`private keys, DB connection strings`) plus `Copilot AI generic secret detection` (`unstructured passwords/keys`, consuming `Secret Protection AI credits` on push)
- **F.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

---

## Domain 3 — Configure and use supply chain security (formerly Dependabot/Dependency Review) (15–20% official weight · 18 questions)

### 37. `assay-analyzer-dotnet` builds NuGet packages with central MSBuild directory props, while `crispr-pipeline-py` builds Conda/pip container layers in Actions. How does VerdantRx Diagnostics ensure both transitive trees appear accurately in GitHub's Dependency Graph?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** `Dependency Graph` (`parsing committed manifests and lockfiles`, augmented by the `Dependency Submission API` for build-time resolved transitive graphs in Maven/Gradle/C++/containers)
- **D.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions

### 38. FDA medical-device cybersecurity guidance (`Section 524B`) requires VerdantRx Diagnostics to submit a machine-readable SBOM for `assay-analyzer-dotnet`. Which GitHub REST API call (`____`) retrieves the `SPDX` JSON SBOM?

- **A.** `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`attaching a Security Configuration across selected or all org repos via REST`)
- **B.** `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** `codeql github upload-results --repository=<org/repo> --ref=<refs/heads/main> --commit=<sha> --sarif=<results.sarif>`

### 39. When VerdantRx Diagnostics exports an SPDX SBOM from `hl7-fhir-broker`, which metadata fields are included for upstream packages—and are downstream hospital microservices that call `hl7-fhir-broker` listed?

- **A.** Export an `SPDX` JSON Software Bill of Materials (`SBOM`) via `Insights -> Dependency graph -> Export SBOM`, `GET /repos/{owner}/{repo}/dependency-graph/sbom`, or `actions/attest-sbom` (`excluding dependents`)
- **B.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **C.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 40. On `crispr-pipeline-py`, Dependabot flags `Pillow` (`CVSS 8.8`, `EPSS 0.004`, `Unreachable`—vulnerable TIFF decoder never imported) and `urllib3` (`CVSS 7.4`, `EPSS 0.79`, `Reachable` across 4 HTTP client call paths in runtime scope). Which alert should be remediated first and why?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Prioritize `Dependabot alerts` combining `EPSS` (`30-day exploitation probability`), `CVSS` severity, `Reachability` call-path analysis (`Reachable` vs `Unreachable`), `runtime` scope, and `patch availability`
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions

### 41. VerdantRx Diagnostics configured an organization Dependabot auto-triage rule dismissing `Low` severity `development`-scope alerts with `EPSS < 0.01`. Which search filter (`____`) lets HIPAA auditors review every auto-dismissed alert, and what happens if `EPSS` spikes to `0.35` next week?

- **A.** `has:deployment runtime-risk:internet-exposed` (`Security Overview and alert search qualifiers powered by ingested deployment metadata`)
- **B.** `queries: security-extended` (`executing default high-precision CodeQL security rules plus medium-precision security queries without style/quality rules`)
- **C.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 42. VerdantRx Diagnostics wants to suppress noisy dev-only Dependabot alerts across 38 clinical repos before on-call pagers fire, while guaranteeing org security policies cannot be weakened by repo admins. Which two behaviors apply? Select two.

- **A.** Use `Dependabot auto-triage rules` to auto-dismiss or snooze low-impact dev/unpatched alerts (`resolution:auto-dismiss`) **before** alert notifications fire
- **B.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Combine `EPSS` (`30-day exploitation probability`) and static `Reachability` call-path verdicts with `CVSS` severity and `runtime` dependency scope
- **E.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 43. VerdantRx Diagnostics wants `pathology-viewer-ts` to open automated Dependabot security PRs **only** for `Critical` and `High` runtime alerts (`not Medium/Low`). Proposed solution: Leave repository-level `Dependabot security updates` enabled globally and create a custom Dependabot auto-triage rule enabling `Open a pull request` for `High, Critical`. Does this restrict security PRs to `High`/`Critical`?

- **A.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **B.** No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs
- **C.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)
- **D.** Yes — this configuration satisfies every security, licensing, and governance requirement

### 44. What are GitHub's **two** curated preset Dependabot auto-triage rules (`____`), and why must teams verify private registry scoping before enabling `Dismiss package malware alerts`?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** `Dependabot auto-triage rules` (`GitHub presets or custom rules on EPSS/CVE/CWE/scope/patch` setting `resolution:auto-dismiss` before notifications; disable global `Dependabot security updates` for custom PR-trigger rules)
- **C.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **D.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step

### 45. `radiology-dicom-gw` uses multi-stage `Dockerfile` base images (`python:3.12-slim`) and reusable GitHub Actions workflows. How can `.github/dependabot.yml` keep both base images and workflows patched automatically?

- **A.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **B.** `Dependabot security updates` (`alert-driven PRs patching vulnerable versions to the minimum fixed version`) vs `.github/dependabot.yml` `Dependabot version updates` (`scheduled ecosystem/Actions freshness PRs`)
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 46. VerdantRx Diagnostics wants pull requests on private `hl7-fhir-broker` blocked whenever a developer introduces a `High`/`Critical` vulnerability or a reciprocal `GPL-2.0` / `AGPL-3.0` package. What is the end-to-end setup sequence?

- **A.** Add SPDX license names to `.github/dependabot.yml` → expect Dependabot version updates to block developer PR merges → skip required status checks → disable lockfiles
- **B.** Enable the Dependency Graph (`and Code Security on private repos`) → add an `on: pull_request` workflow running `actions/dependency-review-action@v4` → configure `fail-on-severity` & `deny-licenses` → mark the check required in a branch ruleset
- **C.** Run `dependency-review-action` on an unlicensed private Free repo → grant `write-all` permissions to untrusted fork code → ignore `fail-on-scopes` → merge failing checks freely
- **D.** Trigger `dependency-review-action` only on weekly cron `schedule` → pass both `allow-licenses` and `deny-licenses` simultaneously → disable the Dependency Graph → leave main unprotected

### 47. In `.github/workflows/dependency-review.yml` on `patient-consent-api`, which exact step configuration (`____`) fails pull requests on `High+` vulnerabilities in `runtime` dependencies while rejecting `GPL-3.0` and `AGPL-3.0` licenses?

- **A.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **B.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **C.** `actions/dependency-review-action@v4` with `fail-on-severity: high`, `fail-on-scopes: runtime`, and `deny-licenses` (`or allow-licenses`, never both)
- **D.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`

### 48. VerdantRx Diagnostics' open-source review board is auditing `actions/dependency-review-action@v4` across its clinical repositories. Which two requirements ensure license and CVE checks cannot be ignored on `main`? Select two.

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Mark the `Dependency Review` workflow job as a **required status check** in a repository or organization Branch Ruleset targeting `main`
- **E.** Configure `actions/dependency-review-action@v4` with `fail-on-severity`, `fail-on-scopes`, and either `allow-licenses` OR `deny-licenses` (`SPDX` IDs)

### 49. `pathology-viewer-ts` pulls private internal UI packages from Azure Artifacts npm and suffers from 35 separate weekly `@testing-library/*` and `eslint-*` PRs. Which `.github/dependabot.yml` configuration (`____`) resolves both problems?

- **A.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)
- **B.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **C.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`
- **D.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)

### 50. VerdantRx Diagnostics validated `hl7-dotnet-core 4.x` under FDA change control and must block Dependabot from proposing `5.x` major upgrades while still receiving `4.x` security and patch updates. Which `.github/dependabot.yml` rule accomplishes this?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **D.** Configure `.github/dependabot.yml` with `groups:` (`batching patch/minor updates into single PRs`), `ignore:` (`version/dependency exclusions`), `open-pull-requests-limit`, and `registries:` (`authenticated via Dependabot secrets`)

### 51. In `.github/dependabot.yml` on `reagent-lot-tracker`, Dependabot security updates still opened a PR even though `open-pull-requests-limit: 5` was already reached by scheduled version updates. Why?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** Configure `.github/dependabot.yml` with `groups:` (`batching patch/minor updates into single PRs`), `ignore:` (`version/dependency exclusions`), `open-pull-requests-limit`, and `registries:` (`authenticated via Dependabot secrets`)
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 52. A workflow on `specimen-barcode-svc` triggered on `pull_request` by `dependabot[bot]` needs an internal NuGet read token to run `dotnet test`. Where **must** that token be stored (`Repository Settings -> Secrets and variables -> ____`) so the Dependabot-triggered run can read it?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Govern Dependabot PR workflows (`read-only GITHUB_TOKEN` & `Dependabot secrets`), fine-grained alert roles, `dependabot_alert` webhooks, and production-context filters (`has:deployment`, `runtime-risk:internet-exposed`)

### 53. VerdantRx Diagnostics streams AKS cluster deployment records from Microsoft Defender for Cloud into GitHub. Which Security Overview filter (`____`) isolates Dependabot alerts affecting live internet-reachable clinical portals?

- **A.** `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)
- **B.** `has:deployment runtime-risk:internet-exposed` (`Security Overview and alert search qualifiers powered by ingested deployment metadata`)
- **C.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **D.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)

### 54. VerdantRx Diagnostics' cloud security architect is reviewing supply-chain CI isolation and runtime alert enrichment. Which two architectural statements are accurate? Select two.

- **A.** Ingest deployment metadata (`from Microsoft Defender for Cloud, JFrog Artifactory, or CI/CD APIs`) to filter `has:deployment` and `runtime-risk:internet-exposed` alerts
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** Workflows triggered by `dependabot` PRs receive a **read-only `GITHUB_TOKEN`** by default and access credentials stored in **`Dependabot secrets`** (`not standard Actions secrets on untrusted triggers`)
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **E.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

---

## Domain 4 — Configure and use Code Security (formerly Code Scanning with CodeQL) (10–15% official weight · 14 questions)

### 55. VerdantRx Diagnostics scans `assay-analyzer-dotnet` (`C#`) with `CodeQL` and scans Kubernetes Helm manifests in the same repo with `Kics` / `Trivy` outputting `SARIF 2.1.0`. How does GitHub Code Scanning unify these tools?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **C.** `CodeQL` (`compiling/extracting code into a queryable relational AST/CFG/dataflow database`) paired with third-party SAST/IaC/container scanners uploading `SARIF 2.1.0` into unified Code Scanning alerts
- **D.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage

### 56. VerdantRx Diagnostics' container scanner produces a `16 MB` gzip-compressed SARIF report on `radiology-dicom-gw` and uploads it alongside CodeQL using the exact same `category` string. Proposed solution: Upload the `16 MB` `.sarif.gz` file directly via `upload-sarif@v3` without splitting categories. Will Code Scanning ingest both scans cleanly?

- **A.** No — `actions/dependency-review-action` forbids specifying `allow-licenses` and `deny-licenses` together, and fails to block merges unless marked as a required status check on `pull_request`
- **B.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)
- **C.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **D.** No — Code Scanning rejects gzip-compressed SARIF files larger than `10 MB` (`and overwrites prior alerts when multiple matrix uploads share an identical SARIF category on one commit`)

### 57. VerdantRx Diagnostics is integrating a custom HIPAA PHI-logging static analyzer (`SARIF 2.1.0`) across four monorepo packages in `hl7-fhir-broker`. Which two SARIF rules ensure reliable uploads and stable alert histories? Select two.

- **A.** Ensure each uploaded `SARIF 2.1.0` file is `<= 10 MB` gzip-compressed and `<= 25,000` results (`knowing GitHub displays only the top 5,000 results prioritized by severity`)
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Assign a unique `category` per tool/language/monorepo target and preserve stable `ruleId` + `partialFingerprints` so alerts deduplicate cleanly without overwriting sibling scans
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **E.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

### 58. `radiology-dicom-gw` (`C++` DICOM image codec) builds on an on-premises GPU Azure DevOps agent rather than GitHub Actions, and findings must publish to GitHub Code Scanning. What is the exact `CodeQL CLI` command order?

- **A.** Install the CodeQL CLI bundle on the CI agent → run `codeql database create` (`tracing compiled builds`) → run `codeql database analyze --format=sarif-latest` → run `codeql github upload-results` (`--sarif`, `--ref`, `--commit`)
- **B.** Run `codeql github upload-results` on raw `.java` source files → run `codeql database analyze` before `codeql database create` → upload an uncompressed 45 MB XML report → omit `--ref` and `--commit`
- **C.** Enable Default Setup simultaneously for the same language/category → upload SARIF with a read-only `contents: read` token → strip `partialFingerprints` → expect >25,000 results to render without truncation
- **D.** Create one shared SARIF file without `--sarif-category` across 6 monorepo services → overwrite prior language alerts on every upload → disable GitHub Code Security on private repos → view alerts in Actions cache

### 59. `pathology-viewer-ts` (`TypeScript`) uses CodeQL `Default Setup`, whereas `assay-analyzer-dotnet` needs a custom `nuget.config` authentication step and custom `CodeQL model pack` before analysis. How should each repository be configured?

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** `Default Setup` (`zero-YAML automatic language/trigger management`) vs `Advanced Setup` (`.github/workflows/codeql.yml` for custom build steps, `codeql-config.yml`, matrix `build-mode`s, or third-party SARIF—mutually exclusive)
- **C.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **D.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage

### 60. In `radiology-dicom-gw` (`C++` compiled with custom `ninja -C build/release` flags after fetching proprietary DICOM SDK headers), `autobuild` fails. Which `codeql-action/init@v3` mode (`____`) should be configured, and why can `build-mode: none` not be used for C++?

- **A.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`
- **D.** `build-mode: manual` (`paired with explicit compiler commands prior to github/codeql-action/analyze@v3`)

### 61. On a `patient-consent-api` pull request, CodeQL flags `Log injection (CWE-117)` showing `HttpRequest.Query["mrn"]` (`source`) flowing unstripped of `\r\n` into `_logger.LogInformation()` (`sink`), and `Copilot Autofix` suggests sanitizing newline characters. Does `Copilot Autofix` require developers to hold `GitHub Copilot` licenses?

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Inspect CodeQL `source -> step -> sink` path-problem dataflow traces and apply `Copilot Autofix` (`enabled by default on CodeQL PRs & default branch without requiring a Copilot seat for classic Autofix`)
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 62. VerdantRx Diagnostics' org policy defaults `GITHUB_TOKEN` workflow permissions to read-only. Which minimal `permissions:` block (`____`) must be declared on the CodeQL job in `.github/workflows/codeql.yml`?

- **A.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`
- **B.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **C.** `Review and manage secret scanning bypass requests` (`fine-grained organization role permission for Push Protection delegated bypass`)
- **D.** `permissions: { security-events: write, contents: read, actions: read }` on `github/codeql-action/upload-sarif@v3`

### 63. VerdantRx Diagnostics' clinical software SOP defines how developers review CodeQL taint alerts and `Copilot Autofix` diffs on ePHI pull requests. Which two statements belong in that SOP? Select two.

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Validate every `Copilot Autofix` suggestion by inspecting dataflow context, running full CI unit/integration tests + re-scanning with `CodeQL`, and completing human PR review
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **E.** Inspect CodeQL `source -> step -> sink` path-problem dataflow traces and apply `Copilot Autofix` (`enabled by default on CodeQL PRs & default branch without requiring a Copilot seat for classic Autofix`)

### 64. A developer on `ehr-sync-adapter` sees two CodeQL findings: Rule A has `Security severity: High` and `Rule severity: Warning`; Rule B has no security-severity tag (`quality rule`) and `Rule severity: Error`. If the branch ruleset sets `Security alerts: High or higher` and `All alerts: None`, which finding blocks the PR?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Distinguish `security-severity` (`Critical/High/Medium/Low` mapped from CVSS `0.0–10.0`) from rule `problem.severity` (`error/warning/note`), use `category` per matrix leg, and record audited dismissal reasons

### 65. VerdantRx Diagnostics' custom PHI linter emits raw line numbers without `partialFingerprints` in its SARIF output, causing every formatting commit on `clia-compliance-bot` to close old alerts and open brand-new alert IDs. How do `upload-sarif` or scanner fingerprints fix this?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** `SARIF 2.1.0` ingestion rules: `<= 10 MB` gzip-compressed upload limit, `<= 25,000` results/run (`top 5,000` displayed by severity), `partialFingerprints` deduplication, distinct `category` tags, and `security-events: write`
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 66. On VerdantRx Diagnostics' Azure DevOps build agent for `radiology-dicom-gw`, which exact `CodeQL CLI` command (`____`) uploads `dicom-scan.sarif` to GitHub Code Scanning for a pull request merge commit?

- **A.** `codeql github upload-results --repository=<org/repo> --ref=<refs/heads/main> --commit=<sha> --sarif=<results.sarif>`
- **B.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **C.** `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)
- **D.** `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`attaching a Security Configuration across selected or all org repos via REST`)

### 67. VerdantRx Diagnostics' internal `.NET` middleware `VerdantRx.PhiGuard.Scrub()` sanitizes patient identifiers before SQL/log sinks, and AppSec wants CodeQL to stop raising false positives whenever `Scrub()` wraps tainted strings. Which file and feature (`____`) models this cleanly?

- **A.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`
- **B.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)
- **C.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **D.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)

### 68. `assay-analyzer-dotnet` fails CodeQL extraction with `java.lang.OutOfMemoryError` / runner OOM during peak PR hours when `C#`, `TypeScript`, and `Python` all run inside a single sequential workflow job on a 7 GB runner. What fixes both memory pressure and PR latency?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **D.** Customize `.github/codeql/codeql-config.yml` (`paths-ignore`, `packs`, `queries`, `threat-models`) & `CodeQL model packs` (`YAML data extensions`), and fix OOM/slow scans via Larger runners or split language matrices

---

## Domain 5 — Security operations: best practices, prioritization, and remediation (15–20% official weight · 18 questions)

### 69. A hospital security researcher submits a critical XML injection report on VerdantRx's public `fhir-r4-lint` library through Private Vulnerability Reporting. What is the correct four-step `GHSA` remediation and disclosure lifecycle?

- **A.** Publish the unpatched exploit details in a public GitHub Issue immediately → ask developers to commit fixes on a public feature branch → request a CVE before confirming the bug → create a draft advisory last
- **B.** Triage the report via Private Vulnerability Reporting (`draft GHSA`) → open a temporary private fork from the advisory to develop & verify the fix → request a `CVE` & prepare patched versions → merge the fix & publish the advisory
- **C.** Dismiss the researcher report without reading it → rotate unrelated SSH keys → add the vulnerable source folder to `secret_scanning.yml` → expect CVEs to assign without advisory metadata
- **D.** Open a temporary private fork and run GitHub Actions workflows directly inside that advisory fork → auto-merge without review → delete the GHSA after release so downstream Dependabot alerts never fire

### 70. How do `CWE-611` (`Improper Restriction of XML External Entity Reference`), `CVE-2026-50911`, and `GHSA-m4p2-...` relate to one another on VerdantRx's `fhir-r4-lint` advisory?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **C.** `CWE` classifies weakness types (`e.g., CWE-89 SQLi`), `CVE` identifies a publicly disclosed vulnerability instance, and `GHSA` (`Repository Security Advisories` + Private Reporting) coordinates private patches & CVEs
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 71. Maintainers of `fhir-r4-lint` want to verify unit tests on their zero-day patch inside `fhir-r4-lint-ghsa-88x2` before publishing the release. Proposed solution: Push a workflow edit inside the temporary private advisory fork expecting GitHub Actions runners to execute automatically inside that fork. Will GitHub Actions run inside the temporary advisory fork?

- **A.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)
- **B.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **C.** No — `actions/dependency-review-action` forbids specifying `allow-licenses` and `deny-licenses` together, and fails to block merges unless marked as a required status check on `pull_request`
- **D.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)

### 72. VerdantRx Diagnostics has 780 historical CodeQL and Dependabot alerts across clinical and internal lab tools. Which dual strategy prevents new severe vulnerabilities from merging while focusing engineers on real patient-facing exposure first?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **D.** Prioritize using `has:deployment` + `runtime-risk:internet-exposed` (`Defender for Cloud / artifact registries`), `EPSS`, and `Reachability`, while blocking new regressions via `Require code scanning results` rulesets

### 73. What happens on a pull request to `hl7-fhir-broker` if an `Active` organization ruleset includes `Require code scanning results` specifying tool `CodeQL`, and someone deletes `.github/workflows/codeql.yml` in their PR branch?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Enforce approved CodeQL scanning via Org/Enterprise `Rulesets` (`Require code scanning results` + Required Workflows) and automate governance via REST/GraphQL (`code-security/configurations`, org alert endpoints & billing APIs)
- **C.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

### 74. VerdantRx Diagnostics is rolling out org-wide `Require code scanning results` rulesets and runtime risk filtering across 38 clinical repositories. Which two practices ensure smooth adoption and accurate prioritization? Select two.

- **A.** Pilot cross-repository `Rulesets` in **`Evaluate` mode** to measure would-be blocked PRs via Ruleset Insights before switching enforcement to **`Active`**
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **E.** Ingest deployment metadata (`from Microsoft Defender for Cloud, JFrog Artifactory, or CI/CD APIs`) to filter `has:deployment` and `runtime-risk:internet-exposed` alerts

### 75. VerdantRx Diagnostics' AppSec lead wants to burn down 150 default-branch `CWE-89` SQL injection and `CWE-117` log-injection alerts across 10 ePHI services ahead of a HITRUST recertification audit. What is the end-to-end Security Campaign workflow?

- **A.** Create a campaign containing 50,000 unmerged fork-branch alerts with no contact owner → auto-merge Copilot suggestions bypassing CI tests → revoke developer write access → close the campaign with alerts still open
- **B.** Filter high-risk default-branch alerts in Security Overview → create a Security Campaign (`<=1,000` alerts) with due date & contact → trigger Copilot Autofix (`or assign <=25 alerts to @copilot`) → verify CI checks & track burndown
- **C.** Export alerts to a static spreadsheet with no GitHub links → disable CodeQL so open counts fall to zero → bulk-dismiss every alert without comments → report 100% remediation
- **D.** Assign 500 alerts in one batch to `@copilot` without AI credits or branch protection → skip human PR review → disable Security Overview → expect secret campaigns to auto-rotate AWS IAM keys

### 76. What is the maximum number of alerts per **Security Campaign** (`1,000`) versus the maximum batch size when assigning campaign alerts directly to the **`@copilot`** coding agent (`____`), and what branch scope do code security campaigns target?

- **A.** Run `Security Campaigns` (`<=1,000` default-branch alerts, named security lead, developer notifications, Copilot Autofix, or assigning `<=25` alerts per batch to `@copilot` cloud agent) with audited dismissal comments
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 77. During VerdantRx's Q3 Security Campaign, a developer closes 6 alerts in `specimen-barcode-svc` as `Won't fix` claiming an upstream WAF blocks the route. How should the campaign security contact govern these closures?

- **A.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Dismissing an alert requires a structured closure reason (`False positive`, `Used in tests`, `Won't fix`) plus an audit-logged justification comment—and never deletes commits or revokes keys

### 78. VerdantRx Diagnostics wants `patient-consent-api` (`ePHI Tier-1`) scanned with medium-precision CodeQL security rules in addition to high-precision `default` rules, without enabling non-security code-style warnings. Which suite (`queries: ____`) should AppSec configure?

- **A.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** `queries: security-extended` (`executing default high-precision CodeQL security rules plus medium-precision security queries without style/quality rules`)
- **D.** `has:deployment runtime-risk:internet-exposed` (`Security Overview and alert search qualifiers powered by ingested deployment metadata`)

### 79. VerdantRx Diagnostics' offensive security engineer found a custom FHIR token-forgery pattern in one `.NET` controller and wants to query all 38 clinical repositories' CodeQL databases at once without modifying repo workflows. Which tool (`____`) runs this hunt?

- **A.** Select CodeQL query suites (`default` high-precision, `security-extended` broader lower-confidence security, `security-and-quality` adds maintainability) and run `Multi-Repository Variant Analysis (MRVA)` in VS Code
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

### 80. `crispr-pipeline-py` runs batch CLI scripts that read untrusted FASTQ headers from local hospital NFS mounts, which CodeQL's default `remote` threat model ignores. Which `.github/codeql/codeql-config.yml` entry enables local file/CLI taint sources?

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Customize `.github/codeql/codeql-config.yml` (`paths-ignore`, `packs`, `queries`, `threat-models`) & `CodeQL model packs` (`YAML data extensions`), and fix OOM/slow scans via Larger runners or split language matrices

### 81. VerdantRx Diagnostics wants lead clinical developers to triage and assign Dependabot and Code Scanning alerts across their assigned repos without giving them `Repository Admin` permissions to delete branches or alter rulesets. How should roles be designed?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)

### 82. How do Push Protection `delegated bypass` and Organization `Ruleset bypass lists` work together during an urgent clinical laboratory outage at VerdantRx Diagnostics?

- **A.** `Delegated bypass for push protection` (`granting Specific roles, visible teams, or custom roles with "Review and manage secret scanning bypass requests" authority—never secret teams`)
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 83. VerdantRx Diagnostics is establishing collaborative governance between its HIPAA Security team and 9 engineering squads. Which two practices balance developer autonomy with compliance enforcement? Select two.

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Pilot cross-repository `Rulesets` in **`Evaluate` mode** to measure would-be blocked PRs via Ruleset Insights before switching enforcement to **`Active`**
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **E.** Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)

### 84. VerdantRx Diagnostics wants every pull request on `hl7-fhir-broker` protected against credential leaks, vulnerable NuGet/npm packages, and `C#` taint vulnerabilities *before* code merges to `main`. Which combination delivers complete shift-left coverage?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Layer `Push Protection` (`pre-receive`), `actions/dependency-review-action` (`PR manifest/license gate`), and `CodeQL` PR checks (`with Copilot Autofix`) so secrets, vulnerable packages, and taint flaws fail pre-merge
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step

### 85. Why didn't `Dependabot alerts` block a developer's feature pull request on `pathology-viewer-ts` from merging a newly added vulnerable npm package into `main`, and which tool (`____`) stops it pre-merge?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **C.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **D.** `actions/dependency-review-action@v4` on `pull_request` (`with fail-on-severity, mutually exclusive allow-licenses OR deny-licenses SPDX lists, fail-on-scopes, and allow-ghsas`) enforced as a required check

### 86. VerdantRx Diagnostics' Secure SDLC Standard requires three pre-merge controls on every ePHI service repository. Which three items satisfy that standard? Select three.

- **A.** Validate every `Copilot Autofix` suggestion by inspecting dataflow context, running full CI unit/integration tests + re-scanning with `CodeQL`, and completing human PR review
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **D.** Configure `actions/dependency-review-action@v4` with `fail-on-severity`, `fail-on-scopes`, and either `allow-licenses` OR `deny-licenses` (`SPDX` IDs)
- **E.** `Push Protection` blocks high-confidence partner and published custom secrets pre-receive during `git push` before commits land on GitHub
- **F.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step

---

## Domain 6 — GitHub Security suites administration (10–15% official weight · 14 questions)

### 87. VerdantRx Diagnostics is rolling out tiered Security Configurations (`ePHI-Enforced` and `Internal-Baseline`) across 85 repositories in two GHEC organizations. What is the recommended four-step rollout sequence?

- **A.** Manually toggle Settings on 2,000 repositories one by one → grant every developer Organization Owner permissions → disable Push Protection globally → rely on `.gitignore` for enterprise governance
- **B.** Apply an `Enforced` configuration across 2,000 private repos with zero available committer seats → set every feature to `Not set` expecting strict locks → leave new repositories uncovered → disable audit logs
- **C.** Enable cloud-only Copilot Autofix on an air-gapped GHES instance with metered billing → skip GitHub Connect → expect transferred external repos to inherit new-repo defaults automatically without policy checks
- **D.** Verify committer license headroom (`or metered budget`) → create/select a Security Configuration → attach to tiered repos (`custom properties`) & enable `Apply to new repositories` → set `Enforced` to lock baseline controls

### 88. VerdantRx Diagnostics operates an on-premises hospital appliance on `GitHub Enterprise Server (GHES)` alongside `GitHub Enterprise Cloud (GHEC)`. Which capabilities require `GHEC` (`or GitHub Connect`) rather than an air-gapped standalone `GHES` instance?

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Roll out org/enterprise `Security Configurations` (`GitHub-recommended` or custom, `Apply to new repositories`), contrasting `GHEC` (`metered or volume + cloud AI features`) with `GHES` (`volume-only + GitHub Connect Advisory sync`)
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 89. What is the difference between setting a Security Configuration's policy enforcement to `Enforced` versus `Unenforced` across VerdantRx Diagnostics' sandbox repositories?

- **A.** `Enforced` Security Configurations lock enabled/disabled settings (`except fields set to "Not set"`), while private/internal repos consume `90-day unique active committer` seats (`plus metered AI credits for AI Scan/generic secrets`)
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners

### 90. VerdantRx Diagnostics' Security Manager wants to prohibit repository admins on `hl7-fhir-broker` from disabling `Secret scanning validity checks` under an `Enforced` Security Configuration. Proposed solution: Leave `Validity checks` configured as `"Not set"` inside the `Enforced` Security Configuration. Does this prevent repo admins from turning it off?

- **A.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)
- **B.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **C.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)
- **D.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)

### 91. Developer Nora at VerdantRx Diagnostics pushed commits to 9 private repositories on `GitHub Secret Protection` and 4 private repositories on `GitHub Code Security` within the last 30 days, plus 6 public repositories. How many seats does Nora consume in each paid SKU pool?

- **A.** `Enforced` Security Configurations lock enabled/disabled settings (`except fields set to "Not set"`), while private/internal repos consume `90-day unique active committer` seats (`plus metered AI credits for AI Scan/generic secrets`)
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect

### 92. VerdantRx Diagnostics' FinOps team wants predictable monthly Security Suite spend on `GitHub Enterprise Cloud` with zero surprise AI overages. Which two billing and budget rules apply? Select two.

- **A.** Count `90-day unique active committers` across private/internal repos (`deduplicating each human user once across the enterprise, plus GitHub Connect sync between GHEC and GHES`)
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **D.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **E.** Monitor `Code Security AI credits` (`AI Scan / agentic autofix`) and `Secret Protection AI credits` (`AI push scanning`), setting **hard metered budgets** to cap spend

### 93. VerdantRx Diagnostics disabled `Repository administrators can enable or disable GitHub Secret Protection` in Enterprise policies so individual squad admins cannot consume unbudgeted seats. Does this prevent `Security Managers` from attaching Security Configurations to new ePHI repositories?

- **A.** Enforce Enterprise Advanced Security policies (`restricting repo admins while preserving Org Owner/Security Manager control`), scope ruleset/push-protection bypass actors, and stream `security_configuration.*` / alert audit logs
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **D.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations

### 94. For HIPAA 6-year audit retention (`beyond GitHub's standard interactive audit log window`), how should VerdantRx Diagnostics preserve tamper-evident records of Security Configuration changes, alert dismissals, and bypass approvals?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Enforce Enterprise Advanced Security policies (`restricting repo admins while preserving Org Owner/Security Manager control`), scope ruleset/push-protection bypass actors, and stream `security_configuration.*` / alert audit logs
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 95. Before enforcing an Enterprise-level branch ruleset requiring `Dependency Review` and `CodeQL` across all `hipaa_ephi:true` repositories at VerdantRx Diagnostics, how can administrators measure exactly which PRs would fail over a 14-day window without blocking clinical hotfixes?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Pilot cross-repository `Rulesets` in **`Evaluate` mode** to measure would-be blocked PRs via Ruleset Insights before switching enforcement to **`Active`**
- **C.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 96. VerdantRx Diagnostics wants its 3-person Clinical AppSec team to manage Security Configurations, view all org alerts, and run Security Campaigns across `verdantrx-cloud` **without** granting access to push source code or edit organization billing. Which built-in organization role (`____`) provides this exact scope?

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Separate `Enterprise/Org Owners` (`billing & global policy`), `Security Managers` (`org-wide alert read/write & security config management, without code-write`), and custom repository roles (`granular view/dismiss per tool`)
- **D.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations

### 97. VerdantRx Diagnostics' open-source licensing paralegal needs read-only access to `Dependabot alerts` on `hl7-fhir-broker` and `pathology-viewer-ts`—with zero access to `Code Scanning` taint traces, `Secret Protection` tokens, or source-code edits. How should access be granted?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** Separate `Enterprise/Org Owners` (`billing & global policy`), `Security Managers` (`org-wide alert read/write & security config management, without code-write`), and custom repository roles (`granular view/dismiss per tool`)

### 98. Why can a standard `Write` contributor on `assay-analyzer-dotnet` view Code Scanning annotations on their pull request by default, yet get `404 / insufficient permissions` when opening the repository's `Secret scanning` alert list?

- **A.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)

### 99. VerdantRx Diagnostics' platform-engineering portal provisions new clinical microservices and attaches the `ePHI-Enforced` Security Configuration via GitHub's REST API. Which endpoint (`____`) attaches that configuration to selected repository IDs?

- **A.** `codeql github upload-results --repository=<org/repo> --ref=<refs/heads/main> --commit=<sha> --sarif=<results.sarif>`
- **B.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **C.** `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`attaching a Security Configuration across selected or all org repos via REST`)
- **D.** `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)

### 100. VerdantRx Diagnostics enforces custom multi-language CodeQL workflows across 25 `.NET + TypeScript` repos and exports nightly alert telemetry into its HIPAA data warehouse. Which two architecture patterns prevent scan tampering and API bottlenecks? Select two.

- **A.** Assign a unique `category` per tool/language/monorepo target and preserve stable `ruleId` + `partialFingerprints` so alerts deduplicate cleanly without overwriting sibling scans
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **E.** Enforce approved CodeQL scanning via Org/Enterprise `Rulesets` (`Require code scanning results` + Required Workflows) and automate governance via REST/GraphQL (`code-security/configurations`, org alert endpoints & billing APIs)

---

## Answer Key and Explanations

### Question 1 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). Because `GitHub Secret Protection` and `GitHub Code Security` are standalone SKUs (`on GitHub Team and Enterprise`), VerdantRx can enable Secret Protection org-wide while licensing Code Security selectively for committers on its 12 external API repos. [Skill 1.1: Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)]

- **A:** Correct. GitHub offers standalone Secret Protection and Code Security products on both GitHub Team and GitHub Enterprise, billed by unique 90-day active committers on private/internal repos
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions

### Question 2 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Secret Protection prevents and detects leaked credentials, Code Security (`CodeQL`/SARIF + Copilot Autofix) analyzes custom `.NET`/Python source code, and Supply Chain Security inventories and remediates open-source package risks. [Skill 1.1: Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Correct. each pillar targets a distinct risk surface: leaked credentials, first-party source vulnerabilities, and third-party open-source dependency/license exposure
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 3 — `B, E` (Describe GitHub Security suites, features, and ecosystem)

Correct answers: B and E (are correct). `GitHub Secret Protection` provides secret scanning, Push Protection, partner validity checks, custom patterns, and AI generic secret detection, while `GitHub Code Security` provides CodeQL/SARIF scanning, Copilot Autofix, private-repo Dependency Review, and Security Campaigns. [Skill 1.1: Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Correct. Secret Protection focuses specifically on credential exposure in pushes and Git history
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **E:** Correct. Code Security covers first-party SAST, Copilot Autofix, and private-repository Dependency Review enforcement

### Question 4 — `B` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: B (is correct). Public GitHub.com repositories get core secret scanning, Push Protection, Dependency Graph, Dependabot, CodeQL default setup, and Dependency Review free, whereas `private` and `internal` repositories require Secret Protection / Code Security licenses for advanced capabilities. [Skill 1.2: Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-overview/about-security-overview)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Correct. GitHub provides core security scanning free to open-source public repositories on GitHub.com while requiring Secret Protection / Code Security licenses for advanced private/internal repo coverage
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers

### Question 5 — `B` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: B (is correct). `Security Overview` (`at Organization and Enterprise levels`) aggregates `Risk`, `Coverage`, `Campaigns`, and per-tool views filterable by custom properties like `props.hipaa_ephi:true`. [Skill 1.2: Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-overview/about-security-overview)]

- **A:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **B:** Correct. Security Overview aggregates posture, enablement gaps, alert trends, and campaign burndown across hundreds of repositories from a single org/enterprise plane
- **C:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets
- **D:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges

### Question 6 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Running the free organization security risk assessment from Security Overview scans private org repositories for exposed secrets and previews CodeQL + Copilot Autofix across up to 20 active repositories. [Skill 1.2: Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-overview/about-security-overview)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Correct. organizations on GitHub Team or Enterprise can run free secret and code risk assessments before purchasing full rollout licenses
- **D:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)

### Question 7 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Secret Protection inspects raw text/config files and Git commits for secret patterns and high-entropy tokens, whereas CodeQL compiles/extracts `C#` into a semantic relational database to trace `XXE` configurations and taint flows. [Skill 1.3: Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Correct. Secret Protection catches leaked tokens in any text/config file at push time, while CodeQL models how untrusted inputs or hardcoded values flow into sensitive code sinks
- **D:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement

### Question 8 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). `.github/secret_scanning.yml` only suppresses post-push user alerts in ignored paths; blocking keys pre-receive requires Push Protection and automated PR XSS patches require CodeQL with Copilot Autofix. [Skill 1.3: Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Correct. secret_scanning.yml suppresses user notifications in excluded folders rather than blocking pushes or cancelling public-repo partner revocations
- **B:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. `.github/secret_scanning.yml` only suppresses post-push user alerts in ignored paths; blocking keys pre-receive requires Push Protection and automated PR XSS patches require CodeQL with Copilot Autofix.
- **C:** Incorrect. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release
- **D:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories

### Question 9 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). Push Protection blocks secrets during `git push` before remote storage, Dependency Review flags vulnerable/unlicensed lockfile changes on the pull request, and CodeQL + Copilot Autofix remediates custom code flaws prior to merge. [Skill 1.3: Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Correct. combining all three shift-left controls prevents new security debt from ever landing on the default branch
- **B:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure

### Question 10 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). Block secrets pre-receive via Push Protection, run Dependency Review and CodeQL on every PR, apply Copilot Autofix or dependency patches before merge, and continuously monitor default-branch advisories in Security Overview. [Skill 1.4: Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns)]

- **A:** Incorrect. deferring secret and code checks until after merge exposes live credentials in Git history and turns security into high-cost reactive firefighting
- **B:** Incorrect. auto-dismissing unreviewed PR findings defeats shift-left prevention, and .gitignore never revokes already-exposed credentials
- **C:** Incorrect. Copilot Autofix requires an upstream CodeQL finding first, and Push Protection intercepts secrets during git push rather than post-merge
- **D:** Correct. a prevention-first secure SDLC stops secrets at git push, blocks vulnerable PR code/dependencies with pre-merge checks and Autofix, and continuously monitors post-merge advisories

### Question 11 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). Secrets have already entered shared Git history (`requiring immediate key rotation and history purges`), and late release-gate blocks stall clinical hotfixes while developers untangle weeks of merged commits. [Skill 1.4: Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns)]

- **A:** Correct. shifting detection to git push and pull requests prevents secret sprawl and vulnerable merges before release cutoffs
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 12 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). `Security Campaigns` package up to 1,000 default-branch alerts with a target deadline, designated security contact, repository writer notifications, and Copilot Autofix remediation support. [Skill 1.4: Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Correct. Security Campaigns turn overwhelming alert backlogs into manageable, developer-friendly remediation sprints with clear ownership
- **D:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names

### Question 13 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). The alert closes in default open queues while permanently retaining the actor, timestamp, closure reason, and comment in the alert timeline, REST/GraphQL endpoints, webhooks, and enterprise audit logs. [Skill 1.5: Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/vulnerability-exposure)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Correct. alert dismissals remain visible in REST/GraphQL APIs, webhooks, and audit logs, so teams must document rationale rather than hiding unverified risk

### Question 14 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Removing a secret in a later commit leaves the password exposed in the earlier commit blob and PR diff; the Snowflake credential must be revoked/rotated immediately and history purged. [Skill 1.5: Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/vulnerability-exposure)]

- **A:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. Removing a secret in a later commit leaves the password exposed in the earlier commit blob and PR diff; the Snowflake credential must be revoked/rotated immediately and history purged.
- **B:** Incorrect. each gzipped SARIF upload must be <=10 MB with a distinct category per language/tool/component and security-events: write permission
- **C:** Correct. alert dismissal only updates GitHub UI/API triage status; attackers can still extract unrotated keys from earlier commits, clones, or reflogs
- **D:** Incorrect. allow-licenses and deny-licenses are mutually exclusive inputs in dependency-review-action, and branch rulesets must require the check to block merging

### Question 15 — `D, E` (Describe GitHub Security suites, features, and ecosystem)

Correct answers: D and E (are correct). Mandate accurate dismissal reasons (`False positive`, `Used in tests`, `Won't fix`) with explanatory comments, and monitor dismissal telemetry via Security Overview, webhooks, REST APIs, and audit log streaming. [Skill 1.5: Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/vulnerability-exposure)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Correct. structured dismissal reasons and comments create an auditable compliance trail in webhooks and GraphQL/REST APIs
- **E:** Correct. Security Overview and org audit logs surface anomalous dismissal spikes or unpatched high-risk repositories

### Question 16 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). Enterprise/Org Admins own licensing and global Security Configurations, Security Managers drive Security Overview posture, triage rules, and campaigns, and Developers author and test PR/campaign fixes. [Skill 1.6: Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)]

- **A:** Correct. effective DevSecOps distributes enablement, posture prioritization, and code-level patching cleanly across Admin, AppSec, and Developer roles
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 17 — `B` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: B (is correct). Restricting raw secret alert access prevents broad internal exposure of active keys, while delegated bypass ensures any developer requesting a push override receives explicit review from authorized security personnel. [Skill 1.6: Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Correct. restricting sensitive secret/vulnerability details and routing bypass requests through designated security reviewers preserves accountability without halting urgent releases
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 18 — `A, C, F` (Describe GitHub Security suites, features, and ecosystem)

Correct answers: A, C, and F (are correct). Partition Admin/Security Manager/Developer responsibilities cleanly, govern Push Protection overrides with least-privilege delegated bypass reviewers, and prioritize Dependabot alerts using `EPSS`, `Reachability`, CVSS, and runtime scope. [Skill 1.6: Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)]

- **A:** Correct. combining EPSS exploit likelihood and static reachability with CVSS and runtime scope focuses engineering effort on genuinely exploitable dependencies
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Correct. restricting sensitive secret/vulnerability details and routing bypass requests through designated security reviewers preserves accountability without halting urgent releases
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **E:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **F:** Correct. effective DevSecOps distributes enablement, posture prioritization, and code-level patching cleanly across Admin, AppSec, and Developer roles

### Question 19 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). Attaching an Organization Security Configuration with `Apply to new repositories` enabled turns on Secret Protection features across existing repositories and newly created repositories alike. [Skill 2.1: Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Correct. Security Configurations scale Secret Protection across existing and newly created repositories consistently, while single-repo toggles suit isolated pilots
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 20 — `D` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: D (is correct). On the public repo, GitHub runs partner scanning free and notifies Slack (`which automatically revokes/handles the exposed token`), whereas on the private repo GitHub creates internal alerts for authorized org/repo users (`and optionally checks validity`). [Skill 2.1: Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Correct. partner notification automatically reports exposed public-repo tokens to the issuing cloud/SaaS vendor, whereas private-repo findings stay internal unless validity checks query the provider

### Question 21 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). No—`Apply to new repositories` covers newly created or newly forked repositories inside the organization, so transferred repositories must have the Security Configuration attached explicitly (`via UI or REST API`). [Skill 2.1: Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)]

- **A:** Correct. understanding Enforced vs Unenforced inheritance, transferred-repo gaps, 90-day active committer deduplication, and hard budgets on metered SKUs/AI credits prevents surprise overages or lockouts
- **B:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 22 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). `Push Protection` scans pushed commits pre-receive across CLI, IDEs, web edits, and REST APIs, rejecting supported high-confidence and published custom secrets before Git history updates. [Skill 2.2: Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)]

- **A:** Correct. blocking leaked credentials before the remote ref updates avoids costly key rotation, incident response, and Git history rewrites
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 23 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). Enabling `non-provider patterns` (`historical/post-push`) plus `Copilot AI generic secret detection` (`push-time unstructured password detection consuming Secret Protection AI credits`) catches non-vendor credentials (`without partner validity checks`). [Skill 2.2: Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)]

- **A:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **B:** Correct. enabling non-provider and AI generic secret detection catches unstructured passwords and connection strings missed by vendor-prefix regexes (noting non-provider patterns lack partner validity checks)
- **C:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 24 — `B, D` (Configure and use Secret Protection (formerly secret scanning))

Correct answers: B and D (are correct). Push Protection blocks high-confidence secrets pre-receive before commits enter Git history, and partner `validity checks` label alerts `Active`, `Inactive`, or `Unknown` so live keys are rotated first. [Skill 2.2: Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Correct. stopping secrets pre-receive prevents Git history contamination and emergency credential rotation
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Correct. Active validation status gives AppSec teams high-signal prioritization during incident triage
- **E:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 25 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). Confirm alert validity and blast radius, immediately revoke and rotate the secret in Microsoft Entra / Azure Key Vault, rewrite Git history (`git filter-repo` plus Support cache purge if needed), and close the alert as `Revoked`. [Skill 2.3: Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts)]

- **A:** Incorrect. delaying credential revocation leaves attackers able to exploit copies harvested from webhooks, clones, or cached diffs while history is rewritten
- **B:** Incorrect. deleting a secret in a follow-up commit leaves the active credential exposed in prior Git commits, reflogs, and clones without revoking access
- **C:** Correct. once a secret reaches Git history, revoking/rotating the live key comes first, followed by history rewrite/cache purge and marking the alert Revoked for auditability
- **D:** Incorrect. using secret_scanning.yml to silence an active production credential leak hides the alert without revoking or rotating the compromised secret

### Question 26 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). Trigger an on-demand validity re-check on the Secret Protection alert so GitHub queries the partner endpoint again and updates the status badge from `Active` to `Inactive`, then resolve as `Revoked`. [Skill 2.3: Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts)]

- **A:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **B:** Correct. knowing a leaked AWS, Stripe, or Slack token is still Active lets incident responders triage live compromises ahead of already-revoked tokens
- **C:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 27 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). Even after a force-push, the dangling commit blob can persist in GitHub's object store, PR caches, webhook payloads, CI logs, or developer clones—so any credential that touched a remote push must be rotated immediately. [Skill 2.3: Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Correct. merely deleting a secret in a later commit leaves it readable in earlier commits; immediate revocation and rotation is mandatory
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 28 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). Enabling `Delegated bypass for push protection` routes developer bypass requests (`with reason and comment`) to designated visible teams, roles, or custom roles for explicit approval or denial. [Skill 2.4: Configure role-based and delegated bypass policies in Secret Protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Correct. delegated bypass replaces ad-hoc writer self-bypasses with a structured request-and-approval workflow audited via webhooks and logs
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 29 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). Assigning `Review and manage secret scanning bypass requests` in a custom organization role grants standalone delegated-bypass reviewer authority. [Skill 2.4: Configure role-based and delegated bypass policies in Secret Protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)]

- **A:** Correct. granting Review and manage secret scanning bypass requests creates least-privilege Push Protection approvers without full Org Owner access
- **B:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **C:** Incorrect. uploading CodeQL or third-party SARIF 2.1.0 findings from GitHub Actions requires least-privilege security-events: write permission
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 30 — `A, C` (Configure and use Secret Protection (formerly secret scanning))

Correct answers: A and C (are correct). Delegated bypass lists accept only **visible** organization teams, standard roles, or custom roles (`secret teams are rejected`), and every bypass request/decision streams to webhooks and the organization audit log. [Skill 2.4: Configure role-based and delegated bypass policies in Secret Protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)]

- **A:** Correct. every bypass leaves an immutable audit trail linking the actor, commit, justification, and approver
- **B:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **C:** Correct. delegated bypass centralizes exception approvals in visible accountable security teams or roles
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **E:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 31 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). Committing `.github/secret_scanning.yml` with `paths-ignore: ["test/hl7-samples/**"]` (`up to 1,000 entries and <= 1 MB`) excludes those synthetic test paths from user secret alerts. [Skill 2.5: Configure Secret Protection alert recipients and path exclusions (.github/secret_scanning.yml) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning)]

- **A:** Correct. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets
- **D:** Incorrect. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup

### Question 32 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). GitHub ignores `.github/secret_scanning.yml` `paths-ignore` exclusions when scanning individual target files larger than `1 MB` (`and also ignores secret_scanning.yml itself if that config file exceeds 1 MB or 1,000 entries`). [Skill 2.5: Configure Secret Protection alert recipients and path exclusions (.github/secret_scanning.yml) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning)]

- **A:** Correct. secret_scanning.yml silences noisy user alerts in synthetic fixture directories up to 1,000 paths / 1 MB while keeping real code paths protected
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement

### Question 33 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). Assigning secret alert `#14` (`or adding it to a secret campaign assigned to Elena`) grants Elena temporary access to view **only** alert `#14` (`not alerts #1–#13`), and that visibility is revoked automatically if she is unassigned. [Skill 2.5: Configure Secret Protection alert recipients and path exclusions (.github/secret_scanning.yml) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning)]

- **A:** Correct. clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 34 — `D` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: D (is correct). Define the pattern name, regex, and test strings (`or Generate with AI`), run `Save and dry run` across org repositories, refine regex/context to eliminate false positives, and `Publish pattern` before enabling Push Protection. [Skill 2.6: Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning)]

- **A:** Incorrect. .gitignore does not configure Secret Protection, AI-generated regexes still require dry-run validation, and secret teams cannot be added to bypass lists
- **B:** Incorrect. GitHub disables the Push Protection toggle until a custom pattern passes dry-run testing and is published, and broad untested regexes flood teams with false positives
- **C:** Incorrect. Enterprise/Org custom patterns are configured in Org/Enterprise settings, and saving edits to an existing custom pattern closes alerts created by its prior version
- **D:** Correct. custom secret patterns require dry-run validation (up to 1,000 sample matches without creating live alerts) and publication before Push Protection can be enabled

### Question 35 — `D` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: D (is correct). Enterprise-level dry runs test up to `10` selected repositories (`returning <= 1,000 matches`), only the original enterprise creator can edit that pattern, and saving pattern edits closes alerts created by its prior version. [Skill 2.6: Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning)]

- **A:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Correct. dry runs preview up to 1,000 historical matches without creating live alerts, and editing a published pattern automatically closes alerts generated by its previous version

### Question 36 — `B, D, E` (Configure and use Secret Protection (formerly secret scanning))

Correct answers: B, D, and E (are correct). Custom patterns support `100/repo` or `500/org-or-enterprise` with dry-run validation before publishing, Copilot AI generic detection + non-provider patterns catch unstructured passwords (`without partner validity checks`), and `.github/secret_scanning.yml` `paths-ignore` caps at `1,000` globs / `1 MB`. [Skill 2.6: Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Correct. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Correct. dry runs preview up to 1,000 historical matches without creating live alerts, and editing a published pattern automatically closes alerts generated by its previous version
- **E:** Correct. enabling non-provider and AI generic secret detection catches unstructured passwords and connection strings missed by vendor-prefix regexes (noting non-provider patterns lack partner validity checks)
- **F:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 37 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). Commit deterministic lockfiles (`packages.lock.json`, `poetry.lock`/`requirements.txt`) and run CI `Dependency Submission API` detector actions to upload resolved build-time transitive dependency graphs. [Skill 3.1: Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Correct. committing lockfiles plus submitting build-resolved snapshots gives GitHub complete direct and transitive dependency visibility
- **D:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names

### Question 38 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). Calling `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`or running actions/attest-sbom` during release builds) exports the repository's full direct and transitive dependency inventory in SPDX JSON format. [Skill 3.1: Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)]

- **A:** Incorrect. the code-security configurations attach endpoint programmatically binds a Security Configuration to targeted or organization-wide repositories
- **B:** Correct. the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Incorrect. codeql github upload-results publishes externally generated SARIF 2.1.0 files to GitHub Code Scanning with exact ref and commit metadata

### Question 39 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). The SPDX 2.3 JSON export records upstream package names (`PURLs`), versions, direct/transitive dependency relationships, and detected SPDX license identifiers—and never lists downstream dependents. [Skill 3.1: Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)]

- **A:** Correct. GitHub exports dependency inventories, versions, licenses, and transitive relationships in standard SPDX JSON (and never includes downstream external dependents)
- **B:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **C:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 40 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). Remediate `urllib3` first because a `0.79` `EPSS` score indicates high near-term wild exploitation likelihood and `Reachability` confirms live runtime code paths invoke the vulnerable method. [Skill 3.2: Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (auto-dismiss) rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Correct. combining EPSS exploit likelihood and static reachability with CVSS and runtime scope focuses engineering effort on genuinely exploitable dependencies
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names

### Question 41 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). Querying `is:closed resolution:auto-dismiss` lists all auto-dismissed alerts, and GitHub automatically **reopens** an auto-dismissed alert (`emitting auto_reopened`) whenever updated `EPSS`, severity, or `runtime` scope violates the rule criteria. [Skill 3.2: Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (auto-dismiss) rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules)]

- **A:** Incorrect. filtering by has:deployment and runtime-risk:internet-exposed isolates alerts affecting live internet-reachable workloads
- **B:** Incorrect. security-extended broadens vulnerability detection beyond default without adding non-security maintainability noise from security-and-quality
- **C:** Correct. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 42 — `A, D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answers: A and D (are correct). Combine `EPSS` + `Reachability` + `runtime` prioritization with Dependabot auto-triage rules (`which apply resolution:auto-dismiss before notifications fire and enforce org-level rules over conflicting repo settings`). [Skill 3.2: Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (auto-dismiss) rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules)]

- **A:** Correct. evaluating auto-triage rules prior to notifications eliminates alert fatigue while keeping alerts auditable and auto-reopenable
- **B:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Correct. high-EPSS reachable runtime vulnerabilities represent immediate real-world exploit risk compared with unreachable dev-only packages
- **E:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 43 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). No—when global `Dependabot security updates` remains enabled, Dependabot still opens PRs for Medium/Low patchable alerts; disable global `Dependabot security updates` first so custom auto-triage `Open a pull request` rules govern selectively. [Skill 3.3: Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **B:** Correct. when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules
- **C:** Incorrect. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts
- **D:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—when global `Dependabot security updates` remains enabled, Dependabot still opens PRs for Medium/Low patchable alerts; disable global `Dependabot security updates` first so custom auto-triage `Open a pull request` rules govern selectively.

### Question 44 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). GitHub provides `Dismiss low impact issues for development-scoped dependencies` and `Dismiss package malware alerts` (`which suppresses all-version malware alerts often triggered by internal package name collisions, provided private registry scoping blocks public typosquats`). [Skill 3.3: Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Correct. auto-triage rules suppress low-risk noise before notifications fire, auto-reopen if metadata/scope changes, and defer to organization rules when repo rules conflict
- **C:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **D:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure

### Question 45 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). Configure `package-ecosystem: "docker"` (`pointing to Dockerfile directories`) and `package-ecosystem: "github-actions"` (`directory: "/"`) inside `.github/dependabot.yml` for scheduled version update PRs. [Skill 3.3: Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **B:** Correct. security updates react to GitHub Advisory Database alerts on default-branch dependencies, whereas dependabot.yml keeps dependencies and github-actions current on a schedule
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 46 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). Enable the Dependency Graph (`and Code Security on private repos`), add an `on: pull_request` workflow running `actions/dependency-review-action@v4`, configure `fail-on-severity` and `deny-licenses`, and mark the check required in a branch ruleset. [Skill 3.4: Secure dependencies during development using pre-merge Dependency Review (dependency-review-action) for vulnerabilities and licenses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action)]

- **A:** Incorrect. dependabot.yml schedules dependency update PRs rather than gating developer PRs on license compliance; pre-merge gating requires dependency-review-action plus required checks
- **B:** Correct. Dependency Review compares PR base-vs-head manifests/lockfiles via the Dependency Graph and blocks vulnerable or non-compliant licenses when required on protected branches
- **C:** Incorrect. private repositories require GitHub Code Security / GHAS for Dependency Review, contents: read suffices, and unenforced checks do not block merges
- **D:** Incorrect. dependency-review-action requires pull_request base/head diffs and an active Dependency Graph, and allow-licenses / deny-licenses are mutually exclusive

### Question 47 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). Run `actions/dependency-review-action@v4` with `fail-on-severity: high`, `fail-on-scopes: runtime`, and `deny-licenses: GPL-3.0, AGPL-3.0` (`omitting allow-licenses so the mutually exclusive inputs do not conflict`). [Skill 3.4: Secure dependencies during development using pre-merge Dependency Review (dependency-review-action) for vulnerabilities and licenses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action)]

- **A:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **B:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **C:** Correct. dependency-review-action@v4 gates pull requests on severity, dependency scope, and SPDX license policy using a single allow OR deny list
- **D:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets

### Question 48 — `D, E` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answers: D and E (are correct). Configure `fail-on-severity` plus a single license list (`allow-licenses` OR `deny-licenses`) on `pull_request` events, and enforce that workflow job as a required status check inside an active branch ruleset (`with GitHub Code Security enabled on private repos`). [Skill 3.4: Secure dependencies during development using pre-merge Dependency Review (dependency-review-action) for vulnerabilities and licenses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Correct. without a required status check rule, a failing Dependency Review workflow warns on the PR without blocking merge
- **E:** Correct. Dependency Review blocks both vulnerable package versions and prohibited copyleft/unknown licenses on pull requests

### Question 49 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). Configure `groups:` (`batching patterns with update-types: [minor, patch]`) and `registries:` (`type: npm-registry` using `token: ${{ secrets.AZURE_ARTIFACTS_TOKEN }}` stored in **Dependabot secrets**). [Skill 3.5: Configure advanced dependency update rules in dependabot.yml (grouping, ignore rules, update strategies, private registries) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference)]

- **A:** Incorrect. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup
- **B:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **C:** Correct. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets
- **D:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories

### Question 50 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). Add an `ignore:` entry for `dependency-name: "hl7-dotnet-core"` with `update-types: ["version-update:semver-major"]` (`leaving security/minor/patch versions unignored`). [Skill 3.5: Configure advanced dependency update rules in dependabot.yml (grouping, ignore rules, update strategies, private registries) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **D:** Correct. grouping related updates cuts CI/PR noise dramatically, while registries + Dependabot secrets authenticate Dependabot to private npm/NuGet/PyPI/Maven feeds

### Question 51 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). By default `open-pull-requests-limit` (`default 5`) throttles scheduled `version updates` separately from `security updates` (`unless explicitly set to 0 to disable security PRs on that target`), ensuring urgent CVE fixes aren't starved by routine bumps. [Skill 3.5: Configure advanced dependency update rules in dependabot.yml (grouping, ignore rules, update strategies, private registries) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Correct. grouping related updates cuts CI/PR noise dramatically, while registries + Dependabot secrets authenticate Dependabot to private npm/NuGet/PyPI/Maven feeds
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 52 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). Store the credential in **`Dependabot secrets`** (`Repository or Organization Settings -> Secrets and variables -> Dependabot`), because workflows triggered by Dependabot do not receive standard `Actions secrets` and get a read-only `GITHUB_TOKEN` by default. [Skill 3.6: Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Correct. understanding Dependabot token/secret isolation, webhook automation, and Defender for Cloud / artifact-registry deployment context integrates supply-chain security safely into operations

### Question 53 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). Filtering with `has:deployment runtime-risk:internet-exposed` narrows the alert backlog to vulnerabilities running in live internet-facing clinical deployments. [Skill 3.6: Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions)]

- **A:** Incorrect. the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON
- **B:** Correct. filtering by has:deployment and runtime-risk:internet-exposed isolates alerts affecting live internet-reachable workloads
- **C:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **D:** Incorrect. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules

### Question 54 — `A, C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answers: A and C (are correct). Workflows triggered by `dependabot` PRs receive a read-only `GITHUB_TOKEN` and access `Dependabot secrets`, while Defender for Cloud / JFrog integrations populate `has:deployment` and `runtime-risk:internet-exposed` qualifiers. [Skill 3.6: Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions)]

- **A:** Correct. production context pinpoints vulnerabilities actually running in internet-facing workloads rather than dead or archived repos
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Correct. isolating Dependabot secrets and read-only default tokens protects repository secrets if a compromised upstream package alters build scripts
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **E:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 55 — `C` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: C (is correct). CodeQL builds a semantic relational database for interprocedural `C#` taint analysis, while third-party IaC/container scanners upload `SARIF 2.1.0` files so code and infrastructure findings share unified PR checks, rulesets, and Security Overview tracking. [Skill 4.1: Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **C:** Correct. CodeQL excels at deep interprocedural taint tracking across supported languages while SARIF 2.1.0 lets specialized IaC/container/linter tools report into one PR interface
- **D:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)

### Question 56 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). No—Code Scanning rejects gzipped SARIF uploads exceeding `10 MB`, and sharing an identical `category` on the same commit causes the second upload to overwrite alerts from the first tool. [Skill 4.1: Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)]

- **A:** Incorrect. allow-licenses and deny-licenses are mutually exclusive inputs in dependency-review-action, and branch rulesets must require the check to block merging
- **B:** Incorrect. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release
- **C:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—Code Scanning rejects gzipped SARIF uploads exceeding `10 MB`, and sharing an identical `category` on the same commit causes the second upload to overwrite alerts from the first tool.
- **D:** Correct. each gzipped SARIF upload must be <=10 MB with a distinct category per language/tool/component and security-events: write permission

### Question 57 — `A, C` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answers: A and C (are correct). Keep each gzip-compressed SARIF upload `<= 10 MB` (`<= 25,000` results, top `5,000` displayed) and set a distinct `category` per package/tool while preserving `ruleId` and `partialFingerprints`. [Skill 4.1: Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)]

- **A:** Correct. exceeding 10 MB gzipped rejects the upload outright, while noisy rule sets over 5,000 findings truncate lower-priority alerts
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Correct. distinct categories prevent multi-job uploads on the same commit from clobbering one another, while fingerprints track alerts across line shifts
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **E:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 58 — `A` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: A (is correct). Install the CodeQL CLI bundle on the CI agent, run `codeql database create` (`tracing the C++ build`), run `codeql database analyze --format=sarif-latest`, and run `codeql github upload-results` (`--sarif`, `--ref`, `--commit`). [Skill 4.2: Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (CodeQL CLI) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages)]

- **A:** Correct. external CI integrations create the semantic CodeQL database, execute query suites into SARIF 2.1.0 (`<=10 MB` gzipped), and upload results with `security_events` write auth
- **B:** Incorrect. CodeQL cannot upload raw source files or XML; a database must be created before analysis, and SARIF 2.1.0 uploads must be <=10 MB gzipped with target ref and commit SHA
- **C:** Incorrect. Default Setup conflicts with custom/external CodeQL uploads, uploading SARIF requires security-events: write, and runs cap at 25,000 results (displaying top 5,000)
- **D:** Incorrect. omitting distinct SARIF categories causes subsequent uploads for the same commit to overwrite/mark prior component results stale, and private repos require Code Security

### Question 59 — `B` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: B (is correct). Keep `Default Setup` on `pathology-viewer-ts` for zero-maintenance automatic scans, and switch `assay-analyzer-dotnet` to `Advanced Setup` (`.github/workflows/codeql.yml` + `codeql-config.yml`, which automatically disables Default Setup). [Skill 4.2: Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (CodeQL CLI) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Correct. Default Setup is fastest for broad rollout, whereas Advanced Setup unlocks manual builds, custom query packs, and granular matrix control (disabling Default Setup automatically on switch)
- **C:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **D:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)

### Question 60 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). Configure `build-mode: manual` and run `ninja -C build/release` before `codeql-action/analyze`, because `C/C++` (`and Swift/Kotlin`) require traced compilation and do not support `build-mode: none`. [Skill 4.2: Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (CodeQL CLI) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages)]

- **A:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets
- **D:** Correct. build-mode: manual traces exact custom C/C++, C#, Go, Java/Kotlin, or Swift compiler invocations when autobuild heuristics fail

### Question 61 — `C` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: C (is correct). No—classic `Copilot Autofix` for CodeQL PR and default-branch alerts is included with `GitHub Code Security` (`and public repos`) without requiring individual GitHub Copilot seats or consuming AI credits. [Skill 4.3: Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Correct. taint-flow paths pinpoint exact user-input sources and unvalidated sinks, while Copilot Autofix proposes context-aware diffs that must still pass CI and human review
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 62 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). Declaring `permissions: { security-events: write, contents: read, actions: read }` allows the job to check out repository code and upload SARIF results to Code Scanning with least privilege. [Skill 4.3: Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning)]

- **A:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets
- **B:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **C:** Incorrect. granting Review and manage secret scanning bypass requests creates least-privilege Push Protection approvers without full Org Owner access
- **D:** Correct. uploading CodeQL or third-party SARIF 2.1.0 findings from GitHub Actions requires least-privilege security-events: write permission

### Question 63 — `B, E` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answers: B and E (are correct). Trace the `source -> step -> sink` dataflow path (`knowing classic CodeQL Autofix needs no Copilot seat`), and validate every Copilot Autofix patch through full unit/integration CI tests, a clean CodeQL re-scan, and human PR review. [Skill 4.3: Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Correct. LLM-generated security fixes lower remediation friction dramatically, yet still require automated test and human semantic verification before merge
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **E:** Correct. taint-flow paths pinpoint exact user-input sources and unvalidated sinks, while Copilot Autofix proposes context-aware diffs that must still pass CI and human review

### Question 64 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). Only Rule A (`Security severity: High`) blocks the PR, because `All alerts: None` ignores non-security quality rules (`Error`/`Warning`/`Note`) while `Security alerts: High or higher` gates on `Critical` and `High` `security-severity`. [Skill 4.4: Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Correct. branch protection rulesets filter security alerts by Critical/High/Medium/Low security-severity independently from non-security error/warning quality notes

### Question 65 — `C` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: C (is correct). Computing `partialFingerprints` (`specifically primaryLocationLineHash`, which `github/codeql-action/upload-sarif` can calculate when source files are checked out) anchors alerts to code content rather than fragile line numbers. [Skill 4.4: Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Correct. compressing SARIF under 10 MB, preserving ruleId + partialFingerprints across runs, and setting unique category strings per tool/language/monorepo slice prevents rejected or overwritten alerts
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 66 — `A` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: A (is correct). `codeql github upload-results --repository=<org/repo> --ref=refs/pull/<num>/merge --commit=<merge_sha> --sarif=dicom-scan.sarif` publishes external CI SARIF findings directly onto the GitHub pull request. [Skill 4.4: Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository)]

- **A:** Correct. codeql github upload-results publishes externally generated SARIF 2.1.0 files to GitHub Code Scanning with exact ref and commit metadata
- **B:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **C:** Incorrect. the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON
- **D:** Incorrect. the code-security configurations attach endpoint programmatically binds a Security Configuration to targeted or organization-wide repositories

### Question 67 — `B` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: B (is correct). Define a YAML data-extension `CodeQL model pack` (`marking Scrub() as a taint sanitizer/neutral summary`) and reference it via `packs:` inside `.github/codeql/codeql-config.yml`. [Skill 4.5: Optimize and troubleshoot Code Security operations with custom configurations, model packs, and build/performance diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning)]

- **A:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets
- **B:** Correct. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup
- **C:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **D:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories

### Question 68 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). Use a per-language `matrix` so each language runs in its own isolated job, move heavy compiled jobs onto Larger runners (`16–32 GB RAM`), and exclude generated swagger/client code via `paths-ignore` in `codeql-config.yml`. [Skill 4.5: Optimize and troubleshoot Code Security operations with custom configurations, model packs, and build/performance diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **D:** Correct. model packs teach CodeQL custom internal framework sources/sanitizers/sinks without forking queries, while Adequate RAM/CPU runners and scoped paths resolve timeout/OOM failures

### Question 69 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Triage the report in a draft `GHSA`, open a temporary private fork from the advisory to develop and verify the fix, request a `CVE` and record patched release versions, then merge the patch and publish the advisory. [Skill 5.1: Understand CVE, CWE, and GitHub Security Advisory (GHSA) concepts and execute end-to-end advisory remediation workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)]

- **A:** Incorrect. publishing zero-day exploit steps in public issues or public branches before a fix exists exposes all downstream users to active exploitation
- **B:** Correct. repository security advisories keep vulnerability details confidential in a temporary private fork until a verified patch is ready to release alongside coordinated GHSA/CVE disclosure
- **C:** Incorrect. secret_scanning.yml only filters secret-scanning paths and has nothing to do with patching or disclosing CWE/CVE code vulnerabilities
- **D:** Incorrect. temporary private advisory forks intentionally disable GitHub Actions to prevent side-channel leaks, and publishing the GHSA is what powers downstream Dependabot alerts

### Question 70 — `C` (Security operations: best practices, prioritization, and remediation)

Correct answer: C (is correct). `CWE-611` classifies the root weakness type, `CVE-2026-50911` uniquely identifies that specific disclosed `fhir-r4-lint` vulnerability worldwide, and the `GHSA` provides coordinated private collaboration and GitHub Advisory Database metadata for Dependabot. [Skill 5.1: Understand CVE, CWE, and GitHub Security Advisory (GHSA) concepts and execute end-to-end advisory remediation workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **C:** Correct. maintainers triage private reports inside draft GHSAs, patch silently in temporary private forks (where Actions stay disabled), request a CVE, and publish coordinated advisories
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 71 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). No—GitHub intentionally disables GitHub Actions execution inside temporary private advisory forks; maintainers must run test suites locally or in a separate private CI environment until ready for coordinated release. [Skill 5.1: Understand CVE, CWE, and GitHub Security Advisory (GHSA) concepts and execute end-to-end advisory remediation workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)]

- **A:** Correct. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release
- **B:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—GitHub intentionally disables GitHub Actions execution inside temporary private advisory forks; maintainers must run test suites locally or in a separate private CI environment until ready for coordinated release.
- **C:** Incorrect. allow-licenses and deny-licenses are mutually exclusive inputs in dependency-review-action, and branch rulesets must require the check to block merging
- **D:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories

### Question 72 — `D` (Security operations: best practices, prioritization, and remediation)

Correct answer: D (is correct). Enforce an active organization ruleset (`Require code scanning results` set to `High or higher`) to stop new PR regressions, and triage existing default-branch alerts by `has:deployment`, `runtime-risk:internet-exposed`, `EPSS`, and `Reachability`. [Skill 5.2: Define, prioritize, and enforce severity rulesets and production-context prioritization at scale | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **D:** Correct. combining runtime deployment exposure with pre-merge High/Critical blocking stops alert growth while burning down real internet-exposed production risk first

### Question 73 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). The pull request is **blocked from merging**, because `Require code scanning results` waits for `CodeQL` to report clean check results on the PR ref—preventing contributors from bypassing SAST simply by deleting the workflow file. [Skill 5.2: Define, prioritize, and enforce severity rulesets and production-context prioritization at scale | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Correct. combining Rulesets with REST/GraphQL security configuration and org-level alert APIs automates compliance reporting and zero-drift enforcement across thousands of repositories
- **C:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 74 — `A, E` (Security operations: best practices, prioritization, and remediation)

Correct answers: A and E (are correct). Ingest deployment telemetry (`Defender for Cloud / JFrog / deployment APIs`) for `has:deployment` + `runtime-risk:internet-exposed` filtering, and pilot new rulesets in `Evaluate` mode before enforcing `Active` mode. [Skill 5.2: Define, prioritize, and enforce severity rulesets and production-context prioritization at scale | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)]

- **A:** Correct. Evaluate mode surfaces missing scans or noisy rules safely without halting production releases on day one
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **E:** Correct. production context pinpoints vulnerabilities actually running in internet-facing workloads rather than dead or archived repos

### Question 75 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Filter priority default-branch alerts in Security Overview, create a Security Campaign (`<=1,000` alerts) with due date and security contact, trigger Copilot Autofix (`or assign <=25 alerts per batch to @copilot`), and verify CI checks while tracking burndown. [Skill 5.3: Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/manage-security-alerts/best-practices-for-participating-in-a-security-campaign)]

- **A:** Incorrect. code security campaigns target default-branch alerts (up to 1,000 per campaign) with a named contact, and developers need write access plus passing CI checks to merge fixes
- **B:** Correct. Security Campaigns group high-risk default-branch alerts around a dedicated security contact and accelerate developer burndown with Copilot Autofix or @copilot draft PRs
- **C:** Incorrect. disabling scanners or bulk-dismissing unreviewed findings hides real production vulnerabilities rather than remediating security debt
- **D:** Incorrect. agentic @copilot campaign assignments cap at 25 alerts per batch (opening a PR for human/CI verification), and Copilot cannot rotate external cloud provider IAM credentials

### Question 76 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). Each Security Campaign holds up to `1,000` default-branch alerts, and managers can assign up to `25` alerts per batch to `@copilot` (`consuming Code Security AI credits`) to open draft remediation pull requests. [Skill 5.3: Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/manage-security-alerts/best-practices-for-participating-in-a-security-campaign)]

- **A:** Correct. grouping related CWEs into focused campaigns builds developer remediation momentum while Copilot Autofix and @copilot PR batches cut manual toil
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 77 — `D` (Security operations: best practices, prioritization, and remediation)

Correct answer: D (is correct). Review the dismissal comment and compensating-control evidence in the campaign's `Closed` tab / Security Overview audit view, reopening any alert lacking verified architectural mitigation. [Skill 5.3: Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/manage-security-alerts/best-practices-for-participating-in-a-security-campaign)]

- **A:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Correct. alert dismissals remain visible in REST/GraphQL APIs, webhooks, and audit logs, so teams must document rationale rather than hiding unverified risk

### Question 78 — `C` (Security operations: best practices, prioritization, and remediation)

Correct answer: C (is correct). Setting `queries: security-extended` runs `default` plus medium-precision security queries while excluding the maintainability and style queries bundled in `security-and-quality`. [Skill 5.4: Customize CodeQL query suites, multi-repository variant analysis, and risk-profile-tailored security detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites)]

- **A:** Incorrect. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Correct. security-extended broadens vulnerability detection beyond default without adding non-security maintainability noise from security-and-quality
- **D:** Incorrect. filtering by has:deployment and runtime-risk:internet-exposed isolates alerts affecting live internet-reachable workloads

### Question 79 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). `Multi-Repository Variant Analysis (MRVA)` in the CodeQL VS Code extension runs custom `.ql` queries across up to 1,000 organization repositories via a controller Actions workflow. [Skill 5.4: Customize CodeQL query suites, multi-repository variant analysis, and risk-profile-tailored security detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites)]

- **A:** Correct. security-extended expands vulnerability coverage beyond high-precision default rules, while MRVA hunts novel zero-day patterns across up to 1,000 org repositories simultaneously
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 80 — `D` (Security operations: best practices, prioritization, and remediation)

Correct answer: D (is correct). Setting `threat-models: [remote, local]` in `codeql-config.yml` activates local file, CLI argument, and environment-variable taint sources alongside remote HTTP sources. [Skill 5.4: Customize CodeQL query suites, multi-repository variant analysis, and risk-profile-tailored security detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Correct. model packs teach CodeQL custom internal framework sources/sanitizers/sinks without forking queries, while Adequate RAM/CPU runners and scoped paths resolve timeout/OOM failures

### Question 81 — `D` (Security operations: best practices, prioritization, and remediation)

Correct answer: D (is correct). Grant a custom repository role (`inheriting Write`) with fine-grained permissions to view and manage Code Scanning and Dependabot alerts while keeping organization-wide rulesets with `Security Managers` and Org Owners. [Skill 5.5: Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Correct. clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity

### Question 82 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). Both replace silent contributor overrides with explicit, identity-scoped exception workflows (`visible reviewer approval for Push Protection; designated break-glass role/PR-approver bypass for Rulesets`) captured permanently in audit logs. [Skill 5.5: Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)]

- **A:** Correct. delegated bypass replaces ad-hoc writer self-bypasses with a structured request-and-approval workflow audited via webhooks and logs
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 83 — `B, E` (Security operations: best practices, prioritization, and remediation)

Correct answers: B and E (are correct). Combine `Security Manager`, custom repository alert roles, and explicit alert `Assignees` (`noting single-alert elevation on assigned secret alerts`), and test cross-repository rulesets in `Evaluate` mode before `Active` enforcement. [Skill 5.5: Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Correct. Evaluate mode surfaces missing scans or noisy rules safely without halting production releases on day one
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **E:** Correct. clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity

### Question 84 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Enable Push Protection (`pre-receive`), `actions/dependency-review-action@v4` (`PR dependency/license gate`), and PR `CodeQL` analysis with `Copilot Autofix` enforced via branch rulesets. [Skill 5.6: Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Correct. combining all three shift-left controls prevents new security debt from ever landing on the default branch
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure

### Question 85 — `D` (Security operations: best practices, prioritization, and remediation)

Correct answer: D (is correct). Standard `Dependabot alerts` scan the **default branch** *after* merge; blocking newly introduced vulnerable or unlicensed packages *on a pull request* before merge requires `Dependency Review` (`actions/dependency-review-action@v4`) as a required check. [Skill 5.6: Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **C:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **D:** Correct. Dependency Review inspects PR manifest/lockfile diffs before merge and fails the check when newly introduced packages breach vulnerability or license policies

### Question 86 — `A, D, E` (Security operations: best practices, prioritization, and remediation)

Correct answers: A, D, and E (are correct). Intercept secrets pre-receive with Push Protection, enforce `dependency-review-action@v4` severity and SPDX license checks on pull requests, and validate CodeQL `Copilot Autofix` patches with automated CI tests and human review. [Skill 5.6: Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Correct. LLM-generated security fixes lower remediation friction dramatically, yet still require automated test and human semantic verification before merge
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **D:** Correct. Dependency Review blocks both vulnerable package versions and prohibited copyleft/unknown licenses on pull requests
- **E:** Correct. stopping secrets pre-receive prevents Git history contamination and emergency credential rotation
- **F:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure

### Question 87 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). Verify committer license headroom (`or metered budget`), create/select Security Configurations, attach them to tiered repos via custom properties with `Apply to new repositories` enabled, and set `Enforced` to prevent drift. [Skill 6.1: Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories)]

- **A:** Incorrect. manual per-repo changes do not scale or prevent configuration drift, and granting Organization Owner violates least privilege when Security Manager / Security Configurations exist
- **B:** Incorrect. exceeding volume committer licenses blocks enablement on additional/new private repos, and features left as Not set remain editable by repository admins even under Enforced configurations
- **C:** Incorrect. standalone GHES uses volume/subscription licensing (not metered billing) and requires GitHub Connect for Advisory DB sync, while transferred repos must be explicitly targeted by configurations
- **D:** Correct. rolling out Security Configurations verifies committer license capacity first, targets repo tiers via custom properties, covers newly created repos, and locks drift with Enforced mode

### Question 88 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). Cloud-hosted metered billing and cloud AI capabilities (`Copilot Autofix`, AI generic secret push detection) run on `GHEC`, while `GHES` uses volume/subscription licensing and relies on `GitHub Connect` for automatic Advisory Database sync and hybrid committer deduplication. [Skill 6.1: Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Correct. Security Configurations eliminate manual repo drift on GHEC and GHES, while hybrid enterprises link GHES to GHEC via GitHub Connect for Advisory DB updates and committer seat deduplication
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 89 — `A` (GitHub Security suites administration)

Correct answer: A (is correct). `Enforced` locks explicitly configured `Enabled`/`Disabled` features so repository admins cannot alter them, whereas `Unenforced` applies those settings once as a starting baseline while letting repository admins adjust toggles afterward. [Skill 6.1: Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories)]

- **A:** Correct. understanding Enforced vs Unenforced inheritance, transferred-repo gaps, 90-day active committer deduplication, and hard budgets on metered SKUs/AI credits prevents surprise overages or lockouts
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers

### Question 90 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). No—any row left at `"Not set"` inside an `Enforced` Security Configuration remains editable by repository administrators; it must be explicitly set to `Enabled` to lock it on. [Skill 6.2: Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security)]

- **A:** Incorrect. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts
- **B:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—any row left at `"Not set"` inside an `Enforced` Security Configuration remains editable by repository administrators; it must be explicitly set to `Enabled` to lock it on.
- **C:** Incorrect. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release
- **D:** Correct. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories

### Question 91 — `A` (GitHub Security suites administration)

Correct answer: A (is correct). Nora consumes `1` seat in the `GitHub Secret Protection` pool and `1` seat in the `GitHub Code Security` pool (`each SKU deduplicates unique 90-day active committers across private/internal repos, while public repo commits consume 0 seats`). [Skill 6.2: Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security)]

- **A:** Correct. understanding Enforced vs Unenforced inheritance, transferred-repo gaps, 90-day active committer deduplication, and hard budgets on metered SKUs/AI credits prevents surprise overages or lockouts
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)

### Question 92 — `A, E` (GitHub Security suites administration)

Correct answers: A and E (are correct). Active-committer seats count unique 90-day committers deduplicated across the enterprise, and metered `Code Security AI credits` + `Secret Protection AI credits` can be capped with **hard spending budgets** (`halting metered AI overages once reached`). [Skill 6.2: Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security)]

- **A:** Correct. a developer pushing to 50 GHAS-enabled repos in an enterprise consumes only one active-committer license seat over the rolling 90-day window
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **D:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **E:** Correct. classic CodeQL Copilot Autofix does not consume AI credits, whereas agentic autofix / AI Scan and AI push secret scanning draw from included or metered AI credit pools

### Question 93 — `A` (GitHub Security suites administration)

Correct answer: A (is correct). No—disabling repository-administrator toggle permissions restricts only repo-level admins while preserving full Security Configuration attachment rights for `Enterprise Owners`, `Organization Owners`, and `Security Managers` (`and leaving existing enabled repos active`). [Skill 6.3: Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise)]

- **A:** Correct. enterprise policies prevent uncontrolled repo-admin license consumption while audit log streaming preserves tamper-evident compliance records across configuration and bypass events
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **D:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges

### Question 94 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). Configure **Enterprise Audit Log streaming** (`to Azure Event Hubs / Blob Storage, Amazon S3, Datadog, or Splunk`) including Git/API security events so `security_configuration.*`, bypass, and dismissal records persist immutably. [Skill 6.3: Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Correct. enterprise policies prevent uncontrolled repo-admin license consumption while audit log streaming preserves tamper-evident compliance records across configuration and bypass events
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 95 — `B` (GitHub Security suites administration)

Correct answer: B (is correct). Deploy the ruleset in **`Evaluate` mode** for 14 days, inspect would-be violations in **Ruleset Insights**, remediate missing workflow setups, and then switch enforcement to **`Active`**. [Skill 6.3: Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Correct. Evaluate mode surfaces missing scans or noisy rules safely without halting production releases on day one
- **C:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 96 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). Assigning the **`Security Manager`** organization role grants full alert read/write, Security Overview, campaign, and Security Configuration governance without code-write or billing-owner permissions. [Skill 6.4: Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Correct. Security Manager and fine-grained custom repository roles grant AppSec and security champions exact triage permissions without over-provisioning Repository Admin or code-push rights
- **D:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges

### Question 97 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). Create a custom repository role inheriting `Read` and add only the fine-grained `View Dependabot alerts` permission (`leaving Code Scanning, Secret Protection, and dismiss permissions unchecked`). [Skill 6.4: Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Correct. Security Manager and fine-grained custom repository roles grant AppSec and security champions exact triage permissions without over-provisioning Repository Admin or code-push rights

### Question 98 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). On private repositories, default permissions allow `Write` collaborators to view Code Scanning (`and Dependabot`) alerts to fix code/packages, whereas Secret Protection alerts contain raw live credentials and default strictly to Repo `Admin`, `Security Manager`, Org Owners, or custom roles. [Skill 6.4: Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization)]

- **A:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Correct. clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity

### Question 99 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`with scope: "selected" and selected_repository_ids`) programmatically attaches the Security Configuration. [Skill 6.5: Enforce default or approved custom CodeQL workflows and automate large-scale security governance via REST and GraphQL APIs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/rest/code-security/configurations)]

- **A:** Incorrect. codeql github upload-results publishes externally generated SARIF 2.1.0 files to GitHub Code Scanning with exact ref and commit metadata
- **B:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **C:** Correct. the code-security configurations attach endpoint programmatically binds a Security Configuration to targeted or organization-wide repositories
- **D:** Incorrect. the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON

### Question 100 — `A, E` (GitHub Security suites administration)

Correct answers: A and E (are correct). Enforce centrally managed Required Workflows + `Require code scanning results` rulesets (`using distinct SARIF category tags and partialFingerprints per language`), and query org/enterprise-level REST/GraphQL alert endpoints (`GET /orgs/{org}/code-scanning/alerts`) instead of polling repositories individually. [Skill 6.5: Enforce default or approved custom CodeQL workflows and automate large-scale security governance via REST and GraphQL APIs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/rest/code-security/configurations)]

- **A:** Correct. distinct categories prevent multi-job uploads on the same commit from clobbering one another, while fingerprints track alerts across line shifts
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **E:** Correct. combining Rulesets with REST/GraphQL security configuration and org-level alert APIs automates compliance reporting and zero-drift enforcement across thousands of repositories
